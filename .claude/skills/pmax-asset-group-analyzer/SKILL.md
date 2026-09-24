---
name: pmax-asset-group-analyzer
description: Deep-dives into Google Performance Max asset group performance, analyzing asset effectiveness, audience signals, search themes, and channel distribution. Triggers when user asks "why isn't my PMax working?", "how do I improve my asset groups?", or wants to understand PMax campaign performance. Provides actionable asset recommendations and structure optimization.
---

# Performance Max Asset Group Analyzer

Crack open the black box. Understand what's actually happening in your PMax campaigns.

## Core Philosophy

**PMax is not magic.** It's machine learning that needs good inputs. Garbage in, garbage out—even with Google's algorithm.

**The PMax Paradox:** Less control doesn't mean less work. It means different work—feeding the machine the right assets and signals.

**The Three Truths of Performance Max:**
1. **Asset quality is everything:** The algorithm can only optimize what you give it
2. **Signals > Targeting:** Your audience signals guide the machine, not restrict it
3. **Structure matters:** One bloated campaign ≠ multiple focused asset groups

---

## Required Context

### Must Have

**1. Campaign Overview**
- Campaign name and objective
- Monthly spend
- Conversions and CPA (or revenue and ROAS)
- Days running

**2. Asset Group Performance**
For each asset group:
- Name
- Spend allocation
- Conversions
- CPA or ROAS

**3. Asset Performance Ratings**
From the Assets tab:
- Text assets (headlines, descriptions) with ratings
- Image assets with ratings
- Video assets with ratings (if applicable)

### Strongly Recommended

**4. Insights Data**
- Search themes report (what queries are triggering)
- Audience insights (which signals are working)
- Placement report (where ads are showing)

**5. Asset Details**
- Specific headlines and descriptions (not just counts)
- Image dimensions and types
- Video presence and performance

**6. Conversion Data**
- Conversion by asset group
- Conversion type breakdown (if multiple)
- Conversion lag/path data

### Nice to Have

- Comparison to non-PMax campaigns
- Historical performance trends
- Competitor context
- Product feed health (for shopping-eligible)
- Brand vs. non-brand search term breakdown

---

## Performance Max Analysis Framework

### Level 1: Campaign Health Check

**Overall Campaign Status:**

| Metric | Green | Yellow | Red |
|--------|-------|--------|-----|
| CPA vs Target | <100% | 100-130% | >130% |
| ROAS vs Target | >100% | 70-100% | <70% |
| Learning Status | Optimized | Learning | Limited |
| Conversions/Week | 30+ | 15-30 | <15 |
| Asset Coverage | Full | Partial | Poor |

**Minimum Viability Check:**
- [ ] 30+ conversions/month (for CPA campaigns)
- [ ] All asset types provided (text, image, video)
- [ ] Audience signals added
- [ ] Final URL expansion ON (unless specific reason)
- [ ] At least 2 weeks of data

---

### Level 2: Asset Group Analysis

**Asset Group Performance Tiers:**

| Tier | Criteria | Action |
|------|----------|--------|
| Star | CPA <80% target, high volume | Scale, replicate structure |
| Performer | CPA 80-100% target | Optimize assets |
| Underperformer | CPA 100-130% target | Test new assets, review signals |
| Problem | CPA >130% target | Restructure or pause |
| Starved | <5% of budget, few conversions | Evaluate necessity |

**Budget Distribution Analysis:**
Is budget flowing to the right asset groups?
- Even distribution isn't always good
- Check if best performers are budget-capped
- Identify if poor performers are draining budget

---

### Level 3: Asset Performance Deep Dive

**Asset Rating Interpretation:**

| Rating | Meaning | Action |
|--------|---------|--------|
| Best | Top performer, high impressions | Keep, create variations |
| Good | Performing well | Maintain |
| Low | Underperforming vs. other assets | Test replacements |
| -- (Pending) | Not enough data | Wait or increase variety |

**Asset Coverage Requirements:**

| Asset Type | Minimum | Recommended | Maximum |
|------------|---------|-------------|---------|
| Headlines (30 char) | 3 | 5-10 | 15 |
| Long Headlines (90 char) | 1 | 2-5 | 5 |
| Descriptions (90 char) | 2 | 3-5 | 5 |
| Images (1200x628) | 1 | 3-5 | 15 |
| Square Images (1200x1200) | 1 | 3-5 | 15 |
| Portrait Images (960x1200) | 0 | 2-3 | 15 |
| Logo (1200x1200) | 1 | 1-2 | 5 |
| Videos (YouTube) | 0 | 1-3 | 5 |

**Common Asset Issues:**

| Issue | Impact | Solution |
|-------|--------|----------|
| Too few assets | Limited combinations, less testing | Add to minimums |
| All assets same rating | Can't identify winners | Increase variety |
| No video | Missing YouTube/Display placements | Add videos |
| Generic headlines | Low relevance, poor CTR | Write specific, benefit-focused |
| Stock images only | Low engagement | Add product/branded images |

---

### Level 4: Search Themes Analysis

**What to Look For:**

1. **Relevance Check:** Are search themes relevant to your business?
2. **Brand vs. Non-Brand:** How much is brand cannibalization?
3. **Negative Needed:** Any completely irrelevant themes?
4. **Opportunity Themes:** High-potential themes not being captured?

**Search Theme Health:**

| Pattern | Diagnosis | Action |
|---------|-----------|--------|
| 80%+ brand terms | PMax cannibalizing brand | Add brand exclusions or separate brand campaign |
| Irrelevant terms | Poor signals or final URL expansion issues | Add campaign-level negatives |
| Very broad terms | Signals too weak | Strengthen audience signals |
| Competitor terms | Might be intentional or not | Decide strategy, add negatives if unintentional |
| High-intent terms | Good signal quality | Ensure sufficient budget |

---

### Level 5: Audience Signal Analysis

**Signal Strength Indicators:**

| Signal Type | Strength | Notes |
|-------------|----------|-------|
| Customer Match list | High | Best signal if list is quality |
| Website visitors (GA4) | High | Shows actual interest |
| Custom segments (search) | Medium | Keyword-based, good intent |
| Custom segments (URL) | Medium | Interest-based |
| In-market audiences | Medium-Low | Broad Google audiences |
| Demographics only | Low | Not enough signal |
| No signals | Very Low | Algorithm flying blind |

**Audience Insights Review:**
- Which signals are indexing high vs. audience?
- Are unexpected audiences converting?
- Any signals to add based on insights?

---

### Level 6: Placement Analysis

**Channel Distribution Assessment:**

| Channel | Typical % | Concern If... |
|---------|-----------|---------------|
| Search | 40-60% | <20% (shopping eating search) |
| Shopping | 20-40% | N/A for non-ecommerce |
| Display | 10-25% | >40% (usually lower quality) |
| YouTube | 5-15% | 0% (missing video assets) |
| Gmail | 1-5% | >10% (usually low quality) |
| Discover | 5-15% | N/A |

**Placement Quality Check:**
- Is Search converting efficiently?
- Is Display dragging down performance?
- Are YouTube placements relevant?

---

## Output Format

### PMax Asset Group Analysis

```
═══════════════════════════════════════════════════════════════
PERFORMANCE MAX ASSET GROUP ANALYSIS
Campaign: [Name]
Analysis Period: [Date Range]
Total Spend: $[X] | Conversions: [X] | CPA: $[X]
Health Status: [HEALTHY/NEEDS WORK/CRITICAL]
═══════════════════════════════════════════════════════════════
```

---

### Campaign Health Dashboard

**Overall Status: [GREEN/YELLOW/RED]**

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| CPA | $[X] | $[X] | [Status] |
| ROAS | [X] | [X] | [Status] |
| Conversions | [X] | [X]/week | [Status] |
| Learning Status | [Status] | Optimized | [Status] |

**Campaign Viability Check:**
- [x] Sufficient conversion volume (30+/month)
- [ ] All asset types provided
- [x] Audience signals configured
- [ ] Final URL expansion enabled
- [x] 2+ weeks of data

---

### Asset Group Performance Breakdown

**Star Performers (Scale These):**
| Asset Group | Spend | Conv | CPA | vs Target | Action |
|-------------|-------|------|-----|-----------|--------|
| [Name] | $[X] | [X] | $[X] | -[X]% | Increase budget |

**Performers (Optimize):**
| Asset Group | Spend | Conv | CPA | vs Target | Action |
|-------------|-------|------|-----|-----------|--------|
| [Name] | $[X] | [X] | $[X] | [X]% | Test new assets |

**Underperformers (Fix or Pause):**
| Asset Group | Spend | Conv | CPA | vs Target | Issue | Action |
|-------------|-------|------|-----|-----------|-------|--------|
| [Name] | $[X] | [X] | $[X] | +[X]% | [Issue] | [Action] |

**Budget Distribution:**
```
Asset Group A:  ████████████████ 45% ($[X])
Asset Group B:  ████████ 25% ($[X])
Asset Group C:  ████ 15% ($[X])
Asset Group D:  ██ 10% ($[X])
Other:          █ 5% ($[X])
```

**Distribution Assessment:** [Is budget flowing to winners?]

---

### Asset Performance Analysis

**[Asset Group Name]**

**Text Assets:**
| Type | Asset | Rating | Impressions | Action |
|------|-------|--------|-------------|--------|
| Headline | "[Text]" | Best | [X]M | Keep |
| Headline | "[Text]" | Good | [X]K | Keep |
| Headline | "[Text]" | Low | [X]K | Replace |
| Long Headline | "[Text]" | Good | [X]K | Keep |
| Description | "[Text]" | Best | [X]M | Keep |
| Description | "[Text]" | Low | [X]K | Replace |

**Image Assets:**
| Type | Description | Dimensions | Rating | Action |
|------|-------------|------------|--------|--------|
| Landscape | [Description] | 1200x628 | Best | Keep |
| Square | [Description] | 1200x1200 | Good | Keep |
| Portrait | [Description] | 960x1200 | -- | Needs data |

**Video Assets:**
| Video | Length | Rating | Views | Action |
|-------|--------|--------|-------|--------|
| [Name] | [X]s | Good | [X]K | Keep |

**Asset Coverage Score: [X]/100**
- Headlines: [X]/15 (need [X] more)
- Images: [X]/15 (need [X] more)
- Videos: [X]/5 (need [X] more)

---

### Search Themes Analysis

**Top Search Themes by Volume:**
| Theme | Impression Share | Conv | CPA | Relevance |
|-------|------------------|------|-----|-----------|
| [theme] | [X]% | [X] | $[X] | High/Med/Low |

**Brand vs. Non-Brand Split:**
```
Brand Terms:     ████████ [X]%
Non-Brand Terms: ████████████ [X]%
```

**Assessment:** [Is brand cannibalizing? Non-brand performing?]

**Search Themes Requiring Action:**
| Theme | Issue | Recommended Action |
|-------|-------|-------------------|
| [theme] | Irrelevant | Add as negative |
| [theme] | Brand term | Consider brand exclusion |
| [theme] | High potential | Ensure assets support this theme |

---

### Audience Signal Analysis

**Configured Signals:**
| Signal Type | Signal | Index | Action |
|-------------|--------|-------|--------|
| Customer Match | [List name] | [X]x | [Assessment] |
| Website visitors | [Audience] | [X]x | [Assessment] |
| Custom segment | [Name] | [X]x | [Assessment] |
| In-market | [Audience] | [X]x | [Assessment] |

**Signal Strength Assessment:** [Strong/Medium/Weak]

**Audience Insights:**
- Top converting audiences: [List]
- Unexpected audiences: [List]
- Recommended signals to add: [List]

---

### Placement Distribution

**Channel Breakdown:**
| Channel | Spend | Conv | CPA | % of Total | Assessment |
|---------|-------|------|-----|------------|------------|
| Search | $[X] | [X] | $[X] | [X]% | [Status] |
| Shopping | $[X] | [X] | $[X] | [X]% | [Status] |
| Display | $[X] | [X] | $[X] | [X]% | [Status] |
| YouTube | $[X] | [X] | $[X] | [X]% | [Status] |
| Gmail | $[X] | [X] | $[X] | [X]% | [Status] |
| Discover | $[X] | [X] | $[X] | [X]% | [Status] |

**Distribution Visualization:**
```
Search:   ████████████████████ [X]%
Shopping: ████████████ [X]%
Display:  ████████ [X]%
YouTube:  ████ [X]%
Gmail:    █ [X]%
Discover: ██ [X]%
```

**Channel Concerns:**
- [Any channels significantly over/underperforming]

---

### Diagnosis & Root Causes

**Primary Issue:** [One sentence summary]

**Contributing Factors:**
1. [Factor with evidence]
2. [Factor with evidence]
3. [Factor with evidence]

**Root Cause Analysis:**
```
Symptom: [What you're seeing]
   ↓
Cause: [First level why]
   ↓
Root: [Underlying issue to fix]
```

---

### Action Plan

**Immediate (This Week):**
1. [ ] [High-priority asset change]
2. [ ] [Structural change if needed]
3. [ ] [Signal/negative adjustment]

**Short-Term (Next 2-4 Weeks):**
1. [ ] [Asset testing plan]
2. [ ] [Optimization action]
3. [ ] [Monitoring setup]

**Medium-Term (Next Month):**
1. [ ] [Structural improvements]
2. [ ] [Expansion opportunities]

**Expected Impact:**
- If actions completed: [Projected improvement]
- Timeline: [When to expect results]

---

### Asset Recommendations

**Headlines to Add:**
1. "[Specific headline suggestion]" - [Why]
2. "[Specific headline suggestion]" - [Why]

**Headlines to Remove:**
1. "[Low performer]" - Replace with benefit-focused alternative

**Images Needed:**
1. [Description of image type needed]
2. [Description of image type needed]

**Video Recommendations:**
- [Video strategy recommendation]

---

### Monitoring Checklist

**Weekly Review:**
- [ ] Asset ratings changes
- [ ] Search themes for irrelevant queries
- [ ] Budget distribution across asset groups
- [ ] Conversion volume stability

**Monthly Review:**
- [ ] Full asset performance audit
- [ ] Audience signal effectiveness
- [ ] Channel distribution assessment
- [ ] Structure optimization opportunity

---

## Common PMax Problems & Solutions

### Problem 1: High CPA, Low Conversion Volume
**Symptoms:** CPA above target, few conversions, "Learning Limited"
**Causes:** Not enough budget, too many asset groups, weak signals
**Solutions:**
- Consolidate to fewer asset groups
- Increase budget per asset group
- Strengthen audience signals
- Use value-based bidding if possible

### Problem 2: Lots of Display, Little Search
**Symptoms:** 60%+ Display, low Search volume
**Causes:** Poor search-focused assets, strong visual assets, shopping not eligible
**Solutions:**
- Add search-focused headlines with keywords
- Review final URL expansion settings
- Check if shopping feed is connected
- Add search themes manually

### Problem 3: All Brand Traffic
**Symptoms:** 80%+ branded search themes
**Causes:** Strong brand, weak non-brand signals, brand in assets
**Solutions:**
- Add brand as campaign-level negative (if desired)
- Create separate brand PMax campaign
- Strengthen non-brand audience signals
- Remove brand from headlines

### Problem 4: Inconsistent Performance
**Symptoms:** Wild CPA swings week to week
**Causes:** Low conversion volume, algorithm still learning, external factors
**Solutions:**
- Ensure 30+ conversions/month minimum
- Use longer conversion windows if applicable
- Check for seasonality/competitive changes
- Give more time before making changes

### Problem 5: One Asset Group Dominates
**Symptoms:** 90%+ budget to one asset group
**Causes:** Clear winner, or others poorly structured
**Solutions:**
- If winner performs well, this may be fine
- Review losing asset groups for gaps
- Consider splitting winner into multiple focused groups
- Pause non-performing asset groups

---

## Limitations

**I can provide:**
- Asset group performance analysis
- Asset-level recommendations
- Signal and theme optimization guidance
- Structure improvement suggestions

**I cannot provide:**
- Specific creative design or copywriting
- Feed optimization (separate skill)
- Bid strategy selection (separate skill)
- Full funnel attribution analysis

**For better analysis, provide:**
- Screenshots of asset ratings
- Search themes report export
- Placement report data
- Audience insights data

---

## Quality Checklist

Before delivering analysis:
- [ ] All asset groups evaluated
- [ ] Asset coverage assessed
- [ ] Search themes reviewed for relevance
- [ ] Audience signals evaluated
- [ ] Channel distribution analyzed
- [ ] Specific asset recommendations provided
- [ ] Actions prioritized and specific
- [ ] Expected impact estimated
