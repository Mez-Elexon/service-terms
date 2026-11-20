# BSC Annex X-2: Technical Glossary V62.0

> **Source file:** `319ca468-X-2.txt` (copy-paste of BSC Section X, Annex X-2)  
> **Version:** Section X-2 Version 62.0, Effective Date 29 October 2026 (from the amendment record at the end)  
> **Coverage:** Full. The contents page ("This page does not form part of the BSC") was removed.  
> **Symbol repair:** The copy-paste kept Word Symbol-font characters as private-use code points (they show as blanks in most viewers). These were mapped back: U+F053 and U+F0E5 → Σ (54), U+F0CE → ∈ (6), U+F061 → α (2), U+F0B0 → ° (2), U+F0B7 → list bullet (6), U+F05A → Z (2, in SMRCZaKJj). Example: "dRFUNCd" now reads "Σd∈R FUNCd".  
> **Re-pairing:** In paragraphs 1–4 the paragraph numbers were split from their text, and in Tables X-4, X-5 and X-9 the symbol column was split from the meaning column. Numbers, symbols and meanings were re-paired in source order; the counts match in every block.  
> **Hyphens:** Where a line wrap split a hyphenated word the hyphen was lost (e.g. "Annex S / 2", "Non / MHHS", "Bid / Offer", "Out / Turn"). These hyphens were restored. Other typos are kept as in the source.  
> **Italics:** Table X-2 says that italic words in its fourth column are explanatory only. The italics were lost in the copy. The explanatory text usually starts "The [defined term] is …" and follows the formal definition after a line break.  
> **Notation:** Acronyms are kept in the BSC's run-together form (e.g. QMij = QM with subscripts i, j). Each formula in paragraphs 1–4 is given as in the source and then rendered in a `math` block. The `math` blocks and the notation guide at the end are editorial.  
> **Converted:** 2026-11-20. Wording kept verbatim; only layout artefacts (page headers/footers, line wraps, split columns) were cleaned up. Notes in *[italic square brackets]* are editorial.

---

## ANNEX X-2: TECHNICAL GLOSSARY

## 1. GENERAL

### 1.1 Introduction

1.1.1 This Annex to Section X sets out:

(a) technical definitions and acronyms applicable in the Code other than in relation to Section S;

(b) technical definitions and acronyms applicable only in relation to Section S;

(c) conventions applicable to the Code, including timing conventions, the use of superscripts/subscripts with variables, summations and mathematical operators; and

(d) the method of interpolation of variables.

### 1.2 Use of Mathematical Operators

1.2.1 The mathematical operators and conventions employed in the formulae and other algebraic expressions contained in the Code shall be construed in accordance with the following:

(a) the symbol `*` requires multiplication to be effected;

(b) in respect of any data items, the symbol ∈ refers to belonging to or falling within. For example a∈p denotes those Energy Accounts 'a' that belong to Party ‘p’, and j∈D denotes those Settlement Periods ‘j’ falling within Settlement Day ‘D’;

```math
a \in p \qquad j \in D
```

(c) the number 0 (zero) shall be treated as a positive whole number;

(d) the convention |FUNC| refers to the absolute value of the expression ‘FUNC’, that is the positive value whether the value obtained is positive or negative;

```math
\lvert FUNC \rvert
```

(e) Where in the Code the minimum value ('min') of a set of numbers is to be selected, then for the avoidance of doubt, the value selected shall be the negative number in that set with the greatest magnitude, or in the absence of any such negative number, the positive number in that set with the lowest magnitude. Where in the Code the maximum value ('max') of a set of numbers is to be selected, then for the avoidance of doubt, the value selected shall be the positive number in that set with the greatest magnitude, or in the absence of any such positive number, the negative number in that set with the lowest magnitude.

## 2. TECHNICAL TERMS AND INTERPRETATION APPLYING EXCEPT IN RELATION TO SECTION S

### 2.1 Introduction

2.1.1 Unless the context otherwise requires the provisions of this paragraph 2 as to the use, interpretation or definition of terms, expressions, acronyms, and subscripts and summations shall apply in relation to the Code except in Section S.

### 2.2 Use of Subscripts and Other Expressions

2.2.1 The subscripts and superscripts employed in the formulae and other algebraic expressions contained in the Code shall bear the respective meanings set out in Table X-1.

### 2.3 Glossary of Terms

2.3.1 Unless the context otherwise requires, and subject as provided in Table X-2, in the Code the words, expressions and acronyms set out in Table X-2 shall bear the respective meanings therein set out.

2.3.2 Table X-3 sets out for convenience the acronyms employed in the formulae and other algebraic expressions contained in the Code in alphabetical order of acronym name.

### 2.4 Sign Convention - Active Energy and Active Power

2.4.1 Subject to paragraph 2.4.2, the sign convention adopted in the Code is that all variables representing Active Energy or Active Power are:

(a) positive in any Settlement Period for which they represent Active Energy or Active Power delivered on to the Total System or (at any Systems Connection Points(s)) the Transmission System; and

(b) negative in any Settlement Period for which they represent Active Energy or Active Power off-taken from the Total System or (at any Systems Connection Points(s)) the Transmission System.

2.4.2 Paragraph 2.4.1 shall not apply in relation to:

(a) GSP Group Take;

(b) Offer Non-Delivery Volume, Period BM Unit Non-Delivery Offer Volume and any other variable representing Active Energy or Active Power derived by calculation undertaken pursuant to Section T,

which shall, for the avoidance of doubt, be positive, negative or zero as determined in accordance with the algebraic determination of such variable pursuant to the Code.

### 2.5 Sign Convention - Cashflows

2.5.1 The sign convention adopted in the Code in relation to amounts payable in respect of Trading Charges is explained in Section T1.2.3 and T1.2.4.

### 2.6 Use of Summations

2.6.1 Variables being summated are indicated by the use of the indices placed in preceding or following superscript or subscript position on the summation sign Σ, for example:

(a) Σc FUNCc means the sum of the values of FUNCc over all values of c.

```math
\sum_{c} FUNC_{c}
```

(b) Σd FUNCd means a sum of the values of FUNCd over all values of d.

```math
\sum_{d} FUNC_{d}
```

(c) ΣcΣdFUNCcd means a sum of the values of FUNCcd over all values of d, and c.

```math
\sum_{c}\sum_{d} FUNC_{cd}
```

(d) Σd∈RFUNCd means a sum of the values of FUNCd over values of d belonging to the set R.

```math
\sum_{d \in R} FUNC_{d}
```

(e) ΣDV=D-6FUNCV means a sum of the values of FUNCv over all values of v from D - 6 to D

```math
\sum_{v=D-6}^{D} FUNC_{v}
```

*[In the source the D sits above the Σ and "v=D-6" below it; the capital V in "V=" and "FUNCV" is as printed.]*

2.6.2 In some instances, where the summation over a particular variable is restricted to a subset of the possible values of such a variable as in paragraph 2.6.1(d), instead adopting of the convention in that paragraph, an equivalent result is achieved by limiting the summation in context, for example:

"ΣdFUNCd;

Where Σd represents a sum over all values of d belonging to the set R."

This is equivalent to Σd∈RFUNCd.

2.6.3 In some instances, for convenience certain summations deviate from the above conventions and are further defined in context, for example:

"ΣdFUNCd;

Where Σd represents a sum over all values of d belonging to the set R."

Again, this is equivalent to Σd∈RFUNCd.

## 3. TECHNICAL TERMS AND INTERPRETATION APPLYING IN RELATION TO SECTION S

### 3.1 Introduction

3.1.1 Unless the context otherwise requires the provisions of this paragraph 3 as to the use, interpretation or definition of terms, expressions, acronyms, and subscripts and summations shall apply only in relation to Section S.

### 3.2 Use of Subscripts and Other Expressions

3.2.1 The subscripts and superscripts employed in the formulae and other algebraic expressions contained in the Code shall bear the respective meanings set out in Table X-4.

### 3.3 Use of Summations

3.3.1 The summations employed in the formulae and other algebraic expressions contained in the Code shall bear the respective meanings set out in Table X-5.

### 3.4 Glossary of Terms

3.4.1 Unless the context otherwise requires, in the Code the words, expressions and acronyms set out in Table X-6 shall bear the respective meanings therein set out.

3.4.2 Table X-7 sets out for convenience the acronyms employed in the formulae and other algebraic expressions contained in the Code in alphabetical order of acronym name.

### 3.5 Consumption Component Classes

3.5.1 Table X-8 sets out the valid Consumption Component Classes as at the Code Effective Date.

3.5.2 The Panel may from time to time amend the list of valid Consumption Component Classes.

### 3.6 Linear Interpolation of Variables

3.6.1 In Section S of the Code, unless the context otherwise requires, whenever linear interpolation is referred to, the procedures set out in paragraphs 3.6.2 to 3.6.4 shall be followed.

3.6.2 Where the relationship between two variables, x and y, is defined only for a set of related pairs of spot values, (x1, y1), (x2, y2) ... (xn, yn), and where a value for y, yi, is to be calculated by linear interpolation for a value of x, xi, which is not a spot value contained in the set of related pairs, but which lies within the range of x spanned by the set of related pairs, the following formula shall be applied:

yi = y0 + ((y1 - y0) * (xi - x0)/(x1 - x0))

```math
y_i = y_0 + \frac{(y_1 - y_0)\,(x_i - x_0)}{x_1 - x_0}
```

where

| Symbol | Meaning |
|---|---|
| x0 | refers to the value of x in that related pair in the set of related pairs in which x is less than xi, and where the x of the related pair is the closest x to xi; |
| x1 | refers to the value of x in that related pair in the set of related pairs in which x is greater than xi, and where the x of the related pair is the closest x to xi; |
| y0 | refers to the value of y related to x0; and |
| y1 | refers to the value of y related to x1. |

3.6.3 Where xi lies outside the range of x spanned by the set of related pairs, yi shall be set equal to the value of y in that related pair in which the value of x is closest to xi.

3.6.4 Where xi is a value of x referred to in a related pair, yi shall be set equal to the value of y contained in that related pair.

### 3.7 Sign Convention

3.7.1 With the exception of BM Unit Allocated Demand Volume, for the purposes of collecting and aggregating metered data as part of Supplier Volume Allocation pursuant to Section S, metered data, whether in respect of an Import (or aggregation of Imports) or an Export (or aggregation of Exports), will be held as the magnitude of the quantity which such metered data represents.

3.7.2 BM Unit Allocated Demand Volume shall be positive in any Settlement Period for which it represents Active Energy offtaken from the Total System and negative in any Settlement Period for which it represents Active Energy delivered to the Total System.

## 4. TIMING CONVENTIONS

### 4.1 Introduction

4.1.1 A number of variables within the Code are expressed as differing functions of time. This paragraph 4 defines the nomenclature used in such expressions.

4.1.2 Paragraphs 4.1 to 4.3 apply in relation to the Code including Section S but paragraphs 4.4 to 4.6 do not apply in relation to Section S.

### 4.2 Spot Time

4.2.1 Many input variables and calculated values are given for spot times within the Code.

4.2.2 Spot times are an instant in time, and have no duration.

### 4.3 Settlement Period Times

4.3.1 Settlement Period j starts at the spot time occurring at the beginning of the half hour and ends at the spot time occurring exactly thirty minutes later. The spot time at the beginning of one period therefore coincides with the spot time at the end of the previous period.

4.3.2 For the avoidance of doubt the first Settlement Period of a Settlement Day begins at the spot time 00:00 on the current Settlement Day (D), and ends at the spot time of 00:30 for the current Settlement Day D.

4.3.3 UTC Period j starts at the spot time occurring at the beginning of the half hour and ends at the spot time occurring exactly thirty minutes later. The spot time at the beginning of one period therefore coincides with the spot time at the end of the previous period.

4.3.4 For the avoidance of doubt the first UTC Period of a UTC Day begins at the spot time 00:00 on the current UTC Day (D), and ends at the spot time of 00:30 for the current UTC Day D.

### 4.4 Point Variables

4.4.1 Where variables are determined in relation to spot times, they are termed ‘point’ variables. The values of point variables and their associated spot times are converted (as provided in Section T3.1) from data provided by the NETSO in a different format. There is a restriction on the resolution of the pre-conversion data, such that values of point variables to which this data is converted may only be for spot times expressed in a whole number of minutes.

4.4.2 Point variables are given the subscript 't', where 't' denotes the spot time to which the point variable applies. As point variables must be submitted in a whole number of minutes, there are 31 spot times for which point data may be submitted for any Settlement Period. Up to two point variables may be submitted for a single spot time. This is to accommodate step changes in the associated variable. As the first and last spot times for any Settlement Period coincide with the adjoining Settlement Periods, only one value may be submitted for these spot times. Thus for example for the period 12:30 – 13:00, only one value of point FPN may be submitted for spot times 12:30 and 13:00 (and up to 2 values for any other spot time which is a whole number of minutes and falls within the Settlement Period).

4.4.3 Whether or not step changes are expected depends upon the variable in question. For example, as FPN Data may normally be expected to comply with dynamic parameters, step changes (especially for generation) might not normally be expected. However, a Party’s view of their operating level may change significantly from one Gate Closure to the next, and step changes may be expected at the start of a Settlement Period.

4.4.4 Where two point values are submitted for the same spot time, the Point Variable Identification Number (f) is used to determine the sequence of the two values (as explained further in paragraph 4.5.4).

4.4.5 An example of a set of Point FPN data for Settlement Period (e.g. 12:30 – 13:00) is as follows:

| Spot time, t | Point fFPNijt (MW) |
|---|---|
| 12:30 | 200 |
| 12:37 | 235 |
| 12:57 | 245 |
| 13:00 | 245 |

4.4.6 The use of the subscript j is retained to represent the fact that the spot values are being submitted for spot times that fall within a particular Settlement Period.

### 4.5 Interpolation of Values of Point Variables Between Spot Times Supplied

4.5.1 For certain spot variables it may be necessary to evaluate values applicable to any spot time within a Settlement Period from the discrete point variables supplied. These are:

| Name | Acronym | Units | Calculated from point variable: |
|---|---|---|---|
| Acceptance Volume | qAkij(t) | MW | fqAkijt |
| Accepted Bid Volume | qABknij(t) | MW | fqABknijt |
| Accepted Bid-Offer Volume | qABOknij(t) | MW | fqABOknijt |
| Accepted Offer Volume | qAOknij(t) | MW | fqAOknijt |
| Bid-Offer Volume | qBOnij(t) | MW | fqBOnijt |
| FPN | FPNij(t) | MW | fFPNijt |

4.5.2 Point variables for a particular parameter are normally used to calculate an associated function that is defined for all spot times in a Settlement Period, or in the time interval between such Point Variables. Such associated functions are expressed as a function of time F(t) and are calculated by linear interpolation from the point variables.

4.5.3 Whenever linear interpolation is referred to, the procedures set out in paragraphs 4.5.4 shall be followed.

4.5.4 Where for the purposes of the Code, a function of time F(t) is to be established by linear interpolation from a set of related pairs of spot values with point identification numbers and associated spot times t (each being a whole number of minutes) the following interpretation shall apply:

(a) For a spot time ti which is not a spot value contained in the set of related pairs, but which lies within the range of t spanned by the set of related pairs, the following formula shall be applied:

F(ti) = HFt0 + (LFt1 – HFt0)*(ti – t0)/(t1–t0)

```math
F(t_i) = {}^{H}F_{t_0} + \left({}^{L}F_{t_1} - {}^{H}F_{t_0}\right)\frac{t_i - t_0}{t_1 - t_0}
```

where

| Symbol | Meaning |
|---|---|
| t0 | refers to the value of t in that related pair in the set of related pairs in which t is less than ti, and where the t of the related pair is the closest t to ti. |
| t1 | refers to the value of t in that related pair in the set of related pairs in which t is greater than ti, and where the t of the related pair is the closest t to ti. |
| HFt0 | refers to the value of fFt related to t0 with the highest value of f; and |
| LFt1 | refers to the value of fFt related to t1 with the lowest value of f. |

*[H and L are the preceding superscripts defined in Table X-1, in the same position as f in fFt.]*

(b) For a spot time ti that is a value of t referred to in a related pair where a single value of fFt exists, the value of F(ti) shall be set to fFti contained in that related pair.

(c) For a spot time ti that is a value of t referred to in a related pair where two values of fFt exist, the value of F(ti) shall (subject to 4.6.1(a)) and 4.6.1(b)) below) remain undefined for that time ti.

### 4.6 Evaluation of Period Variables from Supplied and Interpolated Spot Variables

4.6.1 Period Variables represent the integrated MWh value over the Settlement Period j. Period variables are evaluated as follows:

The value of the Period Variable Fj for Settlement Period j, is determined by integrating the associated function of time F(t) with respect to time across the Settlement Period.

```math
F_j = \int_{j} F(t)\,dt
```

*[The source gives this rule in words only; the `math` line is an editorial rendering.]*

(a) Where the spot time ti is the first spot time of the Settlement Period, the value of F(ti) shall be set to the value of HFti for the purposes of evaluating the integral.

(b) Where the spot time ti is the last spot time of the Settlement Period, the value of F(ti) shall be set to the value of LFti for the purposes of evaluating the integral.

(c) Where for one or more spot time(s) (t1, t2 … tn) falling within the Settlement Period, the value of F(ti) remains undefined because two values of fFti exist for those spot times, and the spot times are neither the first nor last spot times in the Settlement Period, the integral will be evaluated pursuant to 4.6.2.

4.6.2 The integral shall be evaluated as the sum of:

(a) the integral for the period from the first spot time of the Settlement Period to the spot time immediately preceding the first such spot time; plus

(b) the integral from the spot time immediately succeeding the last such spot time to the last spot time of the Settlement Period; plus

(c) the integrals for each of the other periods within the Settlement Period, if any, defined by the interval between the spot time immediately succeeding any such spot time and the spot time immediately preceding the next such spot time.

---

## Table X–1 – Use of Subscripts and Superscripts Applying Except in Relation to Section S

The following subscripts and superscripts are used in the formulae and other algebraic expressions contained in the Code to refer to the following:

| Symbol | Parameter |
|---|---|
| a | Energy Account / Virtual Balancing Account |
| b | Energy Account |
| c | Demand Control Instruction |
| d | Day |
| e | A particular order number of a ranked System Action |
| f | Point Value Identification Number |
| g | A particular System Action |
| H | The higher of two Point Value Identification Numbers f, specified at the same time t for function fF(t) |
| i | BM Unit |
| j | Settlement Period |
| k | Bid-Offer Acceptance Number |
| L | The lower of two Point Value Identification Numbers f, specified at time t for function fF(t) |
| m | Calendar month (except in Section T)<br>Balancing Services Adjustment Action (in Section T) |
| n | Bid-Offer Pair Number |
| N | Node |
| p | Trading Party, Contract Trading Party, Imbalance Party or Virtual Lead Party as the case may be |
| q | The order number of a Ranked Bid Volume or Ranked Offer Volume |
| r | Trading Unit |
| s | Market Index Data Provider |
| S | BSC Season |
| t | STOR Action Number |
| u | The Non-Delivery Order Number |
| v | A particular order number of a ranked System Action |
| w | System Action, or the order number of a ranked System Action |
| x | The order number of a Ranked Priced Offer |
| y | BSC Year |
| z | Energy Contract Volume Notification or Metered Volume Reallocation Notification as the case may be. |
| Z | Zone |

## Table X–2 – Terms and Expressions Applying Except in Relation to Section S

1. Subject to paragraph 2, unless the context otherwise requires, in the Code the words, expressions and acronyms set out in this Table shall bear the respective meanings set out therein.

2. In the fourth column of this Table, words in italics are explanatory only and shall not affect the interpretation of any term in the Table or otherwise of the Code.

| Defined Term | Acronym | Units | Definition/Explanatory Text |
|---|---|---|---|
| | α | | The number 0.45 as specified in Section T2.2.1(b).<br>The factor α is that proportion of transmission losses to be deducted in total from the BM Unit Metered Volume of BM Units in delivering Trading Units, for the purposes of allocating transmission losses.<br>For the purposes of the above, transmission losses are defined as the sum of BM Unit Metered Volume over all BM Units (with BM Units that import having a negative value of BM Unit Metered Volume) |
| *[blank in source; Table X-3: Metered Volume Reallocation Fixed Data]* | QMFRziaj | MWh | An Active Energy value in accordance with Section P3.6.2(a).<br>In relation to any BM Unit i, for any Settlement Period j, QMFRziaj is a fixed volume of Active Energy to be allocated to the corresponding Energy Account a, of a Contract Trading Party other than the Lead Party from the Energy Account of the Lead Party to which the associated Metered Volume Reallocation Notification z, refers. |
| *[blank in source; Table X-3: Metered Volume Reallocation Percentage Data]* | QMPRziaj | % | A percentage value in accordance with Section P3.6.2(b).<br>In relation to any BM Unit i, for any Settlement Period j, QMPRziaj is a percentage of the BM Unit Metered Volume to be allocated to the corresponding Energy Account a of a Contract Trading Party other than the Lead Party from the Energy Account of the Lead Party to which the associated Metered Volume Reallocation Notification z, refers. |
| ABSVD BM Unit Delivered Volume | AQVMDiNLKj | MWh | Has the meaning given to it in Annex S-2 paragraph 7.1.1E for Non-MHHS Metering Systems or in Annex S-3 paragraph 5.1.1E for MHHS Metering Systems. |
| Acceptance Data | | | Data (in accordance with Section Q5.3.1) to be submitted by the NETSO pursuant to Section Q6.2.1(e). |
| Acceptance Volume | qAkij(t) | MW | The quantity determined in accordance with Section T3.4.<br>The Acceptance Volume is a quantity of absolute MW for any spot time t obtained by interpolating between Point Acceptance Volumes, qAkit, derived from the Acceptance Volume Pairs submitted as part of Acceptance Data for BM Unit i. |
| Acceptance Volume Pair | | | A pair of data items expressed in accordance with Section Q5.3.1(a) and submitted as part of the Acceptance Data pursuant to Section Q6.2.1(e).<br>The Acceptance Volume Pair is a pair of MW levels each with an associated spot time which describe the absolute MW level at which a BM Unit should operate at those spot times as a result of Acceptance k. |
| accepted Bid | | MWh | Has the meaning given to that term in Annex T-1. |
| Accepted Bid Volume | qABknij(t) | MW | The quantity established in accordance with Section T3.7.2.<br>The Accepted Bid Volume is the quantity of Bid n being the negative part of the Accepted Bid-Offer Volume accepted as a result of Bid-Offer Acceptance k from BM Unit i at spot times t within Settlement Period j. |
| Accepted Bid-Offer Volume | qABOknij(t) | MW | The quantity established in accordance with Section T3.6<br>The Accepted Bid-Offer Volume is the quantity of Bid or Offer from Bid-Offer Pair n accepted as a result of Bid-Offer Acceptance k, in Settlement Period j from BM Unit i, for any spot time t within Settlement Period j |
| accepted Offer | | MWh | Has the meaning given to that term in Annex T-1. |
| Accepted Offer Volume | qAOknij(t) | MW | The quantity established in accordance with . T3.7.1.<br>The Accepted Offer Volume is the quantity of Offer n being the positive part of the Accepted Bid-Offer Volume accepted as a result of Bid-Offer Acceptance k from BM Unit i at spot times t within Settlement Period j. |
| Account Bilateral Contract Volume | QABCaj | MWh | The quantity determined in accordance with Section P4.1.1.<br>The Account Bilateral Contract Volume is the aggregate of all Energy Contract Volumes relating to Energy Account a in Settlement Period j disregarding those that have been rejected and those contained in Energy Contract Volume Notifications that were refused and represents the energy debited from account a and credited to the other accounts (except in the case of the NETSO) for the purpose of calculating Account Energy Imbalance Volume. |
| Account Credited Energy Volume | QACEaj | MWh | The quantity determined in accordance with Section T4.6.1.<br>The Account Credited Energy Volume is the aggregate of the BM Unit Metered Volumes allocated to Energy Account a in Settlement Period j. |
| Account Energy Imbalance Cashflow | CAEIaj | £ | The amount determined in accordance with Section T4.7.1.<br>The Account Energy Imbalance Cashflow is the total cashflow resulting from the Energy Imbalance of Energy Account a in Settlement Period j such that a negative quantity represents a payment to the Trading Party holding Energy Account a and a positive quantity represents a payment by the Trading Party holding Energy Account a. |
| Account Energy Imbalance Volume | QAEIaj | MWh | The quantity determined in accordance with Section T4.6.3.<br>The Account Energy Imbalance Volume is the sum of the Account Credited Energy Volume, plus the Account Period Bid-Offer Volume less the Account Bilateral Contract Volume for Energy Account a, in Settlement Period j. |
| Account Period Balancing Services Volume | QABSaj | MWh | The quantity determined in accordance with Section T4.6.2.<br>The Account Period Balancing Services Volume is the sum of the net quantity of all accepted Bids and Offers, and the net energy associated with delivery of Applicable Balancing Services from all BM Units for which Energy Account a is the Lead Energy Account in Settlement Period j. |
| Account Period Deviation Volume | QADEij | MWh | The quantity determined in accordance with Section T4.6.2A. |
| Actual Energy Indebtedness | AEIp | MWh | The amount determined as such in accordance with Section M1.2.5.<br>The Actual Energy Indebtedness is the net energy contribution determined to be allocated to a Trading Party for Settlement Periods as defined in Section M1.2.1. |
| Arbitrage Tagged | | | Arbitrage Tagged as provided in paragraph 7 of Part 1 of Annex T-1. |
| Balancing Demand Control Volume | QBDCcj | MWh | Has the meaning given to it in Section T3.15.3(b). |
| Balancing Mechanism Window Period | | | In relation to a particular time, the Balancing Mechanism Window Period is the period from that time to the end of the Settlement Period for which Gate Closure has most recently occurred at that time.<br>The Balancing Mechanism Window Period has a duration of between one and one hour and thirty minutes. *[sic: the source has extra spaces after "one" and "minutes", where a word may have been lost]* |
| Balancing Services Adjustment Action | m | | An individual item in the Balancing Services Adjustment Data for which data is provided pursuant to Section Q6.3.2(b). |
| Balancing Services Adjustment Buy Action | m | | A Balancing Services Adjustment Action for which the Balancing Services Adjustment Volume is positive. |
| Balancing Services Adjustment Buy Volume | QBSABmj | MWh | The Balancing Services Adjustment Volume in respect of a Balancing Services Adjustment Buy Action. |
| Balancing Services Adjustment Cost | | £ | The amount sent by the NETSO as 'Balancing Services Adjustment Cost' in respect of a Balancing Services Adjustment Action in accordance with Section Q6.3. |
| Balancing Services Adjustment Price | BSAPmj | £/MWh | The amount calculated by the SAA and the BMRA as 'Balancing Services Adjustment Price' in respect of a Balancing Services Adjustment Action in accordance with Section Q6.3. |
| Balancing Services Adjustment Sell Action | m | | A Balancing Services Adjustment Action for which the Balancing Services Adjustment Volume is negative. |
| Balancing Services Adjustment Sell Volume | QBSASmj | MWh | The Balancing Services Adjustment Volume in respect of a Balancing Services Adjustment Sell Action. |
| Balancing Services Adjustment Volume | QBSAmj | MWh | The amount sent by the NETSO as 'Balancing Services Adjustment Volume' in respect of a Balancing Services Adjustment Action in accordance with Section Q6.3. |
| Bid | | | The quantity (as provided in Section Q4.1.3(a) or, where applicable, established in Section T3.4B.3) in a Bid-Offer Pair if considered as a possible decrease in Export or increase in Import of the relevant BM Unit at a given time. |
| Bid Non-Delivery Volume | QNDBnij | MWh | The quantity determined in accordance with Section T4.8.10.<br>The Bid Non-Delivery Volume is the quantity of non-delivery apportioned to Bid n from BM Unit i in Settlement Period j. |
| Bid Price | PBnij | £/MWh | The amount in £/MWh associated with a Bid and comprising part of a Bid-Offer Pair. |
| Bid-Offer Acceptance Number | k | | A number used to identify a particular Acceptance. |
| Bid-Offer Acceptance Time | Tkit | Spot time | Has the meaning given to that term in Section Q5.1.11. |
| Bid-Offer Data | | | Data (comprising the items set out in Section Q4.1.3) to be submitted by the NETSO pursuant to Section Q6.2.1(d). |
| Bid-Offer Lower Range | BOLRnij(t) | MW | The range determined in accordance with Section T3.4A.3, T3.4A.4 or T3.5.2 (as the case may be).<br>The Bid-Offer Lower Range is that data calculated for spot times t in Settlement Period j and BM Unit i, for a Bid-Offer Pair with a negative Bid-Offer Pair Number n. It is used to determine the operating range (in absolute MW) below FPN in which a particular Bid-Offer Pair applies. |
| Bid-Offer Pair | | | Data which may be submitted in relation to a BM Unit for a Settlement Period, being data that comprises the items set out in Section Q4.1.3, or (where applicable) data created pursuant to Section T3.4B.1. |
| Bid-Offer Pair Number | n | | A number used to identify a particular Bid-Offer Pair.<br>Values of n are negative for Bid-Offer Pairs that cover operating levels below FPN and positive for those that cover operating levels above FPN. |
| Bid-Offer Upper Range | BOURnij(t) | MW | The range determined in accordance with Section T3.4A.1, T3.4A.2 or T3.5.1 (as the case may be).<br>The Bid-Offer Upper Range is that data calculated for spot times t in Settlement Period j and BM Unit i, for a Bid-Offer Pair with a positive Bid-Offer Pair Number n. It is used to determine the operating range (in absolute MW) above FPN in which a particular Bid-Offer Pair applies. |
| Bid-Offer Volume | qBOnij(t) | MW | The quantity established in accordance with Section T3.3Section T3.3 *[sic]*<br>The Bid-Offer Volume is the quantity of power increase or decrease available (relative to FPN) from Bid-Offer Pair n, in Settlement Period j for BM Unit i at spot time t. Initially the Bid-Offer Volume for a Bid-Offer Pair is constant across a particular Settlement Period. |
| BM Unit Allocated Demand Disconnection Volume | BMUADDVij | MWh | The quantity submitted in accordance with paragraph 9.6.2 of Annex S-2 for Non-MHHS Metering Systems or paragraph 6.6.6 of Annex S-3 for MHHS Metering Systems. |
| BM Unit Allocated Demand Volume | BMUADVij | MWh | The quantity submitted in accordance with paragraph 9.6.2 of Annex S-2 for Non-MHHS Metering Systems or paragraph 6.6.1 of Annex S-3 for MHHS Metering Systems. |
| BM Unit Applicable Balancing Services Volume Data or BM Unit ABSVD | QASij | MWh | In respect of a BM Unit and a Settlement Period, the Applicable Balancing Services Volume Data sent by the NETSO to the SAA pursuant to Section Q6.4.1. |
| BM Unit Chargeable Demand | CBMUDij | MWh | The amount determined in accordance with Section T8.<br>The BM Unit Chargeable Demand is the amount of Demand for a BM Unit which has been adjusted to remove electricity consumed by Generation or Storage Facility under the conditions of the Generation license, which should be subject to the Final Consumption Levy. |
| BM Unit Credit Assessment Export Capability | BMCAECi | MW | The quantity determined in accordance with Section M1.6.1(a). |
| BM Unit Credit Assessment Import Capability | BMCAICi | MW | The quantity determined in accordance with Section M1.6.1(b). |
| BM Unit Identification Number | i | | A unique identifier for each BM Unit. |
| BM Unit Metered Volume | QMij | MWh | In respect of a Settlement Period:<br>(i) in relation to a BM Unit (other than an Interconnector BM Unit) comprising CVA Metering Systems, the Metered Volume (as determined in accordance with Section R);<br>(ii) in relation to an Interconnector BM Unit of an Interconnector User, the quantity determined in accordance with Section R7.4.2 (but without prejudice to Section T1.4.6);<br>(iii) in relation to an Interconnector BM Unit allocated to an Interconnector Error Administrator, the quantity determined in accordance with Section T4.1; and<br>(iv) in relation to a Supplier BM Unit, the quantity determined in accordance with Section T4.2.1 and<br>(v) in relation to a Secondary BM Unit, the quantity determined in accordance with Section T4.2A.1. |
| BM Unit MSID Pair Data | | | Has the meaning given to that term in Section S paragraph 10.1.3. |
| BM Unit Period Non-Delivery Charge | CNDij | £ | The amount determined in accordance with Section T4.8.13.<br>The BM Unit Period Non-Delivery Charge is the total non-delivery charge associated with the non-deliver of Bids or Offers for BM Unit i in Settlement Period j. |
| Buy Price Price Adjustment | BPAj | £/MWh | The amount sent by the NETSO as the ‘Buy Price Price Adjustment’ in accordance with Section Q6.3. |
| CADL Flagged | | | CADL Flagged as provided in paragraph 3 of Part 1 of Annex T-1. |
| Classified Ranked Set | | | One of the Classified Ranked Sets as provided in paragraph 8 of Part 1 of Annex T-1. |
| Continuous Acceptance Duration | CADki | Minutes | Has the meaning given to that term in paragraph 12.3 of Annex T-1. |
| Continuous Acceptance Duration Limit | CADL | Minutes | The value established and from time to time revised and approved in accordance with Section T1.9. |
| Corrected Component | CORCiNj | MWh | The quantity submitted in accordance with paragraph 9.3.3 of Annex S-2 for Non-MHHS Metering Systems or paragraph 6.3.3 of Annex S-3 for MHHS Metering Systems. |
| Corrected MSID ABSVD Component | CORABSVDCi2Nj | | Has the meaning given to it in Annex S-2 paragraph 9.3.5 for Non-MHHS Metering Systems or Annex S-3 paragraph 6.3.5 for MHHS Metering Systems. |
| Credit Assessment Credited Energy Volume | CAQCEiaj | MWh | The amount determined in accordance with Section M1.2.3.<br>The Credit Assessment Credited Energy Volume is the contribution to a Trading Party’s Credit Assessment Energy Indebtedness from BM Unit i and Energy Account a in Settlement Period j. |
| Credit Assessment Energy Indebtedness | CEIpj | MWh | The amount determined as such in accordance with Section M1.2.2.<br>The Credit Assessment Energy Indebtedness is the net energy contribution determined to be allocated to a Trading Party for Settlement Periods as defined in Section M1.2.1. |
| Credit Cover | CCp | £ | Is defined in Annex X-1 |
| Credit Cover Error Compensation | CCECp | £ | Has the meaning given to that term in Section M4.1.1.<br>The Credit Cover Error Compensation is the aggregate payment that may be made to a Trading Party in relation to a Credit Cover Error. |
| Credit Cover Error Erroneous Rejection Flag | FLAGpj | | Has the value determined in accordance with Section M4.2.3.<br>The Credit Cover Error Erroneous Rejection Flag is a flag indicating whether Settlement Period j was determined erroneously to fall within a Credit Default Rejection Period for Trading Party p. |
| Credit Cover Error Imbalance Amount | ECBpj | £ | The amount determined as such in accordance with Section M4.2.3.<br>The Credit Cover Error Imbalance Amount represents the Energy Imbalance related compensation that may be paid to a Trading Party in relation to Settlement Period j, as a consequence of a Credit Cover Error. |
| Credit Cover Error Interest Amount | ECApj | £ | The amount determined as such in accordance with Section M4.2.2.<br>The Credit Cover Error Interest Amount represents the interest related compensation that may be paid to a Trading Party in relation to Settlement Period j, as a consequence of a Credit Cover Error. |
| Credit Cover Error Rejection Volume | REJaj | MWh | The quantity determined in accordance with Section M4.2.3.<br>The Credit Cover Error Rejection Volume represents an assessment of the change (whether positive or negative) in the quantity of energy that would have been allocated to Energy Account a, of Trading Party P, in Settlement Period j, had Energy Contract Volume Notifications and Data relating to Metered Volume Reallocation Notifications not been rejected in accordance with Sections P2.5.2, and P3.5.2, by virtue of Trading Party P being in Level 2 Credit Default. |
| Credit Cover Percentage | CCPpj | % | Has the meaning given to that term in Section M3.1.1. |
| Credited Energy Volume | QCEiaj | MWh | The quantity determined in accordance with Section T4.5.1. |
| Daily Direct Compensation Cashflow | SDCp | £ | The amount determined in accordance with Section T4.11.10. |
| Daily Party BM Unit Cashflow | CBMp | £ | The amount determined in accordance with Section T3.12.2. |
| Daily Party Energy Imbalance Cashflow | CAEIp | £ | The amount determined in accordance with Section T4.7.3. |
| Daily Party Information Imbalance Charge | CIIp | £ | The amount determined in accordance with Section T4.3.8. |
| Daily Party Non-Delivery Charge | CNDp | £ | The amount determined in accordance with Section T4.8.15 |
| Daily Party Residual Settlement Cashflow | RCRCp | £ | The amount determined in accordance with Section T4.10.4. |
| Daily Supplier Compensation Cashflow | SCCp | £ | The amount determined in accordance with Section T4.11.8. |
| Daily System Operator Cashflow | CSO | £ | The amount determined in accordance with Section T4.9.2. |
| Daily Virtual Lead Party Compensation Cashflow | SCVp | £ | The amount determined in accordance with Section T4.11.6 |
| DC Limits | | MW and/or % | Is defined in Annex X-1. |
| De Minimis Acceptance Threshold | DMAT | MWh | The value established and from time to time revised and approved in accordance with Section T1.8. |
| De Minimis Tagged | | | De Minimis Tagged as provided in paragraph 6 of Part 1 of Annex T-1. |
| Default Funding Share | FSDpm | | Has the meaning given to that term in Section D1.3.1(b). |
| Delivering Transmission Losses Adjustment. | TLMO+j | | The factor determined as such in accordance with Section T2.3.1.<br>The factor used in the determination of the Transmission Loss Multiplier for BM Units in Delivering Trading Units in Settlement Period j |
| De-Rated Margin Forecast | | MWh | The forecast submitted in accordance with Section Q6.1.25. |
| Deviation Volume | QDEij | MWh | The quantity determined in accordance with Section T4.3AA. |
| Emergency Acceptance | | | An Acceptance which falls within Section Q5.1.3(b). |
| Emergency Flagged Ranked Set | | | One of the Emergency Flagged Ranked Sets as provided in paragraph 5 of Part 1 of Annex T-1. |
| End Point Demand Control Level | | MW | Has the meaning given to that term in Section T3.15(b). |
| Energy Contract Volume | ECQzabj | MWh | An Active Energy value in accordance with Section P2.6.1. |
| Energy Credit Cover | ECCp | MWh | Has the meaning given to that term in Section M2.4.1. |
| Energy Indebtedness | EIpj | MWh | Has the meaning given to that term in Section M1.2.1. |
| Erroneous Energy Indebtedness | EEIpj | MWh | The amount determined as such in accordance with Section M4.2.2.<br>The Erroneous Energy Indebtedness represents an assessment of that amount of Energy Credit Cover that a Trading Party would have had to establish in Settlement Period j, in order to avoid being in level 1 credit default based on the erroneous calculation of Energy Indebtedness. |
| Final Demand | FDij | MWh | The quantity determined in accordance with Section T4.11.1. |
| Final Loss of Load Probability | LoLPj | | In relation to a Settlement Period, the final probability to be provided by the NETSO in accordance with the Loss of Load Probability Calculation Statement and Section Q6.7.2 or Q6.8.4, as applicable. |
| Final Ranked Set | | | The Final Ranked Set as provided in paragraph 11.3 of Part 1 of Annex T-1. |
| First-Stage Flagged | | | First-Stage Flagged in accordance with paragraph 3, 4 or 5 of Part 1 of Annex T-1. |
| Flagged (and Unflagged) | | | Have the meanings given to those terms in paragraph 1.4 of Annex T-1. |
| Forecast Total Power Park Module Generation | | MW | The forecast of total generation across all Power Park Modules metered by the NETSO in accordance with CC6.5.6 of the Grid Code. |
| FPN | FPNij(t) | MW | The quantity established in accordance with Section T3.2.1.<br>The final physical notification for BM Unit is the level of import or export (as the case may be) that the Party expects to import or export from BM Unit i, in Settlement Period j, in the absence of any Balancing Mechanism Acceptances from the NETSO.<br>The value of FPNij(t) is calculated for spot times t in Settlement Period by linear interpolation from the discrete values of Point FPN submitted. |
| Network Gas Supply Imbalance Adjustment Volume | QNGSIAij | MWh | Has the meaning given to that term in Section T3.9.2A. |
| Network Gas Supply Total Bid Payment | TNGSBi | £ | Has the meaning given to that term in Section T3.12A.1. |
| GC Limits | | MW and/or % | Is defined in Annex X-1. |
| General Funding Share | FSGpm | | Has the meaning given to that term in Section D1.2.1(d).<br>In relation to month m, a Trading Party’s General Funding Share reflects its proportionate share of the aggregate of certain BSCCo Charges for that month. |
| Generating Plant Demand Margin | OCNMFD or OCNMFW | MW | Has the meaning given to that term in OC2 of the Grid Code. |
| Generic Line Loss Factor | | | A Line Loss Factor established for a class of Metering System as provided for in Section K1.7.2. |
| Gross Contract MWh | | MWh | The value established in accordance with Annex D-3 paragraph 3.2.<br>The Gross Contract MWh is the gross aggregate of all Energy Contract Volumes and Metered Volume Fixed Reallocations relating to a Trading Party over a given month. |
| GSP Group Metered Volume | | MWh | In relation to any GSP Group and any Settlement Period, a Metered Volume representing the algebraic sum of:<br>(i) the quantity of Active Energy flowing into a GSP Group at Grid Supply Points connected to that GSP Group and at Distribution Systems Connections Points connected to that GSP Group, and<br>(ii) the quantity of Active Energy flowing out of a GSP Group at Grid Supply Points connected to that GSP Group and at Distribution Systems Connections Points connected to that GSP Group<br>but disregarding Exports and Imports at Boundary Points in that GSP Group. |
| GSP Group Take | | MWh | In relation to any GSP Group and any Settlement Period, shall be determined as follows:<br>GSPGT = GMV + I – E<br>where:<br>GSPGT means the GSP Group Take for that GSP Group and that Settlement Period;<br>GMV means the GSP Group Metered Volume for that GSP Group and that Settlement Period;<br>I means the magnitude of the quantities of Imports at CVA Boundary Points in that GSP Group (as at the Transmission Boundary) for that Settlement Period; and<br>E means the magnitude of the quantities of Exports at CVA Boundary Points in that GSP Group (as at the Transmission Boundary) for that Settlement Period. |
| High Reference Temperature | | Degrees celsius | The daily average temperature for Great Britain which was exceeded on twelve (12) percent (%) of days during a thirty year historic period. |
| High Reference Transmission Energy | | MWh | The daily aggregate Transmission Energy which was exceeded on twelve (12) percent (%) of days during a thirty year historic period. |
| Indicated Constraint Boundary Margin | MELNGC | MW | The import and export constraint limits for a BMRS Zone.<br>The import constraint limit being calculated as the boundary transfer limit minus the Demand Forecast plus the sum of Maximum Export Limits for exporting BM Units and the export constraint limit being calculated as the boundary transfer limit plus the Demand Forecast minus the sum of Maximum Export Limits for exporting BM Units |
| Indicated Demand | INDDEM | MW | The half-hour average MW expected demand in each Settlement Period calculated as the sum of all Physical Notifications for that Settlement Period prevailing at the time of the forecast and for BM Units for which the Physical Notifications are negative, i.e. will be importing energy. |
| Indicated Generation | INDGEN | MW | The half-hour average MW expected generation in each Settlement Period calculated as the sum of all Physical Notifications for that Settlement Period prevailing at the time of the forecast and for BM Units for which the Physical Notifications are positive, i.e. will be exporting energy. |
| Indicated Imbalance | IMBALNGC | MW | Has the meaning given to that term in the Grid Code.<br>Calculated as the difference between the sum of all Physical Notifications for exporting BM Units (i.e. the Indicated Generation) and the Transmission System Demand forecast |
| Indicated Margin | | MW | Has the meaning given to that term in the Grid Code.<br>Calculated as the difference between the sum of all Maximum Export Limits for exporting BM Units and the Transmission System Demand forecast |
| Indicative Loss of Load Probability | | | In relation to a Settlement Period, the indicative probability to be provided by the NETSO in accordance with the Loss of Load Probability Calculation Statement and Sections Q6.8.2 and Q6.8.3. |
| Indicative Net Imbalance Volume | INIVj | MWh | The Indicative Net Imbalance Volume calculated in accordance with Section V2.6.5. |
| Indicative Period Balancing Mechanism Bid Cashflow | ICBnij | £ | The amount determined in accordance with Section V2.6.6. |
| Indicative Period Balancing Mechanism Offer Cashflow | ICOnij | £ | The amount determined in accordance with Section V2.6.6. |
| Indicative Period BM Unit Total Accepted Bid Volume | IQABnij | MWh | The quantity determined in accordance with Section V2.6.4 |
| Indicative Period BM Unit Total Accepted Offer Volume. | IQAOnij | MWh | The quantity determined in accordance with Section V2.6.4 |
| Indicative System Buy Price | ISBPj | £/MWh | The Indicative System Buy Price calculated in accordance with Section V2.6.5. |
| Indicative System Sell Price | ISSPj | £/MWh | The Indicative System Sell Price calculated in accordance with Section V2.6.5. |
| Information Imbalance Charge | CIIij | £ | The amount determined in accordance with Section T4.3.6.<br>The Information Imbalance Charge is the charge applicable to the associated Lead Party as a result of the difference in FPN data as modified by Acceptances and BM Unit Metered Volume from BM Unit i in Settlement Period j. |
| Information Imbalance Price | IIPj | £/MWh | The price specified in Section T4.3.5, being an amount equal to zero. |
| Initial Energy Credit Cover | IECCp | MWh | The amount determined as such in accordance with Section M4.2.2.<br>The Initial Energy Credit Cover is the amount of Credit Cover that a Trading Party p has in place at the start of a Credit Cover Error Period. |
| Initial National Demand Out-Turn | INDO | MW | The demand metered by the NETSO taking into account transmission losses but not including station transformer load, pumped storage demand or Interconnector demand. References to INDO in Section Q6.1.13 and in Table 1 of Section V Annex V-1 mean the half-hour average INDO for a Settlement Period. References to INDO in Section G3.1.4 mean the spot time INDO measured by the NETSO in accordance with that paragraph. |
| Initial Ranked Set | | | One of the Initial Ranked Sets of System Actions as provided in paragraph 2.1(c) of Part 1 of Annex T-1. |
| Initial Transmission System Demand Out-Turn | ITSDO | MW | The half-hour average MW demand metered by the NETSO taking into account transmission losses and including station transformers load, pumped storage demand and Interconnector demand. |
| Interconnector Metered Volume | IMVj | MWh | Is defined in Annex X-1.<br>The net aggregate volume of Active Energy, determined as at the Transmission System Boundary, which flowed from or to the relevant Interconnector in Settlement Period j. |
| Line Loss Factor | | | Means a multiplier which, when applied to data from a CVA Metering System connected to a Boundary Point on a Distribution System, converts such data into an equivalent value at the Transmission System Boundary. |
| Line Loss Factor Class | LLFC | | A set of SVA Metering Systems defined by a Licensed Distribution System Operator relating to any one or more of its Distribution System(s) that are assigned the same Line Loss Factor for the relevant Settlement Period. |
| Loss of Load Probability | | | In relation to a Settlement Period, the Final Loss of Load Probability or the Indicative Loss of Load Probability as the context so requires. |
| Low Reference Temperature | | Degrees celsius | The daily average temperature for Great Britain which was exceeded on eighty eight (88) percent (%) of days during a thirty year historic period. |
| Low Reference Transmission Energy | | MWh | The daily aggregate Transmission Energy which was exceeded on eighty eight (88) percent (%) of days during a thirty year historic period. |
| Main Funding Share | FSMpm | | Has the meaning given to that term in Section D1.2.1(a).<br>The Main Funding Share represents a Trading Party’s proportionate share of the aggregate Credited Energy Volumes for month m. |
| Market Index Price | PXPsj | £/MWh | In relation to a Market Index Data Provider and a Settlement Period, the price data to be provided by that Market Index Data Provider in accordance with the Market Index Definition Statement or (where applicable) deemed in accordance with Section T4.3A.1. |
| Market Index Volume | QXPsj | MWh | In relation to a Market Index Data Provider and a Settlement Period, the volume data to be provided by that Market Index Data Provider in accordance with the Market Index Definition Statement or (where applicable) deemed in accordance with Section T4.3A.1. |
| Market Price | MPj | £/MWh | Has the meaning given to that term in Section T4.3A.2. |
| Maximum Delivery Period | | | Has the meaning given to that term in BC1 of the Grid Code. |
| Maximum Delivery Volume | | | Has the meaning given to that term in BC1 of the Grid Code. |
| Maximum Export Limit | | | Has the meaning given to that term in BC1 of the Grid Code. |
| Maximum Import Limit | | | Has the meaning given to that term in BC1 of the Grid Code. |
| Metered Credit Assessment Credited Energy Volume | MAQCEiaj | MWh | is defined in Section M1.2.4A.<br>The Metered Credit Assessment Credited Energy Volume is the contribution to a Trading Party’s Metered Energy Indebtedness from BM Unit i and Energy Account a in Settlement Period j. |
| Metered Energy Indebtedness | MEIpj | MWh | is defined in Section M1.2.4A.<br>The Metered Energy Indebtedness is the net energy contribution determined to be allocated to a Trading Party for Settlement Periods as defined in Section M1.2.4A. |
| Metered Volume Fixed Reallocation | QMFRiaj | MWh | A MWh value determined in accordance with Section P4.3.1.<br>In relation to any BM Unit i, for any Settlement Period j, Metered Volume Fixed Reallocation means, for Energy Account a of a Contract trading Party, the aggregate of all Metered Volume Reallocation Notification Fixed Data for Metered Volume Reallocation Notifications relating to such Energy Account. |
| Metered Volume Percentage Reallocation | QMPRiaj | % | A percentage value determined in accordance with Section P4.3.1.<br>In relation to any BM Unit i, for any Settlement Period j, Metered Volume Percentage Reallocation means, for Energy Account a of Contract Trading Party, the aggregate of all Metered Volume Reallocation Notification Percentage Data for Metered Volume Reallocation Notifications relating to such Party. |
| Minimum Non-Zero Time | | | Has the meaning given to that term in BC1 of the Grid Code. |
| Minimum Zero Time | | | Has the meaning given to that term in BC1 of the Grid Code. |
| Monthly Consumption Charging Net SVA Costs | MCNSCm | £ | Has the meaning given to that term in Section D4.1(d). |
| Monthly Default Costs | MDCm | £ | Has the meaning given to that term in Section D4.1(e). |
| Monthly Net Main Costs | MNMCm | £ | Has the meaning given to that term in Section D4.1(d). |
| Monthly payment | Ppm | £ | Has the meaning given to that term in Annex D 4 1.1. |
| Monthly Production Charging SVA Costs | MPSCm | £ | Has the meaning given to that term in Section D4.1(d). |
| MSID Pair Data | | | The data comprising the data items pursuant to Section S10.1 and may be:<br>(i) BM Unit MSID Pair Data; or<br>(ii) Non BM Unit ABSVD MSID Pair Data |
| MSID Pair Delivered Volume | MPDV | MWh | The amount determined in accordance with Section Q6.4.10 or S11.1.1.<br>.MSID Pair Delivered Volume is such volumes of Active Energy notified to the SVAA by the NETSO for the purposes of calculating Non BM Unit ABSVD (SNBABSVDij); or by the Virtual Lead Party for the purposes of aggregating Secondary BM Unit Supplier Delivered Volume (VBMUSDViZj). |
| National Demand | | | Has the meaning given to the term National Demand as defined in the Grid Code. |
| Net Imbalance Volume | NIVj | MWh | Has the meaning given to that term in paragraph 14.1 of Annex T-1. |
| NIV Tagged | | | NIV Tagged as provided in paragraph 9 of Part 1 of Annex T-1. |
| Non BM Unit Applicable Balancing Services Volume Data or Non BM Unit ABSVD | | | The following data:<br>(i) Non BM Unit ABSVD MSID Pair Data ;<br>(ii) the associated MSID Pair Delivered Volume. |
| Non BM Unit ABSVD MSID Pair Data | | | Has the meaning given to that term in Section Q 6.4.8. |
| Non-BM STOR Instructed Volume | | MWh | The volume of Short Term Operating Reserve instructed by the NETSO outside of the balancing mechanism in order to increase generation or reduce demand. |
| Non-BM STOR Instruction | | | A Short Term Operating Reserve instruction given by the NETSO outside of the balancing mechanism in order to increase generation or reduce demand. |
| Non-Delivered Bid Charge | CNDBnij | £ | The amount determined in accordance with Section T4.8.12.<br>The Non-Delivered Bid Charge is a charge in Settlement Period j, that may relate to an accepted Bid n, that is determined not to have been delivered (either wholly or in part) from BM Unit i. |
| Non-Delivered Bid Price | NDPBnij | £/MWh | The amount determined in accordance Section T4.8.19.<br>The amount in £/MWh associated with an Accepted Bid that is allocated to Period BM Non-Delivered Bid Volume. |
| Non-Delivered Offer Charge | CNDOnij | £ | The amount determined in accordance with Section T4.8.11.<br>The Non-Delivered Offer Charge is a charge in Settlement Period j, that may relate to an accepted Offer n, that is determined not to have been delivered (either wholly or in part) from BM Unit i. |
| Non-Delivered Offer Price | NDPOnij | £/MWh | The amount determined in accordance Section T4.8.16.<br>The amount in £/MWh associated with an Accepted Offer that is allocated to Period BM Non-Delivered Offer Volume. |
| Non-Delivery Order Number | u | | The number allocated to an Offer or Bid in accordance with Section T4.8.4 or T4.8.8.<br>The Non-Delivery Order Number (u) is an index used to rank non-delivered Offers or Bids from a BM Unit in a particular Settlement Period in order to determine the order of allocation the Period BM Unit Non-Delivered Offer Volume, or the Period BM Unit Non-Delivered Bid Volume. |
| Non-Working Day Credit Assessment Load Factor | NWDCALFi | | Is defined in Annex X-1.<br>The factor is used to establish the BM Unit Credit Assessment Export Capability and BM Unit Credit Assessment Import Capability for BM Unit i on a CALF Non-Working Day determined for the purposes of Credit Assessment Load Factor. |
| Normal Reference Temperature | | Degrees celsius | The daily average temperature for Great Britain which was exceeded on fifty (50) percent (%) of days during a thirty year historic period. |
| Normal Reference Transmission Energy | | MWh | The daily aggregate Transmission Energy which was exceeded on fifty (50) percent (%) of days during a thirty year historic period. |
| Notice to Deliver Bids | | | Has the meaning given to that term in BC1 of the Grid Code. |
| Notice to Deliver Offers | | | Has the meaning given to that term in BC1 of the Grid Code. |
| Notice to Deviate from Zero | | | Has the meaning given to that term in BC1 of the Grid Code. |
| Offer | | | The quantity (as provided in Section Q4.1.3(a) or, where applicable, established in Section T3.4B.3) in a Bid-Offer Pair if considered as a possible increase in Export or decrease in Import of the relevant BM Unit at a given time. |
| Offer Non-Delivery Volume | QNDOnij | MWh | The quantity determined in accordance with Section T4.8.6.<br>The Offer Non-Delivery Volume is the quantity of non-delivery apportioned to Offer n from BM Unit i in Settlement Period j. |
| Offer Price | POnij | £/MWh | The amount in £/MWh associated with an Offer and comprising part of a Bid-Offer Pair. |
| Offtaking Transmission Losses Adjustment | TLMO-j | | The factor determined as such in accordance with Section T2.3.1.<br>The factor used in the determination of the Transmission Loss Multiplier for BM Units in Offtaking in Trading Units in Settlement Period j |
| Output Usable | | MW | Has the meaning given to that term in the Grid Code. |
| Out-Turn Temperature | | Degrees celsius | A single value deemed to be representative of the temperature for Great Britain as measured at midday. |
| PAR Tagged | | | PAR Tagged as provided in paragraph 11 of Part 1 of Annex T-1. |
| Party-Aggregated Secondary BM Unit Delivered Volume | VLPSDVi2j | MWh | For AMSID Pairs registered in LPAMR, the AMSID Pair Delivered Volumes aggregated by Secondary BM Unit. |
| Party-Aggregated Secondary BM Unit Demand Volume | VLPDVi2j | MWh | For AMSID Pairs registered in LPAMR, the AMSID Pair Demand Volumes adjusted for losses and aggregated by Secondary BM Unit. |
| Party Daily Reallocation Proportion | | | Has the meaning given to that term in Section G1.3. |
| Party Submitted Expected Volumes | PSEV | MWh | The volume submitted by the Party which represents the Party’s forecast of expected volumes per Settlement Period for all MSID Pairs not selected for Baselining within a BMU providing Balancing Services |
| Period Accepted Bid Volume | QABknij | MWh | The quantity established in accordance with Section T3.8.2.<br>The Period Accepted Bid Volume is the volume of Bid n, accepted in respect of BM Unit i, in Settlement Period j, as a result of Acceptance k. |
| Period Accepted Offer Volume | QAOknij | MWh | The quantity established in accordance with Section T3.8.1.<br>The Period Accepted Offer Volume is the volume of Offer n, accepted in respect of BM Unit i, in Settlement Period j as a result of Acceptance k. |
| Period BM Unit Balancing Services Volume | QBSij | MWh | The quantity determined in accordance with Section T4.3.2.<br>The Period BM Unit Balancing Services Volume is the sum of the net quantity of accepted Bids and Offers and the net quantity of energy associated with delivery of Applicable Balancing Services from BM Unit i in Settlement Period j. |
| Period BM Unit Bid Cashflow | CBnij | £ | The amount determined in accordance with Section T3.10.2.<br>The Period BM Unit Bid Cashflow is the total cashflow resulting from accepted volumes of Bid n from BM Unit i in Settlement Period j. |
| Period BM Unit Cashflow | CBMij | £ | The amount determined in accordance with Section T3.11.1.<br>The Period BM Unit Cashflow is the total cashflow resulting from all accepted Bids and Offers from BM Unit i in Settlement Period j. |
| Period BM Unit Non Chargeable Demand | NCBMUDij | MWh | The amount determined in accordance with Annex S-2 3.11 for Non-MHHS Metering Systems or S-3 3.13 for MHHS Metering Systems which is used in Section T8.<br>The Period BM Unit Non Chargeable Demand is the amount of Demand for a BM Unit which has been consumed by Generation or Storage Facility under the conditions of the Generation license which should not be subject to the Final Consumption Levy. |
| Period BM Unit Demand Disconnection Volume | QDDij | MWh | The quantity established in accordance with Section R8.2.1.<br>The Period BM Unit Demand Disconnection Volume is the volume of energy for BM Unit i in Settlement Period j that was subject to Demand Disconnection. |
| Period BM Unit Non-Delivered Bid Volume | QNDBij | MWh | The quantity determined in accordance with Section T4.8.2.<br>The Period BM Unit Non-Delivered Bid Volume is the quantity of non-delivered Bids from BM Unit i in Settlement Period j. |
| Period BM Unit Non-Delivered Offer Volume | QNDOij | MWh | The quantity determined in accordance with Section T4.8.1.<br>The Period BM Unit Non-Delivered Offer Volume is the quantity of non-delivered Offers from BM Unit i in Settlement Period j. |
| Period BM Unit Offer Cashflow | COnij | £ | The amount determined in accordance with Section T3.10.1.<br>The Period BM Unit Offer Cashflow is the total cashflow resulting from accepted volumes of Offer n from BM Unit i in Settlement Period j. |
| Period BM Unit Total Accepted Bid Volume | QABnij | MWh | The quantity established in accordance with Section T3.9.2.<br>The Period BM Unit Total Accepted Bid Volume is the quantity of Bid n, accepted in respect of BM Unit i, in Settlement Period j, as a result of all Acceptances. |
| Period BM Unit Total Accepted Offer Volume | QAOnij | MWh | The quantity established in accordance with Section T3.9.1.<br>The Period BM Unit Total Accepted Offer Volume is the quantity of Offer n, accepted in respect of BM Unit i, in Settlement Period j, as a result of all Acceptances. |
| Period Direct Compensation Cashflow | SPDCji2 | £ | The amount determined in accordance with Section T4.11.9. |
| Period Expected Metered Volume | QMEij | MWh | The quantity determined in accordance with Section T4.3.3.<br>The Period Expected Metered Volume is the quantity of energy that a particular BM Unit i, is expected to export or import in Settlement Period j, after taking account of any accepted offers or bids. |
| Period FPN | FPNij | MWh | The quantity determined in accordance with T4.3.1.<br>The Period FPN is the integrated MWh of energy implied by integrating the Final Physical Notification for BM Unit i over Settlement Period j. |
| Period Information Imbalance Volume | QIIij | MWh | The quantity determined in accordance with Section T4.3.4.<br>The Period Information Imbalance Volume is the difference between the BM Unit Metered Volume and the Period Expected Metered Volume for BM Unit i in Settlement Period j. |
| Period Secondary BM Unit Delivered Proportion | SPiji2 | MWh | This quantity is determined in accordance with Section T4.3B.3. |
| Period Secondary BM Unit Delivered Volume | QSDij<br>or<br>QSDi2j | MWh | This quantity is determined in accordance with Section T4.3B.2.<br>This quantity is represented by the acronym QSDi2j in paragraph T4.3B.4 for the sole reason that the formula in this paragraph refers to both Primary BM Units and Secondary BM Units. |
| Period Secondary BM Unit Direct Compensation | QDViji2 | MWh | The quantity determined in accordance with Section T4.3C.3. |
| Period Secondary BM Unit Direct Compensation Volume | QDVji2 | MWh | The quantity determined in accordance with Section T4.3C.6. |
| Period Secondary BM Unit Non-Delivered Volume | QSNDij | MWh | This quantity is determined in accordance with Section T4.3B.1. |
| Period Secondary BM Unit Supplier Compensation | QCViji2 | MWh | The quantity determined in accordance with Section T4.3C.2. |
| Period BM Unit Supplier Compensation Volume | QSVij | MWh | The quantity determined in accordance with Section T4.3C.4. |
| Period Secondary BM Unit Compensation Volume | QCVji2 | MWh | The quantity determined in accordance with Section T4.3C.5. |
| Period Secondary BM Unit Supplier Delivered Volume | QSDiji2 | MWh | This quantity is determined in accordance with Section T4.3B.4. |
| Period Supplier BM Unit Delivered Volume | QBSDij | MWh | This quantity is determined in accordance with Section T4.3B.5. |
| Period Supplier Compensation Cashflow | SPCCij | £ | The amount determined in accordance with Section T4.11.7. |
| Point Acceptance Volume | qAkit | MW | A MW level and associated time created in accordance with Section T3.1.2(c)<br>A Point Acceptance Volume submitted as part of Acceptance Volume Pair, is a level in absolute MW for spot time t and BM Unit i, used to imply the acceptance of one or more Offers and/or Bids. |
| Point Bid-Offer Volume | fqBOnijt | MW | A MW level and associated time in accordance with Section T3.1.2(b).<br>The Point Bid-Offer Volume is one of two MW quantities each with the same or different associated spot time t, determined for each Bid-Offer Pair n, for BM Unit i in Settlement Period j. |
| Point FPN | fFPNijt | MW | A MW quantity and associated time in accordance with Section T3.1.2(a).<br>Point FPN data is a series of one or more MW spot values submitted for spot times t in Settlement Period j for BM Unit i. It is used to determine the values of Final Physical Notification. |
| Point Value Identification Number | f | | A number used to differentiate two values of a point variable determined for the same spot time and established for Point FPN values in Section T3.1.2(a) and for Point Bid-Offer Volumes in Section T3.1.2(b). |
| Price Average Reference Volume | PAR | MWh | The volume determined in accordance with Section T1.10.1 |
| Ranked Set | | | Has the meaning given to that term in paragraph 1.2 of Annex T-1. |
| Registered Capacity | | MW | Has the meaning given to that term in the Grid Code. |
| Remaining Period BM Unit Non-Delivered Bid Volume | RQNDBuij | MWh | The quantity determined as such in accordance with Section T4.8.10<br>The Remaining Period BM Unit Non-Delivered Bid Volume is the amount of Non-Delivered Bid Volume remaining to be allocated to Bid u from BM Unit i in Settlement Period j. |
| Remaining Period BM Unit Non-Delivered Offer Volume | RQNDOuij | MWh | The quantity determined as such in accordance with Section T4.8.6.<br>The Remaining Period BM Unit Non-Delivered Offer Volume is the amount of Non-Delivered Offer Volume remaining to be allocated to Offer u from BM Unit i in Settlement Period j. |
| Replacement Buy Price | RBPj | £/MWh | The Replacement Buy Price determined in accordance with paragraph 15 of Part 2 of Annex T-1. |
| Replacement Price | RPj | £/MWh | Means either the Replacement Buy Price or the Replacement Sell Price as determined in accordance with paragraph 15 of Part 2 of Annex T-1, and Replacement Pricing shall have the same meaning. |
| Replacement Price Average Reference Volume | RPAR | | Has the meaning given to that term in Section T1.11.1. |
| Replacement Sell Price | RSPj | £/MWh | The Replacement Sell Price determined in accordance with paragraph 15 of Part 2 of Annex T-1. |
| Replacement-Priced Ranked Set | | | The Replacement-priced Ranked Set as provided in paragraph 10.4 of Part 1 of Annex T-1. |
| Reserve Scarcity Price | RSVPj | £/MWh | In respect of a Settlement Period, the price determined in accordance with Section T3.13. |
| Residual Cashflow Reallocation Cashflow | RCRCaj | £ | The cashflow determined in accordance with Section T4.10.3.<br>The Residual Cashflow Reallocation Cashflow is the cashflow to Energy Account a in Settlement Period j resulting from the reallocation the Total System Residual Cashflow. |
| Residual Cashflow Reallocation Proportion | RCRPaj | | The proportion determined in accordance with Section T4.10.2.<br>The Residual Cashflow Reallocation Proportion is a fraction expressing the proportion of the Total System Residual Cashflow to be allocated to Energy Account a in Settlement Period j. |
| Run-Down Rate(s) | | | Has the meaning given to that term in BC1 of the Grid Code. |
| Run-Up Rate(s) | | | Has the meaning given to that term in BC1 of the Grid Code. |
| Secondary BM Unit AMSID Pair Data | | | Has the meaning given to that term in Section S paragraph 10.1A |
| Secondary BM Unit Delivered Volume | QVBMDi2NKji | MWh | The quantity determined in accordance with 7.1.1D Annex S-2 for Non-MHHS Metering Systems or 5.1.1D Annex S-3 for MHHS Metering Systems. |
| Secondary BM Unit Supplier Delivered Volume | VBMUSDVi2ji | MWh | The Secondary BM Unit half hourly Supplier Delivered Volumes determined by the SVAA pursuant to paragraph 9.6.1C of Annex S-2 for Non-MHHS Metering Systems or paragraph 6.6.4 of Annex S-3 for MHHS Metering Systems. |
| Second-Stage Flagged | | | Second-Stage Flagged in accordance with paragraph 8 of Part 1 of Annex T-1. |
| Sell Price Price Adjustment | SPAj | £/MWh | The amount sent by the NETSO as the ‘Sell Price Price Adjustment’ in accordance with Section Q6.3. |
| Settlement Expected Volume | SEV | MWh | The quantity determined in accordance with for Non-MHHS Metering Systems. *[sic: the paragraph reference is missing in the source]* |
| Settlement Expected Volumes | SEVij | MWh | The quantity determined in accordance with 5.3.5 Annex S-3 for MHHS Metering Systems. |
| Settlement Period | j | | A period of thirty minutes beginning on the hour or the half-hour and in accordance with paragraph 4.3 of this Annex X-2. |
| Settlement Period Duration | SPD | Hours | 0.5 hours. |
| Settlement Period Virtual Lead Party Compensation Cashflow | SVCCaj | £ | The amount determined in accordance with Section T4.11.5. |
| Site Specific Line Loss Factor | | | A Line Loss Factor established for a single Metering System as provided in Section K1.7.2. |
| Small Scale Third Party Generating Plant Limit | SSTPGPL | | The quantity established in accordance with Section L1.5<br>The Small Scale Third Party Generating Plant Limit is the maximum generation capacity (measured at the Boundary Point) of the aggregate Small Scale Third Party Generating Plant connected to a Distribution System at a single Boundary Point. |
| SO-Flagged Ranked Set | | | One of the SO-Flagged Ranked Sets as provided in paragraph 4 of Part 1 of Annex T-1. |
| Stable Export Limit | | | Has the meaning given to that term in BC1 of the Grid Code. |
| Stable Import Limit | | | Has the meaning given to that term in BC1 of the Grid Code. |
| Start Point Demand Control Level | | MW | Has the meaning given to that term in Section T3.15(a)(a). |
| STOR Action | | | An Accepted Offer derived from a STOR Flagged BOA taken by the NETSO during a STOR Availability Window in order to increase generation or reduce demand. |
| STOR Action Price | STAPt j | £/MWh | In relation to each STOR Action, the price determined in accordance with Section T3.14 |
| STOR Instructed Volume | QSIVt j | MWh | The Period Accepted Offer Volume in respect of each STOR Action instructed by the NETSO in order to increase generation or reduce demand. |
| Submitted Bid-Offer Pair | | | A Bid-Offer Pair in respect of which the NETSO submits Bid-Offer Data pursuant to Section Q6.2. |
| Supplier BM Unit Non BM ABSVD | SNBABSVDij | MWh | The amount determined by the SVAA pursuant to Annex S-2 paragraph 9.6.1C for Non-MHHS Metering Systems or Annex S-3 paragraph 6.6.5 for MHHS Metering Systems. |
| Supplier Compensation Proportion | CMPaj | MWh | The amount determined in accordance with Section T4.11.2. |
| Supplier Compensation Reference Price | SCRP | | Has the meaning given to that term in Paragraph 1.16 of Section T |
| Supplier Compensation Volume | QCVaj | MWh | The amount determined in accordance with Section T4.11.4. |
| Surplus | SPLD or SPLW | MW | Has the meaning given to that term in OC2 of the Grid Code |
| SVA (Production) Funding Share | FSPSpm | | Has the meaning given to that term in Section D1.2.1(c).<br>In relation to a month m, the SVA (Production) Funding Share represents a Party’s proportionate share of aggregate Credited Energy Volumes for Production BM Units for that month. |
| System Action | w | | Has the meaning given to that term in paragraph 1.2 of Annex T-1. |
| System Action Price | SAP wj | £/MWh | Has the meaning given to that term in paragraph 1.2 of Annex T-1. |
| System Buy Action | QSBwj | MWh | Has the meaning given to that term in paragraph 1.2 of Annex T-1. |
| System Buy Price | SBPj | £/MWh | The price determined in accordance with Section T4.4.2. |
| System Demand Control Volume | QSDCcj | MWh | Has the meaning given to it in Section T3.15.3(a). |
| System Operator Cashflow | CSOj | £ | The amount determined in accordance with Section T4.9.1.<br>The System Operator Cashflow is the amount paid by or to the System Operator in Settlement Period j in relation to the settlement of the Balancing Services. |
| System Period Compensation Volume | QCVj | MWh | The quantity determined in accordance with Section T4.11.3. |
| System Sell Action | QSSwj | MWh | Has the meaning given to that term in paragraph 1.2 of Annex T-1. |
| System Sell Price | SSPj | £/MWh | The price determined in accordance with Section T4.4.3. |
| System Warning | | | Has the meaning given to that term in BC1 of the Grid Code. |
| System Zone | | | Has the meaning given to that term in the Grid Code. |
| TLM-adjusted BM Unit Chargeable Demand | TCBMUDij | MWh | The amount determined in accordance with Section T8.1.3. |
| Total Instantaneous Out-Turn Generation | | MW | The total instantaneous generation metered by the NETSO in accordance with CC6.5.6 of the Grid Code. |
| Total Metered Capacity | | MW | The total value of the Registered Capacity of all Power Park Modules metered by the NETSO in accordance with CC6.5.6 of the Grid Code. |
| Total AMSID Pair Delivered Volume | TAPDVj | MWh | The amount determined in accordance with Annex S-2 3.11.3. |
| Total MSID Pair Delivered Volume | TMPDVj | MWh | The amount determined in accordance with Annex S-2 3.10.1B for Non-MHHS Metering Systems or Annex S-3 3.12.4 for MHHS Metering Systems. |
| Total Output Usable | | MW | Means the sum of Output Usables (as defined in the Grid Code) excluding (unless expressly stated otherwise in the Code) expected Interconnector transfer capacity. |
| Total Period Applicable Balancing Services Volume | TQASj | MWh | The amount determined in accordance with Section T4.6.5.<br>The Total Period Applicable Balancing Services Volume is the net quantity of energy associated with delivery of Applicable Balancing Services by all BM Units in Settlement Period j. |
| Total Period Out-Turn Generation | | MW | In respect of a Settlement Period, the total generation for that Settlement Period as metered by the NETSO in accordance with CC6.5.6 of the Grid Code. |
| Total Specified BSC Charges | TSCpm | £ | The sum of the Specified BSC Charges for Trading Party p relating to month m. |
| Total System Cashflow | TCBMj | £ | The amount determined in accordance with Section T3.12.1.<br>The Total System Cashflow is the total payments and charges in respect of settlement of Balancing Services action for all BM Units, disregarding any Non-Delivered Offer Charges and Non-Delivered Bid Charges. |
| Total System Energy Imbalance Cashflow | TCEIj | £ | The amount determined in accordance with Section T4.7.2.<br>The Total System Energy Imbalance Cashflow is the total cashflow resulting from the Settlement of Energy Imbalances, summed over all Energy Accounts in Settlement Period j. |
| Total System Energy Imbalance Volume | TQEIj | MWh | The quantity determined in accordance with Section T4.6.4.<br>Total System Energy Imbalance Volume is the sum over all Energy Accounts of the Account Energy Imbalance Volume.. |
| Total System Information Imbalance Charge | TCIIj | £ | The amount determined in accordance with Section T4.3.7.<br>The Total System Information Imbalance Charge is the total charge for information imbalances, summed over all BM Units in Settlement Period j. |
| Total System Non-Delivery Charge | TCNDj | £ | The amount determined in accordance with Section T4.8.14.<br>The Total System Non-Delivery Charge is the BM Unit Period Non-Delivery Charge summed over all BM Units in Settlement Period j. |
| Total System Residual Cashflow | TRCj | £ | The amount determined in accordance with Section T4.10.1.<br>The Total System Residual Cashflow is the surplus or deficit of funds remaining to be reallocated after the Settlement of Energy Imbalances, Information Imbalances, the Balancing Mechanism (including non-delivery) and the System Operator BM Charge. |
| Trading Unit Delivery Mode | | | A flag identifying whether a Trading Unit was a delivering Trading Unit or an offtaking Trading Unit determined in accordance with Section T6.1.3. |
| Trading Unit Export Volume | QTUErj | MWh | The volume determined in accordance with Section T6.1.1. |
| Trading Unit Import Volume | QTUIrj | MWh | The volume determined in accordance with Section T6.1.2. |
| Transmission Energy | | MWh | The integral with respect to time of National Demand. |
| Transmission Loss Factor | TLFij | | The factor specified in Section T2.2.1(a).<br>The Transmission Loss Factor is that factor used to allocate transmission losses on a locational basis to BM Unit i in Settlement Period j. |
| Transmission Loss Factor Adjustment | TLFAS | | The value determined in accordance with paragraph 9.1 of Annex T-2.<br>The Transmission Loss Factor Adjustment is the value calculated to ensure that, as far as possible, the Adjusted Seasonal Zonal TLF (ATLFZS) values have a zero net aggregate effect on Delivering Transmission Losses Adjustment (TLMO+j) values. |
| Transmission Loss Multiplier | TLMij | | The multiplier calculated in accordance with Section T2.3.1(a) or (b).<br>The Transmission Loss Multiplier is the factor applied to BM Unit i in Settlement Period j in order to adjust for Transmission Losses. |
| Transmission System Demand | | | Has the meaning given to the term National Electricity Transmission System Demand as defined in the Grid Code. |
| Transmission System Frequency | | Hertz | The Frequency of the Transmission System. |
| Unsubmitted Bid-Offer Pair | | | Has the meaning given to that term in Section T3.4B.2. |
| Utilisation Price | | £/MWh | The amount sent by the NETSO as a utilisation payment in respect of a STOR Action which:<br>(i) in relation to a BM STOR Action shall be the Offer Price; and<br>(ii) in relation to a Non-BM STOR Action shall be the Balancing Services Adjustment Cost. |
| Value of Lost Load | VoLL | £/MWh | Has the meaning given to it in Section T1.12.1. |
| Working Day Credit Assessment Load Factor | WDCALFi | | Is defined in Annex X-1.<br>The factor is used to establish the BM Unit Credit Assessment Export Capability and BM Unit Credit Assessment Import Capability for BM Unit i on a CALF Working Day determined for the purposes of Credit Assessment Load Factor. |
| Wholesale Market Proportion of Delivered Volume | WMi2j | | The volume determined in accordance with Section T4.3C.1. |
| Zonal Transmission System Demand | | | The forecast quantity of Transmission System Demand in a BMRS Zone. |

## Table X-3 – Glossary of Acronyms Applying Except In Relation To Section S

This table provides a list of the acronyms defined in Table X-2, presented in alphabetical order of the acronym name.

| Acronym | Units | Corresponding Defined Term or Expression |
|---|---|---|
| AEIp | MWh | Actual Energy Indebtedness |
| BMCAECi | MW | BM Unit Credit Assessment Export Capability |
| BMCAICi | MW | BM Unit Credit Assessment Import Capability |
| BMUADDVij | MWh | BM Unit Allocated Demand Disconnection Volume |
| BMUADVij | MWh | BM Unit Allocated Demand Volume |
| BOLRnij(t) | MW | Bid-Offer Lower Range |
| BOURnij(t) | MW | Bid-Offer Upper Range |
| BPAj | £/MWh | Buy Price Price Adjustment |
| BSAPmj | £/MWh | Balancing Services Adjustment Price |
| CADki | Minutes | Continuous Acceptance Duration |
| CADL | Minutes | Continuous Acceptance Duration Limit |
| CAEIaj | £ | Account Energy Imbalance Cashflow |
| CAEIp | £ | Daily Party Energy Imbalance Cashflow |
| CALFi | | Credit Assessment Load Factor |
| CAP | £/MWh | Credit Assessment Price |
| CAQCEiaj | MWh | Credit Assessment Credited Energy Volume |
| CBMij | £ | Period BM Unit Cashflow |
| CBMp | £ | Daily Party BM Unit Cashflow |
| CBMUDij | MWh | BM Unit Chargeable Demand |
| CBnij | £ | Period BM Unit Bid Cashflow |
| CCECp | £ | Credit Cover Error Compensation |
| CCp | £ | Credit Cover |
| CCPpj | % | Credit Cover Percentage |
| CEIpj | MWh | Credit Assessment Energy Indebtedness |
| CGCAEIaj | £ | Claim Group non-corrected Account Energy Imbalance Cashflow |
| CIIij | £ | Information Imbalance Charge |
| CIIp | £ | Daily Party Information Imbalance Charge |
| CMPaj | MWh | Supplier Compensation Proportion |
| CNDBnij | £ | Non-Delivered Bid Charge |
| CNDij | £ | BM Unit Period Non-Delivery Charge |
| CNDOnij | £ | Non-Delivered Offer Charge |
| CNDp | £ | Daily Party Non-Delivery Charge |
| COnij | £ | Period BM Unit Offer Cashflow |
| CORCiNj | MWh | Corrected Component |
| CORABSVDCi2Nj | | Corrected MSID ABSVD Component |
| CSO | £ | Daily System Operator BM Cashflow |
| CSOj | £ | System Operator BM Cashflow |
| DMAT | MWh | De Minimis Acceptance Threshold |
| ECApj | £ | Credit Cover Error Interest Amount |
| ECBpj | £ | Credit Cover Error Imbalance Amount |
| ECCp | MWh | Energy Credit Cover |
| ECQzabj | MWh | Energy Contract Volume |
| EEIpj | MWh | Erroneous Energy Indebtedness |
| EIpj | MWh | Energy Indebtedness |
| f | | Point Value Identification Number |
| FDij | MWh | Final Demand |
| fFPNijt | MW | Point FPN |
| FLAGpj | | Credit Cover Error Erroneous Rejection Flag |
| FPNij | MWh | Period FPN |
| FPNij(t) | MW | FPN |
| fqBOnijt | MW | Point Bid-Offer Volume |
| FSGpm | | General Funding Share |
| FSMpm | | Main Funding Share |
| FSPSpm | | SVA (Production) Funding Share |
| i | | BM Unit Identification Number |
| ICBnij | £ | Indicative Period Balancing Mechanism Bid Cashflow |
| ICOnij | £ | Indicative Period Balancing Mechanism Offer Cashflow |
| IECCp | MWh | Initial Energy Credit Cover |
| IIPj | £/MWh | Information Imbalance Price |
| IMBALNGC | MW | Indicated Imbalance |
| IMVj | MWh | Interconnector Metered Volume |
| INDDEM | MW | Indicated Demand |
| INDGEN | MW | Indicated Generation |
| INDO | MW | Initial National Demand Out-Turn |
| INIVj | MWh | Indicative Net Imbalance Volume |
| IQABnij | MWh | Indicative Period BM Unit Total Accepted Bid Volume |
| IQAOnij | MWh | Indicative Period BM Unit Total Accepted Offer Volume |
| ISBPj | £/MWh | Indicative System Buy Price |
| ISSPj | £/MWh | Indicative System Sell Price |
| ITSDO | MW | Initial Transmission System Demand Out-Turn |
| j | | Settlement Period |
| k | | Bid-Offer Acceptance Number |
| LLFC | | Line Loss Factor Class |
| LoLPj | | Final Loss of Load Probability |
| m | | Balancing Services Adjustment Action |
| MAQCEiaj | MWh | Metered Credit Assessment Credited Energy Volume |
| MDCm | £ | Monthly Default Costs |
| MEIpj | MWh | Metered Energy Indebtedness |
| MELNGC | MW | Indicated Constraint Boundary Margin |
| MNMCm | £ | Monthly Net Main Costs |
| MPDV | MWh | MSID Pair Delivered Volume |
| MPj | | Market Price |
| MPSCm | £ | Monthly Production-Charging SVA Costs |
| n | | Bid-Offer Pair Number |
| NCBMUDij | MWh | Period BM Unit Non Chargeable Demand |
| NDPBnij | £/MWh | Non-Delivered Bid Price |
| NDPOnij | £/MWh | Non-Delivered Offer Price |
| NIVj | MWh | Net Imbalance Volume |
| NTEBVAj | MWh | NIV Tagged EBVA |
| NTESVAj | MWh | NIV Tagged ESVA |
| NUEBVAj | MWh | NIV Untagged EBVA |
| NUESVAj | MWh | NIV Untagged ESVA |
| NWDCALFi | | Non-Working Day Credit Assessment Load Factor |
| OCNMFD | MW | Generating Plant Demand Margin (daily value) |
| OCNMFW | MW | Generating Plant Demand Margin (weekly value) |
| PAR | MWh | Price Average Reference Volume |
| PBnij | £/MWh | Bid Price |
| POnij | £/MWh | Offer Price |
| PXPsj | £/MWh | Market Index Price |
| QABCaj | MWh | Account Bilateral Contract Volume |
| QABknij | MWh | Period Accepted Bid Volume |
| qABknij(t) | MW | Accepted Bid Volume |
| QABnij | MWh | Period BM Unit Total Accepted Bid Volume |
| qABOknij(t) | MW | Accepted Bid-Offer Volume |
| QABSaj | MWh | Account Period Balancing Services Volume |
| QACEaj | MWh | Account Credited Energy Volume |
| QADEij | MWh | Account Period Deviation Volume |
| QAEIaj | MWh | Account Energy Imbalance Volume |
| qAkij(t) | MW | Acceptance Volume |
| qAkit | MW | Point Acceptance Volume |
| QAOknij | MWh | Period Accepted Offer Volume |
| qAOknij(t) | MW | Accepted Offer Volume |
| QAOnij | MWh | Period BM Unit Total Accepted Offer Volume |
| QASij | MWh | BM Unit Applicable Balancing Services Volume Data or BM Unit ABSVD |
| QBDCcj | MWh | Balancing Demand Control Volume |
| qBOnij(t) | MW | Bid-Offer Volume |
| QBSABmj | MWh | Balancing Services Adjustment Buy Volume |
| QBSAmj | MWh | Balancing Services Adjustment Volume |
| QBSASmj | MWh | Balancing Services Adjustment Sell Volume |
| QBSDij | MWh | Period Supplier BM Unit Delivered Volume |
| QBSij | MWh | Period BM Unit Balancing Services Volume |
| QCEiaj | MWh | Credited Energy Volume |
| QCVaj | MWh | Supplier Compensation Volume |
| QCViji2 | MWh | Period Secondary BM Unit Supplier Compensation |
| QCVj | MWh | System Period Compensation Volume |
| QCVji2 | MWh | Period Secondary BM Unit Supplier Compensation Volume |
| QDDij | MWh | Period BM Unit Demand Disconnection Volume |
| QDEij | MWh | Deviation Volume |
| QDViji2 | MWh | Period Secondary BM Unit Direct Compensation |
| QDVji2 | MWh | Period Secondary BM Unit Direct Compensation Volume |
| QNGSIAij | MWh | Network Gas Supply Imbalance Adjustment Volume |
| QIIij | MWh | Period Information Imbalance Volume |
| QMEij | MWh | Period Expected Metered Volume |
| QMFRiaj | MWh | Metered Volume Fixed Reallocation |
| QMFRziaj | MWh | Metered Volume Reallocation Fixed Data |
| QMij | MWh | BM Unit Metered Volume |
| QMPRiaj | % | Metered Volume Percentage Reallocation |
| QMPRziaj | % | Metered Volume Reallocation Percentage Data |
| QNDBij | MWh | Period BM Unit Non-Delivered Bid Volume |
| QNDBnij | MWh | Bid Non-Delivery Volume |
| QNDOij | MWh | Period BM Unit Non-Delivered Offer Volume |
| QNDOnij | MWh | Offer Non-Delivery Volume |
| QSBwj | | System Buy Action |
| QSDCcj | MWh | System Demand Control Volume |
| QSDij or QSDi2j | MWh | Period Secondary BM Unit Delivered Volume |
| QSDiji2 | MWh | Period Secondary BM Unit Supplier Delivered Volume |
| QSIVt j | MWh | STOR Instructed Volume |
| QSNDij | MWh | Period Secondary BM Unit Non-Delivered Volume |
| QSSwj | | System Sell Action |
| QSVij | MWh | Period BM Unit Supplier Compensation Volume |
| QTUErj | MWh | Trading Unit Export Volume |
| QTUIrj | MWh | Trading Unit Import Volume |
| QVBMDi2NKij | MWh | Secondary BM Unit Delivered Volume |
| QXPsj | MWh | Market Index Volume |
| RBPj | £/MWh | Replacement Buy Price |
| RCRCaj | £ | Residual Cashflow Reallocation Cashflow |
| RCRCp | £ | Daily Party Residual Settlement Cashflow |
| RCRPaj | No Units | Residual Cashflow Reallocation Proportion |
| REJaj | MWh | Credit Cover Error Rejection Volume |
| RPAR | | Replacement Price Average Reference Volume |
| RPj | £/MWh | Replacement Price |
| RQNDBuij | MWh | Remaining Period BM Unit Non-Delivered Bid Volume |
| RQNDOuij | MWh | Remaining Period BM Unit Non-Delivered Offer Volume |
| RSPj | £/MWh | Replacement Sell Price |
| RSVPj | £/MWh | Reserve Scarcity Price |
| SAPwj | | System Action Price |
| SBPj | £/MWh | System Buy Price |
| SCCp | £ | Daily Supplier Compensation Cashflow |
| SCRP | | Supplier Compensation Reference Price |
| SCVp | £ | Daily Virtual Lead Party Compensation Cashflow |
| SDCp | £ | Daily Direct Compensation Cashflow |
| SNBABSVDij | MWh | Supplier BM Unit Non BM ABSVD |
| SPAj | £/MWh | Sell Price Price Adjustment |
| SPBMEIaij | MWh | Settlement Period BM Unit Energy Indebtedness |
| SPD | h | Settlement Period Duration |
| SPiji2 | MWh | Period Secondary BM Unit Delivered Proportion |
| SPLD | MW | Surplus (daily value) |
| SPLW | MW | Surplus (weekly value) |
| SSPj | £/MWh | System Sell Price |
| SSTPGPL | | Small Scale Third Party Generating Plant Limit |
| STAPt j | £/MWh | STOR Action Price |
| SPCCij | £ | Period Supplier Compensation Cashflow |
| SPDCji2 | £ | Period Direct Compensation Cashflow |
| SVCCaj | £ | Settlement Period Virtual Lead Party Compensation Cashflow |
| TCBMj | £ | Total System BM Cashflow |
| TCBMUDij | MWh | TLM-adjusted BM Unit Chargeable Demand |
| TCEIj | £ | Total System Energy Imbalance Cashflow |
| TCIIj | £ | Total System Information Imbalance Charge |
| TCNDj | £ | Total System Non-Delivery Charge |
| TNGSBi | £ | Network Gas Supply Total Bid Payment |
| Tkit | Spot time | Bid-Offer Acceptance Time |
| TLFAS | | Transmission Loss Factor Adjustment |
| TLFij | | Transmission Loss Factor |
| TLMij | No Units | Transmission Loss Multiplier |
| TLMO+j | | Delivering Transmission Losses Adjustment. |
| TLMO-j | | Offtaking Transmission Losses Adjustment |
| TQASj | MWh | Total Period Applicable Balancing Services Volume |
| TQEIj | MWh | Total System Energy Imbalance Volume |
| TRCj | £ | Total System Residual Cashflow |
| TSCpm | £ | Total Specified BSC Charges |
| u | | Non-Delivery Order Number |
| VBMUSDVi2ij | MWh | Secondary BM Unit Supplier Delivered Volume |
| VLPDVi2j | MWh | Party-Aggregated Secondary BM Unit Demand Volume |
| VLPSDVi2j | MWh | Party-Aggregated Secondary BM Unit Delivered Volume |
| VoLL | £/MWh | Value of Lost Load |
| w | | System Action |
| WDCALFi | | Working Day Credit Assessment Load Factor |
| WMi2j | | Wholesale Market Proportion of Delivered Volume |

*[Table X-3 does not always match Table X-2 exactly, e.g. QVBMDi2NKij here vs QVBMDi2NKji in Table X-2, VBMUSDVi2ij vs VBMUSDVi2ji, and CALFi, CAP, CGCAEIaj, NTEBVAj–NUESVAj and SPBMEIaij appear here without a Table X-2 entry. Both are given as in the source.]*

## Table X–4 – Use of Subscripts and Superscripts Applying to Section S

The following subscripts used in the formulae and other algebraic expressions contained in the Code shall bear the following respective meanings for Section S of the Code:

| Subscript | Meaning |
|---|---|
| a | refers to a Data Aggregator or, as the context may require in paragraph 3.5 of Annex S-2, to a Data Aggregator appointed by a Primary Supplier against a Primary SVA Metering System Number and a Data Aggregator appointed by an associated Secondary Supplier against a Secondary SVA Metering System Number; |
| a1 | refers to a Data Aggregator appointed by a Primary Supplier against a Primary SVA Metering System Number K1; |
| a1.1 | refers to a Data Aggregator appointed by a Primary Supplier against a Primary SVA Metering System Number K1.1; |
| an | refers to a Data Aggregator appointed by a Secondary Supplier against a Secondary SVA Metering System Number Kn; |
| an.1 | refers to a Data Aggregator appointed by a Secondary Supplier against a Secondary SVA Metering System Number Kn.1; |
| (aa) | refers to an Analysis Class; |
| (ai) | refers to an Adjusted Interval; |
| j | refers to a Settlement Period; |
| i | refers to a BM Unit; |
| i2 | refers to a Secondary BM Unit (where applicable); |
| (nn) | refers to an individual value of the Regression Coefficient (RC) or of the Matrix of Regression Coefficients (MRC), according to the context; |
| (vv) | refers to a Consumption Component Class (not for line losses) associated with Consumption Component Class N; |
| (vvn) | refers to a Consumption Component Class (not for line losses) associated with Consumption Component Class N for which the data aggregation type is ‘N’; |
| q | refers to a calendar quarter; |
| d(q) | refers to the number of days in a calendar quarter; |
| C | refers to a Standard Settlement Configuration; |
| D | refers to a Settlement Day; |
| D | refers to a Settlement Day in UTC; |
| G | refers to a Supplier Volume Reporting Group; |
| H | refers to a GSP Group; |
| J | refers to a Settlement Register; |
| K | Refers to a Metering System associated with an SVA Non-Final Demand Facility; and<br>refers to an SVA Metering System Number and/or Asset Metering System associated with the provision of a Balancing Service; |
| K1 | refers to a Primary SVA Metering System Number; |
| K1.1 | refers to the "virtual" Primary SVA Metering System Number where Section K2.5.4(c)(ii) applies to the Primary Supplier; |
| Kn | refers to a Secondary SVA Metering System Number; |
| Kn.1 | refers to the "virtual" Secondary SVA Metering System Number where Section K2.5.4(c)(ii) applies to the Secondary Supplier; |
| L | refers to a Line Loss Factor Class; |
| MS | refers to a Market Segment; |
| N | refers to a Consumption Component Class; |
| N(c) | refers to a non half hourly active import Consumption Component Class; |
| P | refers to a Profile Class; |
| Q | refers to a Profile; |
| R | refers to a valid combination of Time Pattern Regime and Standard Settlement Configuration; |
| RT | refers to a Volume Allocation Run; |
| T | refers to a Settlement Day; |
| X | refers to a Time Pattern Regime; |
| Y | refers to a calendar year; |
| Z | refers to a Supplier or, as the context may require in paragraph 3.5 of Annex S-2, to the Suppliers acting in the capacity of Primary Supplier and associated Secondary Supplier(s) in respect of a particular Shared SVA Metering System; |
| Z1 | refers to a Supplier acting in the capacity of Primary Supplier in respect of a Shared SVA Metering System; and |
| Zn | refers to a Supplier acting in the capacity of Secondary Supplier in respect of a Shared SVA Metering System. |

*[D appears twice in the source, once for a Settlement Day and once for a Settlement Day in UTC; it may have been styled differently in the original.]*

## Table X–5 – Use of Summations Applying to Section S

The following summations, used in the formulae and other algebraic expressions in Section S, shall bear the following respective meanings:

*[The "Rendered" column is editorial: the same summation written in LaTeX, with the source's following subscripts placed under Σ.]*

| Summation | Rendered | Meaning |
|---|---|---|
| Σa | $`\sum_{a}`$ | = summed over all Data Aggregators (a); |
| Σ(ai) | $`\sum_{(ai)}`$ | = summed over all Adjusted Intervals ((ai)) associated with the spot time in question for all Time Pattern Regimes associated with a particular Standard Settlement Configuration; |
| Σj | $`\sum_{j}`$ | = summed over all Settlement Periods; |
| Σj | $`\sum_{j}`$ | = summed over all UTC Periods; |
| ΣN | $`\sum_{N}`$ | = summed over all Consumption Component Classes (N) where, in such summation, values associated with Consumption Component Classes associated with Third Party Generating Plant comprised in SVA Metering Systems shall be subtracted and values associated with all other Consumption Component Classes shall be added, except in the case of ΣN(AA) and ΣN(EAC) for the purposes of Annex S-1 paragraph 2 and in the case of ΣN(MHHSA) and ΣN(MHHSL *[sic: closing bracket missing]* for the purposes of Annex s-1 paragraph 3.6; |
| ΣN(n) | $`\sum_{N(n)}`$ | = summed over all those Consumption Component Classes (N) for which the data aggregation type is ‘N’ and where, in such summation, values associated with Consumption Component Classes associated with Third Party Generating Plant comprised in SVA Metering Systems shall be subtracted and values associated with all other Consumption Component Classes shall be added; |
| ΣT | $`\sum_{T}`$ | = summed over all Settlement Days (T) in a particular Meter Advance Period; |
| ΣZ | $`\sum_{Z}`$ | = summed over all Suppliers (Z); |
| ΣKJ | $`\sum_{KJ}`$ | = summed over all Settlement Registers (J) in a particular SVA Metering System (K); |
| ΣKNonDiff | $`\sum_{K_{NonDiff}}`$ | = summed over all Asset Metering Systems “K” allocated to a BM Unit in accordance with paragraph S10.1A.2(e)(i) |
| ΣKDiff | $`\sum_{K_{Diff}}`$ | = summed over all Asset Metering Systems “K” allocated to a BM Unit in accordance with paragraph S10.1A.2(e)(ii) |
| ΣNLK | $`\sum_{NLK}`$ | = summed over all SVA Metering Systems (K) within a particular Line Loss Factor Class (L) and Consumption Component Class (not for line losses) (N); |
| Σ(vv)LK | $`\sum_{(vv)LK}`$ | = summed over all SVA Metering Systems (K) within a Line Loss Factor Class (L) and Consumption Component Class (for line losses) associated with a particular Consumption Component Class (not for line losses) ((vv)); |
| Σ(vv)LK | $`\sum_{(vv)LK}`$ | = summed over all Line Loss Factor Classes (L) and Metering Systems K within a Consumption Component Class (for losses) associated with a particular Consumption Component Class (not for losses) ((vv)); |
| ΣNLPR | $`\sum_{NLPR}`$ | = summed over all kWh readings within a Settlement Class (LPR) itself within a particular Consumption Component Class (N); |
| ΣN(n)LPR | $`\sum_{N(n)LPR}`$ | = summed over all kWh readings within a Settlement Class (LPR) itself within a particular Consumption Component Class (N) for which the data aggregation type is ‘N’; |
| Σ(vv)L | $`\sum_{(vv)L}`$ | = summed over all Line Loss Factor Classes (L) within a Consumption Component Class (for losses) associated with a particular Consumption Component Class (not for losses) ((vv)); |
| Σ(vvn)L | $`\sum_{(vvn)L}`$ | = summed over all Line Loss Factor Classes (L) within a Consumption Component Class (for losses) associated with a particular Consumption Component Class (not for line losses) for which the data aggregation type is ‘N’ ((vvn)); |
| Σ(vv)PR | $`\sum_{(vv)PR}`$ | = summed over all Profile Classes (P) and Time Pattern Regimes within Standard Settlement Configuration (R) within a Consumption Component Class (for losses) associated with a particular Consumption Component Class (not for losses) ((vv)); |
| Σ(vvn)PR | $`\sum_{(vvn)PR}`$ | = summed over all Profile Classes (P) and Time Pattern Regimes within Standard Settlement Configuration (R) within a Consumption Component Class (for losses) associated with a particular Consumption Component Class (not for line losses) for which the data aggregation type is ‘N’ ((vvn)); |
| ΣHZLPRK | $`\sum_{HZLPRK}`$ | = summed over all non half hourly SVA Metering Systems (K) by Settlement Class (HLPR) for a particular Supplier (Z); and |
| ΣHZ | $`\sum_{HZ}`$ | = summed over all Suppliers (Z) active within a particular GSP Group (H). |
| ΣON | $`\sum_{ON}`$ | = summed over all Settlement Periods in a Settlement Day for which the Modified Switched Load State Indicator (SQNEWCj) has been determined as equal to one by the Supplier Volume Allocation Agent; |
| ΣOFF | $`\sum_{OFF}`$ | = summed over all Settlement Periods in a Settlement Day for which the Modified Switched Load State Indicator (SQNEWCj) has been determined as equal to zero by the Supplier Volume Allocation Agent; |
| ΣN(AA) | $`\sum_{N(AA)}`$ | = summed over all Consumption Component Classes N that are associated with Annualised Advances; |
| ΣN(EAC) | $`\sum_{N(EAC)}`$ | = summed over all Consumption Component Classes N that are associated with Estimated Annual Consumptions; |
| Σmd | $`\sum_{md}`$ | = summed over all Settlement Days in a month |
| ΣN(HHA) | $`\sum_{N(HHA)}`$ | = summed over all Consumption Component Classes that are associated with actual values and with half hourly data aggregation in relation to Metering Systems which are 100kW Metering Systems save those which are associated with SVA Generation and SVA Generation line losses; |
| ΣN(HHE) | $`\sum_{N(HHE)}`$ | = summed over all Consumption Component Classes that are associated with estimated values and with half hourly data aggregation in relation to Metering Systems which are 100kW Metering Systems save those which are associated with SVA Generation and SVA Generation line losses. |
| ΣHi | $`\sum_{Hi}`$ | = summed over all Supplier BM Units (i) associated with a particular GSP Group (H); |
| ΣHZi | $`\sum_{HZi}`$ | = summed over all Supplier BM Units (i) associated with a particular GSP Group (H) and Supplier (Z); |
| ΣHPRZL | $`\sum_{HPRZL}`$ | = summed over all Suppliers (Z) and Line Loss Factor Classes (L) for Standard Settlement Configuration and Time Pattern Regime combination (R) in Profile Class (P) within GSP Group (H); |
| ΣHPRT | $`\sum_{HPRT}`$ | = summed over all Settlement Days (T) contained within the Calculation Period for which one or more values of TAAHZLPR was determined for Standard Settlement Configuration and Time Pattern Regime combination (R) in Profile Class (P) within GSP Group (H); |
| ΣHPCR | $`\sum_{HPCR}`$ | = summed over all Standard Settlement Configuration and Time Pattern Regime combinations (R) valid for Standard Configuration (C) and Profile Class (P) within GSP Group (H); |
| ΣHPCTR | $`\sum_{HPCTR}`$ | = summed over all Standard Settlement Configuration and Time Pattern Regime combinations (R) valid for Standard Settlement Configuration (C) in Profile Class (P) within GSP Group (H) for Settlement Day (T); |
| ΣHPCZL | $`\sum_{HPCZL}`$ | = summed over all Suppliers (Z) and Line Loss Factor Classes (L) for any one valid combination of Standard Settlement Configuration and Time Pattern Regime for Standard Settlement Configuration (C) in Profile Class (P) within GSP Group (H); |
| ΣHPTC | $`\sum_{HPTC}`$ | = summed over all Standard Settlement Configurations (C) for Profile Class (P) within GSP Group (H) for Settlement Day (T); |
| ΣHPT | $`\sum_{HPT}`$ | = summed over all Settlement Days (T) for Profile Class (P) within GSP Group (H). |
| ΣN(AI) | $`\sum_{N(AI)}`$ | = summed over all Consumption Component Classes N that are associated with active import. |
| ΣZqG | $`\sum_{ZqG}`$ | = summed by Supplier (Z) over a calendar quarter (q) by Supplier Volume Reporting Group (G); |

*[Σj appears twice (Settlement Periods; UTC Periods), as does Σ(vv)LK; they may have been styled differently in the original. The source writes ΣKNonDiff and ΣKDiff run together; the rendering treats NonDiff/Diff as a qualifier on K.]*

## Table X–6 – Definitions Applying To Section S

Unless otherwise expressly stated the expressions below bear the following meanings in Section S.

The definition of Non Half Hourly Supplier Deemed Take (NHHSDTHZj) also applies to Annex D-1.

The definition of Measurement Class also applies to Section V and Section W.

| Expression | Acronym | Units | Definition |
|---|---|---|---|
| | K1HPC and K2HPC | Numbers | Baseload Profile Consumption during the ‘on’ and ‘off’ periods respectively of switched load Time Pattern Regimes for a valid Standard Settlement Configuration associated with switched load, determined pursuant to paragraph 6.6 of Annex S-2. |
| | SIX_PM | Minutes | The time duration from the start of the Settlement Day to 1800 hours Greenwich Mean Time on that Settlement Day, determined pursuant to paragraph 6.5 of Annex S-2. |
| ABSVD BM Unit Delivered Volume | AQVMDNLKji | MWh | The quantity determined in accordance with paragraph 7.1.1E of Annex S-2 for Non-MHHS Metering Systems. |
| ABSVD BM Unit Delivered Volume | AQVMDiNLKj | | The quantity determined in accordance with paragraph 5.1.1E of Annex S-3 for MHHS Metering Systems. |
| Adjusted Interval | | | A period of time associated with a particular Time Pattern Regime based on a time period for which the associated Settlement Registers record Metered Data and determined pursuant to paragraph 6.4 of Annex S-2. |
| Adjusted Interval End Time | | | A time associated with a particular Time Pattern Regime and Standard Settlement Configuration determined pursuant to paragraph 6.4 of Annex S-2. |
| Adjusted Interval Start Time | | | A time associated with a particular Time Pattern Regime and Standard Settlement Configuration determined pursuant to paragraph 6.4 of Annex S-2. |
| Allocated BM Unit’s Demand Disconnection Volume | ABDDiaNLKj | kWh | The half hour Demand Disconnection volume of a Metering System determined pursuant to paragraph 3.8 of Annex S-2. |
| Allocated BM Unit’s Metering System Metered Consumption | ABMMMCiaNLKj | kWh | The half hour metered Consumption of a Metering System determined pursuant to paragraph 3.6 of Annex S-2. |
| Allocated Metering System Metered Consumption | AVMMCHZaNLKji | MWh | The quantity determined in accordance with paragraph 3.9.2 of Annex S-2 for Non-MHHS Metering Systems.<br>The Allocated Metering System Metered Consumption is the Half Hourly metered volume per Settlement Period of SVA Metering Systems |
| Allocated Metering System Metered Consumption | AVMMCHZNLKji | MWh | The quantity determined in accordance with paragraph 5.1.1F of Annex S-3 for MHHS Metering Systems.<br>The Allocated Metering System Metered Consumption is the Half Hourly metered volume per Settlement Period of SVA Metering Systems |
| Allocated Asset Metering System Metered Consumption | AAVMMCHNLKj | kWh | The quantity determined in accordance with paragraph 3.9.2A of Annex S-2 for Non-MHHS Metering Systems or paragraph 3.11.3 of Annex S-3 for MHHS Metering Systems.<br>The Allocated Asset Metering System Metered Consumption is the Half Hourly metered volume per Settlement Period of Asset Metering Systems |
| ”AMSID Declaration Boundary Point Export” | ADBPEDi | kWh | The quantity determined in accordance with paragraph 3.11.2 of Annex S-2 for Non-MHHS Metering Systems or paragraph 3.13.2 of Annex S-3 for MHHS Metering Systems.<br>The AMSID Declaration Boundary Point Export” is the total metered Line Loss Adjusted Export for an EMR AMSID Declaration. |
| ”AMSID Declaration Boundary Point Import” | ADBPIDj | kWh | The quantity determined in accordance with paragraph 3.11.2 of Annex S-2 for Non-MHHS Metering Systems or paragraph 3.13.2 of Annex S-3 for MHHS Metering Systems.<br>The AMSID Declaration Boundary Point Import” is the total metered Line Loss Adjusted Import for an EMR AMSID Declaration. |
| ”AMSID Declaration Generation Export” | ADGEDj | kWh | The quantity determined in accordance with paragraph 3.11.2 of Annex S-2 for Non-MHHS Metering Systems or paragraph 3.13.2 of Annex S-3 for MHHS Metering Systems.<br>The AMSID Declaration Generation Export” is the total metered Line Loss Adjusted Export from a Generator or Storage Facility for an EMR AMSID Declaration. |
| ”AMSID Declaration Generation Import” | ADGIDj | kWh | The quantity determined in accordance with paragraph 3.11.2 of Annex S-2 for Non-MHHS Metering Systems or paragraph 3.13.2 of Annex S-3 for MHHS Metering Systems.<br>The AMSID Declaration Generation Import” is the total metered Line Loss Adjusted Import to a Generator or Storage Facility for an EMR AMSID Declaration. |
| ”AMSID Declaration Non-Chargeable Proportion” | ADNCPDj | kWh | The quantity determined in accordance with paragraph 3.11.2 of Annex S-2 for Non-MHHS Metering Systems or paragraph 3.13.2 of Annex S-3 for MHHS Metering Systems.<br>The AMSID Declaration Non-Chargeable Proportion is a number between 0.0 and 1.0 inclusive representing the proportion of Boundary Point Imports to the Import MSIDs included in the Declaration that are deemed Non-Chargeable in that Settlement Period |
| Annual Consumption | ANN_CON Ky | kWh | The quantity submitted in accordance with paragraph 3.15.2 of Annex S-3 for MHHS Metering Systems. |
| Asset Metering System Metered Consumption | AMMC Kj | kWh | The half hourly metered Consumption for a SVA Metering System, determined pursuant to paragraph 3.5 of Annex S-2 for Non-MHHS Metering Systems or paragraph 3.6.5 of Annex S-3 for MHHS Metering Systems. |
| Asset Metering System Metered Consumption | VMMC HNLKj | MWhkWh | The Metering System Metered Consumption for an Asset Metering System, determined pursuant to paragraph 7.1.1C of Annex S-2 for Non-MHHS Metering Systems or paragraph 5.1.1BA of Annex S-3 for MHHS Metering Systems. |
| Allocated Supplier’s Demand Disconnection Volume | ASDDHZaNLKj | kWh | The half hour Demand Disconnection volume of a SVA Metering System determined pursuant to paragraph 3.7 of Annex S-2. |
| Allocated Supplier’s Metering System Metered Consumption | ASMMCHZaNLKj | kWh | The half hour metered Consumption of a SVA Metering System determined pursuant to paragraph 3.5 of Annex S-2 for Non-MHHS Metering Systems.. |
| Allocated Supplier’s Metering System Metered Consumption | ASMMCHZNLKj | kWh | The metered Consumption of a SVA Metering System determined pursuant to paragraph 3.7 of Annex S-3 for MHHS Metering Systems. |
| AMSID Pair Data | | | The data comprising the data items pursuant to Section S10.1A |
| AMSID Pair Delivered Volume | AMPDVj | MWh | AMSID Pair Delivered Volume is such volumes of Active Energy notified by the Virtual Lead Party in relation to an AMSID Pair and each Associated MSID Pair for the purposes of aggregating Secondary BM Unit Supplier Delivered Volume (VBMUSDViZj) |
| Alternative Average Fraction of Yearly Consumption | AAFYCHPC | | A value set from time to time by the Panel for one or more multi-register Standard Settlement Configurations, and used in place of the corresponding Average Fraction of Yearly Consumption value for the purpose of calculating profile coefficients pursuant to paragraph 5.1 of Annex S-2. |
| Analysis Class | | | A combination of Season Type and Day Type. |
| Annual Fraction of Yearly Consumption Adjustment | AFYCAHPC | | The difference due to rounding between unity and the sum of the Unadjusted Average Fraction of Yearly Consumption Values for a Standard Settlement Configuration and Profile Class within a GSP Group, determined pursuant to paragraph 5.1 of Annex S-2. |
| Annualised Advance | AAKR | kWh | An estimation of the Meter Advance on a Settlement Register over a period of a year determined pursuant to paragraph 4.3 of Annex S-2. |
| Annualised Advance Adjustment Factor | AAAFKR | Number | A factor used in the determination of Estimated Annual Consumption and determined pursuant to paragraph 4.3 of Annex S-2. |
| Asset Meter Register Consumption | AMRCKJj | kWh | The half hourly metered Consumption for a Settlement Register within an Asset Metering System. |
| Average Fraction Of Yearly Consumption | AFYCHPR | | An estimate of the fraction of the total Consumption of a multi-register Standard Settlement Configuration attributable to each Settlement Register of that Standard Settlement Configuration pursuant to paragraph 4.4 of Annex S-2. |
| Base Fraction | BFHPC | Number | The deemed proportion of Consumption for a Switched Load Metering System which is baseload determined pursuant to paragraph 6.6 of Annex S-2. |
| Baseload Profile | | | The half-hourly profile of all non-switched loads in the Profile Class population, including non-switched loads taken during the periods when the switched load registers are recording Consumption and referred to in paragraph 6.6 of Annex S-2. |
| Baseload Profile Coefficient | BAPHQj | Number | One of the Basic Period Profile Coefficients which correspond to the Baseload Profile associated with a Switched Load Metering System, determined pursuant to paragraph 6.6 of Annex S-2. |
| Basic Period Profile Coefficient | PHQj | Number | A number determined pursuant to paragraph 6.5 of Annex S-2 and representing the fraction of annual Consumption in a given Settlement Period for a particular profile. |
| BM Unit Allocated Demand Disconnection Volume | BMUADDVij | MWh | The disconnection volume per Settlement Period for a Supplier BM Unit determined pursuant to paragraph 9.6.1A of Annex S-2 for Non-MHHS Metering Systems or paragraph 6.6.2 of Annex S-3 for MHHS Metering Systems. |
| BM Unit Allocated Demand Volume | BMUADVij | MWh | The energy volume per Settlement Period for a Supplier BM Unit determined pursuant to paragraph 9.6.1 of Annex S-2 for Non-MHHS Metering Systems or paragraph 6.6.1 of Annex S-3 for MHHS Metering Systems. |
| BM Unit Disconnection Matrix | BMDMiaLPR | | A matrix of data as determined pursuant to paragraph 8.2 of Annex S-2. |
| BMU Unit Period Level Consumption | BMPCiHNDj | MWh | The quantity submitted in accordance with paragraph 3.7.6 of Annex S-3 for MHHS Metering Systems. |
| BMU Unit Period Level Consumption Losses | BMPCLiHNDj | MWh | The quantity submitted in accordance with paragraph 3.7.7 of Annex S-3 for MHHS Metering Systems. |
| BM Unit Eligible Exempt Supply Volume | QBESi1i2j | | The exempt supply volume calculation pursuant to Section S paragraph 2.13.1 (d). |
| BM Unit Purchase Matrix | BMPMiaLPR | | A matrix of data as determined pursuant to paragraph 8.1 of Annex S-2. |
| BM Unit’s Demand Disconnection Volume | BMDDiaNj | MWh | The half hourly Demand Disconnection volume, determined by a Half Hourly Data Aggregator pursuant to paragraph 3.8 of Annex S-2, or by the SVAA pursuant to paragraph 7.1 of Annex S-2. |
| BM Unit’s Demand Disconnection Volume (Losses) | BMDDLiaNj | MWh | The line losses determined by a Half Hourly Data Aggregator as resulting from the BM Unit’s Demand Disconnection Volume pursuant to paragraph 3.8 of Annex S-2, or by the SVAA pursuant to paragraph 7.2 of Annex S-2. |
| BM Unit Gross Demand Volume | BMUGDVij | MWh | The quantity established in accordance with paragraph 9.6.1E of Annex S-2. |
| BM Unit’s Metered Consumption | BMMCiaNLj | MWh | The half hourly metered Consumption, determined by a Half Hourly Data Aggregator pursuant to paragraph 3.6 of Annex S-2, or by the SVAA pursuant to paragraph 7.1 of Annex S-2. |
| BM Unit’s Metered Consumption (Losses) | BMMCLiaNLj | MWh | The line losses determined by a Half Hourly Data Aggregator as resulting from the BM Unit’s Metered Consumption pursuant to paragraph 3.6 of Annex S-2, or by the SVAA pursuant to paragraph 7.2 of Annex S-2. |
| BM Unit’s Profiled Consumption | BMPCiLPRj | MWh | A Supplier BM Unit’s non half hourly Consumption profiled per Settlement Period for a particular Consumption Component Class, determined pursuant to paragraph 8.1 of Annex S-2. |
| BM Unit’s Profiled Disconnection | BMPDiLPRj | MWh | A Supplier BM Unit’s non half hourly Demand Disconnection volume profiled per Settlement Period for a particular Consumption Component Class, determined pursuant to paragraph 8.2 of Annex S-2. |
| Calculation Period | | | The period of consecutive Settlement Days (typically but not necessarily one year in duration) on whose Supplier Purchase Matrix data the calculation of Average Fractions of Yearly Consumption pursuant to paragraph 5.1 of Annex S-2 is based. |
| Certificate of Supply | | | For the purposes of Annex S-2 the Estimated Annual Consumption for a Non Qualifying Unmetered Supply as provided from time to time by Public Distribution Service Operator. |
| Clock Interval | | | A combination of seasons, dates, days and times defining the period over which Consumption is recorded by a Settlement Register the details of which are provided pursuant to paragraph 5.1.1 of Annex S-2. |
| Consumption | | MWh | The amount of electricity produced by a SVA Generator or used by an SVA Customer. |
| Consumption Component Class | | | A classification of half hourly Consumption and/or electricity produced or used by an Asset which comprises one element from each of the following categories as shown in Table X-8:<br>• metered or unmetered;<br>• consumption or SVA generation;<br>• SVA Metering System with or without Metering System specific line losses (but a SVA Metering System without Metering System specific line losses can only be combined with unmetered Consumption);<br>• Consumption without line losses or line losses;<br>• based on actual or estimated half hourly; or<br>• based on Annualised Advance or Estimated Annual Consumption. |
| Consumption Data | | | That part of the Supplier Purchase Matrix containing the values of Total Annualised Advance, Total Metered Estimated Annual Consumption and Total Unmetered Consumption. |
| Co-ordinated Universal Time | UTC | Number | Bears the same meaning as in the document Standard Frequency and Time Signal Emission, International Telecommunication Union RTF.460(ISBN92-61-05311-4) (colloquially referred to as Rugby Time). |
| Corrected Component | CORCiNj | MWh | The Consumption for a Supplier BM Unit's Consumption Component Class after the application of the GSP Group Correction Factor, determined pursuant paragraph 9.3 of Annex S-2 for Non-MHHS Metering Systems or Paragraph 6.3 of Annex S-3 for MHHS Metering Systems. |
| Corrected Component by Profile Class | CORCiN(c)Pj | MWh | The consumption for a Supplier BM Unit's Profile Class after the application of the GSP Group Correction Factor and Line Loss Factor, determined pursuant paragraph 9A.1.3 of Annex S-2. |
| Corrected Disconnection Component | CORDCiNj | MWh | The Demand Disconnection volume for a Supplier BM Unit's Consumption Component Class after the application of the GSP Group Correction Factor, determined pursuant to paragraph 9.3 of Annex S-2 for Non-MHH Meterings Systems or paragraph 6.3 of Annex S-3 for MHHS Metering Systems. |
| Corrected MSID ABSVD Component | CORABSVDCi2Nj | MWh | The quantity determined in accordance with paragraph 9.3.5 of Annex S-2 for Non-MHHS Metering Systems. |
| Corrected MSID ABSVD Component | CORABSVDCiNKj | MWh | The quantity determined in accordance with paragraph 6.3.5 of Annex S-3 for MHHS Metering Systems. |
| Customer Consent Flag | | | A flag in the SVA Metering System Register indicating that, in relation to a Supplier, an SVA Customer or SVA Generator has consented to their Metering System Delivered Volumes being provided to that Supplier in accordance with paragraphs 7.1.8 and 7.2.8 of Annex S-2 for Non-MHHS Metering Systyems or 5.1.8 of Annex S-3 for MHHS Metering Systems. |
| Daily Profile Coefficient | DPCHPRT | Number | A value which, when applied to an Estimated Annual Consumption or Annualised Advance value, supplies an estimate of Consumption for a Settlement Day and which is equal to the sum of the corresponding Period Profile Class Coefficients for that Settlement Day. |
| Day Type | | | A code describing whether a particular Settlement Day is a weekday, a Saturday, a Sunday, or a particular Bank Holiday. |
| Daily Total Volume Actual | DTVAHTZD | MWh | The quantity submitted in accordance with paragraph 3.9.6 of Annex S-3 for MHHS Metering Systems. |
| Daily Total Volume Estimated | DTVEHTZD | MWh | The quantity submitted in accordance with paragraph 3.9.6 of Annex S-3 for MHHS Metering Systems. |
| Deemed Meter Advance | DMAKR | kWh | An estimated Meter Advance calculated by the relevant Non-Half Hourly Data Collector pursuant to paragraph 4.3 of Annex S-2 and BSCP504. |
| Deemed Meter Advance Period | | | A period bearing the same relationship to a Deemed Meter Advance as a Meter Advance Period bears to a Meter Advance. |
| Default Estimated Annual Consumption For Metered Metering Systems | DEMHZLPR | kWh | The Estimated Annual Consumption value determined by a Non-Half Hourly Data Aggregator pursuant to paragraph 4.4 of Annex S-2. |
| Default Estimated Annual Consumption For Unmetered Metering Systems | DEUHZLPR | kWh | The value of Estimated Annual Consumption determined for an Unmetered Supply pursuant to paragraph 4.4 of Annex S-2. |
| Default Load Shape Period Value | DTVEHTZD | kWh | The quantity submitted in accordance with paragraph 3.5.3 of Annex S-3 for MHHS Metering Systems. |
| Demand Disconnection Daily Profile Coefficient | DDDPCHPKRT | Number | A value which, when applied to an Estimated Annual Consumption or Annualised Advance value, supplies an estimate of Demand Disconnection volume for a Settlement Day and which is equal to the sum of the corresponding Period Profile Class Coefficients for that Settlement Day multiplied by the proportion of each Settlement Period in that Settlement Day for which a given Metering System was subject to Demand Disconnection. |
| De-minimis Data Count | | | The de minimis value set against each Load Shape Category in the Industry Standing Data. |
| Effective From Settlement Date | | | The date of the Settlement Day on which an Annualised Advance or an Estimated Annual Consumption becomes effective. |
| Effective To Settlement Date | | | The date of the last Settlement Day on which an Annualised Advance is effective. |
| Embedded Total Uncorrected Volume | ETUVHTEDj | MWh | The quantity submitted in accordance with paragraph 3.9.7 of Annex S-3 for MHHS Metering Systems. |
| Eligible Exempt Supply Volumes | | | The exempt supply volume as calculated pursuant to Section S paragraph 2.13.1 (b). |
| Estimated Annual Consumption | EACKR | kWh | For each Settlement Register, an estimate of Consumption over a year. |
| Estimated Regional Average Demand Per Customer | YHQj | kW | An estimate of customer Consumption by profile and GSP Group in respect of each Settlement Period, determined pursuant to paragraph 6.5 of Annex S-2. |
| Export Consumption Component Class | | | a Consumption Component Class as shown in Table X-8 as having a measurement quantity ID of Active Export |
| Final AMSID Import | | | Active Import as measured by an AMSID Pair less Non-Final AMSID Import. |
| Final MSID Import | | | Active Import as measured by an Import MSID less Non-Final MSID Import less Non-Final AMSID Import of any associated AMSID Pairs. |
| Final Net Exporting AMSID Pair | | | In relation to Settlement Day, an AMSID Pair where the sum of Active Export over all Settlement Periods in the preceding 30 days is greater than the sum of Final AMSID Import over all Settlement Periods in the preceding 30 days. |
| Final Net Exporting MSID Pair | | | In relation to a Settlement Day, an MSID Pair where the sum of Active Export over all Settlement Periods in the preceding 30 days is greater than the sum of Final MSID Import over all Settlement Periods in the preceding 30 days. |
| Fraction Of Yearly Consumption | FYCKR | | The fraction of annual Consumption allocated to a Meter Advance Period pursuant to paragraph 4.3 of Annex S-2. |
| Grid Supply Point Group Measured Temperature | THT | °F | A temperature taken at locations and times from time to time agreed by the Panel and provided by the Temperature Provider pursuant to paragraph 5.2.2 of Annex S-2. |
| Group Average Annual Consumption | GAACHQ | MWh | The average annual Consumption for each GSP Group for each profile as supplied by the Profile Administrator pursuant to paragraph 5.1.4 of Annex S-2. |
| GSP Group Correction Factor for Active Import | CFHj | | The factor by which the relevant components of GSP Group Consumption are adjusted and which is determined pursuant to to paragraph 6.2 of Annex S-3. |
| GSP Group Correction Scaling Weight | WTN | Number | The weighting for each Consumption Component Class used in GSP Group correction and which is supplied pursuant to paragraph 5.1.5 of Annex S-2 for Non-MHHS Metering Systems or paragraph 3.13.5 of Annex S-3 for MHHS Metering Systems. |
| GSP Group Half Hourly Consumption | GCHNj | MWh | The GSP Group half hourly Consumption by Consumption Component Class determined pursuant to paragraph 9.1 of Annex S-2 for Non-MHHS Metering Systems or to paragraph 6.1 of Annex S-3 for MHHS Metering Systems. |
| GSP Group Profile Class Average Estimated Annual Consumption | GGPCAEACHPC | kWh | The average Estimated Annual Consumption in respect of a GSP Group, Profile Class and Standard Settlement Configuration determined pursuant to paragraph 5.1 of Annex S-2. |
| GSP Group Profile Class Default Estimated Annual Consumption | GGPCDEACHP | kWh | The average Estimated Annual Consumption provided in respect of a GSP Group and Profile Class pursuant to paragraph 5.1.3 of Annex S-2. |
| GSP Group Take | GSPGTHj | MWh | In relation to a GSP Group and a Settlement Period, the number submitted to the SVAA by the CDCA pursuant to Section R5.7.1(b). |
| Half Hourly Consumption (Losses) | CLOSSiNj | MWh | The half hourly Consumption for a Consumption Component Class which is defined as line losses, determined pursuant to paragraph 7.2 or 8.1 of Annex S-2 for Non-MHHS Metering Systems or 5.2 of Annex S-3 for MHHS Metering Systems. |
| Half Hourly Consumption (Losses) by Profile Class | CLOSSiN(c)Pj | MWh | The half hourly consumption for a Profile Class within a non half hourly active import Consumption Component Class which is defined as being for line losses, determined pursuant to paragraph 9A.1.2 of Annex S-2. |
| Half Hourly Consumption (Non Losses) | CiNj | MWh | The half hourly Consumption for a Consumption Component Class which is defined as not being line losses, determined pursuant to paragraph 7.1 or 8.1 of Annex S-2 for Non-MHHS Metering Systems or 5.1 of Annex S-3 for MHHS Metering Systems. |
| Half Hourly Consumption (Non Losses) by Profile Class | CiN(c)Pj | MWh | The half hourly consumption for a Profile Class within a non half hourly active import Consumption Component Class which is defined as not being for line losses, determined pursuant to paragraph 9A.1.1 of Annex S-2. |
| Half Hourly Demand Disconnection Volume | HDDKj | kWh | The quantity established in accordance with S-2 3.7.2.<br>The Half Hourly Demand Disconnection Volume (HDDKj) is calculated in reference to, for the Demand Control Impact Settlement Period ZaKj: the estimate of the metered data (E); the Supplier’s Metering System Metered Consumption (SMMC); and the estimated Non-BM STOR Instruction Volume anticipated to have been delivered (NBSVD). |
| Half Hourly Disconnection (Losses) | DLOSSiNj | MWh | The half hourly Demand Disconnection volume for a Consumption Component Class which is defined as line losses, determined pursuant to paragraph 7.2 or 8.2 of Annex S-2 for Non-MHHS Metering Systems. For MHHS Metering Systems, determined pursuant to 5.2.1A of Annex S-3 for MHHS Metering Systems |
| Half Hourly Disconnection (Non Losses) | DiNj | MWh | The half hourly Demand Disconnection volume for a Consumption Component Class which is defined as not being line losses, determined pursuant to paragraph 7.1 or 8.2 of Annex S-2. |
| Half Hourly Non-Final Demand Consumption (Losses) | SCLOSSiNj | MWh | In respect of an SVA Non-Final Demand Facility, the half hourly Consumption for a Consumption Component Class which is defined as line losses, determined pursuant to paragraph 13.5.2 of Annex S-2. |
| Half Hourly Non-Final Demand Consumption (Non Losses) | SCiNj | MWh | In respect of an SVA Non-Final Demand Facility, the half hourly Consumption for a Consumption Component Class which is defined as not being line losses, determined pursuant to paragraph 13.5.1 of Annex S-2. |
| Historical Daily Profile Coefficient | DPCHPRT | Number | A particular Daily Profile Coefficient in respect of a Settlement Day which Settlement Day occurs prior to the 1998 Operational Date and which is determined employing a method authorised by the Executive Committee. |
| Import Consumption Component Class | | | A Consumption Component Class as shown in Table X-8 as having a measurement quantity ID of Active Import |
| Ineligible AMSID Pair | | | In relation to a Settlement Day, an AMSID Pair that has not been identified as Inactive, where any associated MSID Pair of that AMSID Pair is an Ineligible MSID Pair, and the AMSID Pair is a Final Net Exporting AMSID Pair. |
| Ineligible MSID Pair | | | In relation to a Settlement Day, an MSID Pair that has not been identified as Inactive, where the MSID Pair Lookback Export is larger than the Upper Trading Eligibility Threshold, or where the MSID Pair Lookback Export is larger than the Lower Trading Eligibility Threshold and the MSID Pair is a Final Net Exporting MSID Pair. |
| Ineligible Trading Secondary BM Unit | | | A Trading Secondary BM Unit to which one or more Ineligible MSID Pairs or Ineligible AMSID Pairs are allocated. |
| Initial Total Annualised Advance | ITAAHZLPR | KWh | The total of all the Annualised Advances for a Supplier in kWh and in respect of a Profile Class, Line Loss Factor Class, Time Pattern Regime and GSP Group, determined pursuant to paragraph 4.4 of Annex S-2. |
| Initial Total Annualised Advance (Disconnected) | ITAADHZLPR | kWh | The total of all the Annualised Advances for a Supplier in kWh subject to Demand Disconnection and in respect of a Profile Class, Line Loss Factor Class, Time Pattern Regime and GSP Group, determined pursuant to paragraph 4.5 of Annex S-2. |
| Line Loss Factor | LLFLj | | A multiplier which, when applied to the value of a SVA Metering System’s Consumption, converts such value into its estimated value at the Grid Supply Point, that is including distribution losses. |
| Line Loss Factor Class | | | A set of SVA Metering Systems defined by a Distribution System Operator and relating to any one or more of its Distribution System(s) and that are assigned the same Line Loss Factor for the relevant Settlement Period. |
| Load Shape Category Count | LSCCOUNTDJC | | The quantity submitted in accordance with paragraph 3.5.2 of Annex S-3 for MHHS Metering Systems. |
| Load Shape Off-peak Total | LS_OFFDC | kWh | The quantity submitted in accordance with paragraph 3.5.9 of Annex S-3 for MHHS Metering Systems. |
| Load Shape Peak Total | LS_PEAKDC | kWh | The quantity submitted in accordance with paragraph 3.5.10 of Annex S-3 for MHHS Metering Systems. |
| Load Shape Period Total | LS_PEAKDjC | kWh | The quantity submitted in accordance with paragraph 3.5.7 of Annex S-3 for MHHS Metering Systems. |
| Load Shape Rolling 7 Day Off-peak Total | LS_ROLL_OFFDC | kWh | The quantity submitted in accordance with paragraph 3.5.12 of Annex S-3 for MHHS Metering Systems. |
| Load Shape Rolling 7 Day Peak Total | LS_ROLL_PEAKDC | kWh | The quantity submitted in accordance with paragraph 3.5.13 of Annex S-3 for MHHS Metering Systems. |
| Load Shape Rolling 7 Day Total | LS_ROLL_TOTDC | kWh | The quantity submitted in accordance with paragraph 3.5.11 of Annex S-3 for MHHS Metering Systems. |
| Load Shape Rolling Annual Total | LS_ROLL_ANN_TOTDC | kWh | The quantity submitted in accordance with paragraph 3.5.14 of Annex S-3 for MHHS Metering Systems. |
| Load Shape Total Data | LSTOTDC | kWh | The quantity submitted in accordance with paragraph 3.5.8 of Annex S-3 for MHHS Metering Systems. |
| Longest Off Period | | | A period used in determining profile coefficients for Switched Load Metering Systems and determined pursuant to paragraph 6.6 of Annex S-2. |
| Longest On Period | | | A period used in determining profile coefficients for Switched Load Metering Systems and determined pursuant to paragraph 6.6 of Annex S-2. |
| Low Fraction | LOWFHPC | Number | The deemed annual Consumption associated with the switched load Settlement Registers expressed as a fraction of total annual Consumption for a Switched Load Metering System, determined pursuant to paragraph 6.6 of Annex S-2. |
| Low Fraction Consumption | HHPC | Number | The ratio of electricity Consumption deemed as baseload Consumption during the ‘on’ periods of switched load Time Pattern Regimes to that during the ‘off’ periods of switched load Time Pattern Regimes, determined pursuant to paragraph 6.6 of Annex S-2. |
| Low Register Profile Coefficient | LRPCHPCj | Number | The deemed fraction of annual Consumption for a Switched Load Metering System in a Settlement Period recorded on those meter registers which are 'on' during times when there is switched load Consumption at such Metering System, determined pursuant to paragraph 6.6 of Annex S-2. |
| Lower Trading Eligibility Threshold | | | [2] MW multiplied by the Settlement Period Duration. |
| Matrix Of Regression Coefficients | MRCQ(aa)(nn)j | Various | The matrix of regression coefficients from time to time supplied by the Profile Administrator pursuant to paragraph 5.1.4 of Annex S-2. |
| Measurement Class for Non-MHHS Metering Systems | | | A classification of Metering Systems which indicates how Consumption is measured<br>i.e. Non Half Hourly Metering Equipment (equivalent to Measurement Class “A”)<br>Non Half Hourly Unmetered Supplies (equivalent to Measurement Class “B”)<br>Half Hourly Metering Equipment at above 100kW Premises (equivalent to Measurement Class “C”)<br>Half Hourly Unmetered Supplies (equivalent to Measurement Class “D”)<br>Half Hourly Metering Equipment at below 100kW Premises with current transformer (equivalent to Measurement Class “E”)<br>Half Hourly Metering Equipment at below 100kW Premises with current transformer or whole current, and at Domestic Premises (equivalent to Measurement Class “F”)<br>Half Hourly Metering Equipment at below 100kW Premises with whole current and not at Domestic Premises (equivalent to Measurement Class “G”). |
| Measurement Class for MHHS Metering Systems | | | The Measurement Class is only required for the purpose of creating the TUoS Report, and is derived from data held in SMRS as set out below:<br>Measurement Class C\*: Domestic Premises Indicator = F and Connection Type Indicator = L,H or E<br>Measurement Class D: Domestic Premises Indicator = FT and Connection Type Indicator = U<br>Measurement Class E\*: always 0kWh<br>Measurement Class F: Domestic Premises Indicator = T and Connection Type ≠ U: and<br>Measurement Class G: Domestic Premises Indicator = F and Connection Type = W<br>\*Measurement Class C will contain the sum of Measurement Classes C and E. |
| Measurement Quantity | | | An indicator to show whether Metered Data in respect of a Metering System is export or import active energy. |
| Meter Advance | MADVKR | kWh | The difference recorded for a Settlement Register between one reading, or as the case may be, deemed reading of this register and the next reading or, as the case may be, deemed reading of this register (that is over the Meter Advance Period) used in the determination of Annualised Advance pursuant to paragraph 4.3 of Annex S-2. In the case where such next reading is deemed, the Meter Advance may also be known more particularly as a Deemed Meter Advance in which case it shall have an associated Deemed Meter Advance Period. |
| Meter Advance Period | MAP | | The period of complete Settlement Days between successive meter readings for a Settlement Register, which shall be the period from and including the Settlement Day on which a meter reading is taken up to and including the Settlement Day prior to the Settlement Day on which the next meter reading is taken. |
| Metered Data | | | Data concerning the quantities of Active Energy exported or imported measured, collected, recorded and otherwise determined pursuant to the Code. |
| Metering System Delivered Volumes | QVMDKj | MWh | The quantity determined in accordance with paragraph 3.10.4A of Annex S-2 for Non-MHHS Metering Systems or paragraph 3.12.10 of Annex S-3 for MHHS Metering Systems. |
| Metering System Metered Consumption | VMMCHZaNKji | MWh | The quantity determined in accordance with paragraph 7.1.1B of Annex S-2 for Non-MHHS Metering Systems or paragraph 5.1.1B of Annex S-3 for MHHS Metering Systems. |
| “Metering System Non-Chargeable Consumption” | NCMCiNLKj | KWh | The quantity determined in accordance with paragraph 3.11.1 of Annex S-2 for Non-MHHS Metering Systems or paragraph 3.13.1for MHHS Metering Systems of Annex S-3. |
| “Metering System Non-Chargeable Losses” for an EMR MSID Declaration | NCMLiNLKj | KWh | The quantity determined in accordance with paragraph 3.11.1 of Annex S-2 for Non-MHHS Metering systems or paragraph 3.13.1 of Annex S-3 for MHHS Metering Systems. |
| Metering System Period Disconnection Duration | MKj | Hours | The duration in hours in a given Settlement Period for which a given Metering System was subject to Demand Disconnection. |
| Modified Switched Load State Indicator | SQNEWCj | Indicator (1 or 0) | A Switched Load State Indicator modified pursuant to paragraph 6.6 of Annex S-2. |
| MonT, WedT, ThuT and FriT | | Indicators (1 or 0) | A set of indicators whose values are determined pursuant to paragraph 6.5 of Annex S-2. |
| MSID ABSVD (Non Losses) | MSABSVDNKji | MWh | The amount determined in accordance with Annex S-2 paragraph 7.1.6 for Non-MHHS Metering Systems or Annex S-3 paragraph 5.1.6 for MHHS Metering Systems. |
| MSID ABSVD (Losses) | MSABSVDLiNKj | | The data determined by the SVAA in accordance with Annex S-2 paragraph 7.2.6 for Non-MHHS Metering System or Annex S-3 paragraph 5.2.5 for MHHS Metering Systems. |
| MSID Pair Delivered Volume | MPDVj | MWh | MSID Pair Delivered Volume is such volumes of Active Energy notified to the SVAA by the NETSO for the purposes of calculating Non BM Unit ABSVD (SNBABSVDij); or by the Virtual Lead Party for the purposes of aggregating Secondary BM Unit Supplier Delivered Volume (VBMUSDViZj) |
| MSID Pair Lookback Export | | | Means in relation to an MSID Pair and a Settlement Day, the largest Active Export recorded by the SVA Export Metering System in that MSID Pair (if any) in one or more Settlement Periods during the preceding 365 days. |
| MSID Standing Data | | | The data procured by the SVAA where it has confirmed the allocation of an MSID Pair to a Secondary BM Unit and shall include those data items described in Section S11.2.3. |
| Net Differencing Delivered Volume | NDDVj | MWh | has the meaning given to it in Annex S-2 3.11.5 |
| Non-Final Demand Metering System Metered Consumption | SVMMCHZaNLKji | MWh | The quantity determined in accordance with paragraph 7.1.1D of Annex S-2 for Non-MHHS Metering Systems. paragraph 5.1.1F of Annex S-3. |
| Non-Final Demand Metering System Metered Consumption (MHHS) | SVMMCHZNLKji | MWh | The quantity determined in accordance with paragraph paragraph 5.1.1F of Annex S-3 for MHHS Metering Systems. |
| Non-Final Demand Corrected Component | SCORCiNj | MWh | The quantity submitted in accordance with paragraph 13.5.3 of Annex S-2. |
| Net Differencing Delivered Volume | NDDVj | MWh | has the meaning given to it in Annex S-2 3.11.5 |
| Net Differencing Volume | VNDKj | MWh | has the meaning given to it in Annex S-3 5.1.1C. |
| Non Half Hourly Supplier Deemed Take | NHHSDTHZj | MWh | That part of the corrected Supplier Deemed Take associated with those Consumption Component Classes for which the data aggregation type is ‘N’, determined pursuant to paragraph 9.5 of Annex S-2. |
| Non-BM STOR Instruction Volume | NBSVDZaKj | MWh | The estimated volume of demand side Non-BM STOR delivered as determined and notified by the NETSO pursuant to Section S9.2.1. |
| ”Non-Chargeable Consumption (Losses)” | NCCLOSSiNj | MWh | The quantity determined in accordance with paragraph 3.11.3 of Annex S-2 for Non-MHHS Metering Systems or paragraph 3.13.4 of Annex S-3 for MHHS Metering Systems. |
| ”Non-Chargeable Consumption (Non Losses)” | NCCiNj | MWh | The quantity determined in accordance with paragraph 3.11.3 of Annex S-2 for Non-MHHS Meterering Systems of paragraph 3.13.3 of Annex S-3 for MHHS Metering Systems. |
| ”Non-Chargeable Corrected Component” | NCCORCiNj | MWh | The quantity determined in accordance with paragraph 3.11.3 of Annex S-2 for Non- MHHS Metering Systems or paragraph 3.13.5 of Annex S-3 for MHHS Metering Systems. |
| Non-Final AMSID Import | | | Active Import as measured by an AMSID Pair in respect of which an EMR AMSID Declaration is in effect. |
| Non-Final MSID Import | | | Active Import as measured by an Import MSID in respect of which a Non-Final Demand Declaration or EMR MSID Declaration is in effect. |
| Noon Effective Temperature | NETH | °F | A temperature determined pursuant to paragraph 6.5 of Annex S-2. |
| Normal Fraction | NFHPC | Number | The deemed annual Consumption associated with the non-switched load Settlement Registers expressed as a fraction of total annual Consumption for a Switched Load Metering System determined pursuant to paragraph 6.6 of Annex S-2. |
| Normal Register Profile Coefficient | NRPCHPCj | Number | The deemed fraction of annual Consumption for a Switched Load Metering System in a Settlement Period recorded on those meter registers which are 'on' during times when there is no switched load Consumption at such Metering System, determined pursuant to paragraph 6.6 of Annex S-2. |
| Number of Metering Systems Contributing to the Standard Settlement Configuration Estimated Daily Consumption | NMSSCEDCHPCT | Number | The number of non half hourly metering systems for which SPM data was used in determining the Standard Settlement Configuration Estimated Daily Consumption pursuant to paragraph 5.1 of Annex S-2. |
| Number Of Non Half Hourly Metered Metering Systems Requiring A Default Estimated Annual Consumption | NMMDEHZLPR | Number | The number of non half hourly Settlement Registers within metered SVA Metering Systems without either an Annualised Advance or an Estimated Annual Consumption and which therefore require a Default Estimated Annual Consumption to be determined, the value of which is maintained pursuant to Annex S-2. |
| Number Of Non Half Hourly Metered Metering Systems Requiring A Default Estimated Annual Consumption (Disconnected) | NMMDEDHZLPR | Number | The number of non half hourly Settlement Registers within metered SVA Metering Systems without either an Annualised Advance or an Estimated Annual Consumption and which therefore require a Default Estimated Annual Consumption to be determined which were subject to Demand Disconnection, the value of which is maintained pursuant to Annex S-2. |
| Number Of Non Half Hourly Metering Systems Contributing To The Total Annualised Advance | NMAHZLPR | Number | The number of non half hourly Settlement Registers within SVA Metering Systems contributing to the calculation of Total Annualised Advance, the value of which is maintained pursuant to paragraph 4.4 of Annex S-2. |
| Number Of Non Half Hourly Metering Systems Contributing To The Total Estimated Annual Consumption | NMMEHZLPR | Number | The number of non half hourly Settlement Registers within metered SVA Metering Systems contributing to the calculation of Total Estimated Annual Consumption, the value of which is maintained pursuant to paragraph 4.4 of Annex S-2. |
| Number Of Non Half Hourly Metering Systems Contributing To The Total Annualised Advance (Disconnected) | NMADHZLPR | Number | The number of non half hourly Settlement Registers within SVA Metering Systems contributing to the calculation of Total Annualised Advance which were subject to Demand Disconnection, the value of which is maintained pursuant to paragraph 4.5 of Annex S-2. |
| Number Of Non Half Hourly Metering Systems Contributing To The Total Estimated Annual Consumption (Disconnected) | NMMEDHZLPR | Number | The number of non half hourly Settlement Registers within metered SVA Metering Systems contributing to the calculation of Total Estimated Annual Consumption which were subject to Demand Disconnection, the value of which is maintained pursuant to paragraph 4.5 of Annex S-2. |
| Number Of Non Half Hourly Unmetered Metering Systems Contributing To The Total Estimated Annual Consumption | NMUEHZLPR | Number | The number of non half hourly Settlement Registers within Unmetered Supplies contributing to Total Estimated Annual Consumption, the value of which is maintained pursuant to paragraph 4.4 of Annex S-2. |
| Number Of Non Half Hourly Unmetered Metering Systems Contributing To The Total Estimated Annual Consumption (Disconnected) | NMUEDHZLPR | Number | The number of non half hourly Settlement Registers within Unmetered Supplies contributing to Total Estimated Annual Consumption which were subject to Demand Disconnection, the value of which is maintained pursuant to paragraph 4.5 of Annex S-2. |
| Number Of Non Half Hourly Unmetered Metering Systems Requiring A Default Estimated Annual Consumption | NMUDEHZLPR | Number | The number of non half hourly Settlement Registers within Unmetered Metering System without an Estimated Annual Consumption and which therefore require a Default Estimated Annual Consumption to be determined, the value of which is maintained pursuant to paragraph 4.4 of Annex S-2. |
| Number Of Non Half Hourly Unmetered Metering Systems Requiring A Default Estimated Annual Consumption (Disconnected) | NMUDEDHZLPR | Number | The number of non half hourly Settlement Registers within Unmetered Metering System without an Estimated Annual Consumption and which therefore require a Default Estimated Annual Consumption to be determined which were subject to Demand Disconnection, the value of which is maintained pursuant to paragraph 4.5 of Annex S-2. |
| Party-Aggregated Secondary BM Unit Delivered Volume | VLPSDVi2j | MWh | For AMSID Pairs registered in LPAMR, the AMSID Pair Delivered Volumes aggregated by Secondary BM Unit. |
| Party-Aggregated Secondary BM Unit Demand Volume | VLPDVi2j | MWh | For AMSID Pairs registered in LPAMR, the AMSID Pair Demand Volumes adjusted for losses and aggregated by Secondary BM Unit. |
| Period BM Unit Gross Non-Final Demand | SDBMUimj | | The quantity established in accordance with paragraph 13.5.4 of Annex S-2. |
| Period BM Unit Gross Storage Demand | SDBMUimDj | MWh | The quantity submitted in accordance with paragraph 11.4.8 of Annex S-3 for MHHS Metering Systems. |
| Period BM Unit Non Chargeable Demand | NCBMUDij | MWh | The amount determined in accordance with Annex S-2 3.11 for Non-MHHS Metering Systems or Annex S-3 3.13 for MHHS Metering Systems.<br>The Period BM Unit Non Chargeable Demand is the amount of Demand for a BM Unit which has been consumed by Generation or Storage Facility under the conditions of the Generation license which should not be subject to the Final Consumption Levy. |
| Period Profile Class Coefficient | PPCCHPRj | Number | The profile coefficient for a Time Pattern Regime associated with a valid combination of Profile Class and Standard Settlement Configuration determined pursuant to paragraph 6.7 of Annex S-2. |
| Period Time Pattern State Indicator | QRj | Indicator (1 or 0) | An indicator showing for a particular combination of Time Pattern Regime and Standard Settlement Configuration whether the associated Settlement Registers are recording Metered Data, determined pursuant to paragraph 6.4 of Annex S-2. |
| Previous Estimated Annual Consumption | PEACKR | kWh | The value of Estimated Annual Consumption determined pursuant to paragraph 4.3 of Annex S-2. |
| Primary Supplier's Metering System Metered Consumption | PSMMCZ1a1K1j or (where applicable) PSMMCZ1a1.1K1.1j | kWh | The half hourly metered Consumption for a Primary SVA Metering System Number determined pursuant to paragraph 3.5 of Annex S-2. |
| Profile | | | A pattern of Consumption specified over a Settlement Day, or part thereof, on a Settlement Period basis. |
| Profile Class | | | A classification of profiles which represents an exclusive category of customers whose Consumption can be reasonably approximated to a common profile for Settlement purposes. |
| Profile Class Estimated Daily Consumption | PCEDCHPT | kWh | The average Estimated Daily Consumption in respect of a GSP Group, Profile Class, Standard Settlement Configuration and Settlement Day determined pursuant to paragraph 5.1 of Annex S-2. |
| Quarterly Metering Systems by Supplier | NMZqG | Number | The total number of Metering Systems attributed to a Supplier, averaged over a calendar quarter by Supplier Volume Reporting Group, determined pursuant to paragraph 7.1.2 of Annex S-3. |
| Quarterly Supplier Energy Volume | CORCZqG | MWh | The total energy volume attributed to a Supplier, summed over a calendar quarter by Supplier Volume Reporting Group, determined pursuant to paragraph 9A.1.4 of Annex S-2 for Non-MHHS Meterings systems or paragraph 7.1.1 of Annex S-3 for MHHS Metering Systems. |
| Regression Coefficients | RCHQ(nn)j | Various | A set of regression coefficients determined pursuant to paragraph 6.5 of Annex S-2. |
| Replica Settlement Day | | | In relation to a Settlement Day, a Settlement Day having the same attributes as that Settlement Day including any Clock Change. |
| Rounded-Down Duration | RDDR(ai) | minutes | The duration of a period employed in the rounding of Time Pattern Regime data and determined pursuant to paragraph 6.4 of Annex S-2. |
| Rounded-Down Spot Time | | | A spot time associated with a combination of Time Pattern Regimes and Standard Settlement Configuration employed in the rounding of Time Pattern Regime data and determined pursuant to paragraph 6.4 of Annex S-2. |
| Rounded-Up Duration | RUDR(ai) | minutes | The duration of a period employed in the rounding of Time Pattern Regime data and determined pursuant to paragraph 6.4 of Annex S-2. |
| Rounded-Up Spot Time | | | A spot time associated with a combination of Time Pattern Regimes and Standard Settlement Configuration employed in the rounding of Time Pattern Regime data and determined pursuant to paragraph 6.4 of Annex S-2. |
| Secondary BM Unit Delivered Volume | QVBMDi2NLKji | MWh | The quantity determined in accordance with 7.1.1D Annex S-2 with 7.1D Annex S-2 for Non-MHHS Metering System or with 5.1.1D Annex S-3 for MHHS Metering Systems. |
| Secondary BM Unit Demand Volume | VBMUDVi2j | MWh | The quantity is determined in accordance with 9.6.1B Annex S-2 for Non-MHHS Metering Systems or 6.6.3 Annex S-3 for MHHS Metering Systems.<br>The energy volume per Settlement Period for a Secondary BM Unit. |
| Secondary BM Unit Metered Consumption | VBMMCi2aNLKji | MWh | The Secondary BM Unit half hourly metered Consumption, determined by the SVAA pursuant to paragraph 7.1.1C of Annex S-2 or to paragraph 5.1.1C of Annex S-3 for MHHS Metering Systems |
| Secondary BM Unit Supplier Delivered Volume | VBMUSDVi2ji | MWh | The Secondary BM Unit half hourly Supplier Delivered Volumes determined by the SVAA pursuant to paragraph 9.6.1C of Annex S-2 for Non-MHHS Metering Systems or paragraph 6.6.4 of Annex S-3 for MHHS Metering Systems. |
| Secondary Corrected Component | VCORCi2Nj | MWh | The quantity determined in accordance with paragraph 9.3.3 of Annex S-2 for Non-MHHS Metering Systems or paragraph 6.3.4 of Annex S-3 for MHHS Metering Systems.<br>The Consumption for a SVA Metering System allocated to a Secondary BM Unit after the application of the GSP Group Correction. |
| Secondary Corrected Delivered Component | VCORDCi2NKji | MWh | The quantity determined in accordance with paragraph 9.3.4 of Annex S-2 for Non-MHHS Metering Systems or paragraph 6.3.6 of Annex S-3 for MHHS Metering Systems.<br>The Delivered Volumes for a SVA Metering System allocated to a Secondary BM Unit after the application of the GSP Group Correction. |
| Secondary Half Hourly Consumption (Losses) | VLOSSi2Nj | MWh | The quantity determined in accordance with paragraph 7.2.4 of Annex S-2 for Non-MHHS Metering Systems or paragraph 5.2.3 of Annex S-3. for MHHS Metering Systems.<br>The half hourly Consumption for a SVA Metering System allocated to a Secondary BM Unit which is defined as line losses. |
| Secondary Half Hourly Consumption (Non Losses) | Vi2Nj | MWh | The quantity determined in accordance with paragraph 7.1.4 of Annex S-2 for Non-MHHS Metering Systems or paragraph 5.1.4 of Annex S-3 for MHHS Metering Systems.<br>The half hourly Consumption for a SVA Metering System allocated to a Secondary BM Unit which is defined as not being line losses. |
| Secondary Half Hourly Delivered (Losses) | VDLOSSi2NKji | MWh | The quantity determined in accordance with paragraph 7.2.5 of Annex S-2 for Non-MHHS Metering Systems or paragraph 5.2.4 of Annex S-3 for MHHS metering Systems.<br>The half hourly Delivered Volumes for a SVA Metering System allocated to a Secondary BM Unit which is defined as not being line losses. |
| Secondary Half Hourly Delivered (Non Losses) | VDi2NKji | MWh | The quantity determined in accordance with paragraph 7.1.5 of Annex S-2 for Non-MHHS Metering systems or paragraph 5.1.5 of Annex S-3 for MHHS Metering Systems.<br>The half hourly Delivered Volumes for a SVA Metering System allocated to a Secondary BM Unit which is defined as line losses. |
| Secondary Supplier's Metering System Metered Consumption | SSMMCZnanKnj or (where applicable) SSMMCZnan.1Kn.1j | kWh | The half hourly metered Consumption for a Secondary SVA Metering System Number determined pursuant to paragraph 3.5 of Annex S-2 for Non-MHHS Metering Systems. |
| Secondary Supplier's Metering System Metered Consumption (MHHS) | SSMMCZnKnj or (where applicable) SSMMCZn.1Kn.1j | kWh | The half hourly metered Consumption for a Secondary SVA Metering System Number determined pursuant to paragraph 3.6.7 of Annex S-3 for MHHS Metering Systems. |
| Settlement Class | | | For a Supplier a unique combination of Profile Class, Line Loss Factor Class, Time Pattern Regime and Standard Settlement Configuration within a GSP Group provided pursuant to paragraph 5.1.6 of Annex S-2. |
| Settlement Period | j | | A period of thirty minutes beginning on the hour or the half hour and in accordance with paragraph 4.3. |
| Settlement Period Consumption | SPCiHNLkDj | kWh | The quantity submitted in accordance with paragraph 3.7.3 of Annex S-3 for MHHS Metering Systems. |
| Settlement Period Duration | SPD | Hours | 0.5 hours. |
| Settlement Period Quality Indicator | SPQI | | The estimation quality flag set by the Data Service Agent for each UTC Period Level Consumption value. |
| Settlement Register | | | A logical register of a Metering System corresponding to one or more physical active import or active export registers (e.g. totalising meters) and, in the case of SVA Metering Systems not subject to half hourly metering, relating to a single valid combination of Time Pattern Regime and Standard Settlement Configuration. |
| Shared Suppliers' Metering System Metered Consumption | SHMMCZKj | kWh | The half hourly metered Consumption for a SVA Metering System which measures Active Energy that is allocated between a Primary Supplier and the associated Secondary Supplier(s) and which half hourly consumption is determined pursuant to paragraph 3.6 of Annex S-3. |
| Smoothing Parameter | SPAR | Number | A parameter set by the Panel from time to time is used in the determination of the Annualised Advance Adjustment Factor pursuant to paragraph 4.3 of Annex S-2. |
| Specimen Settlement Day | | | In relation to any Settlement Day, a Settlement Day having the same attributes as that Settlement Day other than a Clock Change. |
| Standard Settlement Configuration | | | A standard Metering System configuration recognised by the Supplier Volume Allocation Agent System. |
| Standard Settlement Configuration Estimated Daily Consumption | SSCEDHPCT *[source has a stray backtick after the acronym]* | kWh | The average Estimated Daily Consumption in respect of a GSP Group, Profile Class, Standard Settlement Configuration and Settlement Day determined pursuant to paragraph 5.1 of Annex S-2. |
| Storage Consumption (Losses) | SCLOSSiNDj | MWh | The quantity submitted in accordance with paragraph 11.4.5 of Annex S-3 for MHHS Metering Systems. |
| Storage Consumption (Non Losses) | SCiNDj | MWh | The quantity submitted in accordance with paragraph 11.4.4 of Annex S-3 for MHHS Metering Systems. |
| Sunset Time | SUNT | Minutes | The time duration from the start of the Settlement Day to the time of sunset determined pursuant to paragraph 6.5 of Annex S-2 with reference to the Time of Sunset Data. |
| Sunset Variable | S | Minutes | The number of minutes after 1800 hours GMT that the sun is deemed to set, determined pursuant to paragraph 6.5 of Annex S-2. |
| Supplier BM Unit Non BM ABSVD | SNBABSVDij | MWh | The amount determined in accordance with Annex S-2 paragraph 9.6.1D for Non-MHHS Metering Systems or paragraph Annex S-3 paragraph 6.6.5 for MHHS Metering Systems. |
| Supplier Cap Take | SCTHZj | MWh | The deemed take (active import) at GSP Group level for a SVA Supplier during a Settlement Period pursuant to paragraph 9.7 of Annex S-2 for Non -MHHS Metering Systems or paragraph 6.7 of Annex S-3 for MHHS Metering Systems. |
| Supplier Deemed Take | SDTHZj | MWh | The deemed take at GSP Group level for a SVA Supplier during a Settlement Period determine pursuant to paragraph 9.4 of Annex S-2 for Non-MHHS Metering Sysyems or paragraph 6.4 of Annex S-3 for MHHS Metering Sysyems. |
| Supplier Disconnection Matrix | SDMHZaLPR | | A matrix of data as determined pursuant to paragraph 4.5 of Annex S-2. |
| Supplier Purchase Matrix | SPMHZaLPR | | A matrix of data as determined pursuant to paragraph 4.4 of Annex S-2. |
| Supplier’s Demand Disconnection Volume | SDDHZaNj | MWh | The half hourly Demand Disconnection volume, determined by a Half Hourly Data Aggregator pursuant to paragraph 3.7 of Annex S-2. |
| Supplier’s Demand Disconnection Volume (Losses) | SDDLHZaNj | MWh | The line losses determined by a Half Hourly Data Aggregator as resulting from the Supplier’s Demand Disconnection Volume pursuant to paragraph 3.7 of Annex S-2. |
| Supplier’s Meter Register Consumption | SMRCZaKJj | kWh | The half hourly metered Consumption for a Settlement Register within a SVA Metering System. |
| Supplier’s Metered Consumption | SMCHZaNLj | MWh | The half hourly metered Consumption, determined by a Half Hourly Data Aggregator pursuant to paragraph 3.5 of Annex S-2 for Non-MHHS Metering Systems. |
| Supplier’s Metered Consumption | SMCHZNj | MWh | The metered consumption pursuant to paragraph 3.8.4 of Annex S-3 for MHHS Metering Systems. |
| Supplier’s Metered Consumption (Losses) | SMCLHZaNLj | MWh | The line losses determined by a Half Hourly Data Aggregator as resulting from the Supplier’s Metered Consumption pursuant to paragraph 3.5 of Annex S-2 for Non-MHHS Metering Systems. |
| Supplier’s Metered Consumption (Losses ) | SMCLHZNLj | MWh | The line losses determined as resulting from the Supplier’s Metered Consumption pursuant to paragraph 3.8.5 of Annex S-3 for MHHS Metering Systems. |
| Supplier’s Metering System Metered Consumption | SMMC ZaKj | kWh | The half hourly metered Consumption for a SVA Metering System, determined pursuant to paragraph 3.5 of Annex S-2 for Non-MHHS Metering Systems. |
| Supplier’s Metering System Metered Consumption | SMMCZKj | kWh | The metered Consumption for a SVA Metering System, determined pursuant to paragraph 3.5 of Annex S-3 for MHHS Metering Systems. |
| Switched Fraction | SWFHPC | Number | The deemed proportion of Consumption for a Switched Load Metering System which is switched load determined pursuant to paragraph 6.6 of Annex S-2. |
| Switched Load Metering System | | | A Metering System which has a Profile Class classified as Economy 7 and/or such other classification as may be agreed from time to time by the Panel. |
| Switched Load Profile Coefficient | SLPHPCj | Number | A number determined pursuant to paragraph 6.6 of Annex S-2 and representing the fraction of annual Consumption in a given Settlement Period for a particular switched load profile. |
| Switched Load State Indicator | SQCj | Indicator (1 or 0) | An indicator showing if any Time Pattern Regime associated with a switched load within a Standard Settlement Configuration is recording Metered Data in a given Settlement Period, determined pursuant to paragraph 6.6 of Annex S-2. |
| Teleswitch Contact | | | One of the logical contacts within each teleswitched meter. |
| Teleswitch Contact Interval Data | | | In respect of a Teleswitch Group, the state of a particular Teleswitch Contact within all Metering Systems within such Teleswitch Group at the start of a UTC Day and, for each following change of state of such contact, the new state of such contact and the time in Co-ordinated Universal Time of such change of state. |
| Teleswitch Contact Rule | | | The relationship between a Teleswitch Contact and a Teleswitch Register Rule which is notified by a Supplier pursuant to paragraph 5.1.1 of Annex S-2. |
| Teleswitch Group | | | A group of Metering Systems which are controlled by the same teleswitch messages which messages are under the control of a particular person. |
| Teleswitch Interval | | | A period during which the Settlement Registers associated with a Teleswitch Time Pattern Regime are recording metered consumption and which is determined pursuant to paragraph 6.2 of Annex S-2. |
| Teleswitch Regime Indicator | | Indicator | An indicator indicating whether a Settlement Register is associated with a Time Pattern Regime provided pursuant to paragraph 5.1.5 of Annex S-2. |
| Teleswitch Register Rule | | | A rule defining when the Settlement Registers associated with a Teleswitch Time Pattern Regime are recording metered consumption which is notified by a Supplier pursuant to paragraph 5.1.1 of Annex S-2. |
| Teleswitch Time Pattern Regime | | | A Time Pattern Regime associated with a teleswitched Standard Settlement Configuration in a particular Teleswitch Group. |
| Threshold Parameter | TP | Number | A parameter set by the Panel from time to time and used in the determination of the Default Estimated Annual Consumption pursuant to paragraph 4.4 of Annex S-2. |
| Time of Sunset | | Time | A set of data supplied to the Supplier Volume Allocation Agent pursuant to paragraph 5.1.6 of Annex S-2. *[source reads "Time of Sunset Time A set of data …"; the cell split is inferred, and "Sunset Time" above refers to "Time of Sunset Data"]* |
| Time Pattern Regime | | | A pattern of switching behaviour through time that determines when a Settlement Register is or is not recording Metered Data provided pursuant to paragraph 5.1.5 of Annex S-2. |
| Time Pattern Regime Estimated Annual Consumption | TPREACHPR | kWh | The average Estimated Annual Consumption in respect of a GSP Group, Profile Class, Standard Settlement Configuration and Time Pattern Regime determined pursuant to paragraph 5.1 of Annex S-2. |
| Time Pattern Regime Estimated Daily Consumption | TPREDCHPRT | kWh | The average Estimated Daily Consumption in respect of a GSP Group, Profile Class, Standard Settlement Configuration, Time Pattern Regime and Settlement Day determined pursuant to paragraph 5.1 of Annex S-2. |
| Timeswitch Regime Indicator | | Indicator | An indicator indicating whether a Settlement Register is associated with a Time Pattern Regime provided pursuant to paragraph 5.1.5 of Annex S-2. |
| Total Annualised Advance | TAAHZLPR | MWh | The total of all the Annualised Advances for a Supplier in MWh and in respect of a Profile Class, Line Loss Factor Class, Time Pattern Regime and GSP Group determined pursuant to paragraph 4.4 of Annex S-2. |
| Total Annualised Advance (Disconnected) | TAADHZLPR | MWh | The total of all the Annualised Advances for a Supplier in MWh and in respect of a Profile Class, Line Loss Factor Class, Time Pattern Regime and GSP Group which were subject to Demand Disconnection, determined pursuant to paragraph 4.5 of Annex S-2. |
| Total Estimated Annual Consumption For Non Half Hourly Metered Metering Systems | MEHZLPR | KWh | The sum of Estimated Annual Consumption for non half hourly metered SVA Metering Systems calculated pursuant to paragraph 4.4 of Annex S-2. |
| Total Estimated Annual Consumption For Non Half Hourly Metered Metering Systems (Disconnected) | MEDHZLPR | kWh | The sum of Estimated Annual Consumption for non half hourly metered SVA Metering Systems which were subject to Demand Disconnection, determined pursuant to paragraph 4.5 of Annex S-2. |
| Total Metered Estimated Annual Consumption | TMEACHZLPR | MWh | The total metered annual Consumption for a SVA Supplier and in respect of a Profile Class, Line Loss Factor Class, Time Pattern Regime and GSP Group, determined pursuant to paragraph 4.4 of Annex S-2. |
| Total Metered Estimated Annual Consumption (Disconnected) | TMEACDHZLPR | MWh | The total metered annual Consumption for a SVA Supplier subject to Demand Disconnection and in respect of a Profile Class, Line Loss Factor Class, Time Pattern Regime and GSP Group, determined pursuant to paragraph 4.5 of Annex S-2. |
| Total Metering System Delivered Volume | TQVMDKj | MWh | The quantity determined in accordance with paragraph 3.10.2 of Annex S-2 for Non-MHHS Metering Systems or paragraph 3.12.6 of Annex S-3 for MHHS Metering Systems. |
| Total Number Of Metered Non Half Hourly Metering Systems Contributing To Total Metered Estimated Annual Consumption | TMEACCHZLPR | Number | The number of metered non half hourly Settlement Registers within SVA Metering Systems contributing to the calculation of Total Metered Estimated Annual Consumption the value of which is maintained pursuant to paragraph 4.4 of Annex S-2. |
| Total Number Of Metered Non Half Hourly Metering Systems Contributing To Total Metered Estimated Annual Consumption (Disconnected) | TMEACCDHZLPR | Number | The number of metered non half hourly Settlement Registers within SVA Metering Systems contributing to the calculation of Total Metered Estimated Annual Consumption which were subject to Demand Disconnection, the value of which is maintained pursuant to paragraph 4.5 of Annex S-2. |
| Total Number Of Non Half Hourly Unmetered Metering Systems Contributing To Total Unmetered Consumption | TMUECHZLPR | Number | The number of non half hourly Settlement Registers within Unmetered Supplies contributing to the calculation of Total Unmetered Consumption the value of which is maintained pursuant to paragraph 4.4 of Annex S-2. |
| Total Number Of Non Half Hourly Unmetered Metering Systems Contributing To Total Unmetered Consumption (Disconnected) | TMUECDHZLPR | Number | The number of non half hourly Settlement Registers within Unmetered Supplies contributing to the calculation of Total Unmetered Consumption which were subject to Demand Disconnection, the value of which is maintained pursuant to paragraph 4.5 of Annex S-2. |
| Total Unmetered Consumption | TUEHZLPR | MWh | The total unmetered annual Consumption for a SVA Supplier and in respect of a Profile Class, Line Loss Factor Class, Time Pattern Regime and GSP Group, determined pursuant to paragraph 4.4 of Annex S-2. |
| Total Unmetered Consumption (Disconnected) | TUEDHZLPR | MWh | The total unmetered annual Consumption for a SVA Supplier subject to Demand Disconnection and in respect of a Profile Class, Line Loss Factor Class, Time Pattern Regime and GSP Group, determined pursuant to paragraph 4.5 of Annex S-2. |
| Unadjusted Annual Fraction of Consumption | UAFYCHPR | | An estimate of the fraction of the total average consumption of a multi-register Standard Settlement Configuration attributable to each Time Pattern Regime of that Standard Settlement Configuration, prior to adjustment for rounding errors, determined pursuant to paragraph 5.1 of Annex S-2. |
| Unadjusted Interval | | | A period of time beginning at an Unadjusted Interval Start Time and ending at its associated Unadjusted Interval End Time, determined pursuant to paragraph 6.4 of Annex S-2. |
| Unadjusted Interval End Time | UIETX(ai) | | A time associated with a particular Time Pattern Regime determined pursuant to paragraph 6.4 of Annex S-2. |
| Unadjusted Interval Start Time | UISTX(ai) | | A time associated with a particular Time Pattern Regime determined pursuant to paragraph 6.4 of Annex S-2. |
| Unrounded Duration | UDX(ai) | Minutes | The time duration of an Unadjusted Interval determined pursuant to paragraph 6.4 of Annex S-2. |
| Upper Trading Eligibility Threshold | | | [10] MW multiplied by the Settlement Period Duration. |
| Value Of Estimated Annual Consumption For Non Half Hourly Unmetered Metering Systems | UEHZLPR | KWh | The value of Estimated Annual Consumption for non half hourly Settlement Registers within Unmetered Supplies, the value of which is maintained pursuant to paragraph 4.4 of Annex S-2. |
| Value Of Estimated Annual Consumption For Non Half Hourly Unmetered Metering Systems (Disconnected) | UEDHZLPR | kWh | The value of Estimated Annual Consumption for non half hourly Settlement Registers within Unmetered Supplies which were subject to Demand Disconnection, the value of which is maintained pursuant to paragraph 4.5 of Annex S-2. |
| Weighted Export | WEHj | MWh | The quantity submitted in accordance with paragraph 6.2.1 of Annex S-3 for MHHS Metering Systems. |
| Weighted Import | WIHj | MWh | The quantity submitted in accordance with paragraph 6.2.1 of Annex S-3 for MHHS Metering Systems. |

## Table X–7 – List of Acronyms Applicable to Section S

This table provides a list of the acronyms defined in Table X-6, presented in alphabetical order of the acronym name.

| Acronym | Corresponding Defined Term or Expression |
|---|---|
| AAAFKR | Annualised Advance Adjustment Factor |
| AAFYCHPC | Alternative Average Fraction of Yearly Consumption |
| AAKR | Annualised Advance |
| ABDDiaNLKj | Allocated BM Unit’s Demand Disconnection Volume |
| ABMMMC iaNLKj | Allocated BM Unit's Metering System Metered Consumption |
| ADBPEDi | “AMSID Declaration Boundary Point Export” |
| ADBPIDj | “AMSID Declaration Boundary Point Import” |
| ADGEDj | “AMSID Declaration Generation Export” |
| ADGIDj | “AMSID Declaration Generation Import” |
| ADNCPDj | “AMSID Declaration Non-Chargeable Proportion” |
| AFYCAHPC | Annual Fraction of Yearly Consumption Adjustment |
| AFYCHPR | Average Fraction Of Yearly Consumption |
| AMPDVj | AMSID Pair Delivered Volume |
| AQVMDNLKji | ABSVD BM Unit Delivered Volume |
| ASDDHZaNLKj | Allocated Supplier’s Demand Disconnection Volume |
| ASMMCHZaNLKj | Allocated Supplier’s Metering System Metered Consumption |
| AVMMCHZaNLKji | Allocated Metering System Metered Consumption |
| BAPHQj | Baseload Profile Coefficient |
| BFHPC | Base Fraction |
| BEVji | Baselined Expected Volumes |
| BMDDiaNj | BM Unit’s Demand Disconnection Volume |
| BMDDLiaNj | BM Unit’s Demand Disconnection Volume (Losses) |
| BMDMiaLPR | BM Unit Disconnection Matrix |
| BMMC iaNLj | BM Unit's Metered Consumption |
| BMMCL iaNLj | BM Unit's Metered Consumption (Losses) |
| BMPC iLPRj | BM Unit's Profiled Consumption |
| BMPDiLPRj | BM Unit’s Profiled Disconnection |
| BMPM iaLPR | BM Unit Purchase Matrix |
| BMUADDVij | BM Unit Allocated Demand Disconnection Volume |
| BMUADVij | BM Unit Allocated Demand Volume |
| CFHj | GSP Group Correction Factor |
| CiN(c)Pj | Half Hourly Consumption (Non Losses) by Profile Class |
| CiNj | Half Hourly Consumption (Non Losses) |
| CLOSSiN(c)Pj | Half Hourly Consumption (Losses) by Profile Class |
| CLOSSiNj | Half Hourly Consumption (Losses) |
| CORCiN(c)Pj | Corrected Component by Profile Class |
| CORCiNj | Corrected Component |
| CORCZqG | Quarterly Supplier Energy Volume |
| CORDCiNj | Corrected Disconnection Component |
| DDDPCHPKRT | Demand Disconnection Daily Profile Coefficient |
| DEMHZLPR | Default Estimated Annual Consumption For Metered Metering Systems |
| DEUHZLPR | Default Estimated Annual Consumption For Unmetered Metering Systems |
| DiNj | Half Hourly Disconnection (Non Losses) |
| DLOSSiNj | Half Hourly Disconnection (Losses) |
| DMAKR | Deemed Meter Advance |
| DPCHPRT | Daily Profile Coefficient |
| DPCHPRT | Historical Daily Profile Coefficient |
| EACKR | Estimated Annual Consumption |
| FYCKR | Fraction Of Yearly Consumption |
| GAACHQ | Group Average Annual Consumption |
| GCHNj | GSP Group Half Hourly Consumption |
| GGPCAEACHPC | GSP Group Profile Class Average Estimated Annual Consumption |
| GGPCDEACHP | GSP Group Profile Class Default Estimated Annual Consumption |
| HDDKj | Half Hourly Demand Disconnection Volume |
| HHPC | Low Fraction Consumption |
| ITAADHZLPR | Initial Total Annualised Advance (Disconnected) |
| K1HPC | |
| K2HPC | |
| LLFLj | Line Loss Factor |
| LOWFHPC | Low Fraction |
| LRPCHPCj | Low Register Profile Coefficient |
| MADVKR | Meter Advance |
| MAP | Meter Advance Period |
| MEDHZLPR | Total Estimated Annual Consumption For Non Half Hourly Metered Metering Systems (Disconnected) |
| MKj | Metering System Period Disconnection Duration |
| MPDVj | MSID Pair Delivered Volume |
| MRCQ(aa)(nn)j | Matrix Of Regression Coefficients |
| MSABSVDLHZLKj | MSID ABSVD (Losses) |
| MSABSVDNKji | MSID ABSVD (Non Losses) |
| MBVKiLj | MSID Baseline Value |
| MBLKiLj | MSID Baseline Losses |
| NBSVDZaKj | Non-BM STOR Instruction Volume |
| NDDVj | Net Differencing Delivered Volume |
| NETH | Noon Effective Temperature |
| NCBMUDij | Period BM Unit Non Chargeable Demand |
| NCCiNj | Non-Chargeable Consumption (Non Losses) |
| NCCLOSSiNj | Non-Chargeable Consumption (Losses) |
| NCCORCiNj | Non-Chargeable Corrected Component |
| NCMCiNLKj | Metering System Non-Chargeable Consumption |
| NCMLiNLKj | Metering System Non-Chargeable Losses” for an EMR MSID Declaration |
| NFHPC | Normal Fraction |
| NHHSDTHZj | Non Half Hourly Supplier Deemed Take |
| NMADHZLPR | Number Of Non Half Hourly Metering Systems Contributing To The Total Annualised Advance (Disconnected) |
| NMAHZLPR | Number Of Non Half Hourly Metering Systems Contributing To The Total Annualised Advance |
| NMMDEDHZLPR | Number Of Non Half Hourly Metered Metering Systems Requiring A Default Estimated Annual Consumption (Disconnected) |
| NMMDEHZLPR | Number Of Non Half Hourly Metered Metering Systems Requiring A Default Estimated Annual Consumption |
| NMMEDHZLPR | Number Of Non Half Hourly Metering Systems Contributing To The Total Estimated Annual Consumption (Disconnected) |
| NMMEHZLPR | Number Of Non Half Hourly Metering Systems Contributing To The Total Estimated Annual Consumption |
| NMSSCEDCHPCT | Number of Metering Systems Contributing to the Standard Settlement Configuration Estimated Daily Consumption |
| NMUDEDHZLPR | Number Of Non Half Hourly Unmetered Metering Systems Requiring A Default Estimated Annual Consumption (Disconnected) |
| NMUDEHZLPR | Number Of Non Half Hourly Unmetered Metering Systems Requiring A Default Estimated Annual Consumption |
| NMUEDHZLPR | Number Of Non Half Hourly Unmetered Metering Systems Contributing To The Total Estimated Annual Consumption (Disconnected) |
| NMUEHZLPR | Number Of Non Half Hourly Unmetered Metering Systems Contributing To The Total Estimated Annual Consumption |
| NMZqG | Quarterly Metering Systems by Supplier |
| NRPCHPCj | Normal Register Profile Coefficient |
| ORABSVDCi2Nj | Corrected MSID ABSVD Component |
| PCEDCHPT | Profile Class Estimated Daily Consumption |
| PEACKR | Previous Estimated Annual Consumption |
| PHQj | Basic Period Profile Coefficient |
| PPCCHPRj | Period Profile Class Coefficient |
| PSEVji | Party Submitted Expected Volume |
| PSMMCZ1a1.1K1.1j | Primary Supplier's Metering System Metered Consumption for Secondary SVA Metering System Number K1.1 |
| PSMMCZ1a1K1j | Primary Supplier's Metering System Metered Consumption for Secondary SVA Metering System Number K1 |
| QRj | Period Time Pattern State Indicator |
| QVBMDi2NLKji | Secondary BM Unit Delivered Volume |
| QVMDKj | Metering System Delivered Volume |
| RCHQ(nn)j | Regression Coefficients |
| RDDR(ai) | Rounded-Down Duration |
| RUDR(ai) | Rounded-Up Duration |
| S | Sunset Variable |
| SCiNj | Half Hourly Non-Final Demand Consumption (Non Losses) |
| SCLOSSiNj | Half Hourly Non-Final Demand Consumption (Losses) |
| SCORCiNj | Non-Final Demand Corrected Component |
| SDDHZaNj | Supplier’s Demand Disconnection Volume |
| SDDLHZaNj | Supplier’s Demand Disconnection Volume (Losses) |
| SDMHZaLPR | Supplier Disconnection Matrix |
| SDTHZj | Supplier Deemed Take |
| SEVji | Settlement Expected Volume |
| SHSMMCZaKj | Shared Suppliers' Metering System Metered Consumption |
| SIX_PM | |
| SLPHPCj | Switched Load Profile Coefficient |
| SMCHZaNLj | Supplier's Metered Consumption |
| SMCLHZaNLj | Supplier’s Metered Consumption (Losses) |
| SMMC ZaKj | Supplier’s Metering System Metered Consumption |
| SMRCZaKJj | Supplier’s Meter Register Consumption |
| SNBABSVDij | Supplier BM Unit Non BM ABSVD |
| SPAR | Smoothing Parameter |
| SPD | Settlement Period Duration |
| SPMHZaLPR | Supplier Purchase Matrix |
| SQCj | Switched Load State Indicator |
| SSCEDHPCT | Standard Settlement Configuration Estimated Daily Consumption |
| SSMMCZnan.1Kn.1j | Secondary Supplier's Metering System Metered Consumption for Secondary SVA Metering System Number Kn.1 |
| SSMMCZnanKnj | Secondary Supplier's Metering System Metered Consumption for Secondary SVA Metering System Number Kn |
| SUNT | Sunset Time |
| SVMMCHZaNLKji | Non-Final Demand Metering System Metered Consumption |
| SWFHPC | Switched Fraction |
| TAADHZLPR | Total Annualised Advance (Disconnected) |
| TAPDVj | Total AMSID Pair Delivered Volume |
| THT | Grid Supply Point Group Measured Temperature |
| TMEACCDHZLPR | Total Number Of Metered Non Half Hourly Metering Systems Contributing To Total Metered Estimated Annual Consumption (Disconnected) |
| TMEACDHZLPR | Total Metered Estimated Annual Consumption (Disconnected) |
| TMPDVj | Total MSID Pair Delivered Volume |
| TMUECDHZLPR | Total Number Of Non Half Hourly Unmetered Metering Systems Contributing To Total Unmetered Consumption (Disconnected) |
| TQVMDKj | Total Metering System Delivered Volume |
| TPREACHPR | Time Pattern Regime Estimated Annual Consumption |
| TPREDCHPRT | Time Pattern Regime Estimated Daily Consumption |
| TUEDHZLPR | Total Unmetered Consumption (Disconnected) |
| UAFYCHPR | Unadjusted Annual Fraction of Consumption |
| UEDHZLPR | Value Of Estimated Annual Consumption For Non Half Hourly Unmetered Metering Systems (Disconnected) |
| VBMMCi2aNLKji | Secondary BM Unit Metered Consumption |
| VBMUDVi2j | Secondary BM Unit Demand Volume |
| VBMUSDVi2ji | Secondary BM Unit Supplier Delivered Volume |
| VCORCi2Nj | Secondary Corrected Component |
| VCORDCi2NKji | Secondary Corrected Delivered Component |
| VDi2NKji | Secondary Half Hourly Delivered (Non Losses) |
| VDLOSSi2NKji | Secondary Half Hourly Delivered (Non Losses) |
| Vi2Nj | Secondary Half Hourly Consumption (Non Losses) |
| VLOSSi2Nj | Secondary Half Hourly Delivered (Losses) |
| VLPDVi2j | Party-Aggregated Secondary BM Unit Demand Volume |
| VLPSDVi2j | Party-Aggregated Secondary BM Unit Delivered Volume |
| VMMCHZaNLKji | Metering System Metered Consumption |
| WTN | GSP Group Correction Scaling Weight |
| yHQj | Estimated Regional Average Demand Per Customer |

*[As in the source, Table X-7 does not always match Table X-6: e.g. ORABSVDCi2Nj (Table X-6: CORABSVDCi2Nj), SHSMMCZaKj (Table X-6: SHMMCZKj), MSABSVDLHZLKj (Table X-6: MSABSVDLiNKj), yHQj (Table X-6: YHQj), and the labels of VDLOSSi2NKji and VLOSSi2Nj differ from Table X-6. BEVji, MBVKiLj, MBLKiLj, PSEVji and SEVji have no Table X-6 entry. K1HPC, K2HPC and SIX_PM have no expression in either table.]*

## Table X-8 – List of Valid Consumption Component Classes

The list of valid Consumption Component Classes shall be determined from Market Domain Data for Non-MHHS Metering Systems and Industry Standing Data for MHHS Metering Systems.

## Table X–9

List of Supplier Volume Reporting Groups and associated relationships used for the purposes of the Supplier Quarterly Volume Report determined according to paragraph 9A of Annex S-2:

| Supplier Volume Reporting Group | Consumption Component Classes | Profile Classes (where used and/or applicable) |
|---|---|---|
| 1 | 17, 18, 20, 21 | 1, 2 |
| 2 | 17, 18, 20, 21 | 3, 4 |
| 3 | 17, 18, 20, 21 | 5, 6, 7, 8 |
| 4 | 19, 22 | Not used |
| 5 | 32, 33, 34, 35 | Not used |
| 6 | 1, 3, 4, 9, 11, 12, 23, 25, 26, 28, 30, 31, 42, 43, 44, 45, 46, 47, 54, 55, 56, 57, 58, 59 | Not applicable |
| 7 | 2, 5, 10, 13 | Not applicable |
| 8 | 6, 7, 8, 14, 15, 16, 36, 37, 38, 39, 40, 41, 48, 49, 50, 51, 52, 53, 60, 61, 62, 63, 64, 65 | Not applicable |

For the Supplier Quarterly Volume Report as set out in paragraph 4.2.10 of Section V, the Supplier Volume Reporting Groups with the numbers in the far left column of the table above shall be given the following descriptive labels in the actual report:

1. "Non half hourly metered import, Profile Classes 1 and 2";
2. "Non half hourly metered import, Profile Classes 3 and 4";
3. "Non half hourly metered import, Profile Classes 5, 6, 7 and 8";
4. "Non half hourly unmetered import";
5. "Non half hourly metered export";
6. "Half hourly metered import";
7. "Half hourly unmetered import"; and
8. "Half hourly metered export".

---

## AMENDMENT RECORD – SECTION X-2

Section X-2 Version 62.0 Effective Date: 29 October 2026

| Modification Proposal | Decision Date | Implementation Date | Version |
|---|---|---|---|
| P508 | 10/07/2026 | 29/10/2026 | 62.0 |
| P511 | 10/08/2026 | 24/08/2026 | 61.0 |
| P483 | 21/08/25 | 27/11/25 | 60.0 |
| P444 | 04/04/25 | 06/11/25 | 59.0 |
| P478 | 06/11/24 | 22/09/25 | 58.0 |
| P442 | 08/02/24 | 27/02/25 | 57.0 |
| P473 | 17/09/24 | 07/11/24 | 56.0 |
| P415 | 06/10/23 | 07/11/24 | 56.0 |
| P455 | 09/05/24 | 24/09/24 | 55.0 |
| P395 | 06/10/22 | 02/11/23 | 54.0 |
| P450 | 12/01/23 | 23/02/23 | 53.0 |
| P419 | 25/04/22 | 23/02/23 | 53.0 |
| P376 | 06/08/21 | 23/02/23 | 53.0 |
| P448 | 23/11/22 | 07/12/22 | 52.0 |
| P433 Self Governance | 13/01/22 | 30/06/22 | 51.0 |
| P375 | 24/02/21 | 30/06/22 | 51.0 |
| P418 | 03/02/21 | 01/04/21 | 50.0 |
| P383 | 28/02/20 | 01/04/21 | 50.0 |
| P408 Self-Governance | 09/07/20 | 02/02/21 | 49.0 |
| P388 Self-Governance | 08/08/19 | 01/04/20 | 48.0 |
| P354 | 18/06/18 | 01/04/20 | 48.0 |
| P394 | 12/12/19 | 27/02/20 | 47.0 |
| P386 Self-Governance | 13/06/19 | 07/11/19 | 46.0 |
| P367 Self-Governance | 14/06/18 | 27/06/19 | 45.0 |
| P369 | 24/09/18 | 29/03/19 | 44.0 |
| P344 | 24/08/18 | 28/02/19 | 43.0 |
| P373 (Nullification of P297) | 22/02/19 | 27/02/19 | 43.0 |
| P297 (Nullified by P373) | 28/04/14 | 01/11/18 | 43.0 |
| P350 | 24/03/17 | 01/04/18 | 42.0 |
| P357 | 13/12/17 | 22/02/18 | 41.0 |
| P321 Self Governance | 08/10/15 | 29/06/17 | 40.0 |
| P347 | 19/01/17 | 01/04/17 | 39.0 |
| P339 Self-Governance | 08/12/16 | 01/04/17 | 39.0 |
| P346 Self-Governance | 10/11/16 | 01/04/17 | 39.0 |
| P326 Self-Governance Alternative | 14/04/16 | 23/02/17 | 38.0 |
| P315 Alternative | 20/10/15 | 30/06/16 | 37.0 |
| P328 | 12/11/15 | 16/11/15 | 36.0 |
| P305 | 02/04/15 | 05/11/15 | 35.0 |
| P300 | 15/10/14 | 05/11/15 | 35.0 |
| P276 | 20/07/12 | 31/03/14 | 34.0 |
| P273 Self-Governance | 23/02/12 | 23/02/12 | 33.0 |
| P253 | 18/11/10 | 03/11/11 | 32.0 |
| P243 | 20/01/10 | 04/11/10 | 31.0 |
| P261 | 02/08/10 | 09/08/10 | 30.0 |
| P239 | 21/09/09 | 05/11/09 | 29.0 |
| P232 | 25/06/09 | 05/11/09 | 29.0 |
| P217 | 18/10/08 | 05/11/09 | 29.0 |
| P233 | 19/05/09 | 25/06/09 | 28.0 |
| P215 | 23/04/08 | 25/06/09 | 28.0 |
| P216 | 24/04/08 | 20/04/09 | 27.0 |
| P225 | 07/08/08 | 06/11/08 | 26.0 |
| P220 | 02/04/08 | 06/11/08 | 26.0 |
| P219 | 02/04/08 | 06/11/08 | 26.0 |
| P208 | 16/01/07 | 22/02/07 | 25.0 |
| P194 | 23/02/06 | 02/11/06 | 24.0 |
| P176 | 10/05/05 | 03/11/05 | 23.0 |
| P172 | 29/04/05 | 06/05/05 | 22.0 |
| ADN003 | 11/03/05 | 01/04/05 | 21.0 |
| ORD002 | 01/04/05 | 01/04/05 | 21.0 |
| P179 | 09/02/05 | 23/02/05 | 20.0 |
| P124 | 18/05/04 | 01/12/04 | 19.0 |
| P98 | 18/08/03 | 08/11/04 | 18.0 |
| P131 | 05/04/04 | 03/11/04 | 17.0 |
| P160 | 30/07/04 | 13/08/04 | 16.0 |
| P125<br>Removed by P165 | 08/08/03 | 01/05/04 | 15.0 |
| P165<br>Removed P125 | 14/04/04 | 28/04/04 | 15.0 |
| P130 | 29/08/03 | 20/01/04 | 15.0 |
| P81 | 17/12/02 | 28/09/03 | 14.0 |
| P62 | 12/08/02 | 01/08/03 | 13.0 |
| P78 | 09/09/02 | 11/03/03 | 12.0 |
| P71 | 22/11/02 | 11/03/03 | 12.0 |
| P101 | 02/01/03 | 23/01/03 | 11.0 |
| P68 | 24/07/02 | 01/11/02 | 10.0 |
| P86 | 23/09/02 | 30/09/02 | 9.0 |
| P33 | 07/12/01 | 30/09/02 | 9.0 |
| P2 | 16/10/01 | 30/09/02 | 9.0 |
| P12 | 10/05/02 | 02/07/02 | 8.0 |
| P46 | 14/05/02 | 22/05/02 | 7.0 |
| P37 | 10/05/02 | 20/05/02 | 6.0 |
| P22 | 07/12/01 | 01/04/02 | 5.0 |
| P67 | 01/03/02 | 08/03/02 | 4.0 |
| P18 | 22/08/01 | 25/09/01 | 3.0 |
| P8 | 24/09/01 | 25/09/01 | 3.0 |
| P10 | 14/05/01 | 11/05/01 | 2.0 |

---

## Notation guide for writing new equations *[editorial – not part of the BSC]*

This section explains how to write new equations, for example for consistent asset allocation, in the same notation as the Code. It only restates the rules in paragraphs 1.2, 2.6, 3.3 and 4 and Tables X-1, X-4 and X-5.

### Reading a run-together acronym

A BSC variable is an upper-case base name followed by its indices. Indices are written straight after the name in the order the Code uses, with no separators. The base name is usually the acronym's upper-case letters, and the indices are the lower-case letters (plus the upper-case Section S indices such as H, Z, N, L, K, J from Table X-4).

| Source form | Base | Indices (meaning) | LaTeX |
|---|---|---|---|
| QMij | QM | i BM Unit, j Settlement Period | `QM_{ij}` |
| QMFRziaj | QMFR | z Metered Volume Reallocation Notification, i BM Unit, a Energy Account, j Settlement Period | `QMFR_{ziaj}` |
| fFPNijt | FPN | preceding superscript f (Point Value Identification Number); i, j; spot time t | `{}^{f}FPN_{ijt}` |
| FPNij(t) | FPN | i, j; function of spot time t | `FPN_{ij}(t)` |
| AMRCKJj | AMRC | K Asset Metering System, J Settlement Register, j Settlement Period | `AMRC_{KJj}` |
| SMRCZaKJj | SMRC | Z Supplier, a Data Aggregator, K SVA Metering System, J Settlement Register, j Settlement Period | `SMRC_{ZaKJj}` |
| VBMMCi2aNLKji | VBMMC | i2 Secondary BM Unit, a, N Consumption Component Class, L Line Loss Factor Class, K, j, i | `VBMMC_{i2aNLKji}` |

An example already in this folder (*BSC Section S Annex S-2 Supplier Volume Allocation Rules V35.0*) puts these together:

AMMCKj= ΣKJ AMRCKJj

```math
AMMC_{Kj} = \sum_{KJ} AMRC_{KJj}
```

### Index letters that mean different things inside and outside Section S

Outside Section S, Table X-1 applies; inside Section S, Table X-4 applies (paragraphs 2.1.1 and 3.1.1). Several letters change meaning between the two:

| Letter | Outside Section S (Table X-1) | Section S (Table X-4) |
|---|---|---|
| a | Energy Account / Virtual Balancing Account | Data Aggregator |
| H | Higher of two Point Value Identification Numbers f (preceding superscript) | GSP Group |
| L | Lower of two Point Value Identification Numbers f (preceding superscript) | Line Loss Factor Class |
| N | Node | Consumption Component Class |
| q | Order number of a Ranked Bid Volume or Ranked Offer Volume | Calendar quarter |
| S | BSC Season | *[not listed]* |
| T / t | t = STOR Action Number (and spot time, paragraph 4.4.2) | T = Settlement Day |
| Z | Zone | Supplier |
| d / D | d = Day | D = Settlement Day (also Settlement Day in UTC) |
| K | *[not listed]* | SVA Metering System Number and/or Asset Metering System; Metering System of an SVA Non-Final Demand Facility |

i (BM Unit) and j (Settlement Period) mean the same in both; Section S adds i2 for a Secondary BM Unit.

### Other conventions to carry over

- **Multiplication** is written `*` (1.2.1(a)); **membership** as ∈, e.g. a∈p, j∈D (1.2.1(b)).
- **min / max** follow the rule in 1.2.1(e): min picks the most negative value (or, with no negatives, the smallest positive); max picks the largest positive value (or, with no positives, the negative value of smallest magnitude).
- **Zero** counts as a positive whole number (1.2.1(c)).
- **Summations** put the summed indices on Σ (2.6.1). A restricted range is written Σd∈R, or as plain Σd defined in context (2.6.2, 2.6.3). In Section S, use the named summations in Table X-5, e.g. ΣKNonDiff and ΣKDiff for Asset Metering Systems allocated under S10.1A.2(e)(i) and (ii).
- **Sign convention:** outside Section S, Active Energy is positive when delivered to the Total System and negative when off-taken (2.4.1). In Section S, metered data are held as magnitudes, except BM Unit Allocated Demand Volume, which is positive for offtake (3.7).
- **Time:** spot times carry t; Period variables are the integral of F(t) over Settlement Period j (4.6.1). Section S uses the linear interpolation in 3.6.2, while other Sections use the point-variable interpolation in 4.5.4.
