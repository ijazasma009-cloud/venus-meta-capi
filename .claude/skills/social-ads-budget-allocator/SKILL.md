---
name: social-ads-budget-allocator
description: Analyzes efficiency across social ad platforms (Meta, TikTok, LinkedIn, etc.) and recommends optimal budget reallocation.
---

# Social Ads Budget Allocator

## Purpose

Determine the optimal distribution of advertising budget across:
- Multiple platforms (Meta, TikTok, LinkedIn, Pinterest, Twitter/X, Snapchat)
- Campaigns within each platform
- Objectives and funnel stages

**Core Philosophy:** Not all dollars are equal. A dollar spent on an efficient campaign drives 2-3x the results of a dollar spent on an inefficient one. Move money from expensive conversions to cheap ones.

---

## When to Use This Skill

- Monthly/quarterly budget planning
- When adding a new platform to the mix
- When overall performance is declining
- Before scaling total spend
- When one platform significantly outperforms others
- After major creative or audience changes

---

## Required Context

| Data Point | Required | Notes |
|------------|----------|-------|
| Spend by platform (last 30 days minimum) | Yes | Need volume for comparison |
| Conversions/results by platform | Yes | Primary success metric |
| CPA or ROAS by platform | Yes | Efficiency comparison |
| Conversion value (if ROAS model) | If applicable | Revenue-based optimization |
| Total available budget | Yes | Constraint for allocation |
| Business constraints | Helpful | Minimum presence requirements |
| Historical performance (60-90 days) | Helpful | Trend analysis |
| Audience overlap data | Helpful | Cross-platform redundancy |

---

## The Efficiency Hierarchy

### Platform-Level Analysis

Rank platforms by efficiency (CPA or ROAS):

| Platform | Spend | Conversions | CPA | ROAS | Efficiency Rank |
|----------|-------|-------------|-----|------|-----------------|
| | | | | | |

### Efficiency Tiers

| Tier | Name | Criteria (CPA Model) | Criteria (ROAS Model) |
|------|------|---------------------|----------------------|
| 1 | **Gold** | CPA < 70% of blended avg | ROAS > 143% of target |
| 2 | **Silver** | CPA 70-100% of blended avg | ROAS 100-143% of target |
| 3 | **Bronze** | CPA 100-130% of blended avg | ROAS 77-100% of target |
| 4 | **Underperformer** | CPA 130-200% of blended avg | ROAS 50-77% of target |
| 5 | **Bleeder** | CPA > 200% of blended avg | ROAS < 50% of target |

---

## Marginal Efficiency Analysis

The key question isn't "what's the average CPA?" but "what will happen if I spend $1 more?"

### Marginal CPA/ROAS Estimation

For each platform, estimate the marginal cost of the next conversion:

```
Marginal CPA = Current CPA × Scaling Factor

Scaling Factor by Current Spend vs. Saturation:
- < 30% of estimated saturation: 1.0x (linear scaling)
- 30-60% of saturation: 1.1-1.3x (mild diminishing returns)
- 60-80% of saturation: 1.3-1.6x (significant diminishing returns)
- > 80% of saturation: 1.6-2.5x (severe diminishing returns)
```

### Saturation Signals

| Signal | Indication |
|--------|-----------|
| CPM increasing week over week | Audience exhaustion |
| Frequency > 3.0 | Oversaturating audience |
| CTR declining, CPC rising | Fewer interested users left |
| Same spend, fewer conversions | Diminishing returns active |

---

## The Reallocation Framework

### Step 1: Calculate Current State

```
CURRENT ALLOCATION
Total Budget: $________

| Platform | $ Spend | % of Total | Conversions | CPA | Efficiency Tier |
|----------|---------|------------|-------------|-----|-----------------|
| Meta | | | | | |
| TikTok | | | | | |
| LinkedIn | | | | | |
| [Other] | | | | | |
| TOTAL | | 100% | | Blended: | |
```

### Step 2: Identify Reallocation Opportunities

**Move FROM:**
- Tier 4-5 platforms (Underperformers & Bleeders)
- Campaigns with clear saturation signals
- Platforms with declining efficiency trends

**Move TO:**
- Tier 1-2 platforms (Gold & Silver) that aren't saturated
- Emerging opportunities with strong early signals
- Campaigns with headroom for growth

### Step 3: Calculate Optimal Allocation

Use this prioritization formula:

```
Allocation Score = (Efficiency Score × Volume Potential) / Risk Factor

Where:
- Efficiency Score = Blended CPA / Platform CPA (higher = more efficient)
- Volume Potential = 1 - (Current Spend / Estimated Saturation Point)
- Risk Factor = 1.0 (stable) to 2.0 (volatile/untested)
```

---

## Platform-Specific Considerations

### Meta (Facebook/Instagram)

| Factor | Consideration |
|--------|---------------|
| **Strengths** | Largest scale, best targeting, mature optimization |
| **Saturation Point** | Typically 2-5% of total addressable audience/month |
| **Minimum Viable Budget** | $20-50/day per ad set for learning |
| **Scaling Limit** | 20-30% budget increase per week max |
| **Watch For** | iOS attribution gaps, frequency creep |

### TikTok

| Factor | Consideration |
|--------|---------------|
| **Strengths** | Lower CPMs, younger audience, viral potential |
| **Saturation Point** | Faster saturation (3-4 weeks per creative) |
| **Minimum Viable Budget** | $50-100/day per ad group for learning |
| **Scaling Limit** | Can scale faster (30-50%/week) but higher volatility |
| **Watch For** | Creative-dependent, quality score fluctuations |

### LinkedIn

| Factor | Consideration |
|--------|---------------|
| **Strengths** | B2B targeting, professional intent |
| **Saturation Point** | Lower (smaller professional audiences) |
| **Minimum Viable Budget** | $100/day minimum for meaningful data |
| **Scaling Limit** | Limited by audience size (10-20%/week) |
| **Watch For** | High CPCs, long sales cycles |

### Pinterest

| Factor | Consideration |
|--------|---------------|
| **Strengths** | High-intent shopping, long content lifespan |
| **Saturation Point** | Slow saturation (evergreen content) |
| **Minimum Viable Budget** | $20-30/day per campaign |
| **Scaling Limit** | Gradual scaling works best |
| **Watch For** | Seasonal variations, attribution window |

### Twitter/X

| Factor | Consideration |
|--------|---------------|
| **Strengths** | Real-time relevance, conversation targeting |
| **Saturation Point** | Variable by topic/audience |
| **Minimum Viable Budget** | $30-50/day for testing |
| **Scaling Limit** | Event/moment dependent |
| **Watch For** | Brand safety, volatile performance |

### Snapchat

| Factor | Consideration |
|--------|---------------|
| **Strengths** | Young demographic, AR features |
| **Saturation Point** | Fast creative fatigue |
| **Minimum Viable Budget** | $50/day per ad set |
| **Scaling Limit** | Creative-limited more than budget-limited |
| **Watch For** | Measurement challenges, age skew |

---

## Reallocation Scenarios

### Scenario A: Optimize Existing Mix
Goal: Improve efficiency without adding platforms

```
Action: Shift budget from Tier 4-5 to Tier 1-2
Rule: Move up to 30% of underperformer budget in one cycle
Guardrail: Maintain minimum presence if required
```

### Scenario B: Scale Total Budget
Goal: Increase spend while maintaining efficiency

```
Priority Order:
1. Add to Tier 1 platforms up to saturation signals
2. Add to Tier 2 platforms with headroom
3. Test new platforms with 10-15% of increment
4. Never add to Tier 4-5 without fixing issues first
```

### Scenario C: Add New Platform
Goal: Test and integrate new channel

```
Test Budget: 10-15% of total, or $3K-$5K minimum
Test Duration: 4-6 weeks minimum
Success Criteria: Beat Tier 3 threshold to continue
Kill Criteria: Worse than Tier 5 for 2+ weeks
```

### Scenario D: Cut Total Budget
Goal: Reduce spend while preserving results

```
Cut Priority (first to last):
1. Tier 5 (Bleeders) - cut immediately
2. Tier 4 (Underperformers) - reduce by 50%
3. Tier 3 (Bronze) - hold or reduce 20%
4. Tier 1-2 (Gold/Silver) - protect, last to cut
```

---

## Allocation Constraints

### Hard Constraints
- Platform minimums (e.g., LinkedIn needs $100/day for learning)
- Contractual commitments
- Reach/awareness requirements that override efficiency

### Soft Constraints
- Diversification (no platform > 70% of spend)
- Testing budget (5-15% for experiments)
- Seasonal adjustments

### Constraint Override Rules
```
IF hard constraint conflicts with efficiency optimization:
    → Honor constraint, note efficiency sacrifice
    → Calculate cost of constraint in lost conversions
    → Flag for stakeholder visibility
```

---

## Projection Modeling

Calculate the impact of proposed reallocation:

### Conversion Impact Model

```
For each platform:
    Current Conversions = Spend / CPA
    Projected Conversions = New Spend / Projected CPA

Where Projected CPA accounts for:
    - Scaling factor (diminishing returns)
    - Trend direction (improving/declining)
    - Seasonal adjustments

Net Impact = Σ(Projected Conversions) - Σ(Current Conversions)
```

### Scenario Comparison Template

| Scenario | Total Spend | Est. Conversions | Blended CPA | vs. Current |
|----------|-------------|------------------|-------------|-------------|
| Current State | | | | - |
| Optimized Mix | | | | +X% |
| Aggressive Shift | | | | +Y% |
| Conservative Shift | | | | +Z% |

---

## Output Deliverables

### 1. Current State Summary

```
CROSS-PLATFORM PERFORMANCE SUMMARY
Period: [Date Range]
Total Spend: $[X]
Total Conversions: [X]
Blended CPA: $[X]

PLATFORM BREAKDOWN:
| Platform | Spend | % | Conv | CPA | Tier | Trend | Verdict |
|----------|-------|---|------|-----|------|-------|---------|
| | | | | | | | |

EFFICIENCY ANALYSIS:
├── Gold Tier Spend: $[X] ([X]% of total) - [X] conversions
├── Silver Tier Spend: $[X] ([X]% of total) - [X] conversions
├── Bronze Tier Spend: $[X] ([X]% of total) - [X] conversions
├── Underperformer Spend: $[X] ([X]% of total) - [X] conversions
└── Bleeder Spend: $[X] ([X]% of total) - [X] conversions

WASTE IDENTIFIED: $[X] ([X]% of total spend)
```

### 2. Reallocation Recommendation

```
RECOMMENDED REALLOCATION

| Platform | Current $ | Current % | Recommended $ | Recommended % | Change |
|----------|-----------|-----------|---------------|---------------|--------|
| | | | | | |
| TOTAL | | 100% | | 100% | - |

RATIONALE:
- [Platform A]: [Increase/Decrease] because [reason]
- [Platform B]: [Increase/Decrease] because [reason]
```

### 3. Impact Projection

```
PROJECTED IMPACT

                    | Current | Optimized | Difference |
--------------------|---------|-----------|------------|
Total Spend         | $X      | $X        | -          |
Est. Conversions    | X       | X         | +X (+Y%)   |
Blended CPA         | $X      | $X        | -$X (-Y%)  |
Est. Revenue        | $X      | $X        | +$X        |
Est. ROAS           | X.Xx    | X.Xx      | +X.Xx      |
```

### 4. Implementation Plan

```
IMPLEMENTATION ROADMAP

WEEK 1:
├── [Action 1]
├── [Action 2]
└── [Action 3]

WEEK 2:
├── [Action 4]
└── [Action 5]

MONITORING CHECKPOINTS:
├── Day 7: Check [metric] - abort if [condition]
├── Day 14: Check [metric] - adjust if [condition]
└── Day 30: Full review and next iteration
```

### 5. Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| | | | |

---

## Decision Guardrails

### Before Major Reallocation, Verify:

- [ ] At least 30 days of data for each platform
- [ ] Seasonal factors accounted for
- [ ] No major changes pending (creative, audience, offer)
- [ ] Tracking/attribution consistent across platforms
- [ ] Saturation signals checked (not just averages)
- [ ] Marginal CPA estimated (not just historical)
- [ ] Stakeholder constraints documented

### Red Flags to Pause Reallocation:

- Platform has < 30 conversions (insufficient data)
- Attribution models differ significantly between platforms
- Major creative or offer change in last 14 days
- Seasonal peak/trough in next 30 days
- One platform > 90% of spend (rebalancing should be gradual)

---

## Integration with Other Skills

| Connected Skill | Use Case |
|-----------------|----------|
| meta-ads-creative-ranker | Understand WHY platform is underperforming |
| creative-fatigue-detector | Check if poor performance is creative or budget issue |
| audience-overlap-mapper | Identify cross-platform audience redundancy |

---

## Limitations

- Cannot account for brand awareness effects across platforms
- Attribution models vary; true incrementality unknown
- Assumes current targeting is optimized (budget ≠ only lever)
- Seasonal patterns may not repeat
- New platform testing carries higher uncertainty
- Cannot predict competitive landscape changes

---

## Quality Checklist Before Delivery

- [ ] All platforms have minimum 30 days of data
- [ ] Efficiency tiers assigned correctly
- [ ] Marginal CPA/scaling factors considered
- [ ] Platform-specific considerations addressed
- [ ] Constraints documented and honored
- [ ] At least 2 scenarios modeled
- [ ] Implementation plan is gradual (not overnight shift)
- [ ] Monitoring checkpoints defined
- [ ] Risks identified with mitigations
