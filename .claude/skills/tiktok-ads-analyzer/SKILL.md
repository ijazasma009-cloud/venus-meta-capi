---
name: tiktok-ads-analyzer
description: Analyzes TikTok Ads campaign performance with platform-specific insights on creative performance, audience engagement, and optimization opportunities. Triggers when user asks about TikTok ads, wants to analyze TikTok performance, or mentions "TikTok campaigns," "Spark Ads," "TikTok ROAS," or "TikTok creative testing." Provides actionable recommendations for TikTok's unique algorithm and content style.
---

# TikTok Ads Analyzer

TikTok isn't Meta with dancing. It's a different beast entirely.

## Core Philosophy

**TikTok rewards native content.** The best-performing ads don't look like ads—they look like content that belongs in the For You feed.

**The Algorithm is Different:**
- Meta optimizes for conversions within your audience
- TikTok optimizes for engagement signals that predict conversions
- Creative quality matters MORE on TikTok than targeting

**The 3-Second Rule is Actually a 1-Second Rule.** TikTok users scroll faster than any other platform. You don't have 3 seconds to hook—you have 1.

**What Works on Meta Usually Fails on TikTok:**
- Polished brand content → feels like an ad, gets skipped
- Static images → wrong format entirely
- Long copy → nobody reads it
- Hard sells → users bounce immediately

**What Wins on TikTok:**
- Native, UGC-style content
- Pattern interrupts in first second
- Trends and sounds (when relevant)
- Authentic creators over polished production

---

## Required Context

### Must Have

**1. Campaign Performance Data**
For each campaign:
- Campaign name and objective
- Spend
- Impressions
- Clicks / CTR
- Conversions (or app installs/leads)
- CPA or ROAS
- Video views (2s, 6s, full)

**2. Creative Performance Data**
For each ad:
- Video completion rates (25%, 50%, 75%, 100%)
- Average watch time
- Engagement rate (likes, comments, shares, saves)
- CTR
- Conversion rate

**3. Time Period**
- At least 7 days of data (14+ days preferred)
- TikTok's learning phase is typically 50 conversions

### Strongly Recommended

**4. Creative Details**
- Creator type (in-house, UGC, influencer)
- Hook style used
- Video length
- Use of trending sounds/effects
- Whether it's a Spark Ad or standard ad

**5. Audience Configuration**
- Targeting setup (broad vs. interest-based vs. lookalike)
- Custom audiences used
- Excluded audiences

### Nice to Have

- TikTok Pixel event data
- Organic TikTok performance for comparison
- Competitor ad examples from TikTok Creative Center
- Historical performance trends

---

## Analysis Framework

### Step 1: Platform Health Check

**Account-Level Metrics Assessment:**

| Metric | Poor | Average | Good | Excellent |
|--------|------|---------|------|-----------|
| CTR | <0.5% | 0.5-1% | 1-2% | >2% |
| Video View Rate (2s) | <30% | 30-50% | 50-70% | >70% |
| Video Completion (100%) | <5% | 5-10% | 10-20% | >20% |
| Engagement Rate | <1% | 1-3% | 3-6% | >6% |
| Conversion Rate | <0.5% | 0.5-1% | 1-2% | >2% |

**TikTok-Specific Health Signals:**

| Signal | What It Means |
|--------|---------------|
| High impressions, low 2s views | Hook isn't stopping the scroll |
| Good 2s views, low completion | Content doesn't hold attention |
| High completion, low CTR | No clear call-to-action |
| High CTR, low conversion | Landing page or audience mismatch |
| Low engagement rate | Content isn't resonating, algorithm won't favor it |

---

### Step 2: Creative Performance Analysis

**Hook Effectiveness (First 1-3 Seconds):**

Calculate Hook Rate: `2-Second Views / Impressions × 100`

| Hook Rate | Assessment | Action |
|-----------|------------|--------|
| >60% | Strong hook | Test variations to find even better |
| 40-60% | Average | Hook needs improvement |
| <40% | Weak hook | Completely rethink opening |

**Content Quality (Watch Time):**

| Avg Watch Time vs Video Length | Assessment |
|--------------------------------|------------|
| >50% | Strong content, holds attention |
| 30-50% | Decent, but loses people mid-way |
| <30% | Content isn't working |

**Engagement Quality:**

| Engagement Type | Weight | What It Signals |
|-----------------|--------|-----------------|
| Shares | 🔴 Highest | "This is worth spreading" |
| Saves | 🔴 High | "I want to reference this" |
| Comments | 🟡 Medium | "This sparked a reaction" |
| Likes | 🟢 Lower | "I enjoyed this" |

**Engagement Rate Formula:**
```
Engagement Rate = (Likes + Comments + Shares + Saves) / Impressions × 100
```

---

### Step 3: Creative Categorization

**Rate each creative by type:**

| Creative Type | Typical Performance | Best For |
|---------------|---------------------|----------|
| UGC Testimonial | High trust, moderate CTR | Conversions, consideration |
| Product Demo | Moderate engagement, high intent | Bottom funnel |
| Trending Format | High views, variable conversion | Awareness, testing |
| Problem/Solution | High completion, strong CTR | Direct response |
| Behind-the-Scenes | High engagement, brand building | Awareness |
| Tutorial/How-To | High completion, saves | Consideration |
| Spark Ads (Organic) | Highest authenticity | All objectives |

---

### Step 4: Audience Analysis

**Targeting Efficiency:**

| Targeting Type | When to Use | Expected CPM | Expected Quality |
|----------------|-------------|--------------|------------------|
| Broad | Learning phase, scale | Lower | Variable |
| Interest-Based | Testing, mid-funnel | Medium | Medium |
| Lookalike | Scaling proven audiences | Higher | Higher |
| Custom Audience | Retargeting | Highest | Highest |

**Audience Signal Assessment:**

| Signal | Implication |
|--------|-------------|
| CPM increasing, CPA stable | Healthy scaling |
| CPM increasing, CPA increasing | Audience saturation |
| CPM stable, CPA increasing | Creative fatigue |
| Frequency >3 | Audience too narrow or fatigued |

---

### Step 5: Optimization Opportunities

**Priority Matrix:**

| Issue | Impact | Effort | Priority |
|-------|--------|--------|----------|
| Weak hooks (<40% hook rate) | 🔴 Critical | Medium | P0 - Fix immediately |
| Low completion (<10%) | 🔴 High | Medium | P1 - Address soon |
| Low CTR with good completion | 🟡 Medium | Low | P2 - Add clearer CTA |
| High CPM | 🟡 Medium | Variable | P2 - Test new audiences |
| Low engagement | 🟡 Medium | Medium | P2 - More native content |
| Creative fatigue (declining CTR) | 🔴 High | High | P1 - New creative needed |

---

## Output Format

### Executive Summary

```
TIKTOK ADS PERFORMANCE ANALYSIS
Account: [Account Name]
Period: [Date Range]
Total Spend: $XX,XXX

OVERALL HEALTH: 🟢/🟡/🔴

Key Metrics:
├── Impressions: X.XM
├── Video Views (2s): XXX,XXX (XX% hook rate)
├── Clicks: XX,XXX (X.XX% CTR)
├── Conversions: XXX
├── CPA: $XX.XX
└── ROAS: X.Xx

Top Finding: [Single most important insight]
Biggest Opportunity: [Highest impact optimization]
```

---

### Creative Performance Breakdown

```
📊 CREATIVE ANALYSIS
────────────────────────────────────────────────────────────────────

TOP PERFORMERS:

| Rank | Creative | Spend | Hook Rate | Completion | CTR | CPA | Why It Works |
|------|----------|-------|-----------|------------|-----|-----|--------------|
| 1 | [Name] | $X,XXX | XX% | XX% | X.X% | $XX | [Key factor] |
| 2 | [Name] | $X,XXX | XX% | XX% | X.X% | $XX | [Key factor] |
| 3 | [Name] | $X,XXX | XX% | XX% | X.X% | $XX | [Key factor] |

UNDERPERFORMERS:

| Creative | Issue | Specific Problem | Recommendation |
|----------|-------|------------------|----------------|
| [Name] | Weak hook | XX% hook rate | [Specific fix] |
| [Name] | Low completion | XX% avg watch | [Specific fix] |
| [Name] | Poor CTR | X.X% CTR | [Specific fix] |

CREATIVE PATTERNS IDENTIFIED:
✅ Working: [Pattern that's winning - be specific]
✅ Working: [Another winning pattern]
❌ Not Working: [Pattern that's failing]
❌ Not Working: [Another failing pattern]
```

---

### Hook Analysis

```
🎣 HOOK EFFECTIVENESS ANALYSIS
────────────────────────────────────────────────────────────────────

| Hook Type | # Creatives | Avg Hook Rate | Avg CPA | Verdict |
|-----------|-------------|---------------|---------|---------|
| Question opener | X | XX% | $XX | [Working/Not] |
| Bold statement | X | XX% | $XX | [Working/Not] |
| Pattern interrupt | X | XX% | $XX | [Working/Not] |
| Product first | X | XX% | $XX | [Working/Not] |
| Creator intro | X | XX% | $XX | [Working/Not] |

RECOMMENDED HOOK STRATEGY:
Based on your data, prioritize [hook type] hooks because [specific reason with data].

HOOKS TO TEST:
1. [Specific hook idea based on what's working]
2. [Another hook variation]
3. [Third hook concept]
```

---

### Audience Insights

```
👥 AUDIENCE PERFORMANCE
────────────────────────────────────────────────────────────────────

| Audience | Spend | CPM | CTR | CPA | Efficiency |
|----------|-------|-----|-----|-----|------------|
| [Audience 1] | $X,XXX | $X.XX | X.X% | $XX | ⭐ Star |
| [Audience 2] | $X,XXX | $X.XX | X.X% | $XX | ✅ Solid |
| [Audience 3] | $X,XXX | $X.XX | X.X% | $XX | ❌ Poor |

AUDIENCE RECOMMENDATIONS:
- Scale: [Audience] - [why]
- Maintain: [Audience] - [why]
- Reduce: [Audience] - [why]
- Test: [New audience idea]
```

---

### Optimization Roadmap

```
🎯 OPTIMIZATION RECOMMENDATIONS
────────────────────────────────────────────────────────────────────

IMMEDIATE (This Week):

1. [Specific action]
   - Current: [metric]
   - Target: [metric]
   - Expected impact: [outcome]

2. [Specific action]
   - Current: [metric]
   - Target: [metric]
   - Expected impact: [outcome]

SHORT-TERM (Next 2 Weeks):

1. [Specific action]
   - Rationale: [why]
   - Resources needed: [what]

2. [Specific action]
   - Rationale: [why]
   - Resources needed: [what]

TESTING AGENDA:

| Priority | Test | Hypothesis | Success Metric |
|----------|------|------------|----------------|
| P0 | [Test 1] | [Hypothesis] | [Metric] |
| P1 | [Test 2] | [Hypothesis] | [Metric] |
| P2 | [Test 3] | [Hypothesis] | [Metric] |
```

---

### TikTok-Specific Recommendations

```
📱 PLATFORM-SPECIFIC OPPORTUNITIES
────────────────────────────────────────────────────────────────────

SPARK ADS ASSESSMENT:
- Current Spark Ad usage: [X]% of spend
- Recommendation: [Increase/Maintain/Decrease]
- Why: [Reasoning]

TRENDING OPPORTUNITIES:
- Current trending sounds/formats you could leverage: [List]
- Caution: Only use if genuinely relevant to your brand

CREATIVE CENTER INSIGHTS:
- Top-performing ad formats in your category: [List]
- Competitor creative patterns to consider: [List]

TIKTOK SHOP INTEGRATION (if applicable):
- Current usage: [Yes/No]
- Opportunity: [Assessment]
```

---

## Common Scenarios

### Scenario 1: High Impressions, Low Conversions
**Diagnosis:** Either hook is weak (users scroll past) or content doesn't drive action
**Check:**
1. Hook rate (<40% = hook problem)
2. Completion rate (<10% = content problem)
3. CTR (<0.5% = CTA problem)
4. Post-click conversion rate (<1% = landing page problem)

**Solution Path:** Fix from top of funnel down—hook first, then content, then CTA.

### Scenario 2: Good Metrics, High CPA
**Diagnosis:** Likely an audience or offer problem, not creative
**Check:**
1. Compare CPM across audiences
2. Check frequency (>3 = saturation)
3. Compare to Meta/Google CPA for same offer

**Solution Path:** Test broader audiences, refresh custom audiences, or evaluate offer competitiveness.

### Scenario 3: Creative Fatigue (Declining Performance)
**Signals:**
- CTR declining week-over-week
- Frequency increasing
- CPM stable but CPA rising

**Solution Path:**
1. Immediate: Launch 2-3 new creative variations
2. Short-term: Build creative testing calendar (new hooks weekly)
3. Long-term: Establish UGC creator pipeline

### Scenario 4: Works on Meta, Fails on TikTok
**Common Causes:**
- Content too polished/branded
- Wrong aspect ratio (not 9:16)
- No hook in first second
- Missing platform-native elements (sounds, text overlays)

**Solution Path:** Don't port Meta creative—create TikTok-native content from scratch.

### Scenario 5: Can't Exit Learning Phase
**Diagnosis:** Not enough conversions (need ~50 per week)
**Solutions:**
1. Optimize for upper-funnel event (Add to Cart vs Purchase)
2. Increase budget to accelerate learning
3. Broaden audience to increase volume
4. Combine ad groups if running too many

---

## TikTok-Specific Best Practices

### Creative Guidelines

**DO:**
- Shoot in 9:16 vertical format
- Hook in first 1 second
- Use trending sounds when relevant
- Include text overlays (many watch without sound)
- Feature real people, not just products
- Show the product in use
- Use fast cuts and dynamic editing
- Include clear CTA in final 3 seconds

**DON'T:**
- Repurpose horizontal video
- Start with your logo
- Use stock footage
- Over-produce (too polished = ad)
- Ignore comments on ads
- Run same creative >4 weeks without refresh

### Spark Ads Strategy

| When to Use Spark Ads | When to Use Standard Ads |
|-----------------------|--------------------------|
| Have performing organic content | Testing new concepts |
| Creator partnerships | Full creative control needed |
| Authenticity matters most | Specific CTA requirements |
| Brand building | Direct response focus |

### Budget & Bidding

| Objective | Recommended Budget | Bidding Strategy |
|-----------|--------------------|------------------|
| Learning phase | $50-100/day/ad group | Lowest Cost |
| Scaling | 20% increases every 3-4 days | Lowest Cost |
| Efficiency focus | Stable budget | Cost Cap |
| Predictable costs | Higher budget | Bid Cap |

---

## Limitations

**I can provide:**
- Performance assessment against TikTok benchmarks
- Creative pattern analysis
- Hook effectiveness evaluation
- Audience efficiency ranking
- Specific optimization recommendations
- Testing priorities

**I cannot provide:**
- Access to TikTok Creative Center data
- Real-time trending sound recommendations
- Competitor ad performance data
- Attribution across platforms
- Incrementality measurement

**For deeper analysis, also provide:**
- TikTok Pixel event breakdown
- Day/hour performance data
- Placement breakdown (For You vs Following vs Search)
- New vs returning user performance

---

## Quality Checklist

Before delivering analysis:
- [ ] All creatives categorized by type and performance tier
- [ ] Hook rate calculated for each creative
- [ ] Completion rates analyzed with clear diagnosis
- [ ] Audience efficiency ranked
- [ ] Platform-specific recommendations included (not generic advice)
- [ ] Spark Ads opportunity assessed
- [ ] Testing roadmap prioritized by impact
- [ ] TikTok-native creative guidance provided
- [ ] Limitations clearly stated
