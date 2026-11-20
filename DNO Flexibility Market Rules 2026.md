# DNO Flexibility Market Rules 2026 – FMR-SBM (Baselining), FMR-VSM (Verification & Settlement) and FMR-PQC (Pre-Qualification Criteria) – extracts

> **Source file:** `DNO Rules 2026.txt` (Market Facilitator web pages, copy-pasted)  
> **Coverage:** The source joins extracts from **three** Flexibility Market Rules, kept here in source order as Parts A to C. In each part the summary, section 1 (Applicability), the amendment record and the metadata annex are not included.  
> - **Part A – FMR-SBM (DNO Baselining rule):** sections 2–4.  
> - **Part B – FMR-VSM (Verification & Settlement Methodology):** from section 2 to the glossary. This part is word-for-word identical to the separate file *FMR-VSM Verification and Settlement Methodology V2.3* from section 2.1 onwards.  
> - **Part C – FMR-PQC (Pre-Qualification Criteria):** sections 2–3.  
>
> Section and table numbers restart in each part (each has its own section 2, Table 2 and so on), and Part A itself numbers two tables as Table 2.  
> **Converted:** 2026-10-07. Wording kept verbatim from the source copy-paste; only layout artefacts (page headers/footers, line wraps, website navigation, broken tables) were cleaned up. Sections the source marks as guidance are not legally binding. Notes in *[italic square brackets]* are editorial.

---

# Part A – FMR-SBM: DNO Baselining Flexibility Market Rule (extract)

## 2. Baselining Methodology

### 2.1 Standard Baselining Methodologies definitions

The baselining methodologies used in this Flexibility Market Rule are outlined in Table 2 below.

**Table 2: Baselining methodologies**

| Name | Definition |
|---|---|
| Asset Capacity | Assumes the participating Distributed Energy Resource (DER) operates at its full rated capacity during the flexibility event, irrespective of actual operational conditions. |
| Fixed Reference | Uses a fixed daily profile derived from the observed energy behaviour of a representative group of DERs that represents normal operating behaviour or a DNO’s planning scenarios. |
| Nomination | Uses an estimated/expected set of meter values, provided by the FSP, based on the expected or normal operation of the site / DER without any flexibility event, for a future availability window that then becomes a utilisation event. |
| Recent History | Uses a set of recent, eligible days (i.e. excluding Event Days such as a day providing a flexibility service) preceding a utilisation event. This may also include correction factors such as within-day adjustments for weather variables or removal of outlier values. |
| Zero | The baseline energy consumption or generation is set to zero, meaning no energy usage or production is assumed in the absence of the utilisation event. |

#### Explainer: What does a baselining methodology look like in practice?

This section is provided as guidance to the Flexibility Market Rule. Therefore, it is not legally binding and falls outside of the formal change management process.

A simplified example for each baselining methodology specified in Table 1 is provided in this section. These examples are non-exhaustive and do not cover all circumstances where they would be used (e.g. only one direction of service is shown).

Asset Capacity

This methodology assumes the participating DER operates at its full rated capacity (no de-rating) during the flexibility event, irrespective of actual operational conditions. Worked examples of these principles are shown below for a Schedulable Generation DER which has a full rated export capacity of 5MW. In the example, the Generation DER has a Generation Turn Down contract for 2MW.

The DER turns down generation from 5MW to 3MW and is paid for 2MW as the baseline was set at 5MW (i.e. the full rated capacity) and the measured power during the Service Window was 3MW.

This section is provided as guidance to the Flexibility Market Rule. Therefore, it is not legally binding and falls outside of the formal change management process.

*[Diagram/image in the original web page was not captured in the copy-paste.]*

Fixed Reference

This methodology uses a fixed daily profile derived from the energy behaviour of a representative group of DERs that represents normal operating behaviour or from a DNO’s planning scenarios.

In the example shown below, the baseline value represents a reference, non-smart charging behaviour for a large group of domestic EV charging points.

It is this representative behaviour that is used to set the baseline value of -5MW to assess the level of Demand Turn Down provided by the DER. The measured output during the Service Window is -3MW, therefore it is deemed to have delivered a dispatched capacity of 2MW.

*[Diagram/image in the original web page was not captured in the copy-paste.]*

This section is provided as guidance to the Flexibility Market Rule. Therefore, it is not legally binding and falls outside of the formal change management process.

The above example covers the scenario where there is a reduction or increase in consumption and generation. Where the delivery of flexibility by a DER (e.g. Intermittent Generation, Storage and EV Charger V2G) results in a swing from prevailing Active Energy Import to Active Energy Export (or vice versa) which will typically be where the FSP uses a Point of Connection metering arrangement at a domestic site (not relevant to Industrial and Commercial (I&C) sites as Point of Connection uses Nomination) there may be a need to assess flexibility delivery in comparison to the Fixed Reference Baselines across both the Import and Export MPANs for the site.

Zero

The baseline energy consumption or generation for this methodology is set to zero, meaning no energy usage or production is assumed in the absence of the utilisation event.

In the example shown below, the DER is deemed to have provided a dispatched capacity of 2MW through a Generation Turn Up service as the measured output during the Service Window was 2MW.

*[Diagram/image in the original web page was not captured in the copy-paste.]*

This section is provided as guidance to the Flexibility Market Rule. Therefore, it is not legally binding and falls outside of the formal change management process.

Nomination

This methodology uses a proposed estimated/expected set of meter values / data, provided by the FSP, based on the expected or normal operation of the site / DER without any flexibility event, for a future availability window that then becomes a utilisation event. The timelines for submission of a Nomination baseline are detailed in the Nomination Baselining Methodology Submission Deadline section of this Flexibility Market Rule.

Nomination values may differ over the Service Window or be a single value that is applied for the whole Service Window.

As nomination baseline methodologies rely on FSPs to propose the values used, there will be accuracy standards that the DNO requires the FSP’s nominations to adhere to, to ensure the nominated values accurately reflect normal operating behaviour. This is detailed in the Nomination Baselining Methodology Accuracy section of this Flexibility Market Rule.

In the example shown below, a variable nomination value has been proposed by the FSP (-5MW for the earlier part of the Service Window and -4MW for the later part). In this scenario, the DER is paid for a dispatched capacity of 2MW of Demand Turn Down for the first part of the Service Window and a dispatched capacity of 1MW for the latter part.

*[Diagram/image in the original web page was not captured in the copy-paste.]*

This section is provided as guidance to the Flexibility Market Rule. Therefore, it is not legally binding and falls outside of the formal change management process.

Recent History

This methodology uses a set of recent, eligible days preceding a utilisation event and will complete an assessment based on the same time of day (i.e. 30-minute window) and type of day (i.e. working day or non-working day). This may also include correction factors such as a within-day adjustment for something like weather variables or removal of outlier values (typically defined as Event Days).

Event Days can include activities such as delivery of Balancing Services, Virtual Trading, Site Outage, Equipment and/or Site Disconnection.

In the example shown below, a DER baseline of 4.5MW for a Service Window on a Friday is set based on the mean average of the 10 most recent working days, which weren’t Event Days. Weekends and the Purple coloured Thursday (which met the criteria to be defined as an Event Day) are therefore excluded from the calculation. The measured power during the Service Window was 2.5MW of generation, and therefore, the DER is paid for a dispatched capacity of 2MW of Generation Turn Down.

*[Diagram/image in the original web page was not captured in the copy-paste.]*

Examples of other schemes, which are not in scope of this Flexibility Market Rule that use a recent history baseline are:

Balancing Settlement Code (BSC) historical baseline used for the Balancing Mechanism by Virtual Lead Parties (VLPs) and for Virtual Trading Parties (VTPs) in the wholesale market based on the Baselining Methodology Document. This includes a within-day adjustment for use in the Balancing Mechanism.

NESO Demand Flexibility Service (DFS), where the ‘DFS Participation Guidance document’ details an example of the Operational Baseline calculation in Appendix 5.

Capacity Market Rules use a historical baseline, as defined in Schedule 2 (‘Baseline Methodology’), for Demand Side Response (DSR) Capacity Market Units (CMUs).

### 2.2 Default Baseline Methodologies

The Default Baseline Methodologies (DBM) set out the expected baselining methodology in a given scenario.

The DBM have been designed to align with the variables included in the Standard Pre-Qualification Criteria of:

Asset Scale (i.e. Domestic or I&C).

Metering Arrangement (i.e. Point of Connection Boundary Point Metering System or Asset Metering System at, or part of the Asset providing the flexibility service).

Technology Type (i.e. the type of DER which is the asset providing the flexibility service).

Demand Turn Down (DTD) / Generation Turn Up (GTU) or Demand Turn Up (DTU) / Generation Turn Down (GTD).

The DBMs are shown in Tables 2 (Domestic) and 3 (I&C) below:

**Table 2: DBMs for Domestic DER**  *[This table has merged (row-spanning) cells that could not be rebuilt reliably from the flattened copy-paste. Columns: Asset Scale | Metering Arrangement | Technology Type | DTD / GTU | DTU / GTD. The cells are listed below in source order, left to right and top to bottom.]* 
- Domestic
- Asset Level
- Schedulable Generation
- Zero
- Asset Capacity
- (no de-rating)
- Intermittent Generation
- Storage
- Zero
- Heat Pump
- (Asset Level)
- Fixed Reference
- EV Charger DSR
- EV Charger V2G
- Flexible Site Demand
- Point of Connection
- Schedulable Generation
- Zero
- +
- (Flexible Site Demand)
- Fixed Reference
- Asset Capacity
- (no de-rating)
- +
- (Flexible Site Demand)
- Fixed Reference
- Intermittent Generation
- Storage
- Zero +
- (Flexible Site Demand) Fixed Reference
- Heat Pump
- (Asset Level)
- Fixed Reference
- +
- (Flexible Site Demand)
- Fixed Reference
- EV Charger DSR
- EV Charger V2G
- Flexible Site Demand
- (Flexible Site Demand)
- Fixed Reference

**Table 3: DBMs for I&C DER**  *[This table has merged (row-spanning) cells that could not be rebuilt reliably from the flattened copy-paste. Columns: Asset Scale | Metering Arrangement | Technology Type | DTD / GTU | DTU / GTD. The cells are listed below in source order, left to right and top to bottom.]* 
- I&C
- Asset Level
- Schedulable Generation
- Zero
- Nomination
- Intermittent Generation
- Storage
- Zero
- Heat Pump
- Nomination
- EV Charger DSR
- EV Charger V2G
- Flexible Site Demand
- Point of Connection
- Schedulable Generation
- Intermittent Generation
- Storage
- Heat Pump
- EV Charger DSR
- EV Charger V2G
- Flexible Site Demand

The DBM should be allocated at the point of registration.

NOTE: Where a DER has different default methodologies depending on the direction of the service (i.e. DTD/GTU or DTU/GTD), all relevant options should be listed, and at the point of bidding for a service, where the relevant direction is known, the specific default methodology will be confirmed.

Where a DNO allows Planned Assets (such as DERs that are currently under development or an intention of an FSP to recruit third-party DERs in the future) to be bid into their flexibility markets, the FSP may not have all the information required for the DBM to be allocated at the point of bid submission. Under this scenario, no DBM will be allocated, but as part of the Development Plan that would be agreed between the DNO and the FSP, a deadline for the DBM process to be completed before the first contracted service period will be agreed.

#### Guidance: Mapping of the Energy Source/Technology Types used in the Pre-Qualification Criteria to the technology types in this document

This section is provided as guidance to the Flexibility Market Rule. Therefore, it is not legally binding and falls outside of the formal change management process.

The following mappings apply:

| Energy Source/Technology Type | Consolidated Baselining Category |
|---|---|
| Advanced Fuel (produced via gasification or pyrolysis of biofuel or waste) | Schedulable Generation |
| Biofuel – Biogas from anaerobic digestion (excluding landfill & sewage) | Schedulable Generation |
| Biofuel – Landfill gas | Schedulable Generation |
| Biofuel – Other | Schedulable Generation |
| Biofuel – Sewage gas | Schedulable Generation |
| Biomass | Schedulable Generation |
| Fossil – Brown coal/lignite | Schedulable Generation |
| Fossil – Coal gas | Schedulable Generation |
| Fossil – Gas | Schedulable Generation |
| Fossil – Hard coal | Schedulable Generation |
| Fossil – Oil | Schedulable Generation |
| Fossil – Oil shale | Schedulable Generation |
| Fossil – Other | Schedulable Generation |
| Fossil – Peat | Schedulable Generation |
| Geothermal | Schedulable Generation |
| Hydrogen | Schedulable Generation |
| Nuclear | Schedulable Generation |
| Waste | Schedulable Generation |
| Solar | Intermittent Generation |
| Water (flowing water or head of water) | Intermittent Generation |
| Wind | Intermittent Generation |
| Stored Energy (all stored energy irrespective of the original energy source) | Storage |
| Onsite Battery | Storage |
| Air Source Heat Pump | Heat Pump |
| Ground Source Heat Pump | Heat Pump |
| Water Source Heat Pump | Heat Pump |
| Hybrid Heat Pump | Heat Pump |
| EV Charger DSR | EV Charger DSR |
| EV Charger V2G | EV Charger V2G |
| Flexible Site Demand | Flexible Site Demand |

*[In the original the Consolidated Baselining Category cells span several rows. The category is repeated on each row here.]*

### 2.3 Alternative and Confirmed Baselining Methodologies

An Alternative Baselining Methodology (ABM) is available to ensure that DERs with atypical characteristics or operational behaviours can be fairly and appropriately assessed where the DBM is not suitable. The only option for an ABM is a Nomination baseline. Further details are set out in later sections.

A high-level overview of the ABM request process and how it leads to the Confirmed Baselining Methodology (CBM) is shown below:

The CBM shall be used for all verification and settlement calculations.

*[Diagram/image in the original web page was not captured in the copy-paste.]*

By the implementation deadline of this Flexibility Marker Rule, DNOs will begin publishing the key deadlines for:

confirming the allocated DBM

the latest point at which an FSP can raise an ABM request

when the CBM will be confirmed by the DNO.

NOTE: While it is anticipated that in the majority of cases that once the CBM notification deadline passes, there should be no further changes to the applicable baselining methodology for a Meterable Unit, there may be certain cases where this is an appropriate action. In such cases, either the DNO or the FSP may propose a change to the CBM after the standard deadline, which will be implemented if agreed by both parties.

NOTE: Following notification from a DNO of ABM approval, the platform provider will override the DBM allocated to the specific DER based on an approved use of the ABM for a specific group of DER(s) within a Meterable Unit. This ABM allocation should be the enduring position rather than time limited.

### 2.4 Aggregation of DERs into Meterable Units

Baselining will be completed at a Meterable Unit level rather than individual DER level. A Meterable Unit is the aggregated level used for settlement and may consist of either multiple DERs or a single DER, as shown in the examples below:

*[Diagram/image in the original web page was not captured in the copy-paste.]*

The following controls will be implemented:

Non-Nomination baselined DERs (using the baselines of Asset Capacity, Zero or Fixed Reference) can be grouped into a single Meterable Unit, as all methodologies make use of static values, which are known in advance and are set by DNOs.

Non-Nomination baselined DERs cannot be grouped into a Meterable Unit containing Nomination baselined DERs, as Nomination baselines use values which are submitted by the FSP and therefore, a Meterable Unit containing Nomination baselined DERs are subject to accuracy standards.

If an FSP wishes to combine Non-Nomination baselined DERs with Nomination baselined DERs into a Meterable Unit, the FSP would be required to submit an ABM request (see next section) to the DNO for all Non-Nomination baselined DERs to become Nomination baselined.

NOTE: Where a DER has an option for the DBM used dependent on the direction of the service (i.e. DTD/GTU or DTU/GTD), care must be taken in grouping applicable DERs into a Meterable Unit. For example, I&C DBMs metered at Asset Level for Schedulable Generation or Intermittent Generation have a DTD/GTU methodology of “Zero” but a DTU/GTD methodology of “Nomination”. This means that this particular variant of DER could be grouped into different Meterable Units (i.e. Nomination or Non-Nomination) depending on which direction the service is for.

Explainer: What does aggregation into a Meterable Unit look like in practice?

This section is provided as guidance to the Flexibility Market Rule. Therefore, it is not legally binding and falls outside of the formal change management process.

A simplified example for two scenarios is provided in this section. These examples are non-exhaustive and do not cover all circumstances where they would be used (e.g. combining other types of asset or multiples of the same asset type).

Example - For the grouping of Non-Nomination Baselined DERs into a Meterable Unit. It requires the aggregation of the static baseline values.

In the example, the technology types involved are a Heat Pump and Storage. In both cases, they are installed at a domestic site, the metering arrangement used is Point of Connection, and the service direction is DTD/GTU. From the table for the overview of DBMs for domestic sites (Table 2) the relevant baseline methodology in this case is the Zero plus Fixed Reference baseline for Flexible Site Demand to be used for the Point of Connection metered Storage DER, while the Point of Connection metered Heat Pump DER calls for the Heat Pump Fixed Reference and Flexible Site Demand to be used.

In this example, the Heat Pump and Storage DERs are located in the same domestic property. Therefore, the Fixed Reference value for the Flexible Site Demand is only used once in the baseline values. If these DERs were located at separate domestic properties, the Flexible Site Demand would be included twice to reflect this.

The diagram below illustrates how this would work in practice and, using the indicative figures, would result in a baseline value of -2.75 kW for the property and Meterable Unit.

*[Diagram/image in the original web page was not captured in the copy-paste.]*

NOTE: Note kW values shown are for illustration purposes only

This section is provided as guidance to the Flexibility Market Rule. Therefore, it is not legally binding and falls outside of the formal change management process.

Taking a second example: the technology types involved are a Heat Pump and an EV Charger DSR. In both cases, they are installed at a domestic site, the metering arrangement used is Point of Connection, and the service direction is DTD/GTU. From the table for the overview of DBMs (Table 2) for domestic sites the relevant baseline methodology in this case is the EV Charger Fixed Reference baseline and Flexible Site Demand to be used for the Point of Connection metered EV Charger DSR DER while the Point of Connection metered Heat Pump DER calls for the Heat Pump Fixed Reference and Flexible Site Demand to be used.

Again, in this example, the Heat Pump and EV Charger DSR DERs are located in the same domestic property. Therefore, the Fixed Reference value for the Flexible Site Demand is only used once in the baseline values. If these DERs were located at separate domestic properties, the Flexible Site Demand would be included twice to reflect this.

The diagram below illustrates how this would work in practice and, using the indicative figures, would result in a baseline value of -4 kW for the property and Meterable Unit.

*[Diagram/image in the original web page was not captured in the copy-paste.]*

NOTE: Note kW values shown are for illustration purposes only

### 2.5 Alternative and Confirmed Baselining Methodologies

DNOs shall independently calculate and set their Fixed Reference Baselines.

To provide better visibility of these calculations, DNOs shall submit Reference Data, containing their Fixed Reference Baselines for each distinct categorisation to the Market Facilitator.

### 2.6 Nomination Baselining Requirements

#### 2.6.1 Nomination Baselining Methodology Submission Deadline

For any Meterable Unit where a Nomination baseline is the CBM, the FSP must submit a Nomination to the DNO no later than the bid submission deadline during the flexibility services tender process. This ensures that, should the FSP be issued a contract award notice, the DNO will already hold a valid nomination value that can be used as a fallback for settlement purposes if no updated Nomination is received before the first flexibility service period.

NOTE: Where there may be a significant gap between contract award notice and service delivery (e.g. in the case of long-term tenders), the expected behaviour of a Meterable Unit may change over time (e.g. changes may arise due to portfolio churn within the Meterable Unit or improvements in forecast accuracy closer to delivery). To mitigate this, FSPs will have the ability to resubmit updated Nominations beyond the original bid submission deadline, where appropriate.

NOTE: For any flexibility products where the Utilisation Instruction Timing is set at the point of trade, meaning that upon receiving a contract award notice, the FSP has certainty that flexibility delivery will be required in the awarded service period (e.g. Peak Reduction and Scheduled Utilisation products). Allowing unrestricted Nomination resubmissions after contract award introduces a material risk of gaming, as there is no opportunity to verify the FSP’s nomination against typical operating behaviour. As such, for these products, the Standard Resubmission Deadline is also the bid submission deadline. Nonetheless, provisions have been established to enable post-deadline nomination resubmissions in exceptional circumstances, subject to DNO approval.

Details of the deadlines for nomination submissions are shown in Table 4 below.

**Table 4: Deadlines for Nomination baseline methodology submissions**  *[This table has merged (row-spanning) cells that could not be rebuilt reliably from the flattened copy-paste. Columns: Product Type | Utilisation Instruction Timings | Nomination Type | 1st Submission | Standard Resubmission Deadline | Extended Resubmission Deadline. The cells are listed below in source order, left to right and top to bottom.]* 
- Peak Reduction
- At trade
- Bid Submission Deadline
- Bid Submission Deadline
- Day-1, 12:00
- Scheduled Utilisation
- Operational Utilisation
- (including Scheduled Availability & Variable Availability where applicable)
- Week Ahead
- Week-1, Thursday 12:00
- Day Ahead
- Day-1, 12:00
- Day, Hour-1
- 15 Minutes
- Day, Hour-1
- N/A
- 2 Minutes

An FSP may make a request to a DNO for approval to apply the Extended Resubmission Deadline for a Meterable Unit in situations where the Standard Resubmission Deadline has passed, but extenuating circumstances have materially affected the expected behaviour of that Meterable Unit.

Extenuating circumstances may include, but are not limited to:

Outages affecting the Meterable Unit's normal operation

Communication system failures that prevented the timely submission of a Nomination

Demand Control Events

The impact of Event Days from other contracted services

Significant portfolio churn or fundamental changes in the Meterable Unit’s expected behaviour

Upon receiving such a request, the DNO will assess whether the circumstances constitute a valid extenuating event with a material impact and is satisfied that sufficient evidence (where requested) has been provided to determine whether to grant the use of the Extended Resubmission Deadline for the affected Meterable Unit.

#### 2.6.2. Guidance for Nomination Baselining

FSPs shall adhere to the principles outlined below when developing a Nomination baseline. These principles are recognised as good industry practice.

Consistency: Nominations should be based on a stable and repeatable methodology that does not change arbitrarily between events or periods.

Data-driven approach: Where possible, Nominations should be informed by recent historical meter data or justified forecasts aligned to known operational characteristics, including the impacts of factors such as stacking.

Transparency and traceability: The rationale and assumptions behind Nomination values must be clearly documented and made available to the DNO if requested as part of a Nomination Performance Review.

Forward-looking basis: Nominations should reflect expected behaviour in the nominated period, not be retroactively adjusted based on past performance.

Auditability: The methodology used to generate nominations must be capable of independent verification by the DNO as part of a Nomination Performance Review.

#### 2.6.3. Nomination Baselining Justification

Justification of the Nomination baseline should be submitted by FSPs to DNOs in a concise manner.

The process map below provides a high-level overview of how the Nomination justification and accuracy process should operate.

*[Diagram/image in the original web page was not captured in the copy-paste.]*

In most cases, where a consistent methodology is used, FSPs should be able to reuse their justifications across events with no or minimal change. Only in situations where unique or time-sensitive conditions have affected the Nomination, such as operational constraints or the influence of revenue stacking, would a more specific explanation be required.

In accordance with principles outlined above (i.e. good industry practice), the justification for a Nomination baseline developed by an FSP should address the following questions:

Consistency

What methodology have you used to calculate the Nomination?

Has this methodology been applied consistently across other events or periods? If not, why not?

Data-Driven Approach

What data sources (e.g. historical meter data, forecasts, control system outputs) informed your Nomination?

How have you accounted for known operational factors, including the impact of revenue stacking?

Transparency and Traceability

What are the key assumptions behind your nominated value?

Where are these assumptions and data sources documented for reference?

Forward-Looking Basis

How does the Nomination reflect expected behaviour during the nominated period?

If it differs from recent historic usage, what justifies the change?

Auditability

Can you provide supporting evidence (e.g. data files, forecast models, internal approval records) if requested?

Is the nomination process traceable and verifiable by an independent reviewer?

NOTE: FSPs can submit a standardised justification statement, rather than a submission for each nomination, for scenarios where the asset and site operating conditions allow the principle of consistency to be met. This approach shall be agreed with the relevant DSO.

#### 2.6.4. Nomination Baselining Methodology Accuracy

Accuracy assessments will be completed on a quarterly basis for each calendar month by the DNO, and the results will be reported to the Market Facilitator as per section 3.

The accuracy calculation assessment has been designed to account for the maximum usable swing in either direction (import to export and vice versa), constrained by any declared operational limitations (the Available Capacity), and assesses error levels in proportion to the Meterable Unit’s capacity, to ensure the measure reflects the relative scale of the Meterable Unit.

These will be assessed against the Net % Error and the Absolute % Error.

Net % Error – Identify, over an assessment period, the average net error of a Meterable Unit to highlight whether on average, a Meterable Unit’s behaviour is consistently over or under an FSP’s Nomination values

*[Formula (Net % Error) was an image in the original web page and was not captured in the copy-paste.]*

Absolute % Error – Identify performance of a Meterable Unit over an assessment period in absolute terms to mitigate the risk of positive and negative Net % Errors netting to give a false indication of accurate Nominations. The absolute error assessment provides a clear indication of accuracy over an assessment period.

*[Formula (Absolute % Error) was an image in the original web page and was not captured in the copy-paste.]*

Where Effective Capacity is:

*[Formula (Effective Capacity) was an image in the original web page and was not captured in the copy-paste.]*

The terms used in the formulae are defined in Table 5.

**Table 5: Variable terms definitions**

| Variable | Description |
|---|---|
| u | The Meterable Unit being assessed. |
| m | The month being analysed. |
| s ∈ S(m) | Each settlement period “s” within the month “m” |
| Nominationᵤ,ₛ | The Nomination submitted by the FSP for the Meterable Unit in MW at time “s” |
| Metered Outputᵤ,ₛ | The metered value in MW at time “s” |
| Import Capacityᵤ,ₛ | The fully rated import capacity of the Meterable Unit in MW at time “s” |
| Export Capacityᵤ,ₛ | The fully rated export capacity of the Meterable Unit in MW at time “s” |
| Available Capacityᵤ,ₛ | The declared available capacity for the Meterable Unit at time “s” |

Thresholds, for the measures will be set by the DNOs, in alignment with the standard values set out in Section 3. Upon failure to meet these thresholds, the DNO will have the right to initiate a Nomination Performance Review. These thresholds may be updated in a future revision of this Flexibility Market Rule following data analysis on actual performance data.

#### Explainer: What data is used in the Net % Error and Absolute % Error calculation?

This section is provided as guidance to the Flexibility Market Rule. Therefore, it is not legally binding and falls outside of the formal change management process.

The calculation is based on using data where the contracted asset has not been dispatched for a period within a contracted service window. Taking an example to illustrate this, where the contracted service window is between 16:00 and 18:00 for two days and the service is being delivered by an asset that has a Nomination Baseline.

Day #1 – service is dispatched – meter reads for the full 2-hour service window are provided by the FSP to the DNO - These are used for settlement against the nominated baseline value.

Day #2 – service is not dispatched – meter reads for the full 2-hour service window are provided by the FSP to the DNO – The DNO can then use these meter reads to directly compare to the nominated baseline values, enabling a full analysis of the accuracy of the nomination, without a dispatch event skewing the behaviour.

The Day #2 data is what would be used in the calculation of Net % Error and Absolute % Error for that month. Day #1 data, where the service is dispatched, is only used for settlement purposes.

Event Days should be excluded from the calculation, as this skews the accuracy. In the example, if on Day #2 the service isn't dispatched by the DNO and the FSP knows it isn't going to be utilised and can use the asset for a NESO service this would qualify as an Event Day, one option is to allow the use of the Extended Resubmission Deadline (allows for an FSP to extend the time period that they can re-submit nominations with one of those listed in section 2.6 Table 4, valid reason being the impact from Event Days from other contracted services).

The other option is to account for it under the Nomination Performance Review, where Stage 1 allows that 'the FSP may submit additional information to the DNO to provide any mitigation that explains the cause for the accuracy standards not being adhered to'. This could also cover the scenario where the FSP did breach the thresholds for responding to a dispatch that had been received after the Extended Resubmission Deadline.

Where there are no days that are not Event Days there would be no data available for the Net % Error or Absolute % Error calculations, so the DNO wouldn't be expected to run the calculations. In this scenario where all service windows have been dispatched, this is where the nomination justification would be used. As there isn't a period that allows a direct observation of normal behaviour, the DNO instead would use the nomination justification as the basis for an assurance technique for the assessment.

#### Example: Nomination Baseline Accuracy

This section is provided as guidance to the Flexibility Market Rule. Therefore, it is not legally binding and falls outside of the formal change management process.

The following example for a Battery Energy Storage System (BESS) operating bi-directionally over the assessment period illustrates how the assessment of accuracy would work in practice.

In the example, there are five periods under consideration (Table 6 s1 to s5) and the standard sign convention of export being a positive value and import being a negative value has been used.

**Table 6: Example data**

| Interval | Nomination (MW) | Metered Output (MW) | Import Capacity (MW) | Export Capacity (MW) | Available Capacity (MW) |
|---|---|---|---|---|---|
| s1 | -3 | -5 | -5 | 5 | -4 |
| s2 | 2.5 | 1 | -5 | 5 | -6 |
| s3 | -1 | 1 | -5 | 5 | -3 |
| s4 | 3 | 2.5 | -5 | 5 | -5 |
| s5 | -2 | -1.5 | -5 | 5 | -2.5 |

NOTE: The Available Capacity covers any swing from import to export, or vice versa, where the technology type has that capability. For example, in the table above, the Available Capacity for period s2 is -6MW and this could be a GTD of 2.5MW and a DTU of 3.5MW.

The Nomination (MW) less Metered Output (MW) for each period is aggregated to give a total of 1.5MW of the net error calculation. The absolute value of Nomination (MW) less Metered Output (MW) for each period is aggregated to give a total of 6.5MW of the absolute error calculation.

**Table 7: Aggregated net and absolute value of Nomination (MW) less Metered Output (MW) for s1 to s5** 
| Interval | Nomination (MW) – [A] | Metered Output (MW) – [B] | Aggregate net value [A] – [B] (MW) | Aggregate Absolute value ABS([A] – [B] (MW) |
|---|---|---|---|---|
| s1 | -3 | -5 | 2 | 2 |
| s2 | 2.5 | 1 | 1.5 | 1.5 |
| s3 | -1 | 1 | -2 | 2 |
| s4 | 3 | 2.5 | 0.5 | 0.5 |
| s5 | -2 | -1.5 | -0.5 | 0.5 |
| TOTAL |  |  | 1.5 | 6.5 |

The aggregated Effective Capacity is -19.5MW (Table 8).

**Table 8: Aggregated Effective Capacity for s1 to s5** 
| Interval | Import Capacity (MW) – [A] | Export Capacity (MW) – [B] | Available Capacity (MW) – [C] | Min (Max(\|A\|, \|B\|), \|C\|) (MW) |
|---|---|---|---|---|
| s1 | -5 | 5 | -4 | 4 |
| s2 | -5 | 5 | -6 | 5 |
| s3 | -5 | 5 | -3 | 3 |
| s4 | -5 | 5 | -5 | 5 |
| s5 | -5 | 5 | -2.5 | 2.5 |
| TOTAL |  |  |  | 19.5 |

This gives a Net % Error of 7.69% (i.e. 1.5MW / 19.5MW) and an Absolute % Error of 33.3% (i.e. 6.5MW / 19.5MW).

#### 2.6.5. Nomination Performance Reviews

Where an FSP is not meeting the accuracy performance requirements (i.e. Net % Error and/or Absolute % Error) for a Nomination baseline, a DNO has the right to initiate a Nomination Performance Review. There are three possible stages to the process:

Stage 1: Nomination Performance Review

The DNO will notify the FSP where accuracy standards have not been met. The notification will include the identifier for the Meterable Unit(s), the assessment period and, as applicable, the calculated Net % Error and/or Absolute % Error figures.

The FSP may submit additional information to the DNO to provide any mitigation that explains the cause for the accuracy standards not being adhered to. The information shall demonstrate that the FSP was acting in accordance with the principles of good industry practice as defined in this Flexibility Market Rule and, if applicable, details of a reasonably unforeseeable circumstance which caused the accuracy standards to be exceeded.

If the DNO is satisfied that the principles of good industry practice have been followed, then no further action will be taken, and the FSP may continue participating as normal.

Stage 2: Advanced Monitoring Stage

If the DNO is not satisfied that the FSP demonstrated adherence to the principles of good industry practice during the initial stage of the performance review or that there was a reasonably unforeseeable circumstance which caused the accuracy standards to be exceeded, the DNO will place the Meterable Unit under Advanced Monitoring.

During this period, the FSP will be expected to improve both accuracy performance and compliance with the principles of good industry practice, with more frequent reviews (i.e. more frequently than quarterly).

Stage 3: Removal from Flexibility Services

If, during the Advanced Monitoring stage, the FSP continues to fail to meet the required accuracy thresholds and fails to demonstrate any improvement in either performance or alignment with the principles of good industry practice, the DNO may, at their sole discretion, terminate the contract for flexibility services relating to the affected Meterable Unit(s).

## 3. Market Information

### 3.1 Implementation tracking

The DNOs must provide the Market Facilitator with the data set out in Table 9. The data provided should accurately reflect their implementation of the rule.

The expected values required for compliance are also set out in Table 9.

Initial data shall be sent no later than 20 working days after the Published Date of this Flexibility Market Rule.

Updates shall be sent as soon as reasonably practical, and no later than 10 working days after any changes to the values.

Elexon reserves the right to publish this data within its Implementation Tracker.

**Table 9: Implementation tracking requirements**

| Parameter | Required value (per Sub-Market) |
|---|---|
| Implementation Status | Dependent on date:<br>Before Implementation Date: Not yet started, Implementing, Paused, Implemented<br>Between Implementation Date and End Date: Implemented<br>After End Date: Superseded |
| Target Implementation Date | No later than Implementation Date |

*[The header row of this table begins with the reference FMR-SBM in the source.]*

### 3.2 Flexibility Market Catalogue data

The DNOs must update the Market Facilitator with the data set out in Table 10 below for each Sub-Market in scope of this Flexibility Market Rule. This should accurately reflect their implementation of each Sub-Market.

The expected values required for compliance are also set out in Table 10.

Initial data shall be sent no later than the Implementation Date of this Flexibility Market Rule.

Updates shall be sent as soon as reasonably practical, and no later than 10 working days after any changes to the values.

DNOs shall also publish this information themselves.

Elexon reserves the right to publish this data within its Flexibility Market Catalogue.

**Table 10: Flexibility Market Catalogue data**

| Parameter | Description | Required Value |
|---|---|---|
| Baselining | Summary of the baselining approach used | As per Standard Baselining Methodology |
| Maximum allowable Net % error for nomination baselines | Maximum error allowed in the Accuracy methodology before performance reviews are kicked off | 10% |
| Maximum allowable Absolute % error for nomination baselines | Maximum error allowed in the Accuracy methodology before performance reviews are kicked off | 20% |

#### Comment

This section is provided as guidance to the Flexibility Market Rule. Therefore, it is not legally binding and falls outside of the formal change management process.

We acknowledge there is overlap between the first parameter and that set out in “Sub-Market Definition” Flexibility Market Rule (FMR-SMD) We will look to review this and remove duplication in due course. In the meantime, DNOs are expected to copy the definition data between both rules.

### 3.3 Effectiveness monitoring

The following metrics shall be used to assess the effectiveness of the rule.

The DNOs must provide the Market Facilitator with any Additional Input Data as set out in Table 11 below for element in scope of this rule. The data provided should accurately reflect their implementation of the rule.

The expected values and the minimum required values for compliance, if any, are also set out in Table 11.

Initial Additional Input Data shall be sent as reasonably practical following the first quarter of implementation of this Flexibility Market Rule.

Additional Input Data shall be sent in accordance with the Cadence set out in Table 11.

Updates to Additional Input Data shall be sent as soon as reasonably practical, and no later than 10 working days after any changes to the values.

Elexon reserves the right to publish this data within its Implementation Tracker.

**Table 11: Effectiveness monitoring metrics** 
| Field | Metric 1 | Metric 2 | Metric 3 | Metric 4 |
|---|---|---|---|---|
| Description | Number of ABM requests approved | Average Nomination Baselining Net % Error for a Meterable Unit | Average Nomination Baselining Absolute % Error for a Meterable Unit | Number of Nomination Performance Reviews |
| Why are we tracking this? | To validate the effectiveness of the DBM. A high volume of ABM requests could highlight an issue with a particular DBM(s) that would require further analysis and potential amendment in a subsequent version of this rule. | To validate the effectiveness of the Nomination Baseline calculation by an FSP for a Meterable Unit. A high Net % Error figure could highlight an issue with a particular FSP or Meterable Unit in their procedures for determining a Nomination Baseline.<br>It will also be used to determine if the limits, as specified in Table 12 are at the correct level. This would inform further analysis and potential amendment in a subsequent version of this rule. | To validate the effectiveness of the Nomination Baseline calculation by an FSP for a Meterable Unit. A high Absolute % Error figure could highlight an issue with a particular FSP or Meterable Unit in their procedures for determining a Nomination Baseline.<br>It will also be used to determine if the limits, as specified in Table 12 are at the correct level. This would inform further analysis and potential amendment in a subsequent version of this rule. | To validate the effectiveness of the Nomination Baseline procedures of an FSP. A high number of reviews could highlight an issue with a particular FSP or Meterable Unit in their procedures for determining a Nomination Baseline. |
| Cadence | Quarterly | Quarterly | Quarterly | Quarterly |
| Data Source | Existing Data -<br>Additional Input Data – Number of ABM requests approved in the last quarter | Existing Data -<br>Additional Input Data – Average (monthly) Net % Error figures per Meterable Unit over the last quarter | Existing Data -<br>Additional Input Data – Average (monthly) Absolute % Error figures per Meterable Unit over the last quarter | Existing Data -<br>Additional Input Data – Number of Nomination Performance Reviews in the last quarter |
| What does good look like? | Low volumes | Low percentage | Low percentage | Low volumes |
| Minimum Requirement |  |  |  |  |

## 4. Glossary

The following definitions are specific to this Flexibility Market Rule. These are supplemented by the definitions in the Market Facilitator Glossary. If there is an inconsistency between definitions, the definition in this document shall prevail.

| Term | Meaning |
|---|---|
| Absolute % Error. | Means, over an assessment period, the calculated average absolute error of a Meterable Unit. |
| Alternative Baselining Methodology (ABM) | Means a non-DBM baselining approach where the applicable DBM is not suitable due to the DER having atypical characteristics or operational behaviours. |
| Asset Capacity | Means a baselining technique which assumes the participating DER operates at its full rated capacity during the flexibility event, irrespective of actual operational conditions. |
| Confirmed Baselining Methodology (CBM) | Means the baselining methodology that will be utilised in the assessment of the performance of the DER. This will either be the relevant DBM, or, where approved by the DNO, the ABM. |
| Distributed Energy Resource (DER) | Means energy resources comprised of generation and/or storage and/or controllable load, which is connected at the low or medium voltage distribution level. |
| Default Baselining Methodology (DBM) | Means the baselining methodology that should be applied based on the Location Type, Metering Location, Technology Type and direction of the service (i.e. DTD/GTU or DTU/GTD). |
| Event Days | Means a day that can be excluded from a Recent History baseline methodology for activities such as delivery of Balancing Services, Virtual Trading, Site Outage, Equipment and/or Site Disconnection occurring on that day. |
| Fixed Reference | Means a baselining technique which uses a fixed daily profile derived from the observed energy behaviour of a representative group of DERs that represents normal operating behaviour or a DNO’s planning scenarios. |
| Location Type | Means either a domestic premise or an Industrial & Commercial (I&C) premise. |
| Meterable Unit | Means an aggregated collection of DERs, or a single DER, that are either all a non-Nomination DBM or all a Nomination DBM. |
| Metering Location | Means a location for the metering either at the Point of Connection to the Distribution System (i.e. the Boundary Point Metering System) or a behind the Boundary Point Metering System located at the asset providing the flexibility service. |
| Net % Error | Means, over an assessment period, the calculated average net error of a Meterable Unit. A negative net error indicates Nominations are higher than the Meterable Unit’s normal behaviour, while a positive error indicates the Nominations are under the Meterable Unit’s normal behaviour. |
| Nomination | Means a baselining technique which uses an estimated/expected set of meter values, provided by the Flexibility Services Provider (FSP), based on the expected or normal operation of the site / DER without any flexibility event, for a future availability window that then becomes a utilisation event. |
| Recent History | Means a baselining technique which uses a set of recent, eligible days (i.e. excluding Event Days such as a day providing a flexibility service) preceding a utilisation event. This may also include correction factors such as within-day adjustments for weather variables or removal of outlier values. |
| Technology Type | Means the type of Distributed Energy Resource (DER) which is the asset providing the flexibility service. For example, an EV Charger. |
| Zero | Means a baselining technique where the baseline energy consumption or generation is set to zero, meaning no energy usage or production is assumed in the absence of the utilisation event. |

---

# Part B – FMR-VSM: Verification & Settlement Methodology (extract; identical to FMR-VSM V2.3 from section 2.1)

## 2. Verification and Settlement requirements

### 2.1 Verification and settlement process

The verification and settlement process shall repeat monthly, and follow the process set out in Figure 1 below.

two options are available, for either a Self-billing or invoicing process.

*[Diagram/image in the original web page was not captured in the copy-paste.]*

Figure 1: Verification and Settlement Process

Exact dates will vary by DNO.

### 2.2 Overview of the Verification and Settlement Methodology

Calculation of Charges

There are two types of Flexibility Services payments: Utilisation Payments and Availability Payments. The application of the payment type depends on the Flexibility Service product being delivered.

Utilisation Payments are made when a Utilisation Instruction is issued by the Company. Utilisation Payments are considered in terms of:

for every metered time period, energy delivered (MWh), supplied by the Provider and multiplied by the Utilisation Fee (£/MWh);

or (for the Peak Reduction product)

the capacity (MW) delivered multiplied by the Utilisation Fee (£/MW) over a period-of-time.

Where the Provider has not fully met the volume of the Utilisation Instruction, a Performance Multiplier is applied to determine Utilisation Performance and how much delivery is eligible for payment.

The Company shall calculate Utilisation Performance for each of the flexibility products it procures with the factors set out via the Sub-Market definitions in section 4;

Availability Payments

Where Availability is applicable to a flexibility service, payments are paid for every Accepted Availability Window in respect of the contracted DER. Availability Payments are subject to a Monthly Utilisation Performance Factor.

Availability is determined by:

for every metered time period, the Agreed Availability Capacity (MW) multiplied by the Availability Fee.

Where a Service Provider declares Unavailability, or was not Available at the time of delivery, then no Availability Payment will be made for that metered time period.

Availability Performance is calculated monthly, and Availability Payments are recovered should the delivered capacity be lower than the agreed delivery capacity. To determine the recovery, the Provider’s calculated Monthly Utilisation Performance Factor is applied to the Availability Payment.

### 2.3 Detailed Methodology

*[Editorial: the equations in this section were rendered as maths markup on the web page, and the copy-paste broke them into single characters. They have been rebuilt below in plain linear notation. X[a,b] means X with subscripts/superscripts a and b; Σ_{j=1..t} means the sum from j = 1 to t. Variable definitions are shown in bold.]*

#### 2.3.1 Signage used in calculations

The signage used in calculations shall be as in Table 2: below

**Table 2: Signage for Settlement Calculations**

| Response Type | Direction | Baseline Value | Meter Readings | Dispatched Capacity |
|---|---|---|---|---|
| Demand | Turn Down | Negative | Negative | Positive |
| Demand | Turn Up | Negative | Negative | Negative |
| Generation | Turn Down | Positive | Positive | Negative |
| Generation | Turn Up | Positive | Positive | Positive |

#### 2.3.2 Payment Calculations for Turnup/Turndown Services

##### 2.3.2.1 Availability Payments

Where the contracted Flexibility Service includes Availability, payments are applicable to the FSP in respect of Accepted Availability Windows, whereby the FSP is ready and available to supply the Utilised MW in the event of a Utilisation Instruction.

When applicable, Availability will be calculated, based on performance on a minute or 30-minute granularity. The Availability Payment due is subject to Utilisation Performance and a Grace Factor can be applied at the Company’s discretion to calculate the total Availability Percentage due.

Utilisation Performance is calculated as an average across the Utilisation Events within month, as detailed in section 2.3.2.2 of this document. Where a grace factor is applied to this average, the Company may pay up to 100% of availability for the month where average delivery falls within the grace factor band. For example, if the Grace Factor is defined as 5%, and Utilisation Performance is determined to be 95% then 100% of the Availability Payment is due.

If there are no utilisation events in the month then full availability is paid.

The parameters to calculate the Availability Payments are detailed below. There are two examples shown, minute by minute and 30-minute granularity. The calculations are the same in both instances however minute by minute granularity would allow the MW or price to change (if needed) on a greater granularity level than 30-minute granularity

**Table 3: Parameters used in Availability Calculations**

| ID | Parameter | Description | Example 1, 1 minute granularity | Example 2, 30-minute granularity |
|---|---|---|---|---|
| A | Start Datetime | Start date and time of the Accepted Availability Window | 01/07/23 00:00 | 01/07/23 00:00 |
| B | End Datetime | End date and time of the Accepted Availability Window | 01/07/23 00:01 | 01/07/23 00:30 |
| C | Metered Time Period (minutes/60) | The Metered Time Period divided by sixty. In the datetime in example one the period is 1 minute so 1/60, while in example 2 the period is 30 minutes. | 0.016666667 | 0.5 |
| D | Availability Price £/MW/h | The contracted fee for the availability component of the service in £/MW/h | £2 | £2 |
| E | Contracted Capacity (MW) | The Available MW the service provider has been accepted to supply | 5 | 5 |
| F | Availability (1,0) | 1 if the service was available, 0 if not available for the period | 1 | 1 |
| G | Grace Factor | Availability Grace Factor | 5% | 5% |
| H | Utilisation Performance | The calculated Utilisation Performance taking into account the Grace Factor in G. | 85.33% | 100%a |
| I | Pre-Utilisation Performance Payment £ | The payment for the availability period without any performance applied Using the data above the value shown in the next columns is calculated by (C*D*E*F) | £0.17 | £5.00 |
| J | Post-Utilisation Performance Payment | The actual Availability payment value using the applied performance %, values calculated by (C*D*E*F*H) | £0.14 | £5.00 |

**Detailed Availability Formula**

The Availability Payment (AP[s,m]), to be made by The Company to the Flexibility Service Provider in respect of the Accepted Availability Window(s) in calendar month, m, for Flexible Unit, s, shall be calculated in accordance with the following formula:

```
AP[s,m] = Σ_{j=1..t} AC[s,j] × AVP[s,j] × CC[s,j] × SA[s,j] × MPF[s,m]
```

t represents the number of Metered Time Periods

**AC[s,j]** in respect of each Flexible Unit, s, and each Metered Time Period, j, means the Availability Price in £/MW/h.

**AVP[s,j]** in respect of each Flexible Unit, s, and each Metered Time Period, j, means the Availability Period in minutes/60.

**CC[s,j]** in respect of each Flexible Unit, s, and each Metered Time Period, j, means the Contracted Capacity in MW

**SA[s,j]** in respect of each Flexible Unit, s, and each Metered Time Period, j, is 0 where the Flexible Unit is declared (or redeclared) unavailable or The Company deem unavailable, otherwise 1.

**MPF[s,m]** in respect of each Flexible Unit, s, and each calendar month, m, means the Monthly Utilisation Performance Factor and is 1 where:

there are no Dispatch Events in a month.

the Monthly Utilisation Performance Factor is not being applied by The Company.

the calculated Monthly Utilisation Performance Factor is 100% or within the Grace Factor applied by The Company.

otherwise, is calculated using the formula below:

For a Flexible Unit, s, for each calendar month, m:

```
MPF[s,m] = (1/p) × Σ_{e=1..p} [ (1/n) × Σ_{k=1..n} Max( Min( (MM[e,k] − BM[e,k]) / DC[e,k] , 1 ) , 0 ) ]
```

**BM[e,k]** in respect of each Dispatch Event, e, and each Minute, k, BM[e,k] represents the Baseline MW with the signage negative for a demand unit and positive for a generation unit.

**MM[e,k]** in respect of each Dispatch Event, e, and each Minute, k, MM[e,k] represents the Metered MW with the signage negative for a demand unit and positive for a generation unit.

**DC[e,k]** in respect of each Dispatch Event, e, and each Minute, k, DC[e,k] represents the Dispatched MW with the signage positive for a demand reducing asset or a generation increase asset and the signage negative for a demand increasing asset or generation reducing asset.

n represents the number of minutes for each Dispatch Event

p represents the number of Dispatch Events in a calendar month for a Flexible Unit

##### 2.3.2.2 Utilisation Payments

Utilisation payments are paid to the FSP for the energy delivered during a Utilisation Event.

Utilisation will be calculated, if applicable, on a minute granularity, the payment is subject to a performance metric known as a Performance Multiplier which applies after, if applicable, a Grace Factor.

The parameters to calculate the Utilisation Payments are detailed in Table 4. Two examples are detailed a Demand turndown asset and a Generation turnup asset, note the signage used differs dependent on asset type and is shown in Table 4.

**Table 4: Parameters used in Utilisation Calculations**

| ID | Parameter | Description | Example 1, 1 minute granularity Demand Reducer | Example 2, 1 minute granularity Generation Increase |
|---|---|---|---|---|
| A | Start Datetime | Start date and time of the Utilisation Event | 01/07/23 00:00 | 01/07/23 00:00 |
| B | End Datetime | End date and time of the Utilisation Event | 01/07/23 00:01 | 01/07/23 00:01 |
| C | Dispatched Capacity (MW) | The Utilisation MW instructed. | 5 | 5 |
| D | Utilisation Price £/MWh | The contracted fee for the utilisation component of the service in £/MWh | £25 | £25 |
| E | Utilisation Period (minutes/60) | The duration of the Utilisation Event divided by sixty. | 0.016666667 | 0.016666667 |
| F | Baseline (MW) | The baseline of the asset in the minute in question. | -5 | 10 |
| G | Metered (MW) | The actual Metered MW of the asset in the minute in question. | -0.712 | 14 |
| H | Delivered (MW) | The actual delivered MW of the asset in the minute in question. Calculated by G-F | 4.288 | 4 |
| I | Delivery Percentageb | The actual delivery percentage in the minute in question, calculated by H/C | 85.76% | 80% |
| J | Grace Factorc | A utilisation Grace Factor applied to the MW delivered, if the delivered % is within this tolerance then full payment is made for the minute in question. | 5% | 5% |
| K | Performance Multiplierd | If the delivery % is outside the Grace Factor, then a Performance Multiplier is applied to reduce the % paid. | 3 | 3 |
| L | Payment Percentage | The percentage calculated for payment considering the Grace Factor and penalisation multiplier for the minute in question | 67.28% | 50% |
| M | Utilisation Payment (£) | The actual Utilisation Payment value for the minute in question considering the applied performance % calculated by (D*E*C*L) | £1.40 | £1.04 |

**Detailed Utilisation Formula**

The Utilisation Payment (UP[s,m]), made by The Company to the Flexibility Service Provider in respect of the Utilisation Events(s) in calendar month, m, for Flexible Unit, s, shall be calculated in accordance with the following formula:

```
UP[s,m] = Σ_{j=1..t} UF[s,j] × UVP[s,j] × UC[s,j] × PM[s,j]
```

t represents the number of Metered Time Periods

**UF[s,j]** in respect of each Flexible Unit, s, and each Metered Time Period, j, means the Utilisation Price in £/MWh.

**UVP[s,j]** in respect of each Flexible Unit, s, and each Metered Time Period, j, means the Utilisation Period in minutes/60.

**UC[s,j]** in respect of each Flexible Unit, s, for each Metered Time Period, j, means the delivered/utilised MW calculated as below:

```
UC[s,j] = MAX( MAX( MIN( (MM[s,j] − BM[s,j]) / DC[s,j] , POD[s,j] ) , 0 ) * |DC[s,j]| , |DC[s,j]| )

[Editorial: nesting inferred from the order of the symbols in the source:
 MAX(  MAX MIN  (MM[s,j] − BM[s,j]) / DC[s,j] ,  POD[s,j] ,  0  *  |DC[s,j]|  ,  |DC[s,j]|  )
 Read literally, the result could never be below |DC[s,j]|, which does not fit the
 stated purpose (delivered/utilised MW). Check the original equation before relying on it.]
```

**BM[s,j]** in respect of each Flexible Unit, s, and each Metered Time Period, j, BM[s,j] represents the Baseline MW with the signage negative for a demand unit and positive for a generation unit.

**MM[s,j]** in respect of each Flexible Unit, s, and each Metered Time Period, j, MM[s,j] represents the Metered MW with the signage negative for a demand unit and positive for a generation unit.

**DC[s,j]** in respect of each Flexible Unit, s, and each Metered Time Period, j, DC[s,j] represents the Utilised MW with the signage positive for a demand reducing asset or a generation increase asset and the signage negative for a demand increasing asset or generation reducing asset.

**POD[s,j]** in respect of each Flexible Unit, s, and each Metered Time Period, j, POD[s,j] represents Payable Over Delivery, the percentage over delivery beyond 100% for which remuneration will be allowed. A POD value of 1 will not allow payment for any over delivery whilst a POD value of 1.1 will allow payment for up to 10% over delivery.

**PM[s,j]** in respect of each Flexible Unit, s, for each Metered Time Period, j, means Performance Multiplier calculated using the formula below:

```
PM[s,j] = IF( Delivery% ≥ 1 − GraceFactor , 1 , MAX( 0 , (1 − GraceFactor) − ((1 − GraceFactor) − Delivery%) * Mutiplier% * 100 ) )

[Editorial: 'Mutiplier%' sic. Parentheses inferred from the symbol order. The worked examples in Table 4
 (85.76% delivery, 5% Grace Factor, multiplier 3 -> 67.28%; 80% -> 50%) fit
 PM = MAX(0, (1 − GraceFactor) − ((1 − GraceFactor) − Delivery%) × Multiplier) whenever Delivery% < 1 − GraceFactor.]
```

Delivery% in respect of each Flexible Unit, s, for each Metered Time Period, j, means the actual MW delivered divided by the dispatched MW expressed as a percentage.

GraceFactor: in respect of each Flexible Unit, s, for each Metered Time Period, j, represents the percentage of under delivery below 100% for which renumeration of 100% will be applied.

Multiplier%: in respect of each Flexible Unit, s, for each Metered Time Period, j, represents a multiplier applied to under delivery expressed as a percentage.

#### 2.3.3 Payment Calculations for Peak Reduction Services

**Utilisation Calculations**

Flexibility providers commit to reduce their highest demand peaks during pre-contracted windows. Payments are for utilisation only.

**Detailed Utilisation Formula**

The Utilisation Payment (SP[s,m]), made by The Company to the Flexibility Service Provider in respect of a calendar month, m, for Flexible Unit, s, shall be calculated in accordance with the following formula:

```
SP[s,m] = CC[s] × UF[s] × H[s,m] × PM[s,m]
```

**CC[s]** in respect of each Flexible Unit, s, means the Contracted Capacity in MW.

**H[s,m]** in respect of each Flexible Unit, s, and month, m, means the number of service hours awarded in the month in hours.

**UF[s]** in respect of each Flexible Unit, s, means the Utilisation Fee in £/MW/h

**PM[s,m]** in respect of each Flexible Unit, s, for each Month, m, means Performance Multiplier calculated using the formula below:

```
PM[s,m] = IF( Delivery% ≥ 1 − GraceFactor , 1 , MAX( 0 , (1 − GraceFactor) − ((1 − GraceFactor) − Delivery%) * Multiplier% * 100 ) )

[Editorial: parentheses inferred from the symbol order; see the note on PM[s,j] above.]
```

GraceFactor: in respect of each Flexible Unit, s, for each month, represents the percentage of under delivery below 100% for which renumeration of 100% will be applied.

Multiplier%: in respect of each Flexible Unit, s, for each month, j, represents a multiplier applied to under delivery expressed as a percentage.

Delivery% in respect of each Flexible Unit, s, and month, m, is calculated as below:

```
Delivery% = [ Min( MM[s,j], MM[s,j+1], …, MM[s,j+n] ) − Min( BM[s,j], BM[s,j+1], …, BM[s,j+n] ) ] / CC[s,m]
```

**BM[s,j]** in respect of each Flexible Unit, s, and each Settlement Period, j, BM[s,j] represents the Baseline MW with the signage negative for a demand unit and positive for a generation unit.

**MM[s,j]** in respect of each Flexible Unit, s, and each Settlement Period, j, MM[s,j] represents the Metered MW with the signage negative for a demand unit and positive for a generation unit.

**CC[s,m]** in respect of each Flexible Unit, s, and each Month, m, CC[s,m] represents the Contracted MW with the signage positive for a demand reducing asset or a generation increase asset and the signage negative for a demand increasing asset or generation reducing asset.

n represents the number of dispatched settlement periods

#### 2.3.4 Further Information

The table below shows the impact on Utilisation Payments when there is less than 100% delivery. The table shows a Grace Factor of 5% and a Performance Multiplier of 3 and as can be seen (final column) the payable delivery tapers away to zero once the delivery percentage hits 63%.

**Table 5: Impact on payment with changing delivery percentage (Turnup/Turndown Service)**

| Delivery % | Grace Factor | Performance Multiplier | Calculated Payment % after Grace Factor and Multiplier |
|---|---|---|---|
| 100% | 5% | 3 | 100% |
| 99% | 5% | 3 | 100% |
| 98% | 5% | 3 | 100% |
| 97% | 5% | 3 | 100% |
| 96% | 5% | 3 | 100% |
| 95% | 5% | 3 | 100% |
| 94% | 5% | 3 | 92% |
| 93% | 5% | 3 | 89% |
| 92% | 5% | 3 | 86% |
| 91% | 5% | 3 | 83% |
| 90% | 5% | 3 | 80% |
| 89% | 5% | 3 | 77% |
| 88% | 5% | 3 | 74% |
| 87% | 5% | 3 | 71% |
| 86% | 5% | 3 | 68% |
| 85% | 5% | 3 | 65% |
| 84% | 5% | 3 | 62% |
| 83% | 5% | 3 | 59% |
| 82% | 5% | 3 | 56% |
| 81% | 5% | 3 | 53% |
| 80% | 5% | 3 | 50% |
| 79% | 5% | 3 | 47% |
| 78% | 5% | 3 | 44% |
| 77% | 5% | 3 | 41% |
| 76% | 5% | 3 | 38% |
| 75% | 5% | 3 | 35% |
| 74% | 5% | 3 | 32% |
| 73% | 5% | 3 | 29% |
| 72% | 5% | 3 | 26% |
| 71% | 5% | 3 | 23% |
| 70% | 5% | 3 | 20% |
| 69% | 5% | 3 | 17% |
| 68% | 5% | 3 | 14% |
| 67% | 5% | 3 | 11% |
| 66% | 5% | 3 | 8% |
| 65% | 5% | 3 | 5% |
| 64% | 5% | 3 | 2% |
| 63% | 5% | 3 | 0% |
| 62% | 5% | 3 | 0% |
| 61% | 5% | 3 | 0% |
| 60% | 5% | 3 | 0% |
| 59% | 5% | 3 | 0% |
| 58% | 5% | 3 | 0% |
| 57% | 5% | 3 | 0% |
| 56% | 5% | 3 | 0% |
| 55% | 5% | 3 | 0% |
| 54% | 5% | 3 | 0% |
| 53% | 5% | 3 | 0% |
| 52% | 5% | 3 | 0% |
| 51% | 5% | 3 | 0% |
| 50% | 5% | 3 | 0% |

Figure 2: Indicative Visual representation Impact on payment with changing delivery percentage (Turnup/Turndown)

### 2.4 Required Factors

The required factors for the various DNO products are set out in Table 6 below.

**Table 6: Required factors for the verification and settlement methodology** 
| Parameter | Peak Reduction (PR) | Scheduled Utilisation (SU) | Scheduled Availability, Operational Utilisation (SAOU) | Variable Availability, Operational Utilisation (VAOU) | Operational Utilisation (OU) |
|---|---|---|---|---|---|
| Utilisation Grace Factor | 5% | 5% | 5% | 5% | 10% |
| Availability Grace Factor | N/A | N/A | 5% | 5% | N/A |
| Performance Multiplier | 3 | 3 | 3 | 3 | 2 |
| Payable Over-delivery | 0 | 0 | 0 | 0 | 0 |

The factors used by DNOs shall be provided to the market facilitator as per section 3. These will be published in the Flexibility Market Catalogue

### 2.5 Performance Data Feedback

Performance report/Initial Statements provided by DNOs should be accompanied by the following details:   (a) The period(s) during which the Flexibility Services were made available to the Company and, if applicable, where utilised;

(b) Availability charges (if any), reflecting any reduction for periods of where the service was unavailable or had reduced capacity;

(c) Utilisation charges (if any) reflecting any reductions for periods of where the service was unavailable or reduced, including any utilisation payment cap;

(d) Summary of the relevant Charges (if any); and

(e) The event and zone/service the performance data relates to.

## 3. Market Information

### 3.1 Implementation tracking

The DNOs must provide the Market Facilitator with the data set out in Table 7 for each Sub-Market in scope of this Flexibility Market Rule. The data provided should accurately reflect their implementation of the rule within each Sub-Market.

The expected values required for compliance are also set out in Table 7.

Initial data shall be sent no later than 20 working days after the Published Date of this Flexibility Market Rule.

Updates shall be sent as soon as reasonably practical, and no later than 10 working days after any changes to the values.

Elexon reserves the right to publish this data within its Implementation Tracker.

**Table 7: Implementation tracking requirements**

| Parameter | Required value (per Sub-Market) |
|---|---|
| Implementation Status | Dependent on date:<br>Before Implementation Date: Not yet started, Implementing, Paused, Implemented<br>Between Implementation Date and End Date: Implemented<br>After End Date: Superseded |
| Target Implementation Date | No later than Implementation Date |

*[The header row of this table begins with 'FMR-MRS Version 1.0' in the source.]*

### 3.2 Flexibility Market Catalogue data

The DNOs must update the Market Facilitator with the data set out in Table 8 below for each Sub-Market in scope of this rule. This should accurately reflect their implementation of each Sub-Market.

The expected values required for compliance are also set out in Table 8.

Initial data shall be sent no later than the Implementation Date of this Flexibility Market Rule.

Updates shall be sent as soon as reasonably practical, and no later than 10 working days after any changes to the values.

DNOs shall also publish this information themselves.

Elexon reserves the right to publish this data within its Flexibility Market Catalogue.

**Table 8: Sub-Market definitions**

| Parameter | Description | Required Values |
|---|---|---|
| Verification and Settlement Cycle | How often is the verification and settlement process run | Monthly |
| Settlement Process | Which type of settlement process is being used. | Self-billing/ Invoicing |
| Utilisation Grace Factor | the percentage of under delivery below 100% for which renumeration of 100% will be applied, relevant both to utilisation | As per Table 6 |
| Availability Grace Factor | the percentage of under delivery below 100% for which renumeration of 100% will be applied, relevant both to availability | As per Table 6 |
| Performance Multiplier | If the delivery % is outside the Grace Factor, then a Performance Multiplier is applied to reduce the percentage paid. | As per Table 6 |
| Payable Over-delivery | The volume of over-delivery that will be paid | As per Table 6 |

### 3.3 Effectiveness monitoring

There are no market facilitator metrics for this rule

## 4. Glossary

The following definitions are specific to this Flexibility Market Rule. These are supplemented by the definitions in the Market Facilitator Glossary. If there is an inconsistency between definitions, the definition in this document shall prevail.

| Term | Meaning |
|---|---|
| Accepted Availability Window | means a Committed Availability Window in respect of a Flexible Unit which is notified by the Company in the form of an award as being required by the Company for the Company's Flexibility Services; |
| Availability Payment | payment made by the Company to a Flexibility Service Provider for the period the Flexibility Service Provider was awarded an Availability Window; |
| Availability Percentage | means the calculated percentage of monthly Availability Payment due, following the application of Utilisation Performance and any applicable availability Grace Factor; |
| Availability Price | means the contracted fee £/MW/h in respect of availability; |
| Availability Performance | the overall monthly utilisation delivery performance calculated as a percentage for application to all availability payments at the point of invoicing; |
| Availability Refinement Period | the period defined within the flexibility service parameters where a refinement of the availability window and capacity is agreed; |
| Available MW | means the MW value the Company has awarded the FSP within an Accepted Availability Window; |
| Baseline MW | means the baseline value of the Flexible Unit at the minute in question. A Demand asset is represented by a negative number with a generation asset a positive number; |
| The Company | means the Licensee with whom the FSP is contracted to provide flexibility services; |
| Contracted Capacity | means the target net MW of Demand Response in respect of an awarded Service Window, confirmed to the FSP at time of award or following a refinement window (if applicable for the contracted flexibility service); |
| Delivered MW | means the MW value calculated as delivered following the application of the Baseline MW to the Metered MW; |
| Flexible Unit | means one or more Energy Resources that are aggregated, regarded as a single entity, and metered on a single metering output and, as such, is providing a flexibility service; |
| Grace Factor | the percentage of under delivery below 100% for which renumeration of 100% will be applied, relevant both to utilisation and availability performance at the Company’s discretion; |
| Metered MW | means the actual metered MW value of the Flexible Unit at the minute in question. A Demand asset is represented by a negative number with a generation asset a positive number; |
| Metered Time Period | the time period used in the payment calculations, this will either be minute by minute or 30-minute granularity; |
| Peak Reduction Service | a flexibility service where FSPs commit to reduce their highest demand peaks during pre-contracted windows; |
| Turnup/Turndown Service | flexibility services that require FSPs to change their energy import or export behaviour during pre-scheduled windows or in response to a Utilisation Instruction; |
| Utilisation Event or Utilisation Period | means a utilisation request to deliver flexibility services, inclusive of a specified start and end time; |
| Utilisation Instruction | means an instruction by the Company to the FSP to deliver Flexibility Services; |
| Utilisation Payment | the amount payable by the Company to the Provider for the utilisation of any Flexibility Service; |
| Utilisation Performance | means the calculated performance per utilisation event after any factors have been applied; |
| Utilisation Price | means the contracted fee £/MWh in respect of utilisation; |
| Utilised MW | means the MW value instructed within a Utilisation Event; (Represented by a positive number for a demand reducer / generation increase asset and a negative number for a demand increase/generation reduction asset; |
| Performance Multiplier | the factor by which any percentage of under delivery below the grace factor will be multiplied by in order to calculate payable delivery; |

---

# Part C – FMR-PQC: Pre-Qualification Criteria Flexibility Market Rule (extract)

## 2. Pre-Qualification Criteria

### 2.1 Commercial Qualification Criteria

The below tables present the standard commercial and technical qualification criteria that System Operators must use when assessing Flexibility Service Providers (FSPs) for entry into their local flexibility markets. Their purpose is to:

- Standardise the commercial and technical information required across all System Operators, ensuring consistency in onboarding processes.
- Reduce complexity and duplication for FSPs who engage with multiple System Operators by aligning the questions asked during pre-qualification.
- Define pass criteria for each question, clarifying what constitutes a complete or acceptable response.
- Support transparency and comparability by documenting the exact fields, allowable responses, and expectations.

The 31 standard questions are laid out in Table 2 below

**Table 2: Standard Commercial Qualification Criteria**  *[Table rebuilt from a flattened copy-paste. Each row is anchored on its Field Name code. The other cells (Area / Commercial Qualification Questions / Allowable Responses / Pass Criteria / Description) are given in source order, separated by ‖, because the cell boundaries and the merged Area cells could not be recovered reliably. A short fragment at the end of a row may belong to the next row's Area label, or may continue that row's text.]* 
| Field Name | Row content in source order |
|---|---|
| COMM_REF_ORG1 | Reference ‖ Assigned Reference for this Organisation, if known ‖ free text ‖ completed ‖ If the Organisation has previously been submitted and assigned a reference, this can be detailed here ‖ Company Information |
| COMM_CI_CNAME | Registered or legal name of the contracting party ‖ free text ‖ completed ‖ Full registered/legal name of the party wishing to enter into the flexibility contract |
| COMM_CI_REGNO | Company Registered Number [Or Charity/Trust] ‖ free text ‖ completed ‖ Registered No. as shown on Companies House. Charity or Trust Registration No. is also acceptable |
| COMM_CI_REGA1 | Registered address 1 ‖ free text ‖ completed ‖ Registered Address line 1 |
| COMM_CI_REGA2 | Registered address 2 ‖ free text ‖ completed ‖ Registered Address line 2 |
| COMM_CI_REGA3 | Registered address 3 ‖ free text, ‖ blank ‖ completed, ‖ blank ‖ Registered Address line 3 |
| COMM_CI_POSTC | Registered address postcode ‖ free text ‖ completed ‖ Registered Address Postcode |
| COMM_CI_FIRST | Key contact First Name ‖ free text ‖ completed ‖ First name of main contact in respect of this submission and any subsequent contract |
| COMM_CI_CLAST | Key contact Last Name ‖ free text ‖ completed ‖ Last name of main contact in respect of this submission and ‖ any subsequent contract |
| COMM_CI_EMAIL | Key contact email ‖ free text ‖ completed ‖ email address of main contact in respect of this submission and any subsequent contract |
| COMM_CI_TELNO | Key contact number ‖ free text ‖ completed ‖ Contact telephone number of main contact in respect of this submission and any subsequent contract |
| COMM_CI_WEBSI | Organisation website ‖ free text ‖ completed ‖ Web address for contracting party |
| COMM_CI_RELAT | Legal relationship with flexibility asset/s ‖ Owner, Operator, ‖ Aggregator ‖ one code completed ‖ declare relationship to asset/s, only select one |
| COMM_CI_VATNO | VAT Registration Number ‖ free text ‖ completed ‖ VRN of the contracting party ‖ Terms and Conditions |
| COMM_TC_ACCEP | Confirm; You have read the applicable Contractual requirements and understand it will be a requirement to accept these terms in order to form any contract for the delivery of flexibility services ‖ Y, N ‖ Y ‖ Contracting party must confirm their acceptance of the Contractual requirements applicable to the DNO they are pre-qualifying for |
| COMM_TC_DECLA | Do you declare that you have the authority to submit this application and by confirming you declare that to the best of your knowledge, the information ‖ in this form is accurate? ‖ Y, N ‖ Y ‖ The individual completing this submission must have the authority of the contracting party to both accept the Agreement and provide the information listed in this application ‖ Due Diligence |
| COMM_DD_FLEXA | Is the contracting party a member of Flex Assure Code of Conduct? ‖ Y, N ‖ Y, N ‖ Being a member of flex assure is not required in order to pass commercial qualification, if the contracting party is a member it will speed the required due diligence checks |
| COMM_DD_ACHIL | Contracting parties Achilles UVDB Registered No. if applicable ‖ free text, blank ‖ completed, blank ‖ Being Achilles UVDB (Utilities Vendor Database) registered is not required in order to pass commercial qualification, if the contracting party is a member it will speed the required due diligence ‖ and credit checks |
| COMM_DD_CHECK | Where Achilles UVDB registration has not been advised, you understand that the DNO may access the contracting Parties most recent audited financial accounts via Companies House for the ‖ purpose of credit checks. ‖ Y, N, NA ‖ Y, NA ‖ Please confirm you understand that the DNO may perform credit checks as part of their due diligence checks relating to this application |
| COMM_DD_RECEI | Is this contracting party currently, or has it ever been in receivership? ‖ Y, N ‖ N ‖ This response will be assessed by the DNO as part of their due ‖ diligence checks |
| COMM_DD_ADMIN | Is this contracting party currently, or has it ever been in administration? ‖ Y, N ‖ N ‖ This response will be assessed by the DNO as part of their due diligence checks |
| COMM_DD_LIQUI | Is this contracting party currently, or has it ever been in liquidation? ‖ Y, N ‖ N ‖ This response will be assessed by the DNO as part of their due ‖ diligence checks |
| COMM_DD_DEBTS | Is this contracting party currently, or has it ever been unable to pay its debts as they fall due (within the meaning of Section 268 Insolvency Act 1986)? ‖ Y, N ‖ N ‖ This response will be assessed by the DNO as part of their due diligence checks |
| COMM_DD_WINDI | Is this contracting party currently, or has it ever had, in the past 3 years, any petitions for winding up (other than vexatious petitions)? ‖ Y, N ‖ N ‖ This response will be assessed by the DNO as part of their due diligence checks |
| COMM_DD_BANKR | Is this contracting party currently, or has it ever had any petitions for bankruptcy (or their equivalent in the country in which the Applicant is incorporated) within the last three years? ‖ Y, N ‖ N ‖ This response will be assessed by the DNO as part of their due diligence checks |
| COMM_DD_OFFEN | Is this contracting party currently, or has it ever been convicted of any of the offences or has any discretional exclusion occurred, as contained in Regulation 80 of the Utilities Contract Regulations 2016 (UCR), and listed in Regulation 57 (1) and ‖ 57 (8) of the Public Contracts Regulations 2015 (PCR)? [IF IN SCOTLAND, Is this contracting party currently, or has it ever been convicted of any of the offences or has any discretional exclusion occurred, as contained in Regulation 78 of the Utilities Contract (Scotland) Regulations 2016 (UC(S)R), and listed in Regulation 58 of the Public Contracts (Scotland) ‖ Regulations 2015 (PC(S)R)?] ‖ Y, N ‖ N ‖ This response will be assessed by the DNO as part of their due diligence checks |
| COMM_DD_TERMI | Is this contracting party currently, or has it ever had, in the past 3 years, any similar ‖ contracts terminated prematurely and/or had damages claims or other comparable sanctions brought against the contracting party for any significant or persistent deficiencies in performance of a substantive requirement of the ‖ contract? ‖ Y, N ‖ N ‖ This response will be assessed by the DNO as part of their due diligence checks |
| COMM_DD_LITIG | Has the contracting party been subject to any material non- employment related litigation (pending, threatened or determined) or other legal proceedings against the contracting party within the last three years that may be relevant to your ability to deliver services. ‖ Y, N ‖ N ‖ This response will be assessed by the DNO as part of their due diligence checks ‖ Insurance |
| COMM_IN_EMPLO | Does the contracting party have or commit to have Employer’s liability insurance with a minimum limit of £5m ‖ Y, N ‖ Y ‖ Confirm you meet the minimum insurance level required for Employers Liability |
| COMM_IN_PUBLI | Does the contracting party have or commit to have Public liability insurance with a minimum limit ‖ of £5m ‖ Y, N ‖ Y ‖ Confirm you meet the minimum insurance level required for Public Liability |
| COMM_IN_COPIE | Will the contracting party provide copies of such insurances upon request ‖ Y, N ‖ Y ‖ Confirm you will be able to provide copies of insurances if requested by the DNO |

### 2.2 Technical Qualification Criteria

The 35 standard questions are laid out in Table 3 below

**Table 3: Standard Technical Qualification Criteria**  *[Table rebuilt from a flattened copy-paste. Each row is anchored on its Field Name code. The other cells (Area / Technical Qualification Questions / Allowable Responses / Pass criteria / Description) are given in source order, separated by ‖, because the cell boundaries and the merged Area cells could not be recovered reliably. A short fragment at the end of a row may belong to the next row's Area label, or may continue that row's text.]* 
| Field Name | Row content in source order |
|---|---|
| TECH_REF_DER1 | Reference ‖ Assigned Reference for this DER, if known ‖ Free text, NA ‖ Completed ‖ If the DER has previously been submitted and assigned a reference, this can be detailed here ‖ Connection |
| TECH_CN_STATUS | DER Connection status ‖ Archived, Energised, Awaiting Energisation, Planned, Speculative ‖ Energised, Awaiting Energisation ‖ , Planned, Speculative ‖ One eligible response per DER must be provided to confirm the status of the assets connection to the distribution network; Energised means the DER is already connected to the network and is readily available for flexibility, Awaiting Energisation means the connection application and all installation work is complete but the connection is pending energisation therefore the DER is not yet available for flexibility, Planned means a connection application is in progress but no installation work has started and there is no known date for energisation therefore the DER is not yet available for flexibility, Speculative means that the DER is still being sought through recruitment and once recruited will form an aggregated group therefore the DER is not yet available for flexibility. |
| TECH_CN_AWAI1 | If awaiting energisation, firm ‖ date of energisation ‖ DD/MM/YY, ‖ NA ‖ Completed ‖ If the DER is Awaiting Energisation the firm date of energisation must be provided, if energised, planned or speculative please respond NA |
| TECH_CN_AWAI2 | If awaiting energisation, connection reference number ‖ Free text, NA ‖ Completed ‖ If the DER is Awaiting Energisation the connection reference number must be provided, if energised, planned or speculative please respond NA |
| TECH_CN_PLAN1 | If planned, connection voltage level ‖ 0.23, 0.40, ‖ 0.46, 3, 3.3, 6, ‖ 6.6, 7, 11, 13, ‖ 20, 22, 25, 33, ‖ 66, 132, NA ‖ Completed ‖ If the DER is Planned the voltage level at the point at which the DER is connecting onto the distribution network must be provided, if Energised, Awaiting Energisation or Speculative please respond NA |
| TECH_CN_PLAN2 | If planned, connection offer status ‖ Not yet applied, applied awaiting offer, offer issued, offer accepted ‖ Not yet applied, applied awaiting offer, offer issued, offer ‖ accepted ‖ If the DER is Planned the status of the connection application must be stated, if Energised, Awaiting Energisation or Speculative please respond NA |
| TECH_CN_PLAN3 | If planned, connection reference number ‖ Free text, NA ‖ Completed ‖ If the DER is Planned the status of the connection application must be stated, if Energised, Awaiting Energisation or Speculative please respond NA |
| TECH_CN_PLAN4 | If planned, what is the target delivery date? ‖ DD/MM/YY, NA ‖ Completed ‖ If the DER is Planned, the target for delivery/energisation must be stated, if Energised, Awaiting Energisation or Speculative please respond NA |
| TECH_CN_SPEC1 | If speculative, service readiness date ‖ DD/MM/YY, NA ‖ Completed ‖ If the DER is Speculative, the anticipated date the DER or aggregated group or DER will be available to deliver flexibility. If Energised, Awaiting Energisation or Planned please respond NA |
| TECH_CN_SPEC2 | If speculative, recruitment status ‖ ASSET CONTRACTE D, ASSET KNOWN, ASSET UNKNOWN, ‖ NA ‖ Completed ‖ If the DER is Speculative, the status of recruitment must be stated. If Energised, Awaiting Energisation or Planned please respond NA |
| TECH_CN_SPEC3 | CMZ Location, if known ‖ Free text, NA ‖ Completed ‖ If known, the DNO Constraint Management Zone the DER or if speculative, the Aggregated Group of DER, are sited within. Speculative must complete this field with a valid DER ‖ Site/ Location |
| TECH_LN_POSTC | If Energised, Awaiting ‖ Energisation, Planned; Postcode ‖ free text ‖ Completed ‖ The full post code of the site where the DER is located |
| TECH_LN_IMPAN | If Energised, Awaiting Energisation, Planned; Import MPAN (Meter Point Administration Number) If ‖ known ‖ free text (13 Characters), NA ‖ Completed ‖ The unique 13-digit identification of the meter associated with the DER's energy import from the network |
| TECH_LN_EMPAN | If Energised, Awaiting Energisation, Planned; Export MPAN (Meter Point Administration Number) If ‖ known ‖ free text (13 Characters), NA ‖ Completed ‖ The unique 13-digit identification of the meter associated with the DER's energy export to the network |
| TECH_LN_MSID1 | If Energised, Awaiting Energisation, Planned; MSID ‖ (where applicable) ‖ free text, NA ‖ Completed ‖ If applicable, the BSC unique identifier of the meter associated with the DER |
| TECH_LN_ANAME | DER [If Speculative, then Aggregated Group] Name/Ref ‖ free text ‖ Completed ‖ The human readable name the contracting party wishes to name the DER ‖ Technology |
| TECH_TG_GROU1 | Asset Scale ‖ DOMESTIC, ‖ I&C ‖ Completed ‖ Identifies whether the DER is connected at a site that is domestic, or industrial and commercial. |
| TECH_TG_GROU2 | Metering Point ‖ POINT OF CONNECTIO N, ASSET LEVEL ‖ Completed ‖ Describes where the DER is metered. 'Asset Level' means behind the meter and 'Point of Connection' means the connection at the boundary to the network. |
| TECH_TG_GROU3 | DER Type; Generation &/OR Storage ‖ Y, N ‖ Y, N ‖ Identifies if the purpose of the DER is for generation and/storage |
| TECH_TG_GROU4 | DER Type; Demand ‖ Y, N ‖ Y, N ‖ Identifies if the purpose of the DER is for demand flexibility |
| TECH_TG_GSCL1 | If Generation &/OR Storage, Energy Conversion Type ‖ Battery, Compressed air system, Engine (combustion / reciprocating), Gas turbine (OCGT), ‖ Geothermal power plant, Hydro power system, Liquid air system, Offshore wind turbines, Onshore wind turbines, Photovoltaic, Steam turbine (thermal power plant), Steam-gas turbine (CCGT), Tidal lagoons, Tidal stream devices, ‖ Wave devices ‖ Completed ‖ Complete only if the DER is for generation and/storage |
| TECH_TG_GSCL2 | If Generation &/OR Storage, Energy Source ‖ Advanced Fuel (produced via gasification or pyrolysis of biofuel or waste), Biofuel - Biogas from anaerobic digestion (excluding landfill & sewage), Biofuel - Landfill gas, Biofuel – Other, Biofuel ‖ - Sewage gas, Biomass, Fossil - Brown coal/lignite, ‖ Fossil - Coal gas, Fossil – Gas, Fossil - Hard coal, Fossil – Oil, Fossil - Oil shale, Fossil – Other, Fossil – Peat, Geothermal, Hydrogen, Nuclear, Solar, Waste, Water (flowing water or head of water), Wind, Stored Energy (all stored energy irrespective of the original energy ‖ source) ‖ Completed ‖ Complete only if the DER is for generation and/storage |
| TECH_TG_DDCLS | If Demand, Technology Type ‖ Air source heat pump, Ground source heat pump, Water source heat pump, Hybrid Heat pump, EV Charger DSR, EV ‖ Charger V2G, On site Battery, Flexible Site ‖ Demand ‖ Completed ‖ Complete only if the DER is for demand flexibility ‖ DER ‖ Parameters |
| TECH_PS_INCAP | DER [If Speculative, then ‖ Aggregated Group] Installed capacity (MW) ‖ free text ‖ Completed ‖ The full-load output of the DER |
| TECH_PS_FCDTU | DER [If Speculative, then Aggregated Group] Flexible Active Capacity - Demand ‖ Turn-up (MW) ‖ free text ‖ Completed ‖ The capacity, in MW, of your DER to increase its generation output. If Zero, please respond '0' |
| TECH_PS_FCDTD | DER [If Speculative, then Aggregated Group] Flexible Active Capacity - Demand ‖ Turn-down (MW) ‖ free text ‖ Completed ‖ The capacity, in MW, of your DER to reduce its generation output. If Zero, please respond '0' |
| TECH_PS_FCGTU | DER [If Speculative, then Aggregated Group] Flexible Active Capacity - Generation ‖ Turn-up (MW) ‖ free text ‖ Completed ‖ The capacity, in MW, of your DER to increase its demand on the network. If Zero, please respond '0' |
| TECH_PS_FCGTD | DER [If Speculative, then Aggregated Group] Flexible Active Capacity - Generation ‖ Turn-down (MW) ‖ free text ‖ Completed ‖ The capacity, in MW, of your DER to reduce its demand on the network. If Zero, please respond '0' |
| TECH_PS_REACE | DER [If Speculative, then Aggregated Group] Reactive Export Capacity - Generation Turn-up (MW) ‖ free text ‖ Completed ‖ The capacity, in MVar, that an DER has to generate reactive power: providing an inductive load and lagging effect on current with respect to the network voltage. If Zero, please respond '0' |
| TECH_PS_REACE | DER [If Speculative, then Aggregated Group] Reactive Import Capacity - Generation Turn-down (MW) ‖ free text ‖ Completed ‖ The capacity, in MVar, that a DER has to absorb reactive power: providing a capacitive load and leading effect on current with respect to the network voltage. If Zero, please respond '0' |
| TECH_PF_MINOD | DER [If Speculative, then Aggregated Group] Min Operating Duration (HH:MM) ‖ HH:MM ‖ HH:MM ‖ Minimum amount of time the DER is able to provide a flexibility response. Where a DER is able to run continuously beyond 24hrs, ‖ respond 'Unlimited' |
| TECH_PF_MAXOD | DER [If Speculative, then Aggregated Group] Max Operating Duration (HH:MM) ‖ HH:MM, ‖ Unlimited ‖ HH:MM ‖ Maximum amount of time the DER is able to provide a flexibility response. Where a DER is able to run continuously beyond 24hrs, ‖ respond 'Unlimited' |
| TECH_PS_RESPO | DER [If Speculative, then ‖ Aggregated Group] Response Time (minutes) ‖ HH:MM ‖ HH:MM ‖ The minimum time required for the DER to respond to a utilisation instruction. |
| TECH_PS_RECOV | DER [If Speculative, then Aggregated Group] Recovery Time ‖ HH:MM ‖ HH:MM ‖ The time required by the DER [If Speculative, then Aggregated Group] to recover from one instruction until the next instruction can be actioned. ‖ Metering |
| TECH_PS_METER | Metering Granularity (Second by Second, Minute by Minute or Half Hourly) ‖ SS, MIN, HH ‖ MIN, HH ‖ The metering frequency available for the DER, or if speculative then for the Aggregated Group. Entry should be relevant to the service applicable, for example many DNOs do not accept second x ‖ second metering. |

## 3. Market Information

### 3.1 Implementation tracking

The DNOs must provide the Market Facilitator with the data set out in Table 1 for each Sub-Market in scope of this Flexibility Market Rule. The data provided should accurately reflect their implementation of the rule within each Sub-Market.

The expected values required for compliance are also set out in Table 1.

Initial data shall be sent no later than 20 working days after the Published Date of this Flexibility Market Rule.

Updates shall be sent as soon as reasonably practical, and no later than 10 working days after any changes to the values.

Elexon reserves the right to publish this data within its Implementation Tracker.

**Table 1: Implementation tracking requirements**

| Parameter | Required value (per Sub-Market) |
|---|---|
| Implementation Status | Dependent on date:<br>Before Implementation Date: Not yet started, Implementing, Paused, Implemented<br>Between Implementation Date and End Date: Implemented<br>After End Date: Superseded |
| Target Implementation Date | No later than Implementation Date |

*[The header row of this table begins with the reference FMR-PQC in the source.]*

### 3.2 Flexibility Market Catalogue data

The DNOs must update the Market Facilitator with the data set out in Table 2 below for each Sub-Market in scope of this Flexibility Market Rule. This should accurately reflect their implementation of each Sub-Market.

The expected values required for compliance are also set out in Table 2.

Initial data shall be sent no later than the Implementation Date of this Flexibility Market Rule.

Updates shall be sent as soon as reasonably practical, and no later than 10 working days after any changes to the values.

DNO/System Operators shall also publish this information themselves.

Elexon reserves the right to publish this data within its Flexibility Market Catalogue.

**Table 2: Sub-Market definitions**

| Parameter | Description | Required Value |
|---|---|---|
| Non-Standard criteria in use? | Does the DNO use any non-standard terms (as submitted to the Market Facilitator as per section 2) | - |

### 3.3 Effectiveness monitoring

The following metrics shall be used to assess the effectiveness of the rule.

All DNOs must provide the Market Facilitator with any Additional Input Data as set out in Table 6 below for each Sub-Market in scope of this rule. The data provided should accurately reflect their implementation of the rule within each of their Sub-Markets.

The expected values minimum required values for compliance, if any, are also set out in Table 6.

Initial Additional Input Data shall be sent no later than 20 working days after the Implementation Date of this Flexibility Market Rule.

Additional Input Data shall be sent in accordance with the Cadence set out in Table 6.

Updates to Additional Input Data shall be sent as soon as reasonably practical, and no later than 10 working days after any changes to the values.

Elexon reserves the right to publish this data within its Implementation Tracker.

**Table 3: Effectiveness monitoring metrics** 
| Field | Metric 1 |
|---|---|
| Description | Number of variations to standardised pre-qualification criteria implemented per DNO |
| Why are we tracking this? | To understand the level of alignment and difference across system operators |
| Cadence | Every 6 months |
| Data Source | Existing Data – Derogation requirements as set out in section 1<br>Additional Input Data - None |
| What does good look like? | 0 |
| Minimum Requirement | - |