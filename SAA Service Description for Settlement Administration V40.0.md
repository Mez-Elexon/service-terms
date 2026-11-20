# BSC Service Description for Settlement Administration (SAA) V40.0

> **Source file:** `SAA Service Description for Settlem.txt`  
> **Symbol repair:** The source copy-paste turned Symbol-font characters into doubled Latin letters. These were mapped back: SS→Σ, ÎÎ→∈, ÏÏ→∉, ¹¹→≠, ³³→≥, çç→|, åå→Σ (93 replacements). Example: "CBMp = SSj SSiÎÎp CBMij" now reads "CBMp = Σj Σi∈p CBMij".  
> **Effective From Date:** 27/11/2025  
> **Status:** LIVE  
> **Converted:** 2026-10-07. Wording kept verbatim from the source copy-paste; only layout artefacts (page headers/footers, line wraps, website navigation, broken tables) were cleaned up. Notes in *[italic square brackets]* are editorial.

---

Balancing and Settlement Code

BSC Service Description for Settlement Administration

Version 40.0

Date: 27 November 2025

AMENDMENT HISTORY

| Version | Details (in source column order: Date / Description of Change / Mods /Panel/ Committee Refs) |
|---|---|
| 1.0 | 27/03/01<br>Baseline version<br>NETA Programme |
| 2.0 | 21/08/01<br>Incorporated changes for Modification P10<br>S. Francis |
| 2.4 | 05/09/01<br>Issued for Agent review<br>S. Francis |
| 3.0 | 07/01/02<br>Ph–se B – Modifications P8 and P18A<br>S. Francis |
| 4.0 | 13/08/02<br>Release 2 – Modifications P8, P18A (Reporting), P48, P2, CP595, CP598<br>CVA Programme |
| 5.0 | 10/12/02<br>Phase 2A – P61, CP632, CP639, and CP712.<br>Added ‘Interim Initial’ and ‘Interim Information’ in section 1.8<br>A. Bennington |
| 6.0 | 11/03/03<br>P78/P104/P71, plus residual changes arising from CP632 and CP712<br>CVA Programme |
| 7.0 | 24/06/03<br>CVA Programme Jun 03 Release (CP735)<br>CVA Programme |
| 8.0 | 05/11/03<br>CVA Programme Nov 03 Release – P82, P107, CP830<br>CVA Programme |
| 9.0 | 30/06/04<br>CVA Programme Jun 04 Release – CP915, CP916<br>P82 changes removed<br>CVA Programme |
| 10.0 | 03/11/04<br>CVA Programme Nov 04 Release<br>CP974<br>CVA Programme |
| 11.0 | 23/02/05<br>CVA Programme Feb 05 Release<br>CP1091<br>CVA Programme |
| 12.0 | 02/11/05<br>CVA Programme November 05 Release P172<br>CVA Programme |
| 13.0 | 02/11/06<br>BSC Systems November 06 Release P194<br>Change Implementation |
| 14.0 | 01/12/06<br>BSC Systems November 06 Release – P205<br>Change Implementation |
| 15.0 | 26/06/08<br>June 2008 Release – CP1222<br>Change Implementation |
| 16.0 | 26/02/09<br>February 09 Release – CP1255<br>Change Implementation |
| 17.0 | 5/11/09<br>November 09 Release – P217<br>Change Implementation |
| 18.0 | 25/02/10<br>February 10 Release – CP1314<br>Change Implementation |
| 19.0 | 04/11/10<br>November 10 Release – P257<br>Panel |
| 20.0 | 03/11/11<br>November 11 Release – P253<br>Panel |
| 21.0 | 29/11/12<br>November 12 Release – P278<br>ISG138/10 |
| 22.0 | 27/06/13<br>June 13 Release – P285<br>P206/07 |
| 23.0 | 01/08/14<br>ORD005<br>Directed by the Secretary of State |
| 24.0 | 05/11/15<br>November 15 Release – P305<br>ISG172/04<br>November 15 Release – P323<br>P245/06 |
| 25.0 | 12/04/16<br>12 April 2016 – CP1453<br>ISG178/04 |
| 26.0 | 29/06/17<br>June 2017 Release – P321 Self-Governance<br>Panel 245/05<br>June 17 Release – P350<br>ISG194/02 |
| 27.0 | 29/03/19<br>29 March 2019 Standalone Release – P369<br>Panel 285/12 |
| 28.0 | 27/06/19<br>27 June 2019 Release – P367 Self-Governance<br>SVG219/02<br>ISG216/01 |
| 29.0 | 07/11/19<br>November 2019 Release, P386 Self-Governance<br>Panel 291/05 |
| 30.0 | 11/12/19<br>11 December 2019 Standalone Release, CP1517<br>ISG220/01<br>ISG222/03 |
| 31.0 | 27/02/20<br>February 2020 Release - P394 Self Governance<br>P297/07 |
| 32.0 | 01/04/20<br>1 April 2020 Standalone Release- P354, P388<br>ISG227/0 |
| 33.0 | 04/11/21<br>4 November 2021 Standard Release – P399<br>P310/04 |
| 34.0 | 07/12/22<br>07 December 2022 Special Release P448<br>P330C/02 |
| 35.0 | 23/02/23<br>23 February 2023 Standard Release P376<br>P312/04 |
| 36.0 | 02/11/23<br>02 November 2023 Standard Release P395<br>SVG271/07<br>ISG269/03 |
| 37.0 | 07/11/2024<br>07 November 2024 Standard release P415, P473<br>P339/03 |
| 38.0 | 27/02/2025<br>27 February 2025 Standard release P442<br>P347/05 |
| 39.0 | 06/11/2025<br>06 November 2025 Standard Release P444<br>P376/03 |
| 40.0 | 27/11/2025<br>27 November 2025 Special Release P483 |

*[Amendment record rebuilt from a flattened copy-paste; each row's cells are listed in source column order.]*

Intellectual Property Rights, Copyright and Disclaimer

The copyright and other intellectual property rights in this document are vested in Elexon or appear with the consent of the copyright owner. These materials are made available for you for the purposes of your participation in the electricity industry. If you have an interest in the electricity industry, you may view, download, copy, distribute, modify, transmit, publish, sell or create derivative works (in whatever format) from this document or in other cases use for personal academic or other non-commercial purposes. All copyright and other proprietary notices contained in the document must be retained on any copy you make.

All other rights of the copyright owner not expressly dealt with above are reserved.

No representation, warranty or guarantee is made that the information in this document is accurate or complete. While care is taken in the collection and provision of this information, Elexon Limited shall not be liable for any errors, omissions, misstatements or mistakes in any information or damages resulting from the use of this information or action taken in reliance on it.

## SCHEDULE 1

BSC OPERATING SERVICES

PART A - SERVICE DESCRIPTION FOR SETTLEMENT ADMINISTRATION

## 1. Overview

1.1 This is the Service Description for the SAA appointed by BSCCo to provide a settlement service in connection with the BSC.

1.2 The purpose of this Service Description is to describe the responsibilities and obligations of the SAA for the calculation of and provision of reports to the FAA, BSCCo and BSC Trading Parties detailing monies owed and owing as a result of BM and Replacement Reserve (RR) actions and the settlement of imbalances. The responsibilities and obligations of the SAA under this Service Description are collectively referred to as ‘the SAA Service’.

1.3 The Service Description describes the interfaces between the SAA, and the BSC Trading Party and other BSC Agents. It also implements the relevant provisions as outlined below of Section T (Settlement and Trading Charges) of the Balancing and Settlement Code (Code).

1.4. The SAA shall:

i) for each Settlement Day, operate the Interim Initial Settlement Run, Initial Settlement Run, Reconciliation Settlement Runs and Final Reconciliation Settlement Run, and produce BM Reports and Settlement Reports;

ii) before Initial Settlement:

(a) receive BM Data from the National Electricity Transmission System Operator (NETSO), which will be sent by the time which is 15 minutes following the end of the Settlement Day, including:

Dynamic Data

Bid-Offer Data

FPN Data

Bid-Offer Acceptance Data

BM Unit Applicable Balancing Services Volume

MIL / MEL data

(b) receive Balancing Services Adjustment Data (BSAD) from the NETSO;

(c) receive Loss of Load Probability and STOR Availability Window data from the NETSO;

(d) receive Replacement Reserve Data from the NETSO;

(e) receive Market Index Data from Market Index Data Providers;

(f) receive BM Unit Metered Volumes from the CDCA;

(g) receive volume data from the Interconnector Administrators;

(h) receive the Account Bilateral Contract Volume for each Settlement Period and each Energy Account from the ECVAA;

(i) receive Metered Volume Reallocation data from the ECVAA;

(j) receive BM Unit Metered Volume, Secondary BM Unit Demand Volume, Secondary BM Unit Delivered Volume and BM Unit Settlement Expected Volume (for Baselined BM Units) and Supplier BM Unit Non BM ABSVD from the SVAA;

(k) receive BM Unit and Energy Account registration data from the CRA;

(l) receive Settlement Exchange Rate from BMRA;

(m) Not Used

(n) calculate TLMs;

(o) calculate payments and charges for BM action;

(p) calculate Energy Imbalance Volumes for each Settlement Period and each Energy Account;

(q) calculate charges and payments for Energy Imbalances by applying SBP and SSP to Energy Imbalance Volumes;

(r) calculate Information Imbalance Volumes and charges;

(s) calculate Non-Delivery Charges;

(t) calculate the System Operator BM Charges and Residual Cashflow Reallocation Cashflows;

(u) aggregate charges and payments by BSC Trading Party and charge type, and report to the FAA by 09.00 hours on the relevant Notification Date;

(v) receive BM Unit Gross Demand, Supplier BM Unit Period Total Gross Non-Final Demand and BM Unit Period Deviation Volumes from SVAA;

(w) calculate Total System Virtual Lead Party Compensation Cashflow and Total System Supplier Compensation Cashflow;

(x) receive BM Unit Eligible Exempt Supply data from Exempt Supply Notification Agent(s) (ESNA);

(y) calculate TLM-Adjusted BM Unit Chargeable Demand and send it to EMR Settlement Services Provider in the BM Unit Chargeable Demand Report;

(z) calculate the Total System Direct Compensation Cashflow;

(z) produce the Exempt Supply Volume Report and publish it on the Elexon Portal for use by the BMRA (Insights Solution);

(aa) receive Secondary BM Unit Demand Volume and Secondary BM Unit Supplier Delivered Volume from AMVLP(s).

(iii) for each Emergency Instruction, receive Acceptance Data from the NETSO and take the appropriate actions, as authorised by BSCCo.

iv) for each Network Gas Supply Emergency Acceptance, receive Acceptance Data from the NETSO and enter it into the SAA database by the end of the second full Working Day after receipt.

iv) for each request for data change received from BSCCo on behalf of the Network Gas Supply Emergency Settlement Validation Committee relating to a Network Gas Supply Emergency Acceptance received at least two full Working Days before the Settlement Run date, enter it into the SAA database in time for the next Settlement Run.

v) for each Demand Control event, receive notice of such event from the BMRA or the NETSO.1.5. The terms, definitions and abbreviations used in this Service Description shall have the meanings given in the Glossary and Part A of this Agreement.

1.6. The SAA shall meet the performance standards that are required to be achieved in the delivery of this service as detailed in Part G of Schedule 1 of this Agreement.

1.7 The SAA shall make its systems and processes available such that the provided services are completed within the timescales required by BSC Trading Parties to meet their obligations under the BSC and adhere to the published Settlement Calendar.

1.8 The BSC sometimes uses different terms and acronyms that have the same meaning as those used in this document. The following table indicates which terms and acronyms have equivalent meaning

| Service Description Term/acronym | BSC equivalent term/acronym |
|---|---|
| Deemed Metered Amounts | Metered Volumes |
| TLMOj+ | TLMO+j |
| TLMOj- | TLMO-j |
| Interim Initial | Interim Information |

## 2. Receive input data

### 2.1 National Electricity Transmission System Operator (NETSO)

The SAA shall receive Balancing Services Adjustment Data. BM Data and Loss of Load Probability Data from the NETSO.

2.1.1 BM Data will cover, for each BM Unit:

Final Physical Notification FPN Data

Bid Offer Data

Bid Offer Acceptance Data (including acceptances associated with Replacement Reserve)

MIL / MEL Data

Any Dynamic Data received by the NETSO during the Settlement Day

Emergency Instructions

Network Gas Supply Emergency Acceptances and subsequent requests for data changes relating to Network Gas Supply Emergency Acceptances

2.1.2 The SAA shall receive BM Unit Applicable Balancing Services Volume Data no later than the second Business Day after the Settlement Day and shall:

be expressed in MWh;

follow the sign conventions set out in paragraph 2.4 of Annex X-2; and

represent an aggregate net volume of Active Energy for the whole Settlement Period.

2.1.3 Balancing Services Adjustment Data will consist of:

For Settlement Days after, and including, the P194 effective date up to the P217 effective date:

Buy-Price Cost Adjustment (Energy) (EBCAj)

Buy-Price Volume Adjustment (Energy) (EBVAj)

Buy-Price Volume Adjustment (System) (SBVAj)

Sell-Price Cost Adjustment (Energy) (ESCAj)

Sell-Price Volume Adjustment (Energy) (ESVAj)

Sell-Price Volume Adjustment (System) (SSVAj)

Buy-Price Price Adjustment (BPAj)

Sell-Price Price Adjustment (SPAj)

For Settlement Days after, and including, the P217 effective date:

NETBSAD:

Buy-Price Cost Adjustment (Energy) (EBCAj) – submitted as zero

Buy-Price Volume Adjustment (Energy) (EBVAj) – submitted as zero

Buy-Price Volume Adjustment (System) (SBVAj) – submitted as zero

Sell-Price Cost Adjustment (Energy) (ESCAj) – submitted as zero

Sell-Price Volume Adjustment (Energy) (ESVAj) – submitted as zero

Sell-Price Volume Adjustment (System) (SSVAj) – submitted as zero

Buy-Price Price Adjustment (BPAj)

Sell-Price Price Adjustment (SPAj)

DISBSAD:

A number of Balancing Services Adjustment Actions. For each action:

- Settlement Day
- Settlement Period
- ID
- Cost (£)
- Volume (MWh)
- SO-Flag (T/F)
- STOR Provider Flag (T/F)
- BSAD Party Id (for Settlement Dates on or after the P399 effective date)
- BSAD Asset Id
- Tendered Status
- Service Type

2.1.4 In respect of each Settlement Period within a Settlement Day, the SAA shall receive:

(a) (in relation to all such Settlement periods) not later than 17:00 hours on the preceding day, the NETSO’s estimate (at the relevant time of sending) of Balancing Services Adjustment Data, as described in section 2.1.2.

(b) (in relation to each such Settlement Period) after Gate Closure for, and not later than the end of such Settlement Period, the NETSO’s estimate (at the relevant time of sending) of Balancing Services Adjustment Data, as described in section 2.1.2.

(c) On the day next following such Settlement Day, the Balancing Services Adjustment Data, as described in section 2.1.2.

(d) No later than 15 minutes following Gate Closure, the Loss of Load Probability Data

2.1.4A Loss of Load Probability Data will consist of, for each Settlement Period:

Loss of Load Probability (LOLPj)

De-rated Margin, in MWh

2.1.5 The SAA may receive resubmitted Balancing Services Adjustment Data or Loss of Load Probability Data, from the NETSO, in respect of any Settlement Period within a Settlement Day, at any time prior to the Final Reconciliation Settlement Run for such Settlement Day and the SAA shall correct such data in the Settlement Run next following any such resubmission.

2.1.6 No later than 15 minutes after the start and end of a Demand Control Event, and subsequently in case of update, the SAA shall receive Demand Control Event details from the BMRA or the NETSO. This information shall include:

- A unique identifier for that Demand Control Instruction
- Stage number
- Event type
- Event start date and time
- Event end date and time
- Instructed Distribution System Operator
- Demand Control Event Estimate in MW
- System Management Action Flag

2.1.7 Replacement Reserve Data will consist of:

- RR Bids
- RR Auction Results, including:
- RR Activations
- Volume of GB Need Met
- Interconnector Schedule Data

2.1.A Market Index Data Providers

2.1.A.1 For each Settlement Day, the SAA shall receive, validate and store Market Index Data provided by each Market Index Data Provider comprising of:

(a) a Market Index Volume expressed in MWh for each Settlement Period for each Settlement Day; and

(b) a Market Index Price expressed in £/MWh for each Settlement Period for each Settlement Day.

2.1.A.2 The SAA shall perform the following validation checks:

(a) in respect of a Settlement Period that Market Index Data has been submitted by a valid Market Index Data Provider using data maintained by the CRA;

(b) in respect of a Settlement Period and Market Index Data Provider the Individual Liquidity Threshold does not exceed the Market Index Volume (excluding where the Market Index Volume is supplied as zero);

2.1.A.3 If in respect of a Settlement Period and a Market Index Data Provider:

(a) the Individual Liquidity Threshold exceeds the Market Index Volume (excluding where the Market Index Volume is supplied as zero); or

(b) a Market Index Data Provider fails for whatever reason to submit Market Index Data in time for it to be used in the Settlement Calculations,

the SAA shall default the Market Index Price and Market Index Volume to zero for that Settlement Period.

2.1.A.4 For the purposes of Performance Reporting, the SAA shall for each Market Index Data Provider:

(a) record the number of Settlement Periods where the SAA has defaulted Market Index Data to zero for the reason described in 2.1.4A.3.a;

(b) record the number of Settlement Days where the MIDP has failed to provide Market Index Data (for the purposes of the II Settlement Run) for the reason described in 2.1.4A.3.b.

(c) record the number of Settlement Periods where the Market Index Data with zero values has been used in Settlement calculations, for whatever reason (including, for the avoidance of doubt, instances where the Market Index Data Provider has provided zero values).

### 2.2 CDCA

2.2.1 The SAA shall receive the following data from the CDCA:

BM Unit Metered Volumes, including any Demand Disconnection Volumes;

GSP Group Take;

Interconnector Metered Volumes.

### 2.3 ECVAA

2.3.1 The SAA shall receive from the ECVAA, by the end of the Business Day following the Settlement Day, an initial set of validated Metered Volume Reallocations for BSC Trading Parties and the NETSO and associated BM Units.

2.3.2 The SAA shall receive Account Bilateral Contract Volume for each Settlement Period and each Energy Account from the ECVAA.

### 2.4 IA

2.4.1 The SAA shall receive from the Interconnector Administrators, by the end of the Business Day following the Settlement Day, for each Interconnector with a Transmission System which is not part of the Total System, Deemed Metered Amounts for the BM Unit of each Interconnector User of the relevant Interconnector.

2.4.2 If any expected BM Unit Metered Volumes from an Interconnector Administrator are missing, the SAA shall ask the Interconnector Administrator to resubmit the data. In the event that the Metered volumes are still not received, the SAA shall contact BSCCo for further advice and carry out the actions directed by BSCCo to resolve the problem.

2.4.2A If any BM Unit Metered Volumes are received after the Interim Information Settlement Run, the SAA shall contact BSCCo for further advice and carry out the actions directed by BSCCo. The SAA shall not load these files unless instructed to by BSCCo.

2.4.3 If, in relation to an Interconnector, for any reason:

(a) the Party for the time being appointed as Interconnector Administrator ceases to be a Party, or

(b) otherwise at any time there is no Party so appointed, or

(c) the Interconnector Administrator is in Default (as defined in Section H3.1), or

(d) the Interconnected NETSO becomes the Interconnector Error Administrator pursuant to paragraph 5.4.5,

The BM Unit Metered Volumes for the Interconnector BM Units of any relevant Interconnector User shall be set to zero by the SAA (and, accordingly, the Interconnector Metered Volume shall be attributed to the relevant Interconnector BM Unit of the Interconnector Error Administrator in accordance with Section T4.1) until and unless a replacement Interconnector Administrator or Interconnector Error Administrator (as the case may be) is appointed and registered in accordance with the provisions of paragraph 5.4.3 or (as the case may be) the Interconnector Administrator ceases to be in Default.

2.4.4 BSCCo shall notify the SAA if and when any of the circumstances described in paragraph 2.4.2 occur.

### 2.5 SVAA

2.5.1 The SAA shall receive BM Unit Metered Volumes from the SVAA, including any Demand Disconnection Volumes. The SAA will validate data received from SVAA.

2.5.2 The SAA shall receive Corrected Component volumes from the SVAA. The SAA will validate data received from the SVAA.

2.5.3 The SAA shall receive Secondary BM Unit Demand Volumes, BM Unit Period Deviation Volume, Secondary BM Unit Supplier Delivered Volumes, Supplier BM Unit Non BM ABSVD and BM Unit Settlement Expected Volumes for Baselined BM Units from the SVAA. The SAA will validate data received from the SVAA.

2.5.4 The SAA shall receive Supplier BM Unit Period Non-Chargeable Demand data from the SVAA. The SAA will validate data received from the SVAA.

2.5.5 The SAA shall receive Supplier BM Unit Gross demand and Supplier BM Unit Period Total Gross Non-Final Demand from the SVAA. The SAA will validate data received from the SVAA.

### 2.6 BSCCo

2.6.1 The SAA shall receive a De Minimis Acceptance Threshold (DMATd) for use in calculating imbalance prices. The value of this threshold will be set and from time to time amended by BSCCo, who will also decide upon its effective date. This date shall not be less than 20 Business Days after BSCCo’s initial decision to revise the threshold value.

Initially, the De Minimis Acceptance Threshold will be set at 1MWh.

2.6.2 The SAA shall receive a CADLd (Continuous Acceptance Duration Limit) value from BSCCo for use in the processing of Bid-Offer Volumes. This value may be revised by BSCCo from time to time (subject to consultation with BSC Parties and the NETSO) and can range between 0 and 30 minutes, but will initially be set at 15 minutes. Any revised CADLd value shall become effective from a Settlement Day determined by BSCCo.

2.6.3 The SAA shall receive (from BSCCo), validate and store Individual Liquidity Thresholds for each Market Index Data Provider registered with CRA.

2.6.4 The PARd parameter will be a MWh volume with a value of 500MWh. This value may only be changed by an Approved Modification Proposal. Any revised value shall become effective from a Settlement Day defined by the Approved Modification Proposal and will be communicated to the SAA by the BSCCo.

2.6.5 The RPARd parameter will be a MWh volume with a value of 100MWh. This value may only be changed by an Approved Modification Proposal. Any revised value shall become effective from a Settlement Day defined by the Approved Modification Proposal and will be communicated to the SAA by the BSCCo.

2.6.6 Each year during January (and after publication of the Settlement Calendar) the SAA shall receive from the BSCCo a draft ‘Post Final Settlement Calendar’ for review.

2.6.7 The SAA shall, when instructed by BSCCo to resolve a Manifest Error:

amend the Offer Price and Bid Price of Bid-Offer Pair(s) where such have been identified as Error Bid-Offer Pair(s); and

inform BSCCo when this has been done.

2.6.8 The SAA shall receive an Arbitrage Flag for use in determining whether bids and offers should be removed through the arbitrage process. Initially, the Arbitrage Flag will be set to true.

2.6.9 The SAA shall receive a Value of Lost Load (VoLL) parameter for use in calculating imbalance prices. This value will only be changed following a formal VoLL Review process established in BSCP40. Any revised values shall be communicated to the SAA by the BSCCo. The initial value of VoLL shall be £3000/MWh, rising to £6000/MWh on 1 November 2018.

2.6.10 The SAA shall input the Supplier Compensation Reference Price for calculating the Total System Supplier Compensation Cashflow, the Total System Virtual Lead Party Cashflows and the Total System Direct Compensation Cashflow. The method for obtaining this will be governed by the Supplier Compensation Reference Price Methodology Document.

### 2.7 CRA

2.7.1 The SAA shall receive BM Unit and Energy Account registration data from the CRA to allow BM Unit to Trading Unit mapping.

2.7.2 The SAA shall receive Market Index Data Provider registration data from the CRA for validating Market Index Data described in 2.1A.2.

2.7.3 The SAA shall receive TLF data and the proportion of losses to be allocated to BM Units in delivering Trading Units, from the CRA. . The proportion of losses to be allocated to BM Units in delivering Trading Units will be set to 0.45.

2.7.4 The SAA shall receive BM Unit Details data from the CRA where a Directly-Connected or Embedded CVA BM Unit has been notified to the CRA as part of an EMR CVA BM Unit Declaration.

### 2.8 FAA

2.8.1 The SAA shall receive from the FAA, on an annual basis, a copy of the Payment Calendar developed (in consultation with the SAA) and published by the FAA. Using the Payment Calendar the SAA shall create a Settlement Calendar. This process is described in more detail at section 5.2.

2.8.2 The SAA shall, upon receipt of notification of an invalid Debit/Credit report from the FAA, use its best endeavours to resolve the problem and issue a revised SAA Debit/Credit report to the FAA.

### 2.9 BMRA

2.9.1 The SAA shall receive from the BMRA, on a daily basis, the Settlement Exchange Rate for use in Settlement on the subsequent day.

### 2.10 Data Receipt and Validation

2.10.1 Section 6 describes the operation of the SAA service with respect to the use of default data where the scheduled input data is missing or invalid.

### 2.11 ESNA(s)

2.11.1 The SAA shall receive from each ESNA, on a daily basis, the BM Unit Eligible Exempt Supply, for the purposes of calculating TLM Adjusted BM Unit Chargeable Demand. The SAA shall validate data received from each ESNA.

### 2.12 AMVLP(s)

2.12.1 The SAA shall receive from each AMVLP, on a daily basis, Secondary BM Unit Demand Volume and Secondary BM Unit Supplier Delivered Volume, for the purposes of calculating the Period Secondary BM Unit Delivered Proportion. The SAA shall validate data received from each AMVLP.

## 3. PERFORM SETTLEMENT CALCULATIONS

### 3.1 Determination of the Transmission Loss Multipliers

#### 3.1.1 Delivering and Offtaking Trading Units

For the purpose of scaling for Transmission Losses, in respect of each Settlement Period, a Trading Unit will be identified as either ‘delivering’ to the Total System or ‘offtaking’ from the Total System in respect of any Settlement Period. This is determined by aggregating the BM Unit Metered Volumes from each BM Unit (other than Secondary BM Units) in the Trading Unit to determine whether the Trading Unit was a net importer or net exporter.

A Trading Unit is a "delivering" Trading Unit when ΣiQMij ≥ 0 and

A Trading Unit is an "offtaking" Trading Unit when ΣiQMij << 0

Where Σi represents the sum over all BM Units (other than Secondary BM Units) belonging to that Trading Unit.

Note that, by default, a BM Unit not comprising a Trading Unit with other BM Units shall be considered to be a ‘Sole Trading Unit’ for the purposes of these calculations. The “delivering” and “offtaking” status of such a Trading Unit shall therefore be determined using the Metered Volume of the single BM Unit comprising that Trading Unit.

3.1.2 In any Settlement Period in which a Trading Unit is offtaking or delivering, all BM Unit Metered Volumes associated with that Trading Unit will be scaled by a TLM that allocates a pro-rata of the volume of losses in that Settlement Period. TLMs will be calculated in accordance with the following formulae:

TLMij = 1 + TLFij + TLMO+j

for all non-Interconnector BM Units that are in Trading Units that are net deliverers of energy in Settlement Period j, and

TLMij = 1 + TLFij + TLMO-j

for all non-Interconnector BM Units that are in Trading Units that are net offtakers of energy in Settlement Period j.

Where:

TLMO+j = – {α(Σ+QMij + Σ-QMij) + Σ+(non-I) (QMij * TLFij)} / Σ+(non-I) QMij ;

TLMO-j = {(α–1)(Σ+QMij + Σ-QMij) – Σ-(non-I) (QMij * TLFij)} / Σ-(non-I) QMij ;

Σ+ represents a sum over all BM Units in Trading Units other than Secondary BM Units that are net deliverers of energy in Settlement Period j;

Σ- represents a sum over all BM Units in Trading Units other than Secondary BM Units that are net offtakers of energy in Settlement Period j;

Σ+(non-I) represents the sum over all BM Units other than Interconnector BM Units and Secondary BM Units belonging to Trading Units that are delivering Trading Units in the Settlement Period; and

Σ- (non-I) represents the sum over all BM Units other than Interconnector BM Units and Secondary BM Units belonging to Trading Units that are offtaking Trading Units in the Settlement Period.

3.1.3 In respect of each Settlement Period, for each Interconnector BM Unit, the Transmission Loss Multiplier shall be set as follows:

TLMij = 1

irrespective of whether the Interconnector BM Unit belongs to a delivering or offtaking Trading Unit in the Settlement Period.

3.1.4 In respect of each Settlement Period, for each Secondary BM Unit, the Transmission Loss Multiplier shall be calculated as follows:

TLMij = TLMij(Base)

where TLMij(Base) means the value of TLMij calculated in the Settlement Period for BM Units belonging to the Base Trading Unit in the same GSP Group as the Secondary BM Unit.

3.1.5 The values of TLFij will be as determined in accordance with Section T, Annex T-2 of the Code.

### 3.1A Determination of TLM-Adjusted BM Unit Chargeable Demand (for EMR Settlement purposes)

In order to support EMR Settlement Arrangements the SAA will, for each VAR, calculate and provide to the EMR Settlement Services Provider the Chargeable Demand (‘the TLM-Adjusted BM Unit Chargeable Demand’) for each relevant BM Unit and Settlement Period in the Settlement Day.

For Supplier BM Units the TLM-Adjusted BM Unit Chargeable Demand is defined as:

TLM-Adjusted BM Unit Chargeable Demand = TLM-Adjusted BM Unit Gross Demand - TLM-Adjusted BM Unit Non-Chargeable DemandWhere TLM-Adjusted BM Unit Gross Demand is the BM Unit SVA Gross Demand received from the SVAA for that BM Unit and Settlement Period, adjusted for Transmission Losses, and TLM-Adjusted BM Unit Non-Chargeable Demand is calculated as the sum of:

• the value of Supplier BM Unit Period Non-Chargeable Demand relating to EMR Declarations received from the SVAA for that BM Unit and Settlement Period, adjusted for Transmission Losses; and

• the value of Supplier BM Unit Period Non-Chargeable Demand calculated from the aggregated BM Unit Eligible Exempt Supply volumes received from each ESNA for that BM Unit and Settlement Period, adjusted for the Transmission Loss Multiplier (as each ESNA will have applied the TLF already).

CVA BM Units (other than Interconnector BM Units) which have a BM Unit Metered Volume less than zero in a given Settlement Period the TLM-Adjusted BM Unit Chargeable Demand is defined as:

TLM-Adjusted BM Unit Gross Demand = TLMij * BM Unit Metered Volume

For declared CVA BM Units the TLM Adjusted BM Unit Chargeable Demand will be set to zero.

For all other BM Units, TLM-Adjusted BM Unit Chargeable Demand is not defined (and the SAA will not provide a value for that BM Unit and Settlement Period to a EMR Settlement Services Provider).

### 3.2 Settlement of BM Actions

Introduction

3.2.1 BM actions are remunerated on a “pay-as-bid” basis. BSC Trading Parties from whom the NETSO has accepted a BM action in a particular period will be subject to payments and/or charges for such action. Such payments and charges are calculated for each BM Unit for each Settlement Period and for each Bid-Offer Acceptance. Data conversion will be undertaken on BM Unit data received from the NETSO as described in Section T 3.1.1 of the Code.

Treatment of Time

3.2.2 Bid-Offer Data, Point FPNs, and Bid-Offer Acceptance Data contain information in the form of spot MW data that will be used to determine half-hourly MWh energy quantities. The following algebra is used to specify the relationship between this input data and a number of derived outputs. It includes the ‘calculation’ of interim variables that are continuous functions of time. Note that Balancing Mechanism volumes and RR Acceptance Volumes share the same processes until Accepted Bid and Offer Volumes are calculated, before subsequently diverging.

3.2.3 Whilst all half-hourly integrated MWh energy quantities should be explicitly calculated as part of the settlement process, it is not intended that these continuous functions of time should actually be calculated or reported. The variables to which this applies are as follows:

Final Physical Notification (FPNij(t))

Bid-Offer Volume (qBOnij(t))

Bid-Offer Upper Range (BOURnij(t))

Bid-Offer Lower Range (BOLRnij(t))

Acceptance Volume (qAkij(t))

Accepted Bid-Offer Volume (qABOknij(t))

Accepted Offer Volume (qAOknij(t))

Accepted Bid Volume (qABknij(t))

Conversion of all such data received from the NETSO shall be in accordance with Section T 3.1.2 of the Code.

3.2.4 In each Bid-Offer Acceptance, the NETSO indicates the MW output levels at which it wishes the BM Unit to operate for certain times within the BM Window Period. Each Bid-Offer Acceptance comprises a set of Point Acceptance Volumes. Linear interpolation is used to define the profile of power output expected to be delivered in each Settlement Period within the BM Window Period as a result of Bid-Offer Acceptance, k.

3.2.5 The values of power output defined in this manner that fall within a particular Settlement Period j are termed the Acceptance Volumes qAkij(t). These are ordered by reference to increasing values of k.

3.2.6 The difference between successive Acceptance Volumes represents the volume (in MW) of Offer or Bid accepted by the NETSO at each spot time as a result of that particular Acceptance Volume. If, at any time, the Acceptance Volume increases relative to the previous Acceptance Volume (or FPN initially), then Offers have been accepted at that spot time. If the Acceptance Volume decreases relative to the previous Acceptance Volume, (or FPN initially), then Bids have been accepted.

3.2.7 In assessing the increase or decrease in production or consumption at any given time, the absolute level of the increase or decrease is also important as this dictates which Bid or Offer has been accepted.

3.2.8 Once the volumes attributable to each Bid and Offer for each spot time in a Settlement Period have been calculated, they are integrated over the spot times in the Settlement Period to determine the overall MWh volume. This MWh volume is then multiplied by the appropriate Bid or Offer price and adjusted for Transmission Losses in order to determine the BM Cashflow. All calculations shall be in accordance with Sections T 3.6 to 3.11 of the Code (these Sections are repeated in this SD).

### 3.3 Calculation of Final Physical Notification

3.3.1 The SAA shall calculate FPNs by ensuring that the value of FPNij(t) is calculated for spot times, t, falling within Settlement Period j by linear interpolation from the values of Point FPN (fFPNit), submitted for that Settlement Period j.

3.3.2 If, for a particular time t no value of Point FPN exists within the Settlement Period for which the associated time is at or after time t, the value of the FPNij(t) shall be equal to the value of the Point FPN submitted for the spot time most recently preceding time t and, where more than one Point FPN exists for that spot time, the Point FPN with the higher value of the Point Value Identification Number f.

If no value of Point FPN exists for which the associated time is at or before a particular time, the value of FPNij(t) shall be set equal to zero.

### 3.4 Calculation of Bid-Offer Volume

3.4.1 The SAA shall calculate Bid-Offer Volumes by ensuring that for any value of Bid-Offer Number, n, the Bid-Offer Volume (qBOnij(t)) at any spot time t is calculated by linear interpolation from the values of Point Bid-Offer Volume (fqBOnit) submitted for spot times t in Settlement Period j.

3.4.2 If, for a particular time, t, no subsequent value of Point Bid-Offer Volume has been submitted within the Settlement Period, then the SAA shall set the value of Bid-Offer Volume at the value of the Point Bid-Offer Volume submitted for the time most recently prior to the time in question, and this value shall apply until the end of the Settlement Period.

### 3.5 Calculation of Acceptance Volume

3.5.1 The SAA shall calculate Acceptance Volumes by ensuring that the Acceptance Volume (qAkij(t)) is determined for spot times, t, within each Settlement Period, j, that falls within the BM Window Period (as defined at the Bid-Offer Acceptance Time Tkit). Such calculations shall be in accordance with Section T 3.4.1 of the Code.

3.5.2 It is calculated by linear interpolation from the Point Acceptance Volumes qAkit issued by the NETSO for that Bid-Offer Acceptance, k.

3.5.3 For spot times within the BM Window Period prior to the first value Point Acceptance Volume for Bid-Offer Acceptance k, the value of the Acceptance Volume is set to the last calculated value of Acceptance Volume for those spot times. If no such previously calculated value of Acceptance Volume exists, then the SAA shall set the Acceptance Volume to the value of FPNij(t) for those times.

3.5.4 For spot times which are both:

(a) within the Balancing Mechanism Window Period; and

(b) after the last time associated with a value of Point Acceptance Volume for the Acceptance,

for each BM Unit, the value of the Acceptance Volume shall be set to the last calculated value of Acceptance Volume for those spot times. If no such previously calculated value of Acceptance Volume exists, then the Acceptance Volume shall be set to the value of FPNij(t) for those spot times.

### 3.6 Processing of Bid-Offer Data

3.6.1 Before determining what volume of each Offer and Bid is deemed to have been accepted as a result of each Acceptance Volume, the SAA shall process the Bid-Offer Data for each Settlement Period. This involves calculating the Bid-Offer Upper Range for Bids and Offers that cover volumes of output above FPN, and calculating the Bid-Offer Lower Range for Bids and Offers that cover output below FPN.

### 3.7 Calculation of Bid-Offer Upper Range1

3.7.1 The SAA shall calculate the Bid-Offer Upper Range by ensuring that for Bid-Offer Pairs for which the associated Bid-Offer Pair Number n≥1, the Bid-Offer Upper Range BOURnij(t) is calculated for all spot times in Settlement Period j as:

BOURnij(t) = FPNij(t) + Σn+qBOnij(t); and

BOUR0ij (t) = FPNij(t)

Where Σn+ represents a sum over the range of Bid-Offer Pair Numbers 1 to n.

### 3.8 Calculation of Bid-Offer Lower Range

3.8.1 The SAA shall calculate the Bid-Offer Lower Range by ensuring that for Bid-Offer Pairs for which the associated Bid-Offer Pair Number n<0, the Bid-Offer Lower Range BOLRnij(t) is calculated for all spot times in Settlement Period j as:

BOLRnij(t) = FPNij(t) + Σn- qBOnij(t)

BOLR0ij(t) = FPNij(t)

Where Σn- is the sum over all negative Bid-Offer Pairs, -1 to n.

### 3.9 Calculation of Accepted Bid-Offer Volume

3.9.1 The SAA shall calculate the Accepted Bid-Offer Volume by ensuring that the Accepted Bid-Offer Volume (qABOknij (t)) represents the volume (in MWh) of Bid or Offer from Bid-Offer Pair n accepted as a result of Bid-Offer Acceptance k that is not related to an RR Instruction in Settlement Period j from BM Unit i. It is determined as follows:

For all n>0,

qABOknij(t) = max( min( qAkij(t) , BOURnij(t) ) , BOURn-1ij(t) )

- max( min( qAk-1ij(t), BOURnij(t) ) , BOURn-1ij(t) )

For all n<0,

qABOknij(t) = min( max( qAkij(t) , BOLRnij(t) ) , BOLRn+1ij(t) )

min( max( qAk-1ij(t), BOLRnij(t) ) , BOLRn+1ij(t) ).

3.9.2 Where, from all Bid-Offer Acceptances for which an Acceptance Volume has been determined for Settlement Period j, k-1 represents that Bid-Offer Acceptance with the Bid-Offer Acceptance Time (Tk-1it) most recently preceding that of Bid-Offer Acceptance k. For the purposes of this Service Description the superscript “k-1“ used in the terms above is equivalent to superscript “k-” as used in the Code.

3.9.3 The SAA shall ensure that, if there is no Bid-Offer Acceptance, for which an Acceptance Volume has been determined in Settlement Period j which has a Bid-Offer Acceptance Time that precedes that of Bid-Offer Acceptance k, the value of qAk-1ij(t) = FPNij(t) for each Acceptance k that is not related to an RR Instruction.

For the purposes of this Service Description the superscript “k-1“ used in the term above is equivalent to superscript “k-” as used in the Code.

### 3.10 Continuous Acceptances and CADLd (for Settlement Days on or after the P194 effective date until the P217 effective date)2

3.10.1 The SAA shall carry out the following procedure in order to flag certain short-duration Accepted Bid-Offer Volumes and exclude them from the calculation of energy imbalance prices:

(a) The SAA shall examine Bid-Offer Acceptances and determine whether any are continuous. For an Acceptance k that commences in Settlement Period j and relates to BM Unit i, an Acceptance continuous with k is one that relates to the same BM Unit, and overlaps k (or an Acceptance already continuous with k) for at least one spot time.

(b) The SAA shall then determine the Continuous Acceptance Duration, CADki of Acceptance k. This is defined as the time period between

i) the earliest spot time corresponding to a Point Acceptance Volume for: Acceptance k or an Acceptance continuous with k, whichever is earlier, and

ii) the latest spot time corresponding to a Point Acceptance Volume for: Acceptance k or an Acceptance continuous with k, whichever is later.

(c) If the SAA finds that CADki < CADLd (the Continuous Acceptance Duration Limit set by BSCCo), then it shall flag Acceptance k. In any other case, the Acceptance will remain un-flagged.

### 3.11 Accepted Offer Volume and Accepted Bid Volume

3.11.1 The SAA shall calculate the Accepted Offer Volume and Accepted Bid Volume by ensuring that the Accepted Offer Volume (qAOknij(t)) represents the volume (in MWh) of Offer n accepted as a result of Bid-Offer Acceptance k from BM Unit i at spot times t within Settlement Period j. It is the positive part of the Accepted Bid-Offer Volume.

qAO knij(t) = Max {qABOknij(t), 0}

3.11.2 Similarly, the Accepted Bid Volume (qABknij(t)) represents the volume of Bid n accepted as a result of Bid-Offer Acceptance k from BM Unit i at spot times t within Settlement Period j. It is the negative part of the Accepted Bid-Offer Volume.

qABknij (t) = Min {qABO knij(t), 0}

### 3.12 Calculation of Period Accepted Offer Volume and Period Accepted Bid Volume

3.12.1 The SAA shall determine the Period Accepted Offer Volume (QAOknij) by integrating the Accepted Offer Volume over all spot times t in Settlement Period j, for each Acceptance that is not related to an RR Schedule. It represents the half-hourly integrated volume of Offer n, in MWh, accepted as a result of Bid-Offer Acceptance k.

3.12.2 The SAA shall determine the Period Accepted Bid Volume (QABknij) by integrating the Accepted Bid Volume over all spot times, t, in Settlement Period j, for each Acceptance that is not related to an RR Schedule. It represents the half-hourly integrated volume of Bid n, in MWh, accepted as a result of Bid-Offer Acceptance k.

### 3.12A Calculation of Period RR Accepted Offer Volume and Period RR Accepted Bid Volume

3.12A.1 The SAA shall determine the Period RR Accepted Offer Volume (RRAOknij) by integrating the Accepted Offer Volume over all spot times t in Settlement Period j, for each Acceptance that is related to an RR Schedule.

3.12A.2 The SAA shall determine the Period RR Accepted Bid Volume (RRABknij) by integrating the Accepted Bid Volume over all spot times, t, in Settlement Period j, for each Acceptance that is related to an RR Schedule.

### 3.13 Calculation of Period BM Unit Total Accepted Offer Volume and Period BM Unit Total Accepted Bid Volume

3.13.1 The Period BM Unit Total Accepted Offer Volume (QAOnij) is the total MWh volume of Offer n accepted from Bid-Offer Acceptances that are not related to an RR Schedule. It shall be determined by the SAA as follows:

QAOnij = ΣkQAOknij

3.13.2 The Period BM Unit Total Accepted Bid Volume (QABnij) is the total MWh volume of Bid n accepted from Bid-Offer Acceptances that are not related to an RR Schedule. It shall be determined by the SAA as follows:

QABnij = ΣkQABknij

### 3.13A Calculation of Period RR Total Accepted Offer Volume and Period RR Total Accepted Bid Volume

3.13A.1 The Period RR Total Accepted Offer Volume (RRAOnij) is the total MWh volume of Bid n accepted from Bid-Offer Acceptances that are related to an RR Schedule. It shall be determined by the SAA as follows:

RRAOnij = ΣkRRAOknij

3.13A.2 The Period RR Total Accepted Bid Volume (RRABnij) is the total MWh volume of Bid n accepted from Bid-Offer Acceptances that are related to an RR Schedule. It shall be determined by the SAA as follows:

RRABnij = ΣkRRABknij

3.14 Calculation of Period BM Unit Total Priced Accepted Offer Volume and Period BM Unit Total Accepted Bid Volume (only required for Settlement Days on or after the P194 effective date until the P217 effective date)3

3.14.1 The Period BM Unit Total Priced Accepted Offer and Bid Volumes (QAPOnij and QAPBnij) exclude any Accepted Bid and Offer Volumes where there exists in a particular Settlement Period, a Continuous Acceptance k’ with CADki < CADLd.

If, for each Settlement Period j and BM Unit i there exists any Continuous Acceptance k’ that has been flagged, then:

i) from and including the Settlement Period in which the earliest Point Acceptance Volume associated with k’ falls, and

ii) to and including the Settlement Period in which the latest Point Acceptance Volume associated with k’ falls,

no values for the Period BM Unit Total Priced Accepted Bid or Offer Volumes will be determined in relation to those Settlement Periods, i.e.

QAPOnij = 0, and

QAPBnij = 0.

Note that this applies to the whole of a Settlement Period. For example, if a Continuous Acceptance which affects the first 5 minutes of period j has been flagged, and in the last 20 minutes another non-flagged Acceptance has begun, all the volumes are set to zero.

In any other case,

QAPOnij = QAOnij, and

QAPBnij = QABnij.

In addition, an Acceptance that starts or ends on a Settlement Period boundary is taken to exist simultaneously in the adjoining Settlement Period. Therefore if a Continuous Acceptance k’ is flagged and ends on the boundary between periods j and j + 1, the Priced Bid-Offer Acceptance Volumes of both Settlement Periods will be set to zero.

### 3.15 Calculation of Period BM Unit Offer Cashflow and Period BM Unit Bid Cashflow

3.15.1 The SAA shall calculate the Period BM Unit Offer Cashflow COnij as:

COnij = QAOnij * POnij * TLMij (=ΣkCAOknij)

This represents the Transmission Loss adjusted cashflow relating to BM Unit i for BM action in Settlement Period j, allocated to Offer n.

3.15.2 The SAA shall calculate the Period BM Unit Bid Cashflow CBnij as:

CBnij = QABnij * PBnij * TLMij (=ΣkCABknij)

This represents the Transmission Loss adjusted cashflow relating to BM Unit i for BM action in Settlement Period j, allocated to Bid n. Under normal circumstances, this will be negative as QABnij is negative and PBnij is normally positive.

### 3.16 Calculation of Period BM Unit Cashflow

3.16.1 The Period BM Unit Cashflow CBMij represents the total payment to BM Unit i as a result of accepted BM action in Settlement Period j. It shall be calculated by the SAA as follows:

CBMij = ΣnCOnij + Σn Cbnij

### 3.17 Calculation of Total System BM Cashflow

3.17.1 The SAA shall calculate the Total System BM Cashflow by ensuring that the Total System BM Cashflow, TCBMj, represents the total payments and charges in respect of BM action for all BM Units (excluding any non-delivery adjustments) in Settlement Period j.

TCBMj = Σi CBMij

3.17.2 In respect of each Settlement Day, for each Party p, the Daily Party BM Unit Cashflow shall be determined as:

CBMp = Σj Σi∈p CBMij

where Σj is the sum over all Settlement Periods and ΣI∈p is the sum of all BM Units for which Party p is the Lead Party.

### 3.17A Calculation of Reserve Scarcity Price (RSVPj)

3.17A.1 In respect of each Settlement Period, the SAA shall calculate the Reserve Scarcity Price as:

RSVPj = LoLPj * VoLL

where LoLPj is the Final Loss of Load Probability for the Settlement Period and VoLL is the Value of Lost Load system parameter.

3.17A.2 Subject to paragraph 3.17A.3, from 1 November 2018, if the NETSO reports a ‘null’ Final Loss of Load Probability or fails to report any Final LoLP for a Settlement Period then the Final Loss of Load Probability shall be the most recently reported Indicative Loss of Load Probability for that Settlement Period.

3.17A.3 If no Final Loss of Load Probability is available (whether provided by the NETSO or derived in accordance with 3.17A.2) for a Settlement Period then the Final Loss of Load Probability shall be NULL and the Reserve Scarcity Price shall be calculated as:

RSVPj = 0

### 3.17B Calculation of STOR Action Price

3.17B.1 In respect of each Settlement Period that is in a STOR Availability Window, for each accepted Offer that is a STOR Action, the SAA shall determine the STOR Action Price (STAPtj) as the greater of the Offer Price (POnij) or the Reserve Scarcity Price (RSVPj) applicable to that Settlement Period.

3.17B.2 In respect of each Settlement Period, for each Balancing Services Adjustment Action that is a STOR Action, the SAA shall determine the STAPtj shall be determined as the greater of the Balancing Services Adjustment Price (BSAPmj) or the Reserve Scarcity Price (RSVPj) applicable to that Settlement Period.

### 3.17C Calculation of System Demand Control Volume

3.17C.1 In respect of each Demand Control Instruction, for each Demand Control Event Stage, the SAA shall determine:

(a) the Start Point Demand Control Level as the Demand Control Event Estimate determined as at the relevant time and date notified by the NETSO in accordance with Section Q6.9.3 or Q6.9.4 of the BSC; and

(b) the End Point Demand Control Level as the Demand Control Event Estimate determined as at the Demand Control Event End Point notified by the NETSO in accordance with Section Q6.9.5.

3.17C.2 In respect of each Settlement Period, the SAA shall establish the Demand Control Volume for each Demand Control Event Stage by linear interpolation from the values of Start Point Demand Control Level and End Point Demand Control Level.

3.17C.3 In respect of each Settlement Period:

(a) the System Demand Control Volume (QSDCj) shall be equal to the sum of the Demand Control Volumes determined under paragraph 3.17C.2 where the Demand Control Volume Notice has included a System Management Action Flag set to “Yes”;

(b) the Balancing Demand Control Volume (QBDCj) shall be equal to the sum of the Demand Control Volumes determined under paragraph 3.17C.2 where the Demand Control Volume Notice has included a System Management Action Flag set to “No”.

3.17.D Calculation of RR Cashflows

3.17D.1 The Quarter Hour RR Cashflow CCRiJ represents the total payment to BM Unit i as a result of RR Acceptances in a Quarter Hour J. It shall be calculated by the SAA as follows:

CCRiJ = RRAViJ * RRAPJ

where RRAPJ represents the Quarter Hour RR Activation Price and RRAViJ is the RR Activation Volume established as follows:

RRAViJ = Quarter Hour RR Activated Quantity * 0.25

3.17D.2 The Period RR Hour BM Unit Cashflow (CRRij) shall be calculated as:

CRRij = ΣJ CCRiJ

where ΣJ is the sum over all Quarter Hours J within Settlement Period j.

3.17D.3 The Daily Party RR Cashflow (CRRp) shall be calculated as:

CRRp = Σj Σiϵp CRRij

where Σj is the sum over all Settlement Periods and Σiϵp is the sum of all BM Units for which Party p is the Lead Party in that day.

3.17D.4 The Replacement Reserve Instructed Offer Deviation Cashflow (CDOij) and the Replacement Reserve Instructed Bid Deviation Cashflow (CDBij) for a BM Unit in a Settlement Period is the payment that results from a deviation from the Deemed Standard Product Shape and shall be calculated as:

CDOij = IODij * BEDPj

CDBij = IBDij * BEDPj

Where BEDPj is the Balancing Energy Deviation Price and is equal to zero.

3.17D.5 The Replacement Reserve Period Instruction Deviation Cashflow (CDRij) is the payment in respect of a BM Unit, as a result of deviation from the TERRE Standard Product Shape in the Settlement Period, and shall be calculated as:

CDRij = CDOij + CDBij

3.17D.6 The Daily Party RR Instruction Deviation Cashflow shall be calculated as:

CDRp = Σj Σiϵp CDRij

where Σj is the sum over all Settlement Periods and Σiϵp is the sum of all BM Units for which Party p is the Lead Party in that day.

3.17D.7 The Total System RR Cashflow (TCRRj) for all BM units shall be calculated as:

TCRRj = Σij CRR ij + Σij CDR ij

where Σij is the sum over all BM Units i for Settlement Period j.

### 3.17E Calculation of Daily Virtual Lead Party Compensation Cashflow

3.17E.1 In respect of each Settlement Period, for each Supplier BM Unit, the Final Demand (FDij) shall be determined as follows:

FDij = MAX(BMUGDVij - SDTBMUij, 0)

3.17E.2 In respect of each Settlement Period, for each Energy Account held by a Supplier, the Supplier Compensation Proportion (CMPaj) shall be determined as follows:

CMPaj = Σi FDij / Σa Σi FDij

3.17E.3 In respect of each Settlement Period, the System Period Compensation Volume (QCVj) shall be determined as follows:

QCVj = Σ i2 QCVji2

3.17E.4 In respect of each Settlement Period, for each Energy Account held by a Supplier, the Supplier Compensation Volume (QCVaj) shall be determined as follows:

QCVaj = QCVj * CMPaj

3.17E.5 In respect of each Settlement Period, the Settlement Period Virtual Lead Party Compensation Cashflow (SVCCaj) shall be determined as follows:

SVCCaj = QCVij * SCRP

3.17E.6 In respect of each Settlement Day, for each Party p, the Daily Virtual Lead Party Compensation Cashflow (SCVp) shall be determined as follows:

SCVp = Σj Σa∈p SVCCaj

where Σj represents the sum over all Settlement Periods and Σa∈p represents the sum over the Energy Accounts of Party p.

### 3.17F Calculation of Daily Supplier Compensation Cashflow

3.17F.1 In respect of each Settlement Period, the Period Supplier Compensation Cashflow (SPCCij) will be determined as follows:

SPCCij = QSVij * SCRP

3.17F.2 In respect of each Settlement Day, for each Party p, the Daily Supplier Compensation Cashflow (SCCp) shall be determined as:

SCCp = Σj Σa∈p SPCCij

where Σj represents the sum over all Settlement Periods and Σa∈p represents the sum over the Energy Accounts of Party p.

### 3.17G Calculation of Daily Direct Compensation Cashflow

3.17G.1 In respect of each Settlement Period, the Period Direct Compensation Cashflow (SPDCji2) will be determined as follows:

SPDC ji2 = QDVji2 * SCRP

3.17G.2 In respect of each Settlement Day, for each Party p, the Daily Direct Compensation Cashflow (SDCp) shall be determined as:

SDCp = Σj Σa∈p SPDC ji2

where Σj represents the sum over all Settlement Periods and Σa∈p represents the sum over the Energy Accounts of Party p.

### 3.18 Settlement of Information Imbalances

3.18.1 The Information Imbalance Charge is a charge applied to the difference between the value of FPN for a BM Unit as modified by any Bid-Offer Acceptances and the actual metered Generation or Demand for that BM Unit. The Lead Energy Account is charged the total costs of Information Imbalance associated with the BM Unit. This is detailed in Sections 3.20 and 3.21 below.

3.18.2 The Information Imbalance Price will initially be set to zero. If necessary, a non-zero Information Imbalance Price could be introduced at any time in order to provide incentives on BSC Trading Parties to submit accurate FPN data.

### 3.19 Calculation of Period FPN

3.19.1 The SAA shall ensure that the Period FPN (FPNij) is the value in MWh calculated for BM Unit i, by integrating the value of FPNij(t) across all times t, falling within Settlement Period j.

### 3.20 Calculation of Period BM Unit Balancing Services Volume

3.20.1 The SAA shall ensure that the Period BM Unit Balancing Services Volume (QBSij) represents the net quantity of Balancing Services energy, consisting of accepted Bids and Offers, Supplier Primary BM Unit Delivered Volume, and volume associated with Applicable Balancing Services from BM Unit i in Settlement Period j . It is determined as follows:

QBSij = Σn (QAOnij + QABnij) + Σn (RRAOnij + RRABnij) + QAS ij + BMUADDVij – QDDij+ QBSDij + SNBABSVDij

3.20.2 For the purpose of the calculation in 3.20.1, the SAA shall set QASij to zero in cases where BM Unit Applicable Balancing Services Volume is not provided by the NETSO.

### 3.21 Calculation of Period Expected Metered Volume

3.21.1 The SAA shall calculate the Period Expected Metered Volume QMEij as follows:

QMEij = FPNij + QBSij

Or in the case of Baselined BM Units where a Settlement Expected Volume SEVij is provided (including a zero value),

QMEij = SEVij + QBSij

3.21.2 The Period Expected Metered Volume is the volume of energy that a particular BM Unit is expected to produce or consume in Settlement Period j. It is this that will be compared to BM Unit Metered Volume (QMij) to determine the Information Imbalance Volume.

The SAA shall receive BM Unit Metered Volumes (QMij) for each Settlement Period and each BM Unit from:

the CDCA, for CVA BM Units;

Interconnector Administrators, for Interconnector BM units;

the SVAA, for Supplier BM Units.

In the case of Supplier BM Units,

QMij = - BMUADVij

where BMUADVij is the BM Unit Allocated Demand Volume.

In case of Secondary BM Units,

QMij = - VBMUDVij+ VLPDVij

Where VBMUDVij is the Secondary BM Unit Demand Volume and VLPDVij is the Party-Aggregated Secondary BM Unit Demand Volume (for AMSID Pairs registered in LPAMR).

### 3.22 Calculation of Period Information Imbalance Volume

3.22.1 The SAA shall calculate the Period Information Imbalance Volume (QIIij) for each BM Unit for each Settlement Period as the modulus of the difference between the BM Unit Metered Volume (QMij) and the Period Expected Metered Volume (QMEij).

QIIij = |QMij – QMEij|

### 3.23 Calculation of Information Imbalance Charge

3.23.1 The SAA shall calculate the Information Imbalance Charge by ensuring that the Information Imbalance Charge (CIIij) is the charge applied to the Lead Energy Account for each BM Unit i for each Settlement Period, j. It is calculated as follows:

CIIij = QIIij * IIPij

### 3.24 Calculation of Total System Information Imbalance Charge

3.24.1 The SAA shall calculate the Total System Information Imbalance Charge by ensuring that the Total System Information Imbalance Charge (TCIIj) is the total Information Imbalance Charge paid by all participants in a particular Settlement Period.

TCIIj = Σi CIIij

Where Σi is the sum of all BM Units.

### 3.25 Daily Party Information Imbalance Charge

3.25.1 In respect of each Settlement Day, for each Party p, the Daily Party Information Imbalance Charge shall be determined as:

CIIp = Σj Σi∈p CIIij

where Σj represents the sum over all Settlement Periods and Σi∈p represents the sum over all BM Units for which Party p is the Lead Party.

### 3.26A Calculation of Energy Imbalance Prices for Settlement Days on or after the P194 effective date until the P217 effective date

3.26A.1 For Settlement Days on or after the P194 effective date until the P217 effective date, the SAA shall calculate the Energy Imbalance Price from a proportion (the PAR volume) of the priced balancing actions remaining after De Minimis, Arbitrage, CADL and NIV Tagging. This proportion shall be called the Price Averaging Reference (PAR) volume. For each Settlement Period the following processes will be applied:

Any accepted Bid or Offer Volumes that have been identified and tagged as being of short duration (a duration less than the Continuous Acceptance Duration Limit) according to Section 3.10 will have their volume included in the calculation of Net Imbalance Volume, but will be disregarded for the purposes of the calculation of the Energy Imbalance Price.

Any accepted Offers with volumes lower than DMATd are tagged as De Minimis Accepted Offers and removed from the calculation; any accepted Bids with volumes greater than -DMATd are tagged as De Minimis Accepted Bids and removed from the calculation. If the DMATd is set to zero, no Bids or Offers are excluded.

The Offers and Bids are ranked in price order (known as stacks or ranked sets) and are then inspected for arbitrage trades – these are where the Bid price of an accepted Bid exceeds the Offer price of any accepted Offer. Any arbitrage volume is removed from the calculation – this could take the form of whole or part Offers/Bids.

BSAD is then inserted into the ranked sets. The non-zero (net) Buy Price Volume Adjustment (Energy) (EBVAj) is inserted into the Offer stack in order of price (derived from EBCAj/EBVAj, i.e. a £/MWh price). The non-zero Total System Un-priced Accepted Offer Volume (TQUAOj) is placed at the top of the Offer stack. The non-zero (net) Buy Price Volume Adjustment (System)(SBVAj) is then inserted into the Offer stack below the Total System Un-priced Accepted Offer Volume.

For each Settlement Period the Net Imbalance Volume will be derived as the volume by which the total volume of Bids accepted and volume of BSAD sales exceeds the total volume of Offers accepted and volume of BSAD purchases (or vice versa).

This is done by NIV tagging the remaining price ordered stacks in the following order: un-priced Bid or Offer Acceptance volumes first, then System BSAD volume and then most expensive Priced Offers or least expensive Priced Bids and Energy BSAD volume, until all of the volume associated with the smaller stack (and an equivalent volume on the larger stack) has been NIV tagged. The volume that is not NIV tagged is the Net Imbalance Volume.

PAR Tagging will be performed on the remaining Offers (including priced buy BSAD volumes) and Bids (including priced sell BSAD volumes) in the Net Imbalance Volume, starting from the most expensive Bid and least expensive Offer, Bids and Offers are tagged until the total remaining volume is not more than the PAR Volume (500MWh).

Following PAR tagging the volume weighted average of the PAR is calculated. Once this volume weighted average is known the BPAj (for Settlement Periods where the NIV is positive) or SPAj (for Settlement Periods where the NIV is negative) is added.

Finally the appropriate TLM is applied to the resulting calculation, noting that,

TLMij = 1+ TLMO+ij + TLFij for BM Units in delivering Trading Units

TLMij = 1+ TLMO-ij + TLFij for BM Units in offtaking Trading Units

3.26B Changes to Settlement Data arising from Emergency Instructions for Settlement Days on and after the P194 effective date until the P217 effective date

3.26B.1 On receipt of Acceptance Data from the NETSO relating to an Emergency Instruction, the SAA shall obtain approval from BSCCo to enter such data into Settlement, prior to entering it into the SAA database.

3.26B.1A Where the NETSO has submitted a Network Gas Supply Emergency Acceptance, the SAA shall enter such data into Settlement without requiring approval from BSCCo.

3.26B.2 Where the NETSO has identified the Emergency Instruction as being an ‘Excluded Emergency Acceptance’, the SAA shall receive from BSCCo recalculated main Energy Imbalance Prices for each affected Settlement Period which have been calculated by including the Emergency Acceptance Volume as an un-priced volume.

3.26B.3 Following the receipt of the recalculated Energy Imbalance Prices from BSCCo and to meet the timescales of the next scheduled Run, the SAA shall:

Calculate the amendments to BSAD required to generate the recalculated Energy Imbalance Prices for the next scheduled Settlement Run4.

Carry out a ‘dry run’ of the Settlement Run.

Provide confirmation to BSCCo that the Energy Imbalance Prices calculated by SAA using amended BSAD is acceptable5.

Obtain authorisation from BSCCo to use amended BSAD in the live Settlement Run.

Following receipt of authorisation from BSCCo, ensure amended BSAD is used in live Settlement Run6, to meet Settlement Calendar timescales.

### 3.26C Calculation of Energy Imbalance Prices for Settlement Days on or after the P217 effective date

3.26C.1 For Settlement Days on or after the P217 effective date, the SAA shall calculate the Energy Imbalance Price using the P217 methodology. For the complete description of the calculation see BSC Section T and Annex T-1. The key points of the P217 methodology are:

BSAD is disaggregated into several Balancing Services Adjustment Actions for each Settlement Period. Aggregated BSAD will also be submitted by the NETSO, however, the following aggregated variables will be submitted as zero:

Buy-Price Cost Adjustment (Energy) (EBCAj) – submitted as zero;

Buy-Price Volume Adjustment (Energy) (EBVAj) – submitted as zero;

Buy-Price Volume Adjustment (System) (SBVAj) – submitted as zero;

Sell-Price Cost Adjustment (Energy) (ESCAj) – submitted as zero;

Sell-Price Volume Adjustment (Energy) (ESVAj) – submitted as zero; and

Sell-Price Volume Adjustment (System) (SSVAj) – submitted as zero.

Bid-Offer Acceptances and Balancing Services Adjustment Actions undergo the same flagging, classification and calculation processes. Together they are known as System Actions.

All System Actions undergo De Minimis and Arbitrage Tagging.

System Actions may be ‘Flagged’. Flagging is the identification of System Actions which are deemed to be taken for reasons other than resolving the short-term energy imbalance. There are three types of Flagging.

SO-Flagging of balancing actions deemed as potentially being impacted by transmission constraints;

Emergency Flagging of Emergency Instructions; and

Continuous Acceptance Duration Limit (CADL) Flagging of short duration actions (this only applies to Bid-Offer Acceptances).

These Flagged System Actions are referred to as First Stage Flagged.

All System Actions undergo Classification in order to determine whether they retain their price. Actions which are not First Stage Flagged are referred to as Unflagged. These System Actions retain their price.

For First Stage Flagged System Actions the following occurs:

In the Buy Stack, all First-Stage Flagged System Buy Actions with a price which is more expensive (from the point of view of the System – the higher the price the more expensive the Buy Action) than the most expensive Unflagged System Buy Action are classified as Second-Stage Flagged System Actions and are unpriced

In the Sell Stack, all First-Stage Flagged System Sell Actions with a price which is more expensive (from the point of view of the System – the lower the price the more expensive the Sell Action) than the most expensive Unflagged System Sell Action are classified as Second-Stage Flagged System Actions and are unpriced.

Balancing Services Adjustment Actions where the price is NULL are always Second Stage Flagged.

Following Classification Net Imbalance Volume tagging occurs. Starting from the lowest priced Sell System Action and highest priced System Buy Action, System Actions from the two stacks are matched and tagged until the smaller (in total volume) of the two stacks is completely tagged. Unpriced System Actions are included in NIV Tagging. Unpriced Sell System Actions are considered to be the lowest priced Sell Actions and Unpriced Buy System Actions are considered to be the highest priced Buy Action – i.e. where present they are the first Actions to be considered during the NIV Tagging process.

Until the P305 effective date, if unpriced volume exists in the Net Imbalance Volume it is assigned a Replacement Price. The Replacement Price is calculated from a volume weighted average of the most expensively priced 100MWh of priced volume – the Replacement Price Average Reference (RPAR) Volume. Where the total remaining volume of untagged, priced System Action items is less than the RPAR Volume then all untagged, priced System Action items are selected. RPAR Volume is 100MWh.

From the P305 effective date, if unpriced volume exists in the Net Imbalance Volume it is assigned a Replacement Price. The Replacement Price is calculated from a volume weighted average of the most expensively priced 1MWh of priced volume – the Replacement Price Average Reference (RPAR) Volume. Where the total remaining volume of untagged, priced System Action items is less than the RPAR Volume then all untagged, priced System Action items are selected. RPAR Volume is 1MWh.

Where no priced System Action items remain after NIV Tagging then the Replacement Price is the Market Price. If the Market Price is undefined then the Replacement Price is zero.

The actual volume of System Actions used to calculate the Replacement Price is defined as the Replacement Price Calculation Volume. If the Replacement Price is derived from the Market Price then Replacement Price Calculation Volume will be considered to be zero.

Until the P305 effective date, following the Replacement Price process the average of the most expensive volumes remaining in the Net Imbalance up to a total volume of PAR are used to set the main Energy Imbalance Price, the volumes not within PAR being ‘PAR tagged’. The PAR volume will be 500MWh.

From the P305 effective date, following the Replacement Price process the average of the most expensive volumes remaining in the Net Imbalance up to a total volume of PAR are used to set the main Energy Imbalance Price, the volumes not within PAR being ‘PAR tagged’. The PAR volume will be 50MWh until 1 November 2018 when it will be 1MWh.

Once the volume weighted average of the PAR has been calculated the BPAj (for Settlement Periods where the NIV is positive) or SPAj (for Settlement Periods where the NIV is negative) is added.

### 3.27 Calculation of System Total Accepted Offer Volume

TQAOj = ΣiΣn QAOnij

### 3.28 Calculation of System Total Accepted Bid Volume

TQABj = ΣiΣn QABnij

3.29 No Longer Used.

3.30 No Longer Used.

3.30A No Longer Used.

3.31 No Longer Used.

### 3.31A Calculation of System Buy Price (SBP) for Settlement Days on or after the P217 effective date

3.31A.1 Refer to BSC Section T for the calculation of System Buy Price for Settlement Days on or after the P217 effective date.

3.32 No Longer Used.

### 3.32A Calculation of System Sell Price (SSP) for Settlement Days on or after the P217 effective date

3.32A.1 Refer to BSC Section T for the calculation of System Sell Price for Settlement Days on or after the P217 effective date.

3.32B No Longer Used.

### 3.32C Defaulting and capping scenarios (Price Derivation Codes) for Settlement Days on or after the P217 effective date

3.32C.1 If in respect of a Settlement Period Σs QXPsj = 0:

where Σs represents the sum over all Market Index Data Providers,

then until the P305 effective date:

(a) if the Net Imbalance Volume is a positive number, and {ΣiΣnΣk {QAOknij * TLMij} + Σm QBSABmj} is not equal to zero, SSPj shall be equal to SBPj as determined in accordance with paragraph 3.31A.1(b);

(b) if the Net Imbalance Volume is a positive number, and {ΣiΣnΣk {QAOknij * TLMij} + Σm QBSABmj} is equal to zero, each of SBPj and SSPj shall be zero;

(c) if the Net Imbalance Volume is a negative number, and {ΣiΣnΣk {QABknij * TLMij} + Σm QBSASmj} is not equal to zero, SBPj shall be equal to SSPj as determined in accordance with paragraph 3.32A.1(b);

(d) if the Net Imbalance Volume is a negative number, and {ΣiΣnΣk {QABknij * TLMij} + Σm QBSASmj} is equal to zero, each of SBPj and SSPj shall be zero; and

(e) if the Net Imbalance Volume is zero, each of SBPj and SSPj shall be zero.

Else, from the P305 effective date then:

(f) if the Net Imbalance Volume is equal to zero, or if the Net Imbalance Volume is not equal to zero and is a positive number and {ΣiΣnΣk {QAOknij * TLMij} + Σm QBSABmj + Σt QSIVtj + QSDCj + QBDCj}} is equal to zero, or if the Net Imbalance Volume is not equal to zero and is a negative number and {ΣiΣnΣk {QABknij * TLMij} + Σm QBSASmj} is equal to zero, then:

(i) the System Buy Price will be equal to zero; and

(ii) the System Sell Price shall be equal to the System Buy Price as determined in 3.32 (f)(i).

The 14 different default and capping scenarios are contained in Appendix C.

3.33 No Longer Used.

3.34 No Longer Used.

### 3.35 Energy Imbalance Volumes

3.35.1 Energy Imbalance Volumes are determined for each Energy Account. A number of interim variables are needed for this calculation, as it is necessary to determine for each Energy Account the metered volumes to be allocated (Credited Energy Volume), the volume of any BM actions and the aggregated Energy Contract Volume Notifications associated with the Energy Account.

### 3.36 Calculation of Credited Energy Volume

3.36.1 When allocating the BM Unit Metered Volume (QMij) and the Period BM Unit Balancing Services Volume (QBSij) to Energy Account a for each Settlement Period j, under paragraphs 3.36.3 and 3.36.5:

Where BM Unit i is a Production BM Unit (has a P/C Status of Production) for that Settlement Period j, then Energy Account a shall be the Production Energy Account

Otherwise,

Where BM Unit i is a Consumption BM Unit (has a P/C Status of Consumption) for that Settlement Period j, then Energy Account a shall be the Consumption Energy Account.

3.36.2 For each Settlement Period j, the SAA shall determine the P/C Status of BM Unit i according to the rules applied by the CRA7 for the corresponding Settlement Day. The SAA shall retain a record of the P/C Status applied in the Credited Energy Volume calculation for each BM Unit i and Settlement Period j.

3.36.3 The SAA shall allocate the Credited Energy Volume QCEiaj from each Primary BM Unit i, to each Subsidiary Energy Account a for each Settlement Period j, as follows:

QCEiaj = {(QMij – QBSij)*(QMPRiaj/100) + QMFRiaj}*TLMij

Values of QCEiaj are then rounded towards zero.

Where a≠A, and A is the Lead Energy Account for BM Unit i; QMFRiaj is the Metered Volume Fixed Reallocation, a fixed volume in MWh, assigned to Energy Account a from BM Unit i in Settlement Period j; QMPRiaj is the Metered Volume Percentage Reallocation, the percentage of the BM Unit Metered Volume that remains after QMFRs and BM actions have been deducted, which is allocated to Energy Account a from BM Unit i in Settlement Period j; and QMij is the Primary BM Unit Metered Volume.

3.36.4 The above calculation represents a pro-rata of the loss adjusted metered volume across those Energy Accounts that have title to a proportion of the metered volume. The pro-rata needs to take account of volumes of BM action accepted for the BM Unit.

3.36.5 The SAA shall determine the Credited Energy Volume from each Primary BM Unit i, for the Lead Energy Account (a = A) for each Settlement Period j, as follows:

QCEiAj = (QMij * TLMij) - Σa≠A QCEiaj

Where Σa≠A represents a sum over all values of a, other than a = A.

This allocates any residual metered volume, including any BM action to the Lead Energy Account.

3.36.6 The treatment of Interconnector BM Units shall be in accordance with Section T 4.1 of the Code.

### 3.37 Calculation of Account Credited Energy Volume

3.37.1 The SAA shall calculate the Account Credited Energy Volume (QACEaj) for each Energy Account a, as follows:

QACEaj = Σi QCEiaj

Where Σi represents the sum over all Primary BM Units.

### 3.38 Calculation of Account Period Bid-Offer Volume

3.38.1 The SAA shall ensure that the Account Period Balancing Services Volume (QABSaj) for each Energy Account and Virtual Balancing Account represents the net volume of accepted Balancing Services energy, consisting of accepted Bids and Offers, and volume associated with Applicable Balancing Services attributable to each Energy Account a, in Settlement Period j. It is calculated as follows:

QABSaj = Σ i∈a QBSij * TLMij + (Σi2QSNDi2j * TLMi2j)

Where

Σi∈a in relation to QBSij represents a sum over all Primary BM Units i for which Energy Account a is the Lead Energy Account;

Σi2 in relation to QSNDi2j represents the sum over all Secondary BM Units for which such Energy Account or Virtual Balancing Account (as the case may be) is the corresponding Energy Account or Virtual Balancing Account of the Lead Party;

TLMij is the Transmission Loss Multiplier for Primary BM Unit i in Settlement Period j.

TLMi2j is the Transmission Loss Multiplier for the Secondary BM Unit i2 in Settlement Period j.

### 3.38A Calculation of Total Period Applicable Balancing Services Volume

3.38A.1 In respect of each Settlement Period, the Total Period Applicable Balancing Services Volume will be determined as follows:

TQAS j = Σi QASij

Where Σi represents the sum over all BM Units.

### 3.38B Calculation of Account Period Deviation Volume

3.38B.1 In respect of each Settlement Period, for each Energy Account, the Account Period Deviation Volume (QADEaj) will be determined as follows:

QADEaj = (∑i QDEij * WMij *TLMij)

where QDEij is the Secondary BM Unit Deviation Volume

### 3.39 Calculation of Account Energy Imbalance Volume

3.39.1 The SAA shall determine the Account Energy Imbalance Volume (QAEIaj) attributable to each Energy Account and Virtual Balancing Account, in Settlement Period j as follows:

QAEIaj = QACEaj + QADEaj – QABSaj – QABCaj

### 3.40 Calculation of Total System Energy Imbalance Volume

3.40.1 The SAA shall ensure that the Total System Energy Imbalance Volume (TQEIj) is the total Energy Imbalance Volume in Settlement Period j, summed across all Energy Accounts a except the NETSO, as follows:

TQEIj = Σa∉S QAEIaj

Where Σa∉S is the sum over all Energy Accounts a except the NETSO.

### 3.41 Calculation of the Energy Imbalance Cashflow

3.41.1 In respect of each Settlement Period, the Account Energy Imbalance Cashflow for each Energy Account other than the Energy Accounts held by the NETSO will be determined as follows:

if QAEIaj > 0 then CAEIaj = – QAEIaj * SSPj

Otherwise CAEIaj = – QAEIaj * SBPj

In respect of each Settlement Period, the Account Energy Imbalance Cashflow for each Energy Account held by the NETSO will be determined as follows: CAEIaj = 0

### 3.42 Calculation of the Total System Energy Imbalance Cashflow

3.42.1 The SAA shall ensure that the Total System Energy Imbalance Cashflow (TCEIj) represents the total cashflow relating to Settlement of energy imbalances in Settlement Period j. It is defined as follows:

TCEIj = Σa∉S CAEIaj

Where Σa∉S is the sum over all Energy Accounts a except the NETSO.

3.42.2 In respect of each Settlement Day, for each Party p, the Daily Party Energy Imbalance Cashflow shall be determined as:

CAEIp = Σj Σa∈p CAEIaj

where Σj represents the sum over all Settlement Periods and Σa∈p represents the sum over the Energy Accounts of Party p.

### 3.43 BM Non-delivery Rule

3.43.1 Non-delivery arises when there is a BM Unit imbalance in the opposite direction to the volume of accepted Offers or Bids, integrated over the Settlement Period. An additional charge, payable by the Lead Party associated with the relevant BM Unit, will be made on any non-delivered volumes.

3.43.2 If a BM Unit has more than one Offer (or Bid) accepted, the non-delivery rule will apply first to the highest priced Offer (or lowest priced Bid) up to the Period BM Unit Total Accepted Offer Volume (or Period BM Unit Total Accepted Bid Volume) of that Offer (or Bid), then to the next highest priced Offer (or next lowest priced Bid) and so on.

3.43.3 If both Offers and Bids are accepted from a given BM Unit, the non-delivery rule will apply to imbalances in one direction only. Offers will be deemed non-delivered if the BM Unit under-generates or over-consumes, while Bids would be non-delivered if the BM Unit over-generates or under-consumes.

### 3.44 Determination of Period BM Unit Non-Delivered Offer Volume

3.44.1 The SAA shall determine the Period BM Unit Non-Delivered Offer Volume QNDOij for each BM Unit i in each Settlement Period j as follows:

QNDOij = Min{Max{QMEij – QMij, 0}, ΣnQAOnij + ΣnRRAOnij}

where Σn, in relation to QAOnij, represents the sum over all Bid-Offer Pair Numbers for the Accepted Offer Volumes and Σn, in relation to RRAOnij, represents the sum over all Bid-Offer Pair Numbers for the RR Accepted Offer Volumes, for the BM Unit.

### 3.44A Determination of Period BM Unit Non-Delivered Bid Volume

3.44A.1 The SAA shall determine the Period BM Unit Non-Delivered Bid Volume QNDBij for each BM Unit i in each Settlement Period j as follows:

QNDBij = Max {Min{QMEij – QMij,0}, ΣnQABnij+ ΣnRRABnij }

where Σn, in relation to QABnij, represents the sum over all Bid-Offer Pair Numbers for the Accepted Bid Volumes and Σn, in relation to RRABnij, represents the sum over all Bid-Offer Pair Numbers for the RR Accepted Bid Volumes, for the BM Unit.

Note that Bid volumes are negative, and so is the non-delivered Bid volume by this definition.

### 3.45 Determination of Offer Non-Delivery Volume

3.45.1 The SAA shall ensure that if QNDOij > 0, then the Period BM Unit Non-Delivered Offer Volume is apportioned across all accepted Offers (AOnij), being Accepted Offer Volumes (QAOnij) and, for upward RR Activations within the Settlement Period, the associated Deemed Standard Product Offer Volume (DSPOJij) and the Replacement Reserve Instructed Offer Deviation Volume (IODij) to determine values of Offer Non-Delivery Volume.

3.45.2 The SAA shall ensure that in each Settlement Period, the set of all accepted Offers (i.e. Offers for which QAOnij >0) is considered. This set of Offers is then ranked from highest price to lowest price. The Non-Delivery Order Number u is used for this purpose. The Offer with the highest price is allocated a Non-Delivery Order Number of u=1, the next highest priced Offer is allocated a Non-Delivery Order Number u=2 and so on until all Offers in the Settlement Period is allocated a Non-Delivery Order Number.

The set of Offers {AOn1ij, AOn2ij, …….. AOnuij} is therefore the ranked set of Offers.

3.45.3 The SAA shall ensure that the Offer Non-Delivery Volume is allocated to the highest priced Offers first. The apportionment continues until the Period BM Unit Non-Delivered Offer Volume is fully apportioned or all available Offer volumes have been used up.

Thus, the Offer Non Delivery Volume for Offer n, is:

QNDOnij = Min(AOnuij, RQNDOu-1ij)

Where RQNDOu-1ijis the Remaining Period BM Unit Non-Delivered Offer Volume determined as:

RQNDOuij = RQNDOu-1ij– QNDOnu-1ij

and RQNDO0ij = QNDOij,

and QNDOn0ij = 0

### 3.46 Determination of Bid Non-Delivery Volume

3.46.1 The SAA shall ensure that if QNDBij < 0, then the Period BM Unit Non-Delivered Bid Volume is apportioned across all accepted Bids (ABnij), being Accepted Bid Volumes (QABnij) and for downward RR Activations within the Settlement Period, the associated Deemed Standard Product Bid Volume (DSPBJij) and the Replacement Reserve Instructed Bid Deviation Volume (IBDij), to determine values of Bid Non-Delivery Volume.

3.46.2 The SAA shall ensure that in each Settlement Period, the set of all accepted Bids (i.e. Bids for which QABnij <0) is considered. This set of Bids is then ranked from lowest price to highest price. The Non-Delivery Order Number, u is used for this purpose. The Bid with the lowest price is allocated a Non-Delivery Order Number of u=1, the next lowest priced Offer is allocated a Non-Delivery Order Number u=2 and so on until all Bids in the Settlement Period are allocated a Non-Delivery Order Number.

The set of Bids {ABn1ij, ABn2ij, …….. ABnuij, } is therefore the ranked set of Bids.

3.46.3 The SAA shall ensure that the Bid Non-Delivery Volume is allocated to the lowest priced Bids first. The apportionment continues until the Period BM Unit Non-Delivered Bid Volume is fully apportioned or all available Bid volumes have been used up.

Thus, the Bid Non Delivery Volume for Bid n, is:

QNDBnij = Max(ABnuij, RQNDBu-1ij)

Where RQNDBu-1ij is the Remaining Period BM Unit Non-Delivered Bid Volume determined as:

RQNDBuij = RQNDBu-1ij – QNDBnu-1ij

and RQNDB0ij = QNDBij

and QNDBnoij= 0

### 3.47 Calculation of the Non-Delivered Offer Charge

3.47.1 The SAA shall calculate the Non-Delivered Offer Charge (CNDOnij) associated with the non-delivery of Offer n in Settlement Period j from BM Unit i as follows:

CNDOnij = QNDOnij * Max {(NDPOnij – SBPj ), 0}* TLMij

where NDPOnij is the Non-Delivered Offer Price.

### 3.48 Calculation of Non-Delivered Bid Charge

3.48.1 The SAA shall calculate the Non-Delivered Bid Charge (CNDBnij) associated with the non-delivery of Bid n in Settlement Period j from BM Unit i as follows:

CNDBnij = QNDBnij * Min {(NDPBnij – SSPj), 0} * TLMij

where NDPOnij is the Non-Delivered Offer Price.

Note that this is a product of two negative numbers that results in a positive charge (or zero).

### 3.49 Calculation of BM Unit Period Non-Delivery Charge

3.49.1 The SAA shall ensure that the Non-Delivery Charge (CNDij) is the total charge associated with the non-delivery of Bids and Offers in Settlement Period j from BM Unit i, calculated as follows:

CNDij = Σn (CNDOnij + CNDBnij)

### 3.50 Calculation of Total System Non-Delivery Charge

3.50.1 The SAA shall ensure that the Total System Non-Delivery Charge (TCNDj) is the total charge associated with the non-delivery of Bids and Offers in Settlement Period j, summed across all BM Units, as follows:

TCNDj = Σi CNDij

3.50.2 In respect of each Settlement Day, for each Party p, the Daily Party Non-Delivery Charge shall be determined as:

CNDp = Σj Σi∈p CNDij

where Σj represents the sum over all Settlement Periods and Σi∈p represents the sum over all BM Units for which Party p is the Lead Party.

### 3.51 BSCCo Costs

3.51.1 The costs associated with all of the activities of BSCCo (including the amounts payable by BSCCo to the SAA and other service providers) will be recovered from BSC Trading Parties in accordance with BSC Section Annex D-1.

3.51.2 A proportion of these BSCCo costs be charged out pro-rata as explained below, and the remaining proportion be charged out pro-rata on the modulus of all notified Energy Contract volumes (ECQzbaj). This money will be recovered monthly, based on a cost forecast and reconciled at year end to total actual costs.

(i) Σ+(QCEaij,) where Σ+ is, for each Account a in Settlement Period j, the sum over all BM Units i that are in delivering Trading Units (i.e. each Trading Unit t where Σi∈ t QMij >= 0); and

(ii) Σ-(-QCEaij), where Σ- is, for each Account a in Settlement Period j, the sum over all BM Units i that are in importing Trading Units (i.e. each Trading Unit t where Σi∈ t QMij < 0)

### 3.52 System Operator Cashflow

3.52.1 The NETSO will be charged the net cost of BM actions (amended for non-delivery) with the Total System Energy Imbalance Cashflow deducted. The manner in which these total costs are met is via a charge in each Settlement Period on the NETSO. This is defined as the System Operator Cashflow (CSOj) and represents the amount of costs incurred in the Balancing Mechanism that are to be paid by the NETSO in Settlement Period j.

CSOj = (TCBMj + TCRRj) – TCNDj

### 3.53 Residual Cashflow Reallocation

3.53.1 In order to ensure that the payments and charges under the BSC balance in each Settlement Period, it will be necessary to make good any deficit, or reallocate any surplus. Any residual cashflows arising under the BSC will be reapportioned on the modulus of the Credited Energy Volumes.

### 3.54 Determination of Total System Residual Cashflow

3.54.1 The Total System Residual Cashflow TRCj represents any net difference between total payments and receipts to and from BSC Trading Parties for a particular Settlement Period. If it proves necessary, it will be calculated as:

TRCj = TCIIj + CSOj + TCNDj – TCBMj – TCRRj + TCEIj 8

### 3.55 Determination of Residual Cashflow Reallocation Proportion

3.55.1 In respect of each Settlement Period, for each Energy Account, other than Energy Accounts held by the NETSO, the Residual Cashflow Reallocation Proportion will be determined as follows:

RCRPaj = {Σ+(non-I) (QCEaij) + Σ-(non-I) (– QCEaij )}/ {Σa {Σ+(non-I) (QCEaij) + Σ-(non-I) (– QCEaij)}}

where Σ+(non-I) is, for each Energy Account a in Settlement Period j, the sum over all BM Units other than Interconnector BM Units that are in delivering Trading Units, and

and Σ-(non-I) is, for each Energy Account a in Settlement Period j, the sum over all BM Units other than Interconnector BM Units that are in offtaking Trading Units, and

and Σa represents the sum over all Energy Accounts a, other than those held by the NETSO.

In respect of each Settlement Period, for each Energy Account held by the NETSO, the Residual Cashflow Reallocation Proportion will be determined as follows:

RCRPaj = 0

### 3.56 Determination of Residual Cashflow Reallocation Cashflow

3.56.1 The Residual Cashflow Reallocation Cashflow (RCRCaj) represents that proportion of the Total System Residual Cashflow allocated to the Energy Account a, as follows:

RCRCaj = RCRPaj * TRCj

3.56.2 In respect of each Settlement Day, for each Party p, the Daily Party Residual Settlement Cashflow shall be determined as:

RCRCp = Σj Σa∈p RCRCaj

where Σj represents the sum over all Settlement Periods and Σa∈p represents the sum over the Energy Accounts of Party p.

### 3.57 Aggregate Charges and Payments

3.57.1 The SAA shall store calculated payments by Settlement Day, Settlement Run, Settlement Period, charge type and BM Unit for 7 (seven) years.

3.57.2 The SAA shall aggregate charges and payments by BSC Trading Party, Settlement Day and charge type and report to BSC Trading Parties and to the FAA in accordance with Section N 6.1.2 of the Code.

Such aggregation and reporting may include BSCCo Administration Charges.

3.57.3 To calculate the account charges the SAA shall aggregate for each BSC Trading Party across each Settlement Day:

Daily Party BM Unit Cashflow;

Daily Party RR Cashflow;

Daily Party RR Instruction Deviation Cashflow;

Daily Party Residual Settlement Cashflow;

Daily Party Energy Imbalance Cashflow;

Daily Supplier Compensation Cashflow;

Daily Virtual Lead Party Compensation Cashflow;

Daily Direct Compensation Cashflow;

System Operator BM charges;

Administration charges;

BM Unit Period Non-Delivery Charge, and

Information Imbalance Charges.

And then calculate the Total Account Charge/Payment which aggregates the net cashflows above for each BSC Trading Party only, and adds to this the Account Energy Imbalance Charge/Payment. This results in a net credit or debit by Energy Account by Settlement Day for reporting purposes only.

For the avoidance of doubt: in relation to any Reconciliation Settlement Run, the amounts referred to in paragraphs N 6.1.3 and 6.1.4 of the Code are to be determined as though it were the first Settlement Run to be carried out in relation to the relevant Settlement Day, and so disregarding any payments which may on any prior Payment Date have been paid or payable in respect of the relevant Settlement Day.

### 3.58 Frequency of Settlement Runs

In respect of each Settlement Day the SAA will carry out the following Settlement Runs:

Interim Initial Settlement Run (no report to FAA);

Initial Settlement Run;

Three Reconciliation Settlement Runs;

Final Reconciliation Settlement Run.

All in accordance with the Payment Calendar and the Settlement Calendar as agreed by BSCCo.

In addition, the SAA will be required to carry out re-runs, as necessary, where a Dispute has been raised and a re-run with revised data is required to resolve the Dispute.

### 3.59 Determination of Trading Unit Delivery Mode

3.59.1 For the purpose of calculating and reporting the Trading Unit Delivery Mode, in respect of each Settlement Period at each Settlement Run, a Trading Unit will be identified as either ‘delivering’ to the Total System or ‘offtaking’ from the Total System in respect of any Settlement Period. This is determined by aggregating the BM Unit Metered Volumes from each non-Supplier BM Unit and the Corrected Component volumes from each Supplier BM Unit in the Trading Unit to determine whether the Trading Unit was a net importer or net exporter.

Note that, by default, a BM Unit not comprising a Trading Unit with other BM Units shall be considered to be a ‘Sole Trading Unit’ for the purposes of these calculations. The Delivery Mode of such a Trading Unit shall therefore be determined using the Metered Volume of the single BM Unit comprising that Trading Unit.

3.59.2 The Trading Unit Export Volume will be determined as:

QTUErj = Σ(non-S) max(QMij, 0) + ΣN(AE) | CORCiNj |

where:

Σ(non-S) represents the sum over all BM Units other than Supplier BM Units belonging to the Trading Unit; and

ΣN(AE) represents the sum over all Consumption Component Classes that are associated with active export over all Supplier BM Units belonging to the Trading Unit.

3.59.3 The Trading Unit Import Volume will be determined as:

QTUIrj = Σ(non-S) min(QMij, 0) – ΣN(AI) | CORCiNj |

where:

Σ(non-S) represents the sum over all BM Units other than Supplier BM Units belonging to the Trading Unit; and

ΣN(AI) represents the sum over all Consumption Component Classes that are associated with active import over all Supplier BM Units belonging to the Trading Unit.

#### 3.59.4 The Trading Unit Delivery Mode will be determined as

"Delivering" if QTUErj + QTUIrj > 0; or

"Offtaking" if QTUErj + QTUIrj ≤ 0.

### 3.60 Determination of RR Schedule

3.60.1 For the purpose of settling Replacement Reserve actions, for each Settlement Run the SAA shall determine an RR Schedule. This Schedule defines the volume of energy that a BM Unit must deliver in each Settlement Period in order to be treated as having fully delivered its RR Activations. Where a BM Unit does not deliver this volume, the Lead Party may be liable for Energy Imbalance Changes and Non-Delivery Charges.

3.60.2 The SAA shall determine the RR Schedule in accordance with the RR Schedule Methodology Document approved by the BSC Panel.

### 3.61 Determination of Deemed Standard Product Variables and Volumes

3.61.1 On receipt of Replacement Reserve Auction Result Data from NETSO, SAA shall assign a Quarter Hour variable J to each Quarter Hour RR Activation (RRAJ) in the RR Auction Period.

3.61.2 The SAA shall then determine Deemed Product Point Variables (qDSPJij(t)) for each Quarter Hour RR Activation, in accordance with Section T 3.1 of the BSC.

3.61.3 The SAA shall determine Deemed Standard Product Volume (qDSPVJij(t)) as:

qDSPVJij(t) = qDSPJij(t) - qDSPJ-1ij(t)

where the Settlement Period, J-1 represents that Deemed Standard Product Shape from the previous Quarter Hour and is measured in MWh for each BM Unit i and Settlement period j.

If no qDSPJ-1ij(t) has been determined in the Settlement Period which has a qDSPJij(t) then qDSPJ-1ij(t) shall be set equal to zero.

3.61.4 The SAA shall determine Deemed Standard Product Offer and Bid Volumes for Accepted Offers and Bids (qDSPOJij(t) and qDSPBJij(t)) associated with RR Activations as:

qDSPOJij(t)) = max (qDSPVJij (t) , 0 )

qDSPBJij (t)) = min (qDSPVJij(t) , 0 )

3.61.5 The SAA shall determine Deemed Standard Product Offer and Bid Volume for each Settlement Period (DSPOJij and (DSPBJij) by integrating qDSPOJij(t)) and qDSPBJij (t)) over all spot times in the Settlement Period, for each Quarter Hour RR Activation ‘J’.

3.61.6 The SAA shall determine Total Period Deemed Standard Product Offer and Bid Volume (TDSPOij and TDSPBij) as a result of a Replacement Reserve Auction at spot times within the Settlement Period as:

TDSPOij = ΣJ DSPOJij

TDSPBij = ΣJ DSPBJij

### 3.62 Determination of Period Supplier BM Unit Delivered Volume

3.62.1 In respect of each Settlement Period and each Secondary BM Unit, the SAA shall determine the Period Secondary BM Unit Non-Delivered Volume (QSNDij) as:

QSNDij = Max{ Min( QBSij, QNDOij ) , QNDBij }

3.62.2 In respect of each Settlement Period and each Secondary BM Unit, the SAA shall determine the Period Secondary BM Unit Delivered Volume (QSDij) as:

QSDij = QBSij – QSNDij

3.62.3 In respect of each Settlement Period, for each Secondary BM Unit "i2", for each Primary BM Unit "i", the Period Secondary BM Unit Supplier Delivered Volume (QSDiji2) is the amount determined as follows:

(a) in respect of Trading Secondary BM Units:

QSDiji2 = QDEi2j * SPiji2

where QDEi2j represents Deviation Volume; and

(b) for all other Secondary BM Units:

QSDiji2 = QSDi2j * SPiji2

where the Period Secondary BM Unit Delivered Proportion (SPiji2) is determined as a weighted average of Secondary BM Unit Supplier Delivered Volume:

SPiji2 = VBMUSDViji2 / (VLPDVij + ΣiVBMUSDViji2)

where Σi represents the summation over all Primary BM Units ‘i’ and VBMUSDViji2 is the Secondary BM Unit Supplier Delivered Volume provided by the SVAA.

3.62.4 In respect of each Settlement Period, for each BM Unit, the SAA shall determine the Period Supplier BM Unit Delivered Volume (QBSDij) as:

QBSDij = Σi2QSDiji2

where Σi2 represents the sum over all Secondary BM Units i2 for which Primary BM Unit ‘i’ is to be allocated a value of QSDiji2.

3.62.5 In respect of each Settlement Period and for each BM Unit, the SAA shall determine the Replacement Reserve Instructed Offer Deviation (IODij) and Bid Deviation (IBDij) for Offers and Bids accepted as a result of a Replacement Reserve Auction at spot times within the Settlement Period, that deviate from the Deemed Standard Product Shape, as follows:

IODij = Σn RRAOnij - TDSPOij

IBDij = Σn RRABnij - TDSPBij

### 3.63 Determination of Secondary BM Unit compensation Volume

In respect of each Settlement Period, for each Trading Secondary BM Unit with a non-zero value of QDEij, the Wholesale Market Proportion of Delivered Volume (WMi2j) is the amount determined as follows:

WMi2j = (QDEi2j - QSDi2j) / QDEi2j

Provided that WMi2j shall be equal to or greater than 0 and equal to or less than 1.

In respect of each Settlement Period the Period Secondary BM Unit Supplier Compensation (QCViji2) is the amount determined as follows:

QCViji2 = QSDiji2 * WMi2j

where QSDiji2 represents Period Secondary BM Unit Supplier Delivered Volume calculated in accordance paragraph 4.3B.4(a).

In respect of each Settlement Period the Period Secondary BM Unit Direct Compensation (QDViji2) is the amount determined as follows:

in respect of Trading Secondary BM Units:

QDViji2 = QSDiji2 - QCViji2

where QSDiji2 represents Period Secondary BM Unit Supplier Delivered Volume calculated in accordance paragraph 4.3B.4(a)

in respect of all other Secondary BM Units:

QDViji2 = QSDiji2

where QSDiji2 represents Period Secondary BM Unit Supplier Delivered Volume calculated in accordance paragraph 4.3B.4(b)

In respect of each Settlement Period, the Period BM Unit Supplier Compensation Volume (QSVij) shall be determined as follows:

QSVij = i2Σ QCViji2 + i2Σ QDViji2

where QCViji2 represents Period Secondary BM Unit Supplier Compensation calculated in accordance with paragraph 4.3C.2 and QDViji2 represents Period Secondary BM Unit Direct Compensation calculated in accordance with paragraph 4.3C.3 and i2Σ represents the summation over  Secondary BM Units "i2"

In respect of each Settlement Period, for each Secondary BM Unit, the Period Secondary BM Unit Compensation Volume is the amount determined as follows:

QCVji2 = i Σ QCViji2

Where iΣ represents the summation over Primary BM Units"i".

In respect of each Settlement Period, for each Secondary BM Unit, the Period Secondary BM Unit Direct Compensation Volume is the amount determined as follows:

QDVji2 = i Σ QDViji2

Where iΣ represents the summation over Primary BM Units"i".

## 4. Reporting

### 4.1 Settlement Reports

4.1.1 As information (metered volumes from the CDCA, volumes from the SVAA, etc) becomes available, interim reports will be produced by the SAA and distributed in the same way as the Initial Settlement Report described below. Early release of Settlement information will allow Disputes to be raised before the Initial Settlement Run and associated cash flows.

4.1.2 The SAA shall produce the Initial Settlement Report in accordance with the Settlement Calendar and send it to BSC Trading Parties and to the FAA for payments to be made on the Initial Payment Date determined by the Payment Calendar. The provision of such data shall be in accordance with BSC Section T paragraph 5.3.1.

In carrying out any Reconciliation Settlement Run, the SAA shall:

(a) use data submitted by the CDCA and SVAA pursuant to the corresponding Reconciliation Volume Allocation Runs;

(b) make any adjustment or revision to any data submitted by the NETSO which is to be made following the resolution of any Trading Dispute, and use such adjusted or revised data;

(c) use any adjusted or revised data submitted to it for the relevant Settlement Period by the CRA, the CDCA, the ECVAA, any Market Data Index Provider, the NETSO and any Interconnector Administrator;

(d) should the NETSO submit any revised Balancing Services Adjustment Data, use such revised data.

The NETSO may resubmit to the SAA, the Balancing Services Adjustment Data in respect of any Settlement Period within the Settlement Day at any time prior to the Final Reconciliation Settlement Run for such Settlement Day, and the SAA shall correct such data in the Settlement Run next following such resubmission.

4.1.3 The SAA shall issue Settlement Reports in accordance with the Settlement Calendar as follows:

Interim Initial Settlement Reports;

Initial Settlement Reports;

Reconciliation Settlement Reports (for 3 Reconciliation Settlement Runs as per Settlement Calendar);

Final Reconciliation Settlement Report (Final Reconciliation Settlement Run as per Settlement Calendar).

Post-Final Settlement Runs shall be undertaken as required by BSCCo up to at least 28 months after the relevant Settlement Day and the SAA shall issue accompanying Settlement Reports in support of such runs.

In the event of a Manifest Error Claim being upheld, the SAA shall:

receive replacement prices from the BSCCo Disputes Administrator via a signed form F14/05 ‘Instruction to Resolve Manifest Error’;

within 1 Working Day of receipt complete the form in order to confirm to the Disputes Administrator that the Initial Settlement Data appropriate to the Manifest Error has been, or will be, recalculated using these replacement prices;

reissue the Initial Settlement Report appropriate to the Manifest Error

A copy of the NETSO’s sub-flow of the Settlement Reports must be made available to any BSC Party to download from the NETA ftp site upon request, for a period of at least seven calendar days, in a manner that ensures that data is secure9.

4.1.4 Before each Reconciliation Payment Date, a Reconciliation Settlement Report listing revised energy imbalances must be produced.

4.1.5 The SAA shall also produce the SAA Performance Report for BSCCo in accordance with the Section V, Table 2 of the Code.

4.1.6 The SAA shall also send a copy of the NETSO’s sub-flow of the Settlement Report (see 4.1.3 above) to the EMR Settlement Services Provider for each Settlement Run.

### 4.2 Other Reporting

4.2.1 The SAA shall supply Credits and Debits Reports as follows:

(a) a Report to the ECVAA after the Interim Initial Run;

(b) a Report to the FAA after the Initial Settlement (SF) Run; and

(c) revised Reports to the FAA resulting from timetabled and Post-Final Settlement Runs.

4.2.2 The SAA shall supply reports to BSCCo and BSC Trading Parties.

4.2.3 The SAA shall supply ad hoc reports to BSCCo or BSC Parties as requested in accordance with Schedule 2. All reports shall be as detailed in Section V, Table 2 of the Code (SAA Reporting).

4.2.4 Data Exception Reports shall be issued to the NETSO, Interconnector Administrators, the SVAA or the ECVAA, whichever is relevant. In addition, Data Exception Reports (for any recipient) shall, if requested, be copied and supplied to BSCCo.

4.2.5 SAA Performance Reports shall be issued monthly to BSCCo.

4.2.6 The SAA Performance Report shall include the performance details of each Market Index Data Provider described in 2.1A.4.

4.2.7 The SAA shall report to the CRA the date of the last non-zero metered volumes, as part of the Withdrawals Checklist for a Withdrawing Party.

4.2.8 The SAA shall, on the 15th working day of each month, send Section D Charging information to the BSCCo. The data used shall be the latest available from the Interim Initial Settlement Run and the Initial Settlement Run only.

4.2.9 The SAA shall send, for each Settlement Day, a Daily Activations Report to the SVAA identifying:

(a) Those RR Activations made in respect of each Secondary BM Unit and Additional BM Unit and Settlement Period; and

(b) Those Bid Offer Acceptances in respect of each Secondary BM Unit and Additional BM Unit and Settlement Period.

4.2.10 The SAA shall, on the sixth working day of each month, send the Aggregated Non-Chargeable Demand Report relating to EMR Declarations for a specific Settlement Run Type for the previous calendar month to BSCCo.

4.2.11 The SAA shall, on the sixth working day of each month, publish the Exempt Supply Volume Reports for each Settlement Run Type for the previous calendar month on the Elexon Portal.

## 5. OTHER RESPONSIBILITIES

### 5.1 Disputes Process

5.1.1 The SAA shall provide services in respect of any Disputes in operation under the BSC in accordance with the provisions of Schedule 3, Part B.

5.1.2 A Dispute may be raised by a BSC Trading Party, the NETSO or by BSCCo if they object to the results of a Settlement when they believe that the calculation has been undertaken using the wrong data or the calculation does not follow the rules. The SAA may raise a Dispute on behalf of BSC Trading Parties if errors in calculations or data are detected or suspected.

5.1.3 The SAA shall, when requested by BSCCo, undertake evaluation, or analysis if requested, of a Dispute to determine the facts and its materiality.

5.1.4 The SAA shall, when requested by BSCCo submit written evidence concerning a particular Dispute, to the BSC Panel.

5.1.5 The SAA shall, when requested by the Customer, carry out a re-run of the Settlement process where a Dispute has been resolved between BSC Trading Parties or the BSC Panel have decided the outcome. Due to the CADLd procedure, any Disputes that pertain to a Settlement Day may require additional Settlement Period data from either side of the Day in question.

5.1.6 The SAA shall retain Settlement data:

(a) up to at least 28 months after the relevant Settlement Day for use in a Settlement Run; and

(b) thereafter, until 40 months after the relevant Settlement Day, in a form that may be retrieved, if requested, within 10 Business days, for use in an Extra-Settlement Determination.

5.1.7 The SAA shall submit the output from the re-runs detailed at 5.1.5 to the FAA.

5.1.8 SAA shall notify BSCCo promptly if it becomes aware of any matter which would or might reasonably be expected to give rise to a Trading Dispute.

5.1.9 The SAA shall, when requested by the Customer, carry out a Historic Settlement Run in order to regenerate Settlement Reports (e.g. in the case of non-delivery) using the data that was valid at the time of the production of the original report.

### 5.2 Settlement Calendar

5.2.1 For each BSC Year a Payment Calendar, setting out Payment Dates and Notification Dates in relation to each Settlement Day, will be established pursuant to Section N3 of the Code. The Payment Calendar will be developed by the FAA in consultation with the SAA under Section N3.1.1(a).

The SAA shall, following receipt from the FAA of the Payment Calendar under Section N3.3.2 and in consultation with BSCCo, prepare in accordance with BSCP301 and deliver to BSCCo, each other Party and each other BSC Agent, a Settlement Calendar showing, for the next following BSC Year:

(a) the date upon which, for each Settlement Day in the BSC Year, the Interim Initial Settlement Run, the Initial Settlement Run and each of the Timetabled Reconciliation Settlement Runs are to be carried out;

(b) the date upon which each of the corresponding Volume Allocation Runs, and the Credit Cover Volume Allocation Run are to be carried out and the resulting data delivered to the SAA and/or other BSC Agents.

The Settlement Calendar shall be consistent with the Payment Calendar.

### 5.3 Manage Settlement Registration Data

5.3.1 The SAA will receive from the CRA BM Unit and Energy Account registration data and Authentication details of the BSC Party. The SAA shall use this data for Settlement calculations.

5.3.2 The SAA shall retain all information received from the CRA as historical registration information sufficient to support re-runs of the Settlement Runs and analysis of any archived data.

5.3.3 The SAA shall receive Demand Capacity (DCij) from the CRA.

### 5.4 FAA Data Validation

5.4.1 Upon receipt of a Credits and Debits Report for an Initial, Reconciliation or Post Settlement Run; the FAA will validate the Settlement Results for completeness against Standing Data and for balance between total debits and total credits. In the event that the data fails this validation, the FAA will, by close of business on the Notification Date, send a Notification of Invalidity to the SAA and the BSCCo.

5.4.2 If a Notification of Invalidity is not received by close of business on the Notification date, the SAA will assume that the data have passed the validation checks.

5.4.3 Upon receipt of a Notification of Invalidity, the SAA will use its best endeavours to resolve the problem and to send revised Settlement Results to the FAA in time for scheduled FTS processing.

## 6. HANDLING OF MISSING OR INVALID SETTLEMENT DATA

### 6.1 Settlement Run Checks

6.1.1 For all run types where missing or invalid data is identified by the SAA, according to the checks specified in Appendix B, the SAA shall contact BSCCo and notify them of the details of pre-settlement run validation failures and await further instructions.

6.1.2 Following the notification of a pre-settlement run validation failure, the SAA shall receive a decision from BSCCo to either defer the run or use substitute data.

6.1.3 SAA shall receive from BSCCo instructions on how to progress a settlement run that the SAA has deferred following notification of pre-settlement run validation failures.

### 6.2 Checks at Interim Initial Settlement Run

6.2.1 When incomplete data is submitted for an Interim Initial Settlement Run, section T1.4.2 of the BSC states that the SAA should form an opinion on whether the proportion of data missing is 'significant', and whether the missing data is likely to be received by the end of the next Business Day, before seeking instructions from BSCCo. In practice, however, both BSCCo and the SAA prefer that BSCCo should take the lead in reaching decisions on these issues. For this reason, the SAA informs BSCCo of missing or invalid data in all cases.

### 6.3 Checks at Initial Settlement Runs

6.3.1 When incomplete data is submitted for an Initial Settlement Run, Section T1.4.5 of the BSC states that the SAA should form an opinion on whether the data is 'substantially complete' before seeking instructions from BSCCo. In practice, however, both BSCCo and the SAA prefer that BSCCo should take the lead in reaching decisions on these issues. For this reason, the SAA will inform BSCCo of missing or invalid data in all cases.

## 7. CONTINGENCY PROVISIONS

### 7.1 Single Imbalance Price

In the event that an emergency situation arises where BSCCo is required to enact the contingency provision of a single imbalance price, the SAA shall work with BSCCo to develop a process which will support the use of such a price in its calculations.

## Appendix A – Input Output Flows

**A1. SAA Inputs**

| Input Flow Description | Flow Received From |
|---|---|
| BSC Party and BSC Party Agent Authentication details | CRA |
| Payment Calendar | FAA |
| Balancing Mechanism Data | BMRA (originally from NETSO) |
| BM Unit Metered Volumes | CDCA |
| Interconnector Meter Flow | CDCA |
| GSP Group Take | CDCA |
| Deemed Metered Amounts for an Interconnector User | Interconnector Administrator |
| Account Bilateral Contract Volume | ECVAA |
| Metered Volume Reallocations for Settlement | ECVAA |
| BM Unit and Energy Account registration data | CRA |
| TLFs and proportion of losses allocated to BM Units in delivering Trading Units | CRA |
| BSCCo costs | BSCCo |
| Supplier Volume Allocations | SVAA |
| Dispute notification | BSC Party, NETSO, BSCCo |
| System ParaMeters | BSCCo |
| Balancing Services Adjustment Data (BSAD) | NETSO |
| Acceptance Data relating to Emergency Instruction10 | NETSO |
| Authorisation to use amended BSAD in live Settlement Run11 | BSCCo |
| BM Unit Applicable Balancing Services Volume | NETSO |
| Receive Settlement run decision | BSCCo 12 |
| Receive Settlement run instructions | BSCCo12 |
| Receive form F14/05 ‘Instruction to resolve Manifest Error’ | BSCCo (Disputes Secretary) |
| Receive Notification of Invalidity (of Credits and Debits Report) | FAA |
| Market Index Data Provider Registration Data | CRA |
| Market Index Data Provider Threshold Data | BSCCo |
| Market Index Data | Market Index Data Provider |
| BM Unit SVA Gross Demand | SVAA |
| Corrected Component volumes | SVAA |
| Replacement Reserve Data | NETSO |
| Secondary BM Unit Demand Volumes | SVAA |
| Secondary BM Unit Supplier Delivered Volumes | SVAA |
| Supplier BM Unit Non BM ABSVD | SVAA |
| Settlement Exchange Rate | BMRA |
| BM Unit Settlement Expected Volumes | SVAA |
| BM Unit Period Non-Chargeable Demand | SVAA |
| Supplier BM Unit Period Total Gross Non-Final Demand | SVAA |
| BM Unit Period Deviation Volume | SVAA |
| Supplier Compensation Reference Price | BSCCo |
| BM Unit Eligible Exempt Supply | ESNA |
| Secondary BM Unit Asset Demand and Delivered Volumes | AMVLP(s) |

**A2. SAA Outputs**

| Output Flow Description | Flow Sent To |
|---|---|
| Settlement Calendar | All BSC Parties and BSCCo |
| Initial Credits/Debits | FAA, ECVAA |
| Credits/Debits (revised) | FAA |
| Settlement Reports (Scheduled) | BSC Trading Party, Virtual Lead Party |
| Settlement Reports (Requested) | BSC Party |
| Settlement Reports (Summarised) | BSCCo |
| Settlement Reports (NETSO) | NETSO |
| Settlement Reports (Scheduled) | EMR Settlement Services Provider |
| Data Exception Reports | NETSO, IA, SVAA or EVCAA as required. |
| Performance Reports | BSCCo |
| Dispute details | BSC Party, BSCCo, NETSO |
| Completed form F14/05 ‘Instruction to Resolve Manifest Error’ | BSCCo (Disputes Secretary) |
| Settlement Calendar | CDCA |
| Report pre-Settlement run validation failure | BSCCo12 |
| Withdrawing Party Settlement Details | CRA |
| Confirmation that amendments to BSAD have generated the desired Energy Imbalance Prices relating to an Excluded Emergency Acceptance | BSCCo |
| BSC Section D Charging Data | BSCCo |
| BM Unit Chargeable Demand | EMR Settlement Services Provider |
| Trading Unit Data | BMRA |
| Daily Activations Report | SVAA |
| Aggregated TLM-Adjusted Non-Chargeable Demand | BSCCo |
| Exempt Supply Volume Report | BSCCo |

## Appendix B – Settlement Run Checks

B1. Checks at Interim Initial Settlement Runs

| Data | Detecting Missing or Invalid Data | Action |
|---|---|---|
| Final Physical Notification (FPN) Data | Check that FPN data has been provided for all BM Units with the FPN Flag set, or Bid Offer data provided. | Where this is not the case, SAA will notify BSCCo and where required, default data will be agreed and processed at SAA.<br>Note that workaround W018 (and any enduring solution) allows NGC to provide manual corrections and additions to BM data, post the II run. In most cases this workaround would be used as the means of providing missing FPN data. |
| Replacement Reserve Data | Check that data has been received and loaded for all Quarter Hours | Where this is not the case, SAA will notify BSCCo and default data will be agreed and processed at SAA. |
| Balancing Services Adjustment Data | Check that data has been explicitly provided and successfully loaded, prior to initiating run. | Where this is not the case, SAA will notify BSCCo and default data will be agreed and processed at SAA.<br>Day-ahead files may be used if available, otherwise the System will default to zero values.<br>(The intention of this check is to give BSCCo the opportunity to override the System default.) |
| Bid – Offer Data | Check that Bid / Offer data has been provided for all Settlement periods for any BM Unit with a Bid Offer Acceptance. | Where this is not the case, SAA will notify BSCCo and default data will be agreed and processed at SAA.<br>Note that workaround W018 (and any enduring solution) allows NGC to provide manual corrections and additions to BM data, post the II run. In most cases this workaround would be used as the means of providing missing Bid – Offer data. |
| Interconnector User BM Unit Metered Volumes | Check that Interconnector User BM Unit Metered Volumes have been received for each Interconnector. | Where this is not the case, SAA will notify BSCCo and default data will be agreed and processed at SAA. |
| Account Bilateral Contract Volumes, Metered Volume Reallocation Data | Check that Account Bilateral Contract Volumes and Metered Volume Reallocation Data have been received from ECVAA System. | Where this is not the case, SAA will notify BSCCo and default data will be agreed and processed at SAA. |
| Aggregated CDCA data, e.g.: CVA BM Unit Metered Volumes, GSP Group Takes, Interconnector Metered Volumes | Check that CDCA run has taken place.<br>(CDCA and SAA share a common database, the results of the CDCA run will automatically be available to SAA, provided the aggregation run took place.) | Where this is not the case, SAA will notify BSCCo and default data will be agreed and processed at SAA. |
| SVA Metered Data | Check that BM Unit Allocated Demand Volume, Secondary BM Unit Demand Volume and Secondary BM Unit Supplier Delivered Volume data has been received from SVAA. | Where this is not the case, SAA will notify BSCCo and default data will be agreed and processed at SAA. |
| SVA Metered Data | Check that the GSP Group Take for each GSP Group from CDCA matches the associated Aggregated Supplier Volume Allocation (accounting for tolerances). | Where this is not the case, then SAA will notify BSCCo and SVAA, and BSCCo will determine appropriate action. |
| SVA Metered Data | Check that the CDCA Run Number and Settlement Date received from CDCA matches the CDCA Run Number and Settlement Date received from SVAA. | Where this is not the case, then SAA will notify BSCCo and CDCA, and BSCCo will determine appropriate action. |
| SVA Metered Data | A BM Unit Identifier in the Supplier Volume Allocation is found, by SAA, to be invalid. | SAA, by default, adds the Metered volume for the invalid BM Unit into the Base BM Unit for the Supplier in the relevant GSP Group.<br>SAA should notify BSCCo that it has undertaken this defaulting. BSCCo will determine appropriate action and notify SAA. |
| SVA Metered Data | Check that BM Unit Period Deviation Volume has been received from SVAA | Where this is not the case, SAA will notify BSCCo and default data will be agreed and processed at SAA. |
| SVA Metered Data | Check that Supplier BM Unit Period Total Gross Non-Final Demand has been received from SVAA | Where this is not the case, SAA will notify BSCCo and default data will be agreed and processed at SAA. |
| SVA Metered Data | Check that BM Unit SVA Gross Demand Data has been received from SVAA | Where this is not the case, SAA will notify BSCCo and default data will be agreed and processed at SAA. |
| SVA Metered Data | A BM Unit Identifier in the Supplier Volume Allocation is found, by SAA, to be missing (on the basis that there are no associated SVA Metering Systems and no data is submitted as a result). | SAA, by default, provides a zero Metered volume for the missing BM Unit for the Supplier in the relevant GSP Group.<br>SAA should notify BSCCo that it has undertaken this defaulting in time for BSCCo to instruct SAA otherwise, if deemed appropriate by BSCCo. |
| Market Index Data | Check that all data is present for the relevant post-P78 Settlement Days | Where this is not the case, SAA will notify BSCCo and default data will be agreed and processed at SAA. |
| Settlement Exchange Rate | Check at 17:00 each day that the value for use on the subsequent day has been received from the BMRA | Where the BMRA is unable to send a value for the subsequent day, the default value shall be the value for the current day. |
| Settlement Expected Volume Data | Check that BM Unit Settlement Expected Volume for Baselined BM Units has been received from SVAA. | Where this is not the case, SAA will notify BSCCo and default data will be agreed and processed at SAA. |

*[Table rebuilt from a flattened copy-paste. Rows are anchored on the data item; the split between the check and action cells was inferred.]*

B2. Checks at Initial Settlement and Reconciliation Runs

| Data | Detecting Missing or Invalid Data | Action |
|---|---|---|
| Final Physical Notification (FPN) Data | Check that FPN data has been provided for all BM Units with the FPN Flag set, or Bid Offer data provided. | Where this is not the case, SAA will notify BSCCo and where required, default data will be agreed and processed at SAA.<br>Note that workaround W018 (and any enduring solution) allows NGC to provide manual corrections and additions to BM data. In most cases this workaround would be used as the means of providing missing FPN data. |
| Replacement Reserve Data | Check that data has been receive and loaded for all Quarter Hours | Where this is not the case, SAA will notify BSCCo and default data will be agreed and processed at SAA. |
| Balancing Services Adjustment Data | Check that data has been explicitly provided and successfully loaded, prior to initiating run. | Where this is not the case, SAA will notify BSCCo and default data will be agreed and processed at SAA.<br>Day-ahead files may be used if available, otherwise the System will default to zero values.<br>(The intention of this check is to give BSCCo the opportunity to override this System default.) |
| Bid - Offer Data | Check that Bid / Offer data has been provided for all Settlement periods for any BM Unit with a Bid Offer Acceptance. | Where this is not the case, SAA will notify BSCCo and default data will be agreed and processed at SAA.<br>Note that workaround W018 (and any enduring solution) allows NGC to provide manual corrections and additions to BM data. In most cases this workaround would be used as the means of providing missing Bid - Offer data. |
| Interconnector User BM Unit Metered Volumes | Check that Interconnector User BM Unit Metered Volumes have been received for each Interconnector. | Where this is not the case, SAA will notify BSCCo and default data will be agreed and processed at SAA. |
| Account Bilateral Contract Volumes, Metered Volume Reallocation Data | Check that Account Bilateral Contract Volumes and Metered Volume Reallocation Data have been received from ECVAA System. | Where this is not the case, SAA will notify BSCCo and default data will be agreed and processed at SAA. |
| Aggregated CDCA data, e.g.: CVA BM Unit Metered Volumes, GSP Group Takes, Interconnector Metered Volumes | Check that CDCA run has taken place.<br>(CDCA and SAA share a common database, the results of the CDCA run will automatically be available to SAA, provided the aggregation run took place.) | Where this is not the case, SAA will notify BSCCo and default data will be agreed and processed at SAA. |
| SVA Metered Data | Check that BM Unit Allocated Demand Volume, Secondary BM Unit Demand Volume and Secondary BM Unit Supplier Delivered Volume data has been received from SVAA. | Where this is not the case, SAA will notify BSCCo and default data will be agreed and processed at SAA. |
| SVA Metered Data | Check that the GSP Group Take for each GSP Group from CDCA matches the associated Aggregated Supplier Volume Allocation (accounting for tolerances). | Where this is not the case, then SAA will notify BSCCo and SVAA, and BSCCo will determine appropriate action. |
| SVA Metered Data | Check that the CDCA Run Number and Settlement Date received from CDCA matches the CDCA Run Number and Settlement Date received from SVAA. | Where this is not the case, then SAA will notify BSCCo and CDCA, and BSCCo will determine appropriate action. |
| SVA Metered Data | A BM Unit Identifier in the Supplier Volume Allocation is found, by SAA, to be invalid. | SAA, by default, adds the Metered volume for the invalid BM Unit into the Base BM Unit for the Supplier in the relevant GSP Group.<br>SAA should notify BSCCo that it has undertaken this defaulting. BSCCo will determine appropriate action and notify SAA. |
| SVA Metered Data | A BM Unit Identifier in the Supplier Volume Allocation is found, by SAA, to be missing (on the basis that there are no associated SVA Metering Systems and no data is submitted as a result). | SAA, by default, provides a zero Metered volume for the missing BM Unit for the Supplier in the relevant GSP Group.<br>SAA should notify BSCCo that it has undertaken this defaulting in time for BSCCo to instruct SAA otherwise, if deemed appropriate by BSCCo. |
| Market Index Data | Check that all data is present for the relevant post-P78 Settlement Days | Where this is not the case, SAA will notify BSCCo and default data will be agreed and processed at SAA. |
| SVA Metered Data | Check that BM Unit Period Deviation Volume has been received from SVAA | Where this is not the case, SAA will notify BSCCo and default data will be agreed and processed at SAA. |
| SVA Metered Data | Check that Supplier BM Unit Period Total Gross Non-Final Demand has been received from SVAA | Where this is not the case, SAA will notify BSCCo and default data will be agreed and processed at SAA. |
| SVA Metered Data | Check that BM Unit SVA Gross Demand Data has been received from SVAA | Where this is not the case, SAA will notify BSCCo and default data will be agreed and processed at SAA. |

*[Table rebuilt from a flattened copy-paste. Rows are anchored on the data item; the split between the check and action cells was inferred.]*

B3. Daily Check of Balancing Services Data

| Inbound Data Flow | Detecting Missing or Invalid Data | Action |
|---|---|---|
| Bid – Offer Acceptances | Check the File Sequence Numbers for potential out‑of‑sequence files, indicating missing Acceptance data. | Where missing data is indicated, SAA will notify BSCCo and default data will be agreed and processed at SAA.<br>Note that workaround W018 (and any enduring solution) allows NGC to provide manual corrections and additions to BM data, post II run. In most cases this workaround would be used as the means of providing missing Bid - Offer Acceptance data.<br>Missing data should be provided within 2 days, otherwise the matter will be escalated further. |
| BM Unit Applicable Balancing Services Volume Data | Check there are no missing files. | Where this is not the case, SAA will notify BSCCo and default data will be agreed and processed at SAA. |

*[Table rebuilt from a flattened copy-paste. Rows are anchored on the data item; the split between the check and action cells was inferred.]*

## Appendix C - Price Derivation Codes

| Code | Description | NIV | ΣQXP | Condition Detail |
|---|---|---|---|---|
| A | SBP = Main price; SSP = Reverse Price | Positive | Non Zero | SBP = NIV;<br>SSP = MPj;<br>Final Priced Volume on Stack is not zero;<br>SSP is not greater than SBP |
| B | SSP Capped to SBP | Positive | Non Zero | SBP = NIV;<br>SSP = NIV;<br>Final Priced Volume on Stack is not zero;<br>SSP is greater than SBP |
| C | SSP Defaulted to SBP | Positive | Zero | SBP = NIV;<br>SSP = NIV;<br>Final Priced Volume on Stack is not zero;<br>QXP is zero |
| D *[fn 13]* | SBP & SSP Defaulted to Market Price | Positive | Non Zero | SBP = MPj;<br>SSP = MPj;<br>Final Priced Volume on Stack is zero;<br>QXP is not zero |
| E *[fn 13]* | SSP & SBP Defaulted to Zero | Positive | Zero | SBP = 0;<br>SSP = 0;<br>Final Priced Volume on Stack is zero;<br>QXP is zero |
| F | SSP = Main Price; SBP = Reverse Price | Negative | Non Zero | SBP = MPj;<br>SSP = NIV;<br>Final Priced Volume on Stack is not zero;<br>SSP is not greater than SBP |
| G | SBP Capped to SSP | Negative | Non Zero | SBP = NIV;<br>SSP = NIV;<br>Final Priced Volume on Stack is not zero;<br>SSP is greater than SBP |
| H | SBP Defaulted to SSP | Negative | Zero | SBP = NIV;<br>SSP = NIV;<br>Final Priced Volume on Stack is not zero<br>QXP is zero |
| I *[fn 13]* | SBP & SSP Defaulted to Market Price | Negative | Non Zero | SBP = MPj;<br>SSP = MPj;<br>Final Priced Volume on Stack is zero;<br>QXP is not zero |
| J *[fn 13]* | SSP & SBP Defaulted to Zero | Negative | Zero | SBP = 0;<br>SSP = 0;<br>Final Priced Volume on Stack is zero;<br>QXP is zero |
| K | SSP & SBP Defaulted to Market Price | Zero | Non zero | SBP = MPj;<br>SSP = MPj |
| L | SSP & SBP Defaulted to Zero | Zero | Zero | SBP = 0;<br>SSP = 0 |
| N | SSP Defaulted to Main Price; SBP = SSP | Negative | Any | NIV is Negative |
| P | SBP Defaulted to Main Price, SSP = SBP | Positive | Any | NIV is Positive |

*[Table rebuilt from a flattened copy-paste. "fn 13" marks footnote 13 attached to the code in the source.]*

1 For further detail on the establishment of Bid-Offer Upper Range and Bid-Offer Lower Range in relation to FPN see BSC Section T3.4A. For further detail on the establishment of Bid-Offer Upper Range and Bid-Offer Lower Range in relation to Unsubmitted Bid-Offer Pairs see BSC Section T3.5.

2 Section 3.10 refers to Settlement Days on or after the P194 effective date until the P217 effective date. For Settlement Days on or after the P217 effective date refer to BSC Section T and Annex T-1 for the description of the CADL process.

3 The values QAPOknij and QAPBknij are intermediate steps in the calculations and are not stored or reported by the SAA, therefore they are not required in this Service Description.27 November 2025

4 For the avoidance of doubt, the BSAD is to be manipulated to arrive at the recalculated Energy Imbalance Prices, as these Prices cannot be directly inputted into the SAA database. This will not result in any amendments being made to the BSAD submitted by the NETSO and published on the BMRS.

5 Where there is a discrepancy between the Energy Imbalance Prices calculated by BSCCo and the prices reached by the SAA using the amended BSAD, and the discrepancy exceeds the threshold of £0.05, the SAA shall liaise with BSCCo to resolve the discrepancy prior to the scheduled live Settlement Run.

6 The SAA shall perform checks to ensure the amended BSAD is not subsequently overwritten and is used in the live Settlement Run.

7 As detailed in the CRA Service Description.

8 Given the definition of CSOBMj in 3.52.1, this actually simplifies to TRCj = TCIIj + TCEIj

9 Secure in this case means a compressed but not encrypted file made available from a private area on the NETA ftp site.

10 Authorisation from BSCCo is to be sought prior to inputting this data into the SAA database.

11 This applies where BSAD has been amended to achieve the desired Energy Imbalance Prices arising from an Excluded Emergency Acceptance.

12 All instances of this flow must be initiated or confirmed by e-mail for auditability

13 Price Derivation Codes D, E, I and J only relate to Settlement Days prior to the P217 effective date.