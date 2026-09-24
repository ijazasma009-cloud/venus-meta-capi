---
name: funnel-dropoff-diagnostician
description: Diagnoses conversion funnel drop-offs and identifies their causes. Triggers when user shares funnel data, asks "where am I losing people?", or wants to improve conversion rates. Analyzes step-by-step conversion data, identifies problematic transitions, diagnoses likely causes, and provides prioritized recommendations for improvement.
---

# Funnel Drop-off Diagnostician

Find the leaks in your funnel and plug them.

## Core Philosophy

**Not all drop-offs are created equal.** A 50% drop-off at one stage might be healthy, while 20% at another could be catastrophic. Context and benchmarks matter.

**The Goal:** Identify which funnel leaks cost you the most and what's causing them.

**The Principle:** Systematic diagnosis—measure the drop, assess against benchmarks, hypothesize causes, prioritize by impact.

---

## Required Context

### Must Have

**1. Funnel Data**
For each step:
- Step name/description
- Users/sessions entering step
- Users/sessions completing step
- Conversion rate to next step (or calculate from above)

**2. Funnel Type**
What kind of funnel:
- E-commerce (browse → cart → checkout → purchase)
- SaaS signup (landing → signup → activation → paid)
- Lead gen (landing → form → submit → qualified)
- Content (view → engage → subscribe → convert)

### Strongly Recommended

**3. Segmentation Data**
- Device breakdown (mobile vs. desktop)
- Traffic source breakdown
- New vs. returning visitors
- Geographic breakdown

**4. Time Context**
- Time period of data
- Any recent changes (design, flow, offers)
- Seasonality considerations

### Nice to Have

- Historical comparison (vs. last period)
- Industry benchmarks
- Heatmaps or session recordings
- User feedback or surveys
- Exit page data
- Error logs

---

## Diagnostic Framework

### Step 1: Funnel Mapping

**Standard Funnel Visualization:**

```
STEP 1: [Name]
  │ Users: X,XXX
  │
  ▼ ──────────────────────────── XX% conversion rate
  │ DROP-OFF: X,XXX (XX%)
  │
STEP 2: [Name]
  │ Users: X,XXX
  │
  ▼ ──────────────────────────── XX% conversion rate
  │ DROP-OFF: X,XXX (XX%)
  │
STEP 3: [Name]
  │ Users: X,XXX
  │
  ▼ ──────────────────────────── XX% conversion rate
  │ DROP-OFF: X,XXX (XX%)
  │
STEP 4: [Name] (Goal)
  │ Users: X,XXX

TOTAL FUNNEL CONVERSION: XX%
```

---

### Step 2: Benchmark Assessment

**E-commerce Funnel Benchmarks:**

| Transition | Poor | Average | Good | Excellent |
|------------|------|---------|------|-----------|
| Visit → Product View | <30% | 30-50% | 50-70% | >70% |
| Product View → Add to Cart | <5% | 5-10% | 10-15% | >15% |
| Add to Cart → Checkout Start | <30% | 30-50% | 50-65% | >65% |
| Checkout Start → Purchase | <30% | 30-50% | 50-70% | >70% |
| **Overall: Visit → Purchase** | <1% | 1-2% | 2-4% | >4% |

**SaaS Signup Funnel Benchmarks:**

| Transition | Poor | Average | Good | Excellent |
|------------|------|---------|------|-----------|
| Landing → Signup Start | <5% | 5-15% | 15-25% | >25% |
| Signup Start → Signup Complete | <50% | 50-70% | 70-85% | >85% |
| Signup → Activation | <20% | 20-40% | 40-60% | >60% |
| Free → Paid | <2% | 2-5% | 5-10% | >10% |

**Lead Gen Funnel Benchmarks:**

| Transition | Poor | Average | Good | Excellent |
|------------|------|---------|------|-----------|
| Landing → Form Start | <10% | 10-20% | 20-35% | >35% |
| Form Start → Form Submit | <20% | 20-40% | 40-60% | >60% |
| Submit → Qualified Lead | <30% | 30-50% | 50-70% | >70% |

---

### Step 3: Drop-off Severity Analysis

**Impact Scoring Formula:**

```
Impact Score = (Drop-off Volume) × (Revenue Value) × (Fixability)

Where:
- Drop-off Volume = Users lost at step
- Revenue Value = Estimated value per conversion
- Fixability = How likely a fix will improve (1-3)
```

**Severity Classification:**

| Drop-off Rate | vs. Benchmark | Severity |
|---------------|---------------|----------|
| >2x benchmark | Critical | 🔴 Fix immediately |
| 1.5-2x benchmark | High | 🟠 Fix soon |
| 1-1.5x benchmark | Moderate | 🟡 Optimize |
| At/below benchmark | Normal | 🟢 Monitor |

---

### Step 4: Cause Diagnosis

**Common Drop-off Causes by Funnel Stage:**

**Landing/Entry Stage:**
| Symptom | Likely Cause | Evidence to Check |
|---------|--------------|-------------------|
| High bounce rate | Message mismatch | Compare ad to page |
| Immediate exits | Slow load time | Page speed data |
| No scroll | Weak headline/hook | Scroll depth data |
| Quick exits | Wrong audience | Traffic source quality |

**Consideration Stage (Product/Form):**
| Symptom | Likely Cause | Evidence to Check |
|---------|--------------|-------------------|
| View but no action | Value unclear | Page content |
| Partial engagement | Too much friction | Form fields, steps |
| Mobile-specific drop | Mobile UX issues | Device breakdown |
| Price page exit | Pricing concern | Exit page data |

**Conversion Stage (Cart/Checkout):**
| Symptom | Likely Cause | Evidence to Check |
|---------|--------------|-------------------|
| Cart abandonment | Unexpected costs | Shipping, taxes |
| Checkout drop | Form complexity | Field count |
| Payment step exit | Trust issues | Security signals |
| Account required | Friction | Guest checkout option |

**Post-Conversion Stage:**
| Symptom | Likely Cause | Evidence to Check |
|---------|--------------|-------------------|
| Low activation | Unclear next step | Onboarding flow |
| Early churn | Value not realized | Time to value |
| No upgrade | Upgrade path unclear | Pricing/packaging |

---

### Step 5: Segment Analysis

**Device-Based Drop-off:**

| Step | Desktop Conv | Mobile Conv | Gap | Issue? |
|------|--------------|-------------|-----|--------|
| Step 1→2 | XX% | XX% | X% | Y/N |
| Step 2→3 | XX% | XX% | X% | Y/N |
| Step 3→4 | XX% | XX% | X% | Y/N |

*>5% gap indicates mobile-specific issue*

**Traffic Source Drop-off:**

| Step | Paid Search | Organic | Social | Email |
|------|-------------|---------|--------|-------|
| Step 1→2 | XX% | XX% | XX% | XX% |
| Step 2→3 | XX% | XX% | XX% | XX% |
| Step 3→4 | XX% | XX% | XX% | XX% |

*Significant variance indicates source-specific issues*

---

## Output Format

### Executive Summary

```
FUNNEL HEALTH SCORE: XX/100 [GRADE]

Funnel Type: [E-commerce/SaaS/Lead Gen/etc.]
Period: [Date Range]
Total Users Entering: X,XXX
Total Conversions: XXX
Overall Conversion Rate: X.XX%

BIGGEST LEAK: [Step transition] - $X,XXX revenue impact
ROOT CAUSE: [Primary diagnosis]
PRIORITY FIX: [Recommended action]
```

**Grade Scale:**

| Score | Grade | Assessment |
|-------|-------|------------|
| 85-100 | A | Optimized funnel, minor improvements |
| 70-84 | B | Healthy funnel, clear opportunities |
| 55-69 | C | Significant leaks costing revenue |
| 40-54 | D | Major problems in multiple stages |
| <40 | F | Broken funnel, urgent fixes needed |

---

### Funnel Visualization

```
FUNNEL ANALYSIS: [Funnel Name]

┌─────────────────────────────────────────────────────────────┐
│ STEP 1: [Name]                                    100% │████████████████████│
│ Users: 10,000                                              │
├─────────────────────────────────────────────────────────────┤
│ ↓ TRANSITION: XX% conversion | XX% drop-off                │
│   vs. Benchmark: [Above/At/Below] [🟢/🟡/🔴]               │
├─────────────────────────────────────────────────────────────┤
│ STEP 2: [Name]                                     XX% │███████████████     │
│ Users: X,XXX                                               │
├─────────────────────────────────────────────────────────────┤
│ ↓ TRANSITION: XX% conversion | XX% drop-off                │
│   vs. Benchmark: [Above/At/Below] [🟢/🟡/🔴]               │
├─────────────────────────────────────────────────────────────┤
│ STEP 3: [Name]                                     XX% │██████████          │
│ Users: X,XXX                                               │
├─────────────────────────────────────────────────────────────┤
│ ↓ TRANSITION: XX% conversion | XX% drop-off   ⚠️ CRITICAL  │
│   vs. Benchmark: [Below] [🔴]                              │
├─────────────────────────────────────────────────────────────┤
│ STEP 4: [Name] (Goal)                              XX% │████                │
│ Users: XXX                                                 │
└─────────────────────────────────────────────────────────────┘
```

---

### Drop-off Analysis by Step

**Step [X] → Step [Y]: [XX]% Conversion / [XX]% Drop-off**

| Metric | Value | Benchmark | Status |
|--------|-------|-----------|--------|
| Conversion Rate | XX% | XX-XX% | 🟢/🟡/🔴 |
| Users Lost | X,XXX | — | — |
| Revenue Impact | $X,XXX | — | — |

**Diagnosis:**

| Possible Cause | Likelihood | Evidence |
|----------------|------------|----------|
| [Cause 1] | High/Med/Low | [What suggests this] |
| [Cause 2] | High/Med/Low | [What suggests this] |
| [Cause 3] | High/Med/Low | [What suggests this] |

**Segment Analysis:**

| Segment | Conversion | vs. Average | Issue? |
|---------|------------|-------------|--------|
| Desktop | XX% | +X% | — |
| Mobile | XX% | -X% | ⚠️ Yes |
| Paid Traffic | XX% | -X% | ⚠️ Yes |
| Organic Traffic | XX% | +X% | — |

**Primary Hypothesis:**
> [Most likely cause based on evidence]

**Recommended Fix:**
> [Specific action to address this drop-off]

---

### Priority Matrix

```
                        HIGH IMPACT
                            │
     ┌──────────────────────┼──────────────────────┐
     │                      │                      │
     │   DO FIRST           │   DO SECOND          │
     │   [Fix 1]            │   [Fix 3]            │
     │   [Fix 2]            │                      │
     │                      │                      │
─────┼──────────────────────┼──────────────────────┼─────
LOW  │                      │                      │  HIGH
EFFORT│   DO LATER          │   CONSIDER           │EFFORT
     │   [Fix 5]            │   [Fix 4]            │
     │                      │                      │
     │                      │                      │
     └──────────────────────┼──────────────────────┘
                            │
                        LOW IMPACT
```

---

### Prioritized Fix List

**Fix 1: [Title] — CRITICAL**
- **Step:** [Which transition]
- **Current:** [Current conversion rate]
- **Target:** [Target conversion rate]
- **Impact:** $X,XXX/month additional revenue
- **Cause:** [Diagnosed cause]
- **Solution:** [Specific recommendation]
- **Effort:** Low/Medium/High
- **Timeline:** [When to implement]

---

**Fix 2: [Title] — HIGH PRIORITY**

[Same format]

---

### Segment-Specific Recommendations

**Mobile-Specific Issues:**

| Issue | Impact | Recommendation |
|-------|--------|----------------|
| [Issue 1] | $X,XXX | [Fix] |
| [Issue 2] | $X,XXX | [Fix] |

**Traffic Source Issues:**

| Source | Issue | Recommendation |
|--------|-------|----------------|
| [Source 1] | [Issue] | [Fix] |
| [Source 2] | [Issue] | [Fix] |

---

### Monitoring Dashboard

**Key Metrics to Track:**

| Metric | Current | Target | Tracking Frequency |
|--------|---------|--------|-------------------|
| Step 1→2 Conversion | XX% | XX% | Weekly |
| Step 2→3 Conversion | XX% | XX% | Weekly |
| Step 3→4 Conversion | XX% | XX% | Weekly |
| Overall Funnel Conversion | X.X% | X.X% | Weekly |
| Mobile vs Desktop Gap | X% | <X% | Weekly |

**Alert Thresholds:**

| Metric | Warning | Critical |
|--------|---------|----------|
| [Step] Conversion | <XX% | <XX% |
| Mobile Conversion | <XX% | <XX% |
| Overall Conversion | <X.X% | <X.X% |

---

### A/B Test Recommendations

| Test | Hypothesis | Step Affected | Expected Lift |
|------|------------|---------------|---------------|
| [Test 1] | If [change], then [outcome] because [reason] | Step X→Y | +X-X% |
| [Test 2] | If [change], then [outcome] because [reason] | Step X→Y | +X-X% |
| [Test 3] | If [change], then [outcome] because [reason] | Step X→Y | +X-X% |

**Test Priority:**
1. [Test name] — Highest impact, lowest risk
2. [Test name] — Good potential, moderate effort
3. [Test name] — Worth testing after validating basics

---

## Common Funnel Fixes Reference

### Landing/Entry Fixes

| Problem | Solution |
|---------|----------|
| High bounce rate | Improve message match, speed |
| Low engagement | Stronger headline, clearer CTA |
| Mobile bounce | Mobile-first redesign |
| Source-specific bounce | Source-specific landing pages |

### Consideration Fixes

| Problem | Solution |
|---------|----------|
| Low product views | Better navigation, recommendations |
| Low form starts | Reduce perceived effort, add value |
| Price page exits | Address value before price |
| Comparison shopping | Competitive positioning |

### Conversion Fixes

| Problem | Solution |
|---------|----------|
| Cart abandonment | Show costs upfront, exit intent |
| Checkout drop-off | Reduce fields, progress indicator |
| Payment failures | Multiple payment options |
| Account friction | Guest checkout, social login |

### Activation Fixes

| Problem | Solution |
|---------|----------|
| Low activation | Better onboarding, quick win |
| Early churn | Value demonstration, support |
| No upgrade | Clearer upgrade path, triggers |

---

## Limitations

**I can analyze:**
- Funnel conversion data
- Drop-off patterns
- Segment comparisons
- Benchmark comparisons
- Cause hypotheses
- Fix prioritization

**I cannot provide:**
- Root cause certainty (hypotheses only)
- Technical implementation
- User behavior explanations (need recordings)
- Statistical significance (need sample sizes)
- Real-time monitoring

**For complete diagnosis, also use:**
- Session recordings (Hotjar, FullStory)
- Heatmaps and scroll maps
- User surveys and feedback
- A/B testing platform
- Technical error logs

---

## Quality Checklist

Before delivering diagnosis:
- [ ] All funnel steps mapped with data
- [ ] Each transition benchmarked
- [ ] Segment analysis completed
- [ ] Drop-offs prioritized by impact
- [ ] Causes hypothesized with evidence
- [ ] Fixes are specific and actionable
- [ ] A/B test ideas provided
- [ ] Monitoring recommendations included
- [ ] Limitations acknowledged
