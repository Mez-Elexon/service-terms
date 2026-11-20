# Flexibility Asset Notation – Draft v0.2

> **Status:** DRAFT v0.2 for review. Not BSC text.  
> **Changes from v0.1:** proposed rules S19a, S24a and S29a and the corrected S40 were accepted for drafting and are flagged for review; long equations were split over several lines and checked with MathJax.  
> **Source:** CAA flexibility statements 1–72 (`flex_statements.txt`), formalised in the notation of BSC Annex X-2 (see `BSC Annex X-2 Technical Glossary V62.0.md`).  
> **Approach (agreed):**
> - **Style:** BSC index letters are reused where their meaning matches. New indices use the BSC's bracketed multi-letter style, e.g. (ai), (vv). Set operators are added only where a statement needs them.
> - **Time:** time is indexed by a new activation-period index (ap).
> - **Meters:** meters reuse K.
> - **Units:** a Unit is a generic index, mapped to a Secondary BM Unit i2 in the BM and wholesale sub-markets.
> - **Volumes:** volume equations are added for measurement arrangements.
> - **Open items:** every [Open] branch is written out and labelled.
> - **Statement 5:** restated as "at most one" boundary point.
>
> **Layout:** each statement is quoted, then given in BSC run-together form (`code`), then rendered in LaTeX. Issues the notation exposed are collected in Part C.

## Review checklist

> [!IMPORTANT]
> The items below were **accepted for drafting** but have **not been confirmed by CAA**. Each one is marked with a ⚠️ warning box where it appears.

**Proposed rules and corrections (accepted for drafting, for review)**

| Item | What it says | Why it is needed | Where |
|---|---|---|---|
| S19a | Asset meters at a boundary point are either nested or reach disjoint TRs (they form a tree) | S39 and the topology test in S42 do not hold without it | F4 |
| S24a | Meters subtracted in one Difference arrangement must not be nested in each other | Without it, the Difference volume (V1) subtracts nested TRs twice and V3 fails | F6 |
| S29a | Every Asset is measurable | S35 (composition overlap ⇒ measurement overlap) does not hold without it | F3 |
| S40 (corrected) | An Asset Level Asset on K does not overlap a Difference Asset if K equals, or is nested behind, a subtracted meter | The statement as written is false when K sits behind a subtracted meter | F5 |

**Drafting assumptions (accepted for drafting, for review):** F1, F2, F11, F12, F13, F14 and F15 in Part C.

**Decisions still needed from CAA:** F7 (S32-Yes needs compatibility between control groups), F8 (Assets entered by delegation under 1b bypass the compatibility check), F9 (exclusivity rule for scenario 0b) and F10 (definition of the coordinating group).

---

## Part A – Notation register

### A.1 Conventions

| # | Convention |
|---|---|
| C1 | Every formula holds for each activation period (ap). (ap) is written in definitions. In a rule, it is dropped where every term refers to the same (ap) (cf. Annex X-2 2.6.3, "further defined in context"). |
| C2 | An acronym with no index is the universal set, e.g. TR is every TR. With indices it is a member, subset or value, e.g. TR(bp)(ap). |
| C3 | Indicators take the value 1 or 0, as in BSC Table X-6 (e.g. SQCj "Indicator (1 or 0)"). Counting is done by summing indicators with Σ. Set-size bars are not used, because the BSC already uses \|FUNC\| for absolute value (1.2.1(d)). |
| C4 | Volumes follow the 2.4.1 sign convention: positive for Active Energy delivered to the Total System (export), negative for offtake. |
| C5 | Where a statement is [Open], each branch is a separate formula labelled with the branch, e.g. **S32-Yes**, **S56-1a**. |

### A.2 Indices reused from Annex X-2

| Index | BSC meaning | Use here |
|---|---|---|
| K | Table X-4: an SVA Metering System Number and/or Asset Metering System | A meter. A boundary meter is an MSID Pair; an asset meter is an AMSID Pair (CoP11). See issue F13. |
| j | Settlement Period (Tables X-1, X-4) | Settlement Period, for volumes |
| t | Spot time (paragraph 4.4.2) | Spot time, for location and for allocation start/end |
| p | Table X-1: Trading Party, … Virtual Lead Party | Any party: FSP, Primary (CFPC holder) or Load Controller. Not used in Table X-4, so there is no clash in Section S. |
| i2 | Table X-4: Secondary BM Unit | The BSC counterpart of a Unit (un) in the BM and wholesale sub-markets |

### A.3 New indices

| Index | Meaning | Statement |
|---|---|---|
| (bp) | Boundary point | 1 |
| (tr) | Technical Resource (TR) | 2 |
| (cu) | Customer | 4 |
| (sm) | Sub-market | 4 |
| (ap) | Activation period | 4, C1 |
| (cg) | TR control group (itself a set of TRs) | 10 |
| (ma) | Measurement arrangement | 20 |
| (fa) | Flexibility Asset | 27 |
| (cl) | Registration (claim) | 52 |
| (cc) | Customer contract (CFPC) | 55 |
| (dg) | Delegation | 57 |
| (al) | Allocation | 64 |
| (un) | Unit | 69 |

*Checked against Tables X-1 and X-4: none of these clashes with an existing BSC index. MS (Market Segment) and (ai) (Adjusted Interval) are different symbols.*

### A.4 New sets, functions and indicators

| Acronym | Kind | Meaning | Statement |
|---|---|---|---|
| BP, TR, MTR, PTY, CUS, SM, AP | set | All boundary points, TRs, meters, parties, customers, sub-markets, activation periods | 1–4 |
| MTRB, MTRA | set | Boundary meters, asset meters (MTR = MTRB ∪ MTRA, MTRB ∩ MTRA = ∅) | 3 |
| BEH(tr)(bp)t | indicator | 1 if (tr) is behind (bp) at spot time t | 5 |
| BEH(tr)(bp)(ap) | indicator | max over t∈(ap) of BEH(tr)(bp)t | 6 |
| TR(bp)(ap) | set | TRs behind (bp) in (ap) | 7 |
| ACT(ap) | set | Actively controlled TRs | 9 |
| LC(tr)(ap) | function → p | Load Controller of (tr) | 8, 9 |
| ILC(tr)p(ap) | indicator | 1 if p is the Load Controller of (tr) | 9 |
| BPCG(cg), LCCG(cg)(ap) | function | Boundary point and Load Controller of control group (cg) | 10 |
| CG(bp)(ap) | set | Control groups at (bp) | 10 |
| RG(bp)(ap) | set | Residual group at (bp) | 13 |
| MTR(bp) | set | Meters at (bp) (written K∈(bp), as a∈p in 1.2.1(b)) | 15 |
| KB(bp) | meter | The boundary meter of (bp) | 17, 22 |
| REACH(K)(ap) | set | TRs whose flow passes through meter K | 16 |
| K′ ⊑ K | relation | Asset meter K′ sits behind meter K (nested) | 19 |
| SGN(ma)K | +1, 0, −1 | Sign with which meter K counts in arrangement (ma) | 20 |
| MTR(ma), BPMA(ma) | set, function | Meters used by (ma); its boundary point | 20 |
| TYPE(ma) | label | POC, AL or DIFF | 22–24 |
| KSUB(ma) | set | Meters subtracted in a DIFF arrangement | 24 |
| PER(ma)(ap) | set | Measurement perimeter of (ma) | 21 |
| SMDIFF | set | Sub-markets that accept DIFF | 26 |
| QMKj | MWh | Net metered volume of meter K in j | V1 |
| QMA(ma)j | MWh | Volume measured by arrangement (ma) in j | V1 |
| QTR(tr)j | MWh | Notional (unmetered) net flow of (tr) in j | V3 |
| FCG(fa), FMA(fa) | function | Control group and arrangement of Asset (fa) | 27 |
| BPFA(fa) | function | Boundary point of (fa) | 27 |
| TRFA(fa)(ap) | set | The TRs of Asset (fa) | 28 |
| QFA(fa)j | MWh | Volume of Asset (fa) in j | V2 |
| FA(bp)(ap) | set | Assets at (bp) | 33 |
| MEAS, EXA, INC(fa)(ap) | indicator | Measurable, exactly measured, inclusively measured | 29, 30 |
| COV, MOV(fa)(fa′)(ap) | indicator | Composition overlap, measurement overlap | 33, 34 |
| COMP(fa)(ap) | indicator | (fa) has no measurement overlap with any other Asset at its boundary point | 43, 44 |
| REC, IRR(fa)(fa′)(ap) | indicator | Reconcilable, irreconcilable | 46, 49 |
| FSPCL, FACL, SMCL(cl); APCL(cl) | function; set | Who claims what, where; for which activation periods | 52, 53 |
| VAL(cl) | indicator | Registration is valid | 54 |
| AUTH p(tr)(sm)(ap) | indicator | p has authority over (tr) for (sm) | 54 |
| CUSBP(bp)(ap) | function → (cu) | Customer at (bp) | 55, 59 |
| CUSCC, BPCC, HOLDCC(cc); TRCC, SMCC, APCC(cc) | function; set | Contract's customer, boundary point, holder (Primary); its TRs, sub-markets, periods in force | 55 |
| CCDG, SECDG, SMDG(dg); APDG(dg) | function; set | Delegation's parent contract, Secondary, sub-market; periods in force | 57 |
| CMP(cl)(cl′) | indicator | The registrations compete | 60–62 |
| COORD(fa)(ap) | set of p | Coordinating group of FSPs (scenario 1a) | 62 |
| PRI(fa)(ap) | set of p | Holder(s) of the contracts covering the Asset's TRs (the Primary) | 62, 63 |
| DEL p(fa)(sm)(ap) | indicator | p is the Primary, or holds a delegation for (sm) from the Primary | 62-1b |
| NCC(tr)(sm)(ap) | count | Number of contracts covering (tr) for (sm) | 56 |
| RULE(sm) | rule | A sub-market's own competition rule (scenario 0a) | 62-0a |
| MTR⁺(bp) | set | Existing meters plus meters that could be added at (bp) | 46 |
| ASG(fa)(ap) | function | Prevailing FSP, FSP group or Primary | 63 |
| FAAL(al), GRPAL(al), TSAL(al), TEAL(al), APAL(al) | function; set | Allocation's Asset, FSP group, start/end spot times, activation periods covered | 64, 68 |
| IENT(fa)(sm)p(ap) | indicator | p enters (fa) into (sm) | 67 |
| FSPUN, SMUN(un); FAUN(un)(ap) | function; set | Unit's FSP and sub-market; its Assets | 69 |
| SCN | label | Design scenario: 0a, 0b, 1a, 1b or 2 | 56, 62 |

### A.5 Operators added beyond Annex X-2 paragraph 1.2

Annex X-2 already provides `*`, ∈, Σ, min/max and |FUNC|. This draft adds only the following:

| Operator | Meaning |
|---|---|
| ⊆, ⊂ | subset, proper subset |
| ∪, ∩, \ | union, intersection, set difference |
| ∅ | empty set |
| [P] | 1 if statement P is true, else 0 (used to build indicators) |
| ∀, ∃ | for every, there exists |
| ⇒, ⇔ | implies, if and only if |
| ⊑ | "is nested behind" (asset meters) |

### A.6 Mapping to BSC terms

| This draft | BSC term | Reference |
|---|---|---|
| (bp) | Boundary Point and its Metering Systems (MSIDs), identified by the import MPAN | Statement 1 |
| K∈MTRB | MSID Pair (import + export SVA Metering Systems at the boundary) | Annex X-2 Table X-2 "MSID Pair Data" |
| K∈MTRA | AMSID Pair (Asset Metering Systems, CoP11) | Section S10.1A; BSCP602/603 |
| TYPE(ma) = AL | AMSID Pair flows "allocated to the BM Unit" | S10.1A.2(e)(i); ΣKNonDiff (Table X-5) |
| K∈KSUB(ma), TYPE(ma) = DIFF | AMSID Pair flows "subtracted from … the Associated MSID Pair(s)" ("Asset Differencing") | S10.1A.2(e)(ii); ΣKDiff (Table X-5) |
| QMKj | Net of the export and import metered volumes of the MSID/AMSID Pair, MWh (e.g. built from AMMCKj in kWh ÷ 1000) | Tables X-6/X-7 |
| (un) when (sm) ∈ {BM, wholesale} | Secondary BM Unit i2 | Table X-4 |
| p acting as FSP in BM/wholesale | Virtual Lead Party (AMVLP under P375) | Table X-1 "p" |
| S71 | "an AMSID Pair may not be allocated to more than one Secondary BM Unit for any given time" | S10.1A.3 |

---

## Part B – Statements formalised

### 1. Basic sets

**S1 [Def]** Boundary points.

`(bp) ∈ BP`

```math
(bp) \in \mathrm{BP}
```

**S2 [Def]** Technical Resources.

`(tr) ∈ TR`

```math
(tr) \in \mathrm{TR}
```

**S3 [Def]** Meters are boundary meters or asset meters.

`K ∈ MTR;  MTR = MTRB ∪ MTRA;  MTRB ∩ MTRA = ∅`

```math
K \in \mathrm{MTR}, \qquad \mathrm{MTR} = \mathrm{MTRB} \cup \mathrm{MTRA}, \qquad \mathrm{MTRB} \cap \mathrm{MTRA} = \varnothing
```

**S4 [Def]** Parties, customers, sub-markets, activation periods. Settlement Periods relate to activation periods as j∈D does in 1.2.1(b).

`p ∈ PTY;  (cu) ∈ CUS;  (sm) ∈ SM;  (ap) ∈ AP;  j∈(ap) denotes the Settlement Periods j that overlap (ap)`

```math
p \in \mathrm{PTY},\quad (cu) \in \mathrm{CUS},\quad (sm) \in \mathrm{SM},\quad (ap) \in \mathrm{AP},\quad j \in (ap)
```

### 2. TRs and location

**S5 [Rule, restated: "at most one"]** A TR is behind at most one boundary point at any time.

`Σ(bp) BEH(tr)(bp)t ≤ 1   for every (tr), t`

```math
\sum_{(bp)} \mathrm{BEH}_{(tr)(bp)t} \le 1 \qquad \forall (tr),\ t
```

**S6 [Rule]** A mobile TR is behind at most one boundary point in any activation period.

`BEH(tr)(bp)(ap) = max t∈(ap) BEH(tr)(bp)t;   Σ(bp) BEH(tr)(bp)(ap) ≤ 1`

```math
\mathrm{BEH}_{(tr)(bp)(ap)} = \max_{t \in (ap)} \mathrm{BEH}_{(tr)(bp)t}, \qquad \sum_{(bp)} \mathrm{BEH}_{(tr)(bp)(ap)} \le 1
```

*S5 is the special case of S6 for a single spot time.*

**S7 [Derived]** The TRs behind a boundary point.

`TR(bp)(ap) = { (tr) ∈ TR : BEH(tr)(bp)(ap) = 1 }`

```math
\mathrm{TR}_{(bp)(ap)} = \{\, (tr) \in \mathrm{TR} : \mathrm{BEH}_{(tr)(bp)(ap)} = 1 \,\}
```

*Consequence of S6: TR(bp)(ap) ∩ TR(bp′)(ap) = ∅ for (bp) ≠ (bp′).*

### 3. Control: TR control groups

**S8 [Def]** Load Controller.

`LC(tr)(ap) = p   (the party that creates or changes the control signal for (tr))`

```math
\mathrm{LC}_{(tr)(ap)} = p
```

**S9 [Rule]** Every actively controlled TR has exactly one Load Controller.

`ILC(tr)p(ap) = [LC(tr)(ap) = p];   Σp ILC(tr)p(ap) = [(tr) ∈ ACT(ap)]`

```math
\sum_{p} \mathrm{ILC}_{(tr)p(ap)} = \big[(tr) \in \mathrm{ACT}_{(ap)}\big]
```

*The right-hand side is 1 for a controlled TR (exactly one Load Controller) and 0 otherwise (none).*

**S10 [Def]** A TR control group: non-empty, one boundary point, one Load Controller.

`(cg) ⊆ TR(bp)(ap);  (cg) ≠ ∅;  BPCG(cg) = (bp);  LC(tr)(ap) = LCCG(cg)(ap) for every (tr) ∈ (cg)`
`CG(bp)(ap) = { (cg) : BPCG(cg) = (bp) }`

```math
\varnothing \ne (cg) \subseteq \mathrm{TR}_{(bp)(ap)}, \qquad \forall (tr) \in (cg):\ \mathrm{LC}_{(tr)(ap)} = \mathrm{LCCG}_{(cg)(ap)}
```

**S11 [Rule]** Every actively controlled TR is in exactly one control group.

`Σ(cg)∈CG(bp)(ap) [(tr) ∈ (cg)] = 1   for every (tr) ∈ ACT(ap) ∩ TR(bp)(ap)`

```math
\sum_{(cg) \in \mathrm{CG}_{(bp)(ap)}} \big[(tr) \in (cg)\big] = 1 \qquad \forall (tr) \in \mathrm{ACT}_{(ap)} \cap \mathrm{TR}_{(bp)(ap)}
```

**S12 [Derived from S11]** Control groups do not overlap.

`(cg) ∩ (cg′) = ∅   for (cg) ≠ (cg′)`

```math
(cg) \cap (cg') = \varnothing \qquad (cg) \ne (cg')
```

**S13 [Def]** Residual group.

`RG(bp)(ap) = TR(bp)(ap) \ ∪(cg)∈CG(bp)(ap) (cg)`

```math
\mathrm{RG}_{(bp)(ap)} = \mathrm{TR}_{(bp)(ap)} \setminus \bigcup_{(cg) \in \mathrm{CG}_{(bp)(ap)}} (cg)
```

*By S11 the residual group holds exactly the TRs with no Load Controller: RG(bp)(ap) = TR(bp)(ap) \ ACT(ap).*

**S14 [Derived]** Control groups and the residual group partition the boundary point.

`∪(cg)∈CG(bp)(ap) (cg) ∪ RG(bp)(ap) = TR(bp)(ap);  (cg) ∩ (cg′) = ∅;  (cg) ∩ RG(bp)(ap) = ∅`

```math
\begin{aligned}
&\bigcup_{(cg) \in \mathrm{CG}_{(bp)(ap)}} (cg) \;\cup\; \mathrm{RG}_{(bp)(ap)} = \mathrm{TR}_{(bp)(ap)} \\
&(cg) \cap (cg') = \varnothing \ \ \text{for } (cg) \ne (cg'), \qquad (cg) \cap \mathrm{RG}_{(bp)(ap)} = \varnothing
\end{aligned}
```

### 4. Measurement

**S15 [Def]** Every meter belongs to exactly one boundary point.

`Σ(bp) [K ∈ (bp)] = 1;   MTR(bp) = { K : K ∈ (bp) }`

```math
\sum_{(bp)} \big[K \in (bp)\big] = 1, \qquad \mathrm{MTR}_{(bp)} = \{\, K : K \in (bp) \,\}
```

**S16 [Def]** Reach of a meter.

`REACH(K)(ap) ⊆ TR   (TRs whose energy flow passes through K)`

```math
\mathrm{REACH}_{K(ap)} \subseteq \mathrm{TR}
```

**S17 [Rule]** A boundary meter reaches every TR at its boundary point. Each boundary point has one boundary meter, KB(bp) (see F13).

`MTRB ∩ MTR(bp) = { KB(bp) };   REACH(KB(bp))(ap) = TR(bp)(ap)`

```math
\mathrm{MTRB} \cap \mathrm{MTR}_{(bp)} = \{\mathrm{KB}_{(bp)}\}, \qquad \mathrm{REACH}_{\mathrm{KB}_{(bp)}(ap)} = \mathrm{TR}_{(bp)(ap)}
```

**S18 [Rule]** An asset meter reaches a subset of its boundary point.

`K ∈ MTRA ∩ MTR(bp)  ⇒  REACH(K)(ap) ⊆ TR(bp)(ap)`

```math
K \in \mathrm{MTRA} \cap \mathrm{MTR}_{(bp)} \;\Rightarrow\; \mathrm{REACH}_{K(ap)} \subseteq \mathrm{TR}_{(bp)(ap)}
```

**S19 [Rule]** Nested sub-metering.

`K′ ⊑ K  ⇒  REACH(K′)(ap) ⊆ REACH(K)(ap)`

```math
K' \sqsubseteq K \;\Rightarrow\; \mathrm{REACH}_{K'(ap)} \subseteq \mathrm{REACH}_{K(ap)}
```

**⚠️ S19a [Rule – proposed, needed for S39 and S42; see F4]** Asset meters at a boundary point form a tree: two asset meters are either nested or reach disjoint TRs.

> [!WARNING]
> **For review: proposed rule.** Not in the CAA statements. Accepted for drafting on 2026-11-20 and needs CAA confirmation before use (see F4 and the review checklist).

`for K, K′ ∈ MTRA ∩ MTR(bp):  K′ ⊑ K  or  K ⊑ K′  or  REACH(K)(ap) ∩ REACH(K′)(ap) = ∅`

```math
K' \sqsubseteq K \;\lor\; K \sqsubseteq K' \;\lor\; \mathrm{REACH}_{K(ap)} \cap \mathrm{REACH}_{K'(ap)} = \varnothing
```

**S20 [Def]** A measurement arrangement is a signed set of meters at one boundary point.

`SGN(ma)K ∈ {+1, 0, −1};   MTR(ma) = { K : SGN(ma)K ≠ 0 } ≠ ∅;   MTR(ma) ⊆ MTR(BPMA(ma))`

```math
\begin{aligned}
&\mathrm{SGN}_{(ma)K} \in \{+1, 0, -1\} \\
&\varnothing \ne \mathrm{MTR}_{(ma)} = \{K : \mathrm{SGN}_{(ma)K} \ne 0\} \subseteq \mathrm{MTR}_{\mathrm{BPMA}_{(ma)}}
\end{aligned}
```

**S21 [Def]** Measurement perimeter: given by S22–S24 for each type.

`PER(ma)(ap) ⊆ TR(BPMA(ma))(ap)`

```math
\mathrm{PER}_{(ma)(ap)} \subseteq \mathrm{TR}_{\mathrm{BPMA}_{(ma)}(ap)}
```

**S22 [Rule]** Point of Connection.

`TYPE(ma) = POC:  MTR(ma) = { KB(bp) },  SGN(ma)KB(bp) = +1;   PER(ma)(ap) = TR(bp)(ap)`

```math
\mathrm{TYPE}_{(ma)} = \mathrm{POC}: \quad \mathrm{MTR}_{(ma)} = \{\mathrm{KB}_{(bp)}\},\ \ \mathrm{PER}_{(ma)(ap)} = \mathrm{TR}_{(bp)(ap)}
```

**S23 [Rule]** Asset Level (S10.1A.2(e)(i)).

`TYPE(ma) = AL:  MTR(ma) = { K },  K ∈ MTRA,  SGN(ma)K = +1;   PER(ma)(ap) = REACH(K)(ap)`

```math
\begin{aligned}
&\mathrm{TYPE}_{(ma)} = \mathrm{AL}: \quad \mathrm{MTR}_{(ma)} = \{K\},\ K \in \mathrm{MTRA} \\
&\mathrm{PER}_{(ma)(ap)} = \mathrm{REACH}_{K(ap)}
\end{aligned}
```

**S24 [Rule]** Difference (S10.1A.2(e)(ii), "Asset Differencing").

`TYPE(ma) = DIFF:  MTR(ma) = { KB(bp) } ∪ KSUB(ma);  ∅ ≠ KSUB(ma) ⊆ MTRA ∩ MTR(bp);`
`SGN(ma)KB(bp) = +1;  SGN(ma)K = −1 for K ∈ KSUB(ma);   PER(ma)(ap) = TR(bp)(ap) \ ∪K∈KSUB(ma) REACH(K)(ap)`

```math
\mathrm{TYPE}_{(ma)} = \mathrm{DIFF}: \quad \mathrm{PER}_{(ma)(ap)} = \mathrm{TR}_{(bp)(ap)} \setminus \bigcup_{K \in \mathrm{KSUB}_{(ma)}} \mathrm{REACH}_{K(ap)}
```

**⚠️ S24a [Rule – proposed, needed for V3; see F6]** No subtracted meter is nested behind another subtracted meter.

> [!WARNING]
> **For review: proposed rule.** Not in the CAA statements. Accepted for drafting on 2026-11-20 and needs CAA confirmation before use (see F6 and the review checklist).

`for K ≠ K′ in KSUB(ma):  REACH(K)(ap) ∩ REACH(K′)(ap) = ∅`

```math
K \ne K' \in \mathrm{KSUB}_{(ma)} \;\Rightarrow\; \mathrm{REACH}_{K(ap)} \cap \mathrm{REACH}_{K'(ap)} = \varnothing
```

**S25 [Rule]** Every subtracted meter is the Asset Level meter of another Asset at the same boundary point.

`TYPE(FMA(fa)) = DIFF  ⇒  for every K ∈ KSUB(FMA(fa)) there exists (fa′) ≠ (fa) with BPFA(fa′) = BPFA(fa), TYPE(FMA(fa′)) = AL and MTR(FMA(fa′)) = { K }`

```math
\forall K \in \mathrm{KSUB}_{\mathrm{FMA}_{(fa)}}\ \exists (fa') \ne (fa):\ \mathrm{TYPE}_{\mathrm{FMA}_{(fa')}} = \mathrm{AL},\ \mathrm{MTR}_{\mathrm{FMA}_{(fa')}} = \{K\}
```

**S26 [Rule]** Difference only in accepting sub-markets.

`TYPE(FMA(FACL(cl))) = DIFF  ⇒  SMCL(cl) ∈ SMDIFF;    today SMDIFF = { BM, wholesale } (AMVLPs, P375)`

```math
\mathrm{TYPE}_{\mathrm{FMA}_{\mathrm{FACL}_{(cl)}}} = \mathrm{DIFF} \;\Rightarrow\; \mathrm{SMCL}_{(cl)} \in \mathrm{SMDIFF}
```

**V1 [Def – volume of an arrangement]** The signed sum of meter volumes, in the same form as AMMCKj = ΣKJ AMRCKJj in Annex S-2 3.5.3A.

`QMA(ma)j = ΣK∈MTR(ma) SGN(ma)K * QMKj`

```math
\mathrm{QMA}_{(ma)j} = \sum_{K \in \mathrm{MTR}_{(ma)}} \mathrm{SGN}_{(ma)K} \cdot \mathrm{QM}_{Kj}
```

By type:

```math
\begin{aligned}
\text{POC:}\quad & \mathrm{QMA}_{(ma)j} = \mathrm{QM}_{\mathrm{KB}_{(bp)}j} \\
\text{AL:}\quad & \mathrm{QMA}_{(ma)j} = \mathrm{QM}_{Kj} \\
\text{DIFF:}\quad & \mathrm{QMA}_{(ma)j} = \mathrm{QM}_{\mathrm{KB}_{(bp)}j} - \sum_{K \in \mathrm{KSUB}_{(ma)}} \mathrm{QM}_{Kj}
\end{aligned}
```

**V2 [Def – volume of an Asset]**

`QFA(fa)j = QMA(FMA(fa))j`

```math
\mathrm{QFA}_{(fa)j} = \mathrm{QMA}_{\mathrm{FMA}_{(fa)}j}
```

**V3 [Derived – volume matches perimeter]** Each meter records the net flow of the TRs it reaches (QMKj = Σ(tr)∈REACH(K) QTR(tr)j, ignoring losses inside the premises). With S19a and S24a it follows that:

`QMA(ma)j = Σ(tr)∈PER(ma)(ap) QTR(tr)j   for j∈(ap)`

```math
\mathrm{QMA}_{(ma)j} = \sum_{(tr) \in \mathrm{PER}_{(ma)(ap)}} \mathrm{QTR}_{(tr)j} \qquad j \in (ap)
```

*Without S24a, a TR inside two nested subtracted meters is subtracted twice. V3 then fails even though S24's perimeter is unchanged.*

### 5. Assets

**S27 [Def]** A Flexibility Asset pairs one control group with one arrangement at the same boundary point.

`(fa) ↦ ( FCG(fa), FMA(fa) );  BPFA(fa) = BPCG(FCG(fa)) = BPMA(FMA(fa))`

```math
(fa) \mapsto \big(\mathrm{FCG}_{(fa)},\ \mathrm{FMA}_{(fa)}\big), \qquad \mathrm{BPFA}_{(fa)} = \mathrm{BPCG}_{\mathrm{FCG}_{(fa)}} = \mathrm{BPMA}_{\mathrm{FMA}_{(fa)}}
```

*See F2: S31 also lets FCG(fa) be the residual group RG(bp)(ap).*

**S28 [Def]** An Asset's TRs.

`TRFA(fa)(ap) = FCG(fa)`

```math
\mathrm{TRFA}_{(fa)(ap)} = \mathrm{FCG}_{(fa)}
```

**S29 [Rule]** Measurable.

`MEAS(fa)(ap) = [ TRFA(fa)(ap) ⊆ PER(FMA(fa))(ap) ]`

```math
\mathrm{MEAS}_{(fa)(ap)} = \big[\,\mathrm{TRFA}_{(fa)(ap)} \subseteq \mathrm{PER}_{\mathrm{FMA}_{(fa)}(ap)}\,\big]
```

**⚠️ S29a [Rule – proposed, needed for S35; see F3]** Every Asset is measurable.

> [!WARNING]
> **For review: proposed rule.** Not in the CAA statements. Accepted for drafting on 2026-11-20 and needs CAA confirmation before use (see F3 and the review checklist).

`MEAS(fa)(ap) = 1   for every (fa)`

```math
\mathrm{MEAS}_{(fa)(ap)} = 1 \qquad \forall (fa)
```

**S30 [Def]** Exactly and inclusively measured.

`EXA(fa)(ap) = [ PER(FMA(fa))(ap) = TRFA(fa)(ap) ];   INC(fa)(ap) = [ TRFA(fa)(ap) ⊂ PER(FMA(fa))(ap) ]`

```math
\mathrm{EXA}_{(fa)(ap)} = \big[\mathrm{PER} = \mathrm{TRFA}\big], \qquad \mathrm{INC}_{(fa)(ap)} = \big[\mathrm{TRFA} \subset \mathrm{PER}\big]
```

*Derived for TYPE = POC, from S14 and S22:*

`EXA(fa)(ap) = 1  ⇔  CG(bp)(ap) = { FCG(fa) }  and  RG(bp)(ap) = ∅`

```math
\mathrm{EXA}_{(fa)(ap)} = 1 \iff \mathrm{CG}_{(bp)(ap)} = \{\mathrm{FCG}_{(fa)}\} \ \text{and}\ \mathrm{RG}_{(bp)(ap)} = \varnothing
```

**S31 [Def]** Residual Asset.

`FCG(fa) = RG(bp)(ap)  and  TYPE(FMA(fa)) = DIFF`

```math
\mathrm{FCG}_{(fa)} = \mathrm{RG}_{(bp)(ap)}, \qquad \mathrm{TYPE}_{\mathrm{FMA}_{(fa)}} = \mathrm{DIFF}
```

**S32 [Open]** Can one control group form more than one Asset?

**S32-No** – one Asset per control group:

`FCG(fa) = FCG(fa′)  ⇒  (fa) = (fa′)`

```math
\mathrm{FCG}_{(fa)} = \mathrm{FCG}_{(fa')} \;\Rightarrow\; (fa) = (fa')
```

**S32-Yes** – several Assets per control group, at most one per sub-market. The unique object is (cg). Two extra rules are needed (see F7):

`S32-Yes(i):  at most one Asset per (cg) is entered into each (sm):  Σ(fa):FCG(fa)=(cg) Σp IENT(fa)(sm)p(ap) ≤ 1`
`S32-Yes(ii): S43/S44 are assessed only between Assets with different control groups`

```math
\sum_{(fa):\,\mathrm{FCG}_{(fa)} = (cg)} \ \sum_{p} \mathrm{IENT}_{(fa)(sm)p(ap)} \le 1 \qquad \forall (cg), (sm), (ap)
```

### 6. Overlap

Let `FA(bp)(ap) = { (fa) : BPFA(fa) = (bp) }`.

**S33 [Def]** Composition overlap.

`COV(fa)(fa′)(ap) = [ TRFA(fa)(ap) ∩ TRFA(fa′)(ap) ≠ ∅ ]`

```math
\mathrm{COV}_{(fa)(fa')(ap)} = \big[\,\mathrm{TRFA}_{(fa)(ap)} \cap \mathrm{TRFA}_{(fa')(ap)} \ne \varnothing\,\big]
```

**S34 [Def]** Measurement overlap.

`MOV(fa)(fa′)(ap) = [ PER(FMA(fa))(ap) ∩ PER(FMA(fa′))(ap) ≠ ∅ ]`

```math
\mathrm{MOV}_{(fa)(fa')(ap)} = \big[\,\mathrm{PER}_{\mathrm{FMA}_{(fa)}(ap)} \cap \mathrm{PER}_{\mathrm{FMA}_{(fa')}(ap)} \ne \varnothing\,\big]
```

**S35 [Derived, needs ⚠️ S29a]** Composition overlap implies measurement overlap. The reverse does not hold (Scenario 3).

`COV(fa)(fa′)(ap) = 1  ⇒  MOV(fa)(fa′)(ap) = 1`

```math
\mathrm{COV} = 1 \;\Rightarrow\; \mathrm{MOV} = 1
```

*Proof: a shared TR lies in both TRFA sets, and by S29a in both perimeters.*

**S36 [Derived]** Assets at different boundary points never overlap. This includes mobile TRs, because by S6 each TR is behind at most one boundary point per (ap).

`BPFA(fa) ≠ BPFA(fa′)  ⇒  MOV(fa)(fa′)(ap) = 0   (because PER ⊆ TR(bp)(ap) and S7)`

```math
\mathrm{BPFA}_{(fa)} \ne \mathrm{BPFA}_{(fa')} \;\Rightarrow\; \mathrm{MOV}_{(fa)(fa')(ap)} = 0
```

S37–S41 assume non-empty perimeters, which S29a and S10 guarantee for any Asset with a control group.

**S37 [Derived]** Two Point of Connection Assets at the same boundary point always overlap.

`TYPE(FMA(fa)) = TYPE(FMA(fa′)) = POC  ⇒  MOV = 1`

```math
\mathrm{TYPE}_{\mathrm{FMA}_{(fa)}} = \mathrm{TYPE}_{\mathrm{FMA}_{(fa')}} = \mathrm{POC} \;\Rightarrow\; \mathrm{MOV}_{(fa)(fa')(ap)} = 1
```

**S38 [Derived]** A Point of Connection Asset overlaps every other Asset at its boundary point.

`TYPE(FMA(fa)) = POC,  (fa′) ∈ FA(bp)(ap)  ⇒  MOV = 1`

```math
\mathrm{TYPE}_{\mathrm{FMA}_{(fa)}} = \mathrm{POC},\ (fa') \in \mathrm{FA}_{(bp)(ap)} \;\Rightarrow\; \mathrm{MOV}_{(fa)(fa')(ap)} = 1
```

**S39 [Derived, needs ⚠️ S19a]** Two Asset Level Assets on meters K and K′.

`MOV = 1  ⇔  K = K′  or  K ⊑ K′  or  K′ ⊑ K`

```math
\mathrm{MOV}_{(fa)(fa')(ap)} = 1 \iff K = K' \;\lor\; K \sqsubseteq K' \;\lor\; K' \sqsubseteq K
```

**⚠️ S40 [Derived – corrected; see F5]** Asset Level Asset on K against a Difference Asset (ma′).

> [!WARNING]
> **For review: corrected statement.** This replaces CAA statement 40 as written. Accepted for drafting on 2026-11-20 and needs CAA confirmation before use (see F5 and the review checklist).

`MOV = 0  ⇔  K ∈ KSUB(ma′)  or  K ⊑ K″ for some K″ ∈ KSUB(ma′)`

```math
\mathrm{MOV}_{(fa)(fa')(ap)} = 0 \iff \exists K'' \in \mathrm{KSUB}_{(ma')}:\ K = K'' \ \lor\ K \sqsubseteq K''
```

*As written, S40 says the Asset Level Asset "does overlap a Difference Asset that doesn't [subtract its meter]". That is false when K sits behind a meter that is subtracted.*

**S41 [Derived]** The same arrangement means the same perimeter, so the Assets overlap.

`FMA(fa) = FMA(fa′)  ⇒  MOV = 1`

```math
\mathrm{FMA}_{(fa)} = \mathrm{FMA}_{(fa')} \;\Rightarrow\; \mathrm{MOV}_{(fa)(fa')(ap)} = 1
```

**S42 [Derived]** Measurement overlap from meter topology alone, i.e. from TYPE, KB, KSUB and ⊑, with no REACH sets:

| (fa) \ (fa′) | POC | AL on K′ | DIFF (KSUB′) |
|---|---|---|---|
| **POC** | 1 | 1 | 1 |
| **AL on K** | 1 | 1 iff K = K′ or K ⊑ K′ or K′ ⊑ K | 0 iff K equals or is nested behind some meter in KSUB′, else 1 |
| **DIFF (KSUB)** | 1 | as above | 1 unless the subtracted meters together reach every TR (not decidable from topology; treat as 1) |

### 7. Compatibility, reconfiguration and consolidation

**S43 [Def]** A compatible set of Assets.

`a set A ⊆ FA(bp)(ap) is compatible  ⇔  MOV(fa)(fa′)(ap) = 0 for every (fa) ≠ (fa′) in A`

```math
A \text{ compatible} \iff \forall (fa) \ne (fa') \in A:\ \mathrm{MOV}_{(fa)(fa')(ap)} = 0
```

**S44 [Rule]** Compatibility is assessed across every Asset at the boundary point, whatever sub-market each is registered in. Hence the per-Asset form used in S63–S65:

`COMP(fa)(ap) = [ Σ(fa′)∈FA(BPFA(fa))(ap), (fa′)≠(fa) MOV(fa)(fa′)(ap) = 0 ]`

```math
\mathrm{COMP}_{(fa)(ap)} = \Big[\sum_{(fa') \in \mathrm{FA}_{\mathrm{BPFA}_{(fa)}(ap)},\ (fa') \ne (fa)} \mathrm{MOV}_{(fa)(fa')(ap)} = 0\Big]
```

**S45 [Def]** Reconfiguration replaces FMA(fa), or adjusts FCG(fa), giving (fa)\* with:

`MOV((fa)*)(fa′)(ap) = 0`

```math
(fa) \to (fa)^{*}: \quad \mathrm{MOV}_{(fa)^{*}(fa')(ap)} = 0
```

**S46 [Def]** Reconcilable. Let MTR⁺(bp) be the existing meters plus the meters that could be added at (bp).

`REC(fa)(fa′)(ap) = 1  ⇔  there exist valid (ma*), (ma′*) over MTR⁺(bp) with:`
`TRFA(fa) ⊆ PER(ma*),  TRFA(fa′) ⊆ PER(ma′*),  PER(ma*) ∩ PER(ma′*) = ∅,  and S26 respected`

```math
\begin{aligned}
&\mathrm{REC}_{(fa)(fa')(ap)} = 1 \iff \exists\, (ma^{*}), (ma'^{*}) \text{ over } \mathrm{MTR}^{+}_{(bp)} \text{ such that} \\
&\qquad \mathrm{TRFA}_{(fa)(ap)} \subseteq \mathrm{PER}_{(ma^{*})(ap)}, \quad \mathrm{TRFA}_{(fa')(ap)} \subseteq \mathrm{PER}_{(ma'^{*})(ap)}, \\
&\qquad \mathrm{PER}_{(ma^{*})(ap)} \cap \mathrm{PER}_{(ma'^{*})(ap)} = \varnothing
\end{aligned}
```

**S47 [Derived]** Composition overlap is never reconcilable.

`COV(fa)(fa′)(ap) = 1  ⇒  REC(fa)(fa′)(ap) = 0`

```math
\mathrm{COV} = 1 \;\Rightarrow\; \mathrm{REC} = 0
```

*Proof: a shared TR would have to lie in two disjoint perimeters.*

**S48 [Derived]** With measurement overlap only, the Assets are reconcilable exactly when some meters in MTR⁺(bp) separate their TRs (S46 with COV = 0).

`COV = 0,  MOV = 1:   REC = 1  ⇔  the meters in MTR⁺(bp) can separate TRFA(fa) from TRFA(fa′)`

```math
\begin{aligned}
&\mathrm{COV}_{(fa)(fa')(ap)} = 0,\ \ \mathrm{MOV}_{(fa)(fa')(ap)} = 1: \\
&\qquad \mathrm{REC}_{(fa)(fa')(ap)} = 1 \iff \text{some meters in } \mathrm{MTR}^{+}_{(bp)} \\
&\qquad\qquad \text{separate } \mathrm{TRFA}_{(fa)(ap)} \text{ from } \mathrm{TRFA}_{(fa')(ap)}
\end{aligned}
```

**S49 [Def]** Irreconcilable.

`IRR(fa)(fa′)(ap) = MOV(fa)(fa′)(ap) * (1 − REC(fa)(fa′)(ap))`

```math
\mathrm{IRR}_{(fa)(fa')(ap)} = \mathrm{MOV}_{(fa)(fa')(ap)} \cdot \big(1 - \mathrm{REC}_{(fa)(fa')(ap)}\big)
```

**S50 [Def]** Consolidation of an irreconcilable set A.

`A → (fa)c  with  TRFA((fa)c)(ap) = ∪(fa)∈A TRFA(fa)(ap)  and  MEAS((fa)c)(ap) = 1`

```math
A \to (fa)_c: \quad \mathrm{TRFA}_{(fa)_c(ap)} = \bigcup_{(fa) \in A} \mathrm{TRFA}_{(fa)(ap)}
```

**S51 [Open]** Load Controller of a consolidated Asset.

**S51-A** – the combined group gets one agreed Load Controller, so it is again a control group under S10:

`there exists p with LC(tr)(ap) = p for every (tr) ∈ TRFA((fa)c)(ap)`

```math
\exists p:\ \forall (tr) \in \mathrm{TRFA}_{(fa)_c(ap)}:\ \mathrm{LC}_{(tr)(ap)} = p
```

**S51-B** – an Asset may hold several control groups. S27 and S28 are generalised:

`FCG(fa) ⊆ CG(bp)(ap)  (a set of groups);   TRFA(fa)(ap) = ∪(cg)∈FCG(fa) (cg)`

```math
\mathrm{FCG}_{(fa)} \subseteq \mathrm{CG}_{(bp)(ap)}, \qquad \mathrm{TRFA}_{(fa)(ap)} = \bigcup_{(cg) \in \mathrm{FCG}_{(fa)}} (cg)
```

### 8. Claims, authority and delegation

**S52 [Def]** A registration (claim).

`(cl) ↦ ( FSPCL(cl), FACL(cl), SMCL(cl), APCL(cl) )`

```math
(cl) \mapsto \big(\mathrm{FSPCL}_{(cl)},\ \mathrm{FACL}_{(cl)},\ \mathrm{SMCL}_{(cl)},\ \mathrm{APCL}_{(cl)}\big)
```

**S53 [Rule]** Exactly one Asset and one sub-market. This holds by construction, because FACL and SMCL are single-valued.

**S54 [Rule]** A registration is valid only with authority over every TR of the Asset.

`VAL(cl) = 1  ⇒  AUTH FSPCL(cl)(tr)SMCL(cl)(ap) = 1   for every (ap) ∈ APCL(cl), (tr) ∈ TRFA(FACL(cl))(ap)`

where

`AUTH p(tr)(sm)(ap) = [ there exists (cc) with HOLDCC(cc) = p, (tr) ∈ TRCC(cc), (sm) ∈ SMCC(cc), (ap) ∈ APCC(cc) ]`
`                   or [ there exists (dg) with SECDG(dg) = p, SMDG(dg) = (sm), (ap) ∈ APDG(dg), (tr) ∈ TRCC(CCDG(dg)) ]`

```math
\begin{aligned}
\mathrm{AUTH}_{p(tr)(sm)(ap)} = {} & \big[\exists (cc):\ \mathrm{HOLDCC}_{(cc)} = p,\ (tr) \in \mathrm{TRCC}_{(cc)}, \\
& \qquad (sm) \in \mathrm{SMCC}_{(cc)},\ (ap) \in \mathrm{APCC}_{(cc)}\big] \\
\lor\ & \big[\exists (dg):\ \mathrm{SECDG}_{(dg)} = p,\ \mathrm{SMDG}_{(dg)} = (sm), \\
& \qquad (ap) \in \mathrm{APDG}_{(dg)},\ (tr) \in \mathrm{TRCC}_{\mathrm{CCDG}_{(dg)}}\big]
\end{aligned}
```

*SMCC(cc), the sub-markets a contract covers, is not in the statements. It is added because S56-1a needs it (F11).*

**S55 [Rule]** A customer contract is granted by the customer at the boundary point and covers TRs there. It is in force only while that customer is the customer at the boundary point.

`CUSCC(cc) = CUSBP(BPCC(cc))(ap)  and  TRCC(cc) ⊆ TR(BPCC(cc))(ap)   for every (ap) ∈ APCC(cc)`

```math
\begin{aligned}
(ap) \in \mathrm{APCC}_{(cc)} \;\Rightarrow\; & \mathrm{CUSCC}_{(cc)} = \mathrm{CUSBP}_{\mathrm{BPCC}_{(cc)}(ap)} \\
& \mathrm{TRCC}_{(cc)} \subseteq \mathrm{TR}_{\mathrm{BPCC}_{(cc)}(ap)}
\end{aligned}
```

**S56 [Open]** How far contract exclusivity reaches. Let `NCC(tr)(sm)(ap) = Σ(cc) [ (tr) ∈ TRCC(cc), (sm) ∈ SMCC(cc), (ap) ∈ APCC(cc) ]`.

**S56-0a** – no limit.

**S56-1a** – at most one contract per TR per sub-market:

`NCC(tr)(sm)(ap) ≤ 1`

```math
\mathrm{NCC}_{(tr)(sm)(ap)} \le 1
```

**S56-1b / S56-2** – at most one contract per TR across all in-scope sub-markets:

`Σ(cc) [ (tr) ∈ TRCC(cc), (ap) ∈ APCC(cc) ] ≤ 1`

```math
\sum_{(cc)} \big[(tr) \in \mathrm{TRCC}_{(cc)},\ (ap) \in \mathrm{APCC}_{(cc)}\big] \le 1
```

**S57 [Def]** Delegation from the Primary to a Secondary, for one sub-market. The contract stays with the Primary.

`(dg) ↦ ( CCDG(dg), SECDG(dg), SMDG(dg), APDG(dg) );  the Primary is HOLDCC(CCDG(dg));  SECDG(dg) ≠ HOLDCC(CCDG(dg))`

```math
\begin{aligned}
&(dg) \mapsto \big(\mathrm{CCDG}_{(dg)},\ \mathrm{SECDG}_{(dg)},\ \mathrm{SMDG}_{(dg)},\ \mathrm{APDG}_{(dg)}\big) \\
&\mathrm{SECDG}_{(dg)} \ne \mathrm{HOLDCC}_{\mathrm{CCDG}_{(dg)}}
\end{aligned}
```

**S58 [Rule]** A delegation ends when its contract ends.

`APDG(dg) ⊆ APCC(CCDG(dg))`

```math
\mathrm{APDG}_{(dg)} \subseteq \mathrm{APCC}_{\mathrm{CCDG}_{(dg)}}
```

**S59 [Derived from S55 and S58]** A change of customer ends the contracts at that boundary point, and with them every delegation.

`CUSBP(bp)(ap) ≠ CUSCC(cc)  ⇒  (ap) ∉ APCC(cc)  ⇒  (ap) ∉ APDG(dg) for every (dg) with CCDG(dg) = (cc)`

```math
\mathrm{CUSBP}_{(bp)(ap)} \ne \mathrm{CUSCC}_{(cc)} \;\Rightarrow\; (ap) \notin \mathrm{APCC}_{(cc)} \;\Rightarrow\; (ap) \notin \mathrm{APDG}_{(dg)}
```

### 9. Competing claims, assignment and allocation

**S60 [Def]** Two registrations compete when they name the same Asset and cannot both be allocated under the scenario's rules. CMP(cl)(cl′) is defined by S61 and S62.

**S61 [Rule]** Different FSPs, same Asset, same sub-market, overlapping periods: they compete.

`FACL(cl) = FACL(cl′),  FSPCL(cl) ≠ FSPCL(cl′),  SMCL(cl) = SMCL(cl′),  APCL(cl) ∩ APCL(cl′) ≠ ∅   ⇒  CMP(cl)(cl′) = 1`

```math
\begin{aligned}
&\mathrm{FACL}_{(cl)} = \mathrm{FACL}_{(cl')},\quad \mathrm{FSPCL}_{(cl)} \ne \mathrm{FSPCL}_{(cl')}, \\
&\mathrm{SMCL}_{(cl)} = \mathrm{SMCL}_{(cl')},\quad \mathrm{APCL}_{(cl)} \cap \mathrm{APCL}_{(cl')} \ne \varnothing \\
&\qquad \Rightarrow\; \mathrm{CMP}_{(cl)(cl')} = 1
\end{aligned}
```

**S62 [Open]** As S61, but with SMCL(cl) ≠ SMCL(cl′). Write p = FSPCL(cl), p′ = FSPCL(cl′), (fa) = FACL(cl), and PRI(fa)(ap) for the holder(s) of the contracts covering TRFA(fa).

**S62-2 and S62-0b** – they always compete:

`CMP(cl)(cl′) = 1`

**S62-1a** – they compete unless both FSPs are in the coordinating group:

`CMP(cl)(cl′) = 1 − [ p ∈ COORD(fa)(ap) ] * [ p′ ∈ COORD(fa)(ap) ]`

```math
\mathrm{CMP}_{(cl)(cl')} = 1 - \big[p \in \mathrm{COORD}_{(fa)(ap)}\big]\cdot\big[p' \in \mathrm{COORD}_{(fa)(ap)}\big]
```

**S62-1b** – they compete if either FSP is neither the Primary nor delegated by it. Let DEL p(fa)(sm)(ap) = [p ∈ PRI(fa)(ap)] or [p holds a delegation for (sm) from the Primary].

`CMP(cl)(cl′) = 1 − DEL p(fa)SMCL(cl)(ap) * DEL p′(fa)SMCL(cl′)(ap)`

```math
\mathrm{CMP}_{(cl)(cl')} = 1 - \mathrm{DEL}_{p(fa)\,\mathrm{SMCL}_{(cl)}(ap)} \cdot \mathrm{DEL}_{p'(fa)\,\mathrm{SMCL}_{(cl')}(ap)}
```

**S62-0a** – each sub-market decides:

`CMP(cl)(cl′) = RULE(SMCL(cl))(cl)(cl′)`, where RULE(sm) is supplied by sub-market (sm).

**S63 [Def]** Assignment: for a compatible Asset with competing registrations, choose who prevails.

`COMP(fa)(ap) = 1  ⇒  ASG(fa)(ap) ∈ { FSPCL(cl) : FACL(cl) = (fa) } ∪ { FSP groups } ∪ PRI(fa)(ap)`

```math
\begin{aligned}
&\mathrm{COMP}_{(fa)(ap)} = 1 \;\Rightarrow \\
&\qquad \mathrm{ASG}_{(fa)(ap)} \in \{\mathrm{FSPCL}_{(cl)} : \mathrm{FACL}_{(cl)} = (fa)\} \\
&\qquad\qquad \cup\ \{\text{FSP groups}\} \ \cup\ \mathrm{PRI}_{(fa)(ap)}
\end{aligned}
```

**S64 [Def]** Allocation. The FSP group may be a single FSP. APAL is the set of activation periods inside the allocation's spot-time interval.

`(al) ↦ ( FAAL(al), GRPAL(al) ⊆ PTY, TSAL(al), TEAL(al) );   APAL(al) = { (ap) : (ap) ⊆ [TSAL(al), TEAL(al)) }`

```math
\begin{aligned}
&(al) \mapsto \big(\mathrm{FAAL}_{(al)},\ \mathrm{GRPAL}_{(al)} \subseteq \mathrm{PTY},\ \mathrm{TSAL}_{(al)},\ \mathrm{TEAL}_{(al)}\big) \\
&\mathrm{APAL}_{(al)} = \{(ap) : (ap) \subseteq [\mathrm{TSAL}_{(al)}, \mathrm{TEAL}_{(al)})\}
\end{aligned}
```

**S65 [Rule]** Only compatible Assets can be allocated.

`COMP(FAAL(al))(ap) = 1   for every (ap) ∈ APAL(al)`

```math
\forall (ap) \in \mathrm{APAL}_{(al)}:\ \mathrm{COMP}_{\mathrm{FAAL}_{(al)}(ap)} = 1
```

**S66 [Rule]** At most one allocation per Asset per period.

`Σ(al) [ FAAL(al) = (fa), (ap) ∈ APAL(al) ] ≤ 1`

```math
\sum_{(al)} \big[\mathrm{FAAL}_{(al)} = (fa),\ (ap) \in \mathrm{APAL}_{(al)}\big] \le 1
```

**S67 [Rule]** At most one FSP enters an Asset into a sub-market in a period. With IENT defined from Units (S70), this follows from S71.

`Σp IENT(fa)(sm)p(ap) ≤ 1`

```math
\sum_{p} \mathrm{IENT}_{(fa)(sm)p(ap)} \le 1
```

**S68 [Def]** Re-allocation at spot time τ: the new allocation starts at the moment the old one ends, with no gap and no overlap.

`TEAL(al) := τ;   TSAL(al′) = τ;   FAAL(al′) = FAAL(al)`

```math
\mathrm{TEAL}_{(al)} := \tau = \mathrm{TSAL}_{(al')}, \qquad \mathrm{FAAL}_{(al')} = \mathrm{FAAL}_{(al)}
```

### 10. Units

**S69 [Def]** A Unit, and the entry indicator it defines. In the BM and wholesale sub-markets, (un) ↔ i2.

`(un) ↦ ( FSPUN(un), SMUN(un), FAUN(un)(ap) );`
`IENT(fa)(sm)p(ap) = [ there exists (un) with FSPUN(un) = p, SMUN(un) = (sm), (fa) ∈ FAUN(un)(ap) ]`

```math
\begin{aligned}
\mathrm{IENT}_{(fa)(sm)p(ap)} = \big[\exists (un):\ & \mathrm{FSPUN}_{(un)} = p,\ \mathrm{SMUN}_{(un)} = (sm), \\
& (fa) \in \mathrm{FAUN}_{(un)(ap)}\big]
\end{aligned}
```

**S70 [Rule]** An Asset may be in a Unit only under a valid registration, and only if it is allocated to the FSP, or (scenario 1b) delegated to it.

`(fa) ∈ FAUN(un)(ap)  ⇒  there exists (cl) with FSPCL(cl) = FSPUN(un), FACL(cl) = (fa), SMCL(cl) = SMUN(un), (ap) ∈ APCL(cl), VAL(cl) = 1`
`   and [ there exists (al) with FAAL(al) = (fa), FSPUN(un) ∈ GRPAL(al), (ap) ∈ APAL(al) ]`
`   or [ SCN = 1b and there exists (dg) with SECDG(dg) = FSPUN(un), SMDG(dg) = SMUN(un), (ap) ∈ APDG(dg) ]`

```math
\begin{aligned}
& (fa) \in \mathrm{FAUN}_{(un)(ap)} \;\Rightarrow \\
& \exists (cl):\ \mathrm{VAL}_{(cl)} = 1,\ \mathrm{FSPCL}_{(cl)} = \mathrm{FSPUN}_{(un)}, \\
& \qquad \mathrm{FACL}_{(cl)} = (fa),\ \mathrm{SMCL}_{(cl)} = \mathrm{SMUN}_{(un)},\ (ap) \in \mathrm{APCL}_{(cl)} \\
\text{and}\quad & \Big(\exists (al):\ \mathrm{FAAL}_{(al)} = (fa),\ \mathrm{FSPUN}_{(un)} \in \mathrm{GRPAL}_{(al)}, \\
& \qquad (ap) \in \mathrm{APAL}_{(al)} \\
& \quad \lor\ \big[\mathrm{SCN} = \text{1b} \ \land\ \exists (dg):\ \mathrm{SECDG}_{(dg)} = \mathrm{FSPUN}_{(un)}, \\
& \qquad\quad \mathrm{SMDG}_{(dg)} = \mathrm{SMUN}_{(un)},\ (ap) \in \mathrm{APDG}_{(dg)}\big]\Big)
\end{aligned}
```

**S71 [Rule]** An Asset is in at most one Unit per sub-market per period (cf. S10.1A.3).

`Σ(un):SMUN(un)=(sm) [ (fa) ∈ FAUN(un)(ap) ] ≤ 1`

```math
\sum_{(un):\ \mathrm{SMUN}_{(un)} = (sm)} \big[(fa) \in \mathrm{FAUN}_{(un)(ap)}\big] \le 1
```

### 11. The objective as a property

**S72 [Derived] No duplication (Objective 1).** For every sub-market, activation period and TR:

`Σ(fa) [ Σp IENT(fa)(sm)p(ap) = 1 ] * [ (tr) ∈ PER(FMA(fa))(ap) ] ≤ 1`

```math
\begin{aligned}
&\sum_{(fa)} \Big[\sum_{p} \mathrm{IENT}_{(fa)(sm)p(ap)} = 1\Big] \cdot \big[(tr) \in \mathrm{PER}_{\mathrm{FMA}_{(fa)}(ap)}\big] \le 1 \\
&\qquad \forall (sm), (ap), (tr)
\end{aligned}
```

The volume form follows from V3. The total volume entered into (sm) counts each TR's flow at most once:

```math
\sum_{(fa):\ \text{entered in }(sm)} \mathrm{QFA}_{(fa)j} = \sum_{(tr) \in \bigcup \mathrm{PER}} \mathrm{QTR}_{(tr)j} \qquad j \in (ap)
```

*Proof outline:*
1. An entered Asset is in a Unit (S69). By S70 it is then allocated, and by S65 it is compatible.
2. Two such Assets at the same boundary point therefore have MOV = 0 (S43, S44). At different boundary points their perimeters are disjoint (S36).
3. The same Asset is not entered twice into one sub-market (S67, S71).

**Gaps:**
- the delegated route in S70 under 1b bypasses S65 (F8);
- under S32-Yes, S32-Yes(i) is needed (F7).

---

## Part C – Issues the notation exposed

| # | Statements | Issue | Proposed handling in this draft | Status |
|---|---|---|---|---|
| F1 | 5, 6 | "Exactly one" conflicts with a mobile TR that is in transit. | Restated as "at most one" (agreed). S5 becomes a special case of S6. | Agreed |
| F2 | 27, 31 | S27 pairs a *control group* with an arrangement, but a residual Asset pairs the *residual group*, which has no Load Controller. | Read S27 as FCG(fa) ∈ CG(bp)(ap) ∪ {RG(bp)(ap)}. Confirm. | ⚠️ For review |
| F3 | 29, 35 | S35 ("composition overlap ⇒ measurement overlap") holds only if both Assets are measurable. Nothing requires an Asset to be measurable. | Added S29a "every Asset is measurable". Confirm, or restrict S35. | ⚠️ For review |
| F4 | 18, 19, 39, 42 | S39 and the topology test in S42 need asset meters to be either nested or disjoint. The statements only say each reach is a subset. | Added S19a (asset meters form a tree). | ⚠️ For review |
| F5 | 40 | False when the Asset Level meter K sits behind a subtracted meter: there is no overlap even though K itself is not subtracted. | S40 corrected to "no overlap iff K equals or is nested behind a subtracted meter". | ⚠️ For review |
| F6 | 24, V1 | If two subtracted meters are nested, the Difference volume subtracts the inner TRs twice, although the perimeter (a set difference) does not. | Added S24a: subtracted meters must be disjoint. | ⚠️ For review |
| F7 | 32, 43, 44, 47, 72 | Under **S32-Yes**, two Assets of one control group share TRs, so they always composition-overlap. With S44 they can never both be compatible, and with S47 they are irreconcilable. | S32-Yes needs compatibility assessed between control groups (S32-Yes(ii)), plus at most one Asset per group per sub-market (S32-Yes(i)). | ⚠️ Decision needed |
| F8 | 65, 70, 72 | Under 1b, S70 lets a *delegated* Asset enter a Unit without an allocation. S65 (compatibility) therefore does not cover it, and the S72 proof via 43, 65 and 67 has a gap. | Either require COMP for delegated entry too, or route delegations through allocation. Decision needed. | ⚠️ Decision needed |
| F9 | 56, 62 | Scenario 0b appears in S62 but not in S56. | Need the 0b exclusivity rule. | ⚠️ Decision needed |
| F10 | 62 | The "coordinating group" (1a) is not defined anywhere. | Introduced COORD(fa)(ap). Need its definition: per Asset, per boundary point, or per Primary? | ⚠️ Decision needed |
| F11 | 54–56 | Whether a contract covers named sub-markets is not stated, but S56-1a counts contracts per sub-market. | Added SMCC(cc). Confirm. | ⚠️ For review |
| F12 | 64, 68 | Allocation is in spot time, but every other rule is per activation period. A re-allocation inside an activation period would split it. | Assumed re-allocation times fall on activation-period boundaries. Confirm. | ⚠️ For review |
| F13 | 1, 3, 17, 22 | A boundary point may have import and export MSIDs, but S22 says "the boundary meter". | One logical boundary meter per boundary point: K = MSID Pair for boundary meters, AMSID Pair for asset meters. This uses K at pair level, not single-MSID level as in Table X-4. | ⚠️ For review |
| F14 | 30, 54 | An inclusively measured Asset's volume includes TRs outside the Asset. S54 only requires authority over the Asset's own TRs. | Formalised as written. Flagging in case authority should cover the perimeter. | ⚠️ For review |
| F15 | 62-1b | "Lacks a delegation from the Primary": the Primary itself holds no delegation. | Treated the Primary as authorised (the DEL indicator). Confirm. | ⚠️ For review |
