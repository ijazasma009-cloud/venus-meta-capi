---
name: cross-platform-budget-allocator
description: Optimizes budget allocation across multiple advertising platforms (Google, Meta, TikTok, LinkedIn, Microsoft) based on performance data, goals, and constraints. Triggers when user wants to decide how to split budget between platforms, rebalance channel mix, or asks "how should I allocate my $X budget across channels?" Provides data-driven allocation with clear rationale.
---

# Cross-Platform Budget Allocator

Stop guessing. Start allocating with data.

## Core Philosophy

**Every dollar should earn its place.** Platform loyalty is expensive—money flows to performance.

**The Allocation Paradox:** Your best platform today might not be your best platform at 2x the budget. Efficiency curves are different for every channel.

**The Three Principles of Allocation:**
1. **Marginal returns matter:** $1,000 more to Google might yield less than $1,000 to Meta
2. **Diminishing returns are real:** Every platform has an efficiency ceiling
3. **Portfolio thinking wins:** Diversification protects against platform volatility

---

## Required Context

### Must Have

**1. Platform Performance Data**
For each platform currently running:
- Monthly spend
- Conversions (or revenue)
- CPA (or ROAS)
- Trend direction (improving/stable/declining)

**2. Budget Parameters**
- Total budget to allocate
- Time period (monthly/quarterly)
- Flexibility (fixed total vs. range)

**3. Business Goals**
- Primary KPI (CPA, ROAS, volume, brand awareness)
- Target efficiency metrics
- Growth vs. efficiency priority

### Strongly Recommended

**4. Platform-Specific Context**
- Impression share / audience saturation data
- Historical performance at different spend levels
- Learning phase or scaling status

**5. Constraints**
- Platform minimums (can't go below $X)
- Platform maximums (caps)
- New platform testing budget
- Brand vs. non-brand split requirements

### Nice to Have

- Attribution model being used
- Customer journey insights (which platform drives awareness vs. conversion)
- Competitive landscape by platform
- Seasonality patterns
- Previous allocation experiments

---

## Allocation Framework

### Step 1: Performance Baseline

**Efficiency Ranking:**
Rank platforms by primary KPI (CPA or ROAS)

| Rank | Platform | CPA | vs. Target | Trend |
|------|----------|-----|------------|-------|
| 1 | [Best] | $X | -X% | [→↑↓] |
| 2 | [Second] | $X | X% | [→↑↓] |
| ... | ... | ... | ... | ... |

**Volume vs. Efficiency Matrix:**

```
                    HIGH EFFICIENCY
                          │
         SCALE            │           MAXIMIZE
    (High volume,         │      (High volume,
     good efficiency)     │       great efficiency)
                          │
    ──────────────────────┼──────────────────────
                          │
         TEST/CUT         │           NICHE
    (Low volume,          │      (Low volume,
     poor efficiency)     │       great efficiency)
                          │
                    LOW EFFICIENCY
```

---

### Step 2: Marginal Return Analysis

**Key Question:** If I add $1,000 to each platform, what do I get?

**Estimating Marginal CPA:**
- Platform at <50% impression share: Likely similar CPA on incremental spend
- Platform at 50-70% impression share: Expect 10-20% CPA increase
- Platform at >70% impression share: Expect 20-40% CPA increase
- Platform in "Learning Limited": May improve with more budget

**Efficiency Curve Patterns:**

```
CPA
 │
 │                              ╭────── Saturated
 │                         ╭────╯
 │                    ╭────╯
 │               ╭────╯
 │          ╭────╯
 │     ╭────╯
 │╭────╯
 └─────────────────────────────────────── Spend
   Sweet Spot        Diminishing       Ceiling
```

---

### Step 3: Allocation Models

**Model A: Efficiency-Weighted Allocation**
Allocate proportionally to efficiency (inverse of CPA)

```
Platform Share = (1/Platform CPA) / Sum(1/All CPAs)
```

Best for: Maximizing total conversions at target efficiency

**Model B: Volume-Weighted with Efficiency Floor**
Allocate to platforms meeting efficiency threshold, weighted by current volume

```
If CPA < Target: Eligible for budget
Platform Share = Platform Volume / Total Eligible Volume
```

Best for: Scaling while maintaining efficiency standards

**Model C: Marginal Return Optimization**
Allocate incremental dollars to platform with best marginal return

```
1. Start with minimum allocations
2. Add $1K to platform with best projected marginal CPA
3. Repeat until budget exhausted
```

Best for: Maximizing efficiency at any budget level

**Model D: Portfolio Diversification**
Set minimum/maximum caps to ensure diversification

```
No platform > 50% of total budget
No platform < 10% of total budget (if running)
Testing budget: 10-15% to new/experimental platforms
```

Best for: Risk management and platform dependency reduction

---

### Step 4: Constraint Application

**Common Constraints:**

| Constraint Type | How to Handle |
|-----------------|---------------|
| Platform minimum | Set floor, allocate remaining optimally |
| Platform maximum | Set ceiling, reallocate overflow to next best |
| Brand budget | Carve out first, optimize non-brand separately |
| Testing budget | Reserve %, don't include in optimization |
| Seasonal adjustment | Apply multipliers to base allocation |

---

### Step 5: Scenario Modeling

**Always model three scenarios:**

1. **Conservative:** Prioritize proven performers, minimal change
2. **Balanced:** Optimize based on data, moderate reallocation
3. **Aggressive:** Chase highest marginal returns, significant shifts

---

## Platform-Specific Considerations

### Google Ads
- **Strengths:** High intent, measurable, scalable
- **Scaling signals:** Impression share <80%, budget limited campaigns
- **Watch for:** CPC inflation in competitive auctions
- **Typical efficiency curve:** Gradual decline after 70% IS

### Meta Ads
- **Strengths:** Broad reach, creative-driven, discovery
- **Scaling signals:** Frequency <3, audience not exhausted
- **Watch for:** Creative fatigue, iOS attribution gaps
- **Typical efficiency curve:** Sharp decline when frequency spikes

### TikTok Ads
- **Strengths:** Low CPMs, engaged audience, viral potential
- **Scaling signals:** New platform opportunity, creative performing
- **Watch for:** Conversion tracking maturity, audience fit
- **Typical efficiency curve:** Volatile, creative-dependent

### LinkedIn Ads
- **Strengths:** B2B targeting precision, professional context
- **Scaling signals:** Audience size >50K, frequency manageable
- **Watch for:** High CPMs ($8-15), small audiences exhaust fast
- **Typical efficiency curve:** Quick saturation in niche audiences

### Microsoft Ads
- **Strengths:** Lower CPCs, older demographic, desktop heavy
- **Scaling signals:** Google campaigns profitable, IS headroom
- **Watch for:** Lower volume, import quality issues
- **Typical efficiency curve:** Similar to Google, lower ceiling

---

## Output Format

### Budget Allocation Summary

```
═══════════════════════════════════════════════════════════════
CROSS-PLATFORM BUDGET ALLOCATION
Total Budget: $[X]/month
Primary Goal: [CPA/ROAS/Volume]
Allocation Model: [Model Used]
═══════════════════════════════════════════════════════════════
```

---

### Current State Analysis

**Performance by Platform:**

| Platform | Current Spend | Conversions | CPA | vs. Target | ROAS | Trend |
|----------|--------------|-------------|-----|------------|------|-------|
| Google Ads | $[X] | [X] | $[X] | [X]% | [X] | [→↑↓] |
| Meta Ads | $[X] | [X] | $[X] | [X]% | [X] | [→↑↓] |
| [Platform] | $[X] | [X] | $[X] | [X]% | [X] | [→↑↓] |
| **Total** | $[X] | [X] | $[X] | [X]% | [X] | |

**Current Allocation:**
```
Google Ads:  ████████████████████ [X]% ($[X])
Meta Ads:    ████████████ [X]% ($[X])
[Platform]:  ████ [X]% ($[X])
```

**Efficiency Ranking:** [Platform 1] > [Platform 2] > [Platform 3]

**Scaling Headroom Assessment:**

| Platform | Saturation Signal | Headroom | Notes |
|----------|-------------------|----------|-------|
| Google | [X]% impression share | [High/Med/Low] | [Notes] |
| Meta | [X] frequency | [High/Med/Low] | [Notes] |
| [Platform] | [Signal] | [High/Med/Low] | [Notes] |

---

### Recommended Allocation

**Model Used:** [Model Name]
**Rationale:** [One sentence explanation]

| Platform | Current | Recommended | Change | % of Total |
|----------|---------|-------------|--------|------------|
| Google Ads | $[X] | $[X] | [+/-$X] | [X]% |
| Meta Ads | $[X] | $[X] | [+/-$X] | [X]% |
| [Platform] | $[X] | $[X] | [+/-$X] | [X]% |
| Testing/New | $[X] | $[X] | [+/-$X] | [X]% |
| **Total** | $[X] | $[X] | | 100% |

**Visual Comparison:**
```
CURRENT                         RECOMMENDED
Google:  ████████████ 40%       Google:  ██████████████ 45%
Meta:    ██████████ 35%         Meta:    ████████ 30%
TikTok:  ████ 15%               TikTok:  ██████ 20%
Other:   ██ 10%                 Other:   █ 5%
```

---

### Allocation Rationale

**Why increase [Platform]:**
- [Reason 1 with data]
- [Reason 2 with data]

**Why decrease [Platform]:**
- [Reason 1 with data]
- [Reason 2 with data]

**Why maintain [Platform]:**
- [Reason with data]

---

### Projected Outcomes

**At Recommended Allocation:**

| Metric | Current | Projected | Change |
|--------|---------|-----------|--------|
| Total Conversions | [X] | [X] | [+/-X]% |
| Blended CPA | $[X] | $[X] | [+/-X]% |
| Blended ROAS | [X] | [X] | [+/-X]% |

**Assumptions:**
- [Assumption 1]
- [Assumption 2]
- [Assumption 3]

**Confidence Level:** [High/Medium/Low]
- High: Historical data supports projections
- Medium: Some extrapolation required
- Low: Significant unknowns

---

### Scenario Comparison

| Scenario | Google | Meta | [Other] | Projected CPA | Projected Volume |
|----------|--------|------|---------|---------------|------------------|
| Conservative | $[X] | $[X] | $[X] | $[X] | [X] |
| **Balanced (Rec)** | $[X] | $[X] | $[X] | $[X] | [X] |
| Aggressive | $[X] | $[X] | $[X] | $[X] | [X] |

**Conservative:** [Description]
**Balanced:** [Description]
**Aggressive:** [Description]

---

### Implementation Plan

**Phase 1: Immediate Changes (Week 1)**
- [ ] [Specific budget change]
- [ ] [Specific budget change]

**Phase 2: Gradual Shift (Weeks 2-4)**
- [ ] [Gradual adjustment]
- [ ] [Gradual adjustment]

**Phase 3: Optimization (Week 4+)**
- [ ] Review performance at new levels
- [ ] Fine-tune based on actual results

**Change Management:**
- Don't shift >25% of any platform's budget at once
- Allow 2 weeks for algorithms to adjust
- Monitor daily for first week after changes

---

### Monitoring & Rebalancing

**Weekly Check:**
- [ ] CPA by platform vs. projection
- [ ] Spend pacing vs. allocation
- [ ] Any platform hitting constraints

**Rebalancing Triggers:**
- Platform CPA exceeds projection by >20% for 2 weeks
- Platform underdelivering by >15% for 2 weeks
- Major external change (algorithm update, seasonality shift)

**Quarterly Review:**
- Full reallocation analysis
- Update efficiency curves
- Reassess platform priorities

---

### Risks & Mitigation

**Risk 1: [Platform] underperforms at higher spend**
- Likelihood: [X]
- Impact: [X]
- Mitigation: Gradual scaling, weekly monitoring, quick pullback plan

**Risk 2: [Platform] can't absorb budget decrease**
- Likelihood: [X]
- Impact: [X]
- Mitigation: Reallocate gradually, maintain campaigns for quick scale-back

**Risk 3: Attribution differences distort comparison**
- Likelihood: [X]
- Impact: [X]
- Mitigation: Use consistent windows, acknowledge limitations, focus on trends

---

## Limitations

**I can provide:**
- Data-driven allocation recommendations
- Scenario modeling
- Implementation guidance
- Monitoring framework

**I cannot provide:**
- Cross-platform attribution modeling
- Incrementality measurement
- Platform-specific optimization tactics
- Creative strategy by platform

**For better allocations, also provide:**
- Historical performance at different spend levels
- Impression share / saturation data
- Customer journey insights
- Attribution window consistency info

---

## Quality Checklist

Before delivering allocation:
- [ ] All platforms included with current performance
- [ ] Allocation sums to total budget
- [ ] Rationale provided for each change
- [ ] Constraints respected
- [ ] Projections include assumptions
- [ ] Implementation plan is gradual (not shock changes)
- [ ] Monitoring framework included
- [ ] Risks identified with mitigations
