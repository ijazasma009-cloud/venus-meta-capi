---
name: facebook-ads-budget-allocator
description: Analyzes Meta Ads campaign efficiency and recommends budget reallocation based on marginal CPA analysis. Identifies where to shift spend for maximum impact. Use when deciding how to distribute budget across campaigns or when scaling.
---

# Facebook Ads Budget Allocator

Not all dollars are equal. Spend them where they work hardest.

## Core Philosophy

**The last dollar in Campaign A might buy you 0.5 conversions. The first dollar added to Campaign B might buy you 2.**

This is marginal efficiency—and most advertisers ignore it completely. They either:
1. Spread budget evenly (democratic, but dumb)
2. Put everything in the "winner" (efficient until diminishing returns hit)
3. Never reallocate (set and forget)

**Every campaign has a point of diminishing returns.** At low spend, conversions are cheap. As you scale, you exhaust the low-hanging fruit and CPA rises. The goal is to find the sweet spot for each campaign—then balance across all of them.

**Budget allocation is not a one-time decision.** It's a continuous optimization as campaigns mature, audiences saturate, and creative fatigues.

---

## Required Context

### Must Have

1. **Campaign Performance Data (Last 14-30 Days)**
   - Campaign names
   - Daily/total spend per campaign
   - Conversions per campaign
   - CPA per campaign
   - Trend direction (improving, stable, declining)

2. **Current Budget Allocation**
   - Total daily budget
   - Budget per campaign
   - Any budget constraints or caps?

3. **Business Constraints**
   - Target CPA or ROAS
   - Maximum acceptable CPA
   - Any campaigns that must run (brand, seasonal)?

### Strongly Recommended

4. **Historical Data**
   - How has CPA changed as spend changed?
   - Any campaigns recently scaled up/down?
   - Performance at different budget levels?

5. **Campaign Context**
   - Campaign objectives (prospecting vs retargeting)
   - Audience sizes per campaign
   - Creative freshness

### Nice to Have

6. **Future Plans**
   - Planning to scale total budget?
   - Any new campaigns launching?
   - Seasonal considerations?

---

## Budget Allocation Framework

### Phase 1: Current State Assessment

**Campaign Efficiency Categorization:**

| Category | CPA vs Target | Trend | Assessment |
|----------|---------------|-------|------------|
| 🟢 Star | Below target | Stable/Improving | Scale priority |
| 🟡 Potential | At target | Stable | Maintain, monitor |
| 🟠 Declining | Above target | Declining | Reduce or fix |
| 🔴 Failing | Far above target | Declining | Pause or major change |

**Efficiency Score Formula:**
```
Efficiency Score = (Target CPA / Actual CPA) × 100

>100 = Outperforming
100 = At target
<100 = Underperforming
```

---

### Phase 2: Marginal CPA Analysis

**The Marginal CPA Curve:**

```
CPA
 │
 │                          ╱ Diminishing returns zone
 │                    ╱
 │               ╱
 │          ╱
 │     ────              ← Sweet spot
 │______________________|___________________ Spend
      Low spend         High spend
```

**Estimating Marginal Efficiency:**

When you have historical data at different spend levels:

| Spend Level | Conversions | CPA | Marginal CPA* |
|-------------|-------------|-----|---------------|
| $1,000 | 50 | $20 | - |
| $2,000 | 90 | $22 | $25 |
| $3,000 | 120 | $25 | $33 |
| $4,000 | 140 | $29 | $50 |

*Marginal CPA = Additional spend ÷ Additional conversions

**What this tells you:** Going from $3k to $4k costs $50 per incremental conversion, even though average CPA is $29.

---

### Phase 3: Diminishing Returns Indicators

**Signs You're Hitting Diminishing Returns:**

| Indicator | What It Means | Threshold |
|-----------|---------------|-----------|
| CPA increasing with spend | Audience exhaustion | >15% CPA increase when doubling spend |
| Frequency rising | Same people seeing ads repeatedly | Frequency >2.5 per week |
| CPM rising | Competition for limited audience | >20% CPM increase |
| Conversion rate dropping | Lower-quality traffic | >15% drop in CVR |
| Delivery slowing | Can't spend full budget | Underspending by >20% |

**Saturation Formula (rough estimate):**
```
Weekly saturation % = (Weekly Impressions ÷ Audience Size) × 100

<10% = Plenty of headroom
10-30% = Moderate saturation
>30% = High saturation, diminishing returns likely
```

---

### Phase 4: Reallocation Decision Matrix

**Budget Movement Rules:**

| From Campaign | To Campaign | Decision Logic |
|---------------|-------------|----------------|
| 🔴 Failing | 🟢 Star | Move immediately |
| 🟠 Declining | 🟢 Star | Move 50%, monitor |
| 🟡 Potential | 🟢 Star | Move cautiously, test impact |
| 🟢 Star A | 🟢 Star B | Move to lower marginal CPA |
| Any | New Test | Allocate 10-20% for testing |

**Reallocation Guardrails:**

| Rule | Rationale |
|------|-----------|
| Never increase budget >30% at once | Disrupts algorithm learning |
| Keep minimum 7 days between changes | Let changes stabilize |
| Maintain $50+ daily per campaign | Below this, learning suffers |
| Don't kill retargeting for prospecting | Full funnel matters |
| Reserve 10-20% for testing | Don't over-optimize to status quo |

---

### Phase 5: Budget Scaling Scenarios

**Scenario A: Scaling Total Budget by 20-50%**

| Priority | Action |
|----------|--------|
| 1 | Add to 🟢 Star campaigns first |
| 2 | Scale each by 20-30% max |
| 3 | If still have budget, test new campaigns |
| 4 | Monitor marginal CPA weekly |

**Scenario B: Cutting Total Budget by 20-50%**

| Priority | Action |
|----------|--------|
| 1 | Cut 🔴 Failing campaigns first |
| 2 | Reduce 🟠 Declining campaigns |
| 3 | Protect 🟢 Star campaigns |
| 4 | Maintain minimum viable spend on retargeting |

**Scenario C: Maintaining Budget, Improving Efficiency**

| Priority | Action |
|----------|--------|
| 1 | Move spend from 🔴🟠 to 🟢 |
| 2 | Consolidate similar campaigns |
| 3 | Find and fix creative fatigue |
| 4 | Test new audiences/creative |

---

### Phase 6: Funnel Budget Framework

**Budget Distribution by Funnel Stage:**

| Stage | Role | Typical Allocation | CPA Expectation |
|-------|------|-------------------|-----------------|
| **Prospecting** | Acquire new customers | 60-70% | Higher |
| **Retargeting** | Convert warm audiences | 20-30% | Lower |
| **Retention** | Re-engage past customers | 5-15% | Lowest |

**Funnel Health Check:**

| Imbalance | Risk | Fix |
|-----------|------|-----|
| Too much prospecting | Ignoring cheap conversions | Increase retargeting |
| Too much retargeting | Audience will exhaust | Increase prospecting |
| No retention | Missing repeat purchases | Add customer campaigns |

**Ideal Ratio Test:**
If prospecting CPA is more than 3x retargeting CPA, you're probably under-investing in retargeting.

---

### Phase 7: Impact Projection

**Estimating Reallocation Impact:**

| Metric | Formula |
|--------|---------|
| Expected conversions gained | Budget moved ÷ Destination CPA |
| Expected conversions lost | Budget moved ÷ Source CPA |
| Net conversion change | Gained - Lost |
| Efficiency improvement | Net change ÷ Lost × 100 |

**Example Calculation:**
- Move $1,000 from Campaign A (CPA $50) to Campaign B (CPA $25)
- Conversions lost: $1,000 ÷ $50 = 20
- Conversions gained: $1,000 ÷ $25 = 40
- Net gain: +20 conversions
- Efficiency improvement: +100%

**Conservative Adjustment:**
Assume destination campaign CPA will rise 10-20% when budget increases. Adjust projections accordingly.

---

## Output Format

```
═══════════════════════════════════════════════════════════════════
FACEBOOK ADS BUDGET ALLOCATION ANALYSIS
Account: [Account Name]
Analysis Date: [Date]
Period Analyzed: [Date Range]
═══════════════════════════════════════════════════════════════════

📊 CURRENT STATE OVERVIEW
────────────────────────────────────────────────────────────────────

**Total Daily Budget:** $[X]
**Total Monthly Budget:** $[X]
**Target CPA:** $[X]
**Current Blended CPA:** $[X]

| Campaign | Daily Budget | % of Total | Conversions | CPA | vs Target | Status |
|----------|--------------|------------|-------------|-----|-----------|--------|
| [Name] | $[X] | [X]% | [X] | $[X] | [+/-X]% | [🟢/🟡/🟠/🔴] |

**Funnel Distribution:**
- Prospecting: [X]% ($[X]/day)
- Retargeting: [X]% ($[X]/day)
- Retention: [X]% ($[X]/day)

═══════════════════════════════════════════════════════════════════

📈 EFFICIENCY ANALYSIS
────────────────────────────────────────────────────────────────────

### Campaign Efficiency Scores

| Campaign | Efficiency Score | Trend | Marginal CPA Est. | Headroom |
|----------|------------------|-------|-------------------|----------|
| [Name] | [X] | [↑/→/↓] | $[X] | [High/Med/Low] |

### Diminishing Returns Assessment

| Campaign | Saturation % | Frequency | CPM Trend | At Limit? |
|----------|--------------|-----------|-----------|-----------|
| [Name] | [X]% | [X] | [Trend] | [Y/N] |

═══════════════════════════════════════════════════════════════════

💰 REALLOCATION RECOMMENDATIONS
────────────────────────────────────────────────────────────────────

### Recommended Budget Changes

| Action | Campaign | Current | Recommended | Change | Rationale |
|--------|----------|---------|-------------|--------|-----------|
| [↑/↓/→] | [Name] | $[X] | $[X] | [+/-$X] | [Why] |

### Summary of Movements

| From | To | Amount | Expected Impact |
|------|----|--------|-----------------|
| [Campaign] | [Campaign] | $[X] | [+/- X conversions] |

═══════════════════════════════════════════════════════════════════

📊 PROJECTED IMPACT
────────────────────────────────────────────────────────────────────

**If recommendations implemented:**

| Metric | Current | Projected | Change |
|--------|---------|-----------|--------|
| Total daily conversions | [X] | [X] | [+/-X] |
| Blended CPA | $[X] | $[X] | [+/-$X] |
| Monthly conversions | [X] | [X] | [+/-X] |
| Monthly spend | $[X] | $[X] | [No change] |

**Confidence Level:** [High/Medium/Low]
**Assumptions:** [List key assumptions]

═══════════════════════════════════════════════════════════════════

📋 IMPLEMENTATION PLAN
────────────────────────────────────────────────────────────────────

### Week 1
- [ ] [Specific budget change 1]
- [ ] [Specific budget change 2]

### Week 2
- [ ] Monitor performance
- [ ] Check for CPA changes in scaled campaigns

### Week 3
- [ ] Evaluate results
- [ ] Make secondary adjustments if needed

### Ongoing
- [ ] Weekly budget review
- [ ] Monthly reallocation analysis

═══════════════════════════════════════════════════════════════════

⚠️ RISKS & CONSIDERATIONS
────────────────────────────────────────────────────────────────────

| Risk | Likelihood | Mitigation |
|------|------------|------------|
| [Risk] | [High/Med/Low] | [How to address] |

**Do Not:**
- [ ] Increase any campaign budget by more than 30% at once
- [ ] Make changes more frequently than every 7 days
- [ ] Reduce retargeting below minimum viable level
- [ ] Ignore learning phase on newly scaled campaigns

═══════════════════════════════════════════════════════════════════

🎯 NEXT REVIEW
────────────────────────────────────────────────────────────────────

Schedule next budget review: [Date - 2 weeks out]

Key metrics to track:
1. CPA by campaign (is scaled campaign holding?)
2. Marginal efficiency (are diminishing returns setting in?)
3. Funnel balance (is prospecting feeding retargeting?)

═══════════════════════════════════════════════════════════════════
```

---

## Common Scenarios

### Scenario 1: "One campaign is crushing it, should I put all budget there?"
**Analysis:** Check for diminishing returns. What's the marginal CPA at current spend vs. 2x spend?

**Verdict:** Scale by 30% max, monitor for 7 days, then decide. Going all-in often triggers diminishing returns.

### Scenario 2: "My retargeting has amazing CPA but small volume"
**Analysis:** Retargeting is limited by prospecting. You can't retarget people you never reached.

**Verdict:** Maintain retargeting budget, invest more in prospecting to fill the funnel. Retargeting CPA will stay low.

### Scenario 3: "Every campaign has similar CPA"
**Analysis:** Either you've optimized well, or you haven't tested enough variation.

**Verdict:** Look at marginal CPA and headroom. The campaign with most headroom (lowest saturation) should get more budget.

### Scenario 4: "Boss wants to double the budget overnight"
**Analysis:** Doubling budget typically increases CPA 20-40% short-term.

**Verdict:** Push back. Scale 30% per week maximum. Set expectations for temporary CPA increase during scaling.

### Scenario 5: "Need to cut budget by 50% immediately"
**Analysis:** Protect highest efficiency campaigns, cut lowest performers.

**Verdict:** Cut failing campaigns first. Reduce (don't eliminate) declining campaigns. Protect stars and retargeting.

---

## Limitations

1. **Cannot predict exact marginal CPA** - Estimates based on patterns and assumptions
2. **Algorithm behavior varies** - Meta's delivery optimization affects actual results
3. **External factors impact performance** - Competition, seasonality affect outcomes
4. **Historical data may not predict future** - Past performance isn't guaranteed
5. **Cannot account for creative changes** - New creative changes the equation
6. **Audience sizes are estimates** - Actual reach varies

---

## Quality Checklist

Before delivering recommendations:
- [ ] All campaigns categorized by efficiency
- [ ] Marginal CPA estimated where data allows
- [ ] Diminishing returns indicators assessed
- [ ] Funnel balance evaluated
- [ ] Specific dollar amounts for changes
- [ ] Impact projections with assumptions stated
- [ ] Implementation timeline provided
- [ ] Risks and guardrails documented
