---
name: meta-ads-performance-analyzer
description: Analyzes Meta Ads (Facebook/Instagram) campaign performance with breakdown by placement, creative, audience, and funnel stage. Triggers when user wants to understand Meta Ads performance, diagnose issues, find winners/losers, or asks "why is my Meta performance dropping?" Provides actionable insights with specific optimization recommendations.
---

# Meta Ads Performance Analyzer

Find what's working, what's bleeding money, and what to do about it.

## Core Philosophy

**Meta Ads are not Google Ads.** Different platform, different user intent, different optimization levers. Stop applying search mindset to social.

**The Meta Paradox:** Your best-performing ad today will be your worst performer in 30 days. Creative fatigue is the #1 killer of Meta campaigns.

**The Three Truths of Meta:**
1. **Creative is king:** 70% of performance variance comes from creative
2. **Audience breadth wins:** Narrow targeting is a tax on your CPMs
3. **The algorithm knows:** Fight less, feed more (give it data and budget)

---

## Required Context

### Must Have

**1. Campaign Overview**
- Current campaigns and objectives (Conversions, Traffic, Leads, etc.)
- Monthly spend (or daily budget)
- Time period for analysis (last 7, 14, 30 days)

**2. Core Metrics**
- Spend by campaign
- Results (conversions, leads, purchases)
- Cost per result (CPA, CPL, Cost per Purchase)
- ROAS (if applicable)

### Strongly Recommended

**3. Breakdown Data**
- Performance by ad set (audience)
- Performance by ad (creative)
- Performance by placement (Feed, Stories, Reels, etc.)
- Performance by device (Mobile vs Desktop)

**4. Funnel Metrics**
- Impressions and Reach
- CPM (Cost per 1,000 impressions)
- CTR (Click-through rate)
- CPC (Cost per click)
- Landing page conversion rate

### Nice to Have

- Frequency by ad set
- Audience overlap data
- Creative performance over time (for fatigue analysis)
- Comparison period data (this month vs last month)
- Attribution window settings
- Pixel/CAPI health data

---

## Performance Assessment Framework

### Level 1: Account Health Check

**Traffic Light Status:**

| Metric | Green | Yellow | Red |
|--------|-------|--------|-----|
| CPM | Below industry avg | At industry avg | 50%+ above avg |
| CTR | >1.5% | 1.0-1.5% | <1.0% |
| CPC | Below target | At target | Above target |
| CPA | Below target | At target | 20%+ above target |
| ROAS | Above target | At target | Below target |
| Frequency | <2.0 (7d) | 2.0-3.5 | >3.5 |

**Industry CPM Benchmarks (2024):**
- E-commerce: $10-15
- SaaS/B2B: $15-25
- Finance: $20-35
- Lead Gen: $8-15
- App Install: $5-12

---

### Level 2: Campaign Diagnosis

**Campaign Performance Tiers:**

| Tier | Criteria | Action |
|------|----------|--------|
| Tier 1: Winners | CPA <80% target, positive ROAS trend | Scale budget 20-30% |
| Tier 2: Performers | CPA 80-100% target, stable | Optimize, don't change budget |
| Tier 3: Borderline | CPA 100-130% target | Test new creative/audience |
| Tier 4: Losers | CPA >130% target for 7+ days | Pause or restructure |

**Diagnostic Questions:**
1. Is the problem at the top (CPM/CTR) or bottom (conversion rate)?
2. Is performance declining over time (fatigue) or was it always poor?
3. Is one element dragging down the whole (single bad ad set)?
4. Are you comparing apples to apples (same attribution window)?

---

### Level 3: Deep Dive Analysis

**A. Creative Analysis**
- Identify top 3 and bottom 3 creatives by CPA
- Check for creative fatigue (CTR decline >30% over 2 weeks)
- Assess creative diversity (formats, hooks, angles)
- Compare static vs video performance

**B. Audience Analysis**
- Identify winning audiences vs losers
- Check audience overlap (cannibalizing each other?)
- Evaluate audience size vs performance
- Compare Advantage+ audiences vs manual targeting

**C. Placement Analysis**
- Feed vs Stories vs Reels performance
- Instagram vs Facebook performance
- Automatic vs manual placement ROI
- Mobile vs Desktop breakdown

**D. Funnel Analysis**
- Where is the biggest drop-off?
- CPM → CTR → CPC → Conversion rate
- Which stage needs the most attention?

---

## Common Problem Patterns

### Pattern 1: High CPM, Low Delivery
**Symptoms:** CPMs 2-3x normal, campaigns struggling to spend
**Causes:**
- Audience too narrow (<1M people)
- Too many exclusions
- Low account spend history
- Auction overlap between ad sets
**Solutions:**
- Broaden targeting
- Consolidate ad sets
- Use Advantage+ audiences
- Increase budget to exit learning limited

### Pattern 2: Good CTR, Bad Conversion Rate
**Symptoms:** CTR >2%, but CPA way above target
**Causes:**
- Creative-landing page mismatch
- Wrong audience (curious but not buyers)
- Landing page issues
- Misleading ad copy
**Solutions:**
- Audit landing page experience
- Review audience quality vs quantity
- Ensure message match
- Check mobile landing page speed

### Pattern 3: Creative Fatigue
**Symptoms:** CTR declining 20%+ week over week, frequency rising
**Causes:**
- Same creative running too long
- Audience exhausted
- Not enough creative diversity
**Solutions:**
- Rotate in new creatives every 2-3 weeks
- Test new angles/hooks
- Expand audience
- Use dynamic creative

### Pattern 4: Learning Limited
**Symptoms:** "Learning Limited" status, volatile performance
**Causes:**
- Not enough conversions (need 50/week per ad set)
- Too many ad sets splitting budget
- Budget too low
- Too many constraints
**Solutions:**
- Consolidate ad sets
- Increase budgets
- Use campaign budget optimization (CBO)
- Simplify structure

### Pattern 5: Winning Creative Plateau
**Symptoms:** Best ad's performance flattening, can't find new winners
**Causes:**
- Testing process broken
- Not enough creative volume
- Testing wrong elements
**Solutions:**
- Increase creative testing velocity (3-5 new ads/week)
- Test hooks first, then bodies
- Analyze what made winners work
- Try new formats (UGC, Reels, Carousels)

---

## Output Format

### Performance Analysis Summary

```
═══════════════════════════════════════════════════════════════
META ADS PERFORMANCE ANALYSIS
Period: [Date Range]
Total Spend: $[X] | Results: [X] | CPA: $[X]
Health Score: [X]/100
═══════════════════════════════════════════════════════════════
```

---

### Account Health Dashboard

**Overall Status: [GREEN/YELLOW/RED]**

| Metric | Value | Benchmark | Status | Trend |
|--------|-------|-----------|--------|-------|
| CPM | $[X] | $[X] | [Status] | [↑↓→] |
| CTR | [X]% | [X]% | [Status] | [↑↓→] |
| CPC | $[X] | $[X] | [Status] | [↑↓→] |
| CPA | $[X] | $[X] | [Status] | [↑↓→] |
| ROAS | [X]x | [X]x | [Status] | [↑↓→] |
| Frequency | [X] | <3.0 | [Status] | [↑↓→] |

**Funnel Visualization:**
```
Impressions → Clicks → Landing Page → Conversion
[X]           [X]      [X]%           [X]%
             [X]% CTR  [X]% drop      [X]% CVR
```

---

### Campaign Performance Breakdown

**Tier 1 - Winners (Scale These)**
| Campaign | Spend | Results | CPA | vs Target | Action |
|----------|-------|---------|-----|-----------|--------|
| [Name] | $[X] | [X] | $[X] | -[X]% | Scale 25% |

**Tier 2 - Performers (Optimize)**
| Campaign | Spend | Results | CPA | vs Target | Action |
|----------|-------|---------|-----|-----------|--------|
| [Name] | $[X] | [X] | $[X] | [X]% | [Action] |

**Tier 3 - Borderline (Test/Fix)**
| Campaign | Spend | Results | CPA | vs Target | Action |
|----------|-------|---------|-----|-----------|--------|
| [Name] | $[X] | [X] | $[X] | +[X]% | [Action] |

**Tier 4 - Losers (Pause/Restructure)**
| Campaign | Spend | Results | CPA | vs Target | Action |
|----------|-------|---------|-----|-----------|--------|
| [Name] | $[X] | [X] | $[X] | +[X]% | Pause |

---

### Creative Performance Analysis

**Top Performers:**
| Ad Name | Spend | CPA | CTR | Hook Rate | Status |
|---------|-------|-----|-----|-----------|--------|
| [Name] | $[X] | $[X] | [X]% | [X]% | [Fresh/Fatigued] |

**Underperformers:**
| Ad Name | Spend | CPA | CTR | Issue | Recommendation |
|---------|-------|-----|-----|-------|----------------|
| [Name] | $[X] | $[X] | [X]% | [Issue] | [Action] |

**Creative Fatigue Alert:**
- [Ad Name]: CTR dropped [X]% in [X] days - ROTATE
- [Ad Name]: Frequency at [X] - audience exhausted

**Creative Mix Assessment:**
```
Current Mix:
- Static Images: [X]%
- Videos: [X]%
- Carousels: [X]%
- UGC: [X]%

Recommendation: [Assessment of mix health]
```

---

### Audience Performance Analysis

**Winning Audiences:**
| Audience | Size | Spend | CPA | CPM | Notes |
|----------|------|-------|-----|-----|-------|
| [Name] | [X]M | $[X] | $[X] | $[X] | [Notes] |

**Losing Audiences:**
| Audience | Size | Spend | CPA | Issue | Action |
|----------|------|-------|-----|-------|--------|
| [Name] | [X]M | $[X] | $[X] | [Issue] | [Action] |

**Audience Overlap Issues:**
- [Audience A] and [Audience B]: [X]% overlap - consolidate

**Targeting Recommendations:**
- [Recommendation 1]
- [Recommendation 2]

---

### Placement Performance

| Placement | Spend | CPA | CPM | CTR | Recommendation |
|-----------|-------|-----|-----|-----|----------------|
| FB Feed | $[X] | $[X] | $[X] | [X]% | [Action] |
| IG Feed | $[X] | $[X] | $[X] | [X]% | [Action] |
| IG Stories | $[X] | $[X] | $[X] | [X]% | [Action] |
| IG Reels | $[X] | $[X] | $[X] | [X]% | [Action] |
| FB Reels | $[X] | $[X] | $[X] | [X]% | [Action] |
| Audience Network | $[X] | $[X] | $[X] | [X]% | [Action] |

**Placement Strategy:**
[Assessment and recommendation for Advantage+ vs manual placements]

---

### Diagnosis & Root Cause

**Primary Issue:** [One sentence summary]

**Root Cause Analysis:**
```
Problem: [The symptom]
   ↓
Why: [First-level cause]
   ↓
Why: [Second-level cause]
   ↓
Root Cause: [The real issue to fix]
```

**Contributing Factors:**
1. [Factor 1]
2. [Factor 2]
3. [Factor 3]

---

### Action Plan

**Immediate (This Week):**
1. [ ] [Urgent action with specific details]
2. [ ] [Urgent action with specific details]

**Short-Term (Next 2 Weeks):**
1. [ ] [Action item]
2. [ ] [Action item]
3. [ ] [Action item]

**Medium-Term (Next Month):**
1. [ ] [Strategic action]
2. [ ] [Strategic action]

**Expected Impact:**
- If actions completed: CPA should improve by [X]% within [timeframe]
- Primary risk: [Risk and mitigation]

---

### Monitoring Checklist

Track these daily/weekly:
- [ ] CPA by campaign (daily)
- [ ] CTR trends by creative (daily)
- [ ] Frequency by ad set (every 3 days)
- [ ] Learning phase status (daily)
- [ ] Spend pacing vs budget (daily)

**Red Flag Triggers:**
- CPA increases >20% for 3+ days
- CTR drops >25% week-over-week
- Frequency exceeds 4.0 in 7 days
- Campaign stuck in "Learning Limited" for 7+ days

---

## Limitations

**I can provide:**
- Performance diagnosis and benchmarking
- Creative and audience analysis
- Specific optimization recommendations
- Root cause identification

**I cannot provide:**
- Creative design or copywriting
- Audience research/persona development
- Pixel/CAPI technical debugging
- Competitor intelligence from Ad Library

**For better analysis, also provide:**
- Screenshots of Ads Manager breakdowns
- Creative assets or thumbnails
- Landing page URLs
- Historical performance data (for trend analysis)

---

## Quality Checklist

Before delivering analysis:
- [ ] All campaigns categorized into performance tiers
- [ ] Root cause identified (not just symptoms)
- [ ] Actions are specific and prioritized
- [ ] Creative fatigue assessed
- [ ] Audience overlap considered
- [ ] Benchmarks appropriate for industry
- [ ] Recommendations match advertiser's capacity
- [ ] Expected impact quantified where possible
