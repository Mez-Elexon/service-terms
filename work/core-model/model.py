"""Single source for the Flexibility Core Model: statements, notation, core expressions and findings.

build.py turns this into the Markdown documentation and the HTML visual. Edit here, then rebuild.
LaTeX is written for MathJax (GitHub renders ```math blocks with MathJax).
"""

VERSION = "Draft v0.3"
DATE = "2026-11-20"

SECTIONS = {
    1: "Basic sets",
    2: "Boundary points and metering identities",
    3: "Site Configuration and the metering tree",
    4: "TRs and control",
    5: "Reach and measurement arrangements",
    6: "Assets",
    7: "Overlap, compatibility and consolidation",
    8: "Authority and delegation",
    9: "Registration, allocation and participation",
    10: "Differencing in the BSC",
    11: "Units",
    12: "The objectives as properties",
}

# Layer of each section, used for colour coding in the HTML.
LAYER = {1: "base", 2: "measure", 3: "measure", 4: "control", 5: "measure", 6: "asset", 7: "asset",
         8: "who", 9: "who", 10: "measure", 11: "who", 12: "objective"}

# ---------------------------------------------------------------------------------------------
# The statements, as supplied (consolidated CAA relationships + BSC Site Configuration + control layer).
# (number, tag, section, text)
# ---------------------------------------------------------------------------------------------
STATEMENTS = [
    (1, "Def", 1, "There is a set of Boundary Points: points of connection to the network."),
    (2, "Def", 1, "There is a set of Metering Systems (MSIDs), which identify boundary metering."),
    (3, "Def", 1, "There is a set of Asset Metering Systems (AMSIDs), which identify asset metering."),
    (4, "Def", 1, "There is a set of Asset Meters: the physical devices."),
    (5, "Def", 1, "There is a set of Technical Resources (TRs)."),
    (6, "Def", 1, "There is a set of parties. A party can hold one or more roles: Load Controller, FSP, CFPC holder (Primary), Secondary FSP, Supplier, or BSC Party operating BM Units."),
    (7, "Def", 1, "There are sets of customers, sub-markets and periods. The Balancing Mechanism and the wholesale market are sub-markets."),
    (8, "Rule", 2, "Each MSID belongs to exactly one Boundary Point."),
    (9, "Def", 2, "An MSID Pair is a BSC process construct grouping a Boundary Point’s import MSID with its export MSID, if there is one."),
    (10, "Def", 2, "An AMSID Pair groups an import AMSID with its export AMSID, if there is one, measuring the same equipment."),
    (11, "Rule", 2, "Each AMSID is served by exactly one Asset Meter at any time, recorded as an Asset Meter Allocation."),
    (12, "Derived", 2, "Replacing a physical Asset Meter changes its Asset Meter Allocation, not the AMSID."),
    (13, "Def", 3, "A Site Configuration is an effective-dated record with an immutable ID, stating three things: which MSIDs at one Boundary Point are related; which AMSIDs are related to them; how those AMSIDs are nested."),
    (14, "Rule", 3, "Each Boundary Point has at most one effective Site Configuration at any time."),
    (15, "Rule", 3, "Each AMSID belongs to exactly one effective Site Configuration at any time."),
    (16, "Rule", 3, "Any change to the MSIDs, the AMSIDs or their nesting creates a new Site Configuration with a new ID, replacing the old one from its effective date."),
    (17, "Def", 3, "The metering tree of a Site Configuration has the Boundary Point’s MSIDs at its root. Each AMSID has exactly one parent: either the boundary, or another AMSID it sits behind."),
    (18, "Def", 3, "A Site groups one or more Site Configurations."),
    (19, "Rule", 3, "Changing which Site a Site Configuration belongs to doesn’t create a new Site Configuration."),
    (20, "Rule", 4, "Each TR is located behind exactly one Boundary Point at any time."),
    (21, "Rule", 4, "A mobile TR, such as an EV, may be behind different Boundary Points at different times, but behind at most one in any period."),
    (22, "Def", 4, "A control assignment links a TR to the party acting as its Load Controller for a period."),
    (23, "Rule", 4, "Each actively controlled TR has exactly one Load Controller at any time."),
    (24, "Def", 4, "A TR control group is a non-empty set of TRs, all behind the same Boundary Point, which share one Load Controller and can be instructed by it as one."),
    (25, "Rule", 4, "Each actively controlled TR belongs to exactly one control group at any time."),
    (26, "Def", 4, "The residual group of a Boundary Point is every TR behind it that isn’t in a control group. That includes appliances used through customer behaviour, which have no Load Controller."),
    (27, "Derived", 4, "The control groups and the residual group at a Boundary Point together cover every TR there, with no TR in two of them."),
    (28, "Rule", 4, "An FSP may offer flexibility from a control group only if it is the group’s Load Controller or has a control agreement with it."),
    (29, "Rule", 4, "Where several FSPs offer the same control group (options 1a and 1b), all their instructions reach it through its one Load Controller, which applies an agreed order of precedence."),
    (30, "Rule", 4, "Statements 28 and 29 don’t apply to a residual group. An FSP influences a residual group through the customer, not through a Load Controller."),
    (31, "Def", 5, "The reach of a metering identity is the set of TRs whose energy flow it records."),
    (32, "Rule", 5, "The reach of a Boundary Point’s MSIDs is every TR behind that Boundary Point."),
    (33, "Rule", 5, "The reach of an AMSID is contained within the reach of its parent in the metering tree."),
    (34, "Rule", 5, "Two AMSIDs in the same metering tree, neither of which sits behind the other, have reaches with no TR in common."),
    (35, "Def", 5, "A measurement arrangement lies within one Site Configuration and has one of three types: Boundary: the MSID Pair alone; Asset: one AMSID Pair; Residual: the MSID Pair, net of one or more AMSID Pairs (differencing)."),
    (36, "Def", 5, "The measurement perimeter of an arrangement depends on its type: Boundary: the reach of the MSIDs; Asset: the reach of the AMSID; Residual: the reach of the MSIDs, minus the combined reach of the AMSIDs it subtracts."),
    (37, "Rule", 5, "The AMSIDs a Residual arrangement subtracts must have reaches with no TR in common, so that no nested meter is subtracted twice."),
    (38, "Rule", 5, "A Residual arrangement can exist only if at least one Asset arrangement in the same Site Configuration is in use."),
    (39, "Rule", 5, "Residual arrangements are accepted only in sub-markets that accept differencing. Today that’s the Balancing Mechanism and the wholesale market, for AMVLPs under P375."),
    (40, "Def", 6, "A Flexibility Asset is one control group, or the residual group, measured through one arrangement in the same Site Configuration."),
    (41, "Rule", 6, "An Asset is measurable only if its perimeter contains every TR in its group."),
    (42, "Def", 6, "An Asset is exactly measured if its perimeter equals its group."),
    (43, "Def", 6, "An Asset is inclusively measured if its perimeter also contains TRs outside its group."),
    (44, "Derived", 6, "An inclusively measured Asset is exposed to the compensation effect: TRs inside its perimeter that it doesn’t control can counteract its delivery."),
    (45, "Def", 6, "Sibling Assets are Assets with the same control group but different arrangements."),
    (46, "Rule", 6, "Sibling Assets are always allocated to the same FSP or FSP group."),
    (47, "Rule", 6, "Sibling Assets are never entered into the same sub-market in the same period."),
    (48, "Def", 6, "A residual Asset is the residual group measured through a Residual arrangement."),
    (49, "Derived", 6, "The control group, not the Asset, is the unique object of flexibility. Assets are its views through different measurements."),
    (50, "Def", 7, "Two Assets in the same Site Configuration, belonging to different groups, overlap if their perimeters have at least one TR in common."),
    (51, "Derived", 7, "Different groups never share a TR (statement 25), so any overlap between them is an overlap in measurement, not in composition."),
    (52, "Def", 7, "An identity conflict exists when two declared control groups turn out, or are suspected, to contain the same TR."),
    (53, "Rule", 7, "Identity conflicts are resolved, by correcting or merging the declared groups, before compatibility is assessed."),
    (54, "Derived", 7, "A Boundary arrangement overlaps every Asset of another group in the same Site Configuration."),
    (55, "Derived", 7, "Two Asset arrangements overlap if, and only if, one AMSID sits behind the other."),
    (56, "Derived", 7, "An Asset arrangement and a Residual arrangement don’t overlap if the Residual subtracts that AMSID or one of its ancestors in the metering tree. Otherwise they overlap."),
    (57, "Derived", 7, "Two Assets with the same arrangement always overlap."),
    (58, "Derived", 7, "Apart from identity conflicts, overlap can be determined from the metering tree alone, without knowing TR identities."),
    (59, "Def", 7, "The Assets in a Site Configuration are compatible if no two Assets of different groups that are in use at the same time overlap."),
    (60, "Rule", 7, "Compatibility is assessed across every Asset in the Site Configuration, whichever sub-markets they’re used in."),
    (61, "Def", 7, "Reconfiguration removes an overlap by changing an Asset’s arrangement, which can mean adding metering through a new Site Configuration, or by regrouping its TRs."),
    (62, "Def", 7, "A set of overlapping Assets is reconcilable if some choice of arrangements, using existing or added metering, removes every overlap between different groups."),
    (63, "Def", 7, "Otherwise the set is irreconcilable."),
    (64, "Derived", 7, "Two groups whose TRs can only be measured at the boundary are irreconcilable unless metering is added."),
    (65, "Def", 7, "Consolidation merges irreconcilable groups into one control group, measured as one Asset."),
    (66, "Rule", 7, "A consolidated group must have a single Load Controller, agreed between the parties."),
    (67, "Open", 7, "The alternative to statement 66: allow an Asset to hold several control groups with different Load Controllers, coordinated at site level. That is currently future scope."),
    (68, "Def", 8, "A customer flexibility purchase contract (CFPC) is granted by the customer at a Boundary Point to a holder. It covers a stated set of TRs for a period."),
    (69, "Rule", 8, "A CFPC covers either every TR in a control group or none of them."),
    (70, "Open", 8, "How far a CFPC’s exclusivity reaches: 0a: no limit; 1a: at most one CFPC per TR per sub-market; 1b and 2: at most one per TR across all in-scope sub-markets."),
    (71, "Def", 8, "A delegation is a grant from a CFPC holder (the Primary) to a Secondary FSP, for one sub-market and a period. It doesn’t transfer the CFPC."),
    (72, "Rule", 8, "A delegation ends when the CFPC it derives from ends."),
    (73, "Rule", 8, "A change of customer at a Boundary Point ends every CFPC for the TRs behind it, and every delegation derived from them."),
    (74, "Def", 9, "A registration (claim) is an FSP’s record that it may offer a named Asset in a named sub-market for a period."),
    (75, "Rule", 9, "A registration is valid only if both of these hold for that sub-market and period: the FSP holds a CFPC or a delegation covering the Asset’s TRs; statement 28 is satisfied."),
    (76, "Rule", 9, "Registrations by different FSPs for the same Asset, or for sibling Assets, in the same sub-market and period always compete."),
    (77, "Open", 9, "Whether registrations by different FSPs in different sub-markets compete: 2 and 0b: always; 1a: only if the FSPs aren’t in the coordinating group; 1b: only if one of the FSPs lacks a delegation from the Primary; 0a: decided by each sub-market."),
    (78, "Def", 9, "Assignment decides which FSP, FSP group or Primary prevails among competing registrations."),
    (79, "Def", 9, "An allocation links one control group, and with it all its sibling Assets, to an FSP or FSP group for a period."),
    (80, "Rule", 9, "Only control groups whose Assets are compatible can be allocated."),
    (81, "Rule", 9, "Each control group has at most one allocation at any time."),
    (82, "Def", 9, "Re-allocation replaces an allocation from a given time onwards, with no gap and no overlap between the old and the new."),
    (83, "Def", 9, "A participation is a sub-market’s own record that an FSP is using an Asset there. In the BSC it’s an MSID Pair Allocation or an AMSID Pair Allocation to a BM Unit; on other platforms, membership of a unit."),
    (84, "Rule", 9, "Every participation must trace back to the FSP’s allocation, or its delegation, for that Asset and sub-market."),
    (85, "Rule", 9, "In the BSC, an Asset arrangement participates through an AMSID Pair Allocation. Boundary and Residual arrangements participate through an MSID Pair Allocation."),
    (86, "Rule", 9, "An MSID Pair Allocation and an AMSID Pair Allocation in the same Site Configuration may be held by different parties."),
    (87, "Derived", 9, "Statement 86 is consistent with compatibility: an Asset arrangement and a Residual that subtracts it don’t overlap (statement 56)."),
    (88, "Rule", 10, "In BSC settlement, an MSID Pair participation is differenced in a period if, and only if, at least one AMSID Pair in the same Site Configuration has an active participation in that period."),
    (89, "Derived", 10, "The volume subtracted is the sum over the outermost participating AMSIDs: those with no participating ancestor. That avoids subtracting nested volume twice."),
    (90, "Rule", 10, "When differencing starts or stops because of another party’s AMSID participation, the MSID Pair participant is notified."),
    (91, "Derived", 10, "Differencing removes the overlap between Boundary and Asset arrangements within BSC settlement only."),
    (92, "Derived", 10, "Sub-markets that use the boundary without differencing keep that overlap, and FMAR flags it."),
    (93, "Def", 11, "A Unit belongs to one FSP and one sub-market. In the BSC that’s a Secondary BM Unit."),
    (94, "Rule", 11, "A Unit contains only Assets for which its FSP holds a valid participation."),
    (95, "Rule", 11, "An Asset is in at most one Unit per sub-market per period."),
    (96, "Derived", 12, "O1, avoided duplication: two conditions hold together. In any sub-market and period, no TR lies within the perimeters of two participating Assets from different groups. Sibling Assets never participate in the same sub-market in the same period."),
    (97, "Derived", 12, "O2, clear accountability: every participation traces to exactly one allocation; within an FSP group, each sub-market traces to exactly one FSP."),
    (98, "Derived", 12, "O3, fair and efficient switching: successive allocations of a control group follow on with no gap and no overlap."),
    (99, "Derived", 12, "O4, coordinated participation: every allocation, delegation and participation is recorded with effective dates and visible to the parties entitled to see it."),
]

CHOICES = [
    "Logical metering identities (MSID, AMSID) are the keys for measurement. Physical meters attach through Asset Meter Allocation, so replacing a meter changes nothing above it.",
    "The Site Configuration is the scope for measurement and compatibility. The Site is a grouping only.",
    "The TR control group is the unique object of flexibility. An Asset is that group seen through one measurement arrangement, so one group can have several sibling Assets.",
    "Differencing is derived in the BSC, but the residual Asset is still an explicit FMAR object.",
    "“Who” has two levels. Allocation is cross-market and held in FMAR. Participation is per sub-market. Every participation must trace back to an allocation.",
]

STILL_OPEN = [
    "Allocating at control-group level (statement 79) follows from the sibling rule. It needs confirming against CAA’s current wording, which allocates the Asset.",
    "A single Load Controller after consolidation (statements 66 and 67).",
    "Nesting in Site Configurations (statement 13). This is the question for the BSC team.",
    "CFPCs covering whole control groups (statement 69). It makes authority checkable, but confirm it fits customer contracts in practice.",
]

# ---------------------------------------------------------------------------------------------
# Notation register. (symbol LaTeX, reads as, BSC alignment)
# ---------------------------------------------------------------------------------------------
NOTATION = [
    # sets and elements
    (r"t,\ \tau,\ j", "spot time; a period; a Settlement Period", "t as Annex X-2 4.4; j as Tables X-1/X-4; j ∈ τ as j∈D in 1.2.1(b)"),
    (r"b \in \mathcal{B}", "a Boundary Point", "BSC Boundary Point"),
    (r"K \in \mathcal{K}^{M} \cup \mathcal{K}^{A}", "a metering identity: an MSID or an AMSID", "K, Table X-4 (SVA Metering System and/or Asset Metering System)"),
    (r"M_b", "the MSID Pair of Boundary Point b", "MSID Pair (S10.1)"),
    (r"A \in \mathcal{A}", "an AMSID Pair", "AMSID Pair (S10.1A)"),
    (r"m \in \mathcal{M}", "a physical Asset Meter", "Asset Meter (BSCP603)"),
    (r"c \in \mathcal{C}", "a Site Configuration", "new: proposed BSC Site Configuration"),
    (r"w \in \mathcal{W}", "a Site (a set of Site Configurations)", "new"),
    (r"r \in \mathcal{R}", "a Technical Resource (TR)", "new (CAA)"),
    (r"g \in \mathcal{G}_{b,t}", "a TR control group at b", "new (CAA)"),
    (r"R_{b,t}", "the residual group at b", "new"),
    (r"x \in \mathcal{X}_c", "a measurement arrangement in c", "new; Res(X) ≈ Asset Differencing, S10.1A.2(e)(ii)"),
    (r"a = (g, x)", "a Flexibility Asset: a group seen through an arrangement", "new (CAA)"),
    (r"p \in \mathcal{P}", "a party", "p, Table X-1"),
    (r"s \in \mathcal{S}", "a sub-market", "new; BM and wholesale (WM) are members"),
    (r"\varphi,\ \delta,\ \kappa,\ \lambda,\ \pi", "a CFPC, a delegation, a registration, an allocation, a participation", "new; π in the BSC is an MSID or AMSID Pair Allocation"),
    (r"u", "a Unit", "Secondary BM Unit i2 in the BSC (Table X-4)"),
    # functions and relations
    (r"I(e) = [\operatorname{from}(e), \operatorname{to}(e))", "the effective interval of a record e", "effective from / to dates"),
    (r"\operatorname{live}_t(e) \iff t \in I(e)", "record e is in force at t", "new"),
    (r"\operatorname{loc}(r,t)", "the Boundary Point that TR r is behind at t", "new"),
    (r"\operatorname{LC}(r,t)", "the Load Controller of r at t", "new"),
    (r"\operatorname{par}_c(A)", "the parent of A in the metering tree of c", "new"),
    (r"A \sqsubset A'", "A sits behind A' (A' is an ancestor of A)", "new; ⊑ also allows A = A'"),
    (r"\operatorname{reach}_t(K)", "the TRs whose flow K records", "new"),
    (r"\operatorname{per}_t(x)", "the measurement perimeter of arrangement x", "new"),
    (r"E_t(a)", "the exposure set: TRs in the perimeter but outside the group", "new"),
    (r"[P]", "1 if statement P is true, else 0", "indicator, as BSC 1/0 indicators"),
    (r"QM_{Kj}", "net metered volume of identity or pair K in Settlement Period j (MWh, export positive)", "BSC run-together form, 2.4.1 sign convention"),
]

# ---------------------------------------------------------------------------------------------
# Core expressions. kind ∈ Def, Rule, Derived, Open. 'core' marks the ones on the one-page summary.
# ---------------------------------------------------------------------------------------------
E = []
def ex(id, sec, kind, name, tex, stmts, note=None, core=False, plain=None):
    E.append(dict(id=id, sec=sec, kind=kind, name=name, tex=tex, stmts=stmts, note=note, core=core, plain=plain))

# 1 Basic sets
ex("D1", 1, "Def", "Universe of objects",
   r"\mathcal{B},\ \mathcal{K}^{M},\ \mathcal{K}^{A},\ \mathcal{M},\ \mathcal{R},\ \mathcal{P},\ \mathcal{U},\ \mathcal{S} \ni \mathrm{BM}, \mathrm{WM},\ \mathcal{T}",
   [1, 2, 3, 4, 5, 7], "Boundary Points, MSIDs, AMSIDs, Asset Meters, TRs, parties, customers, sub-markets, periods.")
ex("D2", 1, "Def", "Roles are time-dependent",
   r"\operatorname{roles}(p,t) \subseteq \{\mathrm{LC},\ \mathrm{FSP},\ \mathrm{PRI},\ \mathrm{SEC},\ \mathrm{SUP},\ \mathrm{BMP}\}",
   [6], "Load Controller, FSP, CFPC holder (Primary), Secondary FSP, Supplier, BSC Party operating BM Units.")

# 2 Identities
ex("E1", 2, "Rule", "Each MSID belongs to one Boundary Point",
   r"\operatorname{bp} : \mathcal{K}^{M} \to \mathcal{B}", [8], "A function: exactly one Boundary Point per MSID.")
ex("D3", 2, "Def", "Pairs",
   r"M_b = \big(K^{M}_{\mathrm{imp}},\ K^{M}_{\mathrm{exp}}\big), \qquad A = \big(K^{A}_{\mathrm{imp}},\ K^{A}_{\mathrm{exp}}\big), \qquad K_{\mathrm{exp}} \text{ optional}",
   [9, 10], "An AMSID Pair measures one piece of equipment, so its two identities share one reach (D10).")
ex("E2", 2, "Rule", "Asset Meter Allocation",
   r"\operatorname{AMA} : \mathcal{K}^{A} \times t \to \mathcal{M}", [11],
   "A total function in time: exactly one Asset Meter serves each AMSID at any t.")
ex("E3", 2, "Derived", "Meter replacement is invisible above the identity",
   r"\begin{gathered} \operatorname{AMA}(K, t_1) \ne \operatorname{AMA}(K, t_2) \\ \text{changes no expression below, since none takes } m \text{ as an argument} \end{gathered}",
   [12], "Everything in sections 3 to 12 is keyed on K, never on m (choice 1).", core=True)

# 3 Site Configuration
ex("D4", 3, "Def", "Site Configuration record",
   r"c = \big(\operatorname{id}(c),\ b_c,\ \mathcal{K}^{M}_c,\ \mathcal{A}_c,\ \operatorname{par}_c,\ I(c)\big), \qquad \mathcal{K}^{M}_c \subseteq \operatorname{bp}^{-1}(b_c)",
   [13], "Which MSIDs (at one Boundary Point), which AMSID Pairs, and how they nest (par_c).", core=True)
ex("E4", 3, "Rule", "At most one live configuration per Boundary Point",
   r"\sum_{c} \big[b_c = b\big]\,\big[\operatorname{live}_t(c)\big] \le 1", [14])
ex("E5", 3, "Rule", "Each AMSID in exactly one live configuration",
   r"\sum_{c} \big[K \in \mathcal{A}_c\big]\,\big[\operatorname{live}_t(c)\big] = 1 \qquad \forall K \in \mathcal{K}^{A}", [15],
   "K ∈ 𝒜_c means K is one of the identities of a pair in 𝒜_c.")
ex("E6", 3, "Rule", "Content changes make a new configuration",
   r"\begin{gathered} \operatorname{content}(c) \text{ is constant on } I(c) \\ \text{a change at } t^{*} \Rightarrow \operatorname{to}(c) = t^{*} = \operatorname{from}(c'),\ \ \operatorname{id}(c') \ne \operatorname{id}(c) \end{gathered}",
   [16], "content(c) = (𝒦ᴹ_c, 𝒜_c, par_c).")
ex("D5", 3, "Def", "Metering tree",
   r"\operatorname{par}_c : \mathcal{A}_c \to \mathcal{A}_c \cup \{\top_c\}, \quad \top_c = M_{b_c}, \quad \text{acyclic}; \qquad A \sqsubset A' \iff A' \text{ is reached by repeating } \operatorname{par}_c \text{ from } A",
   [17], "The root ⊤ is the boundary. ⊑ is ⊏ or equal.", core=True)
ex("D6", 3, "Def", "Site", r"w \subseteq \mathcal{C}, \qquad \operatorname{site}(c, t) = w", [18])
ex("E7", 3, "Rule", "Moving a configuration between Sites keeps its ID",
   r"\operatorname{site}(c, t_1) \ne \operatorname{site}(c, t_2) \ \not\Rightarrow\ \text{a new } c", [19],
   "site is not part of content(c), so E6 does not fire.")

# 4 TRs and control
ex("E8", 4, "Rule", "A TR is behind at most one Boundary Point at a time",
   r"\sum_{b} \big[\operatorname{loc}(r,t) = b\big] \le 1", [20],
   "Statement 20 says “exactly one”. Kept as “at most one”, as agreed for v0.1/v0.2, so that an EV in transit is behind none (finding F1).")
ex("E9", 4, "Rule", "Mobile TRs: at most one Boundary Point per period",
   r"\sum_{b} \max_{t \in \tau} \big[\operatorname{loc}(r,t) = b\big] \le 1, \qquad \mathcal{R}_{b,\tau} = \{\, r : \exists t \in \tau,\ \operatorname{loc}(r,t) = b \,\}",
   [21], "max as Annex X-2 1.2.1(e).")
ex("D7", 4, "Def", "Control assignment",
   r"\operatorname{ca} = \big(r,\ p,\ I(\operatorname{ca})\big), \qquad \operatorname{LC}(r,t) = p \iff \exists \operatorname{ca} = (r, p, \cdot) \text{ live at } t", [22])
ex("E10", 4, "Rule", "Exactly one Load Controller for a controlled TR",
   r"\sum_{p} \big[\operatorname{LC}(r,t) = p\big] = \big[\, r \in \mathrm{ACT}_t \,\big]", [23],
   "1 for an actively controlled TR, 0 otherwise.")
ex("D8", 4, "Def", "Control group",
   r"\varnothing \ne g \subseteq \mathcal{R}_{b,t}, \qquad \forall r \in g:\ \operatorname{LC}(r,t) = \operatorname{LC}(g,t), \qquad \operatorname{one}(g,t)",
   [24], "one(g,t): the Load Controller can instruct g as one. 𝒢_{b,t} is the set of control groups at b.", core=True)
ex("E11", 4, "Rule", "Each controlled TR is in exactly one group",
   r"\sum_{g \in \mathcal{G}_{b,t}} \big[r \in g\big] = 1 \qquad \forall r \in \mathrm{ACT}_t \cap \mathcal{R}_{b,t}", [25])
ex("D9", 4, "Def", "Residual group",
   r"R_{b,t} = \mathcal{R}_{b,t} \setminus \bigcup_{g \in \mathcal{G}_{b,t}} g", [26],
   "By E11 these are exactly the TRs with no Load Controller.")
ex("E12", 4, "Derived", "Groups and residual partition the Boundary Point",
   r"\mathcal{R}_{b,t} = R_{b,t}\ \sqcup \bigsqcup_{g \in \mathcal{G}_{b,t}} g", [27],
   "⊔ is a union of sets with no TR in common.", core=True)
ex("E13", 4, "Rule", "Who may offer a control group",
   r"\operatorname{offers}(p, g, t) \Rightarrow p = \operatorname{LC}(g,t)\ \lor\ \operatorname{agr}\big(p, \operatorname{LC}(g,t), t\big)", [28],
   "agr = a control agreement.", core=True)
ex("E14", 4, "Rule", "Several FSPs: one Load Controller, one order",
   r"\begin{gathered} \big|\{p : \operatorname{offers}(p,g,t)\}\big| \ge 2 \Rightarrow \\ \text{every instruction to } g \text{ passes } \operatorname{LC}(g,t), \text{ ordered by } \succ_{g,t} \end{gathered}",
   [29], "≻_{g,t}: the agreed order of precedence (options 1a and 1b).")
ex("E15", 4, "Rule", "The residual group is influenced through the customer",
   r"\operatorname{offers}(p, R_{b,t}, t) \Rightarrow \operatorname{agr}\big(p, \operatorname{cust}(b,t), t\big); \qquad \text{E13, E14 do not apply to } R_{b,t}",
   [30])

# 5 Reach and arrangements
ex("D10", 5, "Def", "Reach", r"\operatorname{reach}_t(K) \subseteq \mathcal{R}, \qquad \operatorname{reach}_t(A) = \operatorname{reach}_t(K^{A}_{\mathrm{imp}}) = \operatorname{reach}_t(K^{A}_{\mathrm{exp}})",
   [31])
ex("E16", 5, "Rule", "The boundary reaches everything behind it",
   r"\operatorname{reach}_t(M_b) = \mathcal{R}_{b,t}", [32])
ex("E17", 5, "Rule", "A child reaches less than its parent",
   r"\operatorname{reach}_t(A) \subseteq \operatorname{reach}_t\big(\operatorname{par}_c(A)\big)", [33])
ex("E18", 5, "Rule", "Side-by-side meters reach different TRs",
   r"A \not\sqsubseteq A' \ \land\ A' \not\sqsubseteq A \ \Rightarrow\ \operatorname{reach}_t(A) \cap \operatorname{reach}_t(A') = \varnothing", [34],
   "With E17 the reaches nest like boxes inside boxes (a laminar family): any two are nested or disjoint.", core=True)
ex("D11", 5, "Def", "Three kinds of arrangement",
   r"\mathcal{X}_c = \{\mathrm{Bnd}\}\ \cup\ \{\mathrm{Ast}(A) : A \in \mathcal{A}_c\}\ \cup\ \{\mathrm{Res}(X) : \varnothing \ne X \subseteq \mathcal{A}_c\}",
   [35], "Boundary, Asset and Residual. X is the set of AMSID Pairs subtracted.", core=True)
ex("D12", 5, "Def", "Measurement perimeter",
   r"\begin{aligned} \operatorname{per}_t(\mathrm{Bnd}) &= \operatorname{reach}_t(M_b) \\ \operatorname{per}_t(\mathrm{Ast}(A)) &= \operatorname{reach}_t(A) \\ \operatorname{per}_t(\mathrm{Res}(X)) &= \operatorname{reach}_t(M_b) \setminus \bigcup_{A \in X} \operatorname{reach}_t(A) \end{aligned}",
   [36], core=True)
ex("E19", 5, "Rule", "A Residual subtracts an antichain",
   r"\mathrm{Res}(X) \in \mathcal{X}_c \Rightarrow \forall A \ne A' \in X:\ A \not\sqsubset A' \iff \operatorname{reach}_t(A) \cap \operatorname{reach}_t(A') = \varnothing",
   [37], "By E17 and E18, “no two nested” and “no TR in common” say the same thing.")
ex("E20", 5, "Rule", "A Residual needs an Asset arrangement in use",
   r"\operatorname{inUse}_t(\mathrm{Res}(X)) \Rightarrow \exists A \in \mathcal{A}_c:\ \operatorname{inUse}_t(\mathrm{Ast}(A))", [38],
   "inUse_t(x): some Asset with arrangement x has a live participation at t (finding F3).")
ex("E21", 5, "Rule", "Residuals only where differencing is accepted",
   r"\operatorname{arr}(a) = \mathrm{Res}(X)\ \land\ \operatorname{part}(a, s, t) \Rightarrow s \in \mathcal{S}^{\mathrm{DIFF}} = \{\mathrm{BM}, \mathrm{WM}\}", [39],
   "Today: AMVLPs under P375.")
ex("V1", 5, "Def", "Volume of an arrangement (BSC form)",
   r"QMA_{\mathrm{Bnd},j} = QM_{M_b j}, \qquad QMA_{\mathrm{Ast}(A),j} = QM_{Aj}, \qquad QMA_{\mathrm{Res}(X),j} = QM_{M_b j} - \sum_{A \in X} QM_{Aj}",
   [35, 36], "Signed sum of metered volumes, as AMMC_{Kj} = Σ_{KJ} AMRC_{KJj} in Annex S-2 3.5.3A.")
ex("V2", 5, "Derived", "Volume matches perimeter",
   r"QM_{Kj} = \sum_{r \in \operatorname{reach}(K)} QTR_{rj} \ \Rightarrow\ QMA_{x,j} = \sum_{r \in \operatorname{per}(x)} QTR_{rj}",
   [37], "Holds because of E19: no TR is subtracted twice. QTR_{rj} is the (unmetered) net flow of TR r.")

# 6 Assets
ex("D13", 6, "Def", "Flexibility Asset",
   r"a = (g, x), \qquad g \in \mathcal{G}_{b,t} \cup \{R_{b,t}\},\ \ x \in \mathcal{X}_c,\ \ b_c = b,\ \operatorname{live}_t(c); \qquad \operatorname{grp}(a) = g,\ \operatorname{arr}(a) = x",
   [40], "𝓕_c is the set of Assets in c.", core=True)
ex("E22", 6, "Rule", "Measurable",
   r"\operatorname{meas}_t(a) \iff \operatorname{grp}(a) \subseteq \operatorname{per}_t(\operatorname{arr}(a)); \qquad \text{every Asset is measurable}",
   [41], "The second half was accepted for drafting in v0.2 (S29a) and is kept for review (finding F7).")
ex("D14", 6, "Def", "Exactly and inclusively measured",
   r"\operatorname{exact}_t(a) \iff \operatorname{per}_t(\operatorname{arr}(a)) = \operatorname{grp}(a), \qquad \operatorname{incl}_t(a) \iff \operatorname{grp}(a) \subsetneq \operatorname{per}_t(\operatorname{arr}(a))",
   [42, 43])
ex("D15", 6, "Def", "Exposure set",
   r"E_t(a) = \operatorname{per}_t(\operatorname{arr}(a)) \setminus \operatorname{grp}(a)", [43, 44],
   "A new term: the TRs an Asset is measured on but does not control.")
ex("E23", 6, "Derived", "Compensation effect",
   r"QMA_{\operatorname{arr}(a),j} = \underbrace{\sum_{r \in \operatorname{grp}(a)} QTR_{rj}}_{\text{delivered}} + \underbrace{\sum_{r \in E(a)} QTR_{rj}}_{\text{exposure}}, \qquad \operatorname{incl}(a) \iff E(a) \ne \varnothing",
   [44], "From V2: the exposure term can counteract delivery.", core=True)
ex("D16", 6, "Def", "Sibling Assets",
   r"a \sim a' \iff \operatorname{grp}(a) = \operatorname{grp}(a')\ \land\ \operatorname{arr}(a) \ne \operatorname{arr}(a')", [45])
ex("E24", 6, "Derived", "Siblings share their allocation",
   r"a \sim a' \Rightarrow \operatorname{alloc}(a, t) = \operatorname{alloc}(a', t)", [46],
   "Tagged [Rule] in the statements; it follows from D29, where an allocation is made to the group (finding F2).")
ex("E25", 6, "Rule", "Siblings never share a sub-market",
   r"\sum_{a :\ \operatorname{grp}(a) = g} \big[\operatorname{part}(a, s, t)\big] \le 1 \qquad \forall g, s, t", [47], core=True)
ex("D17", 6, "Def", "Residual Asset",
   r"a_{R} = \big(R_{b,t},\ \mathrm{Res}(X)\big)", [48])
ex("E26", 6, "Derived", "The group is the unique object",
   r"[g] = \{\, a : \operatorname{grp}(a) = g \,\}; \qquad \text{the classes } [g] \text{ partition the Assets of } b", [49],
   "Assets are views of g; everything that must be unique (allocation, authority) is keyed on g.")

# 7 Overlap, compatibility, consolidation
ex("D18", 7, "Def", "Overlap",
   r"\operatorname{ov}_t(a, a') \iff \operatorname{grp}(a) \ne \operatorname{grp}(a')\ \land\ \operatorname{per}_t(\operatorname{arr}(a)) \cap \operatorname{per}_t(\operatorname{arr}(a')) \ne \varnothing",
   [50], core=True)
ex("E27", 7, "Derived", "Overlap is always in measurement",
   r"\operatorname{grp}(a) \ne \operatorname{grp}(a') \Rightarrow \operatorname{grp}(a) \cap \operatorname{grp}(a') = \varnothing", [51], "From E12.")
ex("D19", 7, "Def", "Identity conflict",
   r"\operatorname{idc}(g, g') \iff g \ne g'\ \land\ \big(g \cap g' \ne \varnothing\ \lor\ \operatorname{suspected}(g, g')\big)", [52])
ex("E28", 7, "Rule", "Resolve identity conflicts first",
   r"\operatorname{assess}(c, t) \Rightarrow \nexists\, g, g' \in \mathcal{G}_{b_c,t}:\ \operatorname{idc}(g, g')", [53])
ex("E29", 7, "Derived", "Overlap from the metering tree alone",
   r"\operatorname{ov}^{\mathrm{tree}}(x, x') = \begin{cases} 1 & x = \mathrm{Bnd}\ \text{or}\ x' = \mathrm{Bnd}\ \text{or}\ x = x' \\ [A \sqsubseteq A' \lor A' \sqsubseteq A] & x = \mathrm{Ast}(A),\ x' = \mathrm{Ast}(A') \\ 1 - [\exists A'' \in X : A \sqsubseteq A''] & x = \mathrm{Ast}(A),\ x' = \mathrm{Res}(X) \\ 1 & x = \mathrm{Res}(X),\ x' = \mathrm{Res}(X')\ ^{\dagger} \end{cases}",
   [54, 55, 56, 57], "† unless the subtracted meters together reach every TR, which the tree alone cannot show; treated as overlapping. Statement 55 omits the case A = A′; statement 57 covers it.", core=True)
ex("E30", 7, "Derived", "Tree and perimeter agree",
   r"\begin{gathered} \text{no identity conflict, non-empty reaches} \Rightarrow \\ \operatorname{ov}_t(a, a') = \operatorname{ov}^{\mathrm{tree}}\big(\operatorname{arr}(a), \operatorname{arr}(a')\big) \cdot \big[\operatorname{grp}(a) \ne \operatorname{grp}(a')\big] \end{gathered}",
   [58], "Proof: E16 to E18 make reaches a laminar family, so every intersection in D12 is decided by ⊑.")
ex("D20", 7, "Def", "Compatibility",
   r"\operatorname{compat}(c, t) \iff \forall a, a' \in \mathcal{F}_c:\ \operatorname{inUse}_t(a) \land \operatorname{inUse}_t(a') \Rightarrow \neg\operatorname{ov}_t(a, a')",
   [59], core=True)
ex("E31", 7, "Rule", "Compatibility ignores sub-market boundaries",
   r"\operatorname{compat}(c, t) \text{ ranges over all of } \mathcal{F}_c, \text{ whatever } s \text{ each Asset is used in}", [60])
ex("D21", 7, "Def", "Reconfiguration",
   r"a = (g, x) \to (g, x'),\ x' \in \mathcal{X}_c \cup \mathcal{X}_{c'} \quad \text{or} \quad g \to g^{*}, \qquad \text{removing } \operatorname{ov}(a, \cdot)",
   [61], "c′ is a successor configuration with added metering (E6).")
ex("D22", 7, "Def", "Reconcilable and irreconcilable",
   r"\begin{gathered} \operatorname{rec}(F) \iff \exists\, \chi : F \to \mathcal{X}_c \cup \mathcal{X}_{c'}\ \ \forall a, a' \in F: \\ \neg \operatorname{ov}\big((\operatorname{grp}(a), \chi(a)),\ (\operatorname{grp}(a'), \chi(a'))\big) \\ \operatorname{irr}(F) \iff \neg\operatorname{rec}(F) \end{gathered}",
   [62, 63], "χ chooses an arrangement for each Asset, using existing or added metering.")
ex("E32", 7, "Derived", "Boundary-only groups need new metering",
   r"\begin{gathered} \nexists A \in \mathcal{A}_c:\ g \subseteq \operatorname{reach}(A),\ g' \cap \operatorname{reach}(A) = \varnothing \ \ (\text{or with } g, g' \text{ swapped}) \\ \Rightarrow \operatorname{irr}_{c}(\{g, g'\}) \end{gathered}",
   [64], "Without an AMSID that separates them, only Bnd or overlapping Residuals remain.")
ex("D23", 7, "Def", "Consolidation", r"\operatorname{irr}(\{g, g'\}) \Rightarrow g^{*} = g \cup g' \in \mathcal{G}_{b,t}", [65])
ex("E33", 7, "Rule", "One Load Controller after consolidation",
   r"\exists!\, p:\ \operatorname{LC}(g^{*}, t) = p, \ \text{agreed between } \operatorname{LC}(g,t) \text{ and } \operatorname{LC}(g',t)", [66])
ex("O67", 7, "Open", "Alternative: multi-group Asset",
   r"a = (\{g_1, \dots, g_n\},\ x), \qquad \operatorname{LC}(g_i, t) \text{ may differ, coordinated at site level}", [67], "Future scope.")

# 8 Authority
ex("D24", 8, "Def", "CFPC",
   r"\varphi = \big(\operatorname{cust}(\varphi),\ b_\varphi,\ \operatorname{holder}(\varphi),\ \operatorname{trs}(\varphi) \subseteq \mathcal{R}_{b_\varphi},\ I(\varphi)\big), \qquad \operatorname{cust}(\varphi) = \operatorname{cust}(b_\varphi, t)\ \ \forall t \in I(\varphi)",
   [68])
ex("E34", 8, "Rule", "A CFPC covers whole groups",
   r"\operatorname{trs}(\varphi) \cap g \in \{\varnothing,\ g\} \qquad \forall g \in \mathcal{G}_{b_\varphi, t}", [69], core=True)
ex("O70", 8, "Open", "CFPC exclusivity",
   r"\begin{aligned} \text{0a:}\ & \text{no limit} \\ \text{1a:}\ & \sum_{\varphi} \big[r \in \operatorname{trs}(\varphi)\big]\big[s \in \operatorname{sm}(\varphi)\big]\big[\operatorname{live}_t(\varphi)\big] \le 1 \\ \text{1b, 2:}\ & \sum_{\varphi} \big[r \in \operatorname{trs}(\varphi)\big]\big[\operatorname{live}_t(\varphi)\big] \le 1 \end{aligned}",
   [70], "sm(φ): the sub-markets a CFPC covers; needed for 1a.")
ex("D25", 8, "Def", "Delegation",
   r"\delta = \big(\varphi_\delta,\ \operatorname{sec}(\delta),\ s_\delta,\ I(\delta)\big), \qquad \operatorname{sec}(\delta) \ne \operatorname{holder}(\varphi_\delta)", [71],
   "The CFPC stays with its holder (the Primary).")
ex("E35", 8, "Rule", "A delegation ends with its CFPC", r"I(\delta) \subseteq I(\varphi_\delta)", [72])
ex("E36", 8, "Rule", "A change of customer ends CFPCs and delegations",
   r"\operatorname{cust}(b, t) \ne \operatorname{cust}(\varphi) \Rightarrow \neg\operatorname{live}_t(\varphi)\ \land\ \neg\operatorname{live}_t(\delta)\ \ \forall \delta : \varphi_\delta = \varphi",
   [73], "Follows from D24 and E35 once the customer changes.")

# 9 Registration, allocation, participation
ex("D26", 9, "Def", "Registration (claim)", r"\kappa = \big(\operatorname{fsp}(\kappa),\ a_\kappa,\ s_\kappa,\ I(\kappa)\big)", [74])
ex("E37", 9, "Rule", "Valid registration",
   r"\operatorname{valid}(\kappa) \iff \forall t \in I(\kappa):\ \operatorname{auth}\big(\operatorname{fsp}(\kappa), \operatorname{grp}(a_\kappa), s_\kappa, t\big)\ \land\ \text{E13 holds}",
   [75], "auth(p,g,s,t): p holds a live CFPC covering g, or a live delegation for s from one.")
ex("E38", 9, "Rule", "Competing registrations",
   r"\begin{gathered} \operatorname{fsp}(\kappa) \ne \operatorname{fsp}(\kappa'),\ \ \operatorname{grp}(a_\kappa) = \operatorname{grp}(a_{\kappa'}),\ \ s_\kappa = s_{\kappa'},\ \ I(\kappa) \cap I(\kappa') \ne \varnothing \\ \Rightarrow \operatorname{cmp}(\kappa, \kappa') \end{gathered}",
   [76], "Same group covers both “same Asset” and “sibling Assets”.")
ex("O77", 9, "Open", "Competition across sub-markets",
   r"s_\kappa \ne s_{\kappa'}:\quad \operatorname{cmp} = \begin{cases} 1 & \text{2, 0b} \\ 1 - [\,p, p' \in \mathrm{COORD}\,] & \text{1a} \\ 1 - \operatorname{del}(p)\operatorname{del}(p') & \text{1b} \\ \operatorname{rule}_{s} & \text{0a} \end{cases}",
   [77], "del(p) = 1 if p is the Primary or holds its delegation.")
ex("D27", 9, "Def", "Assignment", r"\operatorname{asg}(g, t) \in \{\operatorname{fsp}(\kappa) : \operatorname{cmp}\} \cup \{\text{FSP groups}\} \cup \{\operatorname{holder}(\varphi)\}", [78])
ex("D28", 9, "Def", "Allocation (to the group)",
   r"\lambda = \big(g_\lambda,\ F_\lambda \subseteq \mathcal{P},\ I(\lambda)\big), \qquad \operatorname{alloc}(a, t) = \lambda \iff \operatorname{grp}(a) = g_\lambda \land \operatorname{live}_t(\lambda)",
   [79], "One allocation covers all of [g] (E26).", core=True)
ex("E39", 9, "Rule", "Only compatible groups are allocated",
   r"\operatorname{live}_t(\lambda) \Rightarrow \operatorname{compat}(c, t) \text{ for the } c \text{ holding } g_\lambda", [80])
ex("E40", 9, "Rule", "At most one allocation per group",
   r"\sum_{\lambda} \big[g_\lambda = g\big]\big[\operatorname{live}_t(\lambda)\big] \le 1", [81], core=True)
ex("D29", 9, "Def", "Re-allocation",
   r"\lambda \to \lambda' \text{ at } t^{*}: \quad \operatorname{to}(\lambda) = t^{*} = \operatorname{from}(\lambda'), \quad g_{\lambda'} = g_\lambda", [82])
ex("D30", 9, "Def", "Participation",
   r"\pi = \big(\operatorname{fsp}(\pi),\ a_\pi,\ s_\pi,\ I(\pi)\big); \qquad \operatorname{part}(a, s, t) \iff \exists \pi: a_\pi = a,\ s_\pi = s,\ \operatorname{live}_t(\pi)",
   [83], "In the BSC: MSID Pair Allocation (P0278) or AMSID Pair Allocation (P0306) to a Secondary BM Unit i2.")
ex("E41", 9, "Rule", "Every participation traces to an allocation",
   r"\begin{aligned} \forall \pi:\ & \exists!\, \lambda:\ g_\lambda = \operatorname{grp}(a_\pi),\ \operatorname{fsp}(\pi) \in F_\lambda,\ I(\pi) \subseteq I(\lambda) \\ \text{or}\ & \exists \delta:\ \operatorname{sec}(\delta) = \operatorname{fsp}(\pi),\ s_\delta = s_\pi,\ I(\pi) \subseteq I(\delta) \end{aligned}",
   [84], "The delegation route is finding F6.", core=True)
ex("E42", 9, "Rule", "BSC participation by arrangement type",
   r"\operatorname{arr}(a_\pi) = \mathrm{Ast}(A) \Rightarrow \pi \text{ is an AMSID Pair Allocation of } A; \qquad \operatorname{arr}(a_\pi) \in \{\mathrm{Bnd}, \mathrm{Res}(X)\} \Rightarrow \pi \text{ is an MSID Pair Allocation of } M_b",
   [85])
ex("E43", 9, "Rule", "Different parties may hold the two kinds", r"\operatorname{fsp}(\pi_{M}) \ne \operatorname{fsp}(\pi_{A}) \text{ is allowed within one } c", [86])
ex("E44", 9, "Derived", "Consistent with compatibility",
   r"A \in X \Rightarrow \operatorname{ov}^{\mathrm{tree}}\big(\mathrm{Ast}(A), \mathrm{Res}(X)\big) = 0", [87], "From E29, third case.")

# 10 Differencing
ex("E45", 10, "Rule", "When an MSID Pair is differenced",
   r"\mathrm{DIFF}_{cj} = \Big[\, \exists A \in \mathcal{A}_c:\ \operatorname{part}^{\mathrm{BSC}}(A, j) \,\Big]", [88],
   "part^BSC(A, j): A has a live AMSID Pair Allocation in Settlement Period j.", core=True)
ex("E46", 10, "Derived", "Subtract only the outermost participating AMSIDs",
   r"\begin{aligned} \mathrm{PA}_{cj} &= \{A : \operatorname{part}^{\mathrm{BSC}}(A, j)\} \\ \mathrm{OUT}_{cj} &= \{A \in \mathrm{PA}_{cj} : \nexists A' \in \mathrm{PA}_{cj},\ A \sqsubset A'\} \\ QSUB_{cj} &= \sum_{A \in \mathrm{OUT}_{cj}} QM_{Aj} \end{aligned}",
   [89], "OUT is an antichain by construction, so E19 holds automatically and nothing is subtracted twice. Compare ΣKDiff in Table X-5.", core=True)
ex("V3", 10, "Derived", "Differenced MSID Pair volume",
   r"QRES_{cj} = QM_{M_b j} - \mathrm{DIFF}_{cj} \cdot QSUB_{cj} = QMA_{\mathrm{Res}(\mathrm{OUT}_{cj}),\,j}", [88, 89],
   "In the BSC the Residual arrangement is derived each period: X = OUT_{cj}.")
ex("E47", 10, "Rule", "Notify the MSID Pair participant",
   r"\mathrm{DIFF}_{cj} \ne \mathrm{DIFF}_{c,j-1}\ \land\ \operatorname{fsp}(\pi_{A}) \ne \operatorname{fsp}(\pi_{M}) \Rightarrow \operatorname{notify}\big(\operatorname{fsp}(\pi_{M}), j\big)",
   [90], "Existing flows: P0309 Notification of use of AMSID Pair by another AMVLP; P0320 Loss of AMSID Pair Allocation Notification.")
ex("E48", 10, "Derived", "Differencing removes the overlap, in BSC settlement only",
   r"\begin{gathered} s = \mathrm{BM}:\ \operatorname{per}(\pi_M) = \operatorname{per}\big(\mathrm{Res}(\mathrm{OUT}_{cj})\big) \\ \Rightarrow \neg\operatorname{ov}\big(a_{\pi_M}, a_{\pi_A}\big)\ \ \forall \pi_A \text{ with } A \in \mathrm{PA}_{cj} \end{gathered}",
   [91], "Every participating A equals or sits behind a member of OUT, so E29 gives no overlap.")
ex("E49", 10, "Derived", "Elsewhere the overlap stays and is flagged",
   r"\begin{gathered} s \notin \mathcal{S}^{\mathrm{DIFF}}\ \land\ \operatorname{arr}(a) = \mathrm{Bnd} \\ \Rightarrow \operatorname{ov}(a, a') \text{ for every } a' \text{ of another group in use};\ \ \operatorname{flag}(a, a') \end{gathered}",
   [92], "Finding F4: this conflicts with E31 + E39 unless flagged overlaps are allowed.")

# 11 Units
ex("D31", 11, "Def", "Unit", r"u = \big(\operatorname{fsp}(u),\ s_u,\ \mathcal{F}_{u,t}\big); \qquad s_u = \mathrm{BM} \Rightarrow u \text{ is a Secondary BM Unit } i2", [93])
ex("E50", 11, "Rule", "Units hold only validly participating Assets",
   r"a \in \mathcal{F}_{u,t} \Rightarrow \exists \pi:\ a_\pi = a,\ \operatorname{fsp}(\pi) = \operatorname{fsp}(u),\ s_\pi = s_u,\ \operatorname{live}_t(\pi)", [94])
ex("E51", 11, "Rule", "One Unit per Asset per sub-market",
   r"\sum_{u :\ s_u = s} \big[a \in \mathcal{F}_{u,t}\big] \le 1", [95], "Cf. S10.1A.3: an AMSID Pair may not be allocated to more than one Secondary BM Unit at a time.")

# 12 Objectives
ex("O1", 12, "Derived", "Avoided duplication",
   r"\forall s, t, r:\ \sum_{g} \Big[\, \exists a \in [g]:\ \operatorname{part}(a,s,t)\ \land\ r \in \operatorname{per}_t(\operatorname{arr}(a)) \,\Big] \le 1 \qquad \text{and E25}",
   [96], "Holds from E41 → E39 → D20 (no overlap in use), E9 (different Boundary Points are disjoint) and E25. Gaps: F4, F6.", core=True)
ex("O2", 12, "Derived", "Clear accountability",
   r"\forall \pi:\ \sum_{\lambda} \big[\pi \text{ traces to } \lambda\big] = 1; \qquad \forall \lambda, s, t:\ \sum_{p \in F_\lambda} \big[\exists \pi: \operatorname{fsp}(\pi) = p,\ s_\pi = s,\ \operatorname{live}_t(\pi)\big] \le 1",
   [97], "First half from E41 and E40; the second half needs a rule inside FSP groups (finding F8).")
ex("O3", 12, "Derived", "Fair and efficient switching",
   r"\lambda_1, \lambda_2 \text{ successive for } g:\ \operatorname{to}(\lambda_1) = \operatorname{from}(\lambda_2)", [98], "From D29 and E40.")
ex("O4", 12, "Derived", "Coordinated participation",
   r"\forall e \in \{\lambda, \delta, \pi\}:\ I(e) \text{ recorded}\ \land\ \operatorname{vis}(e) \supseteq \operatorname{entitled}(e)", [99],
   "A recording requirement rather than a property of the maths; vis and entitled are new.")

EXPRESSIONS = E

# ---------------------------------------------------------------------------------------------
# Findings from formalising
# ---------------------------------------------------------------------------------------------
FINDINGS = [
    ("F1", [20, 21], "Statement 20 says a TR is behind exactly one Boundary Point at any time, which an EV in transit breaks. v0.1 agreed “at most one”; E8 keeps that.", "Confirm, or reword statement 20."),
    ("F2", [46, 79], "With allocation made to the control group (79), siblings share an allocation automatically. Statement 46 is then [Derived], not [Rule].", "Retag statement 46."),
    ("F3", [38, 59, 88], "“In use” (38, 59) is not defined. The draft reads it as “has a live participation”. In the BSC, statement 88 makes 38 automatic, because differencing only happens when an AMSID Pair participates.", "Confirm the meaning of “in use”."),
    ("F4", [59, 60, 80, 92], "A Boundary arrangement used in a sub-market without differencing overlaps every AMSID Asset of another group (54). Compatibility is assessed across all sub-markets (60) and only compatible groups can be allocated (80), so such a group cannot be allocated. Statement 92 instead expects the overlap to stand and be flagged.", "Choose: allow flagged overlaps as an exception to 80, or assess compatibility per sub-market for Boundary arrangements."),
    ("F5", [35, 48, 88, 89], "The FMAR residual Asset subtracts a declared set X, but BSC settlement subtracts OUT_{cj}, the outermost AMSIDs that participate in that period. If an AMSID Asset exists but is not participating in period j, the two perimeters differ.", "Define the residual Asset’s perimeter per sub-market and period (X = OUT_{cj} in the BSC), or require X to match."),
    ("F6", [80, 84], "A participation can trace to a delegation instead of an allocation (84). The compatibility check (80) sits on allocations, so a delegated participation is not checked. This gap was F8 in v0.2.", "Require a delegated participation to sit under the Primary’s allocation, or check compatibility for delegations too."),
    ("F7", [41], "Statement 41 defines measurability but nothing requires an Asset to be measurable. The overlap results need it. v0.2 accepted “every Asset is measurable” (S29a) for drafting.", "Confirm the rule."),
    ("F8", [97], "O2’s second half (within an FSP group, each sub-market traces to one FSP) is not implied by any rule. It needs its own rule on FSP groups.", "Add a rule, or make it part of the allocation record."),
    ("F9", [55, 57], "Statement 55 omits the case where both Assets use the same AMSID; statement 57 covers it. E29 combines them.", "None, unless you want 55 reworded."),
    ("F11", [26, 41, 48, 89], "A Residual arrangement cannot measure the residual group if a subtracted AMSID also reaches residual TRs. Example: a garage sub-board AMSID feeds an EV charger (controlled) and a freezer (residual); subtracting it removes the freezer from the residual perimeter, so the residual Asset is not measurable (41). In BSC settlement this happens whenever such an AMSID is in OUT_cj.", "Require every AMSID that can be subtracted to reach only controlled TRs, or accept that the residual Asset then misses those TRs."),
    ("F10", [34, 37, 89],"Statements 33 and 34 make the reaches a laminar family (nested or disjoint). Statement 37 then reduces to “no subtracted AMSID sits behind another”, and statement 89’s outermost rule satisfies it by construction.", "None: a consistency result."),
]

FINDINGS.sort(key=lambda f: int(f[0][1:]))
