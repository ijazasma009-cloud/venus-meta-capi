---
name: creative-fatigue-detector
description: Monitors ad creative performance trends to identify fatigue before it tanks results, with refresh timing recommendations.
---

# Creative Fatigue Detector

## Purpose

Identify creative fatigue BEFORE it destroys performance by monitoring:
- Declining engagement metrics over time
- Rising costs as algorithms struggle to find new audiences
- Frequency thresholds that indicate audience saturation
- Performance decay patterns that signal refresh timing

**Core Philosophy:** By the time you notice a creative is "tired," you've already wasted budget. Catch fatigue at the first signs, not the obituary.

---

## When to Use This Skill

- Weekly monitoring of active creatives (recommended)
- When CPMs start rising without explanation
- When CTR drops on previously strong performers
- Before deciding whether to refresh or kill a creative
- When scaling spend (higher spend = faster fatigue)

---

## Required Context

| Data Point | Required | Notes |
|------------|----------|-------|
| Daily/weekly performance by creative | Yes | Need time series data |
| Frequency metrics | Yes | Avg frequency per user |
| CPM over time | Yes | Key fatigue indicator |
| CTR over time | Yes | Engagement decay signal |
| Conversion rate over time | Yes | Bottom-line impact |
| Days running | Yes | Duration in market |
| Cumulative reach | Helpful | Audience exhaustion signal |
| Audience size | Helpful | Context for frequency |

---

## The Fatigue Lifecycle

Every creative follows a predictable lifecycle:

```
PERFORMANCE
    ^
    │         ╭─────╮
    │        ╱       ╲
    │       ╱         ╲
    │      ╱           ╲ ← Peak Performance
    │     ╱             ╲
    │    ╱               ╲
    │   ╱                 ╲
    │  ╱   Learning        ╲  Fatigue
    │ ╱     Phase           ╲  Phase
    │╱                       ╲
    └──────────────────────────────────→ TIME
        │         │          │
      Launch    Peak       Decline
      (3-7d)   (varies)   (action needed)
```

**Typical Timeline by Spend Level:**

| Daily Spend | Learning Phase | Peak Performance | Fatigue Onset |
|-------------|----------------|------------------|---------------|
| < $50/day | 7-14 days | 3-6 weeks | 6-10 weeks |
| $50-200/day | 5-10 days | 2-4 weeks | 4-6 weeks |
| $200-500/day | 3-7 days | 1-3 weeks | 2-4 weeks |
| $500+/day | 2-5 days | 1-2 weeks | 1-3 weeks |

---

## Fatigue Detection Framework

### Primary Fatigue Signals

Monitor these metrics for week-over-week changes:

| Signal | Yellow Flag | Red Flag | Critical |
|--------|-------------|----------|----------|
| **CTR Decline** | -10% WoW | -20% WoW | -30%+ WoW |
| **CPM Increase** | +15% WoW | +25% WoW | +40%+ WoW |
| **CPA Increase** | +15% WoW | +25% WoW | +40%+ WoW |
| **Frequency** | > 2.5 | > 3.5 | > 5.0 |
| **Hook Rate Decline** (video) | -15% WoW | -25% WoW | -35%+ WoW |

### Secondary Fatigue Signals

| Signal | Warning Threshold | Notes |
|--------|-------------------|-------|
| Reach plateau | < 5% new reach in 7 days | Audience exhausted |
| Negative feedback spike | > 50% increase | Users actively hiding/blocking |
| Share/Save decline | -30% WoW | Content no longer resonates |
| Comment sentiment shift | Negative increase | Audience turning on creative |

---

## Fatigue Scoring System

Calculate a Fatigue Score (0-100) for each creative:

### Component Weights

| Component | Weight | Calculation |
|-----------|--------|-------------|
| CTR Decay | 25% | (Current CTR / Peak CTR) × 100 |
| CPM Inflation | 25% | (Peak CPM / Current CPM) × 100 |
| Frequency Pressure | 20% | Max(0, 100 - (Frequency × 20)) |
| Performance Trend | 20% | 7-day trend direction score |
| Days Running | 10% | Decay curve based on spend level |

### Fatigue Score Interpretation

| Score | Status | Recommended Action |
|-------|--------|-------------------|
| 80-100 | **Fresh** | Full steam ahead |
| 60-79 | **Healthy** | Monitor weekly |
| 40-59 | **Early Fatigue** | Prepare refresh, reduce by 20% |
| 20-39 | **Fatigued** | Reduce spend 50%, launch replacement |
| 0-19 | **Exhausted** | Pause immediately |

---

## Fatigue Pattern Recognition

### Pattern 1: Sudden Death
```
Performance: ████████████▁▁▁
Timeline:    ─────────────────→
Cause: Usually algorithm/audience change, not true fatigue
Action: Check for external factors before pausing
```

### Pattern 2: Gradual Decline
```
Performance: ████████▇▇▆▅▄▃▂
Timeline:    ─────────────────→
Cause: Classic fatigue - audience saturation
Action: Begin refresh at ▇ stage, pause at ▃ stage
```

### Pattern 3: Plateau then Drop
```
Performance: ████████████████▄▂
Timeline:    ─────────────────→
Cause: Reached maximum viable audience
Action: Audience expansion or creative refresh needed
```

### Pattern 4: Oscillating Decline
```
Performance: ████▆████▅███▃██▂
Timeline:    ─────────────────→
Cause: Inconsistent delivery, possible targeting issues
Action: Check audience overlap, consider consolidation
```

---

## Frequency Analysis Deep Dive

Frequency is the #1 predictor of fatigue:

### Frequency Thresholds by Objective

| Campaign Objective | Safe Zone | Caution | Danger |
|-------------------|-----------|---------|--------|
| Awareness/Reach | < 3.0 | 3.0-5.0 | > 5.0 |
| Consideration | < 2.5 | 2.5-4.0 | > 4.0 |
| Conversions | < 2.0 | 2.0-3.5 | > 3.5 |
| Retargeting | < 4.0 | 4.0-7.0 | > 7.0 |

### Frequency vs. Audience Size Rule

```
Safe Frequency Limit ≈ Audience Size / (Daily Reach × Days Running)

If actual frequency > Safe Limit × 1.5 → Fatigue risk HIGH
```

---

## Time-Series Analysis Template

Track each creative across these periods:

| Metric | Week 1 | Week 2 | Week 3 | Week 4 | Trend | Alert |
|--------|--------|--------|--------|--------|-------|-------|
| CTR | | | | | | |
| CPM | | | | | | |
| CPA | | | | | | |
| ROAS | | | | | | |
| Frequency | | | | | | |
| Conv Rate | | | | | | |
| Hook Rate | | | | | | |

**Trend Calculation:**
- ↑ = Improving (>5% better than previous)
- → = Stable (within ±5%)
- ↓ = Declining (<5% worse than previous)
- ↓↓ = Rapid Decline (>15% worse)

---

## Creative Lifespan Estimation

Based on current trajectory, estimate remaining viable days:

### Calculation Method

```
Remaining Days = Days to Threshold / Current Decay Rate

Where:
- Days to Threshold = days until CPA exceeds target by 30%
- Current Decay Rate = (This Week CPA - Last Week CPA) / Last Week CPA
```

### Lifespan Categories

| Estimated Remaining Life | Status | Action |
|-------------------------|--------|--------|
| > 21 days | Healthy runway | Continue monitoring |
| 14-21 days | Moderate runway | Brief replacement creative |
| 7-14 days | Short runway | Launch replacement NOW |
| < 7 days | Critical | Replacement should be live |

---

## Refresh vs. Kill Decision Matrix

When fatigue is detected, decide between refresh and kill:

| Factor | Refresh | Kill |
|--------|---------|------|
| Peak performance | Top 20% of account | Bottom 50% of account |
| Brand value | High brand consistency | Generic/replaceable |
| Production cost | High (video, UGC) | Low (static) |
| Pattern history | First fatigue cycle | 2nd+ fatigue cycle |
| Audience response | Positive comments | Negative feedback |

**Decision Formula:**
- If creative was ever a Star (Tier 1) AND it's first fatigue cycle → **Refresh**
- If creative never exceeded Average (Tier 4) → **Kill**
- If 2nd fatigue cycle with refresh already attempted → **Kill**

---

## Refresh Strategies

When refreshing rather than killing:

### Light Refresh (Extends life 2-4 weeks)
- Change thumbnail/cover image
- Update headline/primary text
- Modify CTA
- Adjust color scheme

### Medium Refresh (Extends life 4-6 weeks)
- New opening hook (first 3 seconds)
- Different aspect ratio version
- Add/remove sound
- Re-edit with different pacing

### Heavy Refresh (Essentially new creative)
- New footage/imagery
- Different creator/model
- New concept, same product
- Complete re-brief

---

## Output Deliverables

### 1. Creative Health Dashboard

```
CREATIVE FATIGUE REPORT
Generated: [Date]
Period Analyzed: [Last 4 weeks]

OVERALL HEALTH SCORE: [X]/100

SUMMARY:
├── Fresh (80-100): [X] creatives
├── Healthy (60-79): [X] creatives
├── Early Fatigue (40-59): [X] creatives ⚠️
├── Fatigued (20-39): [X] creatives 🔴
└── Exhausted (0-19): [X] creatives 💀
```

### 2. Fatigue Alert List

| Creative | Fatigue Score | Key Signal | Est. Life | Action |
|----------|---------------|------------|-----------|--------|
| | | | | |

### 3. Trending Concerns

Creatives showing early warning signs (healthy now, but trending down):

| Creative | Current Score | Trend | Watch Metric |
|----------|---------------|-------|--------------|
| | | | |

### 4. Refresh Queue

Creatives recommended for refresh rather than kill:

| Creative | Priority | Refresh Type | Timing |
|----------|----------|--------------|--------|
| | | | |

### 5. Kill List

Creatives beyond saving:

| Creative | Score | Wasted Spend (Last 7d) | Replacement Status |
|----------|-------|------------------------|-------------------|
| | | | |

---

## Proactive Fatigue Prevention

### Production Pipeline Rule

```
For every $X in ad spend, produce Y new creatives:

| Monthly Spend | New Creatives/Month | Reasoning |
|---------------|---------------------|-----------|
| < $5K | 2-4 | Low fatigue pressure |
| $5K-$20K | 4-8 | Moderate rotation needed |
| $20K-$50K | 8-15 | Active rotation required |
| $50K-$100K | 15-25 | Continuous production |
| $100K+ | 25+ | Creative team/agency needed |
```

### Rotation Strategy

- Never let a single creative exceed 40% of total spend
- Maintain 3-5 active creatives minimum per audience
- Launch new creative before old one hits "Fatigued" status
- A/B test refreshes against originals

---

## Integration with Other Skills

| Use Case | Connected Skill | Purpose |
|----------|-----------------|---------|
| Fatigued Star creative | → meta-ads-creative-ranker | Identify what made it win |
| Ready to refresh | → ugc-brief-generator | Brief replacement content |
| Multiple fatigued | → social-ads-budget-allocator | Reallocate away from fatigued |
| Pattern across audiences | → audience-overlap-mapper | Check if fatigue is audience-specific |

---

## Limitations

- Cannot predict algorithm changes that affect delivery
- Requires minimum 2 weeks of data for trend analysis
- Small audiences fatigue faster than estimates suggest
- Seasonal factors can mimic fatigue patterns
- Cannot assess creative quality, only performance metrics

---

## Quality Checklist Before Delivery

- [ ] Minimum 2 weeks of data analyzed per creative
- [ ] Fatigue scores calculated for all active creatives
- [ ] Time-series trends documented (not just current snapshot)
- [ ] Frequency analysis completed
- [ ] Lifespan estimates provided for concerning creatives
- [ ] Clear Refresh vs. Kill recommendations
- [ ] Production pipeline recommendation included
- [ ] Early warning list provided (not just current problems)
