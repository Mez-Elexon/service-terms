# Flexibility Market Rule: Primacy Rules (FMR-PR) V2.0

> **Source file:** `FMR-PR - Primacy Rules V2.0.txt`  
> **Published Date:** 04/02/2026  
> **Converted:** 2026-10-07. Wording kept verbatim from the source copy-paste; only layout artefacts (page headers/footers, line wraps, website navigation, broken tables) were cleaned up. Sections the source marks as guidance are not legally binding. Notes in *[italic square brackets]* are editorial.

---


Sections 1, 2, 3 and 4 form the legally binding Flexibility Market Rule.

Defined terms capitalised in this document shall have the meaning given in Section 4.

## Summary of Primacy Rules

This section is provided as guidance to the Flexibility Market Rule. Therefore, it is not legally binding and falls outside of the formal change management process.

### Context

Primacy rules are used to manage situations of conflict between the actions of different System Operators. For example, NESO might ask a site to increase their generation, whilst the DNO is asking a nearby site to reduce. The Primacy rules set a framework for managing that conflict.

Since this rule codifies the first version of the Primacy Rules, it only applies to NESO, NGED and UKPN, specifically in areas where MW Dispatch is being procured.

### Primacy Rules Requirements

The rule sets out some core requirements:

- The System Operators must share information on potential conflicts via Risk of Conflict reports. DNOs need to be able to create these, and NESO must be able to ingest them
- As DNO primacy is being implemented the DNO action has priority, and so NESO shall not take actions in the MWD sub-market that exacerbate the conflict (as identified in the Risk of Conflict report).

We believe the impact of these requirements to be:

| Impact on System Operators | Impact on FSPs |
|---|---|
| NESO, NGED and UKPN must develop and maintain the processes and systems to delivery primacy | Providers of MW Dispatch may see lower dispatch identified in the Risk of Conflict report. |

### Implementation monitoring requirements

The key requirements are laid out below. A view across the rules is available in our deadline tracker.

| Category | Requirement | Trigger for data submission | What we will do with it |
|---|---|---|---|
| Implementation tracking | Basic tracking of implementation status and target date | From 14/01/2026 (20 working days after the published date).<br>Within 10 days of change | Track whether implementation is on track via our Implementation tracker. |
| Flexibility Market Catalogue data |  | From 06/02/2026.<br>Within 10 days of change | Provide an overview of the sub-market and the market as a whole via the Flexibility Market Catalogue. |
| Effectiveness monitoring data | N/A | - | - |

## 1. Applicability of this Flexibility Market Rule

This Flexibility Market Rules applies only to NESO and DNOs supporting the operation of the MW Dispatch Sub-Market. Innovation trials are not bound by this Flexibility Market Rule.

The relevant System Operators shall develop and maintain the processes defined in section 2.3 to implement DNO Primacy as defined in section 2.2 in the use cases set out in section 2.4 no later than the Implementation Date.

The relevant System Operators shall provide the data set out in section 3 no later than the timings also set out in section 3.

Variations to this rule are only permitted with an approved Derogation from the Market Facilitator.

The core applicability parameters are laid out below.

**Table 1: Flexibility Market Rule dates**

| Parameter | Value |
|---|---|
| Published Date | 04/02/2026 |
| Implementation Date | 06/02/2026 |
| End Date | - |

#### Explainer: What is a Sub-Market?

This section is provided as guidance to the Flexibility Market Rule. Therefore, it is not legally binding and falls outside of the formal change management process.

A Sub-Market means a specific segment of the overall Flexibility Market, distinguished by a specific System Operator, procuring a specific Product within a specific time period.

A Sub-market may be built of multiple distinct geographic zones, operating in different directions, clearing different volumes at different prices.

The diagram below visualises the definition.

*[Diagram/image in the original web page was not captured in the copy-paste.]*

DTU means Demand Turn Up, GTD means Generation Turn Down.

DTD means Demand Turn Down, GTU means Generation Turn Up.

## 2. Primacy Rules

### 2.1 What are Primacy Rules?

Primacy Rules are a defined set of principles and guidelines to manage conflicts between NESO and DNO requirements and constraints. They govern the procurement, planning, scheduling, and dispatch of supporting services across the electricity system. These rules are designed to enable efficient and transparent optimisation of both transmission and distribution networks, operated respectively by NESO and DNOs.

Primacy rules aim to resolve potential overlaps or conflicts between services by prioritising actions based on whole-system value, while distinguishing between market- or price-driven actions and essential operational requirements. They seek to balance the technical needs of local networks, system-wide operability risks, value for service providers, support for emerging market platforms, and cost impacts on consumers. I.e. primacy seeks to avoid a scenario where the dispatch of one System Operator’s service is contrary to the network or system requirements of another System Operator such that it results in increased protective actions (and therefore costs) or risks secure operation.

Primacy typically applies to conflicts between different assets within the same electrical network and may otherwise create inefficiencies.

### 2.2 Definition of DNO primacy

DNO primacy means DNO flexibility services shall take priority over the NESO’s service, due to their localised nature and the limited availability of alternative options at the distribution level.

The Risk of Conflict report will be fed into the NESO’s planning processes for the relevant service, with the NESO removing units from the control room dispatchable options where the DNO has identified a risk of conflict unless such actions cause significant operational harm to NESO.

### 2.3 Required processes to support primacy

The following supporting processes and data exchanges are needed to implement the primacy rules:

- **Asset mapping:** Mapping relevant assets between the System Operators. This should cover the assets impacted by both services in the use case (as set out below). This is currently managed by the DNO, through the mapping of MW Dispatch requirements in its bilateral connection agreements with the NESO. The location of DNO CMZs is publicly available.

- **Forecasting the risk of conflict:** The DNOs shall create a forecast of the risk of conflict. This will reflect the DNO’s specific approach to forecasting and translate it into the identification of risk of conflict.

- **Sharing the risk of conflict report:** DNOs shall share a regular Risk of Conflict report with NESO. This should be updated no less frequently than weekly and include at a minimum:

    - A common ID
    - The start and end time of the unavailability
    - An unavailability reason (this specifies if the asset will be constrained or not by the DNO)
    - An unavailability cause (to allow for further use cases to be added).

- **NESO integration process:** NESO will ingest the forecast and feed into their procurement & dispatch processes.

### 2.4 Applicable use cases

The current use-cases under consideration are highlighted in Table 2 below.

**Table 2: Applicable use cases for the Primacy Rules**

| Relevant NESO Sub-Market | Relevant DNO Sub-Market | Applicable Rule |
|---|---|---|
| MW Dispatch | All DNO Sub-Markets except Restore & Operational Utilisation | DNO has Primacy |

## 3. Market Information

### 3.1 Implementation tracking

The relevant System Operators must provide the Market Facilitator with the data set out in Table 3 for each Sub-Market in scope of this Flexibility Market Rule. The data provided should accurately reflect their implementation of the rule within each of each Sub-Market.

The expected values required for compliance are also set out in Table 3.

Initial data shall be sent no later than 20 working days after the Published Date of this Flexibility Market Rule.

Updates shall be sent as soon as reasonably practical, and no later than 10 working days after any changes to the values.

Elexon reserves the right to publish this data within its Implementation Tracker.

**Table 3: Implementation tracking requirements**

| Parameter | Required value (per Sub-Market) |
|---|---|
| Implementation Status | Dependent on date:<br>Before Implementation Date: Not yet started, Implementing, Paused, Implemented<br>Between Implementation Date and End Date: Implemented<br>After End Date: Superseded |
| Target Implementation Date | No later than Implementation Date |

*[The header row of this table begins with the reference FMR-MRS in the source.]*

### 3.2 Flexibility Market Catalogue data

The relevant System Operators must update the Market Facilitator with the data set out in Table 4 below for each Sub-Market in scope of this Flexibility Market Rule. This should accurately reflect their implementation of each Sub-Market.

The expected values required for compliance are also set out in Table 4.

Initial data shall be sent no later than the Implementation Date of this Flexibility Market Rule.

Updates shall be sent as soon as reasonably practical, and no later than 10 working days after any changes to the values.

The relevant System Operators shall also publish this information themselves.

Elexon reserves the right to publish this data within its Flexibility Market Catalogue.

**Table 4: Sub-Market definitions**

| Parameter Name | Description | Required value |
|---|---|---|
| **NESO: for all DNO Sub-markets in scope of this rule as set out in section 2.4** |  |  |
| Is DNO primacy implemented | Has DNO priority, as defined in section 2 been implemented? | Yes for applicable Sub-Market pair as set out in section 2.4. |
| **DNOs: for all NESO Sub-markets in scope of this rule as set out in section 2.4** |  |  |
| Is DNO primacy implemented | Has DNO priority, as defined in section 2 been implemented? | Yes for applicable Sub-Market pair as set out in section 2.4. |

### 3.3 Effectiveness monitoring

There are no market facilitator metrics for this rule

## 4. Glossary

The following definitions are specific to this Flexibility Market Rule. These are supplemented by the definitions in the Market Facilitator Glossary. If there is an inconsistency between definitions, the definition in this document shall prevail.

| Term | Meaning |
|---|---|
| MW Dispatch | The Sub-Market of that name, operated by NESO |

## FMR: Primacy Rules - Amendment record

*This section is provided as guidance to the Flexibility Market Rule. Therefore, it is not legally binding and falls outside of the formal change management process.*

| Version | Published Date | Document Status | Description of Changes | Change Proposal Reference | Market Facilitator Decision Report Ref |
|---|---|---|---|---|---|
| 1.0 | 12/12/2025 | Final | Document Published | - | - |
| 2.0 | 04/02/2026 | Final | Housekeeping change | CP002 | CP002 |

## Annex 1: Associated meta-data

*This annex is provided as guidance to the Flexibility Market Rule. Therefore, it is not legally binding and falls outside of the formal change management process.*

| Field | Value |
|---|---|
| Identifier | FMR-PR |
| Title | Primacy Rules |
| Type | Flexibility Market Rule |
| Collection | Market Coordination |
| Audience | NESO, DNOs, Flexibility Service Providers |
| Expertise | Operations |
| Owner | Market Facilitator |
| Expected benefit | To manage conflict between system operators to reduce overall system costs and reduce risk to security of supply |
| Related end-to-end process reference | C.3 Clear Market<br>D.3 Dispatch Units |
| References |  |
| IsReferencedBy |  |
| Published version number | 2.0 |
| Applicability | Only NESO and DNOs supporting the operation of the MW Dispatch Sub-Market. |
| Published Date | 04/02/2026 |
| Implementation Date | 06/02/2026 |
| End Date | N/A |
| Terms of variations | Approved Derogation only |
| IsReplacedBy | N/A |
| Replaces | N/A |
| Status | Final |
| Change since last version | Housekeeping change – Correction of Implementation date. Update to table numbering, section 3.3 and sub-market guidance. |

**Description**

**What?**
This rule establishes DNO priority over the dispatch of the MW Dispatch Sub-Market.

**How?**
The rule set out the concept of DNO priority, the use-cases they relate to and the associated processes needed to implement it.

**Who?**
This impacts the DNOs with MW Dispatch deployed (currently NGED and UKPN), and NESO. As MW Dispatch is locational it only impacts generators within specific grid supply points (as set out by NESO and the DNOs)

**When?**
The rule will go live in January 2026 as systems and processes are already in place.

**Why?**
The rule aims to reduce conflicts and increase efficiency across the different Sub-Markets

*[In the source each question label (How?, Who?, When?, Why?) was glued to the end of the previous answer; the labels have been moved onto their own lines.]*