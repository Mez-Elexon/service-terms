# BSCP 15: BM Unit Registration V37.0

> **Source file:** `BSCP 15 BM Unit Registration V33.0.txt`  
> **Effective From Date:** 02/05/2025  
> **Status:** LIVE  
> **Converted:** 2026-10-07. Wording kept verbatim from the source copy-paste; only layout artefacts (page headers/footers, line wraps, website navigation, broken tables) were cleaned up. Notes in *[italic square brackets]* are editorial.

---

1. Reference is made to the Balancing and Settlement Code and, in particular, to the definition of “BSC Procedure” in Section X, Annex X-1 thereof.

2. This is BSC Procedure 15, Version 37.0 relating to BM Unit Registration.

3. This BSC Procedure is effective from 02 May 2025.

4. This BSC Procedure has been approved by the Panel.

## 1. Introduction

### 1.1 Purpose and Scope of the Procedure

This BSCP defines the key interfaces, interdependencies and timetable for the registration and de-registration of Balancing Mechanism (BM) Units by the Party, which, for the avoidance of doubt, includes:

New registration of Primary BM Units;

De-registration of Primary BM Units;

Changes in the Final Physical Notification (FPN) flag status;

Registration of Seasonal Estimates of the Maximum Positive Magnitude and Maximum Negative Magnitude Primary BM Unit Metered Volume;

Application for Exemptable status for a Generating Plant and Exempt Export status for the associated Primary BM Unit(s), including election of the Production / Consumption Status for the Exempt Export Primary BM Unit(s) by the Lead Party;

Change of Production / Consumption Status for an Exempt Export Primary BM, Storage BM Unit or Secondary BM Unit by the Lead Party;

Termination of Exemptable status for a Generating Plant and the Exempt Export status of the associated Primary BM Unit(s);

Mid-Season Changes of the Maximum Positive Magnitude and Maximum Negative Magnitude Primary BM Unit Metered Volume;

Monitoring of BM Unit Metered Volumes for breaches of Generation Capacity and Demand Capacity;

Change of Central Volume Allocation (CVA) Primary BM Unit Lead Party;

Transfer of Supplier Identifier (ID);

Notification of Switching Group1.

New registration of Secondary BM Units and Trading Secondary BM Units; and

De-registration of Secondary BM Units and Trading Secondary BM Units.

#### 1.1.1 Use of the Self-Service Gateway

Where a Party has access to the Self-Service Gateway and an equivalent online form is provided, the Party may use the online form as an alternative to the paper forms defined in this BSCP.

Where a Party has provided data using the Self-Service Gateway, BSCCo may use the service to validate and confirm the input data or to request additional data. Where this is the case, these online transactions will represent a valid equivalent to the transactions defined in this BSCP.

Please note that there will not always be a one-to-one equivalence between the data collected via the Self-Service Gateway and the paper forms defined in this BSCP. For example, data collected in one paper form, may be collected by more than one online form. Conversely, a single online form may collect data from more than one paper form.

All references to the provision of information using BSCP forms in this Procedure, should be construed as provision either by a paper form or via the Self-Service Gateway. References to the CRA, including checks performed by the CRA, may include the Self-Service Gateway as applicable.

#### 1.1.2 Baselined Additional or Secondary BM Units

Suppliers VLPs and AMVLPs can opt for their Additional and Secondary BM Units to be a “Baselined BM Unit”. Virtual Trading Parties (VTPs) must set their Trading Secondary BM Units to be “Baselined BM Units”, but are not required to Baseline individual MSID Pairs.

Setting a BM Unit to Baselined means that instead of using the FPN in the calculation of Delivered Volumes and Non-Delivery Charges an equivalent value can be used. Registration of a Baselined BM Unit is incorporated into sections 3.4 and 3.21.

Note that the Lead Party for a Baselined BM Unit2 must still submit an FPN to the NETSO, but the FPN is not used to forecast Non-Delivery Charges. Instead Settlement systems calculate their own FPN equivalent known as the “Settlement Expected Volume” (detailed in BSCP602). The Lead Party specifies (when they allocate each MSID Pair or AMSID Pair to the Baselined BM Unit) how this will work:

1. Baselined MSID Pairs or AMSID Pairs: The SVAA will use historic metered data to calculate the baseline consumption for the MSID Pair or AMSID Pair (in accordance with the Baselining Methodology Document agreed by the BSC Panel);

2. Submitted MSID Pairs or AMSID Pairs: The Lead Party forecasts the FPN-equivalent, and submits a total figure (per BM Unit and Settlement Period) for all the non-Baselined MSID Pairs and AMSID Pairs; or

3. Inactive MSID Pairs or AMSID Pairs: Temporarily excluded from the BM Unit. Secondary BM Units and Trading Secondary BM Units only.

### 1.2 Main Users of the Procedure and their Responsibilities

The main users of this procedure are:

(a) The Party that is de-registering the relevant Primary BM Unit;

(b) The Party that is registering the relevant Primary BM Unit;

(c) The Virtual Lead Party or Asset Metering Virtual Lead Party that is de-registering the relevant Secondary BM Unit and the Virtual Trading Party that is de-registering the relevant Trading Secondary BM Unit;

(d) The Virtual Lead Party or Asset Metering Virtual Lead Party that is registering the relevant Secondary BM Unit and the Virtual Trading Party that is registering the relevant Trading Secondary BM Unit;

(e) The Lead Party for an Exempt Export Primary BM Unit (or a Primary BM Unit which is the subject of an Exempt Export status application);

(f) The Central Data Collection Agent (CDCA);

(g) The Central Registration Agent (CRA);

(h) The National Electricity Transmission System Operator (NETSO);

(i) Supplier Volume Allocation Agent (SVAA);

(j) Licensed Distribution System Operators (LDSOs);

(k) CfD Counterparty

(l) BSCCo; and

(m) The Panel.

### 1.3 Key Milestones

The key milestones in this procedure are:

Detailed notification of ‘registration’ or reconfiguration of a Primary BM Unit (except a Non-Standard Primary BM Unit or Additional Primary BM Unit) at least 30 Working Days (WD) prior to the Effective From Date;

60 WD notification of registration or reconfiguration of a Non-Standard Primary BM Unit. A longer timescale is required in order that the application may be properly considered by BSCCo, the NETSO and the Panel. The Party should advise BSCCo of any such applications at the earliest opportunity such that indicative registration timescales and Effective From Dates may be discussed.

15,19 WD notification of registration of Additional Primary BM Unit, unless FPN flag is set to ‘yes’ where 30 WD notification may be needed (see section 1.6).

15 WD notification of registration of Secondary BM Unit or Trading Secondary BM Unit;

20 WD notification of de-registering Primary BM Unit (30 WD for a Base Primary BM Unit) prior to proposed Effective To Date;

20 WD notification of de-registering Secondary BM Unit or Trading Secondary BM Unit prior to proposed Effective To Date;

New Suppliers notified to Supplier Volume Allocation (SVA) at least 30 WD prior to the Effective From Date;

5 WD notification of transfer of Directly Connected Demand Primary BM Units, if the criteria set out in section 3.13 are satisfied;

5 WD notification of Change of CVA Primary BM Unit Lead Party , if the criteria set out in section 3.13 are satisfied; and

1 WD notification of transfer of Supplier ID process (Change of SVA Primary BM Unit Ownership).

The notice period required to register and de-register a BM Unit, excluding Base Primary BM Units, may be reduced if there is an agreement between the CRA/BSCCo/Party/NETSO.

### 1.4 Balancing and Settlement Code Provision

This BSCP should be read in conjunction with the Code and in particular Section K. This BSCP has been produced in accordance with the provisions of the Code. In the event of an inconsistency between the provisions of this BSCP and the Code, the provisions of the Code shall prevail.

### 1.5 Associated BSC Procedures

This procedure interfaces with the following BSCPs:

| BSC Procedure | Title |
|---|---|
| BSCP02 | Proving Test Requirements for Central Volume Allocation Metering Systems |
| BSCP06 | CVA Meter Operations for Metering Systems Registered in CMRS |
| BSCP20 | Registration of Metering System for Central Volume Allocation |
| BSCP25 | Registration of Transmission System Boundary Points, Grid Supply Points, GSP Groups & Distribution Systems Connection Points |
| BSCP31 | Registration of Trading Units |
| BSCP32 | Metering Dispensations |
| BSCP38 | Authorisations |
| BSCP65 | Registration of Parties and Exit Procedures |
| BSCP68 | Transfer of Registration of Metering Systems between CMRS and SMRS |
| BSCP71 | Submission of ECVNs and MVRNs |
| BSCP75 | Registration of Meter Aggregation Rules for Volume Allocation Units |
| BSCP128 | Production, Submission, Audit and Approval of Line Loss Factors |
| BSCP509 | Changes to Market Domain Data |
| BSCP602 | SVA Metering System and Asset Metering System Register |

### 1.6 NETSO Registration Requirements

FPN flag set to Yes

Where the Party is registering a BM Unit which has the FPN flag set to Yes, the Party should consult with the NETSO to ensure compliance with the Grid Code and the Connection and Use of System Code regarding timescales. Failure to comply with the Grid Code and the Connection and Use of System Code may delay the registration of the BM Unit and hence the Party would not be able to trade using that BM Unit. The delay may be as a result of procurement, installation and testing of operational metering and Electronic Data Transfer (EDT) and Electronic Despatch Logging (EDL) facilities, as appropriate. This BSCP refers to the last stage of the registration process of the BM Unit.

Offshore Power Park Modules

Where the Party has 2 or more Offshore Power Park Modules for whose Exports the Metering System(s) is or are registered in CMRS, the Party may either:

Apply to register each Power Park Module as a separate Primary BM Unit; or

Apply to register a single Primary BM Unit for some or all of the Offshore Power Park Modules (a ‘Combined Offshore BM Unit’).

A Party may only register a Combined Offshore BM Unit if the NETSO determines that the requested configuration of Offshore Power Park Modules is suitable to constitute a single Primary BM Unit. Where the Party requests a Combined Offshore BM Unit in its Registration of Primary BM Unit form BSCP15/4.1, BSCCo will confirm with the NETSO whether it approves the configuration. BSCCo recommends that the Party consults with the NETSO before submitting this form, to avoid any delay in the registration process.

1.7 BSC Website list of Suppliers which have satisfied the criteria to complete a change of Primary BM Unit Lead Party within 5WDs for a Primary BM Unit with CVA metering and associated with a Customer premises

BSCCo will publish and maintain a list on the BSC Website of the Party Name and ID of those Suppliers who satisfy the criteria referred to in section 3.14 of this procedure, and who have submitted a completed form BSCP15/4.10 Part A3 to BSCCo in accordance with 3.15.1.

Note that BSCP15/4.11 Parts A and B must be received by BSCCo prior to a Change of Primary BM Unit Lead Party becoming Effective. The Primary BM Unit Effective From Date requested on the (re) registration form must be the calendar date after the Effective To Date requested on the de-registration form.

Where a BM Unit has the FPN flag set to “Yes” Parties must comply with the NETSO Registration Requirements, especially paragraph 1.6 above, and the BM Unit’s Effective From Date will be the same as the NETSO Commission Date.

Any change of Primary BM Unit Lead Party must be approved by BSCCo before the requirements of this and any related procedure are initiated.

### 1.8 Obligations

Parties must have successfully completed Qualification under Section O of the BSC before the Effective From Date of a BM Unit registration in order for that BM Unit registration to become effective. However, Parties may begin the process of registering BM Units in accordance with this BSCP before they have completed Qualification under Section O of the BSC (relating to communications requirements), provided that they have begun the process of obtaining such Qualification.

### 1.9 Primary BM Units for CFD or CM Assets

The BSC requires that Primary BM Units with CFD Assets shall not include Assets relating to more than one Contract for Difference or any other Assets (non-CFD Assets) unless that is permitted under the Contracts for Difference applying to those CFD Assets or agreed to in writing by the CfD Counterparty.

Primary BM Units for CFD Assets Registered in Central Meter Registration Service (CMRS)

Lead Parties will be able to register Primary BM Units for Metering Systems registered in CMRS under the existing processes and approach. This is because in CMRS the Primary BM Unit is specific to the Generating Unit and it is therefore possible to change Primary BM Unit ownership (retaining the same identifier). The Primary BM Unit can therefore exist for the lifetime of the Generating Unit, and consequently the lifetime of the CFD. This means that new registration arrangements or processes are not necessary.

Primary BM Units for CFD or CM Assets Registered in SMRS

Additional Primary BM Units are not a permitted CM Metering option. Metered volumes associated with CM Assets registered in SMRS cannot be provided to a CM Settlement Services Provider using Additional Primary BM Units. CM Assets may still be allocated to Additional Primary BM Units, registered under process 3.4.

Additional Primary BM Units for CFD Assets registered in SMRS may be provided to a CFD Settlement Services Provider (CFDSSP) to be used for CFD Settlement purposes. The registration of Additional Primary BM Units for CFD Assets shall follow process 3.18. Additional Primary BM Units for non-CFD Assets registered in SMRS should follow 3.4.

Additional Primary BM Units for CFD Assets Registered in SMRS

Both Lead Parties and BSCCo may initiate the registration process for Additional Primary BM Units for CFD Assets registered in SMRS using process 3.18. Additional Primary BM Units for CFD Assets are not liable for the Section D charge for Additional Primary BM Units. Consequently all Additional BM Unit registrations for CFD Assets must be confirmed with or instructed by the CFDSSP, and shall follow a naming convention.

The CFDSSP instructs Additional Primary BM Unit registration details to BSCCo based on information that generators with a CFD are obliged to notify to the CFDSSP, such as when the Additional Primary BM Units are needed. This reduces the need for Lead Parties to manage the Additional Primary BM Unit registration process. Lead Parties should find Additional Primary BM Units are registered and available for use when needed.

Where it is not known which Supplier will take responsibility for Metering Systems associated with a generator with a CFD, BSCCo will register Additional Primary BM Units for a set of Suppliers. The set will be based on a list maintained by BSCCo. The list is maintained in accordance with section 3.20. Each set of Additional Primary BM Units will be associated with the relevant CFD for the lifetime of the CFD. Only one of the Additional Primary BM Units in the set shall be ‘active’ on any particular Settlement Day.

In SMRS the Primary BM Unit represents the Supplier’s Metering System(s), so the Generating Unit(s) must be assigned to an Additional Primary BM Unit so that the Primary BM Unit Metered Data relates to the relevant CFD and can therefore be used by the CFDSSP for CFD Settlement purposes.

CFD Generating Unit(s) must move between Additional Primary BM Units as responsibility under the BSC for the Metering System(s) changes i.e. as a CFD generator changes Suppliers/Offtakers its Metering Systems must move from its old Supplier’s Additional Primary BM Unit to its new Supplier Additional Primary BM Unit. Supplier Primary BM Unit ownership can only take place when a Supplier transfers its Supplier ID i.e. ownership of the Supplier ID (and license) is transferred. Additional Primary BM Units registered for CFD Assets will therefore only last for the lifetime of the CFD. When the CFD expires the CFDSSP will instruct BSCCo to deregister the relevant Additional Primary BM Units to coincide with the expiry of the CFD. The CFDSSP will know when a CFD expires.

### 1.10 Trading Secondary BM Units

A Trading Secondary BM Unit is a Secondary BM Unit for which the Lead Party holds the VTP Participant Role. Trading Secondary BM Units have Production and Consumption Account (unlike a VLP or an AMVLP) and the VTP must submit GC and DC values based upon its expected Maximum and Minimum Deviation Volumes.

Where the Lead Party of a (non-Trading) Secondary BM Unit – i.e. a VLP and / or an AMVLP - subsequently Qualifies as a VTP, then all of their Secondary BM Units will automatically become Trading Secondary BM Units.

A VTP who is not also a VLP and / or an AMVLP may only use its Trading Secondary BM Units in the Wholesale Market. A Trading Secondary BM Unit must be Baselined. No NGC BM Unit is required for a Trading Secondary BM Unit operating only in the Wholesale Market

A VTP which is also a VLP and / or an AMVLP may use its Trading Secondary BM Units in both the Wholesale Market and in the Balancing Mechanism. A VTP which is also an AMVLP may allocate AMSID Pairs to its Trading Secondary BM Units

## 2. Acronyms and Definitions

### 2.1 List of Acronyms

The following is a list of acronyms used in BSCP15:

| Acronym | Expression |
|---|---|
| AMSID | Asset Metering System Identifier |
| AMVLP | Asset Metering Virtual Lead Party |
| BMRA | Balancing Mechanism Reporting Agent |
| BSCCo | Balancing and Settlement Code Company |
| CDCA | Central Data Collection Agent |
| CFD | Contract For Difference |
| CFDSSP | Contract for Difference Settlement Services Provider |
| CM | Capacity Market |
| CMRS | Central Meter Registration Service |
| CRA | Central Registration Agent |
| CoPBLP | Change of Primary BM Unit Lead Party |
| CVA | Central Volume Allocation |
| DNC | Declared Net Capacity |
| EDL | Electronic Dispatch Logging |
| EDT | Electronic Data Transfer |
| EFD | Effective From Date |
| ETD | Effective To Date |
| FPN | Final Physical Notification |
| GSP | Grid Supply Point |
| IA | Interconnector Administrator |
| ID | Identifier |
| LDSO | Licensed Distribution System Operator |
| MDD | Market Domain Data |
| MSID | Metering System ID |
| NETSO | National Electricity Transmission System Operator |
| P/C | Production / Consumption |
| SEV | Settlement Expected Volume |
| SMRA | Supplier Meter Registration Agent |
| SPD | Settlement Period Duration |
| SVAA | Supplier Volume Allocation Agent |
| SVA | Supplier Volume Allocation |
| TSBP | Transmission System Boundary Point |
| VAU | Volume Allocation Unit |
| VLP | Virtual Lead Party |
| VTP | Virtual Trading Party |
| WD | Working Day |

### 2.2 List of Definitions

AMSID Pair

One Import AMSID and, where applicable, one Export AMSID whose Half Hourly Asset Metering Systems are situated behind the Boundary Point for the purposes of offering Balancing Services.

Baselined BM Unit

A BM Unit that has at least one MSID Pair registered that will have its expected energy flows calculated through a Baseline Methodology.

Contracted LDSO

The Contracted LDSO is an LDSO who has the obligation to provide the SMRS service to the Registrant of the Metering System.

Control Point

As defined in the Grid Code.

Declared Net Capacity

In relation to a generating station, it is the output of that station to the Total System multiplied by the relevant following constant:

Station driven by tidal/wave power – 0.33

Station driven by wind power – 0.43

Station driven by solar power – 0.17

All others – 1.0

This term is used in statutory instrument 2001 No. 3270 The Electricity (Class Exemptions for the Requirement for a Licence) Order 2001.

Effective From Date

The Settlement day from which the Primary and Secondary BM Unit is allowed to trade.

Effective To Date

The final Settlement day that the Primary and Secondary BM Unit is allowed to trade.

GC or DC Breach

The positive or negative value of QMij for the BM Unit divided by SPD has exceeded the GC by the GC Limits or has exceeded the DC by the DC Limits. The GC or DC Limits are defined in Section K3.4.3A

MSID Pair

One Import MSID and, where applicable, one Export MSID whose Half Hourly Metering Systems are situated at a single Boundary Point for the purposes of offering Balancing Services or Wholesale Market Activities...

NETSO Commission Date

The date from 0000 hours on which the BM Unit can trade through the NETSO Systems.

Nominated Licensed Distribution System Operator

The Nominated LDSO is the LDSO which has obligations to submit the GSP Group Metered Volume Aggregation Rules.

Non-Standard Primary BM Unit

A configuration of Plant and Apparatus determined by the Panel to be a single Primary BM Unit in accordance with BSC Section K3.1.6.

Operational Metering

The Metered data associated with the Primary and Secondary BM Unit which is utilised by the NETSO.

Production / Consumption (P/C) Flag

The flag within CRA Systems which records either the fixed P/C Status elected for an Exempt Export Primary BM Unit by the Lead Party, or the fixed P/C Status allocated to an Interconnector Primary BM Unit or the fixed P/C Status elected for a Secondary BM Unit by the Virtual Lead Party or Asset Metering Virtual Lead Party or the fixed P/C Status elected for a Storage BM Unit.

Self-Service Gateway

An online portal, accessible through the BSC Website, that allows authorised users to provide and maintain registration data, including (but not limited to) the data defined in this BSCP.

Standard Primary BM Unit

A configuration of Plant and Apparatus that forms one of the single Primary BM Units set out in BSC Section K3.1.4.

Supplier ID Transferee

Trading Party that will become responsible for the relevant Supplier ID.

Supplier ID Transferor

Trading Party Transferring the relevant Supplier ID.

Trading Agent

The Balancing Mechanism Lead Party or their Agent, registered as submitting data to or receiving data from the NETSO, in respect of Primary and Secondary BM Units assigned to them.

Trading Point

A commercial and, where so specified in the Grid Code, an operational interface between a user and the NETSO, which a user has notified to the NETSO.

All other terms are as defined in the Code

## 3. Interface and Timetable Information

### 3.1 Registration of Primary BM Unit Associated with Metering Systems Registered with the CRA4

A Party applying for a new Storage BM Unit should follow procedure 3.1, and elect their P/C flag in form BSCP15/4.1. A Party with an existing Non-Storage BM Unit applying to change their classification to a Storage BM Unit should follow procedure 3.12, and elect their P/C flag in form BSCP15/4.8.

Steps 3.1.1 to 3.1.11 apply to Non-Standard Primary BM Unit Applications.

Steps 3.1.12 onwards apply to both Standard and Non-Standard Primary BM Unit Applications, and follow the preceding steps specific to Non-Standard Primary BM Unit Applications.

A Party applying for Exempt Export status for a new Primary BM Unit registration should follow procedures 3.1 and 3.10 concurrently.

A Party applying for Exempt Export status for an existing Primary BM Unit does not need to follow this procedure 3.1 but should follow procedure 3.10.

Parties undertaking a Change of CVA Primary BM Unit Lead Party for an Exempt Export Primary BM Unit should follow procedure 3.13.

| REF | WHEN | ACTION | FROM | TO | INPUT INFORMATION REQUIRED | MEDIUM |
|---|---|---|---|---|---|---|
| 3.1.1 | At least 60 WD prior to Effective From Date (in the case of Non-Standard Primary BM Units) | If registering a Standard Primary BM Unit go straight to step 3.1.12<br>If the Party does not believe the application meets the requirements for a Standard Primary BM Unit as set out in the Code or the Party requires a Non-Standard Primary BM Unit for another reason, submit application for Non-Standard Primary BM Unit by submitting a form or request via the Self-Service Gateway.<br>Also submit electrical single line diagram(s) clearly showing the proposed configuration, the location of the Metering Equipment, in particular the Settlement current and voltage transformers (CTs/VTs) and CT/VT ratios5, and all existing Boundary Points and any System Connection Points at or near the proposed Boundary Point(s). 6, 7, 8 | Party | BSCCo | BSCP15/4.13 Application for Non-Standard Primary BM Unit signed by an authorised person registered as such using BSCP38. | Email / Self-Service Gateway |
| 3.1.2 | Following 3.1.1 | Check application for Non-Standard Primary BM Unit for completeness and compliance with requirements of BSC Section K3.1. | BSCCo |  | BSCP15/4.13 Application for Non-Standard Primary BM Unit. | Internal process |
| 3.1.3 | Where appropriate for Non-Standard Primary BM Unit | Where additional information or clarifications are required for a determination to be reached, request such information from the Party. | BSCCo | Party | Request for specific information. | Email |
| 3.1.4 | As required for Non-Standard Primary BM Unit and in the timescales required by BSCCo to meet Panel requirements | If request for more information received, provide requested information as agreed between BSCCo and the Party. | Party | BSCCo | Requested information. | Email |
| 3.1.5 | As soon as possible following 3.1.2 or 3.1.4 as appropriate | Send Non-Standard Primary BM Unit for comment on and agreement of the proposed configuration. | BSCCo | NETSO | BSCP15/4.13 Application for Non-Standard Primary BM Unit. | Email |
| 3.1.6 | Within 5WD of 3.1.5 | Provide comments on the proposed configuration and whether it is agreeable. | NETSO | BSCCo |  | Email |
| 3.1.7 | Following 3.1.6 if the NETSO does not agree with the proposed configuration | Notify Party that the NETSO does not agree with the proposed configuration and ask if the Party wishes to proceed with the Non-Standard Primary BM Unit application in its current form. | BSCCo | Party |  | Email |
| 3.1.8 | Following 3.1.7 | Advise BSCCo whether to proceed with the application or not. Go to 3.1.9 or back to 3.1.1 as appropriate. | Party | BSCCo |  | Email |
| 3.1.9 | Following 3.1.6 or 3.1.8 and following receipt of sufficient information in 3.1.1 and if appropriate 3.1.4 and to meet Panel timescales | Prepare and submit Panel paper for consideration. | BSCCo | Panel | Panel paper<br>BSCP15/4.13 Application for Non-Standard Primary BM Unit<br>Electrical single line diagram(s). | Internal process |
| 3.1.10 | At next convenient Panel meeting | Consider application and either approve the Non-Standard Primary BM Unit, defer the Non-Standard Primary BM Unit application pending more information, or reject the Non-Standard Primary BM Unit. | Panel | BSCCo | Panel decision. |  |
| 3.1.11 | Following Panel meeting for Non-Standard Primary BM Unit | Inform Party of Panel decision. Request further information if required. If further information required go back to step 3.1.9. | BSCCo | Party |  | Email |
| 3.1.12 *[footnotes 9,10,11]* | At least 30 WD prior to Effective From Date | Submit Registration of Primary BM Unit form and, if not already submitted, an electrical single line diagram(s) showing the location of the Metering Equipment, in particular the Settlement current and voltage transformers (CTs/VTs) and CT/VT ratios12, and all existing Boundary Points and any System Connection Points at or near the proposed Boundary Point(s). 13, 14, 15<br>Where the BM Unit includes CFD Assets relating to more than one CfD and/or CFD Assets and non-CFD Assets provide the CfD CounterParty’s written confirmation that this is permitted under the relevant Contracts for Difference or has otherwise been agreed. | Party | CRA | BSCP15/4.1, Registration of Primary BM Unit signed by an authorised person, registered as such using BSCP38.<br>Electrical Single Line Diagram (if required)<br>CfD CounterParty written confirmation of agreement that the BM Unit may contain CFD Assets relating to more than one CfD and/or CFD Assets and non-CFD Assets. (if required) | Fax / Post / Email / Self-Service Gateway |
| 3.1.13 | Within 1 WD of receipt of 3.1.12 | Acknowledge receipt of Registration of Primary BM Unit form | CRA | Party |  | Fax / Email / Post / Self-Service Gateway |
| 3.1.14 | At the same time as 3.1.13 | The CRA checks the following:<br>The Party is registered with the CRA<br>The form has been completed by an authorised person.<br>The Effective From Date for the Primary BM Unit is on or after the Effective From Date for the Party. | CRA |  | As submitted in 3.1.2 | Internal Process |
| 3.1.15 | At the same time as 3.1.13 | Where the Primary BM Unit is embedded within a GSP Group, confirm with the SMRA and Party whether the Metering System was previously registered in SMRA, and if “Yes” ensure that the Effective From Date is such that it prevents dual or no registration of supply in accordance with BSCP68. | CRA | Party<br>SMRA | Primary BM Unit Effective From Date.<br>(Where the Primary BM Unit Effective From Date is such that it will have dual or no registration the Party should be informed to register the Primary BM Unit with a new Effective From Date.) | Fax / Email |
| 3.1.16 | At the same time as 3.1.13 | Inform CDCA, NETSO and BSCCo of the intended Primary BM Unit registration. | CRA | CDCA<br>NETSO<br>BSCCo |  | Fax / Email |
| 3.1.17 | At the same time as 3.1.13 | Where the Primary BM Unit is embedded within a Distribution System inform the Contracted LDSO of the registration.<br>Where the Contracted LDSO is not the Nominated LDSO for the GSP Group, CRA should also inform the Nominated LDSO of the registration. | CRA | Relevant LDSO(s) | Primary BM Unit information including Effective From Date | Post / Fax / Email |
| 3.1.18 | At least 20 WD prior to Effective From Date (unless otherwise agreed by the BSC Panel) | For Embedded Primary BM Units, initiate the Line Loss Factor process (BSCP128) by submitting CVA LLFs for MSID | LDSO | BSCCo | CVA Long or Short Format data files in accordance with BSCP128 Appendix 5. Signed by an authorised person as per BSCP38 | Fax, post or email and Electronic Spreadsheet |
| 3.1.19 | Within 5 WD of 3.1.16 | Where the Party is applying to register 2 or more Offshore Power Park Modules as a Combined Offshore BM Unit, the NETSO shall confirm whether it determines that such a configuration is suitable to constitute a single BM Unit Primary BM Unit. | NETSO | CRA<br>BSCCo | A statement as to whether the NETSO determines that the Party’s requested configuration of Offshore Power Park Modules is suitable to constitute a single Primary BM Unit | Fax / Email / Post |
| 3.1.20 | Within 5 WD of 3.1.16 and (if applicable) at the same time as 3.1.19 | The NETSO may object to the registration. | NETSO | CRA | A statement detailing the nature of the objection<br>Where an objection cannot be resolved, the CRA shall escalate the objection to BSCCo | Fax / Email / Post |
| 3.1.21 | Within 5WDs of 3.1.16 if applicable | Where the BM Unit contains CFD Assets relating to more than one CfD and/or both CFD Assets and non-CFD Assets, and the CfD CounterParty’s written confirmation was not provided in 3.1.12, inform CfD CounterParty of the proposed configuration. | BSCCo | CfD CounterParty | BSCP15/4.1, Registration of Primary BM Unit signed by an authorised person, registered as such using BSCP38.<br>Electrical Single Line Diagram (if required) | Fax / Email / Post |
| 3.1.22 | Within 5WDs of 3.1.21 | Confirm CfD CounterParty agreement to the BM Unit including CFD Assets relating to more than one CfD and/or both CFD Assets and non-CFD Assets. | CfD CounterParty | BSCCo | CfD CounterParty written confirmation of agreement to the BM Unit configuration or rejection of the BM Unit configuration | Fax / Email / Post |
| 3.1.23 | 15 WD prior to the Effective From Date | BSCCo to send data to CRA.<br>CRA to register the Working Day Credit Assessment Load Factor (WDCALF), Non-Working Day Credit Assessment Load Factor (NWDCALF), Supplier Export Credit Assessment Load Factor (SECALF) and Transmission Loss Factor (TLF) data for the Primary BM Unit and ensure that this data is registered prior to the Effective From Date of the Primary BM Unit. | BSCCo | CRA | WDCALF, NWDCALF and SECALF data – Credit Assessment Load Factors (CRA-I011)<br>Transmission Loss Factors (CRA-I029) | Email |
| 3.1.24 | 5 WD prior to Effective From Date | CDCA to confirm the following:<br>Whether the Metering System proving test associated with the Primary BM Unit has been completed successfully.<br>The Aggregation Rules have been successfully registered for the Primary BM Unit in accordance with BSCP75.<br>The Aggregation Rules of any existing VAUs have been updated, if required where another BM Unit is connected at the same CVA Boundary Point and the registration of the new BM Unit affects the Aggregation Rules of the existing VAUs. | CDCA | CRA | Metering System proving test results, Meter Aggregation Rules<br>(Where confirmation has not been provided the Primary BM Unit registration shall remain pending.)<br>Email / Fax / | Electronic |
| 3.1.25 | On or before Effective From Date | Provide Party and BSC Agents with registration reports. | CRA | Party<br>NETSO and BSCCo<br>BSC Agents | Registration reports of data entered onto Systems including Effective From Date – Registration Report (CRA-I014),<br>Operations Registration Report<br>(CRA – I020),<br>BM Unit, Interconnector and GSP Group Data (CRA-I015). | Electronic |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 3.2 Registration of Interconnector Primary BM Units

| REF | WHEN | ACTION | FROM | TO | INPUT INFORMATION REQUIRED | MEDIUM |
|---|---|---|---|---|---|---|
| 3.2.1 | At least 30 WD prior to Effective From Date | Submit Registration of Primary BM Unit form or information via the Self-Service Gateway.<br>Inform the NETSO of Primary BM Unit registration | Party | Party<br>CRA<br>NETSO | BSCP15/4.1, Registration of Primary BM Unit signed by an authorised person, registered as such using BSCP38.<br>Fax / Email / Post / Self-Service Gateway | Fax / Email |
| 3.2.2 | Within 1 WD of receipt of 3.2.1 | Acknowledge receipt of Registration of Primary BM Unit request | CRA | Party |  | Fax / Email / Post / Self-Service Gateway |
| 3.2.3 | At the same time as 3.2.1 | The CRA checks the following:<br>The Party is registered with the CRA as an Interconnector User.<br>The form has been completed by an authorised person.<br>The Effective From Date for the Primary BM Unit is on or after the Effective From Date for the Party. | CRA |  | As submitted in 3.2.1 | Internal Process |
| 3.2.4 | At the same time as 3.2.2 | Inform CDCA, the NETSO and BSCCo of the intended Primary BM Unit registration. | CRA | CDCA<br>NETSO<br>BSCCo |  | Fax / Email /Self-Service Gateway |
| 3.2.5 | Within 5 WD of 3.2.4 | The NETSO may object to the registration. | NETSO | CRA | A statement detailing the nature of the objection | Fax / Email / Post |
| 3.2.6 | 15 WD prior to the Effective From Date | BSCCo to send data to CRA.<br>CRA to register the Transmission Loss Factor (TLF) data for the Primary BM Unit and ensure that this data is registered prior to the Effective From Date of the Primary BM Unit16. | BSCCo | CRA<br>Transmission Loss Factors (CRA-I029) |  | Email |
| 3.2.7 | On or before Effective From Date | Provide Party and BSC Agents with registration reports. | CRA | Party<br>NETSO and BSCCo<br>BSC Agents | Registration reports of data entered onto systems including Effective From Date – Registration Report (CRA-I014),<br>Operations Registration Report (CRA – I020),<br>BM Unit, Interconnector and GSP Group Data (CRA-I015). | Electronic |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 3.3 Notification of a New Supplier or Supplier ID and Base Primary BM Unit IDs

This process does not cover the Registration of a Party. For this procedure, refer to BSCP65.

If a Supplier is applying for Exempt Export status for a Base Primary BM Unit, then procedure 3.10 should also be followed (either concurrently or subsequently, depending on the timing of the Supplier’s application for Exempt Export status).

Parties undertaking a Transfer of Supplier ID whose associated Primary BM Units include any Exempt Export Primary BM Units should follow procedure 3.14 and, where necessary/appropriate, procedure 3.12.

| REF | WHEN | ACTION | FROM | TO | INPUT INFORMATION REQUIRED | MEDIUM |
|---|---|---|---|---|---|---|
| 3.3.1 | At least 30 WD prior to Effective From Date | Notification of a new Supplier or Supplier ID.<br>(The requirement for 30WDs notice may be reduced if there is agreement between the CRA/BSCCo/Party/NETSO and that this date coincides with a MDD publication date.) | BSCCo | CRA | Supplier Name, Supplier ID and Effective From Date | Fax / Email / Self-Service Gateway |
| 3.3.2 | Upon notification of 3.3.1 | The CRA shall register Primary BM Unit identifiers, one for each GSP Group which shall be used for allocating SMRA consumption data for the Supplier or Supplier ID. | CRA |  | Notification of new Supplier or Supplier ID. | Internal Process |
| 3.3.3 | At the same time as 3.3.2 | Allocate each Base Primary BM Unit to the Base Trading Unit for the relevant GSP Group (and set the Base Trading Unit Flag for each Primary BM Unit).17, 18 | CRA |  | Creation of new Base Primary BM Units for each GSP Group | Internal Process |
| 3.3.4 | At the same time as 3.3.2 | Notify SVAA and BSCCo of the Base Primary BM Units registered. | CRA | SVAA<br>BSCCo | BM Unit and GSP Group Data (CRA-I015) including Supplier ID, BM Unit IDs and the Effective From Date<br>Registration Report (CRA-I014)<br>(Where a Base Primary BM Unit will exceed the NETSO’s de minimis requirements to submit Physical Notifications the Party is required to notify the NETSO) | Electronic |
| 3.3.5 | On receipt of data in 3.3.4 | CRA to receive and register the Working Day Credit Assessment Load Factor (WDCALF), Non-Working Day Credit Assessment Load Factor (NWDCALF), Supplier Export Credit Assessment Load Factor (SECALF), and Transmission Loss Factor (TLF) data for the Primary BM Unit and to ensure that this data is registered prior to the Effective From Date of the Primary BM Unit. | BSCCo | CRA | WDCALF, NWDCALF and SECALF data – Credit Assessment Load Factors (CRA-I011)<br>Transmission Loss Factors (CRA-I029) | Email |
| 3.3.6 | Prior to the effective date of the Base Primary BM Units | Supplier to complete the Primary BM Unit registrations by providing the initial GC/DC values and FPN Flag and where appropriate the NGC Primary BM Unit Name. | Party | CRA | BSCP15/4.1, Registration of Primary BM Unit signed by an authorised person, registered as such using BSCP38. | Fax / Post / Email / Self-Service Gateway |
| 3.3.7 | On or before Effective From Date | Provide Party and BSC Agents with registration reports. | CRA | Party<br>BSC Agents<br>NETSO<br>BSCCo | Standing data reports of data entered onto systems (CRA-I014, CRA-I015 and CRA-I020).<br>Electronic<br>(Fax/Email to BSC Agents and BSCCo) |  |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 3.4 Registration of Additional Primary BM Unit (Supplier Only)

A Supplier applying for Exempt Export status for a new Additional Primary BM Unit should follow procedures 3.4 and 3.10 concurrently.

A Supplier applying for Exempt Export status for an existing Additional Primary BM Unit does not need to follow this procedure 3.4 but should follow procedure 3.10.

Parties undertaking a Transfer of Supplier ID whose associated BM Units include any Exempt Export Primary BM Units should follow procedure 3.14 and, where necessary/appropriate, procedure 3.12.

A Supplier registering an Additional Primary BM Unit for CFD Assets should not follow this procedure 3.4, but should follow procedure 3.18.

| REF | WHEN | ACTION | FROM | TO | INPUT INFORMATION REQUIRED | MEDIUM |
|---|---|---|---|---|---|---|
| 3.4.1 | As required, but before 3.4.2. | Initiate Market Domain Data (MDD) process (BSCP509) | Originator | BSCCo | Form BSCP509/01 & relevant part of entity forms document. | Fax / Email |
| 3.4.2 | At least 1519 WD prior to Effective From Date if FPN flag set to ‘no’, or 30 WD19 prior to Effective From Date if FPN flag set to ‘yes’ | Submit Registration of Primary BM Unit form20 or complete relevant sections of the Self-Service Gateway<br>Effective From Date must be on or after the MDD Go Live Date. | Party | CRA | BSCP15/4.1, Registration of Primary BM Unit signed by an authorised person, registered as such using BSCP38.<br>Where a Party wishes for a Settlement Expected Volume (SEV) to replace the FPN they will indicate that the BM Unit is a Baselined BM Unit in form BSCP15/4.1.<br>Fax / Post / Email / Self-Service Gateway | Email / Self-Service Gateway |
| 3.4.3 | Within 1 WD of receipt of 3.4.2 | Acknowledge receipt of Registration of Primary BM Unit request | CRA | Party | As submitted in 3.4.2 | Fax / Email / Self-Service Gateway |
| 3.4.4 | At the same time as 3.4.3 | Check that the Party is registered with the CRA and that the form or the relevant part of the Self-Service Gateway has been completed by an authorised person. Also check the registration data to confirm the FPN flag has been set correctly. | CRA |  | As submitted in 3.4.2 | Internal Process |
| 3.4.5 | At the same time as 3.4.3 | Allocate the Additional Primary BM Unit to the Base Trading Unit for the relevant GSP Group (and set the Base Trading Unit Flag for each Primary BM Unit).21, 22 | CRA |  | As submitted in 3.4.2<br>Creation of new Additional Primary BM Unit for a GSP Group | Internal Process |
| 3.4.6 | At the same time as 3.4.3 | In all cases inform BSCCo of the Additional Primary BM Unit Registrations. | CRA | BSCCo | Manual request for authorisation | Fax / Email / Self-Service Gateway |
| 3.4.7 | On receipt of data in 3.4.6 | CRA to receive and register the Working Day Credit Assessment Load Factor (WDCALF), Non-Working Day Credit Assessment Load Factor (NWDCALF), Supplier Export Credit Assessment Load Factor (SECALF), and Transmission Loss Factor (TLF) data for the Primary BM Unit and to ensure that this data is registered prior to the Effective From Date of the Primary BM Unit. | BSCCo | CRA | WDCALF, NWDCALF and SECALF data – Credit Assessment Load Factors (CRA-I011)<br>Transmission Loss Factors (CRA-I029) | Email |
| 3.4.8 | Following 3.4.7 | Confirm all steps in the Primary BM Unit registration process have been completed. | CRA | BSCCo | Completed BSCCo Checklist | Fax / Email / Self-Service Gateway |
| 3.4.9 | Within 1 WD of 3.4.2 but after 3.4.4 | Inform Party, BSCCo, NETSO and BSC Agents of the Primary BM Unit registration. | CRA | BSCCo<br>NETSO<br>SVAA<br>BSC Agents<br>Party | CRA-I020.<br>BM Unit, Interconnector and GSP Group Data to SVAA (CRA-I015)<br>Registration Report (CRA-I014) to Parties.<br>Electronic<br>(Email / Fax to BSC Agents and BSCCo) |  |
| 3.4.10 | Following publication of final MDD circular | ‘Point of no return’. In order to ensure full data consistency across all BSC Agent and the NETSO systems a pending Additional Primary BM Unit registration cannot be withdrawn or amended beyond this point except by prior agreement with BSCCo.23 |  |  |  |  |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 3.5 De-Registration of Primary BM Unit Excluding Base Primary BM Unit

Not required for Change of CVA Primary BM Unit Lead Party

| REF | WHEN | ACTION | FROM | TO | INPUT INFORMATION REQUIRED | MEDIUM |
|---|---|---|---|---|---|---|
| 3.5.1 | At least 25 WD prior to the Effective To Date | Where the circuits associated with the Primary BM Unit are to be disconnected from the Transmission Distribution Systems, request a Certificate of Disconnection. | Party | LDSO24<br>Or<br>NETSO | Request for Certificate of Disconnection | Fax / Post / Email |
| 3.5.2 | Within 5 WD of 3.5.1 | Send Certificate of Disconnection. | LDSO | Or<br>NETSO<br>CRA<br>Party | Where appropriate a Certificate of Disconnection<br>or<br>BSCP25/5.1 “Deregistration of a TSBP” or BSCP25/5.5 “De-registration of a DSCP”, signed by an authorised person, registered as such using BSCP38.<br>Fax / Post<br>3.5.3 9, 25<br>At least 20 WD prior to Effective To Date<br>Submit de-registration of Primary BM Unit form26 or complete relevant section of the Self-Service Gateway<br>De-registration of Additional Primary BM Units (Supplier only) is processed in parallel with BSCP509 Changes to Market Domain Data27<br>Party<br>CRA<br>BSCP15/4.2, De-Registration of Primary BM Unit signed by an authorised person, registered as such using BSCP38. | Fax / Post / Email / Self-Service Gateway |
| 3.5.4 | Upon receipt of 3.5.3 | Check the form or the Self-Service Gateway for completeness and authorisation (as per BSCP38 Authorisations). | CRA |  |  | Internal |
| 3.5.5 | Within 1 WD of 3.5.4 | Acknowledge receipt of de-registration of Primary BM Unit form | CRA | Party |  | Fax / Post / Email / Self-Service Gateway |
| 3.5.6 | At the same time as 3.5.5 | Notify CDCA, NETSO and BSCCo of the Primary BM Unit de-registration.28 | CRA | CDCA<br>NETSO<br>BSCCo |  | Fax / Email / Self-Service Gateway |
| 3.5.7 | At the same time as 3.5.5 | Where the Primary BM Unit is an additional Supplier Primary BM Unit the CRA shall notify the SVAA of the Primary BM Unit.29 | CRA | SVAA30 |  | Email / Fax |
| 3.5.8 | At the same time as 3.5.5 | Where the Primary BM Unit is embedded within a Distribution System inform the Contracted LDSO of the de-registration.<br>Where the Contracted LDSO is not the Nominated LDSO for the GSP Group, CRA should also inform the Nominated LDSO of the de-registration | CRA | Relevant LDSO(s) | Primary BM Unit information including Effective To Date. | Post / Fax |
| 3.5.9 | Within 1 WD of 3.5.5 | Where the de-registration is associated with an Interconnector, inform the relevant Interconnector Administrator of the Primary BM Unit de-registration. | CRA | IA | Party Name, Primary BM Unit ID(s) and Effective To Date | Fax / Email |
| 3.5.10 | At least 15 WD prior to Effective To Date | Confirmation of Effective To Date. | CRA | CDCA | NETSO / LDSO<br>Party<br>Confirmation of Effective To Date | Fax / Email / Self-Service Gateway |
| 3.5.11 | On or before Effective To Date | Update Systems and provide Party, BSCCo, NETSO and BSC Agents with registration reports. | CRA | Party<br>NETSO and BSCCo<br>BSC Agents | Registration reports of data entered onto Systems – Registration Report (CRA-I014),<br>Operations Registration Report (CRA – I020),<br>BM Unit, Interconnector and GSP Group Data (CRA-I015). | Electronic |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 3.6 De-Registration of Supplier Primary BM Units following Cessation of Supplier

Note: This process is specifically for the de-registration of Supplier Primary BM Units when a Party ceases to be a Supplier and therefore covers both Base Primary BM Units and any Additional Primary BM Units registered in the name of the Supplier and subject to SVA processes. However, it does not cover de-registration of Primary BM Units that are subject to Central Volume Allocation processes. Primary BM Units subject to CVA processes should be de-registered in accordance with section 3.5.

This process does not apply to a transfer of Supplier ID, which should be done in accordance with section 3.14.

| REF | WHEN | ACTION | FROM | TO | INPUT INFORMATION REQUIRED | MEDIUM |
|---|---|---|---|---|---|---|
| 3.6.1 | As required. | Initiate Market Domain Data (MDD) process (BSCP509) | Party | BSCCo | Form BSCP509/01 & relevant part of entity forms document.<br>Effective To Date must be on or after the MDD Go Live Date. | Fax / Email |
| 3.6.2 | At least 30 WD prior to Effective To Date | Notification of cessation of a Supplier.<br>Effective To Date must be on or after the MDD Go Live Date.<br>(The requirement for 30WD notice may be reduced if there is agreement between the CRA/BSCCo/Party/NETSO and that this date coincides with a MDD publication date.) | Party | CRA | Letter detailing the cessation of a Supplier with an Effective To Date and a request to de-register the Primary BM Units associated with the Supplier. This letter must state that the Primary BM Units do not have any associated Supplier Volume Allocation (SVA) Metering. | Post / Email / Self-Service Gateway |
| 3.6.3 | Within 1 WD of receipt of 3.6.2 | Acknowledge receipt of notice of cessation of Supplier. | CRA | Party | Acknowledgement Letter from 3.6.2 | Fax / Email / Self-Service Gateway |
| 3.6.4 | Following 3.6.3 | De-register all Supplier Primary BM Units for that Supplier. | CRA |  | Supplier Primary BM Units for the Supplier with the Effective To Date. | Internal Process |
| 3.6.5 | After 3.6.4 | Inform NETSO and BSC Agents of the Primary BM Units de-registration. | CRA | BSCCo<br>NETSO<br>BSC Agents<br>Party | Registration Report (CRA-I014) containing Supplier name, Supplier ID, Effective To Date, Primary BM Unit Ids<br>Electronic / Email / Fax<br>3.7 Registration of Seasonal Estimates of Maximum Positive Magnitude and Maximum Negative Magnitude for Primary BM Unit Metered Volume and Maximum Positive and Maximum Negative Deviation Volumes for Trading Secondary BM Units<br>For BM Units associated with Metering Systems registered with the CRA, if any change has been made to the configuration of the BM Unit, please refer to section 3.1 and form BSCP15/4.1 to re-register the reconfigured BM Unit. |  |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

| REF | WHEN | ACTION | FROM | TO | INPUT INFORMATION REQUIRED | MEDIUM |
|---|---|---|---|---|---|---|
| 3.7.1 | 10 WD prior to start of next Season | Submit seasonal estimates for the maximum and positive magnitude and maximum negative magnitude Primary BM Unit Metered Volume (QMij) for all Primary BM Units, and / or Maximum Positive and Maximum Negative Deviation Volumes for Trading Secondary BM Units.. | Party | CRA | BSCP15/4.3, Registration of Seasonal Estimates of the maximum and positive and negative Primary BM Unit Metered Volume, and / or Maximum Positive and Maximum Negative Deviation Volumes for Trading Secondary BM Units | Fax / Post / Self-Service Gateway |
| 3.7.2 | Within 1 WD of receipt from 3.7.1 | Acknowledge receipt of Registration of seasonal estimates of the maximum and positive magnitude and maximum negative magnitude Primary BM Unit Metered Volume, and / or Maximum Positive and Maximum Negative Deviation Volumes for Trading Secondary BM Units. | CRA | Party | As submitted in 3.7.1 | Fax / Post / Email / Self-Service Gateway |
| 3.7.3 | Before start of new Season | CRA to update their systems with the GC and DC values derived from the estimated maximum positive magnitude and maximum negative magnitude Primary BM Unit Metered Volume. | CRA |  | As submitted 3.7.1 | Internal |
| 3.7.4 | Within 1 WD of receipt from 3.7.3 | The CRA is to notify, for information only, BSCCo, NETSO, relevant Parties and BSC Agents of the seasonal estimates of the maximum positive magnitude and maximum negative magnitude Primary BM Unit Metered Volume , and Maximum Positive and Maximum Negative Deviation Volumes for Trading Secondary BM Units<br>(The NETSO may request the Panel to review a Party’s submission of the maximum and positive magnitude and maximum negative magnitude Primary BM Unit Metered Volume in accordance with Section K of the Code) | CRA | Party | NETSO, BSCCo<br>BSC Agents<br>Registration Report (CRA-I014) with Seasonal Estimates of the GC/DC for the Primary BM Unit, and for the Trading Secondary BM Unit.<br>Operations Registration Report (CRA – I020),<br>Primary or Secondary BM Unit (CRA – I015).<br>Email / Fax | Electronic |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

3.8 Mid-Season Changes of Generation Capacity and Demand Capacities by the Lead Party, and Maximum Positive and Maximum Negative Deviation Volumes for Trading Secondary BM Units

This process supports the Code obligation on Parties to revise GC/DC capacity of a Primary BM Unit by an amount specified in Section K3.4, and / or GC/DC capacity of a Trading Secondary Unit by an amount specified in Section K8.1.

Parties have the right to downwardly revise the magnitude of DC twice during a BSC Season when the magnitude of the capacity of a Supplier Primary BM Unit and the Deviation Volume of a Trading Secondary BM Unit has decreased. Parties are not permitted to downwardly revise the magnitude of GC.

Parties should note that where a revised GC/DC submission causes a Trading Unit to change its P/C Status in accordance with Section K3.5, any MVRNA Authorisation will be terminated in accordance with Section P3. Parties may therefore need to re-establish such MVRNA Authorisations in accordance with BSCP71.

Where a change in a Primary BM Unit’s Generation Capacity or Demand Capacity results in the FPN Flag being changed to “Yes” the Party is required to complete BSCP15/4.1, or the relevant section of the Self-Service Gateway.

For BM Units associated with Metering Systems registered with the CRA, if the change in Generation Capacity or Demand Capacity is required due to a change to the configuration of the BM Unit, please refer to the BSCP section [new] and form BSCP15/4.1 to re-register the reconfigured BM Unit.

| REF | WHEN | ACTION | FROM | TO | INPUT INFORMATION REQUIRED | MEDIUM |
|---|---|---|---|---|---|---|
| 3.8.1 | At least 1 WD prior to Effective Date. | Submit revised seasonal estimates of the maximum positive magnitude and maximum negative magnitude Primary BM Unit Metered Volume (QMij) for relevant Primary BM Units and maximum positive magnitude and maximum negative magnitude Deviation Volumes for Trading Secondary BM Units.. | Party | CRA | BSCP15/4.4, Mid-Season Changes of Maximum Positive and Negative Primary BM Unit Metered Volume Estimates and maximum positive magnitude and maximum negative magnitude Deviation Volumes for Trading Secondary BM Units | Email / Fax / Post / Self-Service Gateway |
| 3.8.2 | Immediately following receipt in 3.8.1 | Acknowledge receipt of changes of seasonal estimates of the maximum positive magnitude and maximum negative magnitude Primary BM Unit Metered Volume and maximum positive magnitude and maximum negative magnitude Deviation Volumes for Trading Secondary BM Units.. | CRA | Party | As submitted in 3.8.1 | Email / Fax / Self-Service Gateway |
| 3.8.3 | Within 1 WD of receipt from 3.8.1 | The CRA is to notify BSCCo of the revised seasonal estimates of the maximum positive magnitude and maximum negative magnitude Primary BM Unit Metered Volume and maximum positive magnitude and maximum negative magnitude Deviation Volumes for Trading Secondary BM Units. | CRA | BSCCo | As submitted in 3.8.1<br>Validation by CRA<br>Email / Fax | Electronic |
| 3.8.4 | Within 1 WD of receipt from 3.8. 1 | If decreasing the magnitude of the DC of a Supplier Primary BM Unit or a Trading Secondary BM Unitt, the CRA will check the number of times the Party has decreased the magnitude of DC for that BSC Season.<br>If Party has reduced magnitude of DC less than twice for that BSC Season, then steps 3.8.5 to 3.8.6 should apply. If DC has already been reduced twice, then steps 3.8.7 to 3.8.8 should apply. | CRA |  | Validation by CRA | Internal Process |
| 3.8.5 | Within 1 WD of receipt from 3.8.1, if appropriate following 3.8.4 | CRA to update their systems with the revised estimates, to commence from the Effective From Date requested by the Party. | CRA |  | As submitted in 3.8.1 | Internal Process |
| 3.8.6 | At the same time as 3.8.5 | CRA to notify Party of revised estimates | CRA | Party | Registration Report (CRA-I014) with seasonal estimates for the Primary BM Unit or Trading Secondary BM Unit. | Electronic |
| 3.8.7 | Within 1 WD of receipt from 3.8.1, and following 3.8.4 if the Party has reduced the magnitude of DC more than twice | CRA to update internal records and does not process any GC/DC changes. | CRA |  |  | Email / Fax |
| 3.8.8 | At same time as 3.8.7 | CRA to notify Party that DC reduction has not been allowed, and the reason why. | CRA | Party |  | Email / Fax |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 3.9 GC and DC Breach Monitoring by CRA and GC or DC Estimation Challenges by the Lead Party

This process supports the Code obligation on CRA to carry out periodic GC and DC Breach Monitoring as specified in Section K3.4.7A and Section K8.1, where a breach has been identified for either a Primary BM Unit or a Trading Secondary BM Unit, replace GC or DC with a revised value derived from the CRA-Estimated GC or DC Amount. The Lead Party of the BM Unit may challenge this through a GC or DC Estimation Challenge31.

If BSCCo upholds a GC or DC Estimation Challenge, any resultant decrease to the magnitude of the DC of a Supplier Primary BM Unit will not count towards the two permitted downwards mid-season changes to the DC, as specified in Section K3.4.2A.

| REF | WHEN | ACTION | FROM | TO | INPUT INFORMATION REQUIRED | MEDIUM |
|---|---|---|---|---|---|---|
| | **GC and DC Breach Monitoring** | | | | | |
| 3.9.1 | As required. | Monitor Primary BM Unit Metered Volumes or Trading Secondary BM Unit Deviation Volumes from the current BSC Season to identify GC and DC Breaches. | CRA |  | GC and DC Limits | Internal Process |
| 3.9.2 | Where a GC or DC breach has been identified in 3.9.1. | Send GC or DC Breach Notification, including CRA-Estimated GC or DC Amount. | CRA | Party<br>BSCCo | CfD Service Provider<br>CM Service Provider<br>CRA-I048 ‘GC or DC Breach Notification’ | Email / Self-Service Gateway |
| 3.9.3 | Where a GC or DC breach has been identified in 3.9.132. | CRA to update the relevant Primary BM Unit’s or Trading Secondary BM Unit’s registration details with the CRA-Estimated GC or DC Amount, to become effective from the next Working Day. | CRA |  | CRA-Estimated GC or DC Amount.<br>Internal Process<br>GC or DC Estimation Challenges by the Lead Party |  |
| 3.9.4 | If required, no later than 2 full WDs of 3.9.2. | Party to raise a GC or DC Estimation Challenge. | Party | CRA and/or BSCCo33 | CRA-I049 ‘GC or DC Breach Estimation Challenge’ | Email / Self-Service Gateway |
| 3.9.5 | Within 2WDs of 3.9.4. | BSCCo to review evidence submitted by Party and notify Party whether GC or DC Estimation Challenge has been upheld or rejected. | BSCCo | Party | CRA-I049 ‘GC or DC Breach Estimation Challenge’ | Email / Self-Service Gateway |
| 3.9.6 | Immediately following completion of 3.9.5. | BSCCo to notify CRA of GC or DC Estimation Challenge outcome, including any revised BSCCo-Determined GC or DC Estimates. | BSCCo | CRA | CRA-I050 ‘GC or DC Breach Estimation Challenge Decision’ | Email / Self-Service Gateway |
| 3.9.7 | Within 1WD of receipt from 3.9.8. | CRA to update the relevant Primary BM Unit or Trading Secondary BM Unit’s registration details with any changes to GC or DC values34, to become effective from the next Working Day35. | CRA |  | CRA-I050 ‘GC or DC Breach Estimation Challenge Decision’ | Internal Process |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 3.10 Application for Exemptable Generating Plant Status and Exempt Export Status for the Associated Primary BM Unit(s)

This process supports a Lead Party’s ability under Section K1.5 to apply for Exemptable status for its Generating Plant. If the Party’s application is successful, the Primary BM Unit(s) comprising the Exemptable Generating Plant will be granted Exempt Export status.

In accordance with Sections K1.5 and K3.5, the Lead Party must elect whether the P/C Status of each of its Exempt Export Primary BM Units is to be Production or Consumption. To do this, the Lead Party must elect a P/C Flag setting of either Production or Consumption for each Primary BM Unit as part of its application for Exemptable Generating Plant status. The Lead Party’s elected P/C Flag setting will apply from the date that the Primary BM Unit’s Exempt Export status (if granted) becomes effective. It will override the normal determination of P/C Status described in K3.5.2 such that the Exempt Export Primary BM Unit’s P/C Status will be fixed as either Production or Consumption accordingly.

Once a Primary BM Unit has been granted Exempt Export status, its P/C Status as elected by the Lead Party through the Primary BM Unit’s P/C Flag setting does not change unless the Lead Party makes a new election (by following procedure 3.12 or 3.13 as appropriate) or the Primary BM Unit’s Exempt Export status is terminated (by following procedure 3.11).

| REF | WHEN | ACTION | FROM | TO | INPUT INFORMATION REQUIRED | MEDIUM |
|---|---|---|---|---|---|---|
| 3.10.1 | As required. | At least 20 WD prior to Requirement Date<br>Party provides BSCCo with details of the Generating Plant, the reasons for which the Party believes the Generating Plant to be Exemptable, and the P/C Flag that the Lead Party elects for each associated Primary BM Unit should Exemptable status be granted.<br>Or for a Generating Plant whose Exports are measured by SVA Metering Systems, Party provides BSCCo with certification that the Generating Plant is Exemptable and notification of the P/C Flag that the Lead Party elects for each associated Primary BM Unit should Exemptable status be granted. | Party | BSCCo<br>EITHER | Application for Exemptable Generating Plant Status BSCP15/4.5 – (Part A), plus any supporting information where appropriate<br>OR<br>Certification of Exemptable Status for Generating Plant With Exports Measured by SVA Metering Systems BSCP15 / 4.9 – (Part A), plus any supporting information where appropriate | Fax / Post / Email / Self-Service Gateway |
| 3.10.2 | Upon receipt of 3.10.1 | Determine if further information or other evidence is required to demonstrate compatibility with the Code. | BSCCo |  |  |  |
| 3.10.3 | If required by BSCCo | Submit further evidence as required. | Party | BSCCo | Details of further information | Fax / Post / Email / Self-Service Gateway |
| 3.10.4 | Within 20 WD of receipt from 3.10.1 | BSCCo verifies whether or not the Generating Plant is Exemptable and notifies the Party of its conclusion.<br>If the Party agrees with BSCCo’s conclusion, BSCCo updates its records accordingly.<br>If the Party does not agree, go to step 3.10.7. | BSCCo | Party<br>EITHER | Application for Exemptable Generating Plant Status BSCP15/4.5 – (Part B)<br>OR<br>Certification of Exemptable Status for Generating Plant With Exports Measured by SVA Metering Systems BSCP15/4.9 – (Part B) | Fax / Post / Email / Self-Service Gateway |
| 3.10.5 | At the same time as 3.10.4 | Where the Generating Plant is granted Exemptable status, BSCCo will notify CRA to set the Exempt Export Flag and P/C Flag for each Primary BM Unit that comprises the Exemptable Generating Plant. | BSCCo | CRA | BSCP15/4.7 Commencement / Termination of Exempt Export Primary BM Unit Status | Fax / Post / Email / Self-Service Gateway |
| 3.10.6 | Within 1 WD of 3.10.5 | Set the Exempt Export Flag and P/C Flag for each Primary BM Unit that comprises the Exemptable Generating Plant.<br>If the Exempt Export Primary BM Unit is Embedded, and unless notified otherwise by the Lead Party in accordance with BSCP31, allocate the Exempt Export Primary BM Unit to the Base Trading Unit for its GSP Group and set the Base Trading Unit Flag for the Primary BM Unit.36<br>If the Exempt Export Primary BM Unit is Directly Connected, and unless notified otherwise by the Lead Party in accordance with BSCP31, allocate the Exempt Export Primary BM Unit to a Sole Trading Unit.36<br>Notify the Lead Party, BSCCo and the NETSO. | CRA | Lead Party<br>BSCCo<br>NETSO<br>BSC Agents | Registration Report CRA – I014<br>Operations Registration Report<br>CRA – I020<br>BM Unit, Interconnector and GSP Group Data CRA – I015 | Electronic, or equivalent |
| 3.10.7 | Upon receipt of 3.10.4 and if the Party disagrees with the decision | BSCCo refers application to the Panel on behalf of Party. | BSCCo | Panel | As submitted in 3.10.1 and, if appropriate 3.10.3. | Post / Email |
| 3.10.8 | Upon receipt of 3.10.7 | Panel determines whether (in its opinion) Generating Plant is Exemptable and notifies BSCCo of its decision. | Panel | BSCCo | Details of decision | Panel Meeting |
| 3.10.9 | Within 1 WD of Panel Meeting | BSCCo notifies Party of Panel’s decision.<br>If the Party agrees with the decision, BSCCo updates its records accordingly.<br>If the Party does not agree with the decision, go to step 3.10.12. | BSCCo | Party | Details of decision | Fax / Post / Email |
| 3.10.10 | At the same time as 3.10.9 | Where the Generating Plant is granted Exemptable status, BSCCo will notify CRA to set the Exempt Export Flag and P/C Flag for each Primary BM Unit that comprises the Exemptable Generating Plant. | BSCCo | CRA | BSCP15/4.7 Commencement / Termination of Exempt Export Primary BM Unit Status | Fax / Post / Email / Self-Service Gateway |
| 3.10.11 | Within 1 WD of 3.10.10 | Set the Exempt Export Flag and P/C Flag for each Primary BM Unit that comprises the Exemptable Generating Plant.<br>If the Exempt Export Primary BM Unit is Embedded, and unless notified otherwise by the Lead Party in accordance with BSCP31, allocate the Exempt Export Primary BM Unit to the Base Trading Unit for its GSP Group and set the Base Trading Unit Flag for the Primary BM Unit.36<br>If the Exempt Export Primary BM Unit is Directly Connected, and unless notified otherwise by the Lead Party in accordance with BSCP31, allocate the Exempt Export Primary BM Unit to a Sole Trading Unit.36<br>Notify the Lead Party, BSCCo and the NETSO. | CRA | Lead Party<br>BSCCo<br>NETSO<br>BSC Agents | Registration Report CRA – I014<br>Operations Registration Report<br>CRA – I020<br>BM Unit, Interconnector and GSP Group Data CRA – I015 | Electronic, or equivalent |
| 3.10.12 | Within 20 WD of receipt from 3.10.9 and if the Party disagrees with the decision | Party refers application to the Authority. | Party | Authority | As submitted in 3.10.1 and, if appropriate 3.10.3. | Fax / Post / Email |
| 3.10.13 | Upon receipt of 3.10.12 | Authority determines whether Generating Plant is Exemptable and notifies Party and BSCCo of its decision.<br>If the Party agrees with the decision, BSCCo updates its records accordingly. | Authority |  | Party BSCCo<br>Details of decision. | Fax / Post / Email |
| 3.10.14 | At the same time as 3.10.13 | Where the Generating Plant is granted Exemptable status, BSCCo will notify CRA to set the Exempt Export Flag and P/C Flag for each Primary BM Unit that comprises the Exemptable Generating Plant. | BSCCo | CRA | BSCP15/4.7 Commencement / Termination of Exempt Export Primary BM Unit Status | Fax / Post / Email / Self-Service Gateway |
| 3.10.15 | Within 1 WD of 3.10.14 | Set the Exempt Export Flag and P/C Flag for each Primary BM Unit that comprises the Exemptable Generating Plant.<br>If the Exempt Export Primary BM Unit is Embedded, and unless notified otherwise by the Lead Party in accordance with BSCP31, allocate the Exempt Export Primary BM Unit to the Base Trading Unit for its GSP Group and set the Base Trading Unit Flag for the Primary BM Unit.36<br>If the Exempt Export Primary BM Unit is Directly Connected, and unless notified otherwise by the Lead Party in accordance with BSCP31, allocate the Exempt Export Primary BM Unit to a Sole Trading Unit.36<br>Notify the Lead Party, BSCCo and the NETSO. | CRA | Lead Party<br>BSCCo<br>NETSO<br>BSC Agents | Registration Report CRA – I014<br>Operations Registration Report<br>CRA – I020<br>BM Unit, Interconnector and GSP Group Data CRA – I015 | Electronic, or equivalent |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 3.11 Termination of Exempt Export Status for a Primary BM Unit

This process supports the termination of Exempt Export status for a Primary BM Unit as triggered by Section K1.5.8.

| REF | WHEN | ACTION | FROM | TO | INPUT INFORMATION REQUIRED | MEDIUM |
|---|---|---|---|---|---|---|
| 3.11.1 | As required | Where the Exempt Export Status is to be terminated, provide CRA with completed form BSCP15/4.7 or relevant part of the Self-Service Gateway, requesting and authorising CRA to unset the Exempt Export Flag and P/C Flag for the Primary BM Unit.<br>Notify the Party of the termination. | BSCCo | CRA<br>Lead Party | Form BSCP15/4.7 Commencement / Termination of Exempt Export Primary BM Unit Status. | Fax / Post / Email / Self-Service Gateway |
| 3.11.2 | Within 1 WD of 3.11.1 | Unset the Exempt Export Flag and the P/C Flag for the Primary BM Unit.37<br>If a CVA Primary BM Unit, ensure that the Primary BM Unit is allocated to a Sole Trading Unit.38<br>If a Supplier (Base or Additional) Primary BM Unit, ensure that the Primary BM Unit is allocated to the Base Trading Unit for its GSP Group.38<br>Notify the Lead Party, BSCCo and the NETSO. | CRA | Lead Party<br>BSCCo<br>NETSO<br>BSC Agents | Registration Report CRA – I014<br>Operations Registration Report<br>CRA – I020<br>BM Unit, Interconnector and GSP Group Data CRA – I015 | Electronic or equivalent |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 3.12 Change of Production / Consumption Status for an Exempt Export Primary BM Unit or Storage BM Unit by the Lead Party

This process supports a Lead Party’s ability under K3.5 and K3.6 to change the previously-elected P/C Status for an Exempt Export Primary BM Unit, or a Storage BM Unit by enabling the Lead Party to change the Primary BM Unit’s P/C Flag setting from Production to Consumption or vice versa.

Parties needing to elect the P/C Status of a new Exempt Export Primary BM Unit for the first time should refer to procedure 3.10 for details of how to set the Primary BM Unit’s P/C Flag.

Parties needing to elect the P/C Status of a new Storage BM Unit for the first time should refer to procedure 3.1 for details on how to set the Primary BM Unit’s P/C flag. A Party with an existing Non-Storage BM Unit applying to change their classification to a Storage BM Unit should follow this procedure for details on how to set their P/C flag.

Where an existing Exempt Export Primary BM Unit, or a Storage BM Unit, is the subject of a Change of CVA Primary BM Unit Lead Party (CoPBLP), Parties should follow procedure 3.13 to ensure that the Party registering the Primary BM Unit as part of the CoPBLP elects the P/C Status that it wishes to apply from the CoPBLP Effective From Date. In these circumstances, it is not necessary to additionally follow procedure 3.12.

Where an existing Exempt Export Primary BM Unit is the subject of a Transfer of Supplier ID (Change of SVA Primary BM Units Ownership), Parties should refer to procedure 3.14 for details of how the Supplier ID Transferee is notified of the Primary BM Unit’s P/C Status. Any Supplier ID Transferee wishing to change the Exempt Export Primary BM Unit’s P/C Status should follow this procedure 3.12.

| REF | WHEN | ACTION | FROM | TO | INPUT INFORMATION REQUIRED | MEDIUM |
|---|---|---|---|---|---|---|
| 3.12.1 | From time to time if the Lead Party requires | Submit notice to the CRA, copied to BSCCo, requesting a change to the Production / Consumption Flag for an Exempt Export Primary BM Unit or Storage BM Unit..<br>The request should contain an effective date for such amendment of at least 2 WD from this notice unless otherwise agreed with the CRA/BSCCo. | Lead Party | CRA<br>BSCCo | Form BSCP15/4.8 Election of Production / Consumption Flag for Exempt Export Primary BM Unit, Storage BM Unit or Secondary BM Unit or Self-Service Gateway equivalent | Fax / Post / Email or Self-Service Gateway equivalent |
| 3.12.2 | Within 1 WD of receipt of 3.12.1 for Exempt Export Primary BM Units only. | CRA ensures that the Exempt Export Flag is set for the Primary BM Unit.<br>This may involve obtaining authorisation from BSCCo. | CRA |  | As submitted in 3.12.1 | Internal |
| 3.12.3 | As soon as practicable after 3.12.2 for Exempt Export Primary BM Units, or 3.12.1 for Storage BM Units. | Where the Exempt Export Flag is set, or for a Storage BM Unit, then amend the P/C Flag for the Primary BM Unit, effective from the specified date (or 2 WD from 3.12.1, if the specified date is less than 2 WD and no reduced timescale has been agreed).<br>Notify the Party of the change to P/C Flag. | CRA | Party<br>Registration Report | CRA – I014 | Electronic |
| 3.12.4 | As soon as practicable after 3.12.3. | Notify BSCCo and BSC Agents of the change to P/C Flag. | CRA | BSCCo<br>BSC Agents | CRA – I020 to BSCCo<br>CRA – I015 to BSC Agents<br>Fax / Email / | Electronic |
| 3.12.5 | As soon as practicable after 3.12.2. | Where the Exempt Export Flag is not set, then do not amend the P/C Flag for the Primary BM Unit.<br>Notify the Party of the rejection of the request. | CRA | Party | Form BSCP15/4.8<br>Specifying reason for rejection. | Fax / Post / Email or Self-Service Gateway equivalent |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 3.13 Change of CVA Primary BM Unit Lead Party

NOTE: Suppliers taking part in this process must have satisfied the criteria detailed in 3.14 and registered with the CRA.

Prior to initiating this process the Party registering the Primary BM Unit(s) as part of the Change of Primary BM Unit Lead Party (CoPBLP) is required to have acceded to the BSC and completed Party registration and qualification. If appropriate, the Party should also have completed all the NETSO requirements.

The timescales noted within this process are based on the existing MSID(s), Primary BM Unit(s) and Trading Unit registrations being transferred from one Party to another with the associated Meter Technical Details (MTDs), Metering Dispensation(s) and Aggregation Rules. If Parties wish to change any of these registrations (for example to effect changes to configuration and entity Ids) then additional BSCPs may need to be followed and/or the lead-time for completing the process may be increased. Where this applies, Parties should contact BSCCo for advice on the process to be followed and documentation required.

If there are no changes to the registration data associated with the Primary BM Units and the prerequisites stated have been met then Parties may use this process in order to transfer Primary BM Unit(s) and associated MSID(s), MTDs, Metering Dispensations, Aggregation Rules and an associated Trading Unit through this procedure. Under these circumstances Parties will not be required to carry out additional steps in this BSCP, BSCP20, BSCP31, BSCP32 and BSCP75 in order to complete the transfer.

Where a Primary BM Unit is already an Exempt Export Primary BM Unit, or a Storage BM Unit, the Party registering the Primary BM Unit as part of a CoPBLP is required to elect the P/C Flag setting (and thereby the P/C Status) which will apply to the Exempt Export Primary BM Unit or Storage BM Unit from the Effective From Date of the CoPBLP. All other registration details (including the Exempt Export Primary BM Unit’s or Storage BM Unit’s Trading Unit) will be unchanged unless a change is expressly requested. Where this applies, Parties should contact BSCCo for further information.

Parties wishing to apply for Exempt Export Primary BM Unit status should refer to procedure 3.10.

| REF | WHEN | ACTION | FROM | TO | INPUT INFORMATION REQUIRED | MEDIUM |
|---|---|---|---|---|---|---|
| 3.13.1 | If required and at least 3 WD prior to 3.13.3 | Request details of current registrations of Primary BM Unit(s), any associated MSID(s) including any Metering dispensations associated with the MSID(s), and of Trading Unit(s).<br>Party registering Primary BM Unit(s)<br>Party de-registering Primary BM Unit(s) | CRA |  | Letter detailing the information required from BSCCo including the site name and if available the Primary BM Unit Id(s). The letter should be signed by a Category ‘A’ or ‘F’ authorised signatory.39 | Fax / Post / Email / Self-Service Gateway |
| 3.13.2 | Within 2 WD of receipt of request in 3.13.1 | Send information requested in 3.13.1. | CRA |  | Party registering Primary BM Unit(s)<br>Party de-registering Primary BM Unit(s)<br>Information requested in 3.13.1. | Fax / Post / Email / Self-Service Gateway |
| 3.13.3 | As required and at least 5 WD prior to date of transfer | Submit BSCP15/4.11 Part A to de-register Primary BM Unit(s)<br>Please note that if the last Primary BM Unit(s) associated with a particular Party role are being de-registered then the Party is advised to also complete a BSCP65/01 form in order to de-register that role.<br>Party de-registering Primary BM Unit(s) | CRA |  | BSCP15/4.11 Part A40 | Fax / Post / Email / Self-Service Gateway |
| 3.13.4 | As required and at least 5 WD prior to date of transfer | Submit BSCP15/4.11 Part B to register Primary BM Unit(s).<br>Please note that if any new Primary BM Unit(s) result in a new Party role being required, the Party is advised to complete a BSCP65/01 form to register that new role and follow BSCP70 to ensure all required qualification tests for the new role have been passed.<br>If Primary BM Unit is already an Exempt Export Primary BM Unit, or a Storage BM Unit, elect the P/C Flag to apply to the Primary BM Unit from the CoPBLP Effective From Date.<br>Party registering Primary BM Unit(s) | CRA |  | BSCP15/4.11 Part B | Fax / Post / Email / Self-Service Gateway |
| 3.13.5 | At the same time as 3.13.3 and 3.13.4 | For Primary BM Units which are part of an existing Trading Unit (other than a Sole or Base Trading Unit) all Lead Parties within the Trading Unit should be informed of the CoPBLP, and should confirm their agreement to the CoPBLP in writing. | CRA | Trading Unit Lead Parties<br>Trading Unit Lead Parties<br>CRA | Details of CoPBLP<br>Confirmation of agreement to the CoPBLP | Fax / Post / Email |
| 3.13.6 | On receipt of both 3.13.3 and 3.13.4 | Validate BSCP15 /4.11 Parts A and B or the relevant information within the Self-Service Gateway.<br>If validation checks are passed, go to 3.13.7<br>If validation checks are failed, go to 3.13.9 | CRA |  | Confirmation that the Party registering the Primary BM Units has acceded, qualified and registered in the appropriate role.<br>Confirmation that the dates specified on both the BSCP15 /4.11 forms Parts A and B or within the Self-Service Gateway are consecutive. | Internal Process |
| 3.13.7 | Within 1 WD of receipt of both 3.13.3 and 3.13.4 | Send copies of BSCP15 /4.11 Parts A and B to the NETSO.<br>Request that the NETSO confirm that they have no objections to the CoPBLP. | CRA | NETSO |  | Fax / Email |
| 3.13.8 | Within 2 WD of receipt of 3.13.7 | Send written confirmation that the NETSO has no objections to the CoPBLP or state that the NETSO has an objection to the CoPBLP and the reasons for this objection.<br>If the NETSO has any objections, go to 3.13.9<br>If the NETSO has no objections, go to 3.13.10 | NETSO | CRA | Confirmation of no objections or objection specified. | Fax / Post / Email |
| 3.13.9 | Within 1 WD of 3.13.6 or 3.13.8 | In the case that the validation checks are failed and/or the NETSO has an objection, inform both Parties of the rejection and the reason for the rejection. | CRA |  | Party de-registering Primary BM Unit(s)<br>Party registering Primary BM Unit(s)<br>Notification of rejection and reasons for the rejection. | Fax / Post / Email / Self-Service Gateway |
| 3.13.10 | Within 1 WD of the Effective From Date | Process CoPBLP in systems. | CRA | NETSO (where appropriate) | BSCP 15/4.11 Parts A and B | Internal Process |
| 3.13.11 | At the same time as 3.13.10 if the Primary BM Unit is an Exempt Export Primary BM Unit or a Storage BM Unit | Set P/C Flag for the Primary BM Unit as elected by the Party in 3.13.4. | CRA |  | BSCP 15/4.11 Part B | Internal Process / Self-Service Gateway |
| 3.13.12 | At the same time as 3.13.10 if the Primary BM Unit is Embedded | Inform the Nominated LDSO of the CoPBLP. | CRA | Nominated LDSO | Party IDs of the Lead Parties registering and de-registering the Primary BM Unit(s), Primary BM Unit Id(s) and the Effective From Date. | Fax / Email |
| 3.13.13 | Within 1 WD of 3.13.12 | Inform NETSO, BSCCo, BSC Agents, Party de-registering the Primary BM Unit(s) and Party registering the Primary BM Unit(s). | CRA | BSCCo<br>NETSO<br>BSC Agents | Party de-registering Primary BM Unit(s)<br>Party registering Primary BM Unit(s)<br>Operations Registration Report to BSCCo & NETSO (CRA-I020)<br>Registration Report to Parties (CRA-I014)<br>Primary BM Unit, Interconnector and GSP Group Data to BSC Agents (CRA – I015)<br>Electronic | Email confirmation to BSCCo |
| 3.13.14 | Within 1 WD of 3.13.12 | Submit Meter Technical details to Party registering the Primary BM Unit(s). | CDCA | Party registering Primary BM Unit(s) | Meter Technical Details (CDCA-I051) | Fax / Email |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 3.14 Transfer of Supplier ID Process (Change of SVA Primary BM Units Ownership)

This process supports the transfer of a Supplier ID and associated SVA Primary BM Units.

Where an existing Exempt Export Primary BM Unit is the subject of a Transfer of Supplier ID (Change of SVA Primary BM Units Ownership), this procedure also describes how the Supplier ID Transferee is notified of the Primary BM Unit’s P/C Status. Any Supplier ID Transferee wishing to change the Exempt Export Primary BM Unit’s P/C Status should follow procedure 3.12.

| REF | WHEN | ACTION | FROM | TO | INPUT INFORMATION REQUIRED | MEDIUM |
|---|---|---|---|---|---|---|
| 3.14.1 | As required | Submit Notification of Supplier ID Transfer.<br>If the Supplier ID being transferred is the last of the Transferor’s Supplier IDs then the Party must also complete a BSCP 65 4.1 form or the relevant section of the Self-Service Gateway in order to de-register the Supplier role. | Supplier ID Transferor | CRA | Notification of a Supplier ID Transfer (BSCP 15/4.6 – Part A) or the relevant section of the Self-Service Gateway | Fax / Post / Email / Self-Service Gateway |
| 3.14.2 | At the same time as 3.14.1 | Submit Notification of Supplier ID Transfer | Supplier ID Transferee | CRA | Notification of a Supplier ID Transfer (BSCP 15/ 4.6 – Part B) or the relevant section of the Self-Service Gateway | Fax / Post / Email / Self-Service Gateway |
| 3.14.3 | On receipt of both 3.14.1 and 3.14.2 | Validate the documentation. | CRA |  | Ensure that the Transferee has Acceded and qualified in the role of Supplier.<br>Ensure that the Supplier IDs, Party Ids and dates specified on both the BSCP 15 /4.6 forms (A) and (B) or the relevant section of the Self-Service Gateway, match. | Internal Process |
| 3.14.4 | Within 1 WD of 3.14.3. | In the case that the validation checks are failed, inform both the Supplier ID Transferor and the Supplier ID Transferee of the rejection and the reason for the rejection. | CRA | Supplier ID Transferor<br>Supplier ID Transferee | Notification of Supplier ID Transfer rejection and reasons for the rejection. | Fax / Post / Email / Self-Service Gateway |
| 3.14.5 | At the same time as 3.14.3 | In the case that the validation checks are passed, identify the Primary BM Units (both Base and Additional, including any Exempt Export Primary BM Units) associated with the relevant Supplier ID. | CRA |  | Internal process. |  |
| 3.14.6 | Immediately following 3.14.5 | Notify the Transferee of the P/C Status of any Exempt Export Primary `BM Unit(s) associated with the relevant Supplier ID.41 | CRA | Supplier ID Transferee | Details of the P/C Status of any Exempt Export Primary BM Unit(s) associated with the relevant Supplier ID. | Fax / Email / Self-Service Gateway |
| 3.14.7 | Within 1 WD of 3.14.6 or as required to meet the Effective From date | Request that the NETSO identifies the Primary BM Units (both Base and Additional, including any Exempt Export Primary BM Units) associated with the relevant Supplier ID and transfers them from the Transferor to the Transferee. | CRA | NETSO | Copies of BSCP15 4.6 (A) and 4.6 (B) forms and authorisation to identify the associated Primary BM Units and transfer them from the Supplier ID Transferor to the Supplier ID Transferee. | Fax / Email |
| 3.14.8 | At the same time as 3.14.7 | Notify the Authority and each Party. | BSCCo | Authority | All Parties<br>ELEXON Circular42 | Fax / Post / Email |
| 3.14.9 | Within 1 WD of 3.14.7 or as required to meet the Effective From date | Transfer the Primary BM Units identified in 3.14.5 from the Transferor to the Transferee. | CRA | NETSO (where appropriate) | Internal Process | Internal Process |
| 3.14.10 | Within 1 WD of 3.14.7 | Inform the NETSO, BSCCo, BSC Agents and the Parties involved of the Transfer. | CRA | BSCCo<br>NETSO<br>SVAA<br>BSC Agents<br>Supplier ID Transferor<br>Supplier ID Transferee | Operations Registration Report to BSCCo & NETSO (CRA-I020)<br>BM Unit and GSP Group Registration Data to SVAA & BSC Agents (CRA-I015)<br>Registration Report to Parties (CRA-I014)<br>Electronic<br>Email to BSCCo<br>3.15 Process for Parties to Apply for Inclusion in BSC Website List of Suppliers which have Satisfied the Criteria to Complete a Change of Primary BM Unit Lead Party within 5 WDs for a Primary BM Unit with CVA Metering and Associated with a Customer Premises |  |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

| REF | WHEN | ACTION | FROM | TO | INPUT INFORMATION REQUIRED | METHOD |
|---|---|---|---|---|---|---|
| 3.15.1 | As determined by Party | Submit form BSCP15/4.10 Part A or complete the relevant section on the Self-Service Gateway | BSC Party | BSCCo | BSCP15/4.10 Part A Application or the relevant section of the Self-Service Gateway, for inclusion in BSC Website list of Suppliers which have satisfied the criteria to complete a change of Primary BM Unit Lead Party within 5 WD for a Primary BM Unit with CVA metering and associated with a Customer premises. | Post/Fax/Email / Self-Service Gateway |
| 3.15.2 | Within 1 WD of receipt of BSCP15/4.10 Part A or submission by Party the required information on the relevant section of the Self-Service Gateway | Request that the NETSO confirm whether or not the Party has appropriate registration on the NETSO’s systems and has use of a qualified Trading Agent and Trading Point in order to complete a change of Primary BM Unit Lead Party within 5 WD. | BSCCo | NETSO | Party ID and request for confirmation as to whether the Party is appropriately registered on the NETSO’s systems and has use of a qualified Trading Agent and Trading Point. | Fax/Email |
| 3.15.3 | At the same time as 3.15.2 | Check whether the Party has:<br>Acceded to the BSC and completed Party registration in the role of Supplier; and<br>Successfully completed registration and trading flows to register as a Supplier and completed metering flows to register CVA Primary BM Units. | BSCCo |  | Party ID | Internal Process |
| 3.15.4 | Within 2 WD of receipt of request in 3.15.2 | Confirm whether the Party is appropriately registered on the NETSO’s systems and has use of a qualified Trading Agent and Trading Point in order to complete a change of Primary BM Unit Lead Party within 5 WD. | NETSO | BSCCo | Confirmation whether the Party is appropriately registered on the NETSO’s systems and has use of a qualified Trading Agent and Trading Point. | Fax/Email |
| 3.15.5 | Within 2 WD of 3.15.4 | Send a completed BSCP15/4.10 Part B form or the online equivalent of the form to the Party to notify them of the outcome of their application. | BSCCo | Party | BSCP15/4.10 Part B, Application for inclusion in BSC Website list of Suppliers or the online equivalent of the form which have satisfied the criteria to complete a change of Primary BM Unit Lead Party within 5 WD for a Primary BM Unit with CVA metering and associated with a Customer premises. | Post/ Fax/ Email / Self-Service Gateway |
| 3.15.6 | At the same time as 3.15.5 | Where the Party has met the criteria checked by the NETSO in 3.14.2 and by BSCCo in 3.14.3, add the Party Name and ID to the BSC Website list of Suppliers which have satisfied the criteria to complete a change of Primary BM Unit Lead Party within 5 WD for a Primary BM Unit with CVA metering and associated with a Customer premises. | BSCCo |  | Party Name and ID. | Internal Process |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 3.16 Not Used

### 3.17 Not Used

### 3.18 Registration of Additional Primary BM Units for CFD Assets

| REF | WHEN | ACTION | FROM | TO | INPUT INFORMATION REQUIRED | MEDIUM |
|---|---|---|---|---|---|---|
| 3.18.1 | As required | Notify need for Additional Primary BM Unit registration | Supplier | BSCCo | BSCP15/4.1, Registration of Primary BM Unit or its online equivalent signed by an authorised person, registered as such using BSCP38 and including name, address and CFD ID provided by the generator with a CFD. BMU Id and BMU Name must follow naming convention on BSC website. | Email / Self-Service Gateway |
| 3.18.2 | Within 1 WD of 3.18.1 | Confirm registration is required for CFD | BSCCo | CFDSSP | As submitted in 3.18.1 | Email / Self-Service Gateway |
| 3.18.3 | Within 1 WD of 3.18.2 or as required | Instruct registration details | CFDSSP | BSCCo | Registration details, including CFD ID, GSP Group, and whether to register based on specific Supplier ID(s) or the list maintained in procedure 3.20 | Email / Self-Service Gateway |
| 3.18.4 | Within 1 WD of 3.18.3 | Acknowledge and validate request, including Effective From Dates of request and MDD timetable (Effective From Date must be on or after the MDD Go Live Date and registration request must be at least 15 WD19 prior to Effective From Date.) | BSCCo | CFDSSP | As submitted in 3.18.3 | Email / Self-Service Gateway |
| 3.18.5 | Following 3.18.4 | Initiate Market Domain Data process (BSCP509) | BSCCo |  | Form BSCP509/01 & relevant entity forms.<br>Internal Process<br>Initiate Registration of Primary BM Units based on registration details<br>BSCCo<br>CRA<br>BSCP15/4.1 or its online equivalent | Email / Self-Service Gateway |
| 13.18.6 | Within 1 WD of receipt of 3.18.5 | Acknowledge receipt of Registration request | CRA | BSCCo | As submitted in 3.18.5 |  |
| 3.18.7 | At the same time as 13.18.6 | Check that the Party is registered with the CRA and that the form or its online equivalent has been completed by an authorised person. Also check the registration data to confirm the FPN flag has been set correctly. | CRA |  | As submitted in 3.18.5 | Internal Process |
| 3.18.8 | As the same time as 3.18.6 | Where FPN flag is set to ‘Y’, inform the NETSO of the intended Primary BM Unit registration. | CRA | NETSO |  | Email |
| 3.18.9 | Within 5WD of 3.18.8 | The NETSO may object to the registration. | NETSO | CRA | A statement detailing the nature of the objection<br>Where an objection cannot be resolved, the CRA shall escalate the objection to BSCCo | Email |
| 3.18.10 | Following 3.18.9 | Allocate the Additional Primary BM Unit(s) to the Base Trading Unit for the relevant GSP Group (and set the Base Trading Unit Flag for each Primary BM Unit). | CRA |  | As submitted in 3.18.5<br>Creation of new Additional Primary BM Unit for a GSP Group | Internal Process |
| 3.18.11 | On receipt of data in 3.18.6 | CRA to receive and register the Working Day Credit Assessment Load Factor (WDCALF), Non-Working Day Credit Assessment Load Factor (NWDCALF), Supplier Export Credit Assessment Load Factor (SECALF), and Transmission Loss Factor (TLF) data for the Primary BM Unit and to ensure that this data is registered prior to the Effective From Date of the Primary BM Unit. | BSCCo | CRA | WDCALF, NWDCALF and SECALF data – Credit Assessment Load Factors (CRA-I011)<br>Transmission Loss Factors (CRA-I029) | Email / Self-Service Gateway |
| 3.18.12 | Following 3.18.11 | Confirm all steps in the Primary BM Unit registration process have been completed. | CRA | BSCCo | Completed BSCCo Checklist | Email / Self-Service Gateway |
| 3.18.13 | Within 1 WD of 3.18.5 but after 3.18.7 | Inform Party, BSCCo, NETSO and BSC Agents of the Primary BM Unit registration. | CRA | BSCCo<br>NETSO<br>SVAA<br>BSC Agents<br>Lead Party | CRA-I020.<br>BM Unit, Interconnector and GSP Group Data to SVAA (CRA-I015)<br>Registration Report (CRA-I014) to Parties.<br>Electronic<br>(Email to BSC Agents and BSCCo) |  |
| 3.18.14 | Following publication of final MDD circular43 | ‘Point of no return’. In order to ensure full data consistency across all BSC Agent and the NETSO systems a pending Additional Primary BM Unit registration cannot be withdrawn or amended beyond this point except by prior agreement with BSCCo |  |  |  |  |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 3.19 De-Registration of Additional Primary BM Units for CFD

| REF | WHEN | ACTION | FROM | TO | INPUT INFORMATION REQUIRED | MEDIUM |
|---|---|---|---|---|---|---|
| 3.19.1 | As required44 | Instruct de-registration details | CFDSSP | BSCCo | De-registration details, including CFD ID, GSP Group, and whether to deregister based on specific Supplier ID(s) or list maintained in 3.20 |  |
| 3.19.2 | Following 3.19.1 | Acknowledge and validate request, including Effective To Dates of request and MDD timetable (Effective To Date must be on or after the MDD Go Live Date and registration request must be at least 20 WD prior to Effective To Date.) | BSCCo | CFDSSP | As submitted in 3.19.1 |  |
| 3.19.3 | At least 20 WD prior to Effective To Date | Initiate Market Domain Data process (BSCP509) 45 | BSCCo |  | Based on list maintained under 3.20 and details provided in 3.19.1<br>Internal Process<br>Submit de-registration of Primary BM Unit form or its equivalent on the Self-Service Gateway<br>BSCCo<br>CRA<br>BSCP15/4.2, De-Registration of Primary BM Unit or its online equivalent | Email / Self-Service Gateway |
| 3.19.4 | Upon receipt of 3.19.3 | Check the form or its Self-Service Gateway equivalent for completeness and authorisation | CRA |  |  | Internal |
| 3.19.5 | Within 1 WD of 3.19.4 | Acknowledge de-registration request.<br>Where FPN set to ‘yes’, notify the NETSO46. | CRA | BSCCo<br>NETSO |  | Email / Self-Service Gateway |
| 3.19.6 | At the same time as 3.19.4 | Notify the SVAA of the Primary BM Unit.47 | CRA | SVAA48 |  | Email / Self-Service Gateway |
| 3.19.7 | At least 15 WD prior to Effective To Date | Confirmation of Effective To Date. | CRA | NETSO / Party | Confirmation of Effective To Date | Email / Self-Service Gateway |
| 3.19.8 | On or before Effective To Date | Update Systems and provide Party, BSCCo, NETSO and BSC Agents with registration reports. | CRA | Party | Registration reports of data entered onto Systems – Registration Report (CRA-I014),<br>Electronic<br>NETSO and BSCCo<br>Operations Registration Report (CRA – I020),<br>BSC Agents<br>BM Unit, Interconnector and GSP Group Data (CRA-I015). |  |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 3.20 Additional Primary BM Unit Sets for CFD

BSCCo is required by the Code to maintain a list of Active Power Purchasing Suppliers (Suppliers with HH Active Export greater than zero) within each GSP Group to support the registration and deregistration of Additional Primary BM Units for CFD purposes. Suppliers may opt-in and opt-out of this list. Any CFDSSP request supersedes any Supplier request or BSCCo list update. Any Supplier request supersedes any BSCCo list update. Suppliers can request the list from BSCCo via the BSC service desk.

| REF | WHEN | ACTION | FROM | TO | INPUT INFORMATION REQUIRED | MEDIUM |
|---|---|---|---|---|---|---|
| 3.20.1 | As required | Request inclusion/exclusion from list | Supplier / CFDSSP | BSCCo | Supplier ID, GSP Group and details of request | Email |
| 3.20.2 | Within 5 WD of 3.20.1 and before 3.20.3 | Validate and acknowledge request.<br>Where request from Supplier check for authorisation (as per BSCP38) | BSCCo |  | Supplier / CFDSSP<br>As submitted in 13. 20.1 | Email |
| 3.20.3 | Following 3.20.2 and at least quarterly | Update list | BSCCo |  | As submitted in 13.20.1 and based on those active Half Hourly Export Suppliers within each GSP Group | Internal Process |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 3.21 Registration of Secondary BM Units or Trading Secondary BM Units

| REF | WHEN | ACTION | FROM | TO | INPUT INFORMATION REQUIRED | MEDIUM |
|---|---|---|---|---|---|---|
| 3.21.1 | At least 15 WD prior to Effective From Date | Submit Registration of Secondary BM Unit or Trading Secondary BM Unit form | Virtual Lead Party | Asset Metering Virtual Lead Party<br>or<br>Virtual Trading Party<br>CRA | BSCP15/4.14, Registration of Secondary BM Unit or Trading Secondary BM Unit signed by an authorised person, registered as such using BSCP38.<br>Where a Party wishes for a Settlement Expected Volume (SEV) to replace the FPN they will indicate that the BM Unit is a Baselined BM Unit in form BSCP15/4.14.<br>Virtual Trading Parties must indicate that the Trading Secondary BM Unit is a Baselined BM Unit in form BSCP15/4.14. | Email/ Self-Service Gateway |
| 3.21.2 | Within 1 WD of receipt of 3.21.1 | Acknowledge receipt of Registration of Secondary BM Unit or Trading Secondary BM Unit form | CRA | Virtual Lead Party<br>Asset Metering Virtual Lead Party<br>or<br>Virtual Trading Party | As submitted in 3.21.1 | Email/Self-Service Gateway |
| 3.21.3 | At the same time as 3.21.2 | CRA checks the following:<br>That the Virtual Trading Party, Virtual Lead Party or Asset Metering Virtual Lead Party is registered with the CRA;<br>That the Effective From Date for the Secondary BM Unit or Trading Secondary BM Unit is on or after the Effective From Date for the Virtual Trading Party, Virtual Lead Party or Asset Metering Virtual Lead Party;<br>That a Virtual Trading Party Trading Secondary BM Unit is a Baselined BM Unit; and<br>That the form has been completed by an authorised person. | CRA |  | As submitted in 3.21.1 | Internal Process |
| 3.21.4 | At the same time as 3.21.2 | In all cases inform BSCCo of the Secondary BM or Trading Secondary BM Unit Unit Registration. | CRA | BSCCo |  | Email/Self-Service Gateway |
| 3.21.5 | On receipt of data in 3.21.4 | BSCCo to send data to CRA.<br>CRA to register the Transmission Loss Factor (TLF) data for the Secondary BM Unit or Trading Secondary BM Unit and ensure that this data is registered prior to the Effective From Date of the Secondary BM Unit or Trading Secondary BM Unit.<br>CRA to register the SCALF data for the Trading Secondary BM Unit and ensure that this data is registered prior to the Effective From Date of the Secondary BM Unit. | BSCCo | CRA<br>Transmission Loss Factors (CRA-I029) | SCALF data – Credit Assessment Load Factors (CRA-I011) | Email/Self-Service Gateway |
| 3.21.6 | On or before Effective From Date | Inform Virtual Trading Party, Virtual Lead Party or Asset Metering Virtual Lead Party, BSCCo, NETSO and BSC Agents of the Secondary BM Unit or Trading Secondary BM Unit registration. | CRA | Virtual Lead Party<br>Asset Metering Virtual Lead Party<br>Or Virtual Trading Party<br>BSCCo<br>NETSO<br>BSC Agents | CRA-I020.<br>BM Unit, Interconnector and GSP Group Data to SVAA (CRA-I015)<br>Registration Report (CRA-I014) to Parties. | Email/Self-Service Gateway |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 3.22 De-registration of a Secondary BM Unit or Trading Secondary BM Unit

| REF | WHEN | ACTION | FROM | TO | INPUT INFORMATION REQUIRED | MEDIUM |
|---|---|---|---|---|---|---|
| 3.22.1 | At least 20 WD prior to Effective To Date | Submit de-registration of Secondary BM Unit or Trading Secondary BM Unit form49.<br>Virtual Lead Party or | Asset Metering Virtual Lead Party | Or Virtual Trading Party<br>CRA | BSCP15/4.15, De-Registration of Secondary BM Unit or Trading Secondary BM Unit signed by an authorised person, registered as such using BSCP38. | Email/Self-Service Gateway |
| 3.22.2 | Upon receipt of 3.5.3 | Check the form for completeness and authorisation (as per BSCP38 Authorisations). | CRA |  |  | Internal |
| 3.22.3 | Within 1 WD of 3.5.4 | Acknowledge receipt of de-registration of Secondary BM Unit or Trading Secondary BM Unit form | CRA |  | Virtual Lead Party or<br>Asset Metering Virtual Lead Party<br>Or Virtual Trading Party | Email/Self-Service Gateway |
| 3.22.4 | At the same time as 3.5.5 | Notify NETSO and BSCCo of the Secondary BM Unit de-registration50.<br>Notify BSCCo only of the Trading Secondary BM Unit de-registration | CRA | NETSO<br>BSCCo<br>BSCCo |  | Email/Self-Service Gateway |
| 3.22.5 | At least 15 WD prior to Effective To Date | Confirmation of Effective To Date. | CRA |  | NETSO / LDSO<br>Virtual Lead Party<br>or<br>Asset Metering Virtual Lead<br>Party<br>or<br>Virtual Trading Party<br>Confirmation of Effective To Date | Email/Self-Service Gateway |
| 3.22.6 | On or before Effective To Date | Update systems and provide Party, BSCCo, NETSO and BSC Agents with registration reports. | CRA | Virtual Lead Party<br>or<br>Asset Metering Virtual Lead Party<br>or<br>Virtual Trading Party<br>NETSO and BSCCo<br>BSC Agents | Registration reports of data entered onto systems – Registration Report (CRA-I014),<br>Operations Registration Report (CRA – I020),<br>BM Unit, Interconnector and GSP Group Data (CRA-I015). | Email/Self-Service Gateway |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

3.23 Change of Production / Consumption Status for a Secondary BM Unit other than a Trading Secondary BM Unit by the Virtual Lead Party or Asset Metering Virtual Lead Party

This process supports a Virtual Lead Party or Asset Metering Virtual Lead Party’s ability under K8.1to change the previously-elected P/C Status for a Secondary BM Unit other than a Trading Secondary BM Unit, by enabling the Virtual Lead Party or Asset Metering Virtual Lead Party to change the Secondary BM Unit’s P/C Flag setting from Production to Consumption or vice versa. This process does not apply to a Trading Secondary BM Unit, which has separate Production and Consumption accounts, rather than a single Virtual Balancing Account.

Parties needing to elect the P/C Status of a Secondary BM Unit for the first time should refer to procedure 3.21 for details of how to set the Secondary BM Unit’s P/C Flag.

| REF | WHEN | ACTION | FROM | TO | INPUT INFORMATION REQUIRED | MEDIUM |
|---|---|---|---|---|---|---|
| 3.23.1 | From time to time if the Virtual Lead Party | or<br>Asset Metering Virtual Lead Party requires<br>Submit notice to the CRA, copied to BSCCo, requesting a change to the Production / Consumption Flag for a Secondary BM Unit.<br>The request should contain an effective date for such amendment of at least 2 WD from this notice unless otherwise agreed with the CRA/BSCCo.<br>Virtual Lead Party or Asset Metering Virtual Lead Party | CRA | BSCCo | Form BSCP15/4.8 Election of Production / Consumption Flag for Exempt Export Primary BM Unit or Secondary BM Unit, Storage BM Unit | Email/Self-Service Gateway |
| 3.23.2 | As soon as practicable after 3.23.1. | Amend the P/C Flag for the Secondary BM Unit, effective from the specified date (or 2 WD from 3.23.1, if the specified date is less than 2 WD and no reduced timescale has been agreed).<br>Notify the Virtual Lead Party<br>or Asset Metering Virtual Lead Party of the change to P/C Flag. | CRA | Virtual Lead Party<br>or<br>Asset Metering Virtual Lead Party<br>Registration Report | CRA – I014 | Email/Self-Service Gateway |
| 3.23.3 | At the same time as 3.23.2 | Notify BSCCo and BSC Agents of the change to P/C Flag. | CRA | BSCCo<br>BSC Agents | CRA – I020 to BSCCo<br>CRA – I015 to BSC Agents | Email/Self-Service Gateway |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

### 3.24 Reconfiguration of BM Unit Associated with Metering Systems Registered with the CRA

| REF | WHEN | ACTION | FROM | TO | INPUT INFORMATION REQUIRED | MEDIUM |
|---|---|---|---|---|---|---|
| 3.24.1 | At least 30 WD prior to Effective From Date of the reconfiguration | Submit Registration of BM Unit form and an electrical single line diagram(s) showing the location of the Metering Equipment, in particular the Settlement current and voltage transformers (CTs/VTs) and CT/VT ratios, and all existing Boundary Points and any System Connection Points at or near the proposed Boundary Point(s).51 52 | Party | CRA | BSCP15/4.1, Registration of BM Unit signed by an authorised person, registered as such using BSCP38. | Fax / Post / Email |
| 3.24.2 | Within 1 WD of receipt of 3.24.1 | Acknowledge receipt of Registration of BM Unit form | CRA | Party |  | Fax / Email / Post |
| 3.24.3 | At the same time as 3.24.2 | The CRA checks the following:<br>The Party is registered with the CRA<br>The form has been completed by an authorised person.<br>The Effective From Date for the BM Unit is on or after the Effective From Date for the Party. | CRA |  | As submitted in 3.24.1 | Internal Process |
| 3.24.4 | At the same time as 3.24.2 | Inform CDCA, NETSO and BSCCo of the intended BM Unit registration. | CRA | CDCA<br>NETSO<br>BSCCo |  | Fax / Email |
| 3.24.5 | Within 5 WD of 3.24.4 | Where the Party is applying to register 2 or more Offshore Power Park Modules as a Combined Offshore BM Unit, the NETSO shall confirm whether it determines that such a configuration is suitable to constitute a single BM Unit. | NETSO | CRA<br>BSCCo | A statement as to whether the NETSO determines that the Party’s requested configuration of Offshore Power Park Modules is suitable to constitute a single BM Unit | Fax / Email / Post |
| 3.24.6 | Within 5 WD of 3.24.4 and (if applicable) at the same time as 3.22.5 | The NETSO may object to the registration. | NETSO | CRA | A statement detailing the nature of the objection<br>Where an objection cannot be resolved, the CRA shall escalate the objection to BSCCo | Fax / Email / Post |
| 3.24.7 | 15 WD prior to the Effective From Date and if required | BSCCo to send data to CRA.<br>CRA to register the Working Day Credit Assessment Load Factor (WDCALF), Non-Working Day Credit Assessment Load Factor (NWDCALF) and Supplier Export Credit Assessment Load Factor (SECALF) data for the BM Unit and ensure that this data is registered prior to the Effective From Date of the BM Unit. | BSCCo | CRA | WDCALF, NWDCALF and SECALF data – Credit Assessment Load Factors (CRA-I011)<br>Transmission Loss Factors (CRA-I029) | Email |
| 3.24.8 | 5 WD prior to Effective From Date | CDCA to confirm the following:<br>The Aggregation Rules have been updated consistently with the reconfiguration (if required).<br>The Meter Technical Details have been updated consistently with the reconfiguration (if required).<br>Whether a Metering System proving test associated with the BM Unit has been completed successfully (if required).<br>The Aggregation Rules of any other VAUs have been updated, if required where another BM Unit is connected at the same CVA Boundary Point and the reconfiguration of the BM Unit affects the Aggregation Rules of the other VAUs. | CDCA | CRA | Metering System proving test results, Meter Aggregation Rules | Email / Fax / Electronic |
| 3.24.9 | If applicable on or before Effective From Date | Provide Party and BSC Agents with registration reports53. | CRA | Party<br>NETSO and BSCCo<br>BSC Agents | Registration reports of data entered onto Systems including Effective From Date – Registration Report (CRA-I014),<br>Operations Registration Report<br>(CRA – I020),<br>BM Unit, Interconnector and GSP Group Data (CRA-I015). | Electronic |

*[Table rebuilt from a flattened web copy-paste. Cell boundaries were inferred from the column order and party names, so check FROM/TO/INFORMATION splits against the original wherever a finding depends on them. Footnote numbers may be glued to words, e.g. "BSCCo33".]*

## 4. Appendices

### 4.1 BSCP15/4.1 Registration of Primary BM Unit for a CVA Metering System54

To: CRA

Date Sent:

From: Participant Details

Party ID:

Name of Sender:

Contact email address:

Our Ref:

Contact Tel. No.

Name of Authorised Signatory:

Authorised Signature:

Password:

Is this Primary BM Unit registration:

[ ]

a New Primary BM Unit Registration

[ ]

a re-configuration of existing plant and apparatus

[ ]

a Change of registration data associated with a Change of Primary BM Unit Lead Party

[ ]

subject to a Registration Transfer in accordance with BSCP68

[ ]

a change in status of a Primary BM Unit’s FPN Flag

[ ]

Baselined BM Unit Indicator (delete as applicable)55

[ ]

a change in the Switching Group to which the BM Unit belongs

[ ]

an Additional Primary BM Unit registration for CFD Assets

[ ]

an Additional Primary BM Unit registration under instruction of the CFDSSP (only BSCCo should tick this box)

(Tick as appropriate)

BSCP15/4.1 Registration of Primary BM Unit (cont)

Primary BM Unit Id

Primary BM Unit Name(Max 30 Characters)

NGC BM Unit ID56

BM Unit Type57

Primary BM Unit Configuration58

GSP Group Id 59

GC (MW)

DC (MW)

Interconnector Primary BM Unit or Storage BM Unit P/ C Flag 60

FPN Flag (Y/N)

Exempt Export (optional)61

Inter-connector Id 62

Baselined BM Unit Y/N 63

EFD

Note: If BSCCo are registering one or more Additional Primary BM Units under instruction from the CFDSSP, spreadsheets or other suitable formats may be used to detail the registration details. Additional Primary BM Units for CFD Assets must be of Primary BM Unit Type ‘S’ and follow the naming convention for the Primary BM Unit ID and Primary BM Unit Name on the BSC Website

For Embedded and Directly Connected Primary BM Units, tick to confirm that an electrical single line diagram(s) are attached to the application showing:

• the location of the Metering Equipment, in particular the Settlement current and voltage transformers (CTs/VTs) and CT/VT ratios64, and

• any existing Boundary Points and/ or System Connection Points at or near the proposed Boundary Point(s); and

• any back up SVA connection and interlocking arrangements.

Tick to confirm if Storage BM Unit

BSCP15/4.1 Registration of Primary BM Unit (cont)

If BM Unit Configuration is ‘Meets criteria in K3.1.2 (MC)’ confirm the following BM Unit Id………………………………………..

(repeat this table for each BM Unit Id in the MC configuration)

Select

Additional Details

One Party is responsible for the BM Unit;

Yes/No

The Plant and Apparatus in the BM Unit is capable of being controlled independently of any Plant and Apparatus not in the BM Unit

Yes/No

The Metered data for the BM Unit can be submitted to the SAA separately from any Metered Data for any Plant and Apparatus which is not in the BM Unit;

Yes/No

The BM Unit does not comprise Plant and Apparatus whose Imports and Exports are measured by both CVA Metering System(s) and SVA Metering System(s);

Yes/No

If yes provide SVA MSID(s)

…………………………………………………………….

There are no smaller aggregations of the Plant and Apparatus comprised in the BM Unit, for which (a), (b) and (c) would be satisfied

Yes/No

If yes provide details of the number and size of individual Plant and /or Apparatus and confirm that the total size is less than or equal to a Small Power Station for the appropriate region.

…………………………………………………………….

Fuel Type (Directly Connected or Embedded Primary BM Units) – for use in calculation of CALF values

Tick

Biofuel

CCGT

CVA Consumption

Hydro

OCGT

Pumped Storage

Rail Demand

Station Load

Onshore Wind

Offshore Wind

Other (please specify):

BSCP15/4.1 Registration of Primary BM Unit (cont)

Primary BM Unit and Associated CVA Metering Systems

Primary BM Unit

Associated CVA Metering Systems

MPAN Mapping Details (Exemptable Embedded Sites registering Export in CVA and Import in SVA)

MPAN

Effective From Date

Effective To Date

BM Unit Group Details (Supplier BM Units containing SVA Metering System(s) which are part of a Teleswitch Group(s) which include SVA Metering Systems in a different Supplier’s BM Unit)

Teleswitch Group ID

Effective From Date

Effective To Date

Switching Groups65 (list BM Unit Ids for each Switching Group below) Only applicable to a combination of Power Park Modules which belong to a Switching Group.

(Example: Switching Group 1 – T_ABMU-1 and T_BBMU-1)

### 4.2 BSCP15/4.2 De-Registration of Primary BM Unit Page 1 of 1

To: CRA

Date Sent:

From: Participant Details

Party ID:

Name of Sender:

Contact email address:

Our Ref:

Contact Tel. No:

Name of Authorised Signatory:

Authorised Signature:

Password:

Is this Primary BM Unit de-registration:

[ ]

an Interconnector Primary BM Unit

[ ]

a re-configuration of existing plant and apparatus into another Primary BM Unit

[ ]

a disconnection of circuits from the Transmission System or Distribution System (NOTE: if this box is ticked the appropriate Certification of Disconnection must be provided).

[ ]

subject to a Registration Transfer in accordance with BSCP68

[ ]

An Additional Primary BM Unit deregistration for CFD

(Tick as appropriate)

De-Registration Primary BM Unit Data Requirements66

Name:

Primary BM Unit Id:

NGC BM Unit ID:

Effective To Date:

The NGC BM Unit ID must be provided for all Primary BM Units with the FPN Flag set to ‘Y’.

Base Primary BM Units cannot be De-Registered utilising this form.

4.3 BSCP15/4.3 Registration of Seasonal Estimates of the Maximum Positive and Negative Primary BM Unit Metered Volume and Maximum Positive and Maximum Negative Deviation Volumes for Trading Secondary BM Units

Page 1 of 1

To: CRA

Date Sent:

From: Participant Details

Party ID:

Name of Sender:

Contact email address:

Our Ref:

Contact Tel. No.

Name of Authorised Signatory:

Authorised Signature:

Password:

BSC Season

Tick One

Spring

[ ]

1st March to 31st May

Summer

[ ]

1st June to 31st August

Autumn

[ ]

1st September to 30th November

Winter

[ ]

1st December to 28th / 29th February

CRA Use Only

Primary BM Unit Id or Trading Secondary BM Unit Id

Maximum (+ve) QMij or Derivation Volume MWh (for use in calculating GC)

Maximum (-ve) QMij or Derivation Volume MWh (for use in calculating DC)

Generation Capacity MW (+ve)

Demand Capacity MW (-ve)

Note: For the avoidance of doubt, the values of GC/DC will be the positive/negative value of QMij divided by the SPD respectively (as described in Section K of the BSC).

4.4 BSCP15/4.4 Mid-Season Changes of Positive and Negative Primary BM Unit Metered Volume Estimates and Maximum Positive and Maximum Negative Deviation Volumes for Trading Secondary BM Units

Page 1 of 2

To: CRA

Date Sent:

From: Participant Details

Party ID:

Name of Sender:

Contact email address:

Our Ref:

Contact Tel. No.

Name of Authorised Signatory:

Authorised Signature:

Password:

Effective From Date:

CRA Use Only Page 2 of 2

Primary or /Trading Secondary BM Unit Id

Revised Maximum (+ve) QMij or Deviation Volume MWh (for use in calculating GC)

Revised Minimum

(-ve) QMij or Deviation Volume MWh (for use in calculating DC)

Revised Generation Capacity MW (+ve)

Revised Demand Capacity MW (-ve)

Note: For the avoidance of doubt, the values of GC/DC will be the maximum/minimum value of QMij divided by SPD respectively (as described in Section K of the BSC). For Trading Secondary BM Units, QMij relates to Deviation Volume.

### 4.5 BSCP15/4.5 Application for Exemptable Generating Plant Status

Part A Page 1 of 2

To: BSCCo

Date Sent:

From: Participant Details

Party ID:

Name of Sender:

Contact email address:

Our Ref:

Contact Tel. No.

Name of Authorised Signatory:

Authorised Signature:

Password:

Details of the Primary BM Unit(s) comprising the Generating Plant for which Exemptable status is being sought:67

Primary BM Unit ID

Generation Capacity (GC) MW

Demand Capacity (DC) MW

Metering System ID

Exempt Export status required by (date)

Chosen P/C Flag68

Please explain why you believe the Generating Plant is Exemptable.

You may wish to refer to the relevant Statutory Instrument:

Does the Party making this application hold a generation licence? Yes/No (Delete as applicable)

BSCP15/4.5 Application for Exemptable Generating Plant Status

Page 2 of 2

Part B

To:

Date Sent:

From: BSCCo

Name of Sender:

Contact email address:

Our Ref:

Contact Tel. No.

Name of Authorised Signatory:

Authorised Signature:

Password:

Confirmation of figures provided above:

Primary BM Unit ID

Declared Net Capacity (DNC) MW

Total Output to System MW

Exempt Export Primary BM Unit status Effective From (date)

Chosen P/C Flag

Validity of Primary BM Unit Registration(s) Checked: Yes/No (Delete as applicable)

Comments:

BSCCo, not being in a legal position of endorsing what is a legal responsibility of an operator, can see no reason why the Primary BM Unit(s) listed by the applicant should not be treated as comprising Exemptable Generating Plant from the information available.

If BSC Party registration or Primary BM Unit registration is outstanding this declaration remains provisional until the registration process is completed.

OR:

BSCCo can see the following reasons why the above Primary BM Unit(s) should not be treated as comprising Exemptable Generating Plant.

Reasons:

### 4.6 BSCP15/4.6 Notification of a Supplier ID Transfer

Part A (to be completed by the Supplier ID Transferor69) Page 1 of 2

To: BSCCo

Date Sent:

From: Participant Details (Transferor)

Party ID:

Name of Sender:

Contact email address:

Our Ref:

Contact Tel. No.

Contact Fax. No.

Name of Authorised Signatory:

Authorised Signature:

Password:

Please take this as notification that:

Supplier ID(s) ____________________ (4 alpha characters per ID)

Will be transferred from Party Id: ____________________

To Party Id: ____________________

With an Effective From Date of: ____________________

In signing the Party acknowledges that any SVA Metering Systems and Primary BM Units associated with the stated Supplier ID will also be transferred on the stated date.

BSCP15/4.6 Notification of a Supplier ID Transfer

Part B (to be completed by the Supplier ID Transferee70) Page 2 of 2

To: BSCCo

Date Sent:

From: Participant Details (Transferee)

Party ID:

Name of Sender:

Contact email address:

Our Ref:

Contact Tel. No.

Contact Fax. No.

Name of Authorised Signatory:

Authorised Signature:

Password:

Please take this as notification that:

Supplier ID(s) ____________________ (4 alpha characters per ID)

Will be transferred from Party Id: ____________________

To Party Id: ____________________

With an Effective From Date of: ____________________

In signing the Party acknowledges that any SVA Metering Systems and Primary BM Units associated with the stated Supplier ID will also be transferred on the stated date.

### 4.7 BSCP15/4.7 Commencement / Termination of Exempt Export Primary BM Unit Status

To:

CRA

Date Sent:

From: BSCCo

Participant and Primary BM Unit Details

Party Id:

Primary BM Unit ID:

Commencement of Exempt Export Primary BM Unit Status:

YES / NO

P/C Flag to apply:71

Effective From Settlement Date (for Exempt Export Flag and P/C Flag):

Termination of Exempt Export Primary BM Unit Status:

YES / NO

Effective To Settlement Date (for Exempt Export Flag and P/C Flag):

Name of Authorised Signatory:

Authorised Signature:

Password:

Contact email address:

BSCCo Ref:

Contact Tel. No.

### 4.8 BSCP15/4.8 Election of Production / Consumption Flag for Exempt Export Primary BM Unit, Storage BM Unit or Secondary BM Unit

To: CRA

BSCCo

Date Sent:

From: Participant Details

Party ID72:

Name of Sender:

Contact email address:

Our Ref:

Contact Tel. No.

Name of Authorised Signatory:

Authorised Signature:

Password:

BM Unit ID:

Storage BM Unit:

P / C Flag:

_____________________

YES / NO (delete as applicable)

PRODUCTION / CONSUMPTION73 (delete as applicable)

Effective From Settlement Date:

Note that the Production / Consumption Flag as elected here will be deemed effective until/unless the Lead Party makes a new election (by following procedure 3.12 or 3.23 as appropriate) or, in the case of Exempt Export Primary BM Units, the Primary BM Unit’s Exempt Export status is terminated in accordance with procedure 3.11.

From: CRA74

To: Lead Party

Date Sent:

Reason(s) for Rejection:

### 4.9 BSCP15/4.9 Certification of Exemptable Status for Generating Plant With Exports Measured by SVA Metering Systems

Part A Page 1 of 2

To:

BSCCo

Certification of Exemptable Status for Generating Plant With Exports Measured by SVA Metering Systems

Date Sent:

Primary BM Unit ID:

From: Company Details

Party Id:

Name of Sender:

Contact email address:

Our Ref:

Contact Tel. No.

I, the Director of the Party responsible for and requesting Exemptable Generating Plant status for__________________________75, and thereby Exempt Export Primary BM Unit status for ____________________76, (‘the Party’) hereby certify that from 77:

The Generating Plant is Exemptable as defined in Section K1.2.2 of the Code and the Primary BM Unit would, if the Metering Systems comprised in that Primary BM Unit(s) were CVA registered, satisfy the following criteria in accordance with Section K3.3A of the Code:

Only one Party (the Party hereby requesting Exempt Export status) is responsible for Exports and / or Imports from Plant / Apparatus comprised in the Primary BM Unit;

The Exports and/or Imports from and to the Plant / Apparatus are capable of being controlled independently of the Exports and/or Imports from or to any Plant / Apparatus not comprised in the Primary BM Unit;

Exports and/or Imports can be determined separately for Plant / Apparatus comprised in the Primary BM Unit;

OR, the Panel, in accordance with Section K3.1.6, has determined that the Primary BM Unit in question has best satisfied these requirements.

I hereby provide notification in accordance with Section K3.5 that the Party elects the P/C Flag of the Primary BM Unit to be _______ 78 should the Primary BM Unit be granted Exempt Export status.

The Party will take all reasonable steps, in accordance with Section U1.2.3, to ensure that the data and information held or maintained by BSCCo, any BSC Agent, or any SMRA relating to the Party, with specific reference to this application, is and continues to be accurate and complete.

BSCCo can rely on this certification as to the matters set out herein, for the purposes of verification of Exemptable Generating Plant status (and associated Exempt Export Primary BM Unit status), i.e. the matters set out above in (1) to (4).

The Party undertakes to comply with any request to re-certify made by BSCCo in accordance with Section K 1.5.8.

Name of Director:

Signature of Director:

On behalf of:

BSCP15/4.9 Certification of Exemptable Status for Generating Plant With Exports Measured by SVA Metering Systems

Part B Page 2 of 2

To:

BSC Party

Confirmation of Exemptable Status for Generating Plant With Exports Measured by SVA Metering Systems

Date Sent:

Generating Plant Name:

Primary BM Unit ID:

Party Id:

Name of Sender:

Contact email address:

Our Ref:

Contact Tel. No.

From: BSCCo

BSCCo hereby confirms that the above Generating Plant has / has not* been granted Exemptable status and that the above Primary BM Unit therefore has / has not* been granted Exempt Export status.

BSCCo hereby also confirms that, where (and only where) Exempt Export status has been granted, the P/C Flag elected for the Primary BM Unit in Part A of this form BSCP15/4.9 shall become effective concurrently with the Primary BM Unit’s Exempt Export status.

* Delete as applicable

4.10 BSCP15/4.10 Application for Inclusion in BSC Website List of Suppliers which have Satisfied the Criteria to Complete a Change of Primary BM Unit Lead Party within 5 WD for a Primary BM Unit with CVA Metering and Associated with a Customer Premises

Part A Page 1 of 2

To: BSCCo

Date Sent:

From: Participant Details

Party ID:

Name of Sender:

Contact email address:

Our Ref:

Contact Tel. No.

Name of Authorised Signatory (Category A in BSCP38):

Authorised Signature:

Password:

I confirm that the Party above has met the following criteria and is therefore applying to be included in the BSC Website list of Suppliers which have satisfied the criteria to complete a change of Primary BM Unit Lead Party within 5 WD for a Primary BM Unit with CVA metering and associated with a Customer premises:

The Party has acceded to the BSC and completed Party registration in the role of Supplier;

The Party has appropriate registration on the NETSO Systems, and use of a qualified Trading Agent and Trading Point.

By returning this form, I acknowledge that the above Party undertakes to provide written notice by a Category A authorised signatory to BSCCo within 1 WD of any change in its ability to meet these criteria. I confirm that the above Party also recognises that such a change will result in the Party being removed from this list.

I acknowledge that the above Party recognises that, in order to qualify for a change of Primary BM Unit Lead Party within 5 WD, the following criteria (unique to the specific registration) must also be satisfied:

The Primary BM Unit is not associated with a Trading Unit except a Sole Trading Unit; and

The de-registration form (BSCP15/4.2) and registration form (BSCP15/4.3) submitted by the outgoing and incoming Suppliers contain consecutive Effective To and From Dates (in order to demonstrate that both Suppliers are aware of, and agree with, the change of Lead Party).

BSCP15/4.10 Application for Inclusion in BSC Website List of Suppliers which have Satisfied the Criteria to Complete a Change of Primary BM Unit Lead Party within 5 WD for a Primary BM Unit with CVA Metering and Associated with a Customer Premises

Part B Page 2 of 2

To: Party

Date Sent:

From: BSCCo

Party ID:

Name of Sender:

Contact email address:

Our Ref:

Contact Tel. No.

Name of Authorised Signatory (Category A in BSCP38):

Authorised Signature:

Password:

BSCCo hereby confirms that the above Party has/has not* met the necessary criteria to be included in the BSC Website list of Suppliers which have satisfied the criteria to complete a change of Primary BM Unit Lead Party within 5WDs for a Primary BM Unit with CVA metering and associated with a Customer premises.

* Delete as applicable

Parties are reminded of their agreement to notify BSCCo within 1 WD if, at any time, their ability to meet any of the criteria changes. Parties are also reminded that such a change will result in the Party being removed from the list.

### 4.11 BSCP15/4.11 Change of CVA Primary BM Unit Lead Party (CoPBLP)

Part A (to be completed by the Party de-registering the Primary BM Unit(s)) Page 1 of 2

To: CRA

Date Sent:

From: Participant Details

Party ID:

Name of Sender:

Contact email address:

Our Ref:

Contact Tel. No.

Contact Fax. No.

Name of Authorised Signatory:

Authorised Signature:

Password:

Primary BM Unit Id:

NGC Primary BM Unit ID

(if known)

Associated MSIDs (please enter all MSIDs associated with Primary BM Unit)

Associated Approved Metering Dispensations (if applicable, please provide MSID(s) and Metering Dispensation Reference Number(s))

Current P/C Flag (for Exempt Export Primary BM Units and/ or Storage BM Units)79

Trading Unit Name (if applicable):

Please take this as notification that the registrations detailed above will be transferred with an Effective To Date of80: ___________________

BSCP15/4.11 Change of CVA Primary BM Unit Lead Party (CoPBLP)

Part B (to be completed by the Party registering the Primary BM Unit(s)) Page 2 of 2

To: CRA

Date Sent:

From: Participant Details

Party ID:

Name of Sender:

Contact email address:

Our Ref:

Contact Tel. No.

Contact Fax. No.

Name of Authorised Signatory:

Authorised Signature:

Password:

Primary BM Unit Id:

NGC Primary BM Unit ID

(if known)

Associated MSIDs (please enter all MSIDs associated with Primary BM Unit(s))81

Associated Approved Metering Dispensations (if applicable, please provide relevant MSID(s) and Metering Dispensation Reference Number(s))

Chosen P/C Flag (for Exempt Export Primary BM Units and/ or Storage BM Units)82

Trading Unit Name: (if applicable)

Please take this as notification that the registrations detailed above will be transferred with an Effective From Date of83: ___________________

### 4.12 Not Used

### 4.13 BSCP15/4.13 Application for Non-Standard Primary BM Unit

To: BSCCo

Date Sent:

From: Participant Details

Party ID:

Name of Sender:

Contact email address:

Our Ref:

Contact Tel. No.

Contact Fax. No.

Name of Authorised Signatory

Authorised Signature:

Password:

Confidentiality

This form with contact and Authorised Signatory details removed, associated diagrams and BSC Panel documents will routinely be made available in the public domain unless the applicant informs BSCCo otherwise at the time of application

Request for Confidentiality YES/NO* *Delete as applicable

If ‘YES’, what is confidential?

Confidential84?

Yes/No (if only part then indicate which part)

Application form

Diagrams

BSC Panel Documents

Justification for requesting confidentiality:

Site Details

Primary BM Unit Id(s) (if known):

Primary BM Unit Name(s) (Max 30 Characters):

NGC BM Unit Id(s) (if known and applicable):

Application:

Why are you applying for a Non-Standard Primary BM Unit (please tick)

The Plant and Apparatus does not fall into one of the standard categories in K3.1.4

The Plant and Apparatus does fall into one of the standard categories in K3.1.4 but a different configuration satisfies the requirements for Primary BM Units in K3.1.2

The Plant and Apparatus Exports or Imports are at a CVA Boundary Point at which there are other Exports or Imports for which another person is responsible (the Plant and Apparatus may or may not be of a Standard Primary BM Unit configuration)

Description of Non-Standard Primary BM Unit configuration

Please contact BSCCo for guidance on how to complete this section

Please provide electrical single line diagram(s) of the Plant and Apparatus included in the Non-Standard (and any Standard) Primary BM Unit(s) to support your application. The diagrams need to clearly show the location of the Metering Equipment, in particular the Settlement Current and Voltage Transformers (CTs/VTs) and CT/VT ratios, all existing Boundary Points and any System Connection Points at or near the proposed Boundary Point(s) and which items of Plant and Apparatus comprise which Non-Standard (and any Standard) Primary BM Unit(s).

List of electrical single line diagrams attached and description of Plant and Apparatus covered by each diagram.

Rationale

Rationale with reference to BSC Section K3.1 for the request for the Non-Standard Primary BM Unit:

Please contact BSCCo for guidance on how to complete this section

### 4.14 BSCP15/4.14 Registration of Secondary BM Unit or Trading Secondary BM Unit

To: CRA

Date Sent:

From: Participant Details

Party ID85:

Name of Sender:

Contact email address:

Our Ref:

Contact Tel. No.

Name of Authorised Signatory:

Authorised Signature:

Password:

Is this Secondary BM Unit registration:

[ ]

a New Secondary BM Unit Registration

[ ]

a New Trading Secondary BM Unit Registration

[ ]

a change in status of a Secondary BM Unit’s FPN Flag

[ ]

Baselined BM Unit Indicator86

(Tick as appropriate)

Secondary BM Unit Id or Trading Secondary BM Unit Id

Secondary BM Unit Name or Trading Secondary BM Unit Id (Max 30 Characters)

NGC BM Unit ID87

GSP Group Id

P/C Flag87

FPN Flag (Y/N)

Baselined BM Unit86 (Y/N)

EFD

### 4.15 BSCP15/4.15 De-Registration of Secondary BM Unit or Trading Secondary BM Unit

To: CRA

Date Sent:

From: Participant Details

Party ID:

Name of Sender:

Contact email address:

Our Ref:

Contact Tel. No:

Name of Authorised Signatory:

Authorised Signature:

Password:

De-Registration of Secondary BM Unit or Trading Secondary BM Unit Data Requirements

Name:

Secondary BM Unit Id or Trading Secondary BM Unit Id:

NGC BM Unit ID:

Effective To Date:

The NGC BM Unit ID must be provided for all Secondary BM Units with the FPN Flag set to ‘Y’

.

AMENDMENT RECORD – BSCP15

| Version | Details (in source column order: Date / Description of Changes / Changes Included / Mods/ Panel/ Committee Refs) |
|---|---|
| 1.0 | Code Effective Date<br>Designated version<br>n/a<br>n/a |
| 2.0 | 30/11/00<br>Work outstanding at Go Active, resolution of inconsistencies, inclusion of consultation comments.<br>223, 243<br>08/009 |
| 3.0 | 13/08/02<br>Change Proposals for BSC Systems Release 2<br>CP521, 528, 567, 568, 546, 726, 782<br>ISG 16/166, ISG 18/193<br>SVG 19/233 |
| 4.0 | 24/06/03<br>Change Proposals for CVA Programme June 03 Release<br>CP 749, 761, 821, P106 |
| 5.0 | 01/08/03<br>Approved Modification P62<br>P62<br>P62 48/003 |
| 6.0 | 12/09/03<br>Approved Modification P82 and P100 for CVA Programme Nov 03 Release<br>P82<br>P100<br>P82 54/006, P100 57/007 |
| 7.0 | 27/02/04<br>Approved Modification P123 for CVA Programme Feb 04 Release<br>P123<br>P123 66/006 |
| 8.0 | 15/03/04<br>Change Proposal CP1027<br>CP1027<br>ISG37/414 |
| 9.0 | 30/06/04<br>CVA Programme June 04 Release.<br>CP971<br>CP944<br>CP1030<br>P82 Removal<br>ISG40/003<br>SVG40/004 |
| 10.0 | 23/02/05<br>CVA Programme Feb 05 Release<br>BETTA 6.3; CP1015, P159, CP1040, CP1091 |
| 11.0 | 02/11/05<br>CVA Programme Nov 05 Release.<br>CP1108<br>P192<br>ISG52/003<br>P96/004 |
| 12.0 | 28/06/06<br>June 06 Release<br>P190<br>CP1154<br>ISG64/001<br>SVG64/002 |
| 13.0 | 28/02/08<br>February 08 Release<br>CP1201<br>CP1231<br>ISG81/01<br>SVG81/01<br>ISG84/01<br>SVG84/02 |
| 14.0 | 06/11/08<br>November 08 Release<br>CP1239<br>ISG88/01<br>SVG88/02 |
| 15.0 | 20/04/09<br>P216 Release<br>P216<br>ISG97/02<br>SVG97/08 |
| 16.0 | 25/06/09<br>June 09 Release<br>P215<br>23/04/2008<br>(OFGEM) |
| 17.0 | 20/11/09<br>P237<br>P237<br>Panel 160/04 |
| 18.0 | 27/01/10<br>Modification P240<br>P240<br>Panel |
| 19.0 | 04/11/10<br>November 10 Release<br>CP1330<br>ISG112/01<br>SVG112/03 |
| 20.0 | 23/02/12<br>February 2012 Release<br>P268<br>Panel 186/04<br>P269<br>Panel 186/05 |
| 21.0 | 26/06/14<br>June 2014 Release<br>CP1403<br>ISG154/01<br>SVG157/05 |
| 22.0 | 01/08/14<br>Electricity Market Reform<br>ORD005<br>Directed by the Secretary of State |
| 23.0 | 25/06/15<br>June 2015 Release<br>P310<br>ISG169/05<br>SVG172/02 |
| 24.0 | 23/02/17<br>February 2017 Release<br>P326 Self-Governance<br>SVG190/02<br>ISG188/05 |
| 25.0 | 29/06/17<br>June 2017 Release<br>P350<br>ISG194/02<br>SVG196/03 |
| 26.0 | 22/02/18<br>February 2018 Release<br>CP1493<br>ISG200/10<br>SVG202/02 |
| 27.0 | 28/02/19<br>February 2019 Release<br>P344<br>Panel 284C/01 |
| 27.0 | 28/02/19<br>February 2019 Release<br>CP1510<br>ISG211/06<br>SVG214/02 |
| 27.0 | 28/02/19<br>February 2019 Release<br>P359<br>ISG212/03<br>SVG215/03 |
| 28.0 | 29/03/19<br>March 2019 Standalone Release<br>P369<br>Panel 285/12 |
| 29.0 | 27/0/19<br>June 2019 Release<br>P364<br>Panel 288/08 |
| 30.0 | 07/11/19<br>November 2019 Release<br>P386 Self-Governance<br>Panel 291/05 |
| 30.0 | 07/11/19<br>November 2019 Release<br>P389 Self-Governance<br>Panel 294/04 |
| 31.0 | 27/02/20<br>February 2020 Release<br>P394 Self Governance<br>Panel 297/07 |
| 32.0 | 30/06/22<br>30 June 2022 Release<br>P375<br>Panel 309/06 |
| 33.0 | 23/02/2023<br>23 February 2023 Release<br>P376<br>P314/06 |
| 34.0 | 01/10/24<br>01 October 2024 Non-Standard Release<br>ORD009<br>Directed by Secretary of State |
| 35.0 | 07/11/24<br>07 November 2024 Release<br>P415<br>Panel 339/03 |
| 36.0 | 10/12/24<br>10 December 2024 Non-Standard Release<br>P475<br>Panel 353/07 |
| 37.0 | 02/05/25<br>02 May Non-Standard Release<br>P484<br>Panel 361/06 |

*[Amendment record rebuilt from a flattened copy-paste; each row's cells are listed in source column order.]*

Intellectual Property Rights, Copyright and Disclaimer

The copyright and other intellectual property rights in this document are vested in Elexon or appear with the consent of the copyright owner. These materials are made available for you for the purposes of your participation in the electricity industry. If you have an interest in the electricity industry, you may view, download, copy, distribute, modify, transmit, publish, sell or create derivative works (in whatever format) from this document or in other cases use for personal academic or other non-commercial purposes. All copyright and other proprietary notices contained in the document must be retained on any copy you make.

All other rights of the copyright owner not expressly dealt with above are reserved.

No representation, warranty or guarantee is made that the information in this document is accurate or complete. While care is taken in the collection and provision of this information, Elexon Limited shall not be liable for any errors, omissions, misstatements or mistakes in any information or damages resulting from the use of this information or action taken in reliance on it.

1 Per section K3.1.4B, Power Park Modules may belong to a Switching Group on the basis that Plant and Apparatus can be selected to run in any of the BM Units belonging to that Switching Group. A ‘Switching Group’ is described in Section K3.1.4A of BSC.

2 A VTP does not need to submit a FPN to the NETSO in respect of a Trading Secondary BM Unit.

3 Must be authorised by a Category A authorised signatory

4 Not required for Change of CVA Primary BM Unit Lead Party unless any changes are to be made to existing registration data.

5 If the CT / VT ratios are not known 30WD / 60WD prior to the EFD, this information should be sent separately by 16WD prior to the EFD.

6 If a Primary BM Unit registration is requested using Electronic File Data Transfer, the passwords and signatures are not required as the access control to the participant system is sufficient authentication.

7 Where the Party is applying to register two or more Offshore Power Park Modules as a Combined Offshore BM Unit, BSCCo recommends that the Party consults with the NETSO before submitting this form.

8 This information is required to help ensure the energy flow(s) for the proposed Boundary Point(s) are accounted for, where necessary (e.g. under an existing Metering Dispensation for difference Metering), in the Aggregation Rules of any associated Volume Allocation Units (e.g. Interconnectors, other relevant BM Units, Grid Supply Points, GSP Groups or Distribution System Connection Points).

9 Suppliers that have Customers directly connected to the Transmission System can register and de-register the BM Unit associated with that Customer premises within 5WD if the criteria in Section 1.7 have been satisfied.

10 Where the Primary BM Unit has the FPN flag set to Yes the NETSO must be contacted at least 30 WD prior to EFD.

11 Metering Systems are registered in accordance with BSCP20

12 If the CT / VT ratios are not known 30WD / 60WD prior to the EFD, this information should be sent separately by 16WD prior to the EFD.

13 If a BM Unit registration is requested using Electronic File Data Transfer, the passwords and signatures are not required as the access control to the participant system is sufficient authentication.

14 Where the Party is applying to register 2 or more Offshore Power Park Modules as a Combined Offshore BM Unit, BSCCo recommends that the Party consults with the NETSO before submitting this form.

15 This information is required to help ensure the energy flow(s) for the proposed Boundary Point(s) are accounted for, where necessary (e.g. under an existing Metering Dispensation for difference Metering), in the Aggregation Rules of any associated Volume Allocation Units (e.g. Interconnectors, other relevant BM Units, Grid Supply Points, GSP Groups or Distribution System Connection Points).

16 The TLM for an Interconnector BM Unit will be set to 1, irrespective of the value of the TLF

17 If the Primary Base BM Unit is an Exempt Export Primary BM Unit, the Lead Party can change the Primary BM Unit’s allocated Trading Unit by providing notification in accordance with BSCP31.

18 Note that, with the exception of any Exempt Export Primary BM Units in Base Trading Units which have explicitly elected to have a P/C Status of Production, all Primary BM Units in Base Trading Units will always have a P/C Status of Consumption in accordance with Section K3.5.

19 The EFD must align with MDD Release Schedule and be agreed between the NETSO, CRA, Party and BSCCo as applicable

20 If an Additional Primary BM Unit is requested using Electronic File Data Transfer, the passwords and signatures are not required as the access control to the participant system is sufficient authentication. Where faxes are used, participants are required to submit hard copies of the forms by post in case the faxed signatures are illegible.

21 If the Additional Primary BM Unit is an Exempt Export Primary BM Unit, the Lead Party can change the Primary BM Unit’s allocated Trading Unit by providing notification in accordance with BSCP31. If no notification is provided by the Lead Party, the Primary BM Unit will be allocated to the Base Trading Unit for its GSP Group.

22 Note that, with the exception of any Exempt Export BM Units in Base Trading Units which have explicitly elected to have a P/C Status of Production, all BM Units in Base Trading Units will always have a P/C Status of Consumption in accordance with Section K3.5.

23 Primary BM Unit registration timescales may be reduced in certain circumstances if the registering Party agrees that the registration will not be withdrawn or amended after the ‘point of no return’.

24 If the Primary BM Unit is an Embedded BM Unit, Party requests from LDSO. If the Primary BM Unit is a Directly Connected Primary BM Unit, Party requests from NETSO.

25 Any relevant Metering Systems should be de-registered in accordance with BSCP20

26 If a Primary BM Unit De-registration is requested using Electronic File Data Transfer, the passwords and signatures are not required as the access control to the participant system is sufficient authentication. Where faxes are used, participants are required to submit hard copies of the forms by post in case the faxed signatures are illegible.

27 Party to initiate BSCP509 before the de-registration form is submitted to the CRA

28 Where the Primary BM Unit has a FPN set to No, the NETSO does not need to be informed of the De-Registration

29 The Supplier needs to ensure all Metering Systems associated with the additional Supplier Primary BM Unit are re-allocated to either the Base Primary BM Unit or another Supplier BM Unit associated with the same GSP Group (BSCP503 & 507) unless circuits are being disconnected.

30 Notification of such Primary BM Units shall be sent to the SVAA in its capacity as the Market Domain Data manager

31 Please refer to the ‘Generation Capacity (GC) and Demand Capacity (DC) Estimation Methodology and Challenge Guidance’ document for guidance on this process.

32 If the GC or DC Breach has not been processed in time to be included in the CRA registration reports, then the Effective From Date for the CRA-estimated GC or DC value shall be set to the Working Day after next.

33 BSC Parties may elect to raise a GC or DC Estimation Challenge through the Self-Service Gateway, in which case both CRA and BSCCo will be notified, or they can email BSCCo, who will raise the GC or DC Estimation Challenge on their behalf.

34 If the CRA has two or more conflicting updates to Primary BM Unit Registration data or Trading Secondary BM Unit data with the same Effective From Date, it shall prioritise the updates in accordance with Section K3.4.7N and with Section K3.4.7O.

35 If the changes to the GC or DC Values has not been processed in time to be included in the CRA registration reports, then the Effective From Date shall be set to the Working Day after next.

36 The Lead Party can change an Exempt Export Primary BM Unit’s allocated Trading Unit by providing notification in accordance with BSCP31.

37 Once Exempt Export status is terminated, the Primary BM Unit’s P/C Status will no longer be fixed by the Lead Party and will be determined in accordance with Section K3.5.2.

38 The Lead Party can choose to register the Primary BM Unit in a different Trading Unit by following BSCP31.

39 Please note that the responsibility for providing accurate registration data on BSCP15/4.11 forms or in the relevant section of the Self-Service Gateway lies with the Lead Party and not BSCCo.

40 Where a CoPBLP involves multiple Primary BM Units affecting multiple Trading Units, a separate form should be used for each Trading Unit.

41 Because of the short timescales in which a Transfer of Supplier ID can occur, the Exempt Export Primary BM Unit’s P/C Status will remain unchanged on transfer to the Supplier ID Transferee unless the Supplier ID Transferee notifies the CRA/BSCCo to the contrary by following procedure 3.12.

42 The ELEXON Circular is only issued in the event of a Supplier of Last Resort (SoLR).

43 Primary BM Unit registration timescales may be reduced in certain circumstances if the registering Party agrees that the registration will not be withdrawn or amended after the ‘point of no return’

44 Typically this will be when the CFD comes to an end and the Additional Primary BM Unit is no longer required for CFD. Suppliers should ensure any MPANs are re-allocated to another appropriate Primary BM Unit. Any Metering Systems not re-allocated will be assigned to the relevant Supplier’s Base Primary BM Unit by SVAA.

45 BSCCo to initiate BSCP509 before the de-registration form is submitted to the CRA

46 Where the Primary BM Unit has a FPN set to No, the NETSO does not need to be informed of the De-Registration

47 The Supplier needs to ensure all Metering Systems associated with the additional Supplier Primary BM Unit are re-allocated to either the Base Primary BM Unit or another Supplier Primary BM Unit associated with the same GSP Group (BSCP503 & 507) unless circuits are being disconnected.

48 Notification of such Primary BM Units shall be sent to the SVAA in its capacity as the Market Domain Data manager

49 If a Secondary BM Unit or Trading Secondary BM Unit De-registration is requested using Electronic File Data Transfer, the passwords and signatures are not required as the access control to the participant system is sufficient authentication. Where faxes are used, participants are required to submit hard copies of the forms by post in case the faxed signatures are illegible.

50 Where the Secondary BM Unit has a FPN set to No, the NETSO does not need to be informed of the De-Registration

51 If a BM Unit registration is requested using Electronic File Data Transfer, the passwords and signatures are not required as the access control to the participant system is sufficient authentication.

52 This information is required to help ensure the energy flow(s) for the proposed Boundary Point(s) are accounted for, where necessary (e.g. under an existing Metering Dispensation for difference Metering), in the Aggregation Rules of any associated Volume Allocation Units (e.g. Interconnectors, other relevant BM Units, Grid Supply Points, GSP Groups or Distribution System Connection Points).

53 These reports would be sent if the CRA system had to be updated to reflect that change. They would not be sent if the only change was to the fuel type or the configuration of the BM Units as these parameters are not entered into the CRA system.

54 In the case of Base Primary BM Units this form should be used to complete the Base Primary BM Unit Registrations by providing, for example, the initial GC/DC values and if appropriate the FPN Flag.

55 Baselined BM Unit Indicator for Additional BM Unit Registrations only.

56 The NGC BM Unit ID must be provided for all Primary BM Units with the FPN Flag set to ‘Y’.

57 E – Embedded, I – Interconnector, G – Base Supplier S – Additional Supplier, T – Directly Connected

58 CCGT – CCGT registered in CMRS, PPM – a single Power Park Module registered in CMRS, COBMU – a Combined Offshore BM Unit comprising 2 or more Offshore Power Park Modules registered in CMRS, DC – Directly Connected Circuit at Customer (Supplied by BSC Party) Premises, DC+ – Directly Connected Circuit at Customer (Supplied by BSC Party) Premises through more than one Boundary Point, IC – Interconnector Primary Unit, BB – Primary Base BM Unit, AB – Additional Primary BM Unit, OPPM+ - Offshore PPM plus related Imports at separate Boundary Points, COBMU+ - COBMU plus related Imports at separate Boundary Points, MC – Meets criteria in BSC K3.1.2, NS – Non-Standard.

59 If unit type E or S

60 Applicable for Interconnector Primary BM Units, which are registered in fixed Production/Consumption pairs whose P/C Status does not change (Section K3.5/K5.5) , and Storage BM Units (where the Lead Party is able to choose the BM Unit’s P/C Flag). A Party applying for Exempt Export status must follow procedure 3.10 to elect the Exempt Export Primary BM Unit’s P/C Flag.

61 To apply for Exempt Export status for a new BM Unit registration, enter “Yes” and follow procedure 3.10 of this BSCP.

62 If BM Unit Type is I

63 For BM Unit Type is S Only

64 If the CT/VT ratios are not known 30WD / 60WD prior to the EFD, this information should be sent separately by 16WD prior to the EFD. If you are applying for Exempt Export status for an existing BM Unit, you do not need to complete form 4.1 but must follow procedure 3.10.

65 Note that this still applies where Switching Aggregation Rules are not required.

66 Where CFD Additional Primary BM Units are being de-registered, the de-registration details may be provided using spreadsheets or other suitable formats

67 If your application for Exemptable Generating Plant status is successful, the Primary BM Unit(s) comprising the Exemptable Generating Plant will be granted Exempt Export status. Please refer to procedure 3.10 for further details.

68 Please enter the P/C Flag (either “P” for Production or “C” for Consumption) that you as the Lead Party elect to apply to the Primary BM Unit from the date that the Primary BM Unit’s Exempt Export status (if granted) becomes effective. Failure to complete this box will result in rejection of this form and a delay to your application. Please refer to procedure 3.10 for further details.

69 The Trading Party that is transferring the Supplier ID(s)

70 The Trading Party that will become responsible for the Supplier ID(s)

71 Must be either “P” (Production) or “C” (Consumption); otherwise the CRA shall reject this form.

72

73 Please refer to procedure 3.12 or 3.23 for further details.

74 Used for Exempt Export Primary BM Units if the request to change the P/C flag is rejected.

75 Add name of Generating Plant here.

76 Add Primary BM Unit Id here.

77 Add Exemptable Status Effective From date here

78 Please enter either “P” (Production) or “C” (Consumption). Failure to complete this election will result in rejection of this form and a delay to your application. Please refer to procedure 3.10 for further details.

79 Must be either "P” (Production) or “C” (Consumption).

80 The ‘Effective To Date’ specified on this form should be the day before the ‘Effective From Date’ for the associated registration(s) specified on the BSCP15/4.11 Part B form.

81 Please note, if the Party de-registering the Primary BM Unit is not the current Registrant of the MSID, permission should be sought from the current Registrant, in accordance with BSCP20, to ensure they have no objections to the transfer.

82 Please enter the P/C Flag (either “P” for Production or “C” for Consumption) that you elect to apply to the Exempt Export Primary BM Unit and / or Storage BM Unit from the Effective From Date of the CoPBLP. Failure to complete this box will result in rejection of this form and a delay to the transfer. Please refer to procedure 3.13 for further details.

83 The ‘Effective From Date’ specified on this form should be the next consecutive day after the associated ‘Effective To Date’ for the deregistration(s) specified on the BSCP15/4.11 Part A form.

84 BSCCo will publish all Panel determinations, though for confidential papers the details will be anonymised. BSCCo is required to keep a list of all Non-Standard BM Unit determinations which must be made available to any Party upon request.

85 Only Virtual Lead Parties, Asset Metering Virtual Lead Parties may register Secondary BM Units and only Virtual Trading Parties may register Trading Secondary BM Units

86 The Baselined BM Unit Indicator to must be set to Y’ for a Trading Secondary BM Unit.

87 The NGC BM Unit ID is not required for a Trading Secondary BM Unit which is only operating in the Wholesale Market.