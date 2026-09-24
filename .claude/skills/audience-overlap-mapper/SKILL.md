---
name: audience-overlap-mapper
description: Identifies audience cannibalization across campaigns and platforms, recommending exclusions to eliminate wasted spend on redundant reach.
---

# Audience Overlap Mapper

## Purpose

Identify where your ad dollars are competing against themselves by:
- Mapping overlap between campaign audiences
- Detecting cross-platform redundancy
- Quantifying the cost of audience cannibalization
- Recommending exclusions to eliminate waste

**Core Philosophy:** If you're paying twice to reach the same person with the same message, you're paying once too many. Overlap isn't always bad—but unintentional overlap is always waste.

---

## When to Use This Skill

- Monthly audience health check
- Before scaling campaigns (prevent scaling into overlap)
- When frequency spikes across campaigns
- When adding new audiences to account
- When CPMs rise without clear cause
- After noticing "auction overlap" warnings

---

## Required Context

| Data Point | Required | Notes |
|------------|----------|-------|
| Campaign/ad set audience definitions | Yes | Targeting criteria for each |
| Audience sizes (estimated reach) | Yes | For overlap calculation |
| Frequency data by campaign | Yes | Symptom of overlap |
| Platform overlap tools (if available) | Helpful | Meta has built-in overlap tool |
| Cross-platform audience composition | Helpful | For multi-platform analysis |
| Performance by audience segment | Helpful | To prioritize exclusions |

---

## Overlap Types

### Type 1: Within-Platform Campaign Overlap
Same person sees ads from multiple campaigns

```
Campaign A: Interest in Fitness + Ages 25-45
Campaign B: Interest in Running + Ages 25-45
                    ↓
     Overlap: Fitness-interested runners aged 25-45
     Problem: Bidding against yourself, inflating CPM
```

### Type 2: Ad Set Level Overlap
Within same campaign, ad sets compete

```
Ad Set 1: Lookalike 1% from Purchasers
Ad Set 2: Lookalike 1% from Email List
                    ↓
     Overlap: Best customers appear in both lookalikes
     Problem: Same people, fragmented data, inefficient learning
```

### Type 3: Cross-Platform Overlap
Same person targeted on Meta AND TikTok AND LinkedIn

```
Meta: Fitness Interest targeting
TikTok: Fitness Interest targeting
                    ↓
     Overlap: Same person sees similar ad on both platforms
     Problem: May be fine (reinforcement) or waste (redundancy)
```

### Type 4: Retargeting/Prospecting Overlap
Warm audiences bleeding into cold campaigns

```
Prospecting Campaign: Broad targeting
Retargeting Campaign: Website visitors
                    ↓
     Overlap: Retargeting audience appears in prospecting
     Problem: Paying prospecting rates for warm leads
```

---

## Overlap Detection Framework

### Step 1: Audience Inventory

Map all active audiences:

| Campaign | Ad Set | Targeting Description | Est. Size | Objective |
|----------|--------|----------------------|-----------|-----------|
| | | | | |

### Step 2: Overlap Matrix

Create a matrix showing estimated overlap between each audience pair:

```
              Audience A    Audience B    Audience C
Audience A       -            35%           15%
Audience B      35%            -            50%
Audience C      15%           50%            -
```

### Overlap Estimation Methods

**Method 1: Platform Tools (Most Accurate)**
- Meta: Audience Overlap Tool in Ads Manager
- Shows exact overlap percentage

**Method 2: Manual Estimation**
For audiences without tool access:

```
Overlap % ≈ (Shared Targeting Criteria / Total Criteria) × Audience Similarity Factor

Where Similarity Factor:
- Same platform, same objective: 0.8-1.0
- Same platform, different objective: 0.5-0.7
- Different platform: 0.3-0.5
```

**Method 3: Frequency Analysis**
If combined frequency >> individual frequencies, overlap exists:

```
If Campaign A frequency = 2.0
And Campaign B frequency = 2.0
But combined account frequency = 5.0
Then significant overlap exists
```

---

## Overlap Severity Assessment

### Severity Levels

| Overlap % | Severity | Impact | Priority |
|-----------|----------|--------|----------|
| < 10% | Minimal | Negligible waste | Monitor |
| 10-25% | Low | Minor inefficiency | Address when optimizing |
| 25-40% | Moderate | Meaningful waste | Fix within 2 weeks |
| 40-60% | High | Significant waste | Fix within 1 week |
| > 60% | Critical | Major waste | Fix immediately |

### Impact Calculation

```
Estimated Waste = Overlap % × Lower-Performing Audience Spend × Efficiency Loss Factor

Where Efficiency Loss Factor:
- Similar performance: 0.3-0.5 (bidding against yourself)
- One outperforms: 0.5-0.7 (wrong audience getting spend)
- Both underperforming: 0.7-0.9 (compounding inefficiency)
```

---

## Overlap Scenarios & Solutions

### Scenario A: Interest Overlap

**Symptom:** Multiple interest-based ad sets with shared interests

```
Ad Set 1: Interest = Yoga, Pilates, Meditation
Ad Set 2: Interest = Fitness, Gym, Workout
Overlap: People interested in both yoga AND gym
```

**Solution Options:**
1. **Consolidate:** Merge into single ad set with broader targeting
2. **Exclude:** Add exclusions (Ad Set 1 excludes Gym interest)
3. **Separate:** Use different campaign objectives to justify overlap

**Recommendation Matrix:**
| If... | Then... |
|-------|---------|
| Similar performance | Consolidate |
| One significantly better | Keep winner, pause loser |
| Different objectives | Exclude or accept |

---

### Scenario B: Lookalike Overlap

**Symptom:** Multiple lookalikes from related seed audiences

```
LAL 1: 1% from Purchasers
LAL 2: 1% from High-Value Purchasers
LAL 3: 1% from Email Subscribers
Overlap: Best customers appear in all three
```

**Solution Options:**
1. **Tiered approach:** 1% best, 1-2% next, 2-3% broadest
2. **Exclusion cascade:** LAL 2 excludes LAL 1, LAL 3 excludes both
3. **Consolidate seeds:** Combine into single "Best Customers" LAL

**Recommendation:**
```
Best Practice:
├── Tier 1: 0-1% LAL from best seed (highest value)
├── Tier 2: 1-2% LAL (excludes Tier 1)
└── Tier 3: 2-3% LAL (excludes Tiers 1 & 2)
```

---

### Scenario C: Retargeting Bleed

**Symptom:** Retargeting audiences showing up in prospecting campaigns

```
Prospecting: Broad targeting, all ages 25-45
Retargeting: Website visitors last 30 days
Problem: Website visitors get served prospecting ads at higher CPA
```

**Solution:**
**Always exclude retargeting pools from prospecting:**

```
Prospecting Campaign Exclusions:
├── Website visitors (all time or 180 days)
├── Purchasers (all time)
├── Email list
├── Engaged users (video viewers, page engagers)
└── App users (if applicable)
```

---

### Scenario D: Cross-Campaign Cannibalization

**Symptom:** Multiple campaigns targeting same audience with same objective

```
Campaign 1: Conversions - Interest targeting
Campaign 2: Conversions - LAL targeting
Campaign 3: Conversions - Broad targeting
Overlap: Same best prospects appear in all three
```

**Solution Options:**
1. **Consolidate campaigns:** Single campaign, multiple ad sets
2. **Exclusion cascade:** Each campaign excludes others' best performers
3. **Objective separation:** Different objectives justify same audience

**Consolidation Benefits:**
- Unified learning (faster optimization)
- Single auction entry (no self-competition)
- Clearer performance picture

---

### Scenario E: Geographic Overlap

**Symptom:** National + regional campaigns compete

```
Campaign 1: USA - National
Campaign 2: California only
Campaign 3: Los Angeles only
Overlap: Californians (especially LA) appear in all three
```

**Solution:**
**Geographic exclusion waterfall:**

```
Campaign 1 (National): Exclude California
Campaign 2 (California): Exclude Los Angeles
Campaign 3 (Los Angeles): No exclusions needed
```

---

## Cross-Platform Overlap Analysis

### When Cross-Platform Overlap Is OK

| Scenario | Verdict | Reasoning |
|----------|---------|-----------|
| Different funnel stages | ✓ Acceptable | Awareness on TikTok, Retargeting on Meta |
| Different creatives/messages | ✓ Acceptable | Testing resonance across platforms |
| Intentional frequency boost | ✓ Acceptable | Strategic multi-touch |

### When Cross-Platform Overlap Is Waste

| Scenario | Verdict | Reasoning |
|----------|---------|-----------|
| Same creative, same message | ✗ Waste | No incremental value |
| Same offer, same audience | ✗ Waste | Pay twice for same conversion |
| No attribution clarity | ✗ Risk | Don't know which platform drove it |

### Cross-Platform Exclusion Strategy

```
If same audience on Meta + TikTok:

Option 1: Platform Specialization
├── Meta: Retargeting + Lookalikes (better at it)
└── TikTok: Broad/Interest (cheaper reach)

Option 2: Funnel Separation
├── TikTok: Top of funnel (awareness)
└── Meta: Bottom of funnel (conversion)

Option 3: Audience Separation
├── Meta: Ages 35+ (higher concentration)
└── TikTok: Ages 18-34 (higher concentration)
```

---

## Output Deliverables

### 1. Overlap Inventory

```
AUDIENCE OVERLAP ANALYSIS
Account: [Name]
Date: [Date]
Campaigns Analyzed: [X]
Ad Sets Analyzed: [X]

OVERLAP SUMMARY:
├── Critical Overlaps (>60%): [X] pairs
├── High Overlaps (40-60%): [X] pairs
├── Moderate Overlaps (25-40%): [X] pairs
├── Low Overlaps (10-25%): [X] pairs
└── Minimal Overlaps (<10%): [X] pairs

ESTIMATED WASTE: $[X]/month ([X]% of spend)
```

### 2. Overlap Matrix

Visual matrix showing all audience pair overlaps with severity coding:

```
              Prosp-Interest  Prosp-LAL  Retarget  Brand
Prosp-Interest      -           42%🔴      8%🟢     15%🟡
Prosp-LAL          42%🔴         -        12%🟡     22%🟡
Retarget           8%🟢        12%🟡        -       35%🟠
Brand              15%🟡       22%🟡      35%🟠       -

🔴 Critical  🟠 High  🟡 Moderate  🟢 Low/Minimal
```

### 3. Priority Fix List

| Priority | Overlap Pair | Overlap % | Est. Waste | Recommended Fix |
|----------|--------------|-----------|------------|-----------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

### 4. Exclusion Implementation Plan

```
EXCLUSION RECOMMENDATIONS

CAMPAIGN: [Campaign Name]
├── Ad Set 1: Add exclusions for [audiences]
├── Ad Set 2: Add exclusions for [audiences]
└── Ad Set 3: Pause (consolidate into Ad Set 1)

CAMPAIGN: [Campaign Name]
└── Add exclusions for [retargeting pools]
```

### 5. Consolidation Recommendations

| Current Structure | Recommended Structure | Reasoning |
|-------------------|----------------------|-----------|
| | | |

---

## Exclusion Best Practices

### Universal Exclusions (Always Apply to Prospecting)

```
Standard Prospecting Exclusions:
├── All purchasers (lifetime or 180 days)
├── All website visitors (30-180 days based on cycle)
├── Email/CRM lists
├── High-intent engagers (add to cart, initiate checkout)
└── Existing app users
```

### Exclusion Hierarchy

When multiple audiences need exclusions, follow this order:

```
Priority (exclude higher from lower):
1. Purchasers (most valuable, protect first)
2. High-intent (add to cart, checkout started)
3. Website visitors
4. Engagers (video, page, post)
5. Lookalike audiences
6. Interest audiences
7. Broad targeting
```

### Exclusion Pitfalls to Avoid

| Mistake | Problem | Solution |
|---------|---------|----------|
| Over-excluding | Audience too small to deliver | Test reach before applying |
| Stale exclusions | Excluding people who should be re-targeted | Refresh exclusion windows |
| Inconsistent application | Some campaigns excluded, others not | Standardize across account |
| Forgetting cross-campaign | Excluding within but not across campaigns | Use shared audiences |

---

## Frequency as Overlap Indicator

Use frequency patterns to detect hidden overlap:

### Frequency Diagnostic

| Frequency Pattern | Likely Cause | Investigation |
|-------------------|--------------|---------------|
| Single campaign high frequency (>3) | Audience too small or saturated | Check audience size |
| Multiple campaigns moderate frequency but account high | Cross-campaign overlap | Run overlap analysis |
| Steady frequency increase week-over-week | Audience exhaustion | Check reach vs. impressions |
| Sudden frequency spike | Budget increase without audience expansion | Reduce budget or expand |

### Frequency Caps as Overlap Mitigation

If exclusions aren't possible, frequency caps can help:

```
Recommended Caps by Objective:
├── Awareness: 3-4 per week
├── Consideration: 2-3 per week
├── Conversion (prospecting): 2-3 per week
└── Conversion (retargeting): 4-6 per week
```

---

## Integration with Other Skills

| Connected Skill | Integration Point |
|-----------------|-------------------|
| social-ads-budget-allocator | Overlap data informs cross-platform allocation |
| creative-fatigue-detector | High overlap can accelerate fatigue |
| meta-ads-creative-ranker | Performance by audience helps prioritize exclusions |

---

## Limitations

- Exact overlap can only be measured with platform tools (not all available)
- Cross-platform overlap must be estimated (no unified view)
- Exclusion impact takes 1-2 weeks to fully measure
- Over-excluding can harm reach and learning
- Dynamic audiences change over time (overlap shifts)

---

## Quality Checklist Before Delivery

- [ ] All active campaigns/ad sets inventoried
- [ ] Overlap matrix completed for all audience pairs
- [ ] Severity levels assigned correctly
- [ ] Waste calculation methodology documented
- [ ] Priority fixes ranked by impact
- [ ] Exclusion recommendations are specific and actionable
- [ ] Consolidation opportunities identified
- [ ] Cross-platform overlap assessed
- [ ] Retargeting bleed checked
- [ ] Frequency analysis included
- [ ] Implementation plan provided with sequence
