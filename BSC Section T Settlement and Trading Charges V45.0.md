# BSC Section T: Settlement and Trading Charges V45.0

> **Source file:** `BSC Section T Settlement and Tradin.txt`  
> **Effective From Date:** 27/11/2025  
> **Status:** LIVE  
> **Converted:** 2026-10-07. Wording kept verbatim from the source copy-paste; only layout artefacts (page headers/footers, line wraps, website navigation, broken tables) were cleaned up. Notes in *[italic square brackets]* are editorial.

---

## SECTION T: SETTLEMENT AND TRADING CHARGES

## 1. GENERAL

### 1.1 Introduction

1.1.1 This Section T sets out:

(a) the basis on which Trading Charges for each Imbalance Party and the NETSO will be determined;

(b) the data required in order to determine such Trading Charges, and the intermediate quantities which are involved in such calculation;

(c) the processes to be undertaken by the SAA for and in connection with the determination of Trading Charges.

### 1.2 Obligation and entitlement of Parties

1.2.1 Subject to the provisions of the Code, each Imbalance Party and the NETSO shall be liable to pay to, or shall be entitled to be paid by, the BSC Clearer an amount in respect of Trading Charges for each Settlement Day as determined in accordance with this Section T.

1.2.2 For the purposes of paragraph 1.2.1, the Trading Charges for a Party are as follows:

(a) for each Imbalance Party and each Settlement Day:

(i) the Daily Party BM Unit Cashflow for that Imbalance Party, which shall be an amount representing either a credit or a debit to that Imbalance Party (as determined in accordance with paragraph 1.2.3);

(ii) the Daily Party Non-Delivery Charge for that Imbalance Party, which shall be an amount representing a debit to that Imbalance Party;

(iii) the Daily Party Energy Imbalance Cashflow for that Imbalance Party, which shall be an amount representing either a credit or a debit to that Imbalance Party (as determined in accordance with paragraph 1.2.3);

(iv) the Daily Party Information Imbalance Charge for that Imbalance Party, which shall be an amount representing a debit to that Imbalance Party; and

(v) the Daily Party Residual Settlement Cashflow for that Imbalance Party, which shall be an amount representing either a credit or a debit to that Imbalance Party (as determined in accordance with paragraph 1.2.3);

(vi) the Daily Party RR Cashflow for that Imbalance Party;

(vii) the Daily Party RR Instruction Deviation Cashflow for that Imbalance Party;

(viii) where that Imbalance Party is a Supplier, the Daily Virtual Lead Party Compensation Cashflow for that Supplier; and

(ix) where that Imbalance Party is a Supplier, the Daily Supplier Compensation Cashflow for that Supplier; and

(x) where that Imbalance Party is a Virtual Lead Party, the Daily Direct Compensation Cashflow for that Virtual Lead Party.

and, for each Imbalance Party and each Settlement Day, the amounts referred to in paragraphs (i) to (vii) shall be netted, in accordance with paragraph 5.3.3, to produce a single credit or debit amount for each Imbalance Party;

(b) in respect of the NETSO and for each Settlement Day, the Daily System Operator Cashflow, which shall be a single credit or debit amount (as determined in accordance with paragraph 1.2.3).

1.2.3 For the purposes of paragraph 1.2.2:

(a) in relation to each of:

(i) the Daily Party BM Unit Cashflow;

(ii) the Daily Party Residual Settlement Cashflow;

(iii) the Daily Party RR Cashflow;

(iv) the Daily Party RR Instruction Deviation Cashflow; and

(v) the Daily Supplier Compensation Cashflow,

a positive value of any such Cashflow represents a credit to the relevant Party and a negative value of any such Cashflow represents a debit to the relevant Party; and

(b) in relation to each of:

(i) the Daily Party Energy Imbalance Cashflow;

(ii) the Daily System Operator Cashflow;

(iii) the Daily Virtual Lead Party Compensation Cashflow; and

(iv) the Daily Direct Compensation Cashflow,

a positive value of any such Cashflow represents a debit to the relevant Party and a negative value of any such Cashflow represents a credit to the relevant Party.

1.2.4 For the avoidance of doubt, the Daily Party Non-Delivery Charge and the Daily Party Information Imbalance Charge shall have positive values and shall represent a debit to the relevant Imbalance Party.

### 1.3 Data requirements

1.3.1 This paragraph 1.3 sets out data required from different persons in order to make the determinations and calculations set out in this Section T.

1.3.2 Data required from the NETSO are:

(a) Final Physical Notification Data;

(b) Bid-Offer Data;

(c) Acceptance Data;

(d) Balancing Services Adjustment Data;

(e) Applicable Balancing Services Volume Data;

(f) Loss of Load Probability and associated data; and

(g) Replacement Reserve Auction Result Data.

1.3.3 Data required from the CDCA are:

(a) BM Unit Metered Volumes for BM Units other than Supplier BM Units, Interconnector BM Units and Secondary BM Units;

(b) Interconnector Metered Volumes; and

(c) the GSP Group Take for each GSP Group.

1.3.4 Data required from the ECVAA are:

(a) Metered Volume Fixed Reallocations by BM Unit and Subsidiary Energy Account;

(b) Metered Volume Percentage Reallocations by BM Unit and Subsidiary Energy Account; and

(c) the Account Bilateral Contract Volume for each Energy Account.

1.3.5 Data required from Interconnector Administrators are BM Unit Metered Volumes for the Interconnector BM Units of each Interconnector User for each Interconnector.

1.3.6 Data required from the SVAA are:

(a) for each Supplier, the BM Unit Allocated Demand Volume;

(b) for each Secondary BM Unit, the Secondary BM Unit Demand Volume and the Secondary BM Unit Supplier Delivered Volume;

(c) for each Supplier BM Unit, the Supplier BM Unit Non BM ABSVD; and

(d) for each Supplier BM Unit:

the BM Unit Allocated Demand Volume (BMUADVij); and

the Period BM Unit Non Chargeable Demand (NCBMUDij);and

(e) for each BM Unit, the BM Unit Gross Demand Volume and the Period BM Unit Total Gross Non-Final Demand.

1.3.7 Data required from the CRA are:

(a) Data registered in CRS and relevant to Settlement.

(b) CVA BM Units which have been included in an EMR CVA BM Unit Declaration.

1.3.8 Data required from the Market Index Data Provider(s) are Market Index Data.

1.3.9 Data required from the TLFA are Transmission Loss Factors for all BM Units.

1.3.10 Data required from Virtual Lead Parties and Virtual Trading Parties in respect of Assets registered in LPAMR, aggregated to Secondary BM Unit level, are:

(a) Secondary BM Unit Demand Volume; and

(b) Secondary BM Unit Supplier Delivered Volume.

1.3.11 Data required from ESNAs are BM Unit Eligible Exempt Supply Volume (QBESi1i2j).

### 1.4 Data receipt and validation

1.4.1 Whenever the SAA is required to carry out a Settlement Run, the SAA shall receive and validate (in accordance with BSCP01) the data for the relevant Settlement Day described in paragraph 1.3.

1.4.2 Subject to paragraphs 1.4.6, if by the time the SAA is to carry out the Interim Information Settlement Run complete and valid data have not been received by the SAA in accordance with paragraph 1.3 in respect of the relevant Settlement Day, then:

(a) where the invalid or missing data are not, in the SAA's opinion, a significant proportion of the data required to carry out the Interim Information Settlement Run in respect of that Settlement Day, the SAA shall inform BSCCo and shall input default data (in accordance with BSCP01) for the purposes of producing the Interim Information Settlement Run;

(b) where the invalid or missing data are, in the SAA's opinion, a significant proportion of the data required to carry out the Interim Information Settlement Run in respect of that Settlement Day:

(i) if the SAA considers that the invalid data will be corrected and re-submitted or the missing data will be submitted by the end of the next following Business Day, the SAA shall inform BSCCo and shall delay the Interim Information Settlement Run until such data is corrected and re-submitted or submitted (as the case may be);

(ii) if:

(1) the SAA does not consider that the invalid data will be corrected and re-submitted or the missing data will be submitted by the end of the next following Business Day; or

(2) in the case of paragraph (i) above, the SAA does not receive such data by the end of the next following Business Day,

the SAA shall inform BSCCo and BSCCo shall determine whether default data should be substituted for the invalid or missing data (in accordance with BSCP01) for the purposes of producing the Interim Information Settlement Run or whether production of the Interim Information Settlement Run should be delayed for a specified period in order that complete and valid data may be obtained by the SAA;

(c) the SAA shall continue to request the person responsible for submitting such data to resubmit and/or correct the data.

1.4.3 For the purposes of paragraph 1.4.2, "significant" shall be interpreted having regard to the purpose for which the Interim Information Settlement Run is produced, namely to provide a reasonably accurate reflection of what is expected to be contained in the Initial Settlement Run in respect of the relevant Settlement Day (taking into account the fact that the Interim Information Settlement Run does not include any data in respect of Supplier Volume Allocation).

1.4.4 Paragraph 1.4.2 shall not apply to data in respect of Supplier Volume Allocation.

1.4.5 Subject to paragraphs 1.4.6 and 1.4.7, if at any time from the Business Day prior to the day on which the SAA is to carry out the Initial Settlement Run the SAA forms the view that it does not expect to receive substantially complete and valid data in accordance with paragraph 1.3 in respect of the relevant Settlement Day in time to carry out such Settlement Run in accordance with the Settlement Calendar, then:

(a) the SAA shall inform BSCCo; and

(b) BSCCo shall determine whether default data should be substituted for the invalid or missing data (in accordance with BSCP01) for the purposes of producing the Initial Settlement Run or whether production of the Initial Settlement Run should be delayed for a specified period in order that complete and valid data may be obtained by the SAA.

1.4.6 Where and for so long as any of paragraphs (a), (b), (c) or (d) of Section K5.4.6 applies in respect of an Interconnector, all BM Unit Metered Volumes for the Interconnector BM Units of each Interconnector User for that Interconnector (whether or not any such volumes are submitted under paragraph 1.3.5) shall be set to zero.

1.4.7 For those Supplier BM Units or Secondary BM Units with no associated SVA Metering Systems (and in respect of which no data is submitted by the SVAA as a result), the BM Unit Metered Volume shall be zero.

1.4.8 Where Supplier BM Unit Non BM ABSVD has not been received in time for the Interim Information Settlement Run, or any subsequent Settlement Run, paragraphs 1.4.2 and 1.4.5 shall not apply.

### 1.5 Market Index Definition Statement

1.5.1 The Panel shall establish by no later than the commencement date, and have in force at all times thereafter, a statement having regard to the principles set out in paragraph 1.5.3 and which is approved by the Authority (such statement, as revised from time to time in accordance with this paragraph 1.5, being the "Market Index Definition Statement").

1.5.2 The Market Index Definition Statement shall contain the following:

(a) nomination of the particular entity or entities (each a "Market Index Data Provider") which shall be responsible for making available Market Index Data in respect of each Settlement Period for the purposes of paragraph 4.4;

(b) full definition of the particular data and methodology to be used by the Market Index Data Provider(s) in determining the Market Index Data for each Settlement Period (including, where applicable, identification of the particular products, period of trading and any relevant weighting to be applied); and

(c) definition and determination, for the purposes of paragraph 4.3A.1, of a minimum liquidity requirement per Settlement Period (expressed in MWh) in respect of each Market Index Data Provider individually (in each case, an "Individual Liquidity Threshold") which, for the avoidance of doubt, may be zero in any case and may vary in any case according to the Settlement Period and/or the Settlement Day or otherwise.

1.5.3 The principles referred to in paragraph 1.5.1 are:

(a) the Market Index Data is to be used in Settlement to calculate a price (expressed in £/MWh) in respect of each Settlement Period (in accordance with paragraphs 4.4.2(b) and 4.4.3(b)) which reflects the price of wholesale electricity in Great Britain for delivery in respect of that Settlement Period in the short term market, in circumstances where the levels of liquidity in the market during that period and in respect thereof are not exceptionally low;

(b) for the purposes of paragraph 1.5.3(a):

(i) 'reflects' means 'provides a reasonable reflection of';

(ii) references to the 'market' are to the market in general and not to any particular market or particular type of market (organised or otherwise);

(iii) 'short term' is to be taken as meaning, in respect of a Settlement Period, a period of hours or days immediately prior to the Submission Deadline but in any event no more than three Business Days prior to the Submission Deadline;

(iv) 'delivery' refers to transactions where the intended method of performance is by way of submission of Energy Contract Volume Notifications or Metered Volume Reallocation Notifications; and

(v) the price of wholesale electricity for delivery in respect of a Settlement Period may include the price for a block of Settlement Periods which include that Settlement Period, provided the block comprises no more than twenty four hours in total.

1.5.4 The Panel shall review the Market Index Definition Statement:

(a) from time to time, and in any event at least once every twelve months; and/or

(b) if any change in circumstances occurs or is expected to occur which affects or is likely to affect in any material way the provision of Market Index Data by a Market Index Data Provider; and/or

(c) where necessary in order to give full and timely effect to any relevant Approved Modification by the Implementation Date for that Approved Modification,

by reference to the principles set out in paragraph 1.5.3, and shall make such revisions to the Market Index Definition Statement as may be determined by it and approved by the Authority following such review.

1.5.5 In establishing and reviewing the Market Index Definition Statement, the Panel shall:

(a) investigate what data exists and is available in respect of the market referred to in paragraph 1.5.3;

(b) consult with Parties and other interested parties in connection with the Market Index Definition Statement and have due regard to any representations made and not withdrawn during such consultations;

(c) provide to the Authority copies of any written representations so made and not withdrawn.

1.5.6 Where a revised Market Index Definition Statement is approved by the Authority:

(a) such revised Market Index Definition Statement shall be effective from such date as the Panel shall determine with the approval of the Authority (and shall apply in respect of Settlement Days from that date); and

(b) the Panel Secretary shall give notice of such date to each Party, the SAA and the BMRA.

1.5.7 BSCCo shall ensure that a copy of the Market Index Definition Statement (as revised from time to time) is:

(a) sent to each Party, the SAA and the BMRA; and

(b) published, and made available on request to any person.

1.5.8 For the purposes of this paragraph 1.5, the "commencement date" is the Settlement Day with effect from which, pursuant to paragraphs 4.4.2(b) and 4.4.3(b), Market Index Price and Market Index Volume data is first to be applied in determining energy imbalance prices for the purposes of Settlement.

### 1.6 Provision of Market Index Data

1.6.1 The Market Index Data to be provided by each Market Index Data Provider in respect of each Settlement Period shall comprise for that Settlement Period:

(a) a volume expressed in MWh; and

(b) a price expressed in £/MWh,

in each case determined in accordance with the Market Index Definition Statement.

1.6.2 For each Settlement Period, each Market Index Data Provider will determine its Market Index Data in accordance with the Market Index Definition Statement and submit such data to:

(a) the BMRA, such as to be received by the BMRA no later than the end of the Settlement Period to which the data pertains;

(b) the SAA and BSCCo, by way of daily report containing the data separately for each Settlement Period in the Settlement Day to which the data pertains and such as to be received by the SAA and BSCCo no later than the end of the Business Day next following the relevant Settlement Day.

1.6.3 Without prejudice to paragraph 4.3A.1, if in respect of a Settlement Period and a Market Index Data Provider the Individual Liquidity Threshold for that Market Index Data Provider (as determined in accordance with the Market Index Definition Statement) exceeds the Market Index Volume which would otherwise have been submitted by it, the Market Index Data Provider will instead submit a Market Index Volume with a value of zero.

1.6.4 Without prejudice to any rights or remedies available to BSCCo under the Market Index Data Provider Contract, if a Market Index Data Provider is unable to determine and/or submit its Market Index Data or to do so within the timescales set out in paragraph 1.6.2, it will:

(a) inform BSCCo, the BMRA and the SAA immediately, giving details of the cause of such inability, when it expects to be able to determine and submit such data and the Settlement Periods likely to be affected;

(b) endeavour to determine and submit such data as soon as it reasonably can, in which case such data shall be taken into account in the next Settlement Run for the relevant Settlement Day after such submission.

1.6.5 In respect of any Settlement Day for which the SAA does not receive Market Index Data from a Market Index Data Provider:

(a) the provisions of paragraph 1.4, other than paragraph 1.4.1, shall not apply (and the default rules under paragraph 4.3A.1 shall apply instead); and

(b) the SAA shall inform BSCCo.

1.6.6 Without prejudice to Section W1.3.2(c)(iv), where, following the submission by a Market Index Data Provider of Market Index Data in respect of a Settlement Period in accordance with paragraph 1.6.2, a change is made to any underlying data item of the Market Index Data Provider such that the Market Index Data so submitted is no longer the data which would have been submitted by it in respect of that Settlement Period in accordance with the Market Index Definition Statement:

(a) the Market Index Data Provider will promptly:

(i) inform BSCCo of such change and its effect on the Market Index Data;

(ii) resubmit the Market Index Data for the relevant Settlement Period(s) taking account of such change; and

(b) where the Market Index Data Provider resubmits any Market Index Data as provided in paragraph (a)(ii) above, such revised Market Index Data shall be taken into account in the next Settlement Run for the relevant Settlement Day after such submission.

1.6.7 It shall be the responsibility of BSCCo to enter into a contract with each person nominated as a Market Index Data Provider for the provision of Market Index Data in accordance with this paragraph 1.6 and for these purposes:

(a) a Market Index Data Provider shall not be considered to be a 'BSC Agent' under the Code;

(b) notwithstanding paragraph 1.6.7(a), the provisions of Sections E2.1.2, E2.2.4, E2.2.5, E2.2.6, E2.4, E2.6 and Section E3 shall apply to each Market Index Data Provider Contract and to the provision of Market Index Data as if references to BSC Agent included the Market Index Data Provider and references to a BSC Agent Contract included the Market Index Data Provider Contract subject to the following:

(i) provisions in Section E2 and E3 relating to the selection and appointment of BSC Agents shall not apply (the selection and appointment of Market Index Data Provider(s) being prescribed in the Market Index Definition Statement);

(ii) references in Section E2 and E3 to BSC Service Descriptions shall be disregarded; and

(iii) the provisions of Section E3.2 apply to a Market Index Data Provider in its capacity as such and not in any other capacity which it may have under the Code.

1.6.8 It is recognised that a Market Index Data Provider may (but need not) be a Party; where a Market Index Data Provider is a Party:

(a) such Party shall have no rights, benefits, obligations or liability in its capacity as Market Index Data Provider to or against any other Party under the Code, but without prejudice to its rights and obligations:

(i) as Market Index Data Provider under its Market Index Data Provider Contract; and

(ii) in any other capacity under the Code;

(b) references to Party or Parties in the Code shall be construed as excluding any Market Index Data Provider (which is a Party) in its capacity as a Market Index Data Provider (but as including such person in any other capacity it may have under the Code);

(c) the provision of Market Index Data shall be made pursuant to the Market Index Data Provider Contract and not pursuant to the Code and, accordingly, such data shall not be considered relevant party data for the purposes of Section H4.6;

(d) the provision, disclosure and use of any market data relating to a Party which is used in or in connection with the determination of Market Index Data by a Market Index Data Provider shall not be considered or construed as being made pursuant to any provision of the Code.

1.6.9 Notwithstanding paragraph 1.6.7(a):

(a) Section H4.6 shall apply to Market Index Data Providers as if references to BSC Agents included Market Index Data Providers and references to BSC Agent Contracts included Market Index Data Provider Contracts;

(b) references to BSC Agents and BSC Agent Contracts in Section W shall be deemed to include, respectively, Market Index Data Providers and Market Index Data Provider Contracts.

1.6.10 For the purposes of the Code:

(a) references to a Market Index Data Provider are to a Market Index Data Provider nominated in the version of the Market Index Definition Statement prevailing at the time in question;

(b) in respect of a Market Index Data Provider, references to Market Index Data are to such data as that Market Index Data Provider is to submit in accordance with the Market Index Definition Statement.

### 1.6A Loss of Load Probability Calculation Statement

1.6A.1 The Panel shall establish and maintain a "Loss of Load Probability Calculation Statement" which shall be a document approved by the Authority setting out:

(a) in respect of the Static LoLP Function Methodology, the method for calculating a LoLP function; and

(b) the method for calculating a Loss of Load Probability value pursuant to the Static LoLP Function Methodology and the Dynamic LoLP Function Methodology.

1.6A.2 The Loss of Load Probability Calculation Statement shall include:

(a) the constant parameters to be used in the determination of Loss of Load Probability;

(b) where applicable, the range of values used to determine Loss of Load Probability values and functions; and

(c) the processes to follow for reviewing, updating and publishing parameters that are to be performed by the NETSO on a regular basis.

1.6A.3 The Panel shall review the Loss of Load Probability Calculation Statement:

(a) from time to time; and/or

(b) subject to paragraph 1.6A.4, where it considers necessary in order to give full and timely effect to any relevant Approved Modification by the Implementation Date for that Approved Modification,

and shall make such revisions to the Loss of Load Probability Calculation Statement as may be determined by it and approved by the Authority following such review.

1.6A.4 In reviewing the Loss of Load Probability Calculation Statement the Panel shall:

(a) consult with Parties and other interested parties and have due regard to any representations made and not withdrawn during such consultation; and

(b) provide to the Authority copies of any written representations so made and not withdrawn.

1.6A.5 Where a revised Loss of Load Probability Calculation Statement is approved by the Authority:

(a) such revised Loss of Load Probability Calculation Statement shall be effective from such date as the Panel shall determine with the approval of the Authority (and shall apply in respect of Settlement Days from that date); and

(b) the Panel Secretary shall give notice of such date to the NETSO and each Party.

1.6A.6 BSCCo shall ensure that a copy of the Loss of Load Probability Calculation Statement (as revised from time to time) is:

(a) sent to the NETSO and each Party; and

(b) published, and made available on request to any person.

1.6A.7 The Panel shall not delegate its power to determine changes to the Loss of Load Probability Calculation Statement (subject to the approval of the Authority) but it may delegate its responsibility to maintain and review the Loss of Load Probability Calculation Statement.

### 1.7 Single imbalance price

1.7.1 Where, for the purposes of any Contingency Provisions, a single imbalance price is to apply in relation to any Settlement Period:

(a) paragraph 1.7.1A or paragraph 1.7.2 shall apply;

(b) the provisions of paragraphs 4.4.2 and 4.4.3 in relation to the determination of System Buy Price and System Sell Price shall not apply; and

(c) for all purposes of the Code, the System Buy Price and the System Sell Price for that Settlement Period shall be the same and shall have the value established in accordance with paragraphs 1.7.1A or (as applicable) 1.7.2 (and shall be deemed to have been determined under paragraph 4.4).

1.7.1A Where a single imbalance price is to apply in relation to a relevant Settlement Period for the purposes of Section G3 or Section G4, the Panel shall, subject to the approval of the Authority, determine that single imbalance price in accordance with this paragraph 1.7.1A or, where the Panel, in its opinion, considers this provision unsuitable, in accordance with paragraph 1.7.2. For the purposes of this paragraph 1.7.1A the single imbalance price shall be:

(a) subject to paragraphs (b) and (d), the mean of the System Sell Price and the System Buy Price calculated respectively for each set of corresponding Settlement Periods in the thirty whole Settlement Days immediately preceding the Settlement Day on which the System Restoration Period (as defined in Section G3.1.2(d)) or Security Period (as defined in the Fuel Security Code) commenced;

(b) the NETSO shall determine that certain Settlement Periods within the Settlement Days identified under paragraph (a) be excluded from the single imbalance price calculation if those Settlement Periods occur within a System Restoration Period or Security Period or if during those Settlement Periods emergency instructions were issued under the Grid Code;

(c) where paragraph (b) applies, the Panel shall use the System Sell Price and the System Buy Price from additional Settlement Periods to achieve a mean of 30 System Sell Prices and System Buy Prices for each corresponding Settlement Period. Such additional Settlement Periods shall be those corresponding Settlement Periods in the Settlement Day immediately preceding the Settlement Days identified in paragraph (a);

(d) where a Clock Change Day occurs in the thirty Settlement Days immediately prior to the System Restoration Period or Security Period that Settlement Day is to be excluded for the purposes of this paragraph 1.7.1A and a further Settlement Day in accordance with paragraph (e) is to be selected;

(e) where paragraph (d) applies, the Panel shall use the System Sell Price and the System Buy Price from an additional Settlement Day (immediately prior to the thirty Settlement Days referred to in paragraph (a)) to achieve a mean of 30 System Sell Prices and System Buy Prices for each corresponding Settlement Period;

(f) where a Clock Change Day occurs in a System Restoration Period or Security Period:

(i) if the Clock Change Day is short (forty six Settlement Periods) the third and fourth Settlement Periods (and thus the single imbalance price calculated in accordance with this paragraph 1.7.1A for the third and fourth Settlement Periods) shall be ignored for that Clock Change Day; and

(ii) where the Clock Change Day is long (fifty Settlement Periods) the single imbalance price calculated in accordance with this paragraph 1.7.1A for the third and fourth Settlement Periods shall be repeated for the fifth and sixth Settlement Periods of that Clock Change Day. The single imbalance price for the remaining Settlement Periods for that Clock Change Day will be the single imbalance price calculated in accordance with this paragraph 1.7.1A but (other than for the first and second Settlement Periods) for two Settlement Periods earlier (that is to say the single imbalance price calculated for Settlement Period five will apply to Settlement Period seven on a long Clock Change Day, the single imbalance price calculated for Settlement Period six will apply to Settlement Period eight and so on); and

(g) in this paragraph 1.7.1A, save for paragraph (f), "corresponding" means corresponding in sequence (that is to say, the first Settlement Period of a Settlement Day corresponds to the first Settlement Period of another Settlement Day and so on).

1.7.2 Subject to paragraph 1.7.1A, where this paragraph applies, the Panel shall determine, in its opinion, subject to the approval of the Authority, what is or would have been the market price for bulk electricity in the relevant Settlement Period; and for these purposes:

(a) bulk electricity means electricity traded under contracts which may be performed by the notification of Energy Contract Volumes in accordance with Section P;

(b) the Panel may make reference for the purposes of its determination to reported prices and price indices for bulk electricity for any Settlement Period (on any day) which the Panel considers to be comparable, and to equivalent prices and indices relating to periods prior to the Go-Live Date (making appropriate adjustments in respect of any differing treatment of transmission losses and related matters).

1.7.3 The Panel shall wherever practicable make its determination in time for such determinations to be taken into account in the Initial Settlement Run in relation to the relevant Settlement Period.

1.7.4 BSCCo shall promptly notify the Panel's determination to the SAA and to each Party.

### 1.8 De Minimis Acceptance Threshold

1.8.1 For the purposes of the Code the "De Minimis Acceptance Threshold" (DMAT) shall be 1 MWh or such other amount (in MWh) as the Panel may from time to time determine, after consultation with, the NETSO and Trading Parties and subject to the approval of the Authority, as the de-minimis level below which it would be appropriate to disregard accepted Bids and accepted Offers from the calculation of the energy imbalance prices.

1.8.2 Where a revised value for the De Minimis Acceptance Threshold is approved by the Authority:

(a) such revised value shall be effective from such date as the Panel shall determine with the approval of the Authority, not being less than twenty Business Days after the date of the Panel’s determination;

(b) the Panel Secretary shall promptly give notice of the revised value and its effective date to each Party, the SAA and the BMRA and shall copy such notice to the Authority;

### 1.9 Continuous Acceptance Duration Limit (CADL)

1.9.1 For the purposes of the Code the "Continuous Acceptance Duration Limit" (CADL) shall be ten minutes or such other amount (in minutes) determined by the Panel and approved by the Authority.

1.9.2 The Panel may revise such amount from time to time subject to the approval of the Authority.

1.9.3 In revising the amount of the Continuous Acceptance Duration Limit from time to time, the Panel shall consult with Parties and consider the views expressed in the course of such consultation prior to making its determination (and shall provide a detailed summary of such views to the Authority).

### 1.10 Price Average Reference Volume

1.10.1 Subject to paragraph 1.10.2, for the purposes of the Code the "Price Average Reference Volume" (PAR) shall be 50 MWh.

1.10.2 With effect from 1st November 2018 and for all Settlement Days thereafter, for the purposes of the Code the PAR shall be 1 MWh.

### 1.11 Replacement Price Average Reference Volume

1.11.1 For the purposes of the Code the "Replacement Price Average Reference Volume" (RPAR) shall be 1 MWh.

### 1.12 Value of Lost Load

1.12.1 Subject to paragraph 1.12.2, for the purposes of the Code the "Value of Lost Load" (VoLL) shall be £3,000/MWh.

1.12.2 With effect from 1st November 2018 and for all Settlement Days thereafter, for the purposes of the Code the VoLL shall be £6,000/MWh.

1.12.3 The Panel, or any Panel Committee to whom responsibility for conducting a review of the VoLL has been delegated, shall review the VoLL:

(a) from time to time; and/or

(b) upon the request of the Authority,

in each case in accordance with the VoLL Review Process.

1.12.4 The Panel shall establish and maintain a VoLL Review Process which shall document the process for reviewing the VoLL in accordance with paragraph 1.12.3 and shall ensure that:

(a) consideration is given to the views and evidence submitted by the Authority;

(b) a consultation is conducted with Parties and other interested parties;

(c) due regard is given to any representations made and not withdrawn during such consultation; and

(d) the conclusions and any recommendations of the VoLL Review shall be set out in a report prepared for the consideration of the Panel.

1.12.5 Where the VoLL Review includes a recommendation that the VoLL be modified the Panel shall decide at the next following Panel meeting whether to propose a modification to paragraph 1.12 in accordance with Section F.

1.12.6 Where the Panel:

(a) rejects a recommendation of the VoLL Review; or

(b) agrees with a recommendation of the VoLL Review not to modify the VoLL,

the Panel shall submit a report to the Authority in accordance with paragraph 1.12.7.

1.12.7 The report referred to in paragraph 1.12.6 shall:

(a) describe the outcome of the VoLL Review;

(b) set out the views and rationale of Panel Members for why:

(i) no change to the VoLL has been recommended or

(ii) the Panel has rejected the recommendations of the VoLL Review; and

(c) include copies of any written representations made in response the VoLL Review pursuant to paragraph 1.12.4.

1.12.8 The provisions of this paragraph are without prejudice to Section F and the right of any person referred to in Section F2.1.1 to raise a Modification Proposal in respect of the VoLL.

### 1.13 Annex T-2

1.13.1 Annex T-2 shall apply for the purposes of the determination of Transmission Loss Factors.

### 1.14 Replacement Reserve Schedule Methodology Document

1.14.1 The Panel shall establish, and have in force at all times thereafter, a document containing detailed requirements for the construction of Point Acceptance Volumes (qAkit) to represent the physical dispatch by the NETSO of a BM Unit to fulfil a Quarter Hour RR Activation (the "Replacement Reserve Schedule Methodology Document").

1.14.2 The Panel shall review the Replacement Reserve Schedule Methodology Document from time to time and in any event if there is a change to the NETSO’s requirements for the physical dispatch of a BM Unit to fulfil a Quarter Hour RR Activation, and shall make such revisions as it considers necessary.

1.14.3 BSCCo shall ensure that a copy of the Replacement Reserve Schedule Methodology Document (as revised from time to time) is sent to each Party, the SAA and the BMRA.

### 1.15 Winter Contingency BM Units

1.15.1 Where the NETSO has determined that a BM Unit shall be treated as a "Winter Contingency BM Unit" for the purposes of Annex T-1, it shall notify BSCCo and BSCCo shall publish such notification on the BSC Website. Such notification shall identify:

(a) the BM Unit(s) to which the notification relates; and

(b) the Settlement Dates from and to which each BM Unit is to be treated as a Winter Contingency BM Unit, where the end date shall be no later than 31st March 2023.

### 1.16 Supplier Compensation Reference Price

1.16.1 The Supplier Compensation Reference Price shall be the default tariff cap set by the Authority from time to time as further determined, for the purposes of the Code, in accordance with the Supplier Compensation Reference Price Methodology.

1.16.2 The Panel shall establish, and have in force at all times thereafter, a document containing the methodology for the determination of the Supplier Compensation Reference Price including, without limitation:

(a) required data and data sources;

(b) data validation;

(c) the approach to erroneous or duplicated data;

(d) exception scenarios; and

(e) defaulting rules,

in order to determine the amounts payable to Suppliers by way of compensation for VLP Trading (the "Supplier Compensation Reference Price Methodology Document").

1.16.3 The Panel shall review the Supplier Compensation Reference Price Methodology Document from time to time and in any event if the Authority withdraws the default tariff cap or makes a change to the methodology for determining the default tariff cap that impacts the Supplier Compensation Reference Price Methodology Document, and shall make such revisions as it considers necessary.

1.16.4 BSCCo shall ensure that a copy of the Supplier Compensation Reference Price Methodology Document Methodology Document (as revised from time to time) is sent to each Party, the SAA and the BMRA.

## 2. ALLOCATION OF TRANSMISSION LOSSES

### 2.1 Delivering and Offtaking Trading Units

2.1.1 For the purpose of scaling for transmission losses, in respect of each Settlement Period,

(a) a Trading Unit is a "delivering" Trading Unit when ΣiQMij > 0 and

(b) a Trading Unit is an "offtaking" Trading Unit when ΣiQMij ≤ 0

where Σi represents the sum over all BM Units belonging to that Trading Unit.

### 2.2 Transmission Loss Factors

2.2.1 For the purposes of the Code, the Transmission Loss Factor and factor α shall be as follows:

(a) for each BM Unit, TLFij shall be determined in accordance with Annex T-2, and

(b) α = 0.45.

### 2.3 Determination of the Transmission Loss Multipliers

2.3.1 In respect of each Settlement Period, for each BM Unit other than Interconnector BM Units and Secondary BM Units, the Transmission Loss Multiplier shall be calculated as follows:

(a) for all BM Units belonging to Trading Units which in the Settlement Period are delivering Trading Units:

TLMij = 1 + TLFij + TLMO+j

(b) for all BM Units belonging to Trading Units which in the Settlement Period are offtaking Trading Units:

TLMij = 1 + TLFij + TLMO-j

where:

TLMO+j = – {α(Σ+QMij + Σ-QMij) + Σ+(non-I) (QMij * TLFij)} / Σ+(non-I) QMij ;

TLMO-j = {(α–1)(Σ+QMij + Σ-QMij) – Σ-(non-I) (QMij * TLFij)} / Σ-(non-I) QMij ;

Σ+ represents the sum over all BM Units other than Secondary BM Units belonging to Trading Units that are delivering Trading Units in the Settlement Period;

Σ- represents the sum over all BM Units other than Secondary BM Units belonging to Trading Units that are offtaking Trading Units in the Settlement Period;

Σ+(non-I) represents the sum over all BM Units other than Interconnector BM Units and Secondary BM Units belonging to Trading Units that are delivering Trading Units in the Settlement Period; and

Σ-(non-I) represents the sum over all BM Units other than Interconnector BM Units and Secondary BM Units belonging to Trading Units that are offtaking Trading Units in the Settlement Period.

2.3.2 In respect of each Settlement Period, for each Interconnector BM Unit, the Transmission Loss Multiplier shall be calculated as follows:

TLMij = 1

irrespective of whether the Interconnector BM Unit belongs to a delivering or offtaking Trading Unit in the Settlement Period.

2.3.3 In respect of each Settlement Period, for each Secondary BM Unit, the Transmission Loss Multiplier shall be calculated as follows:

TLMij = TLMij(Base)

where TLMij(Base) means the value of TLMij calculated in the Settlement Period for BM Units belonging to the Base Trading Unit in the same GSP Group as the Secondary BM Unit.

## 3. SETTLEMENT OF BALANCING ACTIONS

### 3.1 Conversion of Data Received from the NETSO

3.1.1 It is recognised that Final Physical Notification Data, Bid-Offer Pairs and Acceptance Data derived from data submitted or determined under the Grid Code (and received by the SAA from the NETSO) will contain values with associated from/to times whereas the equivalent data required for the purposes of this Section T are required to contain point values (as defined in Annex X-2).

3.1.2 Accordingly, the SAA shall convert such data received from the NETSO for the purposes of Settlement using the following conventions:

(a) in the case of Final Physical Notification Data:

(i) each value, comprising a MW 'from' level and associated 'from' time and a MW 'to' level and associated 'to' time, shall be allocated a Point Value Identification Number;

(ii) the 'to' MW level and associated 'to' time shall be a Point FPN (fFPNijt) which is allocated a Point Value Identification Number of '1';

(iii) the 'from' MW level and associated 'from' time shall be a Point FPN (fFPNijt) which is allocated a Point Value Identification Number of '2';

(iv) the associated time of each Point FPN with a Point Value Identification Number of 2 shall be equal to the associated time of the Point FPN with a Point Value Identification Number of 1 of the immediately preceding pair of Point FPNs;

(b) in the case of Bid-Offer Pairs:

(i) each value, comprising a MW 'from' level and associated 'from' time and a MW 'to' level and associated 'to' time, shall be allocated a Point Value Identification Number;

(ii) the 'to' MW level and associated 'to' time shall be a Point Bid-Offer Volume (fqBOnijt) which is allocated a Point Value Identification Number of '1';

(iii) the 'from' MW level and associated 'from' time shall be a Point Bid-Offer Volume (fqBOnijt) which is allocated a Point Value Identification Number of '2';

(iv) the associated time of each Point Bid-Offer Volume with a Point Value Identification Number of 2 shall be equal to the associated time of the Point Bid-Offer Volume with a Point Value Identification Number of 1 of the immediately preceding pair of Point Bid-Offer Volumes;

(c) in the case of Acceptance Data:

(i) for each Acceptance Volume Pair, a Point Acceptance Volume (qAkit) shall be created where the MW level is set equal to the 'from' MW level of the Acceptance Volume Pair, the time t shall be set equal to the 'from' time of the Acceptance Volume Pair and the value of k shall be set equal to the Bid-Offer Acceptance Number of the Acceptance Volume Pair;

(ii) for each Acceptance Volume Pair, a Point Acceptance Volume (qAkit) shall be created where the MW level is set equal to the 'to' MW level of the Acceptance Volume Pair, the time t shall be set equal to the 'to' time of the Acceptance Volume Pair and the value of k shall be set equal to the Bid-Offer Acceptance Number of the Acceptance Volume Pair; and

(iii) for each Acceptance Volume Pair, a flag stating whether that Acceptance is relating to an RR Instruction.

3.1.3 References in the succeeding paragraphs of this Section T to any point values submitted or issued by the NETSO (and similar expressions) shall be interpreted as references to the relevant to/from values submitted or issued by the NETSO and converted into point values by the SAA pursuant to this paragraph 3.1.

3.1.4 It is recognised that Replacement Reserve Activation Data, GB Need Met Data and Interconnector Schedule Data derived from data submitted or determined under the Grid Code (and received by the SAA from the NETSO) will contain values with an associated Position and Replacement Reserve Auction Period Resolution Type whereas the equivalent data required for the purposes of this Section T are required to contain Quarter Hour values (as defined in Annex X-2).

3.1.5 Accordingly, the SAA shall convert such data received from the NETSO for the purposes of Settlement using the following conventions:

(a) in the case of, respectively, Replacement Reserve Activation Data, GB Need Met Data and Interconnector Schedule Data:

(i) each Position shall be equal to the duration of the Replacement Reserve Auction Period Resolution Type and have an associated Flow Direction, Replacement Reserve Activation Price and Activated Quantity;

(ii) for the purposes of the Code, each Position shall be fully comprised of Quarter Hours;

(iii) each Quarter Hour within a Position shall be allocated:

(1) a Quarter Hour 'J' expressed as an integer;

(2) a Quarter Hour Replacement Reserve Activation Price being the price associated with such Position pursuant to paragraph 3.1.5(a)(i) (where a Position is comprised of more than one Quarter Hour then each Quarter Hour in such Position shall be allocated the same Replacement Reserve Activation Price); and

(3) an Quarter Hour RR Activated Quantity associated being the Activated Quantity associated with such Position pursuant to paragraph 3.1.5(a)(i) (where a Position is comprised of more than one Quarter Hour then each Quarter Hour in such Position shall be allocated the same Activated Quantity) multiplied by 1 should the associated Flow Direction reference 'UP'; or multiplied by -1 should the associated Flow Direction reference 'DOWN';

(b) in the case of each Position converted to Quarter Hour data pursuant to paragraph 3.1.5(a), such Quarter Hour data shall be deemed to be:

(i) in respect of Replacement Reserve Activation Data, a Quarter Hour RR Activation;

(ii) in respect of GB Need Met Data, a Quarter Hour GB Need Met;

(iii) in respect of Interconnector Schedule Data, a Quarter Hour Interconnector Schedule;

(c) for each Quarter Hour RR Activation within a Replacement Reserve Auction Period the SAA shall create Deemed Product Point Variables (qDSPJijt), to be processed in ascending order by reference to the Quarter Hour RR Activation 'J', where;

(i) a point variable shall be created where the time t shall be set five minutes before the 'start time' of the Quarter Hour period that the Quarter Hour RR Activation relates to and the MW level shall be set equal to the Quarter Hour RR Activated Quantity for the immediately preceding Quarter Hour RR Activation that time t relates to. If no immediately preceding Quarter Hour RR Activation exists then the MW Level shall be set to zero;

(ii) a point variable shall be created where the time t shall be set five minutes after the 'start time' of the Quarter Hour period that the Quarter Hour RR Activation relates to and the MW level shall be set equal to the Quarter Hour RR Activated Quantity MW level of the Quarter Hour RR Activation;

(iii) a point variable shall be created where the time t shall be set five minutes before the 'end time' of the Quarter Hour period that the Quarter Hour RR Activation relates to and the MW level shall be set equal to the Quarter Hour RR Activated Quantity MW level of the Quarter Hour RR Activation;

(iv) a point variable shall be created where the time t shall be set five minutes after the 'end time' of the Quarter Hour period that the Quarter Hour RR Activation and the MW level shall be set equal to zero;

(d) for each Quarter Hour RR Activation within a Replacement Reserve Auction Period the SAA shall deem Acceptance Volume Pairs (qAkit), and such Acceptance Volume Pairs shall be classified as Acceptance Data and as RR Schedule flagged in accordance with Replacement Reserve Schedule Methodology Document.

### 3.2 Establishment of final physical notification (FPNij(t))

3.2.1 In respect of each Settlement Period, for each BM Unit, the value of FPNij(t) for spot times falling within the Settlement Period shall be established by linear interpolation of the values of Point FPN (fFPNijt), established for that Settlement Period pursuant to paragraph 3.1.

3.2.2 If, for a particular time t no value of Point FPN exists within the Settlement Period for which the associated time is at or after time t, the value of the FPNij(t) shall be equal to the value of the Point FPN submitted for the spot time most recently preceding time t and, where more than one Point FPN exists for that spot time, the Point FPN with the higher value of the Point Value Identification Number f.

3.2.3 If no value of Point FPN exists for which the associated time is at or before a particular time, the value of FPNij(t) shall be set equal to zero.

### 3.3 Establishment of Bid-Offer Volume (qBOnij(t))

3.3.1 In respect of each Settlement Period, for each BM Unit, for any value of Bid-Offer Pair Number, the Bid-Offer Volume (qBOnij(t)) at any spot time shall be established by linear interpolation from the values of Point Bid-Offer Volume (fqBOnijt) submitted for spot times in a Settlement Period.

3.3.2 If, for a particular time no subsequent value of Point Bid-Offer Volume has been submitted within the Settlement Period, then the value of Bid-Offer Volume shall be equal to the value of the Point Bid-Offer Volume submitted for the time most recently prior to the time in question, and this value shall apply until the end of the Settlement Period.

### 3.4 Establishment of Acceptance Volume (qAkij(t))

3.4.1 The calculations of Acceptance Volume undertaken with respect to a particular Acceptance for a particular BM Unit, described in paragraphs 3.4.2 to 3.4.4, will be made for each Acceptance for that BM Unit, and the Acceptances will be processed in the order in which they are issued, with the exception of Acceptances that are flagged as relating to an RR Schedule, and which shall be treated as issued at the Gate Closure time of the Replacement Reserve Auction Period to which they relate.

3.4.2 In respect of each Settlement Period that falls within the Balancing Mechanism Window Period, for each BM Unit, the Acceptance Volume (qAkij(t)) for spot times shall be established by linear interpolation from the Point Acceptance Volumes qAkit issued by the NETSO for that Acceptance.

#### 3.4.2A No Acceptance Volume (qAkij(t)) shall be calculated for any spot times t where the following criteria are met

(a) qAkij(t) is not flagged as relating to a RR Schedule or a RR Instruction; and

(b) there exists a qAk*ij(t) flagged as relating to a RR Schedule; and

(c) GCT < qAkij(t) Bid-Offer Acceptance Time < qAk*ij(t) Replacement Reserve Activation Time; and

(d) either:

qAk-ij(t) < qAkij(t) < qAk*ij(t)

or

qAk*ij(t) < qAkij(t) < qAk-ij(t)

where:

qAk-ij(t) represents the latest Acceptance Volume relating to the latest Acceptance issued prior to Gate Closure of the relevant Replacement Reserve Auction Period (GCT). If no such previously calculated value of Acceptance Volume qAk-ij(t) exists, then the Acceptance Volume shall be set to the value of FPNij(t) for those spot times; and

qAkij(t), qAk-ij(t) and qAk*ij(t) represent the associated spot time MW values.

3.4.3 For spot times which are both:

(a) within the Balancing Mechanism Window Period; and

(b) prior to the first time associated with the value of Point Acceptance Volume for the Acceptance,

for each BM Unit, the value of the Acceptance Volume shall be set to the last calculated value of Acceptance Volume for those spot times. If no such previously calculated value of Acceptance Volume exists, then the Acceptance Volume shall be set to the value of FPNij(t) for those spot times.

3.4.4 For spot times which are both:

(a) within the Balancing Mechanism Window Period; and

(b) after the last time associated with a value of Point Acceptance Volume for the Acceptance,

for each BM Unit, the value of the Acceptance Volume shall be set to the last calculated value of Acceptance Volume for those spot times. If no such previously calculated value of Acceptance Volume exists, then the Acceptance Volume shall be set to the value of FPNij(t) for those spot times.

3.4A Establishment of Bid-Offer Upper Range (BOURnij(t)) and Bid-Offer Lower Range (BOLRnij(t)) in relation to FPN and Submitted Bid-Offer Pairs

3.4A.1 In respect of each Settlement Period, for each BM Unit, for each Submitted Bid-Offer Pair for which the associated Bid-Offer Pair Number n is greater than zero (if any), other than the Submitted Bid-Offer Pair with the greatest Bid-Offer Pair Number which is greater than zero, the Bid-Offer Upper Range for each spot time in the Settlement Period shall be established as follows:

(a) BOURnij(t) = FPNij(t) + Σn+ qBOnij(t)

where Σn+ represents the sum over the range of positive Bid-Offer Pair Numbers 1 to n of Submitted Bid-Offer Pairs; and

(b) BOUR0 ij (t) = FPNij(t)

3.4A.2 In respect of each Settlement Period, for each BM Unit, for the Submitted Bid-Offer Pair with the greatest Bid-Offer Pair Number n which is greater than zero (if any), the Bid-Offer Upper Range for each spot time in the Settlement Period shall be established as follows:

(a) if FPNij(t)

≥

0 and qAkij(t) > FPNij(t) + Σn+ qBOnij(t) for any Bid-Offer Acceptance Number k,

then:

BOURnij(t) = Maxk(qAkij(t))

where Maxk(qA kij(t)) represents the maximum value of qAkij(t)) for any value of k for BM Unit i at spot time t in Settlement Period j;

(b) in any other case:

BOURnij(t) = FPNij(t) + Σn+ qBOnij(t)

where Σn+ represents the sum over the range of positive Bid-Offer Pair Numbers 1 to n of Submitted Bid-Offer Pairs.

3.4A.3 In respect of each Settlement Period, for each BM Unit, for Submitted Bid-Offer Pairs for which the associated Bid-Offer Pair Number n is less than zero, other than the Submitted Bid-Offer Pair with the least Bid-Offer Pair Number which is less than zero, the Bid-Offer Lower Range for each spot time in the Settlement Period shall be established as follows:

(a) BOLRnij(t) = FPNij(t) + Σn-qBOnij(t)

where Σn- represents the sum over the range of negative Bid-Offer Pair Numbers -1 to n of Submitted Bid-Offer Pairs; and

(b) BOLR0 ij (t) = FPNij(t).

3.4A.4 In respect of each Settlement Period, for each BM Unit, for the Submitted Bid-Offer Pair with the least Bid-Offer Pair Number n which is less than zero (if any), the Bid-Offer Lower Range for each spot time in the Settlement Period shall be established as follows:

(a) if FPNij(t) <= 0 and qAkij(t) < FPNij(t) + Σn- qBOnij(t) for any Bid-Offer Acceptance Number k,

then:

BOLRnij(t) = Mink(qAkij(t))

where Mink(qA kij(t)) represents the minimum value of qA kij(t)) for any value of k for BM Unit i at spot time t in Settlement Period j;

(b) in any other case:

BOLRnij(t) = FPNij(t) + Σn- qBOnij(t)

where Σn- represents the sum over the range of negative Bid-Offer Pair Numbers -1 to n of Submitted Bid-Offer Pairs.

### 3.4B Creation of Bid-Offer Pairs

3.4B.1 In respect of each Settlement Period, for each BM Unit, a Bid-Offer Pair shall be created in the following circumstances:

(a) if for any spot time t,

(i) FPNij(t)>0; and

(ii) there exists a Submitted Bid-Offer Pair with a Bid-Offer Pair Number of less than zero; and

(iii) qAkij(t) < FPNij(t) + Σn- qBOnij(t) for any value of k;

where Σn- represents the sum over the range of negative Bid-Offer Pair Numbers for all Submitted Bid-Offer Pairs;

then a Bid-Offer Pair shall be created with a Bid-Offer Pair Number n-1, where n-1 has a negative value equal to 1 less than the lowest Submitted Bid-Offer Pair Number;

(b) if for any spot time t,

(i) FPNij(t)<0; and

(ii) there exists a Submitted Bid-Offer Pair with a Bid-Offer Pair Number of greater than zero; and

(iii) qAkij(t) > FPNij(t) + Σn+ qBOnij(t) for any value of k;

where Σn+ represents the sum over the range of positive Bid-Offer Pair Numbers for all Submitted Bid-Offer Pairs;

then a Bid-Offer Pair shall be created with a Bid-Offer Pair Number n+1, where n+1 has a positive value equal to 1 greater than the highest Submitted Bid-Offer Pair Number;

(c) if for any spot time t,

(i) there are no Submitted Bid-Offer Pairs with negative Bid-Offer Pair Numbers; and

(ii) qAkij(t) < FPNij(t) for any value of k;

then an Unsubmitted Bid-Offer Pair shall be created with a Bid-Offer Pair Number n, equal to –1;

(d) if for any spot time t,

(i) there are no Submitted Bid-Offer Pairs with positive Bid-Offer Pair Numbers; and

(ii) qAkij(t) > FPNij(t) for any value of k;

then an Unsubmitted Bid-Offer Pair shall be created with a Bid-Offer Pair Number n, equal to 1.

3.4B.2 A Bid-Offer Pair created pursuant to paragraph 3.4B.1 shall be referred to as an "Unsubmitted Bid-Offer Pair".

3.4B.3 In respect of each Unsubmitted Bid-Offer Pair with Bid-Offer Pair Number n:

(a) the Offer Price (POnij) and the Bid Price (PBnij) shall both be £0.00/MWh; and

(b) the 'from' MW level and the 'to' MW level associated with the spot time at the start of the Settlement Period, and the spot time at the end of the Settlement Period respectively shall both be 0MW.

3.5 Establishment of Bid-Offer Upper Range (BOURnij(t)) and Bid-Offer Lower Range (BOLRnij(t)) in relation to Unsubmitted Bid-Offer Pairs

3.5.1 In respect of each Settlement Period, for each BM Unit, for the Unsubmitted Bid-Offer Pair with a Bid-Offer Pair Number n which is greater than zero (if any), the Bid-Offer Upper Range for all spot times in the Settlement Period shall be established as follows:

(a) if there are no Submitted Bid-Offer Pairs with Bid-Offer Pair Numbers greater than zero,

then:

BOUR1ij(t) = Max{FPNij(t), Maxk(qAkij(t))}

(b) if there are one or more Submitted Bid-Offer Pairs with Bid-Offer Pair Numbers greater than zero,

then:

(i) if FPNij(t) < 0, then

BOURnij(t) = Max{FPNij(t) + Σns+qBOnij(t), Maxk(qAkij(t))}

where Σns+ represents the sum over the range of positive Bid-Offer Pair Numbers for all Submitted Bid-Offer Pairs;

(ii) in any other case, BOURnij(t) = FPNij(t) + Σn+ qBOnij(t)

where Σn+ represents the sum over the range of positive Bid-Offer Pair Numbers for all Submitted Bid-Offer Pairs and all Unsubmitted Bid-Offer Pairs;

where Maxk(qA kij(t)) represents the maximum value of qA kij(t) for any value of k for BM Unit i at spot time t in Settlement Period j and n is the Bid-Offer Pair Number of the Unsubmitted Bid-Offer Pair.

3.5.2 In respect of each Settlement Period, for each BM Unit, for the Unsubmitted Bid-Offer Pair with a Bid-Offer Pair Number n which is less than zero (if any), the Bid-Offer Lower Range for all spot times in the Settlement Period shall be established as follows:

(a) if there are no Submitted Bid-Offer Pairs with Bid-Offer Pair Numbers less than zero, then

BOLR-1ij(t) = Min{FPNij(t), Mink(qAkij(t))}

(b) if there are one or more Submitted Bid-Offer Pairs with Bid-Offer Pair Numbers less than zero, then

(i) if FPNij(t) > 0, then:

BOLRnij(t) = Min{FPNij(t) + Σns-qBOnij(t), Mink(qAkij(t))}

where Σns- represents the sum over the range of all negative Bid-Offer Pair Numbers for each Submitted Bid-Offer Pair;

(ii) in any other case:

BOLRnij(t) = FPNij(t) + Σn- qBOnij(t)

where Σn- represents the sum over the range of all negative Bid-Offer Pair Numbers for Submitted Bid-Offer Pairs and all Unsubmitted Bid-Offer Pairs;

where Mink(qA kij(t)) represents the minimum value of qA kij(t)) for any value of k for BM Unit i at spot time t in Settlement Period j and n is the Bid-Offer Pair Number of the Unsubmitted Bid-Offer Pair.

### 3.6 Determination of Accepted Bid-Offer Volume (qABOknij (t))

3.6.1 In respect of each Settlement Period, for each BM Unit, the volume (in MW) of Bid or Offer from the Bid-Offer Pair accepted as a result of a particular Acceptance k that is not flagged as relating to an RR Instruction shall be the Accepted Bid-Offer Volume and shall be established as follows:

(a) For n>0,

qABOknij (t) = max {min (qAkij(t), BOURn ij (t)), BOURn-1ij(t)}

– max {min (qAk-ij(t), BOURnij(t)), BOURn-1ij(t)}, and

(b) For n<0,

qABOknij (t) = min { max (qAkij(t), BOLRnij(t)), BOLRn+1ij(t)}

– min {max (qAk-ij(t), BOLRnij(t)), BOLRn+1ij(t)}

where, from all Acceptances for which an Acceptance Volume has been determined for the Settlement Period, k- represents that Acceptance with the Bid-Offer Acceptance Time most recently preceding that of the Acceptance.

3.6.2 If there is no Acceptance for which an Acceptance Volume has been determined in the Settlement Period which has a Bid-Offer Acceptance Time that precedes that of the Acceptance, qAk-ij(t) shall be set equal to FPNij(t) for each Acceptance k that is not flagged as relating to an RR Instruction.

### 3.7 Accepted Offer Volume (qAOknij (t)) and Accepted Bid Volume (qABknij (t))

3.7.1 In respect of each Settlement Period, for each BM Unit, the volume (in MW) of an Offer accepted as a result of an Acceptance at spot times within the Settlement Period shall be the Accepted Offer Volume and shall be established as follows:

qAO knij(t) = max (qABOknij(t), 0)

3.7.2 In respect of each Settlement Period, for each BM Unit, the volume of a Bid accepted as a result of an Acceptance at spot times within the Settlement Period shall be the Accepted Bid Volume and shall be established as follows:

qABknij (t) = min (qABO knij(t), 0)

3.8 Determination of Period Accepted Offer Volume (QAOknij), Period Accepted Bid Volume (QABknij), Period RR Accepted Offer Volume (RRAOknij) and Period RR Accepted Bid Volume (RRABknij)

3.8.1 In respect of each Settlement Period, for each BM Unit, the Period Accepted Offer Volume shall be established by integrating the Accepted Offer Volume over all spot times in the Settlement Period, for each Acceptance k that is not flagged as relating to an RR Schedule.

3.8.2 In respect of each Settlement Period, for each BM Unit, the Period Accepted Bid Volume shall be established by integrating the Accepted Bid Volume over all spot times in the Settlement Period, for each Acceptance k that is not flagged as relating to an RR Schedule.

3.8.3 In respect of each Settlement Period, for each BM Unit, the Period RR Accepted Offer Volume shall be established by integrating the Accepted Offer Volume over all spot times in the Settlement Period, for each Acceptance k that is flagged as relating to an RR Schedule.

3.8.4 In respect of each Settlement Period, for each BM Unit, the Period RR Accepted Bid Volume shall be established by integrating the Accepted Bid Volume over all spot times in the Settlement Period, for each Acceptance k that is flagged as relating to an RR Schedule.

3.9 Determination of Period BM Unit Total Accepted Offer Volume (QAOnij), Period BM Unit Total Accepted Bid Volume (QABnij), Period RR Total Accepted Offer Volume (RRAOnij), Period RR Total Accepted Bid Volume (RRABnij) and Quarter Hour RR Activation Volume (RRAViJ)

3.9.1 In respect of each Settlement Period, for each BM Unit, the total MWh volume of the Offer accepted for all Acceptances that are not flagged as relating to an RR Schedule shall be the Period BM Unit Total Accepted Offer Volume and shall be established as follows:

QAOnij = ΣkQAOknij

where Σk represents the sum over all Acceptances within the Settlement Period.

3.9.2 In respect of each Settlement Period, for each BM Unit, the total MWh volume of the Bid accepted for all Acceptances that are not flagged as relating to an RR Schedule shall be the Period BM Unit Total Accepted Bid Volume, and shall be established as follows:

QABnij = ΣkQABknij

where Σk represents the sum over all Acceptances within the Settlement Period.

3.9.2A In respect of each Network Gas Supply Emergency Acceptance, for each Settlement Period and affected BM Unit, the total MWh volume of the Bid for that Acceptance shall be the Network Gas Supply Imbalance Adjustment Volume (QNGSIAij), and shall be established as follows:

QNGSIAij = Σn QABknij

where Σn represents the sum over all Bid-Offer Pair Numbers for the BM Unit.

3.9.3 In respect of each Settlement Period, for each BM Unit, the total MWh volume of Offers accepted for all Acceptances that are flagged as relating to an RR Schedule shall be the Period RR Total Accepted Offer Volume and shall be established as follows:

RRAOnij = ΣkRRAOknij

where Σk represents the sum over all Acceptances within the Settlement Period.

3.9.4 In respect of each Settlement Period, for each BM Unit, the total MWh volume of Bids accepted for all Acceptances that are flagged as relating to an RR Schedule shall be the Period RR Total Accepted Bid Volume, and shall be established as follows:

RRABnij = ΣkRRABknij

where Σk represents the sum over all Acceptances within the Settlement Period.

3.9.5 In respect of each Quarter Hour “J”, for each BM Unit, the MWh volume of a Quarter Hour RR Activation shall be the Quarter Hour RR Activation Volume, and shall be established as follows:

RRAViJ = Quarter Hour RR Activated Quantity * 0.25

### 3.10 Determination of Period BM Unit Offer Cashflow (COnij) and Period BM Unit Bid Cashflow (CBnij)

3.10.1 In respect of each Settlement Period, for each BM Unit, the transmission loss adjusted cashflow for Balancing Mechanism action in the Settlement Period, allocated to an Offer shall be the Period BM Unit Offer Cashflow and shall be determined as follows:

COnij = QAOnij * TLMij * POnij

3.10.2 In respect of each Settlement Period, for each BM Unit, the transmission loss adjusted cashflow for Balancing Mechanism action in the Settlement Period, allocated to a Bid shall be the Period BM Unit Bid Cashflow and shall be determined as follows:

CBnij = QABnij * TLMij * PBnij

### 3.11 Determination of Period BM Unit Cashflow (CBMij)

3.11.1 In respect of each Settlement Period, for each BM Unit, the total payment in respect of the BM Unit as a result of accepted Balancing Mechanism action in the Settlement Period shall be the Period BM Unit Cashflow and shall be determined as follows:

CBMij = ΣnCOnij + Σn CBnij

where Σn represents the sum over all Bid-Offer Pair Numbers for the BM Unit.

### 3.11A Determination of Quarter Hour RR Cashflow (CCRiJ)

3.11A.1 In respect of each Quarter Hour, for each BM Unit, the total payment in respect of the BM Unit as a result of a Quarter Hour RR Activation in the Quarter Hour shall be the Quarter Hour RR Cashflow and shall be determined, as follows:

CCRiJ = RRAViJ * RRAPJ

where RRAPJ represents the Quarter Hour Replacement Reserve Activation Price associated to the Quarter Hour RR Activation

3.11.B Determination of Period RR BM Unit Cashflow (CRRij)

3.11B.1 In respect of each Settlement Period, for each BM Unit, the total payment in respect of the BM Unit as a result of Replacement Reserve activations in the Settlement Period shall be the Period RR BM Unit Cashflow and shall be determined as follows:

CRRij = ΣJ CCRiJ

where ΣJ is the sum over all Quarter Hours J within Settlement Period j.

### 3.12 Determination of Total System BM Cashflow (TCBMj) and Daily Party BM Unit Cashflow (CBMp)

3.12.1 In respect of each Settlement Period, the total payments and charges in respect of Balancing Mechanism action for all BM Units shall be the Total System BM Cashflow and shall be determined as follows:

TCBMj = Σi CBMij

where Σi is the sum over all BM Units.

3.12.2 In respect of each Settlement Day, for each Party p, the Daily Party BM Unit Cashflow shall be determined as:

CBMp = Σj Σi∈p CBMij

where Σj is the sum over all Settlement Periods and Σi∈p is the sum of all BM Units for which Party p is the Lead Party.

### 3.12A Determination of Network Gas Supply Total Bid Payment

3.12A.1 In respect of each Network Gas Supply Emergency Acceptance, for each affected BM Unit, the total Period BM Unit Bid Cashflow relating to that Acceptance shall be the Network Gas Supply Total Bid Payment (TNGSBi), and shall be determined as follows:

TNGSBi = Σj Σn CBnij

where Σn represents the sum over all Bid-Offer Pair Numbers for the BM Unit, and Σj represents the sum over Settlement Periods.

### 3.13 Determination of Reserve Scarcity Price (RSVPj)

3.13.1 In respect of each Settlement Period, the Reserve Scarcity Price shall be calculated as:

RSVPj = LoLPj * VoLL

3.13.2 Subject to paragraph 3.13.3, if there is no Final Loss of Load Probability available for a Settlement Period then the Final Loss of Load Probability shall be the most recently calculated Indicative Loss of Load Probability for that Settlement Period.

3.13.3 If there is no Indicative Loss of Load Probability or Final Loss of Load Probability available for a Settlement Period then the Final Loss of Load Probability shall be NULL and the Reserve Scarcity Price shall be calculated as:

RSVPj = 0

### 3.14 Determination of STOR Action Price (STAPtj)

3.14.1 In respect of each Settlement Period that is in a STOR Availability Window, for each accepted Offer that is a STOR Action, the STOR Action Price (STAPtj) shall be determined as the greater of the Offer Price (POnij) or the Reserve Scarcity Price (RSVPj) applicable to that Settlement Period.

3.14.2 In respect of each Settlement Period, for each Balancing Services Adjustment Action that is a STOR Action, the STAPtj shall be determined as the greater of the Balancing Services Adjustment Price (BSAPmj) or the Reserve Scarcity Price (RSVPj) applicable to that Settlement Period.

### 3.15 Determination of System and Balancing Demand Control Volumes (QSDCcj and QBDCcj)

3.15.1 In respect of each Demand Control Instruction, for each Demand Control Event Stage:

(a) the Start Point Demand Control Level shall be the Demand Control Event Estimate determined as at the relevant time and date notified by the NETSO in accordance with Section Q6.9.3 or Q6.9.4; and

(b) the End Point Demand Control Level shall be the Demand Control Event Estimate determined as at the Demand Control Event End Point notified by the NETSO in accordance with Section Q6.9.5.

3.15.2 In respect of each Settlement Period, the Demand Control Volume for each Demand Control Event Stage shall be established by linear interpolation from the values of Start Point Demand Control Level and End Point Demand Control Level.

3.15.3 In respect of each Demand Control Event and each Settlement Period:

(a) the "System Demand Control Volume" (QSDCcj) shall be equal to the sum of the Demand Control Volumes determined under paragraph 3.15.2 where the related Demand Control Instructions have the same Demand Control Instruction identification number and included a SMAF Flag set to "Yes";

(b) the "Balancing Demand Control Volume" (QBDCcj) shall be equal to the sum of the Demand Control Volumes determined under paragraph 3.15.2 where the related Demand Control Instructions have the same Demand Control Instruction identification number and included a SMAF Flag set to "No".

3.16 Not used.

### 3.17 Determination of Deemed Standard Product Shape (qDSPJij(t))

3.17.1 In respect of each Settlement Period that contains a Deemed Standard Product Point Variable (qDSPJijt), for a particular Quarter Hour RR Activation, for each BM Unit, the Deemed Standard Product Shape (qDSPJij(t)) for spot times shall be established by linear interpolation from the Deemed Standard Product Point Variables (qDSPJijt) created from the Quarter Hour RR Activation issued by the NETSO.

3.17.2 If, for a particular time t no Deemed Standard Product Point Variable (DSPJijt) exists within the Settlement Period, then the value of Deemed Standard Product Shape (qDSPJij(t)) shall be equal to the value of Deemed Standard Product Shape for previous Quarter Hour RR Activation ‘J’. If no activation exists then Deemed Standard Product Shape (qDSPJij(t)) shall equal zero.

### 3.18 Determination of Deemed Standard Product Volume (qDSPVJij(t))

3.18.1 In respect of each Settlement Period, for each BM Unit, for each Quarter Hour RR Activation ‘J’ the volume (in MW) of Deemed Standard Product Volume shall be established as follows:

qDSPVJij(t) = qDSPJij(t) - qDSPJ-1ij(t)

where, for all Replacement Quarter Hour Replacement Reserve within the Replacement Reserve Auction Period for which a Deemed Standard Product Volume has been determined for the Settlement Period, J-1 represents that Deemed Standard Product Shape from the previous Quarter Hour. If no qDSPJ-1ij(t) has been determined in the Settlement Period which has a qDSPJij(t) then qDSPJ-1ij(t) shall be set equal to zero.

3.18.2 If there is no qDSPJ-1ij(t) has been determined in the Settlement Period which has a qDSPJij(t) then qDSPJ-1ij(t) shall be set equal to zero.

### 3.19 Determination of Deemed Standard Product Offer Volume (qDSPOJij(t)) and Deemed Standard Product Bid Volume (qDSPBJij(t))

3.19.1 In respect of each Settlement Period, for each BM Unit, the Deemed Standard Product Offer Volume (in MW) of an Offer accepted as a result of a Quarter Hour RR Activation at spot times within the Settlement Period shall be established as follows:

qDSPOJij(t)) = max (qDSPVJij(t) , 0 )

3.19.2 In respect of each Settlement Period, for each BM Unit, the Deemed Standard Product Bid Volume (in MW) of a Bid accepted as a result of a Quarter Hour RR Activation at spot times within the Settlement Period shall be established as follows:

qDSPBJij(t)) = min (qDSPVJij(t) , 0 )

3.20 Determination of Period Deemed Standard Product Offer Volume (DSPOJij) and Period Deemed Standard Product Bid Volume (DSPBJij)

3.20.1 In respect of each Settlement Period, for each BM Unit, the Period Deemed Standard Product Offer Volume shall be established by integrating the Deemed Standard Product Offer Volume over all spot times in the Settlement Period, for each Quarter Hour RR Activation J.

3.20.2 In respect of each Settlement Period, for each BM Unit, the Period Deemed Standard Product Bid Volume shall be established by integrating the Deemed Standard Product Bid Volume over all spot times in the Settlement Period, for each Quarter Hour RR Activation J.

3.21 Determination of Total Period Deemed Standard Product Offer Volume (TDSPOij) and Total Period Deemed Standard Product Bid Volume (TDSPBij)

3.21.1 In respect of each Settlement Period, for each BM Unit, the Total Deemed Standard Product Offer Volume (in MWh) of Offers accepted as a result of a Replacement Reserve Auction at spot times within the Settlement Period shall be established as follows:

TDSPOij = ∑ J DSPOJij

3.21.2 In respect of each Settlement Period, for each BM Unit, the Total Deemed Standard Product Bid Volume (in MWh) of Bids accepted as a result of a Replacement Reserve Auction at spot times within the Settlement Period shall be established as follows:

TDSPBij = ∑ J DSPBJij

3.22 Determination of Replacement Reserve Instructed Offer Deviation (IODij) and Replacement Reserve Instructed Bid Deviation (IBDij)

3.22.1 In respect of each Settlement Period, for each BM Unit, the Replacement Reserve Instructed Offer Deviation (in MWh) of Offers accepted as a result of a Replacement Reserve Auction at spot times within the Settlement Period that deviate from the Deemed Standard Product Shape shall be established as follows:

IODij = ∑ n RRAOnij - TDSPOii

3.22.2 In respect of each Settlement Period, for each BM Unit, the Replacement Reserve Instructed Bid Deviation (in MWh) of Offers accepted as a result of a Replacement Reserve Auction at spot times within the Settlement Period that deviate from the Deemed Standard Product Shape shall be established as follows:

IBDij = ∑ n RRABnij - TDSPBii

3.23 Determination of Replacement Reserve Period Instructed Offer Deviation Cashflow (CDOij)and Replacement Reserve Period Instructed Bid Deviation Cashflow (CDBij)

3.23.1 In respect of each Settlement Period, for each BM Unit, the Replacement Reserve Instructed Offer Deviation Cashflow of Offers accepted as a result of a Replacement Reserve Auction at spot times within the Settlement Period that deviate from the Deemed Standard Product Shape, shall be determined as follows:

CDOij = IODij * BEDPj

In respect of each Settlement Period, the Balancing Energy Deviation Price (BEDPj) shall be an amount equal to zero.

3.23.2 In respect of each Settlement Period, for each BM Unit, the Replacement Reserve Instructed Bid Deviation Cashflow of Bids accepted as a result of a Replacement Reserve Auction at spot times within the Settlement Period that deviate from the Deemed Standard Product Shape, shall be determined as follows:

CDBij = IBDij * BEDPj

In respect of each Settlement Period, the Balancing Energy Deviation Price (BEDPj) shall be an amount equal to zero.

### 3.24 Determination of the Replacement Reserve Period Instruction Deviation Cashflow (CDRij)

3.24.1 In respect of each Settlement Period, for each BM Unit, the total payment in respect of the BM Unit as a result of deviation from the TERRE Standard Product Shape in the Settlement Period shall be the Replacement Reserve Period Instruction Deviation Cashflow and shall be determined as follows:

CDRij = CDOij + CDBij

3.25 Determination of Total System RR Cashflow (TCRRj), Daily Party RR Cashflow (CRRp) and Daily Party RR Instruction Deviation Cashflow (CDRp)

3.25.1 In respect of each Settlement Period, the total payments and charges in respect of Replacement Reserve activations for all BM Units shall be the Total System RR Cashflow and shall be determined as follows:

TCRRj = Σij CRRij + Σij CDRij

where Σij is the sum over all BM Units i and Settlement Period j.

3.25.2 In respect of each Settlement Day, for each Party p, the Daily Party RR Cashflow shall be determined as:

CRRp = Σj Σi∈p CRRij

where Σj is the sum over all Settlement Periods and Σi∈p is the sum of all BM Units for which Party p is the Lead Party in that day.

3.25.3 In respect of each Settlement Day, for each Party p, the Daily Party RR Instruction Deviation Cashflow shall be determined as:

CDRp = Σj Σi∈p CDRij

where Σj is the sum over all Settlement Periods and Σi∈p is the sum of all BM Units for which Party p is the Lead Party in that day.

## 4. SETTLEMENT CALCULATIONS

### 4.1 Treatment of Interconnector BM Units

4.1.1 For each Settlement Period, the BM Unit Metered Volume for the relevant Interconnector BM Unit (as determined in paragraph 4.1.2) of the Interconnector Error Administrator will be determined as follows:

QMij = IMVj – Σi QMij

where Σi is the sum over all Interconnector BM Units for which the Lead Parties are Interconnector Users in relation to the Interconnector in question.

4.1.2 In respect of the Interconnector BM Units of an Interconnector Error Administrator for the Interconnector in question:

(a) where QMij is positive, it shall be the BM Unit Metered Volume for the Production Interconnector BM Unit of the Interconnector Error Administrator, and

(b) where QMij is negative, it shall be the BM Unit Metered Volume for the Consumption Interconnector BM Unit of the Interconnector Error Administrator,

and, in each case, the BM Unit Metered Volume for the other Interconnector BM Unit of the Interconnector Error Administrator for that Interconnector (the Consumption Interconnector BM Unit, in the case of paragraph (a), and the Production Interconnector BM Unit, in the case of paragraph (b)) shall be zero.

### 4.2 Determination of BM Unit Metered Volume (QMij) for Supplier BM Units

4.2.1 For each Settlement Period, the BM Unit Metered Volume for Supplier BM Units will, subject to paragraph 1.4.7, be determined as follows:

QMij = – BMUADVij

### 4.2A Determination of BM Unit Metered Volume (QMij) for Secondary BM Units

4.2A.1 For each Settlement Period, the BM Unit Metered Volume for Secondary BM Units will, subject to paragraph 1.4.7, be determined as follows:

QMij = – VBMUDVij+ VLPDVi2j

### 4.3 Determination of Information Imbalance Volumes (QIIij) and Charges (CIIij)

4.3.1 In respect of each Settlement Period, for each BM Unit, the Period FPN (FPNij) will be calculated by integrating the value of FPNij(t) over all spot times falling within the Settlement Period in question.

4.3.2 In respect of each Settlement Period, for each BM Unit, the Period BM Unit Balancing Services Volume will be determined as follows:

QBSij = Σn (QAOn ij + QABn ij) +Σn (RRAOn ij + RRABn ij) + QASij + BMUADDVij + SNBABSVDij – QDDij + QBSDij

where Σn represents the sum over all Bid-Offer Pair Numbers for the BM Unit and QBSDij represents the Period Supplier Primary BM Unit Delivered Volume, calculated in accordance with paragraph 4.3B.5 for Supplier BM Unit i.

4.3.3 In respect of each Settlement Period, for each BM Unit, which is not a Baselined BM Unit or for which SVAA has not provided the Settlement Expected Volume, the Period Expected Metered Volume will be determined as follows:

QMEij = FPNij + QBSij

4.3.3A In respect of each Settlement Period, for each Baselined BM Unit and for which SVAA has provided a Settlement Expected Volume, the Period Expected Metered Volume will be determined as follows:

QMEij = SEVij + QBSij

4.3.4 In respect of each Settlement Period, for each BM Unit, the Period Information Imbalance Volume will be determined as follows:

QII ij = |QMij – QMEij|

4.3.5 In respect of each Settlement Period, the Information Imbalance Price (IIPj) shall be an amount equal to zero.

4.3.6 In respect of each Settlement Period, for each BM Unit, the Information Imbalance Charge will be determined as follows:

CII ij = QIIij * IIPj

4.3.7 In respect of each Settlement Period, the Total System Information Imbalance Charge will be determined as follows:

TCIIj = ΣiCIIij

where Σi represents the sum over all BM Units.

4.3.8 In respect of each Settlement Day, for each Party p, the Daily Party Information Imbalance Charge shall be determined as:

CIIp = Σj Σi∈p CIIij

where Σj represents the sum over all Settlement Periods and Σi∈p represents the sum over all BM Units for which Party p is the Lead Party.

### 4.3A Determination of Market Price (MPj)

4.3A.1 Without prejudice to paragraphs 1.6.4(b) and 1.6.6(b), if in respect of a Settlement Period j and a Market Index Data Provider s either:

(a) the Individual Liquidity Threshold exceeds the Market Index Volume (QXPsj); or

(b) the Market Index Data Provider fails for whatever reason to submit the Market Index Data in time such that it can be taken into account in the relevant Settlement Run,

the Market Index Volume (QXPsj) and the Market Index Price (PXPsj) for that Market Index Data Provider shall be deemed to be zero.

4.3A.2 In respect of each Settlement Period the "Market Price" (MPj) is the amount determined as follows:

MPj = Σs {PXPsj * QXPsj} / Σs {QXPsj}

where Σs represents the sum over all Market Index Data Providers.

If Σs {QXPsj} = 0, then the Market Price for the Settlement Period shall be undefined, and the provisions of paragraph 4.4.4 shall apply.

4.3AA Determination of Deviation Volume (QDEij) for Trading Secondary BM Units

4.3.AA.1 In respect of each Trading Secondary BM Unit and each Settlement Period for which either a Bid-Offer Acceptance or a Wholesale Market Activity Notification has been received, the Deviation Volumes (QDEij) shall be determined as follows:

QDEij = QMij - SEVij

Where QM is the BM Unit Metered Volume and SEVij is the Settlement Expected Volume.

### 4.3B Determination of Period Supplier BM Unit Delivered Volume (QBSDij) for Secondary BM Units

4.3B.1 In respect of each Settlement Period, for each Secondary BM Unit, the Period Secondary BM Unit Non-Delivered Volume (QSNDij) is the amount determined as follows:

QSNDij = Max{ Min( QBSij, QNDOij ) , QNDBij }

4.3B.2 In respect of each Settlement Period, for each Secondary BM Unit, the Period Secondary BM Unit Delivered Volume (QSDij) is the amount determined as follows:

QSDij = QBSij - QSNDij

4.3B.3 In respect of each Settlement Period, for each Secondary BM Unit "i2", for each Primary BM Unit "i", the Period Secondary BM Unit Delivered Proportion (SPiji2) is the amount determined as follows:

SPiji2 = VBMUSDVi2ji / (VLPSDVi2j + ΣiVBMUSDViji2)

where Σi represents the summation over all Primary BM Units "i".

4.3B.4 In respect of each Settlement Period, for each Secondary BM Unit "i2", for each Primary BM Unit "i", the Period Secondary BM Unit Supplier Delivered Volume (QSDiji2) is the amount determined as follows:

(a) in respect of Trading Secondary BM Units:

QSDiji2 = QDEi2j * SPiji2

where QDEi2j represents Deviation Volume; and

(b) for all other Secondary BM Units:

QSDiji2 = QSDi2j * SPiji2

4.3B.5 In respect of each Settlement Period, for each Primary BM Unit "i", the Period Supplier BM Unit Delivered Volume (QBSDij) is the amount determined as follows:

QBSDij = Σi2QSDiji2

where Σi2 represents the sum over all Secondary BM Units i2 for which Primary BM Unit "i" is to be allocated a value of QSDiji2.

### 4.3C Determination of Period Secondary BM Unit Supplier Compensation (QSVij)

4.3C.1 In respect of each Settlement Period, for each Trading Secondary BM Unit with a non-zero value of QDEij, the Wholesale Market Proportion of Delivered Volume (WMi2j) is the amount determined as follows:

WMi2j = (QDEi2j - QSDi2j) / QDEi2j

provided that WMi2j shall be equal to or greater than 0 and equal to or less than 1.

4.3C.2 In respect of each Settlement Period the Period Secondary BM Unit Supplier Compensation (QCViji2) is the amount determined as follows:

QCViji2 = QSDiji2 * WMi2j

where QSDiji2 represents Period Secondary BM Unit Supplier Delivered Volume calculated in accordance paragraph 4.3B.4(a).

4.3C.3 In respect of each Settlement Period the Period Secondary BM Unit Direct Compensation (QDViji2) is the amount determined as follows:

(a) in respect of Trading Secondary BM Units:

QDViji2 = QSDiji2 - QCViji2

where QSDiji2 represents Period Secondary BM Unit Supplier Delivered Volume calculated in accordance paragraph 4.3B.4(a)

(b) in respect of all other Secondary BM Units:

QDViji2 = QSDiji2

where QSDiji2 represents Period Secondary BM Unit Supplier Delivered Volume calculated in accordance paragraph 4.3B.4(b)

4.3C.4 In respect of each Settlement Period, the Period BM Unit Supplier Compensation Volume (QSVij) shall be determined as follows:

QSVij = i2 Σ QCViji2+ i2Σ QDViji2

where QCViji2 represents Period Secondary BM Unit Supplier Compensation calculated in accordance with paragraph 4.3C.2 and QDViji2 represents Period Secondary BM Unit Direct Compensation calculated in accordance with paragraph 4.3C.3 and i2Σ represents the summation over  Secondary BM Units "i2"

4.3C.5 In respect of each Settlement Period, for each Secondary BM Unit, the Period Secondary BM Unit Compensation Volume is the amount determined as follows:

QCVji2 = i Σ QCViji2

where iΣ represents the summation over Primary BM Units"i".

4.3C.6 In respect of each Settlement Period, for each Secondary BM Unit, the Period Secondary BM Unit Direct Compensation Volume is the amount determined as follows:

QDVji2 = i Σ QDViji2

Where iΣ represents the summation over Primary BM Units"i".

### 4.4 Determination of Energy Imbalance Prices (SBPj and SSPj)

4.4.1 In respect of each Settlement Period the Final Ranked Set of System Actions shall be established in accordance with Annex T-1.

4.4.2 In respect of each Settlement Period if the Net Imbalance Volume is not equal to zero, and is a positive number, and {ΣiΣnΣk {QAOknij * TLMij} + Σm QBSABmj + Σt QSIVtj + Σc QSDCcj + Σc QBDCcj + ΣJ VGBjJ + RRAUSBj} is not equal to zero:

(a) the System Buy Price will be determined as follows:

SBPj = {ΣiΣnΣk {QAOknij * POnij * TLMij} + Σm {QBSABmj * BSAPmj} + Σt {QSIVtj * STAPtj} + {{QSDCj + QBDCj} * VoLL} + ΣJ {VGBJ * QHRRAPJ} + {RRAUSBj * 0}}

/ {ΣiΣnΣk {QAOknij * TLMij} + Σm QBSABmj + Σt QSIVtj + Σc QSDCcj + Σc QBDCcj + ΣJ VGBjJ + RRAUSBj}

+ {BPAj}

where Σi represents the sum over all BM Units, Σn represents the sum over all accepted Offers in the Final Ranked Set of System Buy Actions, Σk represents the sum over all Acceptances within the Settlement Period, Σm represents the sum over all Balancing Services Adjustment Buy Actions in the Final Ranked Set of System Buy Actions, Σt represents the sum over all STOR Actions in the Final Ranked Set of System Buy Actions, and Σc represents the sum over all Demand Control Instructions in the Final Ranked Set of System Buy Actions; and ΣJ represents the sum overall Quarter Hour Volume GB Need Met in the Final Ranked Set of System Buy Actions; and

(b) the System Sell Price shall be equal to the System Buy Price as determined in 4.4.2(a).

4.4.3 In respect of each Settlement Period if the Net Imbalance Volume is not equal to zero, and is a negative number, and {ΣiΣnΣk {QABknij * TLMij} + Σm QBSASmj } + ΣJ {VGBjJ} + {RRAUSSj} is not equal to zero:

(a) the System Sell Price will be determined as follows:

SSPj = {ΣiΣnΣk {QABknij * PBnij * TLMij} + Σm {QBSASmj * BSAPmj}} + ΣJ {VGBJ * QHRRAPJ} + {RRAUSSj * 0}}

/ {ΣiΣn Σk {QABknij * TLMij} + Σm {QBSASmj } + {SPAj} + ΣJ {VGBjJ} + RRAUSSj}

where Σi represents the sum over all BM Units, Σn represents the sum over all accepted Bids in the Final Ranked Set of System Sell Actions, Σk represents the sum over all Acceptances within the Settlement Period, and Σm represents the sum over all Balancing Services Adjustment Sell Actions in the Final Ranked Set of System Sell Actions; and ΣJ represents the sum overall Quarter Hour Volume GB Need Met in the Final Ranked Set of System Buy Actions; and

(b) the System Buy Price shall be equal to the System Sell Price as determined in 4.4.3(a).

4.4.3A In respect of each Settlement Period, if the Net Imbalance Volume is equal to zero, or if the Net Imbalance Volume is not equal to zero and is a positive number and {ΣiΣnΣk {QAOknij * TLMij} + Σm QBSABmj + Σt QSIVtj + Σc QSDCcj + Σc QBDCcj} + ΣJ {VGBjJ} + {RRAUSBj} is equal to zero, or if the Net Imbalance Volume is not equal to zero and is a negative number and {ΣiΣnΣk {QABknij * TLMij} + Σm QBSASmj} + ΣJ {VGBjJ} + {RRAUSSj} is equal to zero, then:

(a) the System Buy Price will (subject to paragraph 4.4.4) be equal to the Market Price (MPj); and

(b) the System Sell Price shall be equal to the System Buy Price as determined in 4.4.3A(a).

4.4.4 Without prejudice to paragraphs 1.6.4(b) and 1.6.6(b), if for whatever reason (including the submission or deemed submission of zero values or the absence of Market Index Data) in respect of a Settlement Period:

Σs QXPsj = 0

where Σs represents the sum over all Market Index Data Providers,

then, if the Net Imbalance Volume is equal to zero, or if the Net Imbalance Volume is not equal to zero and is a positive number and {ΣiΣnΣk {QAOknij * TLMij} + Σm QBSABmj + Σt QSIVtj + Σc QSDCcj + Σc QBDCcj} + ΣJ {VGBjJ} + {RRAUSBj} } is equal to zero, or if the Net Imbalance Volume is not equal to zero and is a negative number and {ΣiΣnΣk {QABknij * TLMij} + Σm QBSASmj} + ΣJ {VGBjJ} + {RRAUSSj} is equal to zero, then:

(a) the System Buy Price will be equal to zero; and

(b) the System Sell Price shall be equal to the System Buy Price as determined in 4.4.4(a).

### 4.5 Determination of Credited Energy Volumes (QCEiaj) for each Energy Account

4.5.1 In respect of each Settlement Period and each Energy Account, the Credited Energy Volume for each Primary BM Unit to be allocated to the corresponding Energy Account of the Subsidiary Party and of the Lead Party will be determined as follows:

(a) in the case of the corresponding Energy Account of each Subsidiary Party:

QCEiaj = {(QMij – QBSij) * (QMPRiaj/100) + QMFRiaj} * TLMij

where "i" in relation to QMij and QBSij represents Primary BM Units only and values of QCEiaj are then rounded towards zero to the nearest kWh;

(b) in the case of the corresponding Energy Account of the Lead Party:

QCEiaj = (QMij * TLMij) – ΣaQCEiaj

where "i" in relation to QMij and QBSij represents Primary BM Units only andΣa represents the sum over all Energy Accounts for Subsidiary Parties of the Lead Party (not including Energy Accounts for the Lead Party itself).

### 4.6 Determination of Energy Imbalance (QAEIaj) for each Energy Account

4.6.1 In respect of each Settlement Period, for each Energy Account, the Account Credited Energy Volume will be determined as follows:

QACEaj = ΣiQCEiaj

where Σi represents the sum over all Primary BM Units.

4.6.2 In respect of each Settlement Period, for each Energy Account and Virtual Balancing Account, the Account Period Balancing Services Volume will be determined as follows:

QABSaj = (ΣiQBSij * TLMij) + (Σi2QSNDi2j * TLMi2j)

where Σi in relation to QBSij represents the sum over all Primary BM Units for which such Energy Account is the corresponding Energy Account of the Lead Party;

Σi2 in relation to QSNDi2j represents the sum over all Secondary BM Units for which such Energy Account or Virtual Balancing Account (as the case may be) is the corresponding Energy Account or Virtual Balancing Account of the Lead Party;

Multiplication by TLMij in relation to QBSij is for the TLMij of that Primary BM Unit i;

Multiplication by TLMi2j in relation to QSNDi2j is for the TLMij of that Secondary BM Unit i2.

4.6.2A In respect of each Settlement Period, for each Energy Account, the Account Period Deviation Volume (QADEaj) will be determined as follows:

QADEaj = (∑i QDEij * WMij *TLMij)

where QDEij is the Secondary BM Unit Deviation Volume

4.6.3 In respect of each Settlement Period, for each Energy Account and Virtual Balancing Account, the Account Energy Imbalance Volume will be determined as follows:

QAEIaj = QACEaj + QADEa – QABSaj – QABCaj

4.6.4 In respect of each Settlement Period, the Total System Energy Imbalance Volume will be determined as follows:

TQEIj = ΣaQAEIaj

where Σa represents the sum over all Energy Accounts and Virtual Balancing Accounts other than the TC (Non-IEA) Energy Accounts held by the NETSO.

4.6.5 In respect of each Settlement Period, the Total Period Applicable Balancing Services Volume will be determined as follows:

TQASj = ΣiQASij

where Σi represents the sum over all BM Units.

### 4.7 Determination of Energy Imbalance Cashflows (CAEIaj and TCEIj)

4.7.1 In respect of each Settlement Period, the Account Energy Imbalance Cashflow for each Energy Account and Virtual Balancing Account, other than the TC (Non-IEA) Energy Accounts held by the NETSO, will be determined as follows:

if QAEIaj > 0 then CAEIaj = – QAEIaj * SSPj

otherwise CAEIaj = – QAEIaj * SBPj

In respect of each Settlement Period, the Account Energy Imbalance Cashflow for each Energy Account held by the NETSO will be determined as follows:

CAEIaj = 0

4.7.2 The Total System Energy Imbalance Cashflow will be determined as follows:

TCEIj = ΣaCAEIaj

where Σa represents the sum over all Energy Accounts and Virtual Balancing Accounts.

4.7.3 In respect of each Settlement Day, for each Party p, the Daily Party Energy Imbalance Cashflow shall be determined as:

CAEIp = Σj Σa∈p CAEIaj

where Σj represents the sum over all Settlement Periods and Σa∈p represents the sum over the Energy Accounts and Virtual Balancing Account of Party p.

### 4.8 Non-Delivery Rule and Calculations

4.8.1 In respect of each Settlement Period, for each BM Unit, the Period BM Unit Non-Delivered Offer Volume will be determined as follows:

QNDOij = Min{Max{QMEij – QMij, 0},(ΣnQAOnij + ΣnRRAOnij)}

where Σn, in relation to QAOnij, represents the sum over all Bid-Offer Pair Numbers for the Accepted Offer Volumes and Σn, in relation to RRAOnij, represents the sum over all Bid-Offer Pair Numbers for the RR Accepted Offer Volumes, for the BM Unit.

4.8.2 In respect of each Settlement Period, for each BM Unit, the Period BM Unit Non-Delivered Bid Volume will be determined as follows:

QNDBij = Max{Min{QMEij – QMij, 0},(ΣnQABnij + ΣnRRABnij)}

where Σn, in relation to QABnij, represents the sum over all Bid-Offer Pair Numbers for the Accepted Bid Volumes and Σn, in relation to RRABnij, represents the sum over all Bid-Offer Pair Numbers for the RR Accepted Bid Volumes, for the BM Unit.

4.8.3 In respect of each Settlement Period, for each BM Unit, if the Period BM Non-Delivered Offer Volume is greater than zero then to determine values of Offer Non-Delivery Volume (QNDOnij), the Period BM Unit Non-Delivered Offer Volume will be apportioned across all accepted Offers (AOnij) (being Accepted Offers Volumes (QAOnij) and for upward Quarter Hour RR Activations within the Settlement Period the associated Deemed Standard Product Offer Volume (DSPOJij) and the Replacement Reserve Instructed Offer Deviation Volume (IODij)), in the following way.

4.8.4 In respect of each Settlement Period, the set of all accepted Offers will be ranked in order of decreasing price. The accepted Offer with the highest price will be allocated Non-Delivery Order Number 1, the next highest priced accepted Offer will be allocated Non-Delivery Order Number 2 and so on until all accepted Offers for the Settlement Period have been allocated a Non-Delivery Order Number. The set of accepted Offers

{AOn1ij, AOn2ij, …….. AOnuij} is then a ranked set of accepted Offers.

4.8.5 The Offer Non-Delivery Volume will be allocated to the first accepted Offer in the list first, then, once the first accepted Offer has been wholly accepted, to the second accepted Offer and so on until the Period BM Unit Non-Delivered Offer Volume is fully apportioned.

4.8.6 Then the Offer Non-Delivery Volume for accepted Offer n, is:

QNDOnij = Min(AOnuij, RQNDOu-1ij)

where RQNDOu-1ij is the Remaining Period BM Unit Non-Delivered Offer Volume determined as:

RQNDOuij = RQNDOu-1ij – QNDOnu-1ij

and RQNDO0ij = QNDOij

and QNDOn0ij = 0

4.8.7 In respect of each Settlement Period, for each BM Unit, if the Period BM Non-Delivered Bid Volume is less than zero then to determine values of Bid Non-Delivery Volume (QNDBnij), the Period BM Unit Non-Delivered Bid Volume will be apportioned across all accepted Bids (ABnij) (being Accepted Bids Volumes (QABnij) and for downward Quarter Hour RR Activations within the Settlement Period the associated Deemed Standard Product Bid Volume (DSPBJij) and the Replacement Reserve Instructed Bid Deviation Volume (IBDij)), in the following way.

4.8.8 In respect of each Settlement Period, the set of all accepted Bids will be ranked in order of increasing price. The accepted Bid with the lowest price is allocated Non-Delivery Order Number 1, the next lowest priced accepted Bid is allocated Non-Delivery Order Number 2 and so on until all accepted Bids for the Settlement Period have been allocated a Non-Delivery Order Number. The set of accepted Bids {ABn1ij, ABn2ij, …….. ABnuij} is then a ranked set of accepted Bids.

4.8.9 The Bid Non-Delivery Volume will be allocated to the first accepted Bid in the list first, then, once the first accepted Bid has been wholly accepted, to the second accepted Bid and so on until the Period BM Unit Non-Delivered Bid Volume is fully apportioned.

4.8.10 Then the Bid Non-Delivery Volume for accepted Bid n, is:

QNDBnij = Max(ABnuij, RQNDBu-1ij)

where RQNDBu-1ij is the Remaining Period BM Unit Non-Delivered Bid Volume determined as:

RQNDBuij = RQNDBu-1ij – QNDBnu-1ij

and RQNDB0ij = QNDBij

and QNDBn0ij = 0

4.8.11 In respect of each Settlement Period, for each BM Unit, for each accepted Offer, the Non-Delivered Offer Charge will be determined as follows:

CNDOnij = QNDOnij * Max{(NDPOnij – SBPj), 0} * TLMij

4.8.12 In respect of each Settlement Period, for each BM Unit, for each accepted Bid, the Non-Delivered Bid Charge will be determined as follows:

CNDBnij = QNDBnij * Min{(NDPBnij – SSPj), 0} * TLMij

4.8.13 In respect of each Settlement Period, for each BM Unit, the BM Unit Period Non-Delivery Charge will be determined as follows:

CNDij = Σn (CNDOnij + CNDBnij)

where Σn represents the sum over all Bid-Offer Pair Numbers for the BM Unit.

4.8.14 In respect of each Settlement Period, the Total System Non-Delivery Charge will be determined as the sum of all BM Unit Period Non-Delivery Charges for BM Units as follows:

TCNDj = ΣiCNDij

where Σi represents the sum over all BM Units.

4.8.15 In respect of each Settlement Day, for each Party p, the Daily Party Non-Delivery Charge shall be determined as:

CNDp = Σj Σi∈p CNDij

where Σj represents the sum over all Settlement Periods and Σi∈p represents the sum over all BM Units for which Party p is the Lead Party.

4.8.16 For each accepted Offer allocated an Offer Non-Delivery Volume that is an Accepted Offer Volume, the Non-Delivered Offer Price for that accepted Offer n will be determined as follows:

NDPOnij = POnij

4.8.17 For each accepted Offer allocated an Offer Non-Delivery Volume that is a Deemed Standard Product Offer Volume (DSPOJij) associated to an upward Quarter Hour RR Activation, the Non-Delivered Offer Price for that accepted Offer n will be determined as follows:

NDPOnij = RRAPJ

where RRAPJ represents the Quarter Hour Replacement Reserve Activation Price associated to the Quarter Hour RR Activation.

4.8.18 For each accepted Offer allocated an Offer Non-Delivery Volume that is a Replacement Reserve Instructed Offer Deviation Volume (IODij) the Non-Delivered Offer Price for that accepted Offer n will be determined as follows:

NDPOnij = BEDPj

In respect of each Settlement Period, the Balancing Energy Deviation Price (BEDPj) shall be an amount equal to zero.

4.8.19 For each accepted Bid allocated a Bid Non-Delivery Volume that is an Accepted Bid, the Non-Delivered Bid Price for that accepted Bid n will be determined as follows:

NDPBnij = PBnij

4.8.20 For each accepted Bid allocated a Bid Non-Delivery Volume that is a Deemed Standard Product Bid Volume (DSPBJij) associated to a downward Quarter Hour RR Activation, the Non-Delivered Bid Price for that accepted Bid n will be determined as follows:

NDPBnij = RRAPJ

where RRAPJ represents the Quarter Hour Replacement Reserve Activation Price associated to the Quarter Hour RR Activation.

4.8.21 For each accepted Bid allocated a Bid Non-Delivery Volume that is a Replacement Reserve Instructed Bid Deviation Volume (IBDij) the Non-Delivered Bid Price for that accepted Bid n will be determined as follows:

NDPBnij = BEDPj

In respect of each Settlement Period, the Balancing Energy Deviation Price (BEDPj) shall be an amount equal to zero.

### 4.9 Determination of System Operator Cashflow (CSOj)

4.9.1 In respect of each Settlement Period, the System Operator Cashflow will be determined as follows:

CSOj = (TCBMj + TCRRj) – TCNDj

4.9.2 In respect of each Settlement Day, the Daily System Operator Cashflow will be determined as follows:

CSO = Σj CSOj

where Σj represents the sum over all Settlement Periods.

### 4.10 Determination of Residual Cashflow Allocations

4.10.1 In respect of each Settlement Period, the Total System Residual Cashflow will be determined as follows:

TRCj = TCIIj + CSO j + TCNDj – TCBMj - TCRRj + TCEIj

4.10.2 In respect of each Settlement Period, for each Energy Account, other than the TC (Non-IEA) Energy Accounts held by the NETSO, the Residual Cashflow Reallocation Proportion will be determined as follows:

RCRPaj = {Σ+i (QCEiaj) + Σ-i (– QCEiaj )}/ {Σa {Σ+i (QCEiaj) + Σ-i (– QCEiaj)}}

where Σ+i is, for each Energy Account a in Settlement Period j, the sum over all BM Units i other than Interconnector BM Units that are in delivering Trading Units, and

Σ-i is, for each Energy Account a in Settlement Period j, the sum over all BM Units i other than Interconnector BM Units that are in offtaking Trading Units, and

Σa represents the sum over all Energy Accounts a, other than the TC (Non-IEA) Energy Accounts held by the NETSO.

In respect of each Settlement Period, for each TC (Non-IEA) Energy Account held by the NETSO, the Residual Cashflow Reallocation Proportion will be determined as follows:

RCRPaj = 0

4.10.3 In respect of each Settlement Period, for each Energy Account, the Residual Cashflow Reallocation Cashflow will be determined as follows:

RCRCaj = RCRPaj * TRCj

4.10.4 In respect of each Settlement Day, for each Party p, the Daily Party Residual Settlement Cashflow shall be determined as:

RCRCp = Σj Σa∈p RCRCaj

where Σj represents the sum over all Settlement Periods and Σa∈p represents the sum over the Energy Accounts of Party p.

### 4.11 Determination of Compensation Cashflow Allocations

4.11.1 In respect of each Settlement Period, for each BM Unit, the Final Demand (FDij) shall be determined as follows:

FDij = MAX(BMUGDVij - SDTBMUij, 0)

4.11.2 In respect of each Settlement Period, for each Energy Account held by a Supplier, the Supplier Compensation Proportion (CMPaj) shall be determined as follows:

CMPaj = Σi FDij / Σa Σi FDij

4.11.3 In respect of each Settlement Period, the System Period Compensation Volume (QCVj) shall be determined as follows:

QCVj = Σ i2 QCVji2

4.11.4 In respect of each Settlement Period, for each Energy Account held by a Supplier, the Supplier Compensation Volume (QCVaj) shall be determined as follows:

QCVaj = QCVj * CMPaj

4.11.5 In respect of each Settlement Period, the Settlement Period Virtual Lead Party Compensation Cashflow (SVCCaj) shall be determined as follows:

SVCCaj = QCVij * SCRP

where SCRP means the Supplier Compensation Reference Price determined in accordance with paragraph 1.16.

4.11.6 In respect of each Settlement Day, for each Party p, the Daily Virtual Lead Party Compensation Cashflow (SCVp) shall be determined as follows:

SCVp = Σj Σa∈p SVCCaj

where Σj represents the sum over all Settlement Periods and Σa∈p represents the sum over the Energy Accounts of Party p.

4.11.7 In respect of each Settlement Period, the Period Supplier Compensation Cashflow (SPCCij) will be determined as follows:

SPCCij = QSVij * SCRP

4.11.8 In respect of each Settlement Day, for each Party p, the Daily Supplier Compensation Cashflow (SCCp) shall be determined as:

SCCp = Σj Σa∈p SPCCij

where Σj represents the sum over all Settlement Periods and Σa∈p represents the sum over the Energy Accounts of Party p.

4.11.9 In respect of each Settlement Period, the Period Direct Compensation Cashflow (SPDCji2) will be determined as follows:

SPDC ji2 = QDVji2 * SCRP

4.11.10 In respect of each Settlement Day, for each Party p, the Daily Direct Compensation Cashflow (SDCp) shall be determined as:

SDCp = Σj Σa∈p SPDC ji2

where Σj represents the sum over all Settlement Periods and Σa∈p represents the sum over the Energy Accounts of Party p.

## 5. SETTLEMENT

### 5.1 Responsibility of SAA

5.1.1 The SAA shall be responsible for the determination of Trading Charges and shall make all such intermediate and other calculations and determinations as are required to do so in accordance with paragraphs 2, 3 and 4 and to enable the SAA to comply with its reporting requirements under Section V.

### 5.2 Requirement to carry out Settlement Runs

5.2.1 In relation to each Settlement Day, the SAA shall carry out:

(a) no later than the relevant dates set out in the Settlement Calendar (subject to paragraph 1.4),

(i) an Interim Information Settlement Run;

(ii) an Initial Settlement Run;

(iii) four Timetabled Reconciliation Settlement Runs;

(b) any Post-Final Settlement Run required by the Panel pursuant to Section U2.

5.2.2 Not used.

5.2.3 In carrying out any Reconciliation Settlement Run, the SAA shall:

(a) use data submitted by the CDCA and SVAA pursuant to the corresponding Reconciliation Volume Allocation Runs;

(b) make any adjustment or revision to any data submitted by the NETSO which is to be made following the resolution of any Trading Dispute, and use such adjusted or revised data;

(c) use any adjusted or revised data submitted to it for the relevant Settlement Period by the CRA, the CDCA, the ECVAA, the NETSO, any Interconnector Administrator and any Market Index Data Provider;

(d) should the NETSO submit any revised Balancing Services Adjustment Data, use such revised data.

### 5.3 Submission of Settlement data

5.3.1 In relation to each Settlement Day, following each Settlement Run, the SAA shall provide to the FAA the data and information specified in paragraphs 5.3.2 to 5.3.4 on the Notification Date (subject to paragraph 1.4):

(a) specified in the Payment Calendar, in the case of the Initial Settlement Run or a Timetabled Reconciliation Settlement Run;

(b) determined pursuant to Section U2, in the case of a Post-Final Settlement Run.

5.3.2 The following information is to be submitted in relation to the Settlement Run:

(a) the Settlement Day;

(b) whether the Settlement Run is an Initial Settlement Run, Timetabled Reconciliation Settlement Run or Post-Final Settlement Run.

5.3.3 The following information is to be submitted in relation to each Trading Party:

(a) the identity of the Trading Party;

(b) the amount (shown as a debit or a credit in accordance with the applicable rules and conventions established in paragraph 1.2) for the Settlement Day, in respect of each of the following Trading Charges separately:

(i) Daily Party BM Unit Cashflow;

(ii) Daily Party Non-Delivery Charge;

(iii) Daily Party Energy Imbalance Cashflow;

(iv) Daily Party Information Imbalance Charge;

(v) Daily Party Residual Settlement Cashflow;

(vi) Daily Party RR Cashflow;

(vii) Daily Party RR Instruction Deviation Cashflow

(viii) Daily Virtual Lead Party Compensation Cashflow,

(ix) Daily Supplier Compensation Cashflow; and

(x) Daily Direct Compensation Cashflow

(c) the net credit or debit amount for the Settlement Day for all Trading Charges under paragraph (b), determined by the SAA for that Trading Party applying the rules and conventions established in paragraph 1.2.

5.3.4 In relation to the NETSO, the information to be submitted is the credit or debit amount (in accordance with the applicable rules and conventions in paragraph 1.2), for the Settlement Day, for the Daily System Operator Cashflow.

5.3.5 In relation to each Settlement Day, following the Interim Information Settlement Run, the SAA shall provide to the ECVAA the data and information specified in paragraphs 5.3.2 and 5.3.3, relating to each Interim Information Settlement Run, on the day that the Settlement Calendar specifies the Interim Information Settlement Run for the Settlement Day is to take place (subject to paragraph 1.4).

### 5.4 Failure of SAA's systems, etc

5.4.1 This paragraph 5.4 applies if (other than in the circumstances described in paragraph 1.4.5) the SAA is unable for any reason:

(a) to carry out any Settlement Run (not including an Interim Information Settlement Run); or

(b) to submit to the FAA data and information in accordance with paragraph 5.3

and as a result the data and information referred to in paragraph 5.3 in relation to that Settlement Run has not been submitted to and validated (in accordance with Section N6.2) by the FAA by the twentieth day after the Notification Date.

5.4.2 Where this paragraph 5.4 applies, the Panel shall estimate:

(a) for each Party:

(i) the amounts of the Trading Charges for the relevant Settlement Day; and

(ii) subject as follows, for each Settlement Period, the amounts which (in accordance with paragraph 4) are summed to establish Trading Charges for a Settlement Day;

provided that paragraph (ii) shall not apply to the extent that, in the Panel's opinion (in any particular circumstances), it is not reasonably practicable for the Panel to make or obtain estimates under that paragraph, or to do so in a way which is more specific and less approximate than the basis on which the estimate in paragraph (a) is otherwise to be made;

(b) the amount of the System Buy Price and the System Sell Price for each Settlement Period in the relevant Settlement Day.

5.4.3 The Panel's estimate shall be made on such basis and with such approximation as the Panel considers appropriate, having regard to all the circumstances and to the fact that any Timetabled Reconciliation Settlement Run remains to be carried out or (as the case may be) any Settlement Run has already been carried out.

5.4.4 Each BSC Agent and each Party shall cooperate with the Panel to the extent reasonably requested to enable the Panel to make the estimates under paragraph 5.4.2.

5.4.5 BSCCo shall submit the amounts estimated by the Panel under paragraph 5.4.2(a):

(a) to the FAA;

(b) to the SAA, for information;

and shall use the amounts estimated by the Panel under paragraph 5.4.2(b) for publication under Section V4.2.6.

5.4.6 The data estimated by the Panel shall be binding on all Parties (but without prejudice to any subsequent Reconciliation Settlement Run).

## 6. ADDITIONAL CALCULATIONS

### 6.1 Determination of Trading Unit Export and Import Volumes (QTUErj and QTUIrj)

6.1.1 In respect of each Trading Unit for each Settlement Period the "Trading Unit Export Volume" shall be determined as:

QTUErj = Σ(non-S) max(QMij, 0) + ΣN(AE) | CORCiNj |

where:

Σ(non-S) represents the sum over all BM Units other than Supplier BM Units belonging to the Trading Unit; and

ΣN(AE) represents the sum over all Consumption Component Classes that are associated with active export over all Supplier BM Units belonging to the Trading Unit.

6.1.2 In respect of each Trading Unit for each Settlement Period the "Trading Unit Import Volume" shall be determined as:

QTUIrj = Σ(non-S) min(QMij, 0) – ΣN(AI) | CORCiNj |

where:

Σ(non-S) represents the sum over all BM Units other than Supplier BM Units belonging to the Trading Unit; and

ΣN(AI) represents the sum over all Consumption Component Classes that are associated with active import over all Supplier BM Units belonging to the Trading Unit.

6.1.3 In respect of each Trading Unit for each Settlement Period the "Trading Unit Delivery Mode" shall be:

(a) "Delivering" if QTUErj + QTUIrj > 0; or

(b) "Offtaking" if QTUErj + QTUIrj ≤ 0.

## 7 SUBMISSION OF REPLACEMENT RESERVE DATA TO THE SVAA

7.1.1 In respect of each Settlement Day, for each BM Unit for which such data is received or determined by the NETSO under Section Q, the SAA shall send the SVAA an aggregate report of all Quarter Hour RR Activation Data in respect of each Quarter Hour period within each Replacement Reserve Auction Period for such Settlement Day.

## 8 CALCULATION OF BM UNIT CHARGEABLE DEMAND FOR THE EMR SETTLEMENT SERVICES PROVIDER

8.1.1 In respect of each Settlement Day, for each Supplier BM Unit, the BM Unit Chargeable Demand CBMUDij shall be:

CBMUDij = BMUADVij - NCBMUDij - GESBMUij

Where BMUADVij is the BM Unit Allocated Demand Volume and NCBMUDij is the Period BM Unit Non Chargeable Demand.

8.1.2 In respect of each Settlement Day, for each CVA BM Unit which has been included in an EMR CVA BM Unit declaration, the BM Unit Chargeable Demand CBMUDij shall be:

CBMUDij = 0

And for all other CVA BM Units, the BM Unit Chargeable Demand CBMUDij shall be:

CBMUDij = BMUADVij

8.1.3 The SAA shall apply the Transmission Loss Multiplier to the BM Unit Chargeable Demand to determine the TLM-adjusted BM Unit Chargeable Demand “TCBMUDij”.

TCBMUDij = CBMUDij * TLMij

8.1.4 The SAA shall, for each Settlement Day and Settlement Run, issue the TLM-adjusted BM Unit Chargeable Demand TCBMUDij to the EMR Settlement Services Provider.

8.1.5 In respect of each Settlement Period ‘j’ and Supplier BM Unit ‘i’, the BM Unit Gross Exempt Supply Purchase (GESBMUij) shall be:

(a) for all BM Units ‘i’ belonging to Trading Units which in the Settlement Period are delivering Trading Units:

GESBMUij = (1 + TLMO+j) * Σ i1=i QBESi1i2j

(b) for all BM Units ‘i’ belonging to Trading Units which in the Settlement Period are offtaking Trading Units:

GESBMUij = (1 + TLMO-j) * Σ i1=i QBESi1i2j

Where Σ i1=i denotes the sum over all Exempt Supply Notification Agents and BM Units ‘i2’ of those values of QBESi1i2j for which i1 is the BM Unit ‘i’.

## Annex T-1: Final Ranked Set of System Actions

### Part 1 – Derivation of Final Ranked Set of System Actions

## 1. INTRODUCTION

1.1 This Annex T-1 sets out:

(a) in this Part 1, the basis on which, for each Settlement Period, the Final Ranked Set of System Actions will be determined for the purposes of calculating the System Buy Price or (as the case may be) the System Sell Price pursuant to Section T4.4;

(b) in Part 2, detailed provisions for CADL Flagging, Arbitrage Tagging, NIV Tagging, determining the Replacement Price, and PAR Tagging for the purposes of Part 1;

(c) in Part 3, the determination of certain terms for reporting purposes.

1.2 For the purposes of the Code, in relation to a Settlement Period:

(a) in relation to a BM Unit and an Acceptance, an "accepted Offer" means the Period Accepted Offer Volume (QAOknij), and an "accepted Bid" means the Period Accepted Bid Volume (QABknij) but excluding Offers and Bids where the value of Period Accepted Offer Volume or Period Accepted Bid Volume (as the case may be) is zero or which are STOR Actions;

(b) a "System Buy Action" (QSBwj) means:

(i) in relation to each BM Unit, an accepted Offer that is not a STOR Action;

(ii) in relation to each Balancing Services Adjustment Buy Action, the Balancing Services Adjustment Buy Volume (QBSABmj) that is not a STOR Action;

(iii) in relation to each STOR Action, the STOR Instructed Volume (QSIVtj);

(iv) in relation to each Demand Control Impacted Settlement Period, the System Demand Control Volume (QSDCcj); and

(v) in relation to each Demand Control Impacted Settlement Period, the Balancing Demand Control Volume (QBDCcj);

(vii) in relation to Replacement Reserve Auction Results, the positive values of Quarter Hour Volume GB Need Met (VGBJj) in MWh for each Quarter Hour falling within Settlement Period j determined by the SAA as below:

VGBJ = GBJ * 0.25

where GBJ represents the Quarter Hour RR Activated Quantity associated to the Quarter Hour GB Need Met for Quarter Hour ‘J’

(viii) in relation to Replacement Reserve Auction Results, Replacement Reserve Aggregated Unpriced System Buy Actions (RRAUSBj) determined by the SAA for each Settlement Period as below:

RRAUSBj = max {(Σni RRAOnij + Σni RRABnij), 0}

+ max (ΣJ VIJj , 0) – max (ΣJ VGBJj, 0)

where VIJ represents the Quarter Hour Volume Interconnector Schedule to be determined from the Quarter Hour Interconnector Schedule (IJ) as below;

VIJ = IJ * 0.25

where IJ represents the Quarter Hour RR Activated Quantity associated to the Quarter Hour Interconnector Schedule for Quarter Hour ‘J’.

(c) a "System Sell Action" (QSSwj) means:

(i) in relation to each BM Unit, an accepted Bid that is not a Network Gas Supply Emergency Acceptance;

(ii) in relation to each Balancing Services Adjustment Sell Action, the Balancing Services Adjustment Sell Volume (QBSASmj);

(iii) in relation to Replacement Reserve Auction Results, the negative values of Quarter Hour Volume GB Need Met (VGBJj) in MWh for each Quarter Hour falling within Settlement Period j determined by the SAA as below:

VGBJ = GBJ * 0.25

where GBJ represents the Quarter Hour RR Activated Quantity associated to the Quarter Hour GB Need Met for Quarter Hour ‘J’

(iv) in relation to Replacement Reserve Auction Results, Replacement Reserve Aggregated Unpriced System Sell Actions (RRAUSSj) determined by the SAA for each Settlement Period as below:

RRAUSSj = min {(Σni RRAOnij + Σni RRABnij), 0}

+ min (ΣJ VIJj , 0) – min (ΣJ VGBJj, 0)

where VIJ represents the Quarter Hour Volume Interconnector Schedule to be determined from the Quarter Hour Interconnector Schedule (IJ) as below;

VIJ = IJ * 0.25

where IJ represents the Quarter Hour RR Activated Quantity associated to the Quarter Hour Interconnector Schedule for Quarter Hour ‘J’

(d) "System Action" means a System Buy Action or a System Sell Action;

(e) in relation to a System Buy Action or a System Sell Action, the "System Action Price" (SAP wj) is:

(i) in the case of an accepted Offer that is not a STOR Action and does not relate to a Winter Contingency BM Unit, the Offer Price (PO nij);

(ii) in the case of an accepted Bid, the Bid Price (PB nij);

(iii) in the case of an Balancing Services Adjustment Action that is not a STOR Action, the Balancing Services Adjustment Price (BSAPmj);

(iv) in the case of a STOR Action, the STOR Action Price (STAPtj); and

(v) in the case of a System Demand Control Volume or a Balancing Demand Control Volume, the VoLL;

(vii) in the case of Quarter Hour Volume GB Need Met, the associated Quarter Hour Replacement Reserve Activation Price (QHRRAPJ); and

(viii) in the case of Replacement Reserve Aggregated Unpriced System Actions, the price shall be equal to zero; and

(ix) in the case of an accepted Offer that relates to a Winter Contingency BM Unit, the price shall be equal to £99,999/MWh; and.

(f) a "Ranked Set" is a set of System Actions ranked in accordance with the further provisions of this Part 1; and references to the Ranked Sets are to the two Ranked Sets (of System Buy Actions and System Sell Actions respectively).

1.3 In this Annex T-1, references to summation over System Sell Actions or System Buy Actions are to summation (in relation to accepted Offers or accepted Bids) over all BM Units and Acceptances, and (in relation to Balancing Services Adjustment Actions) over all Balancing Services Adjustment Actions.

1.4 In any provision of this Annex T-1, a System Action is "Flagged" where (in relation to the steps in paragraphs 3, 4 and 5) it is a First-Stage Flagged System Action, or (in relation to the step in paragraph 8) a Second-Stage Flagged System Action; and otherwise (in relation to the relevant such step(s)) is "Unflagged".

1.5 Where (pursuant to any provision of this Annex T-1) a fraction of a System Action is to be defined in a particular way, the System Action shall be treated as if it were two System Actions comprising respectively such fraction, and the remainder, of the original System Action, and respectively defined, and not defined, in that way.

## 2. RANKED SETS

2.1 In relation to each Settlement Period:

(a) all System Buy Actions shall be ranked in order of System Action Price, lowest priced first, and numbered (from 1) accordingly;

(b) all System Sell Actions shall be ranked in order of System Action Price, highest priced first, and numbered (from 1) accordingly;

(c) the sets of System Buy Actions and System Sell Actions so ranked are the Initial Ranked Sets of System Actions.

2.2 Any Balancing Services Adjustment Action for which BSAPmj has a NULL value shall be ranked last in the applicable Ranked Set.

2.3 Following the establishing of the Initial Ranked Sets of System Actions in relation to a Settlement Period, each of the steps in paragraphs 3 to 11 below shall be applied (in the order set out) to each such Ranked Set, and following any such step a System Action in the Ranked Set may be re-classed or modified, or excluded (in whole or in part) from the Ranked Set.

2.4 Following each step in paragraphs 3 to 11 below in relation to a Settlement Period:

(a) each of the two Ranked Sets of System Actions will be re-established (and where relevant the System Actions renumbered) on the basis of such step;

(b) in the application of the following step, references to System Actions in either Ranked Set are to the System Actions as re-classed or modified in, and exclude any System Action which has been excluded from, the Ranked Set pursuant to the application of each preceding step.

2.5 In cases where System Buy Actions or (as the case may be) System Sell Actions have the same System Action Price, or where more than one System Buy Action or (as the case may be) System Sell Action has a NULL value of System Action Price, the ordering of such System Buy Actions or (as the case may be) System Sell Actions in the Ranked Sets (or any other set required under this Annex T-1) shall be random, but subject to the further provisions of paragraphs 13.5, 14.2(f) and 16.1(e) in Part 2.

2.6 Where, following any of the steps in this Part 1 either of the Ranked Sets is empty, no further such step shall be taken in relation to such Ranked Set.

## 3. CADL FLAGGING

3.1 This paragraph 3 applies in relation to each accepted Offer and accepted Bid in the Initial Ranked Sets of System Actions.

3.2 Each accepted Offer and accepted Bid which is CADL Flagged in accordance with paragraph 12 of Part 2 shall be a First-Stage Flagged System Action.

3.3 The Ranked Sets of System Actions following the application of this paragraph 3 are the CADL Flagged Ranked Sets of System Actions.

## 4. SO-FLAGGING

4.1 This paragraph 4 applies in relation to each System Action in the CADL Flagged Ranked Sets of System Actions.

4.2 Each accepted Offer and accepted Bid for which the Acceptance was classified by the NETSO as 'SO-Flagged' shall be a First-Stage Flagged System Action.

4.3 Each Balancing Services Adjustment Action which was classified by the NETSO as 'SO-Flagged' shall be a First-Stage Flagged System Action.

4.3A Each System Demand Control Volume shall be a First-Stage Flagged System Action.

4.4 The Ranked Sets of System Actions following the application of this paragraph 4 are the SO-Flagged Ranked Sets of System Actions.

## 5. EMERGENCY INSTRUCTIONS

5.1 This paragraph 5 applies in relation to each System Action in the SO-Flagged Ranked Sets of System Actions.

5.2 Each accepted Offer and accepted Bid for which the Acceptance was an Emergency Acceptance classified by the NETSO as 'Emergency Flagged' shall be a First-Stage Flagged System Action.

5.3 The Ranked Sets of System Actions following the application of this paragraph 5 are the Emergency Flagged Ranked Sets of System Actions.

## 6. DE MINIMIS TAGGING

6.1 This paragraph 6 applies in relation to each System Action in the Emergency Flagged Ranked Sets of System Actions.

6.2 Each accepted Offer for which, in relation to the relevant BM Unit and Offer, QAOnij < DMAT is a De Minimis Tagged System Buy Action.

6.3 Each accepted Bid for which, in relation to the relevant BM Unit and Bid, | QABnij | < DMAT is a De Minimis Tagged System Sell Action.

6.4 Each Balancing Services Adjustment Buy Action for which QBSABmj < DMAT is a De Minimis Tagged System Buy Action.

6.5 Each Balancing Services Adjustment Sell Action for which | QBSASmj | < DMAT is a De Minimis Tagged System Sell Action.

6.6 Each De Minimis Tagged System Action shall be excluded from the applicable Ranked Set of System Actions.

6.7 The Ranked Sets of System Actions following the application of this paragraph 6 are the De Minimis Tagged Ranked Sets of System Actions.

## 7. ARBITRAGE TAGGING

7.1 This paragraph 7 applies in relation to each System Action in the De Minimis Tagged Ranked Sets of System Actions.

7.2 Each System Action which is Arbitrage Tagged in accordance with paragraph 13 of Part 2 shall be excluded from the Ranked Sets of System Actions.

7.3 The Ranked Sets of System Actions following the application of this paragraph 7 are the Arbitrage Tagged Ranked Sets of System Actions.

## 8. CLASSIFICATION

8.1 This paragraph 8 applies in relation to each First-Stage Flagged System Action in the Arbitrage Tagged Ranked Sets of System Actions.

8.2 For each First-Stage Flagged System Buy Action (w') in the Ranked Set of System Buy Actions:

(a) if the System Action Price (SAP w'j) is greater than the System Action Price of the highest-priced Unflagged System Buy Action in the Ranked Set, the System Buy Action (w') shall become a Second-Stage Flagged System Action;

(b) otherwise, the System Buy Action (w') shall become Unflagged, subject to paragraph 8.4.

8.3 For each First-Stage Flagged System Sell Action (w') in the Ranked Set of System Sell Actions:

(a) if the System Action Price (SAP w'j) is less than the System Action Price of the lowest-priced Unflagged System Sell Action in the Ranked Set, the System Sell Action (w') shall become a Second-Stage Flagged System Action;

(b) otherwise, the System Sell Action (w') shall become Unflagged, subject to paragraph 8.4.

8.4 Any Balancing Services Adjustment Action for which BSAPmj has a NULL value shall not become Unflagged under paragraph 8.2(b) or 8.3(b).

8.5 The Ranked Sets of System Actions following the application of this paragraph 8 are the Classified Ranked Sets of System Actions.

## 9. NIV TAGGING

9.1 This paragraph 9 applies in relation to each System Action in the Classified Ranked Sets of System Actions.

9.2 Each System Action which is NIV Tagged in accordance with paragraph 14 of Part 2 shall be excluded from the Ranked Sets of System Actions.

9.3 In accordance with paragraph 14 of Part 2, one of the Ranked Sets of System Actions will necessarily be empty following the application of paragraph 9.2.

9.4 The Ranked Set of System Actions following the application of this paragraph 9 which is not necessarily empty is the NIV Tagged Ranked Set of System Actions.

## 10. REPLACEMENT PRICING OF SECOND-STAGE FLAGGED SYSTEM ACTIONS

10.1 This paragraph 10 applies in relation to Second-Stage Flagged System Actions (if any) in the NIV Tagged Ranked Set of System Actions.

10.2 If NIV is positive:

(a) the System Action Price of each Second-Stage Flagged System Buy Action in the NIV Tagged Ranked Set of System Buy Actions shall be reset to be equal to the Replacement Buy Price determined in accordance with paragraph 15 of Part 2; and for all further purposes of this Annex T and Section T4 the System Action Price of such System Buy Actions shall be deemed to be the Replacement Buy Price, and such System Buy Actions shall become Unflagged;

(b) the System Buy Actions in the Ranked Set shall be re-ranked in order of their System Action Prices as modified under paragraph (a), cheapest first.

10.3 If NIV is zero or negative:

(a) the System Action Price of each Second-Stage Flagged System Sell Action in the NIV Tagged Ranked Set of System Sell Actions shall be reset to be equal to the Replacement Sell Price determined in accordance with paragraph 15 of Part 2; and for all further purposes of this Annex T and Section T4 the System Action Price of such System Sell Actions shall be deemed to be the Replacement Sell Price, and such System Sell Actions shall become Unflagged;

(b) the System Sell Actions in the Ranked Set shall be re-ranked in order of their System Action Prices as modified under paragraph (a), most expensive first.

10.4 The Ranked Set of System Actions following the application of this paragraph 10 is the Replacement-Priced Ranked Set of System Actions.

## 11. PAR TAGGING

11.1 This paragraph 11 applies to the System Actions in the Replacement-Priced Ranked Set of System Actions.

11.2 Each System Action which is PAR Tagged in accordance with paragraph 16 of Part 2 shall be excluded from the Ranked Set of System Actions.

11.3 The Ranked Set of System Actions following the application of this paragraph 11 is the Final Ranked Set of System Actions.

### Part 2 - Detailed Provisions

## 12. CADL FLAGGING

12.1 In relation to each Acceptance, k, for a particular BM Unit, another Acceptance for the same BM Unit is "related" to Acceptance k where such other Acceptance has a Bid-Offer Acceptance Time that falls within the period:

(a) from and including the spot time at the start of the Settlement Period which falls three Settlement Periods prior to the Settlement Period in which the Bid-Offer Acceptance Time for Acceptance k falls, and

(b) to and including the spot time at the end of the Settlement Period which falls three Settlement Periods after the Settlement Period in which the Bid-Offer Acceptance Time for Acceptance k falls.

12.2 In relation to each Acceptance k, another Acceptance is "continuous" with Acceptance k if it is related to Acceptance k, and:

(a) the spot time associated with:

(i) the first Point Acceptance Volume of the Acceptance is earlier, and

(ii) the last Point Acceptance Volume of the Acceptance is not earlier

than the spot time associated with the first Point Acceptance Volume of Acceptance k; or

(b) the spot time associated with:

(i) the last Point Acceptance Volume of the Acceptance is later, and

(ii) the first Point Acceptance Volume of the Acceptance is not later than

the spot time associated with the last Point Acceptance Volume of Acceptance k; or

(c) the Acceptance is continuous (in accordance with paragraph (a) or (b)) with another Acceptance which is determined (including, for the avoidance of doubt, by virtue of this paragraph (c)) to be a continuous Acceptance in relation to Acceptance k.

12.3 In relation to each Acceptance k, for a particular BM Unit, the Continuous Acceptance Duration (CADki) shall be the duration of the period:

(a) commencing at the earliest spot time associated with:

(i) any value of Point Acceptance Volume for Acceptance k; or

(ii) any Point Acceptance Volume for any Acceptance that is a continuous Acceptance in relation to Acceptance k, and

(b) ending at the latest spot time associated with:

(i) any value of Point Acceptance Volume for Acceptance k; or

(ii) any Point Acceptance Volume for any Acceptance that is a continuous Acceptance in relation to Acceptance k.

12.4 In relation to each accepted Offer and accepted Bid in the Ranked Sets of System Actions, if (for the associated Acceptance k) CADki < CADL, then the accepted Offer or accepted Bid shall be CADL Flagged.

12.5 In relation to each Demand Control Volume, the Continuous Acceptance Duration (CAD) shall be the duration of the period:

(a) commencing at the Demand Control Event Start Point; and

(b) ending at the Demand Control Event End Point.

12.6 In relation to each Demand Control Volume in the Ranked Sets of System Actions, if CAD < CADL, then the Demand Control Volume shall be CADL Flagged.

## 13. ARBITRAGE TAGGING

13.1 In respect of each Settlement Period, System Actions in the De Minimis Tagged Ranked Sets of System Actions will be defined as Arbitrage Tagged in the following way.

*[Editorial: from paragraph 13.2 to the end of paragraph 16 the equations were rendered as maths markup on the web page, and the copy-paste broke them into single characters. They have been rebuilt in the same run-together notation the BSC uses in its prose (e.g. QSBwvj, ∑v QSBwvj ≤ -QSSgj), keeping the symbols in source order. Subscripts, superscripts and fraction bars are not marked, so where a formula involves a fraction or nested subscripts, check it against the original.]*

13.2 If, for the highest priced System Sell Action, QSSgj (if any) which is not already an Arbitrage Tagged System Sell Action, there exists any System Buy Action QSBwj which is not already an Arbitrage Tagged System Buy Action for which it is true that SAPwj ≤ SAPgj, then the following procedure will be carried out:

(a) All System Buy Actions for which SAPwj ≤ SAPgj will be ranked in price order, lowest priced first.

(b) The set of such System Buy Actions QSBw1j, QSBw2j, …, QSBwwj is then a ranked set of System Buy Actions for all of which it is true that SAPwj ≤ SAPgj.

(c) Then for all v in such Ranked Set such that:

```
∑v QSBwvj ≤ -QSSgj
```

where ∑v is the sum over all ranked System Buy Actions up to v,

the QSBwvj will be defined as Arbitrage Tagged and the fraction φ of QSSgj which is equal to ∑v -QSBwvj will be defined as Arbitrage Tagged (this fraction may be one (1)).

(d) If:

```
∑v QSBwvj ≤ -QSSgj
```

where Σv is the sum over all ranked System Buy Actions up to v,

then, if a ranked System Buy Action, v+1 exists, the fraction γ of QSBwv+1j which satisfies

```
∑v QSBwvj + γ * QSBwv+1j = -QSSgj
```

will also be defined as Arbitrage Tagged and QSSgj will be defined as Arbitrage Tagged.

13.3 The process in paragraph 13.2 will then be repeated for the highest priced System Sell Action (if any) that remains not Arbitrage Tagged.

13.4 If, for the purposes of carrying out the procedure in paragraph 13.2:

(a) there are two or more System Sell Actions that are not Arbitrage Tagged, that have the same highest System Action Price, or

(b) there are two or more ranked System Buy Actions that have the same System Action Price

then one of the System Sell Actions or (as the case may be) System Buy Actions will be selected at random.

13.5 If the completed application of paragraphs 13.1 to 13.4 inclusive (the 'initial calculation') would result in there being any System Sell Action or ranked System Buy Action which:

(a) is not Arbitrage Tagged, but

(b) has the same price (other than merely by virtue of being a fraction 1 - γ or 1 - φ pursuant to the initial calculation) as a System Sell Action or (as the case may be) ranked System Buy Action which is Arbitrage Tagged,

then:

(i) all such System Sell Actions QSSwrj or ranked System Buy Actions QSBwrj (whether or not Arbitrage Tagged on the basis of the initial calculation) which have the same price are "threshold" System Actions;

(ii) no threshold System Action shall be defined as Arbitrage Tagged pursuant to the relevant provision, but instead the fraction δ of each threshold System Sell Action QSSwrj or threshold System Buy Action QSBwrj which satisfies the following shall be defined as Arbitrage Tagged:

```
δ * ∑wr QSSwrj = ∑wr' QSSwr'j
```

or (as the case may be)

```
δ * ∑wr QSBwrj = ∑wr' QSBwr'j
```

where

**∑wr** is the sum over all threshold System Sell Actions or (as the case may be) threshold System Buy Actions, and

**∑wr'** is the sum over all threshold System Sell Actions or (as the case may be) threshold System Buy Actions (including a fraction γ or φ) which, on the basis of the initial calculation would have been defined as Arbitrage Tagged.

### 14. NIV TAGGING

14.1 In respect of each Settlement Period, the Net Imbalance Volume will be determined as follows:

NIVj = Σw QSBwj – Σw (-QSSwj)

where Σw is the sum over all System Actions in the Classified Ranked Sets.

14.2 In respect of each Settlement Period, System Actions in the Classified Ranked Sets will be defined as NIV Tagged in the following way.

(a) If:

```
∑w' -QSSw'j = 0
```

where ∑w' is the sum over System Sell Actions in the Classified Ranked Set; or

```
∑w* QSBw*j = 0
```

where ∑w* is the sum over System Buy Actions in the Classified Ranked Set:

then no System Actions will be NIV Tagged.

Otherwise, the following procedure will be carried out.

(b) If:

```
∑w' -QSSw'j ≤ ∑w* QSBw*j
```

where ∑w' is the sum over the System Sell Actions and ∑w* is the sum over the System Buy Actions in the Classified Ranked Sets,

then all the System Sell Actions (for all values of w’) in the Ranked Set of System Sell Actions will be defined as NIV Tagged.

(c) Since ∑w' -QSSw'j ≤ ∑w* QSBw*j there must exist a number e and a number φ (which may be a fraction or zero) for which

```
∑w' -QSSw'j = ∑wv>e* QSBwvj* + φ * QSBwej*
```

where ∑w' is the sum over all System Sell Actions and ∑wv>e* is the sum over those System Buy Actions for which v is greater than e.

Subject to paragraph (f), each System Buy Action numbered e+1 or higher in the Classified Ranked Set for which this is true will be defined as NIV Tagged. If φ is a fraction rather than zero, then the fraction φ of the System Buy Action numbered e will be defined as NIV Tagged.

(d) If:

Σw’ (-QSSw’j) > Σw* QSBw*j

where Σw’ is the sum over the System Sell Actions and Σw* is the sum over the System Buy Actions,

then all the System Buy Actions (for all values of w*) in the Ranked Set of System Buy Actions will be defined as NIV Tagged.

(e) Since Σw’ (-QSSw’j) > Σw* QSBw*j there must exist a number e and a number φ (which may be a fraction or zero) for which

```
∑w* QSBw*j = ∑w'v>e -QSSw'vj + φ * -QSSw'ej
```

where ∑w* is the sum over all System Buy Actions and ∑w'v>e is the sum over those System Sell Actions for which v is greater than e.

Subject to paragraph (f), each System Sell Action numbered e+1 or higher in the Classified Ranked Set for which this is true will be defined as NIV Tagged. If φ is a fraction rather than zero, then the fraction φ of the System Sell Action numbered e will be defined as NIV Tagged.

(f) However, for each of paragraphs (c) and (e) (each a "relevant provision") separately, if the application of the relevant provision (the "initial calculation") would result in there being any System Action which:

(1) is not defined as NIV Tagged, but

(2) has the same price (including a NULL price) (other than merely by virtue of being a fraction (1 - φ) pursuant to the initial calculation) as, in the case of a System Buy Action, a System Buy Action which is NIV Tagged or, in the case of a System Sell Action, a System Sell Action which is NIV Tagged,

then:

(i) all such System Buy Actions QSBw'rj or System Sell Actions QSSw'rj (whether or not NIV Tagged on the basis of the initial calculation) which have the same price are "threshold" System Actions;

(ii) no threshold System Action shall be defined as NIV Tagged pursuant to the relevant provision, but instead the fraction δ of each threshold System Buy Action QSBw'rj or threshold System Sell Action QSSw'rj which satisfies the following shall be defined as NIV Tagged:

```
δ * ∑w'r QSBw'rj = ∑w'r' QSBw'r'j
```

or (as the case may be)

```
δ * ∑w'r QSSw'rj = ∑w'r' QSSw'r'j
```

where

**∑w'r** is the sum over all threshold System Buy Actions or (as the case may be) threshold System Sell Actions, and

**∑w'r'** is the sum over all threshold System Buy Actions or (as the case may be) threshold System Sell Actions (including a fraction φ thereof) which, on the basis of the initial calculation would have been defined as NIV Tagged.

### 15. REPLACEMENT PRICE

15.1 In respect of each Settlement Period, the Replacement Buy Price or Replacement Sell Price will be determined as follows.

15.2 If NIV is positive:

(a) if there are no Unflagged System Actions in the NIV Tagged Ranked Set, the Replacement Buy Price shall be the Market Price, unless the Market Price is undefined in which case the Replacement Buy Price shall be zero;

(b) otherwise, the Replacement Buy Price shall be determined as:

RBP j = Σw' (QSBw'j * SAPw'j) / Σw' QSBw'j

where

Σw' is the sum over all Qualifying Unflagged System Actions in the NIV Tagged Ranked Set.

15.3 For the purposes of paragraph 15.2:

(a) if ∑w QSBwj ≤ RPAR, all Unflagged System Buy Actions in the NIV Tagged Ranked Set will be defined as Qualifying;

(b) if ∑w QSBwj > RPAR:

(i) the Unflagged System Buy Actions in the NIV Tagged Ranked Set shall be ranked in price order, lowest priced first;

(ii) as ∑w QSBwj > RPAR there must exist a number f and a number ∅ (which may be a fraction or zero) for which:

```
RPAR = ∑w'v>f QSBw'vj + ∅ * QSBw'fj
```

where

```
∑w'v>f
```

is the sum over those System Buy Actions for which v is greater than f.

(iii) each of the System Buy Actions numbered f+1 or higher in the Ranked Set of Unflagged System Buy Actions for which this is true will be defined as Qualifying. If ∅ is a fraction rather than zero, then the fraction (∅) of the System Buy Action numbered f will be defined as Qualifying.

15.4 If NIV is negative or zero:

(a) if there are no Unflagged System Actions in the NIV Tagged Ranked Set the Replacement Sell Price shall be the Market Price, unless the Market Price is undefined in which case the Replacement Sell Price shall be zero;

(b) otherwise, the Replacement Sell Price shall be determined as:

RSP j = Σw' (QSSw'j * SAPw'j) / Σw' QSSw'j

where

Σw' is the sum over all Qualifying Unflagged System Actions in the NIV Tagged Ranked Set

15.5 For the purposes of paragraph 15.4:

(a) if Σw –QSSwj ≤ RPAR *[source shows £, a Symbol-font ≤]*, all Unflagged System Sell Actions in the NIV Tagged Ranked Set will be defined as Qualifying;

(b) if Σw –QSSwj > RPAR:

(i) the Unflagged System Sell Actions in the NIV Tagged Ranked Set shall be ranked in price order, highest priced first;

(ii) as Σw -QSSwj > RPAR there must exist a number f and a number ∅ (which may be a fraction or zero) for which:

```
RPAR = ∑w'v>f -QSSw'vj + ∅ * -QSSw'fj
```

where ∑w'v>f is the sum over those System Sell Actions for which v is greater than f;

(iii) each of the System Sell Actions numbered f+1 or higher in the Ranked Set for which this is true will be defined as Qualifying. If ∅ is a fraction rather than zero, then the fraction (∅) of the System Sell Action numbered f will be defined as Qualifying.

### 16. PAR TAGGING

16.1 In respect of each Settlement Period, System Actions in the Replacement-Priced Ranked Set will be defined as PAR Tagged in the following way:

(a) If:

```
∑w' QSBw'j ≤ PAR
```

where ∑w' is the sum over the System Buy Actions in the Replacement-Priced Ranked Set

then none of the System Buy Actions (for all values of w') will be defined as PAR Tagged.

(b) If Σw' (QSBw'j) > PAR there must exist a number f and a number ∅ (which may be a fraction or zero) for which

```
PAR = ∑w'v>f QSBw'vj + ∅ * QSBw'fj
```

where ∑w'v>f is the sum over those System Buy Actions for which v is greater than f.

Subject to paragraph (e), each System Buy Action numbered 1 to f-1 in the Replacement-Priced Ranked Set for which this is true will be defined as PAR Tagged. If ∅ is a fraction rather than zero, then the fraction 1 - φ of the System Buy Action numbered f will be defined as PAR Tagged.

(c) If:

```
∑w' -QSSw'j ≤ PAR
```

where ∑w' is the sum over the System Sell Actions in the Replacement-Priced Ranked Set

then none of the System Sell Actions (for all values of w') will be defined as PAR Tagged.

(d) If Σw' (-QSSw'j) > PAR there must exist a number f and a number ∅ (which may be a fraction or zero) for which

```
PAR = ∑w'v>f -QSSw'vj + ∅ * (-QSSw'fj)
```

where ∑w'v>f is the sum over those System Sell Actions for which v is greater than f.

Subject to paragraph (e), each of the System Sell Actions numbered 1 to f-1 in the Replacement-Priced Ranked Set for which this is true will be defined as PAR Tagged. If ∅ is a fraction rather than zero, then the fraction 1 - φ of the System Sell Action numbered f will be defined as PAR Tagged.

(e) However, for each of paragraphs (b) and (d) (each a "relevant provision") separately, if the application of the relevant provision (the "initial calculation") would result in there being any System Buy Action or System Sell Action which:

(1) is not defined as PAR Tagged, but

(2) has the same price (including a NULL price) (other than merely by virtue of being a fraction ∅ pursuant to the initial calculation) as a System Buy Action or (as the case may be) a System Sell Action which is PAR Tagged,

then:

(i) all such System Buy Actions QSBw'rj or System Sell Actions QSSw'rj (whether or not PAR Tagged) which have the same price are "threshold" System Actions;

(ii) no threshold System Action shall be defined PAR Tagged pursuant to the relevant provision, but instead the fraction δ of each threshold System Buy Action QSBw'rj or threshold System Sell Action QSSw'rj which satisfies the following shall be defined as PAR Tagged:

```
δ * ∑w'r QSBw'rj = ∑w'r' QSBw'r'j
```

or (as the case may be)

```
δ * ∑w'r QSSw'rj = ∑w'r' QSSw'r'j
```

where

**∑w'r** is the sum over all threshold System Buy Actions or (as the case may be) threshold System Sell Actions, and

**∑w'r'** is the sum over all threshold System Buy Actions or (as the case may be) threshold System Sell Actions (including a fraction 1 - φ thereof) which, on the basis of the initial calculation would have been defined as PAR Tagged.

### Part 3 – Terms for Reporting

## 17. Table of terms

For the purposes of reporting the following amounts shall be determined as set out below:

| Term | Acronym | Basis of determination |
|---|---|---|
| **1. Amounts by BM Unit and Bid Offer Pair (summed over all Acceptances k)** |  |  |
| Period Accepted Offer Volume | QAOknij | Defined in Section T3.8.1 |
| Period BM Unit Total Accepted Offer Volume | QAOnij | Defined in Section T3.9.1 |
| Period BM Unit Total Tagged Accepted Offer Volume | QATOnij | The amount (if any) of QAOnij which was excluded from the Ranked Set of System Buy Actions by De Minimis Tagging, Arbitrage Tagging, NIV Tagging and/or PAR Tagging under paragraphs 6, 7, 9 or 11 of Part 1. |
| Period BM Unit Total Repriced Accepted Offer Volume | QAROnij | The amount (if any) of QAOnij which was not Tagged and which was Second-Stage Flagged in the NIV Tagged Ranked Set (and accordingly subject to Replacement Pricing under paragraph 10.2(a) of Part 1). |
| Period BM Unit Total Originally-priced Accepted Offer Volume | QAOPOnij | The amount (if any) of QAOnij which was not Tagged and which was Unflagged in the NIV Tagged Ranked Set (and accordingly not subject to Replacement-pricing under paragraph 10.2(a) of Part 1). |
| Period Accepted Bid Volume | QABknij | Defined in Section T3.8.2 |
| Period BM Unit Total Accepted Bid Volume | QABnij | Defined in Section T3.9.2 |
| Period BM Unit Total Tagged Accepted Bid Volume | QATBnij | The amount (if any) of QABnij which was excluded from the Ranked Set of System Sell Actions by De Minimis Tagging, Arbitrage Tagging, NIV Tagging and/or PAR Tagging under paragraphs 6, 7, 9 or 11 of Part 1. |
| Period BM Unit Total Repriced Accepted Bid Volume | QARBnij | The amount (if any) of QABnij which was not Tagged and which was Second-Stage Flagged in the NIV Tagged Ranked Set (and accordingly subject to Replacement Pricing under paragraph 10.3(a) of Part 1). |
| Period BM Unit Total Originally-priced Accepted Bid Volume | QAOPBnij | The amount (if any) of QABnij which was not Tagged and which was Unflagged in the NIV Tagged Ranked Set (and accordingly not subject to Replacement Pricing under paragraph 10.3(a) of Part 1). |
| **2. Amounts by Balancing Services Adjustment Action** |  |  |
| Balancing Services Adjustment Buy Volume | QBSABmj | Defined in Table X-2 of Section X-2. |
| Balancing Services Adjustment Tagged Buy Volume | QBSATBmj | The amount (if any) of QBSABmj which was excluded from the Ranked Set of System Buy Actions by De Minimis Tagging, Arbitrage Tagging, NIV Tagging and/or PAR Tagging under paragraphs 6, 7, 9 or 11 of Part 1. |
| Balancing Services Adjustment Repriced Buy Volume | QBSARBmj | The amount (if any) of QBSABmj which was not Tagged and which was Second-Stage Flagged in the NIV Tagged Ranked Set (and accordingly subject to Replacement-pricing under paragraph 10.2(a) of Part 1). |
| Balancing Services Adjustment Originally-priced Buy Volume | QBSAOPBmj | The amount (if any) of QBSABmj which was not Tagged and which was Unflagged in the NIV Tagged Ranked Set (and accordingly not subject to Replacement-pricing under paragraph 10.2(a) of Part 1). |
| Balancing Services Adjustment Sell Volume | QBSASmj | Defined in Table X-2 of Section X-2. |
| Balancing Services Adjustment Tagged Sell Volume | QBSATSmj | The amount (if any) of QBSASmj which was excluded from the Ranked Set of System Sell Actions by De Minimis Tagging, Arbitrage Tagging, NIV Tagging and/or PAR Tagging under paragraphs 6, 7, 9 or 11 of Part 1. |
| Balancing Services Adjustment Repriced Sell Volume | QBSARSmj | The amount (if any) of QBSASmj which was not Tagged and which was Second-Stage Flagged in the NIV Tagged Ranked Set (and accordingly subject to Replacement-pricing under paragraph 10.3(a) of Part 1). |
| Balancing Services Adjustment Originally-priced Sell Volume | QBSAOPSmj | The amount (if any) of QBSASmj which was not Tagged and which was Unflagged in the NIV Tagged Ranked Set (and accordingly not subject to Replacement-pricing under paragraph 10.3(a) of Part 1). |
| **3. Amounts by Total System – Bid-Offer Pairs** |  |  |
| Total System Accepted Offer Volume | TQAOj | ΣiΣn QAOnij |
| Total System Tagged Accepted Offer Volume | TQATOj | ΣiΣn QATOnij |
| Total System Repriced Accepted Offer Volume | TQAROj | ΣiΣn QAROnij |
| Total System Originally-priced Accepted Offer Volume | TQAOPOj | ΣiΣn QAOPOnij |
| Total System Accepted Bid Volume | TQABj | ΣiΣn QABnij |
| Total System Tagged Accepted Bid Volume | TQATBj | ΣiΣn QATBnij |
| Total System Repriced Accepted Bid Volume | TQARBj | ΣiΣn QARBnij |
| Total System Originally-priced Accepted Bid Volume | TQAOPBj | ΣiΣn QAOPBnij |
| **4. Amounts by Total System – Balancing Services Adjustment Actions** |  |  |
| Total System Balancing Services Adjustment Buy Volume | TQBSABj | Σm QBSABmj |
| Total System Balancing Services Adjustment Tagged Buy Volume | TQBSATBj | Σm QBSATBmj |
| Total System Balancing Services Adjustment Repriced Buy Volume | TQBSARBj | Σm QBSARBmj |
| Total System Balancing Services Adjustment Originally-priced Buy Volume | TQBSAOPBj | Σm QBSAOPBmj |
| Total System Balancing Services Adjustment Sell Volume | TQBSASj | Σm QBSASmj |
| Total System Balancing Services Adjustment Tagged Sell Volume | TQBSATSj | Σm QBSATSmj |
| Total System Balancing Services Adjustment Repriced Sell Volume | TQBSARSj | Σm QBSARSmj |
| Total System Balancing Services Adjustment Originally-priced Sell Volume | TQBSAOPSj | Σm QBSAOPSmj |
| **5. Amounts by Total System – all System Actions** |  |  |
| Total System Buy Volume | TQSBj | TQAOj + TQBSABj |
| Total System Tagged Buy Volume | TQSTBj | TQATOj+ TQBSATBj |
| Total System Repriced Buy Volume | TQSRBj | TQAROj+ TQBSARBj |
| Total System Originally-priced Buy Volume | TQSOPBj | TQAOPOj+ TQBSAOPBj |
| Total System Sell Volume | TQSSj | TQABj+ TQBSASj |
| Total System Tagged Sell Volume | TQSTSj | TQATBj+ TQBSATSj |
| Total System Repriced Sell Volume | TQSRSj | TQARBj+ TQBSARSj |
| Total System Originally-priced Sell Volume | TQSOPSj | TQAOPBj+ TQBSAOPSj |

In the table above Σi represents the sum over all BM Units, Σn represents the sum over all Bid-Offer Pair Numbers for a BM Unit, and Σm represents the sum over all Balancing Services Adjustment Actions.

## Annex T-2: Transmission Loss Factors

## 1. Introduction

1.1 This Annex T-2 sets out the basis for determining Transmission Loss Factors.

1.2 Transmission Loss Factors will be determined by the TLFA:

(a) by reference to Nodal TLFs determined by the application of the Load Flow Model in accordance with paragraph 8.2; and

(b) in accordance with the further provisions of paragraph 8.

1.3 For the purposes of this Annex T-2:

(a) a "node" is a point on an electrical network at which:

(i) a power flow on to or off the network can occur; or

(ii) two or more circuits (forming part of the network) meet;

(b) a "load flow model" is a mathematical model of an electrical network which represents power flows between pairs of adjacent nodes on the network, and from which nodal TLFs can be determined for each node for given power flows;

(c) a "nodal TLF", in relation to a node on a network and a given power flow at the node, is the rate of change of electrical losses on the network with respect to a change of power flow at that node, with network balance being maintained by the slack node;

(d) the "Load Flow Model" is the load flow model established and adopted by the TLFA in accordance with paragraph 3;

(e) the "slack node" is a node that acts:

(i) for the purposes of a load flow model, as a sink for power flow surpluses or as a source for power flow deficits arising from inaccuracies in the load flow model; and

(ii) in relation to each pair of adjacent nodes in a load flow model, as the reference node for calculating the phase angle of the power flow between the nodes;

(f) in relation to a BSC Year, BSC Spring shall be considered to be the periods 1st April to 31st May and 1st March to 31st March in that BSC Year; and

(g) for the avoidance of doubt, this Annex T-2 shall take effect so as to require to be done anything necessary to be done before the Relevant Implementation Date of Modification P350 in order to give effect to this Annex T-2 with effect on and from the Relevant Implementation Date of Modification P350.

## 1A. Transmission Loss Factors relating to the BSC Year commencing 1st April 2025

1A.1 For the purposes of this paragraph 1A:

(a) the "Current BSC Year" means the BSC Year commencing 1st April 2025;

(b) the "Preceding BSC Year" means the BSC Year commencing 1st April 2024;

(c) the "input data" means the data inputs described in paragraph 8.2(f);

(d) the "TLF verification criteria" means the criteria set out in paragraph 1A.3.

1A.2 By no later than 21 November 2025 the Panel shall determine:

(a) whether the Transmission Loss Factors applicable to the Current BSC Year comply with the TLF verification criteria; and

(b) where those Transmission Loss Factors are not in compliance with the TLF verification criteria, that the Transmission Loss Factors should be recalculated. Any such recalculation shall:

(i) give effect to the Panel’s determination under paragraph 1A.3;

(ii) otherwise be determined in accordance with this Annex T-2; and

(c) a timetable for performing the activities set out in this paragraph 1A (whether or not the Panel has determined that a recalculation is required),

and each Party and the TLFA shall comply with any such instructions and timetable determined by the Panel under this paragraph.

1A.3 The criteria referred to in paragraph 1A.2 are as follows:

(a) that the Seasonal Zonal TLF (TLFZS) values reflect the expected change in total variable losses from a marginal change in demand or generation (averaged across each Season, and across the Nodes in each Zone). The expected change is the change that might reasonably be expected (based on expectations when BSC Modification P350 was approved, and on the TLF values previously used in Settlement); and

(b) to the extent that (a) is not met, whether a recalculation using amended input data is likely to yield TLFZS values that do substantially improve compliance with (a).

1A.4 With effect from the later of 1st April 2025 or the Relevant Implementation Date of Modification P485, but subject to paragraph 1A.5, the Transmission Loss Factors to be used for the purposes of Section T2 shall be the Transmission Loss Factors determined for the Preceding BSC Year.

1A.5 Following a determination by the Panel under paragraph 1A.2 (and, where applicable, the recalculation of Transmission Loss Factors), the Transmission Loss Factors for the Current BSC Year, for the purposes of Section T2, shall be:

(a) where the Panel has determined that no recalculation of Transmission Loss Factors for the Current BSC Year is required, the Transmission Loss Factors originally determined for the Current BSC Year by the TLFA and published on the BSC Website in December 2024; or

(b) where the Panel has required the recalculation of Transmission Loss Factors, the Transmission Loss Factors that have been recalculated pursuant to paragraph 1A.2,

and such Transmission Loss Factors shall take effect from and including the first BSC Season that commences immediately following the Panel’s determination.

1A.6 The Panel’s determinations (including any recalculation of Transmission Loss Factors under paragraph 1A.2) shall, in the absence of manifest error, be final and binding on all Parties.

## 2. LFM Specification

2.1 The Panel shall, in consultation with the NETSO and other Parties and the Authority, establish (to form part of the BSC Service Description for the TLFA) a specification ("LFM Specification") for a load flow model for the AC Transmission System, to operate based on the data inputs specified in paragraph 8.2(f), and consistent with the requirements in paragraph 2.2.

2.2 The LFM Specification shall provide for the following assumptions and approximations to be made in the load flow model:

(a) only electrical losses associated with power flows between adjacent nodes (forming part of the network) ("Load Flow Model power flows") will be used in determining nodal TLFs; and

(b) in respect of the power flow between adjacent nodes it is assumed:

(i) there is no Reactive Power component;

(ii) the ratio of the change of power flow over a circuit to the injection of power at a given node is not dependent on the overall electrical load on the network;

(iii) the sine of the voltage phase angle is equal to the phase angle (as measured in radians); and

(iv) the power flow in a circuit is equal to the difference in the voltage phase angles across the circuit multiplied by the circuit susceptance.

## 3. Load Flow Model

3.1 The TLFA shall establish, and (subject to paragraph 3.2) adopt and from time to time modify, a load flow model which implements and complies with the LFM Specification.

3.2 The TLFA shall not adopt such load flow model or a modification thereof unless the model reviewer has reported to the Panel (in such terms, and as to such materiality, as the Panel may decide) that such model or modification complies with the LFM Specification and the Panel accepts such model or modification; and the TLFA shall not modify the Load Flow Model except as the Panel may instruct or agree.

3.3 The Panel shall appoint, and may from time to time reappoint or replace, an independent expert (the "model reviewer") for the following purposes:

(a) to inspect and test the Load Flow Model and report to the Panel as to the compliance of the Load Flow Model with the LFM Specification or any particular aspect of the LFM Specification:

(i) before the Load Flow Model is first used for the purposes of this Annex T-2;

(ii) upon any modification of the Load Flow Model (whether upon a change to the LFM Specification or otherwise); and

(iii) on any other occasion on which the Panel decides to obtain such a report; and

(b) to verify and report to the Trading Disputes Committee as to whether Nodal TLFs were determined in accordance with the Load Flow Model, on any occasion on which it is necessary to do so for the purposes of any Trading Dispute.

3.4 Any report produced by the model reviewer on Nodal TLFs for the Trading Disputes Committee shall be final and binding on all Parties (save in the case of fraud or manifest error) and if a Party refers a Trading Dispute to arbitration under Section W3.6, then save in the case of fraud or manifest error, the arbitrator(s) appointed in accordance with Section H7 shall not have the power to query, review or in any way revise the model reviewer's report on whether Nodal TLFs were, or were not, determined in accordance with the Load Flow Model.

3.5 BSCCo shall enter into a contract of engagement (for the term for which the model reviewer is appointed) with the model reviewer, which shall, inter alia:

(a) provide terms of reference set or approved by the Panel for the model reviewer; and

(b) require the model reviewer to enter into a confidentiality undertaking in favour of the TLFA in such terms as the Panel shall reasonably require or approve.

3.6 As regards the Load Flow Model:

(a) the TLFA shall deposit a copy of the Load Flow Model in escrow with an escrow agent in such form and on such terms and conditions as BSCCo may require; and

(b) the TLFA shall be responsible for the payment of all fees due to the escrow agent.

3.7 The TLFA shall be required to make the Load Flow Model (and any details thereof) available to the model reviewer and the BSC Auditor (and as may be required by the arbitral tribunal in connection with any arbitration); but shall not be required to make available or disclose the Load Flow Model or details thereof to the Panel, any Panel Committee or Parties other than to BSCCo as required for the provision of the reports set out in Table 9 in Annex V-1 or in accordance with the release terms included in the escrow agreement pursuant to paragraph 3.6.

3.8 Subject to paragraph 3.4, once the Load Flow Model (or any modification thereof) has been adopted by the TLFA, Nodal TLFs which are properly determined by the Load Flow Model shall be definitive; and accordingly:

(a) (without prejudice to any question as to whether such Nodal TLFs were in fact properly determined) no Party may challenge or question on any grounds the validity of any Nodal TLF which was so determined; and

(b) any modification of the Load Flow Model shall have effect only prospectively, that is for the purposes of determining Transmission Loss Factors in respect of BSC Years for which (at the time the modification was made) Transmission Loss Factors have not already been determined in accordance with paragraph 8.

3.9 For the purposes of paragraph 3.8(a), Nodal TLFs are properly determined if they are determined by and only by the application of the Load Flow Model on the basis of data input in compliance with the further provisions of this Annex T-2.

## 4. Zones, Nodes and Mapping

4.1 For the purposes of this Annex T-2:

(a) a "Zone" is the geographic area:

(i) in which the following lie:

(1) a GSP Group (there being no more than one GSP Group in any one Zone);

(2) any part of an Offshore Transmission System which connects directly to that GSP Group; and/or

(3) any part of an Offshore Transmission System which connects to the onshore AC Transmission System at a point within the geographic area of that GSP Group; and

(ii) which is determined by the Panel (applying such criteria as it shall decide in its discretion) but so that the Zones are mutually exclusive and are contained within the area specified in the terms of the ESO Licence;

(b) the Panel may from time to time review and upon reasonable notice to Parties change its determination of any Zones, where there is any change in the GSP Group, any change to a part of the AC Transmission System contained within the Zone, upon the application of a Party or otherwise on its own initiative; provided that a change in the determination of any Zone(s) shall be effective only in relation to BSC Years for which (at the time the change was made) Transmission Loss Factors have not already been determined in accordance with paragraph 8;

(c) the Panel may, but shall not be required to, consult any Party on the determination of any part of the boundary of a Zone where it considers there is material doubt as to such boundary; and

(d) the Panel shall publish a description of the Zones from time to time (but may do so by referring to any other document which describes or identifies the geographic areas determined by the Panel to be the Zones).

4.2 For the purposes of this Annex T-2:

(a) a "Node" is a node on the AC Transmission System;

(b) the NETSO shall:

(i) identify each Node and prepare, keep up-to-date, and maintain, a list of all Nodes, each identified or capable of being identified geographically; and

(ii) provide to BSCCo, as soon as practicable, each updated list of Nodes; and

(c) BSCCo shall publish the same on the BSC Website.

4.3 For the purposes of this Annex T-2:

(a) a "network mapping statement" is a statement of the following:

(i) for each Volume Allocation Unit (other than a GSP Group, or BM Unit embedded in a Distribution System), the Node which represents or best represents that Volume Allocation Unit or (as the case may be) the Boundary Point(s) at which that Volume Allocation Unit is connected to the AC Transmission System (it being recognised that one Node may represent several such points);

(ii) for each Node which represents or best represents a Volume Allocation Unit in accordance with paragraph (i), the Zone in which the Node lies or should best be considered to lie;

(iii) for each BM Unit, the Zone in which the BM Unit lies, in accordance with what has been established under paragraphs (i) and (ii), except that:

(1) Interconnector BM Units lie in the Zone in which (in accordance with paragraph (ii)) the Node for the relevant Interconnector lies; and

(2) Supplier BM Units, Secondary BM Units and other BM Units embedded in a Distribution System lie in the Zone which incorporates the geographical area of the corresponding GSP Group; and

(iv) for each HVDC Boundary, the Node which represents or best represents the HVDC Boundary; and

(b) in relation to each BSC Year:

(i) the "reference network mapping statement" is the version of the network mapping statement approved by the Panel under paragraph 4.4(b);

(ii) for the purposes of determining Nodal power flows under paragraph 8.2(e) the reference network mapping statement shall be used and any update thereof under paragraph 4.4(d) shall have no effect;

(iii) the "prevailing network mapping statement" is the reference network mapping statement as from time to time updated by BSCCo under paragraph 4.4(d); and

(iv) the prevailing network mapping statement shall be used to determine the Zone in which each BM Unit is located for the purposes of determining from time to time the Transmission Loss Factor applicable to such BM Unit under paragraph 8.6(a).

4.4 For each BSC Year:

(a) BSCCo shall:

(i) prepare (on the basis of data relating to the Reference Year, and taking account of the prevailing network mapping statement for the preceding BSC Year) a draft reference network mapping statement;

(ii) provide a copy of the draft reference network mapping statement to the Panel and each Party, wherever practicable not later than 31st August in the preceding BSC Year; and

(iii) submit to the Panel any representations or comments on the draft statement which were received from Parties within ten Business Days after the statement was provided under paragraph (ii);

(b) the Panel shall approve the draft reference network mapping statement with such amendments (if any) as the Panel may decide, taking into account (inter alia):

(i) any representations and comments submitted to it under paragraph (a)(iii); and

(ii) any determination made by the Panel under paragraph 4.5 in relation to a question or dispute which was raised with the Panel within the ten Business Days referred to in paragraph 4.4(a)(iii) in the preceding BSC Year;

(c) BSCCo shall, no later than 19th October in the preceding BSC Year, provide the approved reference network mapping statement to the TLFA and the NETSO and publish the same on the BSC Website; and

(d) following the approval of the reference network mapping statement under paragraph (b) BSCCo shall:

(i) from time to time update the reference network mapping statement (or prevailing network mapping statement as the case may be) so as to reflect any changes to, or in respect of, the list of Nodes, the definition of any Zone, BM Units, Transmission System Boundary Points, HVDC Boundaries or Systems Connection Points and any determination by the Panel under paragraph 4.5 (such updated reference network mapping statement being the prevailing network mapping statement); and

(ii) publish each such update of the prevailing network mapping statement on the BSC Website.

4.5 Any question or dispute as to the matters in sub-paragraphs (i) and (ii) of paragraph 4.3(a) shall be determined by the Panel in its discretion, after consultation with the NETSO and the Lead Party(ies) of the BM Unit(s) affected by such question or dispute, having regard (so far as appears to the Panel to be relevant) to the parts of the AC Transmission System in which power flows are typically most influenced by changes in power flows at the relevant Node or (as the case may be) the relevant BM Unit.

4.6 The NETSO, each Distribution System Operator, the CRA and the CDCA shall cooperate with and provide information as may be required to BSCCo and the Panel in connection with the preparation of each network mapping statement and the determination of any question or dispute under paragraph 4.5.

## 5. Transmission Network Data and HVDC Boundary Data

5.1 For the purposes of this Annex T-2:

(a) "Transmission Network Data" means the following data relating to the AC Transmission System:

(i) the identity of each pair of adjacent Nodes; and

(ii) for each such pair of Nodes, values of the resistance and the reactance between the Nodes;

(b) Transmission Network Data shall be established on the assumption of an 'intact network', that is disregarding any planned or other outage of any part of the AC Transmission System; and

(c) "HVDC Boundary Data" means the NETSO’s estimate (based on metering or other available data) of the flow of Active Energy to or from each HVDC Boundary.

5.2 The NETSO shall determine Transmission Network Data and the HVDC Boundary Data in good faith and based on its operational knowledge of the Transmission System, and in accordance with any relevant assumption made in the LFM Specification, but in the absence of a manifest error no Party may challenge or question the validity or correctness of the Transmission Network Data or the HVDC Boundary Data determined by the NETSO.

5.3 The NETSO and the TLFA shall cooperate so as to ensure that the form and medium in which Transmission Network Data and the HVDC Boundary Data is provided by the NETSO is compatible with the Load Flow Model and the BSC Agent System on which the Load Flow Model operates.

## 6. Distribution Network Data

6.1 For the purposes of this Annex T-2:

(a) "Distribution Network Data" means the following data showing power flows from an Offshore Transmission Connection Point to other Grid Supply Points on a Distribution System:

(i) the identity of each Node that represents an Offshore Transmission Connection Point (an "Offshore Transmission Connection Point Node");

(ii) the identity of each Node on a Distribution System (representing a Grid Supply Point) to which power flows from an Offshore Transmission Connection Point Node (a "corresponding Node"); and

(iii) the percentage of net energy received by each corresponding Node, of the total energy flowing from the Offshore Transmission Connection Point Node, as an estimated average value for each Reference Year; and

(b) Distribution Network Data shall be established on the assumption of an 'intact network', that is disregarding any planned or other outage of any part of a Distribution System.

6.2 Each Distribution System Operator shall determine Distribution Network Data in good faith for each Distribution System that it operates, based on the operation of that Distribution System and in accordance with any relevant assumption made in the LFM Specification.

6.3 Each Distribution System Operator and the TLFA shall cooperate so as to ensure that the form and medium in which Distribution Network Data is provided by the Distribution System Operator is compatible with the Load Flow Model and the BSC Agent System on which the Load Flow Model operates.

6.4 Any question or dispute as to the determination of Distribution Network Data pursuant to paragraph 6.2 shall be determined by the Panel in its discretion, after consultation with the relevant Distribution System Operator, the NETSO and the Lead Party(ies) of the BM Unit(s) affected by such question or dispute, having regard (so far as appears to the Panel to be relevant) to the parts of the Total System in which power flows are typically most influenced by changes in power flows at the relevant Node(s) or (as the case may be) the relevant BM Unit.

6.5 Each Distribution System Operator, the NETSO, the CRA and the CDCA shall cooperate with and provide information as may be required to BSCCo and the Panel in connection with the determination of any question or dispute under paragraph 6.4.

## 7. Sample Settlement Periods

7.1 For each BSC Year, Transmission Loss Factors shall be determined by reference to Nodal TLFs for sample Settlement Periods in the twelve month period (a "Reference Year") ending 31st August in the preceding BSC Year.

7.2 For the purposes of so determining Transmission Loss Factors, the Panel, after consultation with the NETSO and other Parties:

(a) shall divide the Reference Year into a number of different periods (each a "Load Period"), representing (in the opinion of the Panel) typically different levels of load on the AC Transmission System, defined by time of day, day of week, season and such other factors as the Panel considers relevant, such that every Settlement Period in the Reference Year falls into one and only one Load Period;

(b) shall specify, for each Load Period, a representative (in the opinion of the Panel) number of sample Settlement Periods (each a "Sample Settlement Period") within that Load Period; and

(c) will revise the specification of Load Periods or Sample Settlement Periods (if required) for each BSC Year.

7.3 BSCCo shall, not later than 31st August in the preceding BSC Year, notify the specification of each Load Period and the Sample Settlement Periods to the TLFA, the NETSO and the CDCA, and publish such specification on the BSC Website.

## 8. Determination of TLFs

8.1 For each BSC Year, Transmission Loss Factors for each BM Unit shall be determined in accordance with this paragraph 8.

8.2 For each Sample Settlement Period:

(a) the NETSO shall, not later than 5th October in the preceding BSC Year, send to BSCCo the Transmission Network Data and the HVDC Boundary Data;

(b) each Distribution System Operator shall, not later than 5th October in the preceding BSC Year, send to BSCCo the Distribution Network Data;

(c) the CDCA shall, not later than 5th October in the preceding BSC Year, send to BSCCo Metered Volumes for each Volume Allocation Unit (other than GSP Groups and BM Units embedded in a Distribution System);

(d) BSCCo shall, not later than 19th October in the preceding BSC Year, send to the TLFA the information received by BSCCo pursuant to paragraphs 8.2(a), 8.2(b) and 8.2(c);

(e) the TLFA shall translate the:

(i) Metered Volume data provided by BSCCo; and

(ii) flows of Active Energy at HVDC Boundaries,

to power flows (on the assumption they are constant in a Settlement Period) for each Node by applying the reference network mapping statement ("Nodal power flows"); and

(f) the TLFA shall input into the Load Flow Model the Transmission Network Data under paragraph (a), the Distribution Network Data under paragraph (b) and Nodal power flows under paragraph (e), and apply the Model to derive a nodal TLF for each Node ("Nodal TLF").

8.2A For each Zone and for each Settlement Period in the Reference Year, BSCCo shall, not later than 19th October, send to the TLFA:

(a) the sum of BM Unit Metered Volume (QMij) for all BM Units in the Zone (other than Secondary BM Units and Interconnector BM Units) belonging to Trading Units that are delivering Trading Units in the Settlement Period;

(b) the sum of BM Unit Metered Volume (QMij) for all BM Units in the Zone (other than Secondary BM Units and Interconnector BM Units) belonging to Trading Units that are offtaking Trading Units in the Settlement Period; and

(c) the sum of BM Unit Metered Volume (QMij) for all BM Units in the Zone, Secondary BM Units.

8.3 For each Sample Settlement Period, the TLFA shall determine the Zonal TLF (TLFZj) for each Zone according to the following formula:

TLFZj = ΣN (TLFNj * QMNj) / ΣN QMNj

where for that Settlement Period, and for each Node in that Zone (determined by the TLFA on the basis of the reference network mapping statement):

TLFNj is the value of Nodal TLF; and

QMNj is the absolute value of the Nodal power flow, disregarding any power flows to or from an Interconnector or an HVDC Boundary;

and where ΣN is summation by Node in a Zone.

8.4 For each BSC Season (the "relevant BSC Season") in each BSC Year, the TLFA shall determine the Seasonal Zonal TLF (TLFZS) for each Zone according to the following formula:

TLFZS = Σp ((ΣS TLFZj / SpS) * JpS) / Σp JpS

where (in relation to the Reference Year):

SpS is the number of Sample Settlement Periods within a Load Period which fall within the relevant BSC Season;

JpS is the total number of Settlement Periods falling within a Load Period which fall within the relevant BSC Season;

ΣS is summation by Sample Settlement Periods within a Load Period which fall within the relevant BSC Season; and

Σp is summation by Load Period within the relevant BSC Season.

8.5 For each BSC Year:

(a) the TLFA shall, not later than 30th November in the preceding BSC Year:

(i) determine the Adjusted Seasonal Zonal TLF (ATLFZS) for each Zone and each BSC Season according to the following formula:

ATLFZS = (TLFZS * 0.5) + TLFAS

where, for the relevant BSC Season, TLFAS is the Transmission Loss Factor Adjustment value determined in accordance with paragraph 9;

(ii) calculate indicative values of TLMij, TLMO+j and TLMO-j for every Settlement Period in the Reference Year using the rules set out in Section T2 and the metered data provided by BSCCo pursuant to paragraph 8.2A save that TLFij shall be zero;

(iii) calculate indicative values of TLMij, TLMO+j and TLMO-j for every Settlement Period in the Reference Year using the rules set out in Section T2 and the metered data provided by BSCCo pursuant to paragraph 8.2A save that TLFij shall be determined by applying to the Reference Year the ATLFZS values calculated for the forthcoming BSC Year in accordance with paragraph 8.5(a)(i); and

(iv) send the Seasonal Zonal TLFs, the Adjusted Seasonal Zonal TLFs and the indicative TLMij, TLMO+j and TLMO-j values to BSCCo; and

(b) BSCCo shall, not later than 31st December in the preceding BSC Year, publish on the BSC Website:

(i) the Adjusted Seasonal Zonal TLF (ATLFZS) for each Zone and each BSC Season;

(ii) the Seasonal Zonal TLF (TLFZS) for each Zone and each BSC Season;

(iii) the Transmission Loss Factor Adjustment (TLFAS) for each BSC Season;

(iv) indicative values of TLMij, TLMO+j and TLMO-j for every Settlement Period in the Reference Year calculated by the TLFA pursuant to paragraph (a)(ii); and

(v) indicative values of TLMij, TLMO+j and TLMO-j for every Settlement Period in the Reference Year calculated by the TLFA pursuant to paragraph (a)(iii),

provided that the TLMij, TLMO+j and TLMO-j data referred to in this paragraph 8.5 shall be indicative only and shall not replace and shall be without prejudice to the determination and application of the actual TLMij, TLMO+j and TLMO-j values for the purposes of Settlement in accordance with Section T2.3.

8.6 For each BSC Season in each BSC Year:

(a) the Transmission Loss Factor (TLFij) for each BM Unit shall be the Adjusted Seasonal Zonal TLF (ATLFZS) for the Zone in which that BM Unit is located (allocated on the basis of the prevailing network mapping statement) and for that BSC Season;

(b) the TLFA shall, not later than 30th November in the preceding BSC Year, determine and send the Transmission Loss Factors for each BM Unit to BSCCo;

(c) BSCCo shall, not later than 31st December in the preceding BSC Year, send such Transmission Loss Factors to the CRA; and

(d) upon any revision of the network mapping statement under paragraph 4.4(d), in relation to any BM Unit affected by such revision, BSCCo shall determine the new or revised Transmission Loss Factors (in accordance with the prevailing network mapping statement) and send such Transmission Loss Factors to the CRA.

8.7 The CRA shall maintain in CRS, as BM Unit registration data, the Transmission Loss Factors for each BM Unit.

## 9. Determination of the Transmission Loss Factor Adjustment (TLFAS)

9.1 Subject to paragraph 9.3, the Transmission Loss Factor Adjustment (TLFAS) shall be the value calculated annually by the TLFA for each BSC Season as follows:

TLFAS = – Σj {Σ+(non-I) (QMij * TLFZS * 0.5) / Σ+(non-I) QMij} / N

Where

Σj is summation by Settlement Period in a BSC Season within the Reference Year;

Σ+(non-I) represents the sum over all BM Units (other than Interconnector BM Units) belonging to Trading Units that are delivering Trading Units; and

N is the total number of Settlement Periods in that BSC Season of the Reference Year.

9.2 Subject to paragraph 9.3, the TLFA shall send the Transmission Loss Factor Adjustments to BSCCo by not later than 30th November in the preceding BSC Year.

9.3 The Transmission Loss Factor Adjustment value shall be zero for all BSC Years if the NETSO has received a direction to that effect from the Competition and Markets Authority (or any successor to that body) on or before 23 November 2017 in which case the NETSO shall notify BSCCo as soon as possible after receiving such direction.

## 10. Role and powers of the NETSO

10.1 For the purposes of this paragraph 10, "determination of Transmission Loss Factors" shall be construed as including the steps and processes:

(a) set out in this Annex T-2 for the determination of Transmission Loss Factors; and

(b) any other steps and processes necessary to enable compliance with the Transmission Losses Principle as set out in the ESO Licence (the "Transmission Losses Principle").

10.2 Where the NETSO is unable or has reasonable grounds to believe that it will be unable to comply with the Transmission Losses Principle, it shall be entitled to assume responsibility for the determination of Transmission Loss Factors pursuant to this Annex T-2 by giving prior written notice to the Panel and BSCCo setting out:

(a) the time and date from which the NETSO shall assume responsibility for the determination of Transmission Loss Factors;

(b) with reference to this Annex T-2, the extent to which the NETSO shall assume responsibility for the determination of Transmission Loss Factors; and

(c) whether the NETSO requires the suspension of the functions and duties of the TLFA,

(the "Transmission Loss Factor Step In Notice").

10.3 Upon receipt of a Transmission Loss Factor Step In Notice (or any amended notice issued by the NETSO to the Panel and BSCCo), BSCCo shall immediately publish such notice on the BSC Website.

10.4 If the NETSO issues a Transmission Loss Factor Step In Notice, the following provisions shall apply with effect from the time and date set out in such notice:

(a) the NETSO shall assume responsibility for the determination of Transmission Loss Factors to the extent set out in the Transmission Loss Factor Step In Notice;

(b) the Panel, any Panel Committee and BSCCo shall provide such assistance to the NETSO and shall take such steps as the NETSO may reasonably request to enable the NETSO to determine Transmission Loss Factors and, in the case of BSCCo, such assistance shall include:

(i) the provision at the cost of BSCCo of all necessary data, facilities, suitably qualified staff and other support;

(ii) the exercise and enforcement, at the request of the NETSO, of relevant rights under the TLFA BSC Agent Contract; and

(iii) the publication of data pursuant to Section V4.6;

(c) subject to paragraph (b), the powers, functions and duties of the Panel, any Panel Committee and BSCCo in relation to the determination of Transmission Loss Factors shall be suspended to the extent set out in the Transmission Loss Factor Step In Notice (or any subsequent amendment to that notice) and for the period that the NETSO assumes responsibility for the determination of Transmission Loss Factors;

(d) where requested by the NETSO, BSCCo shall ensure that the functions and duties of the TLFA shall be suspended to the extent set out in the Transmission Loss Factor Step In Notice (or any subsequent amendment to that notice) and for the period that the NETSO assumes responsibility for the determination of Transmission Loss Factors;

(e) the NETSO shall assume (and there are hereby conferred on the NETSO) the powers, functions and duties of the Panel, BSCCo and, to the extent suspended under paragraph (d), the TLFA as set out in this Annex T-2 for the period that the NETSO assumes responsibility for the determination of Transmission Loss Factors;

(f) the NETSO shall determine Transmission Loss Factors in accordance with the provisions mutatis mutandis of this Annex T-2 but the remaining provisions of Annex T-2 shall not be affected in any way except to the extent set out in this paragraph 10;

(g) the costs and expenses of the NETSO properly incurred in determining Transmission Loss Factors shall be paid by BSCCo to the NETSO and recovered by BSCCo from Trading Parties in accordance with the provisions of Section D; and

(h) the benefit of Section B2.9.1 shall be extended to apply to the NETSO, as if references to a Panel Member were to the NETSO, to the extent that the NETSO is carrying out the functions of the Panel pursuant to this paragraph 10.

10.5 Before ceasing to exercise its powers, functions and responsibilities under this paragraph 10, the NETSO shall deliver a notice to the Panel and BSCCo specifying the date on which the Panel, BSCCo and, where applicable, the TLFA are to resume their roles under Annex T-2 and the provisions of this paragraph 10 shall cease to have effect from that date.

AMENDMENT RECORD – SECTION T

Section T

Version 45.0

Effective Date: 27 November 2025

| Version | Details (in source column order: Modification Proposal / Decision Date / Implementation Date) |
|---|---|
| 45.0 | P483<br>21/08/2025<br>27/11/2025 |
| 44.0 | P444<br>04/04/2025<br>06/11/2025 |
| 43.0 | P485<br>09/04/2025<br>16/04/2025 |
| 42.0 | P442<br>08/02/2025<br>27/02/2025 |
| 41.0 | P473<br>17/09/2024<br>07/11/24 |
| 41.0 | P415<br>06/10/2023<br>07/11/24 |
| 40.0 | ORD009<br>13/09/2024<br>01/10/2024 |
| 39.0 | P467<br>09/05/2024<br>27/06/2024 |
| 38.0 | P451<br>22/03/24<br>02/04/24 |
| 37.0 | P464<br>09/11/23<br>29/02/24 |
| 36.0 | P395<br>06/10/22<br>02/11/23 |
| 35.0 | P450<br>12/01/23<br>23/02/23 |
| 35.0 | P376<br>06/08/21<br>23/02/23 |
| 34.0 | P448<br>23/11/22<br>07/12/22 |
| 33.0 | P447<br>21/10/22<br>24/10/22 |
| 32.0 | P388 Self Governance<br>08/08/19<br>01/04/20 |
| 32.0 | P354<br>18/06/18<br>01/04/20 |
| 31.0 | P386 Self Governance<br>13/06/19<br>07/11/19 |
| 30.0 | P367 Self Governance<br>14/06/18<br>27/07/19 |
| 29.0 | P377<br>14/03/19<br>18/04/19 |
| 28.0 | P369<br>24/09/18<br>29/03/19 |
| 27.0 | P344<br>24/08/18<br>28/02/19 |
| 26.0 | P350<br>24/03/17<br>01/04/18 |
| 25.0 | P321 Self Governance<br>08/10/15<br>29/06/17 |
| 24.0 | P323<br>15/10/15<br>05/11/15 |
| 24.0 | P327 Fast Track Self Governance<br>10/09/15<br>05/11/15 |
| 24.0 | P305<br>02/04/15<br>05/11/15 |
| 23.0 | P276<br>20/07/12<br>31/03/14 |
| 22.0 | P285<br>23/01/13<br>27/06/13 |
| 21.0 | P278<br>01/05/12<br>29/11/12 |
| 20.0 | P253<br>18/11/10<br>03/11/11 |
| 19.0 | P257<br>20/09/10<br>04/11/10 |
| 18.0 | P239<br>21/09/09<br>05/11/09 |
| 18.0 | P232<br>25/06/09<br>05/11/09 |
| 18.0 | P234<br>19/05/09<br>05/11/09 |
| 18.0 | P217<br>16/10/08<br>05/11/09 |
| 17.0 | P208<br>22/02/07<br>22/02/07 |
| 16.0 | P205<br>20/10/06<br>02/11/06 |
| 16.0 | P194<br>23/02/06<br>02/11/06 |
| 15.0 | P172<br>29/04/05<br>09/05/05 |
| 14.0 | ORD001<br>BETTA<br>01/09/04 |
| 13.0 | P164<br>08/06/04<br>30/06/04 |
| 12.0 | P151<br>05/04/04<br>19/04/04 |
| 11.0 | P126<br>18/07/03<br>08/08/03 |
| 10.0 | P104<br>11/12/02<br>11/03/03 |
| 10.0 | P78<br>09/09/02<br>11/03/03 |
| 10.0 | P71<br>22/11/02<br>11/03/03 |
| 9.0 | P101<br>02/01/03<br>23/01/03 |
| 8.0 | P61<br>28/08/02<br>10/12/02 |
| 7.0 | P2<br>16/10/01<br>30/09/02 |
| 6.0 | P72<br>22/11/02<br>12/07/02 |
| 5.0 | P12<br>10/05/02<br>02/07/02 |
| 4.0 | P46<br>14/05/02<br>22/05/02 |
| 3.0 | P18<br>22/08/01<br>25/09/01 |
| 3.0 | P8<br>24/09/01<br>25/09/01 |
| 2.0 | P10<br>14/05/01<br>11/05/01 |

*[Amendment record rebuilt from a flattened copy-paste; each row's cells are listed in source column order.]*