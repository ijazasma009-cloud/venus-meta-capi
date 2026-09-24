---
name: ad-copy-performance-ranker
description: Analyzes RSA ad performance using Google Ads MCP data. Ranks headlines and descriptions by effectiveness, identifies winners/losers, and provides creative optimization recommendations. Triggers when user asks about ad copy performance, RSA analysis, or wants to improve ad creative. Pulls live data via ad_group_ad action.
---

# Ad Copy Performance Ranker

Find your winning headlines and descriptions. Kill the losers. Write better ads based on what actually works.

## Core Philosophy

**Not all headlines are equal.** Google's RSA system tests combinations, but you need to know which assets are carrying the weight and which are dragging you down.

**The Ad Copy Questions:**
1. Which headlines/descriptions are driving clicks and conversions?
2. Which assets should be replaced?
3. What patterns make winning copy?
4. Is my ad strength helping or misleading me?

---

## MCP Integration

### Required Data Pull

Use the Google Ads MCP `ad_group_ad` action with this GAQL query:

```
SELECT
  campaign.id,
  campaign.name,
  ad_group.id,
  ad_group.name,
  ad_group_ad.ad.id,
  ad_group_ad.ad.type,
  ad_group_ad.ad.responsive_search_ad.headlines,
  ad_group_ad.ad.responsive_search_ad.descriptions,
  ad_group_ad.ad.responsive_search_ad.path1,
  ad_group_ad.ad.responsive_search_ad.path2,
  ad_group_ad.ad.final_urls,
  ad_group_ad.ad_strength,
  ad_group_ad.status,
  ad_group_ad.policy_summary.approval_status,
  metrics.impressions,
  metrics.clicks,
  metrics.conversions,
  metrics.cost_micros,
  metrics.ctr,
  metrics.conversions_from_interactions_rate
FROM ad_group_ad
WHERE ad_group_ad.ad.type = 'RESPONSIVE_SEARCH_AD'
  AND ad_group_ad.status != 'REMOVED'
  AND segments.date BETWEEN '{start_date}' AND '{end_date}'
ORDER BY metrics.impressions DESC
```

### Data Requirements

**From MCP Response:**
- `ad_group_ad.ad.responsive_search_ad.headlines` - Array of headline assets
- `ad_group_ad.ad.responsive_search_ad.descriptions` - Array of description assets
- `ad_group_ad.ad_strength` - EXCELLENT, GOOD, AVERAGE, POOR
- `metrics.impressions`, `metrics.clicks`, `metrics.conversions`
- `metrics.ctr`, `metrics.conversions_from_interactions_rate`

**Note on Asset-Level Performance:**
Google Ads API provides ad-level metrics, not individual headline/description performance. For asset-level data:
- Use Google Ads UI "View asset details" report
- Analyze patterns across ads that share similar headlines
- Compare ad strength vs actual performance

**User Should Provide:**
- Target metrics (CTR benchmark, conversion rate benchmark)
- Date range (default: last 30 days)
- Industry/vertical for context

---

## Analysis Framework

### Tier 1: Ad-Level Performance

**Ad Performance Ranking:**

| Tier | CTR vs Avg | CVR vs Avg | Assessment |
|------|------------|------------|------------|
| Star | +20%+ | +20%+ | Study and replicate |
| Above Avg | +10-20% | +10-20% | Solid performer |
| Average | ±10% | ±10% | Room to improve |
| Below Avg | -10-20% | -10-20% | Needs attention |
| Underperformer | -20%+ | -20%+ | Replace or revise |

---

### Tier 2: Ad Strength Analysis

**Ad Strength Reality Check:**

| Ad Strength | What Google Says | What Actually Matters |
|-------------|------------------|----------------------|
| EXCELLENT | Optimal setup | May or may not perform |
| GOOD | Meets requirements | Usually acceptable |
| AVERAGE | Missing elements | Check performance data |
| POOR | Needs work | Fix if data agrees |

**Key Insight:** Ad Strength ≠ Performance. An "Excellent" ad can underperform a "Good" one. Always prioritize actual metrics over ad strength scores.

---

### Tier 3: Headline Pattern Analysis

**Winning Headline Patterns to Look For:**

| Pattern | Example | Why It Works |
|---------|---------|--------------|
| Benefit-First | "Save 50% Today" | Immediate value |
| Action-Oriented | "Get Your Free Quote" | Clear CTA |
| Social Proof | "Trusted by 10,000+" | Credibility |
| Urgency | "Limited Time Offer" | FOMO |
| Question | "Looking for [X]?" | Relevance |
| Specificity | "24-Hour Delivery" | Concrete promise |

**Weak Headline Patterns:**

| Pattern | Example | Problem |
|---------|---------|---------|
| Generic | "Welcome to Our Site" | No differentiation |
| Vague | "Quality Products" | Means nothing |
| Feature-Only | "We Have Inventory" | No benefit to user |
| Too Long | "..." (truncated) | Message cut off |

---

### Tier 4: Description Analysis

**Description Best Practices:**

| Element | Good Practice | Poor Practice |
|---------|--------------|---------------|
| Length | Uses 80+ characters | Short, wasted space |
| CTA | Clear action included | No direction |
| Benefits | Multiple benefits listed | Feature dump |
| Differentiation | Why choose you | Generic claims |

---

## Output Format

### Executive Summary

```
AD COPY HEALTH: 🟢/🟡/🔴
Ads Analyzed: XX
Period: [dates]
Avg CTR: X.XX%
Avg CVR: X.XX%
Top Performing Ad: [Campaign > Ad Group > Ad ID]
Ads Needing Attention: XX
```

---

### Top Performing Ads

| Rank | Campaign | Ad Group | CTR | CVR | Ad Strength | Status |
|------|----------|----------|-----|-----|-------------|--------|
| 1 | [name] | [name] | X.XX% | X.XX% | EXCELLENT | Star |
| 2 | [name] | [name] | X.XX% | X.XX% | GOOD | Star |
| 3 | [name] | [name] | X.XX% | X.XX% | GOOD | Above Avg |

**Winning Headlines from Top Ads:**
1. "[Headline text]" - appears in X of top Y ads
2. "[Headline text]" - appears in X of top Y ads
3. "[Headline text]" - appears in X of top Y ads

**Winning Descriptions from Top Ads:**
1. "[Description text]"
2. "[Description text]"

**Patterns Observed:**
- [Pattern 1: e.g., "Top ads use specific numbers"]
- [Pattern 2: e.g., "Strong CTAs in position 1"]
- [Pattern 3: e.g., "Benefit-first headlines dominate"]

---

### Underperforming Ads

| Campaign | Ad Group | CTR | CVR | Ad Strength | Issue |
|----------|----------|-----|-----|-------------|-------|
| [name] | [name] | X.XX% | X.XX% | POOR | Low CTR |
| [name] | [name] | X.XX% | X.XX% | AVERAGE | Low CVR |

**Common Problems:**
- [Issue 1: e.g., "Generic headlines without differentiation"]
- [Issue 2: e.g., "No clear CTA in descriptions"]

**Recommended Actions:**
1. **[Ad Group]**: Replace headlines X, Y with [suggested approach]
2. **[Ad Group]**: Add benefit-focused description
3. **[Ad Group]**: Pin strong headline to position 1

---

### Ad Strength vs Performance Analysis

| Ad Strength | Avg CTR | Avg CVR | Count | Reality |
|-------------|---------|---------|-------|---------|
| EXCELLENT | X.XX% | X.XX% | XX | [Assessment] |
| GOOD | X.XX% | X.XX% | XX | [Assessment] |
| AVERAGE | X.XX% | X.XX% | XX | [Assessment] |
| POOR | X.XX% | X.XX% | XX | [Assessment] |

**Key Finding:** [Observation about ad strength correlation with performance]

---

### Headline Audit

**Headlines by Frequency (Across All Ads):**

| Headline | Used In | Avg CTR When Used | Assessment |
|----------|---------|-------------------|------------|
| "[text]" | X ads | X.XX% | Keep |
| "[text]" | X ads | X.XX% | Keep |
| "[text]" | X ads | X.XX% | Test replace |
| "[text]" | X ads | X.XX% | Replace |

**Headline Gaps:**
- Missing: [Type of headline, e.g., "No urgency-based headlines"]
- Missing: [Type of headline, e.g., "No social proof headlines"]

**Suggested New Headlines:**
1. "[Suggested headline]" - adds [missing element]
2. "[Suggested headline]" - adds [missing element]
3. "[Suggested headline]" - adds [missing element]

---

### Description Audit

**Descriptions by Performance:**

| Description | Avg CTR | Avg CVR | Assessment |
|-------------|---------|---------|------------|
| "[text snippet...]" | X.XX% | X.XX% | Star |
| "[text snippet...]" | X.XX% | X.XX% | Solid |
| "[text snippet...]" | X.XX% | X.XX% | Replace |

**Description Gaps:**
- [Missing element, e.g., "No descriptions mention free shipping"]
- [Missing element, e.g., "No urgency in descriptions"]

---

### Quick Wins

```
ACTION                           ADS     EST. IMPACT
────────────────────────────────────────────────────
Replace weak headlines           XX      +XX% CTR
Add missing headline types       XX      Improved coverage
Fix description CTAs             XX      +XX% CVR
Address policy issues            XX      Increase impressions
```

---

### Creative Recommendations

**Based on Top Performers, Test These:**

**Headlines:**
1. "[Suggested headline]" - mirrors winning pattern
2. "[Suggested headline]" - adds variety
3. "[Suggested headline]" - competitive angle

**Descriptions:**
1. "[Suggested description]" - benefit stack
2. "[Suggested description]" - urgency + CTA

**Pinning Strategy:**
- Pin "[best headline]" to Position 1
- Pin "[brand headline]" to Position 2 or 3
- Leave other positions unpinned for testing

---

## Composability

**Chains from:**
- `keyword-performance-analyzer` - Keyword themes inform ad copy relevance

**Chains to:**
- MCP `create_responsive_search_ad` - Can create new ads based on winning patterns
- `ab-test-designer` - Test new creative variations

---

## Limitations

**I can assess:**
- Ad-level performance (CTR, CVR, conversions)
- Ad strength ratings
- Headline/description text and patterns
- Policy status
- Performance vs account average

**I cannot assess (API limitation):**
- Individual headline/description performance scores
- Combination-level performance
- Impression share by asset
- Asset-level Quality Score

**For asset-level details:**
- Use Google Ads UI → Assets → "View asset details"
- Export asset performance report manually
- Provide as supplementary input

---

## Quality Checklist

Before delivering analysis:
- [ ] Ads ranked by CTR and CVR
- [ ] Ad strength vs performance comparison included
- [ ] Top headline patterns identified
- [ ] Underperformers flagged with specific issues
- [ ] Suggested new headlines provided
- [ ] Quick wins prioritized by impact
- [ ] Composability next steps noted
