# Applicable Balancing Services Volume Data (ABSVD) Methodology Statement

> **Source file:** `ABSVD statement.txt` (NESO PDF, copy-pasted)  
> **Coverage:** Extract only. The copy starts part-way through Section 1, at 1.2 "Purpose of Document" (PDF page 7–8), and runs to the end of the document (page 21). The cover page, contents and Section 1.1 are not included.  
> **Converted:** 2026-10-07. Wording kept verbatim from the source copy-paste; only layout artefacts (page headers/footers, line wraps, website navigation, broken tables) were cleaned up. Notes in *[italic square brackets]* are editorial.

---

## Section 1 (partial) *[the Section 1 heading is not in the extract]*

### 1.2 Purpose of Document

This document sets out the Applicable Balancing Services Volume Data (ABSVD) Methodology that NESO is required to establish in accordance with Standard Condition C9 of the NESO ESO Licence.

The purpose of this Statement is to outline the process NESO takes to determine and provide the volumes of Applicable Balancing Services which are to be taken into account in determining ABSVD under the BSC.

Balancing Services are defined in the NESO ESO Licence and described in more detail in the Procurement Guidelines, which NESO is required to establish in accordance with Standard Condition C9 of the NESO ESO Licence.

In general, Balancing Services deemed to be applicable will be those services required by NESO for economic operation of the transmission system, that result in the service provider being exposed to imbalance charges whilst assisting in system balancing.

For the avoidance of doubt:

- a. NESO is responsible for aggregating Applicable Balancing Services Volumes per Settlement Period (SP) and submitting those volumes to Elexon.
- b. Elexon is responsible in accordance with BSC section T, part 4 of using Quantitative Ancillary Services (QAS) data (along with Bid-Offer acceptance (BOA), Transmission Loss Multipliers, Contracted Positions) to determine Balancing Mechanism (BM) imbalance volumes, and imbalance settlement.
- c. Elexon is responsible in accordance with BSC, Annex S-2 to correct Balancing Responsible Party (BRP) imbalance positions.

## 2. Applicable Balancing Services Volume Data (ABSVD) for BM Participants

### 2.1 Definition of BM Unit

BM Units are used as units of trade within the BM. Any energy produced or consumed by the contents of a BM Unit is accredited to that BM Unit.

BM Units can be classed as either a Primary BM Unit or a Secondary BM Unit. The definition of Primary BM Unit and Secondary BM Unit shall have the same meaning given to them by Elexon in the documents related to the BM Units (e.g. BM-Units-v16.0.docx).

The BM Units are visible in Balancing Mechanism data by BMU view | Insights Solution *[hyperlink in original]*

### 2.2 Basis of Calculation for BM ABSVD

The ABSVD is specified in Section Q, Paragraph 6.4 of the BSC and consists of QASij, being the ABSVD in respect of BM Unit i, in Settlement Period j, determined in accordance with this Statement.

The following Applicable Balancing Services will be included in the calculation of the ABSVD:

**Table 1 - BM ABSVD Volumes Supplied to Elexon**

| Balancing Service | Data Volume Source |
|---|---|
| Frequency Response Services (Dynamic Containment (DC) High/Low, Dynamic Moderation (DM) High/Low and Dynamic Regulation (DR) High/Low) | Response Energy Volumes computed in accordance with clause 4.1.3.9A of the CUSC - SECTION 4 |
| Commercial Intertrips | Volume Computed in accordance with the Commercial Services Agreement (CSA) |
| System to Generator Operational Intertripping | Export Restricted Volume computed from the time of the trip to end of the BM Window |
| Maximum Generation (MaxGen) Service | Service Volume computed in accordance with clause 4.2.5 of the CUSC - SECTION 4 |
| Demand Flexibility Service (DFS)* | Delivered Volume (See Note 4) |

\*DFS - Non-Balancing Mechanism (Non-BM) Half Hourly (HH) settled Domestic consumers whose Metering System Identifier (MSID) is signed up to provide DFS with the supplier that has an ELEXON BM Unit Identifier (ID).

In reference to the DFS BM ABSVD volumes supplied to Elexon, the reporting mechanism describes the volumes delivered by a Non-BM provider, without its own individual BM Unit dispatched by NESO outside the BM. If NESO dispatches a provider outside the BM who has its own BM Unit, then the ABSVD volumes will be submitted via the BM ABSVD applied process and allocated to the relevant BM Unit.

For the avoidance of doubt, for the following services NESO submit BOA instructions to Elexon via a process separate to the ABSVD process:

**Table 2 - BOA Instruction Data Supplied to Elexon**

| Balancing Service | Data Volume Source |
|---|---|
| Short Term Operating Reserve (STOR) | BOA Instruction |
| Negative Balancing Reserve (NBR) | BOA Instruction |
| Positive Balancing Reserve (PBR) | BOA Instruction |
| Negative Quick Reserve (NQR) | BOA Instruction |
| Positive Quick Reserve (PQR) | BOA Instruction |
| Negative Slow Reserve (NSR) | BOA Instruction |
| Positive Slow Reserve (PSR) | BOA Instruction |

### 2.3 ABSVD Provision for Applicable Balancing Services from BM Providers

ABSVD will be submitted in accordance with BSC, Section Q, Paragraph 6.4. This entails the submission of ABSVD within two Business Days following the relevant Settlement Day.

The ABSVD data is sent to Elexon to be used in their imbalance calculation process as specified in Section T, Paragraph 4.3 of the BSC and is displayed under Balancing Services Volume on Balancing Mechanism data by BMU view | Insights Solution. *[hyperlink in original]*

### 2.4 Re-submission of ABSVD for Applicable Balancing Services from BM Providers

In the event that an error or incompleteness is identified in the submitted ABSVD, the data will be investigated, re-calculated and re-submitted to Elexon, as soon as reasonably practicable, once the corrected data is available.

Any queries related to the calculation and submission of ABSVD should be addressed to settlement.queries@neso.energy

### 2.5 Disputes for BM ABSVD

A dispute arises where the Lead Party of the relevant BM Unit disagrees with the value of QASij notified by NESO. Where such a dispute arises, a representative of NESO and each BSC Party concerned who has authority to resolve the dispute shall meet (either in person or virtually) within 10 Business Days of a request by either party (or within such longer period as may be agreed, acting reasonably) and seek to resolve it. If the parties to the dispute are unable to resolve it within 10 Business Days of the meeting (or within such longer period as they may agree within that initial 10 Business Day period, both parties acting reasonably as to the length of the period), then the parties’ obligations under this paragraph to undertake such discussions shall no longer apply in relation to that dispute. Either party may then refer the dispute to arbitration pursuant to the rules of the London Court of Arbitration in force from time to time.

The laws of England shall be the proper law of reference to arbitration under this paragraph and in particular (but not so as to derogate from the generality of the foregoing) the provisions of the Arbitration Act 1996 shall apply to any such arbitration wherever it or any part of it shall be conducted.

Any arbitrator or panel of arbitrators appointed under this Paragraph 3 shall determine such issues as are referred to him or them consistently with any determination by the Authority, whether or not relating to the same or different facts.

For the avoidance of doubt, a party may only raise a dispute in respect of QASij where they are Lead Party of the relevant BM Unit.

## 3. Applicable Balancing Services Volume Data (ABSVD) for Non-BM Providers

### 3.1 Definition of Non-BM Provider

Non-BM Provider refers to a provider that is dispatched by NESO outside the BM. If a company supplies a Balancing Service to NESO, but its units are not registered as BM Units, these are considered as Non-BM Units for the purposes of ABSVD calculation and submission to Elexon.

### 3.2 Basis of calculation for Non-BM providers

The following Applicable Balancing Services will be included in the calculation of the ABSVD:

**Table 3 - Non-BM ABSVD Volumes Supplied to Elexon**

| Unit Type | Balancing Service | Data Volume Source |
|---|---|---|
| Non-BM | Short Term Operating Reserve (STOR) | Delivered Volume restricted to Instructed Volume (see Note 1) |
| Non-BM | Fast Reserve (FR) | Delivered Volume restricted to Instructed Volume (see Note 1) |
| Non-BM | Negative Quick Reserve (NQR) | Delivered Volume restricted to Instructed Volume (see Note 1) |
| Non-BM | Positive Quick Reserve (PQR) | Delivered Volume restricted to Instructed Volume (see Note 1) |
| Non-BM | Negative Slow Reserve (NSR) | Delivered Volume restricted to Instructed Volume (see Note 1) |
| Non-BM | Positive Slow Reserve (PSR) | Delivered Volume restricted to Instructed Volume (see Note 1) |
| Non-BM | MW Dispatch (MWD) | Delivered Volume restricted to Instructed Volume (see Note 1) |
| Non-BM Assets HH settled* | Local Constraint Market (LCM) | Delivered Volume restricted to Instructed Volume (see Note 1) |
| Non-BM<br>Industrial and Commercial consumers (except for Industrial and Commercial Consumers in Profile Class 3 and 4)<br>Renewable Assets | Demand Flexibility Service (DFS) | Delivered Volume |
| Non-BM | Frequency Response Services (Dynamic Containment (DC) High/Low, Dynamic Moderation (DM) High/Low and Dynamic Regulation (DR) High/Low) | Expected Volume |

*[Table rebuilt from a flattened copy-paste. Cell boundaries in the DFS row were inferred from the column order.]*

**Note 1:** If additional energy is shown as a positive value then Min(Delivered MWh, Instructed MWh), if a reduction in energy to the system is shown as a negative value then Max(Delivered Volume MWh, Instructed MWh)

**Note 2:** Providing the necessary data to meet the NESO ABSVD process requirements, will be part of the contract terms for each Applicable Balancing Service.

**Note 3:** NBM Providers can see the monthly volumes submitted for ABSVD in the utilisation files for the appropriate service in the Ancillary Services Backing Reports Guide in the following location: Settlements | National Energy System Operator *[hyperlink in original]*

**Note 4:** ABSVD volumes are calculated as follows:

- For Frequency response (DC/DM/DR), ABSVD expected volumes are calculated using an initial 1MW calculation to determine difference between Actual and Target Frequency. This is then multiplied by the tendered MW value to give the expected volume.
- For DFS the volumes reported are the actual delivered metered volumes.
- For all other services in the table, volumes reported are actual metered but capped by instruction. Therefore, always reporting the minimum of expected and delivered.

\*LCM - NESO submit ABSVD to Elexon with respects to eligible Non-BM providers delivered HH-settled volumes, where it is feasible to do so. With the optionality to opt out of ABSVD for eligible Non-BM providers and calculation in accordance with the relevant CSA.

### 3.3 Registration of Metering System Identifier (MSID) pairs

As a condition of Elexon’s acceptance of the ABSVD volumes (calculated and submitted by NESO), NESO is required to notify Elexon of all MSID Pairs that may be used for the provision of Non-BM Unit ABSVD, before it sends MSID Pair Delivered Volumes. In accordance with Section Q, 6.4.8 of BSC, the high-level requirements of registration of MSID pairs with Elexon are:

- The Non-BM Providers submit via the relevant customer registration system for each service the information about MSID pairs for every unit that provides a Non-BM Service
- NESO submit to Elexon the data received from the Non-BM providers
- Elexon confirm to NESO the eligibility and registration of MSID pairs

Note: A failure to register MSID pairs may result in a unit being disqualified from providing a service.

### 3.4 ABSVD provision for Applicable Balancing Services from Non-BM Providers

For the purpose of calculation and submission of ABSVD volumes to Elexon, the following steps are required to be undertaken:

- NESO calculate energy volumes per Non-BM units as specified in the Non-BM ABSVD Volumes Supplied to Elexon table
- Providers allocate the energy volume to four decimal places for each MSID pair via the relevant customer registration system for each service
- The volume allocation against registered MSID pairs is validated via the relevant customer registration system for each service
- The ABSVD allocated volumes, in respect of any MSID pair and Settlement Period within a Settlement Day expressed in MWh, will be submitted by NESO to Elexon

Note: If an energy allocation is not given by the registered service provider, a default allocation will be conducted, dividing the energy volume equally between MSIDs registered to the unit providing the service.

In accordance with BSC, Section Q, 6.4 MSID Pair Delivered Volume shall be sent to the SVAA by the fifteenth day after such Settlement Day to the extent such data has been received by the NESO, and in any event by the forty fifth day after such Settlement Day, as stated in 6.4.7, b.

### 3.5 Re-submission of ABSVD for Applicable Balancing Services from Non-BM Providers

In the event that an error or incompleteness is identified in the submitted ABSVD, the data will be investigated, re-calculated and re-submitted to Elexon, as soon as reasonably practicable, once the corrected data is available but not later than the Final Reconciliation Run.

Any queries related to the calculation and submission of ABSVD should be addressed to settlement.queries@neso.energy

### 3.6 Disputes for Non-BM ABSVD

#### 3.6.1 Disputes relating to Non-BM Provider volumes passed to Elexon

A dispute may arise relating to Non-BM Provider volumes passed to Elexon. Where such a dispute arises, a representative of NESO and the BSP concerned who has authority to resolve the dispute shall meet (either in person or virtually) within 10 Business Days of a request by either party (or within such longer period as may be agreed, acting reasonably) and seek to resolve it. If the parties to the dispute are unable to resolve it within 10 Business Days of the meeting (or within such longer period as they may agree within that initial 10 Business Day period, both parties acting reasonably as to the length of the period), then the parties’ obligations under this paragraph to undertake such discussions shall no longer apply in relation to that dispute. Either party may then refer the dispute to arbitration pursuant to the rules of the London Court of Arbitration in force from time to time.

The laws of England shall be the proper law of reference to arbitration under this paragraph and in particular (but not so as to derogate from the generality of the foregoing) the provisions of the Arbitration Act 1996 shall apply to any such arbitration wherever it or any part of it shall be conducted.

Any arbitrator or panel of arbitrators appointed under this Paragraph 3 shall determine such issues as are referred to him or them consistently with any determination by the Authority, whether or not relating to the same or different facts.

For the avoidance of doubt, a party may only raise a dispute in respect of non-BM ABSVD where they are the contracted BSP for the service.

In the event that an error is identified in the ABSVD, the data will be corrected and re-submitted, as soon as reasonably practicable, but not later than the Final Reconciliation Run, once the corrected data is available.

#### 3.6.2 Disputes relating to ABSVD volumes applied to Supplier Energy Accounts

These will be dealt with via Elexon through BSC Trading Disputes processes (BSCP11). Where the dispute requires investigation into the source data provided to Elexon, NESO will seek to provide supporting information to resolve this matter.

In the event that an error is identified in the ABSVD, the data will be resubmitted and corrected, as soon as reasonably practicable, but usually not later than the Final Reconciliation Run, once the corrected data is available.

If a Trading Dispute relating to ABSVD is upheld, NESO may be required to resubmit ABSVD after Reconciliation Final (up to DF at D+28 months, or potentially up to D+40 months for an Extra Settlement Determination).
