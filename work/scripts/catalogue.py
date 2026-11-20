"""Parse SVA Data Catalogue Volume 1 Appendix A (index: routes) and Appendix B (definitions: data items,
notes, physical file specification, version history) from the text copy of the PDF."""
import re, collections

ROLES = ['Relevant Participant', 'PA Administrator', 'Meter Administrator', 'The Authority', 'Not Stated',
         'BSC Panel', 'SVA MOA', 'AMVLP', 'VLP', 'VTP', 'SVAA', 'Supplier', 'SAA', 'NETSO', 'AMHHDC', 'HHDC',
         'AMMOA', 'MOA', 'HHDA', 'NHHDC', 'NHHDA', 'HHMO', 'NHHMO', 'LDSO', 'ECVAA', 'CDCA', 'MDDM', 'ISDM',
         'SMRA', 'PAB', 'UMSO', 'BSCCo', 'ADS', 'SDS', 'MRS', 'RPS', 'FAA', 'CRA', 'CMRS']
ROLE_TOKENS = sorted(([r.split() for r in ROLES]), key=len, reverse=True)

FOOTER = re.compile(r'^(SVA Data Catalogue|Appendix [AB]|© 2026,? ELEXON.*Page \d+ of \d+|Date/Issue No:.*'
                    r'|Flow Ref\. Data Flow Name|SVA Data Catalogue Volume 1: Data Interfaces Appendix [AB]'
                    r'|Source From To Version|APPENDIX [AB] - .*|SVA Data Catalogue Volume 1: Data Interfaces)$')

norm = lambda s: re.sub(r'[^a-z0-9]', '', s.lower())


def split_appendices(text):
    lines = text.replace('\r', '').split('\n')
    b0 = next(i for i, l in enumerate(lines) if l.startswith('APPENDIX B - '))
    return lines[:b0], lines[b0:]


# ---------------- Appendix A: routes ----------------
def match_role(tokens, i):
    for rt in ROLE_TOKENS:
        if tokens[i:i + len(rt)] == rt:
            return ' '.join(rt), len(rt)
    return None, 0


def parse_appendix_a(lines, names):
    """names: ref -> catalogue flow name (Appendix B), used to strip the wrapped name from each block."""
    body = [l for l in lines if l.strip() and not FOOTER.match(l)]
    blocks = collections.OrderedDict(); cur = None
    for l in body:
        m = re.match(r'^([PD]\d{4}|P[A-Z]{3,4}_|IF/PUB-\d+|REP-\d+\w*)\b ?(.*)$', l)
        if m:
            cur = m.group(1)
            blocks.setdefault(cur, []).append(('REF', m.group(2)))
        elif cur:
            blocks[cur].append(('TXT', l))
    out = {}
    for ref, parts in blocks.items():
        if not ref.startswith('P'):
            continue
        name_toks = [norm(t) for t in names.get(ref, '').split()]
        # Build records: each ends with a line whose last token is a 3-digit version.
        records, buf, need_strip = [], [], False
        for kind, l in parts:
            if kind == 'REF':
                need_strip = True
            toks = l.split()
            buf.append((need_strip and kind == 'REF', toks))
            if toks and re.fullmatch(r'\d{3}', toks[-1]):
                records.append(buf); buf = []
        routes, source, problems = [], None, []
        name_seen_name = None
        for rec in records:
            toks = [t for _, ts in rec for t in ts]
            # strip flow name (possibly repeated after a page break) from the start of a record that began with REF
            if rec[0][0]:
                k = 0
                while k < len(toks) and k < len(name_toks) and norm(toks[k]) == name_toks[k]:
                    k += 1
                toks = toks[k:]
            version = toks[-1]; toks = toks[:-1]
            # find the From/To role pair: rightmost adjacent pair of roles
            found = None
            for i in range(len(toks) - 1, -1, -1):
                r1, n1 = match_role(toks, i)
                if r1:
                    r2, n2 = match_role(toks, i + n1)
                    if r2:
                        found = (i, r1, n1, r2, n2); break
            if not found:
                problems.append(' '.join(toks + [version])); continue
            i, r1, n1, r2, n2 = found
            src = ' '.join(toks[:i] + toks[i + n1 + n2:]).strip()
            if src:
                b = re.findall(r'\bBSCP\d+\b', src)
                source = b[-1] if b else src  # leftover wrapped-name words before a BSCP are dropped
            routes.append({'source': source, 'from': r1, 'to': r2, 'version': version})
        out[ref] = {'routes': routes, 'unparsed': problems}
    return out


# ---------------- Appendix B: definitions ----------------
TITLE = re.compile(r'^(.*\S) (P\d{4}) (\d{3})$')
HEADERS = {'Data Requirement from BSC Procedures:': 'items', 'Data Group Data Item Name Comment': 'items',
           'Source Document Known as From To Comment': 'routes', 'Version History:': 'history',
           'Physical File Specification:': 'pfs', 'Notes:': 'notes'}
PFS_CONTINUES = {'P0291'}  # continuation page resumes the Physical File Specification
SKIP = {'Catalogue release', 'change takes effect', 'Record Field Name Comment Value Opt'}


def parse_appendix_b(lines):
    flows = collections.OrderedDict(); cur = None; state = None; i = 0
    while i < len(lines):
        l = lines[i]
        if re.match(r'^© 2026, ELEXON.*Page \d+ of 252$', l) and i + 2 < len(lines) and lines[i + 1].startswith('Date/Issue'):
            m = TITLE.match(lines[i + 2])
            if m:
                ref = m.group(2)
                if ref == cur:
                    # continuation page: unless it opens with a section header, it resumes the data items
                    # (or the version history if the break fell inside it)
                    nxt = lines[i + 4] if i + 4 < len(lines) else ''
                    if nxt not in HEADERS and state != 'history':
                        state = 'pfs' if ref in PFS_CONTINUES else 'items'
                else:
                    cur = ref; state = None
                    flows[ref] = {'name': m.group(1), 'version': m.group(3), 'sections': collections.defaultdict(list)}
                i += 4; continue
        if FOOTER.match(l) or not l.strip():
            i += 1; continue
        if cur:
            if l in HEADERS:
                state = HEADERS[l]
            elif l in SKIP or l.startswith('Mod/CP No. Brief description'):
                pass
            else:
                flows[cur]['sections'][state or 'pre'].append(l)
        i += 1
    return flows


# Comment starters seen in the Data Item Comment column.
COMMENT_STARTS = ['True or False', 'Applicable to P', '1 day per file', '1-14', '1-*', '46, 48 or 50', '46,48 or 50',
                  'In MWh', 'For MSID Pair or AMSID Pair', 'For Export AMSID', 'For Import AMSID', 'For AMSID',
                  'For AMHHDC', 'For Boundary Point MSIDs', 'Mandatory', 'Optional', 'Secondary BM Unit',
                  'Secondary/Additional', 'Additional/Secondary', 'Supplier BM Unit', 'Suppier BM Unit',
                  'Primary or Secondary BM Unit', 'MSID or AMSID', 'Id of ', 'B - Balancing', 'May include',
                  'Null if', 'MWh', 'Only issued', 'Only import', 'Only required', '2 digits for', "'T' means",
                  'From Associated MSID Pair', 'Where present', 'Required if', 'Required where', 'In kW',
                  'Boolean', 'Valid Set:', 'Activation for', 'A unique identifier', 'Leave blank', 'Contains details',
                  'For the appointed', 'The same HHDC', 'For the association', 'An AMHHDC may', 'If sent to',
                  'For the Losing', 'Omit for HHDC', 'MSID for']
CONTINUATION_PREFIXES = ('Required if ', 'Leave blank', 'Indicator = ', 'An AMMOA may', 'CoP11.', 'Pair in the ',
                         'If sent to the non-Registrant', 'Registrant AMVP')
CONTINUATION_LINES = {'AMSID Pair.', 'Pair.'}
CONTINUATION = {'MSID Declaration and/or in a NFD Declaration are reported',
                'Pair, all of which are required if Action Indicator = ‘N’ or ‘U’.'}
GROUP_START = re.compile(r'^(Structure [Nn]ot [Ss]pecified)(?: (.*))?$')
GROUP_LONG = re.compile(r'^(Structure specified|Stucture specified|Refer to SVAA Tab)')
GROUP_WRAP = re.compile(r'^((the )?(NETA )?IDD Part \d.*|Spreadsheet.*|IDD Part \d Spreadsheet)$')


def split_item(line, known):
    best = None
    for s in COMMENT_STARTS:
        for m in re.finditer(re.escape(s), line):
            p = m.start()
            if p > 0 and line[p - 1] == ' ':
                name = line[:p - 1].strip()
                if name.lower() in known and (best is None or p < best[0]):
                    best = (p, name, line[p:].strip())
    if best:
        return best[1], best[2], False
    flagged = any(s in line[1:] for s in COMMENT_STARTS) and line.lower() not in known
    return line.strip(), None, flagged


def parse_items(raw, known):
    groups, cur, uncertain = [], None, []
    lines = list(raw); k = 0
    while k < len(lines):
        l = lines[k]
        m = GROUP_START.match(l)
        if m:
            cur = {'name': 'Structure not specified', 'items': []}; groups.append(cur)
            l = m.group(2)
            if not l:
                k += 1; continue
        elif GROUP_LONG.match(l):
            text = l
            while k + 1 < len(lines) and GROUP_WRAP.match(lines[k + 1]):
                k += 1; text += ' ' + lines[k]
            cur = {'name': text, 'items': []}; groups.append(cur)
            k += 1; continue
        if cur is None:
            cur = {'name': None, 'items': []}; groups.append(cur)
        if (l[:1] in "'‘’" or l[:1].islower() or l in CONTINUATION or l in CONTINUATION_LINES
                or l.startswith(CONTINUATION_PREFIXES)) and cur['items']:
            it = cur['items'][-1]
            it['comments'] = (it.get('comments') + ' ' if it.get('comments') else '') + l
        else:
            name, comment, flag = split_item(l, known)
            item = {'name': name}
            if comment:
                item['comments'] = comment
            if flag:
                uncertain.append(l)
            cur['items'].append(item)
        k += 1
    return groups, uncertain


def parse_history(raw):
    out = []
    for l in raw:
        m = re.match(r'^(\d+(?:\.\d+)?) (\S+) (.*)$', l)
        if m:
            out.append({'catalogueRelease': m.group(1), 'change': m.group(2), 'description': m.group(3)})
        elif out:
            out[-1]['description'] += ' ' + l
    return out
