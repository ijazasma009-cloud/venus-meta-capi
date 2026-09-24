---
name: search-term-gold-miner
description: Analyzes Google Ads search term reports to uncover wasted spend, hidden opportunities, and negative keyword gaps. Triggers when user wants to review search terms, find wasted budget, discover new keywords, or clean up irrelevant traffic. Provides actionable lists of negatives to add, keywords to promote, and spend-saving estimates.
---

# Search Term Gold Miner

Turn your search term report into actionable profit. Find the money you're wasting and the opportunities you're missing.

## Core Philosophy

**Every search term tells a story.** Either it's making you money, costing you money, or waiting to be discovered.

**The 3 Buckets:**
1. **Gold** - Converting terms that deserve their own keywords
2. **Garbage** - Non-converting terms bleeding your budget
3. **Grey Zone** - Terms needing more data before judgment

---

## Required Context

### Must Have

**1. Search Terms Data**
Export or paste search term report including:
- Search term
- Impressions
- Clicks
- Cost
- Conversions (critical)

Better if you also have: conversion value, match type, campaign/ad group

**2. Time Period**
- Minimum: 14 days (need enough data for patterns)
- Ideal: 30-60 days (reliable patterns)
- Maximum: 90 days (beyond this, data gets stale)

### Strongly Recommended

**3. Performance Thresholds**
- Target CPA: $___
- Minimum acceptable CVR: ____%
- Cost threshold for "significant spend": $___

Without thresholds, I'll use these defaults:
- Significant spend = $50+ with 0 conversions
- Promotion threshold = 3+ conversions
- CVR concern = below 1%

### Nice to Have

- Existing negative keyword lists (I'll check for gaps)
- Business context (B2B/B2C, product type, sales cycle)
- Brand terms to exclude from analysis

---

## Analysis Framework

### Phase 1: The Garbage Hunt

**Objective:** Stop the bleeding. Find terms wasting money.

#### Tier 1: Obvious Waste (Pause Immediately)

**Zero-Conversion Bleeders**
- Terms with $50+ spend and 0 conversions
- Action: Add as exact match negatives
- Priority: CRITICAL

**Intent Mismatches**
Patterns indicating wrong audience:
- Job seekers: "jobs," "careers," "salary," "hiring"
- Students: "course," "certification," "learn," "tutorial"
- DIYers: "how to," "DIY," "free," "template"
- Researchers: "what is," "definition," "vs," "comparison"

**Competitor Searches**
- Terms containing competitor brand names
- Unless: You're intentionally conquesting
- Action: Negative or dedicated conquesting campaign

**Location Mismatches**
- Geographic terms outside service area
- "near me" variations in wrong markets

#### Tier 2: Likely Waste (Review & Negate)

**High Click, Zero Convert**
- 20+ clicks with 0 conversions
- Indicates: Wrong intent or landing page mismatch

**CPA > 3x Target**
- Terms technically converting but unprofitably
- Threshold: If target CPA is $50, flag terms with CPA > $150

**Low Quality Indicators**
- Very short queries (1-2 words, too broad)
- Questions without purchase intent
- Informational queries in transactional campaigns

---

### Phase 2: The Gold Discovery

**Objective:** Find money-makers hiding in broad match.

#### Promotion Criteria

**Star Performers** (Promote to Exact Match)
- 3+ conversions
- CPA at or below target
- Currently matching via broad or phrase

**Why Promote?**
1. Better Quality Score potential
2. More bidding control
3. Dedicated ad copy opportunity
4. Cleaner data attribution

#### Opportunity Patterns

**Theme Clusters**
Multiple related terms converting = ad group opportunity
- Example: "emergency plumber," "24 hour plumber," "plumber now"
- Action: Create dedicated ad group with themed ads

**Long-Tail Winners**
4+ word queries with good CVR often indicate:
- High intent
- Lower competition
- Specific landing page opportunity

**New Keyword Ideas**
Terms with:
- Decent impressions (100+)
- Good CTR (above account average)
- Reasonable clicks but no conversions YET
- Clear commercial intent

---

### Phase 3: The Grey Zone

**Objective:** Identify terms needing more data before judgment.

**Insufficient Data Criteria:**
- < 10 clicks: Too early to judge
- < $20 spend: Not enough investment
- < 7 days of data: Could be anomaly

**Monitoring Recommendations:**
- Set calendar reminder to re-review in 2 weeks
- Consider bid reduction (not elimination) if concerning
- Flag for increased monitoring

---

## Scoring & Prioritization

### Waste Impact Score

| Score | Criteria | Urgency |
|-------|----------|---------|
| 10 | $200+ spend, 0 conversions | Immediate |
| 8 | $100-200 spend, 0 conversions | This week |
| 6 | $50-100 spend, 0 conversions | Priority |
| 4 | CPA > 3x target | Review |
| 2 | Low volume concerns | Monitor |

### Opportunity Score

| Score | Criteria | Action |
|-------|----------|--------|
| 10 | 5+ conversions, CPA < target | Promote immediately |
| 8 | 3-4 conversions, CPA at target | Strong promote candidate |
| 6 | 2 conversions, good signals | Add to watchlist |
| 4 | 1 conversion, high intent | Monitor |

---

## Output Format

### Executive Summary

```
SEARCH TERM HEALTH: 🟢/🟡/🔴
Period Analyzed: [dates]
Total Terms Reviewed: [X]
Estimated Monthly Waste: $[X]
Opportunities Found: [X] keywords
```

---

### 🚨 Immediate Negatives (Add Today)

**Total Wasted Spend: $[X]**

| Search Term | Clicks | Cost | Conv | Action |
|-------------|--------|------|------|--------|
| [term] | [X] | $[X] | 0 | Exact negative |
| [term] | [X] | $[X] | 0 | Exact negative |
| [term] | [X] | $[X] | 0 | Exact negative |

**Pattern-Based Negatives:**
Add these as phrase match negatives to block variations:
- "[pattern]" - Reason: [why]
- "[pattern]" - Reason: [why]

**Copy-Paste Negative List:**
```
[term 1]
[term 2]
[term 3]
```

---

### ⭐ Keywords to Promote

**Estimated Monthly Value if Promoted: $[X]**

| Search Term | Conv | CPA | Current Match | Recommendation |
|-------------|------|-----|---------------|----------------|
| [term] | [X] | $[X] | Broad | Add as Exact |
| [term] | [X] | $[X] | Phrase | Add as Exact |

**Ad Group Opportunities:**
Terms that cluster together for dedicated ad groups:
1. **[Theme]:** [term 1], [term 2], [term 3]
2. **[Theme]:** [term 1], [term 2], [term 3]

---

### 👀 Watchlist (Need More Data)

| Search Term | Clicks | Cost | Signal | Review Date |
|-------------|--------|------|--------|-------------|
| [term] | [X] | $[X] | [note] | [date] |

---

### 📊 Search Term Quality Breakdown

```
Gold (Converting well):     XX% of spend
Garbage (Wasted):           XX% of spend
Grey Zone (Needs data):     XX% of spend
Branded (Excluded):         XX% of spend
```

---

### 💡 Strategic Insights

**Pattern 1: [Observation]**
[What you're seeing in the data and what it means]

**Pattern 2: [Observation]**
[What you're seeing in the data and what it means]

**Recommendation:**
[One strategic recommendation based on overall patterns]

---

## Analysis Principles

### Be Conservative with Negatives
- When in doubt, DON'T negate
- One good conversion can justify previous waste
- Use exact match negatives to preserve variations
- Consider: Is this term genuinely irrelevant, or just underperforming?

### Be Aggressive with Promotions
- Winning terms deserve attention
- The cost of NOT promoting: poor QS, less control, attribution issues
- Threshold: If it converted 3x, it's proven

### Context Matters
- B2B: Longer sales cycles mean patience with grey zone
- E-commerce: Faster feedback, can be more aggressive
- High-ticket: One conversion can change everything
- Lead gen: Quality matters more than volume

### Account for Seasonality
- Compare to same period last year if available
- Note any obvious seasonal patterns
- Flag terms that might be temporarily poor performers

---

## Limitations

**I can assess:**
- Conversion patterns at search term level
- Obvious waste patterns
- Keyword promotion opportunities
- Theme clustering

**I cannot assess:**
- Lead quality (need backend data)
- Assisted conversions (need attribution data)
- Impression share by term (not in standard export)
- Why specific terms aren't converting (need landing page analysis)

**For deeper analysis, also provide:**
- Landing page URLs for non-converting terms
- Backend conversion quality data
- Multi-touch attribution report
- Competitor auction insights

---

## Quality Checklist

Before delivering analysis:
- [ ] Negative recommendations sorted by spend impact
- [ ] Each negative includes match type guidance
- [ ] Promotion candidates verified for statistical significance
- [ ] Copy-paste lists provided for easy implementation
- [ ] Dollar impact estimated for key recommendations
- [ ] Grey zone items have clear review timeline
- [ ] No branded terms accidentally flagged as waste
