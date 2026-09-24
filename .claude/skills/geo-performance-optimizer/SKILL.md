---
name: geo-performance-optimizer
description: Analyzes geographic performance using Google Ads MCP data. Identifies top/bottom performing locations, recommends geo bid adjustments, and finds location expansion opportunities. Triggers when user asks about location performance, geo targeting, or regional efficiency. Pulls live data via user_location_view action.
---

# Geo Performance Optimizer

Find where your ads are killing it and where they're dying. Optimize bids by location to get more conversions from the same budget.

## Core Philosophy

**Location is a hidden lever.** Most advertisers set geo targeting and forget it. The smart ones constantly adjust bids based on where conversions actually come from.

**The Geo Questions:**
1. Which locations are driving efficient conversions?
2. Which locations are bleeding money?
3. Where should I increase/decrease bids?
4. Are there locations I'm missing?

---

## MCP Integration

### Required Data Pull

Use the Google Ads MCP `user_location_view` action with this GAQL query:

```
SELECT
  campaign.id,
  campaign.name,
  user_location_view.country_criterion_id,
  user_location_view.targeting_location,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions,
  metrics.conversions_value,
  metrics.ctr,
  metrics.average_cpc,
  metrics.cost_per_conversion
FROM user_location_view
WHERE segments.date BETWEEN '{start_date}' AND '{end_date}'
  AND metrics.impressions > 0
ORDER BY metrics.cost_micros DESC
```

### Supplementary Query (Geographic View)

For country-level aggregation, also pull `geographic_view`:

```
SELECT
  campaign.id,
  campaign.name,
  geographic_view.country_criterion_id,
  geographic_view.location_type,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions
FROM geographic_view
WHERE segments.date BETWEEN '{start_date}' AND '{end_date}'
```

### Data Requirements

**From MCP Response:**
- `user_location_view.targeting_location` - Whether location is targeted
- `user_location_view.country_criterion_id` - Location identifier
- `metrics.cost_micros`, `metrics.conversions`, `metrics.clicks`
- `metrics.cost_per_conversion` - CPA by location
- `metrics.average_cpc` - Avg CPC by location

**User Should Provide:**
- Target CPA or ROAS
- Date range (default: last 30 days)
- Service area constraints (if any)
- Current geo bid adjustments (if known)

---

## Analysis Framework

### Tier 1: Location Performance Ranking

**Performance Buckets:**

| Tier | CPA vs Target | Volume | Action |
|------|---------------|--------|--------|
| Star | <75% of target | High | Increase bid +15-25% |
| Solid | 75-100% of target | Any | Maintain or slight increase |
| Average | 100-125% of target | Any | Monitor, no change |
| Underperformer | 125-175% of target | Any | Decrease bid -15-25% |
| Bleeder | >175% of target | Any | Decrease bid -30-50% |
| Dead Zone | High spend, 0 conv | Any | Exclude or -50% bid |

---

### Tier 2: Volume-Weighted Analysis

**Not all locations are equal.** A location with 2 conversions at $40 CPA is less reliable than one with 50 conversions at $45 CPA.

**Statistical Confidence:**

| Conversions | Confidence | Action Threshold |
|-------------|------------|------------------|
| 1-2 | Low | Don't adjust, monitor |
| 3-5 | Medium | Adjust if trend clear |
| 6-10 | Good | Make moderate adjustments |
| 11+ | High | Full adjustment confidence |

**Spend Significance:**
- Minimum $50 spend to evaluate
- Minimum $200 spend for confident adjustment
- High volume = more reliable CPA signal

---

### Tier 3: Bid Adjustment Calculation

**Bid Modifier Formula:**

```
Target CPA: $50
Location CPA: $40

Efficiency Ratio = Target / Actual = 50 / 40 = 1.25 (25% more efficient)
Recommended Bid Modifier = +25%

Location CPA: $75
Efficiency Ratio = 50 / 75 = 0.67 (33% less efficient)
Recommended Bid Modifier = -33%
```

**Adjustment Caps:**
- Maximum increase: +50% (avoid overspending before validation)
- Maximum decrease: -50% (keep some presence for data)
- Zero conversion locations: -50% or exclude

---

### Tier 4: Expansion Opportunities

**Signals for Location Expansion:**
- Adjacent markets to top performers
- Similar demographic profiles
- Underserved areas with low competition

**Signals for Location Exclusion:**
- Consistent 0 conversions with $100+ spend
- CPA consistently 3x+ target
- Outside service area

---

## Output Format

### Executive Summary

```
GEO PERFORMANCE HEALTH: 🟢/🟡/🔴
Locations Analyzed: XXX
Period: [dates]
Top Performing Region: [location] (CPA: $XX)
Worst Performing Region: [location] (CPA: $XX)
Estimated Monthly Savings from Optimization: $X,XXX
```

---

### Top Performers (Increase Bids)

| Rank | Location | Spend | Conv | CPA | vs Target | Rec. Bid Adj |
|------|----------|-------|------|-----|-----------|--------------|
| 1 | [City/State] | $X,XXX | XX | $XX | -XX% | +XX% |
| 2 | [City/State] | $X,XXX | XX | $XX | -XX% | +XX% |
| 3 | [City/State] | $X,XXX | XX | $XX | -XX% | +XX% |

**Why These Locations Win:**
- [Observation about top performers]
- [Pattern or demographic insight]

---

### Underperformers (Decrease Bids)

| Rank | Location | Spend | Conv | CPA | vs Target | Rec. Bid Adj |
|------|----------|-------|------|-----|-----------|--------------|
| 1 | [City/State] | $X,XXX | X | $XXX | +XX% | -XX% |
| 2 | [City/State] | $X,XXX | X | $XXX | +XX% | -XX% |

**Why These Locations Struggle:**
- [Observation about underperformers]
- [Possible reasons: competition, intent mismatch, etc.]

---

### Dead Zones (Exclude or Minimize)

| Location | Spend | Conv | Clicks | Recommendation |
|----------|-------|------|--------|----------------|
| [City/State] | $XXX | 0 | XX | Exclude |
| [City/State] | $XXX | 0 | XX | -50% bid |

---

### Bid Adjustment Implementation

**Campaign: [Campaign Name]**

| Location | Current Adj | Recommended | Change |
|----------|-------------|-------------|--------|
| [Location] | +0% | +25% | +25% |
| [Location] | +0% | -30% | -30% |
| [Location] | +10% | +20% | +10% |

**Copy-Paste for Bulk Edit:**
```
Location, Bid Adjustment
[Location 1], +25%
[Location 2], -30%
[Location 3], +20%
```

---

### Geographic Distribution

```
REGION          SPEND     CONV    CPA      % of TOTAL
────────────────────────────────────────────────────
[Region 1]      $X,XXX    XX      $XX      XX%
[Region 2]      $X,XXX    XX      $XX      XX%
[Region 3]      $X,XXX    XX      $XX      XX%
National Avg    $X,XXX    XX      $XX      100%
```

---

### Expansion Recommendations

**Consider Adding:**
- [Location] - Adjacent to top performer [X], similar demographics
- [Location] - Underserved market, low competition signals

**Consider Excluding:**
- [Location] - 90-day 0 conversions, $XXX wasted
- [Location] - Consistently 3x+ target CPA

---

### Impact Projection

**If All Recommendations Implemented:**

| Metric | Current | Projected | Change |
|--------|---------|-----------|--------|
| Total Spend | $XX,XXX | $XX,XXX | — |
| Conversions | XXX | XXX | +XX% |
| Blended CPA | $XX | $XX | -XX% |

**Confidence Level:** High / Medium / Low

**Assumptions:**
- Bid increases don't exhaust efficient inventory
- CPA patterns hold with bid changes
- No major market shifts

---

## Composability

**Chains from:**
- `budget-allocation-optimizer` - Geo insights inform budget decisions

**Chains to:**
- `scaling-roadmap-builder` - Top geos feed expansion strategy
- MCP `add_location_targeting` - Can implement targeting changes

---

## Limitations

**I can assess:**
- Location-level CPA and efficiency
- Bid adjustment recommendations
- Spend distribution by geography
- Expansion/exclusion candidates

**I cannot assess:**
- User location vs targeted location nuances
- Local competitive landscape
- Offline conversion attribution by location
- Seasonality patterns by region

**For deeper geo analysis:**
- Review auction insights by location (Google Ads UI)
- Check device × location cross-segments
- Validate with backend conversion quality data

---

## Quality Checklist

Before delivering analysis:
- [ ] Locations ranked by CPA efficiency
- [ ] Volume/confidence noted for each
- [ ] Bid adjustments calculated with formula
- [ ] Dead zones identified with spend impact
- [ ] Copy-paste format provided for implementation
- [ ] Expansion opportunities noted
- [ ] Impact projection included
