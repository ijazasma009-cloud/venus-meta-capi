---
name: meta-ads-creative-ranker
description: Analyzes Meta (Facebook/Instagram) ad creative performance to identify winners, losers, and the patterns that drive results.
---

# Meta Ads Creative Ranker

## Purpose

Transform raw Meta Ads creative data into actionable insights that answer:
- Which creatives are actually driving profitable results?
- What creative patterns (hooks, formats, CTAs) consistently win?
- Where is creative spend being wasted?
- What should we test next based on winning patterns?

**Core Philosophy:** Ad Strength and Relevance Scores lie. Engagement metrics deceive. Only conversion data tells the truth.

---

## When to Use This Skill

- Weekly creative performance reviews
- Before scaling ad spend (know what to scale)
- When creative performance declines
- Before briefing new creative production
- When ROAS drops despite "good" engagement

---

## Required Context

| Data Point | Required | Notes |
|------------|----------|-------|
| Ad-level performance export | Yes | Last 7-30 days minimum |
| Spend per ad | Yes | Need volume for statistical validity |
| Conversions/purchases per ad | Yes | Primary success metric |
| Cost per conversion (CPA) or ROAS | Yes | Efficiency metric |
| CTR (Click-through rate) | Yes | Engagement signal |
| CPM (Cost per 1000 impressions) | Yes | Delivery/competition signal |
| Hook rate (3-sec video views / impressions) | If video | Video engagement metric |
| Hold rate (ThruPlays / 3-sec views) | If video | Content quality signal |
| Creative assets (or descriptions) | Helpful | For pattern analysis |
| Account average CPA/ROAS | Helpful | Benchmark for categorization |

---

## Analysis Framework

### Step 1: Data Sufficiency Check

Before analyzing, verify each creative has enough data:

| Spend Level | Minimum for Analysis | Confidence |
|-------------|---------------------|------------|
| < $50 | Skip - insufficient data | None |
| $50-$200 | Directional only | Low |
| $200-$500 | Analyze with caution | Medium |
| $500-$1,000 | Reliable analysis | High |
| $1,000+ | High confidence | Very High |

**Rule:** Never make definitive judgments on creatives with < $200 spend. They haven't had a fair chance.

---

### Step 2: Creative Performance Tiers

Categorize each creative into one of 6 tiers based on efficiency AND volume:

| Tier | Name | Criteria | Action |
|------|------|----------|--------|
| 1 | **Stars** | CPA < 70% of avg AND spend > $500 | Scale immediately, analyze patterns |
| 2 | **Solid Performers** | CPA 70-100% of avg AND spend > $300 | Maintain, test iterations |
| 3 | **Promising** | CPA < 100% of avg BUT spend < $300 | Increase budget, needs more data |
| 4 | **Average** | CPA 100-130% of avg | Monitor, consider refresh |
| 5 | **Underperformers** | CPA 130-200% of avg | Pause or reduce spend |
| 6 | **Bleeders** | CPA > 200% of avg OR 0 conversions with $200+ spend | Kill immediately |

**For ROAS-focused accounts:**
- Stars: ROAS > 143% of target
- Solid: ROAS 100-143% of target
- Promising: ROAS > target but low spend
- Average: ROAS 77-100% of target
- Underperformers: ROAS 50-77% of target
- Bleeders: ROAS < 50% of target

---

### Step 3: The Engagement vs. Efficiency Matrix

Plot creatives on this matrix to identify deceptive performers:

```
                    HIGH EFFICIENCY (Low CPA / High ROAS)
                              │
         "HIDDEN GEMS"        │        "TRUE STARS"
         Low engagement,      │        High engagement,
         high conversion.     │        high conversion.
         Scale carefully.     │        Scale aggressively.
                              │
    LOW  ─────────────────────┼───────────────────── HIGH
    ENGAGEMENT                │                ENGAGEMENT
    (CTR)                     │                (CTR)
                              │
         "SILENT FAILURES"    │        "ENGAGEMENT TRAPS"
         Low engagement,      │        High engagement,
         low conversion.      │        low conversion.
         Kill or refresh.     │        DANGER: Looks good, wastes money.
                              │
                    LOW EFFICIENCY (High CPA / Low ROAS)
```

**Critical Insight:** "Engagement Traps" are the most dangerous. High CTR, lots of likes/comments, but no conversions. These fool many advertisers into scaling losers.

---

### Step 4: Video Creative Deep Dive (If Applicable)

For video ads, analyze the funnel:

| Metric | Calculation | Benchmark | What It Tells You |
|--------|-------------|-----------|-------------------|
| **Hook Rate** | 3-sec views / Impressions | > 30% good, > 40% excellent | Does the opening grab attention? |
| **Hold Rate** | ThruPlays / 3-sec views | > 20% good, > 30% excellent | Does content maintain interest? |
| **Click Rate** | Clicks / ThruPlays | > 5% good, > 10% excellent | Does CTA drive action? |
| **Convert Rate** | Conversions / Clicks | Varies by offer | Does landing page deliver? |

**Funnel Diagnosis:**

| Pattern | Diagnosis | Fix |
|---------|-----------|-----|
| Low Hook Rate | Opening doesn't grab | Test new first 3 seconds |
| High Hook, Low Hold | Content loses interest | Tighten middle, faster pacing |
| High Hold, Low Click | Weak CTA or unclear offer | Stronger end card, clearer CTA |
| High Click, Low Convert | Landing page problem | Not a creative issue |

---

### Step 5: Creative Pattern Analysis

Identify patterns across winning vs. losing creatives:

#### A. Format Performance

| Format | Avg CPA | Conversion Volume | Verdict |
|--------|---------|-------------------|---------|
| Static Image | $ | | |
| Carousel | $ | | |
| Video (< 15s) | $ | | |
| Video (15-30s) | $ | | |
| Video (30s+) | $ | | |
| UGC Style | $ | | |
| Polished/Brand | $ | | |

#### B. Hook Type Performance (First 3 Seconds / Headlines)

Categorize hooks and track performance:

| Hook Type | Example | Avg CPA | Win Rate |
|-----------|---------|---------|----------|
| **Problem-Agitate** | "Tired of [pain point]?" | $ | |
| **Bold Claim** | "The only [product] that..." | $ | |
| **Social Proof** | "10,000+ customers..." | $ | |
| **Curiosity Gap** | "The secret [experts] won't tell you" | $ | |
| **Direct Benefit** | "Get [result] in [timeframe]" | $ | |
| **Question** | "What if you could [desire]?" | $ | |
| **Demonstration** | Shows product in action immediately | $ | |
| **Transformation** | Before/after or A/B comparison | $ | |

#### C. CTA Performance

| CTA Type | Examples | Avg CPA | Notes |
|----------|----------|---------|-------|
| **Urgency** | "Shop Now", "Get It Today" | $ | |
| **Value** | "Start Free Trial", "Get 20% Off" | $ | |
| **Curiosity** | "Learn More", "See How" | $ | |
| **Social** | "Join 10K+ Members" | $ | |

---

### Step 6: Waste Identification

Calculate total waste from underperforming creatives:

```
Total Creative Spend: $________
Spend on Tiers 5-6 (Underperformers + Bleeders): $________
Waste Percentage: ________%
Conversions Lost (if reallocated to Tier 1-2): ________
```

**Waste Impact Scoring:**

| Waste % | Severity | Priority |
|---------|----------|----------|
| < 10% | Healthy | Maintain vigilance |
| 10-20% | Moderate | Weekly optimization needed |
| 20-35% | Significant | Immediate reallocation required |
| > 35% | Critical | Creative strategy overhaul needed |

---

## Output Deliverables

### 1. Creative Performance Summary

```
CREATIVE PERFORMANCE SUMMARY
Period: [Date Range]
Total Creatives Analyzed: [X]
Total Spend: $[X]

TIER BREAKDOWN:
├── Stars (Tier 1): [X] creatives, $[X] spend, [X] conversions
├── Solid (Tier 2): [X] creatives, $[X] spend, [X] conversions
├── Promising (Tier 3): [X] creatives, $[X] spend, [X] conversions
├── Average (Tier 4): [X] creatives, $[X] spend, [X] conversions
├── Underperformers (Tier 5): [X] creatives, $[X] spend, [X] conversions
└── Bleeders (Tier 6): [X] creatives, $[X] spend, [X] conversions

WASTE ANALYSIS:
└── Wasted Spend: $[X] ([X]% of total)
└── Potential Conversions Lost: [X]
```

### 2. Top Performers List

| Rank | Creative Name/ID | Format | CPA | ROAS | Spend | Conv | Why It Works |
|------|------------------|--------|-----|------|-------|------|--------------|
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |

### 3. Kill List (Immediate Pause)

| Creative Name/ID | Spend | Conv | CPA | Reason |
|------------------|-------|------|-----|--------|
| | | | | |

### 4. Winning Patterns Summary

```
FORMAT WINNERS:
#1: [Format] - [X]% better than average
#2: [Format] - [X]% better than average

HOOK WINNERS:
#1: [Hook Type] - [X]% better than average
#2: [Hook Type] - [X]% better than average

CTA WINNERS:
#1: [CTA Type] - [X]% better than average
```

### 5. Creative Testing Recommendations

Based on winning patterns, test:

| Priority | Test Concept | Based On | Expected Impact |
|----------|--------------|----------|-----------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |

---

## Red Flags to Call Out

- **High-spend creative with 0 conversions:** Immediate pause, investigate targeting
- **Declining Star:** Previously top performer losing efficiency - creative fatigue likely
- **Engagement Trap pattern:** High CTR/engagement, low conversion - misleading metrics
- **Format imbalance:** All winners same format = opportunity to diversify
- **Hook homogeneity:** All hooks same type = testing gap

---

## Integration with Other Skills

| After This Skill | Use | Purpose |
|------------------|-----|---------|
| → creative-fatigue-detector | Pass Star/Solid creatives | Monitor for fatigue signals |
| → ugc-brief-generator | Pass winning patterns | Brief new content based on what works |
| → social-ads-budget-allocator | Pass efficiency data | Inform budget decisions |
| → audience-overlap-mapper | Cross-reference by audience | See if creative wins are audience-dependent |

---

## Limitations

- Cannot analyze creative visual quality (only performance data)
- Pattern analysis requires 5+ creatives per category for validity
- Short time windows may not show true performance
- Cannot account for external factors (seasonality, competition, market events)
- Attribution model affects all conversion data

---

## Quality Checklist Before Delivery

- [ ] Data sufficiency verified for all analyzed creatives
- [ ] All 6 tiers populated (or noted as empty with explanation)
- [ ] Engagement vs. Efficiency matrix completed
- [ ] Video metrics analyzed (if applicable)
- [ ] Pattern analysis covers format, hook, and CTA
- [ ] Waste calculation completed
- [ ] Kill list is actionable (not just flagged, but recommended pause)
- [ ] Testing recommendations tied to winning patterns
- [ ] Red flags explicitly called out
