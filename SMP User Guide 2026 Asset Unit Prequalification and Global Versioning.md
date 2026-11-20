# SMP (Single Market Platform) User Guide – August 2026 – Asset & Unit Management, Alignment, Prequalification, ABSVD Allocation and Global Versioning (extract)

> **Source file:** `SMP 2026.txt` (NESO SMP user guide, slide-style PDF, copy-pasted; each page was headed "August 2026 / Public", now removed)  
> **Coverage:** Extract only. Chapter 4 (Asset & Unit Management), Chapter 6 (Units), 7.1 (Interconnector User, truncated), Chapter 8 (Asset Alignment), Chapter 9 (Prequalification, truncated), Chapter 10 (ABSVD Delivery Allocation, start missing) and Chapter 11 (Global Versioning). Chapter 5 is not included.  
> **Screenshots:** The guide is mostly screenshots, which a copy-paste does not capture. Lines that were image captions are shown in *italics* where they could be identified. "Figure below/overleaf" refers to a missing image.  
> **Converted:** 2026-10-07. Wording kept verbatim from the source copy-paste; only layout artefacts (page headers/footers, line wraps, broken tables) were cleaned up. Notes in *[italic square brackets]* are editorial.

---

## 4. Asset & Unit Management

### 4.1. Navigating the Landing Page for Unit & Asset Management.

- The Unit Management Page is made up of several components as follows:

- Unit Management Tab: Click on this to always land back on this page.
  - Units & Asset Sub Tabs: Click on these to switch between the collection of Units and collection of Assets.
  - Trading Agent (EDT) Sub Tab
  - Control Point (EDL) Sub Tab

- Search bar: Enter text into the search bar to help you find a specific Unit/Asset. This will narrow down the tiles that are displayed, so that tiles are only displayed if the search text matches the start of the Unit/Asset name.

- Create New Unit: Click on this to register a new unit*

- Align assets to Units: Click on this to undertake the alignment of assets to Units*

*Subsequent sections in this guide will cover each of these features in depth.

### 4.2. Navigating the Landing Page for Unit & Asset Management.

Asset & Unit Management Home Page Screen

### 4.3. Creating & Managing Assets

### 4.4. Create an asset.

- To register a new asset, the first step is to click on the ‘Create new asset’ where a user will be presented with the screen illustrated in Figure 22.0 ‘New Asset registration’ where a unique asset name will be required. Please note that, firstly, an asset cannot be created without an asset name, and secondly, the name must be unique in naming convention to the asset in question. Once the asset name is provided, the user will be able to progress to the next step by clicking Create.

Creating Assets- Asset Registration

### 4.5. Create an asset.

### 4.6. Asset Registration: Submitting Asset Information

- The user is navigated to the Asset Registration Page as outlined in Figure overleaf, the format is similar to the Account Management Page structure with an accordion section on the left-hand side for direct navigation to a specific section or the user can select the subsection they wish to complete.

- The figure illustrates the unique named asset for which the details are being registered; ‘Roe dean Windfarm’.

- Please note that the user is not able to progress the registration process for a created asset without completing all the sections and corresponding fields. The icon next to each subsection heading on the left-hand side will reflect the state the subsection is in.

- A circular green icon with a tick indicates that the all the mandatory fields in the subsection have been completed.

A triangular amber icon with an exclamation mark indicates that some but not all of the mandatory fields in the subsection have been completed.

- A circular blue icon with a number indicates that none of the mandatory fields have been completed yet.

### 4.7. Create an asset.

Figure below shows the Asset Registration Detail Page where Subsection 1 has been completed, Subsection 2 is in progress while Subsections 3 & 4 are yet to be started.

Asset Registration Detail Page

### 4.8. Asset Registration: Asset Details Section

- Figure below illustrates the Detail Section for the Asset.

- Please note that as the Asset Ownership, Asset Type, the Effective from Date and Fuel Type are all mandatory and therefore marked with a red asterisk. It is essential that these fields have information submitted.

- Please consult the Glossary Appendix for a translation of the Fields if the User is not clear about what is being requested.

Completing the ‘Asset Details’ Section

### 4.9. Asset Registration: Asset Connection Details Section

- Figure below illustrates the Asset Connection Details Section for the Asset.

- Please note that as the Generation Capacity, Demand Capacity, the Connection Type , Connection Point Voltage <=415V and Meter Refresh fields are all mandatory and therefore marked with a red asterisk. It is essential that these fields have information submitted. If Connection Point Voltage <=415V? is equal to ‘Yes’ then Connection Point Voltage will be set as 0.415. If it is equal to ‘No’ then Meter Refresh will be set as ‘1s Refresh Rate’.

Completing the ‘Asset Connection Details’ Section

### 4.10. Asset Registration: Asset Site Location

- Figure below illustrates the Site Location Section for the Asset.

- Please note that the Asset Latitude, Asset Longitude, the Nearest Node, Grid Supply Point, GSP Group ID, GSP Group ID (location picklist), Primary Dispatch phone number & Secondary dispatch phone number are all mandatory and therefore marked with a red asterisk. It is essential that these fields have information submitted.

- The Grid Supply Point (GSP) field is multiple choice, so a user can select several values as indicated in the figure below.

- Please ensure that the following fields meet the requirements:

- The Asset Latitude field requires a value between -90 and 90.

- The Asset Longitude field requires a value between -180 and 180.

- The phone number and fax fields require a value with 10 digits.

- The Agent/Applicant Operational Email field requires the value to be in a valid email format.

### 4.11. Asset Registration: Asset Site Location

Completing the ‘Asset Site Location Details’ Section

### 4.12. Asset Registration: Asset MPAN Details

- Figure below illustrates the MPAN Details Section for the Asset.

- Please note that the Operational Metering Availability is mandatory and therefore marked in a red asterisk.

- The user must enter a value into either MPAN Import OR MPAN Export fields, and give MPAN Effective From and To Dates for the value(s).

- The user must also indicate whether or not they give consent for those values to be shared by SVAA with the Supplier as detailed by the BSC by selecting ‘True’ or ‘False’ in the MPAN Import/Export Consent fields, and then give Start and End Dates for that Consent.

- The user has the option to add another MPAN Pair by clicking on ‘Add New MPAN Pair’. Clicking on this bring up another set of fields for the user to enter the details and consent details for another pair of MPANs

- The user must tick the ‘I consent to the verification of the above MPAN details with Elexon’ box for the Save Asset button to be enabled.

### 4.13. Asset Registered: Asset Tile

Following on from the Asset Registration, the asset tile will appear on the Unit Management Home Page under the ‘Asset Tab’. Each asset will have a corresponding tab. The tile displays the ‘key or summary information’. To view the full registration details, click on the three dots on the right-hand corner of the tile. The user then selects the ‘View Asset Details’ link to be re-directed to the Asset Detail page expanded version.

Please note that Users will be expected to submit all asset information at once. Upon ‘saving the asset’ registration details, the Asset Status will appear as ‘Accepted’ automatically as illustrated in Figure below

*Asset Tiles*

### 4.14. Asset Map View

As of Release 4.7 a map view of all Assets where the user is an Owner or Agent is available. To access, navigate to the ‘Assets on a Map’ tab on the Unit Management page.

The Map view allows the user to filter by the following categories. All are multi-select allowing the user to choose more than one value if they wish:

- BMU Id – the BMU/Non-BMU Id of the Unit the Assets are aligned to
- GSP Group Id – the GSP Group entered by the User when registering the Unit the assets are aligned to
- Unit Category – the category i.e. Primary/Secondary Additional Supplier BMU or NonBMU of the unit the assets are aligned to
- Unit Status – whether the Unit aligned to the Assets has been Accepted, Submitted or Deregistered
- Fuel Type – the Fuel Type of the Unit the Assets are aligned to
- Include Unaligned Assets checkbox – this will include assets that are not aligned to units, regardless of the selections in the above filters

Press ‘Reset Filters’ to clear all filter values.

Press ‘Load Map’ to render the asset locations as red circles on the map. These are based on the Longitude and Latitude entered by the user when registering the assets.

---

*[Chapter 5 is not in the source, and the Chapter 6 heading was not captured.]*

## 6. *[Unit Management; chapter title not captured]*

### 6.1. Create a Unit

- To register a new Unit, the first step is to click on the ‘Create new unit’ where a user will be presented with the screen illustrated in Figure below ‘New Unit registration’ where a unique Unit name will be required. Please note that, firstly, a Unit cannot be created without a Unit name and secondly, the name must be unique in naming convention to the Unit in question. Once the Unit name is provided, the user will be able to progress to the next step by clicking Create.

Create Unit

### 6.2. Unit Registration: Overview Page

- The user is navigated to the Unit Registration Page as outlined in Figure below, the format is similar to the Asset Registration Page structure with an accordion section on the left-hand side for direct navigation to a specific section or the user can select the subsection they wish to complete.

- The figure illustrates the unique named Unit for which the details are being registered; ‘Sussex Coast Renewables’

- Please note that the user is not able to progress the registration process for a created Unit without completing all the sections and corresponding fields. When any of the following is selected as the Unit Category:

- Primary BMU

- Secondary BMU

- Additional Supplier BMU

The user will be prompted to enter additional Balancing Mechanism specific information. Additional fields will be added to the existing sections and four new sections will be added to the form for the user to complete, namely:

- Control Point (EDL)

- Trading Agent (EDT)

- OFTO

- eGAMA

*Unit Registration Detail Page*

### 6.3. Classification of Unit Category Concept

As of Release 2.7, the user must select a Category for their unit. If Demand Flexibility Service is selected as the Applicable Market, ‘Non-BMU’ will be automatically selected as the Category. If the Category is not known, the user can click ‘Find Unit Category’ to be guided through a wizard that will help them determine their category.

Upon selecting ‘Find Unit Category, the user is asked if they are registering a BMU or Non-BMU unit.

Selecting ‘Non-BMU’ will lead to a recommendation of non-BMU as a category. Pressing ‘Select’ on this screen will automatically populate the value of the Category field. Selecting ‘BMU’ will lead to the user being asked if they know their National Energy System Operator If ‘Yes’ is selected, the next screen will advise the user to cancel the wizard to get their Unit ID and then select the category of their unit on the registration screen.

If ‘No’ is selected, the user is asked if they know their Elexon BMU ID Prefix for this Unit.

Selecting ‘No’ will lead to a screen advising the user to contact the Market Entry team at Elexon.

Selecting ‘Yes’ will prompt the user to select the Elexon BMU ID Prefix they have.
- 2_ will identify the unit as Additional Supplier BMU
- V_ will identify it as ‘Secondary BMU
- T_,E_,I_,C_,M_ will identify it as ‘Primary BMU’

### 6.4. Submitting Unit Information: Unit Details Section

- Figure below illustrates the Detail Section for the Unit where the Category is Non-BMU

- Please note that the Unit Type, the Effective from Date and Fuel Type are all mandatory and therefore marked with a red asterisk. It is essential that these fields have information submitted.

Completing the ‘Unit Details’ Section – Non-BMU

Completing the ‘Unit Details’ Section – BMU

- Figure below illustrates the Detail Section for the Unit where the Category is Primary BMU, Secondary BMU or Additional Supplier BMU

- Please note that the Unit Type, the Effective from Date, Fuel Type, Application Contact Email and Application Contact Number are all mandatory and therefore marked with a red asterisk. It is essential that these fields have information submitted. Elexon Organisation ID, BSC Signatory and Party EIC Code (Type X) are pre-filled and cannot be edited by the user.

### 6.5. Submitting Unit Information: Unit Connection Section

- Figure below illustrates the Unit Connection Details Section for the Unit where Category = Non-BMU

- Please note that the Generation Capacity, Demand Capacity, Connection Type and DNO Type (picklist field) are all mandatory and therefore marked with a red asterisk. It is essential that these fields have information submitted.

*Completing the ‘Unit Connection Details’ Section – Non BMU*

- Figure below illustrates the Unit Connection Details Section for the Unit where Category = Primary BMU, Secondary BMU or Additional Supplier BMU

- Please note that the Generation Capacity, Demand Capacity, Connection Type ,DNO Type, FPN Flag, Control Telephony Number and System Telephony Number are all mandatory and therefore marked with a red asterisk. It is essential that these fields have information submitted.

Completing the ‘Unit Connection Details’ Section – BMU

### 6.6. Submitting Unit Information: Unit Site Location Section

- Figure below illustrates the Unit Site Location Section for the Unit

- Please note that the Grid Supply Point, GSP Group ID, GSP Group ID (location picklist), Primary Dispatch phone number & Secondary dispatch phone number are all mandatory and therefore marked with a red asterisk. It is essential that these fields have information submitted.

- The Grid Supply Point (GSP) field is multiple choice, so a user can select several values as indicated in the figure below.

Completing the ‘Unit Site Location Details’ Section

### 6.7. Linking a Control Point (EDL) to a Unit

The user will have the option to either link an existing Control Point (where the Status is Submitted or Accepted) or create a new Control Point record to proceed with the registration. To link an existing Control Point, populate the Control Point ID field. The user can find IDs of Control Points linked to their account on the Control Point (EDL) tab of the Unit Management page. If the Control Point is not owned by the user’s account they will need to obtain it from the NESO BM Registration team.

Upon input of the Control Point ID, the name of the associated Control Point record will appear. Click on the name to populate the field.

If there is no existing Control Point record to link to, the user can select ‘Create new Control Point (EDL)’. Input a name and press ‘Create’ to be taken to the New Control Point (EDL) Registration overlay (this will not exit the registration page for the Unit) When all mandatory information has been added, press ‘Save EDL’ The Control Point ID and Control Point Name fields will then be populated with the details of the record. The Control Point record will automatically created with a status of Submitted, meaning the user will not be able to edit any details of it in SMP.

### 6.8. Linking a Trading Agent (EDT) to a Unit

In the same manner as the linking of a Control Point, the user will have the option to either link an existing Trading Agent (where the Status is Submitted or Accepted) or create a new Trading Agent record to proceed with the registration. To link an existing Trading Agent, populate the Trading Agent ID field. The user can find IDs of Trading Agents linked to their account on the Trading Agent (EDT) tab of the Unit Management page.

Upon input of the Trading Agent ID, the name of the associated Trading Agent record will appear. Click on the name to populate the field.

If there is no existing Trading Agent record to link to, the user can select ‘Create new Trading Agent (EDT)’. Input a name and press ‘Create’ to be taken to the New Trading Agent (EDT) Registration overlay (this will not exit the registration page for the Unit) When all mandatory information has been added, press ‘Save EDT Agent’ The Trading Agent ID and Trading Agent Name fields will then be populated with the details of the record. The Control Point record will automatically created with a status of Submitted, meaning the user will not be able to edit any details of it in SMP.

### 6.9. Submitting Unit Information: OFTO and eGAMA Sections

- Figure below illustrates the OFTO Section for the Unit where Category = Primary BMU, Secondary BMU or Additional Supplier BMU.

- Figure below illustrates the eGAMA Section for the Unit where Category = Primary BMU, Secondary BMU or Additional Supplier BMU.

### 6.10. Submitting Unit Information: Confirmation of Submission.

- Once all the sections are completed correctly, then the ‘Save Unit’ button will appear in a blue background, enabling the user to complete the registration process for creating the Unit.

- If the User wishes to repeat the exercise and create subsequent Units, they can select the ‘save and create new one’ button instead.

- Please note for Balancing Mechanism Units registration is not considered to be complete until the Unit Service has been submitted too – see Chapter 8 for details.

Confirmation of Unit Saved Successfully.

### 6.11. Submitting Unit Registration for Approval

Once the finalised alignment of Asset(s) to Unit has been completed, to signify the submission of the Unit Registration has been undertaken, the Portal User will have to select the ‘Submit for Registration’ option on the drop down menu as indicated on the picture below.

Once this option is selected, the Unit is considered for appraisal by the Registrations Team at the National Energy System Operator . Please note that Units in Submitted State are considered different then Draft, where the assumption is that alignment or Asset(s) has not taken place or not finalised.

### 6.12. Submitting Unit Registration for Approval

### 6.13. Modifications to Registration of Units

- Following on from the Unit Registration, the asset tile will appear on the Unit Management Home Page under the ‘Units’ Tab. Each asset will have a corresponding tab. The tile displays the ‘key or summary information’. To view the full registration details, click on the three dots on the right-hand corner of the tile. The user then selects the ‘View Unit Details’ link to be re-directed to the Unit Detail page expanded version.

- Users have the ability to retrospectively edit Unit Registration Details before final submission. Upon ‘saving the Unit’ registration details, the Unit Status will appear as ‘Draft’ automatically as illustrated in Figure 35.0

- To make edits, the user should click on ‘Edit Unit Details’ link to be redirected to the Unit Detail page expanded version. They then have the ability to edit the sections or specific fields desired. The Unit Status will appear as ‘Submitted’ once the Unit is finally submitted for consideration.

- Once the Unit is submitted for approval, the National Energy System Operator Registration Team will a) assign the Unit a Unit ID (which will auto populate on the Unit Id field) b) set the Unit Status field from ‘submitted’ to ‘approved’ or ‘rejected’.

### 6.14. Modifications to Registration of Units: cont

*Unit Tiles*

*Modifications to Registration of Units: cont.*

*Edit Unit Details & View Expanded Unit Details Page for Editing*

*Modifications to Registration of Units: cont.*

Then select ‘Edit Unit Information’.

### 6.15. Deregistration of Units

- Portal User can initiate the de-registration of a Unit only on the condition it is in ‘Accepted’ Status. A Unit that warrants De-Registration is defined as a Unit that ceases to continue operating.

- To start the process, click the icon containing three dots on a tile of an accepted unit and then click ‘Deregister Unit’, as illustrated in Figure overleaf

- A pop-up window (shown in Figure below) will appear, which informs the user that an email will be sent to the National Energy System Operator Registration Team, who will complete the process offline. Click ‘Continue’ to proceed with the deregistration of the unit.

- Another pop-up window (shown in Figure overleaf) will appear, asking the user to select an ‘Effective to’ date. This date needs to be in the future and cannot be less than the ‘Effective from’ date of the Unit’s original version. After clicking ‘Submit’, a green confirmation banner will appear at the top of the screen.

- The Approval Request will be directed towards the National Energy System Operator Registration Team who will either decide to Approve or Reject the Unit De-registration request.

- If the Decision is to approve the request, then the Unit will no longer appear on the Unit Management screen and the user will also receive an email to confirm that the Unit has been deregistered (See Figure overleaf).

If however the Registration Team Reject the deregistration request, then the user will receive an email to let them know the request was rejected. Once the ‘Effective to’ date has passed, the unit will no longer be visible on the Unit Management page.

### 6.16. Process for Deregistering Units

Deregister a Unit

Pop-up Window for Deregistering a Unit

### 6.17. Process for Deregistering Units - cont

Figure 35.4: Pop-up Message for ‘Effective To’ Date

### 6.18. Process for Deregistering Units -cont

Figure 35.4: Deregistration Request Email

---

## 7. *[chapter title not captured]*

### 7.1. Create an Interconnector User record

To Create a new Interconnector User, select the Unit Management tab, then the Interconnector User tab. Press the ‘Create new Intercon *[source breaks off here mid-word; the rest of Chapter 7 is missing]*

---

## 8. *[Asset Alignment; chapter title not captured]*

### 8.1. Grouping Assets by Unit (Asset Alignment)

- Prior to initiating the Pre-qualification Process, the registered asset(s) must be aligned to a specified Unit(s). To align assets to units, it is pre-supposed that the asset(s) and the unit(s) have all been registered in advance. If this is not the case, the user must ensure these steps are completed.

- Upon initial registration of an asset the ‘status’ will be set to ‘Accepted’ by default as indicated on the tile in Figure below

- When ready, the User must select ‘Align Assets to Units’ on the Unit Management Landing Page

*Align Assets to Unit*

### 8.2. Grouping Assets by Unit (Asset Alignment)

### 8.3. Selecting Unit for Grouping

- The User will be prompted to select or identify the Unit for grouping or alignment. The user can search by entering the Unit Name in the search bar or selecting it from the drop down list. Please note the exact naming of the Unit to produce a successful search result.

- A unit can only be aligned if its Status is equal to ‘Draft’. Once has a Unit has been appraised by the Registrations Team and set to ‘Accepted’ it is no longer available for re-alignment. If the situation arises where the Unit in question requires an amendment or modification to its asset(s) then the Unit in question must undergo the Unit Versioning Process. To learn more about Unit Versioning, refer to the Chapter on Unit Versioning.

### 8.4. Match & Un-matching selected assets to Unit for Grouping

- The User will be presented with two adjacent columns 1) the Unit selected in the search result on the left-hand column and 2) all available registered assets eligible for grouping on the right-hand side.

Asset Alignment Screen

- If an asset is not listed, then the user will still have the option to use the search button to undertake a secondary search of the asset in question. The user must ensure they have the correct unique name reference to ensure a successful search result match. Once the asset(s) are identified, the User can either choose to a) ‘move all’ or b) ‘move selected’ assets to be grouped or aligned with the desired unit.

- Once the User is satisfied with the grouping they can then confirm the selection or alignment by selecting the Confirm button as illustrated in Figure overleaf in the adjacent page.

- The User has the option to switch assets out of the grouping by ‘moving selected’ from the left column (unit name) to the right column (available assets) if they decide it was an incorrect grouping of assets for alignment and wish to reverse their decision before final confirmation. To enable this feature, the user must check the box against each asset on the left-hand column and select ‘’Move Selected’’ to transfer the assets back into the right-handed column (available assets). This may be required when a user decides it was an incorrect grouping of assets for alignment and wish to reverse their decision before final confirmation.

- The User will receive a confirmation pop up notification to alert them to the Unit Grouping being completed.

### 8.5. Match & Un-matching selected assets to Unit for Grouping Asset Alignment Screen – Reverse decision

### 8.6. Asset Alignment for multiple units

- There will be a requirement for Users to undertake secondary alignments between assets and additional units beyond the initial grouping. In this instance, users are given the ability to deploy the same assets to be grouped under different Units.

- Figure below illustrates the example where 2 Units have been created, but both Units will be aligned to one specific asset. For example, Hampshire Coast Renewables Unit is made up of both Peacehaven Wind Farm AND Roe dean Wind Farm. Sussex Coast Renewables is only made up of Peacehaven Wind Farm. Therefore, the Asset Peacehaven Wind Farm is being aligned to 2 independent Units. This configuration is possible during the registration stage by repeating the asset alignment exercise for each Unit in turn.

Multiple Units for Alignment with existing assets

---

## 9. Prequalification for Services

### 9.1. Identifying Units to participate in Pre-qualification.

Once the Units and Assets have been registered and the Alignment exercise has been undertaken, the user is in a position to identify units they wish to elect for participation in the Market and subject to the pre-qualification process. To start, the user must navigate to the selected unit on the Unit Management home page and hover over the right hand three corner and click on the three dots on the Unit tile as highlighted in the Figure below. They will be prompted with the link ‘pre-qualify for services.

Pre-qualify for Services Link

### 9.2. Pre-qualification Home Page

The user will then be presented with the Pre-qualify for Services Page as illustrated in Figure below and prompted to then select the services to prequalify the Unit for.

*Pre-qualify for Services Page*

- The user will then be presented with the current seven Balancing Services they can select from. To select the user checks the checkbox. A user can select all or one of the services.

- The user then selects the ‘’Confirm Selection’’ button to proceed to the next step.

### 9.3. De-selecting Services to apply for prequalification for selected Unit.

- If the user makes an error or wishes to reverse the decision to not select a particular service, they can simply uncheck the tick box before proceeding to the next step. If a user decides to make this decision after proceeding with completing the Service ‘data capture’ sub-sections, this is also possible by unchecking the service checkbox and clicking the ‘confirm services’ button.

- The user must note that if they proceed to populate service specific information for more than one service for the same Unit, in several attempts or over a duration of time (i.e. they submit information for service x on day 1, but then go onto update the portal with additional submission of information for service x on day 3) that they can keep track of which service is still in flight (or ‘draft’) as opposed to ‘submitted’ by referencing the ‘Service Status’ field. If the field value = Incomplete, then the submission for that service in example below ‘’Dynamic Containment LF’’ has yet to be completed, and therefore will require the user to select the ‘Confirm Services’ button again.

- This will ensure the secondary service submission has been accepted. If the Service Status Field = Submitted, then the application for that particular service, in the example below ‘’Dynamic Regulation HF’’ has already been ‘registered’.

Service Status Field

### 9.4. De-selecting Services to apply for prequalification for selected Unit: Cont

### 9.5. Completing Pre-qualification Criteria Sections by Service: Unit Calibration Section

- Each service selected will present the user with a series of sub-sections to complete with criteria specific fields. Each service is identified by the highlighted row illustrated in the figure below.

- The first subsection is entitled Unit Calibration and the user is expected to populate the corresponding fields. All the metric fields in this section are marked with a red asterisk and therefore mandatory. A user will not be able to proceed with the pre-qualification process without submitting information.

Services Specific Subsection – Unit Calibration

### 9.6. Obtain Service Values Feature

Obtain Service Values

Where a portal user has already made a prequalification for another service for the same Unit, they are able to ‘copy’ over the identical values from the existing application under the Unit Calibration Section over the new corresponding section under the new application by clicking ‘Obtain Service Values’ and selecting the Service for which they want to copy the pre-existing values over from and then selecting the Confirm button to complete the exercise.

### 9.7. Obtain Service Values Feature: Cont

### 9.8. Completing Pre-qualification: Attaching Supplementary Evidence

Services Specific Sub section

Once the Authorised Signatory is selected (this step is covered in the next section), the portal user is expected to upload any supporting evidence using the Upload Files button. Once selected the Portal User can upload files from their desktop etc and confirmation the documents or the zip file of multiple documents should highlight in blue with the ‘Done’ outcome.

### 9.9. Confirmation of Upload Completed

Services Specific Subsection

### 9.10. Completing Pre-qualification Criteria Sections by Service: Asset Testing Section

- The final sub-section to be completed requires gathering information on Asset Testing requirements for selected Service.

- As Figure below illustrates, each asset aligned to the Unit being considered will be listed and the corresponding asset testing data fields are expected to be populated by the user.

- Please note that whilst the fields are not marked with a red asterisk and therefore not currently designated as mandatory, a Unit cannot proceed with the pre-qualification request without the asset testing fields being completed.

Services Specific Asset Testing

### 9.11. Qualifying for the Balancing Mechanism Service

When the user has selected Balancing Mechanism as the service they wish to qualify for, as of Release 3.9 there is no information required in the Unit Calibration section, so the user can proceed to upload a copy of the Lead Party form or use the Authorised Signatory functionality as detailed in the following chapter to sign the form electronically before submitting their application.

### 9.12. Completion of Pre-qualification Criteria: Terms & Conditions Section

- The step preceding final submission involves completing the Service Specific Terms & Conditions Checkboxes.

- To complete the Pre-qualification process, the user must click on the ‘Save Draft’ button. This will appear in blue in its activated state on condition that all the prior subsections have been completed correctly. If it is in the shaded state, the user must revisit the subsections and ensure that the fields are populated and the evidence has been uploaded correctly. The user has the option to review the draft application at a later stage when they next login to the portal.

- When the user is ready to submit the Unit for pre-qualification application for approval, they then select the Submit button in Figure 48.0. In this instance, the National Energy System Operator Account Manager will be notified and undertake an internal appraisal of the application for the selected Unit and Service.

- To apply for additional Units for Pre-qualification, the user simply repeats the steps in this chapter for each respective Unit.

Services Specific Terms and Conditions

Using Authoris *[source breaks off here mid-word; the rest of Chapter 9 and the start of Chapter 10 are missing]*

---

## 10. *[ABSVD; chapter title not captured]*

### *[10.1.]* ABSVD Delivery Allocation *[heading partly lost in the source, where it appeared as “0. ABSVD Delivery Allocation”]*

Select the Service Name from the list of available Services.

Input the Settlement Date

And optionally select an Allocation Status.

Press ‘Search’ and the records that match your search criteria will appear. If the record’s status is ‘Pending Allocation’, you will then be able to press ‘Allocate’ to take you to the ‘ABSVD Allocation’ screen for that record.

### 10.2. ABSVD Allocation

On this sub-tab, the user can submit ABSVD Delivery Allocation values for every MPAN pair associated with an Asset per Settlement Period.

On this screen the user again uses the Unit ID, Service Name and Settlement Date to search, though if the Allocate link on a CDV record has been used, the filters will be prefilled On pressing Search, if results are found the below table will load for the selected Unit, Service and Settlement Date The user then has the option to filter using the Settlement Period Click on the down arrow on the row to expand. Every row will be for an MPAN pair associated to that Asset. Enter the allocation value into the MPAN Import/Export (MWh) field. If the CVD volume for the record is positive a positive value must be entered and if it negative a negative value must be entered.

The total of the values entered must match the value of the CDV Volume for that Settlement Period. If the user does not believe the CDV Volume to be correct, press the ‘Report Discrepancy’ button. This will update the CDV Status to ‘In Dispute’ for the NESO Settlements team to review.

Pressing Save will save the values and allow the user to come back later to submit. Please note that submission must take place before the Allocation Due Date. On pressing Submit then user will see a Success message and the status of the allocation will update to ‘Submitted’ for the NESO Settlements team to review.

### 10.3. ABSVD Bulk Allocation

The ABSVD Bulk Allocation tab allows the user to download CDV records in a CSV file, then having inputted the desired allocation values into the file, upload and submit them into SMP.

To find pending allocation records, search using the filters below. The Bulk CDV Download button will be enabled if matching records are found

On pressing ‘Bulk CDV Download’, a CSV file will generate with the below headers:

| SETTLEMENT DATE | SETTLEMENT PERIOD | Unit ID | Service Name | Asset ID | CDV Volume (MWh) | MPAN IMPORT | MPAN EXPORT | Volume (MWh) |
|---|---|---|---|---|---|---|---|---|

*[Header names re-joined; the copy-paste had split them mid-word, e.g. “SETTLEME NT”.]*

The user can then prepare the file for upload. The columns in the upload will have to match the columns obtained in the download file. Please note that the values in the ‘SETTLEMENT DATE’ column for the upload must follow YYYY-MM-DD format and MPAN IMPORT and MPAN EXPORT must be stored as numbers with 0 decimal places. Input the Allocation values in the Volume(MWh) column. The values must total the CDV Volume (MWh) for the Settlement Period e.g. if the CDV Volume(MWh) is 30 there are multiple entries for the same Settlement Period these must total 30. Once the file is ready, select ‘Bulk CDV Upload’ then the ‘Upload Files’ button. Upon successful upload, a success message will appear at the top of the screen. The status of the allocation will update to ‘Submitted’ for the NESO Settlements team to review. This can be verified by returning to the CDV view and searching for the same records

---

## 11. Global Versioning

### 11.1. What is Global Versioning?

The term Global Versioning refers to the process whereby a Market Provider can modify or alter the Unit, the Unit’s composition of Asset(s) and the reevaluation of any existing prequalification applications to ensure their continued eligibility to participate in the services it had originally been qualified for.

The process has been designed to be more streamlined so that all prospective modifications and/or alterations are captured in one instance from Market Providers and any tests or conditions are applied in real time and the outcome is calculated instantly where possible and the subsequent changes are applied to the Unit automatically.

The Global Versioning Process comprises of the following stages;

- The identification of the Unit in question and the capture of information relating to the Unit and associated asset(s) and updates to the connected prequalification applications.

- The verification of the data supplied in line with Versioning Criteria and the outcome decision on the modifications/alteration.

- The automated processing of the Unit to generate the latest Unit Version and the associated records to reflect the latest changes/alterations.

- The communication of the latest Unit Version and associated records to downstream systems such as the EAC platform.

### 11.2. Changes permitted through Global Versioning

As of Release 2.12 Global Versioning permits the following modifications or alterations to be made.

A Unit is subject to versioning when it requires a change or modification to its properties or to a change or modification to its composition of asset(s). This can include any of the following combination.

- An Increase or Decrease in the Total Demand or Generation Capacity resulting from an alteration in the composition of asset(s)
- The addition or remove/withdrawal of asset(s)
- A Modification to the Demand or Generation Capacity at an individual Asset Level.

A Unit and it’s connected Asset(s) can be subject to multiple iterations of Global Versioning during its lifetime. For example, a Unit can require several changes over time and each change will constitute a case for Versioning – therefore one Unit within a provider’s portfolio may have 1 Version whilst another may have 10 more.

Please note that as of Release 2.12 a ‘standalone’ asset is not eligible for Global Versioning after it has been registered. Only asset(s) that are committed to a Unit at the point of embarking on Global Versioning are eligible to be ‘modified’.

### 11.3. Changes not permitted through Global Versioning

Please note that as of Release 2.12 any other ‘Parameter’ on the Unit or the corresponding Asset outside of the Demand and/or Generation Capacity is not eligible for Global Versioning, meaning any modifications to such parameter values will require the Market Provider to liaise with the Account Manager to establish if modifications can be made to registered Units and Assets.

### 11.4. Why is Global Versioning required?

The main rationale for introducing Global Versioning on the SMP Portal is to keep track of changes of a Unit & a connected Asset over time which are documented and available for the Registrations & Contracts Team to monitor for auditing purposes as well as recording the history of a Unit and an Asset as it evolves or changes during its lifetime. Essentially, when changes are made to the Unit, it’s composition of Assets or the individual Assets, a cloned copy of the original record is produced with the original retaining its original properties, allowing a new version (cloned) to be subject to modifications or updates by the Portal User(s).

Moreover, ‘related’ or supplementary records linked to the Unit will also be cloned automatically. For example, if the origin Unit has a pre-qualification ‘application’ attached, the application record will also be cloned – critically retaining the Status at the point of Versioning. Equally all corresponding Asset Testing Data and Supplementary Evidence pegged to the original application will be tagged against the latest version of the Unit automatically. It is important to note that if the Unit satisfies particular ‘‘Service Criteria’’ or conditions then as a result of the modifications made by the Portal User, then additional information or evidence will be required to support the modification request.

It is important to note that with the introduction of User Roles, all Unit and Asset Records including those Versioned will be available to view and edit or manage exclusively by User(s) with the ‘Unit Manager’ Role assigned to their User Record/Profile by their respective Super User. For more on User Roles please visit the Chapter on User Management. Moreover, it is recommended that only one user at any one time is solely responsible for undertaking the task of Versioning a Unit.

For the purposes of the Guide, the naming convention will run as follows; the origin Unit and Asset will be referred to as Version 1.0 and the second iteration of the Unit and Asset will be referred to as Version 2.0. Any subsequent iterations will follow the same logic, so a third version will be referred to as 3.0.

### 11.5. What types of Global Versioning apply to Units?

There are currently two different types or instances of Global Versioning. These are as follows;

**Manual Versioning**

If the alterations to (or the composition of) assets connected to the Unit in question result in a total increase in either/both Demand and Generation Capacity, then the Unit will require appraisal by the Registrations Team before approval.

Any associated impacts on the Service Criteria for all or any of the Services the Unit is already approved to participate in will be evaluated and an outcome determined automatically.

Any associated existing prequalification post evaluation deemed ineligible will be classified as ‘Rejected’ automatically with an external notification sent to Portal Users associated with the Market Provider to notify them of the outcome decision at the point the Global Versioning Application ‘Form’ has been completed but whilst the Unit is pending manual appraisal.

A Unit subject to Manual Versioning cannot complete the Global Versioning Process until the Unit has been approved by the Registrations Team despite the connected pre-qualifications reevaluated automatically and deemed eligible or ineligible to continue.

**Automated Versioning**

If the alterations to (or the composition of) assets connected to the Unit in question result in a total decrease in either/both Demand and Generation Capacity, then the Unit will not require appraisal by the Registrations Team, instead it will be granted automatic approval.

Any associated impacts on the Service Criteria for all or any of the Services the Unit is already approved to participate in will be evaluated and an outcome determined automatically.

Any associated existing prequalification post evaluation deemed ineligible will be classified as ‘Rejected’ automatically with an external notification sent to Portal Users associated with the Market Provider to notify them of the outcome decision at the point the Global Versioning Application ‘Form’ has been completed but whilst the Unit is pending manual appraisal.

A Unit subject to Automated Versioning is able to complete the Global Versioning Process as it has been classified as ‘approved’ (Accepted) automatically, independently of the connected pre-qualifications which are also re-evaluated simultaneously and deemed eligible or ineligible to continue.

### 11.6. Conditions for Re-evaluating Prequalification Applications

Existing Prequalification applications subject to re-evaluation as part of Global Versioning will be in ‘Approved’ Status and the following key conditions are applied as part of the re-evaluation conditions to determine if the Unit remains eligible or is deemed ineligible.

- Where either a total increase or reduction in Generation and/or Demand Capacity results in drop below The Service Minimum threshold (SMT).

- Where the total increase or reduction in Generation and/or Demand Capacity results in a drop below, the adjusted/revised Allocated Volume is then checked against the SMT for the specified Service.

- Where the adjusted/revised Allocated Volume has also dropped below the SMT then the Unit is deemed ineligible to continue to participate in the service when the latest version of the Unit takes effect.

- If the total increase or reduction in Generation and/or Demand Capacity results does not result in a drop below The Service Minimum threshold (SMT) then the Unit is eligible to continue to participate in the service in question.

*The SMT is defined as the baseline Generation and/or Demand capacity volume a Unit is expected to deliver for the respective Service. Each Service will have a universal ‘constant’ threshold figure determined as part of the original specification by the National Energy System Operator when a service is devised.

### 11.7. Global Versioning Process Steps

### 11.8. Selection of ‘Primary’ Unit.

To initiate the GV process, you will be required to firstly identify the ‘Primary’ Unit that you wish to submit for Global Versioning. Please note the following;

1. Only Units in ‘Accepted’ Status can qualify for GV

2. A Unit must have at least one Asset ‘aligned’ to it.

The Portal User must navigate to the Change Request Tab on the Unit Management Landing Page and then select ‘Add Basket for Versioning’ custom button.

### 11.9. Selection of ‘Primary’ Unit: Cont

### 11.10. Creation of Global Versioning Basket – Basket Rules

Global Versioning uses the concept of Baskets to contain all of the Units that are subject to changes. The Basket ‘Rules’ are as follows;

- A Basket can contain one or more Units. These can be ‘Primary’ or ‘Impacted’ Units.

- Primary Units are those selected by the Market Provider

- Impacted Units are those Units identified as sharing at least one or more common assets as part of the composition of assets. Modifications made to the common asset will result in subsequent changes to other Units by virtue of the asset(s) being shared. These Units will be identified automatically and ‘pulled’ into the same Basket for the Portal User to preview and either approve or make further changes if required.

- All Units within a given Basket must share a Universal Basket ‘Effective From Date’ This Date is when the latest Version of the Unit will take effect. This date can be amended with future alternative dates.

- Each Basket also has a ‘Basket Processing Date’. This Date is calculated automatically and is currently used as a ‘cut-off’ date for committing the proposed changes (captured in the GV Application Form for each individual Unit) to be ‘executed’. This Date is currently 10 days from the Effective From Date. The 10 day period allows for any National Energy System Operator Approval or Intervention to be undertaken. If the Effective From Date is adjusted by the Portal User, then the Processing Date is adjusted automatically.

- A Basket can only be ready for processing when the following conditions are met;

1. The Processing Date has been reached or lapsed.

2. Every Unit in the Basket has a completed Application Form.

3. All Units in the Basket (Primary and Impacted) have been marked as ‘Eligible’ in the Eligibility Outcome Status.

### 11.11. Creation of Global Versioning Basket – Basket Steps

When the Portal User selects the Create New Basket, they will be prompted to set the Effective From Date entering a specific format of DD-MM-YYYY. To proceed, select ‘Confirm’.

### 11.12. Creation of Global Versioning Basket – Selection of the ‘Primary’ Unit.

When the Basket is created, the Portal User will be prompted to select the Unit by entering the Name in the Search Box and then pressing the ‘+’ button adjacent to it. If the Unit is found, it will instantly be added to the Basket and appear as a ‘line item’. The Basket Reference Number will always use the prefix CL-‘000000000’. If any Units fail the Validation Tests, the internal teams can use this reference to locate the corresponding Error Logs.

A Basket can be deleted at any stage prior to ‘Basket Committal’ (as outlined in the conditions overleaf).

### 11.13. Creation of Global Versioning Basket – Selection of the ‘Primary’ Unit.

Once selected the Unit will appear as illustrated below. The Line Item entry will contain the headline data for each Unit and will display the ‘before’ and ‘after’ the modifications or alterations have been made by way of completion of the Versioning Application Form for the Unit in question.

The ‘after’ columns shaded in Grey will be updated in real time upon completion of the Versioning Application Form with the latest updated parameters.

At the point a Unit is added to the Basket, the Eligibility Test Outcome Status will automatically be set to ‘Draft’. The next step is to complete the application form. To do this, select the ‘Proceed with application’ button.

Select the three dots next to this button to view other options:

The option ‘Preview Unit Details’ will enable the Portal User to review the existing Unit’s ‘data’ and current parameter values.

The option to ‘Remove Unit from Versioning’ allows the Portal User to withdraw the Unit from the Basket completely.

The option to ‘Cancel’ an individual Versioning Application Form once ‘started’ is available throughout by selecting the option ‘Cancel Versioning’ which is located on the bottom left hand side of the ‘Application Form’ Screens.

### 11.14. Completion of Global Versioning Application Form

By completing the Global Versioning Application Form you are able to notify us of;

- Any alteration to the composition of the primary asset(s)

- Any modification to primary individual asset(s)

- Both alteration the composition of the primary asset(s) & the modification to any individual primary asset(s)

### 11.15. Step 1: Selecting the action type

The Form allows the Portal User to capture changes resulting from either Adding/Removing Asset’s and/or also modifications to existing Asset(s) within the same Form. These are labelled as ‘Versioning Categories’.

Once the category options are selected, the Portal User is able to proceed with the Form by pressing ‘Confirm’.

### 11.16. Step 2.a: Use Case 1: Modifying Asset(s) exclusively.- Increase in Total Capacity.

This example will cover the instance where only one more Asset(s) that compose the Unit require a modification to the Demand and/or Generation Capacity. This next section in the Form will prompt the Portal User to provide the revised/latest Values for the Demand and/or Generation Capacity. Once entered, to proceed to the next section, the portal user will be prompted to select ‘next’ on the bottom right hand screen.

### 11.17. Step 2.b: Use Case 1: Modifying Asset(s) exclusively: Re-evaluation of existing Prequalification Application Data

Where the Total Capacity has increased at the Unit Level, the system will detect that any existing Prequalification Applications in Approved State will require attention. An orange banner with yellow warning will appear on this section of the form, providing the portal user the opportunity to update the relevant pre-qual application.

- The Portal User will be prompted to update or ‘re-affirm’ the Prequalification Parameters for any associated Prequalification applications that were previously approved.

- The mandatory field value is the Allocated Volume; however it is expected at this point of the application form to also included the Tested Capacity Volume.

- Currently as of Release 2.12, a revised ITE Certificate and a Date of said revised ITE Certificate is not mandatory for existing asset(s)..

### 11.18. Step 3: Use Case 1: Modifying Asset(s) exclusively: Submission of the Versioning Application Form.

To mark the completion of the Versioning Application Form for an individual Unit, the Portal User will be presented with two subsequent ‘pop-up’ notification screens as illustrated below. To proceed, click on the ‘ Validate and Submit’ button followed by the ‘Go back to the Versioning Basket’ Screen to navigate to the ‘Change’ Request’ Page and the Basket.

### 11.19. Trigger of Manual Versioning Conditions

In the Use Case example where the origin Primary Unit has increased in its total capacity, the Unit will be treated as follows;

- The Eligibility Test Outcome will be classified as ‘In Review’ in the Basket

- Any impacted Units that share the Asset in common will appear under the ‘Impacted ‘ Units Tab. These Units will also be classified as ‘In Draft’ in the Basket

- The Cumulative Value for the Demand and/or Generation Capacity Field will be updated in the ‘Grey’ Shaded columns (New Unit)

- The National Energy System Operator Business Units will be expected to appraise the Units (Both Primary and Impacted) to approve the changes. Once done, the Eligibility Test Outcome will change to ‘Eligible’ unless upon final Validation checks, errors in the associated Unit or Asset(s) have been identified that need National Energy System Operator input in which case the status will change to ‘Partially Eligible’.

### 11.20. Processing of Basket

Once the conditions for Processing the Basket have been met (below), then the Units in the Basket will be processed and new versions will be created as appropriate

1. The Processing Date has been reached or lapsed.

2. Every Unit in the Basket has a completed Application Form.

3. All Units in the Basket (Primary and Impacted) have been marked as ‘Eligible’ in the Eligibility Outcome Status.

### 11.21. Completion of Global Versioning Process

When Processing is complete, a ‘Unit Tile’ is instantly created for the latest Version of the Unit (Version 2.0) and adjacent to it will be the predecessor Version (V1.0). The Unit ‘Versions’ are distinguishable by the Status ‘Value’. Version 2.0 (the most recent will display as ‘Accepted’ and the predecessor Version 1.0 will display as ‘Versioned’. The Unit Tile marked Versioned’ will not be available to make any further edits or for example submit any prequalification applications under.

### 11.22. Limitations whilst Global Versioning Process is ‘Inflight’.

Once a Unit has been subject to Global Versioning, there are several limitations in place to prevent any further activity from occurring whilst the Global Versioning Process is in flight.

- Portal User are unable to modify or make repeated changes to the same Unit or any implicated Assets after Global Versioning has been initiated.

- Portal User are unable to prequalify the Unit for new services after Global Versioning has been initiated.

- Portal User are unable to re-align the same Unit with any new assets whilst in flight via the standard alignment process under Unit Management, as such changes will be encompassed through the Global Versioning process.

A Unit Tile is marked as ‘locked’ or ‘frozen’ whilst Global Versioning is in flight using a ‘I’ symbol adjacent to the name of the Unit.

### 11.23. Variation to the Global Versioning Application Form

#### 11.23.1. Reduction in Capacity via modification to individual asset(s)

In the instance that a Unit ‘s ‘Use Case’ for Global Versioning is due to an overall reduction in Demand or Generation Capacity, either by way of a change in the asset composition or a modification to an individual asset, the steps adopted to initiate Global Versioning as the same as previously outlined. It is critical to ensure the steps to confirm/update the prequalification parameters are also undertaken to ensure the accurate eligibility status is arrived.

When the Versioning Tests are concluded the Unit is deemed as ‘Eligible’ on the assumption that the ‘automated’ versioning criteria is satisfied. This eligibility status is also awarded if the Unit has any existing associated prequalification applications that have since been classified as ‘Rejected’. In this instance, these prequalification applications for specific service delivery will no longer be eligible to continue as of the effective from date for Version 2.0 (or the latest version). A supporting email notification will be issued to confirm this outcome for each respective prequalification application affected as advance warning.

#### 11.23.2. Increase in Capacity (or no net change in Capacity) due to re-alignment or change in composition of asset(s)

In the instance that a Unit‘s ‘Use Case’ for Global Versioning is due to an overall increase in Demand or Generation Capacity (or results in no net change in the total capacity) by way of a re-formation of asset composition - the steps adopted to initiate Global Versioning as the same as previously outlined. The Portal User must ensure when completing the Global Versioning Application Form that they select the correct option on the first screen to only ‘Add/Remove’ Asset(s).

The Portal User will also be expected to complete the re-alignment section to confirm the new formation of assets.

#### 11.23.3. Increase in Capacity (or no net change in Capacity) due to re-alignment or change in composition of asset(s)

Where the Unit’s Total Capacity increases, the eligibility outcome status will change to ‘In Review’ immediately after the Global Versioning Form is completed. It will be routed to the National Energy System Operator Registrations Team to appraise and change the status to Eligible.

### 11.24. Distinction between Primary and Impacted Units

Primary Units are considered as those which the Market Provider intentionally selects for Global Versioning. Impacted Units are those Units which share at least one common asset that is subject to modification. The Global Versioning Process rules will detect and implicate any connected Units at the point the ‘primary’ Unit’s asset(s) have been modified and at the end of the Global Versioning Application Form completion. Impacted Units will be ‘pulled’ into the same Global Versioning Basket as the Primary Unit and will require the same approach as the primary Unit in order to allow the Basket to complete processing. This means, that an application form will require completion for every impacted Unit in the same basket.

The application form for Impacted Units has been adjusted however to allow Portal Users the option to indicate the following options;

- No further changes to be added.

- Additional changes required – subsequent changes to the current composition of asset(s)

- Additional changes required – subsequent changes to prequalification section only as a direct result of the modification to the connected asset(s)

An example of listed impacted Units connected to a Primary Unit will display as illustrated below within a given basket.

Additional Customised Options for Impacted Units only

### 11.25. Errors in Processing Global Versioning Requests

Upon submitting Global Versioning Application Forms for every Unit in the Basket and the Validate Basket Custom Button has been selected, there may be occasion for an individual Unit to fail the Validation Tests due to incorrect or missing data. The eligibility test outcome will display as ‘partially eligible’ for such Units. The user will have an ‘Input Missing Data’ link available to them Click the link to be presented with the data that needs to be inputted to the Unit.

- Close will take the user back to the Change Request page

- Next will take the user to the next record related to the unit (e.g. an aligned Asset) that requires data input (if applicable)

- Validate and Next will check if the data entered meets requirements e.g. a Phone Number must be entered into a Phone Number field. If it does not an error will appear at the top of the screen

When the user has pressed Validate on the final screen and all data has been entered successfully the following screen will appear:

The basket Eligibility test Status will then update to In Review or Eligible as appropriate.

### 11.26. Managing Associated Units that share Assets that have been subject to Global Versioning

**Unit Formation**

If an asset has been aligned to a Unit in ‘Draft’ or ‘Submitted’ States , where the asset has been subject to Global Versioning it is expected that the Portal User must essentially refresh the Unit’s alignment to factor in the latest incarnation of the Asset that has been versioned.

This may require the Unit to be re-aligned and then re-submitted to the National Energy System Operator Business Unit for appraisal.

**Existing Pre-qualifications associated with Assets that have been subject to Global Versioning**

If an asset has been aligned to a Unit in ‘Draft’ or ‘Submitted’ States that also has premature prequalification applications (Draft, Incomplete, Signature in Progress) then it is also expected that a new prequalification is applied for to ensure the latest asset version is referenced, and the correct asset testing data is factored in the application.

### Global Versioning Scenarios & Global Versioning Criteria

**Evaluation Criteria & Scenario's for Versioning Types.**

| Use Case | Example | Requires Versioning | Versioning Type | Eligibility Status |
|---|---|---|---|---|
| My Unit's total capacity will reduce beyond the current capacity as a result of removing or modifying the capacity on an existing asset(s) AND The total capacity will reduce below the Service Minimum Threshold for the Service(s) for ALL OR ANY it has been pre-qualified for already | Capacity on Version 1.0 20 MW<br>Allocated Volume for DC HF 10 MW<br>Allocated Volume for DC LF 15 MW<br>Capacity Version 2.0 10 MW<br>Service Minimum Threshold (SMT) DC HF (8 MW) DC LF (8 MW) | Yes | Unit: Automated<br>Prequalification: Automated | Eligible (Unit = Accepted) (Prequalification = Rejected) |
| My Unit's total capacity will reduce beyond the current capacity as a result of removing or modifying the capacity on an existing asset(s) BUT The total capacity will remain above the Service Minimum Threshold for the Service(s) for ALL OR ANY it has been pre-qualified for already | Capacity on Version 1.0 50 MW<br>Allocated Volume for DC HF 10 MW<br>Allocated Volume for DC LF 15 MW<br>Capacity Version 2.0 20 MW<br>Service Minimum Threshold (SMT) DC HF (10 MW) DC LF (10 MW) | Yes | Unit: Automated<br>Prequalification: Automated | Eligible (Unit = Accepted) (Prequalification = Approved) |
| My Unit's total capacity will increase beyond the current capacity as a result of adding or modifying the capacity on an existing asset(s) AND The total capacity will increase above the Service Minimum Threshold for the Service(s) for ALL OR ANY it has been pre-qualified for already | Capacity on Version 1.0 20 MW<br>Allocated Volume for DC HF 10 MW<br>Allocated Volume for DC LF 15 MW<br>Capacity Version 2.0 30 MW<br>Service Minimum Threshold (SMT) DC HF (10 MW) DC LF (10 MW) | Yes | Unit: Manual Versioning required.<br>Prequalification: Automated Approval. | In Review (Unit = In Review) (Prequalification = Approved) |

*[Table rebuilt from three flattened scenario tables in the source; "Prequalifica tion" re-joined. Straight apostrophes are used in this table only.]*