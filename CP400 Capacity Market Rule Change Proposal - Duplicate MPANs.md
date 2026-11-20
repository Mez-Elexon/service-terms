# Proposal for a Capacity Market Rule Change – CP400 (P400): Using a consumer consent-based solution for the issue of ‘Duplicate MPANs’

> **Source file:** `CP400.txt` (Capacity Market Rule change proposal form, copy-pasted)  
> **Converted:** 2026-10-07. Wording kept verbatim from the source copy-paste; only layout artefacts (page headers/footers "Public", line wraps, form layout) were cleaned up. Notes in *[italic square brackets]* are editorial.  
> **Important:** The proposed legal text in the original almost certainly used tracked changes (strikethrough for deletions, highlighting for insertions). **That markup was lost in the copy-paste**, so in Rule 8.3.3(f)(i) the deleted and inserted wording now run together. Check the original form before relying on the exact amended wording.

---

## Proposal details

| Field | Entry |
|---|---|
| Reference number | P400 |
| Title | Using a consumer consent-based solution for the issue of ‘Duplicate MPANs’ |
| Name of organisation(s)/individual(s) | CMAG sub-group |
| Contact e-mail address | Matthew.woolliscroft@elexon.co.uk |
| Contact Telephone Number | 020 7380 4165 |
| Date submitted | 14/07/2026 |

## Proposal abstract

*(a short summary, suitable for published description on our website)*

This proposal seeks to replace the first come first served process that the Settlement Body has used to resolve the issue of ‘duplicate MPANs’ for the 2026/27 Delivery Year with a solution based on the time when Capacity Providers obtained consent from the relevant consumer to use their demand in the Capacity Market.

## Description of the issue that the change proposal seeks to address

As part of the Metering Configuration Solution (MCS) process, a Capacity Provider that is registering an Unproven Demand Side Response (DSR) Capacity Market Unit (CMU) must provide the Settlement Body with the metering details for all the components that comprise the CMU.

To register an asset as a CMU component, a Capacity Provider must establish ‘contractual DSR control’ over the customer. Where asset level metering is installed, allowing a differencing solution to accurately separate demand, assets at the same site can be registered to different CMUs. However, multiple Capacity Providers are not permitted to register the same meter in the Capacity Market if the individual demands cannot be separately identified.

There have been instances where a consumer has erroneously signed up the same asset with multiple providers, and cases where a consumer has signed up with different providers to use their flexibility in exchange for compensation. For example, a consumer with a heat pump and an EV may sign up to flex the heat pump through their Supplier, and the EV charging point through their charging provider. If the consumer does not have asset level metering to differentiate between asset energy flows and flexibility providers, this scenario is not permitted in the Capacity Market. This creates a scenario where two Capacity Providers believe they have valid contracts with the same consumer to use their flexibility in the Capacity Market but are unable to both register the energy flow through the same Meter.

As there is no way for Capacity Providers to verify whether a consumer’s Meter has already been registered by another Capacity Provider when the consumer initially signs up, the issue may not be identified until later – after both Capacity Providers have established contracts with the consumer. This can leave a Capacity Provider not being able to register a significant proportion of their expected DSR components. This may increase the risk of Capacity Providers facing reduced capacity payments or even Termination Fees if they have not been able to secure enough capacity, which could lead to higher Auction bids and costs to consumers. Additionally, if a CMU is terminated after the modelling which sets the parameters for the T-1 auction has concluded, the terminated capacity will be lost to the market which could pose a threat to the Security of Supply. Ultimately, these impacts threaten the effectiveness of the Capacity Market.

The Settlement Body encourages Capacity Providers to bilaterally agree a resolution where duplicates are submitted in MCSs. However for the Delivery Year 2026/27, the Settlement Body has taken a ‘First Come, First Served’ approach. Under this process, the Capacity Provider that submits a meter as part of an MCS first is assigned the contested meter in the event of a duplication.

The first come, first served approach does not reflect the preference of the consumer whose demand is being used to provide capacity. Basing the registration on when it was submitted rather than when consent was obtained may leave a Capacity Provider unable to register a significant portion of their DSR capacity.

The CMAG established a sub-group in January 2026 to investigate alternative solutions that can be used for the duplicate MPANs issue. This proposal is the result of that sub-group’s work.

## Proposed solution to the issue

The proposed solution is to build a solution which is based on ‘enduring consumer consent’. Under this, the Capacity Provider that most recently gained consumer consent to use their demand in the Capacity Market (e.g. through signing terms and conditions) will be deemed to have enduring consent and have the asset registered to its CMU.

As with the current process, the Settlement Body is keen that Capacity Providers reach a mutual agreement where possible, with the proposed solution being used as the backstop.

Under the proposed solution the MCS dataset will be expanded to include a consumer consent timestamp for all DSR CMUs where the Capacity Provider is not the legal owner. The sub-group noted that although its solution was targeted at domestic DSR assets, it would not be overly burdensome for this data to be provided by all DSR assets. This approach also mirrors the data required by participants in NESO’s Demand Flexibility Service. The Settlement Body will not be required to validate this new data item, but will have the right to request supporting evidence at its discretion. The sub-group believed this would dissuade Capacity Providers from submitting an erroneous timestamp.

Under the proposed solution, DSR CMUs with components at sites where the electricity is taken for domestic purposes will have a shortened window of 20WD after CAN release during which to submit their MCSs. At the end of this window, the Settlement Body will check for duplicates and register any meters which are uncontested. Where duplicates are identified, the Settlement Body will notify all competing Capacity Providers with the details of the other competing Capacity Providers. This will allow bilateral discussions to take place to resolve the duplication.

If Capacity Providers have not reached an agreement and notified the Settlement Body four months and 10 Working Days before the start of a Delivery Year, the Settlement Body will compare the consumer consent timestamps for any remaining duplicated meters and register the asset to the CMU with the most recent timestamp.

The subgroup considered that as only one Capacity Provider can have contractual control of a DSR asset at any given time, when a consumer consents to have their demand used by a Capacity Provider, this would supersede any existing consent for the purpose of the CM Rules.

## List of alternative proposals already submitted which this proposal relates to (if any)

None

## Proposed changes to the CM Rules

*If you know the specific change to the Capacity Market (CM) Rules you wish to make, please select the type of change below and propose specific revised text, indicating the provision number from the CM Rules and highlighting the change (if left blank, the Capacity Market Advisory Group (CMAG)/Ofgem may suggest revised text to achieve the proposed solution above):*

- ☒ Amendment
- ☒ Addition
- ☐ Revocation
- ☐ Substitution

### Amend Rule 8.3.3 as follows

*[Tracked-change markup lost in the copy-paste; see the note at the top. Comparing with the existing rule, "Provide to the CM Settlement Body as soon as reasonably practicable and, in any event, within 10 Working Days" and "ensure the accurate submission of the following information to the CM Settlement Body as applicable" look like the old and new wording, but the source does not show which is which. Item (ccz) looks like the new insertion.]*

f) A Capacity Provider or CMVR Registered Participant must:

(i) Provide to the CM Settlement Body as soon as reasonably practicable and, in any event, within 10 Working Days ensure the accurate submission of the following information to the CM Settlement Body as applicable;

- (aa) All relevant Meters, and Meter Point Administration Numbers, for all the relevant Meter(s),
- (bb) BM Unit Identifiers (as defined in the Balancing and Settlement Code), if applicable; and
- (ccz) in the case of a DSR CMU where the Capacity Provider or CMVR Registered Participant is not the legal owner, a timestamp (in format HH:MM:SS) and date on which the Capacity Provider or CMVR Registered Participant obtained agreement from the owner and/or occupier of the Premises to its participation in the Capacity Market for each Meter and Meter Point Administration Number in (aa); and
- (cc) in the case of an Interconnector CMU, the relevant interconnector identifier(s) as specified for the purposes of the BSC in file CDCA-I041 of the Central Data Collection Agent (CDCA).
- (dd) if any Meter Point Administration Number specified has already been registered to another CMU which is a Capacity Committed CMU in respect of one or more of the same Delivery Years, include a declaration explaining how the two CMUs relate and how metering will separately identify the output of each of them.

### Insert New Rule 8.3.3AA after Rule 8.3.3

**8.3.3AA.1** If an Unproven DSR CMU that comprises at least one component that is located at a premises at which the supply of electricity is taken wholly or partly for domestic purpose is awarded a Capacity Agreement, then the Capacity Provider must provide to the CM Settlement Body no later than 20 Working Days after the award of a Capacity Agreement: All relevant Metering Configuration Solutions.

**8.3.3AA.2** Where a Meter in a Metering Configuration Solution has been provided to the CM Settlement Body under 8.3.3AA.1 by more than one Capacity Provider, the CM Settlement Body will notify all relevant Capacity Providers of the contested Meter no later than five Working Days after the date specified in 8.3.3AA.1.

**8.3.3AA.3.** On the day falling 4 months and 10 Working Days prior to the start of the Delivery Year, the CM Settlement Body will compare the consumer consent timestamps provided by Capacity Providers and register the Meter to the CMU of the Capacity Provider with the most recent timestamp.

*[There is no 8.3.3AA.4 in the source; the numbering jumps from .3 to .5, yet .5 refers to "8.3.3AA.4".]*

**8.3.3AA.5.** As soon as practicable after 8.3.3AA.4, The CM Settlement Body must notify relevant Capacity Providers which contested Meters have been accepted or rejected.

**8.3.3AA.6.** The Settlement Body may at its discretion request evidence supporting the timestamp provided by Capacity Providers in Rule 8.3.3(f)(i)(ccz).

## Analysis and evidence for the impact of the proposed change

*Analysis and evidence for the impact of the proposed change on industry and/or consumers, highlighting how the proposal meets the Ofgem/Capacity Market objectives set out in Regulation 78 of The Electricity Capacity Regulations 2014, any risks to consider and any implications for industry codes:*

The sub-group believe that this change will better facilitate Ofgem’s Principal Objective to protect the interests of existing and future consumers as it ensures that the consumer consent is better reflected in the registration process and would encourage greater participation in DSR capacity to the benefit of Security of Supply.

The sub-group also believe this change is positive against the objectives ‘promoting investment in capacity to ensure security of supply’ and ‘facilitating efficient operation and administration of the Capacity Market’. It puts into place clearly defined processes for resolving DSR asset conflicts which will give DSR CMUs greater confidence that asset registration process will be based on consumer consent, fostering engagement with the Capacity Market and increasing the level of DSR capacity available to the market.

## Urgency

*Select this box if you would like this proposal to be treated as “urgent” (see 1.14 of “The Change Process for the Capacity Market Rules – Guidance” (2022) for details on the requirements of an urgent proposal)?* ☐ (not selected)

*If selected, please include a justification, including any dates by which the CM Rule Change needs to be made and the consequences of not acting in time (Note that urgent proposals may be deprioritised or rejected if the Rule Change suggested cannot be implemented before the date(/s) set out in this section)*

The sub-group is not seeking urgent status for this Change Proposal. However, it believes that it should be implemented as soon as possible to provide certainty to Capacity Providers that their ability to register DSR assets for the upcoming Delivery Year will be based on consumer consent.
