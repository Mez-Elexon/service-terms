# P-flow JSON build scripts

These scripts rebuild `work/P-flows - AMSID IDD v0.1 and SVA Data Catalogue v66.0.json` from its two sources.

| File | What it does |
|---|---|
| `build_pflows.py` | Reads the IDD workbook and the catalogue text, merges them and writes the JSON. |
| `catalogue.py` | Parses the text copy of the SVA Data Catalogue Volume 1. It reads Appendix A (Data Interface Index: routes) and Appendix B (Data Interface Definition: data items, notes, physical file specification, version history). |

## Inputs

1. **AMSID IDD workbook** (`.xlsm`). The script reads the `SVAA P375`, `Items` and `Valid Sets` sheets.
2. **SVA Data Catalogue Volume 1, Appendix A and Appendix B**, as one plain-text file copied from the PDF, with Appendix A first. The parser depends on the PDF's page headers and footers (`© … Page n of …`, `Date/Issue No: …`) to find page breaks.

## Run

Requires Python 3 and `openpyxl` (built and tested with Python 3.13 and openpyxl 3.1.5).

```bash
python3 work/scripts/build_pflows.py path/to/AMSID_IDD.xlsm path/to/APPENDIX_A.txt "work/P-flows - AMSID IDD v0.1 and SVA Data Catalogue v66.0.json"
```

The script prints a summary (flows, routes, families) and any conversion notes. The same notes are stored in the JSON under `conversionNotes`. A note listing "Data-item lines where the item/comment split is uncertain" means a line needs a new rule in `catalogue.py`.

## Review these when a source changes

Some parts are not parsed automatically and are specific to catalogue v66.0 and IDD v0.1. Check them against the new documents:

- **`SCOPE` and `FAMILIES`** in `build_pflows.py`: which flows are included, and how they are grouped.
- **`ROUTE_COMMENTS`**: route comments copied by hand from the Appendix B Comment column. The PDF text runs that column together with the "Known as" column.
- **`CATALOGUE_OBSERVATIONS`**: possible inconsistencies noticed in catalogue v66.0. Remove each entry once it is fixed at source.
- **`COMMENT_STARTS`, `CONTINUATION_*` and `PFS_CONTINUES`** in `catalogue.py`: the rules that split data-item names from their comments and handle page breaks.
- **`ROLES`** in `catalogue.py`: the participant roles recognised in route rows. Add any new role.

The workbook has a print-titles name of `#N/A` that openpyxl cannot read. The script skips defined names, which hold no data.
