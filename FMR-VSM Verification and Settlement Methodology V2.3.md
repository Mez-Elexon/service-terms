# Flexibility Market Rule: Verification & Settlement Methodology (FMR-VSM) V2.3

> **Source file:** `FMR-VSM - Verification & Settlement.txt`  
> **Published Date:** 12/05/2026  
> **Converted:** 2026-10-07. Wording kept verbatim from the source copy-paste; only layout artefacts (page headers/footers, line wraps, website navigation, broken tables) were cleaned up. Sections the source marks as guidance are not legally binding. Notes in *[italic square brackets]* are editorial.

---


Sections 1, 2, 3 and 4 form the legally binding Flexibility Market Rule.

Defined terms capitalised in this document shall have the meaning given in Section 4.

## Summary of Verification & Settlement Methodology requirements

This section is provided as guidance to the Flexibility Market Rule. Therefore, it is not legally binding and falls outside of the formal change management process.

### Context

The Verification & Settlement of flexibility services involves assessing the performance of providers and determining how much they should get paid. This rule establishes a standardised process and methodology for that process to reduce complexity and increase consistency in the payments received for FSPs. The rule comes into force in February 2026 across DNO sub-markets.

### Verification & Settlement Requirements

The rule sets out a monthly cycle to which DNOs must operate their verification and settlement processes.

It also sets out an aligned methodology for assessing delivery and common factors to be used, and a sign convention for the calculations. For utilisation, this is based on a clawback of payment for under-delivery (below an agreed grace factor). Where availability payments are due, performance across the utilisation events is used to determine payment.

Finally, the rule sets out requirements on the information that DNOs must provide to FSPs to provide feedback on performance.

Alongside the standard implementation tracking, DNOs must also report on whether they use any non-standard figures, and formulae. The number of variations will be tracked by the Market Facilitator.

We believe the impact of these requirements to be:

| Impact on System Operators | Impact on FSPs |
|---|---|
| System Operators must use the standardised methodology to assess performance and calculate performance.<br>They must ensure their systems use the sign convention set out, and provide FSPs with the relevant information to understand their payments. | FSPs should understand the methodology as it determines the System Operators view of successful delivery, and ultimately their payment. |

### Implementation monitoring requirements

The key requirements are laid out below. A view across the rules is available in our deadline tracker.

| Category | Requirement | Trigger for data submission | What we will do with it |
|---|---|---|---|
| Implementation tracking | Basic tracking of implementation status and target date | From 14/01/2026 (20 working days after the published date).<br>Within 10 days of change | Track whether implementation is on track via our Implementation tracker. |
| Flexibility Market Catalogue data | Confirmation of use of standard or non-standard methodology | From 06/02/2026.<br>Within 10 days of change | Provide an overview of the sub-market and the market as a whole via the Flexibility Market Catalogue. |
| Effectiveness monitoring data | - | - | - |

### Derogations against this Rule

The following derogations are in place:

| Who | What | For how long | Why |
|---|---|---|---|
| UKPN | Section 2.3 and Section 2.4 | Until 31/07/2026 | To allow for comprehensive implementation |
| SSEN | The full requirements for LMA Interim Payment Service | Until 01/02/2027 | To prevent blockers to LMA Interim Service settlement |
| NPg | The full requirements for Empower Flex product | Until 31/03/2027 | To prevent blockers to Empower Flex product settlement |

## 1. Applicability of this Flexibility Market Rule

This Flexibility Market Rule applies to all DNO Sub-Markets within the Market Facilitator scope.

Innovation trials are not bound by this Flexibility Market Rule.

All DNOs shall adhere to the monthly self-billing or invoicing process as set out in section 2.1 across all their Sub-markets no later than the Implementation Date

All DNOs shall use the standard verification and settlement methodology set out in sections 2.2 & 2.3, with the required factors set out in section 2.4 across all their Sub-markets no later than the Implementation Date.

All DNOs shall provide their FSPs with the performance data feedback as set out in section 2.5 across all their Sub-markets no later than the Implementation Date.

Variations to this rule are only permitted with an approved Derogation from the Market Facilitator.

The core dates for this Flexibility Market Rule are laid out below.

**Table 1: Flexibility Market Rule dates**

| Parameter | Value |
|---|---|
| Published Date | 04/02/2026 |
| Implementation Date | 06/02/2026 |
| End Date | - |

#### Explainer: What is a Sub-Market?

This section is provided as guidance to the Flexibility Market Rule. Therefore, it is not legally binding and falls outside of the formal change management process.

A Sub-Market means a specific segment of the overall Flexibility Market, distinguished by a specific System Operator, procuring a specific Product within a specific time period.

A Sub-market may be built of multiple distinct geographic zones, operating in different directions, clearing different volumes at different prices.

The diagram below visualises the definition.

*[Diagram/image in the original web page was not captured in the copy-paste.]*

DTU means Demand Turn Up, GTD means Generation Turn Down.

DTD means Demand Turn Down, GTU means Generation Turn Up.

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