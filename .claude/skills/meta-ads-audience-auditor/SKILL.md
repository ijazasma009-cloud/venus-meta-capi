---
name: meta-ads-audience-auditor
description: Audits Meta (Facebook/Instagram) ad audiences for efficiency and saturation. Triggers when user shares Meta Ads data, asks about audience overlap, wants to improve ROAS, or asks "why are my CPMs increasing?" Analyzes audience targeting, overlap, saturation, custom audiences, and lookalikes. Provides optimization recommendations for better performance.
---

# Meta Ads Audience Auditor

Get more from your Meta ad spend by targeting smarter.

## Core Philosophy

**Audience quality beats audience size.** A perfectly targeted 100K audience will outperform a poorly targeted 10M audience every time. The goal isn't reaching everyone—it's reaching the right people efficiently.

**The Goal:** Identify audience inefficiencies costing you money and optimize targeting for better ROAS.

**The Principle:** Systematic evaluation of audience health across overlap, saturation, quality, and structure.

---

## Required Context

### Must Have

**1. Audience Performance Data**
For each ad set/audience:
- Audience name/description
- Audience size
- Spend
- Impressions
- Reach
- Frequency
- CPM
- Results (conversions, leads, purchases)
- Cost per result

**2. Audience Configuration**
- Targeting type (interest, lookalike, custom, broad)
- Audience definition (what targeting is used)
- Exclusions applied

### Strongly Recommended

**3. Campaign Structure**
- Campaign objectives
- How audiences are organized
- Budget allocation across audiences

**4. Historical Context**
- How long audiences have been running
- Performance trends over time
- Any recent changes

### Nice to Have

- Audience overlap reports from Meta
- Conversion breakdown by placement
- Creative performance by audience
- Customer lifetime value data
- Pixel event data quality metrics

---

## Audit Framework

### The 6 Audience Health Dimensions

| Dimension | Focus | Impact |
|-----------|-------|--------|
| **Saturation** | Is the audience exhausted? | High |
| **Overlap** | Are audiences competing? | High |
| **Quality** | Is targeting precise? | High |
| **Structure** | Is organization logical? | Medium |
| **Custom Audiences** | Are seed audiences optimized? | High |
| **Lookalikes** | Are LALs configured correctly? | Medium |

---

### Dimension 1: Saturation Analysis

**Key Metrics:**

| Metric | Healthy | Warning | Critical |
|--------|---------|---------|----------|
| Frequency (7-day) | <2 | 2-4 | >4 |
| Frequency (30-day) | <4 | 4-8 | >8 |
| Reach % of Audience | <40% | 40-70% | >70% |
| CPM trend | Stable/Down | +10-25% | >+25% |
| CTR trend | Stable/Up | -10-25% | >-25% |

**Saturation Assessment:**

| Audience | Size | Reach | Freq (7d) | Freq (30d) | Status |
|----------|------|-------|-----------|------------|--------|
| [Audience 1] | X | X | X.X | X.X | 🟢/🟡/🔴 |
| [Audience 2] | X | X | X.X | X.X | 🟢/🟡/🔴 |

**Saturation Warning Signs:**
- Frequency climbing while results declining
- CPMs increasing without market explanation
- Same users seeing ads 5+ times
- Diminishing returns on spend increases
- Negative comments increasing

**Saturation Solutions:**

| Situation | Solution |
|-----------|----------|
| High frequency, good results | Expand audience or add fresh creative |
| High frequency, poor results | Pause and let audience rest, new creative |
| Approaching saturation | Proactively expand or rotate |

---

### Dimension 2: Overlap Analysis

**Overlap Risk Matrix:**

| Overlap Level | Definition | Impact |
|---------------|------------|--------|
| Low (<20%) | Minimal audience duplication | Safe |
| Moderate (20-40%) | Some users in multiple audiences | Monitor |
| High (40-60%) | Significant cannibalization | Consolidate |
| Critical (>60%) | Self-competition | Urgent fix |

**Overlap Assessment:**

| Audience A | Audience B | Overlap % | Action |
|------------|------------|-----------|--------|
| [Audience 1] | [Audience 2] | XX% | [Recommendation] |
| [Audience 1] | [Audience 3] | XX% | [Recommendation] |

**Common Overlap Scenarios:**

| Scenario | Problem | Solution |
|----------|---------|----------|
| Interest + LAL overlap | Bidding against yourself | Exclude one from other |
| Multiple LALs overlap | Similar seed audiences | Consolidate or differentiate seeds |
| Retargeting + prospecting overlap | Paying premium for existing visitors | Exclude retargeting from prospecting |
| Broad + targeted overlap | Unclear attribution | Ensure exclusions |

**Exclusion Audit:**

| Audience | Should Exclude | Currently Excluded? |
|----------|----------------|---------------------|
| Prospecting | Purchasers, leads | Y/N |
| Lookalikes | Custom audiences | Y/N |
| Interest targeting | Existing customers | Y/N |
| Broad targeting | All other audiences | Y/N |

---

### Dimension 3: Audience Quality Analysis

**Targeting Precision Assessment:**

| Audience | Targeting Type | Specificity | Quality Score |
|----------|---------------|-------------|---------------|
| [Audience 1] | [Type] | Broad/Moderate/Tight | X/10 |
| [Audience 2] | [Type] | Broad/Moderate/Tight | X/10 |

**Interest Targeting Evaluation:**

| Interest Category | Relevance | Size | Competition |
|-------------------|-----------|------|-------------|
| [Interest 1] | High/Med/Low | X M | High/Med/Low |
| [Interest 2] | High/Med/Low | X M | High/Med/Low |

**Interest Quality Signals:**

| Signal | Good | Bad |
|--------|------|-----|
| Relevance to offer | Direct match | Tangential |
| Audience size | 1-10M sweet spot | <500K or >50M |
| Behavior vs. interest | Behaviors preferred | Interests only |
| Layering | AND logic for precision | OR logic only |

**Targeting Layer Analysis:**

| Ad Set | Demographics | Interests | Behaviors | Custom | Assessment |
|--------|--------------|-----------|-----------|--------|------------|
| [Ad Set 1] | [Details] | [Count] | [Count] | [Y/N] | [Score] |
| [Ad Set 2] | [Details] | [Count] | [Count] | [Y/N] | [Score] |

---

### Dimension 4: Structure Analysis

**Campaign Organization Assessment:**

| Issue | Present? | Impact |
|-------|----------|--------|
| Too many ad sets (>5 per campaign) | Y/N | Budget fragmentation |
| Audiences not separated by funnel | Y/N | Can't optimize by stage |
| Mixed objectives in structure | Y/N | Learning phase issues |
| No clear testing structure | Y/N | Can't identify winners |

**Recommended Structure:**

```
PROSPECTING CAMPAIGN
├── Ad Set: Broad Targeting
├── Ad Set: Interest Stack 1
├── Ad Set: Lookalike 1-2%
└── Ad Set: Lookalike 2-5%

RETARGETING CAMPAIGN
├── Ad Set: Website Visitors (1-7 days)
├── Ad Set: Website Visitors (8-30 days)
├── Ad Set: Engaged (Video/Page)
└── Ad Set: Cart Abandoners

RETENTION CAMPAIGN
├── Ad Set: Past Purchasers
└── Ad Set: Lapsed Customers
```

**Budget Distribution Assessment:**

| Funnel Stage | % of Budget | Recommended | Gap |
|--------------|-------------|-------------|-----|
| Prospecting | XX% | 60-70% | [+/-X%] |
| Retargeting | XX% | 20-30% | [+/-X%] |
| Retention | XX% | 5-15% | [+/-X%] |

---

### Dimension 5: Custom Audience Analysis

**Custom Audience Inventory:**

| Audience | Source | Size | Last Updated | Match Rate |
|----------|--------|------|--------------|------------|
| [Audience 1] | [Source] | X | [Date] | XX% |
| [Audience 2] | [Source] | X | [Date] | XX% |

**Custom Audience Quality:**

| Type | Quality Indicators |
|------|-------------------|
| Customer List | >50% match rate, recent data, segmented |
| Website Visitors | 180-day window, event-based segments |
| App Activity | High-value events, recent activity |
| Engagement | Video viewers (50%+), page engagers |
| Offline Events | Accurate tracking, attribution window |

**Custom Audience Health Check:**

| Audience | Issue | Recommendation |
|----------|-------|----------------|
| [Audience 1] | [Issue found] | [Fix] |
| [Audience 2] | [Issue found] | [Fix] |

**Missing Custom Audiences:**

| Recommended Audience | Why | Priority |
|---------------------|-----|----------|
| [Audience type] | [Value] | High/Med/Low |
| [Audience type] | [Value] | High/Med/Low |

---

### Dimension 6: Lookalike Analysis

**Lookalike Inventory:**

| LAL | Seed Audience | Size (%) | Audience Size | Performance |
|-----|---------------|----------|---------------|-------------|
| [LAL 1] | [Seed] | X% | X M | [CPA/ROAS] |
| [LAL 2] | [Seed] | X% | X M | [CPA/ROAS] |

**Lookalike Size Guidance:**

| Size | Use Case | Trade-off |
|------|----------|-----------|
| 1% | Highest quality | Smallest reach |
| 1-2% | Quality + scale | Good balance |
| 2-5% | Moderate expansion | Some quality loss |
| 5-10% | Wide reach | Approaches broad |
| >10% | Not recommended | Defeats purpose |

**Seed Audience Quality:**

| Factor | Good | Bad |
|--------|------|-----|
| Size | 1,000-50,000 | <1,000 or >100,000 |
| Recency | Last 180 days | >365 days old |
| Quality | High-value customers | All customers |
| Events | Conversion events | Page views only |

**LAL Optimization Opportunities:**

| Current Seed | Better Seed | Why |
|--------------|-------------|-----|
| All purchasers | Top 20% by LTV | Higher quality signal |
| Website visitors | Add to cart | Stronger intent |
| Email list | Recent engaged only | Better recency |

---

## Output Format

### Executive Summary

```
AUDIENCE HEALTH SCORE: XX/100 [GRADE]

Account: [Name or ID]
Audiences Analyzed: X
Total Spend (Period): $XX,XXX

CRITICAL ISSUE: [Biggest problem]
QUICK WIN: [Easiest high-impact fix]
ESTIMATED SAVINGS: $X,XXX/month (from inefficiencies)
```

**Grade Scale:**

| Score | Grade | Status |
|-------|-------|--------|
| 85-100 | A | Healthy audiences, minor tweaks |
| 70-84 | B | Good foundation, optimization opportunities |
| 55-69 | C | Significant inefficiencies |
| 40-54 | D | Major problems hurting ROAS |
| <40 | F | Audience strategy needs overhaul |

---

### Dimension Scores

```
SATURATION:       ████████████████░░░░ 40/50
OVERLAP:          ████████░░░░░░░░░░░░ 20/50  ⚠️ CRITICAL
QUALITY:          ████████████░░░░░░░░ 30/50
STRUCTURE:        ██████████████░░░░░░ 35/50
CUSTOM AUDIENCES: ████████████████░░░░ 40/50
LOOKALIKES:       ██████████░░░░░░░░░░ 25/50  ⚠️ NEEDS WORK

OVERALL: 190/300 = 63/100 (C)
```

---

### Critical Issues

**Issue 1: [Title]**
- **Dimension:** [Which dimension]
- **Problem:** [Specific description]
- **Evidence:** [Data showing the issue]
- **Impact:** $X,XXX wasted/month estimated
- **Fix:** [Specific action to take]
- **Priority:** CRITICAL

---

### Audience-by-Audience Analysis

**[Audience Name]**

| Metric | Value | Benchmark | Status |
|--------|-------|-----------|--------|
| Size | X M | — | — |
| Spend | $X,XXX | — | — |
| CPM | $X.XX | $X-$X | 🟢/🟡/🔴 |
| Frequency (7d) | X.X | <2 | 🟢/🟡/🔴 |
| CTR | X.XX% | >1% | 🟢/🟡/🔴 |
| CPA | $X.XX | [Target] | 🟢/🟡/🔴 |

**Assessment:** [Summary of this audience's health]

**Recommendations:**
1. [Specific recommendation]
2. [Specific recommendation]

---

### Overlap Report

```
OVERLAP MAP:

[Audience A] ←——40%——→ [Audience B]  ⚠️ HIGH
[Audience A] ←——15%——→ [Audience C]  ✓ OK
[Audience B] ←——55%——→ [Audience C]  🔴 CRITICAL
```

**Consolidation Recommendations:**

| Merge | Into | Rationale |
|-------|------|-----------|
| [Audience B] | [Audience A] | 55% overlap, similar performance |

**Exclusion Recommendations:**

| Audience | Add Exclusion | Why |
|----------|---------------|-----|
| [Audience] | [What to exclude] | [Reason] |

---

### Custom Audience Recommendations

**Create These Audiences:**

| Audience | Source | Definition | Expected Value |
|----------|--------|------------|----------------|
| [Name] | [Source] | [Criteria] | [Why valuable] |
| [Name] | [Source] | [Criteria] | [Why valuable] |

**Improve These Audiences:**

| Audience | Current Issue | Improvement |
|----------|---------------|-------------|
| [Name] | [Issue] | [Fix] |

---

### Lookalike Recommendations

**New Lookalikes to Create:**

| Seed | LAL Size | Rationale |
|------|----------|-----------|
| [Best customers] | 1% | Highest quality signal |
| [Converters last 30d] | 1-2% | Recency value |

**Existing LAL Changes:**

| Current LAL | Change | Why |
|-------------|--------|-----|
| [LAL name] | [What to change] | [Reason] |

---

### Budget Reallocation

**Current vs. Recommended:**

| Audience | Current Spend | Recommended | Change |
|----------|---------------|-------------|--------|
| [Audience 1] | $X,XXX | $X,XXX | +$XXX |
| [Audience 2] | $X,XXX | $X,XXX | -$XXX |
| [Audience 3] | $X,XXX | Pause | -$XXX |
| **Total** | $XX,XXX | $XX,XXX | — |

**Expected Impact:**
- Estimated CPA improvement: -$X.XX (-XX%)
- Estimated additional conversions: +XX
- ROAS improvement: +XX%

---

### Implementation Checklist

**Immediate (This Week):**
- [ ] [Critical fix 1]
- [ ] [Critical fix 2]
- [ ] Set up missing exclusions

**Short-Term (Next 2 Weeks):**
- [ ] Create new custom audiences
- [ ] Launch new lookalikes
- [ ] Consolidate overlapping audiences

**Ongoing:**
- [ ] Monitor frequency weekly
- [ ] Refresh custom audiences monthly
- [ ] Test new audience angles

---

## Benchmarks Reference

### CPM Benchmarks by Objective

| Objective | Low | Average | High |
|-----------|-----|---------|------|
| Awareness | $2-5 | $5-10 | $10-20 |
| Traffic | $3-8 | $8-15 | $15-30 |
| Engagement | $2-5 | $5-12 | $12-25 |
| Leads | $5-15 | $15-35 | $35-75 |
| Conversions | $8-20 | $20-50 | $50-100+ |

*Varies significantly by industry, country, and season*

### Frequency Guidelines

| Funnel Stage | Ideal Frequency | Max Before Fatigue |
|--------------|-----------------|-------------------|
| Prospecting | 1-2 per week | 4 per week |
| Retargeting | 2-4 per week | 7 per week |
| Retention | 1-2 per week | 3 per week |

---

## Limitations

**I can analyze:**
- Audience performance metrics
- Targeting configuration quality
- Structural organization
- Overlap patterns (if data provided)
- Optimization opportunities

**I cannot access:**
- Live Meta Ads account data
- Real-time overlap reports
- Pixel health diagnostics
- Creative performance by audience
- Algorithm learning status

**For complete analysis, also provide:**
- Meta Audience Overlap tool exports
- Breakdown reports by audience
- Frequency distribution data
- Historical performance trends

---

## Quality Checklist

Before delivering audit:
- [ ] All 6 dimensions evaluated
- [ ] Each audience analyzed individually
- [ ] Overlap patterns identified
- [ ] Saturation warnings flagged
- [ ] Custom audience gaps noted
- [ ] LAL optimization covered
- [ ] Budget reallocation quantified
- [ ] Implementation prioritized
- [ ] Limitations acknowledged
