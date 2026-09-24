---
name: budget-allocation-optimizer
description: Analyzes campaign performance and recommends optimal budget distribution to maximize conversions at target efficiency. Triggers when user asks about budget allocation, wants to redistribute spend, or asks "where should I put my budget?" Uses marginal CPA analysis to identify reallocation opportunities. Shows exactly how much to move and expected impact.
---

# Budget Allocation Optimizer

Get more conversions from the same budget by putting money where it works hardest.

## Core Philosophy

**Not all dollars are equal.** The last $100 spent in Campaign A might get you 1 conversion, while the first $100 added to Campaign B might get you 5.

**The Goal:** Find the allocation where every dollar is working equally hard across all campaigns.

**The Principle:** Marginal CPA analysis—move budget from campaigns where the NEXT dollar is expensive to campaigns where the NEXT dollar is cheap.

---

## Required Context

### Must Have

**1. Campaign Performance Data**
For each campaign:
- Campaign name
- Current daily/monthly budget
- Current spend
- Conversions
- CPA

**2. Time Period**
- At least 14 days of data (30 days preferred)
- Consistent period across all campaigns

### Strongly Recommended

**3. Targets & Constraints**
- Target CPA or ROAS
- Total budget (fixed or flexible)
- Minimum spend per campaign (if any)
- Maximum spend per campaign (if any)

**4. Budget Utilization**
- Is each campaign spending its full budget?
- Any campaigns limited by budget?

### Nice to Have

- Impression share data (especially lost IS due to budget)
- Historical performance at different spend levels
- Conversion value data (for ROAS optimization)
- Seasonality context

---

## Analysis Framework

### Step 1: Current State Assessment

**Campaign Efficiency Ranking:**

| Tier | CPA vs Target | Assessment |
|------|---------------|------------|
| ⭐ Star | <75% of target | Highly efficient, likely underfunded |
| ✅ Solid | 75-100% of target | Meeting goals, balanced |
| ⚠️ Borderline | 100-125% of target | Marginal, watch closely |
| ❌ Underperformer | >125% of target | Inefficient, likely overfunded |

**Budget Utilization Check:**
- Spending 100%+ of budget = Potentially constrained
- Spending <90% of budget = Demand issue or targeting too narrow
- Spending 90-100% = Healthy utilization

---

### Step 2: Marginal CPA Analysis

**The Key Question:** What happens to CPA as we increase/decrease spend?

**General Patterns:**
- **Stars at budget cap:** Marginal CPA likely still good—room to scale
- **Underperformers at budget cap:** Already inefficient at current spend
- **Low-spend campaigns:** Insufficient data to judge marginal efficiency

**Marginal CPA Estimation:**

When historical data is unavailable, use these heuristics:

| Current Efficiency | Budget Status | Estimated Marginal CPA |
|-------------------|---------------|------------------------|
| Star (<75% target) | Capped | ~1.1-1.2x current CPA |
| Star (<75% target) | Not capped | ~1.0x current CPA |
| Solid (75-100%) | Capped | ~1.2-1.3x current CPA |
| Solid (75-100%) | Not capped | ~1.1x current CPA |
| Borderline (100-125%) | Capped | ~1.3-1.5x current CPA |
| Underperformer (>125%) | Any | Already too high |

**The Reallocation Principle:**
Move budget from campaigns with HIGH marginal CPA to campaigns with LOW marginal CPA until marginal CPAs equalize.

---

### Step 3: Reallocation Recommendations

**Identify Donors (Reduce Budget):**
- Campaigns with CPA significantly above target
- Campaigns with declining efficiency trends
- Campaigns not spending full budget anyway

**Identify Recipients (Increase Budget):**
- Campaigns with CPA below target AND budget-capped
- Campaigns with strong efficiency AND room to grow
- High impression share loss due to budget

**Calculate Reallocation:**
```
Recommended shift = MIN(
  Donor's reducible budget,
  Recipient's absorbable budget,
  Amount that keeps both at acceptable CPA
)
```

---

### Step 4: Impact Projection

**Conservative Estimate:**
- Assume recipient CPA increases 10-20% with more budget
- Assume donor CPA stays flat or improves slightly
- Net conversion gain = (new conversions from recipient) - (lost conversions from donor)

**Projection Formula:**
```
Additional conversions = Budget shifted / Recipient's projected CPA
Lost conversions = Budget shifted / Donor's current CPA
Net gain = Additional - Lost

If Net gain > 0, reallocation is beneficial
```

---

## Output Format

### Executive Summary

```
CURRENT ALLOCATION EFFICIENCY: 🟢/🟡/🔴
Total Budget: $XX,XXX/month
Blended CPA: $XX.XX
Optimization Opportunity: +XX conversions/month (estimated)
```

---

### 📊 Current State Analysis

**Campaign Efficiency Ranking:**

| Rank | Campaign | Spend | Conv | CPA | vs Target | Budget Status | Tier |
|------|----------|-------|------|-----|-----------|---------------|------|
| 1 | [Name] | $X,XXX | XX | $XX | -XX% | Capped | ⭐ |
| 2 | [Name] | $X,XXX | XX | $XX | -X% | OK | ✅ |
| 3 | [Name] | $X,XXX | XX | $XX | +XX% | Capped | ⚠️ |
| 4 | [Name] | $X,XXX | XX | $XX | +XX% | Under | ❌ |

**Key Observations:**
- [Observation about efficiency distribution]
- [Observation about budget utilization]
- [Observation about optimization opportunity]

---

### 💰 Reallocation Recommendations

**Summary:**
```
Total to reallocate: $X,XXX/month
From: [X] campaigns
To: [X] campaigns
Expected impact: +XX conversions/month
```

---

**Recommendation 1: [Donor] → [Recipient]**

| | Donor: [Campaign] | Recipient: [Campaign] |
|---|---|---|
| Current Budget | $X,XXX | $X,XXX |
| Current CPA | $XX | $XX |
| Recommended Change | -$XXX | +$XXX |
| New Budget | $X,XXX | $X,XXX |
| Projected CPA | $XX | $XX |

**Rationale:** [Why this reallocation makes sense]

**Expected Impact:**
- Conversions lost from donor: ~X
- Conversions gained from recipient: ~X
- Net gain: +X conversions
- Net CPA improvement: -$X.XX

---

**Recommendation 2: [Donor] → [Recipient]**

[Same format as above]

---

### 📈 Projected Outcome

**Before vs After:**

| Metric | Current | Projected | Change |
|--------|---------|-----------|--------|
| Total Budget | $XX,XXX | $XX,XXX | — |
| Total Conversions | XXX | XXX | +XX (+X%) |
| Blended CPA | $XX.XX | $XX.XX | -$X.XX (-X%) |

**Confidence Level:** High / Medium / Low

**Assumptions:**
- [Key assumption 1]
- [Key assumption 2]

---

### ⚠️ Risks & Considerations

**Scaling Risk:**
- [Campaign] may see CPA increase faster than projected if scaled aggressively
- Recommendation: Increase budget incrementally (20% per week)

**Reduction Risk:**
- [Campaign] contributes to brand visibility even if CPA is high
- Consider: Strategic value beyond direct conversions

**Data Limitations:**
- [Any data gaps that affect confidence]

---

### 🎯 Implementation Plan

**Week 1:**
- [ ] Reduce [Campaign A] budget by $XXX
- [ ] Increase [Campaign B] budget by $XXX
- [ ] Monitor daily for 3 days

**Week 2:**
- [ ] Evaluate performance
- [ ] If stable, continue with next reallocation
- [ ] If CPA spikes, pause and reassess

**Success Metrics:**
- Blended CPA should decrease within 2 weeks
- Conversion volume should increase within 2 weeks
- No single campaign CPA should exceed [threshold]

---

### 📋 Monitoring Checklist

After reallocation, check daily for first week:
- [ ] Recipient campaign spending new budget
- [ ] Recipient CPA within projected range
- [ ] Donor campaign stable or improved
- [ ] No impression share collapse
- [ ] Conversion volume trending up

---

## Special Scenarios

### Scenario 1: All Campaigns Efficient
**Situation:** Every campaign at or below target CPA
**Recommendation:**
- If budget-capped: Request budget increase
- If not capped: Expand targeting, add keywords
- Maintain current allocation if no expansion possible

### Scenario 2: All Campaigns Inefficient
**Situation:** Every campaign above target CPA
**Recommendation:**
- Don't reallocate (moving deck chairs on Titanic)
- Focus on fixing fundamentals first
- Consider: targeting, landing pages, offer, tracking

### Scenario 3: One Dominant Campaign
**Situation:** One campaign drives 80%+ of conversions efficiently
**Recommendation:**
- Prioritize scaling that campaign
- Reduce others to minimum viable spend
- Test new campaigns to diversify

### Scenario 4: New Campaigns with Limited Data
**Situation:** Some campaigns <14 days old
**Recommendation:**
- Exclude from reallocation analysis
- Let them mature before judging
- Note in limitations

---

## Calculation Reference

### Marginal CPA Estimation

When you don't have historical data at different spend levels:

**For budget-capped efficient campaigns:**
```
Projected CPA at +20% budget = Current CPA × 1.15
Projected CPA at +50% budget = Current CPA × 1.25
Projected CPA at +100% budget = Current CPA × 1.40
```

**For non-capped campaigns:**
```
Efficiency likely stable—CPA won't change much with budget increase
Focus on expanding targeting instead
```

### Net Conversion Calculation

```
Budget to move: $1,000

Donor campaign:
- Current CPA: $100
- Conversions lost: $1,000 / $100 = 10

Recipient campaign:
- Current CPA: $50
- Projected CPA at higher spend: $50 × 1.15 = $57.50
- Conversions gained: $1,000 / $57.50 = 17.4

Net gain: 17.4 - 10 = +7.4 conversions
```

---

## Limitations

**I can provide:**
- Efficiency-based allocation recommendations
- Impact projections based on heuristics
- Implementation framework
- Risk assessment

**I cannot provide:**
- Exact marginal CPA curves (need historical spend experiments)
- Incrementality analysis (need holdout tests)
- Cross-channel impact (need full funnel data)
- Guaranteed outcomes (projections are estimates)

**For better recommendations, also provide:**
- Historical performance at different budget levels
- Impression share data
- Conversion value data
- Competitive auction insights

---

## Quality Checklist

Before delivering recommendations:
- [ ] All campaigns ranked by efficiency
- [ ] Budget utilization status checked
- [ ] Donors clearly justified (why reduce)
- [ ] Recipients clearly justified (why increase)
- [ ] Impact projection includes assumptions
- [ ] Risks identified for each reallocation
- [ ] Implementation plan is gradual (not all at once)
- [ ] Monitoring checklist provided
- [ ] Limitations clearly stated
