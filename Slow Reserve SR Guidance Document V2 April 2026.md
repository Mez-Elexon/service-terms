# Slow Reserve (SR) Guidance Document – Version 2 (April 2026)

> **Source file:** `slow reserve guidance.txt` (NESO slide deck, 82 slides, copy-pasted). Published on the NESO Slow Reserve page as "Slow Reserve Guidance Document" (`https://www.neso.energy/document/375811/download`).  
> **Version history:** V1 January 2026; V2 April 2026 – "Clarification on additional headroom/footroom for BM units (Page 24)".  
> **Status:** Guidance only. The deck itself says: in the event of any conflict or inconsistency between this document and the contractual documents (Service Terms, Procurement Rules and Balancing Services Glossary), the latter shall prevail.  
> **Converted:** 2026-10-29. **Condensed, not a full transcript.** Substantive wording kept verbatim. Removed: cover, contents, "Public" markings and slide numbers; the user-journey diagram; SMP/EAC screen-by-screen registration and bidding steps (summarised in one line each); chart axis labels and legends; the "Dynamic Parameter definitions" box repeated on most slides (given once below); duplicate unit-characteristic boxes in the worked examples; contact slide. Where the BM and Non-BM slides say the same thing, the text is given once. Original slide numbers are in *[s.N]* markers. Notes in *[italic square brackets]* are editorial.

**Dynamic Parameter definitions (repeated on most monitoring slides):** FPN – Final Physical Notification, MEL – Maximum Export Limit, SEL – Stable Export Limit, MIL – Maximum Import Limit, MZT – Minimum Zero Time, MNZT – Minimum Non-Zero Time, Ramp Rates, SIL – Stable Import Limit, NTO – Notice to Offer, NTB – Notice to Bid, NDZ – Notice to Deviate from Zero, BOA – Bid Offer Acceptance.

---

## 1. Service Specification

Slow Reserve (SR) is part of our new suite of Reserve products. The SR market will allow us to procure access to post-fault upwards (headroom) and downwards (footroom) flexibility through two new balancing services: Positive Slow Reserve and Negative Slow Reserve. This capacity can then be manually dispatched by NESO control room engineers in real time. The SR service will allow NESO to better meet its system and statutory requirements following updates to the System Operator Guidelines (SOGL) standard, which state that the system frequency must be returned to ±0.2Hz within 15 minutes of a loss event. *[s.4]*

### Technical Parameters *[s.6–7]*

| Technical Design Element | Detail |
|---|---|
| Direction | Positive and Negative |
| Minimum Contract Size | 1 MW |
| Provider eligibility | Non-BM & BM units with control/system telephony during contracted windows |
| Time to full delivery | Up to 15 minutes |
| Minimum Activation Period | Up to 30 minutes |
| Maximum Recovery Period | Up to 60 minutes |
| Energy Requirement | The unit must be able to deliver the full contracted capacity per SR Window |
| Operational Metering | 0.0667 Hz / once per 15s for both BM and non-BM units, up to 5s latency |
| Dispatch mechanism | BOAs for BM units. OBP dispatch instruction for non-BM units |
| Notice to Start Ramping | Up to 14 minutes |
| Time to accept instruction | Up to 2 minutes |
| Ramp rates | Notice period > 10 mins: Max ramp rate of 100% contracted capacity per minute. Unit cannot deliver >50% contracted capacity in any 30s ramping period.<br>Notice period ≤ 10 mins: No maximum ramp rate limit.<br>Minimum ramp-up and ramp-down rate to be in line with Time to Full Delivery. |
| Performance Metering | 0.0667Hz / once per 15s for both BM and non-BM units |
| Performance Monitoring | Time to Full Delivery, Availability, Ramp Rates and Utilisation – Payment Penalties for over (>120%) and under (<95%) delivery |
| Baselining | All providers are expected to provide nomination baselines, equivalent to the BM Physical Notification, with Final Physical Notifications 60-mins ahead of contracted Settlement Period. Both zero and non-zero baselines allowed. |
| Aggregation | Allowed, per GSP group |
| Operational data requirements | BM units as per current BM operations. Non-BM units to submit availability declarations (including price and MW). |
| Passing through zero | Allowed |
| Cross-overs | Units are expected to be available for instruction into a subsequent settlement period (including where non-contracted) up to its Minimum Activation Period |

Note: Volumes associated with prices must be sufficient to dispatch Contracted MW, and Excessive Utilisation Prices may lead to penalties.

## 2. Onboarding *[s.9–12, summarised]*

*[Slides 9–12 walk through SMP portal registration (first-time user, primary user, UK / non-UK company lookup), creating Assets and Units, and pre-qualifying Units for Positive and/or Negative Slow Reserve via SMP. Systems named: DEP (Digital Engagement Platform), EAC (Enduring Auction Capability), OBP (Open Balancing Programme), STAR (Settlement and Revenue system). Points of substance kept below.]*

- Users who already have Assets and Units in SMP for other services (i.e, DC/DM/DR, Balancing Reserve) can move straight to pre-qualifying them for Slow Reserve.
- Once you have submitted your unit/s for pre-qualification, they will be reviewed by the NESO team. We will check that: a signed Form B has been provided, as well as that the Unit information is correct and meets the service parameters.
- Please note that all company information must match what is listed on Companies House.
- A failure to submit valid MPAN information will result in pre-qualification approval being delayed/withdrawn.

## 3. Linked Windows & MUP (service go-live only) *[s.13]*

NESO will be linking certain contiguous SR Windows for Positive Slow Reserve (PSR) only through the procurement process for an initial transitional period from Slow Reserve service go-live.

There will be three separately procured linked SR Window periods for each operational day during the transition period, as follows.
- A morning window which will run from 06:00 to 10:30
- A midday window which will run from 10:30 to 15:00
- An evening window which will run from 15:00 to 21.00

To minimise the impact on market participants during the transition period, we intend to relax the SR service obligation that SR units must be capable of delivering energy (if instructed) continuously for the entire Contracted Service Period. Instead, we will allow SR units to cease delivery when they reach their declared Maximum Utilisation Period (MUP).

For further information on these transition period requirements, please see the Slow Reserve Transition Plan, and Linked Window Recording and Slide Pack.

## 4. Auctions

*[s.15, summarised: orders are built on EAC as baskets of 30-minute service windows (parent, child and substitutable child orders; looped baskets carry a family name). All participants must be registered as a user for EAC, even after registering units on SMP. Bids can also be submitted via API. Results appear in the EAC results tab and on the Data Portal.]*

### Single market for response and reserve *[s.16]*

- Frequency Response services (Dynamic Containment, Dynamic Moderation, Dynamic Regulation) and the new Reserve services (Balancing Reserve, Quick Reserve, Slow Reserve) are procured simultaneously in a single, pay-as-clear auction.
- **Co-optimisation:** The auction clearing algorithm is able to select between alternative provider offers and alternate NESO requirements to better optimise the overall market clearing.
- **EAC clearing algorithm:** Our strategic partner, N-SIDE, is developing a new, bespoke market clearing algorithm to enable the new market features.
- **Overholding:** The auction clearing algorithm may clear a quantity of service in excess of NESO requirements if this better optimises the market.

### Auction Overview *[s.17–18]*

- The EAC Auction is used for the clearing of capacity (availability) for: Frequency Response Services – DC, DM, DR; Reserve Services – QR, BR and SR.
- For every service, there are 2 product directions. For Response these are Low (L) and High (H) products (DRL and DRH, DML and DMH, DCL and DCH). For Reserve these Positive (P) and Negative (N) Products (PBR, PQR, PSR and NBR, NQR, NSR).
- DC, DM, DR, BR, QR, SR will be procured in a single, simultaneous day-ahead auction held daily at 14:00.
- Auction type: Closed double-sided auction. Objective function: Maximisation of social welfare. Pricing: Uniform clearing price per product for each service window. Locational granularity: GB synchronous area. Overholding allowed (cleared quantity may exceed NESO bid quantity). Procurement: Capacity (MW).

| | Response | QR | SR |
|---|---|---|---|
| **Auction Timing** | | | |
| Gate Opening | 08:00 BST / GMT D-15 | | |
| Gate Closure | 14:00 BST / GMT D-1 | | |
| Publication of Results on UI | By 14:30 BST / GMT D-1 | | |
| Publication of Results on Data Portal | By 15:00 BST / GMT D-1 | | |
| **Sell Order Design** | | | |
| Number of Baskets per Unit per EFA day | 25 | 100 | 100 |
| Number of Parent Orders per Basket | Must be 1 | Must be 1 | Must be 1 |
| Number of Child Orders per Basket | No more than 10 | No more than 10 | No more than 10 |
| Number of Substitutable Child Orders per Basket | No more than 10 | No more than 10 | No more than 10 |
| **Technical Parameters** | | | |
| Technical Minimum Prices (£/MW/h) | -20 | 0 | 0 |
| Technical Maximum Prices (£/MW/h) | 999.99 | 999.99 | 999.99 |
| Minimum Contract Size (MW) | 1 | 1 | 1 |

*[Auction timing rows appear once across all three columns in the source.]* Note: "D" stands for "delivery date". For more information, please see EAC Market Design Report and EAC Market Design Explainer.

### Volume Requirement *[s.19]*

The requirement will be published on the Data Portal in the future which will specify what Positive and Negative Slow Reserve volumes we are aiming to procure. For the initial Day 1 launch of Slow Reserve, the expected total volume requirements are 1,800MW for the positive side and 1,800MW for the negative side. Please note that the MW requirement may be subject to change following a review of system operating conditions.

## 5. Service Stacking & Splitting

Note: Positive and Negative is not considered the same MW. Therefore, where 100% of a unit's capacity can be awarded a contract in opposite directions for the same service window, this is not considered stacking or co-delivery.

### Co-delivery *[s.21]*

Definition: Being paid multiple revenues from the same asset, using the same capacity/MW, in the same time period (and in the same direction).

- Slow Reserve cannot be co-delivered with any other frequency management Ancillary Service e.g. Reserve (including Balancing Reserve) or any Dynamic Frequency Response.
- Slow Reserve can be co-delivered with the Capacity Market (CM), the BM, and Voltage and Stability services.
- Where a CM Notice (CMN) is issued, these providers should continue to make headroom available to us as per any active Slow Reserve commitments.
- To ensure that providers are protected from penalties for breach of their CM agreement should a System Stress Event occur following the CMN, Slow Reserve has been added to the list of Relevant Balancing Services.

### Splitting *[s.22–23]*

Definition: Being paid multiple revenues from the same asset, but with different capacity/MW, in the same time period.

- Slow Reserve can only be Split with the same Reserve service, but in the opposite direction. Therefore; Positive Slow Reserve can be split with Negative Slow Reserve. For example, a unit with 10MW of headroom and footroom may be awarded a 10MW contract in both directions.
- Slow Reserve cannot be Split with any other Ancillary Service at launch.
- Slow Reserve can be split with the BM, Voltage and Stability services.

The Slow Reserve auction is going to be co-optimised with the Dynamic Response auction (EAC auction) and therefore providers may offer Slow Reserve, Quick Reserve and Dynamic Response products during the same time periods, however they must not be in the same Sell Order or Basket and must always meet the terms of the relevant services.

**Splitting Matrix** *[s.23; the colour-coded grid was not captured, only its notes]*
- Splitting with Response: allowed between any frequency response products (i.e., any combination of DCL, DCH, DML, DMH, DRL, and DRH).
- Splitting within Reserve: allowed between Balancing Reserve products (PBR and NBR), between Quick Reserve products (PQR and NQR), and between Slow Reserve products (PSR and NSR). However, splitting is not currently allowed between different Reserve products.
- Splitting Reserve with Response: There is work underway to understand the end-to-end requirement for Stacking across Reserve and Response Balancing Services. As part of this work and our continued reform of Balancing Services, we will keep all service parameters under review.

### Additional Headroom/Footroom – BM Units *[s.24, added in V2]*

The SR Service Terms (clause 17) set out the rules for the provision of other services whilst contracted for SR and allows a BM unit to offer any additional volume (headroom/footroom), beyond its contracted quantity, through the Balancing Mechanism, where that volume is not for another Balancing Service.

A SR unit's primary obligation, whilst contracted for Slow Reserve, is to allow NESO to instruct either part, all or more (where applicable) than their contracted volume of SR. Bid-Offer pairs 1 to 5 must be constructed accordingly, such that NESO can first access the contracted volume of SR before accessing any additional MW volume.

NESO procures SR capacity at day ahead as a post fault reserve product (to cover the largest infeed or outfeed loss on the system), and SR units are paid an Availability fee for this capacity. There is no obligation on NESO to dispatch an SR unit during the contract period and as result, SR units may be held back from normal dispatch actions for this purpose. It is therefore possible that NESO will not instruct any additional volume, as this volume can only be accessed after the SR contracted volume has been instructed.

## 6. Operational Data

### Pre-gate Closure Data – BM Units *[s.26]*

Relevant Data for Slow Reserve: Maximum Export Limit (MEL); Maximum Import Limit (MIL); Stable Export Limit (SEL); Stable Import Limit (SIL); Run-up Rate; Run-down Rate; Minimum Non-Zero Time (MNZT); Minimum Zero Time (MZT); Bid/Offer pairs; Notice to Offer (NTO); Notice to Bid (NTB); Notice to Deviate from Zero (NDZ); FPN; BO Pair Price/Volumes data.

Contracted BM Slow Reserve (SR) providers are to submit BM data to NESO via EDL/EDT. This data should be submitted in accordance with the Grid Code (in particular BC1 & BC2).

NESO engineers repeatedly calculate the expected operating margin between 24 hours and 4 hours ahead of real time. The introduction of Slow Reserve means that some contracted reserve volume is known at 14:00 the Day Ahead of delivery and therefore these contracted volumes will be included in the engineer's margin assessments.

To help us to ensure the margin assessments are as accurate as possible, we would appreciate contracted BM units submitting Day Ahead Submissions even when not mandated to do so by the Grid Code. Data should then be revised if new information becomes available to the BM Participant.

Failure to submit any data required for the determination of contract compliance will result in payment being with-held.

### Pre-gate Closure Data – non-BM Units *[s.27]*

Relevant Data for Slow Reserve: Availability (Price and MWs) – Note: Post gate declarations can be made to notify unavailability; Physical Notifications.

Contracted non-BM Slow Reserve (SR) providers need to submit data to NESO via OBP. This data should be submitted ahead of gate closure (i.e., 1 hour ahead of the relevant Settlement Period).

NESO engineers repeatedly calculate the expected operating margin between 24 hours and 4 hours ahead of real time. The introduction of non-BM Slow Reserve means that some non-BM contracted reserve volume is known at Day Ahead of delivery and therefore these contracted volumes will be included in the engineer's margin assessments.

To help NESO ensure margin assessments are as accurate as possible, contracted non-BM providers should submit PN declarations within 2 hours of contract award.

Data should then be revised once new information becomes available to the non-BM Participant up to 1 hour before the relevant Settlement Period (i.e., Gate Closure), where the PN becomes a Final Physical Notification.

### BM Participants – Operational Data Submissions *[s.28; slide cites "SR Service Terms" and "BC1"]*

- The Grid Code, within Section BC1 lays out the option for Balancing Mechanism participating Units (BMUs) to provide NESO with indicative Physical Notifications (PNs) and import and export limits (MELs/MILs) well in advance of real time.
- Large and Medium Power Stations and all BMUs which are Transmission connected are required to submit their indicative PNs at 11:00 hours each day for every Settlement Period of the following Operational Day (which begins at 05:00 the following morning).
- NESO's scheduling teams use this data within their margin assessments to inform strategic decisions.
- Slow Reserve contracted units know their contract award outcomes by ~14:30 for delivery in the majority of the next Operational Day. Their PNs, MELs, and MILs should be reviewed and, if necessary, revised, as soon as reasonably practical after formation of a SR contract (and in any event by no later than gate closure).
- This will help us to conduct efficient scheduling and allow the Slow Reserve market deliver the most value.

### Non-BM Participants – Operational Data Submissions *[s.29; slide cites "SR Service Terms"]*

- The SR Service Terms lay out the requirement for non-Balancing Mechanism participating Units (non-BMUs) to provide NESO with indicative Baselines (equivalent to Physical Notifications in the BM) in advance of real time.
- All non-BMUs are required to submit their indicative PNs (by no later than 2 hours following publication of auction results) for every Settlement Period of the following Service Day (which begins at 23:00 the same evening).
- NESO's scheduling teams use this data within their margin assessments to inform strategic decisions.
- Slow Reserve contracted units know their contract award outcomes by ~14:30 for delivery in the next Service Day. Their Baselines should regularly be reviewed and, if necessary, revised, as soon as reasonably practical after formation of a SR contract (and in any event by no later than gate closure).
- This will help us to conduct efficient scheduling and allow the Slow Reserve market deliver the most value.

### Energy Limited Assets *[s.30]*

Battery Energy Storage Systems (BESS) and Pumped Storage have energy limitations based on the storage capacity of their equipment. BESS can participate in the SR auctions but are expected to be able to manage their state of energy to be able to deliver the full contracted quantity for the duration of the SR service window.

NESO has already published guidance on the submission of MEL/MIL parameters for BM participants (guidance note from December 2023; an update with the 30-minute rule was published in February 2024).

### Data and Transparency *[s.31]*

- Registered Service Providers are required to submit Operational Data as outlined in the Service Terms.
- NESO requires Performance data to be submitted by all SR providers. A failure to submit this data will result in payments being withheld. Performance Monitoring data is to be submitted to NESO by no later than 24 hours following the end of the relevant Service Day. Metering is positive for export, and negative for import.
- Details of the SR auction results including a breakdown of each Sell Order, NESO's Buy Order and results summaries will be available on the data portal by 14:30 every afternoon.
- Publication of unit availability, dispatch, and baseline data can be found via ELEXON's website for BM units. For non-BM units, availability, dispatch, and baseline data can be found on the following NESO data portal pages: non-BM Reserve Instructions; non-BM Mandatory Availability Declarations; Non-BM Baselines (FPNs).

## 7. Metering & Heartbeat

### Operational Metering *[s.33]*

All providers must submit Operational metering at a 0.0667Hz / once per 15s granularity, with a latency of no more than 5 seconds.

NESO's 'Operational Metering' document describes the operational metering architecture NESO has in place to enable the connection for non-transmission connected BM & Non-BM Participants' to NESO's Systems. There are three routes for providing operational metering to the balancing systems:
- Connect to an existing GB Transmission Owner's Real-time Telemetry Unit (RTU).
- Install a new RTU and provide dedicated telecommunication signals to that location.
- Connect to the SCADA Data Concentrator host.

BM Providers may also submit their Operational Metering through the existing BM Fixed Line.

### Performance Metering *[s.34]*

All providers (both BM and non-BM) are required to submit data to NESO for post-event performance monitoring. This data is required by NESO to validate the performance where units are dispatched to deliver an instruction for the SR Contract and Optional Slow Reserve services.

- **Where a SR Contract is held:** Service Providers are required to submit (via the agreed IT interface) a Performance Metering file for all contracted SR Windows in the Service Day and for any SR Window where a Crossover occurs (including the 1st SR Window of the following Service Day if applicable).
- **For the Optional service:** Service Providers are required to submit (via the agreed IT interface) Performance Metering file for all SR Windows where the Optional Service is utilised and for any SR Window where a Crossover occurs (including the 1st SR Window of the following Service Day if applicable).
- Where, due to a fault, the service providers Performance Metering file is unavailable for submission by the agreed IT interface, the Service Provider can agree with NESO to submit alternative Performance Metering data by not later than five calendar days after the Service Day on which SR was provided.

All files must be submitted at a 0.0667Hz / once per 15s granularity by no later than one calendar day (24 hours) after the end of the Service Day on which SR was provided.

### Heartbeat (Connection Indicator) *[s.35]*

The 'Heartbeat' also referred to as the 'Connection Indicator' is used to ensure that NESO control-room has a live connection to each SR unit and that its operational and remains dispatchable.

- **For BM:** The Connection Indicator refers to the handshake between NESO systems and control point systems to establish a connection exists and a unit is operational. Further handshakes also confirm the link is operational and exchanged whenever a message is sent. The Connection Indicator is via EDL and part of the business-as-usual operations for BM participation.
- **For non-BM:** we have added the requirement into the service terms in order to mirror the existing BM EDL requirement to ensure we have visibility that a non-BM unit will be able to receive and respond to a message (instruction/cease). Details are set out in the OBP web service specification.

## 8. Performance Monitoring

### General rules *[s.37]*

A contracted unit must be capable of being dispatched during all contracted service windows in accordance with the following rules:
- being dispatched from any prevailing Stable Export Limit or Stable Import Limit (which for the avoidance of doubt may be 0MW) or from any other higher level of Output or Demand
- being dispatched for a single or multiple consecutive periods each of not more than 30 minutes in duration (representing the max minimum activation period) which for these purposes include all Ramping
- being capable of dispatch for the full length of all contracts
- being capable of dispatch no more than 60 minutes after the end of delivery of a previous instruction (Recovery Period)
- being capable of not exceeding ramp rates of 100% contracted capacity per minute and, for non-linear ramping, 50% of the contracted capacity in any 30-second period for units with a > 10-minute notice period

The unit participating in the service will be subject to performance monitoring on Time to Full Delivery, Ramp Rates, Availability, and Utilisation. Note: For the purpose of delivery assessment, ramping periods are computed based on ramp rates (submitted or derived).

**Every Event of Default (EoD) below carries the same consequence on its slide:** When a reserve unit triggers an EOD, it will forfeit Availability Payment for all the relevant Committed Windows. Most slides also note: SR units can participate from non-zero baselines.

### Availability – BM (EoD code "AVAL") *[s.38–39]*

A contracted unit should be able to demonstrate 100% of contracted Positive Slow Reserve (headroom) and/or Negative Slow Reserve (footroom). Failure to demonstrate the contracted availability will trigger an Event of Default (EoD).

**Positive Slow Reserve**
- For a generator (or a unit with only positive output): MEL – FPN ≥ Contracted Quantity AND FPN ≥ 0. Plus also check that If FPN<SEL then SEL ≤ Contracted Quantity
- For a supplier (or a unit with only negative output): SIL – FPN ≥ Contracted Quantity AND FPN < 0
- For a "through-zero" unit:
  1. If FPN ≥ 0 then (MEL-FPN) ≥ Contracted Quantity
  2. If FPN < 0 and SEL and SIL = 0 then (MEL-FPN) ≥ Contracted Quantity
  3. If FPN < 0, and SEL and SIL ≠ 0 then if (MEL-FPN) ≥ Contracted Quantity And (SEL-FPN) ≤ Contracted Quantity then (MEL-FPN) ≥ Contracted Quantity else
  4. (SIL-FPN) ≥ Contracted Quantity
  
  Also check that If FPN ≥ 0 and FPN < SEL then SEL ≤ Contracted Quantity
- For a Power Park Module powered by an Intermittent Power Source: PA-FPN ≥ Contracted Quantity

**Negative Slow Reserve**
- For a generator (or a unit with only positive output): FPN – SEL ≥ Contracted Quantity AND FPN 0 *[operator missing in source]*
- For a supplier (or a unit with only negative output): FPN – MIL ≥ Contracted Quantity AND FPN ≤ 0
- For a "through-zero" unit:
  1. If FPN ≥ 0 AND SEL and SIL = 0 then (FPN-MIL) ≥ Contracted Quantity
  2. If FPN > 0 and SEL and SIL ≠ 0 then If (FPN-SIL) ≤ Contracted Quantity then (FPN-MIL) ≥ Contracted Quantity else (FPN-SEL) ≥ Contracted Quantity
  3. If FPN ≤ 0 (FPN-MIL) ≥ Contracted Quantity
- For a Power Park Module powered by an Intermittent Power Source: FPN – PA ≥ Contracted Quantity

For the avoidance of doubt, and if not already indicated, a unit must make available the contracted MWs for the required service(s) within the specified Service Window(s), and NESO should not have to send an instruction greater than or less than a unit's contracted capacity due to a limitation of the unit. That is to say: Available capacity ≥ contracted SR volume; Minimum instructible volume ≤ contracted SR volume.

### Availability – NBM (EoD code "ADEC") *[s.40]*

Availability check is not relevant for NBM units, therefore, confirmation that the Headroom (for Positive reserve services) & Footroom (for Negative reserve services) is there for a settlement period is done monitoring the availability declarations history.

For an NBM unit to be deemed available, the declaration at gate closure for the service must be: Declared MW = Contracted MW. And the declaration throughout the SP must be: Declared MW = Contracted MW.
- Note 1: Gate closure is 60 minutes prior to the start of the settlement period
- Note 2: The check is undertaken at the start of each settlement period, and throughout the settlement period
- Note 3: If a units declared MW ≠ Contracted MW, it would fail Availability checks but will remain available to NESO for dispatch

### Response Time – BM (EoD code "RESP") *[s.41–42]*

A contracted unit must be capable of achieving the full contracted capacity within the Response Time of 15 minutes, which is inclusive of Notice to Offer (NTO) or Notice to Bid (NTB) and NDZ (Notice To Deviate from Zero) time parameters.

`Response Time (minutes) = Notice Period + Time to Ramp Up` (positive) / `+ Time to Ramp Down` (negative)

The time to ramp will be determined from the ramp rates and elbow points submitted. Please note however that the computations below are based on a single ramp rate. *[Fractions were flattened in the copy; rebuilt as `a / b`.]*

| Unit | Positive Slow Reserve | Negative Slow Reserve |
|---|---|---|
| Generator (only positive output) | Notice Period + Contracted capacity [MW] / Run up rate export [MW/minute] | Notice Period + Contracted capacity [MW] / Run down rate export [MW/minute] |
| Supplier (only negative output) | Notice Period + Contracted capacity [MW] / Run up rate import [MW/minute] | Notice Period + Contracted capacity [MW] / Run down rate import [MW/minute] |
| Bi-directional, simple case | if FPN ≥ 0: Notice Period + Contracted capacity [MW] / Run up rate export | if FPN ≤ 0: Notice Period + Contracted capacity [MW] / Run down rate export |
| Bi-directional, crossing zero | if FPN < 0: Notice Period + Min(Contracted capacity MW, (SIL − FPN)) / Run up rate import + Max(0, (Contracted MW − Min(Contracted capacity MW, SIL − FPN))) / Run up rate export | if FPN > 0: Notice Period + Min(Contracted capacity MW, (FPN − SEL)) / Run down rate export + Max(0, (Contracted MW − Min(Contracted capacity MW, FPN − SEL))) / Run down rate export |

*[Rate labels reproduced as printed, including "Run down rate export" for the FPN ≤ 0 negative case.]*

### Response Time – NBM (EoD code "RESP") *[s.43]*

A contracted unit must be capable of achieving the full contracted capacity within the Time to Full Delivery of 15 minutes, which is inclusive of Notice to Start (NTS). Note: Currently ramp rates are derived but in the future they will be submitted as part of NBM pre-qualification.
- Positive Slow Reserve: Units calculated Response Time <= Contracted Response Time, Where Positive service utilises a Run-Up Rate
- Negative Slow Reserve: Units calculated Response Time <= Contracted Response Time, Where Negative service utilises a Run-Down Rate

### Utilisation – BM and NBM (EoD code "CDEL") *[s.44–45]*

The unit must deliver within the acceptable ramping envelope, and the Notice period plus time to ramp must be no greater than 15 minutes. Under-delivery below 95% and over-delivery above 120% output will mean availability payments for the relevant service window will be withheld.

- BM – PSR: Expected Volume = Positive net BOA volume (MWh); NSR: Expected Volume = Negative net BOA volume (MWh)
- NBM: Volumes are computed per instruction per second and aggregated per settlement period into Ramping and Non-Ramping Periods. PSR: the provider ramps up to deliver and ramps down to cease delivery. NSR: the provider ramps down to deliver and ramps up to cease delivery. The calculation of ramping and non-ramping periods will be based on actual ramp rates submitted or derived from pre-qualification data.

The check (for all units):
- (Settlement metering – Baseload) ≥ (Expected Volume * 95%)
- (Settlement metering – Baseload) ≤ (Expected Volume * 120%)

**Baseload = Profiled FPN data adjusted for Response delivery.**

*[Chart (not captured): delivery envelope between 95% and 120% of Instructed Capacity from Reserve Request Starts T0 to Reserve Request Stops T1 – "100% availability payment" inside the band, "No availability payment" above or below; phases Ramping up / Time at full delivery / Ramping down, then Recovery Period.]*

### Service delivers in Contracted Response Time – BM and NBM (EoD code "CRSP") *[s.46–47]*

The unit must deliver against the Instructed Megawatts within the time to full delivery (BM) / contracted response time (NBM). When unit DOES NOT deliver between 95% and 120% of its expected MW at the expiry time of the Ramp period then the CRSP failure will be generated.

- BM: The system processes the check at the start time of the first BOA in a contiguous BOA period + Contracted Response Time – Notice period. *For SR, Notice period = ≤14 minutes.*
- NBM: As instructions can be issued with a deferred start, the check is undertaken at the instruction Start Date time (start ramp date/time) + Contracted Response less NTS. Note: NTS and ramp rates are computed at the point the pre-qual data was uploaded.

The Check: `[(Metered MW - Baseload MW) / Expected MW] * 100` should be between Under Delivery % and Over Delivery %, where Expected MW are positive for a positive reserve service, and negative for a Negative reserve service: i.e., ≤95% and ≤120% *[as printed]*.

### Activation Period – BM and NBM (EoD code "MNZT") *[s.48–49]*

Being dispatched for a single or multiple consecutive periods each of not more than 30 minutes in duration (representing the max minimum activation period) which for these purposes include all Ramping.

The check – Minimum Activation Period (MNZT): 0 - 30 mins. Where a unit's min activation period is ≤ 30 mins, the unit will pass the check, and an AVAIL payment will be made.

### Recovery Period – BM and NBM (EoD code "MZT") *[s.50–51]*

Being capable of dispatch no more than 60 minutes after the end of delivery of a previous instruction (Recovery Period).

The check – Recovery Period (MZT): 0 - 60 mins. Where a unit's recovery period ≤ 60 mins, the unit will pass the check, and an AVAIL payment will be made.

### Available Dispatch Volume (EoD code "VOL" or "IBOD") *[s.52–53]*

It must be possible to dispatch the contracted MWs.

- **BM:** Where a unit is contracted for Positive Quick Reserve, the BO_LEVEL MW will be summed for all positive BO Pairs (1 to 5) to ensure that the resultant volume >= Contracted MW. Where a unit is contracted for Negative Quick Reserve, the BO_LEVEL MW will be summed for all negative BO Pairs (-1 to -5), to ensure that the absolute (resultant volume) >= Contracted MW. *[Source says "Quick Reserve" on this SR slide.]* Where this is not possible because the Bid-Offer Price submission does not have a MW level >= Contracted MW then an "VOL" failure will be recorded for Invalid Bid-Offer Data.
- **NBM:** Where a unit is contracted for Slow Reserve, the unit will be checked to ensure the MWs provided in the "Avail at GC File" (which also contains prices) = Contracted MW. Where this is not possible because the unit has not submitted a price against a MW value that is greater or equal to the Contracted MW then an "VOL" failure will be recorded.

Any failures will result in the following: EoD code VOL will be recorded, and NO availability payment will be made.

### Submitted Ramp ("SRMP") and Delivery Ramp ("DRMP") – BM and NBM *[s.54–55]*

Where a unit's notice period > 10 mins:
- The maximum ramp rate limit is set at ≤100% contracted capacity per minute.
- For instantaneous ramping (i.e., units than cannot ramp linearly), the unit cannot deliver more than 50% of the contracted capacity in any 30-second period.

This is monitored in two separate checks:
1. The Maximum submitted (or derived) Ramp rates MW/min <= Contracted MW for each settlement. If this is not the case then a "SRMP" EoD will be reported, and no payment will be made for the Settlement Period.
2. During service Utilisation; The MW delivered must be <= Expected MW as monitored for each 15 seconds during the contracted ramp period = Contracted Response Time less Notice Period. If this is not the case then a "DRMP" EoD will be reported, and no payment will be made for the Settlement Period.

Where a unit's notice period ≤ 10 mins, there is no maximum ramp rate limit.

### Performance Metering Data – BM and NBM (EoD code "DATA") *[s.56–57]*

The provision of PN (Physical Notification) data and Performance Settlement Period is a pre-requisite to assessing the availability and delivery of the service.

The checks – Performance Metering and PN Data: When a unit fails to supply either: a) PN data, or b) Metering Data, then the unit will be subject to a "DATA" event of default and an 'Availability Failure' flag will be set to "Y", resulting in no availability payment made for the Settlement period.

### Cease Time – BM and NBM (EoD code "CEAS") *[s.58–59]*

Submitted ramp rates are checked to ensure that a unit is capable of ceasing the provision of the service within the cease time specified in the service terms.

If a units' calculated cease ramping time (based on the tendered MW and Ramp Rate) is > 15 minutes, then the unit will be subject to a "CEAS" event of default and an 'Availability Failure' flag will be set to "Y", resulting in no availability payment made for the Settlement period. Note: The unit is required to cease service provision within 15 minutes.

### Crossover Check (EoD code "COVR") *[s.60–61]*

Verification that contracted units could deliver the service, if instructed, at the end of the Settlement Period as per service terms and Crossover Rules.

**BM:**
1. The provider must maintain its contracted Headroom or Footroom check (for a PSR or NSR service) into the following settlement period for the duration of the cross over period. For example; if a unit was contracted for 25 MW PSR from 18:00 – 18:30, and the cross over period was 3 minutes; then the units' headroom must be at least 25MW for the period 18:30 – 18:33 or it will be subject to a COVR Failure.
2. The provider must be capable of being dispatched up to its contracted MW during a cross over period. To validate this, in the settlement period following a contracted settlement period MW are totalled and compared to the requirement: (a) For a PSR service positive BO pair BO_LEVEL are totalled. (b) For a NSR negative BO Pairs Absolute BO_LEVEL MW are totalled.

   Example: A unit is contracted for 25 MW PSR from 18:00–18:30, and has a cross over period of 3 minutes. It has submitted 2 positive BO pairs for 18:30 – 19:00; BO pair 1 with a BO_LEVEL of 20 MW and BO Pair 2 with a BO_LEVEL of 3. In this case the unit can be dispatched only for 23MW (20 +3) during the cross over period, and as this is less that the contracted PSR of 25MW in the previous SP there is a COVR failure.

**NBM** – for the cross over period, a NBM provider:
- (a) Must submit an FPN
- (b) If a price is submitted for the tendered service, then the associated MW <>0. Note: If no price is submitted then this check passes, or if a price is submitted and the MW is not zero, then this check passes
- (c) Must not have a declaration =0. (Note: A null value i.e. no value, or a non-zero value is acceptable)

If any one of the above fails Then COVR failure will be generated, AVAL flag will be set to "0" and no Availability payment will be made.

### Stacking – Splitting (EoD code "SPLT") – BM and NBM *[s.62–63]*

Splitting is not allowed between the same polarity Reserve products, i.e., PSR & PBR. Positive contracted units can ONLY be split with: Slow Reserve negative. Negative contracted units can ONLY be split with: Slow Reserve positive.

The Check: Where a unit is contracted for Slow Reserve Positive and Slow Reserve Negative, units will pass and Availability payment will be made. Any failures will result in the following: EoD code SPLT will be recorded, and NO availability payment will be made.

### Excessive pricing *[s.64]*

NESO has implemented the Excessive Pricing Service Term clause, drawing on insights gained from other Balancing Services. It seeks to ensure that SR units remain available through contracted periods and do not intentionally deter NESO from dispatch by submitting excessively high or low pricing.

For the purpose of monitoring, our tool considers a BM/NBM unit bid/offer price submitted is excessively high/low when compared to the calculated statistical threshold value for the relevant fuel category in a particular settlement period. The Price Threshold Formula we apply (which NESO reserves the right to review periodically) is:
- BM/NBM Bid Price Threshold = Median BM Bid (for the relevant SP and unit fuel category) - 3 * the Standard Deviation (for the relevant SP and unit fuel category)
- BM/NBM Offer Price Threshold = Median BM Offer Price (for the relevant SP and unit fuel category) + 3 * the Standard Deviation (for the relevant SP and unit fuel category)

Note: These formulas are used to define the thresholds that help NESO assess whether the BM/NBM Bid Price or BM/NBM Offer Price may be excessively high or excessively low, pursuant to Paragraph 5.12 of the SR Service Terms.

**"Excessive Pricing" – Process flow** *[reordered from the diagram]*
1. **Stage One – Flagging potential pricing anomalies / outliers:** Price threshold formula to identify potential anomalies/outliers which are taken into stage two.
2. **Stage Two – Assessment:** Consideration of market conditions and other relevant circumstances (example unplanned/planned BM EDL OR EDT + EDL outages, wider BM scarcity) to identify any potential legitimate justifications – if none, or in doubt, then taken into stage three.
3. **Stage Three – Provider explanation:** Provider explanation sought and considered – If NESO considers sole or primary motivation was to discourage dispatch, then taken into stage four.
4. **Stage Four – Identifying mitigating and aggravating factors:** Mitigating factors include first 'offence', minor divergence from acceptable pricing range, cooperative with NESO, having efficient corrective actions in place, self-reporting and having resilient processes in place. Aggravating factors include repetitive or persistent non-compliance, significant divergence from the acceptable pricing range, delays in taking corrective action, failure to implement a resilient/ robust process, aggravating actions or failure to act in a timely manner after becoming aware of the breach either before or during NESO's investigation.

**Possible sanctions:** No action; No availability fee for affected service window; Refer to Ofgem (via Market Monitoring team). If same or similar facts in preceding 90 days (same or different asset), then also: Deregister relevant asset on SMP from affected service; Deregister provider on SMP from affected service; Deregister provider on SMP for all services.

### Worked examples *[s.66–77; condensed to inputs, checks and outcome. Prices are purely fictional in the source; BOA timings include ramps.]*

**Example 1 – Managing State of Energy (BESS)** *[s.66–67]*
- Unit: BESS, max generation capacity 20MW; linear run-up rate 10MW/minute; no response contracts; contracted for 10MW PSR in Service Windows 27-30; MZT = 0 mins; NTO/NTB = 0 mins; 10MWh stored energy at 12:00. 0 PN from 12:00 - 13:00; provider has also submitted a -10MW PN for 13:00. Control Room send a 23-minute BOA @12:12 for 10MW through the BM. BESS unit has limited the offered PSR capacity such that it could sustain full delivery for all contracted windows.
- Settlement metering: SW27 (12:00–12:30) = 2.917MWh; SW28 (12:30–13:00) = 0.750MWh.
- Checks (SW27-30): Availability MEL – FPN ≥ 10MW → (10 – 0) ≥ 10 → CORRECT. Time to full delivery (10 / 10) + 0 ≤ 15 → CORRECT. Recovery Period 0 ≤ 60 → CORRECT. Ramp rates: NTO/NTB ≤ 10 mins → No Ramp check required.
- Utilisation: SW27 2.917 – 0 ≥ 2.917 * 0.95 AND ≤ 2.917 * 1.2 → 2.917 ≥ 2.771 AND 2.917 ≤ 3.500 → CORRECT. SW28 0.750 ≥ 0.713 AND 0.750 ≤ 0.900 → CORRECT.
- Payment: clearing price £19/MW/hour; for each contracted window (£19*10)/2 = £95.00. Utilisation – BOAs are settled by Elexon.

**Example 2a – Using price bands to manage state of energy (30-minute MEL)** *[s.68–69]*
- Unit: BESS, max generation capacity 30MW; run up rate 30MW/minute; no response contracts; contracted for 10MW PSR in SR Service Window 28-31; MZT = 0; NTO/NTB = 0; 15MWh stored energy at 12:00.
- SW27 (uncontracted): the control room requires volume in SW27 to manage system conditions – the BESS is dispatched via the BM for 20MW across the two price bands at 12:00 and 12.10 for 5 minutes each. Unit submits MEL to 10MW to protect state of charge going in to contracted SR window. Later, unit submits MEL to 0MW, offering contracted 10MW positive Slow Reserve from charging PN.
- Settlement metering: SW27 = 2.888MWh; SW28 = 0MWh.
- Checks: SW28 Availability (10 – 0) ≥ 10 → CORRECT; SW29 Availability (0 – (-10)) ≥ 10 → CORRECT. Recovery 0 ≤ 60 → CORRECT. Time to full delivery (10 / 30) + 0 = 0.33 ≤ 15 → CORRECT. Utilisation: 0 BOA volume → PSR NOT CHECKED. Assumed also complied with MNZT, Bid-Offer and Cease time Checks.
- Payment: clearing price £5/MW/hour; per window (£5*10)/2 = £50.00. Total Availability from NESO for SW 28-31 → £200.00.

**Example 2b – as 2a but MEL set too low** *[s.70–71]*
- As 2a, but 5MWh stored at 12:00 and the unit submits MEL to 5MW to offer available volume during SR window.
- SW28 Availability (5 – 0) ≥ 10 → FAILED. SW29-31: same as example 2a.
- Total Availability → £150.00 (SW28 failed, SW29-31 passed).
- Note: We consider SW28 failure "commercial unavailability" as the unit was dispatched by NESO through a BOA during an uncontracted Settlement Period which led to its energy limitations (see 8.1 in the SR service terms). The unit did not maintain its state of charge correctly ahead of a contracted Reserve service. Therefore, the unit is at risk of being levied a cost of reimbursement for replacing the reserve volume which has been exhausted.

**Example 3 – Headroom and Footroom checks (CCGT)** *[s.72–73]*
- Unit: CCGT, max generation capacity 150MW, SEL 50MW; run-up and run-down rate 5MW/minute (not subject to maximum ramp rate checks as notice period ≤10 mins); contracted for 25MW PSR and 25MW NSR in SR Service Windows 20 - 34; MZT = 2 minutes; NTO/NTB = 0. The control room requires negative SR volume in SW27; the CCGT is dispatched for bid volume @12:25 for 45 minutes.
- Settlement metering: SW27 = 61.458MWh; SW28 = 50.000MWh; SW29 = 59.375MWh.
- Checks (SW27-29): Availability MEL – FPN ≥ 25MW → (150 – 125) ≥ 25 → CORRECT; FPN – SEL ≥ 25MW → (125 – 50) ≥ 75MW → CORRECT. Recovery 2 ≤ 60 → CORRECT. Time to full delivery (25 / 5) + 0 = 5 ≤ 15 → CORRECT.
- Utilisation (NSR): SW27 ABS(61.458 – 62.500) = 1.042 ≥ 0.99 AND ≤ 1.25 → CORRECT. SW28 ABS(50.000 – 62.500) = 12.5 ≥ 11.875 AND ≤ 15.00 → CORRECT. SW29 ABS(59.375 – 62.500) = 3.125 ≥ 2.969 AND ≤ 3.75 → CORRECT. *[The source writes the inequality signs the other way round in the first line of each check; the evaluated lines are as above.]*
- Payment: clearing price £6/MW/hour; (£6*25)/2 * 2 = £300 per SW. Total Availability SW27-29 → £900.00.

**Example 4 – Ramp rate checks (CCGT)** *[s.74–75]*
- Unit: CCGT, max generation capacity 20MW, SEL 10MW; run-up and run-down rate 20MW/minute for all SR Windows; contracted for 10MW PSR in SR Service Windows 20 - 34; MZT = 30 minutes; MNZT = 30 mins; NDZ = 11 mins. The CCGT is sent a dispatch instruction at 12:14 for 10MW for 45 minutes; unit begins to ramp at 12:25, honouring its 11 min NDZ.
- Settlement metering: SW27 = 0.792MWh; SW28 = 5.000MWh; SW29 = 1.625MWh.
- Checks: Availability (20 – 0) ≥ 10 → CORRECT. Recovery 30 ≤ 60 → CORRECT. Time to full delivery (10 / 20) + 11 = 11.5 ≤ 15 → CORRECT. **Ramp rate check (as NDZ > 10):** Ramp rate ≤ Contracted MW / min AND ≤ 50% Contracted MW per 30s period → 20 ≤ 10 AND 10MW per 30s period ≤ 5 → FAILED. Utilisation SW27–29 → CORRECT (0.792 ≥ 0.753; 5.000 ≥ 4.75; 1.625 ≥ 1.544, each within 120%). *[Source labels these "Utilisation (NSR)" although the contract is PSR.]*
- The unit fails ramp rate checks but remains available to the control room. Payment: (£6*10)/2 = £30 per SW expected; Total Availability SW27-29 → £0.00.

**Example 5a – Excessive Pricing: no action** *[s.76; values illustrative]*
- Provider A – BM Unit X (OCGT) wins a Slow Reserve Contract for 08 Jan 2025 SP33; BM Offer price £400.
- Stage One: Price Threshold Formula result £215.96; offer price is greater than threshold, stage 2 assessment is required. Stage Two: Day Ahead Nordpool Price = £330.07; Average Intraday price = £977.92; Peak BM Price = £5,750. A day of tight margins; average intraday price was higher than the BM offer price of £400, which can be understood as Provider A pricing according to market conditions.
- Outcome → No action.

**Example 5b – Excessive Pricing: sanction** *[s.77; values illustrative]*
- Provider B – BM Unit Y (OCGT) wins a Slow Reserve Contract for 09 Jan 2025 SP31; BM Offer price £600.
- Stage One: threshold £414.44; offer price greater than threshold. Stage Two: Day Ahead Nordpool £104.42; Average Intraday £103.16; Peak BM £144.9. Provider B offer pricing exceeded market prices; no unplanned/planned EDL BM outages observed that could have impeded the provider adjusting MIL/MEL to reflect unavailability. Stage Three: Provider B declared that BM price was used to discourage BOA. Stage Four: first offence; after becoming aware of the failure provider has put corrective action in place.
- Outcome → No availability fee for affected service window. Incident recorded in case of further breaches.

## 9. Settlement

### Availability Payments *[s.79]*

- The day ahead SR auction is Pay-as-Clear.
- Forty-eight 30-minute service windows for both Positive Slow Reserve and Negative Slow Reserve, running 23:00-23:00 (UK local time).
- Market participants submit sell orders for SR (including availability prices and offered volumes) before 14:00 Gate Closure time.
- NESO submits a buy order which represents the willingness to pay for a given volume of firm SR volume.
- An auction is conducted by auction partners NSIDE using the EAC algorithm via a co-optimised auction for Balancing Reserve, Quick Reserve, Slow Reserve and Response run in the afternoon.
- A cohort of accepted sell orders and buy orders is determined to maximise market welfare.
- A clearing price is determined to maximise market welfare whilst minimising total cost of procurement.

All successful providers for each firm Service Window will be paid the clearing price for that Service Window (subject to contract compliance). Detailed information about the day ahead auction: EAC market explainer, `https://www.neso.energy/document/277671/download`.

### Utilisation Payments (BM) *[s.80]*

- Utilisation of SR is through bids and offers in the BM and applies to both firm and optional participants.
- Holding a SR contract is not a guarantee of dispatch – in some periods, reserve will not be required and/or the unit may not adequately meet the system need (e.g. we may not be able to dispatch units located behind constraints).
- Submitted dynamic parameters MEL, MIL, SEL, SIL, MNZT, MZT, NTO, NTB, NDZ, Run-up/Run-down rates, FPN, etc., should reflect contract terms.

Payments for BM utilisation are made from ELEXON via the usual BOA settlements processes.

*[Chart (not captured): BOA sent at SP2+:07, unit at full delivery SP2+:15, unit back to FPN SP5+15, followed by Max Recovery Period; contracted vs uncontracted SR windows shown against MEL and FPN.]*

### Utilisation Payments (NBM) *[s.81]*

- Holding an SR contract is not a guarantee of dispatch – in some periods, reserve will not be required and/or the unit may not adequately meet the system need (e.g. we may not be able to dispatch units located behind constraints).
- Pre-qualification parameters should reflect the prevailing Service Terms published on the Slow Reserve webpage.
- Payments for utilisation are made from NESO via the usual settlements processes.
- Where a unit is instructed, Expected, Delivered and Capped Energy delivered MWh are computed for each second that metering data is required to be provided e.g. at 0,15.30,45 seconds.

| Service | Payment per second | Capped Energy Delivered |
|---|---|---|
| Positive | Capped Energy Delivered (MWh) * Applicable Utilisation Price | Min(Delivered, Expected) |
| Negative | - Capped Energy Delivered (MWh) * Applicable Utilisation Price | Max(Delivered, Expected) |

- Note 1: If the utilisation occurs in a Firm Service Window, then this would be classified as Firm Service Delivery and will be stored against a different payment code to Optional Reserve service delivery.
- Note 2: On the payment report; data is aggregated per settlement period, per instruction, with start and cease ramping periods separately reported.
- Note 3: It is feasible for there to be multiple instructions in a settlement period.
