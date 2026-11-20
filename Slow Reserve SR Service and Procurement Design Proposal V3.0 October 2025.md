# Slow Reserve (SR) Service and Procurement Design Proposal – Version 3.0 (October 2025)

> **Source file:** `slowreserveSTs.txt` (NESO PDF, 38 pages, copy-pasted). *[The file name suggests Service Terms, but the document is the Design Proposal; the Service Terms are in `Slow Reserve SR Service Terms V1.0.md`.]*  
> **Status:** Explanatory design document. Per its own purpose statement it "supports the SR Service Terms and Procurement Rules as published on the NESO website", following Ofgem's approval on 9 October 2025 of NESO's EBR Article 18 consultation for SR. It pre-dates Service Terms V1.0 (published 16 March 2026); where they differ, the Service Terms govern.  
> **Converted:** 2026-10-29. **Condensed, not a full transcript.** Substantive wording kept verbatim. Removed: page numbers, contents list, the transition-plan placeholder, design rationale and history paragraphs (each replaced by a one-line *[summary]*), infographic references, the acronym list, and the tail of Appendix 1 (BC1 definitions shortened). Notes in *[italic square brackets]* are editorial; *[p.N]* gives the original page.

---

## Key terms *[p.2]*

| Term | Meaning |
|---|---|
| SR Contract(s) | Contract(s) for the delivery of Slow Reserve from an Auction Unit either formed through the daily auction (Firm Service) or upon utilisation by NESO of the Optional Service. |
| Contracted Service Period | An SR Window which is the subject of an SR Contract as procured through the daily auction (Firm Service). |
| SR Window(s) | Each consecutive thirty (30) minute period commencing at 23.00 hours. This is equivalent to each Settlement Period in an EFA day. |
| Service Window Block | SR Auction bids for a continuous period of not less than two (2) hours in duration comprising consecutive SR Windows with identical MW. |

## 1. Introduction *[p.5]*

Slow Reserve (SR) is primarily aimed at reacting to post-fault disturbances to restore energy imbalances to +/- 0.2Hz of 50Hz within 15 minutes of a loss event (generation or demand). For Negative Slow Reserve (NSR), units are instructed to increase demand or decrease generation in full within 15 minutes. The inverse is true for Positive Slow Reserve (PSR). SR is open to any technology with the ability to provide net change in demand/generation of at least 1MW. Slow Reserve will ultimately replace the legacy Short Term Operating Reserve (STOR) service.

| Requirement | STOR | Slow Reserve |
|---|---|---|
| Direction | Positive only | Positive & Negative |
| SR Window (previously STOR Service Windows) | Seasonal variations, 2 windows a day, ~4 hours each. Must deliver for min 2 hours once instructed | Any 4 or more contiguous SR Windows. Unit must be able to deliver for all SR Windows |
| Operational day | 05:00 – 05:00 | 23:00 – 23:00 |
| Recovery Period | ≤1200 minutes | ≤60 minutes |
| Time to full delivery | ≤20 minutes | ≤15 minutes |
| Minimum Capacity | 3MW | 1MW |
| Baselining | From-zero | Non-zero baselines allowed |
| Payments | Availability + Utilisation | Availability + Utilisation |
| Metering | Every 60s (0.01667 Hz) | Every 15s (0.0667 Hz) |
| Aggregation | Allowed, nationally | Allowed, per GSP group |
| Procurement | Daily, D-1 with a further 400MW of legacy 'long-term' contracts | Daily, D-1 |

## 3. Technical Design Summary *[p.7]*

| Technical Design Element | Proposal |
|---|---|
| Direction | Positive and Negative |
| Provider Eligibility | NBM & BM units with control/system telephony during contracted periods |
| Time to full delivery | Up to 15 minutes from instruction receipt |
| Minimum Activation Period | Not greater than 30 minutes |
| Maximum Recovery Period | Not greater than 60 minutes |
| Energy Requirement | The unit must be able to deliver the full contracted capacity |
| Operational Metering | 0.0667 Hz / once per 15s for both BM and NBM units |
| Dispatch mechanism | BOA for BM units; OBP dispatch instruction for non-BM units |
| Notice to Start Ramping | Up to 14 minutes |
| Time to accept instruction | Up to 2 minutes |
| Ramp rates | Max ramp rate of 100% contracted capacity per minute. For max instantaneous ramp rates, unit cannot deliver >50% contracted capacity in any 30s ramping period. |
| Performance Metering | 0.0667 Hz / once per 15s for both BM and NBM units |
| Performance Monitoring | Time to Full Delivery, Availability, Ramp Rates and Utilisation – Penalties for over (>120%) and under (<95%) delivery |
| Baselining | All providers must submit a nomination baseline, equivalent to the BM Physical Notification, with Final Physical Notifications by gate closure. Both zero and non-zero baselines allowed |
| Aggregation | Yes, per GSP group |
| Operational data requirements | BM units as per current BM operations. Non-BM units to submit relevant operational data |
| Ramp rates for baselines | Aligned with Dynamic Response – no limit |
| Passing through zero | Allowed |

## 4. Procurement Design Summary *[p.8]*

| Procurement Design Element | Proposal |
|---|---|
| Firm Requirement | Minimum 2-hours (4 contiguous SR Windows) |
| Maximum Bid Size | N/A |
| Frequency of Procurement | Daily (day-head) – SR Contract firm procurement. Within day – optional procurement (non-BM only). |
| Locationality | National |
| Auction Platform | EAC |
| Auction Timing | Auction close by D-1, 14:00 (co-optimised) |
| Stacking & Splitting | Same MW cannot be sold twice. |
| Bid Sizing | ≥1MW, integer bids |
| Linking of bids | Allowed by service and Product (Positive/Negative only) |
| Bid Curtailment Rules | User defined |
| Payment Structure | Firm: Availability + Utilisation. Optional (non-BM only): Utilisation only |
| Payment Mechanism | Availability: Pay-as-Clear. Utilisation: Pay-as-Bid |

## 5. Technical Design

### Key features *[p.9–10]*

- The service is open to BM (Balancing Mechanism) and non-BM (non-Balancing Mechanism) market participants.
- SR units must have a minimum 1MW capacity of generation reduction/increase or demand reduction/increase from any technology. The unit can be a single asset or an aggregated unit (at GSP group level) comprising more than one constituent asset. BSC aggregation rules apply for BM units.
- All Slow Reserve units must be able to:
  - Submit relevant service parameters, location, and prices (similar to the Balancing Code requirements).
  - Achieve full delivery of contracted capacity within submitted data, if instructed.
  - Achieve full delivery of contracted volume in 15 minutes from instruction receipt or less, including notice time. Ramp rate limits apply.
  - Units with a >10-minute notice period must restrict ramp-up and ramp-down delivery rates to 100% contracted capacity per minute. For instantaneous ramping (for units that cannot ramp linearly), the ramp cannot exceed >50% contracted capacity in any 30-second period. There are no restrictions on ramp-up and ramp-down rates for units with a ≤10-minute notice period.
  - Have the Minimum Activation Period not greater than 30 minutes and Maximum Recovery Period not greater than 60 minutes.
  - Submit Physical Notifications and Operational Metering appropriately.
- Units can be aggregated at GSP Group level to meet the 1.0MW minimum participation threshold, with location submitted during pre-qualification.
- There is no restriction on the maximum size a participating unit can bid up to. Contracts will be awarded upon acceptance of bids (SR Contracts) in whole MWs (minimum 1MW) submitted into the daily auction.
- Providers with a SR Contract will receive an availability payment (£/MW/hour) for the Firm Service and a utilisation payment (£/MWh) if dispatched, subject to Availability and Utilisation checks.
- Providers must deliver metering data with a minimum granularity of no less than once every 15s at a latency of no more than 5s. This is inclusive of BM and NBM providers. Providers may submit at a higher granularity (i.e., 1Hz) should they wish. The requirement is specified at the unit level, and it is possible with staggered polling with a large enough group of assets to achieve the required accuracy and latency with assets that have less granular metering.
- **BM units need to provide NESO with dynamic parameters as defined in BC 1.A.1.5. Dynamic Parameters and Physical Notifications are to be submitted 24 hours in advance, with Final Physical Notifications by gate closure and relevant price bands.**
- **Non-BM units must submit all relevant non-BM service parameters during all contracted windows along with Physical Notifications submitted at day-ahead, with final notifications 60-minutes ahead of gate closure and relevant pricing. For crossover purposes, non-BM units must also submit Availability, Final Physical Notifications, and relevant pricing post-contracted/optional windows for control room visibility and performance monitoring purposes.** *[Bold added. "60-minutes ahead of gate closure" is as printed; Service Terms 20.1–20.2 and the Guidance put the lock at 60 minutes ahead of the SR Window / Settlement Period, i.e. at Gate Closure.]*
- Stacking with other active power ancillary services will be limited for initial launch, however, co-delivery with the Capacity market and Balancing Mechanism are allowed. Units may also only split their Slow Reserve capacity with opposite Slow Reserve (e.g., Positive with Negative), Voltage and Stability services along with the Balancing Mechanism.
- NBM providers will have their energy position corrected through the ABSVD process.
- SR units will be performance monitored using performance metering data, at 0.0667 Hz/once per 15s, submitted after the contracted day to be evaluated on availability, ramp rates, time to full delivery and utilisation. If stacking with any other ancillary services or markets, then the more granular metering is applicable and should be submitted to NESO.
- All SR providers have up to 2 minutes to signal to NESO that they have received and accept the SR instruction. Time to Full Delivery is inclusive of these 2 minutes.

### Provider Eligibility *[p.10–11]*

To participate in the Slow Reserve market, providers must:
- have control telephony for the entire duration of a Contracted service period, which could be Control Telephony or System Telephony as per Grid Code definitions. For non-BM this will require an operational telephone so that NESO can contact the non-BM unit to allow for dispatch during planned or unplanned outages of the OBP system interface.
- be capable of providing 1MW or more of reserve volume in line with the service design. Bids must be made in integer MWs.
- Complete the Slow Reserve pre-qualification registration process through our Single Market Platform (SMP).
- Non-BM providers will be required to complete onboarding to the Open Balancing Platform (OBP) as part of pre-qualification.

Both BM and non-BM participants with a connection to either the electricity transmission or distribution network will be eligible to provide Slow Reserve.

### Service Utilisation & Dispatch Mechanism *[p.11]*

Utilisation for BM units is in line with normal Balancing Mechanism operation in accordance with BC2 via Bid-Offer Acceptances. Dispatch instructions to BM providers will be by way of Bid-Offer Acceptances (BOAs) via EDT/EDL or telephone instruction if required.

Non-BM providers are dispatched via the Open Balancing Platform (OBP) system and will be issued a start instruction followed by a stop instruction at a later point. The Start and Stop instructions may be sent in advance, with an effective date-time for action. The non-BM providers control point will need to receive these instructions and only action at the specified effective date-time points.

### Timing parameters *[p.11–12]*

- **Time to Full Delivery:** 15 minutes or less, inclusive of any notice to start ramping, i.e., NDZ and/or NTO/NTB or equivalent, and time to accept instruction. That is to say, the unit must be capable of reaching its full contracted output within 15 minutes of instruction receipt.
- **Notice to Start Ramping:** no longer than 14 minutes from instruction receipt. This includes, where applicable, a unit's NTO, NTB, NDZ, and Time to Accept Instruction, or equivalent for NBM. Non-BM units are not required to provide an NTS as this is already submitted via the prequalification process.
- **Time to Accept Instruction:** all units must send an acceptance of a Slow Reserve instruction within 2 minutes of receipt. A unit's Time to Full Delivery is inclusive of this time to accept requirement.
- **Cease Time:** defined as the converse of Time to Full Delivery. That is, the time a unit takes for a unit to ramp down from a Slow Reserve request ending to its FPN. A unit therefore has up to 15-minutes from a Cease Instruction start time to return to its PN and includes all notice periods.
- **Minimum Activation Period (MAP):** the minimum duration for which an instruction can be issued, and it is specified by providers. Slow Reserve providers will be able to specify a MAP of between 1 and 30 minutes inclusive. A unit's MAP is inclusive of any ramping.

### Energy Requirements *[p.13]*

Participating Slow Reserve units must be able to deliver the full contracted MW capacity for the entire Contracted Service Period. A participating SR unit must therefore be capable of delivering the service for any length of time between its defined MAP and the full offered Contracted Service Period. Providers can offer capacity into the SR service via the day-ahead auction for as long as they wish, provided it is for a minimum of 4 (four) contiguous SR Windows (Service Window Block) and/or in line with any Linking Notice published by NESO, and such that delivery can be sustained for the entire offered duration. Providers may also offer optional SR capacity within-day for any relevant SR Window with no minimum duration requirement.

### Recovery Period *[p.13]*

The maximum Recovery Period for positive and negative Slow Reserve is 60 minutes. This means that an asset has 60 minutes to return to availability before NESO can send another dispatch instruction. *[Rationale summarised: no active participants excluded; revised from 30 to 60 minutes after industry feedback; lets the control room secure the system within gate closure timeframes; acts as an anti-gaming measure against extended Recovery Periods.]*

### Ramping Envelope *[p.14]*

- For those units with a Notice to Start Ramping period of >10 minutes, the maximum ramp rate limit is set at ≤100% contracted capacity per minute. For instantaneous ramping (for units than cannot ramp up linearly), the unit cannot deliver more than 50% of the contracted capacity in any 30-second period.
- For those units with a Notice to Start Ramping period of ≤ 10 minutes, there is no maximum ramp rate limit.
- The minimum ramp rate is directly set from the time to full delivery - a unit may not deliver at a rate of less than 100% per 15 minutes. This applies to both ramp-up and ramp-down periods.
- The unit may start delivery immediately after accepting a dispatch instruction.

The maximum ramping from the instruction must have the identical envelope in the opposite direction.

### Ramp rates for baselines for energy limited assets *[p.14–15]*

Slow Reserve ramp rates for baselines are aligned with the Dynamic Response services. Ramp rates for baselines are therefore not required for Slow Reserve until such time as if and when these requirements are updated for the Dynamic Response services, should they be required for system security purposes. *[History summarised: the former Dynamic Response 5%-of-contracted-MW/minute Maximum Ramp Rate on baselines, introduced against herded energy recovery, was removed from the DR Service Terms and so not carried into SR; subject to review and may become a future requirement.]*

### Operational Dataset Requirements *[p.15]*

BM units are required to submit operational data in accordance with current BM obligations. Non-BM units must submit availability declarations (including price and MW), PN's, and Operational Metering.

### Availability Declarations (technical) *[p.15–16]*

BM providers should submit their Availability Declarations as per the Grid Code (BOAs). Non-BM Availability Declarations are required for each Contracted Service Period (and/or where declaring optionally available), and should consist of: 1. Unit ID; 2. Service; 3. Breakpoint (MW); 4. Utilisation Price; 5. Start Datetime; 6. End Datetime.

### Operational Metering *[p.16–17]*

All providers (BM and non-BM) are required to submit operational metering at a minimum frequency of once per 15 seconds (0.0667Hz) with a latency of no greater than five (5) seconds whilst providing the service. All operational metering, including active power and system frequency data, should be provided at an accuracy according to the relevant Code of Practice (e.g., 1.0% for assets >10MW & ≤100MVA).

- **BM Units:** should submit operational metering in accordance with the Grid Code and via existing processes.
- **Non-BM Units:** should submit Operational Metering as detailed in the 'Operational Metering for non-transmission connected BM & Non-BM Participants' documentation. Where one or more contracts have been awarded, Operational Metering is required for all SR Windows in the Service Day. For the Optional Service, Operational Metering is required where a unit is declared optionally available and for the immediate SR Window that follows (see Crossover section). For the avoidance of doubt, Operational Metering is also required for the first SR Window in the subsequent Service Day if a contract (or optionally available) is held in the final SR Window of a Service Day for Crossover purposes.

### Physical Notifications (Operational Baselines) *[p.17–18]*

Physical Notifications (PN) are defined in the Grid Code as a forecast or an indication of the generation or demand levels a unit expects to operate at during specific periods. Physical Notifications are required by NESO for real-time operational awareness, margin assessments and during the settlements process.

All providers will be expected to provide a PN, giving a forward-looking view of unit output and is locked in for the forthcoming two SR Windows (Settlement Periods) at Gate Closure.

**BM Units:** Should continue to submit Physical Notifications in accordance with Grid Code and via the existing processes.

**Non-BM Units:** Physical Notifications are to be submitted to the Open Balancing Platform (OBP) as detailed in 'OBP Web Services Specification', and should consist of: 1. Unit ID; 2. PN Start (MW); 3. PN End (MW); 4. PN Start datetime; 5. PN End datetime.

Where a Firm SR Contract is held:
- Where one or more firm SR Contracts held in a Service Day (23:00 – 23:00), a PN is required for each SP of that Service Day. The 48 PNs (or 46/50 as applicable for clock change days) for the subsequent Service Day should be submitted within 2 hours of the contract award (Daily Auction), nominally 16:30 each day. If the unit has a contract for the last SR Window of the Service Day, then the PN for the 1st SR Window of the following Service Day is also required for Crossover purposes.
- The provider will have the opportunity to submit/update its PN (or FPN) up to 60-minutes ahead of gate closure for the relevant Contracted Service Period, plus the subsequent SR Window. **If there is no (F)PN submitted by this time, then the unit will be dispatchable but will not receive an availability fee.**

For the Optional service:
- Where a unit does not hold a firm contract for any period in a Service Day (23:00 – 23:00), but makes itself optionally available, a PN is required only for the optionally declared SR Window(s), plus the subsequent SR Window for Crossover purposes.

### Performance Metering *[p.18–19]*

All providers (both BM and non-BM) are required to submit data to NESO for real-time monitoring of service availability and post-event performance monitoring.

- Where a SR Contract is held: a Performance Metering file for all contracted SR Windows in the Service Day and for any SR Window where a Crossover occurs (including the 1st SR Window of the following Service Day if applicable).
- For the Optional service: Performance Metering file for all SR Windows where the Optional Service is utilised and for any SR Window where a Crossover occurs (including the 1st SR Window of the following Service Day if applicable).

All files must be submitted by no later than one calendar day (24 hours) after the end of the Service Day on which SR was provided. Where no valid Performance Metering file has been received within one day (24 hours) after the end of the Service Day on which SR was provided, NESO will withhold Availability Payments (where applicable) and for non-BM, no Energy Utilisation Payments in respect of the Service Day will be paid (no data to assess availability and derive energy delivery). Where, due to a fault, the file is unavailable for submission by the agreed IT interface, the Service Provider can agree with NESO to submit alternative Performance Metering data by not later than five calendar days after the Service Day on which SR was provided.

### Publication of Data *[p.19]*

We publish (or intend to publish at a future time) on the NESO data portal the following non-anonymised data relating to all SR units providing the service, where this data is not already published pursuant to the BSC: Operational Baselines; Operational Metering Data; Performance Metering Data; SR Unit availability for Slow Reserve (comprising Contracted or Optional MW); SR Utilisation Price; Details of instructions issued.

### Performance Monitoring *[p.19–21]*

NESO will monitor the availability of units in order to confirm that they are holding sufficient headroom/footroom and can therefore deliver their contracted MW if instructed. We will evaluate the conditions below for each Contracted Service Period, individually. Failure to deliver at 100% of contracted availability will result in the Availability Payment being withheld for all relevant SR Windows.

A unit must make available the contracted MWs for the required service(s) within the specified SR Window(s), and NESO should not have to send an instruction greater than or less than a unit's contracted capacity due to a limitation of the unit:
1. Where a provider declares LESS than their contracted MW – the declared volume remains available to NESO, however the provider has not met its contracted obligation and therefore receives no availability payment. It will however receive payments for any instructed utilisation.
2. Where a provider declares MORE than their contracted MW – same consequence.

*[Tables below: "% of availability payment received" / "K factor" is 100 / 1 when the condition holds and 0 / 0 when it fails.]*

| Positive Reserve – BM: Provider Type | Pass condition (100%, K=1) | Fail condition (0%, K=0) |
|---|---|---|
| Generator, Through-zero | MEL – PN ≥ (Contracted Volume) | MEL – PN < (Contracted Volume) |
| Generator, From zero | SEL ≤ (Contracted Volume) | SEL > (Contracted Volume) |
| Through-zero (further) | SIL – PN ≥ (Contracted Volume) or SEL – PN ≤ (Contracted Volume) | SIL – PN < (Contracted Volume) or SEL – PN > (Contracted Volume) |
| Supplier | SIL – PN ≥ (Contracted Volume) | SIL – PN < (Contracted Volume) |
| Intermittent Generator | PA – PN ≥ (Contracted Volume) | PA – PN < (Contracted Volume) |

| Negative Reserve – BM: Provider Type | Pass condition (100%, K=1) | Fail condition (0%, K=0) |
|---|---|---|
| Generator, Intermittent Generator | PN – SEL ≥ (Contracted Volume) | PN – SEL < (Contracted Volume) |
| Supplier, Through-zero | PN – MIL ≥ (Contracted Volume) | PN – MIL < (Contracted Volume) |
| Through-zero (further) | PN – SEL ≥ (Contracted Volume) or PN – SIL ≤ (Contracted Volume) | PN – SEL < (Contracted Volume) or PN – SIL > (Contracted Volume) |

| Positive & Negative Reserve – NBM: Provider Type | Pass condition (100%, K=1) | Fail condition (0%, K=0) |
|---|---|---|
| Generator, Supplier, Intermittent Generator | (Available Volume) ≥ (Contracted Volume) | (Available Volume) < (Contracted Volume) |

That is to say: the available capacity should be ≥ the SR Contract volume; the minimum instructible capacity should be ≤ the SR Contract volume.

### Service Delivery *[p.21–23]*

NESO will conduct performance monitoring of service delivery for all SR Contracts.

- **Under-delivery:** Where a unit has a SR Contract, a minimum 95% of instructed MW must be delivered by the relevant unit throughout the instructed period. Failure to deliver will result in Availability Payments being withheld for the relevant SR Contract(s) (Firm Service). Utilisation payments for SR Contracts and Optional Services (Non-BM only) will be made for energy delivered.
- **Over-delivery:** Where a unit has an SR Contract, a maximum of 120% of instructed MWs can be delivered by the unit throughout the instructed period, delivery beyond 120% will result in availability payments being withheld for relevant SR Contract(s) (Firm Service). Utilisation payments for SR Contracts and Optional Services (Non-BM only) will be made for energy delivered.

For the avoidance of doubt, availability payments will be made when a unit delivers between 95% and 120% of its instructed MW volume. Where a unit delivers outside of these limits, the Availability Payment will be withheld for the relevant Settlement Period(s).

The ramp rate limit for units with a notice period of >10 minutes is set to no more than 100% contracted capacity per minute, with no single instantaneous ramp more than 50% of the contracted capacity in any 30-second period; this applies to any viable point within the acceptable ramping envelope defined.

In addition to performance penalties, NESO will conduct regular performance monitoring of reserve units' service delivery over a greater period than the individual service day in order to establish overall delivery against the 95%-120% performance measure. There will be no further financial penalties associated with this monitoring, but to ensure that we do not award Slow Reserve contracts to Reserve units with continued poor performance, we will link the performance monitoring to the Reserve unit's prequalification status. Depending on the root cause, we would expect either a reproving test or possibly revised base parameters (e.g., reduced maximum MW) before we would reconfirm prequalification status and access to the daily auction process.

Additionally, Providers who do not fulfil their SR Contract and do not provide the contracted capacity may be responsible for covering costs of alternative actions for replacing the missing volume. Furthermore, the providers will be penalised for over/under-delivery when utilised via the usual route of imbalance charges, giving a natural incentive for units to follow expected delivery profiles. ABSVD methodology will apply to non-BM providers for delivered energy volumes.

### State of Energy Management *[p.23–24]*

Regardless of technology type, we expect all SR units to be capable of delivering the full contracted quantity for the duration of each SR Contract, whether Firm or Optional and that capability shall not impair any subsequent SR Contract.

Through our learning from other Balancing Services we have identified instances where some energy limited assets have had insufficient energy to honour their full contracted period and have maintained market positions (such as discharging PNs) and increased their Bid-Offer prices during contracted periods such that their high prices make the units unlikely to be selected as they are economically out of merit, but ensure they continue to receive the capacity Availability Payments.

We believe that withholding the Availability Payment does not provide a sufficient sanction to deter this behaviour. Therefore, for Slow Reserve, we are utilising terms, as seen in the Quick Reserve service, that deal with excessively high or excessively low Bid-Offer prices and provide NESO, at our discretion, with a range of enforceable sanctions. We intend to introduce a similar method of recovering the cost of alternative action needed to be taken and, at our discretion, will treat instances of unavailability for a SR Contract, due to insufficient state of charge, as commercial unavailability and penalise with the cost of alternative action taken.

### Crossovers, Aggregation, Heartbeat *[p.24]*

- **Crossovers:** When instructed, the unit must be able to continue delivering a dispatch instruction into the next SR Window. (Additional guidance on Crossover operation is published on the Slow Reserve webpage.)
- **Aggregation:** Aggregated units can participate in the Slow Reserve auction. The aggregation will be allowed up to GSP group which is in line with our Grid Code requirement for aggregated BMUs.
- **Heartbeat:** The 'Heartbeat' also referred to as the 'Connection Indicator' is used to ensure that NESO control-room has visibility that a unit remains dispatchable. For BM this should be as per Grid Code. For non-BM units, details to provide the 'Heartbeat' can be found in the published Web Specification.

## 6. Procurement Design

### SR Contract (Firm Service) *[p.25]*

NESO will consider Slow Reserve volumes required for each Settlement Period in a service day (23:00 to 23:00) and this will be procured through the daily auction. Where there is a firm requirement in a Settlement Period, this will be defined by NESO and published on the NESO website. Providers will be able to bid in their SR units to the daily auction for a minimum of 4 (four) contiguous SR Windows (Service Window Block). Where there is a firm requirement and units are awarded SR Contracts for a Service Window Block via the daily auction, this will be known as the Firm Service with contracts awarded for each discrete SR Window. This commits the SR unit's availability for the full Contracted Service Period and the service provider will receive availability payments (pay-as-clear) for each SR Contract along with any relevant Utilisation Payments (pay-as-bid) if dispatched.

### Optional Service *[p.25]*

Where NESO do not specify a firm requirement for a Settlement Period at day-ahead or the service provider has been unsuccessful in the daily auction, SR units will be able to submit utilisation-only bids for the Optional Service within-day for any relevant SR Window(s) with no minimum duration requirement. That is to say, valid Optional Availability declarations can be as short as one Settlement Period. If SR units are dispatched under the Optional Service, service providers will receive a Utilisation Payment (pay-as-bid) only. BM units should continue to offer reserve to NESO via the Balancing Mechanism and will be dispatched via Bid Offer Acceptances (BOAs).

### Registration and Prequalification *[p.25–26]*

Registration and pre-qualification for Slow Reserve services will be completed via NESO's Single Market Platform (SMP). Providers will be expected to register their units by supplying the following parameters:
- **Unit Data:** Provider Name; Unit ID; Generation & Demand Capacity; Fuel Type; DNO; GSP; Nearest node.
- **Prequal Data:** Service Capacity; Service Type; Prequal Start date; Prequal End date; Response Time (seconds); Time to Full Delivery (seconds); Minimum Activation Period; Cease Time (seconds); Recovery Period; Maximum Utilisation Period.

### Maximum Bid Volume and Procurement Requirements *[p.26]*

There is no restriction on the maximum size a participating unit can bid up to.

The indicative daily requirement for Positive and Negative Slow Reserve following the recent reserve requirement review is 1,800MW and 800MW respectively. NESO will publish separate Market Information Reports on our website which will set out the volume of each Slow Reserve product we will look to procure (Firm Service) each day. *[The April 2026 Guidance gives 1,800MW positive and 1,800MW negative for Day 1.]*

### Daily, co-optimised auction *[p.27]*

As per NESO's obligations under the Clean Energy Package 6.9, we must aim to procure most or all balancing services no earlier than day-ahead. Slow Reserve will be procured along with Quick Reserve, Balancing Reserve and the Dynamic Response services (DC, DM, DR) in a single, simultaneous, day-ahead, pay-as-clear auction with market welfare being maximised across all services, held daily on our EAC Platform in the afternoon. Where a unit can provide both frequency response services, Quick Reserve and Slow Reserve services, a provider can make alternative offers to the auction. The clearing algorithm will allocate the unit's capacity to either Frequency Response, Quick Reserve or Slow Reserve to best optimise the market clearing.

### Bid Submission *[p.27–29]*

A Registered Service Provider can only participate in the daily SR auctions once they have completed pre-qualification. For each product, a sell order will include the required bid parameters, such as the availability price (£/MW/h), the volume (MW), confirmation if the bid is curtailable (the minimum capacity they are willing to accept) and any other additional parameter(s) as may be specified in the relevant Auction Rules. Bid validation, such as checking minimum (MW) not exceeding the pre-qualified asset MW, will be done at bid submission stage.

Each Unit can bid for a minimum of 4 (four) or more consecutive SR Windows within an Operational Day (Service Window Block), starting from any applicable SR Window. Units can submit different MWs for each different Service Window Block but must contain consistent MW per SR Window within each Service Window Block. *[Illustration summarised: Unit 1 one block 17:00-23:00 at a MW; Unit 2 three blocks 17:00-19:00, 19:00-21:00, 21:00-23:00 at b, c, b MW; Unit 3 two blocks 17:30-19:30 and 20:30-23:00 at d MW with a gap between.]*

NESO submits daily buy-orders to the EAC platform which specify a max volume (MW) we are willing to buy at different price levels (£/MW/h) for each product and SR Window. The auction gate will be open in advance such that orders can be submitted 14 days before each auction. Sell-Orders can be submitted, reviewed, modified, or deleted before auction gate closure.

### Assessment Principles and Results *[p.29]*

To secure the system economically, the clearing algorithm will aim to first maximise the Total Welfare, then minimise the overall procurement cost (when there is a choice of clearing prices), as set out in the EAC Market Design Report. A buy curve (generated for each SR Window) will be applied to reflect that the volume NESO is willing to procure varies with price. The cost of taking alternative actions, offered by units of similar capability and services, will be taken into consideration when generating the buy curve. All bids will be ranked in price ascending order against the buy curve to identify the marginal bid.

Auction results can be accessed after each auction via the enduring auction platform nominally by 14:30 and NESO Data Portal by 14:45.

### Linked Sell-Orders *[p.29–30]*

Provider Bids (sell-orders) that are linked can only be accepted or rejected all together. There are two types of linking: link by time (i.e., SR Windows) and link by products (i.e., Positive and Negative Slow Reserve). Thus, linking bids (by SR Window or product) will be permitted for Slow Reserve. *[Rationale summarised: lets providers avoid non-adjacent awards (e.g. SOC management), spread start-up costs, and avoid over-pricing when they want dual-direction awards; positive and negative remain two separately cleared markets, so CEP Art. 6.9 is not breached.]*

### Linked Service Windows *[p.30]*

Crossovers occur at Settlement Period boundaries and require significant consideration during real-time operations. A key risk period for the SR service is during peak periods of demand where there are fewer alternatives available in the market. As a solution to effectively manage these high-risk periods, NESO are introducing Linked Service Windows. Such Linked Service Windows, issued by NESO, state that the submission and/or acceptance of a sell-order is conditional on the submission and/or acceptance of sell-orders of identical MW volume for each SR Window described in the Linked Service Window section. This ensures there are consistent units contracted across key crossover periods. Slow Reserve is planned to go live with this functionality enabled. NESO will assess the requirement for Linked Service Windows and may introduce the requirement if we see a system security need by the publication of a formal Linking Notice well in advanced of any such requirement.

### Bid Curtailment Rules *[p.30]*

NESO will allow SR providers to user-define the curtailibility of the bid (i.e., the minimum capacity they are willing to accept).

### Revenue Stacking *[p.31]*

Stacking is the ability to use the same unit to provide different products simultaneously (i.e., in the same window).

- **Co-delivery** – Definition: Being paid multiple revenues from the same asset, using the same capacity, in the same time period (in the same direction). SR providers can Co-deliver their capacity with the Capacity Market (CM). Where a CM Notice (CMN) is issued, these providers should continue to make headroom available as per any active Slow Reserve commitments. To ensure providers are protected from penalties for breach of their CM agreement, should a System Stress Event occur following a CMN, SR has been added to the list of Relevant Balancing Services. In some cases, it may also be appropriate for providers to Co-deliver SR with the BM.
- **Splitting** – Definition: Being paid multiple revenues from the same asset, but with different capacity, in the same time period. For a given SR Window, splitting is allowed between Positive and Negative SR as long as different capacity from the asset is used for each service. Splitting is also allowed with the BM as well as Voltage and Stability services. However, Splitting is not allowed between the same polarity Reserve products, i.e., PSR & PBR. Availability payments will be withheld for any units holding >1 Reserve service in the same direction for a given SR Window.

It is not the intention to prevent providers from co-delivering Reserve with non-active power services, such as SpinPump or SpinGen, as this would significantly reduce the availability of other assets. However, if a unit is required to be in SpinGen etc. in order to be able to deliver the service, they should not be paid for that service. If a unit is stacking/splitting multiple services, then the data submitted to NESO must be that of the most granular service.

### Locationality *[p.32]*

*[Summarised: locational assessment (avoiding reserve behind anticipated network constraints) was considered but is not used; work on Locational Procurement capability has started with no details or timescales; any future proposal would be subject to full industry consultation.]*

### Active Network Management Schemes *[p.32]*

Eligible Assets will not normally be registered by NESO for participation in Slow Reserve if they have a condition in their DNO connection agreement whereby they are signed up to an Active Network Management (ANM) scheme / Flexibility Connection. However, NESO will consider this on a case-by-case basis and may (at its sole discretion) enable such participation if there is reasonable evidence to demonstrate that the asset has significantly high forecasted availability (e.g., as shown by Curtailment Assessment Reports from DNOs).

### Availability Declarations (procurement) *[p.32–33]*

Once a contract has been awarded for the Firm Service, or the Service Provider wishes to declare themselves available for the Optional Service, they will be required to submit an availability declaration for the relevant unit.

- **Non-BM:** these (re)declarations will be submitted into the appropriate OBP route as soon as reasonably practicable after contract award but in any event must be submitted no later than sixty (60) minutes prior to each SR Window. Availability declarations must be submitted in accordance with the Service Terms and include: Confirmation of MW available; A utilisation price (£/MWh).
- **BM:** declarations must be made by way of Grid Code BM Unit Data submissions via EDL/EDT (or wider access equivalent) as soon as reasonably practical after contract award but in any event must be by no later than Gate Closure.

Declarations can be submitted ahead of time (either before, during or after auction/contract award) provided that the MW value in a Service Provider's contract (Firm Service) and availability declaration match. Where no (re)declaration has been submitted by the deadline, or the declared available MW value does not match the contracted MW, the unit will be assumed to be unavailable. The declared available MW value should equal contracted MW where a unit is participating as part of the Firm Service. Declaring LESS or MORE than contracted MW: the declared volume remains available to NESO, but no availability payments; payment is still made for any instructed utilisation.

Unavailability for commercial or non-technical reasons is not permitted for the Firm Service.

### Settlement and Pricing *[p.33–34]*

1. **Availability Payments:** Where a Service Provider (BM and non-BM) secures a contract for the Firm Service, NESO will make an Availability Payment subject to the relevant market clearing price (£/MW/h) for the SR Window covered by the Firm Service SR Contract. Payments for availability are subject to performance monitoring.
2. **Utilisation Payments:** For each Slow Reserve instruction, non-BM providers will receive a payment for the energy instructed on a £/MWh basis if instructed to deliver the Firm service in a SR Window. Additionally, where NESO instructs an Optional Service from a Non-BM Unit which is declared available for the Service Window, then it will pay for the energy instructed on a £/MWh basis.

All Utilisation Payments will be calculated using the Utilisation Price on a pay-as-bid basis submitted by the Service Provider for the relevant SR Window. Utilisation payments will include the energy delivered in ramping towards and ramping from the instructed MW level. For BM providers, energy delivered will be settled by Elexon as part of the Balancing Mechanism. Non-BM providers will be settled by NESO. Availability payments and utilisation payments will be settled by NESO monthly, subject to deductions for service delivery failures following performance monitoring.

### ABSVD *[p.34]*

ABSVD will be applied in accordance with the published ABSVD Methodology for non-BM units. BM units will have their market position adjusted by the BSC approach used for BOAs in a similar way. To apply the methodology, non-BM units will need to submit the MSID pairs to allow the ABSVD to be assigned to the Balancing Responsible Party.

### Transfer of Slow Reserve Contracts *[p.34–35]*

The SR Service Terms will allow a Service Provider (Primary Service Provider) to transfer their SR contract to another unit prequalified for SR (either their own or another Service Provider (Secondary Service Provider)). In line with Quick Reserve, all applicable payments are to be made direct to the Secondary Service Provider. A transfer is a full assignment, transferring all rights and obligations under the Service Terms of the SR Contract.

Any providers wishing to transfer firm contracts must ensure that the minimum requirement of a 2-hour contiguous firm commitment is satisfied both for the contracts being transferred to the Secondary Service Provider and also for any that remain with the Primary Service Provider. Where a Slow Reserve Contract is subject to a Linking Notice, all other contracts in the Service Window Block subject to the Linking Notice must also be transferred to the same SR Unit. *[Example scenarios on p.35 were images and not captured.]*

## Appendix 1 – Dynamic Parameters as per Balancing Code BC1 *[p.36–37, shortened]*

Please refer to the Balancing Code BC1 for full details. The Dynamic Parameters comprise:
- Up to three Run-Up Rate(s) and up to three Run-Down Rate(s), expressed in MW/minute and associated Run-Up Elbow(s) and Run-Down Elbow(s), expressed in MW for output and the same for input. Run-Up Rate(s) are applicable to a MW figure becoming more positive;
- Notice to Deviate from Zero (NDZ): the notification time required for a BM Unit to start importing or exporting energy, from a zero Physical Notification level as a result of a Bid-Offer Acceptance, expressed in minutes;
- Notice to Deliver Offers (NTO) and Notice to Deliver Bids (NTB): the notification time required for a BM Unit to start delivering Offers and Bids respectively from the time the Bid-Offer Acceptance is issued. In the case of a BM Unit comprising a Genset, NTO and NTB will be set to a max period of two minutes;
- Minimum Zero Time (MZT): the minimum time that an exporting BM Unit must operate at zero or be importing, before returning to exporting (or the converse for an importing BM Unit), as a result of a Bid-Offer Acceptance, expressed in minutes;
- Minimum Non-Zero Time (MNZT): the minimum time that a BM Unit can operate at a non-zero level as a result of a Bid-Offer Acceptance, expressed in minutes;
- Stable Export Limit (SEL) / Stable Import Limit (SIL): the minimum value (MW, at the Grid Entry Point or Grid Supply Point) at which the BM Unit can, under stable conditions, export to / import from the National Electricity Transmission System;
- Maximum Export Limit (MEL) / Maximum Import Limit (MIL): a series of MW figures and associated times making up a profile of the maximum level at which the BM Unit may be exporting / importing (in MW) at the Grid Entry Point or Grid Supply Point or GSP Group, as appropriate.
