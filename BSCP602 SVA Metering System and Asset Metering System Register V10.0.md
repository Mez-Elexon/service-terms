# BSCP602: SVA Metering System & Asset Metering System Register V10.0

> **Source file:** `BSCP602.txt`  
> **Effective From Date:** 27/11/2025  
> **Status:** LIVE  
> **Converted:** 2026-10-07. Wording kept verbatim from the source copy-paste; only layout artefacts (page headers/footers, line wraps, website navigation, broken tables) were cleaned up. Notes in *[italic square brackets]* are editorial.

---

Balancing and Settlement Code

BSC Procedure

SVA METERING SYSTEM & ASSET METERING SYSTEM REGISTER

BSCP602

Version 10.0

Date: 27 November 2025

BSCP602

relating to the

SVA Metering System & Asset Metering System & Asset Metering System Register

1. Reference is made to the Balancing and Settlement Code and, in particular, to the definition of “BSC Procedure” in Section X, Annex X-1 thereof.

2. This is BSC Procedure 602, Version 10.0 relating to the SVA Metering and Asset Metering System Register.

3. This BSC Procedure is effective from 27 November 2025.

4. This BSC Procedure has been approved by the BSC Panel or its relevant delegated Panel Committee(s).

## 1 Introduction

### 1.1 Purpose and Scope of the Procedure

The purpose of this Balancing and Settlement Code Procedure (BSCP) is to set out the processes for MSIDS, MSID Pair and AMSID Pair allocation for supporting the calculation of network charges, Final Consumption Levy (FCL) charges1, Deviation Volumes relating to Trading Secondary BM Units registered to Virtual Trading Parties (VTPs) and for Submitting Expected Volumes, informing about Wholesale Market trades and registering Event days.

Please refer to BSCP607 for processes relating to Asset Metering Systems located behind Metering Systems which are Non Half Hourly or, for MHHS Metering Systems, are not capable of recording UTC Period Level Consumption for Settlement purposes.

#### 1.1.1 MSID Pair and AMSID Pair allocation

This BSCP sets out the processes that:

Suppliers, VTPs, Virtual Lead Parties (VLPs), Asset Metering Virtual Lead Parties (AMVLPs2) and the NETSO should follow when submitting MSID Pair allocation(s) and MSID Pair Delivered Volumes to the SVAA;

AMVLPs3 and Suppliers should follow when registering an Asset thus creating AMSID number(s) and an AMSID Pair; and

AMVLPs should follow when submitting MSID Pair allocation(s) and AMSID Pair allocation(s) and MSID Pair Delivered Volumes or AMSID Pair Delivered Volumes to the SVAA.

A MSID Pair allocation is the notification from the Lead Party (i.e. Supplier, VTP, VLP or AMVLP) or the NETSO of MSID Pairs that may be used for the purposes of providing Balancing Services4 or Applicable Balancing Services to the NETSO. Where the MSID Pair allocation is notified by a Lead Party, the BM Unit Id must be provided along with all MSID Pairs associated with that BM Unit. Where a MSID Pair allocation is notified by the NETSO, no association with a BM Unit will be required.

All references to MSIDs in this BSCP602 relate to Metering Systems which are Half Hourly or, for MHHS Metering Systems, are capable of recording UTC Period Level Consumption for Settlement purposes.

An AMSID Pair allocation is the notification from the AMVLP of an AMSID Pair that may be used for the purposes of providing Balancing Services as part of a Secondary BM Unit. An AMSID Pair allocation must specify the MSID Pair in the Secondary BM Unit behind which the AMSID Pair is located (the “Associated MSID Pair”) and which should be used in conjunction with the AMSID Pair in Settlement calculations, all related AMSID Pairs and an indicator whether the AMSID Pair Delivered Volume will be used for Asset Metering or for Asset Differencing.

Note that one or more AMSID Pairs may be associated with one or more MSID Pairs in a Secondary BM Unit. The paragraph above describes the scenario where one AMSID Pair is associated with one Boundary Point MSID Pair.

Appendix 3.8 defines Asset Metering and Asset Differencing and Appendix 3.9 sets out the valid combinations of MSID Pair Indicator and AMSID Pair Asset Differencing Indicator allowed in a Secondary BM Unit for these different uses of AMSID Pairs.

An ‘MSID Pair’ means one SVA Import Metering System and, where applicable, one SVA Export Metering System situated at a single Boundary Point. To clarify, an MSID Pair must contain an SVA Import Metering System but does not always have to contain a SVA Export Metering System. All Metering Systems in an MSID Pair must be able to record UTC Period Level Consumption for use in Settlement.

An ‘AMSID Pair’ means one AMSID measuring the flow of electricity to the Asset and, where applicable, one AMSID measuring the flow of electricity from the Asset, whose Half Hourly Metering Systems are used for the purposes of offering Balancing Services.

An ‘Associated MSID Pair’ is, in relation to an AMSID Pair, a Boundary Point MSID Pair which is included in the same Secondary BM Unit as that AMSID Pair and is connected to the Asset to which the AMSID Pair relates. Note that an AMSID Pair can have more than one Associated MSID Pair, if the Asset sits behind more than one Boundary Points on a site. If an AMSID Pair is involved in two Secondary BM Units (one for Asset Metering and one for Asset Differencing), it must have different Associated MSID Pair(s) in each Secondary BM Unit (see section 3.9-3.11 for allowed combinations of MSID Pairs and AMSID Pairs in a Secondary BM Unit).

This BSC Procedure focuses on the interfaces between Lead Parties or the NETSO and the SVAA seen from the perspective of the Lead Party or the NETSO.

The purpose of this procedure is:

to ensure maintenance of an accurate, up-to-date SVA Metering System and Asset Metering System Register;

to ensure the correct working of the SVAA internal processing for use in validating submissions of MSID Pair Allocations and AMSID Pair Allocations to the SVA Metering System Register;

to ensure MSID Pair Delivered Volumes and AMSID Pair Delivered Volumes are determined in good faith, in accordance with Good Industry Practice and notified in a timely manner; and

to ensure the correct working of the SVAA internal processing for use in validating MSID Pair Delivered Volumes and AMSID Pair Delivered Volumes.

#### 1.1.2 Supporting the calculation of network charges

The SVAA must regularly produce and send the P0210 ‘TUoS Report’ to the NETSO. The TUoS Report contains details about Supplier BM Units’ net and gross metered volumes (taking account of Imports to SVA Non-Final Demand Facilities), which the NETSO uses in the calculation of TNUoS and BSUoS charges.

The SVAA generates the TUoS Report in accordance with the Settlement Timetable so that it includes calculated and recalculated metered volumes for each Settlement Day for each Volume Allocation Run.

In addition to overall net and gross metered volumes, the SVAA is responsible for receiving Imports to and Exports from declared SVA Non- Final Demand Facilities and reporting aggregated Import metered volumes to NETSO in the TUoS Report. To do this, the SVAA must validate (and keep under review) declarations made by Suppliers (on behalf of their customers, SVA Non- Final Demand Facility Operators) and maintain a record of these SVA Non- Final Demand Facilities. Also, the SVAA must obtainmetered data for specific SVA Non- Final Demand Facilities, aggregate and report this metered data to the NETSO, and support BSCCo in its periodic review of declared facilities, the volumes reported and the operation of the processes.

This BSCP sets out the processes followed by the SVAA, SVA Non- Final Demand Facility Operators, Suppliers, VLPs, AMVLPs, VTPs, HHDAs (where appropriate) and BSCCo to support the calculation of Network Charges.

Appendix 3.7.3 sets out the template with the information that SVA Non- Final Demand Facility Operators must complete, which Suppliers send to the SVAA, when declaring an SVA Non- Final Demand Facility.

Appendix 3.7.4 sets out the template with the information that SVA Non- Final Demand Facility Operators must use if they wish to stop being an SVA Non- Final Demand Facility Operator.

#### 1.1.3 Baselined BM Units

Suppliers, VLPs, and AMVLPs can opt for their Additional and Secondary BM Units to be Baselined BM Units and VTPs must set their Trading Secondary BM Units as Baselined BM Units. Registration of a Baselined BM Unit is covered in BSCP15.

Note that the Lead Party for a Baselined BM Unit other than VTPs must still submit an FPN to the NETSO, but the Final Physical Notification (FPN) is not used to calculate Non-Delivery Charges. Instead Settlement systems calculate their own FPN equivalent known as the “Settlement Expected Volume”. The Lead Party specifies (when they allocate each MSID Pair or AMSID Pair to the Baselined BM Unit) how this will work:

Baselined MSID Pairs (or AMSID Pairs): The SVAA will use historic metered data to forecast the baseline consumption for the MSID Pair in accordance with the Baselining Methodology

Submitted MSID Pairs (or AMSID Pairs): The Lead Party works out the FPN-equivalent, and submits a total figure (per BM Unit and Settlement Period) for all the non-Baselined MSID Pairs.

Inactive MSID Pairs (or AMSID Pairs): excluded from the BM Unit (for Settlement purposes). Secondary BM Units only.

#### 1.1.4 Submitted Expected Volumes

A BM Unit may contain a mix of MSID Pairs which are not suitable for having their expected usage calculated via a baselining methodology, for example where the site is highly variable, or the historical data required for baselining is not yet available. The Party can therefore select which sites they want expected volumes to be calculated via a baselining methodology.

Submitted Expected Volumes are registered by a Lead Party (i.e. VLP, AMVLP, VTP or Supplier) for MSID Pairs in a Baselined BM Unit not using the Baselining Methodology. The Lead Party will register Submitted Expected Volumes as a single value per BM Unit for all non-Baselined MSID Pairs (section 2.13).

The Submitted Expected Volumes and calculated Baselined Expected Volumes are added together to create a Settlement Expected Volume for the BMU. The Settlement Expected Volumes will replace the current FPN received from the NETSO in the Settlement of the Balancing Service.

#### 1.1.5 Event Days

If an MSID Pair is selected by the Lead Party to have its expected volumes derived from a Baselining Methodology it will be calculated based on normal usage. The Baselining Methodology needs to discount days where the site is doing something abnormal (e.g. providing a balancing service). This will be known as an Event Day and will be removed from the Baselining Methodology calculation (section 2.14). The SVAA can cancel an Event Day at any time if it was created in error.

#### 1.1.6 EMR Declarations

BEIS and Ofgem’s joint Smart Systems and Flexibility Plan (2017) specifies that the Final Consumption Levy charges calculated by EMRCo should exclude electricity imported for the purposes of Licensed Generation (including Battery Storage). In order to receive FCL charges based on “Chargeable Demand”, rather than “Gross Demand”, Suppliers and Registrants of CVA BM Units (other than Interconnector BM Units) are required to declare the necessary information to SVAA or CRA as appropriate.

There are three types of EMR Declaration:

EMR MSID Declaration: where Generation and / or Battery Storage – but no Final Demand - is supplied via a SVA Import Metering System5, the Supplier for that Metering System should specify the SVA Boundary Point Import MSID.

The total half hourly Metered for the SVA Boundary Point Import MSID will be non-chargeable for the purposes of calculating FCL charges, and will be deducted from the SVA BM Unit Demand sent to SAA.

EMR AMSID Declaration: where Generation and / or Battery Storage is co-located with Final Demand is supplied by one or more Import SVA Boundary Point Metering Systems which have the same Supplier, the Import Supplier should specify the relevant SVA Boundary Point MSID Pair(s) and AMSID Pair(s) that relate to the Licensed Generation and / or Battery Storage facilities. Each Generation and Battery Storage facility must be registered as an Asset in accordance with Sections 2.9 – 2.11 of this BSCP to obtain the AMSID Pair.

The proportion of the half hourly Metered Volume for the SVA Boundary Point Import MSID(s) which will be non-chargeable for the purposes of calculating FCL charges will be calculated according to a formula set out in the BSC Configurable Item ‘On-Site Energy Allocation Methodology’, and will be deducted from the SVA BM Unit Demand sent to SAA.

EMR CVA BM Unit Declaration: where Generation and / or Battery Storage is located behind one or more CVA Boundary Point Metering Systems included in a single CVA BM Unit (Type T or E only), the registrant of that BM Unit should specify that CVA BM Unit.

For each Settlement Period where a CVA BM Unit is net importing, the SAA will set the chargeable Demand for that CVA BM Unit to be 0 MWh for the purposes of calculating FCL charges.

#### 1.1.7 Wholesale Market Activity Notifications6

A VTP must notify the ECVAA of a Settlement Period in which it will trade in the Wholesale Market, and the Trading Secondary BM Unit used, by submitting a Wholesale Market Activity Notification (WMAN) to the ECVAA prior to Gate Closure for the relevant Settlement Period. The ECVAA will collate all WMANs received for a calendar day and will notify the SVAA in the Daily WMAN Report.

### 1.2 Main Users of the Procedure

This BSC Procedure should be used by:

Suppliers

VLPs

AMVLPs

VTPs

The NETSO

SVAA

SVA Non-Final Demand Facility Operators

The systems and processes used by Suppliers, VLPs, VTPs, AMVLPs, the NETSO, the SVAA and SVA Non-Final Demand Facility Operators must comply with all other applicable requirements set out in the Code, PSL100, CoP11, BSCP537 and BSCP603.

### 1.3 Use of Procedure

The remaining sections in this document are:

Section 2 – Interface and Timetable Information: this section defines the step by step processes for the SVA Metering System & Asset Metering System Register.

Section 3 – Appendices: this section contains supporting information.

### 1.4 Balancing and Settlement Code Provisions

This BSC Procedure has been produced in accordance with the provisions of the Balancing and Settlement Code (BSC). In the event of an inconsistency between the provisions of this BSC Procedure and the BSC, the provisions of the BSC shall prevail.

### 1.5 Associated BSC Procedures

This BSC Procedure interfaces with:

| BSC Procedure | Title |
|---|---|
| BSCP15 | BM Unit Registration |
| BSCP503 | Half Hourly Data Aggregation for SVA Metering Systems Registered in SMRS |
| BSCP507 | Supplier Volume Allocation Standing Data Changes |
| BSCP508 | Supplier Volume Allocation Agent |
| BSCP537 | Qualification Process for SVA Parties, SVA Party Agents VLPs, AMVLPs, AMVLP Agents and CVA MOAs |
| BSCP603 | Meter Operations and Data Collection for Asset Metering Systems |
| BSCP607 | Lead Party Asset Meter Register and Secondary BM Unit Asset Volumes |
| BSCP703 | BSC Central Services for MHHS Metering Systems |
| BSCP707 | Changes to Industry Standing Data |

### 1.6 Acronyms and Definitions

Any capitalised term that is not defined in this BSCP shall have the same meaning given to it as in the Code.

The acronyms used in this BSC Procedure are defined as follows:

| Acronym | Expression |
|---|---|
| ADS | Advanced Data Service |
| AMHHDC | Asset Metering Half Hourly Data Collector |
| AMMOA | Asset Metering Meter Operator Agent |
| AMSID | Asset Metering System Identifier |
| AMVLP | Asset Metering Virtual Lead Party |
| BM | Balancing Mechanism |
| BSC | Balancing and Settlement Code (the “Code”) |
| BSCCo | Balancing and Settlement Code Company |
| BSCP | Balancing and Settlement Code Procedure |
| BSP | Balancing Service Provider |
| BSUoS | Balancing Services Use of System |
| CRA | Central Registration Agent |
| ECVAA | Energy Contract Volume Aggregation Agent |
| EES | Electricity Enquiry Service |
| EFSD | Effective From Settlement Date |
| EMR | Electricity Market Reform |
| ETSD | Effective To Settlement Date |
| FCL | Final Consumption Levy |
| HHDA | Half Hourly Data Aggregator |
| HHDC | Half Hourly Data Collector |
| kWh | Kilowatt-hour |
| MOA | Meter Operator Agent |
| MHHS | Market-wide Half Hourly Settlement |
| MSID | Metering System Identifier |
| Ref | Reference |
| SDS | Smart Data Service |
| SVA | Supplier Volume Allocation |
| SVAA | Supplier Volume Allocation Agent |
| TNUoS | Transmission Network Use of System |
| TUoS | Transmission Use of System |
| VAR | Volume Allocation Run |
| VLP | Virtual Lead Party |
| VTP | Virtual Trading Party |
| WD | Working Day |

## 2. Interface and Timetable Information

### 2.1 MSID Pair Allocation Notification

Where a VLP or AMVLP has registered a Secondary BM Unit, a VTP has registered a Trading Secondary BM Unit, or a Supplier intends to use an Additional Primary BM Unit, for the purposes of providing Balancing Services7, the BM Unit must be specified in terms of the component MSID Pairs. Where the NETSO has contracts with non BM Applicable Balancing Services Providers, it must specify the MSID Pairs that may be used to provide those non BM Applicable Balancing Services.

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.1.1 | At least 5 WD before the EFSD of the MSID Pair | Send the MSID Pair Allocation | Lead Party,<br>NETSO | SVAA | P0278 – MSID Pair Allocation | Self-Service Gateway or other method, as agreed. |
| 2.1.2 | As required upon receiving additional information | Send an amended MSID Pair Allocation8 | Lead Party,<br>NETSO | SVAA | P0278 – MSID Pair Allocation<br>Appendix 3.2 – Amendments to MSID Pair Allocations | Self-Service Gateway, as agreed. |
| 2.1.3 | Within 1 WD of 2.1.1 | or where appropriate within 1 WD of 2.1.2<br>If the MSID Pair Allocation was not submitted via the Self-Service Gateway, log MSID Pair in the SVA Metering System and Asset Metering System Register. | SVAA |  |  | Internal Process |
| 2.1.4 | Immediately following 2.1.1, 2.1.2 or 2.1.3 | Validate MSID Pair Allocation in accordance with Appendix 3.1 – Validation of MSID Pair Allocation and AMSID Pair Allocation files | SVAA |  | Appendix 3.1 – MSID Pair Allocation File Validation |  |
| 2.1.5 | Immediately following2.1.4 | If MSID Pair Allocation is invalid, the SVAA shall send notification of the rejection to the Lead Party or the NETSO | SVAA |  | Lead Party, NETSO<br>P0280 – Rejection of MSID Pair Allocation | Self-Service Gateway or other method, as agreed. |
| 2.1.6 | After 2.1.5 | Return to 2.1.2 if Lead Party or the NETSO wishes to provide revised notification.<br>Lead Party NETSO |  |  |  |  |
| 2.1.7 | Immediately following 2.1.4 | or where appropriate within 1 WD of 2.1.2<br>If MSID Pair Allocation is valid, log the MSID Pair in the SVA Metering System & Asset Metering System Register. | SVAA |  |  |  |
| 2.1.8 | Immediately following 2.1.7 | Send confirmation of MSID Pair Allocation. | SVAA | Lead Party, NETSO | P0279 – Confirmation of MSID Pair Allocation | Self-Service Gateway or other method, as agreed. |
| 2.1.9 | Immediately following 2.1.7 | Where an MSID Pair is allocated to a Lead Party and to the NETSO at the same time the SVAA shall notify the NETSO of the dual allocation immediately.<br>Note that this is allowed, and so the Lead Party will not lose the MSID Pair. | SVAA | NETSO | Import MSID and related Secondary BM Unit Id. | Email or other method, as agreed. |
| 2.1.10 | *[cell boundaries not recoverable - row content in order:]* If the MSID Pair was already allocated to a different Lead Party, the SVAA shall transfer the MSID Pair allocation from that Lead Party (the ‘Losing Lead Party’) to the new Lead Party (the ‘Gaining Lead Party’) in the SVA Metering System & Asset Metering System Register.<br>SVAA<br><br>Internal process |  |  |  |  |  |
| 2.1.11 | Within 1 WD of 2.1.10 | Upon allocation to the Gaining Lead Party the SVAA shall send a Loss of MSID Pair Allocation notification to the Losing Lead Party | SVAA | Losing Lead Party | P0281 – Loss of MSID Pair Allocation | Self-Service Gateway or other method, as agreed. |
| 2.1.12 | If the Losing Lead Party disagrees with the Loss of MSID Pair Allocation they may initiate the Disputed MSID Pair Allocation Process (go to Section 2.3.1). | Losing Lead Party |  |  |  |  |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 2.1A AMSID Pair Allocation to a Secondary BM Unit

An AMVLP may allocate AMSID Pairs to its Secondary BM Units for the purposes of providing Balancing Services. Where an AMVLP has allocated MSID Pair(s) to a Secondary BM Unit in accordance with Section 2.1, and has registered an Asset and related Asset Metering System(s) in accordance with Sections 2.4-2.6 and has received an AMSID Pair in respect of such registration, the AMVLP may allocate that AMSID Pair to that Secondary BM Unit9.

The AMVLP must specify whether it intends to use the AMSID Pair for the purposes of Asset Metering or Asset Differencing (as defined in Section 3.9), and must specify the Associated MSID Pair(s) and set the MSID Pair Indicator and AMSID Pair Asset Differencing Indicator in a valid combination (as set out in 3.10).

A second AMVLP may use the same AMSID Pair in a different Secondary BM Unit at the same time, without the registrant AMVLP losing the AMSID Pair Allocation, provided that the AMSID Pair is used for different purposes in the two Secondary BM Units. If the second AMVLP wishes to use the AMSID Pair for the same purpose as the first AMVLP, this would result in a Loss of AMSID Pair Allocation for the Registrant AMVLP.

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.1A.1 | At least 1 WD before the AMSID Pair will be used in the Secondary BM Unit | Submit an AMSID Pair Allocation | AMVLP | SVAA | P0306 – AMSID Pair Allocation to a Secondary BM Unit | Self-Service Gateway or other method, as agreed. |
| 2.1A.2 | As required | Submit an amended AMSID Pair Allocation10 | AMVLP | SVAA | P0306 - AMSID Pair Allocation to a Secondary BM Unit<br>Appendix 3.2 – Amendments to a MSID Pair Allocation or an AMSID Pair Allocation | Self-Service Gateway, or other method, as agreed. |
| 2.1A.3 | Within 1 WD of 2.1A.1 or 2.1A.2 | If the AMSID Pair Allocation was not submitted via the Self-Service Gateway, log AMSID Pair Allocation in the SVA Metering System and Asset Meter Register. | SVAA |  |  | Internal Process |
| 2.1A.4 | Immediately following 2.1A.1, 2.1A2 or 2.1A.3 | Validate AMSID Pair Allocation. | SVAA |  | Appendix 3.1 – Validation of MSID Pair Allocation or AMSID Pair Allocation File<br>Appendix 3.10 - Valid combinations of ‘MSID Pair Indicator’ and ‘AMSID Pair Differencing Indicator’ in a Secondary BM Unit.<br>Appendix 3.12 Effect of Proposed AMSID Pair use in AMSID Pair Allocations. | Internal Process |
| 2.1A.5 | Immediately following 2.1A.4 | If the AMSID Pair Allocation fails validation, reject the AMSID Pair Allocation. | SVAA | AMVLP | P0308 – Rejection of AMSID Pair Allocation to a Secondary BM Unit | Self-Service Gateway |
| 2.1A.6 | Immediately following 2.1A.5, or as required | Return to 2.1A.2 if AMVLP wishes to provide a revised AMSID Pair Allocation. |  |  |  |  |
| 2.1A.7 | After 2.1A.4 | If the AMSID Pair Allocation is valid, and the AMSID Pair is not already allocated to another Secondary BM Unit, allocate the AMSID Pair to the Secondary BM Unit and notify the AMVLP | SVAA | AMVLP | P0307– Confirmation of AMSID Pair Allocation to a Secondary BM Unit | Self-Service Gateway |
| 2.1A.8 | After 2.1A.4 | If the AMSID Pair Allocation is valid, but the AMSID Pair is already allocated to another Secondary BM Unit for the same purpose:<br>de-allocate the AMSID Pair from its current Secondary BM Unit; and<br>allocate the AMSID Pair to new Secondary BM Unit | SVAA |  |  | Internal Process |
| 2.1A.9 | After 2.1A.8 | Notify ‘Gaining’ AMVLP of successful AMSID Pair Allocation | SVAA | AMVLP | P0307– Confirmation of AMSID Pair Allocation to a Secondary BM Unit | Self-Service Gateway |
| 2.1A.10 | After 2.1A.8 | Notify ‘Losing’ AMVLP’ of the loss of the AMSID Pair from its Secondary BM Unit | SVAA | AMVLP | P0320 – Loss of AMSID Pair Allocation Notification | Self-Service Gateway |
| 2.1A.11 | After 2.1A.10 | AMVLPs agree the effective from date for the transfer of responsibility for the Asset Metering System to the Gaining AMVLP. | Losing AMVLP |  | Gaining<br>AMVLP | Telephone, email or other method, as agreed. |
| 2.1A.12 | After 2.1A.11 and at least 5WD before Effective From Date | Notify SVAA of the new Registrant AMVLP for the Asset Metering System. | Gaining AMVLP | SVAA | P0297 Asset Registration<br>with the “Action Indicator” set to ‘Change of Registrant’ | Self-Service Gateway, or other method, as agreed. |
| 2.1A.13 | After 2.1A.12 | If the P0297 is invalid, reject the file and notify the AMVLP | SVAA | Gaining AMVLP | P0298 – Rejection of Asset Registration | Internal process |
| 2.1A.14 | After 2.1A.13 | If the P0297 is valid, amend the AMVLP Id of the AMVLP responsible for the Asset in the Register.<br>NB As this is not a new Asset Registration, SVAA shall keep the existing AMSID Pair relating to the Asset. | SVAA |  |  |  |
| 2.1A.15 | After 2.1A.14 | Notify the new AMVLP of the Successful change of Registrant AMVLP for the Asset. | SVAA | Gaining AMVLP | P0299 Confirmation of Asset Registration. | Self-Service Gateway |
| 2.1A.16 | After 2.1A.15 | Where the new AMVLP decides to replace one or both Asset Metering Agent, go to 2.10.1 to Register the new Asset Metering Agent(s) |  |  |  |  |
| 2.1A.17 | *[cell boundaries not recoverable - row content in order:]* After 2.1A.4<br>If the AMSID Pair Allocation is valid, but the AMSID Pair is already allocated to another Secondary BM Unit for a different purpose:<br>allocate the AMSID Pair to new Secondary BM Unit11<br><br><br><br>Internal Process |  |  |  |  |  |
| 2.1A.18 | After 2.1A.17 | Notify AMVLP of the successful allocation of the AMSID Pair to its BM Unit. | SVAA | AMVLP | P0307– Confirmation of AMSID Pair Allocation to a Secondary BM Unit<br>Self-Service Gateway<br>Notify the AMVLP that already had the AMSID Pair Allocated to its BM Unit of this Allocation.<br>SVAA<br>AMVLP<br>P0309 - Notification of use of AMSID Pair by another AMVLP | Self-Service Gateway |
| 2.1A.19 | At any time after 2.1A.18 | If either AMVLP decides to stop using the AMSID Pair, notify the other AMVLP. | SVAA | AMVLP | P0309 - Notification of use of AMSID Pair by another AMVLP | Self-Service Gateway |
| 2.1A.20 | After 2.1A.19 | If the AMVLP that has decided to stop using the AMSID Pair was the ‘Registrant’ AMVLP, then the remaining AMVLP12 must either:<br>become the ‘Registrant’ of the related Asset; | or |  | de-allocate the AMSID Pair from its Secondary BM Unit and delete their registration of the related Asset.<br>P0297 - Asset Registration - populated with Action Indicator ‘C’<br>P0306 - AMSID Pair Allocation to a Secondary BM Unit - populated with a non-null ‘AMSID Pair in Secondary BM Unit ETD’<br>P0297 - Asset Registration - populated with Action Indicator ‘D’ |  |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

2.2A MSID Pair Delivered Volume Notification by Virtual Lead Parties and Virtual Trading Parties and MSID Pair / AMSID Pair Delivered Volume Notification by Asset Metering Virtual Lead Parties

For each Settlement Day where a VLP or AMVLP has provided Balancing Services13 using a Secondary BM Unit, or a VTP has carried out Wholesale Market Activities using a Trading Secondary BM Unit, the VLP or VTP must notify to the SVAA the MSID Pair Delivered Volume, for each MSID Pair allocated to that Secondary BM Unit, for each Settlement Period within that Settlement Day.

For each Settlement Day where an AMVLP has provided Balancing Services using a Secondary BM Unit including AMSID Pairs for the purposes of Asset Metering, the AMVLP must notify to the SVAA the AMSID Pair Delivered Volume for each AMSID Pair, adjusted for losses between the Asset Metering System and the Boundary Point Metering System, for each Settlement Period within that Settlement Day. Where an AMVLP has provided Balancing Services using a Secondary BM Unit including AMSID Pairs for the purposes of Asset Differencing, or does not use AMSID Pairs, the AMVLP should only send MSID Pair Delivered Volume data.

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.2A.1 | Within 1 WD of the provision of a Balancing Service | Submit the MSID Pair Delivered Volume for each MSID Pair used to delivered a Balancing Service<br>Submit the AMSID Pair Delivered Volume for each AMSID Pair used to deliver a Balancing Service via Asset Metering. | Or<br>Submit the MSID Pair Delivered Volume for each AMSID Pair used to deliver a Balancing Service via Asset Differencing or where no AMSID Pair used. |  | VLP, AMVLP or VTP<br>AMVLP<br>SVAA<br>SVAA<br>P0282 – Delivered Volume Notification14 | Electronic or other method, as agreed. |
| 2.2A.2 | As required15 | Re-submit MSID Pair Delivered Volume or AMSID Pair Delivered Volume<br>VLP or VTP | AMVLP | SVAA<br>SVAA | P0282 –Delivered Volume Notification | Electronic or other method, as agreed. |
| 2.2A.3 | Within 1 WD of 2.2A.1 | or where appropriate within 1 WD of 2.2A.2<br>Log and validate MSID Pair Delivered Volume or AMSID Pair Delivered Volume. | SVAA |  | Appendix 3.4 Delivered Volume File Validation<br>Internal process. |  |
| 2.2A.4 | Within 1 WD of 2.2A.1 | or where appropriate within 1 WD of 2.2A.2<br>If the file cannot be processed send notification. | SVAA |  | VLP VTP<br>or<br>AMVLP<br>Negative Acknowledgement<br>Electronic or other method, as agreed.<br>Return to 2.2A.2 if VLP wishes to provide revised MSID Pair Delivered Volume or AMVLP wishes to provide revised MSID Pair Delivered Volume or AMSID Pair Delivered Volume. |  |
| 2.2A.5 | Within 1 WD of 2.2A.1 | or where appropriate within 1 WD of 2.2A.2<br>If MSID Pair Delivered Volume fails validation send rejection.<br>If AMSID Pair Delivered Volume fails validation send rejection. | SVAA |  | VLP VTP or AMVLP<br>AMVLP<br>P0283 – Rejection of Delivered Volume11<br>Electronic or other method, as agreed.<br>Return to 2.2A.2 if VLP, VTP or AMVLP wishes to provide revised MSID Pair Delivered Volume or AMSID Pair Delivered Volume. |  |
| 2.2A.6 | Within 1 WD of 2.2A.1 | or where appropriate within 1 WD of 2.2A.2<br>If MSID Pair Delivered Volume passes validation send confirmation.<br>If AMSID Pair Delivered Volume passes validation send confirmation | SVAA | SVAA | VLP, VTP or AMVLP<br>AMVLP<br>P0284 – Confirmation of Delivered Volume11 | Electronic or other method, as agreed. |
| 2.2A.7 | As late as possible to meet the relevant VAR for the SD (to ensure most recent data from VLP or AMVLP) to meet the SVAA Calendar. | Perform checks in accordance with Appendix 3.6 | SVAA |  | Appendix 3.6 – MSID Pair / AMSID Pair Delivered Volume Allocation | Internal process |
| 2.2A.8 | Immediately following 2.2A.7 | If appropriate, send Delivered Volume Exception Report. | SVAA | VLP, VTP or AMVLP | P0285 –Delivered Volume Exception Report8 | Electronic or other method, as agreed. |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 2.2B MSID Pair Delivered Volume Notification by the NETSO

For each Settlement Day, the NETSO shall notify to the SVAA the MSID Pair Delivered Volume for each MSID Pair that has been used to provide non BM Applicable Balancing Services for each Settlement Period within that Settlement Day.

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.2B.1 | Within 45 WD of the provision of a non BM Applicable Balancing Service to the NETSO | Submit the ABS MSID Pair Delivered Volume for each MSID Pair used to deliver the Balancing Service | NETSO | SVAA | P0292 – ABS MSID Pair Delivered Volume Notification | Electronic or other method, as agreed. |
| 2.2B.2 | As required16 | Re-submit ABS MSID Pair Delivered Volume | NETSO | SVAA | P0292 – ABS MSID Pair Delivered Volume Notification | Electronic or other method, as agreed. |
| 2.2B.3 | Within 1 WD of 2.2B.1 | or where appropriate within 1 WD of 2.2B.2<br>Log and validate ABS MSID Pair Delivered Volume | SVAA |  | Appendix 3.5 – ABS MSID Pair Delivered Volume File Validation | Electronic or other method, as agreed. |
| 2.2B.4 | Within 1 WD of 2.2B.1 | or where appropriate within 1 WD of 2.2B.2<br>If the file cannot be processed send notification. | SVAA | NETSO<br>Negative Acknowledgement | Electronic or other method, as agreed.<br>Return to 2.2B.1 if the NETSO wishes to provide revised ABS MSID Pair Delivered Volume |  |
| 2.2B.5 | Within 1 WD of 2.2B.1 | or where appropriate within 1 WD of 2.2B.2<br>If ABS MSID Pair Delivered Volume fails validation send rejection. | SVAA | NETSO | P0293 – Rejection of ABS MSID Pair Delivered Volume<br>Electronic or other method, as agreed.<br>Return to 2.2B.1 if the NETSO wishes to provide revised MSID Pair Delivered Volume |  |
| 2.2B.6 | Within 1 WD of 2.2B.1 | or where appropriate within 1 WD of 2.2.2<br>If ABS MSID Pair Delivered Volume passes validation send confirmation. | SVAA | NETSO | P0294 – Confirmation of ABS MSID Pair Delivered Volume | Electronic or other method, as agreed. |
| 2.2B.7 | As late as possible to meet the relevant VAR for the SD (to ensure most recent data from the NETSO) to meet the SVAA Calendar. | Perform calculations in accordance with Appendix 3.6 and, where it has not been possible to allocate an ABS MSID Pair Delivered Volume to the MSIDs in that MSID Pair, send an exception report to the NETSO | SVAA | NETSO | Appendix 3.6 – ABS MSID Pair Delivered Volume Allocation<br>P0295 – ABS MSID Pair Delivered Volume Exception Report | Electronic or other method, as agreed. |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 2.3 Disputed MSID Pair Allocation or Disputed AMSID Pair Allocation Resolution

Where a Lead Party has received a Loss of MSID Pair Allocation notification, or an AMVLP has received a Loss of AMSID Pair Allocation notification and, after discussion with the customer, they believe it to be an erroneous reallocation, they may initiate the Disputed MSID Pair Allocation or Disputed AMSID Pair Allocation Procedure.

Note the Disputed MSID Pair Allocation or Disputed AMSID Pair Allocation process is anonymised and so the ‘From’ and ‘To’ columns are indicative only.

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.3.1 | Within 5 WD of receipt of a Loss of MSID Pair / AMSID Pair Allocation notification in 2.1.8 | Initiate the Disputed MSID Pair Allocation or Disputed AMSID Pair Allocation Resolution Process in accordance with Section 3.3 of this document.<br>Losing Lead Party / AMVLP | Losing AMVLP |  | Gaining Lead Party / AMVLP<br>Gaining AMVLP<br>P0286 – Disputed MSID Pair Allocation<br>or<br>P0312 Disputed AMSID Pair Allocation | Self-Service Gateway or other method, as agreed. |
| 2.3.2 | Within 5 WD of 2.3.1 | Respond to Disputed MSID Pair Allocation or Disputed AMSID Pair Allocation notification | Gaining Lead Party | Gaining AMVLP<br>Losing Lead Party<br>Losing AMVLP | P0286 – Disputed MSID Pair Allocation<br>or<br>P0312 Disputed AMSID Pair Allocation | Self-Service Gateway or other method, as agreed. |
| 2.3.3 | Once the initial request has been made one of the following options shall be taken | The Gaining Lead Party / AMVLP agrees that the MSID Pair / AMSID Pair is to be allocated to the Losing Lead Party / AMVLP; | or<br>After appropriate investigation e.g. checking a valid contract is in place, the Gaining Lead Party / AMVLP disagrees with the Losing Lead Party / Losing AMVLP |  |  | Internal Process |
| 2.3.4 | Same day as 2.3.3 | If both parties agree to the resolution of the Disputed MSID Pair Allocation or Disputed AMSID Pair Allocation go to 2.3.6 |  |  |  |  |
| 2.3.5 | Following 2.3.3 | If the Gaining Lead Party does not agree with the resolution in 2.3.3 and the Losing Lead Party wishes to re-raise the dispute, go to 2.3.1.<br>See Appendix 3.3.6 for guidance. |  |  |  |  |
| 2.3.6 | Within 1 WD of 2.3.4 | Send a revised MSID Pair Allocation with agreed EFSD and ETSD | or<br>Send a revised AMSID Pair Allocation with agreed EFSD and ETSD | Gaining Lead Party<br>Gaining AMVLP<br>SVAA<br>SVAA | P0278 – MSID Pair Allocation<br>or<br>P0306 AMSID Pair Allocation | Self-Service Gateway or other method, as agreed. |
| 2.3.7 | Within 1 WD of 2.3.4 | Send new MSID Pair Allocation with agreed EFSD and ETSD | or<br>Send new AMSID Pair Allocation with agreed EFSD and ETSD | Losing Lead Party<br>Losing AMVLP<br>SVAA<br>SVAA | P0278 – MSID Pair Allocation<br>or<br>P0306 AMSID Pair Allocation | Self-Service Gateway or other method, as agreed. |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

2.4 SVA Non- Final Demand Facilities – initial declaration of an SVA Non- Final Demand Facility17 (and, where necessary, an SVA Non- Final Demand Facility Operator18)

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.4.1 | *[cell boundaries not recoverable - row content in order:]* As soon as an SVA Non- Final Demand Facility Operator identifies that it would like to declare a facility<br>Complete and send a Non- Final Demand Declaration Document<br><br>Declaration Documents must be signed by an SVA Non- Final Demand Facility Operator’s director registered with Companies House.<br>SVA Facility Operator<br>Supplier(s)<br>Director-signed Non- Final Demand Declaration Document (Part B-D) – see Appendix 3.7.1.1 and Appendix 3.7.3.<br><br><br>Agreed between SVA Non- Final Demand Facility Operator and Supplier |  |  |  |  |  |
| 2.4.2 | Within 5WD of 2.4.1 | Send SVA Non- Final Demand Facility Operator’s Declaration Document to the SVAA<br>Supplier(s) | SVAA |  | Director-signed Non- Final Demand Declaration Document (Part A-D).<br>Self-service gateway, Email or other method agreed |  |
| 2.4.3 | Within 2WD of 2.4.2; |  | or |  | if the SVAA determines that a Declaration is one of a set19 then within 5WD of 2.4.2.<br>Check that each Non- Final Demand Declaration Document is complete and valid. The SVAA may liaise with the Supplier that submitted the declaration to seek additional information, corrections or a resubmission of the declaration.<br>The SVAA must register (or update) details of each SVA Non- Final Demand Facility declared to it, irrespective of whether successfully validated.<br>SVAA | Internal process |
| 2.4.4 | Within 1WD of 2.4.3 | Notify the Supplier of the outcome of 2.4.3. | SVAA | Supplier | The SVAA must inform the relevant Supplier(s) whether the Declaration for an SVA Non-Final Demand Facility identified in a Declaration Document was successfully validated or not.<br>Where the SVAA decides a Non-Final Demand Declaration is invalid or incomplete it must provide a short explanation to the Supplier(s). | Email or, where agreed, by other electronic means |
| 2.4.5 | Following receipt of 2.4.4 | Suppliers should send details of whether a Declaration(s) was successful or not for each declared SVA Non-Final Demand Facility sent per 2.4.2. | Supplier | SVA Non-Final Demand Facility Operator |  | Agreed between SVA Non-Final Demand Facility Operator and Supplier |
| 2.4.6 | Within 1WD of 2.4.3 | Where an SVA Non-Final Demand Facility is successfully declared, determine whether for each of the facility’s MSIDs to instruct HHDA to begin reporting Metered data to the SVAA20.<br>If instruction required, follow BSCP503 Section 3.7. | SVAA | HHDA | D0354 - Metering System Reporting Notification21 | Electronic, or other method, as agreed. |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 2.5 SVA Non-Final Demand Facilities – voluntary withdrawal of an SVA Non-Final Demand declaration22

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.5.1 | *[cell boundaries not recoverable - row content in order:]* As soon as an SVA Non Final Demand Facility Operator identifies that it must send notice that a declaration must end<br>Complete and send a Declaration Document to Supplier(s)<br><br>Declaration Documents must be signed by a Non Final Demand Facility Operator’s director registered with Companies House.<br>SVA Non Final Demand Facility Operator<br>Supplier(s)<br>Director-signed Declaration Document (Part B-D) – see Appendix 3.7.1.3 and Appendix 3.7.3.<br><br><br>Agreed between SVA Non Final Demand Facility Operator and Supplier |  |  |  |  |  |
| 2.5.2 | Within 5WD of 2.5.1 | Send SVA Non Final Demand Facility Operator’s Declaration Document to the SVAA<br>Supplier(s) | SVAA |  | Director-signed Declaration Document (Part A-D).<br>Self Service Gateway or Email. |  |
| 2.5.3 | Within 2WD of 2.5.2. | Check that each director-signed Declaration Document is complete and valid. The SVAA may liaise with the Supplier that submitted the Declaration Document to seek additional information, corrections or a resubmission of the declaration.<br>The SVAA must update the details of each SVA Non-Final Demand Facility identified to it to cease being a valid declared facility. | SVAA |  |  | Internal process |
| 2.5.4 | Within 1WD of 2.5.3 | Notify the Supplier(s) of the outcome of 2.5.3. | SVAA |  | Supplier(s)<br>Where the Declaration Document is successfully validated, the SVAA must inform the Supplier(s) that it has updated the registration details for the SVA Non-Final Demand Facility.<br>Otherwise, where a Declaration Document fails validation, the SVAA must provide a short explanation to the Supplier. | Electronic, or other method, as agreed. |
| 2.5.5 | Following receipt of 2.5.4 | Notify the SVA Non-Final Demand Facility Operator of the outcome of 2.5.3 and whether the SVAA has updated its records | Supplier(s) | SVA Storage Non-Final Facility Operator | Confirmation (or otherwise) that SVA Non-Final Demand Facility’s Declaration has been updated as having/expected to cease/d. | Agreed between SVA Non Final Demand Facility Operator and Supplier |
| 2.5.6 | Within 1WD of 2.5.3 | Where a Declaration for an SVA Non-Final Demand Facility has ended or is due to end, determine whether, for each of the facility’s MSIDs, to instruct HHDA to cease reporting Metered data to the SVAA23.<br>If instruction required, follow BSCP503 Section 3.8. | SVAA | HHDA24 | D0354– Metering System Reporting Notification24 | Electronic, or other method, as agreed. |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 2.6 SVA Non-Final Demand Facilities – enforced withdrawal of an SVA Non-Final Demand Facility’s declaration25

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.6.1 | Where the SVAA identifies a need to end a declaration or is instructed by the BSC Panel (via BSCCo) to end a declaration. | Update the details of each SVA Non-Final Demand Facility identified by or to it26 to cease being a valid declared facility. | SVAA |  |  | Internal SVAA process |
| 2.6.2 | Within 1WD of 2.6.1 | Notify the Supplier(s) of the action taken. | SVAA | Supplier(s) | The SVAA must provide a short explanation to the Supplier(s). | Electronic, or other method, as agreed. |
| 2.6.3 | Following receipt of 2.6.2 | Notify the SVA Non-Final Demand Facility Operator of the outcome of 2.6.2 | Supplier | SVA Non-Final Demand Facility Operator |  | Agreed between SVA Non-Final Demand Facility Operator and Supplier |
| 2.6.4 | Within 1WD of 2.6.1 | Where a Declaration for an SVA Non-Final Demand Facility has ended or is due to end, determine whether, for each of the facility’s MSIDs, to instruct HHDA28 to cease reporting Metered data to the SVAA27.<br>If instruction required, follow BSCP503 3.8. | SVAA | HHDA | D0354 – Metering System Reporting Notification28 | Electronic, or other method, as agreed. |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 2.7 SVA Non- Final Demand Facilities – withdrawal of an SVA Non- Final Demand Operator29

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.7.1 | As soon as an SVA Non- Final Demand Facility Operator identifies that it must or would like to cease to be an SVA Non- Final Demand Operator | Send a SVA Non- Final Demand Operator Withdrawal letter to the SVAA<br>SVA Non- Final Demand Facility Operator | SVAA |  | Director-signed Operator Withdrawal letter – see Appendix 3.7.1.5 and Appendix 3.7.4.<br>Agreed between SVA Non-Final Demand Facility Operator and Supplier. |  |
| 2.7.2 | Within 2WD of 2.7.1 | Check that each SVA Non-Final Demand Operator Withdrawal letter is complete and valid. | SVAA |  |  | Internal process |
| 2.7.3 | Where SVA Non-Final Demand Facility Operator Withdrawal Letter successfully validated per 2.7.2 |  | Or |  | Where Panel instructs the SVAA<br>Or<br>Where BSCCo confirms that an SVA Non-Final Demand Facility Operator is no longer<br>Update the details of the SVA Non-Final Demand Facility Operator and end-date each related SVA Non-Final Demand Facility related to the SVA Non-Final Demand Facility Operator.<br>SVAA | Internal process |
| 2.7.4 | Within 1WD of 2.7.2 | Where the SVA Non-Final Demand Facility Operator Withdrawal is successfully validated, notify the SVA Non-Final Demand Facility Operator and all related Suppliers of the outcome of 2.7.2, and follows the steps in 2.6 to ensure all related SVA Non-Final Facilities are end-dated.<br>Where the SVA Non-Final Demand Facility Operator Withdrawal letter fails validation, notify the SVA Non-Final Demand Facility Operator of the outcome of 2.7.2 | SVAA |  | SVA Non-Final Facility Operator, Supplier(s)<br>Where the SVA Non-Final Demand Facility Operator Withdrawal Letter is successfully validated, the SVAA must inform the SVA Non-Final Demand Facility Operator and the Supplier(s) that it has updated the registration details for the SVA Non-Final Demand Facility Operator and SVA Non-Final Demand Facility(ies).<br>Otherwise, where a Withdrawal Letter fails validation, the SVAA must provide a short explanation to the SVA Non-Final Demand Facility Operator only. | Email or, where agreed, by other electronic means |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

2.8 SVA Non-Final Demand Facilities – update following Change of Supplier or change of the Metering Systems registered for the Non-Final Demand Facility30

A Change of Supplier (CoS) or Change of Metering System (CoM) event would invalidate the SVA Non-Final Demand declaration without an update. Furthermore, a CoS or CoM requires the SVA Non-Final Demand Facility Operator to resubmit a Declaration Document for each Supplier and all Metering Systems related to the SVA Non-Final Demand Facility.

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.8.1 | As soon as an SVA Non-Final Demand Facility Operator identifies that it must update an existing declaration | Complete and send a Declaration Document to its Supplier(s) | SVA Non-Final Demand Facility Operator |  | Supplier(s)<br>Director-signed Declaration Document (Part B-D) – see Appendix 3.7.1.2 and Appendix 3.7.3.<br>Agreed between SVA Non-Final Demand Facility Operator and Supplier |  |
| 2.8.2 | Within 5WD of 2.8.1 | Send SVA Non-Final Demand Facility Operator’s director-signed Declaration Document to the SVAA<br>Supplier(s) | SVAA |  | Director-signed Declaration Document (Part A-D).<br>Self Service Gateway or Email |  |
| 2.8.3 | Within 2WD of 2.8.2; | or<br>if the SVAA determines that a Declaration is one of a set31 then within 5WD of 2.8.2.<br>Check that each director-signed Declaration Document is complete and valid. The SVAA may liaise with the Supplier that submitted the declaration to seek additional information, corrections or a resubmission of the declaration.<br>Where successfully validated, the SVAA must update the details of each SVA Non-Final Demand Facility. | SVAA |  |  | Internal process |
| 2.8.4 | Within 1WD of 2.8.3 | Notify the Supplier of the outcome of 2.8.3. | SVAA | Supplier | Where the Declaration Document is successfully validated, the SVAA must inform the Supplier(s) that it has updated the registration details for the SVA Non-Final Demand Facility.<br>Otherwise, where a Declaration Letter fails validation, the SVAA must provide a short explanation to the Supplier. | Electronic, or other method, as agreed. |
| 2.8.5 | Following receipt of 2.8.4 | Supplier(s) should notify the SVA Non-Final Demand Facility Operator of the outcome of 2.8.3 and so whether the SVAA has updated its records | Supplier | SVA Non-Final Demand Facility Operator | Confirmation (or otherwise) that SVA Non-Final Demand Facility’s Declaration has been updated as having/expected to cease/d. | Agreed between SVA Non-Final Facility Operator and Supplier |
| 2.8.6 | Within 1WD of 2.8.3 | Where a Declaration for an SVA Non-Final Demand Facility has ended or is due to end, determine whether, for each of the facility’s MSIDs, to instruct HHDA to cease reporting Metered data to the SVAA32.<br>If instruction required, follow BSCP503 3.8. | SVAA | HHDA35 | D0354 - Metering System Reporting Notification33 | Electronic, or other method, as agreed. |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 2.9 Asset Registration

An AMVLP or Supplier may register an Asset and related Asset Metering System(s), in order to receive an AMSID Pair34. An AMVLP shall only be allowed to allocate an AMSID Pair to a Secondary BM Unit in accordance with Section 2.1A of this BSCP and a Supplier shall only be allowed to include the AMSID Pair in an EMR AMSID Declaration in accordance with Section 2.15 of this BSCP.

The Self-Service Gateway facilitates a two-stage approval process: a Category A or F Authorised person may submit the registration information required by this Section 2.9 and Sections 2.10 and 2.11 themselves, or they may delegate the submission of the information to an Assistant who is not a Category A Authorised person. Where so delegated, a Category A or F Authorised person must approve the full set of submitted registration information – i.e. at the end of the Registration of Asset Meter Details set out in Section 2.11 – before the AMSID Pair can be used. The Category A or F Authorised person will be notified via email when an Asset registration is ready for their approval.

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.9.1 | At least 10 WD before inclusion in Secondary BM unit or EMR AMSID Declaration | Submit details of the Asset. | AMVLP<br>or<br>Supplier | SVAA | P0297 - Asset Registration | Self-Service Gateway or other method, as agreed. |
| 2.9.2 | Within 1 WD of 2.9.1 | If Self-Service Gateway was not the method used in 2.9.1, log the Asset details in the Register. | SVAA |  |  | Internal Process |
| 2.9.3 | Within 1 WD of 2.9.1 | Validate the Asset details. | SVAA |  | Appendix 3.1.1 | Internal Process |
| 2.9.4 | Immediately following 2.9.3 | If Asset details are invalid, send rejection notification with rejection reason. | SVAA | AMVLP<br>or<br>Supplier | P0298 - Rejection of Asset Registration | Self-Service Gateway |
| 2.9.5 | After 2.9.4 | Return to 2.9.1 if AMVLP or Supplier wishes to submit valid Asset details. | AMVLP<br>or<br>Supplier |  |  |  |
| 2.9.6 | Immediately following 2.9.3 | If Asset details are valid, create and store unique AMSID(s) as an AMSID Pair. | SVAA |  |  | Internal Process |
| 2.9.7 | Immediately following 2.9.6 | Send an acceptance notification, including the AMSID Pair details. | SVAA | AMVLP<br>or<br>Supplier | P0299 - Confirmation of Asset Registration | Self-Service Gateway |
| 2.9.8 | After 2.9.7 | Go to Section 2.10. | AMVLP<br>or<br>Supplier |  |  |  |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 2.10 Registration of Asset Metering Agents for Asset Metering System(s)

After the successful registration of an Asset, the AMVLP or Supplier must appoint Asset Metering Agents - a Qualified SVA MOA35 and Qualified HHDC and, where desired, an AMHHDC 36 - to the Asset Metering System(s) and register them in the SVA Metering System & Asset Metering System Register before the AMVLP or Supplier may use the related AMSID Pair. The Asset Metering Agent appointments should be carried out in accordance with BSCP603

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.10.1 | After 2.9.8 or 2.1A.15 | Appoint Asset Metering Agents for the Asset Metering System(s) and related AMSID Pair. | AMVLP<br>or<br>Supplier |  |  | Internal process |
| 2.10.2 | After 2.10.1 and at least 5 WD before inclusion in Secondary BM unit or EMR AMSID Declaration | Register the Asset Metering Agent details in the SVA Metering System & Asset Metering System Register | AMVLP<br>or<br>Supplier | SVAA | P0300 – Registration of Asset Metering Agents | Self-Service Gateway or other method, as agreed. |
| 2.10.3 | Within 1 WD of 2.10.2 | If Self-Service Gateway was not used in 2.10.2, log the Asset Metering Agent details in the Register | SVAA |  |  | Internal process |
| 2.10.4 | Immediately following 2.10.2 or 2.10.3 | Validate Asset Metering Agent details | SVAA |  | Appendix 3.1.2 | Internal process |
| 2.10.5 | Within 1 WD of 2.10.4 | If Asset Metering Agent details are invalid, send rejection notification with rejection reason | SVAA | AMVLP<br>or<br>Supplier | P0301 - Rejection of Asset Metering Agent Registration | Self-Service Gateway |
| 2.10.6 | After 2.10.5 | Return to 2.10.1 if AMVLP or Supplier wishes to submit valid Asset Metering Agent details | AMVLP<br>or<br>Supplier |  |  |  |
| 2.10.7 | Within 1 WD of 2.10.4 | If Asset Metering Agent Details are valid, send acceptance notification | SVAA | AMVLP<br>or<br>Supplier | P0302 - Confirmation of Asset Metering Agent Registration | Self-Service Gateway |
| 2.10.8 | After 2.10.7 | Go to 2.11.1 | AMVLP<br>or<br>Supplier |  |  |  |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 2.11 Registration of Asset Meter Details for an Asset and related Asset Metering Systems

Once the MOA or AMMOA has installed the Asset Meter(s) for the Asset Metering System(s), the AMVLP or Supplier must complete the registration of the Asset by registering the Asset Meter Details before the AMSID Pair can be allocated to a Secondary BM Unit.

For those Assets which are eligible to be registered by an AMVLP (for the AMSID Pair to be Allocated to a Secondary BM Unit) or by a Supplier (for the AMSID Pair to be included in an EMR AMSID Declaration), the Asset must only be registered once; the AMSID Pair can be used by up to two AMVLPs and one Supplier simultaneously. The AMVLP or Supplier seeking to register an Asset should first check with the Asset owner whether the Asset has already been registered, as it will not be possible to identify any such duplication before this third stage of the Asset Registration process.

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.11.1 | After 2.10.8 and at least 3 WD before allocation of the AMSID Pair to a Secondary BM Unit | Submit Asset Meter details. | AMVLP<br>or<br>Supplier | SVAA | P0303 - Asset Meter Registration | Self-Service Gateway or other method, as agreed. |
| 2.11.2 | Within 1 WD of 2.11.1 | If Self-Service Gateway was not the method used, in 2.11.1, log the Asset Meter details in the Register. | SVAA |  |  | Internal Process |
| 2.11.3 | Within 1 WD of 2.11.1 | Validate the Asset Meter details. | SVAA |  | Appendix 3.1.3 | Internal Process |
| 2.11.4 | Immediately following 2.11.3 | If Asset Meter details are invalid, send rejection notification with rejection reason.<br>If Asset Meter details are valid, but have already been registered, send rejection notification with rejection reason “This Asset has already been registered and AMSID Pair [xxxxxxxxxxxxx_yyyyyyyyyyyyy] has been generated. You may use this AMSID Pair without being the Registrant of the Asset”. | SVAA | AMVLP<br>or<br>Supplier | P0304 - Rejection of Asset Meter Registration<br>P0304 - Rejection of Asset Meter Registration | Self-Service Gateway |
| 2.11.5 | After 2.11.4 | Return to 2.11.1 if AMVLP wishes to submit revised Asset Meter details | AMVLP<br>or<br>Supplier |  |  |  |
| 2.11.6 | Immediately following 2.11.3 | If Asset Meter details are valid, send acceptance notification. | SVAA |  | AMVLP or<br>Supplier<br>P0305 - Confirmation of Asset Meter Registration | Self-Service Gateway |
| 2.11.7 | After 2.11.6 | Asset Meter registration is complete. | AMVLP<br>or<br>Supplier |  |  |  |
| 2.11.8 | After 2.11.7 | AMVLPs proceed to Section 2.1A to allocate AMSID Pair(s) to a Secondary BM Unit.<br>Suppliers proceed to Section 2.15 to include AMSID Pair(s) in an EMR AMSID Declaration. | AMVLP | or<br>Supplier |  |  |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 2.12 BM Unit Allocation Baselining Detail

Where a Lead Party registers a Secondary BM Unit, a Trading Secondary BM Unit or Additional BM Unit as a Baselined BM Unit, any MSID Pairs or AMSID Pairs already allocated to that BM Unit will default to a Baseline Indicator of “S” (indicating that the Lead Party will include them in the Submitted Expected Volume for that BM Unit). Where the Lead Party requires the expected volumes for an MSID Pair or AMSID Pair to be created via the Baselining Methodology, it must register each such MSID Pair or AMSID Pair for Baselining (updating the Baseline Indicator to “B”).

Where there may be insufficient demand data to calculate an MSID Baseline Value and the Lead Party may not be confident in their own ability to forecast expected usage (within the Submitted Expected Volume), the Lead Party can register MSID Pairs or AMSID Pairs to be inactive (Baseline Indicator of “I”).

This process applies to VLPs and Suppliers (for MSID Pairs), and AMVLPs (for MSID Pairs and AMSID Pairs).

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.12.1 | By 23:59 on the Settlement Day before it becomes effective. | Send the Baselined MSID Pairs or AMSID Pairs<br>Send Inactive MSID Pairs | Lead Party | SVAA | P0326 –BM Unit Allocation Baselining Detail | Self-Service Gateway or other method, as agreed. |
| 2.12.2 | Within 1 WD of 2.12.1 | If the BM Unit Allocation Baselining Detail was not submitted via the Self-Service Gateway, log Baselined or Inactive MSID Pairs or AMSID Pairs in the SVA Metering System and Asset Metering System Register. | SVAA |  |  | Internal Process |
| 2.12.3 | Immediately following successful receipt of Baselined MSID/AMSID Pair(s) or Inactive MSID Pair or AMSID Pair(s) into SVAA | Validate Baselined MSID Pairs or AMSID Pairs in accordance with Appendix 3.13 – Validation of Baselined MSID Pair or AMSID Pair files<br>Validate Inactive MSID Pairs or AMSID Pairs in accordance with Appendix 3.13 – Validation of Inactive MSID Pair or AMSID Pair files | SVAA |  | Appendix 3.13 – Baselined MSID Pair or AMSID Pair File Validation<br>Appendix 3.13 – Inactive MSID Pair or AMSID Pair File Validation |  |
| 2.12.4 | Immediately following 2.12.3 | If Baselined or Inactive MSID Pair or AMSID Pair is invalid, the SVAA shall send notification of the rejection to the Lead Party | SVAA | Lead Party | P0327 – Rejection of BM Unit Allocation Baselining Detail | Self-Service Gateway or other method, as agreed. |
| 2.12.5 | Immediately following 2.12.4 | If Baselined or Inactive MSID Pairs or AMSID Pairs is valid, update the Baselined or Inactive MSID Pairs or AMSID Pairs in the SVA Metering System & Asset Metering System Register. | SVAA |  |  | Internal Process |
| 2.12.6 | Immediately following 2.12.5 | Send confirmation of Baselined or Inactive MSID Pairs or AMSID Pairs. | SVAA | Lead Party | P0334 – Confirmation of BM Unit Allocation Baselining Detail | Self-Service Gateway or other method, as agreed. |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 2.13 BM Unit Submitted Expected Volumes

Where a Baselined BM Unit has non-Baselined MSID Pairs or non-Baselined AMSID Pairs allocated to it, the Lead Party must submit a Submitted Expected Volume to SVAA and/or submit a Default Submitted Expected Volume (which will be used where no Submitted Expected Volume has been provided).

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.13.1 | By 23:59 on the Settlement Day before it becomes effective. | Submit the MSID Pair or AMSID Pair Default Submitted Expected Volumes (relating to non-Baselined MSID Pairs and non-Baselined AMSID Pairs in a Baselined BM Unit). | Lead Party | SVAA | P0328 BM Unit Submitted Expected Volume Notification | Electronic or other method, as agreed. |
| 2.13.2 | No later than Gate closure for a Settlement Period | Submit the MSID Pair or AMSID Pair Submitted Expected Volumes (relating to non-Baselined MSID Pairs and non-Baselined AMSID Pairs in a Baselined BM Unit). | Lead Party | SVAA | P0328 BM Unit Submitted Expected Volume Notification | Electronic or other method, as agreed. |
| 2.13.3 | Within 1 WD of 2.13.2 | or where appropriate within 1 WD of 2.13.1<br>Log and validate Submitted Expected Volumes | SVAA |  |  | Internal Process |
| 2.13.4 | Within 1 WD of 2.13.2 | or where appropriate within 1 WD of 2.13.1<br>If MSID Pair or AMSID Pair Delivered Volume fails validation send rejection. | SVAA | Lead Party | P0329 – BM Unit Submitted Expected Volume Rejection | Electronic or other method, as agreed. |
| 2.13.5 | Within 1 WD of 2.13.2 | or where appropriate within 1 WD of 2.13.1<br>If MSID Pair or AMSID Pair Submitted Expected Volume passes validation send confirmation. | SVAA | Lead Party | P0330 –BM Unit Submitted Expected Volume Acceptance | Electronic or other method, as agreed. |
| 2.13.6 | By Calendar Day prior to Settlement Day | Submitted Expected Volumes revalidation of EFD<br>(Non-zero Submitted Expected Volumes for BMU with no MSID/AMSID Pair with status ‘S’) | SVAA | Lead Party | P0331 BM Unit Submitted Expected Volume Warning | Electronic or other method, as agreed. |
| 2.13.7 | As per SVAA Calendar (for each Volume Allocation Run) | If a Submitted Expected Volume or Default Submitted Expected Volume for MSID Pair or AMSID Pair is not registered before Gate Closure for a particular Settlement Period, set Settlement Expected Volume to NULL | SVAA |  |  | Internal process |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 2.14 BM Unit Allocation Event Day

The Baseline Methodology creates a baseline (for a Baselined MSID Pair or Baselined AMSID Pair) based on normal usage and predicts what the MSID Pair should be doing. Therefore, the Lead Party of the Baselined BM Unit may require to discount days where the site is doing something not normal, such as providing a Balancing Service. As providing a Balancing Service can affect the site outside of the Settlement Period providing the Balancing Service the whole day is discounted from the calculation of the baseline. Trading Secondary BM Units registered by VTPs for the must be Baselined.

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.14.1 | Up to 30 calendar days before an Event Day | Send notification of Event days for MSID Pairs or AMSID Pairs<br>Event Days can be submitted before the event and submissions can be updated subsequently if required (up until 30 calendar days after the event) | Lead Party | SVAA | P0323 BM Unit Allocation Event Day | Self-Service Gateway |
| 2.14.2 | Within 1 WD of 2.14.1 | Log and validate Event Day(s) or change to Event Day(s) | SVAA |  |  | Internal Process |
| 2.14.3 | Within 1 WD of 2.14.1 | If Event Day notification fails validation send rejection. Where SVAA has received an instruction to cancel an Event Day this will be notified via the rejection. | SVAA | Lead Party | P0324 Rejection of BM Unit Allocation Event Day | Self-Service Gateway |
| 2.14.4 | Within 1 WD of 2.14.1 | If Event day notification passes validation send confirmation. | SVAA | Lead Party | P0325 Confirmation of BM Unit Allocation Event Day | Self-Service Gateway |
| 2.14.5 | As required | Cancel Event Day(s)<br>Where an event day has been created in error. | SVAA |  |  | Internal Process |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 2.15 Submission of EMR Declarations

The submission of an EMR Declaration37 should be performed by a Category A or Category F Authorised person by manual entry into the Self Service Gateway (Elexon Kinnect). Each data item will be validated for compliance with specified data format on entry; when each mandatory data item has been submitted successfully, the details in the draft Declaration will then be subject to further validation checks.

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.15.1 | As required, and at least 10 WD prior to the required Effective From date | Submit EMR MSID Declaration | Or |  | Submit EMR AMSID Declaration<br>Supplier<br>SVAA<br>EMR MSID Declaration<br>(see Appendix 3.x)<br>EMR AMSID Declaration<br>(see Appendix 3.y).<br>Self-Service Gateway38<br>or<br>Submit EMR CVA BM Unit Declaration<br>CVA Registrant<br>CRA<br>EMR CVA BM Unit Declaration<br>(see Appendix 3.z). | Self-Service Gateway38 |
| 2.15.2 | Immediately following 2.15.1 | Register submitted details. | SVAA<br>or<br>CRA |  |  | Internal Process |
| 2.15.3 | Within 4WD of 2.15.2 | Validate the EMR Declaration. | SVAA<br>or<br>CRA |  |  | Internal Process |
| 2.15.4 | Immediately following 2.15.3 | Notify Supplier or CVA Registrant of the outcome of the validation of the EMR Declaration | SVAA<br>or<br>CRA | Supplier or CVA Registrant |  | Email |
| 2.15.5 | Following 2.15.4, and at least 4 WD prior to the required Effective From date, if Declaration was invalid, | Provide updated details and go to 2.15.3. | Supplier or CVA Registrant |  |  | Self-Service Gateway38 |
| 2.15.6 | Following 2.15.4, if Declaration was valid | End |  |  |  |  |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 2.16 Voluntary withdrawal of an EMR Declaration

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.16.1 | Where a Supplier or CVA Registrant becomes aware that the EMR Declaration will become invalid | End date EMR MSID Declaration | or |  | End date EMR AMSID Declaration<br>Supplier<br>SVAA<br>Effective To Date for the Declaration39.<br>Self-Service Gateway38<br>or<br>End date EMR CVA BM Unit Declaration<br>CVA Registrant<br>CRA<br>Effective To Date for the Declaration39 | Self-Service Gateway38 |
| 2.16.2 | Immediately following 2.16.1 | Validate the Declaration | SVAA<br>or<br>CRA |  |  | Internal Process |
| 2.16.3 | Immediately following 2.16.2 | If the Effective To Date is valid, store the Effective To Date and confirm acceptance to the Supplier or CVA Registrant | SVAA<br>or<br>CRA | Supplier or CVA Registrant | Confirmation acceptance | Email |
| 2.16.4 | Immediately following 2.16.3 | End process |  |  |  |  |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 2.17 Enforced withdrawal of an EMR Declaration

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.17.1 | Where the SVAA identifies40 - or is instructed by the BSC Panel (via BSCCo) - that an EMR Declaration is no longer valid. | The SVAA or CRA shall terminate the EMR Declaration by adding the Effective To Date specified by BSCCo.<br>Note that the Effective To Date could be retrospective and could be set to the Effective From Date to nullify an EMR Declaration. | SVAA | or<br>CRA | Effective To date<br>Internal SVAA process |  |
| 2.17.2 | Within 1WD of 2.6.1 | Notify the Supplier or CVA Registrant of the action taken. | SVAA | or<br>CRA<br>Supplier | Or CVA Registrant<br>The SVAA must provide a short explanation for the action taken | Email |
| 2.17.3 | Following 2.6.2 | End process |  |  |  |  |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 2.18 Wholesale market Activity Notifications

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.18.1 | Before Gate Closure for the relevant Settlement Period for the Wholesale Market trade | Submit WMAN to notify BM Unit, Settlement Date and Settlement Period relating to the Wholesale Market trade<br>Note that this can be sent multiple times if required | VTP | ECVAA | ECVAA-I051 WMAN | Electronic data file transfer |
| 2.18.2 | Immediately following 2.18.1 | Validate WMAN against valid Trading Secondary BM Units and time of receipt | ECVAA |  | ECVAA-I051 WMAN | Internal Process |
| 2.18.3 | Immediately following 2.18.2 | If WMAN received after Gate Closure or contains invalid BM Unit(s) issue WMAN Exception Report | ECVAA | VTP | ECVAA-I052 WMAN Exception Report | Electronic data file transfer |
| 2.18.4 | At 01:00 each calendar day | Notify the SVAA of all valid WMANs received for the previous calendar day | ECVAA | SVAA | ECVAA-I053 Daily WMAN Report | Electronic data file transfer |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

## 3. Appendices

### 3.1 Validation of MSID Pair and AMSID Pair Allocation File

If the MSID Pair Allocation or AMSID Pair Allocation was submitted via a method other than the Self-Service Gateway, the SVAA will validate the MSID Pair Allocation or AMSID Pair Allocation data file it receives and will log that data in the SVA Metering System and Asset Metering System Register, if the file has passed both Validation Stages below. If the data file fails validation, the SVAA will issue a Rejection of MSID Pair Allocation or a ‘Rejection of AMSID Pair Allocation to a Secondary BM Unit’ to the AMVLP.

If the MSID Pair Allocation or AMSID Pair Allocation was submitted via the Self-Service Gateway, Validate Stage 1 will not be required, as there will not be an Allocation File to validate; the Self-Service Gateway form will require all mandatory data items to be entered in the correct format before the AMVLP can save the Allocation.

#### 3.1.1 Validate Stage 1 – Schema Validation

The SVAA will validate the MSID Pair Allocation data from Lead Parties or the NETSO and the AMSID Pair Allocation data from AMVLPs. The incoming data will be validated to ensure:

Physical integrity; and

That the data file contains all mandatory data items in the required formats in accordance with the SVA Data Catalogue

#### 3.1.2 Validate Stage 2 – Business Logic Validation

The SVAA will validate the MSID Pair Allocation or the AMSID Pair Allocation to a Secondary BM Unit in accordance with the requirements in Section S. to ensure that:

3.1.2.1 For and MSID Pair:

it is from a valid Lead Party (i.e. a qualified Supplier, VLP, or AMVLP, VTP) or the NETSO

the BM Unit to be allocated is a valid BM Unit41

the Lead Party sending the notification is the Lead Party of the specified BM Unit to have a MSID Pair allocated

a MSID may not be allocated to more than one MSID Pair at any given time

each MSID within the MSID Pair is located within the same GSP group associated with the BM Unit40 to which they are to be allocated to; and

the EFSD of the MSID Pair Allocation is at least 5 working Days ahead of the date of receipt of the MSID Pair *

* Note that retrospective amendments are allowed and are detailed in Appendix 3.2

3.1.2.2 For an AMSID Pair:

it is submitted by a valid AMVLP

the BM Unit specified is a valid Secondary BM Unit

an AMSID may not be allocated to more than one AMSID Pair at any given time

the AMSID Pair is in the same GSP Group as the Secondary BM Unit4040 to which it is to be allocated

the Associated MSID Pair(s) has already been associated to that Secondary BM Unit

the combination of MSID Pair Indicator and AMSID Pair Differencing Indicator is allowed (see Section 3.9)

deallocate it from the first AMVLP’s Secondary BM Unit identify whether the AMSID Pair is already included in another Secondary BM Unit; and, if it is

whether the AMSID Pair is being used for the same purpose (i.e. for Asset Differencing or Asset Metering) in the other Secondary BM Unit:

an allowed combination of MSID Pair Indicator and AMSID Pair Differencing Indicator would result in a loss of AMSID Pair (see Section 3.10)

#### 3.1.3 Validate Stage 3 – Data Validation

3.1.3.1 The SVAA will further validate MSID Pair Notifications to be allocated to Secondary BM Units40 against reference data held by the relevant SMRS and published on the Electricity Enquiry Service (EES). This validation will ensure that:

each MSID is registered in the EES Database;

each MSID can record UTC Period Level Consumption for use in Settlement;

each MSID notified by a Lead Party is allocated to a Secondary BM Unit;

each MSID is not disconnected; and

the GSP Group for each MSID has been recorded correctly.

3.1.3.2 The SVAA will also validate AMSID Pair Notifications to be allocated to Secondary BM Units against data held within the SVA Metering System and Asset Meter Register. This validation will ensure that:

each AMSID is an Asset Metering System;

each AMSID Pair relates to an Asset which has successfully completed the three stage Registration process.

### 3.2 Amendments to MSID Pair Allocation or an AMSID Pair Allocation

Where a Lead Party wishes to retrospectively correct a MSID Pair Allocation error or an AMSID Pair Allocation error - or the NETSO wishes to retrospectively correct a MSID Pair Allocation error and, where correction of the identified error ensures that the future accuracy of Settlement, the SVAA shall facilitate such amendments for Settlement Days prior to having undergone the R1 Volume Allocation Run (VAR).

To clarify, only existing MSID Pair Allocations and existing AMSID Pair Allocations qualify for a Retrospective error correction.

The obligation remains with the Lead Party or the NETSO to ensure, wherever possible, that accurate data is submitted to the SVA Metering System & Asset Metering System Register for use in Settlement.

### 3.3 Disputed MSID Pair or AMSID Pair Allocation Resolution

Where a Lead Party has received a Loss of MSID Pair Allocation notification (a ‘Losing Lead Party’) or an AMVLP has received a Loss of AMSID Pair Allocation notification (a Losing AMVLP), and after discussion with the customer they believe it to be an erroneous notification, they may initiate the Disputed Allocation Procedure.

A Losing Lead Party or Losing AMVLP may initiate the Disputed MSID Pair Allocation Resolution Process by sending the P0286 or P0312 to the Gaining Lead Party or Gaining AMVLP.

The Gaining Lead Party or Gaining AMVLP shall use reasonable endeavours to respond to the Losing Lead Party or Losing AMVLP within 5 Working Days of receipt of the P0286or P0312.

Once the initial request has been made one of the following options shall be taken:

The Gaining Lead Party or AMVLP agrees that the MSID Pair or AMSID Pair is to be allocated to the Losing Lead Party or Losing AMVLP.

After appropriate investigation e.g. checking a valid contract is in place, the Gaining Lead Party or Gaining AMVLP disagrees with the Losing Lead Party or Losing AMVLP.

Where the Gaining Lead Party agrees with the Losing Lead Party:

The Gaining Lead Party or Gaining AMVLP shall update the SVA Metering System & Asset Metering System Register with a revised MSID Pair Allocation or AMSID Pair Allocation populated appropriately.

The Losing Lead Party or Losing AMVLP shall send a new MSID Pair Allocation or AMSID Pair Allocation populated appropriately.

Where Lead Parties are not in agreement:

The Gaining Lead Party or Gaining AMVLP shall send the Losing Lead Party or Losing AMVLP the P0286 or P0312 indicating the Gaining Lead Party or Gaining AMVLP disagrees with the Losing Lead Party or Losing AMVLP

The Losing Lead Party or Losing AMVLP can restart process should they remain in the belief that the rejection is erroneous (please return to step 1)

Where the Gaining Lead Party or Gaining AMVLP has received three transfer requests for the same MSID Pair or AMSID Pair from the same Losing Lead Party or Losing AMVLP and all requests are believed to be validly rejected, and prior to sending the third rejection:

They shall telephone the Customer to discuss the transfer and the reason for rejection,

They shall come to a conclusion with the Customer as to whether the transfer request is valid or invalid.

If valid, they shall amend the EFSD as requested and continue as per current process

If invalid, they will follow the current process in sending the rejection flow along with comments ‘validly rejected 3 times as agreed’.

If a further transfer request is received, the request will be escalated to a Gaining Lead Party team manager who will endeavour to reach a resolution with the Customer.

### 3.4 MSID Pair Delivered Volume or AMSID Pair Delivered Volume Notification

To ensure that MSID Pair Delivered Volumes, AMSID Pair Delivered Volumes and ABS MSID Pair Delivered Volumes are determined in good faith and in accordance with Good Industry Practice, VTPs, VLPs, AMVLPs and the NETSO must be able to provide upon request:

Sufficient information to demonstrate how the MSID Pair Delivered Volumes or ABS MSID Pair Delivered Volumes for any MSID Pair and the AMSID Pair Delivered Volumes for any AMSID Pair were derived.

It shall be possible for the VTP, VLP, AMVLP or the NETSO to re-run any individual determination of Delivered Volumes to recreate the results exactly as originally calculated, as a historical report. This shall include the facility to exclude later versions of business data which were received after the process was originally run.

Should any Delivered Volume process or other report process generate informational, warning or error logs as part of its processing, these logs should be available for inspection.

### 3.5 Validation of MSID Pair Delivered Volume or AMSID Pair Delivered Volume Files

The SVAA will validate the MSID Pair Delivered Volume or AMSID Pair Delivered Volume data it receives prior to allocating those volumes to the constituent MSIDs of the MSID Pair or to the constituent AMSIDs of the AMSID Pair as follows:

Validate Stage 1 – Schema Validation

The SVAA will validate the aggregated MSID Pair Delivered Volume or AMSID Pair Delivered Volume data from VTPs, VLPs or AMVLPs. The incoming data will be validated to ensure:

Physical integrity

That the data file contains all mandatory data items in the required formats in accordance with the SVA Data Catalogue

Validate Stage 2 – Business Logic Validation

The SVAA will validate the MSID Pair Delivered Volume, AMSID Pair Delivered Volume or ABS MSID Pair Delivered Volume in accordance with the requirements in Section S. The incoming data will be validated to ensure that:

it is from a valid Lead Party (i.e. a qualified Supplier, VTP, VLP or AMVLP) or the NETSO

the BM Unit specified is a valid BM Unit40

the sender of the notification is the Lead Party of the specified BM Unit for the relevant MSID Pair or AMSID Pair, or the NETSO

the MSID Pair Delivered Volume, AMSID Pair Delivered Volume or ABS MSID Pair Delivered Volume is for a valid MSID Pair or AMSID Pair stored in the SVA Metering System Register.

### 3.6 Allocation of MSID Pair Delivered Volumes, AMSID Pair Delivered Volumes and ABS MSID Pair Delivered Volumes

The SVAA will use the disaggregated kWh MSID metered data provided by:

HHDAs (in accordance with BSCP503) and; or

SDSs; or

ADSs.

and, where applicable, the kWh AMSID Metered data provided by HHDCs (in accordance with BSCP603) to allocate the MSID Pair Delivered Volume42 and, where applicable, the AMSID Pair Delivered Volume to the component MSIDs in that MSID Pair and to the component AMSIDs in that AMSID Pair for each Settlement Period, creating the Total Metering System Delivered Volume (TQVMDKj).

The steps of this process are as follows:

For each MSID Pair, start by allocating the MSID Pair Delivered Volume39 to the Export MSID for a positive value (or to the Import MSID for a negative value), subject to the constraint that the magnitude of the MSID Pair Delivered Volume that can be allocated is capped by the magnitude of the half hourly Metered data.

Allocate any remaining MSID Pair Delivered Volume40 to the other MSID in the MSID Pair (i.e. the Import MSID for a positive value, or the Export MSID for a negative value).

In the special case of an MSID Pair that does not include an Export MSID this process, all of the MSID Pair Delivered Volume will be allocated to the Import MSID.

If a MSID Pair Delivered Volume cannot be allocated in full to the component MSIDs using this process, the SVAA System will report an exception.

The SVAA operator will then report this exception to BSCCo and the VTP, VLP or the NETSO, as an exception indicates that the MSID Delivered Volume is inconsistent with the Settlement MSID Metered data (suggesting that the MSID Delivered Volume has been reported incorrectly).

If the review by the VTP, VLP or the NETSO identifies that the exception was caused by the MSID Pair Delivered Volume being incorrect, the Virtual Lead Party or the NETSO will submit a corrected MSID Delivered Volume to the SVAA.

For AMSID Pair Delivered Volumes, SVAA will assign those delivered volumes to the Associated MSID Pairs and will apply losses to those Delivered Volumes to take account of any losses between the Asset Metering System and the Boundary Point.

Where there is more than one AMVLP using AMSID Pairs and the same MSID Pair, MSID Pair Delivered Volumes will be assigned to each AMVLP based on their contribution to the MSID Pair Delivered Volume.

### 3.7 SVA Non-Final Demand Facilities

#### 3.7.1 Submission and validation of SVA Non-Final Demand Facility Declarations

In order for the SVAA to collect, aggregate, and report an SVA Non-Final Demand Facility’s Imports to the NETSO, the SVA Non-Final Demand Facility Operator (via their Supplier(s)) must submit and from time to time resubmit a valid director-signed Declaration Document to the SVAA.

The following methods can be used to submit a Declaration Document

The Facility Operator can submit Declaration details using an on-line form via the BSC Website for the Supplier to complete via Self Service Gateway

The Supplier can submit Declaration details on behalf of Facility Operator using Self Service Gateway.

Facility Operators via their Suppliers can submit a Declaration Form (F602/01) paper form via e-mail

Note: This route of submission where the Supplier sends the paper Declaration Form to the BSC Service Desk should only be used as a last resort and in the event that online channels are unavailable (as part of a system outage or maintenance).

Appendix 3.7.3 provides a Declaration Document form (F602/01) which can be used where paper method is used. The Declaration Document form comprises four parts:

Completed by the Supplier:

Part A - provide details about the Supplier and the Authorised Person submitting the entire Declaration Document to the SVAA on behalf of the SVA Non-Final Demand Facility Operator – the Supplier is responsible for filling out Part A but is responsible for submitting the entire Declaration Document, comprising Part A-D;

Completed by the SVA Non-Final Demand Facility Operator:

Part B – is a declaration letter containing a standard text with elements in square brackets which must be filled in or deleted as appropriate by the SVA Facility Operator depending on the circumstances. The final letter must be signed by one of the SVA Non-Final Demand Facility Operator’s registered directors;

Part C and Part D – provide templates for providing necessary details about a SVA Facility, the SVA Non-Final Demand Facility Operator and the related Metering Systems.

Where the SVA Non-Final Demand Facility Operator wishes to provide details for more than one SVA Facility in a Declaration Document, it may complete multiple copies of Part C, i.e. for each SVA Non-Final Demand Facility being declared. No matter how many Part Cs are provided, please list all MSID details in Part D.

Each copy of Part C and D in a single Declaration Document contain details specific to the Supplier submitting the Declaration Document. A separate Declaration Document(s) is produced for Metering Systems registered by other Supplier(s) at the same SVA Non-Final Demand Facility.

Collectively a single Part A, B, C and D constitute a single declaration. Where multiple Part Cs are provided in a single Declaration Document, there are as many Declarations as there are Part Cs in the Declaration Document.

Should an SVA Facility Operator need to declare, update or withdraw a declaration for an SVA Non-Final Demand Facility it must provide details as in the Declaration Document form (F602/01) provided in Appendix 3.7.3. Additional guidance is provided below in 3.7.1.1, 3.7.1.2 and 3.7.1.3.

SVA Non-Final Demand Facility Operators and Suppliers should endeavour to submit Declaration Documents before the date they are to take effect from. This is both to ensure that Metered Data can be collected, and before reaching the Final Reconciliation Volume Allocation Run (RF).

A Declaration Set refers to a single Declaration or several Declarations prepared by an SVA Non-Final Demand Facility Operator at a particular point in time which collectively provide details for the first time or update details in respect of a single SVA Non-Final Demand Facility. That is, the SVA Non-Final Demand Facility may be the subject of Metering Systems registered by more than one Supplier, so the SVA Non-Final Demand Facility Operator must prepare Declaration Documents for each Supplier to submit.

In accordance with Section 2.4, upon receipt of a Declaration Document, the SVAA will validate the declaration(s) by checking that the SVA Non-Final Demand Facility Operator has completed the Declaration Document in full, that its contents are (as far as the SVAA is able to determine) accurate and where appropriate that it has received Declaration Documents from all related Suppliers for a/the Non-Final Demand Facility/ies declared. The SVAA will register details of valid SVA Non-Final Demand Facilities and keep records of all Declaration Documents sent to it (whether valid or not). The SVAA will confirm to each Supplier that submits a Declaration Document whether the SVA Non-Final Demand Facilities therein were successfully validated or not, and if not, why not. The SVAA may liaise with the Supplier to clarify or seek further information before deciding whether an SVA Non-Final Demand Facility’s declaration is accepted or rejected.

The SVAA will publish and maintain on the BSC Website a list of all valid SVA Non-Final Demand Facilities. The list will show the SVA Facility name and the GSP Group it is located in.

The following subsections provide guidance for declaring an SVA Facility, updating a declaration and withdrawing a declaration.

The following subsections also summarise how an SVA Facility’s declaration may be withdrawn as a consequence of an assurance technique performed by the Panel, BSCCo and/or the SVAA, and how an SVA Facility Operator may withdraw from the BSC arrangements.

In all cases Non-Final Demand Declaration Documents and Operator Withdrawal letters must be submitted by email or, where agreed, by other electronic means using forms F602/01 or F602/02.

##### 3.7.1.1 Declaring an SVA Non-Final Demand Facility

This subsection describes how to declare an SVA Non-Final Demand Facility for the first time or when declaring an SVA Non-Final Demand Facility after it having been withdrawn at some point.

The SVA Facility Operator must complete a Non-Final Demand Declaration Document(s) and provide the necessary information using the template in Appendix 3.7.3.

The SVA Facility Operator may include details for more than one Non-Final Demand Facility in a single Declaration Document, so long as each Non-Final Demand Facility uses a distinct Non-Final Demand Facility Name and all of the Metering Systems listed in the Declaration Document are registered by the same Supplier.

Where the Metering Systems at a Non-Final Demand Facility are registered by more than one Supplier, the SVA Non-Final Demand Facility Operator must prepare a separate Declaration Document for each Supplier. Each Supplier must then submit the Declaration Document to the SVAA on the SVA Non-Final Demand Facility Operator’s behalf. In such a scenario, please ensure that each separate Declaration Document uses the same unique Non-Final Demand Facility Name.

The SVA Non-Final Demand Facility Operator must ensure that an SVA Non-Final Demand Facility is the subject of at least one Import and one Export SVA HH Metering System, which it identifies in the director-signed Declaration Document(s).

The Declaration ID should be left blank as this will be assigned by the SVAA where a Supplier is declaring a Facility for the first time. If redeclaring since the Facility’s declaration was withdrawn the Declaration ID should be left blank and SVAA will assign a new Declaration ID.

The Declaration Set ID and Declaration Set Effective From Date is specific to the Non-Final Demand Facility being declared, is set by the SVA Facility Operator and should be used consistently across all Declaration Documents related to the SVA Non-Final Demand Facility being declared. The Declaration Set EFD(s) should be the same as the date on the cover letter.

The Declaration Type should be – ‘NEW’.

The Total Count of MSIDs should equal the total number of Metering Systems measuring Imports and Exports at the SVA Facility on the date a Declaration is to take effect, irrespective of whether the Metering Systems are registered by different Suppliers.

Please ensure that SVA Facility Operator details are consistent with those registered with Companies House and with Ofgem.

##### 3.7.1.2 Amending an existing Declaration

Where any of the details relating to a current Declaration change or circumstances or operation of a declared SVA Non-Final Demand Facility change then the SVA Non-Final Demand Facility Operator must amend that Non-Final Demand Declaration(s). In order to do this, the SVA Non-Final Demand Facility Operator must use the Declaration Document template to create a new Declaration Document(s) that relist all details for the Declaration(s), not just those items to be updated.

The SVA Non-Final Demand Facility Operator must send its Declaration Document(s) to its Supplier(s), which in turn submit them to the SVAA. Please note that where a Non-Final Demand Facility is the subject of a Change of Supplier or Change of Metering System(s), even if the change affects a single Metering System or Supplier, the SVA Non-Final Demand Facility Operator must resubmit Declaration Documents covering all Metering Systems and Suppliers related to the Non-Final Demand Facility.

In all cases when updating an existing Declaration the SVA Non-Final Demand Facility Operator must:

use existing Declaration ID

use a new Declaration Set ID43

use a new Declaration Set EFD44. - i.e. the date on which the Declaration changes take effect. The Declaration Set EFD(s) should be the same as the date added to the letter in Part B.

use an appropriate Declaration Type – the SVA Non-Final Demand Facility Operator must use a Declaration Type that best reflects the purpose of updating the Declaration(s), i.e. ‘CoS’ (change of Supplier), or ‘CoM’ (change of Metering System details).

Where more than one type of update is being made for a SVA Non-Final Demand Facility, each update should be submitted using a distinct Declaration set and Declaration Type.

Where multiple Declarations are submitted at the same time for the same Non-Final Demand Facility these should be submitted in chronological order of when updates take effect.

ensure the Total MSID Count must equal the number of all MSIDs at the Facility, on the date the Declaration takes effect, which are registered by the Supplier(s), taking account of any new or removed MSIDs.

Where CoS or CoM:

The SVA Non-Final Demand Facility Operator must ensure Declaration Documents are submitted for all Suppliers and all Metering Systems related to the SVA Non-Final Demand Facility.

Where CoM:

Where the SVA Non-Final Demand Facility Operator updates an existing declaration by adding or removing a Metering System then the updated Metering System’s MSID EFD or ETD will reflect when the MSID was added or removed and all other unchanged MSIDs EFD/ETDs will be relisted as they were originally declared. Please note that the Declaration Set EFD for all rows related to the Non-Final Demand Facility should be the same, even if other items in a row, e.g. MSID EFD, are not changing.

##### 3.7.1.3 Withdrawing a Facility – voluntarily

Where any of the details relating to an existing Declaration change, or circumstances or operation of a declared facility change, and these changes would invalidate the Declaration for the SVA Non-Final Demand Facility then the SVA Non-Final Demand Facility Operator must withdraw the Declaration by submitting a Declaration Document via one of the Non-Final Demand Facility’s Suppliers. That is, a single Declaration Document submitted by one Supplier can end all other Declarations for Suppliers related to the same SVA Non-Final Demand Facility.

Similarly should the SVA Non-Final Demand Facility Operator choose to voluntarily withdraw its Non-Final Demand Facility(ies), even if no change in the operation of circumstances of the Facility(ies), then, it must submit a Declaration Document.

The Declaration Type must state ‘Withdrawal’.

The SVA Non-Final Demand Facility Operator must

use existing Declaration ID

use a new Declaration Set ID45.

use a new Declaration Set EFD46. - i.e. the date on which the Declaration changes take effect. The Declaration Set EFD(s) should be the same as the date on the cover letter.

Set each MSID

ensure the Total MSID Count equals the number of all MSIDs at the Facility registered by the Supplier(s)

##### 3.7.1.4 Withdrawing a Facility – enforced

Each month the SVAA and BSCCo perform assurance checks which may result in an SVA Non-Final Demand Facility’s Declarations being withdrawn.

Where the SVAA is required to change (e.g. add or remove a Metering System) or withdraw a SVA Non-Final Demand Facility Declaration(s) it will notify the Supplier(s) accordingly. It is then the Supplier’s responsibility to inform the SVA Non-Final Demand Facility Operator.

##### 3.7.1.5 Withdrawing an SVA Non-Final Demand Facility Operator’s details

Where an existing SVA Non-Final Demand Facility Operator with current or historical Declarations chooses to cease participating as a SVA Non-Final Demand Facility Operator then they may withdraw from that role by sending an Operator Withdrawal Letter to the SVAA. SVA Non-Final Demand Facility Operators should use the template letter provided in paragraph 3.7.4.

The letter must be signed by a registered Director of the SVA Non-Final Demand Facility Operator’s company.

Withdrawing as an SVA Non-Final Demand Facility Operator has the effect of causing all related SVA Non-Final Demand Facilities to be withdrawn on the same day.

#### 3.7.2 No Longer Used

#### 3.7.3 F602/01 SVA Non-Final Demand Facility Declaration Document form – Supplier

SVA Non-Final Demand Facility Declaration Document – F602/01 Part B, C and D are completed by the SVA Non-Final Demand Facility Operator prior to being sent to the Supplier to complete Part A. Once all parts are completed the Supplier should send to the SVAA by email or where agreed the equivalent information by other electronic means

Part A - Completed by Supplier – Category F or Category A Authorised Person Market Participant Id (MPID)………………… Authorised Person’s Name ................................................ Company .............................................. Party ID………………………………………….Password……………………………………………. Date………………………(Authorised in accordance with BSCP38)

Part B - Completed by SVA Non-Final Demand Facility Operator (please replace square bracketed text with correct/relevant information)(please see BSCP602 3.7.1 for guidance) [Insert company name] [Insert company address] [Insert current date] Director’s declaration of SVA Non-Final Demand Facility(ies) FAO the SVAA, I [insert full name], being a director of [insert your company name] (company number [insert company number]), hereby declare that, having made all due and careful enquiries, the information contained in this declaration is true, complete and accurate in all material respects and is not misleading by reference to the facts and circumstances at the date of this declaration. Capitalised terms used in this declaration have the meaning given to them in the Balancing and Settlement Code unless stated otherwise. I declare that as of [insert Non-Final Demand Declaration Set effective from date] the SVA Non-Final Demand [Facility/Facilities] identified in the attachments to this letter [comply with the meaning/will cease to comply with the meaning/ceased to comply with the meaning] of an SVA Non-Final Demand Facility. In particular that each SVA Non-Final Demand Facility to which this declaration relates: i. performs Electricity Storage and/or Generation and/or Eligible Services(as defined in the Connection and Use of System Code) as its sole function; ii. is operated by [insert your company name], and iii. has its Imports and Exports measured only by Metering Systems which are registered in the Supplier Meter Registration Service (SMRS), and can record UTC Period Level Consumption, as part of a Supplier BM Unit, and where those Metering Systems only measure activities necessary for performing Electricity Storage, Generation or Eligible Services (or a combination thereof) I declare that any material changes to the operation, configuration or measurement of electricity to or from any SVA Non-Final Demand Facility identified in the annex to this letter will be notified to you as soon as reasonably practicable. This director’s declaration is governed by and construed in accordance with English Law. Yours sincerely, [Insert Director’s Signature] [Insert full name] For and on behalf of: [Insert company name]

Part C - Completed by SVA Non-Final Demand Facility Operator (Please note that the following table has been populated for illustrative purposes. Please delete and replace entries as appropriate. Please see BSCP602 3.7.1 for guidance.

Non-Final Demand Declaration Set details

Declaration Type:

Declaration Set Id:

Declaration Id (where known):

Declaration Set Effective Date:

SVA Non-Final Demand Facility Operator (FO) details

FO Participant ID

FO Company Number

FO Company Name

FO Company Address

FO Company Director

FO Company Director Email

FO Contact Name

FO Contact Phone

FO Contact Email

Non-Final Demand Facility details

Facility ID:

Facility Name:

Facility Category

Facility Address/Location:

Facility Description ( Including technology type and size of facility):

Facility Maximum Import Capacity (MW)

Facility Maximum Export Capacity (MW)

Facility Effective From Date:

Facility Effective To Date:

Facility Total MSIDs Count:

Non-Final Demand Declaration Set details

Part D – Completed by SVA Non-Final Demand Facility Operator Please note that the following table has been populated for illustrative purposes. Please delete and replace entries as appropriate, working with your Supplier/s where necessary. Note that HHDA details should not be populated where no HHDA is appointed to the MSID. Please add more rows as necessary. Please see BSCP602 3.7.1 for guidance.

Declaration Set ID

Facility ID

MSID

Import/Export Indicator

GSP Group

MSID EFD

MSID ETD

Supplier MPID

MSID Supplier EFD

HHDA MPID

HHDA EFD

#### 3.7.4 Non-Final Demand Facility Operator Withdrawal Letter template – F602/02

SVA Non-Final Demand Facility Operator Withdrawal Letter – F602/02

Completed by SVA Non-Final Demand Facility Operator and sent to SVA Agent by email or where agreed, by other electronic means (please replace square bracketed text with correct/relevant information). (Please see BSCP602 3.7.1 for guidance.)

[Insert company name]

[Insert company address]

[Insert current date]

SVA Non-Final Demand Facility Operator withdrawal

FAO the SVAA,

I [insert full name], being a director of [insert your company name] (company number [insert company number]), hereby declare that, having made all due and careful enquiries, the information contained in this declaration is true, complete and accurate in all material respects and is not misleading by reference to the facts and circumstances at the date of this declaration. Capitalised terms used in this declaration have the meaning given to them in the Balancing and Settlement Code unless stated otherwise.

I declare that as of [insert date] [insert your company name] will [cease/have ceased] to be an SVA Non-Final Demand Facility Operator and that all SVA Non-Final Demand Facilities currently declared by [insert your company name] will cease to be SVA Non-Final Demand Facilities on the same date.

This director’s declaration is governed by and construed in accordance with English Law.

Yours sincerely,

[Insert Director’s Signature]

[Insert full name]

For and on behalf of: [Insert company name]

### 3.8 Data required for the Registration of Asset Metering Systems

#### 3.8.1 Asset details Required in Section 2.9

Action Indicator

Address Line 1

Address Line 2

Address Line 3

Address Line 4

Address Line 5

Address Line 6

AMSID Pair EFD

AMSID Pair ETD

AMVLP Id

Asset Capacity

Asset Registration Id

Asset Type

Asset Voltage

Delete Flag

Effective From Settlement Date

Export AMSID

Export AMSID required indicator

Export MSID

GSP Group Id

Import AMSID

Import MSID

Measurement Transformer Indicator

Postcode

#### 3.8.2 AMVLP Agent Details Required in Section 2.10

Action Indicator

AMHHDC Effective From Date

AMHHDC Id

AMMOA Effective From Date

AMMOA Id

Export AMSID

HHDC Effective From Date

HHDC Id

Import AMSID

MOA Effective From Date

MOA Id

#### 3.8.3 Asset Meter Details Required in Section 2.11

Action Indicator

Asset Meter Effective From Date

Asset Meter Effective To Date*

Asset Meter make and model

Asset Meter Serial Number

Asset Metering Type

Export AMSID

Import AMSID

Outstation Type

#### 3.8.4 AMSID Pair Allocation to a Secondary BM Unit details required in Section 2.1A

AMSID Pair Differencing Indicator

AMSID Pair in Secondary BM Unit EFD

AMSID Pair in Secondary BM Unit ETD

AMVLP Id

BM Unit Id

Export AMSID

Export MSID

Import AMSID

Import MSID

MSID Pair Indicator

#### 3.8.5 Validation of Asset Registration Data

##### 3.8.5.1 Schema Validation

The SVAA will validate each incoming data file to ensure that:

The structure of data file conforms to the specification in the IDD and / or the SVA Data Catalogue; and

all mandatory data items have been included

##### 3.8.5.2 Business Logic Validation

The incoming data will be validated to ensure that:

it is from a valid AMVLP

The Asset Meters are not already in use in another Asset Metering System

All Associated MSID Pairs have been registered

The Asset Meter Type exists in the list of CoP11 compliant Asset Meters

The HHDC is Qualified

The AMHHDC (where appointed) is Qualified

The MOA or AMMOA appointed is Qualified

Outstation Type is in list of valid Types

Note there is no requirement to have AMVLP Agents assigned when registering the Asset Metering System in the Asset Meter Register but they must be registered and be effective, and all Asset Meters on the site must be registered before the AMSID Pair(s) may be allocated to a Secondary BM Unit.

### 3.9 Definitions of Asset Metering and Asset Differencing

#### 3.9.1 Asset Metering

When an AMSID Pair is included in a Secondary BM Unit for the purposes of Asset Metering, the AMSID Pair Delivered volume will be allocated to the Secondary BM Unit instead of the Boundary Point MSID Pair Delivered Volume in the Secondary BM Unit. The Boundary Point MSID Pair is an Associated MSID Pair to the Secondary BM Unit, but is not included in it. AMVLPs should send only AMSID Pair Delivered Volumes to SVAA.

#### 3.9.2 Asset Differencing

When an AMSID Pair is included in a Secondary BM Unit for the purposes of Asset Differencing, the AMSID Pair Delivered volume will be deducted from the Boundary Point MSID Pair Delivered Volume in the Secondary BM Unit. The Boundary Point MSID Pair is an Associated MSID Pair to the Secondary BM Unit, and is included in it. There is no limit to the number of AMSID Pairs that may be combined with an Associated MSID Pair in a Secondary BM Unit for the purposes of Asset Differencing. AMVLPs should only send MSID Pair Delivered Volumes to SVAA.

For the avoidance of doubt Asset Differencing is only possible where the Boundary Point Metering System is Half Hourly or, for MHHS Metering Systems, records UTC Period Level Consumption. Asset Metering Systems registered in the Lead Party Asset Meter Register in accordance with BSCP607 may not be used for Asset Differencing.

### 3.10 Valid combinations of ‘MSID Pair Indicator’ and ‘AMSID Pair Asset Differencing Indicator’ in a Secondary BM Unit

The table below shows allowed usage of an AMSID Pair in a Secondary BM Unit:

MSID Pair Indicator

“T”

(No AMSIDs in Secondary BM Unit)

“A”

(AMSIDs in Secondary BM Unit used for Asset Metering)

“D”

(AMSIDs in Secondary BM Unit used for Differencing)

AMSID Pair Asset Differencing Indicator

“T”

(Apply Differencing)

Not allowed

Not allowed

AMSID Pair Delivered Volume(s) subtracted from MSID Pair Delivered Volume

“F”

(Do not apply Differencing)

Not allowed

AMSID Pair Delivered Volume(s) used instead of MSID Pair Delivered Volume

Not allowed

The same AMSID Pair / may be used by another AMVLP in its Secondary BM Unit without requiring a MSID Pair reallocation or an AMSID Pair reallocation.

AMVLP1 uses AMSID Pair (X) for Asset Metering and AMVLP2 uses AMSID Pair (X) for Asset Differencing:

AMVLP1 Secondary BM Unit 1:

MSID Pair (A) Indicator = A

AMSID Pair (X) Differencing Indicator = F

AMVLP2 Secondary BM Unit 2:

MSID Pair (B) Indicator = D

AMSID Pair (X) Differencing Indicator = T

AMVLP2 may include more than one AMSID Pair used for Asset Differencing in a Secondary BM Unit – for example:

AMVLP2 Secondary BM Unit 2:

MSID Pair (B) Indicator = D

AMSID Pair (X) Differencing Indicator = T

AMSID Pair (Y) Differencing Indicator = T

AMSID Pair (Z) Differencing Indicator = T

### 3.11 Shared use of MSID Pairs

The same MSID Pair may be used by multiple AMVLPs in their Secondary BM Units without requiring a MSID Pair reallocation or an AMSID Pair reallocation, provided that zero or one of the Secondary BM Units have the MSID Pair Indicator set to “D”, and all the others have the MSID Pair Indicator set to “A” (and the AMSID Pair Asset Differencing Indicators are set in accordance with 3.9).

### 3.12 Effect of Proposed AMSID Pair use in AMSID Pair Allocations

Ref

Proposed use of MSID Pair

Existing use of MSID Pair by another AMVLP

Outcome

Proposed Solution

1

MSID Pair Indicator = “T”

Another AMVLP has the MSID Pair allocated to their Secondary BM Unit with indicator of ‘T’

Reallocation process triggered.

This is the MSID Pair reallocation process for Secondary BM Units without AMSID Pairs.

2

MSID Pair Indicator = “T”

Another AMVLP has the MSID Pair allocated to their Secondary BM Unit with indicator of ‘A’ or ‘D’

Allocation is not allowed

The parties involved must agree how to resolve the inconsistency.

For example, If an existing AMVLP is using Asset Metering, the new AMVLP could use Differencing.

3

MSID Pair Indicator = “A”

Another AMVLP is already using the AMSID Pair, with ‘Apply Differencing’ Indicator of False

Automatic reallocation process triggered

SVAA re-allocates the AMSID Pair to the gaining AMVLP.

This is similar to #1 above, except that MSID Pair and AMSID Pair allocations will need to be end-dated for the losing AMVLP.

4

MSID Pair Indicator = “A”

Another AMVLP is already using the AMSID Pair, with ‘Apply Differencing’ Indicator of True

No reallocation process required

Both AMVLPs can use the same AMSID Pair.

5

MSID Pair Indicator = “A”

Another AMVLP is already using one of the Boundary Point MSID Pairs, with Indicator of ‘T’

SVAA validation prevents the allocation.

The AMVLPs involved must agree how to resolve the inconsistency.

For example, the existing AMVLP could switch to Differencing (removing the new AMVLP’s Asset from their Secondary BM Unit).

6

MSID Pair Indicator = “A”

Another AMVLP is already using one of the Boundary Point MSID Pairs, with Indicator of ‘A’

No reallocation process required

Both AMVLPs can use Asset Metering for their respective Assets. Note that they couldn’t use Asset Metering with the same AMSID Pair – that is covered by #3 above.

7

MSID Pair Indicator = “A”

Another AMVLP is already using one of the Boundary Point MSID Pairs, with Indicator of ‘D’

No reallocation process required…

…provided the new AMVLP’s AMSID Pair is also in the existing AMVLP’s Secondary BM Unit (scenario #4 above).

If it is not, SVAA will prevent the new AMVLP’s allocation.

The AMVLPs involved must agree how to resolve the discrepancy e.g. by the existing AMVLP adding the new AMSID Pair into their Secondary BM Unit.

8

MSID Pair Indicator = “D”

Another AMVLP is already using the AMSID Pair, with ‘Apply Differencing’ Indicator of True

SVAA validation prevents the allocation

Differencing is sufficiently complex that the new AMVLP will be blocked until the old AMVLP has end-dated their allocations.

9

MSID Pair Indicator = “D”

Another AMVLP is already using the AMSID Pair, with ‘Apply Differencing’ Indicator of False

No reallocation process required

Both AMVLPs can use the AMSID Pair

10

MSID Pair Indicator = “D”

Another AMVLP is already using one of the Boundary Point MSID Pairs, with Indicator of ‘T’

SVAA validation prevents the allocation

The AMVLPs involved must agree how to resolve the inconsistency.

11

MSID Pair Indicator = “D”

Another AMVLP is already using one of the Boundary Point MSID Pairs, with Indicator of ‘A’

No reallocation process required…

…provided the new AMVLP includes the AMSID Pair(s) that the existing Secondary BM Unit is using in their Secondary BM Unit.

12

MSID Pair Indicator = “D”

Another AMVLP is already using one of the Boundary Point MSID Pairs, with Indicator of ‘D’

SVAA validation prevents the allocation

The AMVLPs involved must agree how to resolve the inconsistency. For example, the existing AMVLP could end-date their allocation, or switch to Asset Metering

### 3.13 Validation of Baselined or Inactive MSID Pair and AMSID Pair Files

If the MSID Pair or AMSID Pair for Baselining was submitted via a method other than the Self-Service Gateway, the SVAA will validate the MSID Pair or AMSID Pair for Baselining data file it receives and will log that data in the SVA Metering System and Asset Metering System Register, if the file has passed both Validation Stages below. If the data file fails validation, the SVAA will issue a Rejection of MSID Pair for Baselining or a ‘P0327 - Rejection of BM Unit Allocation Baselining Detail’ to the VLP, AMVLP, VTP47 or Supplier.

If the MSID Pair or AMSID Pair for Baselining was submitted via the Self-Service Gateway, Validate Stage 1 will not be required, as there will not be a Baselining File to validate; the Self-Service Gateway form will require all mandatory data items to be entered in the correct format.

#### 3.13.1 Validate Stage 1 – Schema Validation

The SVAA will validate the MSID Pair for Baselining data or the AMSID Pair for Baselining data from VLP, AMVLP, VTP or Supplier. The incoming data will be validated to ensure:

Physical integrity; and

That the data file contains all mandatory data items in the required formats in accordance with the SVA Data Catalogue

#### 3.13.2 Validate Stage 2 – Business Logic Validation

The SVAA will validate the Baselined MSID Pair or the Baselined AMSID Pair for allocation to a Baselined BM Unit in accordance with the requirements in Section S to ensure that:

3.13.2.1 For a Baselined MSID Pair:

it is from a valid Lead Party (i.e. a qualified Supplier, VLP, AMVLP or VTP48)

the BM Unit to be allocated is a Baselined BM Unit

the Lead Party sending the notification is the Lead Party of the Baselined BM Unit

the Baselining Methodology selected by the Lead Party is one of the approved; and

the EFSD of the Baselined MSID Pair is at least 1 Working Day ahead of the date of receipt of the Baselined MSID Pair

3.13.2.2 For a Baselined AMSID Pair:

it is submitted by a valid AMVLP

the BM Unit specified is a valid Baselined BM Unit

the Lead Party sending the notification is the Lead Party of the Baselined BM Unit

the Baselining Methodology selected by the Lead Party is one of the approved

the EFSD of the Baselined AMSID Pair is at least 1 Working Day ahead of the date of receipt of the Baselined MSID Pair

3.13.2.3 For an Inactive MSID Pair:

it is from a valid Lead Party (only a VLP, AMVLP or VTP)

the BM Unit to be allocated is a Secondary BM Unit

the Lead Party sending the notification is the Lead Party of the Secondary BM Unit; and

the EFSD of the Inactive MSID Pair is at least 1 Working Day ahead of the date of receipt of the MSID Pair

3.13.2.4 For an Inactive AMSID Pair:

it is submitted by a valid AMVLP

the BM Unit specified is a valid Secondary BM Unit

the Associated MSID Pair(s) has already been associated to that Secondary BM Unit; and

the EFSD of the Inactive MSID Pair is at least 1 Working Day ahead of the date of receipt of the MSID Pair {{

### 3.14 EMR Declarations

#### 3.14.1 Submission and validation of EMR Declarations

In order for BSC Systems to identify the volume of electricity consumed by Generating plant and / or Battery Storage operated at a site in accordance with a Generation Licence for each Settlement Period, and to deduct such volumes from the Gross BM Unit Demand sent to the EMR Settlement Company for the purposes of calculating the Final Consumption Levy charges, the Supplier or CVA Registrant must submit an EMR Declaration, including Generation Licensee details, to the SVAA. The three types of EMR Declaration are specified in Section 1.1.6.

The Supplier (for an EMR MSID Declaration or an EMR AMSID Declaration) or the CVA Registrant (for a CVA BM Unit Declaration) should use reasonable endeavours to submit the EMR Declaration via the Self Service Gateway.

If it is not possible, e.g. due to a systems outage, for the Supplier or CVA Registrant (Category A or F Authorised Person) to use the Self Service Gateway, they may email the completed form to the BSC Service Desk, for it to be uploaded on their behalf. This mechanism should only be used in exceptional circumstances.

Appendices 3.14.5, 3.14.6 & 3.14.7 provide the three EMR Declaration forms (F602/05, F602/06, F602/07) for use when the mechanism is ‘email’. Any EMR Declaration submitted in this way will require longer to process than an EMR Declaration entered via the Self Service Gateway.

In accordance with Section 2.15, upon receipt of an EMR Declaration, the SVAA or CRA, as appropriate, will validate the Declaration.

3.14.2 Validation of EMR Declarations:

Where an EMR Declaration is submitted via the Self Service Gateway each data item entered will be checked for compliance with the data item format, and will not save any details that are entered incorrectly. When all mandatory data items have been entered successfully, the user will be allowed to submit the completed declaration for validation.

3.14.3 Validation of EMR MSID Declarations:

Final Demand flag is “F”

The Import MSID is appointed to the Supplier that submitted the EMR MSID Declaration

Each MSID is:

Energised

Correctly Specified as Import or Export

Recording UTC Period Level Consumption for Settlement

Generation Licence is valid

Generation Licensee is registered

Note that the Import MSID and the Export MSID should not be considered as a MSID Pair, and MSID Pair validations will not apply.

#### 3.14.4 Validation of EMR AMSID Declarations

Final Demand flag is “T”

Each MSID Pair is a valid MSID Pair recorded in the SVA Metering Systems and Asset Metering Systems Register

Each MSID is:

Energised

Correctly Specified as Import or Export

Half Hourly

Each Import MSID is appointed to the Supplier that submitted the EMR MSID Declaration

Each AMSID Pair is a valid MSID Pair recorded in the SVA Metering Systems and Asset Metering Systems Register

Generation Licence is valid

Generation Licensee is registered

A Supplier that has submitted, or intends to submit an EMR AMSID Declaration must ensure that every Generator or Battery at a site operating under the terms of a Generation Licence has been registered as an Asset in the SVA Metering Systems and Asset Metering Systems Register in order to obtain an AMSID Pair for inclusion in the EMR AMSID Declaration.

3.14.5 Validation of EMR CVA BM Unit Declarations:

Final Demand flag is “F”

Each CVA BM Unit is:

registered in CMRS

Type T or E (but not Type I)

Registrant is a valid Role for the BM Unit Type

Generation Licence is valid

Generation Licensee is registered

#### 3.14.6 Change of details for an existing EMR Declaration

When a Supplier is de-appointed from an Import MSID which is in an EMR MSID Declaration or an EMR AMSID Declaration, then the relevant EMR Declaration will cease to be valid and the Supplier should withdraw the EMR Declaration by end-dating it. If the Supplier fails to do so, the SVAA System will alert the SVAA operator of a mismatch between the Supplier for the MSID in the SVA Metering Systems and Asset Metering Systems Register and the EMR Declaration will be end dated.

If the Generation Licensee details relating to a current EMR Declaration change, but there is still a valid Licensee, then the Supplier should amend the details. This will not invalidate the EMR Declaration.

If the configuration of a site represented by an EMR AMSID Declaration changes, through the addition or removal of Generation and / or Storage, the Supplier must amend the EMR AMSID Declaration to add or remove AMSID Pairs with the appropriate Effective From Date. This will create a new version of the EMR AMSID Declaration and SVAA will process the EMR AMSID Declaration on a Settlement Day basis.

#### 3.14.7 Enforced Withdrawal of an EMR Declaration

The SVAA and BSCCo perform assurance checks which, if they identify that a site has not been represented correctly, could result in an EMR Declaration being withdrawn. Reasons for enforced withdrawal include, but are not limited to:

Supplier is no longer appointed to

The Import MSID in an EMR MSID Declaration; or

Every Import MSID in an EMR AMSID Declaration

there is Final Demand present at a site represented by an EMR MSID Declaration or a CVA BM Unit Declaration;

the Generation and / or Storage at a site is not operated under a Generation Licence.

#### 3.14.8 Director’s Declaration of Generation

The Supplier or the CVA Registrant, if they are not the Generation Licensee, should obtain the Director’s Declaration of Generation Licence form below, completed by the Generation Licensee, and should enter the required details into the relevant EMR Declaration49.

Completed by the Generation Licensee (please replace square bracketed text with correct/relevant information)

[Insert company name]

[Insert company address]

[Insert current date]

Director’s Declaration of Generation Licence

I [insert full name], being a director of [insert your company name] (company number [insert company number]), hereby declare that, having made all due and careful enquiries, the information contained in this declaration is true, complete and accurate in all material respects and is not misleading by reference to the facts and circumstances at the date of this declaration. Capitalised terms used in this declaration have the meaning given to them in the Balancing and Settlement Code unless stated otherwise.

I declare that as of [insert effective from date] the [Generation and/or Battery Storage plant identified in the attachments to this letter] comply with the requirements of the EMR Declaration Type to which this declaration relates:

is operated by [insert your company name], which also holds a valid Generation Licence;

has its Imports and Exports measured by Half Hourly Metering Systems which are registered in:

the Supplier Meter Registration Service (SMRS) as part of a Supplier BM Unit (for an EMR MSID Declaration or an EMR AMSID Declaration); or

the Central Meter Registration Service (CMRS) as part of a CVA BM Unit (for an EMR CVA BM Unit Declaration); and

[is / is not] used solely in relation to the generation of electricity carried out in accordance with the relevant generation licence.

I declare that any material changes to the operation, configuration or measurement of electricity to or from any Generation and/or Battery Storage plant identified in the annex to this letter will be notified to you as soon as reasonably practicable.

This director’s declaration is governed by and construed in accordance with English Law.

Yours sincerely,

[Insert Director’s Signature]

[Insert full name]

Generation and/or Battery Storage plant at site

#### 3.14.9 F602/04 EMR MSID Declaration form

This form should only be completed where the Supplier cannot use the Self Service Gateway to submit the EMR MSID Declaration (as set out in 3.14.1).

EMR MSID Declaration – F602/04

Completed by Supplier – Category A or Category F Authorised Person

Market Participant Id (MPID)………………...

Authorised Person’s Name ................................................ Company ..............................................

Party ID………………………………………….Password…………………………………………….

Date………………………(Authorised in accordance with BSCP38)

EMR Declaration Reference

Should be an unique identifier specified by submitter

Initial / Revised Declaration indicator

I / R

Declaration Effective From Date

Cannot be retrospective

Declaration Effective To Date

Optional for Initial Declarations

Postcode of site

GSP Group

Final Demand indicator

Must be “N” for an EMR MSID Declaration

N

Import MSID

Export MSID

Generation licensee details:

To be taken from the Director’s Declaration of Generation Licence

Generation licensee Company name

Generation licensee Company number

Facility Category (Generation or Battery Storage)

If more than one at site, please insert additional rows and enter details separately

#### 3.14.9 F602/05 EMR AMSID Declaration form

This form should only be completed where the Supplier cannot use the Self Service Gateway to submit the EMR AMSID Declaration (as set out in 3.14.1).

An EMR AMSID Declaration may include a site with more than one Import MSID, but each Import MSID must be serviced by the same Supplier.

EMR AMSID Declaration – F602/05

Completed by Supplier – Category A or Category F Authorised Person

Market Participant Id (MPID)………………...

Authorised Person’s Name ................................................ Company ..............................................

Party ID………………………………………….Password…………………………………………….

Date………………………(Authorised in accordance with BSCP38)

EMR Declaration Reference

Should be an unique identifier specified by submitter

Initial / Revised Declaration indicator

I / R

Declaration Effective From Date

Cannot be retrospective

Declaration Effective From Date

Declaration Effective To Date

Optional for Initial Declarations

Postcode of site

GSP Group

Final Demand Indicator

Must be “Y” for an EMR AMSID Declaration

Y

Generation licensee details

To be taken from the Director’s Declaration of Generation Licence

Generation licensee Company name

Generation licensee Company number

MSID Pair Details

If there is more than one MSID Pair, please insert additional rows

Import MSID

Export MSID

Asset & AMSID Pair Details

If there is more than one AMSID Pair, please insert additional rows

Import AMSID

Facility Name

Facility Category (Generation or Battery Storage)

If more than one at site, please insert additional rows and enter details separately

#### 13.14.10 F602/06 EMR CVA BM Unit Declaration form

This form should only be completed where the CVA registrant cannot use the Self Service Gateway to submit the EMR CVA BM Unit Declaration (as set out in 3.14.1).

EMR CVA BM Unit Declaration – F602/06

Completed by CVA registrant – Category A or Category F Authorised Person

Market Participant Id (MPID) ……………….......................

Only required for Suppliers

Authorised Person’s Name ................................................ Company ..............................................

Party ID………………………………………….Password…………………………………………….

Date………………………(Authorised in accordance with BSCP38)

EMR Declaration Reference

Should be an unique identifier specified by submitting company

CVA BM Unit Name

Initial / Revised Declaration indicator

I / R

Declaration Effective From Date

Cannot be retrospective

Declaration Effective To Date

Optional for Initial Declarations

Postcode of site

Final Demand indicator

Must be “N” for a CVA BM Unit Declaration

N

Generation licensee details:

To be taken from the Director’s Declaration of Generation Licence

Generation licensee Company name

Generation licensee Company number

Facility Category (Generation or Battery Storage)

If more than one at site, please insert additional rows and enter details separately

### 3.15 Validation of and retrieval of Supplier and HHDA50 details for MSIDs

The validation and data retrieval carried out on each MSID that is registered in the SVA Metering System and Asset Metering System Register in accordance with this BSCP will depend on whether that MSID has been migrated to the new MHHS arrangements.

Each HH MSID that has been migrated to the new MHHS arrangements (MHHS MSID) will not be serviced by a HHDC and a HHDA, they will be serviced by a Data Service, which will send the metered data to the SVAA. Only HH MSIDs which have not been migrated to the new MHHS arrangements – or those which have been migrated but have subsequently reverse-migrated - will be serviced by a HHDC and a HHDA.

Consequently, the SVA Metering System and Asset Metering System Register will need to carry out the validation and data retrieval activities described above on a daily basis, as it will need to know whether a MSID is a MHHS MSID or a non-MHHS MSID when it is first registered in it, and will need to know at the earliest opportunity when a MSID has changed migration status, to ensure that SVAA requests the Metered data for each MSID from the correct source.

The SVA Metering System and Asset Metering System Register uses the Electricity Enquiry Service (EES) service to validate the following data for each MSID registered in accordance with this BSCP602:

MSID exists;

MSID is energised;

Energy Direction (Import or Export) is correct;

GSP Group Id is correct;

Whether the MSID is a MHHS MSID; and

Where the MSID is not a MHHS MSID, whether the MSID is Half Hourly;

The SVA Metering System and Asset Metering System Register will also retrieve and store the following details from the EES:

For Non-MHHS MSIDs:

Supplier;

Supplier EFD;

HHDA; and

HHDA EFD.

For MHHS MSIDs:

Supplier;

Supplier EFD; and

MHHS Indicator EFD

As there will be no HHDA MPID for a MHHS MSID, the SVA Metering System and Asset Metering System Register will allocate the same generic ‘pseudo-HHDA’ MPID to each, to enable MHHS MSIDs and non-MHHS MSIDs to be stored together.

Amendment Record

| Version | Details (in source column order: Date / Description of Change / Changes Included / Mods/Panel/Committee Refs.) |
|---|---|
| 1.0 | 28 Feb 2019<br>February 2019 Release<br>P344<br>Panel 284C/01 |
| 2.0 | 01 Apr 2020<br>April 2020 Release<br>P354, P388<br>Panel 276/04 |
| 3.0 | 01 April 2021<br>April 2021 Release<br>P383<br>Panel 312/08 |
| 4.0 | 30 June 2022<br>June 2022 Release<br>P375, P433<br>Panel 318/06, Panel 322/05 |
| 5.0 | 23 Feb 2023<br>February 2023 Release<br>P376,P419<br>P312/04, P323/06 |
| 6.0 | 29 June 2023<br>June 2023 Release<br>CP1580<br>P338/04 |
| 7.0 | 02 November 2023<br>November 2023 Release<br>P395<br>P340/05 |
| 8.0 | 07 November 2024<br>November 2024 Release<br>P415<br>Panel 339/03 |
| 9.0 | 22 September 2025<br>September 2025 Release<br>P478, CP1599, P486<br>Panel 355A/02<br>SVG 285/04<br>Panel 363/04 |
| 10.0 | 27 November 20<br>27 November 2025 Special Release<br>P483 |

*[Amendment record rebuilt from a flattened copy-paste; each row's cells are listed in source column order.]*

Intellectual Property Rights, Copyright and Disclaimer

The copyright and other intellectual property rights in this document are vested in Elexon or appear with the consent of the copyright owner. These materials are made available for you for the purposes of your participation in the electricity industry. If you have an interest in the electricity industry, you may view, download, copy, distribute, modify, transmit, publish, sell or create derivative works (in whatever format) from this document or in other cases use for personal academic or other non-commercial purposes. All copyright and other proprietary notices contained in the document must be retained on any copy you make.

All other rights of the copyright owner not expressly dealt with above are reserved.

No representation, warranty or guarantee is made that the information in this document is accurate or complete. While care is taken in the collection and provision of this information, Elexon Limited shall not be liable for any errors, omissions, misstatements or mistakes in any information or damages resulting from the use of this information or action taken in reliance on it.

1

2 Final Consumption Levy charges are calculated by the Electricity Market Reform Settlement Company

3 A VLP that has not also Qualified as an Asset Metering VLP may not register an Asset

4 Balancing Services in this instance refers to the Balancing Mechanism and Replacement Reserve

5 For the avoidance of doubt, the same SVA MSID may be included in an EMR MSID Declaration and in a SVA Non-Final Demand Declaration where it meets the criteria for both.

6 This is received by ECVAA but is required by SVAA

7 Balancing Services in this instance refers to the Balancing Mechanism and Replacement Reserve

8 Where such amendments correct an identified error that impacts Settlement accuracy, the SVAA shall facilitate such amendments for Settlement Days prior to having undergone the R1 VAR Run

9 Provided that the AMSID Pair is in the same GSP Group as the Secondary BM Unit

10 Where such amendments correct an identified error that impacts Settlement accuracy, the SVAA shall facilitate such amendments for Settlement Days prior to having undergone the R1 VAR Run

11 Note that does not result in a ‘Loss of AMSID Pair Allocation’ for the first AMVLP, as both AMVLPs are allowed to use the AMSID Pair

12 If a Supplier is also using the AMSID Pair in an EMR AMSID Declaration in accordance with Section 2.15, they would be eligible to become the Registrant of the relevant Asset. If the Supplier became the Registrant of the Asset, the 2nd AMVLP would be allowed to continue to use the AMSID Pair.

13 Balancing Services in this instance refers to the Balancing Mechanism, Replacement Reserve

14 P375 will introduce new versions of the P0282, P0283, P0284 & P0285 that will include AMSID Pair Delivered Volumes or MSID Pair Delivered Volumes, as applicable.

15Upon receipt of revised Delivered Volume data

16 Upon receipt of revised ABS MSID Pair Delivered Volume data

17 Please see Appendix 3.7.1 for guidance.

18 Please note that where an SVA Facility Operator is declaring an SVA Non- Final Demand Facility for the first time, i.e. where the SVAA has no record of the person acting as an SVA Non- Final Demand Facility Operator, then the SVAA will create an ‘operator record’ as part of processing the declaration(s) for the SVA Non- Final Demand Facility. There is no dedicated ‘create operator record’ process.

19 That is, an SVA Non- Final Demand Facility may have more than one Metering System and each Metering System may be registered by a different Registrant. In such a scenario the SVAA should expect to receive a Declaration from each Supplier that is a Registrant of at least one of the Metering Systems at the SVA Non- Final Demand Facility. The SVAA determines whether they are expecting more than one declaration (i.e. a Declaration set) by reviewing the numbers of MSIDs declared in a Declaration and comparing it against the Total Number of MSIDs which is also identified in each Declaration.

2020 [CP1599] An HHDA will not be appointed to MHHS MSIDs (MSIDs operating under the MHHS Arrangements).SVAA will already have received the data from Data Services.

21[CP1599] The SVAA may not need to obtain Metered data for an MSID if that MSID is the subject of an existing Metering System Reporting Notification (D0354) for another BSC process,[P478] or of no HHDA is appointed to the MSID.

2122The SVAA shall specify the Effective to Settlement Date (J1870) in the D0354 Metering System Reporting Notification.

2223Please see Appendix 3.7.1 for guidance.

2324 [CP1599] An HHDA will not be appointed to MHHS MSIDs.

25The SVAA must not instruct the HHDA to cease reporting Metered data for an MSID if that MSID is the subject of an existing Metering System Reporting Notification (D0354) for another BSC process.

2426The SVAA shall specify the Effective to Settlement Date (J1870) in the D0354 Metering System Reporting Notification.

2527Please see Appendix 3.7.1 for guidance.

2628The SVAA may identify that a Non-Final Demand Facility has become or will become invalid following a routine assurance check. Alternatively, following routine assurance checking by BSCCo, SVAA may be notified by BSCCo following a decision by BSC Panel that an SVA Non-Final Demand Facility is or should become invalid and have its Declaration withdrawn.

29 An HHDA will not be appointed to any MSID which has been migrated to the MHHS arrangements, and SVAA shall instruct the DAH to stop sending the metered data for such MSIDs.

2730 The SVAA must not instruct the HHDA to cease reporting Metered data for an MSID if that MSID is the subject of an existing Metering System Reporting Notification (D0354) for another BSC process.

2831 The SVAA shall specify the Effective to Settlement Date (J1870) in the D0354 Metering System Reporting Notification.

2932 Nb there is not an equivalent ‘create operator’ process as this is inherent within 2.4, i.e. the SVAA will create an operator role if none exists. Please see Appendix 3.7.1 for guidance.

3033Please see Appendix 3.7.1 for guidance

3134That is, an SVA Non-Final Demand Facility may have more than one Metering System and each Metering System may be registered by a different Registrant. In such a scenario the SVAA should expect to receive a Declaration from each Supplier that is a Registrant of at least one of the Metering Systems at the SVA Non-Final Demand Facility. The SVAA determines whether they are expecting more than one declaration (i.e. a set) by reviewing the numbers of MSIDs declared in a Declaration and comparing it against the Total Number of MSIDs which is also identified in each Declaration.

3235 An HHDA will not be appointed to any MSID which has been migrated to the MHHS arrangements, and SVAA shall instruct the DAH to stop sending the Metered data for such MSIDs.

36The SVAA must not instruct HHDA to cease reporting Metered data for an MSID if that MSID is the subject of an existing Metering System Reporting Notification (D0354) for another BSC process, or if no HHDA is appointed to the MSID.

3337 The SVAA shall specify the Effective to Settlement Date (J1870) in the D0354 Metering System Reporting Notification.

3438 If an Asset has no Generation capacity, no Export Asset Metering System will be required, so only an Import AMSID will be generated for that Asset’s AMSID Pair.

3539 A Qualified AMMOA may be appointed for certain Asset Meters instead of a Qualified MOA in accordance with CoP11.

3640A Qualified AMHHDC may be required to be appointed in addition to a Qualified HHDC for certain Asset Meters in accordance with CoP11 and BSCP601

3741The three types of EMR Declaration are specified in Section 1.16.

3842See section 3.14.1

3943 Where a Supplier or CVA Registrant is not able to withdraw an EMR Declaration using the Self Service Gateway, e.g. if there is a systems outage, they may submit a Declaration including the Effective To Date. All other details in the emailed EMR Declaration must match the details in the Self Service Gateway exactly.

4044 If a Supplier was de-appointed from an MSID, the D0385 from the HHDA in respect of that MSID would include details of the new Supplier and the D0385 would be rejected.

4145 This validation is not applicable where the NETSO has submitted the MSID Pair

4246[CP1599] An HHDA will not be appointed to any MSID which has been migrated to the MHHS arrangements, and SVAA shall instruct the DAH to stop sending the metered data for such MSIDs.

47 Or ABS MSID Pair Delivered Volumes, as appropriate

4348 The Declaration Set ID and Declaration Set EFD should be refreshed whenever updating, withdrawing or re-declaring a Non-Final Demand Facility. For example, if on 1 January an SVA Non-Final Demand Facility Operator declares a Facility for the first time then the Declaration Set ID and Declaration Set EFD should be the same in each Declaration Document submitted on 1 January for the Facility; once declared, should the SVA Non-Final Demand Facility Operator wish to update the declaration details on 28 February then the Declaration Document(s) submitted must consistently use a new Declaration Set ID and Declaration Set EFD.

4449 See footnote 43

4550 See footnote 43

4651 See footnote 43

4752 If a VTP wishes to include AMSID Pair(s) in its Trading Secondary BM Unit(s), then they must also have Qualified as an AMVLP

4853 VTPs must Baseline their Trading Secondary BM Units, but do not have to Baseline individual MSID Pairs.

49 The Supplier or CVA Registrant is not required to submit this form to the SVAA, but they should retain it as supporting evidence for the EMR Declaration, if subject to a BSC Audit or TAPAP check.

50 Not applicable to MHHS MSIDs