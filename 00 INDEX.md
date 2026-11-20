# Evidence pack – index of cleaned Markdown files

Converted on 2026-10-07 from copy-pasted `.txt` files (website pages and PDFs); the three Slow Reserve files marked 2026-10-29 were added later. Each file starts with a header that names its source, its coverage (whether it is complete or an extract) and any repairs made.

This folder holds only the cleaned source documents. Analysis outputs (the earlier `audit_work` folder, the V2.3/V2.4 Revised Table `.docx` files and the CAA resolution-flow diagrams) were moved to `..\work\` on 2026-10-29.

**Conventions used in every file**
- Wording is kept **verbatim**. Only layout artefacts were removed: page headers/footers, page numbers, website navigation, broken line wraps and flattened tables.
- Notes in *[italic square brackets]* are editorial, not source text.
- `<br>` inside a table cell separates lines that sat in the same cell.
- A checker compared every word in each source with its cleaned file. The only gaps are the removed headers/footers, navigation and image placeholders, plus the deliberate repairs listed in each file's header.

## BSC (Elexon) documents

| File | What it is | Coverage |
|---|---|---|
| BSC Section K Classification and Registration of Metering Systems and BM Units | BSC Section K | Full section text (version/date not in the copy) |
| BSC Section Q Balancing Services Activities | BSC Section Q | Full section text (version/date not in the copy) |
| BSC Section S Supplier Volume Allocation | BSC Section S | Full section text (version/date not in the copy) |
| BSC Section S Annex S-2 Supplier Volume Allocation Rules V35.0 | Annex S-2, effective 27/11/2025 | Full |
| BSC Annex X-2 Technical Glossary V62.0 | Annex X-2: subscripts, summations, operators, timing conventions and glossaries (Tables X-1 to X-9), effective 29/10/2026 (added 2026-11-20) | Full; Symbol-font maths repaired; formulas also rendered as LaTeX; editorial notation guide at the end |
| BSC Section T Settlement and Trading Charges V45.0 | Section T incl. Annexes T-1, T-2, effective 27/11/2025 | Full; equations in Annex T-1 paras 13.2–16 rebuilt |
| BSC Baselining Methodology Document V3.0 | Code Subsidiary Document, effective 07/11/2024 | Full |
| BSC Code of Practice 11 | CoP11 (balancing services asset metering) | Extract from Section 3 to the end |
| BSCP01 / BSCP15 / BSCP31 / BSCP602 / BSCP603 / BSCP607 | BSC Procedures | Full |
| SAA Service Description for Settlement Administration V40.0 | SAA service description, effective 27/11/2025 | Full; Symbol-font maths repaired |

## NESO / Market Facilitator / other documents

| File | What it is | Coverage |
|---|---|---|
| ABSVD Methodology Statement | NESO ABSVD Methodology Statement | Extract from 1.2 to the end |
| DFS Procurement Rules and Service Terms 2026 | DFS Service Terms (Part A) + DFS Procurement Rules (Part B) | Extracts (see header) |
| DFS Stacking List v2 April 2026 | DFS stacking list | Full |
| Quick Reserve QR Procurement Rules 2026 | QR Procurement Rules | Paras 3–7, Schedules 1–2, plus a fragment of SR rules para 21 |
| Slow Reserve Procurement Rules Schedule 2 … | SR Schedule 2 | Extract; truncated at the end |
| Slow Reserve SR Service Terms V1.0 | NESO SR Service Terms, effective 31/03/2026 (added 2026-10-29) | Full. Extracted from the NESO PDF, not a copy-paste; cover and contents removed; Schedule 2 table and Schedule 4 formulae rebuilt |
| Slow Reserve SR Guidance Document V2 April 2026 | NESO SR guidance slide deck (added 2026-10-29) | **Condensed**: substantive slide text verbatim, repeated boilerplate and onboarding click-steps removed, worked examples cut down to inputs/checks/outcomes. Guidance only; the Service Terms prevail |
| Slow Reserve SR Service and Procurement Design Proposal V3.0 October 2025 | NESO SR design document supporting the Ofgem-approved terms (source file `slowreserveSTs.txt`; added 2026-10-29) | **Condensed**: substantive wording verbatim, design rationale and history summarised in one line each. Pre-dates Service Terms V1.0; where they differ, the Service Terms govern |
| Static FFR Procurement Rules | Static FFR rules | Paras 1–6, Schedules 1–2 |
| LCM Local Constraint Market Service Terms V2.0 | NESO LCM Service Terms | Full |
| SMP User Guide 2026 (two files) | NESO SMP user guide chapters | Extracts; screenshots not captured |
| Capacity Market Rules 2026 consolidated extract | CM Rules (consolidated 24 July 2026) | Schedules 2–6, Rules 3.9–3.10, 7.4–7.4A |
| CP400 Capacity Market Rule Change Proposal – Duplicate MPANs | CM rule change proposal (P400), submitted 14/07/2026 | Full |
| FMR-PD / FMR-PR / FMR-SMD / FMR-VSM | Flexibility Market Rules (Market Facilitator) | Full |
| DNO Flexibility Market Rules 2026 | FMR-SBM + FMR-VSM + FMR-PQC joined together | Extracts. Part B duplicates FMR-VSM V2.3 |
| DNO Common Flexibility Service Terms and Conditions V3.2 General Terms | DNO standard agreement general terms | Paragraphs 3–24 |

## Reconstructions to check against the original before relying on them

1. **BSCP procedure tables (REF / WHEN / ACTION / FROM / TO / …).** Rows are reliable. The FROM/TO/INFORMATION cell boundaries were inferred from party names; the few rows that could not be split say so.
2. **FMR-VSM / DNO Rules Part B equation for UC[s,j]** (delivered/utilised MW). The nesting is ambiguous in the source and is flagged in place. The Performance Multiplier reconstruction was checked against the worked examples in Table 4.
3. **BSC Section T, Annex T-1 paras 13.2–16.** Equations are rebuilt in the BSC's run-together notation with symbols in source order. Subscripts, superscripts and fraction bars are not marked.
4. **DNO Rules Part A, Default Baseline Methodology tables and nomination deadlines table; Part C qualification criteria tables.** These have merged cells, so they are given as cells in source order or as rows keyed on field codes, not as a guessed grid.
5. **Images and diagrams were not captured.** This includes process diagrams, the FMR-SBM accuracy formulas (Net % Error, Absolute % Error, Effective Capacity) and the SMP screenshots. Each is marked where it occurred.
6. **CP400 proposed legal text.** Tracked-change markup (deletions and insertions) was lost in the copy-paste, so the amended wording of CM Rule 8.3.3(f)(i) cannot be told apart from the old wording.
7. **BSC Annex X-2, Tables X-4, X-5 and X-9.** The symbol column was split from the meaning column in the copy. They were re-paired in source order (the counts match in every block). The Table X-6 row "Time of Sunset" has an inferred cell split.
