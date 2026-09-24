---
name: bid-strategy-auditor
description: Evaluates whether your Google Ads bid strategy is helping or hurting performance. Triggers when user questions Smart Bidding effectiveness, wants to compare bid strategies, or asks "should I use manual or automated bidding?" Analyzes conversion data, learning period status, and strategy fit. Provides honest assessment with switch recommendations when warranted.
---

# Bid Strategy Auditor

Is Google's AI actually helping you, or just spending your money? Find out.

## Core Philosophy

**Smart Bidding isn't always smart.** It works brilliantly in the right conditions and fails silently in the wrong ones.

**The Uncomfortable Truth:**
- Google profits whether Smart Bidding works for you or not
- Most accounts don't have enough data for ML to work properly
- "Learning" can be an expensive excuse for poor performance

**This Audit Answers:**
1. Is your current bid strategy appropriate for your data volume?
2. Is it actually outperforming simpler alternatives?
3. What would you need to change for it to work better?

---

## Required Context

### Must Have

**1. Current Bid Strategy**
- Strategy type (Target CPA, Target ROAS, Max Conversions, Max Conv Value, Manual CPC, Enhanced CPC)
- How long it's been running
- Target values (if applicable)

**2. Performance Data (Last 30 Days)**
- Conversions
- Conversion value (if using value-based bidding)
- Cost
- CPA or ROAS achieved

**3. Campaign-Level Data**
Per campaign using the strategy:
- Conversions
- Cost
- CPA/ROAS

### Strongly Recommended

**4. Historical Comparison**
Performance BEFORE current strategy vs. AFTER
- Or: Last 30 days vs. prior 30 days

**5. Conversion Volume Context**
- Monthly conversion count
- Conversion lag (days from click to conversion)

### Nice to Have

- Auction insights (impression share trends)
- Bid strategy status (Learning, Limited, Eligible)
- Any recent changes (budget, targets, structure)
- Seasonality factors

---

## Bid Strategy Requirements

### Minimum Data Thresholds

Google's official recommendations are minimums. Real-world requirements are higher.

| Strategy | Google Says | Reality Check | Why |
|----------|-------------|---------------|-----|
| Target CPA | 15 conv/month | 30-50 conv/month | Need statistical significance |
| Target ROAS | 15 conv/month | 50+ conv/month | Value variance needs more data |
| Max Conversions | 15 conv/month | 30+ conv/month | No ceiling without volume |
| Max Conv Value | 15 conv/month | 50+ conv/month | Value optimization is harder |
| Portfolio Strategies | Varies | 100+ conv/month across portfolio | Aggregation helps but has limits |

### Strategy-Specific Red Flags

**Target CPA:**
- Actual CPA consistently 30%+ above target
- Strategy in "Learning" for 2+ weeks
- Wild CPA swings day-to-day
- Impression share dropping while CPA rising

**Target ROAS:**
- Actual ROAS consistently 30%+ below target
- Conversion value highly variable
- Low conversion volume with high-value outliers
- Strategy "Limited by budget" while missing ROAS

**Max Conversions:**
- CPA increasing month-over-month
- Conversion quality declining
- Strategy spending budget but CPA rising
- No efficiency improvement over time

**Max Conversion Value:**
- Low-value conversions increasing
- High-value conversion rate dropping
- Average order value declining
- Strategy chasing easy wins vs. valuable ones

---

## Audit Framework

### Phase 1: Data Sufficiency Check

**Question:** Does this account have enough data for the chosen strategy?

**Assessment Matrix:**

| Monthly Conversions | Recommended Strategy |
|--------------------|---------------------|
| < 15 | Manual CPC or Enhanced CPC |
| 15-30 | Enhanced CPC or cautious Target CPA |
| 30-50 | Target CPA viable |
| 50-100 | Target CPA/ROAS comfortable |
| 100+ | Any strategy viable, portfolio recommended |

**Conversion Lag Factor:**
- Lag > 7 days: Add 2 weeks to learning period expectations
- Lag > 14 days: Consider if Smart Bidding can even work (delayed signal problem)

---

### Phase 2: Performance Reality Check

**Question:** Is the strategy actually delivering?

**Target CPA Assessment:**

| Actual vs Target | Assessment | Recommendation |
|------------------|------------|----------------|
| < 90% of target | Over-delivering | Consider lowering target to capture more volume |
| 90-110% of target | On target | Maintain |
| 110-130% of target | Underperforming | Check for issues, consider target adjustment |
| > 130% of target | Failing | Strategy change likely needed |

**Target ROAS Assessment:**

| Actual vs Target | Assessment | Recommendation |
|------------------|------------|----------------|
| > 110% of target | Over-delivering | Consider lowering target for more volume |
| 90-110% of target | On target | Maintain |
| 70-90% of target | Underperforming | Check for issues |
| < 70% of target | Failing | Strategy change likely needed |

**Trend Analysis:**
- Improving trend: Strategy may still be learning/optimizing
- Flat trend: Strategy has likely plateaued
- Declining trend: Strategy is degrading, intervention needed

---

### Phase 3: Alternative Comparison

**Question:** Would a different strategy perform better?

**Manual CPC Benchmark:**
- If you have historical manual CPC data, compare directly
- If not, estimate: What CPA would you achieve at avg CPC with current CVR?

**Strategy Comparison Framework:**

```
Current: Target CPA at $45 (target: $40)
Calculation: If CVR is 3% and avg CPC is $1.20
Manual CPC theoretical CPA = $1.20 / 0.03 = $40

Verdict: Manual CPC might match or beat current Smart Bidding
```

**Portfolio vs. Individual:**
- If running same strategy across multiple campaigns
- Could consolidation into portfolio improve performance?
- More data = better ML performance

---

### Phase 4: Diagnosis

**If Strategy is Underperforming, Why?**

**Data Issues:**
- Not enough conversions (most common)
- Conversion lag too long
- Conversion tracking issues
- Mixed conversion types (leads + sales in same campaign)

**Target Issues:**
- Target too aggressive (strategy can't hit it)
- Target too conservative (leaving money on table)
- Target doesn't reflect true business value

**Structure Issues:**
- Too many campaigns fragmenting data
- Audience overlap causing competition
- Budget limiting before strategy can optimize

**External Issues:**
- Recent major changes disrupted learning
- Seasonality not accounted for
- Competitive landscape shifted

---

## Output Format

### Executive Summary

```
CURRENT STRATEGY: [Strategy Name]
RUNNING SINCE: [Date/Duration]
VERDICT: 🟢 Working / 🟡 Marginal / 🔴 Not Working

[2-3 sentence summary of findings and primary recommendation]
```

---

### 📊 Data Sufficiency Assessment

| Requirement | Your Data | Threshold | Status |
|-------------|-----------|-----------|--------|
| Monthly Conversions | [X] | 30+ recommended | ✅/⚠️/❌ |
| Conversion Lag | [X] days | < 7 days ideal | ✅/⚠️/❌ |
| Time on Strategy | [X] weeks | 4+ weeks | ✅/⚠️/❌ |
| Strategy Status | [Status] | "Eligible" | ✅/⚠️/❌ |

**Data Verdict:** [Sufficient / Borderline / Insufficient] for [current strategy]

---

### 📈 Performance Analysis

**Target vs. Actual:**

| Metric | Target | Actual | Variance | Trend |
|--------|--------|--------|----------|-------|
| CPA/ROAS | $X / X.X | $X / X.X | +X% | ↑/↓/→ |

**Performance Verdict:** [On Target / Underperforming / Failing]

**Trend Analysis:**
- Week 1-2: [Performance]
- Week 3-4: [Performance]
- Direction: [Improving / Flat / Declining]

---

### 🔍 Diagnosis

**Primary Issue:** [What's causing underperformance]

**Contributing Factors:**
1. [Factor] - [Evidence]
2. [Factor] - [Evidence]

**What the Data Shows:**
[Specific observations that support the diagnosis]

---

### 💡 Recommendations

**Option A: [Primary Recommendation]**
- What: [Specific change]
- Why: [Rationale based on diagnosis]
- Expected Impact: [What should improve]
- Risk: [What could go wrong]
- Timeline: [When to evaluate]

**Option B: [Alternative]**
- What: [Specific change]
- Why: [When this makes more sense]
- Expected Impact: [What should improve]

**What NOT to Do:**
- [Common mistake to avoid given this situation]

---

### 🧪 If Switching Strategies

**Recommended Switch:** [From] → [To]

**Transition Plan:**
1. [Step 1 with timing]
2. [Step 2 with timing]
3. [Step 3 with timing]

**Success Metrics:**
- Primary: [Metric] should [improve/stabilize] within [timeframe]
- Secondary: [Metric] should [expectation]

**Rollback Criteria:**
- If [condition], revert to [previous strategy]

---

### ⚠️ Watch Items

- [Thing to monitor] - Check in [timeframe]
- [Thing to monitor] - Check in [timeframe]

---

## Common Scenarios & Verdicts

### Scenario 1: Low Volume + Target CPA
**Situation:** < 30 conversions/month on Target CPA
**Typical Finding:** CPA volatile, often above target
**Recommendation:** Switch to Enhanced CPC or Manual CPC
**Why:** Insufficient data for ML to learn patterns

### Scenario 2: Target ROAS Consistently Missing
**Situation:** ROAS 30%+ below target for 4+ weeks
**Typical Finding:** Strategy is "working" but not effectively
**Recommendation:** Either lower target or switch to Max Conv Value with caps
**Why:** Target may be unrealistic for current traffic quality

### Scenario 3: Max Conversions CPA Creep
**Situation:** CPA steadily increasing on Max Conversions
**Typical Finding:** No efficiency ceiling, strategy just spending
**Recommendation:** Switch to Target CPA with current CPA as starting target
**Why:** Need to give the algorithm a goal, not just "get more"

### Scenario 4: Strategy in "Learning" Forever
**Situation:** Status shows "Learning" for 2+ weeks
**Typical Finding:** Too many changes or insufficient data
**Recommendation:** Stabilize (stop changes for 2 weeks) or consolidate campaigns
**Why:** Every change restarts learning, perpetual learning = perpetual inefficiency

### Scenario 5: Great Performance, Low Volume
**Situation:** Hitting targets but impression share < 50%
**Typical Finding:** Strategy being too conservative
**Recommendation:** Gradually adjust targets to capture more volume
**Why:** Leaving money on the table by being too restrictive

---

## Limitations

**I can assess:**
- Data sufficiency for strategy type
- Performance vs. targets
- Trend direction
- Strategy fit diagnosis

**I cannot assess:**
- Conversion quality (need backend data)
- Competitive auction dynamics (need auction insights)
- Whether targets reflect true business value
- Incrementality of conversions

**For complete analysis, also provide:**
- Auction insights data
- Backend conversion quality metrics
- Business context for target setting
- Historical strategy performance comparisons

---

## Quality Checklist

Before delivering audit:
- [ ] Data sufficiency clearly assessed with thresholds
- [ ] Performance comparison uses appropriate benchmarks
- [ ] Diagnosis is evidence-based, not assumed
- [ ] Recommendations are specific and actionable
- [ ] Transition plan included if strategy switch recommended
- [ ] Risks and rollback criteria defined
- [ ] Timeline expectations set appropriately
- [ ] Avoided generic "it depends" conclusions
