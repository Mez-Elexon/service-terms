# Flexibility Market Rule: Sub-Market definitions (FMR-SMD) V2.1

> **Source file:** `FMR-SMD - Sub-Market definitions V2.txt`  
> **Published Date:** 17/02/2026  
> **Converted:** 2026-10-07. Wording kept verbatim from the source copy-paste; only layout artefacts (page headers/footers, line wraps, website navigation, broken tables) were cleaned up. Sections the source marks as guidance are not legally binding. Notes in *[italic square brackets]* are editorial.

---


Sections 1, 2, 3 and 4 form the legally binding Flexibility Market Rule.

Defined terms capitalised in this document shall have the meaning given in Section 4.

## Summary of Sub-Market definitions Flexibility Market Rule

This section is provided as guidance to the Flexibility Market Rule. Therefore, it is not legally binding and falls outside of the formal change management process.

### Context

This rule establishes a common framework for defining and cataloguing individual Sub-Markets within the wider flexibility market. It translates the Open Networks “Products technical requirements document” into a set of standardised Sub-Market definitions, supplemented by parameters from related rules.

The aim is to provide clarity on how Sub-Markets are designed and to enable simple presentation and consistent comparison and alignment across the different Sub-Markets in our Flexibility Market Catalogue. The rule applies to all Sub-Markets within the Market Facilitator’s scope and comes into force in February 2026.

### Sub-Market Definition Requirements

The rule sets out a number of parameters that define a Sub-Market. This includes elements such as the buyer, payment structure, procurement method, pre-qualification criteria, metering requirements, platforms, availability, utilisation, settlement, and baselining. System operators are obligated to provide the Market Facilitator with these parameters for each of their Sub-Markets, to be shared with industry via the Flexibility Market Catalogue.

We believe the impact of these requirements to be:

| Impact on System Operators | Impact on FSPs |
|---|---|
| System Operators must maintain these parameters for each of their Sub-Markets. | FSPs will be able to better understand the different markets via the Flexibility Market Catalogue. |

### Implementation monitoring requirements

The key requirements are laid out below. A view across the rules is available in our deadline tracker.

| Category | Requirement | Trigger for data submission | What we will do with it |
|---|---|---|---|
| Implementation tracking | Basic tracking of implementation status and target date | From 14/01/2026 (20 working days after the published date).<br>Within 10 days of change | Track whether implementation is on track via our Implementation tracker |
| Flexibility Market Catalogue data | Confirmation of Sub-Market parameter alignment and updates | From 06/02/2026.<br>Within 10 days of change | Provide an overview of Sub-Markets via the Flexibility Market Catalogue. |
| Effectiveness monitoring data | N/A | - | - |

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

## 2. Sub-Market Definitions

### 2.1 Sub-Market definition parameters

The parameters that define a Sub-market are:

**Table 2: Sub-market definition parameters**

| Purpose | Parameter Name | Description | Required values for DNO Sub-Markets | Required values for NESO Sub-Markets |
|---|---|---|---|---|
| User | Buyer | Who is the buyer of the services | - | NESO |
| Strategic Direction | Strategic Direction | The high-level plan for the service in the near future. | - | - |
| Structure | Payment Structure | How the service is structured (i.e. what is the SO asking of the FSP) | As set out in the Product definitions rule (FMR-PD) | - |
| Structure | Procurement Method | The type of mechanism used to procure the service | - | - |
| Structure | When Prices are Set | Time before use that prices are determined | As set out in the Product definitions rule (FMR-PD) | - |
| Structure | Generation/demand turn down service or generation/demand turn up service? | Does the service require the provider to export or import power to the grid | - | - |
| Pre-qualification | Required to be a Balancing and Settlement Code (BSC) Party? | The rules and governance arrangements for electricity Balancing and Settlement in Great Britain. | No | - |
| Pre-qualification | Non-BM Party Accessible? | Can you participate without being a Balancing Mechanism Party? | - | - |
| Pre-qualification | Asset Location Grouping Requirement? | Requirement for where multiple assets within a unit must be located | per specific CMZ | - |
| Pre-qualification | Aggregation /Virtual Lead Party (VLP) Route Available? | The option of having more than a single asset within a unit | Yes | - |
| Pre-qualification | Minimum MW Delivery Required (also referred to as Minimum Aggregated Unit Size) | The minimum MW capacity that a unit must exceed to enter the service | As set out in the Product definitions rule (FMR-PD) under "Minimum Aggregate Unit Size" | - |
| Pre-qualification | Unit volume cap | Maximum amount of MW volume per unit registered in the service | - | - |
| Pre-qualification | Open to Flexible Connections or similar? | If the asset's network connection has 'restrictions' (eg a Curtailable, Flexible or Ramped connection), can they participate? | - | - |
| Pre-qualification | Open to Planned Connections? | Identifying when assets must be connected to the network before participating in flexibility market. | - | - |
| Metering | Asset metering permitted? (vs boundary point metering system) | What type of metering is permitted? Some services only allow boundary meter data whilst others allow metering behind the boundary i.e. asset metering | - | - |
| Metering | Operational Metering Required? | A live feed to the relevant System Operator control room to measure providers live service delivery | - | - |
| Metering | Operational Meter Accuracy Required? | The accuracy rating required of physical meters providing operational metering | - | - |
| Metering | Operational Meter Refresh Frequency | The frequency that the physical meter captures real-time data snapshots | - | - |
| Metering | Operational Metering Latency | Operational metering data must reach relevant System Operator Control Room within this time | - | - |
| Metering | Operational Metering Signal Type | The type of electrical data collected for operational metering | - | - |
| Metering | Performance Meter Refresh Frequency | The frequency that the physical meter captures real-time data snapshots (e.g. 20Hz= 20 snapshots per second) | - | - |
| Platforms | Service Registration Platform | The platform used to register to enter the service | - | - |
| Platforms | Procurement Platform | The platform that providers use to bid into the service and form contracts | - | - |
| Platforms | Operational Platform | The platform for operational instructions (e.g. utilisation declarations or dispatch) |  |  |
| Platforms | Settlement Registration Platform | The platform to register and submit settlement data | - | - |
| Availability | Availability period | the periods in which the service is made available or utilisation is committed | As set out in the Product definitions rule (FMR-PD) | - |
| Availability | Availability Payment Unit | The units used for Availability Payments | As set out in the Product definitions rule (FMR-PD) | - |
| Utilisation | Instruction Notice Period (also referred to as Utilisation Instruction Timings) | Notice given to providers that they will need to respond to an instruction in the immediate future | As set out in the Product definitions rule (FMR-PD)" | - |
| Utilisation | Gate closure | Dispatched before or after gate closure | - | - |
| Utilisation | Delivery Duration (also referred to as Minimum Utilisation Time) | Minimum amount of time that a provider must be able to provide its obligated delivery volume | As set out in the Product definitions rule (FMR-PD) | - |
| Utilisation | Utilisation period | The periods in which the service is made available or utilisation is committed | As set out in the Product definitions rule (FMR-PD) | - |
| Utilisation | Time to respond to instruction | Time to show unit ramping has began | N/A | - |
| Utilisation | Max time to full delivery from Instruction (also referred to as Maximum Response Time) | Time taken from utilisation instruction or triggering event to reach procured volume delivery | As set out in the Product definitions rule (FMR-PD) | - |
| Utilisation | Ramping requirements | The specific requirements of the service in relation to ramping up or down of delivery | N/A | - |
| Utilisation | Maximum Recovery Period | The time between the end of the delivery of one instruction and the start of the delivery of the next instruction | - | - |
| Utilisation | Instruction Trigger | What triggers a request to deliver the contracted volume | Tender result will be seen as instruction<br>OR<br>DNO instruction | - |
| Utilisation | Auction contract length | How long the providers delivery contract lasts | - | - |
| Utilisation | Utilisation Payment Unit | The units used for Utilisation payments | As set out in the Product definitions rule (FMR-PD) | - |
| Settlement & Performance Monitoring | Settlement or Performance Monitoring required? | Identification of any service specific performance monitoring requirements. | Yes | - |
| Baselining | Baselining | Summary of the baselining approach used | As set out in the DNO Baselining rule (FMR-SBM) | - |
| Reporting | EBR Article 18 | Is the sub-market within scope of Electricity Balancing Regulations Article 18? | - | - |

Null values (-) indicate that there is no required value for this parameter.

#### Commentary

This section is provided as guidance to the Flexibility Market Rule. Therefore, it is not legally binding and falls outside of the formal change management process.

We acknowledge there is overlap between these definitions and those set out in the “Product Definition” Flexibility Market Rule (FMR-PD) and the “Metering Requirements and Standards” Flexibility Market Rule (FMR-MR) and the “Standard Baselining Methodology” (FMR-SBM). We will look to review this and remove duplication in due course. In the meantime, DNOs are expected to copy the definition data between both rules.

## 3. Market Information

### 3.1 Implementation tracking

The System Operators must provide the Market Facilitator with the data set out in Table 3 for each Sub-Market in scope of this rule. The data provided should accurately reflect their implementation of the rule within each of each Sub-Market.

The expected values required for compliance are also set out in Table 3.

Initial data shall be sent no later than 20 working days after the Published Date of this Flexibility Market Rule.

Updates shall be sent as soon as reasonably practical, and no later than 10 working days after any changes to the values.

Elexon reserves the right to publish this data within its Implementation Tracker.

**Table 3: Implementation tracking requirements**

| Parameter | Required value (per Sub-Market) |
|---|---|
| Implementation Status | Dependent on date:<br>Before Implementation Date: Not yet started, Implementing, Paused, Implemented<br>Between Implementation Date and End Date: Implemented<br>After End Date: Superseded |
| Target Implementation Date | No later than Implementation Date |

*[The header row of this table begins with the reference FMR-SMD in the source.]*

### 3.2 Flexibility Market Catalogue data

The System Operators must update the Market Facilitator with the data set out in Table 4 below for each Sub-Market in scope of this Flexibility Market Rule. This should accurately reflect their implementation of each Sub-Market.

The expected values required for compliance are also set out in Table 4.

Initial data shall be sent no later than the Implementation Date of this Flexibility Market Rule.

Updates shall be sent as soon as reasonably practical, and no later than 10 working days after any changes to the values.

System Operators shall also publish this information themselves.

Elexon reserves the right to publish this data within its Flexibility Market Catalogue.

**Table 4: Sub-Market definitions** 
| Parameter | Description | Required values |
|---|---|---|
| All the parameters set out in Table 2 |  |  |

### 3.3 Effectiveness monitoring

There are no market facilitator metrics for this rule

## 4. Glossary

The following definitions are specific to this Flexibility Market Rule. These are supplemented by the definitions in the Market Facilitator Glossary. If there is an inconsistency between definitions, the definition in this document shall prevail.

| Term | Meaning |
|---|---|
| None used in this document |  |

## FMR: Sub-market Definitions - Amendment record

*This section is provided as guidance to the Flexibility Market Rule. Therefore, it is not legally binding and falls outside of the formal change management process.*

| Version | Published Date | Document Status | Description of Changes | Change Proposal Reference | Market Facilitator Decision Report Ref |
|---|---|---|---|---|---|
| 1.0 | 12/12/2025 | Final | Document Published |  |  |
| 2.0 | 04/02/2026 | Final | Housekeeping change | CP002 | CP002 |
| 2.1 | 17/02/2026 | Final | Derogation Rule added |  |  |