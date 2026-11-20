# Flexibility Market Rule: Product Definitions (FMR-PD) V4.2

> **Source file:** `FMR-PD - Product definitions V4.2.txt`  
> **Published Date:** 25/08/2026  
> **Converted:** 2026-10-07. Wording kept verbatim from the source copy-paste; only layout artefacts (page headers/footers, line wraps, website navigation, broken tables) were cleaned up. Sections the source marks as guidance are not legally binding. Notes in *[italic square brackets]* are editorial.

---


Sections 1, 2, 3 and 4 form the legally binding Flexibility Market Rule.

Defined terms capitalised in this document shall have the meaning given in Section 4.

## Summary of Product Definitions Flexibility Market Rule

This section is provided as guidance to the Flexibility Market Rule. Therefore, it is not legally binding and falls outside of the formal change management process.

### Context

This rule establishes a standardised set of flexibility products for Distribution Network Operators (DNOs), aiming to reduce procurement variation and improve market coordination. It comes into force in February 2026.

A product, alongside it’s variants, defines what a System Operator is procuring. Adding further details like who is procuring it and when/how they are procuring creates an individual Sub-market.

By aligning product definitions, the rule simplifies access for Flexibility Service Providers (FSPs) and supports interoperability across DNOs.

### Product Definition Requirements

The rule defines five core DNO products and twelve variants using a structured set of parameters including payment structure, availability mechanisms, and utilisation expectations

All DNOs must use the five standard products and their defined variants for at least 80% of their tendered and procured volume.

DNOs must confirm the products used across their sub-markets back to the Market Facilitator, who will track the procured and tendered volumes via data the DNOs have already published in accordance with License condition 31E.

We believe the impact of these requirements to be:

| Impact on System Operators | Impact on FSPs |
|---|---|
| SOs must align product definitions and limit use of non-standard products. They must report implementation status and catalogue data. | FSPs benefit from simplified access and consistent product expectations across DNOs. |

### Implementation monitoring requirements

The key requirements are laid out below. A view across the rules is available in our deadline tracker.

| Category | Requirement | Trigger for data submission | What we will do with it |
|---|---|---|---|
| Implementation tracking | Basic tracking of implementation status and target date | 31/08/2026 (20 working days after the published date). | Track whether implementation is on track via our Implementation tracker. |
| Flexibility Market Catalogue data | Confirmation of product use and parameter alignment | Within 10 days of change | Provide an overview of the sub-market and the market as a whole via the Flexibility Market Catalogue. |
| Effectiveness monitoring data | KPI tracking use of standard products in tenders and contracts | 21/06/2027 (15 working days after the first Reporting Period)<br>Monthly reporting via data submitted for FMR-DDR | Assess market alignment and identify areas for improvement via our Effectiveness Monitoring Report |

### Derogations against this rule

The following derogations are in place:

| Who | What | For how long | Why |
|---|---|---|---|
| SSEN | The full requirements for LMA Interim Payment Service | Until 01/02/2027 | To prevent blockers to LMA Interim Service settlement |

## 1. Applicability of this Flexibility Market Rule

This Flexibility Market Rule applies to all System Operator Sub-Markets within the Market Facilitator’s scope. Innovation trials are not bound by this Flexibility Market Rule.

All System Operators shall provide the data set out in section 3 no later than the timings also set out in section 3.

Variations to this rule are only permitted with an approved Derogation from the Market Facilitator.

The core dates for this Flexibility Market Rule are laid out below.

**Table 1: Flexibility Market Rule dates**

| Parameter | Value |
|---|---|
| Published Date | 25/08/2026 |
| Implementation Date | 31/03/2027 |
| End Date | - |

#### Explainer: What is a Sub-Market?

This section is provided as guidance to the Flexibility Market Rule. Therefore, it is not legally binding and falls outside of the formal change management process.

A Sub-Market means a specific segment of the overall Flexibility Market, distinguished by a specific System Operator, procuring a specific Product within a specific time period.

A Sub-market may be built of multiple distinct geographic zones, operating in different directions, clearing different volumes at different prices.

The diagram below visualises the definition.

*[Diagram/image in the original web page was not captured in the copy-paste.]*

DTU means Demand Turn Up, GTD means Generation Turn Down.

DTD means Demand Turn Down, GTU means Generation Turn Up.

## 2. Product Definitions

### 2.1 Product definition parameters

The parameters that define a Product are:

**Table 2: Product definition parameters** 
| Purpose | Parameter Name | Description | Options |
|---|---|---|---|
| Structure | Payment structure | How the service is structured (i.e. what is the DNO asking of the Flexibility Service Provider) | Utilisation Only<br>Availability and Utilisation |
|  | When Prices are set (procurement timescales) | Time before use that prices are determined | At Trade<br>Operational |
| Availability | Availability request mechanism | How availability is requested from providers | Request initiated by DNO<br>Request Initiated by Flexibility Service Provider |
|  | Availability Acceptance timing | When availability is accepted by the DNOs | At trade<br>After trade |
|  | Availability Refinement timing | Can the DNO refine the availability required? If so, when. This determines what availability payments are due. | Yes<br>No |
|  | Availability changes allowed? | Can Flexibility Service Providers change their availability declaration post acceptance? | Yes<br>No |
|  | Minimum aggregate unit size | The minimum volume requirement for provision of availability | e.g. 50kW, 1MW, N/A |
|  | Partial availability acceptance possible? | Whether the DNO can accept a portion of the offered volume | Yes<br>No |
|  | Time variable availability volumes allowed? | Can the Flexibility Service Provider provide different volumes for availability for the different periods within the availability window? | Yes<br>No |
|  | Availability Payment unit | The Units used for Availability Payments | £/MW/h<br>£/MWh<br>£/h |
|  | Availability period | The unit of time considered for Availability Instructions | Electricity Forward Agreement (EFA) blocks<br>Settlement Periods<br>Minutes |
| Utilisation | Utilisation Payment unit | The Units used for Utilisation Payments | £/MWh<br>£/MW/season |
|  | Utilisation period | The unit of time considered for Utilisation Instructions | Electricity Forward Agreement (EFA) blocks<br>Settlement Periods<br>Minutes |
|  | Delivery expectation | How the Flexibility Service Provider is expected to respond to a utilisation instruction | Continuous (a sustained delivery over the entire utilisation window)<br>Peak Delivery (targeting the maximum response that can be delivered within the window)<br>Maximum generation cap |
|  | Maximum response time | Time from Utilisation Instruction to full output | N/A<br>15mins<br>2 mins |
|  | Payments during response time? | Are Flexibility Service Providers paid during the response time | Yes<br>No |
|  | Minimum utilisation time | The minimum time a unit can be instructed for | 60 minutes (Hour)<br>30 minutes (Half Hour) |
|  | Minimum utilisation volume | The minimum volume that can be instructed | Measured in kW |
|  | Utilisation instruction timings | Timeframes in which utilisation Instructions are communicated. | At trade<br>Operational<br>Real Time |
|  | Partial utilisation instruction possible? | Whether the DNO can instruct a portion of the available volume | Yes<br>No |
|  | Time variable utilisation volumes allowed? | Can the DNO vary the utilisation instruction for the different periods within the availability window? | Yes<br>No |

*[Table rebuilt from a flattened copy-paste; each option is on its own line in the Options column. The Purpose label is shown on the first row of each group.]*

### 2.2 Standard DNO products

The five standard DNO products (Scheduled Utilisation, Peak Reduction, Operational Utilisation, Scheduled Availability + Operational Utilisation, Variable Availability + Operational Utilisation) and twelve variants are defined in the table below.

**Table 3: Standard DNO products (and variants)** 
| Purpose | Parameter Name | Scheduled Utilisation (SU) | Peak Reduction (PR) | Operational Utilisation: 2 min (OU-2) | Operational Utilisation: 15 min (OU-15) | Scheduled Availability + Operational Utilisation: 2 min (SA OU-2) | SA + OU: 15 min (SA OU-15) | SA + OU: Day ahead (SA OU-DA) | SA + OU: Week ahead (SA OU-WA) | Variable Availability + Operational Utilisation: 2 min (VA OU -2) | VA + OU: 15 min (VA OU-15) | VA + OU: Day ahead (VA OU-DA) | VA + OU: Week ahead (VA OU-WA) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Structure | Payment Structure | Utilisation Only | Utilisation Only | Utilisation Only | Utilisation Only | Availability and Utilisation | Availability and Utilisation | Availability and Utilisation | Availability and Utilisation | Availability and Utilisation | Availability and Utilisation | Availability and Utilisation | Availability and Utilisation |
| Structure | When Prices are set [procurement timescales] | At trade | At trade | At trade | At trade | At trade | At trade | At trade | At trade | At trade | At trade | At trade | At trade |
| Availability | Availability Request Mechanism | N/A | N/A | N/A | N/A | Request initiated by DNO | Request initiated by DNO | Request initiated by DNO | Request initiated by DNO | Request initiated by DNO | Request initiated by DNO | Request initiated by DNO | Request initiated by DNO |
| Availability | Availability Acceptance timing | N/A | N/A | N/A | N/A | At trade | At trade | At trade | At trade | At trade | At trade | At trade | At trade |
| Availability | Availability Refinement timing | N/A | N/A | N/A | N/A | Not allowed | Not allowed | Not allowed | Not allowed | Week Ahead | Week Ahead | Week Ahead | Month Ahead |
| Availability | Availability Changes Allowed? | N/A | N/A | N/A | N/A | No | No | No | No | No | No | No | No |
| Availability | Minimum Aggregate Unit Size | - | - | - | - | - | - | - | - | - | - | - | - |
| Availability | Partial Availability Acceptance Possible? | - | - | - | - | - | - | - | - | - | - | - | - |
| Availability | Time Variable Availability Volumes Allowed? | - | - | - | - | - | - | - | - | - | - | - | - |
| Availability | Availability Payment unit | N/A | N/A | N/A | N/A | £/MW/H | £/MW/H | £/MW/H | £/MW/H | £/MW/H | £/MW/H | £/MW/H | £/MW/H |
| Availability | Availability Period | N/A | N/A | N/A | N/A | Settlement Periods | Settlement Periods | Settlement Periods | Settlement Periods | Settlement Periods | Settlement Periods | Settlement Periods | Settlement Periods |
| Utilisation | Utilisation Payment unit | £/MWh | £/MWh | £/MWh | £/MWh | £/MWh | £/MWh | £/MWh | £/MWh | £/MWh | £/MWh | £/MWh | £/MWh |
| Utilisation | Utilisation Period | Settlement Periods | Settlement Periods | Minutes | Minutes | Minutes | Minutes | Minutes | Minutes | Minutes | Minutes | Minutes | Minutes |
| Utilisation | Delivery Expectation | Continuous | Peak Delivery | Continuous | Continuous | Continuous | Continuous | Continuous | Continuous | Continuous | Continuous | Continuous | Continuous |
| Utilisation | Maximum Response Time | N/A | N/A | 2 mins | 15 mins | 2 mins | 15 mins | N/A | N/A | 2 mins | 15 mins | N/A | N/A |
| Utilisation | Payments during response time? | No | No | No | No | No | No | No | No | No | No | No | No |
| Utilisation | Minimum Utilisation Time | 30 mins | 30 mins | 30 mins | 30 mins | 30 mins | 30 mins | 30 mins | 30 mins | 30 mins | 30 mins | 30 mins | 30 mins |
| Utilisation | Minimum Utilisation Volume | - | - | - | - | - | - | - | - | - | - | - | - |
| Utilisation | Utilisation Instruction Timings | At trade | At trade | Real Time | Real Time | Real Time | Real Time | Operational - Day Ahead | Operational- Week Ahead | Real Time | Real Time | Operational - Day Ahead | Operational- Week Ahead |
| Utilisation | Partial Utilisation Instruction possible? | - | - | - | - | - | - | - | - | - | - | - | - |
| Utilisation | Time Variable Utilisation Volumes Allowed? | - | - | - | - | - | - | - | - | - | - | - | - |

*[Table rebuilt from a flattened copy-paste. In the source the product names form a two-level header: Operational Utilisation, Scheduled Availability + Operational Utilisation (SA + OU) and Variable Availability + Operational Utilisation (VA + OU) each span their variant columns. The combined names are shown here.]*

Null values (-) indicate that there is no aligned requirements for this parameter across DNOs

#### Commentary

This section is provided as guidance to the Flexibility Market Rule. Therefore, it is not legally binding and falls outside of the formal change management process.

Many parameters had 2 states under the Open Networks definitions: an interim and end state. For this first version, we have removed the end state, as there was no clear route to implementation. These may be added back into future versions

## 3. Market Information

### 3.1 Implementation tracking

The DNOs must provide the Market Facilitator with the data set out in Table 4 for each Sub-Market in scope of this rule. The data provided should accurately reflect their implementation of the rule within each of each Sub-Market.

The expected values required for compliance are also set out in Table 4.

Initial data shall be sent no later than 20 working days after the Published Date of this Flexibility Market Rule.

Updates shall be sent as soon as reasonably practical, and no later than 10 working days after any changes to the values.

Elexon reserves the right to publish this data within its Implementation Tracker.

**Table 4: Implementation tracking requirements**

| Parameter | Required value (per Sub-Market) |
|---|---|
| Implementation Status | Dependent on date:<br>Before Implementation Date: Not yet started, Implementing, Paused, Implemented<br>Between Implementation Date and End Date: Implemented<br>After End Date: Superseded |
| Target Implementation Date | No later than Implementation Date |

*[The header row of this table begins with the reference FMR-PD in the source.]*

### 3.2 Flexibility Market Catalogue data

The DNOs must update the Market Facilitator with the data set out in Table 5 below for each Sub-Market in scope of this Flexibility Market Rule. This should accurately reflect their implementation of each Sub-Market.

The expected values required for compliance are also set out in Table 1.

Initial data shall be sent no later than the Implementation Date of this Flexibility Market Rule.

Updates shall be sent as soon as reasonably practical, and no later than 10 working days after any changes to the values.

System Operators shall also publish this information themselves.

Elexon reserves the right to publish this data within its Flexibility Market Catalogue.

**Table 5: Sub-Market definitions** 
| Parameter | Description | Required values |
|---|---|---|
| Product | Which product is in use within the Sub-Market | Scheduled Utilisation (SU); Peak Reduction (PR);<br>Operational Utilisation - 2 min (OU-2);<br>Operational Utilisation - 15 min (OU-15);<br>Scheduled Availability + Operational Utilisation - 2 minutes (SA OU-2);<br>Scheduled Availability + Operational Utilisation - 15 minutes (SA OU-15);<br>Scheduled Availability + Operational Utilisation - Day ahead (SA OU-DA);<br>Scheduled Availability + Operational Utilisation - week ahead (SA OU-WA);<br>Variable Availability + Operational Utilisation - 2 minutes (VA OU-2);<br>Variable Availability + Operational Utilisation - 15 minutes (VA OU-15);<br>Variable Availability + Operational Utilisation - Day ahead (VA OU-DA);<br>Variable Availability + Operational Utilisation - week ahead (VA OU-WA); |
| Each parameter set out in Table 3. This should confirm the implementation of the products as defined and confirm the status of the parameters where no aligned values are currently set. |  |  |

*[The second row of Table 5 appears as a single cell in the source; it is shown in the first column.]*

#### Commentary

This section is provided as guidance to the Flexibility Market Rule. Therefore, it is not legally binding and falls outside of the formal change management process.

We acknowledge there is overlap between these definitions and those set out in the “Sub-Market definition” Flexibility Market Rule (FMR-SMD). We will look to review this and remove duplication in due course. In the meantime, DNOs are expected to provide the data in duplicate for both rules.

### 3.3 Effectiveness monitoring

The following metrics shall be used to assess the effectiveness of the rule.

The DNOs must provide the Market Facilitator with any Additional Input Data as set out in Table 6 below for each Sub-Market in scope of this rule. The data provided should accurately reflect their implementation of the rule within each of each Sub-Market.

The expected values minimum required values for compliance, if any, are also set out in Table 6.

Initial Additional Input Data shall be sent no later than 20 working days after the Implementation Date of this Flexibility Market Rule.

Additional Input Data shall be sent in accordance with the Cadence set out in in Table 6.

Updates to Additional Input Data shall be sent as soon as reasonably practical, and no later than 10 working days after any changes to the values.

Elexon reserves the right to publish this data within its Implementation Tracker.

**Table 6: Effectiveness monitoring metrics** 
| Field | Metric 1 | Metric 2 |
|---|---|---|
| Description | Percentage of DNO tenders in reporting year using standard products | Percentage of DNO contracts in reporting year using standard products |
| Why are we tracking this? | To understand the volume of standard products being put out to the market by the DNOs | To understand the volume of standard products being bought from the market by the DNOs |
| Cadence | Monthly | Monthly |
| Data source | Existing Data – DNO Data Reporting Rule: Total Tendered in Reporting Period (Sum of standard products/Sum of all products)<br>Additional Input Data - None | Existing Data - DNO Data Reporting Rule: Total Contracted in Reporting Period (Sum of standard products/Sum of all products)<br>Additional Input Data - None |
| What does good look like | 100% | 100% |
| Minimum Requirement | >80% | >80% |

## 4. Glossary

The following definitions are specific to this Flexibility Market Rule. These are supplemented by the definitions in the Market Facilitator Glossary. If there is an inconsistency between definitions, the definition in this document shall prevail.

| Term | Meaning |
|---|---|
| Continuous | a sustained delivery over the entire utilisation window |
| Peak Delivery | targeting the maximum response that can be delivered within the window |
| Reporting Period | in respect of data submitted under section 3.4 of FMR-DDR, the period of time to which the submitted data should relate. The first Reporting Period shall be 01/04/2027 to 31/05/2027 inclusive. Each subsequent Reporting Period shall be a calendar month, beginning on the first day of that month and ending on the last day of that month. More frequent submissions by a System Operator shall not create additional Reporting Periods. |

## FMR: Product Definitions - Amendment record

*This section is provided as guidance to the Flexibility Market Rule. Therefore, it is not legally binding and falls outside of the formal change management process.*

| Version | Published Date | Document Status | Description of Changes | Change Proposal Reference | Market Facilitator Decision Report Ref |
|---|---|---|---|---|---|
| 1.0 | 12/12/2025 | Final | Document Published |  |  |
| 2.0 | 04/02/2026 | Final | Housekeeping changes | CP002 | CP002 |
| 2.1 | 17/02/2026 | Final | Derogation Rule added |  |  |
| 3.2 | 12/05/2026 | Final | Revision of the Rule | CP003 | CP003 |
| 4.2 | 25/08/2026 | Final | Revision of Implementation Monitoring Requirements | CP005 | CP005 |

## Annex 1: Associated meta-data

*This annex is provided as guidance to the Flexibility Market Rule. Therefore, it is not legally binding and falls outside of the formal change management process.*

| Field | Value |
|---|---|
| Identifier | FMR-PD |
| Title | Product definitions |
| Type | Flexibility Market Rule |
| Collection | Sub-Market Alignment |
| Audience | DNOs, Flexibility Service Providers |
| Expertise | Market Design |
| Owner | Market Facilitator |
| Expected benefit | Deliver aligned flexibility Products across DNOs to:<br>- reduce variation across DNOs<br>- simplify access for Flexibility Service Providers |
| Related end-to-end process reference | E.1 Define Sub-market |
| References | FMR-SMD, FMR-DDR |
| IsReferencedBy | FMR-SMD, FMR-SBM |
| Published version number | 4.2 |
| Applicability | All DNO Sub-markets |
| Published Date | 25/08/2026 |
| Implementation Date | 31/03/2027 |
| End Date | - |
| Terms of variations | Approved Derogation |
| IsReplacedBy | N/A |
| Replaces | N/A |
| Status | Final |
| Change since last version | Revision of the Rule |

**Description**

**What?**
This rule sets out the 5 standard DNO products (with 12 variants)

**How?**
Core parameters are used to define products. 12 variations of products are defined using those parameters

**Who?**
This rule impact DNOs and how they define products. In turn this impacts the products available to Flexibility Service Providers. It does not cover NESO product

**When?**
This rule comes into force in May 2026

**Why?**
This rule aims to reduce the variation in procurement across DNOs to simplify access, and improve market coordination

*[In the source each question label (How?, Who?, When?, Why?) was glued to the end of the previous answer; the labels have been moved onto their own lines.]*