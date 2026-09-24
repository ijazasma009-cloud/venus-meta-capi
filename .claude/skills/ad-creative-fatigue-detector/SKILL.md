---
name: ad-creative-fatigue-detector
description: Identifies creative fatigue across ad platforms by analyzing performance decay patterns, frequency metrics, and engagement trends. Triggers when user asks "why is my ad performance dropping?", "are my creatives fatigued?", or wants to know when to rotate creative. Works across Meta, Google, TikTok, and LinkedIn. Provides rotation schedules and refresh priorities.
---

# Ad Creative Fatigue Detector

Your best ad today is tomorrow's worst performer. Catch fatigue before it kills your CPA.

## Core Philosophy

**Creative fatigue is inevitable.** Every ad has a lifecycle. The question isn't if it will fatigue—it's when, and whether you'll catch it in time.

**The Fatigue Trap:** Most advertisers notice fatigue after it's already cost them thousands. By the time CPA spikes, the damage is done.

**The Three Laws of Creative Fatigue:**
1. **Frequency is the leading indicator:** High frequency = fast fatigue
2. **CTR decays before CPA spikes:** Watch click-through rate, not just cost
3. **Winners fatigue fastest:** Your best ads get the most impressions—and burn out quickest

---

## Required Context

### Must Have

**1. Creative Performance Data**
For each active ad/creative:
- Ad name or identifier
- Format (video, image, carousel, etc.)
- Impressions (total or daily)
- Click-through rate (CTR)
- Days running
- Current CPA or conversion rate

**2. Time Series Data**
At minimum:
- Performance by week (CTR and/or CPA)
- OR performance comparison: first 7 days vs. last 7 days

### Strongly Recommended

**3. Engagement Metrics (especially for video)**
- Hook rate / thumb-stop rate (% watched 3+ seconds)
- Average watch time or % completion
- Engagement rate (likes, comments, shares)

**4. Frequency Data**
- Ad-level or ad set-level frequency
- Audience size
- Days since launch

**5. Platform Context**
- Which platform (Meta, Google, TikTok, LinkedIn)
- Campaign type (prospecting vs. retargeting)
- Audience type (broad vs. narrow)

### Nice to Have

- Historical performance of similar creatives
- Baseline metrics for this account/vertical
- Creative refresh history (when were new ads added?)
- Seasonal context

---

## Fatigue Detection Framework

### Primary Fatigue Indicators

**Indicator 1: CTR Decay**
The most reliable early warning sign.

| CTR Change | Fatigue Level | Action |
|------------|---------------|--------|
| Stable (±10%) | None | Monitor |
| -10% to -20% | Early | Prepare rotation |
| -20% to -35% | Moderate | Rotate within 1 week |
| -35% to -50% | Severe | Rotate immediately |
| >-50% | Critical | Pause, replace now |

**Indicator 2: Frequency Threshold**
Platform-specific thresholds where fatigue accelerates:

| Platform | Prospecting | Retargeting | Critical |
|----------|-------------|-------------|----------|
| Meta | 2.5-3.0 | 4.0-5.0 | >6.0 |
| TikTok | 3.0-4.0 | 5.0-6.0 | >7.0 |
| LinkedIn | 4.0-5.0 | 6.0-8.0 | >10.0 |
| Google Display | 3.0-4.0 | 5.0-6.0 | >8.0 |
| YouTube | 2.0-3.0 | 3.0-4.0 | >5.0 |

**Indicator 3: Hook Rate Decay (Video)**
For video ads, watch the first 3 seconds.

| Hook Rate Change | Status |
|------------------|--------|
| -0% to -15% | Normal variance |
| -15% to -30% | Early fatigue |
| >-30% | Severe fatigue |

**Indicator 4: CPA Inflation**
Lagging indicator—by the time CPA rises, you've already lost money.

| CPA Change | Status |
|------------|--------|
| +0% to +15% | Acceptable variance |
| +15% to +30% | Fatigue likely present |
| >+30% | Fatigue confirmed |

---

### Fatigue Velocity Factors

**Factors that accelerate fatigue:**

| Factor | Impact | Why |
|--------|--------|-----|
| Narrow audience | Fast fatigue | Same people see ad repeatedly |
| High spend | Fast fatigue | Burns through audience quickly |
| Retargeting | Fast fatigue | Small pool, high frequency |
| Single creative | Fast fatigue | No variety to spread impressions |
| Static image | Moderate fatigue | Less engaging than video |
| Viral creative | Fast fatigue | Algorithm pushes hard, burns fast |

**Factors that slow fatigue:**

| Factor | Impact | Why |
|--------|--------|-----|
| Broad audience | Slow fatigue | Fresh eyeballs continuously |
| Multiple creatives | Slow fatigue | Impressions spread across ads |
| Video content | Slower fatigue | More engaging, longer view time |
| Lower frequency cap | Slow fatigue | Limits exposure per person |
| Dynamic creative | Slow fatigue | Variations extend lifespan |

---

### Creative Lifecycle Model

```
PERFORMANCE
    │
    │    ╭──────╮
    │   ╱        ╲          ← Learning → Peak → Fatigue
    │  ╱          ╲
    │ ╱            ╲
    │╱              ╲
    │                ╲
    └─────────────────────────────────── TIME

    |← Learning →|←  Peak  →|← Fatigue →|← Exhausted →|
       (1-2 wks)   (2-6 wks)   (2-4 wks)    (pause)
```

**Typical Creative Lifespans by Platform:**

| Platform | Prospecting | Retargeting |
|----------|-------------|-------------|
| Meta | 3-6 weeks | 2-4 weeks |
| TikTok | 2-4 weeks | 1-3 weeks |
| LinkedIn | 6-10 weeks | 4-6 weeks |
| Google Display | 4-8 weeks | 3-5 weeks |
| YouTube | 4-8 weeks | 3-5 weeks |

---

## Fatigue Scoring Model

### Calculate Fatigue Score (0-100)

```
Fatigue Score = (CTR Decay Score × 0.4) +
                (Frequency Score × 0.3) +
                (Age Score × 0.2) +
                (CPA Score × 0.1)
```

**CTR Decay Score (0-100):**
- No decay: 0
- 10% decay: 25
- 20% decay: 50
- 35% decay: 75
- 50%+ decay: 100

**Frequency Score (0-100):**
- Below threshold: 0
- At threshold: 50
- 50% above threshold: 75
- 2x threshold: 100

**Age Score (0-100):**
- <2 weeks: 0
- 2-4 weeks: 25
- 4-6 weeks: 50
- 6-8 weeks: 75
- >8 weeks: 100

**CPA Score (0-100):**
- At or below baseline: 0
- 15% above: 25
- 30% above: 50
- 50% above: 75
- >50% above: 100

**Interpretation:**

| Score | Status | Action |
|-------|--------|--------|
| 0-25 | Fresh | Monitor weekly |
| 26-45 | Healthy | Prepare backup creative |
| 46-65 | Early Fatigue | Rotate within 2 weeks |
| 66-80 | Moderate Fatigue | Rotate within 1 week |
| 81-100 | Severe Fatigue | Pause/rotate immediately |

---

## Output Format

### Creative Fatigue Report

```
═══════════════════════════════════════════════════════════════
CREATIVE FATIGUE ANALYSIS
Platform: [Platform]
Analysis Period: [Date Range]
Total Creatives Analyzed: [X]
Creatives Needing Rotation: [X]
═══════════════════════════════════════════════════════════════
```

---

### Fatigue Summary Dashboard

**Overall Creative Health: [HEALTHY/WARNING/CRITICAL]**

```
Creative Status Distribution:
Fresh (0-25):        ████████ [X] creatives
Healthy (26-45):     ██████ [X] creatives
Early Fatigue (46-65): ████ [X] creatives
Moderate Fatigue (66-80): ██ [X] creatives
Severe Fatigue (81-100): █ [X] creatives
```

**Urgent Attention Required:** [X] creatives need immediate rotation

---

### Creative-Level Analysis

**CRITICAL - Rotate Immediately:**

| Creative | Format | Days Live | Fatigue Score | CTR Decay | Frequency | Action |
|----------|--------|-----------|---------------|-----------|-----------|--------|
| [Name] | [Format] | [X] | [X]/100 | -[X]% | [X] | Pause now |

**WARNING - Rotate Within 1 Week:**

| Creative | Format | Days Live | Fatigue Score | CTR Decay | Frequency | Action |
|----------|--------|-----------|---------------|-----------|-----------|--------|
| [Name] | [Format] | [X] | [X]/100 | -[X]% | [X] | Prepare rotation |

**MONITOR - Early Signs:**

| Creative | Format | Days Live | Fatigue Score | CTR Decay | Frequency | Status |
|----------|--------|-----------|---------------|-----------|-----------|--------|
| [Name] | [Format] | [X] | [X]/100 | -[X]% | [X] | Watch CTR |

**HEALTHY - No Action:**

| Creative | Format | Days Live | Fatigue Score | Status |
|----------|--------|-----------|---------------|--------|
| [Name] | [Format] | [X] | [X]/100 | Performing well |

---

### Detailed Creative Analysis

**[Creative Name]**
```
Status: [CRITICAL/WARNING/MONITOR/HEALTHY]
Fatigue Score: [X]/100

Performance Timeline:
Week 1: CTR [X]% | CPA $[X] | Freq [X] ← Baseline
Week 2: CTR [X]% | CPA $[X] | Freq [X] | Change: [X]%
Week 3: CTR [X]% | CPA $[X] | Freq [X] | Change: [X]%
Week 4: CTR [X]% | CPA $[X] | Freq [X] | Change: [X]%

Decay Analysis:
- CTR: [X]% → [X]% ([X]% decline)
- CPA: $[X] → $[X] ([X]% increase)
- Frequency: [X] (vs [X] threshold)

Diagnosis: [Why this creative is fatiguing]
Recommendation: [Specific action]
```

---

### Video Creative Analysis (if applicable)

| Video | Hook Rate Wk1 | Hook Rate Now | Decay | Avg Watch Time | Status |
|-------|---------------|---------------|-------|----------------|--------|
| [Name] | [X]% | [X]% | -[X]% | [X]s | [Status] |

**Video-Specific Insights:**
- [Insight about hook rate patterns]
- [Insight about watch time degradation]

---

### Campaign/Ad Set Context

**High-Risk Ad Sets (accelerating fatigue):**

| Ad Set | Audience Size | Frequency | Creatives | Risk Level |
|--------|---------------|-----------|-----------|------------|
| [Name] | [X]M | [X] | [X] | HIGH |

**Notes:** [Why these ad sets are burning creative faster]

---

### Rotation Schedule

**Immediate (This Week):**
1. [ ] Pause [Creative Name] - Fatigue score [X]
2. [ ] Replace with [new creative type/angle]

**Next Week:**
1. [ ] Prepare rotation for [Creative Name]
2. [ ] Test [X] new variations of [winning angle]

**2-3 Weeks:**
1. [ ] Monitor [Creative Name] for fatigue signs
2. [ ] Have backup ready for [Creative Name]

---

### Creative Pipeline Recommendations

**Current Velocity:**
- Creatives launched last 30 days: [X]
- Average creative lifespan: [X] weeks
- Rotation rate needed: [X] new creatives per week

**Recommended Pipeline:**
- Always have [X] creatives in testing
- Plan [X] new creatives per week
- Keep [X] proven concepts ready for iteration

**Creative Types to Test:**
Based on what's fatiguing:
1. [Recommendation based on analysis]
2. [Recommendation based on analysis]
3. [Recommendation based on analysis]

---

### Fatigue Prevention Strategies

**For This Account:**
1. [Specific strategy based on analysis]
2. [Specific strategy based on analysis]
3. [Specific strategy based on analysis]

**General Best Practices:**
- Set frequency caps on prospecting (3.0 for Meta)
- Run 3-5 creatives per ad set minimum
- Iterate on winners before they fatigue (variations)
- Monitor CTR weekly, not just CPA

---

## Platform-Specific Guidance

### Meta Ads
- Watch frequency most closely
- Hook rate decay is early warning for video
- Consider Advantage+ Creative for auto-optimization
- Dynamic creative can extend lifespan

### Google Display/YouTube
- Frequency data less granular—use time-based rotation
- Rotate every 6-8 weeks proactively
- Performance Max obscures creative data—check asset reports

### TikTok
- Fastest fatigue of any platform
- Trend-based content fatigues even faster
- Plan 2-week creative cycles
- Hook rate is everything

### LinkedIn
- Slower fatigue due to smaller audiences
- Can run longer before rotation
- But when fatigued, hard to recover
- B2B audiences are finite—refresh matters

---

## Limitations

**I can provide:**
- Fatigue scoring and prioritization
- Rotation schedules and timelines
- Pattern identification
- Prevention recommendations

**I cannot provide:**
- New creative concepts or copywriting
- Visual design or video editing
- Audience strategy (separate skill)
- Attribution analysis

**For better analysis, also provide:**
- Week-over-week performance data (not just current snapshot)
- Frequency data at ad or ad set level
- Hook rate / video metrics if running video
- Audience sizes

---

## Quality Checklist

Before delivering analysis:
- [ ] All creatives scored with consistent methodology
- [ ] Urgency levels clearly indicated
- [ ] Rotation schedule is actionable
- [ ] Platform-specific thresholds applied
- [ ] Root causes identified (not just symptoms)
- [ ] Prevention strategies included
- [ ] Pipeline recommendations based on actual velocity needs
