---
name: facebook-ads-account-auditor
description: Audits Meta Ads accounts for structural issues, pixel health, audience overlap, and budget efficiency. Identifies hidden problems costing money. Use when user asks "is my account set up correctly?" or wants health assessment.
---

# Facebook Ads Account Auditor

Your Meta account is either your foundation or your bottleneck. Find out which.

## Core Philosophy

**Most Facebook accounts are broken in ways you don't notice.**

They look fine on the surface—campaigns are running, budgets are spending. But underneath:
- Pixels aren't tracking conversions properly
- Audiences are overlapping and competing against themselves
- Campaign structure is fragmenting data so the algorithm can't learn
- Conversion events are misconfigured or firing on the wrong actions
- Creative fatigue has set in but nobody noticed

**The algorithm can only optimize what it can measure.** Bad tracking = bad optimization. Fragmented structure = fragmented learning. Overlapping audiences = you bidding against yourself.

This audit identifies the hidden problems that are silently draining your budget.

---

## Required Context

### Must Have

1. **Account Structure Overview**
   - Number of active campaigns
   - Campaign names and objectives
   - Ad set count per campaign
   - Current daily/monthly budget allocation

2. **Performance Data (Last 30 Days)**
   - Total spend
   - Total conversions (purchases, leads, etc.)
   - CPA or CPL
   - ROAS (if e-commerce)
   - CTR and CPM

3. **Tracking Setup**
   - Pixel installed? (Y/N)
   - Which events are configured?
   - Conversions API enabled? (Y/N)
   - What conversion event are you optimizing for?

### Strongly Recommended

4. **Audience Information**
   - Types of audiences used (Custom, Lookalike, Broad/Advantage+)
   - Audience sizes
   - Any audience overlap concerns?

5. **Creative Status**
   - How many active ads per ad set?
   - When was last new creative added?
   - Creative types (static, video, carousel, etc.)

### Nice to Have

6. **Historical Context**
   - How long has account been running?
   - Any major changes in last 90 days?
   - Previous CPA/ROAS benchmarks

---

## Audit Framework

### Phase 1: Pixel & Tracking Health

**Critical Questions:**
- Is the pixel firing correctly on all pages?
- Are conversion events properly configured?
- Is there event deduplication between Pixel and CAPI?
- Are you optimizing for the right conversion event?

**Assessment Matrix:**

| Issue | Symptom | Severity | Fix Priority |
|-------|---------|----------|--------------|
| No Pixel | Zero events tracked | 🔴 Critical | Immediate |
| Pixel fires, no CAPI | 30-40% data loss | 🟡 High | This week |
| Wrong conversion event | Optimizing for wrong action | 🔴 Critical | Immediate |
| No event deduplication | Double-counting conversions | 🟡 Medium | This week |
| PageView only | No conversion tracking | 🔴 Critical | Immediate |
| Events fire on wrong trigger | Inflated/deflated metrics | 🔴 Critical | Immediate |

**Tracking Health Score:**

| Score | Status | Meaning |
|-------|--------|---------|
| 🟢 Healthy | Pixel + CAPI + Deduplication + Correct Events | Full data, algorithm can optimize |
| 🟡 Degraded | Pixel only OR missing some events | 30-50% data loss, limited optimization |
| 🔴 Broken | No pixel OR wrong events OR major gaps | Algorithm flying blind |

---

### Phase 2: Campaign Structure Assessment

**The Consolidation Principle:**
Meta's algorithm needs data to learn. Fragmented campaigns = fragmented learning. The goal is **50+ conversions per ad set per week** for optimal learning.

**Structure Red Flags:**

| Issue | Why It's Bad | Evidence |
|-------|--------------|----------|
| Too many campaigns | Budget fragmentation, no campaign gets enough data | >10 active campaigns with <$100/day each |
| Too many ad sets | Learning phase never exits, inconsistent delivery | Ad sets with <10 conversions/week |
| 1 ad per ad set | No creative testing, no winner identification | Single ad ad sets |
| Duplicate audiences | Bidding against yourself, inflated CPMs | Same/similar audiences across ad sets |
| Mixed objectives | Confuses the algorithm | Conversions + Traffic in same strategy |

**Campaign Structure Score:**

| Score | Criteria |
|-------|----------|
| 🟢 Optimal | 3-5 campaigns, clear objectives, consolidated ad sets, 50+ conv/week/ad set |
| 🟡 Suboptimal | 6-10 campaigns, some fragmentation, 20-50 conv/week/ad set |
| 🔴 Fragmented | 10+ campaigns, heavy overlap, <20 conv/week/ad set |

---

### Phase 3: Audience Health Check

**Audience Overlap Analysis:**

When audiences overlap significantly (>30%), you're bidding against yourself. This drives up CPMs and wastes budget.

| Overlap Level | Impact | Action |
|---------------|--------|--------|
| 0-20% | Acceptable | Monitor |
| 20-40% | Moderate waste | Consider consolidating |
| 40%+ | Significant waste | Must consolidate or exclude |

**Audience Freshness:**

| Audience Type | Refresh Frequency | Stale After |
|---------------|-------------------|-------------|
| Website Custom (Purchase) | Real-time | N/A |
| Website Custom (Visitor) | Real-time | 180 days max window |
| Customer List | Manual upload | 90 days without refresh |
| Lookalike | Based on source | When source is stale |
| Engagement Audiences | Real-time | N/A |

**Audience Strategy Assessment:**

| Pattern | Verdict |
|---------|---------|
| Only Lookalikes | 🟡 Missing retargeting and broad |
| Only Retargeting | 🟡 Missing prospecting |
| Only Broad/Advantage+ | 🟡 Missing warm audiences |
| Balanced mix (Retargeting + Prospecting + Broad) | 🟢 Healthy funnel |
| Same audience in 5+ ad sets | 🔴 Severe overlap |

---

### Phase 4: Budget Efficiency Analysis

**Budget Distribution Check:**

| Pattern | Assessment |
|---------|------------|
| 80%+ budget on best performer | 🟡 Over-concentrated, scaling risk |
| Budget spread evenly regardless of performance | 🔴 Not optimizing for efficiency |
| Budget weighted by efficiency with testing allocation | 🟢 Optimal |
| <$20/day per ad set | 🔴 Insufficient for learning |

**Learning Phase Assessment:**

Ad sets need ~50 conversions in 7 days to exit learning phase.

| Daily Budget | Target CPA | Can Exit Learning? |
|--------------|------------|-------------------|
| $50 | $10 | 🟢 Yes (5 conv/day × 7 = 35, close) |
| $50 | $50 | 🔴 No (1 conv/day × 7 = 7) |
| $200 | $50 | 🟢 Yes (4 conv/day × 7 = 28, acceptable) |
| $100 | $100 | 🔴 No (1 conv/day × 7 = 7) |

**Formula:** Daily Budget ÷ Target CPA × 7 days ≥ 50 conversions

---

### Phase 5: Creative Health Assessment

**Creative Fatigue Indicators:**

| Metric | Healthy | Warning | Fatigued |
|--------|---------|---------|----------|
| Frequency (7-day) | <2.0 | 2.0-3.5 | >3.5 |
| CTR trend | Stable/Up | -10-20% | >20% decline |
| CPM trend | Stable | +10-20% | >20% increase |
| Conversion rate | Stable/Up | -10-20% | >20% decline |

**Creative Volume Assessment:**

| Ads per Ad Set | Verdict |
|----------------|---------|
| 1 ad | 🔴 No testing, no optimization |
| 2-3 ads | 🟡 Minimal testing |
| 4-6 ads | 🟢 Good testing volume |
| 10+ ads | 🟡 Too fragmented, hard to get signal |

**Creative Diversity Check:**

| Pattern | Assessment |
|---------|------------|
| All static images | 🟡 Missing video engagement |
| All video | 🟡 Missing quick-load static |
| Mix of static + video + carousel | 🟢 Healthy diversity |
| Same creative running 60+ days | 🔴 Likely fatigued |
| No new creative in 30+ days | 🟡 Testing stagnant |

---

## Output Format

```
═══════════════════════════════════════════════════════════════════
FACEBOOK ADS ACCOUNT AUDIT
Account: [Account Name]
Audit Date: [Date]
Period Analyzed: [Date Range]
═══════════════════════════════════════════════════════════════════

📊 EXECUTIVE SUMMARY
────────────────────────────────────────────────────────────────────
Overall Health Score: [🟢 Healthy / 🟡 Needs Work / 🔴 Critical Issues]

| Area | Score | Priority |
|------|-------|----------|
| Pixel & Tracking | [🟢/🟡/🔴] | [High/Medium/Low] |
| Campaign Structure | [🟢/🟡/🔴] | [High/Medium/Low] |
| Audience Health | [🟢/🟡/🔴] | [High/Medium/Low] |
| Budget Efficiency | [🟢/🟡/🔴] | [High/Medium/Low] |
| Creative Health | [🟢/🟡/🔴] | [High/Medium/Low] |

💰 ESTIMATED IMPACT
Current monthly spend: $X
Estimated waste from issues: $X-$X (X-X%)
Potential savings with fixes: $X-$X/month

═══════════════════════════════════════════════════════════════════

🔍 DETAILED FINDINGS
────────────────────────────────────────────────────────────────────

### 1. PIXEL & TRACKING [🟢/🟡/🔴]

**Current State:**
- Pixel Status: [Installed/Not Installed]
- CAPI Status: [Enabled/Not Enabled]
- Events Configured: [List events]
- Optimization Event: [Event name]
- Deduplication: [Yes/No]

**Issues Found:**
1. [Issue description]
   - Impact: [What this costs you]
   - Fix: [Specific action to take]

**Tracking Recommendations:**
- [ ] [Action item 1]
- [ ] [Action item 2]

────────────────────────────────────────────────────────────────────

### 2. CAMPAIGN STRUCTURE [🟢/🟡/🔴]

**Current State:**
- Active Campaigns: [Number]
- Total Ad Sets: [Number]
- Total Ads: [Number]
- Avg. Conversions per Ad Set/Week: [Number]

**Structure Analysis:**

| Campaign | Objective | Ad Sets | Weekly Conv | Status |
|----------|-----------|---------|-------------|--------|
| [Name] | [Obj] | [#] | [#] | [🟢/🟡/🔴] |

**Issues Found:**
1. [Issue description]
   - Impact: [What this costs you]
   - Fix: [Specific action to take]

**Structure Recommendations:**
- [ ] [Action item 1]
- [ ] [Action item 2]

────────────────────────────────────────────────────────────────────

### 3. AUDIENCE HEALTH [🟢/🟡/🔴]

**Current Audiences:**

| Audience | Type | Size | Used In | Overlap Risk |
|----------|------|------|---------|--------------|
| [Name] | [Type] | [Size] | [# ad sets] | [Low/Med/High] |

**Audience Mix:**
- Retargeting: [X]%
- Prospecting (Lookalikes): [X]%
- Broad/Advantage+: [X]%

**Issues Found:**
1. [Issue description]
   - Impact: [What this costs you]
   - Fix: [Specific action to take]

**Audience Recommendations:**
- [ ] [Action item 1]
- [ ] [Action item 2]

────────────────────────────────────────────────────────────────────

### 4. BUDGET EFFICIENCY [🟢/🟡/🔴]

**Budget Distribution:**

| Campaign | Daily Budget | % of Total | CPA | Efficiency |
|----------|--------------|------------|-----|------------|
| [Name] | $[X] | [X]% | $[X] | [🟢/🟡/🔴] |

**Learning Phase Status:**

| Ad Set | Daily Budget | Target CPA | Conv/Week | Learning Status |
|--------|--------------|------------|-----------|-----------------|
| [Name] | $[X] | $[X] | [#] | [Active/Exited/Limited] |

**Issues Found:**
1. [Issue description]
   - Impact: [What this costs you]
   - Fix: [Specific action to take]

**Budget Recommendations:**
- [ ] [Action item 1]
- [ ] [Action item 2]

────────────────────────────────────────────────────────────────────

### 5. CREATIVE HEALTH [🟢/🟡/🔴]

**Creative Inventory:**
- Total Active Ads: [Number]
- Avg. Ads per Ad Set: [Number]
- Creative Types: [Static: X, Video: X, Carousel: X]
- Oldest Active Creative: [Age in days]
- Last New Creative Added: [Date]

**Fatigue Analysis:**

| Ad | Age | Frequency | CTR Trend | Status |
|----|-----|-----------|-----------|--------|
| [Name] | [Days] | [X] | [Trend] | [🟢/🟡/🔴] |

**Issues Found:**
1. [Issue description]
   - Impact: [What this costs you]
   - Fix: [Specific action to take]

**Creative Recommendations:**
- [ ] [Action item 1]
- [ ] [Action item 2]

═══════════════════════════════════════════════════════════════════

🎯 PRIORITIZED ACTION PLAN
────────────────────────────────────────────────────────────────────

### IMMEDIATE (This Week)
1. [Highest priority fix]
2. [Second priority fix]

### SHORT-TERM (Next 2 Weeks)
3. [Fix]
4. [Fix]

### ONGOING
5. [Maintenance item]
6. [Maintenance item]

═══════════════════════════════════════════════════════════════════

📈 EXPECTED OUTCOMES
────────────────────────────────────────────────────────────────────

If all recommendations implemented:
- Expected CPA reduction: [X-X]%
- Expected ROAS improvement: [X-X]%
- Estimated monthly savings: $[X]-$[X]
- Timeline to see results: [X-X weeks]

═══════════════════════════════════════════════════════════════════
```

---

## Common Scenarios

### Scenario 1: "Everything looks fine but CPA keeps increasing"
**Likely Issues:**
- Creative fatigue (check frequency and CTR trends)
- Audience saturation (check audience size vs. spend)
- iOS 14.5 tracking gaps (check CAPI implementation)
- Competition increase (check CPM trends)

**Verdict:** Deep dive into creative freshness and tracking completeness first.

### Scenario 2: "Learning Phase Limited on all ad sets"
**Likely Issues:**
- Budget too low for target CPA
- Too many ad sets fragmenting conversions
- Wrong conversion event (too rare)

**Verdict:** Consolidate ad sets and/or increase budgets.

### Scenario 3: "Lots of clicks but no conversions"
**Likely Issues:**
- Wrong audience (traffic, not buyers)
- Landing page issues (not a Facebook problem)
- Pixel not firing on conversion page
- Optimizing for wrong event

**Verdict:** Check pixel fires on thank you/confirmation page first.

### Scenario 4: "CPMs are really high"
**Likely Issues:**
- Audience overlap (bidding against yourself)
- Small audience size (<100k for prospecting)
- Low relevance/quality score
- Competitive period (Q4, holidays)

**Verdict:** Check audience overlap in Ads Manager and audience sizes.

### Scenario 5: "New campaigns don't perform like old ones"
**Likely Issues:**
- Different audience quality
- Creative hasn't been tested
- Attribution window differences
- Algorithm still learning

**Verdict:** Give 7-14 days and 50+ conversions before judging.

---

## Limitations

1. **Cannot access actual Ads Manager** - Relies on user-provided data
2. **Cannot see pixel implementation** - Can only assess based on reported events
3. **Cannot calculate exact audience overlap** - User must check in Ads Manager
4. **Cannot predict algorithm behavior** - Can only apply best practices
5. **Market conditions vary** - Benchmarks are guidelines, not guarantees
6. **iOS 14.5+ impact varies** - Tracking gaps differ by audience and setup

---

## Quality Checklist

Before delivering audit:
- [ ] All five areas assessed (Tracking, Structure, Audience, Budget, Creative)
- [ ] Each issue has specific impact and fix
- [ ] Recommendations are prioritized by impact
- [ ] Action items are specific and actionable
- [ ] Expected outcomes are realistic, not overpromised
- [ ] Limitations acknowledged where data is incomplete
