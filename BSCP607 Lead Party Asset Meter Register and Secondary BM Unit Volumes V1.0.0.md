# BSCP607: Lead Party Asset Meter Register & Secondary BM Unit Volumes V1.0.0

> **Source file:** `BSCP607 Lead Party Asset Meter Regi.txt`  
> **Effective From Date:** 27/11/2025  
> **Status:** LIVE  
> **Converted:** 2026-10-07. Wording kept verbatim from the source copy-paste; only layout artefacts (page headers/footers, line wraps, website navigation, broken tables) were cleaned up. Notes in *[italic square brackets]* are editorial.

---

**BSCP607 relating to the Lead Party Asset Meter Register & Secondary BM Unit Volumes**

1. Reference is made to the Balancing and Settlement Code and, in particular, to the definition of “BSC Procedure” in Section X, Annex X-1 thereof.

2. This is BSC Procedure 607, Version 1.0 relating to the Lead Party Asset Meter Register and Secondary BM Unit Asset Volumes.

3. This BSC Procedure is effective from 27 November 202527 November 2025. *[sic - date duplicated in source]*

### Intellectual Property Rights, Copyright and Disclaimer

The copyright and other intellectual property rights in this document are vested in Elexon or appear with the consent of the copyright owner. These materials are made available for you for the purposes of your participation in the electricity industry. If you have an interest in the electricity industry, you may view, download, copy, distribute, modify, transmit, publish, sell or create derivative works (in whatever format) from this document or in other cases use for personal academic or other non-commercial purposes. All copyright and other proprietary notices contained in the document must be retained on any copy you make.

All other rights of the copyright owner not expressly dealt with above are reserved.

No representation, warranty or guarantee is made that the information in this document is accurate or complete. While care is taken in the collection and provision of this information, Elexon Limited shall not be liable for any errors, omissions, misstatements or mistakes in any information or damages resulting from the use of this information or action taken in reliance on it.

4. This BSC Procedure has been approved by the BSC Panel or its relevant delegated Panel Committee(s).

### Amendment Record

| Version | Details (in source column order: Date / Description of Change / Changes Included / Mods/Panel/Committee Refs.) |
|---|---|
| 1.0 | 27/11/2025<br>P483<br>P483 |

*[Amendment record rebuilt from a flattened copy-paste; each row's cells are listed in source column order.]*

## 1 Introduction

### 1.1 Purpose and Scope of the Procedure

The purpose of this Balancing and Settlement Code Procedure (BSCP) is to set out the processes for Asset Metering Virtual Lead Parties (AMVLP) to register, and maintain the registration of, Asset Metering System Identifier (AMSID) Pairs in their Lead Party Asset Meter Register (LPAMR) where these AMSID Pairs are located behind a Boundary Point Metering System that does not record UTC Period Level Consumption for Settlement purposes. These AMSID Pairs are referred to as Party-Registered AMSID Pairs.

Any AMVLP intending to operate in the Wholesale Market must also be Qualified as a Virtual Trading Party (VTP) and submit Wholesale Market Activity Notifications in accordance with BSCP602.

Note – Due to technical constraints, a Secondary BM Unit may not consist entirely of Party-Registered AMSID Pairs. There must be at least one active MSID Pair or AMSID Pair (Registered in the Asset Metering System Register) in the Secondary BM Unit.

This BSCP also sets out the processes for AMVLPs to submit Demand and Delivered Volumes to the Settlement Administration Agent (SAA) in respect of AMSID Pairs registered in their LPAMR.

#### 1.1.1 AMSID Pair allocation

This BSCP sets out the processes that AMVLPs should follow:

when registering an Asset Meter in their LPAMR - assigning AMSID number(s), an AMSID Pair and allocating the AMSID Pair to a Secondary BM Unit; and

for maintaining their LPAMR; and

when submitting aggregated Secondary BM Unit Demand and Delivered Volumes to the SAA.

An AMSID Pair allocation must specify the Secondary BM Unit and the Boundary Point Metering System[s] behind which the AMSID Pair is located. If any such Boundary Point Metering System can record UTC Period Level Consumption for Settlement purposes then the allocation is not valid. Also Party-Registered AMSID Pairs cannot be used for Asset Differencing.

Note that one or more Party-Registered AMSID Pairs may be located behind one or more Boundary Point Metering Systems

An ‘AMSID Pair’ means one AMSID measuring the flow of electricity to the Asset and, where applicable, one AMSID measuring the flow of electricity from the Asset, whose Metering Systems must record UTC Period Level Consumption for the purposes of offering Balancing Services.

An Asset Meter registered in one LPAMR cannot, at the same time, also be registered in another LPAMR (or in the Asset Meter Register outlined in BSCP602).

This BSC Procedure focuses on the interfaces between AMVLPs, BSCCo and SAA.

The purpose of this procedure is:

to ensure maintenance of an accurate, up-to-date LPAMR;

to ensure the correct BSCCo processing for validating submissions of each AMVLP’s LPAMR;

to ensure AMSID Pair Delivered Volumes are determined in good faith, in accordance with Good Industry Practice and notified in a timely manner; and

to ensure the correct processing of Secondary BM Unit Asset Demand and Delivered Volumes.

#### 1.1.2 Submitted Expected Volumes

The Submitted Expected Volumes must be provided, by the AMVLP, for each Secondary BMU with Party-Registered AMSID Pairs, where the Secondary BM Unit is participating in the Wholesale Market. For clarity - baselining is optional where the Secondary BM Unit is participating in the Balancing Mechanism.

### 1.3 Main Users of the Procedure

This BSC Procedure should be used by:

AMVLPs

The systems and processes used by AMVLPs must comply with all other applicable requirements set out in the Code, CoP11, BSCP537 and BSCP603.

### 1.4 Use of Procedure

The remaining sections in this document are:

Section 2 – Interface and Timetable Information: this section defines the step by step processes for the LPAMR & Secondary BM Unit Asset Volumes.

### 1.5 Balancing and Settlement Code Provisions

This BSC Procedure has been produced in accordance with the provisions of the Balancing and Settlement Code (BSC). In the event of an inconsistency between the provisions of this BSC Procedure and the BSC, the provisions of the BSC shall prevail.

### 1.6 Associated BSC Procedures

This BSC Procedure interfaces with:

| BSC Procedure | Title |
|---|---|
| BSCP15 | BM Unit Registration |
| BSCP507 | Supplier Volume Allocation Standing Data Changes |
| BSCP508 | Supplier Volume Allocation Agent |
| BSCP537 | Qualification Process for SVA Parties, SVA Party Agents VLPs, AMVLPs, AMVLP Agents and CVA MOAs |
| BSCP602 | SVA Metering System & Asset Metering System Register |
| BSCP603 | Meter Operations and Data Collection for Asset Metering Systems |
| BSCP703 | BSC Central Services for MHHS Metering Systems |
| BSCP707 | Industry Standing Data |

### 1.7 Acronyms and Definitions

Any capitalised term that is not defined in this BSCP shall have the same meaning given to it as in the Code.

The acronyms used in this BSC Procedure are defined as follows:

| Acronym | Expression |
|---|---|
| AMHHDC | Asset Metering Half Hourly Data Collector |
| AMMOA | Asset Metering Meter Operator Agent |
| AMSID | Asset Metering System Identifier |
| AMVLP | Asset Metering Virtual Lead Party |
| BM | Balancing Mechanism |
| BSC | Balancing and Settlement Code (the “Code”) |
| BSCCo | Balancing and Settlement Code Company |
| BSCP | Balancing and Settlement Code Procedure |
| BSP | Balancing Service Provider |
| CRA | Central Registration Agent |
| EES | Electricity Enquiry Service |
| EFD | Effective From Date |
| HHDC | Half Hourly Data Collector |
| MOA | Meter Operator Agent |
| MSID | Metering System Identifier |
| Ref | Reference |
| SAA | Settlement Administration Agent |
| SVA | Supplier Volume Allocation |
| SVAA | Supplier Volume Allocation Agent |
| VAR | Volume Allocation Run |
| VTP | Virtual Trading Party |
| WD | Working Day |

## 2. Interface and Timetable Information

### 2.1 Asset Registration

An AMVLP may register an Asset and related Asset Metering System(s), in order to assign an AMSID Pair1 and then allocate the AMSID Pair to a Secondary BM Unit.

Note a Secondary BM Unit must be registered in CRA, in accordance with BSCP 15, before an AMSID Pair can be allocated to it.

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.1.1 | At any time but no later than 10WD before allocation to a Secondary BM Unit | Request a valid range of AMSIDs which can be assigned to Asset Metering Systems in the AMVLP’s LPAMR | AMVLP | BSCCo | Indication of expected number of Asset Metering Systems | Electronic or other means, as agreed. |
| 2.1.2 | Within 2WD of 2.1.1 | Provide range of AMSIDs | BSCCo | Requesting party | Valid range of AMSIDs | Electronic or other means, as agreed. |
| 2.1.3 | At any time but no later than 10WD before allocation to a Secondary BM Unit | Ensure Asset Meter is installed and commissioned as per BSCP 603. | AMVLP |  |  | Internal process |
| 2.1.4 | Following 2.1.3 | Identify the Boundary Point Metering Systems behind which the Asset Meter is located | AMVLP |  | MSID(s) of Boundary Point Metering | Internal process |
| 2.1.5 | Following 2.1.4 | Assign AMSIDs from range provided by BSCCo, for the Metering Systems of the Asset Meter | AMVLP |  |  | Internal process |
| 2.1.6 | Following 2.1.5 | Ensure Asset Metering Agents have been appointed in accordance with BSCP603 | AMVLP |  |  | Internal process |
| 2.1.7 | 1 WD following 2.1.6 | Add a record to the LPAMR thus allocating the AMSID Pair to the appropriate Secondary BM Unit belonging to the AMVLP. | AMVLP |  | See Appendix 3.3 | Internal process |
| 2.1.8 | No later than 1WD of a change to new registration details becoming effective | Update LPAMR with revised record details | AMVLP |  | As above | Internal process |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 2.2 Validation of the LPAMR

AMSID Pairs are ineligible for inclusion in LPAMR if one or more of the Boundary Point Metering Systems are HH-Settled or [under MHHS] have Metering which can record UTC Period Level Consumption for Settlement purposes. Also, an AMSID Pair must be removed from an AMVLP’s LPAMR if the same Asset Meter has since been registered by another AMVLP.

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.2.1 | On a weekly basis, as advised by BSCCo | Submit a copy of LPAMR to BSCCo | AMVLP | BSCCo | See Appendix 3.3 | Electronic or other means, as agreed. |
| 2.2.2 | On a weekly basis | Collate LPAMR submissions and check for anomalies (see Appendix 3.1) | BSCCo |  |  | Internal Process |
| 2.2.3 | Within 1WD of 2.2.2 | Notify AMVLP where an AMSID Pair does not meet criteria for inclusion in LPAMR | BSCCo | AMVLP | Affected AMSID Pairs and the associated reason for ineligibility (eg. wrong type of Boundary Point Metering System, or Asset Meter later registered in another AMVLP’s LPAMR) | Electronic or other means, as agreed. |
| 2.2.4 | Within 4WD of 2.2.5 | Remove ineligible AMSIDs from LPAMR or correct erroneous data. Else raise a dispute as per Section 2.4 | AMVLP |  |  | Internal Process |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 2.3 Submission of Aggregated Delivered Volumes and Demand Volumes for Party-Registered AMSID Pairs

For each Settlement Day where an AMVLP has participated in the Balancing Mechanism or Wholesale Market, using a Secondary BM Unit, the AMVLP must notify to the SAA the LLF-adjusted Secondary BM Unit Asset Delivered Volume for each relevant Settlement Period, and the LLF-adjusted Secondary BM Unit Asset Demand Volume for every Settlement Period, within that Settlement Day.

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.3.1 | By 9am on the fourth working day following action in the BM or Wholesale Market | Submit the LLF-adjusted Secondary BM Unit Asset Delivered Volumes and the LLF-adjusted Secondary BM Unit Asset Demand Volumes to the SAA | AMVLP | SAA | SAA-IO63 | Electronic Data File |
| 2.3.2 | As required | Re-submit the LLF-adjusted Secondary BM Unit Asset Delivered Volumes and the LLF-adjusted Secondary BM Unit Asset Demand Volumes to the SAA | AMVLP | SAA | SAA-IO63 | Electronic Data File |
| 2.3.3 | Within 1 WD of 2.3.1 (or 2.3.2 as appropriate) | Load and provide file-level validation on SAA-IO63. | SAA |  |  | Internal process. |
| 2.3.4 | Within 1 WD of 2.3.3 | If the file cannot be processed then send Negative Acknowledgement (or Nack). | SAA | AMVLP |  | Electronic or other method, as agreed. |
| 2.3.5 | Following receipt of notification in 2.3.4 | Go to step 2.3.2 | AMVLP |  |  |  |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 2.4 Disputed Asset Meter Allocation Resolution

Where a Lead Party has received a Loss of AMSID Pair Allocation notification and, after discussion with the customer, they believe it to be an erroneous reallocation, they may initiate the Disputed Aset Meter Allocation Procedure.

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.4.1 | Within 5 WD of receipt of a Loss of AMSID Pair Allocation notification in 2.2.3 | Initiate the Disputed Asset Meter Allocation Resolution Process | Losing AMVLP | BSCCo | Asset Meter Serial Number, Dispute Reason, Supporting Detail | Electronic or other method, as agreed. |
| 2.4.2 | Following 2.4.1 within 1WD | Forward to Gaining AMVLP | BSCCo | Gaining AMVLP | Asset Meter Serial Number, Dispute Reason, Supporting Detail | Electronic or other method, as agreed. |
| 2.4.3 | Within 5 WD of 2.4.2 | Respond to or Disputed AMSID Pair Allocation notification | Gaining Lead Party | BSCCo | Asset Meter Serial Number, Dispute Reason, Supporting Detail | Electronic or other method, as agreed. |
| 2.4.4 | Once the initial request has been made one of the following options shall be taken | The Gaining AMVLP agrees that the AMSID Pair is to be allocated to the Losing AMVLP;<br>or<br>After appropriate investigation e.g. checking a valid contract is in place, the Gaining AMVLP disagrees with the Losing AMVLP |  |  |  | Internal Process |

*[Row 2.4.4: the split between the WHEN and ACTION cells was inferred; FROM/TO/INFORMATION are blank in the source.]*

| 2.4.5 | Within 1WD of 2.4.3 | If disagreement, advise Losing AMVLP of the ability to re-raise the dispute. | BSCCo | Losing AMVLP |  | Electronic or other method, as agreed. |
| 2.4.6 | Within 1 WD of 2.4.3 | If agreement, advise Gaining AMVLP to remove the AMSID Pair from their LPAMR | BSCCo | Gaining AMVLP |  | Electronic or other method, as agreed. |
| 2.4.7 | Within 4 WD of 2.4.6 | Update LPAMR | Gaining AMVLP |  |  | Internal Process |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 2.5 BM Unit Submitted Expected Volumes

Where a Baselined BM Unit has Party-Registered AMSID Pairs allocated to it, the Lead Party must submit a Submitted Expected Volume to SVAA and/or submit a Default Submitted Expected Volume (which will be used where no Submitted Expected Volume has been provided).

| REF | WHEN | ACTION | FROM | TO | INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 2.5.1 | By 23:59 on the Settlement Day before it becomes effective. | Submit the Default Submitted Expected Volumes (relating to Party-Registered AMSID Pairs in a Baselined BM Unit). | AMVLP | SVAA | P0328 BM Unit Submitted Expected Volume Notification | Electronic or other method, as agreed. |
| 2.5.2 | No later than Gate closure for a Settlement Period | Submit the Submitted Expected Volumes (relating to Party-Registered AMSID Pairs in a Baselined BM Unit). | AMVLP | SVAA | P0328 BM Unit Submitted Expected Volume Notification | Electronic or other method, as agreed. |
| 2.5.3 | On receipt of P0238 | Log and validate Submitted Expected Volumes | SVAA |  |  | Internal Process |
| 2.5.4 | Immediately following 2.5.3 | If Submitted Expected Volume fails validation send rejection. | SVAA | AMVLP | P0329 – BM Unit Submitted Expected Volume Rejection | Electronic or other method, as agreed. |
| 2.5.5 | On receipt of rejection notification | Go to 2.5.2 | AMVLP |  |  |  |
| 2.5.6 | Immediately following 2.5.3 | If Submitted Expected Volume passes validation send confirmation. | SVAA | AMVLP | P0330 –BM Unit Submitted Expected Volume Acceptance | Electronic or other method, as agreed. |
| 2.5.7 | By Calendar Day prior to Settlement Day | Submitted Expected Volumes revalidation of EFD<br>(Non-zero Submitted Expected Volumes for BMU with no AMSID Pair with status ‘S’) | SVAA | AMVLP | P0331 BM Unit Submitted Expected Volume Warning | Electronic or other method, as agreed. |
| 2.5.8 | As per SVAA Calendar (for each Volume Allocation Run) | If a Submitted Expected Volume or Default Submitted Expected Volume is not registered before Gate Closure for a particular Settlement Period, set Settlement Expected Volume to NULL | SVAA |  |  | Internal process |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

## 3 Appendices

### 3.1 Amendments to LPAMR

An AMVLP’s LPAMR holds the current registration data for each AMSID Pair contained within it. Where the AMSID Pair is no longer eligible for inclusion in the LPAMR for reason of the Boundary Point Metering becoming HH-Settled or [under MHHS] having Metering which can record UTC Period Level Consumption for Settlement purposes, the LPAMR should remove the AMSID Pair from their LPAMR as advised by BSCCo. The registration ceases at the time the AMSID Pair is removed from the LPAMR. From this point onwards Demand and Delivered Volumes relating to the AMSID Pair should not be included in the aggregated figures provided to SAA in the SAA-IO63 submission.

Where BSCCo discovers that the same Asset is registered in more than one LPAMR, the default resolution is that the registration with the earlier EFD is terminated. Assuming no dispute (Section 2.4) then the Losing AMVLP has 5WD to remove the AMSID Pair from their LPAMR and they must resubmit SAA-IO63 files for the Settlement Days where the AMSID Pair’s volumes had been incorrectly included.

### 3.2 Notification of Aggregated Delivered Volumes and Demand Volumes

To ensure that AMSID Pair Delivered Volumes are determined in good faith and in accordance with Good Industry Practice, AMVLPs must be able to provide upon request:

Sufficient information to demonstrate how the AMSID Pair Delivered Volumes for any AMSID Pair were derived.

It shall be possible for the AMVLP to re-run any individual determination of Delivered Volumes to recreate the results exactly as originally calculated, as a historical report. This shall include the facility to exclude later versions of business data which were received after the process was originally run.

Should any Delivered Volume process or other report process generate informational, warning or error logs as part of its processing, these logs should be available for inspection.

### 3.3 Data required for the LPAMR

- Asset Type
- Asset Meter Serial Number
- Date of Asset Meter Installation
- Import AMSID
- Import AMSID EFD
- Import AMSID MOA/AMMOA
- Import AMSID MOA/AMMOA EFD
- Import AMSID AMHHDC (where applicable)
- Import AMSID AMHHDC EFD (where applicable)
- Import AMSID HHDC (if present)
- Import AMSID HHDC EFD (where applicable)
- Export AMSID
- Import MSID
- Export MSID
- GSP Group
- Secondary BM Unit ID
- Party ID

1 If an Asset has no Generation capacity, no Export Asset Metering System will be required, so only an Import AMSID will be generated for that Asset’s AMSID Pair.