---
name: audience-overlap-analyzer
description: Identifies audience overlap and cannibalization across campaigns and platforms. Triggers when user asks "are my audiences competing?", "why are my CPMs rising?", or wants to understand audience efficiency. Analyzes overlap percentages, auction competition, and provides consolidation recommendations.
---

# Audience Overlap Analyzer

Stop bidding against yourself. Find the hidden overlap killing your efficiency.

## Core Philosophy

**Overlap is the silent budget killer.** You could be paying twice to reach the same person—once in Campaign A, again in Campaign B.

**The Overlap Paradox:** More audiences feels like more coverage. But overlapping audiences mean you're competing against yourself in the auction.

**The Three Laws of Audience Efficiency:**
1. **Overlap raises CPMs:** When you bid against yourself, everyone loses (except Google/Meta)
2. **Frequency compounds:** Overlap + retargeting = ad fatigue at warp speed
3. **Attribution gets messy:** Who gets credit when the same user sees 3 campaigns?

---

## Required Context

### Must Have

**1. Audience Definitions**
For each audience/ad set:
- Name
- Targeting criteria (interests, behaviors, lookalikes, custom, etc.)
- Estimated size
- Platform

**2. Performance Data**
- Spend per audience
- Conversions per audience
- CPM per audience
- Frequency per audience

### Strongly Recommended

**3. Overlap Data (if available)**
- Meta: Audience Overlap tool results
- Google: Audience insights overlap %
- Manual analysis of targeting criteria

**4. Campaign Structure**
- Which campaigns use which audiences
- Budget allocation across campaigns
- Audience exclusions currently in place

### Nice to Have

- Historical CPM trends
- Conversion path data (multi-touch)
- Audience refresh dates
- Cross-platform audience usage

---

## Overlap Detection Framework

### Type 1: Direct Overlap

**Definition:** Same users appear in multiple audiences

**Common Causes:**
| Overlap Pattern | Example | Detection |
|-----------------|---------|-----------|
| Lookalike overlap | 1% LAL and 2% LAL | First 1% is contained in 2% |
| Interest overlap | "Marketing" and "Digital Marketing" | Nested interests |
| Behavior overlap | "Engaged Shoppers" + "Purchase Intent" | Similar signals |
| Retargeting overlap | "Cart Abandoners" + "All Visitors" | Subset relationship |

**Severity Calculation:**
```
Overlap Impact = (Overlap %) × (Higher CPM - Lower CPM) × Impressions
```

---

### Type 2: Auction Collision

**Definition:** Audiences competing in same auctions even if not identical

**Signs of Auction Collision:**
- Rising CPMs across multiple campaigns simultaneously
- Similar delivery times across audiences
- Auction insights showing self-competition

**Detection Method:**
1. Check if audiences target same demographics
2. Check if audiences target same placements
3. Check if campaigns run same schedules
4. Review auction insights for same-advertiser competition

---

### Type 3: Cross-Campaign Cannibalization

**Definition:** Multiple campaigns reaching same users with different messages

**Impact Assessment:**
| Scenario | Impact | Priority |
|----------|--------|----------|
| Brand + Non-brand overlap | Low (intentional funnel) | Monitor |
| Prospecting + Prospecting overlap | High (wasted spend) | Fix |
| Prospecting + Retargeting overlap | Medium (frequency issue) | Exclude |
| Retargeting + Retargeting overlap | High (fatigue + waste) | Consolidate |

---

## Overlap Severity Scoring

### Calculate Overlap Score (0-100)

```
Overlap Score = (Size Factor × 0.3) +
                (CPM Impact × 0.3) +
                (Frequency Factor × 0.2) +
                (Budget Factor × 0.2)
```

**Size Factor (0-100):**
- <10% overlap: 10
- 10-25% overlap: 30
- 25-50% overlap: 60
- 50-75% overlap: 80
- >75% overlap: 100

**CPM Impact (0-100):**
- CPMs normal: 0
- CPMs 10-20% elevated: 30
- CPMs 20-40% elevated: 60
- CPMs >40% elevated: 100

**Frequency Factor (0-100):**
- Combined frequency <3: 0
- Combined frequency 3-5: 30
- Combined frequency 5-8: 60
- Combined frequency >8: 100

**Budget Factor (0-100):**
Based on combined budget of overlapping audiences as % of total

**Severity Interpretation:**

| Score | Severity | Action |
|-------|----------|--------|
| 0-25 | Low | Monitor quarterly |
| 26-50 | Moderate | Implement exclusions |
| 51-75 | High | Restructure audiences |
| 76-100 | Critical | Immediate consolidation |

---

## Platform-Specific Analysis

### Meta Ads Overlap

**Using Audience Overlap Tool:**
1. Go to Audiences → Select multiple audiences → Compare
2. Tool shows % overlap between any two audiences

**Common Meta Overlap Issues:**
| Pattern | Overlap Risk | Solution |
|---------|--------------|----------|
| 1% LAL + 2% LAL | 100% (1% inside 2%) | Use only 1%, or exclude 1% from 2% |
| Interest + Broad | High | Broad absorbs interest, run separately |
| Multiple interests | Medium-High | Consolidate or use Advantage+ |
| Custom audiences + LAL | Varies | Check actual overlap % |

**Meta-Specific Recommendations:**
- Use Advantage+ Audience to let algorithm manage overlap
- Consolidate ad sets to reduce internal competition
- Set up exclusion lists systematically

---

### Google Ads Overlap

**Audience Insights Tool:**
1. Go to Tools → Audience Manager → Insights
2. Compare audience compositions

**Common Google Overlap Issues:**
| Pattern | Overlap Risk | Solution |
|---------|--------------|----------|
| Affinity + In-Market | High | Similar users, different intent labels |
| Custom Intent audiences | Medium | Keyword overlap common |
| Remarketing lists | Variable | Check date ranges for overlap |
| Similar audiences | High with source list | Exclude source list |

**Google-Specific Recommendations:**
- Use audience exclusions at campaign level
- Review Observation vs. Targeting mode
- Consolidate custom intent audiences with similar keywords

---

### Cross-Platform Overlap

**Same Users, Different Platforms:**
- Customer email lists uploaded to multiple platforms
- Website visitors pixeled everywhere
- Same demographics targeted across platforms

**Cross-Platform Considerations:**
| Situation | Impact | Action |
|-----------|--------|--------|
| Same CRM list everywhere | High frequency | Coordinate messaging |
| Retargeting on all platforms | Fatigue | Choose primary retargeting platform |
| Same demos everywhere | Auction neutral | Focus on platform strengths |

---

## Output Format

### Audience Overlap Analysis

```
═══════════════════════════════════════════════════════════════
AUDIENCE OVERLAP ANALYSIS
Platform(s): [Platform(s)]
Audiences Analyzed: [X]
Critical Overlaps Found: [X]
Estimated Wasted Spend: $[X]/month
═══════════════════════════════════════════════════════════════
```

---

### Overlap Summary Dashboard

**Overall Overlap Health: [HEALTHY/MODERATE/CRITICAL]**

**Overlap Distribution:**
```
No Overlap (0-10%):      ████████████████ [X] pairs
Low Overlap (10-25%):    ████████ [X] pairs
Moderate (25-50%):       ████ [X] pairs
High (50-75%):           ██ [X] pairs
Critical (75%+):         █ [X] pairs
```

**Estimated Monthly Impact:**
- Wasted Spend: $[X]
- CPM Inflation: +[X]%
- Excess Frequency: [X] extra impressions/user

---

### Overlap Matrix

| Audience | Aud 1 | Aud 2 | Aud 3 | Aud 4 | Aud 5 |
|----------|-------|-------|-------|-------|-------|
| Aud 1 | - | [X]% | [X]% | [X]% | [X]% |
| Aud 2 | [X]% | - | [X]% | [X]% | [X]% |
| Aud 3 | [X]% | [X]% | - | [X]% | [X]% |
| Aud 4 | [X]% | [X]% | [X]% | - | [X]% |
| Aud 5 | [X]% | [X]% | [X]% | [X]% | - |

**Legend:** 🟢 <25% | 🟡 25-50% | 🔴 >50%

---

### Critical Overlap Pairs

**Pair 1: [Audience A] × [Audience B]**
```
Overlap: [X]%
Combined Spend: $[X]/month
Combined Frequency: [X]
CPM Comparison: $[X] vs $[X]
Overlap Score: [X]/100 (CRITICAL)
```

**Diagnosis:** [Why this overlap exists]

**Impact:**
- Estimated waste: $[X]/month
- Users seeing ads from both: ~[X]
- Attribution confusion: [Assessment]

**Recommendation:** [Specific action]

---

### Audience-Level Analysis

**[Audience Name]**
```
Size: [X]
Spend: $[X]
CPM: $[X]
Frequency: [X]
Overlaps with: [X] other audiences

Overlap Breakdown:
- [Audience B]: [X]% overlap (HIGH)
- [Audience C]: [X]% overlap (LOW)
- [Audience D]: [X]% overlap (MODERATE)

Primary Concern: [Main issue]
Recommendation: [Action]
```

---

### Consolidation Recommendations

**Audiences to Merge:**

| Current Audiences | Combined Into | Rationale | Projected Savings |
|-------------------|---------------|-----------|-------------------|
| [A], [B] | [New name] | [X]% overlap | $[X]/month |
| [C], [D], [E] | [New name] | Similar targeting | $[X]/month |

**Exclusions to Implement:**

| Audience | Exclude From | Reason |
|----------|--------------|--------|
| [Smaller audience] | [Larger audience] | Subset relationship |
| [Retargeting] | [Prospecting] | Funnel separation |

**Structure Recommendation:**
```
CURRENT STRUCTURE          RECOMMENDED STRUCTURE
├─ Campaign 1              ├─ Campaign 1 (Prospecting)
│  ├─ Audience A           │  ├─ Broad/Advantage+
│  ├─ Audience B           │  └─ (exclude retargeting)
│  └─ Audience C           │
├─ Campaign 2              ├─ Campaign 2 (Retargeting)
│  ├─ Audience D           │  ├─ Consolidated Retargeting
│  └─ Audience E           │  └─ (frequency capped)
```

---

### CPM Impact Analysis

**Before vs. After Projection:**

| Metric | Current | Projected | Change |
|--------|---------|-----------|--------|
| Avg CPM | $[X] | $[X] | -[X]% |
| Total Reach | [X] | [X] | +[X]% |
| Effective Frequency | [X] | [X] | -[X] |
| Wasted Spend | $[X] | $[X] | -[X]% |

---

### Action Plan

**Immediate (This Week):**
1. [ ] Implement exclusion: [Specific exclusion]
2. [ ] Pause duplicate audience: [Audience name]
3. [ ] Set frequency cap on: [Audience name]

**Short-Term (Next 2 Weeks):**
1. [ ] Consolidate: [Audiences] into [New audience]
2. [ ] Restructure: [Campaign] to separate funnel stages
3. [ ] Test: Advantage+ audience vs. manual targeting

**Monitoring:**
- [ ] Weekly CPM tracking by audience
- [ ] Frequency monitoring
- [ ] Overlap tool check monthly

---

## Common Overlap Scenarios

### Scenario 1: Lookalike Ladder
**Structure:** 1% LAL, 2% LAL, 3% LAL running simultaneously
**Problem:** Each larger LAL contains the smaller ones
**Solution:** Run only 1%, or exclude 1% from 2%, exclude 2% from 3%

### Scenario 2: Interest Stacking
**Structure:** Multiple interest audiences with similar themes
**Problem:** Heavy overlap between related interests
**Solution:** Use one broad interest or Advantage+ targeting

### Scenario 3: Retargeting Fragmentation
**Structure:** Separate retargeting for visitors, cart, past purchasers
**Problem:** Same user in multiple lists
**Solution:** Prioritize with exclusions (purchasers excluded from cart, cart from visitors)

### Scenario 4: Prospecting + Retargeting Collision
**Structure:** No exclusions between prospecting and retargeting
**Problem:** Retargeting users getting prospecting ads
**Solution:** Exclude all retargeting audiences from prospecting campaigns

---

## Limitations

**I can provide:**
- Overlap identification and scoring
- Consolidation recommendations
- Exclusion strategies
- CPM impact estimates

**I cannot provide:**
- Exact overlap percentages without tool data
- Cross-platform overlap (requires unified identity)
- Conversion path deduplication
- Real-time auction dynamics

**For better analysis, provide:**
- Meta Audience Overlap tool screenshots
- Google Audience Insights data
- Actual audience sizes and definitions
- CPM history over time

---

## Quality Checklist

Before delivering analysis:
- [ ] All audiences mapped with sizes and spend
- [ ] Overlap pairs identified and scored
- [ ] Consolidation recommendations are practical
- [ ] Exclusion hierarchy is logical (no circular exclusions)
- [ ] CPM impact estimated where possible
- [ ] Action plan is prioritized
- [ ] Platform-specific nuances addressed
