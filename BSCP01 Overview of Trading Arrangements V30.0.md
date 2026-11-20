# BSCP 01: Overview of Trading Arrangements V30.0

> **Source file:** `BSCP 01 Overview of Trading Arrange.txt`  
> **Effective From Date:** 27/11/2025  
> **Status:** LIVE  
> **Converted:** 2026-10-07. Wording kept verbatim from the source copy-paste; only layout artefacts (page headers/footers, line wraps, website navigation, broken tables) were cleaned up. Notes in *[italic square brackets]* are editorial.

---

BSC Procedure 01

relating to

OVERVIEW OF TRADING ARRANGEMENTS

1. Reference is made to the Balancing and Settlement Code and, in particular, to the definition of “BSC Procedure” in Section X, Annex X-1 thereof.

2. This is BSC Procedure 01, Version 30.0 relating to Overview of Trading Arrangements.

3. This BSC Procedure is effective from 27 November 2025.

4. This BSC Procedure has been approved by the Panel.

Intellectual Property Rights, Copyright and Disclaimer

The copyright and other intellectual property rights in this document are vested in Elexon or appear with the consent of the copyright owner. These materials are made available for you for the purposes of your participation in the electricity industry. If you have an interest in the electricity industry, you may view, download, copy, distribute, modify, transmit, publish, sell or create derivative works (in whatever format) from this document or in other cases use for personal academic or other non-commercial purposes. All copyright and other proprietary notices contained in the document must be retained on any copy you make.

All other rights of the copyright owner not expressly dealt with above are reserved.

No representation, warranty or guarantee is made that the information in this document is accurate or complete. While care is taken in the collection and provision of this information, Elexon Limited shall not be liable for any errors, omissions, misstatements or mistakes in any information or damages resulting from the use of this information or action taken in reliance on it.

## 1 Introduction

### 1.1 Purpose and Scope of the Procedure

This overview describes the component activities of the Trading Arrangements detailed in the Code, from submission of trading data prior to Gate Closure through to final exchange of funds up to fourteen months later. This is in the form of a set of overview process diagrams and a schedule of trading activities (i.e., the Settlement process timetable).

As this document is an overview, process details relating to validation and handling of errors at interfaces are excluded from the process diagrams and schedules. The actions taken by the Settlement Administration Agent in the event of missing or invalid data are described in Appendices 5.1 and 5.2.

### 1.2 Main Users of the Procedure and their Responsibilities

The main users of this procedure are:

(a) Party Agents

(b) Parties

(c) The Central Registration Agent (CRA)

(d) The Energy Contract Volume Aggregation Agent (ECVAA)

(e) The Balancing Mechanism Reporting Agent (BMRA)

(f) The Central Data Collection Agent (CDCA)

(g) The Settlement Administration Agent (SAA)

(h) The Funds Administration Agent (FAA)

(i) The Supplier Volume Allocation Agent (SVAA)

(j) The Dispute Administrator (DA)

(k) The Teleswitch Agent

(l) Supplier Agents

(m) Market Index Data Providers

(n) The NETSO

(o) The Exempt Supply Notification Agent (ESNA)

All of the above Parties have a responsibility for fulfilling their obligations under the Code, either directly or via other contractual arrangements with signatories to the Code, in respect of ensuring adherence to the Settlement process timetable.

### 1.3 Key Milestones

The key milestones in this procedure are defined as follows:

(a) Interim Information and Initial Settlement (Section 4.1)

(b) Reconciliation and Final Settlement (Section 4.2)

### 1.4 Balancing and Settlement Code Provision

This BSCP should be read in conjunction with the Code. This BSCP has been produced in accordance with the provisions of the Code. In the event of an inconsistency between the provisions of this BSCP and the Code, the provisions of the Code shall prevail.

### 1.5 Associated BSC Procedures

The following is a list of BSCPs covering activities and interfaces that are dependent on the Settlement timetable:

| BSC Procedure | Title |
|---|---|
| BSCP03 | Data estimation and substitution for CVA |
| BSCP04 | BM Unit Metered Volumes for Interconnector Users |
| BSCP11 | Trading Disputes |
| BSCP65 | Registration of BSC Parties and Exit Procedures |
| BSCP68 | Transfer of Registration of Metering Systems between CMRS and SMRS |
| BSCP71 | Submission of ECVNs and MVRNs |
| BSCP301 | Clearing, Invoicing and Payment |
| BSCP501 | Supplier Meter Registration Service |
| BSCP502 | Half Hourly Data Collection for Metering Systems Registered in SMRS |
| BSCP503 | Half Hourly Data Aggregation for Metering Systems Registered in SMRS |
| BSCP504 | Non Half Hourly Data Collection for Metering Systems Registered in SMRS |
| BSCP505 | Non Half Hourly Data Aggregation for Metering Systems Registered in SMRS |
| BSCP508 | Supplier Volume Allocation Agent |
| BSCP602 | SVA Metering System & Asset Metering System Register |
| BSCP603 | Meter Operations and Data Collection for Asset Metering Systems |
| BSCP606 | BM Unit Metered Volumes for Exempt Supply Notification Agents |
| BSCP607 | Lead Party Asset Meter Register (LPAMR) |
| and Party-Registered AMSID Pair Volumes | BSCP700 |
| UnMetered Supplier Data Services | BSCP701 |
| Smart Data Service | BSCP702 |
| Advanced Data Service | BSCP703 |
| BSC Central Systems for MHHS Metering Systems | BSCP706 |

Supplier Meter Registration Service for MHHS Metering Systems

### 1.6 Overview of Trading Arrangements and Settlement Process

#### 1.6.1 Introduction

The Code sets out the obligations with which all Parties must comply and details the arrangements for participation in the balancing mechanism and the Settlement of balancing mechanism transactions and imbalances in Great Britain.

Seasonal Transmission Loss Factors (TLFs) in respect of a BSC Year will be derived and published on the Elexon Portal by no later than 31 December in the preceding BSC Year. Seasonal TLFs will be loaded into CRA no later than 5 WD before the start of the relevant BSC Season. SAA will access Seasonal TLFs for a Settlement Day via the shared SAA/CRA/CDCA database. Consequently Seasonal TLFs are not referenced in Section 4, Interface and Timetable Information.

It is expected that Trading Parties will enter into bilateral contracts in advance of the Submission Deadline (the notification deadline for the purposes of submitting Energy Contract Volume and Meter Volume Reallocation Notifications for each Settlement Period as defined in Annex X-1). These bilateral contract volumes must be notified to the ECVAA no later than the Submission Deadline for the relevant Settlement Period if they are to be taken into account for the purposes of calculating energy imbalances for that Settlement Period, but may be submitted at any time in advance of the Submission Deadline for the relevant Settlement Period.

Prior to Gate Closure, some Lead Parties of BM Units must submit (and some Lead Parties of BM Units may choose to submit) a Final Physical Notification (FPN) to the National Electricity Transmission System Operator (NETSO). This is a minute by minute profile of the expected power output or consumption of the relevant generation or demand across each Settlement Period.

Lead Parties of BM Units may choose to participate in the Balancing Mechanism, i.e. provide balancing services actions for a particular Settlement Period. This willingness to operate at a level other than their FPN is demonstrated with the use of Balancing Mechanism Bids and Offers. An Offer indicates a willingness to increase the level of generation or reduce the level of demand. A Bid indicates a willingness to reduce the level of generation or increase the level of demand.

Lead Parties of BM Units may also choose to participate in the Replacement Reserve market, i.e. to provide balancing services actions, for a particular Settlement Period. This willingness to operate at a level other than their FPN is demonstrated with the use of Replacement Reserve Bids. Note a Replacement Reserve Bid can indicate either a willingness to increase the level of generation or reduce the level of demand, or a willingness to reduce the level of generation or increase the level of demand.

Virtual Lead Parties, Asset Metering Virtual Lead Parties and Suppliers may take part in both the Balancing Mechanism and the Replacement Reserve markets. Virtual Lead Parties and Asset Metering Virtual Lead Parties will submit bids to provide balancing services actions through the mechanism of Secondary BM Units and Suppliers will do so through Additional BM Units. Virtual Trading Parties will submit Wholesale Market Activity Notifications ) to the ECVAA, will be party to Energy Contract Volume Notifications or Metered Volume Reallocation Notifications1 which reflect the Wholesale volumes traded and will submit MSID Pair Delivered Volumes relating to Wholesale Market Activity through Trading Secondary BM Units. Secondary BM Units, Trading Secondary BM Units and Additional Supplier BM Units will be comprised of MSID Pairs; Secondary BM Units submitted by Asset Metering Virtual Lead Parties may also include AMSID Pairs. A MSID Pair must contain an Import MSID and will usually (but does not have to) contain an Export MSID. Similarly, an AMSID Pair must contain an Import AMSID and will usually (but does not have to) contain an Export AMSID. Virtual Trading Parties and Virtual Lead Parties will submit MSID Pair Delivered volumes and Asset Metering Virtual Lead Parties will submit MSID Pair Delivered volumes or AMSID Pair Delivered volumes to the BSC Central Systems for each accepted Balancing Mechanism Bid/Offer, Replacement Reserve Bid and Wholesale Market Activity.

Suppliers, Virtual Lead Parties and Asset Metering Virtual Lead Parties can opt to set their Additional and Secondary BM Units as a “Baselined BM Unit”. Virtual Trading Parties must set their Trading Secondary BM Units as a “Baselined BM Unit” An FPN is still submitted to National Grid for dispatch purposes, with the exception that Virtual Trading Parties are not required to submit FPNs in respect of Wholesale Market Activities, but the FPN is not used to calculate Non-Delivery Charges. Instead Settlement systems calculate their own FPN-equivalent (the “Settlement Expected Volume”). The Lead Party specifies (when they allocate each MSID Pair or AMSID Pair to the Baselined BM Unit) how that MSID Pair or AMSID Pair’s contribution to the Settlement Expected Volume should be calculated:

1. Baselined MSID Pairs (or AMSID Pairs): SVAA will use historic metered data to calculate the baseline consumption for the MSID Pair or AMSID Pair (in accordance with a Baselining Methodology Document agreed by the BSC Panel);

2. Non-Baselined MSID Pairs (or AMSID Pairs): The Lead Party calculates the FPN-equivalent, and submits a total figure (per BM Unit and Settlement Period) for all the non-Baselined MSID Pairs and AMSID Pairs; or

3. Inactive MSID Pairs (or AMSID Pairs): temporarily excluded from the BM Unit (for Settlement purposes). Secondary BM Units and Trading Secondary BM Units only.

The NETSO takes the submitted FPNs, Bid/Offer data and Replacement Reserve Bids, together with its own forecast of demand and knowledge of System constraints in the relevant Settlement Period and identifies which Bids and/or Offers it needs to accept in order to control the national and local balance of generation and demand. For each Bid-Offer Acceptance (BOA) the NETSO indicates whether the Acceptance was potentially taken to resolve a transmission constraint using a System Operator Flag (SO-Flag). If the BOA was potentially taken to resolve a transmission constraint the SO-Flag is set to TRUE (and is set to FALSE if the NETSO considers the BOA was not taken to resolve a transmission constraint). The SO-Flag is used to determine whether a BOA should retain its price in the calculation of the main Energy Imbalance Price. SO-Flagged BOAs with a price which is more expensive (from the point of view of the System) than the most expensively priced unflagged balancing action are unpriced. BOAs with a less expensive price (from the point of view of the System) than the most expensively priced unflagged action retain their price.

For each Settlement Period the actual volume of energy transferred will be measured for each BM Unit and compared to the expected contracted volume (as notified to the ECVAA) adjusted for any accepted Bids and/or Offers. The resulting energy imbalance will be settled using the relevant cash out price calculated by SAA.

In addition to these payments and charges, there is also an information imbalance charge which is applied to the difference between the metered output of a BM Unit and the level at which a BM Unit was expected to operate given its FPN adjusted for any accepted Offers and Bids.

All Balancing Mechanism and Imbalance Settlement calculations will be performed by the SAA who will then issue information to the FAA detailing the amounts payable to or by Trading Parties with respect to each Settlement Period.

For accepted Secondary BM Unit balancing services actions, Trading Secondary BM Unit Wholesale Market Activity Notifications and for non BM Unit Applicable Balancing Services actions provided to the NETSO outside of the BM, the SVAA will receive MSID Pair Delivered Volume Data or AMSID Pair Delivered Volume Data and will calculate the appropriate corrections to the imbalance position of each Supplier whose (Primary) BM Unit(s) contain MSID(s) that have been used to provide balancing services actions and send these, along with Secondary BM Unit Delivered Volumes and Supplier BM Unit Non BM Unit ABSVD to the SAA for use in Settlement.

Suppliers who operate within Supplier Volume Allocation appoint agents to carry out certain functions required by the Code. Under the pre-Market-Wide Half Hourly Settlement (MHHS) arrangements, these agents include Data Collectors (half hourly and non half hourly) and Data Aggregators (half hourly and non half hourly). Note, under MHHS arrangements, these agents include Smart Data Service (SDS), Advanced Data Service (ADS) and UnMetered Supplies Data Service (UMSDS). SVA Meter Operator Agents are appointed in accordance with the Retail Energy Code Metering Operation Schedule to carry out certain functions as required by the REC. Suppliers register their Agents with the relevant Supplier Meter Registration Service (SMRS).

Asset Metering Virtual Lead Parties and Suppliers appoint Meter Operator Agents or Asset Metering Meter Operator Agents, and Half Hourly Data Collectors and (where appropriate may also appoint Asset Metering Half Hourly Data Collectors) to carry out certain functions relating to SVA Asset Meters registered with the SVAA required by the Code. Asset Metering Virtual Lead Parties and Suppliers register Meter Operator Agents and Half Hourly Data Collectors with the SVAA.

The Data Collectors collect and process Meter readings (including data estimation). Settlement of Non Half Hourly Metering Systems is performed on the basis of profiled Annualised Advance (AA) and Estimated Annual Consumption (EAC) values for onward submission to the Non Half Hourly Data Aggregator. Half Hourly Data Collectors pass validated half hourly Metered consumption values to the Half Hourly Data Aggregator.

Half Hourly Data Collectors collect and process Asset Meter readings (including data estimation), which they provide directly to the SVAA (and not to the HHDA). Where an Asset Metering Half Hourly Data Collector is also appointed, they shall pass Asset Meter readings to the HHDC to process and provide to the SVAA.

Half Hourly Data Aggregators will send HH Metering System Metered Volume Data to the SVAA for each MSID notified to it by the SVAA, for use in the Secondary BM Units Settlement calculations.

The Data Aggregators aggregate the meter readings (half hourly) or AA and EAC values (non half hourly) received from the Data Collectors according to the registration data held by the SMRA. The Data Aggregators provide the aggregated data to the SVAA.

Exempt Supply Notification Agents receive HH metered data from Suppliers or HHDCs (where instructed by the Supplier) where an exempt supply arrangement exists. They will use the details of the exempt supply arrangement details provided by the Supplier(s) to identify exempt supply volumes. The ESNA will aggregate the exempt volumes to BM Unit level and provide to the SAA for each Settlement Period.

Asset Metering Virtual Lead Parties (AMVLPs) who self-register Assets located behind Non Half Hourly Metering Systems will send Secondary BM Unit Asset Demand and Delivered Volumes to the Settlement Administration Agent (SAA) for use in the Secondary BM Units Settlement calculations.

As part of the Market-wide Half Hourly Settlement (MHHS) arrangements, new Supplier agents have been introduced within the SVA. These include the Smart Data Service (SDS), Advanced Data Service (ADS) and Unmetered Supplies Data Service (UMSDS). Each Data Service is responsible for retrieving, processing, and submitting disaggregated consumption data to the BSC Central Services. These BSC Central Services include the Load Shaping Service (LSS), Market wide Data Service (MDS) and the Volume Allocation Service (VAS).

The LSS will provide the Load Shape Data to Suppliers, the MDS, SDS, ADS and UMSDS. The MDS is responsible for carrying out the aggregation function, defaulting where consumption data is missing and applying distribution losses. The MDS provides data for the VAS, which calculates energy volumes allocated to Suppliers on a Balancing Mechanism (BM) Unit and GSP Group basis. The MDS also provides data for the volume allocation calculations carried out by the SVAA.

### 1.7 Use of the Procedure

#### 1.7.1 Description of Context and Process Diagrams

The Trading Arrangements context diagram shown in section 3.1 shows only the main processes and interfaces between Parties, Party Agents, the ECVAA, BMRA, CDCA, the NETSO, the MIDPs, the SAA, the Supplier Volume Allocation Agent (SVAA) and the Funds Administration Agent (FAA).

The Context and Process Diagrams provide a summary of the activities and interactions of the main parties involved in the trading process, shown without timescales and do not cover non-Settlement dependent processes and dataflows. Please note however, whilst a time-line is implied from left to right across the page, the relationship between process schedules may not be accurately reflected here. To ensure as much clarity as possible, some minor dataflows and reports are not shown in the diagrams.

Section 3.2 shows the trading processes prior to Settlement

Section 3.3 illustrates the Interim Information and Initial Volume Allocation / Settlement Runs

Section 3.4 shows the three Reconciliation and Final Reconciliation Volume Allocation / Settlement Run Processes.

#### 1.7.2 Overview of Settlement Timetable

Table 4.1 shows the tasks from Energy Contract Volume and Meter Volume Reallocation Notification through to the Interim Information Volume Allocation Run by the SVAA, the Interim Information Settlement Run by SAA, the Initial Volume Allocation Run by SVAA, the Initial Settlement Run by SAA through to Initial Funds Transfer by FAA.

Table 4.2 details the three Reconciliation Runs through to the Final Reconciliation Settlement Run at 14 months.

Table 4.3 (the annual processes involved in the production of the Payment Calendar and SAA Settlement Calendar) has been transferred to BSCP301.

### 1.8 Settlement Administration Agent Obligations with regard to input data

In accordance with the Code, the SAA has an obligation to receive and validate input data (described in more detail in the Settlement timetable) from the following Parties and Agents:

National Electricity Transmission System Operator;

Balancing Mechanism Reporting Agent;

Central Data Collection Agent;

Energy Contract Volume Aggregation Agent;

Interconnector Administrators;

Supplier Volume Aggregation Agent;

Exempt Supply Notification Agent;

Central Registration Agent;

Market Index Data Providers; and

Asset Metering Virtual Lead Parties.

The actions to be taken when data is found to be missing or invalid (where not already defined in the Code) for inputs into Settlement are described in Appendices 5.1 and 5.2.

## 2 Acronyms and Definitions

### 2.1 Acronyms

A list of acronyms can be found in Annex X of the Code.

The following acronym is used in this Procedure:

T is the Payment Date for all Timetabled Reconciliation Settlement Runs, as set by the Payment Calendar, and expressed in Working Days from the relevant Settlement Day. In order to allow for days when processing does not take place such as Bank Holidays, the value of T will fall within a “window” as defined in 4.2.

### 2.2 Definitions

A list of definitions can be found in Annex X of the Code. Definitions used in this Procedure (if any) are as follows:

Dynamic Data – Data included in the Dynamic Data Set.

QAS - Applicable Balancing Services Volume

IIR – Interim Information Run

## 3 Process Diagrams

### 3.1 Trading Arrangements Context Diagram

*[Diagram/image in the original web page was not captured in the copy-paste.]*

*[Diagram/image in the original web page was not captured in the copy-paste.]*

### 3.2 Trading Processes prior to Settlement

Please note that within this diagram, TC is the equivalent of NETSO.

### 3.3 Interim Information and Initial Volume Allocation / Settlement Runs

*[Diagram/image in the original web page was not captured in the copy-paste.]*

### 3.4 Reconciliation and Final Reconciliation Volume Allocation / Settlement Runs2

*[Diagram/image in the original web page was not captured in the copy-paste.]*

### 3.5 Replacement Reserve Process

*[Diagram/image in the original web page was not captured in the copy-paste.]*

## 4 Interface and Timetable Information

### 4.1 Interim Information and Initial Settlement Timetable and Settlement Reports

This section covers the tasks required for the Interim Information and Initial Settlement Runs. The Interim Information run is carried out at approximately 5 WD, with no associated Payment Date. The Initial Settlement Run is carried out at approximately 16 WD, with an associated Payment Date of approximately 20 – 21 WD.

| Ref | Task | Responsibility | Time-scale |
|---|---|---|---|
| 1 | Send to ECVAA<br>Energy Contract Volume Notifications | ECVNA | To be received by ECVAA before the Submission Deadline |
| 2 | Send to ECVAA:<br>Meter Volume Reallocation Notifications | MVRNA | To be received by ECVAA before the Submission Deadline |
| 2A | Send to ECVAA:<br>Wholesale Market Activity Notifications | VTP | To be received by ECVAA before Gate Closure |
| 3 | Send the following information (for each BM Unit in respect of which the Lead Party is obliged to submit a FPN or has chosen to submit a FPN) to the NETSO:<br>Final Physical Notification Data<br>Bid / Offer Data (Required only if trading in Balancing Mechanism)<br>Dynamic Data | Lead Parties | To be received by the NETSO before Gate Closure |
| 4 | Send to SVAA for each Baselined BM Unit, and for MSID Pairs or AMSID Pairs which are not Baselined or Inactive:<br>Submitted Expected Volumes | Lead Parties | To be received by SVAA before Gate closure for a Settlement Period |
| 5 | Send to BMRA:<br>Market Index Data | Market Index Data Providers | Target by end of Settlement Period |
| 6 | Accept Bids and Offers as required to meet forecast and actual System conditions. Acceptances which are taken to resolve transmission constraints are SO-Flagged. | NETSO | Not later than 15 minutes following the issue of an Acceptance; or<br>In the case of an Emergency Instruction, as soon as reasonably practicable. |
| 7 | Energy Transfer and Metering | Lead Parties | Settlement Period |
| 8 | Send the following information to BMRA (for information / storage) for each BM Unit in respect of which the Lead Party is obliged to submit a FPN or has chosen to submit a FPN to the NETSO:<br>Maximum Export Limit<br>Maximum Import Limit<br>Final Physical Notification Data<br>Dynamic Data<br>Bid Offer Data (for those BM Units for which such data has been provided)<br>Acceptance Data<br>System related Data<br>BM Unit Applicable Balancing Services Volume Data<br>Replacement Reserve Data | NETSO | Target Times:<br>Not later than 5 minutes following receipt<br>Not later than 15 minutes following Gate closure for each Settlement Period<br>Not later than 1200 hrs each day |
| 9 | Send Final Physical Notification Data to ECVAA.<br>Calculate Indicative System Buy Price and Indicative System Sell Price and publish relevant data | BMRA | Upon receipt from the NETSO.<br>15 + CADL minutes after end of Settlement Period. |
| 10 | Send the following information to SAA to enable Settlement:<br>Final Physical Notification Data<br>Balancing Services Adjustment Data<br>Bid Offer Data<br>Acceptance Data<br>Any Dynamic Data received by the NETSO during the Settlement Day<br>BM Unit Applicable Balancing Services Volume Data | BMRA | The next day following the Settlement Day for Balancing Services Adjustment Data, and by 15 minutes following the end of the Settlement Day for the other items.<br>Within 2 Business Days following the relevant Settlement Period for BM Unit Applicable Balancing Services Volume Data |
| 11 | Interrogate Metering Systems registered by Parties with the CRA and collect consumption data.<br>Send to relevant Parties:<br>Raw Meter Data together with any validation criteria | CDCA | Send out by Settlement Day +1 (1300hrs) |
| 12 | Send to SVAA:<br>Tele-switch data | Tele-switch Agent | By +1 WD (by 1000hrs) |
| 13 | Obtain the following data from relevant authorised providers:<br>Daily temperature paraMeters by GSP Group<br>Sunset times by GSP Group (annually)<br>Perform Profile Production Run<br>Send Profile Reports to Suppliers and NHHDCs | SVAA | By +1 WD (by 1000hrs)<br>By +1 WD (by 1700hrs) |
| 14 | Send to SAA:<br>BM Unit Metered Volumes for the BM Units of each Interconnector User for each Interconnector | IA | By +1 WD |
| 15 | Send to SAA:<br>Market Index Data | Market Index Data Providers | By +1 WD |
| 16 | Send to SVAA<br>MSID Pair Delivered Volumes for<br>procured balancing services<br>or<br>Wholesale Market Activities | VLP | or<br>VTP<br>By +1 WD (by 1700hrs)<br>MSID Pair Delivered Volumes or AMSID Pair Delivered Volumes for procured balancing services<br>AMVLP<br>Wholesale Market Activity Notification Report<br>ECVAA |
| 17 | Suppliers raise query on Daily Profile Production Reports if necessary and log with Dispute Administrator | Supplier | By +3 WD (by 1000hrs) |
| 18 | Ensure Agents send to SVAA:<br>Available Actual<br>Consumption data from all Data Services (SDS, ADS and UMSDS) | Suppliers | By +4 Calendar Days (0000hrs) |
| 19 | Resolve Daily Profile Production query | SVAA | By +4 WD (by 1300hrs) |
| 20 | Amend Profile variables ready to re-run Daily Profile Production, if necessary | SVAA | By +4 WD (by 1500hrs) |
| 21 | If re-run of Daily Profile Production required then carry this out and send revised Daily Profile Production Reports to relevant Suppliers | SVAA | By +4 WD (by 1730hrs) |
| 22 | Collate information for use in the Interim Information Run<br>Send to SAA:<br>Meter Volume Reallocation Notification, by BM Unit for each Settlement Period<br>Account Bilateral Contract Volumes for each Settlement Period by BSC Party | ECVAA | In accordance with SAA Settlement Calendar |
| 23 | Carry out CDCA Aggregation for Interim Information Volume Allocation Run using the latest available data, i.e. valid actual Meter data and/or agreed estimated Meter data (for all missing or invalid readings) and the latest available approved Line Loss Factors, Aggregation Rules, Registration Data and Meter Technical Details.<br>Send to SAA:<br>BM Unit Metered Volumes for each BM Unit<br>GSP Group Take<br>Interconnector Metered Volumes<br>Send to SVAA:<br>GSP Group Take<br>Send to BSC Parties:<br>GSP Group Take<br>Send to Lead Party and NETSO<br>BM Unit Aggregation Report | CDCA | By + 4 WD (0900hrs) |
| 24 | Ensure Agents send to SVAA:<br>Half Hourly Aggregation Files from HHDAs<br>Half Hourly Metering System Metered Volumes from HHDAs<br>Supplier Purchase Matrices from NHHDAs | Suppliers | By +4 WD (0900hrs) |
| 25 | Ensure Agents send to SAA:<br>BM Unit Eligible Exempt Supply Volumes from ESNAs | Suppliers | For receipt by + 4 WD (0900hrs)<br>2<br>Carry out Interim Information Volume Allocation Run<br>Calculate the Supplier Volume Allocations for each BM Unit<br>Calculate the Supplier BM Unit Period Total Gross Non-Final Demand for each BM Unit<br>Calculate the BM Unit Period Deviation Volume for each BM Unit<br>SVAA<br>By +4 WD (from 0900hrs) |
| 27 | Carry out Load Shaping Run and publish Load Shape data | SVAA | By +4 Calendar Days (1200hrs) |
| 28 | Send to SAA:<br>BM Unit Metered volumes for Supplier BM Units<br>Secondary BM Units Demand Volumes<br>Secondary BM Unit Delivered Volumes<br>Supplier BM Unit Non-Chargeable Demand<br>Supplier BM Unit Period Total Gross Non-Final Demand<br>BM Unit Period Deviation Volume | SVAA | For receipt by + 5 WD (0900hrs)<br>26A<br>[P483] Send to SAA:<br>LLF-adjusted Secondary BM Unit Asset Delivered Volumes<br>LLF-adjusted Secondary BM Unit Asset Delivered Volumes<br>AMVLP<br>For receipt by + 5 WD (0900hrs) |
| 29 | Send Interim Information Volume Allocation Run Reports to relevant Suppliers | SVAA | By +5 WD |
| 30 | Carry out Interim Information Settlement Run using data from CDCA, ECVAA, SVAA, NETSO and MIDPs and send relevant reports to Parties.<br>Issue IIR Credits/Debits Report to ECVAA.<br>Issue BM Unit Non-Chargeable Demand Report to the EMR Settlement Company. Publish TLM-Adjusted Non-Chargeable Demand Report on Elexon Portal. | SAA | By + 5 WD or later if delayed in accordance with the Code |
| 31 | Implement SVAA resolution on profile query or request arbitration from Disputes Administrator | Supplier | By + 5 WD (by 1600hrs) |
| 32 | Ensure Agents send to SVAA:<br>Consumption data from all Data Services (SDS, ADS and UMSDS) | Suppliers | By +6 WD (0000hrs) |
| 33 | Communicate outcome of arbitration to affected Suppliers and SVAA | Dispute Administrator | By +7 WD (by 1000hrs) |
| 34 | If arbitration against SVAA, amend profile variables ready to re-run Daily Profile Production | SVAA | By +7 WD (by 1430hrs) |
| 35 | Implement results from arbitration and send revised profiles to affected Suppliers | SVAA | By +7 WD (by 1800hrs) |
| 36 | Send MSID Pair Delivered Volumes to SVAA | NETSO | By +11 WD3 |
| 37 | Estimate volumes for missing or disputed data in accordance with the Code.<br>Carry out CDCA Aggregation for Initial Volume Allocation Run using the latest available data i.e. valid actual Meter readings and/or any agreed estimates and the latest available approved Line Loss Factors, Aggregation Rules, Registration Data and Meter Technical Details.<br>Send to Parties:<br>GSP Group Take<br>Send to Lead Party and NETSO<br>BM Unit Aggregation Report<br>Send to SVAA:<br>GSP Group Take<br>Send to SAA:<br>CDCA Aggregation File | CDCA | For receipt by +14 WD |
| 38 | Ensure Agents send to SVAA:<br>Half Hourly Aggregation Files from HHDAs<br>Half Hourly Metering System Metered Volumes from HHDAs<br>Supplier Purchase Matrices from NHHDAs<br>Half Hourly Asset Metering System Metered Volumes from HHDCs | Suppliers | AMVLPs<br>By +14 WD |
| 39 | Ensure Agents send to SAA:<br>BM Unit Eligible Exempt Supply Volumes from ESNAs | Suppliers | By + 14 WD |
| 40 | Carry out Initial Volume Allocation Run<br>Calculate the Supplier Volume Allocations for each BM Unit | SVAA | By +15 WD (from 0900hrs) |
| 41 | Send to SAA:<br>BM Unit Metered volumes for Supplier BM Units<br>Secondary BM Units Demand Volumes<br>Secondary BM Unit Delivered Volumes<br>Supplier BM Unit Non BMU ABSVD Volume4<br>Supplier BM Unit Period Total Gross Non-Final Demand<br>BM Unit Period Deviation Volume | SVAA | For receipt by + 16 WD (0900hrs) |
| 42 | Send:<br>Relevant Reports to NETSO<br>DUoS Report to Distribution Businesses<br>Initial Volume Allocation Run Reports to Suppliers | SVAA | By + 16 WD (before 1230hrs)<br>)<br>)By + 17 WD<br>) |
| 43 | Carry out Initial Settlement Run using latest files from NETSO, ECVAA, CDCA and SVAA and MIDPs; and send relevant reports to BSC Parties.<br>Send Settlement Report to FAA | SAA | By +16 WD<br>(subject to SAA Settlement Calendar) or later if delayed in accordance with the Code<br>For receipt by + 17 WD (0900hrs)<br>(subject to Payment Calendar) |
| 44 | Receive Settlement Report from SAA<br>Calculate Payments | FAA | By +17–18 WD<br>(subject to Payment Calendar) |
| 45 | Send Invoices to Payment Parties | FAA | By +17–18 WD<br>(subject to Payment Calendar) |
| 46 | Funds transfers between Parties’ Banks | FAA | By +20–21 WD<br>(subject to Payment Calendar) |

*[Table rebuilt from a flattened web copy-paste. Rows are anchored on the Ref numbers and the Responsibility cell is matched against known party names; the other cell boundaries were inferred.]*

### 4.2 Reconciliation Timetable and Settlement Reports

This section covers all Timetabled Volume Allocation Runs and all Timetabled Reconciliation Settlement Runs. The tasks required for the Interim Information and Initial Settlement Runs are defined in Section 4.1.

The following tasks are repeated at:

T = approximately 39 WD (between 36 and 40 WD) for the 1st Reconciliation Settlement Run;

T = approximately 84 WD (between 81 and 85 WD) for the 2nd Reconciliation Settlement Run;

T = approximately 154 WD (between 151 and 155 WD) for the 3rd Reconciliation Settlement Run; and

T = approximately 292 WD (between 289 and 293 WD) for the Final Reconciliation Settlement Run.

T is the Payment Date, expressed by reference to the Settlement Day.

In each case, the first figure reflects the target to be used in preparing the Payment Calendar, and all dates must be within the range specified in brackets. Precise timings for Reconciliation Settlement Runs and are governed by the Payment Calendar and/or SAA Settlement Calendar for the relevant period.

It should be noted that all tasks relating to all Timetabled Volume Allocation Runs and all Timetabled Reconciliation Settlement Runs may also be repeated in support of a Post Final Settlement Run up to and including 28 months after the Settlement Day5.

| Ref | Task | Responsibility | Time-scale (*) |
|---|---|---|---|
| 1 | Ensure Agents send to SVAA:<br>Revised Consumption data from all Data Services (SDS, ADS and UMSDS) | Suppliers | When Consumption or estimates are revised |
| 2 | Ensure Agents send to SVAA:<br>Revised Half Hourly Aggregation Files from HHDAs<br>Half Hourly Metering System Metered Volumes from HHDAs<br>Revised Supplier Purchase Matrices from NHHDAs | Suppliers | By T – 6 WD<br>Note: Dependent on SVAA Calendar |
| 3 | Estimate volumes for missing or disputed data in accordance with the Code.<br>Re-run Aggregation Process using the latest available data i.e. valid actual Meter data and/or any agreed estimates and the latest approved Line Loss Factors, Aggregation Rules, Registration Data and Meter Technical Details applicable for the relevant Settlement Day.<br>Send to Parties:<br>CDCA Aggregation Reports<br>Send to SVAA:<br>GSP Group Take<br>Send to SAA:<br>CDCA Aggregation File | CDCA | By T – 6 WD<br>Note: Dependent on SAA Settlement Calendar |
| 4 | Carry out Reconciliation Volume Allocation Run<br>Calculate the Supplier Volume Allocation for each BM Unit. | SVAA | By T – 5 WDNote: Dependent on SVAA Calendar |
| 5 | Send to SAA<br>BM Unit Metered Volumes for Supplier BM Units<br>Secondary BM Units Demand Volumes<br>Secondary BM Unit Delivered Volumes<br>Supplier BM Unit Non BMU ABSVD Volume<br>Supplier BM Unit Non-Chargeable Demand | SVAA | For receipt by T – 4 WD (0900hrs)<br>Note: Dependent on SVAA Calendar |
| 6 | Send to SAA<br>BM Unit Eligible Exempt Supply Volumes | ESNA | For receipt by T – 4 WD (0900hrs) |
| 7 | Send:<br>Relevant Reports to NETSO<br>Updated DUoS Report to Distribution Businesses<br>Reconciliation Volume Allocation Run Reports to Suppliers | SVAA | By T – 4 WD (before 1230hrs)<br>)<br>) By T – 3 WD<br>)<br>8 *<br>Carry out Reconciliation Settlement Run using latest available files from NETSO, ECVAA, CDCA and SVAA and MIDP<br>Send to FAA<br>Reconciliation Settlement Report<br>Send to BSC Parties:<br>Reports on financial position<br>Send to EMR Settlement Company<br>BM Unit Non-Chargeable Demand Report<br>SAA<br>By T – 4 WD<br>For receipt by T – 3 (0900hrs) |
| 9 | Receive Reconciliation Settlement Report from SAA (Notification Date)<br>Calculate Payments | FAA | By T – 3 WD |
| 10 | Send to Parties<br>Invoices | FAA | By T – 3 WD |
| 11 | Authorise the financial transfers between Parties’ Banks (Payment Date) | FAA | By T |
| 12 | Send MSID Pair Delivered Volumes to SVAA | NETSO | No later than SD + 45 calendar days6<br>(*) Precise timings are governed by the Payment Calendar and/or SAA Settlement Calendar and/or SVAA Calendar. |

*[Table rebuilt from a flattened web copy-paste. Rows are anchored on the Ref numbers and the Responsibility cell is matched against known party names; the other cell boundaries were inferred.]*

### 4.3 Produce Payment Calendar and SAA Settlement Calendar (transferred to BSCP301)

Note: this has been amended to include both FAA and SAA obligations and has been transferred to BSCP301 (Clearing, Invoicing and Payment).

## 5 Appendices

### 5.1 Interim Information Settlement Run

If the SAA detects invalid or missing data in respect of the relevant Settlement Day prior to carrying out the relevant Settlement Run for the following data items:

Final Physical Notification Data (from BMRA/NETSO)

Balancing Services Adjustment Data (from BMRA/NETSO)

Bid Offer Data (from BMRA/NETSO)

Acceptance Data (from BMRA/NETSO)

BM Unit Applicable Balancing Services Volume Data (from BMRA/NETSO)

BM Unit Metered Volumes for Interconnector BM Units (from IA)

BM Unit Metered Volumes for BM Units other than Supplier BM Units and Interconnector BM Units (from CDCA)

Metered Volume Reallocations by BM Unit (from ECVAA)

Account Bilateral Contract Volumes (from ECVAA)

GSP Group Take for each GSP Group (from CDCA)

Interconnector Metered Volumes (from CDCA); and

Market Index Data (from MIDP)

BM Unit Metered Volumes for Supplier BM Units (from SVAA)

BM Unit Eligible Exempt Supply Volumes (from ESNA)

Secondary BM Units Demand Volumes and Secondary BM Unit Delivered Volumes (from SVAA)

BM Unit Period Non-Chargeable Demand (from SVAA)

LLF-adjusted Secondary BM Unit Asset Delivered Volume and LLF-adjusted Secondary BM Unit Asset Delivered Volumes (from AMVLPs)

Supplier BM Unit Period Total Gross Non-Final Demand and BM Unit Period Deviation Volume (from SVAA)

Then the SAA shall inform BSCCo and proceed in accordance with BSCCo instruction.

In the event that the SAA receives invalid or missing data and is required to consult with BSCCo, the decision on whether and what default data should be substituted shall be at the absolute discretion of BSCCo.

When incomplete data is submitted for an Interim Information Settlement Run, section T1.4.2 of the BSC states that the SAA should form an opinion on whether the proportion of data missing is 'significant', and whether the missing data is likely to be received by the end of the next Business Day, before seeking instructions from BSCCo. In practice, however, both BSCCo and the SAA prefer that BSCCo should take the lead in reaching decisions on these issues. For this reason, the SAA informs BSCCo of missing or invalid data in all cases.

### 5.2 Initial Settlement Run

If the SAA does not expect to receive substantially complete and valid data in respect of the relevant Settlement Day in time to carry out the relevant Settlement Run for the following data items:

Final Physical Notification Data

Balancing Services Adjustment Data

Bid Offer Data

Acceptance Data

BM Unit Applicable Balancing Services Volume Data

BM Unit Metered Volumes for Interconnector BM Units (from IA)

BM Unit Metered Volumes for Supplier BM Units (from SVAA)

BM Unit Eligible Exempt Supply Volumes (from ESNA)

Secondary BM Units Demand Volumes and Secondary BM Unit Delivered Volumes (from SVAA)

Supplier BM Unit Period Total Gross Non-Final Demand and BM Unit Period Deviation Volume (from SVAA)

BM Unit Metered Volumes for BM Units other than Supplier BM Units and Interconnector BM Units (from CDCA)

Metered Volume Reallocations;

Account Bilateral Contract Volumes;

GSP Group Take for each GSP Group;

Interconnector Metered Volumes; and

Market Index Data

The SAA shall consult BSCCo and proceed in accordance with the BSC under BSCCo instruction. The decision by BSCCo on whether and what default data should be substituted shall be at the absolute discretion of BSCCo.

When incomplete data is submitted for an Initial Settlement Run, Section T1.4.5 of the BSC states that the SAA should form an opinion on whether the data is 'substantially complete' before seeking instructions from BSCCo. In practice, however, both BSCCo and the SAA prefer that BSCCo should take the lead in reaching decisions on these issues. For this reason, the SAA will inform BSCCo of missing or invalid data in all cases.

AMENDMENT RECORD

| Version | Details (in source column order: Date / Description of Changes / Changes Included / Mods/ Panel/ / Committee Refs) |
|---|---|
| 1.0 | 08/08/2000<br>Go Active version<br>n/a<br>n/a |
| 2.0 | 30/11/00<br>Work Outstanding at Go Active, resolution of inconsistencies, inclusion of consultation comments.<br>242,191,216<br>08/009 |
| 3.0 | 13/8/02<br>Change Proposals and Code Modifications for BSC Systems Release 2<br>CP563, CP572, CP630; P18A, P49<br>ISG/1 |
| 4.0 | 30/9/02<br>Code Modification P2<br>P2<br>ISG16/166<br>SVG17/208 |
| 5.0 | 27/08/02<br>Phase 2A (Dec 02) Release – Draft<br>CP629, CP639<br>ISG15/151<br>ISG11/093 |
| 6.0 | 25/02/03<br>February 03 Release<br>P71, P78<br>ISG 24/265<br>SVG24/311 |
| 7.0 | 24/06/03<br>June 03 Release<br>CP736<br>ISG17/177 |
| 8.0 | 04/11/03<br>November 03 Release<br>P107, P82<br>59/009<br>54/006 |
| 9.0 | 30/06/04<br>CVA Programme June 04 Release<br>CP945<br>CP854, CP971<br>P82 Removal<br>ISG40/003 |
| 10.0 | 03/11/04<br>CVA Programme Nov 04 Release<br>CP1032<br>TDC58/03 |
| 11.0 | 23/02/05<br>CVA Programme Feb 05 Release<br>CP1091<br>BETTA 6.3<br>P140 |
| 12.0 | 26/06/08<br>June 08 Release<br>CP1223<br>SVG84/02<br>ISG84/01<br>TDC109/01<br>PAB84/11 |
| 13.0 | 05/11/09<br>November 09 Release<br>P217<br>Panel 142/06 |
| 14.0 | 03/11/11<br>November 11 Release<br>P253<br>ISG127/02<br>SVG127/13 |
| 15.0 | 25/06/15<br>June 15 Release<br>CP1426<br>ISG166/06, SVG169/05 |
| 16.0 | 29/06/17<br>June 17 Release<br>P350<br>ISG194/02<br>SVG196/03 |
| 17.0 | 02/11/17<br>November 17 Release<br>P342 Alternative<br>ISG198/04<br>SVG200/03 |
| 18.0 | 29/03/19<br>29 March 19 Standalone Release<br>P369<br>P285/12 |
| 19.0 | 11/12/19<br>11 December 2019 Standalone Release<br>CP1517<br>ISG220/01, SVG223/03 |
| 20.0 | 27/02/2020<br>27 February 2020 Release<br>P394 Self-Governance<br>P297/07 |
| 21.0 | 01/04/2020<br>1 April 2020 Standalone Release<br>P354, P388<br>ISG227/04,<br>SVG 229/07 |
| 22.0 | 01/09/2021<br>1 September 2021 Non-Standard Release<br>P420<br>P316/05 |
| 23.0 | 30/06/2022<br>30 June 2022 Standard Release<br>P375, P433<br>P309/06, P322/05 |
| 24.0 | 23/02/2023<br>23 February 2022 Standard Release<br>P376<br>P314/06 |
| 25.0 | 02/11/2023<br>02 November 2023 Standard Release<br>P395<br>P340/05 |
| 26.0 | 07/11/2024<br>07 November 2024 Standard Release<br>P415 |
| 27.0 | 27/02/2025<br>27 February 2025 Standard Release<br>P442<br>P347/05 |
| 28.0 | 08/04/2025<br>08 April 2025 Non-Standard Release<br>P466 |
| 29.0 | 22/09/2025<br>22 September 2025 Non-Standard Release<br>P478<br>P489<br>P355A/02, P364/09 |
| 30.0 | 27/11/2025<br>27 November 2025 Special Release<br>P483<br>1Virtual Trading Parties may not use Secondary BM Units in MVRNs.<br>2 Where an upheld Trading Dispute is to be processed after the Final Reconciliation Settlement Run has been performed then a Post-Final Settlement Run or Extra-Settlement Determination may be required as described in BSCP11.<br>3 Where such data is available to the NETSO<br>4 Relating to the MSID Pair Delivered Volumes received by the SVAA<br>5 Note that that Post-Final Settlement or Volume Allocation Runs may be requested after 28 months, but only for the purposes of the Rectification of Past Notification Error<br>6 Where such data has not been supplied already under Section 4.1.31 |

*[Amendment record rebuilt from a flattened copy-paste; each row's cells are listed in source column order.]*