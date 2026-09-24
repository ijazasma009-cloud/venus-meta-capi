---
name: ab-test-designer-google-ads
description: Designs rigorous A/B tests for Google Ads with clear hypotheses, success metrics, sample size calculations, and test duration estimates. Triggers when user wants to test something, run an experiment, compare ad variations, or asks "should I test X vs Y?" Provides scientific test framework that prevents common mistakes and ensures statistically valid results.
---

# A/B Test Designer

Stop random testing. Start learning.

## Core Philosophy

**Most PPC "tests" aren't tests—they're guesses with extra steps.**

**What Makes a Real Test:**
1. Clear hypothesis (not just "let's try something")
2. Single variable isolation (know what caused the change)
3. Adequate sample size (statistical significance)
4. Predetermined success criteria (no moving goalposts)
5. Documented learnings (builds institutional knowledge)

**The Goal:** Every test either wins, loses, or teaches you something valuable.

---

## Required Context

### Must Have

**1. What You Want to Test**
- Variable being tested (headline, CTA, landing page, bid strategy, etc.)
- Current state (control)
- Proposed change (variation)

**2. Current Performance Baseline**
- Relevant metric (CTR, CVR, CPA, etc.)
- Current value
- Sample size available (monthly clicks, conversions)

### Strongly Recommended

**3. Business Context**
- Why are you testing this? What problem are you solving?
- What would make this test "worth it"?
- Minimum detectable effect that matters to business

**4. Constraints**
- Budget limitations
- Time constraints
- Technical limitations

### Nice to Have

- Historical test results (what's worked/failed before)
- Competitive context
- Seasonality considerations

---

## Test Framework

### Step 1: Hypothesis Formation

**Format:** "If we [change X], then [metric Y] will [improve/decrease] because [reasoning]."

**Good Hypothesis:**
"If we change the headline from 'Project Management Software' to 'Ship Projects 2x Faster,' then CTR will improve by 15%+ because benefit-focused headlines outperform feature-focused headlines in our space."

**Bad Hypothesis:**
"Let's try a new headline and see what happens."

**Hypothesis Quality Checklist:**
- [ ] Specific change identified
- [ ] Measurable outcome defined
- [ ] Magnitude of expected change stated
- [ ] Reasoning based on evidence or logic
- [ ] Falsifiable (can be proven wrong)

---

### Step 2: Variable Isolation

**Golden Rule:** Test ONE thing at a time.

**Why This Matters:**
If you change the headline AND the CTA AND the image, and performance improves, which change caused it?

**Variable Categories:**

| Variable Type | Examples | Isolation Challenge |
|---------------|----------|---------------------|
| Ad Copy | Headlines, descriptions, CTAs | Test one element per variation |
| Landing Page | Headline, form, layout, images | One change per page variation |
| Targeting | Keywords, audiences, locations | Separate campaigns/ad groups |
| Bidding | Strategy, targets, adjustments | Requires campaign split |
| Creative | Images, videos, formats | One creative element per test |

**Multi-Variable Testing:**
Only do this if you have very high volume AND proper multivariate testing tools. Otherwise, you're just creating noise.

---

### Step 3: Sample Size Calculation

**Required Inputs:**
- Baseline conversion rate (current performance)
- Minimum detectable effect (MDE) - smallest improvement worth detecting
- Statistical significance level (typically 95%)
- Statistical power (typically 80%)

**Sample Size Formula (Simplified):**

For conversion rate tests:
```
n = 16 × p × (1-p) / MDE²

Where:
n = sample size per variation
p = baseline conversion rate
MDE = minimum detectable effect (as decimal)
```

**Quick Reference Table:**

| Baseline CVR | 10% MDE | 15% MDE | 20% MDE | 25% MDE |
|--------------|---------|---------|---------|---------|
| 1% | 15,840 | 7,040 | 3,960 | 2,534 |
| 2% | 31,360 | 13,938 | 7,840 | 5,018 |
| 3% | 46,560 | 20,693 | 11,640 | 7,450 |
| 5% | 76,000 | 33,778 | 19,000 | 12,160 |
| 10% | 144,000 | 64,000 | 36,000 | 23,040 |

*Sample size per variation. Multiply by 2 for total test traffic needed.*

**For CTR tests:** Use same formula with CTR as baseline rate.

---

### Step 4: Test Duration Calculation

**Formula:**
```
Test Duration (days) = Sample Size Needed / Daily Traffic

Where:
Sample Size Needed = From calculation above (for BOTH variations)
Daily Traffic = Average daily clicks to test location
```

**Minimum Duration Rules:**
- Never less than 7 days (need full week for day-of-week variation)
- Ideally 14-28 days for reliability
- Avoid major holidays or promotional periods
- Account for conversion lag

**Duration Constraints:**
```
If calculated duration < 7 days → Run for 7 days minimum
If calculated duration > 60 days → Consider:
  - Accepting larger MDE
  - Testing in higher-traffic location
  - Questioning if test is viable
```

---

### Step 5: Success Criteria Definition

**Define BEFORE the test starts:**

**Primary Metric:**
- What metric determines win/lose?
- What improvement threshold = "winner"?
- What confidence level required?

**Secondary Metrics:**
- What other metrics to monitor?
- What would disqualify a "winner"? (e.g., CTR up but CVR down)

**Guardrail Metrics:**
- Metrics that must NOT get worse
- Acceptable variance on guardrails

**Example Success Criteria:**
```
PRIMARY: CTR must improve by ≥15% with 95% confidence
SECONDARY: Monitor conversion rate (must not decrease >10%)
GUARDRAIL: CPA must not increase >20%
WINNER: Variation beats control on primary metric while respecting guardrails
```

---

### Step 6: Test Execution Plan

**Setup Checklist:**
- [ ] Control and variation created
- [ ] Traffic split configured (50/50 recommended)
- [ ] Tracking verified for all metrics
- [ ] Start date set (avoid anomalous days)
- [ ] End date set (based on duration calculation)
- [ ] Success criteria documented
- [ ] Notification set for test completion

**During Test:**
- [ ] Check for implementation errors (Day 1-2)
- [ ] Verify traffic splitting correctly
- [ ] DO NOT peek at results and make early calls
- [ ] Document any external factors

**After Test:**
- [ ] Wait for statistical significance
- [ ] Check all metrics (primary, secondary, guardrails)
- [ ] Document results and learnings
- [ ] Implement winner (or document why not)
- [ ] Plan next test based on learnings

---

## Output Format

### Test Design Document

```
═══════════════════════════════════════════════════════
TEST: [Descriptive Name]
STATUS: Ready for Launch / In Review
═══════════════════════════════════════════════════════
```

---

### 🎯 Hypothesis

**Statement:**
"If we [specific change], then [metric] will [expected outcome] because [reasoning]."

**Confidence Level:** High / Medium / Low
**Basis:** [What evidence or logic supports this hypothesis]

---

### 🔬 Test Design

| Element | Control | Variation |
|---------|---------|-----------|
| [Variable] | [Current state] | [New state] |

**Variable Being Tested:** [Single variable]
**Everything Else Held Constant:** [Confirm isolation]

---

### 📊 Statistical Requirements

| Parameter | Value | Notes |
|-----------|-------|-------|
| Baseline Metric | [X%] | Current [CTR/CVR/etc.] |
| Minimum Detectable Effect | [X%] | Smallest meaningful improvement |
| Required Sample Size | [X] per variation | [X] total |
| Estimated Daily Traffic | [X] | To test location |
| Estimated Test Duration | [X] days | Minimum 7 days |
| Confidence Level | 95% | Standard |
| Statistical Power | 80% | Standard |

---

### ✅ Success Criteria

**To declare a winner:**

**Primary Metric:** [Metric name]
- Winner threshold: ≥[X]% improvement
- Confidence required: 95%

**Secondary Metrics:**
- [Metric]: Monitor, no threshold
- [Metric]: Must not decrease >X%

**Guardrails:**
- [Metric]: Must not worsen by >X%

**Decision Rules:**
- If primary wins AND guardrails pass → Implement variation
- If primary wins BUT guardrails fail → Investigate, likely reject
- If primary inconclusive → Extend test or accept null result
- If primary loses → Document learning, reject variation

---

### 📅 Execution Plan

**Timeline:**
- Setup complete by: [Date]
- Test start: [Date]
- Minimum end date: [Date]
- Decision date: [Date]

**Traffic Split:** 50% Control / 50% Variation

**Monitoring Checkpoints:**
- Day 1-2: Verify implementation
- Day 7: First statistical check (no decisions)
- Day [X]: End of test, final analysis

---

### ⚠️ Risks & Considerations

- [Risk 1]: [Mitigation]
- [Risk 2]: [Mitigation]

**External Factors to Document:**
- Seasonality: [Relevant?]
- Promotions: [Any during test?]
- Competitor activity: [Known changes?]

---

### 📝 Documentation Template

**Pre-Test:**
```
Test Name:
Hypothesis:
Start Date:
Expected End Date:
Success Criteria:
```

**Post-Test:**
```
Actual End Date:
Result: Win / Lose / Inconclusive
Primary Metric: Control [X%] vs Variation [X%]
Statistical Significance: [X%]
Secondary Metrics: [Results]
Guardrails: [Pass/Fail]
Decision: Implement / Reject / Extend
Key Learning:
Next Test:
```

---

## Common Test Types

### Ad Copy Tests

**What to test:**
- Headlines (one at a time)
- Description lines
- CTA variations
- Value prop emphasis

**Typical MDE:** 10-20% CTR improvement
**Duration:** 7-14 days typically

### Landing Page Tests

**What to test:**
- Headline/value prop
- CTA button (text, color, placement)
- Form length
- Social proof placement
- Hero image

**Typical MDE:** 15-25% CVR improvement
**Duration:** 14-28 days typically

### Bid Strategy Tests

**What to test:**
- Manual vs. automated
- Different target values
- Bid adjustments

**Typical MDE:** 10-15% CPA improvement
**Duration:** 28-42 days (need learning period)

### Audience Tests

**What to test:**
- Demographics
- In-market segments
- Custom audiences
- Lookalikes

**Typical MDE:** 20-30% CVR improvement
**Duration:** 14-28 days typically

---

## Common Mistakes to Avoid

### 1. Peeking and Stopping Early
**Problem:** Checking results daily and stopping when you see a "winner"
**Why It's Wrong:** Statistical significance fluctuates; early stopping = false positives
**Solution:** Set duration in advance, stick to it

### 2. Testing Too Many Things
**Problem:** Changing 5 things and calling it an "A/B test"
**Why It's Wrong:** Can't attribute causality
**Solution:** One variable per test, period

### 3. Insufficient Sample Size
**Problem:** Running test for 3 days with 50 clicks
**Why It's Wrong:** Results are random noise, not signal
**Solution:** Calculate required sample size before starting

### 4. No Clear Hypothesis
**Problem:** "Let's just try this and see"
**Why It's Wrong:** You learn nothing even if it "wins"
**Solution:** Write hypothesis first, then design test

### 5. Moving Goalposts
**Problem:** Changing success criteria after seeing results
**Why It's Wrong:** Confirmation bias, invalid conclusions
**Solution:** Document criteria before test starts

### 6. Ignoring Practical Significance
**Problem:** Celebrating 0.5% improvement at 95% confidence
**Why It's Wrong:** Statistically significant ≠ business meaningful
**Solution:** Set MDE based on business impact

---

## Limitations

**I can provide:**
- Rigorous test design framework
- Sample size calculations
- Duration estimates
- Success criteria templates
- Common pitfall warnings

**I cannot provide:**
- Actual statistical analysis of results (need raw data)
- Bayesian vs. frequentist methodology choice (depends on your setup)
- Tool-specific implementation (varies by platform)
- Guaranteed test ideas that will win

**For better test design, also provide:**
- Historical test results
- Conversion funnel data
- Competitive ad examples
- User research insights

---

## Quality Checklist

Before launching test:
- [ ] Hypothesis is specific and falsifiable
- [ ] Single variable isolated
- [ ] Sample size calculated
- [ ] Duration set (minimum 7 days)
- [ ] Success criteria documented
- [ ] Guardrail metrics defined
- [ ] Traffic split configured
- [ ] Tracking verified
- [ ] External factors noted
- [ ] Documentation template ready
