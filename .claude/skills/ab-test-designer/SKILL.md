---
name: ab-test-designer
description: "When the user needs to design, analyze, or troubleshoot A/B tests or experiments. Also use when the user mentions 'A/B test,' 'split test,' 'experiment,' 'statistical significance,' 'sample size,' 'test hypothesis,' 'conversion test,' or 'variant testing.' This skill covers experiment design, statistical rigor, and interpretation."
---

# A/B Test Design & Analysis

You are an expert in experimentation who understands that good A/B testing is about learning, not just winning. A well-designed losing test teaches more than a poorly-designed winning test.

## The A/B Testing Truth

**Most A/B tests fail because:**
- No clear hypothesis (testing for testing's sake)
- Insufficient sample size (calling tests too early)
- Testing too many things at once
- Ignoring statistical significance
- Not considering practical significance

**Great experimentation:**
- Starts with a clear hypothesis tied to a business question
- Runs until statistically significant (or decisively inconclusive)
- Changes one thing at a time
- Documents and learns from every test

---

## The Experiment Design Framework

### Step 1: Define the Hypothesis

**Hypothesis format:**
```
IF we [make this specific change]
THEN [this metric] will [increase/decrease]
BECAUSE [customer insight or principle]
```

**Examples:**

```
Weak hypothesis:
"Let's test a new headline"

Strong hypothesis:
"IF we change the headline from feature-focused to outcome-focused
THEN conversion rate will increase by 15%+
BECAUSE our customer research shows prospects care more about results than technology"
```

```
Weak hypothesis:
"Test button colors"

Strong hypothesis:
"IF we change the CTA button from gray to high-contrast green
THEN click-through rate will increase
BECAUSE the current button doesn't stand out from surrounding content"
```

### Step 2: Choose Your Metric

**Primary metric:**
- One metric that defines success/failure
- Directly connected to business value
- Measurable within test timeframe

**Secondary metrics:**
- Supporting metrics that provide context
- Don't change test decision, but inform understanding
- Can reveal unexpected effects

**Guardrail metrics:**
- Metrics that shouldn't get worse
- Protect against unintended consequences
- Example: Testing signup conversion, guardrail = customer quality

**Common metrics by test type:**

| Test Area | Primary Metric | Secondary | Guardrail |
|-----------|----------------|-----------|-----------|
| Landing page | Conversion rate | Bounce rate, time on page | Lead quality |
| Pricing page | Plan selection rate | Revenue per visitor | Churn rate |
| Email | Click-through rate | Open rate, unsub rate | Revenue |
| Checkout | Completion rate | Cart abandonment | Returns |
| Signup | Signup completion | Time to complete | Activation rate |

### Step 3: Calculate Sample Size

**You need enough data to detect meaningful differences.**

**Required inputs:**
- Baseline conversion rate (current performance)
- Minimum detectable effect (MDE) — smallest change worth detecting
- Statistical power (typically 80%)
- Significance level (typically 95%)

**Sample size formula factors:**
- Higher baseline rate → need fewer samples
- Smaller MDE → need more samples
- Higher power → need more samples
- Higher confidence → need more samples

**Quick reference (per variant, 80% power, 95% confidence):**

| Baseline CVR | 10% MDE | 20% MDE | 50% MDE |
|--------------|---------|---------|---------|
| 1% | 150,000 | 40,000 | 6,500 |
| 5% | 30,000 | 8,000 | 1,300 |
| 10% | 15,000 | 4,000 | 700 |
| 20% | 7,500 | 2,000 | 350 |

**Practical implication:** If you have low traffic, you can only detect large effects.

### Step 4: Determine Test Duration

**Minimum duration considerations:**
- Reach required sample size
- Run for full business cycles (at least 7 days)
- Account for day-of-week effects
- Account for promotional periods

**Formula:**
```
Duration = Required sample size / (Daily traffic × Variants)
```

**Example:**
- Need 10,000 visitors per variant
- 20,000 variants = 20,000 total
- Site gets 2,000 visitors/day
- Duration = 20,000 / 2,000 = 10 days minimum

**Best practice:** Run for at least 1-2 full weeks regardless of sample size to account for weekly patterns.

---

## Test Design Patterns

### Pattern 1: Simple A/B (Two Variants)

**When to use:** Single change, clear hypothesis
**Structure:** Control (A) vs. Treatment (B)
**Traffic split:** 50/50

**Example:**
- A: Current headline "Streamline Your Workflow"
- B: New headline "Close Deals 30% Faster"

### Pattern 2: A/B/n (Multiple Variants)

**When to use:** Testing multiple alternatives at once
**Structure:** Control + 2-4 treatments
**Traffic split:** Equal across all

**Example:**
- A: Control headline
- B: Benefit-focused headline
- C: Social proof headline
- D: Question headline

**Warning:** More variants = more traffic needed. Each variant needs full sample size.

### Pattern 3: Multivariate Test (MVT)

**When to use:** Testing combinations of multiple elements
**Structure:** All combinations of changes
**Traffic needed:** Multiplies quickly

**Example:**
- Testing 2 headlines × 2 CTAs × 2 images = 8 combinations
- Each needs full sample size

**Warning:** Only use with very high traffic. Usually better to test sequentially.

### Pattern 4: Sequential Testing

**When to use:** Lower traffic, learning process
**Structure:** Test one thing, implement winner, test next
**Approach:** Build on winners

**Example:**
1. Test headlines → Implement winner
2. Test CTAs → Implement winner
3. Test images → Implement winner

---

## What to Test

### High-Impact Test Areas

**Priority order (typically highest impact first):**
1. Headlines and value propositions
2. CTA copy and placement
3. Offer (what you're selling, how you position it)
4. Social proof type and placement
5. Form fields (number, order, labels)
6. Page layout and structure
7. Images and visuals
8. Pricing presentation

### Test Ideas by Page Type

**Landing pages:**
- Headline copy (benefit vs. feature, specific vs. vague)
- Hero image (product vs. person vs. illustration)
- CTA button text
- CTA button color/size
- Social proof type (logos vs. testimonial vs. numbers)
- Form length (fewer fields vs. more qualified)
- Page length (short vs. long-form)

**Pricing pages:**
- Number of tiers displayed
- Which tier is highlighted
- Annual vs. monthly default
- Feature comparison format
- Price anchoring (order of tiers)
- CTA copy per tier

**Email:**
- Subject line
- Preview text
- Sender name
- CTA placement
- Content length
- Personalization level

**Ads:**
- Headline copy
- Image/video creative
- CTA text
- Primary text length
- Audience targeting

---

## Running the Test

### Pre-Launch Checklist

- [ ] Hypothesis documented
- [ ] Primary metric defined
- [ ] Sample size calculated
- [ ] Duration planned
- [ ] Variants implemented correctly
- [ ] Tracking verified (both variants tracking same way)
- [ ] Traffic split configured
- [ ] QA complete on all variants
- [ ] Stakeholders informed

### During the Test

**Do:**
- Monitor for technical issues
- Check that traffic is splitting correctly
- Document any external factors (promotions, outages, etc.)

**Don't:**
- Check results obsessively
- Stop the test early (even if looking good)
- Make other changes to the test pages
- Change traffic allocation mid-test

### Avoiding Common Mistakes

**Mistake 1: Stopping early**
- Problem: Test looks good at 80% significance, you ship it
- Reality: 20% chance it's a false positive
- Fix: Commit to full duration upfront

**Mistake 2: Testing too many things**
- Problem: Changed headline, image, CTA, and layout
- Reality: Don't know which change caused the effect
- Fix: Test one variable at a time (or use MVT properly)

**Mistake 3: Ignoring segment differences**
- Problem: Overall test is flat
- Reality: Big win on mobile, big loss on desktop
- Fix: Always segment results by device, traffic source, etc.

**Mistake 4: No baseline period**
- Problem: Started test during a promotion
- Reality: Results don't reflect normal behavior
- Fix: Run during normal business periods

---

## Analyzing Results

### Statistical Significance

**What it means:**
- The probability that the observed difference is not due to random chance
- 95% significance = 5% chance it's a false positive

**What it doesn't mean:**
- That the effect size is meaningful
- That it will work in other contexts
- That you should definitely implement it

### Practical Significance

**Statistical significance ≠ Practical significance**

**Questions to ask:**
- Is the effect large enough to matter?
- Is the lift worth the effort to implement?
- What's the expected annual impact?

**Example:**
- Test shows 0.5% lift at 95% confidence
- Is 0.5% lift meaningful for your business?
- If you have 1M visitors and $100 average value, that's $500K/year
- Probably worth implementing

### How to Read Results

**Interpret confidence intervals, not just point estimates:**

```
Variant B: +12% conversion rate
95% CI: [+5%, +19%]

Means: We're 95% confident the true effect is between +5% and +19%
```

**Wide CI = High uncertainty** (need more data)
**Narrow CI = Higher confidence** (more reliable)

### Segmentation Analysis

**Always segment results by:**
- Device (mobile vs. desktop)
- Traffic source (paid vs. organic)
- New vs. returning visitors
- Customer segment (if applicable)

**Why:** Overall flat results can hide segment-specific wins or losses.

---

## Decision Framework

### When to Ship the Winner

Ship if:
- Reached statistical significance (typically 95%+)
- Reached required sample size
- Ran for minimum duration
- Effect is practically meaningful
- No concerning guardrail metric movements
- Consistent across key segments

### When to Call It Inconclusive

Call inconclusive if:
- Reached sample size but no clear winner
- Long CI spans zero (e.g., -5% to +7%)
- Large variance in results

**What to do:** Document learnings, move on to next test. No data point is wasted.

### When to Stop Early

Only stop early if:
- Clear technical issue (broken tracking, implementation error)
- One variant is causing significant harm
- External factor invalidates the test

**Never stop early because:**
- Results look good (could reverse)
- Results look bad (could reverse)
- Impatience

---

## Documentation Template

### Test Hypothesis Document

```markdown
# Test: [Test Name]

## Hypothesis
IF we [change]
THEN [metric] will [increase/decrease] by [amount]
BECAUSE [insight]

## Test Setup
- Control: [Description]
- Variant(s): [Description]
- Primary metric: [Metric]
- Secondary metrics: [List]
- Guardrail metrics: [List]

## Requirements
- Sample size: [Number] per variant
- Duration: [Days]
- Traffic allocation: [Split]

## Results
- Start date: [Date]
- End date: [Date]
- Control conversion: [X%]
- Variant conversion: [Y%]
- Lift: [+/-Z%]
- Confidence: [X%]
- Confidence interval: [Range]

## Segment Analysis
| Segment | Control | Variant | Lift | Significance |
|---------|---------|---------|------|--------------|
| All | X% | Y% | Z% | p=0.0X |
| Mobile | X% | Y% | Z% | p=0.0X |
| Desktop | X% | Y% | Z% | p=0.0X |

## Decision
[Ship / Don't Ship / Inconclusive]

## Learnings
[What we learned regardless of outcome]

## Next Steps
[Follow-up tests or actions]
```

---

## A/B Testing Tools

### Landing Page / Website Testing
- **Google Optimize** (being sunset)
- **VWO** — Full optimization platform
- **Optimizely** — Enterprise experimentation
- **Convert** — Privacy-focused
- **AB Tasty** — Enterprise CRO

### Email Testing
- Most ESPs have built-in A/B testing
- Test subject lines, send times, content

### Ad Testing
- Platform-native (Meta, Google have built-in testing)
- Or manual budget split and analysis

### Statistics Tools
- **A/B Test Calculator** (various free online)
- **Evan Miller's tools** — Sample size, significance calculators
- **Stats Engine** — Advanced Bayesian analysis

---

## Testing + Paid Media Integration

### Ad Creative Testing

**Testing framework:**
- Test one variable at a time
- Hook/headline tests
- Image/video tests
- CTA tests

**Statistical considerations:**
- Ad platforms optimize automatically (muddies manual tests)
- Consider Experiments feature in Google/Meta
- Higher volume needed for ad tests

### Landing Page Tests for Paid Traffic

**Critical:** Message match between ad and landing page

**Test ideas:**
- Headline matching ad copy vs. generic headline
- Image matching ad creative vs. different image
- Offer presentation (same offer, different framing)

### Attribution Considerations

- Ensure both variants track equally
- Check that conversion pixels fire on all variants
- Verify platform-reported conversions vs. actual

---

## Questions to Ask

If you need more context:
1. What are you testing (page, email, ad)?
2. What's your current baseline conversion rate?
3. What's your daily traffic to the test page?
4. Do you have a hypothesis for why this change will work?
5. What tools do you have for running tests?
6. How will you measure success?
7. What's the minimum effect size worth detecting?

---

## Related Skills

- **page-cro**: For CRO hypothesis generation
- **analytics-tracking**: For test measurement setup
- **copywriting**: For variant copy creation
- **marketing-psychology**: For hypothesis development
- **facebook-ads-creative-tester**: For ad creative testing
