# BSC Code Subsidiary Document – Baselining Methodology Document V3.0

> **Source file:** `Baselining Methodology Document V3..txt`  
> **Effective From Date:** 07/11/2024  
> **Status:** LIVE  
> **Converted:** 2026-10-07. Wording kept verbatim from the source copy-paste; only layout artefacts (page headers/footers, line wraps, website navigation, broken tables) were cleaned up. Notes in *[italic square brackets]* are editorial.

---

Balancing and Settlement Code

Code Subsidiary Document

Baselining Methodology Document

Version 3.0

Effective Date: 07 November 2024

Baselining Methodology Document

relating to

Baselining Methodologies For Settlement

This is the Baselining Methodology Document Version 3.0 relating to Baselining Methodologies for Settlement.

This document is Effective from: 07 November 2024

### Intellectual Property Rights, Copyright and Disclaimer

The copyright and other intellectual property rights in this document are vested in ELEXON or appear with the consent of the copyright owner. These materials are made available for you for the purposes of your participation in the electricity industry. If you have an interest in the electricity industry, you may view, download, copy, distribute, modify, transmit, publish, sell or create derivative works (in whatever format) from this document or in other cases use for personal academic or other non-commercial purposes. All copyright and other proprietary notices contained in the document must be retained on any copy you make.

All other rights of the copyright owner not expressly dealt with above are reserved.

No representation, warranty or guarantee is made that the information in this document is accurate or complete. While care is taken in the collection and provision of this information, ELEXON Limited shall not be liable for any errors, omissions, misstatements or mistakes in any information or damages resulting from the use of this information or action taken in reliance on it.

### AMENDMENT RECORD

| Version | Details (in source column order: Date Approved / Description of release / Changes Included / Committee) |
|---|---|
| 1.0 | 06/08/21<br>23 February Standard Release 2023<br>P376<br>P314/06 |
| 2.0 | 13/09/24<br>01 October 2024 Non-Standard Release<br>ORD009<br>Directed by Secretary of State |
| 3.0 | 07/11/24<br>07 November Standard Release 2024<br>P415<br>P339/03 |

*[Amendment record rebuilt from a flattened copy-paste; each row's cells are listed in source order.]*

## 1. INTRODUCTION

This document is the Baselining Methodology Document. It describes one or more Baselining Methodologies approved by the BSC Panel for the purpose of calculating volumes of electricity delivered by Additional BM Units and Secondary BM Units in response to Bid Offer Acceptances or Replacement Reserve Instructions issued by the National Electricity Transmission System Operator (NETSO); and for electricity delivered by Secondary BM Units in the Wholesale Market where a Wholesale Market Activity Notification has been submitted by a Virtual Trading Party (VTP).

Section S13 of the Balancing and Settlement Code (BSC) requires the BSC Panel to establish this document (and subsequently have it in force at all times). This requirement arose from implementation of BSC Modification Proposal P376 (‘Utilising a Baselining Methodology to set Physical Notifications’). Its purpose is to describe one or more approved Baselining Methodologies for calculating volumes of electricity delivered by Suppliers and Virtual Lead Parties (VLPs) in the Balancing Mechanism. Following the implementation of BSC Modification P415 (‘Facilitating access to wholesale markets for flexibility dispatched by Virtual Lead Parties’) this document is also used for calculating electricity delivered by VTPs in the Wholesale Market.

Currently the BSC Panel has approved a single Baselining Methodology, described in section 3.4 below, which will be used for all Baselined MSID Pairs and Baselined AMSID Pairs. The BSC does allow the BSC Panel to approve additional Baselining Methodologies. Any such additional methodology would be introduced into this document using the change process described in section 4 below.

If the BSC Panel were to approve more than one Baselining Methodology, Suppliers, VLPs and VTPs would be able to choose the most appropriate Baselining Methodology for each MSID Pair, and notify the Supplier Volume Allocation Agent of their choice using the Participant Management Platform (in accordance with the process specified in BSC Procedure BSCP602 (‘SVA Metering System Register’)). Similarly Asset Metering Virtual Lead Parties (AMVLPs) would be able to choose the most appropriate Baselining Methodology for each AMSID Pair.

### 1.1 Why does the BSC require a Baselining Methodology Document?

#### 1.1.1 Balancing Mechanism

Prior to the implementation of BSC Modification P376, BSC Systems would always use the Physical Notifications submitted by Lead Parties to the NETSO to determine the volume of electricity delivered by each BM Unit in the Balancing Mechanism:

Lead Parties of BM Units participating in the Balancing Mechanism are required by the BSC (and Grid Code) to submit Physical Notifications to the NETSO. These provide the Lead Party’s best estimate of the MW level of demand or generation that the BM Unit will deliver (in the absence of any Bid Offer Acceptance issued by the NETSO).

The Physical Notification in force at Gate Closure becomes a Final Physical Notification (FPN). The NETSO is required to send the FPN to the Balancing Mechanism Reporting Agent (BMRA) for reporting to the market, and to the Settlement Administration Agent (SAA) for use in Settlement.

The SAA compares the FPN to the BM Unit Metered Volume, in order to verify that the BM Unit has delivered the Bid Offer Acceptance instructed by the NETSO.

Modification Proposal P376 introduced an optional alternative mechanism for verifying that Additional BM Units and Secondary BM Units have delivered Bid Offer Acceptances. A BM Unit making use of this mechanism is referred to as a “Baselined BM Unit”, and is treated as follows in Settlement:

The Lead Party must still submit Physical Notifications to the NETSO (who will continue to use them for purposes of despatch).

The SVAA will use historical metered data to calculate MSID Baseline Values for some or all of the MSID Pairs and/or AMSID Pairs in the BM Unit, in accordance with the Baselining Methodology specified in this document. The Lead Party may choose which of the MSID Pairs and AMSID Pairs within the BM Unit (known as “Baselined MSID Pairs” or “Baselined AMSID Pairs”) SVAA should perform this calculation for.

If there are non-Baselined MSID Pairs or AMSID Pairs in the BM Unit, the Lead Party must provide SVAA with a Submitted Expected Volume. This is equivalent to a Final Physical Notification, but only includes those MSID Pairs (and AMSID Pairs) in the BM Unit that are not Baselined MSID Pairs (or AMSID Pairs).

If an MSID Pair or AMSID Pair has been declared as Baselined, but SVAA is unable to calculate a Baseline Value (due to lack of historic metered data), the Baseline Value will default to the actual Half Hourly meter reading in that Settlement Period. The effect of this is that the MSID Pair or AMSID Pair will be assumed (for purposes of Settlement) not to have contributed to delivery of any Acceptance by the BM Unit. However, this may be corrected in a subsequent Reconciliation Run, if the metered data required to calculate a Baseline Value has become available by that point.

If a VLP knows in advance that there will be insufficient data to calculate a Baselined Value for an MSID Pair or AMSID Pair (and does not wish to include it in their Submitted Expected Volume) they may declare it as “Inactive”. An MSID Pair or AMSID Pair cannot participate in the Balancing Mechanism while it remains Inactive, but SVAA will continue trying to calculate Baseline Values for it, and inform the VLP when there is sufficient data to do so (at which point they may elect to change it from Inactive to Baselined). Note that the option of declaring MSID Pairs to be Inactive is not available for Supplier BM Units (only VLP’s Secondary BM Units).

SVAA will aggregate the Submitted Expected Volume and all of the MSID/AMSID Baseline Values to derive a Settlement Expected Volume (SEVij) (for each Baselined BM Unit and Settlement Period). SVAA will send the Settlement Expected Volume to SAA, who will use it (in place of the FPN) to verify that the BM Unit has delivered the Bid Offer Acceptance instructed by the NETSO.

This mechanism is intended to permit more accurate Settlement of Bid Offer Acceptances, particularly where the BM Unit contains MSID Pairs (or AMSID Pairs) for which it is difficult for the Lead Party to forecast the baseline metered volume accurately. Treating these MSID Pairs (or AMSID Pairs) as Baselined MSID Pairs (or Baselined AMSID Pairs) allows them to be settled using Baseline Values that are calculated:

By a centrally-appointed BSC Agent, using a Panel-approved methodology (providing assurance to all affected Parties that the calculation has been performed in an independent and unbiased way); and

Using up-to-date metered data that would not have been available to the Lead Party in advance (allowing for a more accurate estimate of the baseline).

For Baselined MSID Pairs (and Baselined AMSID Pairs) in Secondary BM Units, the MSID Baseline Values are also used to calculate the Delivered Volumes for each MSID Pair (or AMSID Pair). These Delivered Volumes are used to adjust the Energy Imbalance Position of the Supplier(s) who registered the Metering Systems to remove the effect of the delivery (rather than having the VLP determine the Delivered Volumes, which they are required to do for non-Baselined MSID Pairs and AMSID Pairs).

#### 1.1.2 Wholesale Market

Prior to the implementation of BSC Modification P415 the only access a customer had to obtain any value for any flexibility they had with their energy consumption in the Wholesale Market was via their Supplier.

P415 will enable a VTP to trade Deviation Volumes on the Wholesale Market on behalf of their customer(s). These trades shall be captured in the same manner as existing Parties i.e. via Energy Contract Volume Notifications (ECVN).

Deviation Volumes are a measurable commodity that represent an import/export MWh deviation to the Total System as a result of independent aggregation activity by a VTP.

Trading of Deviaton Volumes by VTPs is restricted to Baselined BM Units, and the process is essentially the same as that usd by VLPs in the BM:

The Lead Party (i.e. the VTP) must submit a Wholesale Market Activity Notification to the SVAA via the Energy Contract Volume Aggregation Agent (ECVAA).

The SVAA will use historical metered data to calculate MSID Baseline Values for all of the MSID Pairs and/or AMSID Pairs in the BM Unit, in accordance with the Baselining Methodology specified in this document. The Lead Party may choose which of the MSID Pairs and AMSID Pairs within the BM Unit (known as “Baselined MSID Pairs” or “Baselined AMSID Pairs”) SVAA should perform this calculation for.

If there are non-Baselined MSID Pairs or AMSID Pairs in the BM Unit, the Lead Party must provide SVAA with a Submitted Expected Volume. This only includes those MSID Pairs (and AMSID Pairs) in the BM Unit that are not Baselined MSID Pairs (or AMSID Pairs).

If an MSID Pair or AMSID Pair has been declared as Baselined, but SVAA is unable to calculate a Baseline Value (due to lack of historic metered data), the Baseline Value will default to the actual Half Hourly meter reading in that Settlement Period. The effect of this is that the MSID Pair or AMSID Pair will be assumed (for purposes of Settlement) not to have contributed to delivery of any energy in the Wholesale Market by the BM Unit. However, this may be corrected in a subsequent Reconciliation Run, if the metered data required to calculate a Baseline Value has become available by that point.

If a VTP knows in advance that there will be insufficient data to calculate a Baselined Value for an MSID Pair or AMSID Pair they may declare it as “Inactive”. An MSID Pair or AMSID Pair cannot participate in the Wholesale Market while it remains Inactive, but SVAA will continue trying to calculate Baseline Values for it, and inform the VTP when there is sufficient data to do so (at which point they may elect to change it from Inactive to Baselined). Note that the option of declaring MSID Pairs to be Inactive is only for VTP’s Trading Secondary BM Units.

SVAA will aggregate the Submitted Expected Volume and all of the MSID and AMSID Baseline Values to derive a Settlement Expected Volume (SEVij) (for each Baselined BM Unit and Settlement Period). SVAA will send the Settlement Expected Volume to SAA.

Note that a Party who has Qualified as both a VTP and a VLP may use their Baselined BM Units both in the BM, and to trade Deviation Volumes. In this case the baseline calculated by SVAA will be used for both purposes.

For the avoidance of doubt, any queries on the Baselining Methodologies and baselining techniques should be directed to the BSC Service Desk.

### 1.2 Scope of the Baselining Methodology Document

This Baselining Methodology Document uses the term “Baselined Entity” for any Metering System (or combination of Metering Systems) for which a Baseline Value must be calculated. The requirement to calculate Baseline Values is defined in paragraph 7.3.1 of BSC Annex S-2, which defines three types of Baselined Entity. The methodology used to calculate the Baseline Values is the same in each case, but the calculated Baseline Values are given different names in the legal text:

| Baselined Entity | Name for calculated Baseline Value |
|---|---|
| Metering System in Baselined MSID Pair | MSID Baseline Value (MBVKiLj) |
| Metering System in Baselined AMSID Pair | AMSID Baseline Value (AMBVKiLj) |
| Asset Differencing scheme (i.e. the net Import of all MSID Pairs and AMSID Pairs involved in a given instance of Asset Differencing) | Net Differencing Baseline Value (NDBVij) |

Figure 1 summarises the context of the baseline calculations described in this document:

*[Figure 1 is a diagram in the original. Only its text labels were captured in the copy-paste (listed below in source order); the arrows and layout are not available.]*

- Details of Settlement Periods in which VTP submitted a Wholesale Market Activity Notification
- Details of Baselined Entities (notified by Lead Party in accordance with BSCP602)
- Baseline Values (for use in subsequent Settlement calculations)
- Metered Data (provided by HHDCs & HHDAs in accordance with BSCP503 & BSCP502)
- Baseline Calculations (as specified in this document)
- Details of Settlement Periods in which NETSO instructed each Baseline BM Unit
- Details of Event Days (notified by Lead Party for each MSID Pair in accordance with BSCP602)
- Details of Baselined Entities for which no baseline could be calculated, due to insufficient data (for reporting to Lead Party)

**Figure 1 – Context of the Baseline calculations**

Note that Baseline Values are calculated (subject to availability of data) for all Baselined Entities, including MSID Pairs and AMSID Pairs that the Lead Party has declared to be Inactive. However, the Baseline Values for Inactive MSID Pairs and Inactive AMSID Pairs are excluded from subsequent Settlement calculations (in accordance with Annex S-2 of the BSC).

The Baselining Methodology Document contains the following information:

(a) Details of the approved baseline techniques;

(b) Full definitions of the particular data and methodology to be used by the SVAA in determining the Baseline Values for each Settlement Period;

(c) Details of the types of event that can be treated as causing an Event Day for purposes of the Methodology (see Appendix A); and

(d) The processes that will be used to make changes to this Baselining Methodology Document.

It does not include:

(a) Details of the processes used by Lead Parties to notify SVAA of Baselined MSID Pairs and AMSID Pairs, and their associated Event Days. These processes are specified in BSC Procedure BSCP602 (‘SVA Metering System Register’); or

(b) Details of how MSID Baseline Values calculated in accordance with this Methodology Document are then adjusted for line losses, and used to calculate Settlement Expected Volumes and Delivered Volumes. Details of these calculations are specified in Annex S-2 of the BSC; or

(c) Details of the processes used by Lead Parties to submit a Wholesale Market Activity Notification to SVAA via ECVAA. These processes are specified in BSC Procedure BSCP602 (‘SVA Metering System Register’).

### 1.3 Main Users of the Baselining Methodology Document

The main users of this Baselining Methodology Document are:

SVAA;

Virtual Lead Parties;

Virtual Trading Parties;

Suppliers; and

BSC Panel

## 2 ACRONYMS AND DEFINITIONS

### 2.1 List of Acronyms

The following is a list of acronyms used in this Baselining Methodology Document:

| Acronym | Expression |
|---|---|
| AMVLP | Asset Metering Virtual Lead Party |
| BMRA | Balancing Mechanism Reporting Agent |
| BSC | Balancing and Settlement Code |
| ECVAA | Energy Contract Volume Aggregation Agent |
| ECVN | Energy Contract Volume Notifications |
| FPN | Final Physical Notification |
| HHDA | Half Hourly Data Aggregator |
| NETSO | National Electricity Transmission System Operator |
| SAA | Settlement Administration Agent |
| SVAA | Supplier Volume Allocation Agent |
| VLP | Virtual Lead Party |
| VTP | Virtual Trading Party |

### 2.2 List of Definitions

The following is a list of definitions used in this Baselining Methodology Document:

| Term | Definition |
|---|---|
| Acceptance | Has the meaning given to that term in Annex X-1 of the BSC. |
| Additional BM Unit | Has the meaning given to that term in Annex X-1 of the BSC. |
| AMSID Baseline Value | Has the meaning given to that term in Annex S-2 of the BSC. |
| AMSID Pair | Has the meaning given to that term in Annex X-1 of the BSC. |
| Asset Differencing | Has the meaning given to that term in Annex X-1 of the BSC. |
| Asset Metering Virtual Lead Party | A Virtual Lead Party (VLP) who has Qualified (in accordance with BSCP537) to register Asset Metering Systems and allocate AMSID Pairs to Secondary BM Units. |
| Balancing Service | Has the meaning given to that term in the ESO Licence. |
| Baseline Value | An MSID Baseline Value, AMSID Baseline Value or Net Differencing Baseline Value. |
| Baselined AMSID Pair | Has the meaning given to that term in Annex X-1 of the BSC. |
| Baselined BM Unit | Has the meaning given to that term in Annex X-1 of the BSC. |
| Baselined Entity | A Metering System or Metering System(s) for which paragraph 7.3.1 of BSC Annex S-2 requires Baseline Values to be calculated. A Baselined Entity may be either:<br>An MSID Pair;<br>An AMSID Pair; or<br>A set of SVA Metering Systems and Asset Metering Systems that are related to each other for purposes of Asset Differencing. |
| Baselined Entity Metered Volume | In relation to a Baselined Entity to which Approved Baselining Methodology BL01 applies, the net Import of the Baselined Entity (in a historical Settlement Period), calculated in accordance with section 3.4.2 of this Baselining Methodology Document. |
| Baselined MSID Pair | Has the meaning given to that term in Annex X-1 of the BSC. |
| Baselining Methodology | Has the meaning given to that term in Annex X-1 of the BSC. |
| Baselining Methodology Document | Has the meaning given to that term in Annex X-1 of the BSC. |
| BSC Auditor | Has the meaning given to that term in Annex X-1 of the BSC. |
| BSCCo | Has the meaning given to that term in Annex X-1 of the BSC. |
| Deviation Volume | Has the meaning given to that term in Annex X-2 of the BSC. |
| Eligible Day | An historical Settlement Day which meets certain criteria allowing data from that day to be used in the calculation of MSID Baseline Values. For Approved Baselining Methodology BL01, the criteria for a Settlement Day to be an Eligible Day are defined in section 3.4.1 of this Baselining Methodology Document. |
| Event Day | A Settlement Day affected by any of the circumstances listed in Appendix A of this Baselining Methodology Document, about which the Lead Party has notified SVAA in accordance with BSC Procedure BSCP602. |
| Gate Closure | Has the meaning given to that term in Annex X-1 of the BSC. |
| Inactive AMSID Pair | Has the meaning given to that term in Annex X-1 of the BSC. |
| Inactive MSID Pair | Has the meaning given to that term in Annex X-1 of the BSC. |
| In Day Adjustment | An additive adjustment to the baseline, used to adjust its level to more closely match outturn demand on the given Settlement Day. For Approved Baselining Methodology BL01, the calculation of the In Day Adjustment is defined in section 3.4.3 of this Baselining Methodology Document. |
| In Day Reference Window | A period immediately prior to despatch of a BM Unit, used to calculate an In Day Adjustment for each Baselined Entity within that BM Unit. For Approved Baselining Methodology BL01, the In Day Reference Window is three hours long, as defined in section 3.4.3 of this Baselining Methodology Document. |
| MSID Baseline Value | Has the meaning given to that term in Annex S-2 of the BSC. |
| MSID Pair | Has the meaning given to that term in Annex X-1 of the BSC. |
| Net Differencing Baseline Value | Has the meaning given to that term in Annex S-2 of the BSC. |
| Non-Working Day | A Settlement Day that is not a Working Day. |
| Participant Management Platform | An IT System established by Elexon that (among other functions) allows the SVAA to record notifications of MSID Pairs submitted by Suppliers and Virtual Lead Parties. |
| Secondary BM Unit | Has the meaning given to that term in Annex X-1 of the BSC. |
| Settlement Day | Has the meaning given to that term in Annex X-1 of the BSC. |
| Settlement Period | Has the meaning given to that term in Annex X-2 of the BSC. |
| Technical Assurance Agent | Has the meaning given to that term in Annex X-1 of the BSC. |
| Unadjusted Baseline Value | In relation to a Baselined Entity to which Approved Baselining Methodology BL01 applies, the baseline value calculated by SVAA, prior to applying the In Day Adjustment. This is an intermediate data item within the BL01 methodology, calculated in accordance with section 3.4.2 of this Baselining Methodology Document. |
| Virtual Lead Party | Has the meaning given to that term in Annex X-1 of the BSC. |
| Virtual Trading Party | Has the meaning given to that term in Annex X-1 of the BSC. |
| Wholesale Market Activity Notification | Has the meaning given to that term in Annex X-1 of the BSC. |
| Working Day | Has the meaning given to that term in Annex X-1 of the BSC. |

## 3 DETAILED REQUIREMENTS FOR CALCULATION OF MSID BASELINE VALUES

### 3.1 Inputs to the calculation

The input data required to calculate Baseline Values (for a Settlement Day D) is as follows:

Details of the Baselined Entities for which data is to be calculated (and the Baselined BM Unit to which each Baselined Entity belongs). This data is notified to SVAA by the Lead Party in accordance with BSC Procedure BSCP602.

The Metered data for each Baselined Entity. Metered data is required for the Settlement Day D, and as many as possible of the previous 60 Settlement Days. If insufficient Metered Data is available, it may not be possible to calculate Baseline Values (in which case the Baseline Value will be set equal to the Metered Data for that Settlement Period, effectively deeming there to have been no volume delivered). The source of this metered data depends upon the type of Baselined Entity:

For MSID Pairs, Metering System Metered Consumption (VMMCHZaNLKji) values are required for each of the SVA Metering System(s) in the MSID Pair. The VMMCHZaNLKji values are in MWh, and are calculated by SVAA from Metered data provided by Half Hourly Data Aggregators (HHDAs). The process for provision of Metered data to SVAA by HHDAs is described in BSC Procedure BSCP503 (‘Half Hourly Data Aggregation for SVA Metering Systems Registered in SMRS’);

For AMSID Pairs, Asset Metering System Metered Consumption (VMMCHNLKj) values are required for each of the Asset Metering System(s) in the AMSID Pair. The VMMCHNLKj values are in MWh, and are calculated by SVAA from Metered data provided by Half Hourly Data Collectors (HHDCs). The process for provision of Metered data to SVAA by HHDCs is described in BSC Procedure BSCP603 (‘Meter Operations and Data Collection for Asset Metering Systems’); and

For Asset Differencing, the required Metered data are Net Differencing Volume (VNDKj) values calculated by the SVAA in accordance with BSC Annex S-2 paragraph 7.1.1C.

Details of which Settlement Periods (if any) each Baselined BM Unit received an Acceptance from the NETSO. This information is sent to SVAA each day by the Settlement Administration Agent (the Daily Activations Report).

Details of which Settlement Periods (if any) each Baselined BM Unit had a Wholesale Market Activity Notification submitted by the VTP.

Details (for each MSID Pair or AMSID Pair) of Settlement Days which should be treated as Event Days. These details are notified to SVAA by the Lead Party in accordance with BSC Procedure BSCP602

### 3.2 Outputs of the Calculation

The minimum required outputs of any approved Baselining Methodology (for a Settlement Day D) are:

A Boolean (True or False) indicator of whether there was sufficient Metered data available to calculate a Baseline Value. This is required for every Baselined Entity, and is reported to the Lead Party of the BM Unit.

A Baseline Value for each Baselined Entity and Settlement Period. This is required for every Baselined Entity. The Baseline Value must be in units of MWh, and represent an estimate of what the net Metered data would have been for the Metering System(s) included in the Baselined Entity, in the absence of any Acceptance from the NETSO.or Wholesale Market Activity Notifications being received. Where insufficient historic data is available to calculate a Baseline Value, the Baseline Value will default to the Metered data value for the individual Settlement Period.

These outputs are required for all Baselined Entities (including Inactive MSID Pairs and Inactive AMSID Pairs). However, the Baseline Values calculated for Inactive MSID Pairs and Inactive AMSID Pairs will not be used in subsequent Settlement calculations (and are available only for reporting and monitoring purposes).

In addition to these generic outputs (which apply to all approved Baselining Methodologies), specific Baselining Methodologies may produce additional outputs (for reporting and monitoring purposes), as specified in each relevant section below.

### 3.3 Summary of Approved Baselining Methodologies

The BSC allows for the possibility of multiple Baselining Methodologies (for example, to cater for different types of generation or demand side response). Section 4 below describes the process by which the BSC Panel may add or amend Baselining Methodologies. Currently there is a single approved Baselining Methodology (BL01) that will therefore be applied to all Baselined MSID Pairs.

Table 1 below summarises the key features of each approved Baselining Methodology:

**Table 1 – Summary of Approved Baselining Methodologies**

| Methodology Id | Data range | Selection criteria | Selected data | Working Day | Non Working Day |
|---|---|---|---|---|---|
| BL01 | 60 days | Is a like day (e.g. Working/Non-Working) | Up to 10 days for Working Days, 4 days for Non-Working Days | Straight average over available data | Straight average of middle 2 days |

*[Table rebuilt from a flattened copy-paste. The Working Day / Non Working Day columns appear to sit under a parent header (the calculation applied) that was not captured.]*

### 3.4 Baselining Methodology BL01

The process by which Baselining Methodology BL01 calculates Baseline Values for a Baselined Entity on a given Settlement Day D can be summarised as follows:

Identify the required number of previous Settlement Days of the same type (Working or Non-Working) for which Metered data is available, as described in section 3.4.1 below. If insufficient days are available, the Baseline Value will default to the Metered data for the same Settlement Period (i.e. the Baseline will equal the out-turn Metered data), and the Metering System(s) in the Baselined Entity will be reported to the Lead Party as having insufficient data.

For each Settlement Period, calculate an Unadjusted Baseline Value (for the Baselined Entity) by averaging the Metered data values of the corresponding Settlement Period in some or all of the previous days identified in step 1. See 3.4.2 below for details of which days are included in the average, and the treatment of clock change days (at the start and end of British Summer Time).

If the BM Unit containing the Baselined Entity was issued with an Acceptance by the NETSO in any Settlement Period of the day, calculate an In Day Adjustment, and add it to the Unadjusted Baseline Value – see section 3.4.3 below. Where no Acceptance was issued, but a Wholesale Market Activity Notification was submitted by a VTP, the In Day Adjustment value will be set to zero – see section 3.4.3 below. Where no acceptance was issued or Wholesale Market Activity Notice was submitted, a separate In Day Adjustment will be calculated for each Settlement Period of the Settlement Day (purely to facilitate assurance of the Baselining Methodology, not for purposes of Settlement).

Allocate the calculated baseline values to the Import or Export Metering System (depending on whether they are positive or negative) – see section 3.4.4 below.

#### 3.4.1 BL01 Step 1 – Identify historical days with metered data

Step 1 of the BL01 process is to identify the historical Settlement Days (in the sixty-day window from day D–60 to day D–1) that will be used to calculate the baseline. The process begins with SVAA identifying all “Eligible Days” for the Baselined Entity i.e. Settlement Days in the 60-day window that:

Are of the same time type (Working Day or non-Working Day) as day D;

Have Metered data available for the Baselined Entity, as follows:

For an MSID Pair, VMMCHZaNLKji values must be available for the Import Metering System and (if there is one) the Export Metering System;

For an AMSID Pair, VMMCHNLKj values must be available for the Import Metering System and (if there is one) the Export Metering System; and

For Asset Differencing, values of Net Differencing Volume (VNDKj) must be available.

Note that this data does not have to relate to the current Settlement Run Type (i.e. SVAA will default to a previous Settlement Run for the same Settlement Day, if data is not available for the current Settlement Run);

Have not been notified to SVAA by the Lead Party as being an Event Day for the Baselined MSID Pair or Baselined AMSID Pair (see Appendix A); and

Are not ‘clock change’ days (i.e. the calendar days at the start and end of British Summer Time, currently the last Sunday of March and October).

Having identified the Eligible Days, those used to calculate the baseline will be selected (four for a non-Working Day, and up to 10 for a Working Day), in accordance with Table 2 below:

**Table 2 – Selection of Eligible Days for use in calculating the baseline**

| Day Type | No. of Eligible Days identified in the 60-day window | Historical Settlement Days used to calculate the baseline |
|---|---|---|
| Working Day | Ten or more Eligible Days | Ten most recent Eligible Days |
| Working Day | Five to Nine Eligible Days | All Eligible Days |
| Working Day | Less than five Eligible Days | Baseline Values default to out-turn Metered data for the Metering System(s) in the Baselined Entity, and they will be reported to the Lead Party as having insufficient data. |
| Non-Working Day | Four or more Eligible Days | Four most recent Eligible Days |
| Non-Working Day | Less than four Eligible Days | Baseline Values will default to out-turn Metered data for the Metering System(s) in the Baselined Entity, and they will be reported to the Lead Party as having insufficient data. |

#### 3.4.2 BL01 Step 2 – Calculate Unadjusted Baseline Value

Step 2 of the BL01 methodology is for SVAA to calculate an Unadjusted Baseline Value (for each Settlement Period of the Settlement Day D), as follows:

Calculate the net Metered data (“Baselined Entity Metered Volume”) for the Baselined Entity (for each Settlement Period of each historical Settlement Day identified in step 1). These Baselined Entity Metered Volumes represents the net Import for the Baselined Entity (with negative values representing net Export), and are calculated as follows:

For MSID Pairs, subtract the VMMCHZaNLKji value for the Export Metering System (if there is one) from the VMMCHZaNLKji value for the Import Metering System;

For AMSID Pairs, subtract the VMMCHNLKj value for the Export Metering System (if there is one) from the VMMCHNLKj value for the Import Metering System; and

For Asset Differencing, the Baselined Entity Metered Volume is equal to the Net Differencing Volume (VNDKj)

Identify the subset of historical Settlement Days (identified in step 1) that will be used to calculate the Unadjusted Baseline Value:

For a Working Day, all of the six to 10 Eligible Days identified in step 1 will be used; and

For a Non-Working Day, two of the four Eligible Days identified in step 1 will be used. The two selected will be the middle two of the four (ranking them in order of the total Baselined Entity Metered Volume, summed over the Settlement Day)

For each Settlement Period in Settlement Day D, calculate the Unadjusted Baseline Value as the arithmetic mean of the Baselined Entity Metered Volume in the corresponding Settlement Period of each of the historical days identified in step (b).

**Treatment of Clock Change Days**

Where Settlement Day D is a clock change day, step (c) must take this into account when identifying the corresponding Settlement Period in each historical Settlement Day. When Settlement Day D is a ‘long day’, containing 50 Settlement Periods, the mapping is as follows:

Settlement Periods 1-2 on Settlement Day D correspond to Settlement Periods 1-2 on the historical Settlement Day;

Settlement Periods 3-4 on Settlement Day D also correspond to Settlement Periods 1-2 on the historical Settlement Day; and

Settlement Periods 5-50 on Settlement Day D correspond to Settlement Periods 3-48 on the historical Settlement Day.

When Settlement Day D is a ‘short day’, containing 46 Settlement Periods, the mapping is as follows:

Settlement Periods 1-2 on Settlement Day D correspond to Settlement Periods 1-2 on the historical Settlement Day; and

Settlement Periods 3-46 on Settlement Day D correspond to Settlement Periods 5-48 on the historical Settlement Day.

Note that these are the same rules used for Energy Contract Volume Notifications (in Section P of the BSC).

#### 3.4.3 BL01 Step 3 – Calculate In Day Adjustment

The Unadjusted Baseline Values create a profile shape for a day based on previous days’ data, but will not account fully for variations in factors such as weather and temperature. For this reason, In Day Adjustments are used, where the BM Unit containing the Baselined Entity was issued with an Acceptance by the NETSO, to provide an up or down lift, ensuring the values used in Settlement calculations are better representative of conditions on the day.

The In Day Adjustment will consider actual Metered data over the three hour period up until Gate Closure. This will be compared to the calculated values and an additive adjustment applied to ensure that the profile created by the baseline best matches real data for the run up to the Settlement Period. In other words:

```
In Day Adjustment = ∑j (Baselined Entity Metered Volume – Unadjusted Baseline Value) / 6
```

where ∑j represents summation over the six Settlement Periods in the “In Day Reference Window”. The In Day Reference Window is defined as the three hour period ending at Gate Closure for the first Settlement Period in Settlement Day D for which the BM Unit containing the MSID Pair received an Acceptance from National Grid.

Note that:

For an Acceptance in the first three hours of the Settlement Day, the In Day Reference Window will stretch back into the previous Settlement Day (D-1). In this case the calculation of the In Day Adjustment will require Baseline Values and Baselined Entity Metered Volumes for day (D-1) as well as day D.

If the Baselined Entity Metered Volumes and/or Unadjusted Baseline Values required to calculate the In Day Adjustment are not available, SVAA shall set the In Day Adjustment to zero. This is most likely to happen if day D is the first Settlement Day for which data was available to calculate a baseline, but the In Day Reference Window falls partly or wholly into the previous Settlement Day.

If the BM Unit containing the MSID Pair and/or AMSID Pair did not receive any Acceptances from the NETSO on Settlement Day D, there is no Settlement requirement to calculate an In Day Adjustment. But for assurance purposes (to allow monitoring of how well the Baselining Methodology is functioning), SVAA will calculate a separate In Day Adjustment for each Settlement Period of the Settlement Day – see section 3.4.3.1 below.

Where an MSID Pair is dispatched multiple times on the same day, it will not be possible to calculate a second In Day Adjustment, as the data will have been contaminated by the first dispatch. Therefore the same In Day Adjustment will also be applied to the profile shape for any subsequent dispatches.

3.4.3.1 In Day Adjustments for Settlement Days without Acceptances

As explained above, the In Day Reference Window (for a BM Unit with one or more Acceptances) ends at Gate Closure for the first Settlement Period that has an Acceptance. This definition is intended to ensure that metered volumes during the In Day Reference Window (and hence the In Day Adjustment calculated from them) reflect the behaviour of the site in the absence of any Acceptance being issued.

If the BM Unit containing the MSID Pair and/or AMSID Pair did not have any Acceptances, no In Day Adjustment will be made:

If the BM Unit had a Wholesale Market Activity Notification, no adjustment will be made i.e. the In Day Adjustment will be zero.

If the BM Unit did not have an Acceptance or a Wholesale Market Activity Notification, SVAA will calculate a separate In Day Adjustment for each Settlement Period of the Settlement Day. For the purposes of this calculation, the In Day Reference Window for each Settlement Period is defined as the period of three hours ending at Gate Closure for that Settlement Period.

This calculation is intended to produce Baseline Values for each Settlement Period that reflect the values that would have been used in Settlement, had the BM Unit received an Acceptance starting in that Settlement Period. This will facilitate monitoring and analysis of the accuracy of the Baselining Methodology. However, none of them will be used in Settlement.

For the avoidance of doubt, if the BM Unit containing the MSID Pair, and/or AMSID Pair received no Acceptances in the Settlement Day, the In Day Adjustment used in Settlement will be zero.

#### 3.4.4 BL01 Step 4 – Calculate Baseline Values

For each Baselined Entity (and each Settlement Period within Settlement Day D), SVAA will now calculate the Baseline Value:

Baseline Value = Unadjusted Baseline Value + In Day Adjustment

For MSID Pairs and AMSID Pairs, Annex S-2 of the BSC assumes that the Baselining Methodology will calculate separate Baseline Values for the Import and Export Metering Systems. This can be done by splitting out the positive and negative values.

For the Import Metering System:

Baseline Value = Max (Baseline Value, 0)

For the Export Metering System (if the MSID Pair or AMSID Pair contains one):

Baseline Value = – Min (Baseline Value, 0)

## 4 PROCESS FOR AMENDING THIS BASELINING METHODOLOGY DOCUMENT

Section S13.2 of the BSC requires the BSC Panel to keep this document updated:

13.2 The Panel shall review the Baselining Methodology Document from time to time and in any event if there is a significant change which may lead to historic metered data not reflecting future volumes due to but not limited to;

(a) significant changes to Network Charges; and

(b) events which lead to large changes to demand such as a National epidemic

and shall make such revisions to the Baselining Methodology Document as necessary.

For the purposes of BSC Procedure BSCP40 (‘Change Management’) this document is a Category 3 BSC Configurable Item, meaning that it is not subject to the Modification Procedures in Section F (‘Modification Procedures’) of the BSC, or the Change Proposal process described in BSCP40. The Panel has agreed the following process for changes:

It is the BSC Panel’s decision whether to review or change the Methodology, but BSCCo or any Supplier or VLP or VTP can request them to do so;

The BSC Panel may request assistance from BSCCo e.g. in analysing whether a change is needed;

Unless otherwise agreed by the BSC Panel, changes to the document will be drafted by BSCCo; and

The BSC Panel will consult with Parties in a manner appropriate to the scale and complexity of the changes before agreeing them.

It should be noted that any material change to the Methodology will require changes to Settlement systems, and the BSC Panel would take this into account when agreeing the effective date for any change.

Examples of possible reasons for a Supplier, VLP, or VTP to request a change to the Methodology include (but are not limited to):

Those identified in BSC Section S13.2; and

Identification of specific generation or demand side response technologies that are not accurately baselined by the existing approved Baselining Methodology (or Methodologies).

## APPENDIX A: DEFINITION OF EVENT DAYS

Section S15 of the BSC and BSC Procedure BSCP602 specify the process by which Lead Parties may notify SVAA of an Event Day (for a Baselined MSID Pair or Baselined AMSID Pair). A Party may treat a Settlement Day as an Event Day if the metered volumes for that MISD Pair or AMSID Pair on that Settlement Day are affected by:

Delivery of a Balancing Service;

Virtual Trading,

A Site outage;

Equipment failure; and/or

Site Disconnection.

The Lead Party must retain evidence that the Event Day met these criteria, and provide that evidence upon request to BSCCo, the BSC Auditor or the Technical Assurance Agent (if required for assurance purposes).