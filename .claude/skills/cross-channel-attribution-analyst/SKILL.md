---
name: cross-channel-attribution-analyst
description: Analyzes customer journeys across marketing channels to understand true channel contribution. Triggers when user asks about attribution, channel ROI, "which channel is really working?", or wants to understand multi-touch journeys. Compares attribution models, identifies undervalued channels, and recommends budget reallocation based on actual impact.
---

# Cross-Channel Attribution Analyst

Understand which channels truly drive conversions—not just which ones get the credit.

## Core Philosophy

**Last-click is lying to you.** The channel that gets the conversion credit often isn't the one that did the heavy lifting. A customer might discover you through organic search, research you via paid ads, and finally convert through a branded search—but last-click gives all credit to brand.

**The Goal:** Uncover the true contribution of each channel so you invest in what actually drives growth.

**The Principle:** Multi-touch analysis reveals the full customer journey, exposing channels that initiate, assist, and close—each valuable in different ways.

---

## Required Context

### Must Have

**1. Conversion Path Data**
For each conversion:
- Touchpoint sequence (channel/source/medium for each interaction)
- Timestamps for each touchpoint
- Conversion value (if applicable)
- Conversion type

**2. Channel List**
All marketing channels in the mix:
- Paid Search (brand vs. non-brand)
- Paid Social (Meta, LinkedIn, TikTok, etc.)
- Organic Search
- Direct
- Email
- Referral
- Display/Programmatic
- Affiliates
- Others

### Strongly Recommended

**3. Spend Data by Channel**
- Monthly or weekly spend per channel
- Current allocation percentages

**4. Volume Metrics**
- Conversions per channel (current attribution)
- Revenue per channel
- Traffic per channel

### Nice to Have

- Customer lifetime value by acquisition channel
- Conversion lag (time from first touch to conversion)
- Device cross-over data
- Offline touchpoint data
- CRM integration data

---

## Analysis Framework

### Step 1: Current Attribution Assessment

**Attribution Model Comparison:**

| Model | Logic | Best For | Bias |
|-------|-------|----------|------|
| **Last Click** | 100% to final touchpoint | Closing channels | Undervalues awareness |
| **First Click** | 100% to first touchpoint | Discovery channels | Undervalues nurture |
| **Linear** | Equal credit to all touchpoints | Balanced view | No differentiation |
| **Time Decay** | More credit to recent touchpoints | Sales-focused | Undervalues top-funnel |
| **Position-Based** | 40% first, 40% last, 20% middle | Balanced bookends | Undervalues middle |
| **Data-Driven** | ML-based on actual impact | Most accurate | Needs large data volume |

**Model Comparison Matrix:**

| Channel | Last Click | First Click | Linear | Time Decay | Position-Based |
|---------|------------|-------------|--------|------------|----------------|
| Channel A | X conv | X conv | X conv | X conv | X conv |
| Channel B | X conv | X conv | X conv | X conv | X conv |
| ... | ... | ... | ... | ... | ... |

---

### Step 2: Journey Pattern Analysis

**Common Journey Patterns:**

| Pattern | Example | Frequency | Value |
|---------|---------|-----------|-------|
| Single Touch | Paid → Convert | X% | $X |
| Two Touch | Organic → Paid → Convert | X% | $X |
| Three+ Touch | Social → Organic → Email → Convert | X% | $X |

**Journey Length Distribution:**

| Touchpoints | % of Conversions | Avg Value | Avg Days |
|-------------|------------------|-----------|----------|
| 1 | X% | $X | X |
| 2 | X% | $X | X |
| 3 | X% | $X | X |
| 4+ | X% | $X | X |

**Key Insight:** Longer journeys often indicate higher-value customers who research more before committing.

---

### Step 3: Channel Role Analysis

**Channel Roles Framework:**

| Role | Definition | Value |
|------|------------|-------|
| **Initiator** | First touchpoint in journey | Builds awareness, starts relationship |
| **Influencer** | Middle touchpoints | Nurtures, educates, builds consideration |
| **Closer** | Final touchpoint | Converts intent to action |
| **Solo** | Single-touch conversions | Full-funnel in one touch |

**Channel Role Distribution:**

| Channel | Initiator | Influencer | Closer | Solo | Total Involvement |
|---------|-----------|------------|--------|------|-------------------|
| Paid Search - Brand | X% | X% | X% | X% | X conversions |
| Paid Search - Non-Brand | X% | X% | X% | X% | X conversions |
| Paid Social | X% | X% | X% | X% | X conversions |
| Organic Search | X% | X% | X% | X% | X conversions |
| Email | X% | X% | X% | X% | X conversions |
| Direct | X% | X% | X% | X% | X conversions |
| Referral | X% | X% | X% | X% | X conversions |

**Role Insights:**
- High Initiator % = Strong awareness driver
- High Closer % = Strong conversion driver
- High Influencer % = Critical for consideration stage
- Balanced % = Full-funnel channel

---

### Step 4: Assisted Conversion Analysis

**Assisted vs. Last-Click Comparison:**

| Channel | Last-Click Conv | Assisted Conv | Assist Ratio | Assessment |
|---------|-----------------|---------------|--------------|------------|
| Channel A | 100 | 150 | 1.5 | Undervalued |
| Channel B | 100 | 50 | 0.5 | Fairly valued |
| Channel C | 100 | 250 | 2.5 | Very undervalued |
| Channel D | 100 | 30 | 0.3 | Possibly overvalued |

**Assist Ratio Interpretation:**

| Ratio | Meaning | Implication |
|-------|---------|-------------|
| >2.0 | Strong assister | Critical for journey, undervalued by last-click |
| 1.5-2.0 | Moderate assister | Plays important supporting role |
| 1.0-1.5 | Balanced | Both assists and closes |
| 0.5-1.0 | Strong closer | Converts more than assists |
| <0.5 | Primary closer | Almost always the final touch |

---

### Step 5: True Channel Value Estimation

**Weighted Attribution Calculation:**

For balanced view, use position-based or custom model:

```
Channel Value = (Initiations × Init Weight) +
                (Assists × Assist Weight) +
                (Closes × Close Weight)

Recommended Weights:
- Initiations: 30%
- Assists: 20% (divided among all assists)
- Closes: 50%
```

**Channel Efficiency Metrics:**

| Channel | Spend | Attributed Conv | True Conv* | CPA (Last-Click) | CPA (True) | Δ |
|---------|-------|-----------------|------------|------------------|------------|---|
| Channel A | $X | X | X | $X | $X | X% |
| Channel B | $X | X | X | $X | $X | X% |
| ... | ... | ... | ... | ... | ... | ... |

*True Conv = Weighted attribution based on multi-touch model

---

### Step 6: Cross-Channel Synergy Detection

**Channel Combination Analysis:**

| First Touch | Final Touch | Conversion Rate | Avg Value | Frequency |
|-------------|-------------|-----------------|-----------|-----------|
| Paid Social | Paid Search Brand | X% | $X | X |
| Organic | Email | X% | $X | X |
| Display | Paid Search | X% | $X | X |

**High-Synergy Pairs:**
Channels that work well together—investing in one makes the other more effective.

**Cannibalization Risks:**
Channels that may be claiming credit for each other's work.

---

## Output Format

### Executive Summary

```
ATTRIBUTION HEALTH: 🟢/🟡/🔴
Analysis Period: [Date Range]
Total Conversions Analyzed: X,XXX
Channels in Mix: X

KEY FINDING: [Primary insight]
BIGGEST OPPORTUNITY: [Reallocation opportunity]
RISK: [Channel that may be over/undervalued]
```

---

### Attribution Model Comparison

**Conversions by Model:**

| Channel | Last Click | First Click | Linear | Position-Based | Δ (PB vs LC) |
|---------|------------|-------------|--------|----------------|--------------|
| Paid Search - Brand | XXX | XX | XX | XX | -XX% |
| Paid Search - Non-Brand | XXX | XXX | XXX | XXX | +XX% |
| Paid Social | XX | XXX | XX | XXX | +XX% |
| Organic Search | XX | XXX | XXX | XXX | +XX% |
| Email | XXX | XX | XXX | XXX | -XX% |
| Direct | XXX | XX | XX | XX | -XX% |

**Key Observations:**
- [Observation about which channels gain/lose under different models]
- [Observation about biggest discrepancies]
- [Observation about data quality/limitations]

---

### Channel Role Analysis

```
INITIATORS (Awareness Drivers):
1. [Channel] - XX% of journeys start here
2. [Channel] - XX% of journeys start here

INFLUENCERS (Consideration Builders):
1. [Channel] - Present in XX% of multi-touch journeys
2. [Channel] - Present in XX% of multi-touch journeys

CLOSERS (Conversion Drivers):
1. [Channel] - XX% of conversions close here
2. [Channel] - XX% of conversions close here
```

---

### Undervalued Channels Report

**Channels Deserving More Credit/Budget:**

| Channel | Current Credit | True Contribution | Gap | Recommendation |
|---------|----------------|-------------------|-----|----------------|
| [Channel A] | $XX,XXX | $XX,XXX | +XX% | Increase budget XX% |
| [Channel B] | $XX,XXX | $XX,XXX | +XX% | Increase budget XX% |

**Why Undervalued:**
- [Channel A]: [Explanation - e.g., "Strong initiator, starts 40% of converting journeys but gets 10% of credit under last-click"]

---

### Overvalued Channels Report

**Channels Getting Too Much Credit:**

| Channel | Current Credit | True Contribution | Gap | Recommendation |
|---------|----------------|-------------------|-----|----------------|
| [Channel C] | $XX,XXX | $XX,XXX | -XX% | Decrease budget XX% |
| [Channel D] | $XX,XXX | $XX,XXX | -XX% | Test reduction |

**Why Overvalued:**
- [Channel C]: [Explanation - e.g., "Primarily closes journeys started by other channels; removing would redirect closes to other channels"]

---

### Journey Insights

**Average Journey:**
- Touchpoints: X.X
- Duration: X days
- Most common path: [Channel] → [Channel] → [Channel]

**High-Value Journey Patterns:**

| Journey Pattern | Conversion Rate | Avg Value | Volume |
|-----------------|-----------------|-----------|--------|
| [Pattern 1] | XX% | $XXX | XX/month |
| [Pattern 2] | XX% | $XXX | XX/month |
| [Pattern 3] | XX% | $XXX | XX/month |

**Optimization Opportunity:** [Insight about how to encourage more high-value journeys]

---

### Budget Reallocation Recommendations

**Current vs. Recommended Allocation:**

| Channel | Current Spend | Current % | Recommended % | Δ | Action |
|---------|---------------|-----------|---------------|---|--------|
| [Channel A] | $XX,XXX | XX% | XX% | +X% | Increase $X,XXX |
| [Channel B] | $XX,XXX | XX% | XX% | -X% | Decrease $X,XXX |
| [Channel C] | $XX,XXX | XX% | XX% | — | Maintain |
| **Total** | $XX,XXX | 100% | 100% | | |

**Reallocation Impact Projection:**
- Expected additional conversions: +XX/month
- Expected CPA improvement: -$X.XX (-X%)
- Confidence: High/Medium/Low

**Risks of Reallocation:**
- [Risk 1 and mitigation]
- [Risk 2 and mitigation]

---

### Testing Recommendations

**Attribution Experiments to Run:**

| Test | Hypothesis | Method | Duration |
|------|------------|--------|----------|
| [Channel] Holdout | If we pause [Channel], will other channels capture the demand? | Geo-holdout or time-based pause | 2-4 weeks |
| [Channel] Lift Test | What's the true incremental value of [Channel]? | Conversion lift study | 4 weeks |
| Budget Shift Test | Does [Channel A] improve when [Channel B] is reduced? | Controlled budget reallocation | 4 weeks |

---

### Data Quality Assessment

**Attribution Data Health:**

| Factor | Status | Impact |
|--------|--------|--------|
| Cross-device tracking | 🟢/🟡/🔴 | [Impact on analysis] |
| Cookie/consent coverage | 🟢/🟡/🔴 | [Impact on analysis] |
| UTM consistency | 🟢/🟡/🔴 | [Impact on analysis] |
| Conversion tracking | 🟢/🟡/🔴 | [Impact on analysis] |
| Data recency | 🟢/🟡/🔴 | [Impact on analysis] |

**Known Blind Spots:**
- [Blind spot 1 - e.g., "View-through conversions not captured"]
- [Blind spot 2 - e.g., "Phone call conversions not in attribution"]
- [Blind spot 3 - e.g., "Offline impact not measured"]

---

## Special Scenarios

### Scenario 1: Heavy Brand Search Reliance
**Situation:** Brand search accounts for 60%+ of last-click conversions
**Analysis Focus:**
- What channels feed into brand search?
- Would brand searches exist without upper-funnel?
- Test: Pause display/social, measure brand search drop

### Scenario 2: Long Sales Cycles (B2B)
**Situation:** 30+ day average time to conversion
**Analysis Focus:**
- First-touch attribution more important
- Content/nurture channels likely undervalued
- Need to extend lookback window
- Consider lead quality, not just conversion count

### Scenario 3: High Direct Traffic
**Situation:** "Direct" shows as top channel
**Analysis Focus:**
- Direct often = tracking failure or dark social
- Investigate: Are UTMs consistent? Links shared?
- Consider: Branded organic may be mislabeled as direct
- True direct usually means strong brand awareness (good thing)

### Scenario 4: Single Dominant Channel
**Situation:** One channel drives 80%+ of conversions
**Analysis Focus:**
- Is this true dominance or attribution artifact?
- Check: What assists this channel?
- Risk: Over-dependence on one channel
- Test: Incremental lift to verify true impact

---

## Calculation Reference

### Position-Based Attribution Formula

```
For a journey with N touchpoints:

First Touch: 40% of conversion value
Last Touch: 40% of conversion value
Middle Touches: 20% / (N-2) each (if N > 2)

Example (4 touchpoints, $100 conversion):
- Touch 1: $40
- Touch 2: $10
- Touch 3: $10
- Touch 4: $40
```

### Assist Ratio Calculation

```
Assist Ratio = Assisted Conversions / Last-Click Conversions

Where:
- Assisted = Conversions where channel appeared but wasn't last
- Last-Click = Conversions where channel was the final touchpoint
```

### True CPA Calculation

```
True CPA = Channel Spend / Weighted Conversions

Where Weighted Conversions uses position-based or custom model
```

---

## Limitations

**I can analyze:**
- Multi-touch journey patterns
- Channel role distribution
- Model comparison impact
- Assist ratios and contribution
- Budget reallocation logic

**I cannot provide:**
- Statistical incrementality (need lift tests)
- Cross-device stitching (need identity resolution)
- Offline attribution (need integration)
- View-through impact (need impression data)
- Definitive "correct" attribution (always involves judgment)

**For complete attribution, also integrate:**
- Marketing mix modeling (MMM) for top-down validation
- Incrementality testing for ground truth
- Customer surveys for self-reported attribution
- CRM data for full lifecycle view

---

## Quality Checklist

Before delivering analysis:
- [ ] All attribution models compared
- [ ] Channel roles clearly identified
- [ ] Assist ratios calculated and interpreted
- [ ] Undervalued/overvalued channels flagged
- [ ] Journey patterns analyzed
- [ ] Budget reallocation quantified
- [ ] Risks of reallocation noted
- [ ] Data quality issues acknowledged
- [ ] Testing recommendations provided
- [ ] Limitations stated clearly
