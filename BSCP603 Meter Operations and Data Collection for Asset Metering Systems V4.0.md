# BSCP603: Meter Operations and Data Collection for Asset Metering Systems V4.0

> **Source file:** `BSCP603 Meter Operations and Data C.txt`  
> **Effective From Date:** 27/11/2025  
> **Status:** LIVE  
> **Converted:** 2026-10-07. Wording kept verbatim from the source copy-paste; only layout artefacts (page headers/footers, line wraps, website navigation, broken tables) were cleaned up. Notes in *[italic square brackets]* are editorial.

---

BSC Procedure 603 relating to Meter Operations and Data Collection for Asset Metering Systems

1. Reference is made to the Balancing and Settlement Code and, in particular, to the definition of “BSC Procedure” in Section X, Annex X-1 thereof.

2. This is BSC Procedure 603, Version 4.0 relating to Meter Operations and Data Collection for Asset Metering Systems.

3. This BSC Procedure is effective from 27 November 2025.

4. This BSC Procedure has been approved by the BSC Panel or its relevant delegated Panel Committee(s).

## 1 Introduction

### 1.1 Purpose and Scope of the Procedure

The purpose of this Balancing and Settlement Code Procedure (BSCP) is to set out the processes for use by the agents appointed by the Registrant -Asset Metering Virtual Lead Party (AMVLP) or Supplier - for all Asset Metering Systems registered either with the Supplier Volume Allocation Agent (SVAA) or in their Lead Party Asset Meter Register (LPAMR):

For the Half Hourly Data Collector (HHDC) and, where appointed, the Asset Metering Half Hourly Data Collector (AMHHDC) and to carry out the work for data collection (including data retrieval and data processing); and

For Supplier Volume Allocation (SVA) Meter Operator Agent (SVA MOA) or, where appointed, the Asset Metering Meter Operator Agent (AMMOA) and to carry out the work for Meter operations (including, appointment changes, market data activities, connections, disconnections, reconfiguration or changes and where required proving (of Asset Metering Systems)).

For Asset Metering Systems, each Metering System is assigned a unique Asset Metering System Identifier (AMSID). This is for Asset Metering Systems with Asset Metering Equipment.

This BSCP describes the key interfaces and timetables for sending appropriate Asset Metering System data to/from the associated HHDC, associated AMHHDC, associated AMMOA, and associated SVA MOA on behalf of the associated AMVLP or Supplier. In this BSCP, the “associated” agent is the agent for the relevant Asset Metering System for the time being appointed by the associated AMVLP or Supplier. It also describes the key interfaces and timetables for the HHDC sending appropriate Asset Metering Systems data values to the SVAA or to the AMVLP (for Asset Metering Systems registered in LPAMR).

In this BSCP, any reference to “Meter Technical Details” means all the relevant information about Asset Metering Equipment required by the appropriate Data Collector, AMVLP, Supplier or AMMOA/ SVA MOA) to carry out their duties. For the avoidance of doubt this includes, but is not limited to, the D0268 (Half Hourly Meter Technical Details) item listed in Data Interface flows.

This BSCP contains guidance on the completion of an ‘Asset Metering Complex Site Supplementary Information Form’ for the D0268 ‘Half Hourly Meter Technical Details’ data flow where the Asset Metering System is deemed to be at a Complex Site. This is where a fixed multiplier is to be applied to Metered data and is not used for Asset Differencing. Asset Differencing is the responsibility of the AMVLP or Supplier and is completed at the time of registration. For the avoidance of doubt Asset Metering Systems registered in LPAMR are not eligible for Asset Differencing.

### 1.2 Main Users of Procedure and their Responsibilities

This BSCP should be used by AMVLPs, Suppliers and their Agent(s) (including SVA MOAs, AMMOAs, HHDCs and AMHHDCs) and the SVA Agent (SVAA).

Asset Metering Agents using this BSCP shall be appropriately Qualified in Asset Metering.

The SVA MOAs, AMMOAs, HHDCs and AMHHDCs shall perform the responsibilities and obligations set out in this BSCP for an Asset Metering System for all Settlement Days for which the SVA MOA or AMMOA, HHDC and, where applicable, AMHHDC is appointed by the AMVLP or Supplier for Asset Metering Systems registered either with the SVAA or in LPAMR.

The HHDC and AMHHDC shall use Qualified systems and processes so approved in accordance with BSCP537 and the Self-Assessment Document in carrying out the collection of data from Asset Metering Equipment; and for the purposes of collecting data have protocols for every Asset Meter Type for which it is responsible for data retrieval.

Where the same Asset Metering Equipment is being utilised for the measurement of the Import and/or Export Energy for more than one AMSID at a site, the AMVLP or Supplier shall ensure that the same SVA MOA or AMMOA, HHDC and/or AMHHDC is appointed for all the AMSIDs involved to comply with the requirements of the BSC.

In the case where the SVA MOA, AMMOA, HHDC or AMHHDC cannot complete the required processes in this BSCP, this shall be reported to the AMVLP or Supplier and the AMVLP or Supplier shall resolve as appropriate.

In Asset Metering, either the SVAA or the AMVLP (in the case of Assets located either behind Boundary Point Metering which cannot record UTC Period Level Consumption for use in Settlement or behind NHH Boundary Point Metering Systems) will be managing the registration of Assets and creation and issuing of related AMSIDs.

The HHDC’s and AMHHDC’s systems shall be set in accordance with Co-ordinated Universal Time (UTC) at least once every day.

On change of HHDC and / or AMHHDC, the HHDC and / or AMHHDC shall retain responsibility for data collected for all Settlement Days that they were appointed by the AMVLP or Supplier for an Asset Metering System either with the SVAA or in LPAMR.

For each Asset Metering System the AMHHDC is appointed to, the AMHHDC shall send Asset Metering System Half Hourly Metered Data to the HHDC in kWh and in clocktime.

For each Asset Metering System the HHDC is appointed to, the HHDC shall send Asset Metering System Half Hourly Metered Data to the SVAA in kWh and in clocktime.

Where the HHDC has not received data in sufficient time to enable it to fulfil its obligations as HHDC, it shall request from the AMVLP, Supplier or its agent that the data that has not been received be supplied forthwith.

The HHDC and, where appointed, the AMHHDC, shall prepare and maintain plans that will enable the AMVLP’s or Supplier’s obligations under the Code to continue to be met notwithstanding the expiry or termination of the HHDC’s, or AMHHDC’s appointment as the HHDC or AMHHDC. The plans, which the HHDC, or AMHHDC, undertakes to implement on any such expiry or termination, will include the transfer of data and other information to an incoming HHDC or AMHHDC appointed by the AMVLP or Supplier in accordance with section 2.1.4, 2.1.5, 2.1.6, 2.1.7, 2.1.8, 2.1.9, 2.1.10, 2.1.11 and 2.1.12 of this BSCP.

On expiry or termination of the HHDC’s, or AMHHDC’s, appointment as HHDC, or AMHHDC, in respect of an Asset Metering System the outgoing HHDC, or AMHHDC, shall continue to retain data and support the Trading Disputes process, as specified in Appendix 3.12, for all Settlement Days they were appointed by the associated AMVLP or Supplier either with the SVAA on in LPAMR.

The HHDC and AMHHDC shall maintain and use records (as updated from time to time) of the Meter Technical Details (MTD), including energisation status received from the SVA MOA or AMMOA for each Meter and communication System comprising each Asset Metering System for which it is responsible, together with access and site location details in respect of all such Asset Metering Systems.

The HHDC’s and AMHHDC’s system shall be capable of receiving, processing and transmitting all required data accurately and within the timescales agreed by the Panel and AMVLPs or Suppliers and shall be capable of supporting Metered data (processed and unprocessed) and associated standing data for all Asset Metering AMSIDs for which the HHDC and AMHHDC is appointed (with allowance for growth) for the retention periods specified.

The HHDC must only provide AMVLPs or Suppliers with data relating to AMSIDs against which the AMVLPs or Suppliers are contracted with the HHDC.

The AMHHDC must only provide HHDCs with data relating to AMSIDs against which the AMHHDCs and the HHDCs are contracted with the AMVLP or Supplier.

### 1.3 Use of the Procedure

The remaining sections in this document are:

Section 2 - Interface and Timetable Information for Asset Metering Systems: this section defines in more detail the requirements of each business process. In addition, there may be references to ‘D-flows’ (EMAR Market Messages) and ‘P-flows’ (BSC SVA Data Catalogue data flows) in the ‘Information Required’ column.

Section 3 - Appendices: this section contains supporting information.

Where Energy Market Architecture Repository (EMAR) Market Messages (“D-flows”) are referenced, these shall normally be sent over the Data Transfer Network (DTN). Where agreed between the relevant parties or where this is not possible, another method of transfer shall be agreed between the relevant parties, and the information transferred shall have the same content and format as it would if being transferred using the DTN.

AMHHDCs will not be recognised by the DTN, so should send D0390 data to HHDCs using an alternative method agreed with the HHDC.

AMMOAs will not be recognised by the DTN, so should send flows to AMVLPs, Suppliers, HHDCs, AMHHDCs and other AMMOAs/SVA MOAs using an alternative method agreed between the relevant parties.

### 1.4 Balancing and Settlement Code Provision

This BSC Procedure has been produced in accordance with the provisions of the Balancing and Settlement Code (BSC). In the event of an inconsistency between the provisions of this BSC Procedure and the Code, the provisions of the Code shall prevail.

Meter Operators

For Asset Metering Systems a MOA (SVA MOA or AMMOA) is required to:

be subject to the Qualification Requirements of Section J applicable to an AMMOA or to the functions of a AMMOA (Section J 2.1.2(a)) or in the case of an SVA MOA the equivalent requirements in the Retail Energy Code;

install, commission, test, maintain, rectify faults and provide a sealing service in respect of Asset Metering Equipment (including if applicable associated Communications Equipment), in accordance with any relevant BSC Procedures and Codes of Practice (Section L 1.2.3A); and

maintain Meter Technical Details and to provide such Details, in accordance with Section L, to the relevant HHDC, AMHHDC, AMVLP or Supplier to enable such Data Collector to read and process data in accordance with the BSC and all relevant Code Subsidiary Documents (Section S2.2.1(b) and (c)).

Data Collectors

The requirements of HHDCs under the Code can be found in BSC Sections J ‘Party Agents’ and S ‘Supplier Volume Allocation’. An overview of these requirements is as follows:

The functions of a HHDC are defined in BSC Section J as follows: to retrieve, validate and process Metering data from Half Hourly Meters and Equivalent Meters in respect of Asset Metering Equipment in accordance with the provisions of Section S.

HHDCs are subject to the Qualification Requirements of Section J.

The principal functions of a HHDC for Asset Metering Systems are defined in S2.3.1 as (only items related to Asset Metering Systems included):

to collect Asset Metering System Metered data;

to validate data and provide reports;

to enter validated Metered data into the relevant data collection System;

to maintain relevant standing data;

to undertake Meter Advance Reconciliation to reconcile half hourly energy values with Meter advances;

to sum register level data to produce Asset Metering System level data (where applicable);

for an AMHHDC, to provide Asset Metering System level data to the relevant HHDC; and

with the exception of AMHHDCs, to provide Asset Metering System level data either to SVAA or to the AMVLP.

### 1.5 Associated BSC Procedures

| BSC Procedure | Title |
|---|---|
| BSCP01 | Overview of Trading Arrangements |
| BSCP11 | Trading Disputes |
| BSCP32 | Metering Dispensations |
| BSCP508 | Supplier Volume Allocation Agent |
| BSCP537 | Qualification Process for SVA Parties, SVA Party Agents, Asset Metering Agents and CVA MOAs. |
| BSCP602 | SVA Metering System & Asset Metering System Register |
| BSCP607 | Lead Party Asset Meter Register and Secondary BM Unit Asset Volumes |

### 1.6 Acronyms and Definitions

#### 1.6.1 Acronyms

The terms used in this BSC Procedure are defined as follows.

| Acronym | Expression |
|---|---|
| AMHHDC | Asset Metering Half Hourly Data Collector |
| AMMOA | Asset Metering Meter Operator Agent |
| AMSID | Asset Metering System Identifier |
| AMVLP | Asset Metering Virtual Lead Party |
| BSC | Balancing and Settlement Code |
| BSCP | BSC Procedure |
| CoP | Code of Practice |
| CT | Current Transformer |
| DC | Data Collector |
| DTC | Data Transfer Catalogue |
| DTN | Data Transfer Network |
| HH | Half Hourly |
| HHDC | Half Hourly Data Collector |
| HHU | Hand Held Unit |
| Id | Identifier |
| kV | Kilo Volt |
| kWh | Kilowatt hour |
| LPAMR | Lead Party Asset Meter Register |
| MAR | Meter Advance Reconciliation |
| MOA | Meter Operator Agent1 |
| MTD | Meter Technical Details |
| SMRS | Supplier Meter Registration System |
| SVA | Supplier Volume Allocation |
| SVAA | Supplier Volume Allocation Agent |
| SVA MOA | SVA Meter Operator Agent |
| UTC | Co-ordinated Universal Time |
| VT | Voltage Transformer |
| WD | Working Day |
| Wh | Watt hour |

#### 1.6.2 Definitions

Full definitions of the above acronyms are, where appropriate, included in the BSC.

‘Active Power AMSID’ is an AMSID with a Measurement Quantity ID equal to Active Import (AI) or Active Export (AE).

‘Complex Site’ is defined for Asset Metering Systems under Appendix 3.9 ‘Guide to Asset Metering Complex Sites’.

‘de-energisation’ as defined for an Asset Metering System means in relation to any Asset (or the Plant or Apparatus connected to any Asset at such a point) the movement of any isolator, breaker or switch or the removal of any fuse whereby no electricity can flow at such point to and from an Asset; and "de-energised" shall be construed accordingly.

‘Manually Intervened (with regard to proving tests)’ is defined under Appendix 3.6 ‘Proving of Half Hourly Metering Systems’.

‘AMHHDC’ is a role limited to Asset Metering Systems only and its Systems and processes are so approved in accordance with BSCP537. The AMHHDC shall have completed the BSCP601 ‘Metering Protocol Approval and Compliance Testing’ process and is on the CoP Compliance and Protocol Approval list (https://www.elexon.co.uk/bsc-and-codes/bsc-related-documents/codes-of-practice/codes-practice-compliance-protocol-approvals/) for the relevant Asset Meter Type, retrieve data from an Asset Metering System and pass this on to an HHDC.

‘AMMOA’ can act as an agent of the AMVLP or Supplier for “whole current” Asset Metering Type 4 and 5 Asset Metering Systems, who is responsible to install, commission, test and maintain, rectify faults and provide a sealing service in respect of Asset Metering Equipment (including, if applicable, associated Communications Equipment) in accordance with the circumstances allowed under this BSCP (except to the extent that the relevant Code of Practice requires the Equipment Owner to perform such activities).

‘AMVLP’ is a role limited to Virtual Lead Parties using Asset Metering Systems only and its Systems and processes are so approved in accordance with BSCP537. Where an AMVLP2 is the Registrant of an Asset Metering System, it is responsible for appointing Asset Metering agents and registering these details with the SVAA and managing the performance of its appointed agents and for monitoring the completion of business processes that it has initiated.

### 1.7 Meter Operator Agent Obligations

General Obligations

##### 1.7.1.1 Systems and Processes

The AMMOA shall use systems and processes so approved in accordance with BSCP537 in the operation of Asset Metering Equipment. These systems and processes must also comply with all other applicable requirements set out in the BSC and the BSC Procedures. OR

The SVA MOA shall use Systems and processes so approved in accordance with the qualification requirements for a Half Hourly SVA MOA under the Retail Energy Code for Half Hourly SVA Metering Systems.

b) Controls to ensure that input, processing and output are valid may include the use of software validation checks and exception reporting to identify problems.

##### 1.7.1.2 Recording Devices

a) The MOA shall ensure that the import or export of electrical energy by every Asset Metering System for which it is responsible is accurately recorded by Metering, time control and load switching devices calibrated, installed and maintained in compliance with the relevant Code of Practice.

Notification Requirements to the Supplier Volume Allocation Agent (SVAA) for Asset Metering Equipment

This section only applies in respect of Assets located behind Boundary Point Metering which records UTC Period Level Consumption for use in Settlement. Other Assets can be registered in LPAMR in accordance with BSCP607.

Meter Information

This section applies to Asset Meters registered in the Asset Metering System Register only and not those registered in LPAMR.

a) The AMVLP or Supplier shall notify the Supplier Volume Allocation Agent (SVAA) of the following items (upon installation or following any subsequent changes to the items):

Asset Metering System ID;

Asset Meter Serial Number;

Asset Meter Type;

Date of Asset Meter Installation; and

Date of Asset Meter Removal.

This will be done by sending a P0303 ‘Asset Meter Registration’ flow.

b) The SVAA shall validate the P0303 ‘Asset Meter Registration’ received and shall send a response to the AMVLP or Supplier:

P0304 ‘Rejection of Asset Meter Registration’; or

P0305 ‘Confirmation of Asset Meter Registration’.

Registration Obligations

##### 1.7.3.1 Recording of Details

a) The SVA MOA or AMMOA shall record sufficient details, received from its associated AMVLP or Supplier, of its appointment in respect of an Asset Metering System to enable the SVA MOA or AMMOA to perform its functions as SVA MOA or AMMOA. These details shall include the relevant Asset Metering System Number and the Identifiers for the associated HHDC and, where applicable, associated AMHHDC, and the associated AMVLP’s or Supplier’s Metering requirements.

b) On appointment to an Asset Metering System, and where the same Asset Meter is to be used, the incoming SVA MOA or AMMOA shall request the transfer of data and other information, in accordance with Section 1.7.3.2 c), from the outgoing SVA MOA or AMMOA to enable such incoming SVA MOA or AMMOA to assume responsibility for the Asset Metering System.

##### 1.7.3.2 Termination of Appointment of HH Meter Operator Agent or Asset Metering Meter Operator Agent

a) The SVA MOA or AMMOA shall prepare and maintain plans that will enable its associated AMVLP’s or Supplier’s obligations under the BSC to continue to be met notwithstanding the expiry or termination of the SVA MOA’s or AMMOA’s appointment as the SVA MOA or AMMOA. The plans, which the SVA MOA or AMMOA undertakes to implement on any such expiry or termination, will include the immediate transfer of data and other information to an incoming SVA MOA or AMMOA appointed by the associated AMVLP or Supplier or to the Panel.

b) In the event of a Change of SVA MOA or AMMOA3 in respect of an Asset Metering System, and where the same Asset Meter is to be used, the outgoing SVA MOA or AMMOA shall transfer the data and other information, as specified in Section 1.7.3.2 c), in accordance with the timescales and processes specified in the relevant BSC Procedures, to the incoming SVA MOA or AMMOA. This shall be done when requested by the incoming SVA MOA or AMMOA and is not dependent on receipt of notification of de-appointment. The outgoing SVA MOA or AMMOA shall cooperate with the incoming SVA MOA or AMMOA, and any subsequent incoming SVA MOA or AMMOA, to correct any errors relating to data associated with the outgoing SVA MOA’s or AMMOA’s period of appointment. In all cases the incoming SVA MOA or AMMOA will retain an auditable record of any changes to the data.

Where information has not been provided to the outgoing SVA MOA or AMMOA then the incoming and outgoing SVA MOA(s) or AMMOA(s), along with the AMVLP or Supplier shall work together to resolve the issue.

c) Data and other information to be transferred shall include Meter Technical Details including that relating to the associated Communications Equipment as appropriate, commissioning data, mapping data and certification and/or calibration details.

d) On expiry or termination of the SVA MOA’s or AMMOA’S appointment in respect of an Asset Metering System, and where the same Asset Meter is to be used, the outgoing SVA MOA’s or AMMOA’s obligations under Appendix 3.12.2 and 3.12.3 shall survive.

Metering Obligations

##### 1.7.4.1 Energisation of Meters

a) The SVA MOA or AMMOA shall only energise an Asset Metering System if requested to do so by its associated AMVLP or Supplier.

b) The SVA MOA or AMMOA shall as soon as reasonably practicable inform its associated AMVLP or Supplier and the associated HHDC and if applicable AMHHDC of any change in the energisation status of any Asset Metering System to which it has been appointed.

##### 1.7.4.2 Installation, Removal and Re-programming of Meters

a) The SVA MOA or AMMOA shall maintain records and comply with systems and processes so approved in accordance with BSCP537 to commission, recommission, remove, replace or reprogram Asset Meters, and shall inform its associated AMVLP or Supplier and its associated HHDC, and if applicable AMHHDC, of the nature and date of any related work carried out within such time as shall allow its associated HHDC, and if applicable AMHHDC, to carry out its obligations to ensure that correct data is taken into Initial Volume Allocation Runs.

b) The SVA MOA or AMMOA shall seal and reseal Asset Metering Equipment in accordance with Section 3.11.

c) The SVA MOA or AMMOA shall request Site Technical Details from the AMVLP or Supplier in the case of Asset Metering Equipment, in accordance with this BSCP.

#### 1.7.5 Interface to Other Asset Metering Agents and AMVLPs or Suppliers

1.7.5.1 Information to HHDCs AMHHDCs AMVLPs and Suppliers.

a) Upon any change of Meter Technical Details or any change of associated HHDC, and if applicable AMHHDC, or upon the SVA MOA’s or AMMOA’s appointment in respect of an Asset Metering System the SVA MOA or AMMOA shall give Meter Technical Details and access details of the Asset Metering System and its energisation status at feeder level to its associated HHDC, and if applicable AMHHDC.

b) Except in an emergency, the SVA MOA or AMMOA shall give its associated HHDC, or associated AMHHDC sufficient notice of the installation, repair, removal, reprogramming, energisation or de-energisation of any Asset Meter associated with an Asset Metering System for which the associated HHDC, or associated AMHHDC, is responsible to enable the associated HHDC, or associated AMHHDC, as the case may be to recover the data required for Settlement using its normal method of data collection.

c) The SVA MOA or AMMOA shall provide initial / final Asset Meter readings to its associated HHDC, and if applicable AMHHDC, following installation, removal, reprogramming, energisation, de-energisation or replacement of an Asset Meter, by the SVA MOA or AMMOA, as appropriate and in accordance with this BSCP.

d) Where the SVA MOA or AMMOA has collected data from an Asset Metering System other than for the circumstances described in Section 1.7.5.1 c) the Metered Data shall be provided to the associated HHDC or associated AMHHDC via the associated AMVLP or Supplier as applicable.

Meter Fault Reporting

a) Upon the SVA MOA or AMMOA being notified by any person or discovering that any Asset Meter, for which the SVA MOA or AMMOA is responsible is potentially recording incorrect data, the SVA MOA or AMMOA shall investigate and rectify the problem and notify its associated AMVLP or Supplier as applicable and its associated HHDC, or if applicable AMHHDC, of the nature of the fault and the date and time at which it was rectified.

b) The SVA MOA or AMMOA shall report Asset Meter faults to its associated AMVLP or Supplier as applicable and its associated HHDC, or if applicable AMHHDC, and advise the associated HHDC, or if applicable AMHHDC, as to the period covered by the fault and, for Half Hourly Meters Asset Meters, as to how to estimate Half Hourly consumption correctly.

c) The SVA MOA or AMMOA shall separately identify Asset Meter faults, affecting data quality and those not affecting data quality and shall record the date on which each fault was reported and the date on which each fault was cleared. For this purpose a fault affecting data quality shall be treated as cleared when the relevant Asset Metering System, once again records in compliance with the relevant Code of Practice.

#### 1.7.6 Service Levels

The SVA MOA or AMMOA shall perform the services to be performed by it as SVA MOA or AMMOA pursuant to this BSCP to standards which shall be at least as good as those specified in Appendix 3.10.

## 2 Interface and Timetable Information

### 2.1 Registration Activities

#### 2.1.1 Installation of a New Asset Metering System

Where an AMVLP or Supplier has requested that an Asset Metering System be installed for an AMSID. For Asset Metering Types4 1, 2 and 3 the Meter Operator activities shall be done by a SVA MOA; for Asset Metering Types 4 and 5 the AMVLP or Supplier can choose to appoint a SVA MOA or an AMMOA.

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.1.1.1 | As required | AMVLP or Supplier appoints a Meter Operator and HHDC and, if applicable, an AMHHDC | AMVLP<br>or<br>Supplier | SVA MOA<br>or<br>AMMOA<br>HHDC | and where applicable<br>AMHHDC<br>D0155 Notification of Meter Operator or Data Collector Appointment and Terms<br>P0314 Notification of AMHHDC | Electronic or other method, as agreed. |
| 2.1.1.2 | If appointment rejected and within 5 WD of 2.1.1.1 | Send notification of rejection of appointment including the reason why the request has been rejected.<br>Where HHDC and AMHHDC required and one of them rejects the appointment the AMVLP or Supplier must resolve the issue and appoint all Asset Metering Agent(s) prior to step 2.1.1.4)<br>(Go to 2.1.1.1 if required) | SVA MOA<br>or<br>AMMOA | HHDC<br>or<br>AMHHDC<br>AMVLP<br>or<br>Supplier | D0261 Rejection of Agent Appointment | Electronic or other method, as agreed. |
| 2.1.1.3 | If appointment accepted and within 5 WD of 2.1.1.1 | Send notification of acceptance of appointment. | SVA MOA<br>or<br>AMMOA | HHDC<br>or<br>AMHHDC<br>AMVLP<br>or<br>Supplier | D0011 Agreement of Contractual Terms | Electronic or other method, as agreed. |
| 2.1.1.4 | On appointment of agents and within 5 WD of 2.1.1.3 | Send notification of appointed agents | AMVLP<br>or<br>Supplier | SVA MOA<br>or<br>AMMOA<br>HHDC | and where applicable<br>AMHHDC<br>D0148 Notification of Change to Other Parties<br>P0314 Notification of AMHHDC<br>D0302 Notification of Customer Details. | Electronic or other method, as agreed. |
| 2.1.1.5 | Following 2.1.1.4 and upon receipt of Asset Metering System details | Record Asset Metering System details | HHDC | AMHHDC (if applicable) | Sufficient details of HHDC’s and AMHHDC’s appointment in respect of an Asset Metering System to enable the HHDC and AMHHDC to perform its HHDC and AMHHDC functions.<br>These details shall include the relevant Asset Meter AMSID and the Identifiers for the SVA MOA or AMMOA.<br>The details shall also include the Settlement Days for which the HHDC and AMHHDC are appointed.<br>Internal Process. |  |
| 2.1.1.6 | Following 2.1.1.3 and at least 10 WD before 2.1.1.105 | Request installation, Commissioning and energisation of Asset Metering System | AMVLP<br>or<br>Supplier | SVA MOA<br>or<br>AMMOA | D0142 Request for Installation or Change to a Metering System Functionality or the Removal of All Meters | Electronic or other method, as agreed. |
| 2.1.1.7 | Within 2 WD of 2.1.1.6 | Request Site Technical Details.<br>Optional for SVA MOA or AMMOA to request – if not requested continue to 2.1.1.10 | SVA MOA<br>or<br>AMMOA | AMVLP<br>or<br>Supplier | D0170 Request for Metering System Related Details | Electronic or other method, as agreed. |
| 2.1.1.8 | If request for Site Technical Details rejected and within 5 WD of 2.1.1.7 | Send Rejection response for request for Site Technical Details including the reasons why the request has been rejected. | AMVLP<br>or<br>Supplier | SVA MOA<br>or<br>AMMOA | P0319 ‘Rejection Response for Request for Asset Metering System Site Technical Details’ | Electronic or other method, as agreed. |
| 2.1.1.9 | Within 5 WD of 2.1.1.7 | Send Site Technical Details | AMVLP6<br>or<br>Supplier | SVA MOA<br>or<br>AMMOA | P0315 Provision of Site Technical Details | Electronic or other method, as agreed. |
| 2.1.1.10 | On the date requested or agreed in 2.1.1.6 | Install Asset Metering System in accordance with Code of Practice Eleven<br>If requested energise Asset Metering System and note initial Asset Meter register reading (if applicable). | SVA MOA<br>or<br>AMMOA |  |  | Internal Process |
| 2.1.1.11 | Following 2.1.1.10 | Commission Asset Metering System in accordance with Code of Practice Eleven and sections 2.1.2 | SVA MOA<br>or<br>AMMOA |  |  | Internal Process |
| 2.1.1.12 | If Asset Metering System cannot be installed or energised, as soon as possible and within 5 WD of 2.1.1.10 | Inform AMVLP | SVA MOA<br>or<br>AMMOA | AMVLP<br>or<br>Supplier | D0221 Notification of Failure to Install or Energise Metering System | Electronic or other method, as agreed. |
| 2.1.1.13 | Within 5 WD of 2.1.1.10 or within 2 WD of 2.1.1.17 (as applicable) | Send energisation status, Meter Technical Details and initial Asset Meter register reading (if applicable) | SVA MOA<br>or<br>AMMOA | AMVLP<br>or<br>Supplier<br>HHDC<br>and<br>AMHHDC (if applicable) | D0010 Meter Readings<br>D0268 Half Hourly Meter Technical Details<br>If site is Complex, send Asset Metering Complex Site Supplementary Information Form. Refer to Appendix 3.9 Guide to Asset Metering Complex Sites; | Electronic or other method, as agreed. |
| 2.1.1.14 | Where appropriate, from HHDC or AMHHDC appointment start date | Collect Asset Metered Data | HHDC | AMHHDC (if applicable) | Refer to Section 2.3.1 or 2.3.2 as applicable | Internal Process |
| 2.1.1.15 | Within 5 WD of 2.1.1.10 and at same time as 2.1.1.13 | This step does not apply for Asset Meters registered in LPAMR.<br>Send the relevant Asset Meter information. | AMVLP<br>or<br>Supplier | SVAA<br>HHDC<br>and<br>AMHHDC (if applicable) | P0303 Asset Meter Registration | Electronic or other method, as agreed. |
| 2.1.1.16 | Immediately following 2.1.1.15 or 2.1.1.17 | Perform validation checks and send response<br>If response is “Accepted”, proceed to 2.1.1.18, otherwise proceed to 2.1.1.17. | SVAA | AMVLP<br>or<br>Supplier | P0304 Rejection of Asset Meter Registration; or<br>P0305 Confirmation of Asset Meter Registration | Electronic or other method, as agreed. |
| 2.1.1.17 | Within 5 WD of 2.1.1.16 | This step does not apply for Asset Meters registered in LPAMR.<br>Where the rejection is of a type the AMVLP or Supplier can resolve without involving other industry parties, send a corrected flow.<br>Proceed to 2.1.1.16<br>If the AMVLP or Supplier needs to involve other industry parties to resolve the issue, then reasonable endeavours should apply. Notify SVA MOA or AMMOA of rejection reasons and request new D0268.<br>Proceed to 2.1.1.13 | AMVLP<br>or<br>Supplier | AMVLP<br>or<br>Supplier<br>SVAA<br>HHDC<br>and<br>AMHHDC (if applicable)<br>SVA MOA<br>or<br>AMMOA | P0303 Asset Meter Registration<br>P0304 Rejection of Asset Meter Registration<br>Electronic or other method, as agreed. | Electronic or other method, as agreed. |
| 2.1.1.18 | In accordance with timescales in Appendix 3.6.5 | Carry out a Proving Test on the Asset Metering System in accordance with Section 2.5, Appendix 3.6 and Code of Practice Eleven. | SVA MOA<br>or<br>AMMOA | HHDC<br>AMHHDC (if applicable) | Refer to Appendix 3.6 | Internal Process |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

#### 2.1.2 Commissioning of a New Asset Metering System

Where an AMVLP or Supplier has requested that an Asset Metering System be installed for an AMSID for Asset Metering Types4 1, 2 and 3 the Meter Operator activities shall be done by a SVA MOA; for Asset Metering Types 4 and 5 the AMVLP or Supplier can choose to appoint a SVA MOA or an AMMOA.

Where the SVA MOA, AMMOA or AMVLP or Supplier is not the Equipment Owner for the Measurement Transformers (i.e. Current Transformers and Voltage Transformers) it will be the Equipment Owner who shall be responsible for ensuring the Commissioning requirements are performed on its Metering Equipment up to and including the Testing Facilities, if fitted; where not fitted this will be to the Asset Meter or a point where the Asset Meter can be isolated from the Measurement Transformers.

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.1.2.1 | On the date requested or agreed in 2.1.1.6 but no later than 16 WD after energisation | If the SVA MOA or AMMOA or AMVLP or Supplier does not own the Measurement Transformers then Commission Measurement Transformers in accordance with Code of Practice Eleven.<br>(If not applicable, i.e. SVA MOA or AMMOA or AMVLP or Supplier does own the Measurement Transformers or there are no Measurement Transformers in the Asset Metering System go to 2.1.2.3) | Equipment Owner |  |  | Internal Process |
| 2.1.2.2 | Following 2.1.2.1 and no later than 5 WD of completion of tests in 2.1.2.1 | Send Commissioning information for the Measurement Transformers to the SVA MOA or AMMOA and AMVLP or Supplier. | Equipment Owner | SVA MOA<br>or<br>AMMOA<br>and<br>AMVLP<br>or<br>Supplier | D0383 ‘Notification of Commissioning Information’ | Electronic or other method, as agreed. |
| 2.1.2.3 | On the date requested or agreed in 2.1.1.5 but no later than 32 WD after Energisation | Commission Asset Metering System in accordance with Code of Practice Eleven. | SVA MOA<br>or<br>AMMOA |  |  | Internal Process |
| 2.1.2.4 | Following 2.1.2.3 | If there has been a defect/omission that has prevented Commissioning7. | OR<br>If Commissioning has been completed | SVA MOA<br>or<br>AMMOA | Go to 2.1.2.5<br>OR<br>Go to 2.1.2.8 | Internal Process |
| 2.1.2.5 | At the earliest opportunity but no later than 5 WD of 2.1.2.4 | Inform the AMVLP or Supplier where there is a defect/omission that has prevented Commissioning. | SVA MOA<br>or<br>AMMOA | AMVLP<br>or<br>Supplier | D0384 Notification of Commissioning Status | Electronic or other method, as agreed. |
| 2.1.2.6 | At the earliest opportunity but no later than 65 WD after energisation | Resolve the defect/omission that has prevented Commissioning8.<br>Inform the SVA MOA or AMMOA that the defect/omission that has prevented Commissioning has been resolved. | AMVLP<br>or<br>Supplier | SVA MOA<br>or<br>AMMOA | D0384 Notification of Commissioning Status | Electronic or other method, as agreed. |
| 2.1.2.7 | When defect/omission has been resolved, but no later than 80 WD after energisation | Commission Asset Metering System in accordance with Code of Practice Eleven. | SVA MOA<br>or<br>AMMOA |  |  | Internal Process |
| 2.1.2.8 | Within 5 WD of 2.1.2.3 or 2.1.2.7, as applicable | Inform the AMVLP or Supplier that Commissioning has been completed | SVA MOA<br>or<br>AMMOA | AMVLP<br>or<br>Supplier | D0384 Notification of Commissioning Status | Electronic or other method, as agreed. |
| 2.1.2.9 | Following 2.1.2.8 | Create internal record of Commissioning information | SVA MOA<br>or<br>AMMOA |  | D0383 ‘Notification of Commissioning Information’ | Internal Process |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

#### 2.1.3 Using an Existing Metering System as an Asset Metering System

Where an AMVLP or Supplier has requested that an existing Metering System be used as an Asset Metering System for an AMSID for Asset Metering Types4 1, 2 and 3 the Meter Operator activities shall be done by a SVA MOA; for Asset Metering Types 4and 5 the AMVLP or Supplier can choose to appoint a SVA MOA or an AMMOA.

An existing Asset Metering System is one which has not been used in Settlement but has been used for other purposes, for example the Electricity Market Reform Capacity Market. An existing Metering System must be compliant with Code of Practice Eleven to be used as an Asset Metering System. Where it is not the Asset Metering System may require to be replaced and/or re-commissioned.

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.1.3.1 | As required | AMVLP or Supplier appoints a Meter Operator and HHDC and, if applicable, an AMHHDC | AMVLP<br>or<br>Supplier | SVA MOA<br>or<br>AMMOA<br>HHDC | and where applicable<br>AMHHDC<br>D0155 Notification of Meter Operator or Data Collector Appointment and Terms<br>P0314 Notification of AMHHDC | Electronic or other method, as agreed. |
| 2.1.3.2 | If appointment rejected and within 5 WD of 2.1.3.1 | Send notification of rejection of appointment including the reason why the request has been rejected.<br>Where HHDC and AMHHDC required and one of them rejects the appointment the AMVLP or Supplier must resolve the issue and appoint all Asset Metering Agent(s) prior to step 2.1.3.4)<br>(Go to 2.1.3.1 if required) | SVA MOA<br>or<br>AMMOA | HHDC<br>or<br>AMHHDC<br>AMVLP<br>or<br>Supplier | D0261 Rejection of Agent Appointment | Electronic or other method, as agreed. |
| 2.1.3.3 | If appointment accepted and within 5 WD of 2.1.3.1 | Send notification of acceptance of appointment. | SVA MOA<br>or<br>AMMOA | HHDC<br>or<br>AMHHDC<br>AMVLP<br>or<br>Supplier | D0011 Agreement of Contractual Terms | Electronic or other method, as agreed. |
| 2.1.3.4 | On appointment of agents and within 5 WD of 2.1.3.3 | Send notification of appointed agents | AMVLP<br>or<br>Supplier | SVA MOA<br>or<br>AMMOA<br>HHDC | and where applicable<br>AMHHDC<br>D0148 Notification of Change to Other Parties<br>P0314 Notification of AMHHDC<br>D0302 Notification of Customer Details. | Electronic or other method, as agreed. |
| 2.1.3.5 | Following 2.1.3.4 and upon receipt of Asset Metering System details | Record Asset Metering System details | HHDC | AMHHDC (if applicable) | Sufficient details of HHDC’s and AMHHDC’s appointment in respect of an Asset Metering System to enable the HHDC and AMHHDC to perform its HHDC and AMHHDC functions.<br>These details shall include the relevant Asset Meter AMSID and the Identifiers for the SVA MOA or AMMOA.<br>The details shall also include the Settlement Days for which the HHDC and AMHHDC are appointed.<br>Internal Process. |  |
| 2.1.3.6 | Following 2.1.3.3 and at least 10 WD before 2.1.3.79 | Request confirmation of compliance as an Asset Metering System and if applicable installation, Commissioning and energisation of Asset Metering System | AMVLP10<br>or<br>Supplier | SVA MOA<br>or<br>AMMOA | D0142 Request for Installation or Change to a Metering System Functionality or the Removal of All Meters<br>P0315 Provision of Site Technical Details<br>D0268 Half Hourly Meter Technical Details<br>D0383 ‘Notification of Commissioning Information’<br>If site is Complex, send Asset Metering Complex Site Supplementary Information Form. Refer to Appendix 3.9 Guide to Asset Metering Complex Sites; | Electronic or other method, as agreed. |
| 2.1.3.7 | Following receipt of information in 2.1.3.6 | Determine if Asset Metering System is compliant with Code of Practice Eleven, determine Overall Accuracy of Metering System and Risk to Settlement.<br>Where Asset Metering System compliant continue to 2.1.3.9; or<br>Where Asset Metering System in non-compliant continue to 2.1.3.8 | SVA MOA<br>or<br>AMMOA |  |  | Internal Process |
| 2.1.3.8 | Following 2.1.3.7 | Inform the AMVLP or Supplier that verification checks have been completed and that the Asset Metering System is non-compliant, the reasons for non-compliance must be detailed.<br>If applicable, continue to 2.2.4 where Asset Meter System to be reconfigured or replaced<br>If applicable, continue to 2.1.2 where Asset Metering System to be re-commissioned.<br>END PROCESS | SVA MOA<br>or<br>AMMOA | AMVLP<br>or<br>Supplier | D0384 Notification of Commissioning Status<br>P0318 Metering Non-Compliance Notification | Electronic or other method, as agreed. |
| 2.1.3.9 | Following 2.1.3.7 and within 5 WD of receipt of Site Technical Details in 2.1.3.7 | Send energisation status, Meter Technical Details and initial Asset Meter register reading (if applicable) | SVA MOA<br>or<br>AMMOA | AMVLP<br>or<br>Supplier<br>HHDC<br>and<br>AMHHDC (if applicable) | D0010 Meter Readings<br>D0268 Half Hourly Meter Technical Details<br>If site is Complex, send Asset Metering Complex Site Supplementary Information Form. Refer to Appendix 3.9 Guide to Asset Metering Complex Sites; | Electronic or other method, as agreed. |
| 2.1.3.10 | Where appropriate, from HHDC or AMHHDC appointment start date | Collect Asset Metered Data | HHDC | AMHHDC (if applicable) | Refer to Section 2.3.1 or 2.3.2 as applicable | Internal Process |
| 2.1.3.11 | At same time as 2.1.3.9 | This step does not apply for Asset Meters registered in LPAMR.<br>Send the relevant Asset Meter information. | AMVLP<br>or<br>Supplier | SVAA<br>HHDC<br>and<br>AMHHDC (if applicable) | P0303 Asset Meter Registration | Electronic or other method, as agreed. |
| 2.1.3.12 | Immediately following 2.1.3.11 | Perform validation checks and send response<br>If response is “Accepted”, proceed to 2.1.3.14, otherwise proceed to 2.1.3.13. | SVAA | AMVLP<br>or<br>Supplier | P0304 Rejection of Asset Meter Registration<br>or<br>P0305 Confirmation of Asset Meter Registration | Electronic or other method, as agreed. |
| 2.1.3.13 | Within 5 WD of 2.1.3.12 | This step does not apply for Asset Meters registered in LPAMR.<br>Where the rejection is of a type the AMVLP or Supplier can resolve without involving other industry parties, send a corrected flow.<br>Proceed to 2.1.3.12<br>If the AMVLP or Supplier needs to involve other industry parties to resolve the issue, then reasonable endeavours should apply. Notify MOA of rejection reasons and request new D0268.<br>Proceed to 2.1.3.9 | AMVLP | AMVLP<br>or<br>Supplier<br>SVAA<br>HHDC<br>and<br>AMHHDC (if applicable)<br>SVA MOA<br>or<br>AMMOA | P0303 Asset Meter Registration<br>P0304 Rejection of Asset Meter Registration<br>Electronic or other method, as agreed. | Electronic or other method, as agreed. |
| 2.1.3.14 | In accordance with timescales in Appendix 3.6.5 | Carry out a Proving Test on the Asset Metering System in accordance with Section 2.5, Appendix 3.6 and Code of Practice Eleven. | SVA MOA<br>or<br>AMMOA | HHDC<br>AMHHDC (if applicable) | Refer to Appendix 3.6 | Internal Process |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

#### 2.1.4 Change of AMVLP or Supplier for an Existing Metering System (No Change of Agent)

For Asset Metering Types4 1, 2 and 3 the Meter Operator activities shall be done by a SVA MOA; for Asset Metering Types 4) and 5 the AMVLP or Supplier can choose to appoint a SVA MOA or an AMMOA.

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.1.4.1 | As required | New AMVLP or Supplier notifies the Meter Operator and HHDC, and AMHHDC (if applicable) | New AMVLP<br>or<br>Supplier | SVA MOA<br>or<br>AMMOA<br>HHDC | and where applicable<br>AMHHDC<br>D0155 Notification of Meter Operator or Data Collector Appointment and Terms<br>P0314 Notification of AMHHDC | Electronic or other method, as agreed. |
| 2.1.4.2 | If appointment rejected and within 5 WD of 2.1.4.1 | Send notification of rejection of appointment including the reason why the request has been rejected.<br>Where HHDC and AMHHDC required and one of them rejects the appointment the AMVLP or Supplier must resolve the issue and appoint all Asset Metering Agent(s) prior to step 2.1.4.4)<br>(Go to 2.1.4.1 if required) | SVA MOA<br>or<br>AMMOA | HHDC<br>AMHHDC (if applicable)<br>New AMVLP<br>or<br>Supplier | D0261 Rejection of Agent Appointment | Electronic or other method, as agreed. |
| 2.1.4.3 | If appointment accepted and within 5 WD of 2.1.4.1 | Send notification of acceptance of appointment. | SVA MOA<br>or<br>AMMOA | HHDC<br>AMHHDC (if applicable)<br>New AMVLP<br>or<br>Supplier | D0011 Agreement of Contractual Terms | Electronic or other method, as agreed. |
| 2.1.4.4 | Within 5 WD of notification or by last date of AMVLP or Supplier appointment | Send notification of termination of appointment. | Current AMVLP<br>or<br>Supplier | SVA MOA<br>or<br>AMMOA<br>HHDC<br>AMHHDC (if applicable) | D0151 Termination of Appointment or Contract by Supplier<br>In this instance this is Termination of Appointment or Contract by the Registrant (AMVLP or Supplier) | Electronic or other method, as agreed. |
| 2.1.4.5 | Within 10 WD after the end of HHDC or AMHHDC appointment to old AMVLP or Supplier. | Complete Asset Metered Data collection activities for old AMVLP or Supplier. | HHDC | AMHHDC (if applicable) | Refer to Section 2.3.1 or 2.3.2 as applicable | Internal Process |
| 2.1.4.6 | On appointment of agents and within 5 WD of 2.1.4.3 | Send notification of appointed agents | New AMVLP<br>or<br>Supplier | SVA MOA<br>or<br>AMMOA<br>HHDC<br>and | and where applicable<br>AMHHDC<br>D0148 Notification of Change to Other Parties<br>P0314 Notification of AMHHDC<br>D0302 Notification of Customer Details. | Electronic or other method, as agreed. |
| 2.1.4.7 | Within 1 WD of 2.1.4.6 | Request Meter Technical Details | New AMVLP<br>or<br>Supplier | SVA MOA<br>or<br>AMMOA | D0170 Request for Metering System Related Details | Electronic or other method, as agreed. |
| 2.1.4.8 | Within 5 WD of 2.1.4.7 | Send Meter Technical Details | SVA MOA<br>or<br>AMMOA | New AMVLP<br>or | New Supplier<br>HHDC<br>and<br>AMHHDC (if applicable)<br>D0268 Half Hourly Meter Technical Details<br>If site is Complex, send Asset Metering Complex Site Supplementary Information Form. Refer to Appendix 3.9 Guide to Asset Metering Complex Sites; | Electronic or other method, as agreed. |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

#### 2.1.5 Change of SVA MOA or AMMOA (No Change of Metering System or Change of AMVLP or Supplier)

For Asset Metering Types4 1, 2 and 3 the Meter Operator activities shall be done by a SVA MOA; for Asset Metering Types 4 and 5 the AMVLP or Supplier can choose to appoint a SVA MOA or an AMMOA.

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.1.5.1 | As required | AMVLP or Supplier appoints a SVA MOA or AMMOA | AMVLP<br>or<br>Supplier | New SVA MOA<br>or<br>New AMMOA | D0155 Notification of Meter Operator or Data Collector Appointment and Terms | Electronic or other method, as agreed. |
| 2.1.5.2 | If appointment rejected and within 5 WD of 2.1.5.1 | Send notification of rejection of appointment including the reason why the request has been rejected.<br>(Go to 2.1.5.1 if required) | New SVA MOA<br>or<br>New AMMOA | AMVLP<br>or<br>Supplier | D0261 Rejection of Agent Appointment | Electronic or other method, as agreed. |
| 2.1.5.3 | If appointment accepted and within 5 WD of 2.1.5.1 | Send notification of acceptance of appointment. | New SVA MOA<br>or<br>New AMMOA | AMVLP<br>or<br>Supplier | D0011 Agreement of Contractual Terms | Electronic or other method, as agreed. |
| 2.1.5.4 | Within 5 WD of 2.1.5.3 | Send de-appointment | AMVLP<br>or<br>Supplier | Current SVA MOA<br>or<br>Current AMMOA | D0151 Termination of Appointment or Contract by Supplier | Electronic or other method, as agreed. |
| 2.1.5.5 | If de-appointment rejected and within 5 WD of 2.1.5.4 | Send notification of rejection of de-appointment. | Current SVA MOA<br>or<br>Current AMMOA | AMVLP<br>or<br>Supplier | D0261 Rejection of Agent Appointment | Electronic or other method, as agreed. |
| 2.1.5.6 | On appointment of new SVA MOA / AMMOA and within 5 WD of 2.1.5.4 | Send notification of SVA MOA / AMMOA appointment / de-appointment | AMVLP<br>or<br>Supplier | New SVA MOA<br>or<br>New AMMOA<br>HHDC<br>and | and where applicable<br>AMHHDC<br>D0148 Notification of Change to Other Parties<br>P0314 Notification of AMHHDC<br>D0302 Notification of Customer Details. | Electronic or other method, as agreed. |
| 2.1.5.7 | Within 2 WD of 2.1.5.6 | Instruct current SVA MOA / AMMOA to send Meter Technical Details to new SVA MOA/ AMMOA | AMVLP<br>or<br>Supplier | Current SVA MOA<br>or<br>Current AMMOA | D0170 Request for Metering System Related Details | Electronic or other method, as agreed. |
| 2.1.5.8 | Within 5 WD of 2.1.5.7 | Send Meter Technical Details. | Current SVA MOA<br>or<br>Current AMMOA | New SVA MOA<br>or<br>New AMMOA | D0268 Half Hourly Meter Technical Details<br>If site is Complex, send Asset Metering Complex Site Supplementary Information Form. Refer to Appendix 3.9 Guide to Asset Metering Complex Sites; | Electronic or other method, as agreed. |
| 2.1.5.9 | Following 2.1.5.8 | Send Commissioning information | Current SVA MOA<br>or<br>Current AMMOA | New SVA MOA<br>or<br>New AMMOA | D0383 ‘Notification of Commissioning Information’<br>D0384 Notification of Commissioning Status | Electronic or other method, as agreed. |
| 2.1.5.10 | Within 5 WD of 2.1.5.8 | Send Meter Technical Details | New SVA MOA<br>or<br>New AMMOA | AMVLP<br>or<br>Supplier<br>HHDC<br>and<br>AMHHDC (if applicable) | D0268 Half Hourly Meter Technical Details<br>If site is Complex, send Asset Metering Complex Site Supplementary Information Form. Refer to Appendix 3.9 Guide to Asset Metering Complex Sites; | Electronic or other method, as agreed. |
| 2.1.5.11 | Following 2.1.5.10 | Send Commissioning information | New SVA MOA<br>or<br>New AMMOA | AMVLP<br>or<br>Supplier | D0384 Notification of Commissioning Status | Electronic or other method, as agreed. |
| 2.1.5.12 | Following 2.1.5.11 and in accordance with timescales in Appendix 3.6.5 | Prove Asset Metering System in accordance with Section 2.5, Appendix 3.6 and Code of Practice Eleven. | New SVA MOA<br>or<br>New AMMOA | HHDC<br>AMHHDC (if applicable) | Refer to Appendix 3.6 | Electronic or other method, as agreed. |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

#### 2.1.6 Concurrent Change of AMVLP or Supplier and SVA MOA or AMMOA (No change to Asset Metering System)

For Asset Metering Types4 1, 2 and 3 the Meter Operator activities shall be done by a SVA MOA; for Asset Metering Types 4 and 5 the AMVLP or Supplier can choose to appoint a SVA MOA or an AMMOA.

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.1.6.1 | As required | AMVLP or Supplier appoints a SVA MOA or an AMMOA | New AMVLP<br>or<br>Supplier | New SVA MOA<br>or<br>New AMMOA | D0155 Notification of Meter Operator or Data Collector Appointment and Terms | Electronic or other method, as agreed. |
| 2.1.6.2 | If appointment rejected and within 5 WD of 2.1.6.1 | Send notification of rejection of appointment including the reason why the request has been rejected.<br>(Go to 2.1.6.1 if required) | New SVA MOA<br>or<br>New AMMOA | New AMVLP<br>or<br>Supplier | D0261 Rejection of Agent Appointment | Electronic or other method, as agreed. |
| 2.1.6.3 | If appointment accepted and within 5 WD of 2.1.6.1 | Send notification of acceptance of appointment. | New SVA MOA<br>or<br>New AMMOA | New AMVLP<br>or<br>Supplier | D0011 Agreement of Contractual Terms | Electronic or other method, as agreed. |
| 2.1.6.4 | Within 5 WD of notification from SVAA or by last date of AMVLP or Supplier Appointment | Send notification of termination of appointment. | Current AMVLP<br>or<br>Supplier | Current SVA MOA<br>or<br>Current AMMOA | D0151 Termination of Appointment or Contract by Supplier | Electronic or other method, as agreed. |
| 2.1.6.5 | Within 5 WD of 2.1.6.311 | Send notification of appointed HHDC and AMHHDC (if applicable), and current SVA MOA or AMMOA. | New AMVLP<br>or<br>Supplier | New SVA MOA<br>or<br>New AMMOA<br>HHDC<br>and | and where applicable<br>AMHHDC<br>D0148 Notification of Change to Other Parties<br>P0314 Notification of AMHHDC<br>D0302 Notification of Customer Details. | Electronic or other method, as agreed. |
| 2.1.6.6 | Within 2 WD of 2.1.6.5 | Request Meter Technical Details | New SVA MOA<br>or<br>New AMMOA | Current SVA MOA<br>or<br>Current AMMOA | D0170 Request for Metering System Related Details | Electronic or other method, as agreed. |
| 2.1.6.7 | Within 5 WD of 2.1.6.6 | Send Meter Technical Details | Current SVA MOA<br>or<br>Current AMMOA | New SVA MOA<br>or<br>New AMMOA | D0268 Half Hourly Meter Technical Details<br>If site is Complex, send Asset Metering Complex Site Supplementary Information Form. Refer to Appendix 3.9 Guide to Asset Metering Complex Sites; | Electronic or other method, as agreed. |
| 2.1.6.8 | Following 2.1.6.7 | Send Commissioning information | Current SVA MOA<br>or<br>Current AMMOA | New SVA MOA<br>or<br>New AMMOA | D0383 ‘Notification of Commissioning Information’<br>D0384 Notification of Commissioning Status | Electronic or other method, as agreed. |
| 2.1.6.9 | Within 5 WD of receipt of Meter Technical Details in 2.1.6.7 | Send Meter Technical Details | New SVA MOA<br>or<br>New AMMOA | New AMVLP<br>or<br>Supplier<br>HHDC<br>and<br>AMHHDC (if applicable) | D0268 Half Hourly Meter Technical Details<br>If site is Complex, send Asset Metering Complex Site Supplementary Information Form. Refer to Appendix 3.9 Guide to Asset Metering Complex Sites; | Electronic or other method, as agreed. |
| 2.1.6.10 | Following 2.1.6.9 | Send Commissioning information | New SVA MOA<br>or<br>New AMMOA | New AMVLP<br>or<br>Supplier | D0384 Notification of Commissioning Status | Electronic or other method, as agreed. |
| 2.1.6.11 | Following 2.1.6.10 and in accordance with timescales in Appendix 3.6.5 | If Meter Technical Details manually intervened or there has been a key field change carry out a Proving Test on the Asset Metering System in accordance with Section 2.5, Appendix 3.6 and Code of Practice Eleven. | New SVA MOA<br>or<br>New AMMOA | HHDC<br>and<br>AMHHDC (if applicable) | Refer to Appendix 3.6 | Internal Process |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

#### 2.1.7 Change of HHDC for an existing Asset Metering System (No change of AMHHDC)

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.1.7.1 | As required on appointment of new HHDC | AMVLP or Supplier appoints an HHDC | AMVLP<br>or<br>Supplier | New HHDC | D0155 Notification of Meter Operator or Data Collector Appointment and Terms | Electronic or other method, as agreed. |
| 2.1.7.2 | If appointment rejected and within 5 WD of 2.1.7.1 | Send notification of rejection of appointment including the reason why the request has been rejected.<br>(Go to 2.1.7.1 if required) | New HHDC | AMVLP<br>or<br>Supplier | D0261 Rejection of Agent Appointment | Electronic or other method, as agreed. |
| 2.1.7.3 | If appointment accepted and within 5 WD of 2.1.7.1 | Send notification of acceptance of appointment. | New HHDC | AMVLP<br>or<br>Supplier | D0011 Agreement of Contractual Terms | Electronic or other method, as agreed. |
| 2.1.7.4 | On appointment of new HHDC and within 5 WD of 2.1.7.3 | Send notification of appointed SVA MOA or AMMOA, HHDC and, if applicable, AMHHDC; and Asset Meter Registration details<br>P0303 only needs sent to new HHDC | AMVLP<br>or<br>Supplier | New HHDC | and where applicable<br>AMMHDC<br>SVA MOA<br>or<br>AMMOA<br>D0148 Notification of Change to Other Parties<br>P0314 Notification of AMHHDC<br>D0302 Notification of Customer Details.<br>P0303 Asset Meter Registration | Electronic or other method, as agreed. |
| 2.1.7.5 | Following 2.1.7.4 and upon receipt of Asset Metering System details | Record Asset Metering System details | New HHDC |  | Sufficient details of HHDC’s appointment in respect of an Asset Metering System to enable the HHDC to perform its HHDC functions.<br>These details shall include the relevant Asset Meter AMSID and the Identifiers for the SVA MOA or AMMOA.<br>The details shall also include the Settlement Days for which the HHDC is appointed.<br>Internal Process. |  |
| 2.1.7.6 | Within 5 WD of notification of appointment of new HHDC | Send Meter Technical Details and details of any current faults. | SVA MOA<br>or<br>AMMOA | New HHDC | D0002 Fault Resolution Report or Request for Decision on Further Action<br>D0268 Half Hourly Meter Technical Details<br>If site is Complex, send Asset Metering Complex Site Supplementary Information Form. Refer to Appendix 3.9 Guide to Asset Metering Complex Sites; | Electronic or other method, as agreed. |
| 2.1.7.7 | On appointment of new HHDC | Send notification of termination of appointment for Asset Metering System. | AMVLP<br>or<br>Supplier | Old HHDC | D0151 Termination of Appointment or Contract by Supplier<br>In this instance this is Termination of Appointment or Contract by AMVLP rather than Supplier | Electronic or other method, as agreed. |
| 2.1.7.8 | Within 10 WD after end of old HHDC appointment to AMVLP | Complete data collection activities for the AMVLP or Supplier. | Old HHDC | AMHHDC | Refer to Section 2.3.1 or 2.3.2 as applicable | Internal Process |
| 2.1.7.9 | In accordance with timescales in Appendix 3.6.5 | Where no AMHHDC is appointed, Prove Asset Metering System in accordance with Section 2.4, Appendix 3.6 and Code of Practice Eleven | SVA MOA<br>or<br>AMMOA | New HHDC | Refer to Appendix 3.6 | Electronic or other method, as agreed. |
| 2.1.7.10 | Where appropriate, from new HHDC appointment start date | Collect Asset Metered Data including an initial Asset Meter reading.<br>Where an AMHHDC has been appointed END PROCESS<br>Where the HHDC collects data from the Asset Meter continue to 2.1.7.11 | New HHDC<br>or<br>AMHHDC |  | Refer to Section 2.3.1 or 2.3.2 as applicable | Internal Process |
| 2.1.7.11 | Before Final Reconciliation Volume Allocation Run12 | Request 14 months of historic Asset Metered Data | New HHDC | Old HHDC | D0170 Request for Metering System Related Details | Electronic or other method, as agreed. |
| 2.1.7.12 | Within 5 WD of request in 2.1.7.11 | Send historic Asset Metered Data as available | Old HHDC | New HHDC | D0036 Validated Half Hourly Advances for Inclusion in Aggregated Supplier Matrix | Electronic or other method, as agreed. |
| 2.1.7.13 | As required | Request final Asset Meter reading | New HHDC | Old HHDC | D0005 Instruction on Action | Electronic or other method, as agreed. |
| 2.1.7.14 | Within 5 WD of 2.1.7.13 | Send final Asset Meter reading (if available in Asset Meter)13 | Old HHDC | New HHDC | D0010 Meter Readings | Electronic or other method, as agreed. |
| 2.1.7.15 | If there is a separate outstation (or integral outstation that does not provide a cumulative electronic reading) and within 10 WD of the later of the HHDC appointment start date and receipt of Meter Technical Details (unless physical read acquired through site visit within 10 WD of appointment start date); or if required by AMVLP or Supplier. | Request final physical Asset Meter reading | New HHDC | Old HHDC | This reading is required for use in the Meter Advance Reconciliation process - Appendix 3.8 - Meter Advance Reconciliation – Asset Metering Systems14. | Email. |
| 2.1.7.16 | Within 5 WD of 2.1.7.15 | Send final physical Asset Meter reading (if available in Asset Meter)13 | Old HHDC | New HHDC | D0010 Meter Readings | Electronic or other method, as agreed. |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

#### 2.1.8 Change of AMHHDC for an existing Asset Metering System (No change of HHDC)

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.1.8.1 | As required on appointment of new AMHHDC | AMVLP or Supplier appoints a new AMHHDC | AMVLP<br>or<br>Supplier | New AMHHDC | D0155 Notification of Meter Operator or Data Collector Appointment and Terms | Electronic or other method, as agreed. |
| 2.1.8.2 | If appointment rejected and within 5 WD of 2.1.8.1 | Send notification of rejection of appointment including the reason why the request has been rejected.<br>(Go to 2.1.8.1 if required) | New AMHHDC | AMVLP<br>or<br>Supplier | D0261 Rejection of Agent Appointment | Electronic or other method, as agreed. |
| 2.1.8.3 | If appointment accepted and within 5 WD of 2.1.8.1 | Send notification of acceptance of appointment. | New AMHHDC | AMVLP<br>or<br>Supplier | D0011 Agreement of Contractual Terms | Electronic or other method, as agreed. |
| 2.1.8.4 | On appointment of new AMHHDC and within 5 WD of 2.1.8.3 | Send notification of appointed SVA MOA or AMMOA and HHDC, and if applicable AMHHDC; and Asset Meter Registration details<br>P0303 only needs sent to new AMHHDC | AMVLP<br>or<br>Supplier | New AMHHDC<br>HHDC<br>SVA MOA<br>or<br>AMMOA | D0148 Notification of Change to Other Parties<br>P0314 Notification of AMHHDC<br>D0302 Notification of Customer Details.<br>P0303 Asset Meter Registration | Electronic or other method, as agreed. |
| 2.1.8.5 | Following 2.1.8.4 and upon receipt of Asset Metering System details | Record Asset Metering System details | New AMHHDC |  | Sufficient details of AMHHDC’s appointment in respect of an Asset Metering System to enable the AMHHDC to perform its AMHHDC functions.<br>These details shall include the relevant Asset Meter AMSID and the Identifiers for the SVA MOA or AMMOA.<br>The details shall also include the Settlement Days for which the AMHHDC is appointed.<br>Internal Process. |  |
| 2.1.8.6 | Within 5 WD of notification of appointment of new AMHHDC | Send Meter Technical Details and details of any current faults. | SVA MOA<br>or<br>AMMOA | New AMHHDC | D0002 Fault Resolution Report or Request for Decision on Further Action<br>D0268 Half Hourly Meter Technical Details<br>If site is Complex, send Asset Metering Complex Site Supplementary Information Form. Refer to Appendix 3.9 Guide to Asset Metering Complex Sites; | Electronic or other method, as agreed. |
| 2.1.8.7 | On appointment of new AMHHDC | Send notification of termination of appointment for Asset Metering System. | AMVLP<br>or<br>Supplier | Old AMHHDC | D0151 Termination of Appointment or Contract by Supplier<br>In this instance this is Termination of Appointment or Contract by AMVLP rather than Supplier | Electronic or other method, as agreed. |
| 2.1.8.8 | Within 10 WD after end of old AMHHDC appointment to AMVLP or Supplier. | Complete data collection activities for the AMVLP or Supplier. | HHDC | Old AMHHDC (if applicable) | Refer to Section 2.3.2 | Internal Process |
| 2.1.8.9 | In accordance with timescales in Appendix 3.6.5 | Prove Asset Metering System in accordance with Section 2.5, Appendix 3.6 and Code of Practice Eleven | SVA MOA<br>or<br>AMMOA | HHDC<br>New AMHHDC | Refer to Appendix 3.6 | Electronic or other method, as agreed. |
| 2.1.8.10 | Where appropriate, from new AMHHDC appointment start date | Collect Asset Metered Data including an initial Asset Meter reading. | HHDC<br>or<br>New AMHHDC |  | Refer to Section 2.3.2 | Internal Process |
| 2.1.8.11 | Before Final Reconciliation Volume Allocation Run15 | Request 14 months of historic Asset Metered Data | New AMHHDC | Old AMHHDC | D0170 Request for Metering System Related Details | Electronic or other method, as agreed. |
| 2.1.8.12 | Within 5 WD of request in 2.1.8.11 | Send historic Asset Metered Data as available | Old AMHHDC | New AMHHDC | D0036 Validated Half Hourly Advances for Inclusion in Aggregated Supplier Matrix | Electronic or other method, as agreed. |
| 2.1.8.13 | As required | Request final Asset Meter reading | New AMHHDC | Old AMHHDC | D0005 Instruction on Action | Electronic or other method, as agreed. |
| 2.1.8.14 | Within 5 WD of 2.1.8.13 | Send final Asset Meter reading (if available in Asset Meter)16 | Old AMHHDC | New AMHHDC | D0010 Meter Readings | Electronic or other method, as agreed. |
| 2.1.8.15 | If there is a separate outstation (or integral outstation that does not provide a cumulative electronic reading) and within 10 WD of the later of the AMHHDC appointment start date and receipt of Meter Technical Details (unless physical read acquired through site visit within 10 WD of appointment start date); or if required by AMVLP or Supplier. | Request final physical Asset Meter reading | New AMHHDC | Old AMHHDC | This reading is required for use in the Meter Advance Reconciliation process - Appendix 3.8 - Meter Advance Reconciliation – Asset Metering Systems17. | Email. |
| 2.1.8.16 | Within 5 WD of 2.1.8.15 | Send final physical Asset Meter reading (if available in Asset Meter)13 | Old AMHHDC | New AMHHDC | D0010 Meter Readings | Electronic or other method, as agreed. |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

#### 2.1.9 Concurrent Change of HHDC and AMHHDC for an existing Asset Metering System

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.1.9.1 | As required | AMVLP or Supplier appoints a new HHDC and a new AMHHDC | AMVLP<br>or<br>Supplier | New HHDC<br>New AMHHDC | D0155 Notification of Meter Operator or Data Collector Appointment and Terms<br>P0314 Notification of AMHHDC | Electronic or other method, as agreed. |
| 2.1.9.2 | If appointment rejected and within 5 WD of 2.1.9.1 | Send notification of rejection of appointment including the reason why the request has been rejected.<br>Where HHDC and AMHHDC required and one of them rejects the appointment the AMVLP or Supplier must resolve the issue and appoint all Asset Metering Agent(s) prior to step 2.1.9.4)<br>(Go to 2.1.9.1 if required) | New HHDC | New AMHHDC<br>AMVLP<br>or<br>Supplier | D0261 Rejection of Agent Appointment | Electronic or other method, as agreed. |
| 2.1.9.3 | If appointment accepted and within 5 WD of 2.1.9.1 | Send notification of acceptance of appointment. | New HHDC | New AMHHDC<br>AMVLP<br>or<br>Supplier | D0011 Agreement of Contractual Terms | Electronic or other method, as agreed. |
| 2.1.9.4 | On appointment of Data Collector(s) and within 5 WD of 2.1.9.3 | Send notification of appointed SVA MOA or AMMOA, HHDC and if applicable AMHHDC; and Asset Meter Registration details<br>P0303 only needs sent to new AMHHDC and HHDC | AMVLP<br>or<br>Supplier | New HHDC<br>New AMHHDC<br>SVA MOA<br>or<br>AMMOA | D0148 Notification of Change to Other Parties<br>P0314 Notification of AMHHDC<br>D0302 Notification of Customer Details.<br>P0303 Asset Meter Registration | Electronic or other method, as agreed. |
| 2.1.9.5 | Following 2.1.9.4 and upon receipt of Asset Metering System details | Record Asset Metering System details | New HHDC | New AMHHDC | Sufficient details of HHDC’s and AMHHDC’s appointment in respect of an Asset Metering System to enable the HHDC and AMHHDC to perform its HHDC and AMHHDC functions.<br>These details shall include the relevant Asset Meter AMSID and the Identifiers for the SVA MOA or AMMOA.<br>The details shall also include the Settlement Days for which the HHDC and AMHHDC are appointed.<br>Internal Process. |  |
| 2.1.9.6 | Within 5 WD of notification of appointment of new HHDC and new AMHHDC | Send Meter Technical Details and details of any current faults. | SVA MOA<br>or<br>AMMOA | New HHDC<br>New AMHHDC<br>AMVLP<br>or<br>Supplier | D0002 Fault Resolution Report or Request for Decision on Further Action<br>D0268 Half Hourly Meter Technical Details<br>If site is Complex, send Asset Metering Complex Site Supplementary Information Form. Refer to Appendix 3.9 Guide to Asset Metering Complex Sites; | Electronic or other method, as agreed. |
| 2.1.9.7 | On appointment of new HHDC and new AMHHDC | Send notification of termination of appointment for Asset Metering System. | AMVLP<br>or<br>Supplier | Old HHDC<br>Old AMHHDC | D0151 Termination of Appointment or Contract by Supplier<br>In this instance this is Termination of Appointment or Contract by AMVLP rather than Supplier | Electronic or other method, as agreed. |
| 2.1.9.8 | Within 10 WD after end of old HHDC and old AMHHDC appointment to AMVLP or Supplier. | Complete data collection activities for the AMVLP or Supplier. | Old HHDC | Old AMHHDC | Refer to Section 2.3.1 or 2.3.2 as applicable | Internal Process |
| 2.1.9.9 | In accordance with timescales in Appendix 3.6.5 | Prove Asset Metering System in accordance with Section 2.5, Appendix 3.6 and Code of Practice Eleven | SVA MOA<br>or<br>AMMOA | New HHDC<br>New AMHHDC | Refer to Appendix 3.6 | Electronic or other method, as agreed. |
| 2.1.9.10 | Where appropriate, from new HHDC and AMHHDC appointment start date | Collect Asset Metered Data including an initial Asset Meter reading. | New HHDC | New AMHHDC | Refer to Section 2.3.1 or 2.3.2 as applicable | Internal Process |
| 2.1.9.11 | Before Final Reconciliation Volume Allocation Run18 | Request 14 months of historic Asset Metered Data | New AMHHDC | Old AMHHDC | D0170 Request for Metering System Related Details | Electronic or other method, as agreed. |
| 2.1.9.12 | Within 5 WD of request in 2.1.9.11 | Send historic Asset Metered Data as available | Old AMHHDC | New AMHHDC | D0036 Validated Half Hourly Advances for Inclusion in Aggregated Supplier Matrix | Electronic or other method, as agreed. |
| 2.1.9.13 | As required | Request final Asset Meter reading | New AMHHDC | Old AMHHDC | D0005 Instruction on Action | Electronic or other method, as agreed. |
| 2.1.9.14 | Within 5 WD of 2.1.9.13 | Send final Asset Meter reading (if available in Asset Meter) 19 | Old AMHHDC | New AMHHDC | D0010 Meter Readings | Electronic or other method, as agreed. |
| 2.1.9.15 | If there is a separate outstation (or integral outstation that does not provide a cumulative electronic reading) and within 10 WD of the later of the AMHHDC appointment start date and receipt of Meter Technical Details (unless physical read acquired through site visit within 10 WD of appointment start date); or if required by AMVLP or Supplier. | Request final physical Asset Meter reading | New AMHHDC | Old AMHHDC | This reading is required for use in the Meter Advance Reconciliation process - Appendix 3.8 - Meter Advance Reconciliation20. | Email |
| 2.1.9.16 | Within 5 WD of 2.1.9.15 | Send final physical Asset Meter reading (if available in Asset Meter)22 | Old AMHHDC | New AMHHDC | D0010 Meter Readings | Electronic or other method, as agreed. |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

#### 2.1.10 Concurrent Change of AMVLP or Supplier and HHDC for an existing Asset Metering System (No change of AMHHDC)

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.1.10.1 | As required | New AMVLP or Supplier appoints a new HHDC | New AMVLP<br>or<br>Supplier | New HHDC | and where applicable<br>AMHHDC<br>D0155 Notification of Meter Operator or Data Collector Appointment and Terms<br>P0314 Notification of AMHHDC | Electronic or other method, as agreed. |
| 2.1.10.2 | If appointment rejected and within 5 WD of 2.1.10.1 | Send notification of rejection of appointment including the reason why the request has been rejected.<br>Where HHDC and AMHHDC required and one of them rejects the appointment the AMVLP or Supplier must resolve the issue and appoint all Asset MeteringAgent(s) prior to step 2.1.10.4)<br>(Go to 2.1.10.1 if required) | New HHDC | AMHHDC (if applicable)<br>New AMVLP<br>or<br>Supplier | D0261 Rejection of Agent Appointment | Electronic or other method, as agreed. |
| 2.1.10.3 | If appointment accepted and within 5 WD of 2.1.10.1 | Send notification of acceptance of appointment. | New HHDC | New AMVLP<br>or<br>Supplier | D0011 Agreement of Contractual Terms | Electronic or other method, as agreed. |
| 2.1.10.4 | On appointment of Data Collector(s) and within 5 WD of 2.1.10.3 | Send notification of appointed SVA MOA or AMMOA, HHDC and if applicable AMHHDC; and Asset Meter Registration details<br>P0303 only needs sent to new AMHHDC and HHDC | New AMVLP<br>or<br>Supplier | New HHDC | and where applicable<br>AMHHDC<br>SVA MOA<br>or<br>AMMOA<br>D0148 Notification of Change to Other Parties<br>P0314 Notification of AMHHDC<br>D0302 Notification of Customer Details.<br>P0303 Asset Meter Registration | Electronic or other method, as agreed. |
| 2.1.10.5 | Following 2.1.10.4 and upon receipt of Asset Metering System details | Record Asset Metering System details | New HHDC |  | Sufficient details of HHDC’s appointment in respect of an Asset Metering System to enable the HHDC to perform its HHDC functions.<br>These details shall include the relevant Asset Meter AMSID and the Identifiers for the SVA MOA or AMMOA.<br>The details shall also include the Settlement Days for which the HHDC are appointed.<br>Internal Process. |  |
| 2.1.10.6 | Within 5 WD of notification of appointment of new HHDC | Send Meter Technical Details and details of any current faults. | SVA MOA<br>or<br>AMMOA | New HHDC<br>AMHHDC (if applicable)<br>New AMVLP<br>or<br>Supplier | D0002 Fault Resolution Report or Request for Decision on Further Action<br>D0268 Half Hourly Meter Technical Details<br>If site is Complex, send Asset Metering Complex Site Supplementary Information Form. Refer to Appendix 3.9 Guide to Asset Metering Complex Sites; | Electronic or other method, as agreed. |
| 2.1.10.7 | On appointment of new AMVLP or Supplier and new HHDC | Send notification of termination of appointment for Asset Metering System. | Old AMVLP<br>or<br>Supplier | Old HHDC<br>AMHHDC (if applicable) | D0151 Termination of Appointment or Contract by Supplier<br>In this instance this is Termination of Appointment or Contract by the Registrant (AMVLP or Supplier) | Electronic or other method, as agreed. |
| 2.1.10.8 | Within 10 WD after end of old HHDC and if applicable AMHHDC appointment to old AMVLP or Supplier | Complete data collection activities for the old AMVLP or Supplier | Old HHDC | AMHHDC (if applicable) | Refer to Section 2.3.1 or 2.3.2 as applicable | Internal Process |
| 2.1.10.9 | In accordance with timescales in Appendix 3.6.5 | Where no AMHHDC is appointed, Prove Asset Metering System in accordance with Section 2.5, Appendix 3.6 and Code of Practice Eleven | SVA MOA<br>or<br>AMMOA | New HHDC | Refer to Appendix 3.6 | Electronic or other method, as agreed. |
| 2.1.10.10 | Where appropriate, from new HHDC appointment start date | Collect Asset Metered Data including an initial Asset Meter reading.<br>Where an AMHHDC has been appointed END PROCESS<br>Where the HHDC collects data from the Asset Meter continue to 2.1.10.11 | New HHDC | AMHHDC (if applicable) | Refer to Section 2.3.1 or 2.3.2 as applicable | Internal Process |
| 2.1.10.11 | Before Final Reconciliation Volume Allocation Run21 | Request 14 months of historic Asset Metered Data | New HHDC | Old HHDC | D0170 Request for Metering System Related Details | Electronic or other method, as agreed. |
| 2.1.10.12 | Within 5 WD of request in 2.1.10.11 | Send historic Asset Metered Data as available | Old HHDC | New HHDC | D0036 Validated Half Hourly Advances for Inclusion in Aggregated Supplier Matrix | Electronic or other method, as agreed. |
| 2.1.10.13 | As required | Request final Asset Meter reading | New HHDC | Old HHDC | D0005 Instruction on Action | Electronic or other method, as agreed. |
| 2.1.10.14 | Within 5 WD of 2.1.10.13 | Send final Asset Meter reading (if available in Asset Meter) 22 | Old HHDC | New HHDC | D0010 Meter Readings | Electronic or other method, as agreed. |
| 2.1.10.15 | If there is a separate outstation (or integral outstation that does not provide a cumulative electronic reading) and within 10 WD of the later of the HHDC appointment start date and receipt of Meter Technical Details (unless physical read acquired through site visit within 10 WD of appointment start date); or if required by AMVLP or Supplier. | Request final physical Asset Meter reading | New HHDC | Old HHDC | This reading is required for use in the Meter Advance Reconciliation process - Appendix 3.8 - Meter Advance Reconciliation23. | Email |
| 2.1.10.16 | Within 5 WD of 2.1.10.15 | Send final physical Asset Meter reading (if available in Asset Meter)22 | Old HHDC | New HHDC | D0010 Meter Readings | Electronic or other method, as agreed. |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

#### 2.1.11 Concurrent Change of AMVLP or Supplier and AMHHDC for an existing Asset Metering System (No change of HHDC)

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.1.11.1 | As required | New AMVLP or Supplier sends notification of a new AMHHDC | New AMVLP<br>or<br>Supplier | HHDC<br>New AMHHDC | D0155 Notification of Meter Operator or Data Collector Appointment and Terms<br>P0314 Notification of AMHHDC | Electronic or other method, as agreed. |
| 2.1.11.2 | If appointment rejected and within 5 WD of 2.1.11.1 | Send notification of rejection of appointment including the reason why the request has been rejected.<br>Where HHDC and AMHHDC required and one of them rejects the appointment the AMVLP or Supplier must resolve the issue and appoint all Asset Metering Agent(s) prior to step 2.1.11.4)<br>(Go to 2.1.11.1 if required) | HHDC | New AMHHDC<br>New AMVLP<br>or<br>Supplier | D0261 Rejection of Agent Appointment | Electronic or other method, as agreed. |
| 2.1.11.3 | If appointment accepted and within 5 WD of 2.1.11.1 | Send notification of acceptance of appointment. | New AMHHDC | New AMVLP<br>or<br>Supplier | D0011 Agreement of Contractual Terms | Electronic or other method, as agreed. |
| 2.1.11.4 | On appointment of Data Collector(s) and within 5 WD of 2.1.11.3 | Send notification of appointed SVA MOA or AMMOA, HHDC and if applicable AMHHDC; and Asset Meter Registration details<br>P0303 only needs sent to new AMHHDC and HHDC | New AMVLP<br>or<br>Supplier | HHDC<br>New AMHHDC<br>SVA MOA<br>or<br>AMMOA | D0148 Notification of Change to Other Parties<br>P0314 Notification of AMHHDC<br>D0302 Notification of Customer Details.<br>P0303 Asset Meter Registration | Electronic or other method, as agreed. |
| 2.1.11.5 | Following 2.1.11.4 and upon receipt of Asset Metering System details | Record Asset Metering System details | New AMHHDC |  | Sufficient details of AMHHDC’s appointment in respect of an Asset Metering System to enable the AMHHDC to perform its AMHHDC functions.<br>These details shall include the relevant Asset Meter AMSID and the Identifiers for the SVA MOA or AMMOA.<br>The details shall also include the Settlement Days for which the AMHHDC are appointed.<br>Internal Process. |  |
| 2.1.11.6 | Within 5 WD of notification of appointment of new AMHHDC | Send Meter Technical Details and details of any current faults. | SVA MOA<br>or<br>AMMOA | New AMHHDC<br>New AMVLP<br>or<br>Supplier | D0002 Fault Resolution Report or Request for Decision on Further Action<br>D0268 Half Hourly Meter Technical Details<br>If site is Complex, send Asset Metering Complex Site Supplementary Information Form. Refer to Appendix 3.9 Guide to Asset Metering Complex Sites; | Electronic or other method, as agreed. |
| 2.1.11.7 | On appointment of new AMVLP or Supplier and new AMHHDC | Send notification of termination of appointment for Asset Metering System. | Old AMVLP<br>or<br>Supplier | Old AMHHDC | D0151 Termination of Appointment or Contract by Supplier<br>In this instance this is Termination of Appointment or Contract by the Registrant of the Asset Metering System (Supplier or AMVLP). | Electronic or other method, as agreed. |
| 2.1.11.8 | Within 10 WD after end of old HHDC and AMHHDC appointment to old AMVLP or Supplier. | Complete data collection activities for the old AMVLP or Supplier. | HHDC | Old AMHHDC (if applicable) | Refer to Section 2.3.2 | Internal Process |
| 2.1.11.9 | In accordance with timescales in Appendix 3.6.5 | Prove Asset Metering System in accordance with Section 2.5, Appendix 3.6 and Code of Practice Eleven | SVA MOA<br>or<br>AMMOA | HHDC<br>New AMHHDC (if applicable) | Refer to Appendix 3.6 | Electronic or other method, as agreed. |
| 2.1.11.10 | Where appropriate, from new AMHHDC appointment start date | Collect Asset Metered Data including an initial Asset Meter reading. | HHDC | New AMHHDC (if applicable) | Refer to Section 2.3.1 or 2.3.2 as applicable | Internal Process |
| 2.1.11.11 | Before Final Reconciliation Volume Allocation Run24 | Request 14 months of historic Asset Metered Data | New AMHHDC | Old AMHHDC | D0170 Request for Metering System Related Details | Electronic or other method, as agreed. |
| 2.1.11.12 | Within 5 WD of request in 2.1.11.11 | Send historic Asset Metered Data as available | Old AMHHDC | New AMHHDC | D0036 Validated Half Hourly Advances for Inclusion in Aggregated Supplier Matrix | Electronic or other method, as agreed. |
| 2.1.11.13 | As required | Request final Asset Meter reading | New AMHHDC | Old AMHHDC | D0005 Instruction on Action | Electronic or other method, as agreed. |
| 2.1.11.14 | Within 5 WD of 2.1.11.13 | Send final Asset Meter reading (if available in Asset Meter)25 | Old AMHHDC | New AMHHDC | D0010 Meter Readings | Electronic or other method, as agreed. |
| 2.1.11.15 | If there is a separate outstation (or integral outstation that does not provide a cumulative electronic reading) and within 10 WD of the later of the AMHHDC appointment start date and receipt of Meter Technical Details (unless physical read acquired through site visit within 10 WD of appointment start date); or if required by AMVLP or Supplier. | Request final physical Asset Meter reading | New AMHHDC | Old AMHHDC | This reading is required for use in the Meter Advance Reconciliation process - Appendix 3.8 - Meter Advance Reconciliation – Asset Metering Systems26. | Email. |
| 2.1.11.16 | Within 5 WD of 2.1.11.15 | Send final physical Asset Meter reading (if available in Asset Meter)13 | Old AMHHDC | New AMHHDC | D0010 Meter Readings | Electronic or other method, as agreed. |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

#### 2.1.12 Concurrent Change of AMVLP or Supplier, HHDC and AMHHDC for an existing Asset Metering System

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.1.12.1 | As required | New AMVLP or Supplier appoints a new HHDC and a new AMHHDC | New AMVLP<br>or<br>Supplier | New HHDC<br>New AMHHDC | D0155 Notification of Meter Operator or Data Collector Appointment and Terms<br>P0314 Notification of AMHHDC | Electronic or other method, as agreed. |
| 2.1.12.2 | If appointment rejected and within 5 WD of 2.1.12.1 | Send notification of rejection of appointment including the reason why the request has been rejected.<br>Where HHDC and AMHHDC required and one of them rejects the appointment the AMVLP or Supplier must resolve the issue and appoint all Asset Metering Agent(s) prior to step 2.1.12.4)<br>(Go to 2.1.12.1 if required) | New HHDC | New AMHHDC<br>New AMVLP<br>or<br>Supplier | D0261 Rejection of Agent Appointment | Electronic or other method, as agreed. |
| 2.1.12.3 | If appointment accepted and within 5 WD of 2.1.12.1 | Send notification of acceptance of appointment. | New HHDC | New AMHHDC<br>New AMVLP<br>or<br>Supplier | D0011 Agreement of Contractual Terms | Electronic or other method, as agreed. |
| 2.1.12.4 | On appointment of Data Collector(s) and within 5 WD of 2.1.12.3 | Send notification of appointed SVA MOA or AMMOA, HHDC and if applicable AMHHDC; and Asset Meter Registration details<br>P0303 only needs sent to new AMHHDC and HHDC | New AMVLP<br>or<br>Supplier | New HHDC<br>New AMHHDC<br>SVA MOA<br>or<br>AMMOA | D0148 Notification of Change to Other Parties<br>P0314 Notification of AMHHDC<br>D0302 Notification of Customer Details.<br>P0303 Asset Meter Registration | Electronic or other method, as agreed. |
| 2.1.12.5 | Following 2.1.12.4 and upon receipt of Asset Metering System details | Record Asset Metering System details | New HHDC | New AMHHDC | Sufficient details of HHDC’s and AMHHDC’s appointment in respect of an Asset Metering System to enable the HHDC and AMHHDC to perform its HHDC and AMHHDC functions.<br>These details shall include the relevant Asset Meter AMSID and the Identifiers for the SVA MOA or AMMOA.<br>The details shall also include the Settlement Days for which the HHDC and AMHHDC are appointed.<br>Internal Process. |  |
| 2.1.12.6 | Within 5 WD of notification of appointment of new HHDC and new AMHHDC | Send Meter Technical Details and details of any current faults. | SVA MOA<br>or<br>AMMOA | New HHDC<br>New AMHHDC<br>New AMVLP<br>or<br>Supplier | D0002 Fault Resolution Report or Request for Decision on Further Action<br>D0268 Half Hourly Meter Technical Details<br>If site is Complex, send Asset Metering Complex Site Supplementary Information Form. Refer to Appendix 3.9 Guide to Asset Metering Complex Sites; | Electronic or other method, as agreed. |
| 2.1.12.7 | On appointment of new AMVLP or Supplier, new HHDC and new AMHHDC | Send notification of termination of appointment for Asset Metering System. | Old AMVLP | Supplier<br>Old HHDC<br>Old AMHHDC | D0151 Termination of Appointment or Contract by Supplier<br>In this instance this is Termination of Appointment or Contract by the Registrant of the Asset Metering System (Supplier or AMVLP). | Electronic or other method, as agreed. |
| 2.1.12.8 | Within 10 WD after end of old HHDC and old AMHHDC appointment to old AMVLP or Supplier. | Complete data collection activities for the old AMVLP or Supplier. | Old HHDC | Old AMHHDC | Refer to Section 2.3.1 or 2.3.2 as applicable | Internal Process |
| 2.1.12.9 | In accordance with timescales in Appendix 3.6.5 | Prove Asset Metering System in accordance with Section 2.5, Appendix 3.6 and Code of Practice Eleven | SVA MOA<br>or<br>AMMOA | New HHDC<br>New AMHHDC | Refer to Appendix 3.6 | Electronic or other method, as agreed. |
| 2.1.12.10 | Where appropriate, from new HHDC and AMHHDC appointment start date | Collect Asset Metered Data including an initial Asset Meter reading. | New HHDC | New AMHHDC | Refer to Section 2.3.1 or 2.3.2 as applicable | Internal Process |
| 2.1.12.11 | Before Final Reconciliation Volume Allocation Run27 | Request 14 months of historic Asset Metered Data | New AMHHDC | Old AMHHDC | D0170 Request for Metering System Related Details | Electronic or other method, as agreed. |
| 2.1.12.12 | Within 5 WD of request in 2.1.12.11 | Send historic Asset Metered Data as available | Old AMHHDC | New AMHHDC | D0036 Validated Half Hourly Advances for Inclusion in Aggregated Supplier Matrix | Electronic or other method, as agreed. |
| 2.1.12.13 | As required | Request final Asset Meter reading | New AMHHDC | Old AMHHDC | D0005 Instruction on Action | Electronic or other method, as agreed. |
| 2.1.12.14 | Within 5 WD of 2.1.12.13 | Send final Asset Meter reading (if available in Asset Meter) 28 | Old AMHHDC | New AMHHDC | D0010 Meter Readings | Electronic or other method, as agreed. |
| 2.1.12.15 | If there is a separate outstation (or integral outstation that does not provide a cumulative electronic reading) and within 10 WD of the later of the AMHHDC appointment start date and receipt of Meter Technical Details (unless physical read acquired through site visit within 10 WD of appointment start date); or if required by AMVLP or Supplier. | Request final physical Asset Meter reading | New AMHHDC | Old AMHHDC | This reading is required for use in the Meter Advance Reconciliation process – Appendix 3.8 - Meter Advance Reconciliation29. | Email |
| 2.1.12.16 | Within 5 WD of 2.1.12.15 | Send final physical Asset Meter reading (if available in Asset Meter)22 | Old AMHHDC | New AMHHDC | D0010 Meter Readings | Electronic or other method, as agreed. |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

#### 2.1.13 Change from AMHHDC to HHDC for an existing Asset Metering System

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.1.13.1 | As required on de-appointment of AMHHDC | Send notification of termination of appointment for Asset Metering System. | AMVLP<br>or<br>Supplier | AMHHDC | D0151 Termination of Appointment or Contract by Supplier<br>In this instance this is Termination of Appointment or Contract by AMVLP rather than Supplier | Electronic or other method, as agreed. |
| 2.1.13.2 | Within 10 WD after end of AMHHDC appointment to AMVLP or Supplier. | Complete data collection activities for the AMVLP or Supplier. | HHDC | AMHHDC | Refer to Section 2.3.2 | Internal Process |
| 2.1.13.3 | On de-appointment of AMHHDC and within 5 WD of 2.1.13.1 | Send notification of AMHHDC de-appointment to HHDC | AMVLP<br>or<br>Supplier | HHDC | P0314 Notification of AMHHDC | Electronic or other method, as agreed. |
| 2.1.13.4 | In accordance with timescales in Appendix 3.6.5 | Prove Asset Metering System in accordance with Section 2.5, Appendix 3.6 and Code of Practice Eleven | SVA MOA<br>or<br>AMMOA | HHDC | Refer to Appendix 3.6 | Electronic or other method, as agreed. |
| 2.1.13.5 | Where appropriate, from AMHHDC de-appointment date | Collect Asset Metered Data including an initial Asset Meter reading. | HHDC |  | Refer to Section 2.3.1 | Internal Process |
| 2.1.13.6 | Before Final Reconciliation Volume Allocation Run30 | Request 14 months of historic Asset Metered Data | AMHHDC | HHDC | D0170 Request for Metering System Related Details | Electronic or other method, as agreed. |
| 2.1.13.7 | Within 5 WD of request in 2.1.13.6 | Send historic Asset Metered Data as available | AMHHDC | HHDC | D0036 Validated Half Hourly Advances for Inclusion in Aggregated Supplier Matrix | Electronic or other method, as agreed. |
| 2.1.13.8 | As required | Request final Asset Meter reading | HHDC | AMHHDC | D0005 Instruction on Action | Electronic or other method, as agreed. |
| 2.1.13.9 | Within 5 WD of 2.1.13.8 | Send final Asset Meter reading (if available in Asset Meter)31 | AMHHDC | HHDC | D0010 Meter Readings | Electronic or other method, as agreed. |
| 2.1.13.10 | If there is a separate outstation (or integral outstation that does not provide a cumulative electronic reading) and within 10 WD of the later of the HHDC appointment start date and receipt of Meter Technical Details (unless physical read acquired through site visit within 10 WD of appointment start date); or if required by AMVLP or Supplier. | Request final physical Asset Meter reading | HHDC | AMHHDC | This reading is required for use in the Meter Advance Reconciliation process - Appendix 3.8 - Meter Advance Reconciliation – Asset Metering Systems32. | Email. |
| 2.1.13.11 | Within 5 WD of 2.1.13.10 | Send final physical Asset Meter reading (if available in Asset Meter)13 | AMHHDC | HHDC | D0010 Meter Readings | Electronic or other method, as agreed. |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 2.2 Metering Activities

#### 2.2.1 Energise an Asset Metering System

For Asset Metering Types4 1, 2 and 3 the Meter Operator activities shall be done by a SVA MOA; for Asset Metering Types 4 and 5 the AMVLP or Supplier can choose to appoint a SVA MOA or an AMMOA.

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.2.1.1 | As required | Send request to energise Asset Metering System | AMVLP<br>or<br>Supplier | SVA MOA<br>or<br>AMMOA | D0134 Request to Change Energisation Status | Electronic or other method, as agreed. |
| 2.2.1.2 | If request rejected and within 2 WD of 2.2.1.1 | Send notification of rejection including the reason why the request has been rejected.<br>(Go to 2.2.1.1 if required) | SVA MOA<br>or<br>AMMOA | AMVLP<br>or<br>Supplier | D0139 Confirmation or Rejection of Energisation Status Change<br>or<br>D0221 Notification of Failure to Install or Energise Metering System<br>or<br>P0211 Site Visit Rejection | Electronic or other method, as agreed. |
| 2.2.1.3 | On the date requested or agreed in 2.2.1.1 | Energise Asset Metering System and note initial Asset Meter register reading (If available). | SVA MOA<br>or<br>AMMOA |  |  | Internal Process |
| 2.2.1.4 | Within 5 WD of attempting to change energisation status | OR<br>Following the SVA MOA / AMMOA becoming aware of a discrepancy between the energisation status on site and that held by the AMVLP Supplier / HHDC / AMHHDC.<br>Send change of energisation status and the initial Asset Meter register reading (if available). | SVA MOA<br>or<br>AMMOA | AMVLP<br>or<br>Supplier<br>HHDC<br>and<br>AMHHDC (if applicable) | D0139 Confirmation or Rejection of Energisation Status Change<br>D0010 Meter Readings | Electronic or other method, as agreed. |
| 2.2.1.5 | Following receipt of notification in 2.2.1.4 | Record notification by SVA MOA or AMMOA of Asset Metering Systems which have been energised, and the date on which they were energised. | HHDC | AMHHDC | Details of Asset Metering Systems which have been energised and the dates on which they were energised. | Internal Process |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

#### 2.2.2 De-energise an Asset Metering System

For Asset Metering Types4 1, 2 and 3 the Meter Operator activities shall be done by a SVA MOA; for Asset Metering Types 4 and 5 the AMVLP or Supplier can choose to appoint a SVA MOA or an AMMOA.

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.2.2.1 | As required and at least 10 WD before 2.2.2.6 | Send request to de-energise Asset Metering System | AMVLP<br>or<br>Supplier | SVA MOA<br>or<br>AMMOA | D0134 Request to Change Energisation Status | Electronic or other method, as agreed. |
| 2.2.2.2 | If request rejected and within 2 WD of 2.2.2.1 | Send notification of rejection including the reason why the request has been rejected.<br>(Go to 2.2.2.1 if required) | SVA MOA<br>or<br>AMMOA | AMVLP<br>or<br>Supplier | D0139 Confirmation or Rejection of Energisation Status Change<br>or<br>D0221 Notification of Failure to Install or Energise Metering System<br>or<br>P0211 Site Visit Rejection | Electronic or other method, as agreed. |
| 2.2.2.3 | If request accepted and within 3 WD of 2.2.2.1 and before planned date for de-energisation. | Arrange with HHDC or AMHHDC (if applicable) to collect final Metered Data from Asset Meter. | SVA MOA<br>or<br>AMMOA | HHDC<br>or<br>AMHHDC (if applicable) | D0005 Instruction on Action<br>Date and time of Settlement Periods to be collected | Electronic or other method, as agreed. |
| 2.2.2.4 | On the date and time agreed in 2.2.2.3 | Collect final Metered Data from Asset Meter. | HHDC<br>or<br>AMHHDC (if applicable) |  |  | Internal Process |
| 2.2.2.5 | Immediately following 2.2.2.4 | Confirm final Metered Data from Asset Meter collected. | HHDC<br>or<br>AMHHDC (if applicable) | SVA MOA<br>or<br>AMMOA | The MOA will telephone the HHDC/AMHHDC when the MOA is on site.<br>Following the HHDC/AMHHDC collecting the data, the HHDC/AMHHDC will provide confirmation to the SVA MOA.<br>Where telephone communication is not possible33 another agreed method may be used. | Telephone or Electronic or other method, as agreed. |
| 2.2.2.6 | Immediately following 2.2.2.5 | Note final Asset Meter register reading (if available).<br>If final Metered Data from Asset Meter was not collected in 2.2.2.4, download Metered Data from the Asset Meter, if available.<br>De-energise Asset Metering System | SVA MOA<br>or<br>AMMOA |  |  | Internal Process |
| 2.2.2.7 | Within 5 WD of attempting to change energisation status | OR<br>Following the SVA MOA becoming aware of a discrepancy between the energisation status on site and that held by the AMVLP/Supplier/HHDC.<br>Send change of energisation status and the final Asset Meter register reading (if available). | SVA MOA<br>or<br>AMMOA | AMVLP<br>or<br>Supplier<br>HHDC<br>and<br>AMHHDC (if applicable) | D0139 Confirmation or Rejection of Energisation Status Change<br>D0010 Meter Readings | Electronic or other method, as agreed. |
| 2.2.2.8 | Following receipt of notification in 2.2.2.7 | Record notification by SVA MOA or AMMOA of Asset Metering Systems, which have been de-energised and the date on which they were de-energised. | HHDC | AMHHDC | Details of Asset Metering Systems which have been de-energised, and the dates on which they were de-energised. | Internal Process |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

#### 2.2.3 Removal of an Asset Metering System

Where a AMVLP or Supplier has requested that an Asset Metering System be removed for an AMSID for Asset Metering Types4 1, 2 and 3 the Meter Operator activities shall be done by a SVA MOA; for Asset Metering Types 4 and 5 the AMVLP or Supplier can choose to appoint a SVA MOA or an AMMOA.

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.2.3.1 | As required | Send request to remove an Asset Metering System | AMVLP<br>or<br>Supplier | SVA MOA<br>or<br>AMMOA | D0142 Request for Installation or Change to a Metering System Functionality or the Removal of All Meters | Electronic or other method, as agreed. |
| 2.2.3.2 | If request rejected and within 2 WD of 2.2.3.1 | Send notification of rejection including the reason why the request has been rejected.<br>(Go to 2.2.3.1 if required) | SVA MOA<br>or<br>AMMOA | AMVLP<br>or<br>Supplier | P0211 Site Visit Rejection | Electronic or other method, as agreed. |
| 2.2.3.3 | If request accepted and within 3 WD of request and before data collection date or as the SVA MOA/AMMOA sees necessary. | Arrange with HHDC or AMHHDC (if applicable) to collect final Metered Data from Asset Meter. | SVA MOA<br>or<br>AMMOA | HHDC<br>or<br>AMHHDC (if applicable) | D0005 Instruction on Action<br>Date and time of Settlement Periods to be collected | Electronic or other method, as agreed. |
| 2.2.3.4 | On date and time agreed in 2.2.3.3 | Collect final Metered Data from Asset Meter. | HHDC<br>or<br>AMHHDC (if applicable) |  |  | Internal Process |
| 2.2.3.5 | Following 2.2.3.4 | Confirm final Metered Data from Asset Meter collected. | HHDC<br>or<br>AMHHDC (if applicable) | SVA MOA<br>or<br>AMMOA | The MOA will telephone the HHDC/AMHHDC when the MOA is on site.<br>Following the HHDC/AMHHDC collecting the data, the HHDC/AMHHDC will provide confirmation to the SVA MOA or AMMOA.<br>Where telephone communication is not possible34 another agreed method may be used. | Telephone or Electronic or other method, as agreed. |
| 2.2.3.6 | Following 2.2.3.5 | Note final Asset Meter register reading, if available.<br>If final Metered Data from Asset Meter was not collected in 2.2.3.4, download Metered Data from the Asset Meter, if available.<br>Remove Asset Metering System. | SVA MOA<br>or<br>AMMOA |  |  | Internal Process |
| 2.2.3.7 | Within 5 WD of the removal of the Asset Metering System or within 2 WD of 2.2.3.10 (as applicable) | Send final Asset Meter register reading for removed Asset Metering System or notification that Asset Meter register reading not obtainable.<br>Send Meter Technical Details and notification that the Asset Metering System has been removed. | SVA MOA<br>or<br>AMMOA | HHDC<br>or<br>AMHHDC (if applicable)<br>AMVLP<br>or<br>Supplier | D0010 Meter Readings<br>or<br>D0002 Fault Resolution Report or Request for Decision on Further Action<br>and<br>D0268 Half Hourly Meter Technical Details<br>If site is Complex, send Asset Metering Complex Site Supplementary Information Form. Refer to Appendix 3.9 Guide to Asset Metering Complex Sites; | Electronic or other method, as agreed. |
| 2.2.3.8 | At same time as 2.2.3.7 | This step does not apply for Asset Meters registered in LPAMR.<br>Send the relevant Asset Meter information. | AMVLP<br>or<br>Supplier | SVAA | P0303 Asset Meter Registration | Electronic or other method, as agreed. |
| 2.2.3.9 | Immediately following 2.2.3.8 or 2.2.3.10 | Perform validation checks and send response<br>If response is “Accepted”, proceed to 2.2.3.11, otherwise proceed to 2.2.3.10. | SVAA | AMVLP<br>or<br>Supplier | P0304 Rejection of Asset Meter Registration<br>Or<br>P0305 Confirmation of Asset Meter Registration | Electronic or other method, as agreed. |
| 2.2.3.10 | Within 5 WD of 2.2.3.9 | This step does not apply for Asset Meters registered in LPAMR.<br>Where the rejection is of a type the AMVLP or Supplier can resolve without involving other industry parties, send a corrected flow.<br>Proceed to 2.2.3.9<br>If the AMVLP or Supplier needs to involve other industry parties to resolve the issue, then reasonable endeavours should apply. Notify SVA MOA or AMMOA of rejection reasons and request new D0268.<br>Proceed to 2.2.3.7 | AMVLP<br>or<br>Supplier | AMVLP<br>or<br>Supplier<br>SVAA<br>SVA MOA<br>or<br>AMMOA | P0303 Asset Meter Registration<br>P0304 Rejection of Asset Meter Registration<br>Electronic or other method, as agreed. | Electronic or other method, as agreed. |
| 2.2.3.11 | On confirmation from SVAA of disconnection | Send end date for Asset Metering System | AMVLP<br>or<br>Supplier | HHDC<br>AMHHDC (if applicable) | D0151 Termination of Appointment or Contract by Supplier<br>In this instance this is Termination of Appointment or Contract by AMVLP rather than Supplier | Electronic or other method, as agreed. |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

#### 2.2.4 Reconfigure or Replace an Asset Metering System

Where an AMVLP or Supplier has requested that an Asset Metering System is reconfigured or replaced for an AMSID for Asset Metering Types4 1, 2 and 3 the Meter Operator activities shall be done by a SVA MOA; for Asset Metering Types 4 and 5 the AMVLP or Supplier can choose to appoint a SVA MOA or an AMMOA.

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.2.4.1 | As required | Send request to reconfigure or replace Asset Metering System | AMVLP<br>or<br>Supplier | SVA MOA<br>or<br>AMMOA | D0142 Request for Installation or Change to a Metering System Functionality or the Removal of All Meters | Electronic or other method, as agreed. |
| 2.2.4.2 | If request rejected and within 2 WD of 2.2.4.1 | Send notification of rejection including the reason why the request has been rejected.<br>(Go to 2.2.4.1 if required) | SVA MOA<br>or<br>AMMOA | AMVLP<br>or<br>Supplier | P0211 Site Visit Rejection | Electronic or other method, as agreed. |
| 2.2.4.3 | If request accepted and within 3 WD of request and before data collection date or as the SVA MOA/AMMOA sees necessary. | Arrange with HHDC or AMHHDC (if applicable) to collect final Metered Data from Asset Meter. | SVA MOA<br>or<br>AMMOA | HHDC<br>or<br>AMHHDC (if applicable) | D0005 Instruction on Action<br>Date and time of Settlement Periods to be collected | Electronic or other method, as agreed. |
| 2.2.4.4 | On date and time agreed in 2.2.4.3 | Collect final Metered Data from Asset Meter. | HHDC<br>or<br>AMHHDC (if applicable) |  |  | Internal Process |
| 2.2.4.5 | Following 2.2.4.4 | Confirm final Metered Data from Asset Meter collection. | HHDC<br>or<br>AMHHDC (if applicable) | SVA MOA<br>or<br>AMMOA | The MOA will telephone the HHDC/AMHHDC when the MOA is on site.<br>Following the HHDC/AMHHDC collecting the data, the HHDC/AMHHDC will provide confirmation to the SVA MOA or AMMOA.<br>Where telephone communication is not possible35 another agreed method may be used. | Telephone or Electronic or other method, as agreed. |
| 2.2.4.6 | Following 2.2.4.5 | Note final Asset Meter register reading, if available.<br>If final Metered Data from Asset Meter was not uploaded by the HHDC/AMHHDC, download final HH Metered Data, if available.<br>Reconfigure Asset Metering System or replace and energise Asset Metering System36,37.<br>Note initial Asset Meter register reading. | SVA MOA<br>or<br>AMMOA |  |  | Internal Process |
| 2.2.4.7 | Within 5 WD of the replacement / reconfiguration of the Asset Metering System or within 2 WD of 2.2.4.10 (as applicable) | Send final Asset Meter register reading for replaced / reconfigured Asset Metering System or notification that Asset Meter register reading not obtainable.<br>Send initial Asset Meter register reading for replacement Asset Metering System / new configuration.<br>Send Meter Technical Details for replacement Asset Metering System / new configuration. | SVA MOA<br>or<br>AMMOA | HHDC<br>or<br>AMHHDC (if applicable)<br>AMVLP<br>or<br>Supplier | D0010 Meter Readings<br>or<br>D0002 Fault Resolution Report or Request for Decision on Further Action<br>and<br>D0268 Half Hourly Meter Technical Details<br>If site is Complex, send Asset Metering Complex Site Supplementary Information Form. Refer to Appendix 3.9 Guide to Asset Metering Complex Sites; | Electronic or other method, as agreed. |
| 2.2.4.8 | Following 2.2.4.7 | This step does not apply for Asset Meters registered in LPAMR.<br>Send the relevant Asset Meter information. | AMVLP<br>or<br>Supplier | SVAA | P0303 ‘Asset Meter Registration | Electronic or other method, as agreed. |
| 2.2.4.9 | Immediately following 2.2.4.8 or 2.2.4.10 | Perform validation checks and send response<br>If response is “Accepted”, proceed to 2.2.4.11, otherwise proceed to 2.2.4.10. | SVAA | AMVLP<br>or<br>Supplier | P0304 Rejection of Asset Meter Registration<br>Or<br>P0305 Confirmation of Asset Meter Registration | Electronic or other method, as agreed. |
| 2.2.4.10 | Within 5 WD of 2.2.4.9 | This step does not apply for Asset Meters registered in LPAMR.<br>Where the rejection is of a type the AMVLP or Supplier can resolve without involving other industry parties, send a corrected flow.<br>Proceed to 2.2.4.9<br>If the AMVLP or Supplier needs to involve other industry parties to resolve the issue, then reasonable endeavours should apply. Notify SVA MOA or AMMOA of rejection reasons and request new D0268.<br>Proceed to 2.2.4.7 | AMVLP<br>or<br>Supplier | AMVLP<br>or<br>Supplier<br>SVAA<br>SVA MOA<br>or<br>AMMOA | P0303 Asset Meter Registration<br>P0304 Rejection of Asset Meter Registration<br>Electronic or other method, as agreed. | Electronic or other method, as agreed. |
| 2.2.4.11 | After planned date for replacement / reconfiguration of the Asset Metering System | Collect Asset Metered Data for replacement Asset Metering System / new configuration | HHDC<br>or<br>AMHHDC |  | Refer to 2.3.1 or 2.3.2 as applicable | Internal Process |
| 2.2.4.12 | In accordance with timescales in Appendix 3.6.5 | Carry out a Proving Test on the Asset Metering System in accordance with Section 2.5, Appendix 3.6 and Code of Practice Eleven. | SVA MOA<br>or<br>AMMOA | HHDC<br>and<br>AMHHDC (if applicable) | Refer to Appendix 3.6 | Electronic or other method, as agreed. |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

#### 2.2.5 Change of Asset Feeder Status – Energise Feeder for an Asset

For Asset Metering Types4 1, 2 and 3 the Meter Operator activities shall be done by a SVA MOA; for Asset Metering Types 4 and 5 the AMVLP or Supplier can choose to appoint a SVA MOA or an AMMOA.

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.2.5.1 | As required | Send request to change the status of an Asset feeder of an Asset | AMVLP<br>or<br>Supplier | SVA MOA<br>or<br>AMMOA | D0142 Request for Installation or Change to a Metering System Functionality or the Removal of All Meters | Electronic or other method, as agreed. |
| 2.2.5.2 | If request rejected and within 2 WD of 2.2.5.1 | Send notification of rejection including the reason why the request has been rejected.<br>(Go to 2.2.5.1 if required) | SVA MOA<br>or<br>AMMOA | AMVLP<br>or<br>Supplier | P0211 Site Visit Rejection | Electronic or other method, as agreed. |
| 2.2.5.3 | On date requested or agreed in 2.2.5.1 or as the SVA MOA/AMMOA sees necessary | Change Asset feeder status.<br>Note Asset Meter register reading (if available). | SVA MOA<br>or<br>AMMOA |  |  | Internal Process |
| 2.2.5.4 | Within 5 WD of change to Asset feeder status | If available, send Asset Meter register reading. | Send Meter Technical Details | SVA MOA<br>or<br>AMMOA<br>AMVLP<br>or<br>Supplier<br>HHDC<br>and<br>AMHHDC (if applicable) | D0010 Meter Readings<br>D0268 Half Hourly Meter Technical Details<br>If site is Complex, send Asset Metering Complex Site Supplementary Information Form. Refer to Appendix 3.9 Guide to Asset Metering Complex Sites; | Electronic or other method, as agreed. |
| 2.2.5.5 | Following 2.2.5.4 and in accordance with timescales in Appendix 3.6.5 | If feeder for the Asset has been energised for the first time carry out a Proving Test on the Asset Metering System in accordance with Section 2.5, Appendix 3.6 and Code of Practice Eleven | SVA MOA<br>or<br>AMMOA | HHDC<br>and<br>AMHHDC (if applicable) | Refer to Appendix 3.6 | Electronic or other method, as agreed. |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

#### 2.2.6 Change of Asset Feeder Status – De-Energise Feeder for an Asset

For Asset Metering Types4 1, 2 and 3 the Meter Operator activities shall be done by a SVA MOA; for Asset Metering Types 4 and 5 the AMVLP or Supplier can choose to appoint a SVA MOA or an AMMOA.

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.2.6.1 | As required | Send request to change the status of an Asset feeder of an Asset | AMVLP<br>or<br>Supplier | SVA MOA<br>or<br>AMMOA | D0142 Request for Installation or Change to a Metering System Functionality or the Removal of All Meters | Electronic or other method, as agreed. |
| 2.2.6.2 | If request rejected and within 2 WD of 2.2.6.1 | Send notification of rejection including the reason why the request has been rejected.<br>(Go to 2.2.6.1 if required) | SVA MOA<br>or<br>AMMOA | AMVLP<br>or<br>Supplier | P0211 Site Visit Rejection | Electronic or other method, as agreed. |
| 2.2.6.3 | If request accepted and within 3 WD of request and before data collection date or as the SVA MOA/AMMOA sees necessary. | Arrange with HHDC or AMHHDC (if applicable) to collect final Metered Data from Asset Meter. | SVA MOA<br>or<br>AMMOA | HHDC<br>or<br>AMHHDC (if applicable) | D0005 Instruction on Action<br>Date and time of Settlement Periods to be collected | Electronic or other method, as agreed. |
| 2.2.6.4 | On date and time agreed in 2.2.6.3 | Collect final Metered Data from Asset Meter. | HHDC<br>or<br>AMHHDC (if applicable) |  |  | Internal Process |
| 2.2.6.5 | Following 2.2.6.4 | Confirm final Metered Data from Asset Meter collection. | HHDC<br>or<br>AMHHDC (if applicable) | SVA MOA<br>or<br>AMMOA | The SVA MOA or AMMOA will telephone the HHDC/AMHHDC when the SVA MOA or AMMOA is on site.<br>Following the HHDC/AMHHDC collecting the data, the HHDC/AMHHDC will provide confirmation to the SVA MOA or AMMOA.<br>Where telephone communication is not possible38 another agreed method may be used. | Telephone or Electronic or other method, as agreed. |
| 2.2.6.6 | Following 2.2.6.5 | Note final Asset Meter register reading, if available.<br>If final Metered Data from Asset Meter was not uploaded by the HHDC/AMHHDC, download final HH Metered Data, if available.<br>Change Asset feeder status | SVA MOA<br>or<br>AMMOA |  |  | Internal Process |
| 2.2.6.7 | Within 5 WD of changing Asset feeder status in 2.2.6.6 | If available, send Asset Meter register reading.<br>Send Meter Technical Details. | SVA MOA<br>or<br>AMMOA | HHDC<br>or<br>AMHHDC (if applicable)<br>AMVLP<br>or<br>Supplier | D0010 Meter Readings<br>D0268 Half Hourly Meter Technical Details<br>If site is Complex, send Asset Metering Complex Site Supplementary Information Form. Refer to Appendix 3.9 Guide to Asset Metering Complex Sites; | Electronic or other method, as agreed. |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 2.3 Collection Activities

2.3.1 HHDC collects, validates and sends consumption data for an Asset Metering System where Half Hourly data is not sourced by the AMHHDC

Where the HHDC communicates directly with the Asset Meter.

See Section 2.3.2 where the HHDC receives Half Hourly data from the AMHHDC, processes and sends consumption data for an Asset Metering System.

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.3.1.1 | As required | Collect and validate Half Hourly Metered Data from an Asset Metering System.<br>Data from the Asset Meter shall be retrieved as soon as possible before historical data is overwritten.<br>This can be data in other formats where it can be converted to Half Hourly Metered Data by the HHDC. | HHDC |  | Refer to Appendix 3.1, Appendix 3.2, Appendix 3.3, and where relevant Appendix 3.8. | Internal Process |
| 2.3.1.2 | Following 2.3.1.1 and in accordance with timescales in Appendix 3.1 and 3.8 | Provide relevant reports | HHDC | AMVLP<br>or<br>Supplier<br>SVA MOA<br>or<br>AMMOA | Refer to Appendix 3.1 and where relevant Appendix 3.8.<br>D0008 Meter Advance Reconciliation Report in accordance with Appendix 3.8 | Electronic or other method, as agreed. |
| 2.3.1.3 | When fault suspected with Metering or communications equipment. | Investigate and report any faults detected. | HHDC |  | Refer to Section 2.3.3 | Internal Process |
| 2.3.1.4 | Within 2 WD of detecting consumption on de-energised Metering or if maximum permissible energy exceeds that allowed. | Report any consumption detected on de-energised Metering and escalate any occurrences where the energy recorded, for any Settlement Period, exceeds the maximum permissible on energised metering.<br>HHDC. | AMVLP<br>or<br>Supplier | SVA MOA<br>or<br>AMMOA | Refer to Appendix 3.1<br>D0001 Request Metering System Investigation.<br>Internal Process. | Electronic or other method, as agreed. |
| 2.3.1.5 | When maximum permissible energy exceeds that allowed. | Send notification of action to be taken. | AMVLP<br>or<br>Supplier |  | .<br>HHDC.<br>D0005 Instruction on Action.<br>The HHDC will be instructed to validate the actual data or to replace the actual data with estimated successfully validated data. | Electronic or other method, as agreed. |
| 2.3.1.6 | Following 2.3.1.5. | Undertake action requested by AMVLP or Supplier or if no response provided by AMVLP or Supplier apply the rules defined in Appendix 3.1. | HHDC. |  |  | Internal Process. |
| 2.3.1.7 | If no response received from AMVLP or Supplier and following 2.3.1.6. | Report any occurrences where estimated consumption data used because energy recorded exceeds that allowed and AMVLP or Supplier has not provided an appropriate course of action. | HHDC. | BSCCo. | P0208 Estimation Due To High Energy Recorded. | Manual. |
| 2.3.1.8 | Where required. | Provide operational data or additional information where the exceptions identified in Appendix 3.2 are met. | AMVLP<br>or<br>Supplier. |  | HHDC.<br>In accordance with Appendix 3.2. | Electronic or other method, as agreed. |
| 2.3.1.9 | When data is invalid or cannot be retrieved or if requested by AMVLP or Supplier to estimate consumption or if energy exceeds that allowed by more than the limit defined in 2.3.1.4. | Estimate consumption data.<br>Send estimated consumption data report.<br>HHDC. | AMVLP<br>or<br>Supplier |  | Refer to Appendix 3.2.<br>D0022 Estimated Half Hourly Data Report.<br>Internal Process. | Electronic or other method, as agreed. |
| 2.3.1.10 | Prior to next Volume Allocation Run | Validate consumption data for estimated data and actual data where not done in 2.3.1.1.<br>Send valid consumption data39 | HHDC | HHDC<br>SVAA<br>AMVLP<br>or<br>Supplier | Refer to Appendix 3.1.<br>D0390 ‘Asset Metering System Half Hourly Metered Data’40<br>Internal Process | Electronic or other method, as agreed. |
| 2.3.1.11 | 2WDs Before invoking run | Where available: Load and validate incoming HHDC files.<br>If D0390 file expected but not received or if estimated data41 has been received, ask HHDC to send file with actual data. | OR<br>If file fails any validation check for reasons other than standing data mismatch, ask HHDC to assess if file is valid. | SVAA<br>SVAA<br>SVAA<br>HHDC<br>AMVLP<br>or<br>Supplier<br>HHDC | P0310 Missing Metering System Data<br>P0311 Invalid Metering System Data<br>Internal Process<br>Electronic or other method, as agreed. | Electronic or other method, as agreed |
| 2.3.1.12 | Within 2 working hours of notification received from SVAA. | If file is valid, notify the SVAA via a BSC Service Desk call; or<br>Send corrected file to SVAA. Where corrected file sent to SVAA also send to AMVLP or Supplier. | HHDC | SVAA<br>AMVLP<br>or<br>Supplier | D0390 ‘Asset Metering System Half Hourly Metered Data’ | Electronic or other method, as agreed. |
| 2.3.1.13 | On receipt of a corrected file up until the Volume Allocation Run is invoked | Re-load and validate HHDC file | SVAA |  |  | Internal Process |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

#### 2.3.2 HHDC receives Half Hourly data from the AMHHDC, processes and sends consumption data for an Asset Metering System

Where the HHDC receives Half Hourly data from the AMHHDC, processes and sends consumption data for an Asset Metering System.

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.3.2.1 | As required | Collect and validate Half Hourly Metered Data from an Asset Metering System.<br>Data from the Asset Meter shall be retrieved as soon as possible before historical data is overwritten.<br>This can be data in other formats where it can be converted to Half Hourly Metered Data by the AMHHDC. | AMHHDC |  | Refer to Appendix 3.1, Appendix 3.2, Appendix 3.3, and where relevant Appendix 3.8. | Internal Process |
| 2.3.2.2 | Following 2.3.2.1 and in accordance with timescales in Appendix 3.1 and 3.8 | Provide relevant reports | AMHHDC | AMVLP<br>or<br>Supplier<br>SVA MOA<br>or<br>AMMOA | Refer to Appendix 3.1 and where relevant Appendix 3.8.<br>D0008 Meter Advance Reconciliation Report in accordance with Appendix 3.8 | Electronic or other method, as agreed. |
| 2.3.2.3 | When fault suspected with Metering or communications equipment. | Investigate and report any faults detected. | AMHHDC |  | Refer to Section 2.3.3 | Internal Process |
| 2.3.2.4 | Within 2 WD of detecting consumption on de-energised Metering or if maximum permissible energy exceeds that allowed. | Report any consumption detected on de-energised Metering and escalate any occurrences where the energy recorded, for any Settlement Period, exceeds the maximum permissible on energised metering.<br>AMHHDC. | AMVLP<br>or<br>Supplier | SVA MOA<br>or<br>AMMOA | Refer to Appendix 3.1<br>D0001 Request Metering System Investigation.<br>Internal Process. | Electronic or other method, as agreed. |
| 2.3.2.5 | When maximum permissible energy exceeds that allowed. | Send notification of action to be taken.<br>AMVLP. | or<br>Supplier |  | AMHHDC.<br>D0005 Instruction on Action.<br>The AMHHDC will be instructed to validate the actual data or to replace the actual data with estimated successfully validated data. | Electronic or other method, as agreed. |
| 2.3.2.6 | Following 2.3.2.5. | Undertake action requested by AMVLP or Supplier or if no response provided by AMVLP or Supplier apply the rules defined in Appendix 3.1. | AMHHDC. |  |  | Internal Process. |
| 2.3.2.7 | If no response received from AMVLP or Supplier and following 2.3.2.6. | Report any occurrences where estimated consumption data used because energy recorded exceeds that allowed and AMVLP or Supplier has not provided an appropriate course of action. | AMHHDC. | BSCCo. | P0208 Estimation Due To High Energy Recorded. | Manual. |
| 2.3.2.8 | Where required. | Provide operational data or additional information where the exceptions identified in Appendix 4.2A are met. | AMVLP<br>or<br>Supplier. |  | AMHHDC.<br>In accordance with Appendix 3.2. | Electronic or other method, as agreed. |
| 2.3.2.9 | When data is invalid or cannot be retrieved or if requested by AMVLP or Supplier to estimate consumption or if energy exceeds that allowed by more than the limit defined in 2.3.2.4. | Estimate consumption data.<br>Send estimated consumption data report.<br>AMHHDC. | AMVLP<br>or<br>Supplier |  | Refer to Appendix 3.2.<br>D0022 Estimated Half Hourly Data Report.<br>Internal Process. | Electronic or other method, as agreed. |
| 2.3.2.10 | 3WD prior to next Volume Allocation Run | Validate consumption data for estimated data and actual data where not done in 2.3.2.1<br>Send valid consumption data42<br>Where issue with data suspected and data estimated notify HHDC of the nature of the issue | AMHHDC | AMHHDC<br>HHDC | Refer to Appendix 3.1<br>D0390 ‘Asset Metering System Half Hourly Metered Data’<br>P0313 Consumption Data Issue Notification<br>Internal Process | Electronic or other method, as agreed. |
| 2.3.2.11 | Following 2.3.2.10 | If D0390 file expected but not received or if estimated data43 has been received, ask AMHHDC to send file with actual data | HHDC | AMHHDC | P0310 Missing Metering System Data | Electronic or other method, as agreed. |
| 2.3.2.12 | Within 2 working hours of notification received from HHDC. | Where possible send valid consumption data<br>Where P0313 has not been sent in 2.3.2.10 where issue with data suspected and data estimated notify HHDC of the nature of the issue | AMHHDC | HHDC | D0390 ‘Asset Metering System Half Hourly Metered Data’<br>P0313 Consumption Data Issue Notification | Electronic or other method, as agreed |
| 2.3.2.13 | Prior to next Volume Allocation Run | Send valid consumption data44 | HHDC | SVAA<br>AMVLP<br>or<br>Supplier | D0390 ‘Asset Metering System Half Hourly Metered Data’45 | Electronic or other method, as agreed. |
| 2.3.2.14 | 2WDs Before invoking run | Where available: Load and validate incoming HHDC files.<br>If D0390 file expected but not received or if estimated data46 has been received, ask HHDC to send file with actual data. | OR<br>If file fails any validation check for reasons other than standing data mismatch, ask HHDC to assess if file is valid. | SVAA<br>SVAA<br>SVAA<br>HHDC<br>AMVLP<br>or<br>Supplier<br>HHDC<br>AMVLP | P0310 Missing Metering System Data<br>P0311 Invalid Metering System Data<br>Internal Process<br>Electronic or other method, as agreed. | Electronic or other method, as agreed |
| 2.3.2.15 | Within 2 working hours of notification received from SVAA. | If file is valid, notify the SVAA via a BSC Service Desk call. Where the fault is continuous the HHDC is only required to raise one BSC Service Desk call and not one for each day or for each impacted Settlement Run; or<br>Send corrected file to SVAA. Where corrected file sent to SVAA also send to AMVLP or Supplier. | HHDC | SVAA<br>AMVLP<br>or<br>Supplier | D0390 ‘Asset Metering System Half Hourly Metered Data’ | Electronic or other method, as agreed. |
| 2.3.2.16 | On receipt of a corrected file up until the Volume Allocation Run is invoked | Re-load and validate HHDC file | SVAA |  |  | Internal Process |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

#### 2.3.3 HHDC or AMHHDC investigates inconsistencies

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.3.3.1 | As required | Send notification of inconsistencies.<br>Any Participant | AMVLP<br>or<br>Supplier |  | Details of inconsistencies (e.g. invalid data, faulty Metering, invalid Meter Technical Details etc.).<br>P0316 Details of Asset Metering Fault | Electronic or other method, as agreed. |
| 2.3.3.2 | Within 2 WD of 2.3.3.1 (if applicable), or as required | Send notification of inconsistencies and request investigation. | AMVLP<br>or<br>Supplier | HHDC<br>AMHHDC | (as applicable)<br>D0001 Request Metering System Investigation | Electronic or other method, as agreed. |
| 2.3.3.3 | Within 5 WD of 2.3.3.2 | Investigate inconsistencies.<br>Take corrective action if possible.<br>Go to 2.3.3.4 if an Asset Metering System investigation is required OR<br>Go to 2.3.3.5 if inconsistencies have been resolved and an Asset Metering System investigation was not required OR<br>Go to 2.3.3.10 if inconsistencies remain unresolved and an Asset Metering System investigation was not required. | HHDC | AMHHDC | (as applicable) | Internal Process |
| 2.3.3.4 | Following 2.3.3.3 | Initiate process in Section 2.4 | HHDC | AMHHDC | (as applicable) |  |
| 2.3.3.5 | Within 5 WD of resolution of inconsistencies | Report resolution of inconsistencies. | HHDC<br>or<br>AMHHDC | AMVLP<br>or<br>Supplier | D0002 Fault Resolution Report or Request for Decision on Further Action | Electronic or other method, as agreed. |
| 2.3.3.6 | Within 5 WD of 2.3.3.5 | Report resolution of inconsistencies. | AMVLP<br>or<br>Supplier |  | Relevant Participant<br>D0002 Fault Resolution Report or Request for Decision on Further Action | Electronic or other method, as agreed. |
| 2.3.3.7 | If appropriate, following 2.3.3.5 | If a problem has caused incorrect consumption to be recorded correct consumption data.<br>If AMHHDC collects data continue to 2.3.3.8 or<br>If HHDC collects data directly continue to 2.3.3.9 | HHDC | AMHHDC | (as applicable)<br>Refer to Appendix 3.2 | Internal Process |
| 2.3.3.8 | As soon as possible following 2.3.3.7 | Send corrected data<br>As required where data estimated, send estimated consumption data report | AMHHDC | AMHHDC<br>HHDC<br>AMVLP<br>or<br>Supplier | D0390 ‘Asset Metering System Half Hourly Metered Data’<br>D0022 Estimated Half Hourly Data Report.<br>Electronic or other method, as agreed. | Electronic or other method, as agreed. |
| 2.3.3.9 | As soon as possible following 2.3.3.7 or 2.3.3.8 as applicable | Send corrected data<br>As required where data estimated, and where HHDC communicates directly with Asset Meter directly send estimated consumption data report.<br>For AMSIDs registered in LPAMR, the consumption data should be sent to the AMVLP only. | HHDC | HHDC<br>SVAA<br>AMVLP<br>or<br>Supplier<br>AMVLP<br>or<br>Supplier | D0390 ‘Asset Metering System Half Hourly Metered Data’<br>D0022 Estimated Half Hourly Data Report.<br>Electronic or other method, as agreed. | Electronic or other method, as agreed. |
| 2.3.3.10 | Following 2.3.3.3 and as soon as possible, if inconsistencies remain unresolved but an Asset Metering System investigation was not required. | Report action required | HHDC<br>or<br>AMHHDC | AMVLP<br>or<br>Supplier | AMSID;<br>Details of Action Required;<br>P0317 Report Action Required | Electronic or other method, as agreed. |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 2.4 Meter Operation Activities for Asset Metering Systems

#### 2.4.1 Asset Metering System Investigation Process

Where an AMVLP or Supplier has requested that an Asset Metering System is to be investigated for an AMSID for Asset Metering Types4 1, 2 and 3 the Meter Operator activities shall be done by a SVA MOA; for Asset Metering Types 4 and 5 the AMVLP or Supplier can choose to appoint a SVA MOA or an AMMOA.

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.4.1.1 | As required | Send request to investigate an Asset Metering System<br>Any Participant47 | AMVLP<br>or<br>Supplier |  | Details of fault<br>P0316 Details of Asset Metering Fault | Electronic or other method, as agreed. |
| 2.4.1.2 | Within 2 WD of 2.4.1.1 or as required | Send request to investigate an Asset Metering System | AMVLP<br>or<br>Supplier | HHDC<br>or | AMHHDC (if applicable) 48<br>SVA MOA<br>or<br>AMMOA<br>D0001 Request Metering System Investigation | Electronic or other method, as agreed. |
| 2.4.1.3 | Within 5 WD of 2.4.1.2 | Investigate Asset Metering System.<br>Attempt to resolve fault. | SVA MOA<br>or<br>AMMOA |  |  | Internal Process |
| 2.4.1.4 | As required following 2.4.1.3 | If the resolution involves a site visit, take a register reading of the Asset Meter (if possible). Following resolution of the fault. | SVA MOA<br>or<br>AMMOA | HHDC<br>or<br>AMHHDC | D0010 Meter Readings | Electronic or other method, as agreed. |
| 2.4.1.5 | If fault resolved within 5 WD of receipt of notification in 2.4.1.2 | Go to 2.4.1.13 | Note nature of fault | SVA MOA | or | AMMOA |
| 2.4.1.6 | If fault remains unresolved 5 WD after receipt of notification in 2.4.1.2 | Send notification that the fault cannot be resolved within 5WD, and send a corresponding fault resolution plan (if required) detailing the actions that need to be taken to resolve the fault and the proposed timescales or update on proposed next steps. Request decision on further action if appropriate49. | SVA MOA<br>or<br>AMMOA | HHDC<br>or<br>AMHHDC<br>or<br>AMVLP<br>or<br>Supplier | (as appropriate)<br>D0005 Instruction on Action50<br>Or equivalent communication, by other means, with the AMVLP or Supplier..<br>Fault resolution plan (if required). | Electronic or other method, as agreed. |
| 2.4.1.7 | As soon as possible after 2.4.1.6, if appropriate | Send decision on further action | HHDC<br>or<br>AMHHDC<br>or<br>AMVLP<br>or<br>Supplier |  | (as appropriate)<br>SVA MOA<br>or<br>AMMOA<br>D0005 Instruction on Action<br>Or equivalent communication, by other means, with the AMVLP or Supplier. | Electronic or other method, as agreed. |
| 2.4.1.8 | Following 2.4.1.6 or 2.4.1.7, as applicable | Attempt to resolve fault | SVA MOA<br>or<br>AMMOA |  |  | Internal Process |
| 2.4.1.9 | If fault resolved within 15WD of receipt of notification in 2.4.1.2 | Go to 2.4.1.13 | SVA MOA<br>or<br>AMMOA |  |  | Internal Process |
| 2.4.1.10 | If fault remains unresolved 15WD after receipt of notification in 2.4.1.2 | Notify that the fault remains unresolved | SVA MOA<br>or<br>AMMOA | HHDC<br>or<br>AMHHDC<br>or<br>AMVLP<br>or<br>Supplier | (as appropriate)<br>D0005 Instruction on Action<br>Or equivalent communication, by other means, with the AMVLP or Supplier. | Electronic or other method, as agreed. |
| 2.4.1.11 | As soon as possible following 2.4.1.10 | Progress resolution of outstanding fault | SVA MOA<br>or<br>AMMOA |  | As appropriate:<br>D0005 Instruction on Action<br>Fault resolution plan | Internal Process |
| 2.4.1.12 | If and when appropriate following 2.4.1.11 | Consult and / or update HHDC or AMHHDC, or AMVLP or Supplier as appropriate, regarding investigation on regular basis (as agreed) until fault resolved. | SVA MOA<br>or<br>AMMOA | HHDC<br>or<br>AMHHDC<br>or<br>AMVLP<br>or<br>Supplier | (as appropriate)<br>D0005 Instruction on Action<br>Or equivalent communication, by other means, with the AMVLP or Supplier. | Electronic or other method, as agreed. |
| 2.4.1.13 | Within 5 WD of resolving fault | Send fault resolution report and undertake any steps in Section 2.2.4 which may be appropriate. | SVA MOA<br>or<br>AMMOA | AMVLP<br>or<br>Supplier<br>HHDC<br>or<br>AMHHDC | D0002 Fault Resolution Report or Request for Decision on Further Action | Electronic or other method, as agreed. |
| 2.4.1.14 | Within 5 WD of 2.4.1.13 | Report resolution of fault | AMVLP<br>or<br>Supplier |  | Relevant Participant (instigator in 2.4.1.1)<br>D0002 Fault Resolution Report or Request for Decision on Further Action<br>Details of resolution | Electronic or other method, as agreed. |
| 2.4.1.15 | If appropriate, at the same time as 2.4.1.13 | Send Meter Technical Details if changed or corrected | SVA MOA<br>or<br>AMMOA | HHDC<br>or<br>AMHHDC (if applicable)<br>AMVLP<br>or<br>Supplier | D0268 Half Hourly Meter Technical Details<br>If site is Complex, send Asset Metering Complex Site Supplementary Information Form. Refer to Appendix 3.9 Guide to Asset Metering Complex Sites; | Electronic or other method, as agreed. |
| 2.4.1.16 | If appropriate and within 10 WD of resolving fault | Send the relevant Asset Meter information.<br>This does not apply for Asset Meters registered in LPAMR. | AMVLP<br>or<br>Supplier | SVAA | P0303 Asset Meter Registration | Electronic or other method, as agreed. |
| 2.4.1.17 | Immediately following 2.4.1.16 or 2.4.1.18 | Perform validation checks and send response<br>If response is “Accepted”, proceed to 2.4.1.19, otherwise proceed to 2.4.1.17. | SVAA | AMVLP<br>or<br>Supplier | P0304 Rejection of Asset Meter Registration<br>Or<br>P0305 Confirmation of Asset Meter Registration | Electronic or other method, as agreed. |
| 2.4.1.18 | Within 5 WD of 2.4.1.17 | This step does not apply for Asset Meters registered in LPAMR.<br>Where the rejection is of a type the AMVLP or Supplier can resolve without involving other industry parties, send a corrected flow.<br>Proceed to 2.4.1.17<br>If the AMVLP or Supplier needs to involve other industry parties to resolve the issue, then reasonable endeavours should apply. Notify SVA MOA or AMMOA of rejection reasons and request new D0268.<br>Proceed to 2.4.1.15 | AMVLP<br>or<br>Supplier | AMVLP<br>or<br>Supplier<br>SVAA<br>SVA MOA<br>or<br>AMMOA | P0303 Asset Meter Registration<br>P0304 Rejection of Asset Meter Registration<br>Electronic or other method, as agreed. | Electronic or other method, as agreed. |
| 2.4.1.19 | In accordance with timescales in Appendix 3.6.5 | Carry out a Proving Test on the Asset Metering System in accordance with Section 2.5, Appendix 3.6 and Code of Practice Eleven. | SVA MOA<br>or<br>AMMOA | HHDC<br>AMHHDC (if applicable) | Refer to Appendix 3.6 | Internal Process |
| 2.4.1.20 | If appropriate, following 2.4.1.13 | If a problem has caused incorrect consumption to be recorded correct consumption data.<br>If AMHHDC collects data continue to 2.4.1.21 or<br>If HHDC collects data directly continue to 2.4.1.22 | HHDC | AMHHDC (if applicable) | Refer to Appendix 3.2 | Internal Process |
| 2.4.1.21 | As soon as possible following 2.4.1.20 | Send corrected data<br>As required where data estimated, send estimated consumption data report<br>Continue to 2.4.1.22 | AMHHDC | AMHHDC<br>HHDC<br>AMVLP<br>or<br>Supplier | D0390 ‘Asset Metering System Half Hourly Metered Data’<br>D0022 Estimated Half Hourly Data Report.<br>Electronic or other method, as agreed. | Electronic or other method, as agreed. |
| 2.4.1.22 | As soon as possible following 2.4.1.20 or 2.4.1.22 as applicable | Send corrected data<br>As required where data estimated, and where HHDC communicates directly with Asset Meter directly send estimated consumption data report.<br>For AMSIDs registered in LPAMR, the valid consumption data should be sent to the AMVLP only. | HHDC | HHDC<br>SVAA<br>AMVLP<br>or<br>Supplier | D0390 ‘Asset Metering System Half Hourly Metered Data’<br>D0022 Estimated Half Hourly Data Report.<br>Electronic or other method, as agreed. | Electronic or other method, as agreed. |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 2.5 Proving an Asset Metering System

#### 2.5.1 Basic Proving Test

For Half Hourly Integral Outstation integral Meters which can only have a pulse multiplier of one as identified on the Elexon website (compliance and protocol approval list), a proving test is not required. All other Asset Metering Systems shall complete a Proving Test for an AMSID. This shall be for new installations (see Section 2.1.1) and where an Asset Metering System is reconfigured or replaced (see Section 2.2.4).

For Asset Metering Types4 1, 2 and 3 Meter Operator activities shall be done by a SVA MOA; for Asset Metering Types 4 and 5 the AMVLP or Supplier can choose to appoint a SVA MOA or an AMMOA.

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.5.1.1 | As required | When Asset Metering System is installed, existing Metering System used as an Asset Metering System, reconfigured or replaced commission to Section 2.1.2 and Code of Practice Eleven, record Asset Meter Technical Details and carry out a Proving Test in accordance with Code of Practice Eleven and Appendix 3.6.<br>(Refer to Appendix 3.6) | SVA MOA<br>or<br>AMMOA |  |  | Internal Process |
| 2.5.1.2 | Following 2.5.1.1 | Send request for Proving Test (indicating which Settlement Periods to be collected) | SVA MOA<br>or<br>AMMOA | HHDC<br>AMHHDC (if applicable) | D0268 Half Hourly Meter Technical Details<br>D0005 Instruction on Action<br>Date and time of Settlement Periods to be collected;<br>If site is Complex, send Asset Metering Complex Site Supplementary Information Form. Refer to Appendix 3.9 Guide to Asset Metering Complex Sites; | Electronic or other method, as agreed. |
| 2.5.1.3 | Following 2.5.1.2 | Download Asset Meter for the same Half Hourly Settlement Period as requested by the MOA.<br>If Asset Meter downloaded directly by HHDC continue to 2.5.1.5 | HHDC<br>or<br>AMHHDC (if applicable) |  | As a minimum the HHDC or AMHHDC shall collect the data required by the SVA MOA or AMMOA, but may also collect and send more data than requested. | Internal Process |
| 2.5.1.4 | Following 2.5.1.3 | Send raw Half Hourly Metered Data or notification that Metered Data cannot be collected for the Settlement Periods requested49.<br>If unable to collect Metered Data for Settlement Period requested, send alternative Settlement Period Half Hourly Metered Data. | HHDC<br>or<br>AMHHDC (if applicable) | SVA MOA<br>or<br>AMMOA | D0003 Half Hourly Advances<br>OR<br>D0001 Request Metering System Investigation | Electronic or other method, as agreed. |
| 2.5.1.5 | Following 2.5.1.4 | If data received from HHDC or AMHHDC (if applicable), proceed to 2.5.1.6 to undertake a comparison and issue the results.<br>If data not received from HHDC or AMHHDC (if applicable) proceed to 2.5.1.2 to undertake a re-test | SVA MOA<br>or<br>AMMOA |  |  | Internal Process |
| 2.5.1.6 | Following 2.5.1.5 and receipt of data from HHDC or AMHHDC | Compare SVA MOA or AMMOA Half Hourly Metered Data with HHDC or AMHHDC Half Hourly Metered Data for the same Settlement Period. | SVA MOA<br>or<br>AMMOA |  |  | Internal Process |
| 2.5.1.7 | Following 2.5.1.6 and where Proving Test is successful and in accordance with timescales in Appendix 3.6.5 | Send notification of successful Proving Test | SVA MOA<br>or<br>AMMOA | HHDC<br>or<br>AMHHDC (if applicable) | D0214 Confirmation of Proving Tests | Electronic or other method, as agreed. |
| 2.5.1.8 | Following 2.5.1.6 and where Proving Test is unsuccessful and in accordance with timescales in Appendix 3.6.5 | Send notification that Proving Test failed | SVA MOA<br>or<br>AMMOA | HHDC<br>or<br>AMHHDC (if applicable) | D0002 Fault Resolution Report or Request for Decision on Further Action | Electronic or other method, as agreed. |
| 2.5.1.9 | Following 2.5.1.8 and in accordance with timescales in Appendix 3.6.5 | Investigate problem and take corrective action. | SVA MOA<br>or<br>AMMOA |  |  | Internal Process |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

## 3 APPENDICES

### 3.1 Validate Meter Data for Asset Metering Systems

Where the HHDC dials the Asset Meter directly it is responsible for these validation checks. Where the AMHHDC dials the Asset Meter it is responsible for these validation checks.

Unless the HHDC or AMHHDC is informed by the SVA MOA or AMMOA that the retrieved data is incorrect, the HHDC or AMHHDC shall accept Meter Period Value data collected from the Asset Meter for validation processing.

The HHDC and AMHHDC shall record all occurrences where data entering Settlements has been changed following instruction from the AMVLP or Supplier.

The HHDC and AMHHDC shall retain the original reading value along with any alarms recorded in the Asset Meter, the reason for failure where the value is invalid and the reason for accepting data previously flagged as suspect.

The data retrieval process shall include the following checks; however in the case where data is received from the Outstation automatically step 3.1.3 ‘Outstation Time’ shall be performed at least every 20 calendar days by interrogation only.

#### 3.1.1 Asset Meter Id (Device Id)

When the Asset Meter is interrogated by the HHDC or AMHHDC (as applicable), or when data is received from the Asset Meter the ‘electronic serial number’ of the Asset Meter is compared with that expected. If they differ then no data is collected (or processed further) and the failure is investigated in accordance with section 2.3.3.

#### 3.1.2 Asset Meter Number of Channels

When the Asset Meter is interrogated by the HHDC or AMHHDC (as applicable), or when data is received from the Asset Meter automatically, the number of channels of the Asset Meter is compared with that expected. If they differ then no data is collected (or processed further) and the failure is investigated in accordance with section 2.3.3.

#### 3.1.3 Asset Meter Time

When the Asset Meter is interrogated, by the HHDC or AMHHDC (as applicable) the time of the Asset Meter is compared with that expected. If they differ by more than 20 seconds and less than 15 minutes then the outstation time is corrected by the data collection system. If the time differs by more than 15 minutes then the problem is resolved in accordance with section 2.3.3.

#### 3.1.4 Alarms

When the Asset Meter is interrogated by the HHDC or AMHHDC (as applicable), or when data is received from the Asset Meter automatically, the individual alarms shall be investigated if flagged. Half Hourly Integral Outstation Meters will have alarms but other Asset Meters may not have alarm flag functionality.

Each alarm shall be investigated in accordance with section 2.3.3.

#### 3.1.5 Cumulative/Total Consumption Comparison

When the Asset Meter is interrogated by the HHDC or AMHHDC (as applicable), or when data is received from the Asset Meter automatically, and where the Asset Meter provides an electronic cumulative reading of the prime register equivalent to the total consumption of the Asset Meter at that point in time. Using these readings, the following checks will be performed at least every seven days (i.e. on a daily or weekly basis or as agreed by the AMVLP or Supplier and HHDC, or AMHHDC).

i) The difference between the cumulative readings shall be calculated to ensure that the HH Metered Data used in Settlements sums to the Asset Meter advance for the same interval51, i.e. that the difference between cumulative readings and the sum of the Metered Period Data for the same date(s) and time(s) is within a suitable tolerance. It is recommended that the level of the tolerance should be set to take into account the period over which the check was performed. The recommended maximum levels are ±0.7% where the check is carried out on a weekly basis and ±5% where the check is carried out on a daily basis.

Specifically:

Σ(pulses * pulse multiplier) for all Asset Meter periods in the time interval = (Asset Meter advance * Asset Meter multiplier) for the time interval.

The calculation below outlines how the discrepancy should be calculated when performing tolerance checks.

*[Diagram/image in the original web page was not captured in the copy-paste.]*

Where:

∑HHE is the sum of HH Energy volumes in kWh; and MA is the corresponding Asset Meter Advance, i.e.

MA = M2 – M1

Where:

M2 is the cumulative reading (in kWh) returned from the last time that the Asset Meter was interrogated; and M1 is the cumulative reading (in kWh) returned from the previous time that the Asset Meter was interrogated or data was received automatically over the same time period as the sum of HH period energy.

ii) Where a main and check Asset Meter is fitted, the main and check Asset Meter advances are compared for any discrepancy between the two values in excess of 1.5 times the class accuracy requirements for the individual Asset Meters at full load, as defined in the CoP 11 for the relevant Asset Metering Type.

Allowances shall be made for low load discrepancies. If the discrepancy is unacceptable it shall be investigated in accordance with section 2.3.3.

#### 3.1.6 Maximum Permissible Energy by Metering System Code of Practice Eleven

During validation by the HHDC or AMHHDC (as applicable), where the energy recorded exceeds the permissible allowed, in accordance with column 4 in the table below, for one or more given Settlement Period, the HHDC or AMHHDC (as applicable) will notify the AMVLP or Supplier.

CoP11 Asset Metering Type

Max. kW

Max kWh / Half Hour

Permissible Allowed:

kWh per Half Hour

1

675,000

337,500

400,000

2

100,000

50,000

50,000

3

10,000

5,000

5,000

4

1,000

500

600

5

100

50

50

Following instruction from the AMVLP or Supplier, the AMHHDC or HHDC (as applicable) will enter the actual data into Settlements or the HHDC or AMHHDC (as applicable) will replace the actual data with estimated data and enter this into Settlements.

Where however the AMVLP or Supplier does not provide instructions to the HHDC or AMHHDC (as applicable), the HHDC or AMHHDC (as applicable) will apply the following rules, either:

use actual consumption data if the energy has exceeded the permissible allowed by no more than 20%; or

use estimated consumption data, rather than the actual consumption data if the energy exceeded the permissible allowed by more than 20%.

Note that:

Asset Metering Types 1, 2 and 3 are circuit capacity based and it is assumed that the Maximum Demand will not exceed the maximum kWh / Half Hour value.

Asset Metering Types 4 and 5 are demand based and may occasionally exceed the maximum kWh / Half Hour value.

#### 3.1.7 Main/Check Comparison

Where main and check Asset Meters are installed the HHDC or AMHHDC (as applicable), ensure that the Metered Data recorded by each Asset Meter is compared for each circuit. Allowance shall be made for low load discrepancies. Any discrepancy between the two values in excess of 1.5 times the accuracy requirements of that prescribed for the individual Asset Meters at full load, as defined in the CoP 11 for the relevant Asset Metering Type, shall be investigated in accordance with section 2.3.3.

#### 3.1.8 Site Checks of Asset Metering System - Site Visit Report

The following checks shall be carried out by the HHDC or AMHHDC (as applicable) on the Asset Metering System when visiting a Site:

1.

Any evidence of suspected faults to the Asset Metering System including phase/fuse failure.

2.

Any evidence of damage to Metering and associated equipment.

3.

Any evidence of tampering of any sort with the Asset Metering System or associated equipment, particularly seals.

4.

Any evidence of supply being taken when the Asset Meters are de-energised.

NB The Local Interrogation Unit (IU) or Hand Held Unit (HHU) should be set to ensure agreement with the UTC clock at least every week.

For Asset Metering Types 1, 2, 3 and 4 sites with polyphase Asset Metering Systems should be visited at least annually, Asset Metering Type 5 and single phase at least at two yearly intervals to perform the checks described above. Site visits made for other reasons may be used to carry out these checks.

Any problems are investigated in accordance with section 2.3.3 and a report is issued. The HHDC or AMHHDC (as applicable) shall ensure that where a site visit was not possible, the reasons are explained sufficiently such that appropriate action can be taken to improve the chances of securing a successful site visit.

#### 3.1.9 Reporting

Ensure that all cases of suspected Asset Metering Systems faults are investigated in accordance with section 2.3.3 and are reported to the AMVLP or Supplier and SVA MOA or AMMOA, as appropriate.

Ensure that the original metered value (where obtained) and alarm(s), together with the reason for the changes to that value are retained.

### 3.2 Data Estimation for Asset Metering Systems

Where an AMHHDC has been appointed, they will perform the estimation and the HHDC will not be required to do so. The HHDC will perform the estimation only where they communicate with the Asset Meter directly.

Active Energy data will be estimated for Asset Import and Asset Export Metering using one of the following data estimation methods in the order of precedence specified below. Data will be flagged appropriately as indicated below.

No estimation is required for Reactive Energy.

When the HHDC or AMHHDC (as applicable) receives information from the SVA MOA or AMMOA, site reports or other sources concerning Metered data which has been or will be collected and processed, the Meter Period Value data shall be estimated in accordance with this BSCP where the HHDC or AMHHDC (as applicable) believes the data to be in error. The HHDC or AMHHDC (as applicable) shall inform the AMVLP or Supplier where an error might affect a different AMVLP or Supplier or data affects the Final Reconciliation Volume Allocation Run.

The HHDC or AMHHDC (as applicable) shall retain any original value collected, whether such value is processed before or after receipt of any details of invalid data from the SVA MOA or AMMOA, site reports or other source, and any alarms set up at the Asset Meter.

Details of all data estimations and the rationale behind using the chosen method must be recorded for Audit purposes.

The HHDC or AMHHDC (as applicable) will notify the relevant AMVLP or Supplier of the data estimation method in accordance with 3.2.3 below.

HHDCs and AMMHDCs should consider local information, where available, when carrying out estimations. Where no instruction or additional information has been received from the AMVLP or Supplier missing data should be estimated to zero in techniques d. and e. in 3.2.1 and 3.2.2.

Having estimated data using one of the methods below, a report is to be produced in accordance with 3.2.3 below.

If a data estimation has been completed and submitted to the SVAA and actual ‘A’ flag data OR information leading to more accurate estimated data becomes available, this revised data shall be notified to the AMVLP or Supplier and submitted to the SVAA for use in the next Volume Allocation Run.

Where a MAR has failed, in accordance with Appendix 3.8, due to a data estimation being included in the period of reconciliation, that period of data estimation shall be re-estimated.

#### 3.2.1 Standard Methods – Import Metering Systems

a. Main Asset Meter data available but check Meter data missing.

Data from main Asset Meter used.

Data Flag ‘A’

b. Main Asset Meter data missing and check Asset Meter installed.

Data copied from the check Asset Meter.

Data Flag ‘A’

c. One Settlement Period missing or incorrect where a prime Asset Meter register reading can be taken.

Missing or incorrect Settlement Period data calculated from the prime Asset Meter register advance and the other actual HH data recorded for the specific period of the calculation. Note that the prime Asset Meter register advance will not correlate to Settlement Periods.

Data Flag ‘A’

d. Asset Meter advance available.

Operational data or additional information will be used in conjunction with Asset Meter reading advance to construct the profile supplied from another source (SVA MOA or AMMOA, AMVLP or Supplier). Information to be supplied by the AMVLP or Supplier to the HHDC or AMHHDC (as applicable) in a format agreed by both parties.

Data Flag ‘E’ except where the data is automatically retrieved by the SVA MOA or AMMOA via an Interrogation Unit, in which case it will have an ‘A’ flag.

e. Asset Meter advance unavailable.

Operational data or additional information will be used to construct the kWh consumption load shape supplied from another source (SVA MOA or AMMOA, AMVLP, Supplier). Information to be supplied by the AMVLP or Supplier to the HHDC or AMHHDC (as applicable) in a format agreed by both parties. The operational data or additional information submitted must include evidence that overlaps actual data held by the HHDC or AMHHDC (as applicable) that will be used as a validation check on the information submitted.

Data Flag ‘E’

f. Where none of the above methods can be utilised missing data shall be estimated to zero for the Initial Volume Allocation run.

Data Flag ‘E’

#### 3.2.2 Standard Methods – Export Metering Systems

a. Main Asset Meter data available but check Asset Meter data missing.

Data from main Meter used.

Data Flag ‘A’

b. Main Asset Meter data missing and check Asset Meter installed.

Data copied from the check Meter.

Data Flag ‘A’

c. One Settlement Period missing or incorrect where a prime Asset Meter register reading can be taken.

Missing or incorrect Settlement Period data calculated from the prime Asset Meter register advance and the other actual HH data recorded for the specific period of the calculation. Note that the prime Asset Meter register advance will not correlate to Settlement Periods.

Data Flag ‘A’

d. Asset Meter advance available

Operational data or additional information will be used in conjunction with Asset Meter reading advance to construct the profile supplied from another source (SVA MOA or AMMOA, AMVLP Supplier). Information to be supplied by the AMVLP or Supplier to the HHDC or AMHHDC (as applicable) in a format agreed by both parties.

Or

Where the HHDC or AMHHDC (as applicable) determines that the export is predictable then the HHDC or AMHHDC (as applicable) shall use the average of four weeks of surrounding data in conjunction with the Asset Meter reading advance.

Data Flag ‘E’ except where the data is automatically retrieved by the SVA MOA or AMMOA via an Interrogation Unit, in which case it will have an ‘A’ flag.

e. Asset Meter advance unavailable

Operational data or additional information will be used to construct the profile supplied from another source (SVA MOA or AMMOA, AMVLP, Supplier). Information to be supplied by the AMVLP or Supplier to the HHDC or AMHHDC (as applicable) in a format agreed by both parties. The operational data or additional information submitted must include evidence that overlaps actual data held by the HHDC or AMHHDC (as applicable) that will be used as a validation check on the information submitted.

Data Flag ‘E’

f. Where none of the above methods can be utilised missing data shall be estimated to zero for the Initial Volume Allocation run.

Data Flag ‘E’

#### 3.2.3 Reporting

For Asset Metering Systems, the report identifies all Asset Metering Systems for which Asset Meter period estimated data (‘E’ flag data only) has been used, showing the dates and Settlement Periods affected. The HHDC or AMHHDC (as applicable) will additionally provide full details of the data estimation method used to the AMVLP or Supplier (this information may be provided by any method agreed with the AMVLP or Supplier).52

3.3 Process Meter Data.

3.3.1 Where there is more than one Asset Meter for an AMSID, total the Asset Meter period data by Measurement Quantity.

3.3.2 Where one or more Asset Meter, period values for a Measurement Quantity is estimated, the Status of the totalled value shall be set to “estimated”.

3.3.3 For Asset Metering Systems, the AMHHDC shall send the totalled active data to the HHDC according to the Settlement Timetable:

for the Initial Volume Allocation the AMHHDC sends data for all Asset Meter periods for all relevant AMSIDs; the data may be actual or estimated.

for subsequent reconciliation(s) the AMHHDC shall send updates only for this data.

The AMHHDC shall send actual data to the HHDC as soon as it is available, but shall send estimated data for the Initial Volume Allocation if actual data is not available. The AMHHDC shall not be required to resend data for subsequent VARs after submitting actual data, unless more accurate data has become available and this data should be sent as soon as it is available.

For Asset Metering Systems, the HHDC shall send the totalled active data to the SVAA and AMVLP or Supplier according to the Settlement Timetable:

for the Initial Volume Allocation the HHDC sends data for all Asset Meter periods for all relevant AMSIDs; the data may be actual or estimated.

for subsequent reconciliation(s) the HHDC shall send updates only for this data.

The HHDC shall send actual data to the SVAA as soon as it is available, but shall send estimated data for the Initial Volume Allocation if actual data is not available. The HHDC shall not be required to resend data for subsequent VARs after submitting actual data, unless more accurate data has become available and this data should be sent as soon as it is available.

#### 3.3.4 Data File Flags

Ensure that Asset Metering System data files transmitted by the HHDC and AMHHDC to other parties are flagged according to the following table:

Data Flag

Description

A

Actual data (read automatically or manually)

C

Long day / short day indicator

E

Estimated data

Any Asset Metering System data received with Data Flag “C” will be processed as if it had contained Data Flag “E”.

3.4 Reasons for Requesting a Metering System Investigation.

For an Asset Metering System, a D0001 Request Metering System Investigation, or equivalent P flow, is issued where the HHDC, AMHHDC, AMVLP or Supplier identifies or is made aware of a problem that requires an Asset Metering System investigation by the SVA MOA or AMMOA to resolve. Possible reasons include but are not limited to:

• The HHDC, or AMHHDC, suspects invalid MTD on the D0268 Half Hourly Meter Technical Details;

• The HHDC, or AMHHDC, has reason to suspect data retrieved from an Asset Metering System;

• Data retrieved from an Asset Metering System failed validation and/or Meter Advance Reconciliation;

• Consumption data is detected on an Asset Metering System registered as de-energised;

• The HHDC, or AMHHDC, is unable to resolve an issue in retrieving data from an Asset Metering System;

• Data required for a proving test cannot be obtained;

• Consumption data is flagged with an alarm; and/or

• At the request of the AMVLP or Supplier.

3.5 Key Asset Meter Technical Details.

Subject to 2.5, below is a list of key fields of Meter Technical Details (MTD) that will cause the Asset Metering System to be proved if any, or all, of them are changed whilst the Asset Metering System, is energised:

Outstation Id;

Asset Meter Id (serial number);

Outstation number of channels;

Measurement Quantity Id;

Asset Meter multiplier;

Pulse multiplier;

CT and / or VT Ratios; and

Access to Asset Metering Equipment at Password level 3.

Where any, or all of the above are changed whilst an Asset Metering System, is de-energised, a proving test shall be initiated as soon as that Asset Metering System becomes energised and completed in the timescales set out in Appendix 3.6.5.

3.6 Proving of Half Hourly Metering Systems.

For Outstations which can only have a pulse multiplier of 1 as identified on the Elexon website (compliance and protocol approval list), a proving test is not required unless the Outstation is subject to a Complex Site arrangement or is separate from the Asset Meter.

3.6.1 Reasons for a Proving Test.

Subject to 2.5 for Asset Metering Systems, a proving test shall be carried out on both main and check Asset Metering Systems and shall be carried out in any of the following circumstances:

Following a change of HHDC, or AMHHDC, appointment but only in the event that the MTD was manually intervened;

Following a change of SVA MOA, or AMMOA, appointment but only in the event that the MTD was manually intervened;

Following a concurrent Change of AMVLP or Supplier and HHDC, or AMHHDC, but only in the event that the MTD was manually intervened;

When an Asset Metering System is reconfigured / replaced;

When there is a key field change (refer to Appendix 3.5);

Where there has been a key field change (refer to Appendix 3.5) whilst a site has been de-energised and the Asset Metering System becomes energised; or

Where a feeder is energised for the first time.

3.6.2 Methods of Proving.

For Asset Metering Systems, the SVA MOA or AMMOA shall decide which technique from the list below is to be used to collect data in conjunction with the HHDC and AMHHDC.

The techniques the SVA MOA or AMMOA can use to record HH data for a proving test are:

Record the HH Metered Data reading while on site; or

Use the Asset Meter manufacturer’s software to download the HH Metered Data; or

Use software which has a relevant protocol approval in accordance with BSCP601 ‘Metering Protocol Approval and Compliance Testing’ to download the HH Metered Data.

The HHDC or AMHHDC collects the HH Settlement Period requested and where an AMHHDC collects the HH Settlement Period requested they should send it on to the HHDC. The HHDC then sends this raw HH Metered Data to the SVA MOA or AMMOA for comparison. If unable to collect Metered Data for Settlement Period requested, the HHDC should send alternative Settlement Period Half Hourly Metered Data.

3.6.3 Comparison of Data.

After a proving test on an Asset Metering System has been undertaken by any of the methods selected above, the SVA MOA or AMMOA then compares the data received from the HHDC to determine a successful or a failed proving test.

3.6.4 Reporting.

The SVA MOA or AMMOA shall report both successful and non-successful proving tests to relevant parties.

3.6.5 Proving Test / Re-Test Timescales.

Proving Test Timescales

A proving test on an Asset Metering System may be undertaken prior to the appointment of the HHDC or AMMHDC and / or SVA MOA or AMMOA so long as there is agreement between the AMVLP Supplier,, SVA MOA or AMMOA (as applicable), HHDC and AMHHDC (if applicable) and the customer.

The timescale for carrying out the proving test shall vary depending on the Asset Metering Type in Code of Practice Eleven that the Asset Metering System is assigned to.

The maximum timescale between the initiation of a proving test for an Asset Metering System as a result of the circumstances in 3.6.1 and the successful completion of the proving test by the SVA MOA, or AMMOA, (by sending the D0214 Confirmation of Proving Tests) to the HHDC and, if applicable, AMHHDC is listed below for each Asset Metering Type.

Re-Test Timescales

Where the proving test has failed, the SVA MOA or AMMOA shall initiate a re-test and the SVA MOA or AMMOA, and HHDC and AMHHDC (if applicable) should ensure wherever possible that the timescale is the same as for the original proving test.

Timescales – Asset Metering Systems

CoP11 Asset Metering Type

WDs to Complete Proving Test53

WDs to Complete Re-Test

Total

One

5

5

10

Two

5

5

10

Three

10

10

20

Four

15

15

30

Five

15

15

30

In the event that timescales are exceeded and the proving test is not completed, the process shall proceed to completion and an audit trail will be maintained by Asset Metering Agents in order to explain the delay.

3.6.6 Failed Proving Test.

If a proving test has failed, then the Metered Data collected will be flagged as estimated i.e. ‘E’ flagged. This collected HH Metered Data will continue to be flagged as estimated until a successful proving test is completed.

The SVA MOA or AMMOA, and HHDC, and AMHHDC if applicable shall complete the re-test as soon as possible after failure of the original proving test.

For an Asset Metering Type Three related Asset Metering System, the timescale for completing the proving test may extend beyond the Initial Volume Allocation Run, in which case the rules for Asset Metering Type Four related Asset Metering System’s shall apply as far as data estimation is concerned.

3.6.7 Non-Completion of Proving Test.

If a proving test is not completed so that proved data can enter Settlements by the due timescales, the actual retrieved HH Metered Data shall be used for Settlements and shall be ‘A’ flagged until a proving test has been completed. Once a proving test has been completed, the data will be flagged as either estimated or actual i.e. ‘A’ flagged depending on whether or not there was a successful proving test.

#### 3.6.8 Proving Test Exemptions

If a proving test is not required as set out in section 2.5 then the actual retrieved HH Metered Data shall be used for Settlements and shall be ‘A’ flagged.

### 3.7 Inbound Data Comparison Check

For an Asset Metering System, where data is to be sent automatically from the Asset Meter to the HHDC or AMHHDC instation for use in Settlement and following a successful Proving Test, the HHDC or AMHHDC shall perform a comparison check between one half hour of data received via the inbound method of communication and the equivalent half hour of data received by interrogating the Asset Meter. The results of the comparison test shall be recorded for audit purposes and any inconsistency shall be investigated in accordance with section 2.3.3. In the event of any inconsistency the HHDC or AMHHDC shall revert to interrogation of the Asset Meter. In addition, the HHDC or AMHHDC shall revert to interrogation of the Asset Meter, at any time, on request by the Registrant of the Asset Metering System.

3.8 Meter Advance Reconciliation – Asset Metering Systems.

A Meter Advance Reconciliation (MAR) is the reconciliation of the advance on the Asset Meter register between two specific date(s) and time(s) compared with the summation of the relevant Settlement Period data used in Settlement over the same date(s) and time(s). This activity is performed by the HHDC or the AMHHDC (as applicable).

Care should be exercised where the Asset Meter register reading does not align with the end of a Settlement Period, and this should be taken into consideration in the reconciliation.

3.8.1 Asset Meters that record cumulative energy with either separate Outstations or integral Outstations which do not provide an electronic cumulative reading of the prime Asset Meter register equivalent to the total consumption or production of the Asset Meter as part of its normal function.

The HHDC or AMMHDC (as applicable) shall perform a MAR:

a) at least once every three months for Asset Meters over 100kW; or

b) at least once every twelve months for Asset Meters below 100kW.

Where a change of HHDC or AMHHDC (as applicable) has occurred, the new HHDC or AMHHDC (as applicable) shall perform a MAR within the first six months of the appointment for Asset Meters below 100kW using the last physical Asset Meter register reading taken on site by a Qualified Asset Metering Agent or read remotely by the AMVLP or Supplier or a Qualified Asset Metering Agent provided by the old HHDC or AMHHDC (as applicable).

Asset Meter readings recorded from the physical Asset Meter register during a site visit by a Qualified Asset Metering Agent or read remotely by the AMVLP or Supplier or a Qualified Asset Metering Agent may be used for the purpose of the MAR under a) or b) above.

Using the Asset Meter register readings taken during any site visit or remote reading, the following checks shall be performed:

i) Ensure that the HH Metered Data between two different date(s) and time(s), as used in Settlements, sums to the Asset Meter advance from site readings of the prime Asset Meter registers for the same date(s) and time(s), i.e. that the difference between successive cumulative Asset Meter register readings and the total of the Metered Period Data for the same time interval, is within a tolerance of ±0.1%.

Specifically:

Σ(pulses * pulse multiplier) for all Asset Meter periods in the time interval = (Asset Meter advance * Asset Meter Multiplier) for the time interval.

The calculation below outlines how the discrepancy should be calculated when performing tolerance checks.

*[Diagram/image in the original web page was not captured in the copy-paste.]*

Where:

∑HHE is the sum of HH Energy volumes in kWh; and MA is the corresponding Asset Meter Advance, i.e.

MA = M2 – M1

Where:

M2 is the Asset Meter register reading (in kWh) taken during the recent site visit; and M1 is the Asset Meter register reading (in kWh) taken during the site visit prior to the recent site visit (e.g. 3 months prior for a 100kW+ Asset Metering System)

ii) Where a main and check Asset Meter is fitted, the main and check Asset Meter advances are compared for any discrepancy between the two values in excess of 1.5 times the class accuracy requirements for the individual Asset Meters at full load, as defined in CoP 11 for the relevant Asset Metering Type.

If after making allowance for the readings not being taken at the end of the preceding Settlement Period (and other factors such as estimates made during the period of the MAR calculation) the above checks fail, then the failure shall be investigated in accordance with section 2.3.3.

The D0008 ‘Meter Advance Reconciliation Report’ shall be produced for the AMVLP or Supplier on a monthly basis. This will include:

MAR confirmation;

MAR failure; and

MAR overdue,

for all Asset Metering Systems for which a MAR has been, or should have been, carried out during the preceding month.

3.8.2 Asset Meters with integral Outstations which provide an electronic cumulative reading of the prime Asset Meter register equivalent to the total consumption or production of the Asset Meter as part of its normal function.

A MAR is not obligatory providing that the Cumulative / Total Consumption Comparison as described in Appendix 3.1.5 can be carried out. Where the Cumulative / Total Consumption Comparison validation cannot be carried out, a MAR shall be performed as described in 3.8.1.

#### 3.8.3 De-energised Asset Meters

Routine MAR is not required for de-energised Asset Meters, on the basis that there is no advance to reconcile.

### 3.9 Guide to Asset Metering Complex Sites

‘Complex Site’ means; any site that requires an ‘Asset Metering Complex Site Supplementary Information Form’ to enable the HHDC to interpret the standing and dynamic Metered Data relating to Asset Metering Systems for Settlement purposes. This is to be provided to the HHDC or AMHHDC in addition to the D0268, ‘Half Hourly Meter Technical Details’.

Asset Differencing does not require an ‘Asset Metering Complex Site Supplementary Information Form’ and this is the responsibility of the AMVLP or Supplier to arrange as part of the registration process.

There are two situations where an adjustment for losses can be made using an ‘Asset Metering Complex Site Supplementary Information Form’:

System Losses – Where the Asset Meter is subject to a Metering Dispensation and is not located at the Defined Metering at the Asset Point and an electrical loss factor has been applied to account for equipment and cabling between the Actual Metering at the Asset Point and the Defined Metering at the Asset Point; and

Inverter and Rectifier Losses – Where the location of the Asset Meter, where it is Asset Metering Type 5, is in such a place that it does not account for the losses of the inverter or rectifier.

Where the AMSID is 1234567890111 and the losses between the Actual Metering at the Asset Point and the Defined Metering at the Asset Point have been calculated as 2% the aggregation rule would be:

1234567890111 = 1234567890111 x 1.02

An adjustment for losses should be done for both the Import AMSID and the Export AMSID should the Asset Meter be configured to record both Asset Import and Asset Export.

Number of Import AMSIDs = 1

Number of Export AMSIDs = 0 or 1 (as applicable)

The primary electronic data flow between the SVA MOA or AMMOA and HHDC, and AMHHDC (if applicable) for Half Hourly Meter Technical Details is the D0268. Where this data flow alone is insufficient to accurately describe to the HHDC or AMHHDC how to apply a fixed multiplier to the various channels of data that should be utilised in Settlements the MTDs is supplemented with the ‘Asset Metering Complex Site Supplementary Information Form’. The HHDC or AMHHDC will run the aggregation rule specified in the ‘Asset Metering Complex Site Supplementary Information Form’ to apply the fixed multiplier.

The SVA MOA or AMMOA, should identify a Complex Site by providing an ‘Asset Metering Complex Site Supplementary Information Form’ in addition to the D0268 data flow to the HHDC, AMHHDC and AMVLP or Supplier indicating in the D0268 data flow that the site is complex. The ‘Asset Metering Complex Site Supplementary Information Form’ shall be sent no later than, or preferably in advance of, the sending of the D0268 data flow. This action shall alert the HHDC to expect an ‘Asset Metering Complex Site Supplementary Information Form’ from the SVA MOA or AMMOA, containing details of how to configure the data collected by an HHDC, or AMHHDC, for Asset Metering Systems. The ‘Asset Metering Complex Site Supplementary Information Form’ should be sent electronically or by any other method agreed.

It is the responsibility of AMVLPs or Suppliers to manage and co-ordinate their Agents to achieve compliance and to intervene should any issues arise.

The AMVLP or Supplier should identify to the SVA MOA, or AMMOA, which AMSIDs relate to the Import energy and which AMSIDs relate to the Export energy.

In some cases, a Complex Site for Asset Metering Systems shall meet the conditions required to apply for a Metering Dispensation as described in BSCP32 ‘Metering Dispensations’. Where Complex Sites use Asset Metering Systems that are not fully compliant with CoP 11, a Metering Dispensation should be applied for via BSCP32. Once a Metering Dispensation has been granted, the information shall be available for all future AMVLPs or Suppliers, so that they shall have the ability to understand the Metering configuration at the Complex Site. As part of the dispensation application process, the AMVLP or Supplier shall need to submit a simplified schematic diagram of the Complex Site connection arrangements and the proposed metering points, as required in BSCP32.

Form CoP11/Fa ‘Asset Metering Complex Site Supplementary Information Form’ provides a means for the SVA MOA or AMMOA to convey the information necessary for correct aggregation. CoP11/Fa shows the information needed to collect that data.

Where Meter channel data is missing, incomplete or incorrect, the HHDC or AMHHDC (as applicable) should attempt to use the associated check data where a check Asset Meter is installed.

### 3.10 Service Levels – Asset Metering Systems

The HHDC shall perform the services to be performed by it as HHDC pursuant to this BSCP to standards which shall be at least as good as those specified in this Appendix.

HHDC processes must be capable of providing statistical information to enable monitoring of performance by the Panel in accordance with this Appendix.

This Appendix has effect for the purposes of this BSCP to determine:

i) the functions to be performed by the SVA MOA, AMMOA and HHDC, as described in columns 2 to 5 of the table set out in this Appendix, in respect of which minimum standards of performance are required;

ii) the minimum standards of performance (Service Levels) relating to the functions referred to in paragraph (i) above, as described in columns 6 and 7 of the table set out in this Appendix; and

iii) a reference number (Serial) in respect of each Service Level, as described in column 1 of the table set out in this Appendix;

iv) the method by which the HHDC’s adherence to the Service Levels is to be measured, as described in column 8 of the table set out in this appendix.

For the purposes of this Appendix:

a) the references in column 3 of the table to a numbered section are to the relevant section in this BSCP;

b) the references in column 4 of the table to a sub-process/data flow are to the relevant sub-process or data flow as described in this BSCP;

c) references to “Timescales” are to those specified by the relevant BSCP and, if applicable, the SVAA Calendar;

d) references to a certain percentage of tasks being completed within a certain specified period are to be read as a reference to that percentage of tasks being completed during an applicable reporting period as specified by the relevant BSC procedure;

e) references to an item being “valid” are to an item which conforms to an applicable SVA Data Catalogue item;

f) reference to an item being in “correct format” are to an item which complies with the applicable SVA Data Catalogue format or the format specified by the relevant BSCP;

g) references to an item being “accurate” are to an item being correctly recorded; and

h) in calculating percentages, the performance figures shall be rounded up or down to the nearest one decimal place (with 0.05 being rounded upwards).

Serial

Sender

Process

Sub-Process

Recipient

Performance Measure

Service Levels

Reporting Method

AC01

HHDC or AMHHDC

### 2.3 Collection Activities

HH Estimates at RF

SVAA;

or in the case of an AMHHDC the HHDC

Extent of estimated data submitted for Final Reconciliation

100% of estimated data at RF to be based upon techniques (a) – (e) as described in BSCP502 Section 4.2A

Provision of data under Appendix 3.12

AC02

Old HHDC or Old AMHHDC

### 2.1 Registration Activities

HH Read History to New HHDC

New HHDC or New AMHHDC

D0036 issued within timescales

100% issued within 5WD of request

Provision of data under Appendix 3.12

AM11

SVA MOA or AMMOA

### 2.4 Interface to Other Party Agents

Timely Sending of HH Asset Meter MTDs to HHDCs and AMHHDCs

HHDC, AMHHDC

D0268, transferred within timescales

100% of D0268s, received by HHDCs and AMHHDCs within 5 WD of the HHDC and AMHHDC EFD

[HHDC/AMHHDC]

AM12

SVA MOA or AMMOA

### 2.4 Interface to Other Party Agents

Missing HH Asset Meter MTDs

New HHDC, new AMHHDC, current HHDC current AMHHDC, or new SVA MOA or new AMMOA

D0268 transferred within timescales

100% of D0268s, received by New and current HHDCs or AMHHDCs and New SVA MOAs or AMMOAs within 5 WD of agents EFD following a change of Agent.

[New SVA MOA/AMMOA or HHDC/AMHHDC]

AM13

SVA MOA or AMMOA

### 2.4 Interface to Other Party Agents

Quality of Asset Meter MTDs

HHDC, AMHHDC

Accurate D0268s, sent

None

[HHDC/AMHHDC]

AM14

SVA MOA or AMMOA

### 2.4 Interface to Other Party Agents

Timely Asset Meter Investigation Requests

HHDC, AMHHDC

Total number of D0002s, received since Date Fault Suspected/Detected

100% of D0001 flows, resolved within +15 WD

[HHDC/AMHHDC]

### 3.11 Sealing

All Asset Metering Equipment shall be sealed in accordance with Code of Practice Eleven.

### 3.12 Retention of Records and Provision of Data

For Asset Metering Systems the associated Asset Metering Agents (i.e. the SVA MOA, AMMOA, HHDC and AMHHDC) shall meet the requirements for retention of records and provision of data specified in 3.12.1 and 3.12.2.

#### 3.12.1 Retention of Records

3.12.1.1 The Asset Metering Agent must ensure that they have processes in place that are capable of maintaining data records together with the user ids of the persons creating or making changes to these records.

3.12.1.2 These records must contain such cross references as are necessary to allow verification by tracing data through processing, forwards and backwards, conveniently and old software programs and hardware must, where necessary, be retained to enable these records to be accessed.

#### 3.12.2 Provision of Data

##### 3.12.2.1 Provision of Data to BSCCo and Associated AMVLPs or Suppliers

3.12.2.1.1 The Asset Metering Agent shall provide other Asset Metering Agents and BSCCo with data and other information derived from its systems and processes within the timescales defined in the BSC and any relevant CSDs in order to enable the other Asset Metering Agents and/or BSCCo to satisfy its related obligations under the BSC and any relevant CSDs. All such communications shall be date-time stamped by the Asset Metering Agent who is sending the data.

3.12.2.1.2 Asset Metering Agents shall provide their associated AMVLP or Supplier with all the information necessary to enable the associated AMVLP or Supplier to report at any time.

##### 3.12.2.2 Provision of Data for resolution of Trading Disputes

3.12.2.2.1 The Asset Metering Agent shall retain the Settlement data acquired or held by it for a minimum period of 40 months after the Settlement Day, the first 28 months of Settlement data being retained in a form capable of supporting a Volume Allocation Run and the remaining 12 months of Settlement data being retained in a form which can be supplied in 10 Business Days, if requested by the Panel, for input into an Extra-Settlement Determination.

3.12.2.2.2 In the event that Settlement data beyond 40 months after the Settlement Day is required to be retained in support of an Extra-Settlement Determination, the Asset Metering Agent shall retain the Settlement data relating to the Settlement Days as requested by the Panel.

##### 3.12.2.3 Provision of Data - General

3.12.2.3.1 The Asset Metering Agent shall ensure that all data and other information acquired or held by it as a Asset Metering Agent is made available at all reasonable times upon request for inspection and copying by the BSC Auditor and the Panel or any person nominated by it and any other person authorised for the purpose under the terms of the BSC and this CSD. The data shall be retained in such a format which will allow items of information retained to be subsequently searched, located and checked for validation purposes.

3.12.2.3.2 The Asset Metering Agent shall ensure that all data and other information acquired or held by it as a Asset Metering Agent is kept confidential and is disclosed only to those persons authorised or required to receive it under the terms of the BSC and this CSD and, where relevant, to those persons authorised by its associated AMVLP or Supplier.

3.12.2.3.3 Asset Metering Agents’ obligations under this section shall survive termination of its appointment under any of the roles which it is qualified to perform as an Asset Metering Agent for whatever reason.

AMENDMENT RECORD - BSCP603

| Version | Details (in source column order: Date / Description of Change / Changes Included / Mods/Panel/Committee Refs.) |
|---|---|
| 1.0 | 30 June 2022<br>June 2022 Standard Release<br>P375, P433<br>P309/06<br>P332/05 |
| 2.0 | 02 November 2023<br>November 2023 Standard Release<br>P395<br>P340/05 |
| 3.0 | 26 June 2025<br>June 2025 Standard Release<br>CP1602<br>SVG290/01 |
| 4.0 | 27 November 2025<br>November 2025 Special Release<br>P483 |

*[Amendment record rebuilt from a flattened copy-paste; each row's cells are listed in source column order.]*

Intellectual Property Rights, Copyright and Disclaimer

The copyright and other intellectual property rights in this document are vested in Elexon or appear with the consent of the copyright owner. These materials are made available for you for the purposes of your participation in the electricity industry. If you have an interest in the electricity industry, you may view, download, copy, distribute, modify, transmit, publish, sell or create derivative works (in whatever format) from this document or in other cases use for personal academic or other non-commercial purposes. All copyright and other proprietary notices contained in the document must be retained on any copy you make.

All other rights of the copyright owner not expressly dealt with above are reserved.

No representation, warranty or guarantee is made that the information in this document is accurate or complete. While care is taken in the collection and provision of this information, Elexon Limited shall not be liable for any errors, omissions, misstatements or mistakes in any information or damages resulting from the use of this information or action taken in reliance on it.

1 References to MOA include both an SVA MOA and an AMMOA.

2 Where a Supplier is the Registrant of an Asset Metering System, it is responsible for these activities.

3 An AMMOA can only be appointed to an Asset Metering Type 4 and Asset Metering Type 5 site

4 Asset Metering Types are defined on Code of Practice Eleven

5 This step could be completed in shorter timescales where the AMVLP and SVA MOA or AMMOA, as applicable, have reached mutual agreement.

6 The AMVLP may have to consult the Equipment Owner where they do not own the Measurement Transformers (i.e. Current Transformers and Voltage Transformers) for the required information

7 A defect or omission in the completion of the processes is set out in Code of Practice Eleven and will also include that the Commissioning information has not been received from the Equipment Owner

8 It shall be the responsibility of the Registrant to ensure that all Asset Metering Equipment is appropriately Commissioned. If the Registrant believes that there is a risk to Settlement it shall, where appropriate, consult with the relevant Equipment Owner and agree the appropriate steps to be taken to minimise the risks to Settlement. Such agreements shall also be recorded and made available on request to the BSC Panel.

9 This step could be completed in shorter timescales where the AMVLP and SVA MOA or AMMOA, as applicable, have reached mutual agreement.

10 The AMVLP may have to consult the Equipment Owner where they do not own the Measurement Transformers (i.e. Current Transformers and Voltage Transformers) for the required information in the P0315

11 Note that if there is also a concurrent Change of HHDC or AMHHDC, the New AMVLP shall send the D0148 once the D0011 from both the SVA MOA or AMMOA and the HHDC and if applicable AMHHDC has been received and within 5WD of the receipt of the latter D0011

12 The new HHDC should not send the D0170 flow prior to the HHDC Effective From Date on their D0155 ‘Notification of Meter Operator or Data Collector Appointment and Terms’ flow received from their associated AMVLP

13 If a register reading not available in Asset Meter notify new HHDC

14 This Meter Advance Reconciliation will require historic Asset Metered Data from the old HHDC, and the new HHDC shall therefore ensure that step 2.1.7.11 is carried out in time for this data to be received.

15 The new AMHHDC should not send the D0170 flow prior to the AMHHDC Effective From Date on their P0314 ‘Notification of AMHHDC’ flow received from their associated AMVLP

16 If a register reading not available in Asset Meter notify new AMHHDC

17 This Meter Advance Reconciliation will require historic Asset Metered Data from the old AMHHDC, and the new AMHHDC shall therefore ensure that step 2.1.8.11 is carried out in time for this data to be received.

18 The new AMHHDC should not send the D0170 flow prior to the AMHHDC Effective From Date on their P0314 ‘Notification of AMHHDC’ flow received from their associated AMVLP

19 If a register reading not available in Asset Meter notify new AMHHDC

20 This Meter Advance Reconciliation will require historic Asset Metered Data from the old AMHHDC, and the new AMHHDC shall therefore ensure that step 2.1.9.11 is carried out in time for this data to be received.

21 The new HHDC should not send the D0170 flow prior to the HHDC Effective From Date on their D0155 ‘Notification of Meter Operator or Data Collector Appointment and Terms’ flow received from their associated AMVLP

22 If a register reading not available in Asset Meter notify new HHDC

23 This Meter Advance Reconciliation will require historic Asset Metered Data from the old HHDC, and the new HHDC shall therefore ensure that step 2.1.10.11 is carried out in time for this data to be received.

24 The new AMHHDC should not send the D0170 flow prior to the AMHHDC Effective From Date on their P0314 ‘Notification of AMHHDC’ flow received from their associated AMVLP

25 If a register reading not available in Asset Meter notify new AMHHDC

26 This Meter Advance Reconciliation will require historic Asset Metered Data from the old AMHHDC, and the new AMHHDC shall therefore ensure that step 2.1.11.11 is carried out in time for this data to be received.

27 The new AMHHDC should not send the D0170 flow prior to the AMHHDC Effective From Date on their P0314 ‘Notification of AMHHDC’ flow received from their associated AMVLP

28 If a register reading not available in Asset Meter notify new AMHHDC

29 This Meter Advance Reconciliation will require historic Asset Metered Data from the old AMHHDC, and the new AM HHDC shall therefore ensure that step 2.1.12.11 is carried out in time for this data to be received.

30 The HHDC should not send the D0170 flow prior to the AMHHDC Effective To Date on their P0314 ‘Notification of AMHHDC’ flow received from their associated AMVLP

31 If a register reading not available in Asset Meter notify HHDC

32 This Meter Advance Reconciliation will require historic Asset Metered Data from the AMHHDC, and the HHDC shall therefore ensure that step 2.1.13.6 is carried out in time for this data to be received.

33 For example due to the remoteness no mobile communication being possible or site restrictions on the use of mobile communications.

34 For example due to the remoteness no mobile communication being possible or site restrictions on the use of mobile communications.

35 For example due to the remoteness no mobile communication being possible or site restrictions on the use of mobile communications.

36 If the Asset Metering System cannot be reconfigured or replaced at the appointed time, the SVA MOA or AMMOA, as applicable, shall liaise with the AMVLP to agree the way forward.

37 If replacement includes Measurement Transformers, commission in accordance with Code of Practice Eleven and proceed as per section 2.1.2.

38 For example due to the remoteness no mobile communication being possible or site restrictions on the use of mobile communications.

39 The HHDC shall send actual data to the SVAA as soon as it is available, but shall send estimated data for the SF VAR if actual data is not available. The HHDC shall not be required to resend data for subsequent VARs after submitting actual data, unless more accurate data has become available.

40 J0020 ‘Actual/Estimated Indicator’ should only include the J0020 populated with ‘A’ or ‘E’, and not include the J0020 populated with ‘C’

41 Estimated data in the D0390 identified in the J0020 ‘Actual/Estimated Indicator’ Data Item containing “E”

42 The AMHHDC shall send actual data to the HHDC as soon as it is available but shall send estimated data for the SF VAR if actual data is not available. The AMHHDC shall not be required to resend data for subsequent VARs after submitting actual data, unless more accurate data has become available. For AMSIDs registered in LPAMR, the valid consumption data should be sent to the AMVLP only.

43 Estimated data in the D0390 identified in the J0020 ‘Actual/Estimated Indicator’ Data Item containing “E”.

44 The HHDC shall send actual data to the SVAA as soon as it is available, but shall send estimated data provided by the AMHHDC for the SF VAR if actual data is not available. The HHDC shall not be required to resend data for subsequent VARs after submitting actual data, unless more accurate data has become available. For AMSIDs registered in LPAMR, the valid consumption data should be sent to the AMVLP only.

45 J0020 ‘Actual/Estimated Indicator’ should only include the J0020 populated with ‘A’ or ‘E’, and not include the J0020 populated with ‘C’

46 Estimated data in the D0390 identified in the J0020 ‘Actual/Estimated Indicator’ Data Item containing “E”

47 Any Participant other than the HHDC, AMHHDC or AMVLP wishing to request that the SVA MOA or AMMOA carries out an Asset Metering System investigation shall do so via the VLP

48 Where the HHDC or AMHHDC (if applicable) raises the fault, it should send the notification to the AMVLP for information purposes only. Where the AMVLP raises the fault, it should send the notification to the HHDC or AMHHDC (if applicable) for information purposes only

49 The SVA MOA or AMMOA should contact and liaise with the AMVLP if appropriate

50 The D0005 ‘Instruction on Action’ should always be sent containing the high level points so that an audit trail can be maintained. For complex cases where the D0005 is not sufficient, or where requested by the HHDC or AMHHDC, further details can be given in the fault resolution plan. In these instances the sending of the fault resolution plan should be referred to in the D0005. Any other correspondence between the AMVLP, SVA MOA or AMMOA and HHDC or AMHHDC which is required to resolve the fault should be sent in a format and by a method agreed by those Participants involved.

51 Described as performing a mini-MAR.

52 For the avoidance of doubt, the data estimation method may be provided using the D0022 Additional Information Field, or by any other method agreed between the HHDC or AMHHDC (as applicable), AMVLP and SVAA (e.g. spreadsheets, emails) providing that an audit trail of such information is maintained.

53 The starting date for this time is either the Date of Asset Meter Installation, the Date of Commissioning, the Effective From Date of the Asset Meter, the Effective Date of a Change of Agent as described in Section 3.6.1, or the date when an Asset Metering System becomes energised where there has been a key field change whilst the Asset Metering System was de-energised, whichever is the later.