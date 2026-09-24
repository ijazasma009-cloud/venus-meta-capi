---
name: attribution-model-auditor
description: Audits attribution setups across platforms, identifies gaps, compares models, and recommends improvements. Triggers when user asks "is my attribution setup correct?", "why don't my platform numbers match?", or wants to understand measurement discrepancies. Provides actionable recommendations for better measurement.
---

# Attribution Model Auditor

If you can't measure it, you can't improve it. But are you measuring it right?

## Core Philosophy

**All attribution is wrong. Some is useful.** The goal isn't perfect measurement—it's consistent, directional decision-making.

**The Attribution Paradox:** The more sophisticated your marketing, the harder it is to attribute. Multi-touch journeys break simple models.

**The Three Truths of Attribution:**
1. **Platform data is biased:** Every platform claims credit for everything it can
2. **Last-click is lazy:** But it's consistent and actionable
3. **Perfect attribution doesn't exist:** Pick a model and optimize consistently

---

## Required Context

### Must Have

**1. Current Attribution Setup**
- Platforms running ads (Google, Meta, TikTok, etc.)
- Attribution windows by platform
- Conversion tracking method (pixel, CAPI, offline)

**2. Conversion Data**
- Reported conversions by platform
- Actual conversions (from CRM/backend)
- Discrepancy if known

**3. Business Model**
- Conversion type (purchase, lead, signup)
- Sales cycle length
- Online vs. offline conversion

### Strongly Recommended

**4. Technical Setup**
- Pixels/tags installed
- CAPI/server-side tracking status
- UTM parameter usage
- GA4 setup

**5. Cross-Platform Comparison**
- Same-period conversions by platform
- Total actual conversions
- Sum vs. actual (overlap indicator)

### Nice to Have

- Historical tracking changes
- iOS14+ impact observations
- Multi-touch path data
- CRM integration status

---

## Attribution Audit Framework

### Level 1: Technical Setup Audit

**Tracking Method Assessment:**

| Method | Reliability | iOS Resilience | Setup Complexity |
|--------|-------------|----------------|------------------|
| Platform Pixel (browser) | Medium | Low | Easy |
| Platform Pixel + CAPI | High | High | Medium |
| CAPI only | High | High | Complex |
| GA4 + Platform | Medium-High | Medium | Medium |
| Offline Import | High | High | Complex |

**Essential Tracking Checklist:**

| Element | Status | Impact if Missing |
|---------|--------|-------------------|
| Meta Pixel | Required | No Meta conversion tracking |
| Meta CAPI | Strongly Rec | 20-30% data loss on iOS |
| Google Ads Tag | Required | No Google conversion tracking |
| Google Enhanced Conversions | Strongly Rec | Better matching, especially email |
| GA4 | Strongly Rec | No cross-platform view |
| UTM Parameters | Required | Can't attribute in GA4 |
| Offline Import | For leads | CRM data not connected |

---

### Level 2: Attribution Window Analysis

**Platform Default Windows:**

| Platform | Default Click | Default View | Adjustable? |
|----------|---------------|--------------|-------------|
| Google Ads | 30 days | 1 day (display) | Yes |
| Meta Ads | 7 days | 1 day | Yes |
| TikTok | 28 days | 7 days | Yes |
| LinkedIn | 30 days | 7 days | Yes |
| Microsoft | 30 days | 1 day | Yes |

**Window Mismatch Issues:**

| Scenario | Problem | Solution |
|----------|---------|----------|
| Different windows across platforms | Unfair comparison | Standardize where possible |
| Window longer than sales cycle | Over-attribution | Shorten window |
| Window shorter than sales cycle | Under-attribution | Lengthen or use offline import |
| View-through counting | Inflated Meta/TikTok | Consider 7d click only |

---

### Level 3: Platform Comparison Analysis

**Sum vs. Actual Analysis:**

```
Platform A reported: 100 conversions
Platform B reported: 80 conversions
Platform C reported: 50 conversions
---------------------------------
Sum of platforms: 230 conversions
Actual (CRM): 150 conversions
---------------------------------
Overcounting: 53% ((230-150)/150)
```

**Overcounting Interpretation:**

| Overcounting % | Interpretation | Action |
|----------------|----------------|--------|
| <10% | Normal | Minor overlap |
| 10-30% | Moderate | Review attribution windows |
| 30-50% | High | Significant double-counting |
| >50% | Severe | Attribution fundamentally broken |

---

### Level 4: Model Comparison

**Attribution Models Explained:**

| Model | Credit Allocation | Best For | Limitation |
|-------|-------------------|----------|------------|
| Last Click | 100% to last ad clicked | Direct response | Ignores awareness |
| First Click | 100% to first ad clicked | Brand campaigns | Ignores conversion |
| Linear | Equal across touchpoints | Balanced view | May overvalue low-impact |
| Time Decay | More to recent touches | Long sales cycles | Complex to action |
| Position-Based | 40% first, 40% last, 20% middle | Balanced | Arbitrary weights |
| Data-Driven | ML-weighted | Mature accounts | Needs volume |

**Model Selection Framework:**

| Business Type | Sales Cycle | Recommended Model |
|---------------|-------------|-------------------|
| E-commerce DTC | Short (<7 days) | Last Click or 7-day window |
| SaaS B2C | Medium (7-30 days) | 30-day click, position-based |
| B2B Lead Gen | Long (30-90+ days) | First Click + Offline import |
| Brand campaigns | N/A | Multi-touch or MMM |

---

### Level 5: Data Loss Assessment

**iOS 14+ Impact Checklist:**

| Factor | Pre-iOS 14 | Post-iOS 14 | Mitigation |
|--------|------------|-------------|------------|
| Meta tracking | ~95% | 70-80% | CAPI required |
| TikTok tracking | ~90% | 65-75% | CAPI required |
| Google tracking | ~90% | 85-90% | Enhanced Conversions |
| Cross-device | Good | Degraded | Customer data matching |

**CAPI Implementation Check:**

| Platform | CAPI Available? | Event Match Quality | Status |
|----------|-----------------|---------------------|--------|
| Meta | Yes | [X]% | [Good/Poor] |
| TikTok | Yes | [X]% | [Good/Poor] |
| Google | Enhanced Conv. | [Match rate] | [Good/Poor] |
| LinkedIn | Limited | N/A | [Status] |

---

### Level 6: Measurement Framework Recommendation

**Framework Levels:**

| Level | Components | Best For | Complexity |
|-------|------------|----------|------------|
| Basic | Platform pixels + UTMs + GA4 | Small spend (<$10K/mo) | Low |
| Intermediate | + CAPI + CRM integration | Medium spend ($10-100K/mo) | Medium |
| Advanced | + Offline import + data warehouse | Large spend ($100K+/mo) | High |
| Sophisticated | + MMM + Incrementality testing | Enterprise | Very High |

---

## Output Format

### Attribution Audit Report

```
═══════════════════════════════════════════════════════════════
ATTRIBUTION MODEL AUDIT
Platforms Audited: [Platforms]
Analysis Period: [Date Range]
Overall Attribution Health: [GOOD/NEEDS WORK/CRITICAL]
═══════════════════════════════════════════════════════════════
```

---

### Executive Summary

**Current Setup Assessment:**

| Area | Status | Priority |
|------|--------|----------|
| Technical Tracking | [Good/Fair/Poor] | [High/Med/Low] |
| Attribution Windows | [Aligned/Misaligned] | [High/Med/Low] |
| Cross-Platform Consistency | [Good/Fair/Poor] | [High/Med/Low] |
| Data Loss Mitigation | [Good/Fair/Poor] | [High/Med/Low] |

**Top Issues:**
1. [Issue] - [Impact]
2. [Issue] - [Impact]
3. [Issue] - [Impact]

**Recommended Actions:**
1. [Action] - [Expected improvement]
2. [Action] - [Expected improvement]
3. [Action] - [Expected improvement]

---

### Technical Setup Audit

**Tracking Coverage:**

| Platform | Pixel | CAPI/Enhanced | Offline Import | Status |
|----------|-------|---------------|----------------|--------|
| Google Ads | [Y/N] | [Y/N] | [Y/N] | [Status] |
| Meta | [Y/N] | [Y/N] | [Y/N] | [Status] |
| TikTok | [Y/N] | [Y/N] | [Y/N] | [Status] |
| LinkedIn | [Y/N] | [Limited] | [Y/N] | [Status] |

**GA4 Integration:**
- Connected: [Y/N]
- UTM tracking: [Consistent/Inconsistent]
- Cross-platform view: [Available/Not available]

**Issues Identified:**

| Issue | Impact | Priority | Fix |
|-------|--------|----------|-----|
| [Issue] | [Impact] | [Priority] | [Fix] |

---

### Attribution Window Analysis

**Current Windows:**

| Platform | Click Window | View Window | Assessment |
|----------|--------------|-------------|------------|
| Google | [X] days | [X] days | [Assessment] |
| Meta | [X] days | [X] days | [Assessment] |
| TikTok | [X] days | [X] days | [Assessment] |
| LinkedIn | [X] days | [X] days | [Assessment] |

**Sales Cycle Alignment:**
- Your sales cycle: [X] days
- Longest window: [X] days
- Shortest window: [X] days
- Assessment: [Aligned/Misaligned]

**Window Recommendations:**

| Platform | Current | Recommended | Rationale |
|----------|---------|-------------|-----------|
| [Platform] | [Current] | [Recommended] | [Why] |

---

### Cross-Platform Analysis

**Conversion Comparison:**

| Platform | Reported Conversions | % of Total Reported |
|----------|---------------------|---------------------|
| Google | [X] | [X]% |
| Meta | [X] | [X]% |
| TikTok | [X] | [X]% |
| LinkedIn | [X] | [X]% |
| **Total Reported** | [X] | - |
| **Actual (CRM)** | [X] | - |
| **Overcounting** | [X] | [X]% |

**Analysis:**
[Interpretation of overcounting and what it means]

**Overlap Sources:**
1. [Source of overlap]
2. [Source of overlap]

---

### Data Loss Assessment

**Estimated Data Loss:**

| Platform | Pre-iOS14 Accuracy | Current Accuracy | Gap |
|----------|-------------------|------------------|-----|
| Meta | ~95% | [X]% | [X]% |
| TikTok | ~90% | [X]% | [X]% |
| Google | ~90% | [X]% | [X]% |

**CAPI/Enhanced Conversion Status:**

| Platform | Implementation | Event Match Quality | Assessment |
|----------|----------------|---------------------|------------|
| Meta | [Status] | [X]% | [Good/Poor] |
| Google | [Status] | [Match rate] | [Good/Poor] |
| TikTok | [Status] | [X]% | [Good/Poor] |

**Data Recovery Recommendations:**
1. [Recommendation]
2. [Recommendation]

---

### Model Recommendation

**Current Model:** [Model]

**Recommended Model:** [Model]

**Rationale:**
- Your business type: [Type]
- Your sales cycle: [Length]
- Your main goal: [Goal]
- [Why recommended model fits]

**Implementation Notes:**
- [Note 1]
- [Note 2]

---

### Discrepancy Resolution

**Why Numbers Don't Match:**

| Discrepancy | Cause | Resolution |
|-------------|-------|------------|
| Platform A > CRM | [Cause] | [Resolution] |
| Platform B < Platform A | [Cause] | [Resolution] |
| Sum > Actual | [Cause] | [Resolution] |

**Establishing Source of Truth:**

Recommended hierarchy:
1. [Primary source] - Why
2. [Secondary source] - Why
3. [Platform data] - Use for optimization only

---

### Action Plan

**Immediate (This Week):**
1. [ ] [Technical fix]
2. [ ] [Configuration change]

**Short-Term (Next 2-4 Weeks):**
1. [ ] [Implementation]
2. [ ] [Integration]

**Medium-Term (Next 1-3 Months):**
1. [ ] [Advanced setup]
2. [ ] [Testing/validation]

---

### Monitoring Framework

**Weekly Checks:**
- [ ] Platform vs. CRM conversion delta
- [ ] Event Match Quality (Meta CAPI)
- [ ] GA4 cross-platform view

**Monthly Checks:**
- [ ] Attribution window performance review
- [ ] Overcounting trend
- [ ] Data loss assessment

**Red Flags:**
- Overcounting increases >10% month-over-month
- Event Match Quality drops below 70%
- Platform data diverges >50% from CRM

---

## Common Attribution Problems

### Problem 1: Platforms Sum to 2x Actual
**Cause:** View-through attribution, long windows, multi-platform journeys
**Solution:**
- Standardize to click-only attribution for comparison
- Shorten windows to match sales cycle
- Accept overlap and use platform data for platform optimization only

### Problem 2: Meta Shows 50% Fewer Conversions Than Before
**Cause:** iOS 14 privacy changes, lack of CAPI
**Solution:**
- Implement CAPI with Conversions API Gateway or direct integration
- Use Aggregated Event Measurement properly
- Consider Conversion Lift studies for validation

### Problem 3: Can't Compare Platforms Fairly
**Cause:** Different windows, different models, different tracking
**Solution:**
- Standardize windows (e.g., all 7-day click)
- Use GA4 as neutral source
- Focus on incrementality, not attribution

### Problem 4: CRM Shows Leads, Platforms Show Purchases
**Cause:** Different conversion events tracked
**Solution:**
- Audit conversion events across platforms
- Ensure same event is tracked everywhere
- Set up offline import for lead-to-customer tracking

---

## Limitations

**I can provide:**
- Attribution setup audit
- Window recommendations
- Technical gap identification
- Framework recommendations

**I cannot provide:**
- Pixel implementation code
- CAPI setup instructions
- MMM modeling
- Incrementality test design

**For better audits, provide:**
- Actual conversion counts from CRM
- Platform-reported conversions for same period
- Current technical setup details
- Sales cycle information

---

## Quality Checklist

Before delivering audit:
- [ ] All platforms assessed
- [ ] Windows compared across platforms
- [ ] Overcounting calculated
- [ ] Data loss estimated
- [ ] Technical gaps identified
- [ ] Model recommendation matches business
- [ ] Action plan is prioritized
- [ ] Source of truth established
