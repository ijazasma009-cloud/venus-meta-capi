---
name: post-click-experience-auditor
description: Audits the entire post-click journey from ad click to conversion, identifying friction points, message mismatches, and drop-off causes. Triggers when user asks about landing page performance, conversion rate optimization, "why aren't my ads converting," "post-click analysis," or "landing page audit for ads." Bridges the gap between ad performance and conversion rate optimization.
---

# Post-Click Experience Auditor

Your ad got the click. Now what? The post-click experience is where most ad budgets go to die.

## Core Philosophy

**The click is not the goal.** The conversion is. Every friction point between click and conversion is money burned.

**Message Match is Non-Negotiable.** If your ad says "50% off running shoes" and your landing page shows your full catalog with no mention of the offer, you've betrayed the click. That visitor is gone.

**Speed Kills (Slowly).** Every second of load time costs you 7% of conversions. A 5-second load time means you've lost 35% before they even see your page.

**Mobile First Isn't Optional.** 70%+ of paid traffic is mobile. If your page isn't optimized for thumbs, you're optimizing for failure.

**The Landing Page Isn't the End.** The journey continues through form fills, checkout flows, confirmation pages. Audit the entire path.

---

## Required Context

### Must Have

**1. The Ad**
- Ad copy (headlines, descriptions, primary text)
- Ad creative (image/video description or actual asset)
- Offer communicated in the ad
- Call-to-action used

**2. The Landing Page**
- URL
- Screenshot or description of above-the-fold content
- Primary CTA on the page
- Key messaging/headline

**3. Performance Data**
- Click-through rate (CTR)
- Landing page conversion rate
- Bounce rate
- Average time on page (if available)

### Strongly Recommended

**4. Traffic Context**
- Traffic source (Google, Meta, TikTok, etc.)
- Campaign type (Search, Display, Social)
- Audience targeting (cold, warm, retargeting)
- Device breakdown (mobile vs desktop)

**5. Conversion Action**
- What counts as a conversion?
- Form fill, purchase, sign-up, etc.
- Number of steps to complete conversion

**6. Page Load Data**
- Page load time (especially mobile)
- Core Web Vitals if available
- Any known technical issues

### Nice to Have

- Heat maps or scroll maps
- Session recordings
- Form analytics (field drop-off)
- Exit page data
- A/B test history

---

## Audit Framework

### Audit Layer 1: Message Match Analysis

**The Promise-Delivery Check:**

| Ad Element | Landing Page Element | Match Score |
|------------|---------------------|-------------|
| Headline claim | H1/Hero headline | ✅ Exact / ⚠️ Partial / ❌ Missing |
| Specific offer | Visible offer | ✅ Exact / ⚠️ Partial / ❌ Missing |
| CTA action | Primary CTA | ✅ Exact / ⚠️ Partial / ❌ Missing |
| Visual style | Page design | ✅ Consistent / ⚠️ Different / ❌ Jarring |
| Audience language | Page copy | ✅ Aligned / ⚠️ Generic / ❌ Mismatched |

**Message Match Scoring:**

| Score | Assessment | Expected Impact |
|-------|------------|-----------------|
| 5/5 matches | Excellent | Optimal conversion potential |
| 4/5 matches | Good | Minor friction |
| 3/5 matches | Fair | Noticeable drop-off |
| 2/5 matches | Poor | Significant conversion loss |
| 0-1/5 matches | Critical | Majority of clicks wasted |

**Common Message Match Failures:**

| Failure Type | Example | Fix |
|--------------|---------|-----|
| Offer mismatch | Ad: "Free trial" → Page: No mention | Hero must show offer |
| Audience mismatch | Ad: "For agencies" → Page: Generic | Audience-specific landing page |
| Feature mismatch | Ad: "AI writing" → Page: All features | Dedicated feature page |
| Visual disconnect | Ad: Lifestyle image → Page: Product grid | Consistent visual story |
| CTA mismatch | Ad: "Get quote" → Page: "Contact us" | Match CTA language exactly |

---

### Audit Layer 2: First Impression Assessment

**The 5-Second Test:**
If someone saw this page for 5 seconds, would they know:
- [ ] What you're offering?
- [ ] Why it matters to them?
- [ ] What to do next?

**Above-the-Fold Checklist:**

| Element | Present | Effective | Score |
|---------|---------|-----------|-------|
| Clear headline | ✅/❌ | ✅/❌ | /2 |
| Supporting subhead | ✅/❌ | ✅/❌ | /2 |
| Primary CTA | ✅/❌ | ✅/❌ | /2 |
| Relevant visual | ✅/❌ | ✅/❌ | /2 |
| Value proposition | ✅/❌ | ✅/❌ | /2 |

**Score Interpretation:**
- 9-10: Strong first impression
- 7-8: Good, minor improvements possible
- 5-6: Weak, significant improvements needed
- <5: Critical issues, likely high bounce rate

---

### Audit Layer 3: Page Speed & Technical

**Speed Benchmarks:**

| Load Time | Assessment | Conversion Impact |
|-----------|------------|-------------------|
| <2 seconds | Excellent | Optimal |
| 2-3 seconds | Good | ~7% loss |
| 3-5 seconds | Fair | ~20% loss |
| 5-7 seconds | Poor | ~35% loss |
| >7 seconds | Critical | ~50%+ loss |

**Core Web Vitals Targets:**

| Metric | Good | Needs Work | Poor |
|--------|------|------------|------|
| LCP (Largest Contentful Paint) | <2.5s | 2.5-4s | >4s |
| FID (First Input Delay) | <100ms | 100-300ms | >300ms |
| CLS (Cumulative Layout Shift) | <0.1 | 0.1-0.25 | >0.25 |

**Technical Checklist:**

- [ ] Page loads in <3 seconds on mobile
- [ ] No layout shifts during load
- [ ] Images optimized and lazy-loaded
- [ ] No broken elements or console errors
- [ ] HTTPS secure connection
- [ ] Mobile-responsive design
- [ ] Forms work on all devices
- [ ] Payment systems functional (if applicable)

---

### Audit Layer 4: Mobile Experience

**Mobile-Specific Assessment:**

| Element | Check | Score |
|---------|-------|-------|
| Touch targets | Buttons >44px, spaced properly | ✅/❌ |
| Readable text | No pinch-to-zoom needed | ✅/❌ |
| Form usability | Proper keyboard types, autofill | ✅/❌ |
| Thumb-friendly | Key actions in thumb zone | ✅/❌ |
| No horizontal scroll | Content fits viewport | ✅/❌ |
| Fast load | <3 seconds on 4G | ✅/❌ |

**Mobile Conversion Killers:**

| Issue | Impact | Priority |
|-------|--------|----------|
| Tiny tap targets | High friction, rage taps | P0 |
| Intrusive pop-ups | Blocks content, Google penalty | P0 |
| Unresponsive forms | Cannot convert | P0 |
| Slow load time | Abandonment | P1 |
| Horizontal scrolling | Confusion, frustration | P1 |
| Small text | Cannot read offer | P1 |

---

### Audit Layer 5: Conversion Path Analysis

**Funnel Mapping:**

```
AD CLICK
    ↓
LANDING PAGE (Entry)
    ↓ [Drop-off point 1: Bounce]
SCROLL / ENGAGEMENT
    ↓ [Drop-off point 2: Lack of interest]
CTA CLICK
    ↓ [Drop-off point 3: CTA not compelling]
FORM / CHECKOUT
    ↓ [Drop-off point 4: Form friction]
SUBMISSION
    ↓ [Drop-off point 5: Technical failure]
CONFIRMATION
```

**Conversion Rate Benchmarks by Type:**

| Conversion Type | Poor | Average | Good | Excellent |
|-----------------|------|---------|------|-----------|
| Lead gen form | <2% | 2-5% | 5-10% | >10% |
| E-commerce | <1% | 1-2% | 2-4% | >4% |
| Free trial | <3% | 3-7% | 7-15% | >15% |
| Webinar signup | <10% | 10-20% | 20-35% | >35% |
| Content download | <15% | 15-30% | 30-50% | >50% |

**Form Friction Analysis:**

| Factor | Low Friction | High Friction |
|--------|--------------|---------------|
| Number of fields | 3-5 fields | 8+ fields |
| Required info | Email only | Phone, company size, etc. |
| Field types | Dropdowns, radios | Open text, multiple pages |
| Error handling | Inline, clear | Page reload, vague |
| Progress indication | Visible steps | No indication |

---

### Audit Layer 6: Trust & Credibility

**Trust Element Checklist:**

| Element | Present | Placement | Effectiveness |
|---------|---------|-----------|---------------|
| Social proof (reviews, ratings) | ✅/❌ | Above/Below fold | ✅/⚠️/❌ |
| Logos (clients, press, partners) | ✅/❌ | Above/Below fold | ✅/⚠️/❌ |
| Testimonials | ✅/❌ | Above/Below fold | ✅/⚠️/❌ |
| Security badges | ✅/❌ | Near forms/checkout | ✅/⚠️/❌ |
| Money-back guarantee | ✅/❌ | Near CTA | ✅/⚠️/❌ |
| Contact information | ✅/❌ | Visible | ✅/⚠️/❌ |

**Trust Gap Analysis:**

For cold traffic (top of funnel):
- [ ] Proof that others have succeeded
- [ ] Low-risk first step (free, trial, guarantee)
- [ ] Credibility signals visible above fold

For warm traffic (retargeting):
- [ ] Reminder of previous interaction
- [ ] Urgency or incentive to act now
- [ ] Reduced friction (pre-filled info)

---

### Audit Layer 7: Objection Handling

**Common Objection Checklist:**

| Objection | Addressed? | Where? |
|-----------|------------|--------|
| "Is this worth the price?" | ✅/❌ | [Location] |
| "Will this work for me?" | ✅/❌ | [Location] |
| "Can I trust this company?" | ✅/❌ | [Location] |
| "What if it doesn't work?" | ✅/❌ | [Location] |
| "Is now the right time?" | ✅/❌ | [Location] |
| "Is this difficult to use?" | ✅/❌ | [Location] |

**Objection Handling Best Practices:**

| Objection | Best Response |
|-----------|---------------|
| Price concern | Value demonstration, ROI calculator, comparison |
| Fit concern | Testimonials from similar customers, use cases |
| Trust concern | Reviews, guarantees, security badges |
| Risk concern | Free trial, money-back guarantee, case studies |
| Timing concern | Urgency (real, not fake), cost of waiting |
| Complexity concern | Demo video, "how it works" section |

---

## Output Format

### Executive Summary

```
POST-CLICK EXPERIENCE AUDIT
═══════════════════════════════════════════════════════════════════
Ad Source: [Platform - Campaign]
Landing Page: [URL]
Audit Date: [Date]
═══════════════════════════════════════════════════════════════════

OVERALL SCORE: [X/100]

| Category | Score | Priority |
|----------|-------|----------|
| Message Match | [X/20] | [P0/P1/P2] |
| First Impression | [X/20] | [P0/P1/P2] |
| Page Speed | [X/15] | [P0/P1/P2] |
| Mobile Experience | [X/15] | [P0/P1/P2] |
| Conversion Path | [X/15] | [P0/P1/P2] |
| Trust Elements | [X/15] | [P0/P1/P2] |

TOP 3 ISSUES:
1. [Critical issue #1] - [Expected impact]
2. [Critical issue #2] - [Expected impact]
3. [Critical issue #3] - [Expected impact]

QUICK WIN:
[Single highest-impact, lowest-effort fix]
```

---

### Detailed Analysis

```
📊 MESSAGE MATCH ANALYSIS
────────────────────────────────────────────────────────────────────

AD PROMISE vs PAGE DELIVERY:

| Ad Element | Ad Says | Page Shows | Match |
|------------|---------|------------|-------|
| Headline | "[text]" | "[text]" | ✅/⚠️/❌ |
| Offer | "[text]" | "[text]" | ✅/⚠️/❌ |
| CTA | "[text]" | "[text]" | ✅/⚠️/❌ |
| Visual | [description] | [description] | ✅/⚠️/❌ |
| Audience | [description] | [description] | ✅/⚠️/❌ |

MESSAGE MATCH SCORE: [X/5]

ISSUES IDENTIFIED:
- [Specific mismatch #1]: [Description of problem]
- [Specific mismatch #2]: [Description of problem]

RECOMMENDATIONS:
- [Specific fix #1]
- [Specific fix #2]

────────────────────────────────────────────────────────────────────

🎯 FIRST IMPRESSION ANALYSIS
────────────────────────────────────────────────────────────────────

5-SECOND TEST RESULTS:
- What you're offering: [Clear/Unclear]
- Why it matters: [Clear/Unclear]
- What to do next: [Clear/Unclear]

ABOVE-THE-FOLD ASSESSMENT:

| Element | Status | Notes |
|---------|--------|-------|
| Headline | [Assessment] | [Specific feedback] |
| Subheadline | [Assessment] | [Specific feedback] |
| Hero visual | [Assessment] | [Specific feedback] |
| Primary CTA | [Assessment] | [Specific feedback] |
| Value prop | [Assessment] | [Specific feedback] |

FIRST IMPRESSION SCORE: [X/10]

RECOMMENDATIONS:
- [Specific improvement #1]
- [Specific improvement #2]

────────────────────────────────────────────────────────────────────

⚡ PAGE SPEED ANALYSIS
────────────────────────────────────────────────────────────────────

CURRENT PERFORMANCE:

| Metric | Desktop | Mobile | Target |
|--------|---------|--------|--------|
| Load time | [X.Xs] | [X.Xs] | <3s |
| LCP | [X.Xs] | [X.Xs] | <2.5s |
| FID | [Xms] | [Xms] | <100ms |
| CLS | [X.XX] | [X.XX] | <0.1 |

SPEED SCORE: [X/15]

ISSUES IDENTIFIED:
- [Speed issue #1]: [Impact]
- [Speed issue #2]: [Impact]

RECOMMENDATIONS:
- [Technical fix #1]
- [Technical fix #2]

────────────────────────────────────────────────────────────────────

📱 MOBILE EXPERIENCE
────────────────────────────────────────────────────────────────────

MOBILE ASSESSMENT:

| Factor | Status | Notes |
|--------|--------|-------|
| Touch targets | ✅/❌ | [Details] |
| Text readability | ✅/❌ | [Details] |
| Form usability | ✅/❌ | [Details] |
| Load time | ✅/❌ | [Details] |
| Layout stability | ✅/❌ | [Details] |
| Thumb-friendly | ✅/❌ | [Details] |

MOBILE SCORE: [X/15]

CRITICAL MOBILE ISSUES:
- [Issue #1]
- [Issue #2]

────────────────────────────────────────────────────────────────────

🔄 CONVERSION PATH ANALYSIS
────────────────────────────────────────────────────────────────────

CURRENT FUNNEL:

[Visual representation of steps from ad click to conversion]

DROP-OFF ANALYSIS:

| Stage | Expected Rate | Notes |
|-------|---------------|-------|
| Bounce rate | [X%] | [Assessment] |
| Scroll depth | [X%] | [Assessment] |
| CTA click rate | [X%] | [Assessment] |
| Form start rate | [X%] | [Assessment] |
| Form completion | [X%] | [Assessment] |

CONVERSION PATH SCORE: [X/15]

FRICTION POINTS IDENTIFIED:
1. [Friction point #1]: [Impact and recommendation]
2. [Friction point #2]: [Impact and recommendation]

────────────────────────────────────────────────────────────────────

🛡️ TRUST ELEMENTS
────────────────────────────────────────────────────────────────────

TRUST INVENTORY:

| Element | Present | Placement | Effectiveness |
|---------|---------|-----------|---------------|
| Social proof | ✅/❌ | [Location] | [Rating] |
| Testimonials | ✅/❌ | [Location] | [Rating] |
| Client logos | ✅/❌ | [Location] | [Rating] |
| Security badges | ✅/❌ | [Location] | [Rating] |
| Guarantees | ✅/❌ | [Location] | [Rating] |
| Contact info | ✅/❌ | [Location] | [Rating] |

TRUST SCORE: [X/15]

TRUST GAPS:
- [Missing element #1]: [Recommendation]
- [Missing element #2]: [Recommendation]

────────────────────────────────────────────────────────────────────
```

---

### Action Plan

```
🎯 OPTIMIZATION ROADMAP
═══════════════════════════════════════════════════════════════════

IMMEDIATE FIXES (Do This Week)
Priority: P0 - Critical

1. [Fix #1]
   - Problem: [Description]
   - Solution: [Specific action]
   - Expected impact: [Metric improvement]

2. [Fix #2]
   - Problem: [Description]
   - Solution: [Specific action]
   - Expected impact: [Metric improvement]

────────────────────────────────────────────────────────────────────

SHORT-TERM IMPROVEMENTS (Next 2 Weeks)
Priority: P1 - Important

1. [Improvement #1]
   - Problem: [Description]
   - Solution: [Specific action]
   - Expected impact: [Metric improvement]

2. [Improvement #2]
   - Problem: [Description]
   - Solution: [Specific action]
   - Expected impact: [Metric improvement]

────────────────────────────────────────────────────────────────────

TESTING OPPORTUNITIES
Priority: P2 - Optimization

| Test | Hypothesis | Success Metric |
|------|------------|----------------|
| [Test 1] | [Hypothesis] | [Metric] |
| [Test 2] | [Hypothesis] | [Metric] |
| [Test 3] | [Hypothesis] | [Metric] |

════════════════════════════════════════════════════════════════════
```

---

## Common Scenarios

### Scenario 1: High CTR, Low Conversion Rate
**Diagnosis:** Message mismatch or page experience issue
**Check First:**
1. Does the page headline match the ad promise?
2. Is the offer visible above the fold?
3. Page load time on mobile?
4. Any technical errors preventing conversion?

### Scenario 2: High Bounce Rate from Ads
**Diagnosis:** First impression failure or speed issue
**Check First:**
1. 5-second test: Is value clear immediately?
2. Page load time (>3s = bounce)
3. Mobile experience (if traffic is mobile)
4. Visual continuity from ad to page

### Scenario 3: High Form Start, Low Completion
**Diagnosis:** Form friction
**Check First:**
1. Number of fields (too many?)
2. Required vs optional fields
3. Error messaging clarity
4. Mobile form usability
5. Any fields causing confusion

### Scenario 4: Good Metrics, But Revenue Low
**Diagnosis:** Lead quality or downstream issue
**Check First:**
1. Are you attracting the right audience?
2. Is qualification happening on the page?
3. Post-conversion experience (email, sales follow-up)
4. Pricing/offer alignment with expectations

---

## Limitations

**I can provide:**
- Message match analysis
- User experience assessment
- Speed and technical recommendations
- Conversion path optimization suggestions
- Trust and credibility audit
- Prioritized action plan

**I cannot provide:**
- Actual page speed testing (need tools like PageSpeed Insights)
- Heat map or session recording analysis (need Hotjar, Clarity, etc.)
- Statistical significance calculations for tests
- Design mockups or wireframes
- Code fixes or technical implementation

**For deeper analysis, also provide:**
- Analytics data (GA4, etc.)
- Heat maps or scroll maps
- Session recordings
- Form analytics
- A/B test history

---

## Quality Checklist

Before delivering audit:
- [ ] Message match scored with specific examples
- [ ] First impression evaluated with 5-second test
- [ ] Page speed assessed for mobile
- [ ] Mobile experience checked comprehensively
- [ ] Conversion path mapped with friction points
- [ ] Trust elements inventoried
- [ ] All issues prioritized by impact
- [ ] Specific, actionable recommendations provided
- [ ] Quick wins identified separately from larger projects
- [ ] Limitations of analysis clearly stated
