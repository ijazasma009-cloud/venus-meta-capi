---
name: keyword-performance-analyzer
description: Analyzes keyword performance using Google Ads MCP data. Identifies Quality Score issues, underperforming keywords, bid opportunities, and match type optimization. Triggers when user asks about keyword health, QS problems, or wants to optimize keyword bids. Pulls live data via keyword_view action.
---

# Keyword Performance Analyzer

Deep-dive into your keywords to find what's working, what's bleeding money, and where Quality Score is killing your efficiency.

## Core Philosophy

**Keywords are the foundation.** Bad keywords = bad account. Great keywords with poor QS = overpaying for every click.

**The 3 Keyword Questions:**
1. Which keywords are actually driving results?
2. Where is Quality Score costing me money?
3. What bid adjustments will improve efficiency?

---

## MCP Integration

### Required Data Pull

Use the Google Ads MCP `keyword_view` action with this GAQL query:

```
SELECT
  campaign.id,
  campaign.name,
  ad_group.id,
  ad_group.name,
  ad_group_criterion.keyword.text,
  ad_group_criterion.keyword.match_type,
  ad_group_criterion.negative,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions,
  metrics.conversions_value,
  metrics.ctr,
  metrics.historical_quality_score
FROM keyword_view
WHERE segments.date BETWEEN '{start_date}' AND '{end_date}'
  AND ad_group_criterion.negative = FALSE
  AND metrics.impressions > 0
ORDER BY metrics.cost_micros DESC
```

### Data Requirements

**From MCP Response:**
- `ad_group_criterion.keyword.text` - The keyword
- `ad_group_criterion.keyword.match_type` - BROAD, PHRASE, EXACT
- `metrics.historical_quality_score` - QS (1-10 scale)
- `metrics.impressions`, `metrics.clicks`, `metrics.cost_micros`
- `metrics.conversions`, `metrics.conversions_value`
- `metrics.ctr` - Click-through rate

**User Should Provide:**
- Target CPA or ROAS
- Date range (default: last 30 days)
- Minimum spend threshold for analysis (default: $10)

---

## Analysis Framework

### Tier 1: Quality Score Analysis

**QS Breakdown:**

| QS Range | Assessment | Priority |
|----------|------------|----------|
| 1-3 | Critical - Major cost penalty | Immediate |
| 4-5 | Poor - Significant penalty | High |
| 6-7 | Average - Room to improve | Medium |
| 8-10 | Good - Maintain | Low |

**QS Impact Calculation:**
```
Estimated CPC penalty = (10 - QS) × 10%
Example: QS 5 = ~50% higher CPCs than QS 10
```

**QS Improvement Levers:**
1. **Expected CTR** - Ad relevance, compelling copy
2. **Ad Relevance** - Keyword-ad alignment
3. **Landing Page Experience** - Page quality, load speed, relevance

---

### Tier 2: Performance Segmentation

**Keyword Categories:**

| Category | Criteria | Action |
|----------|----------|--------|
| Stars | Conv > 0, CPA < target, QS 7+ | Scale bids, add budget |
| Solid | Conv > 0, CPA at target | Maintain, test improvements |
| Potential | Good CTR, 0 conv, low spend | Give more budget/time |
| Bleeders | High spend, 0 conv | Pause or reduce bids |
| QS Victims | Good conv, QS < 6 | Fix QS to reduce CPA |
| Zombies | Low impressions, no activity | Evaluate relevance |

---

### Tier 3: Match Type Analysis

**Match Type Health Check:**

| Match Type | Ideal Use | Red Flags |
|------------|-----------|-----------|
| EXACT | High-intent, proven converters | Too few impressions |
| PHRASE | Balanced reach + control | High spend, low conv |
| BROAD | Discovery, volume | Bleeding on irrelevant terms |

**Match Type Migration Signals:**
- BROAD → PHRASE: Good conv but also waste in search terms
- PHRASE → EXACT: Consistent performer, want more control
- EXACT → Pause: No impressions, too restrictive

---

### Tier 4: Bid Optimization

**Bid Adjustment Framework:**

| Signal | Recommendation |
|--------|----------------|
| CPA 30%+ below target, limited by rank | Increase bid 15-20% |
| CPA at target, good volume | Maintain bid |
| CPA 10-30% above target | Decrease bid 10-15% |
| CPA 30%+ above target | Decrease bid 20-30% or pause |
| QS < 6 with high CPA | Fix QS before adjusting bid |

---

## Output Format

### Executive Summary

```
KEYWORD HEALTH SCORE: 🟢/🟡/🔴
Keywords Analyzed: XXX
Period: [dates]
Avg Quality Score: X.X
Keywords with QS Issues: XX (XX%)
Estimated Monthly QS Penalty: $X,XXX
```

---

### Quality Score Report

**Critical QS Issues (QS 1-5):**

| Keyword | Match | QS | Impressions | CPA | Est. Penalty |
|---------|-------|-----|-------------|-----|--------------|
| [keyword] | EXACT | 4 | X,XXX | $XX | +XX% CPC |
| [keyword] | PHRASE | 3 | X,XXX | $XX | +XX% CPC |

**QS Improvement Priorities:**

1. **[Keyword]** (QS: 4)
   - Issue: Low expected CTR
   - Action: Test new ad copy with keyword in headline
   - Potential savings: $XXX/month

2. **[Keyword]** (QS: 5)
   - Issue: Landing page experience
   - Action: Improve page load speed, add keyword relevance
   - Potential savings: $XXX/month

---

### Performance Tiers

**Stars (Scale These):**

| Keyword | Conv | CPA | vs Target | QS | Recommendation |
|---------|------|-----|-----------|-----|----------------|
| [keyword] | XX | $XX | -XX% | 8 | Increase bid 15% |

**Bleeders (Fix or Pause):**

| Keyword | Spend | Conv | QS | Action |
|---------|-------|------|-----|--------|
| [keyword] | $XXX | 0 | 5 | Pause |
| [keyword] | $XXX | 0 | 7 | Reduce bid 30% |

**QS Victims (Fix QS First):**

| Keyword | Conv | CPA | QS | Potential CPA |
|---------|------|-----|-----|---------------|
| [keyword] | XX | $XX | 4 | $XX (if QS=8) |

---

### Match Type Recommendations

**Migrate to Exact:**
- [keyword] (PHRASE) - 5+ conversions, consistent performer
- [keyword] (BROAD) - Proven term, want bid control

**Consider Pausing:**
- [keyword] (EXACT) - 0 impressions in 30 days
- [keyword] (BROAD) - 80% of clicks from irrelevant terms

---

### Bid Adjustment Queue

**Increase Bids:**

| Keyword | Current Bid | Conv | CPA | Recommended |
|---------|-------------|------|-----|-------------|
| [keyword] | $X.XX | XX | $XX | $X.XX (+15%) |

**Decrease Bids:**

| Keyword | Current Bid | Conv | CPA | Recommended |
|---------|-------------|------|-----|-------------|
| [keyword] | $X.XX | X | $XX | $X.XX (-20%) |

---

### Quick Wins Summary

```
ACTION                          KEYWORDS    EST. IMPACT
────────────────────────────────────────────────────────
Pause bleeders                  XX          Save $X,XXX/mo
Fix QS issues                   XX          Save $X,XXX/mo
Increase bids on stars          XX          +XX conv/mo
Migrate to exact match          XX          Better control
```

---

## Composability

**Chains from:**
- `search-term-gold-miner` - Promoted search terms become keywords to analyze

**Chains to:**
- `bid-strategy-auditor` - Keywords feed into bid strategy analysis
- `budget-allocation-optimizer` - Keyword efficiency informs budget moves

---

## Limitations

**I can assess:**
- Quality Score and its cost impact
- Keyword-level performance tiers
- Match type distribution health
- Bid adjustment opportunities

**I cannot assess:**
- QS component breakdown (need Google Ads UI)
- Search term quality within keyword (need search term report)
- Competitor keyword bids
- Incrementality of keyword conversions

**For deeper analysis, also run:**
- `search-term-gold-miner` for search term quality
- Landing page audit for QS improvements

---

## Quality Checklist

Before delivering analysis:
- [ ] QS distribution calculated
- [ ] Bleeders identified with spend impact
- [ ] Stars identified with scaling opportunity
- [ ] QS penalty estimated in dollars
- [ ] Bid recommendations include % change
- [ ] Match type migrations justified
- [ ] Composability next steps noted
