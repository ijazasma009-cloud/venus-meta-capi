---
name: ad-landing-page-match-scorer
description: Scores the alignment between ads and their landing pages to identify conversion-killing disconnects. Triggers when user shares ad copy and landing page together, asks "why is my Quality Score low?", or wants to improve post-click experience. Evaluates headline match, offer consistency, keyword presence, visual continuity, and audience alignment. Provides specific fixes to improve conversion rate and Quality Score.
---

# Ad-to-Landing Page Match Scorer

Bridge the gap between what your ad promises and what your page delivers.

## Core Philosophy

**Every click is a micro-commitment.** When someone clicks your ad, they've made a small bet that what's on the other side will match their expectation. Break that promise, and they bounce.

**The Goal:** Achieve perfect message match so visitors instantly recognize they're in the right place.

**The Principle:** The landing page should feel like a natural continuation of the ad—same promise, same language, same offer, just expanded.

---

## Required Context

### Must Have

**1. Ad Creative**
For each ad:
- Headlines (all variations for RSAs)
- Descriptions
- Display URL/path
- Final URL
- Any extensions (sitelinks, callouts, etc.)

**2. Landing Page**
- URL or screenshots (full page)
- Above-the-fold content (critical)
- Primary CTA

### Strongly Recommended

**3. Campaign Context**
- Target keywords (for search ads)
- Target audience (for social/display)
- Campaign objective
- Ad platform (Google, Meta, LinkedIn, etc.)

**4. Performance Data**
- Quality Score (Google Ads)
- Landing page experience rating
- Conversion rate
- Bounce rate

### Nice to Have

- Multiple ad variations to compare
- Competitor ad/landing page examples
- Historical performance by ad variation
- Heatmaps or user behavior data

---

## Scoring Framework

### The 5 Dimensions of Message Match

| Dimension | Weight | What It Measures |
|-----------|--------|------------------|
| **Headline Match** | 25% | Does LP headline echo ad headline? |
| **Offer Match** | 25% | Is the promised offer prominently displayed? |
| **Keyword Match** | 20% | Are search terms reflected on the page? |
| **Visual Match** | 15% | Is design/imagery consistent? |
| **Audience Match** | 15% | Does language fit the target audience? |

**Total Score: XX/100**

---

### Dimension 1: Headline Match (25 points)

**The Instant Recognition Test:** In under 2 seconds, can visitors confirm they clicked on the right thing?

**Evaluation Criteria:**

| Element | Check | Points |
|---------|-------|--------|
| Exact phrase match | Ad headline words appear in LP headline | 0-10 |
| Semantic match | Same meaning, different words | 0-5 |
| Benefit continuation | LP headline expands on ad promise | 0-5 |
| Visibility | Headline is immediately visible | 0-5 |

**Scoring Guide:**

| Score | Assessment | Example |
|-------|------------|---------|
| 22-25 | Excellent | Ad: "Get 50% Off Today" → LP: "Get 50% Off Your First Order Today" |
| 17-21 | Good | Ad: "Get 50% Off Today" → LP: "Half-Price Sale - Today Only" |
| 10-16 | Weak | Ad: "Get 50% Off Today" → LP: "Welcome to Our Store" |
| <10 | Poor | Ad: "Get 50% Off Today" → LP: "Premium Quality Products" |

**Common Headline Disconnects:**
- Generic LP headline for specific ad promise
- LP headline buried below hero image
- LP uses different terminology than ad
- Ad promotes feature, LP headline promotes different feature

---

### Dimension 2: Offer Match (25 points)

**The Promise Test:** Is the specific offer in the ad delivered on the landing page?

**Evaluation Criteria:**

| Element | Check | Points |
|---------|-------|--------|
| Offer presence | Advertised offer visible above fold | 0-10 |
| Offer prominence | Not buried in fine print | 0-5 |
| Terms match | Same discount/free trial/bonus terms | 0-5 |
| Exclusions clear | Any limitations stated | 0-5 |

**Common Offer Types to Check:**

| Ad Promise | LP Must Have |
|------------|--------------|
| "50% Off" | Discount clearly shown, applies to visible products |
| "Free Trial" | Trial length, no credit card (if claimed), start button |
| "Free Shipping" | Threshold and conditions visible |
| "Get Quote" | Quote form, not generic contact form |
| "$X/month" | Pricing visible, same number, billing terms |
| "Download Free Guide" | Guide download form, guide preview/cover |

**Scoring Guide:**

| Score | Assessment |
|-------|------------|
| 22-25 | Offer prominently displayed exactly as advertised |
| 17-21 | Offer present but requires scrolling/searching |
| 10-16 | Offer exists but terms differ or are unclear |
| <10 | Offer not found or significantly different |

---

### Dimension 3: Keyword Match (20 points)

**The Relevance Test:** Do the user's search terms appear naturally on the page?

**Evaluation Criteria:**

| Element | Check | Points |
|---------|-------|--------|
| Primary keyword | Main keyword in headline or first paragraph | 0-8 |
| Secondary keywords | Related terms throughout page | 0-5 |
| Natural integration | Keywords don't feel forced | 0-4 |
| Semantic coverage | Related concepts addressed | 0-3 |

**Keyword Presence Check:**

| Keyword | In Headline? | In Body? | In Meta? | Natural? |
|---------|--------------|----------|----------|----------|
| [Keyword 1] | Y/N | Y/N | Y/N | Y/N |
| [Keyword 2] | Y/N | Y/N | Y/N | Y/N |
| [Keyword 3] | Y/N | Y/N | Y/N | Y/N |

**Impact on Quality Score:**
- Primary keyword in headline: +significant QS boost
- Keywords in body content: Improves relevance rating
- Natural language: Better than keyword stuffing
- Missing keywords: Major relevance signal loss

---

### Dimension 4: Visual Match (15 points)

**The Continuity Test:** Does the landing page feel like it belongs to the same campaign?

**Evaluation Criteria:**

| Element | Check | Points |
|---------|-------|--------|
| Color consistency | Brand colors match ad/display creative | 0-4 |
| Imagery alignment | Similar style, quality, subject matter | 0-4 |
| Logo presence | Brand visible immediately | 0-3 |
| Layout expectations | Matches what ad implied | 0-4 |

**For Display/Social Ads:**

| Ad Element | LP Presence | Match Quality |
|------------|-------------|---------------|
| Hero image | Same/similar image used? | Exact/Similar/Different |
| Color scheme | Colors consistent? | Yes/Partial/No |
| Typography style | Font style similar? | Yes/Partial/No |
| Model/person | Same person appears? | Yes/No/N/A |

**Visual Discontinuity Red Flags:**
- Ad shows product, LP shows lifestyle image
- Ad is clean/minimal, LP is cluttered
- Ad uses photos, LP uses illustrations (or vice versa)
- Different brand feel between ad and page

---

### Dimension 5: Audience Match (15 points)

**The "Right Place" Test:** Does the language feel like it was written for this specific audience?

**Evaluation Criteria:**

| Element | Check | Points |
|---------|-------|--------|
| Tone consistency | Same voice in ad and LP | 0-4 |
| Terminology | Appropriate for audience expertise | 0-4 |
| Pain points | Same problems addressed | 0-4 |
| Use cases | Relevant to audience's situation | 0-3 |

**Audience Alignment Check:**

| Factor | Ad Implies | LP Delivers | Match? |
|--------|------------|-------------|--------|
| Expertise level | Beginner/Intermediate/Expert | ? | Y/N |
| Industry/vertical | [Specific industry] | ? | Y/N |
| Company size | SMB/Enterprise | ? | Y/N |
| Role/persona | [Specific role] | ? | Y/N |
| Problem focus | [Specific pain point] | ? | Y/N |

**Common Audience Mismatches:**
- Ad targets beginners, LP uses jargon
- Ad targets enterprise, LP shows SMB testimonials
- Ad speaks to specific role, LP is generic
- Ad addresses pain point A, LP focuses on pain point B

---

## Output Format

### Executive Summary

```
MESSAGE MATCH SCORE: XX/100 [GRADE]

Ad: [Ad headline or identifier]
Landing Page: [URL or name]
Platform: [Google/Meta/LinkedIn/etc.]

MATCH LEVEL: Excellent / Good / Weak / Poor
PRIMARY DISCONNECT: [Biggest issue]
ESTIMATED CONVERSION IMPACT: -XX% (due to mismatch)
QUALITY SCORE IMPACT: [For Google Ads only]
```

**Grade Scale:**

| Score | Grade | Match Level | Typical Impact |
|-------|-------|-------------|----------------|
| 85-100 | A | Excellent | Optimal conversion |
| 70-84 | B | Good | ~5-15% conversion loss |
| 55-69 | C | Weak | ~15-30% conversion loss |
| 40-54 | D | Poor | ~30-50% conversion loss |
| <40 | F | Severe Mismatch | ~50%+ conversion loss |

---

### Dimension Scores Breakdown

```
HEADLINE MATCH:   ████████████████░░░░ 20/25
OFFER MATCH:      ████████████░░░░░░░░ 15/25  ⚠️
KEYWORD MATCH:    ██████████████████░░ 18/20
VISUAL MATCH:     ████████████░░░░░░░░ 12/15
AUDIENCE MATCH:   ██████████████░░░░░░ 13/15

TOTAL SCORE:      78/100 (B)
```

---

### Detailed Analysis

#### Headline Match Analysis

**Ad Headline:**
> "[Exact ad headline text]"

**Landing Page Headline:**
> "[Exact LP headline text]"

**Assessment:**
- Word overlap: [X out of Y key words]
- Semantic similarity: High/Medium/Low
- Promise continuity: [Assessment]
- Immediate visibility: Yes/No

**Score: XX/25**

**Recommendation:**
> [Suggested improved LP headline that better matches ad]

---

#### Offer Match Analysis

**Ad Offer:**
> "[What the ad promises - discount, trial, download, etc.]"

**Landing Page Offer:**
- Present: Yes/No
- Prominence: Above fold / Below fold / Buried / Missing
- Terms match: Exact / Similar / Different
- Visibility: Immediate / Requires scrolling / Hidden

**Score: XX/25**

**Issues Found:**
- [Issue 1]
- [Issue 2]

**Recommendation:**
- [Specific fix to improve offer visibility/match]

---

#### Keyword Match Analysis

**Target Keywords:**
| Keyword | Search Volume | In Headline | In Body | In CTA |
|---------|---------------|-------------|---------|--------|
| [Keyword 1] | High | ✓/✗ | ✓/✗ | ✓/✗ |
| [Keyword 2] | Medium | ✓/✗ | ✓/✗ | ✓/✗ |
| [Keyword 3] | Medium | ✓/✗ | ✓/✗ | ✓/✗ |

**Coverage Assessment:**
- Primary keyword presence: [Assessment]
- Semantic relevance: [Assessment]
- Natural integration: [Assessment]

**Score: XX/20**

**Recommendation:**
- [Specific suggestions for keyword integration]

---

#### Visual Match Analysis

**Ad Creative Elements:**
- Primary color: [Color]
- Image type: [Photo/Illustration/None]
- Style: [Modern/Traditional/Minimal/etc.]

**Landing Page Elements:**
- Primary color: [Color]
- Hero image: [Description]
- Style: [Assessment]

**Continuity Assessment:**
| Element | Match Level |
|---------|-------------|
| Colors | ✓ Match / ~ Partial / ✗ Different |
| Imagery | ✓ Match / ~ Partial / ✗ Different |
| Typography | ✓ Match / ~ Partial / ✗ Different |
| Overall feel | ✓ Match / ~ Partial / ✗ Different |

**Score: XX/15**

---

#### Audience Match Analysis

**Ad Targeting:**
- Audience: [Description]
- Implied expertise: [Level]
- Pain point focus: [Description]

**Landing Page Audience Signals:**
- Language complexity: [Assessment]
- Examples/use cases: [Relevant/Generic/Misaligned]
- Social proof: [Matches audience or not]

**Score: XX/15**

---

### Priority Fixes

**Fix 1: [Highest Priority Issue]**
- **Dimension:** [Which dimension]
- **Current:** [What exists now]
- **Recommended:** [What it should be]
- **Impact:** +XX points / Estimated +XX% conversion
- **Effort:** Low / Medium / High

---

**Fix 2: [Second Priority Issue]**
- **Dimension:** [Which dimension]
- **Current:** [What exists now]
- **Recommended:** [What it should be]
- **Impact:** +XX points / Estimated +XX% conversion
- **Effort:** Low / Medium / High

---

### Rewrite Recommendations

**Landing Page Headline:**
| Current | Recommended | Rationale |
|---------|-------------|-----------|
| "[Current headline]" | "[Better headline]" | [Why this matches better] |

**Landing Page Subheadline:**
| Current | Recommended | Rationale |
|---------|-------------|-----------|
| "[Current]" | "[Better]" | [Why] |

**CTA Button:**
| Current | Recommended | Rationale |
|---------|-------------|-----------|
| "[Current CTA]" | "[Better CTA]" | [Why] |

---

### Quality Score Impact (Google Ads)

**Landing Page Experience Factors:**

| Factor | Assessment | Impact |
|--------|------------|--------|
| Relevance to ad/keywords | Good/Average/Poor | High |
| Transparency | Good/Average/Poor | Medium |
| Navigation ease | Good/Average/Poor | Medium |
| Load time | Good/Average/Poor | High |
| Mobile optimization | Good/Average/Poor | High |

**Expected QS Component Ratings:**
- Ad Relevance: Above Average / Average / Below Average
- Landing Page Experience: Above Average / Average / Below Average

**Recommendations to Improve QS:**
1. [Specific recommendation]
2. [Specific recommendation]

---

### Side-by-Side Comparison

```
┌─────────────────────────────────────────────────────────────────┐
│ AD                              │ LANDING PAGE                  │
├─────────────────────────────────┼───────────────────────────────┤
│ Headline:                       │ Headline:                     │
│ [Ad headline]                   │ [LP headline]                 │
│                                 │ Match: ✓/✗                    │
├─────────────────────────────────┼───────────────────────────────┤
│ Offer:                          │ Offer:                        │
│ [Ad offer]                      │ [LP offer]                    │
│                                 │ Match: ✓/✗                    │
├─────────────────────────────────┼───────────────────────────────┤
│ Keywords:                       │ Keywords:                     │
│ [Target keywords]               │ [Keywords present]            │
│                                 │ Match: ✓/✗                    │
├─────────────────────────────────┼───────────────────────────────┤
│ CTA:                            │ CTA:                          │
│ [Ad CTA/extension]              │ [LP CTA]                      │
│                                 │ Match: ✓/✗                    │
└─────────────────────────────────┴───────────────────────────────┘
```

---

## Platform-Specific Guidance

### Google Search Ads

**Additional Checks:**
- RSA headline variations: Do ALL headlines have LP match?
- Sitelink alignment: Do sitelinks match LP navigation?
- Callout extensions: Are claims substantiated on LP?
- Dynamic keyword insertion: Does LP handle all keyword variations?

**Quality Score Focus:**
- Landing page experience is 1/3 of Quality Score
- Match directly impacts Ad Relevance rating
- Poor match = higher CPCs, lower impression share

### Google Display Ads

**Additional Checks:**
- Visual creative to LP hero image consistency
- Display targeting match (audience, placement context)
- Responsive display ad variations all have LP match

### Meta (Facebook/Instagram) Ads

**Additional Checks:**
- Ad image to LP hero match (critical for visual platform)
- Ad copy tone to LP copy tone
- Audience targeting vs LP personalization
- Carousel card to LP section alignment

### LinkedIn Ads

**Additional Checks:**
- B2B credibility signals match
- Professional tone consistency
- Company size/industry targeting reflected
- Lead gen form to LP form consistency

---

## Special Scenarios

### Scenario 1: RSA with Many Variations
**Challenge:** 15 headlines, 4 descriptions—how to match all?
**Approach:**
- Identify most-shown combinations (via ad asset report)
- Ensure LP has elements matching top performers
- Use dynamic text replacement if significant keyword variation
- Consider separate LPs for different intent groups

### Scenario 2: Multiple Keywords, One Landing Page
**Challenge:** Various keywords pointing to same page
**Approach:**
- Score for each major keyword theme
- Identify which keywords have weakest match
- Consider: Dynamic keyword insertion on LP
- Consider: Separate LPs for keyword groups with poor match

### Scenario 3: Generic Landing Page
**Challenge:** LP is homepage or category page, not specific
**Approach:**
- Always recommend dedicated landing page
- Score as-is for baseline
- Quantify expected lift from dedicated LP
- Provide minimum viable LP elements

### Scenario 4: Localized Ads
**Challenge:** Geo-targeted ads, one landing page
**Approach:**
- Check for location signals on LP
- Score location match as additional dimension
- Recommend dynamic geo-personalization
- Consider location-specific landing pages

---

## Limitations

**I can assess:**
- Message/copy alignment between ad and LP
- Keyword presence and prominence
- Visual consistency (from screenshots)
- Obvious friction and disconnects
- Quality Score factors (for Google Ads)

**I cannot assess:**
- Actual page load speed (use PageSpeed Insights)
- Technical LP implementation
- Real user behavior (need heatmaps)
- Actual Quality Score data (need Google Ads access)
- Post-click tracking accuracy

**For complete analysis, also provide:**
- Google Ads Quality Score and component ratings
- Bounce rate for ad traffic specifically
- Heatmaps showing click/scroll behavior
- Conversion rate by ad variation

---

## Quality Checklist

Before delivering analysis:
- [ ] All 5 dimensions scored
- [ ] Specific disconnects identified
- [ ] Side-by-side comparison clear
- [ ] Rewrite recommendations specific and actionable
- [ ] Priority order justified
- [ ] Platform-specific factors addressed (if applicable)
- [ ] Quality Score impact estimated (for Google Ads)
- [ ] Effort level indicated for each fix
- [ ] Limitations acknowledged
