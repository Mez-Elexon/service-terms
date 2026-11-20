"""Build one JSON file of P-flows from:
  1. the AMSID IDD v0.1 workbook ('SVAA P375' sheet: full record structure for 16 flows;
     'Items' and 'Valid Sets' sheets), and
  2. the SVA Data Catalogue Volume 1 v66.0, Appendix A (Data Interface Index: routes) and
     Appendix B (Data Interface Definition: data items, notes, version history).
Usage: build_pflows.py <idd.xlsm> <appendix.txt> <out.json>
"""
import json, os, re, sys, collections
import openpyxl

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # catalogue.py sits next to this script
from openpyxl.reader import workbook as _wb
import catalogue as cat

_wb.WorkbookParser.assign_names = lambda self: None  # the workbook's '#N/A' print-titles name is unreadable; not data

idd_path, app_path, out_path = sys.argv[1:4]

SCOPE = [f'P{n:04d}' for n in list(range(278, 321)) + list(range(323, 343))]
FAMILIES = [  # grouping used in this file (by flow number), with the change named in the catalogue
    (range(278, 291), 'MSID Pair allocation and delivered volumes (P344)'),
    (range(291, 292), 'Daily activations (CP1517)'),
    (range(292, 297), 'Applicable Balancing Services Volume Data (P354)'),
    (range(297, 321), 'Asset metering: AMSID Pairs (P375)'),
    (range(323, 338), 'Baselining (P376)'),
    (range(338, 343), 'Non-final and non-chargeable demand (P395, P415, CP1620)'),
]
# Route comments curated from the Appendix B 'Comment' column (the PDF text interleaves that column with
# the 'Known as' column, so these were read by hand rather than parsed).
ROUTE_COMMENTS = {
    'P0283': [('BSCP602', 'SVAA', 'AMVLP', 'Will include only data items included in the received P0282 plus Delivered Volume Rejection Reason')],
    'P0285': [('BSCP602', 'SVAA', 'AMVLP', 'Will include only data items included in the received P0282 for the relevant MSIDs and / or AMSIDs')],
    'P0287': [('BSCP508', 'SVAA', 'Supplier', 'One file per Settlement Day per Settlement Run')],
    'P0289': [('BSCP508', 'SVAA', 'SAA', 'One file per Settlement Day per Settlement Run')],
    'P0290': [('BSCP508', 'SVAA', 'SAA', 'One file per Settlement Day per Settlement Run')],
    'P0297': [('BSCP602', 'AMVLP', 'SVAA', 'Content of P0297 depends on the purpose as defined by the Action Indicator data item.')],
    'P0298': [('BSCP602', 'SVAA', 'AMVLP', 'Response to P0297. Only contains data items submitted in P0297 plus Rejection Reason.')],
    'P0299': [('BSCP602', 'SVAA', 'AMVLP', 'Response to P0297. Only contains data items submitted in P0297.')],
    'P0300': [('BSCP602', 'AMVLP', 'SVAA', 'Content of P0300 depends on the purpose as defined by the Action Indicator data item.')],
    'P0301': [('BSCP602', 'SVAA', 'AMVLP', 'Response to P0300. Only contains data items submitted in P0300 plus Rejection Reason.')],
    'P0302': [('BSCP602', 'SVAA', 'AMVLP', 'Response to P0300. Only contains data items submitted in P0300')],
    'P0304': [('BSCP603', 'Supplier', 'HHDC', 'Response to P0303.')],
    'P0305': [('BSCP602', 'SVAA', 'AMVLP', 'Response to P0303.')],
    'P0307': [('BSCP602', 'SVAA', 'AMVLP', 'Response to P0306. Only contains data items submitted in P0306 plus Rejection Reason.')],
    'P0308': [('BSCP602', 'SVAA', 'AMVLP', 'Response to P0306. Only contains data items submitted in P0306.')],
    'P0312': [('BSCP602', 'AMVLP', 'AMVLP', 'Sent by the AMVLP that had the AMSID Pair allocated to its Secondary BM Unit in P0309.')],
    'P0320': [('BSCP602', 'SVAA', 'AMVLP', 'Sent to the AMVLP that had the AMSID Pair allocated to its Secondary BM Unit prior to an AMSID Pair Reallocation.')],
}
for ref, resp_to in (('P0324', 'P0323'), ('P0325', 'P0323'), ('P0327', 'P0326'), ('P0334', 'P0326'),
                     ('P0329', 'P0328'), ('P0330', 'P0328')):
    ROUTE_COMMENTS[ref] = [(None, None, None, f'Response to {resp_to} (stated on every route)')]
ROUTE_COMMENTS['P0336'] = [(None, None, None, 'Rejection of P0335 (stated on every route)')]
ROUTE_COMMENTS['P0337'] = [(None, None, None, 'Confirmation of P0335 (stated on every route)')]

# Points noticed while reading the catalogue; kept factual and flagged for review.
CATALOGUE_OBSERVATIONS = {
    'P0299': ["Appendix B 'Known as' for the Supplier to AMVLP route reads 'Rejection of Asset Registration' on this Confirmation flow."],
    'P0305': ["Appendix B lists Rejection Reason as a data item of this Confirmation flow."],
    'P0307': ["Appendix B route comment says this Confirmation 'only contains data items submitted in P0306 plus Rejection Reason', while the Rejection flow P0308 says the opposite; the two comments look swapped."],
    'P0308': ["Appendix B route comment says this Rejection 'only contains data items submitted in P0306' without Rejection Reason, although Rejection Reason is listed as a data item; see P0307."],
    'P0330': ["Appendix A lists a route SVAA to SVAA; the matching P0329 route is SVAA to Supplier."],
    'P0335': ["Appendix A lists the VTP route as SVAA to VTP, while every other route of this flow is participant to SVAA."],
    'P0320': ["Appendix B spells the data item 'AMSID Pair Differencint Indicator'."],
    'P0300': ["Appendix B lists 'AMHHDC Effective from Date' twice; the IDD has an AMHHDC Effective From Date and an AMHHDC Effective To Date."],
}

clean = lambda v: (re.sub(r'[ \t]+', ' ', v.replace('\r', '')).strip() or None) if isinstance(v, str) else v


def parse_type(t):
    if t is None:
        return None
    m = re.fullmatch(r'(\w+)\((\d+)(?:,(\d+))?\)', t.replace(' ', ''))
    if m:
        d = {'type': m.group(1), 'length': int(m.group(2))}
        if m.group(3):
            d['decimalPlaces'] = int(m.group(3))
        return d
    return {'type': t}


def parse_card(c):
    c = str(c).strip(); lo, _, hi = c.partition('-')
    return {'min': int(lo), 'max': None if hi == '*' else int(hi or lo), 'raw': c}


# ---------------- IDD workbook ----------------
wb = openpyxl.load_workbook(idd_path, data_only=True)
items_by_name = {}
for r in wb['Items'].iter_rows(min_row=2, values_only=True):
    if r[2]:
        items_by_name[clean(r[2]).lower()] = {'id': r[1], 'name': clean(r[2]), 'type': clean(r[6]), 'validSet': clean(r[7])}
valid_sets = collections.OrderedDict()
for r in wb['Valid Sets'].iter_rows(min_row=2, values_only=True):
    if r[0] is None:
        continue
    e = {'value': r[2]}
    if r[3] is not None:
        e['high'] = r[3]
    if r[4] is not None:
        e['description'] = clean(r[4])
    valid_sets.setdefault(clean(r[0]), []).append(e)
vs_lower = {k.lower(): k for k in valid_sets}
INFERRED_VS = {'measurement class': ('Measurement Class Id', 'inferred (SF Field "Measurement Class Id")')}
used_sets = set()
notes = []


def link(name, item):
    """Attach IDD Items-sheet entry and valid set, by item name."""
    catg = items_by_name.get(name.lower())
    vset = how = None
    if catg and catg['validSet']:
        vset, how = catg['validSet'], 'IDD Items sheet'
    elif name.lower() in vs_lower:
        vset, how = vs_lower[name.lower()], 'valid set with the same name'
    elif name.lower() in INFERRED_VS:
        vset, how = INFERRED_VS[name.lower()]
    if vset and 'validSet' not in item:
        item['validSet'] = vset; item['validSetLinkedBy'] = how; used_sets.add(vset)
    if catg:
        item['itemCatalogue'] = {'id': catg['id'], 'type': catg['type']}
    return catg


def impl(v):
    d = {k: clean(v.get(c)) for k, c in (('sfObject', 'Q'), ('sfField', 'R'), ('sfDataType', 'S'),
                                          ('conditions', 'T'), ('apiDevComment', 'U'))}
    return {k: x for k, x in d.items() if x is not None} or None


idd_flows = collections.OrderedDict(); flow = None; stack = []
for row in wb['SVAA P375'].iter_rows(min_row=2):
    v = {c.column_letter: c.value for c in row if clean(c.value) is not None}
    kind = clean(v.get('B'))
    if kind is None:
        continue
    levels = [(i + 1, clean(v[c])) for i, c in enumerate('DEFGHIJKL') if c in v]
    for c in 'VW':
        if c in v:
            notes.append(f"IDD row {row[0].row}: ignored value {v[c]!r} in unlabelled column {c}")
    if kind == 'F':
        flow = {'flowId': clean(v['A']), 'version': str(clean(v['C'])), 'name': clean(v['O']), 'groups': []}
        if impl(v):
            flow['iddNotes'] = impl(v).get('apiDevComment')
        idd_flows[flow['flowId']] = flow; stack = []
    elif kind == 'R':
        assert len(levels) == 1 and levels[0][1] == 'G'
        lvl = levels[0][0]
        g = {'groupId': clean(v['A']), 'name': clean(v['O']), 'level': lvl, 'cardinality': parse_card(v['C'])}
        if clean(v.get('P')):
            g['comments'] = clean(v['P'])
        if impl(v):
            g['implementation'] = impl(v)
        g['items'] = []; g['groups'] = []
        while stack and stack[-1]['level'] >= lvl:
            stack.pop()
        (flow['groups'] if lvl == 1 else stack[-1]['groups']).append(g)
        stack.append(g)
    elif kind == 'D':
        lvl, opt = levels[0]
        while stack and stack[-1]['level'] >= lvl:
            stack.pop()
        assert stack and stack[-1]['level'] == lvl - 1
        name = clean(v['O'])
        it = {'name': name, 'mandatory': str(opt) == '1', 'dataType': parse_type(clean(v.get('M'))),
              'dataTypeRaw': clean(v.get('M')), 'dataTypeSource': 'IDD flow sheet'}
        catg = link(name, it)
        if catg and catg['type'] and catg['type'].replace(' ', '') != (it['dataTypeRaw'] or '').replace(' ', ''):
            it['itemCatalogue']['typeDiffers'] = True
        if clean(v.get('P')):
            it['comments'] = clean(v['P'])
        if impl(v):
            it['implementation'] = impl(v)
        stack[-1]['items'].append(it)

# ---------------- SVA Data Catalogue ----------------
A, B = cat.split_appendices(open(app_path, encoding='utf-8').read())
cb = cat.parse_appendix_b(B)
ca = cat.parse_appendix_a(A, {k: v['name'] for k, v in cb.items()})
header = next(l for l in A if l.startswith('Date/Issue No:'))
known = set(items_by_name) | {i['name'].lower() for f in idd_flows.values() for g in f['groups'] for i in g['items']}
for f in idd_flows.values():
    for g in f['groups']:
        for sg in g['groups']:
            known |= {i['name'].lower() for i in sg['items']}
            for ssg in sg['groups']:
                known |= {i['name'].lower() for i in ssg['items']}
for k in cb:
    for l in cb[k]['sections'].get('items', []):
        if not any(s in l[1:] for s in cat.COMMENT_STARTS):
            known.add(l.strip().lower())
    for l in cb[k]['sections'].get('pfs', []):
        known.add(re.sub(r' Yes$', '', l).strip().lower())
known |= {'delivered volume rejection reason', 'mpan core'}


def all_idd_items(groups):
    for g in groups:
        yield from g['items']
        yield from all_idd_items(g['groups'])


def family(ref):
    n = int(ref[1:])
    return next(lbl for rng, lbl in FAMILIES if n in rng)


flows_out = []; uncertain_all = []
for ref in SCOPE:
    b = cb[ref]; a = ca.get(ref, {'routes': [], 'unparsed': []})
    groups_c, uncertain = cat.parse_items(b['sections'].get('items', []), known)
    uncertain_all += [f'{ref}: {u}' for u in uncertain]
    history = cat.parse_history(b['sections'].get('history', []))
    created = next((h['change'] for h in history if re.search(r'[Cc]reated|[Nn]ew flow', h['description'])
                    and h is history[0]), None)
    catalogue = {'name': b['name'], 'version': b['version']}
    if groups_c and groups_c[0]['name']:
        catalogue['dataGroup'] = groups_c[0]['name']
    cat_notes = (b['sections'].get('notes') or []) + [l for l in b['sections'].get('pre', []) if l != 'Notes:']
    if cat_notes:
        catalogue['notes'] = cat_notes
    if ref in ROUTE_COMMENTS:
        catalogue['routeComments'] = [{k: x for k, x in zip(('source', 'from', 'to', 'comment'), rc) if x}
                                      for rc in ROUTE_COMMENTS[ref]]
    if b['sections'].get('pfs'):
        catalogue['physicalFileSpecificationText'] = b['sections']['pfs']
    catalogue['versionHistory'] = history

    out = {'flowId': ref, 'name': b['name'], 'version': b['version'], 'family': family(ref),
           'introducedBy': created,
           'structureSource': 'AMSID IDD v0.1' if ref in idd_flows else 'SVA Data Catalogue Appendix B',
           'routes': a['routes']}
    cat_items = [it for g in groups_c for it in g['items']]
    if ref in idd_flows:
        f = idd_flows[ref]
        if f.get('iddNotes'):
            out['iddNotes'] = f['iddNotes']
        out['groups'] = f['groups']
        catalogue['items'] = cat_items
        # reconciliation IDD vs catalogue
        idd_names = [i['name'] for i in all_idd_items(f['groups'])]
        il = {n.lower() for n in idd_names}; cl = {i['name'].lower() for i in cat_items}
        rec = {}
        if f['name'] != b['name']:
            rec['nameInIDD'] = f['name']
        if f['version'] != b['version']:
            rec['versionInIDD'] = f['version']
        only_idd = sorted({n for n in idd_names if n.lower() not in cl})
        only_cat = sorted({i['name'] for i in cat_items if i['name'].lower() not in il})
        if only_idd:
            rec['itemsOnlyInIDD'] = only_idd
        if only_cat:
            rec['itemsOnlyInCatalogue'] = only_cat
        out['reconciliation'] = rec
    else:
        groups = []
        for g in groups_c:
            items = []
            for ci in g['items']:
                it = {'name': ci['name'], 'mandatory': None, 'dataType': None, 'dataTypeRaw': None}
                catg = link(ci['name'], it)
                if catg and catg['type']:
                    it['dataType'] = parse_type(catg['type']); it['dataTypeRaw'] = catg['type']
                    it['dataTypeSource'] = 'IDD Items sheet (by item name)'
                if ci.get('comments'):
                    it['comments'] = ci['comments']
                items.append(it)
            groups.append({'groupId': None, 'name': g['name'], 'level': 1, 'cardinality': None,
                           'items': items, 'groups': []})
        out['groups'] = groups
    out['catalogue'] = catalogue
    text = json.dumps(catalogue) + json.dumps(out['groups'])
    refs = sorted(set(re.findall(r'\bP\d{4}\b', text)) - {ref})
    if refs:
        out['referencedFlows'] = refs
    if ref in CATALOGUE_OBSERVATIONS:
        out['observationsForReview'] = CATALOGUE_OBSERVATIONS[ref]
    if a['unparsed']:
        notes.append(f'{ref}: Appendix A rows not parsed: {a["unparsed"]}')
    flows_out.append(out)

counts = collections.Counter(f['structureSource'] for f in flows_out)
doc = {
    'source': {
        'documents': [
            'AMSID IDD v0.1 (Copy_of_AMSID_IDD_v_0_1.xlsm), sheets SVAA P375, Items and Valid Sets',
            f'SVA Data Catalogue Volume 1: Data Interfaces, Appendix A (Data Interface Index) and Appendix B (Data Interface Definition), {header.replace("Date/Issue No: ", "")}',
        ],
        'scope': 'P0278-P0320 and P0323-P0342: the 16 P375 flows in the IDD plus the related MSID Pair (P344), daily activations (CP1517), ABSVD (P354), other P375, baselining (P376) and non-final/non-chargeable demand flows.',
        'note': 'Generated from the source documents. Wording is as in the sources; whitespace was trimmed.',
    },
    'conventions': {
        'structureSource': "'AMSID IDD v0.1' = groups/items/types from the IDD flow sheet; 'SVA Data Catalogue Appendix B' = data items from the catalogue, where record structure, optionality and types are not given",
        'routes': 'From Appendix A: source document (BSCP, or the technical specification / known-as name where Appendix A gives one), From role, To role, version',
        'mandatory': "true/false from the IDD ('1' / 'O'); null where the source does not say",
        'cardinality': 'IDD record-group occurrences (min/max, max null = unbounded); null for catalogue-only flows',
        'dataType': "IDD flow-sheet type; for catalogue-only flows, the IDD Items-sheet type of an item with the same name where one exists (dataTypeSource says which)",
        'validSet': 'name of an entry in validSets; validSetLinkedBy says how it was linked',
        'family': 'grouping used in this file, by flow number; introducedBy is the change named in the first version-history entry, where the catalogue gives one',
        'catalogue': 'what Appendix B says about the flow: name, version, data group, notes, route comments, version history; for IDD flows also its data-item list, compared in reconciliation',
        'reconciliation': 'IDD against catalogue: differing name/version, and item names found in only one of the two (case-insensitive)',
        'observationsForReview': 'possible inconsistencies noticed in the catalogue; not corrected',
    },
    'summary': {'flows': len(flows_out), 'withIddStructure': counts['AMSID IDD v0.1'],
                'fromCatalogueOnly': counts['SVA Data Catalogue Appendix B'],
                'routes': sum(len(f['routes']) for f in flows_out),
                'families': dict(collections.Counter(f['family'] for f in flows_out))},
    'flows': flows_out,
    'validSets': {k: valid_sets[k] for k in sorted(used_sets) if k in valid_sets},
}
if uncertain_all:
    notes.append('Data-item lines where the item/comment split is uncertain: ' + '; '.join(uncertain_all))
if notes:
    doc['conversionNotes'] = notes
with open(out_path, 'w', encoding='utf-8') as fh:
    json.dump(doc, fh, ensure_ascii=False, indent=2); fh.write('\n')
print(json.dumps(doc['summary'], indent=1)); print('notes:', len(notes)); [print(' -', n[:300]) for n in notes]
