---
name: incrementality-test-designer
description: Designs rigorous incrementality tests (geo-lift, holdout, conversion lift) to measure the true causal impact of advertising spend. Triggers when user asks about incrementality, "how do I know if my ads actually work," lift testing, geo experiments, holdout tests, or wants to measure true ad effectiveness beyond attribution. Provides statistically valid test designs with clear implementation plans.
---

# Incrementality Test Designer

Attribution tells you who saw your ad before converting. Incrementality tells you if your ad actually caused the conversion.

## Core Philosophy

**Attribution is not causation.** Just because someone clicked your ad before buying doesn't mean the ad caused the purchase. They might have bought anyway.

**The fundamental question:** Of all the conversions attributed to your ads, how many would have happened without the advertising?

**Why this matters:**
- If 50% of attributed conversions would happen organically, your true CPA is 2x what you think
- You might be "acquiring" customers who were already going to buy
- Scaling ineffective channels wastes budget

**The only way to know is to test.** Incrementality testing creates controlled experiments where you compare outcomes with and without advertising.

**Types of Incrementality Tests:**

| Test Type | How It Works | Best For |
|-----------|--------------|----------|
| Geo-lift | Compare regions with/without ads | Large budgets, broad targeting |
| Holdout | Exclude % of audience from seeing ads | Retargeting, specific audiences |
| Conversion lift | Platform-native A/B test | Meta, Google, TikTok |
| Ghost ads | Log but don't show ads to control | Display, programmatic |

---

## Required Context

### Must Have

**1. Current Advertising Setup**
- Channels running (Google, Meta, TikTok, etc.)
- Monthly spend per channel
- Current attributed CPA/ROAS per channel
- Campaign types (brand, non-brand, retargeting, prospecting)

**2. Business Context**
- Conversion type (purchase, lead, sign-up)
- Average order value or lead value
- Typical conversion volume per day/week
- Geographic distribution of customers

**3. Test Objective**
- What specifically do you want to measure?
- Which channel or campaign type?
- What decision will this test inform?

### Strongly Recommended

**4. Historical Data**
- 3-6 months of conversion data
- Seasonal patterns
- Geographic breakdown of conversions
- Day-of-week/time patterns

**5. Test Constraints**
- Minimum budget for testing
- Maximum acceptable risk
- Timeline requirements
- Geographic restrictions

### Nice to Have

- Prior incrementality test results
- Marketing mix model data
- CRM data on customer acquisition source
- Competitive intelligence

---

## Test Design Framework

### Step 1: Select Test Type

**Decision Matrix:**

| Factor | Geo-Lift | Holdout | Platform Lift | Ghost Ads |
|--------|----------|---------|---------------|-----------|
| Minimum spend | High ($50K+/mo) | Medium ($10K+/mo) | Medium ($10K+/mo) | High |
| Setup complexity | High | Medium | Low | High |
| Statistical rigor | Highest | High | Medium | High |
| Platform dependency | None | None | Platform-specific | DSP-specific |
| Best for | Prospecting, brand | Retargeting | Quick reads | Display |

**Recommendation Logic:**

```
IF measuring prospecting/brand campaigns AND budget > $50K/month
  → Geo-lift test

IF measuring retargeting AND have defined audience segments
  → Holdout test

IF need quick directional read AND running on Meta/Google
  → Platform conversion lift

IF running programmatic display
  → Ghost ads (if DSP supports)
```

---

### Step 2: Geo-Lift Test Design

**Concept:** Divide geographic regions into test (ads on) and control (ads off), compare conversion rates.

**Region Selection Criteria:**

| Factor | Requirement |
|--------|-------------|
| Similarity | Test and control regions should have similar historical performance |
| Independence | Regions shouldn't have spillover effects |
| Volume | Each region needs sufficient conversions for significance |
| Stability | Avoid regions with unusual volatility |

**Recommended Approach:**

1. **Identify candidate regions** (DMAs, states, countries)
2. **Analyze historical correlation** between regions
3. **Match test/control pairs** by:
   - Historical conversion rate
   - Seasonality patterns
   - Demographic similarity
   - Business penetration
4. **Randomize assignment** within matched pairs
5. **Calculate required sample size**

**Geo Selection Best Practices:**

| Good Pairs | Bad Pairs |
|------------|-----------|
| Similar population size | Major metro vs rural |
| Similar historical trends | Seasonal vs non-seasonal |
| No cross-border shopping | Border regions with spillover |
| Both have retail presence | One has stores, one doesn't |

**Minimum Requirements:**

| Metric | Minimum |
|--------|---------|
| Regions per group | 5+ (ideally 10+) |
| Conversions per region/week | 30+ |
| Test duration | 4-8 weeks |
| Pre-test observation | 4+ weeks |

---

### Step 3: Holdout Test Design

**Concept:** Randomly exclude a percentage of your target audience from seeing ads.

**Audience Holdout Structure:**

```
TOTAL AUDIENCE
    ↓
┌───────────────────────────────────────┐
│  TEST GROUP (85-95%)                  │
│  → See ads as normal                  │
│  → Track all conversions              │
├───────────────────────────────────────┤
│  CONTROL GROUP (5-15%)                │
│  → Excluded from seeing ads           │
│  → Track organic conversions          │
└───────────────────────────────────────┘
```

**Holdout Percentage Guidelines:**

| Scenario | Holdout % | Rationale |
|----------|-----------|-----------|
| High confidence needed | 10-15% | More statistical power |
| Limited budget | 5-10% | Minimize lost opportunity |
| High-value audience | 5% | Don't exclude too many |
| Testing hypothesis | 10-15% | Clear signal needed |

**Implementation Options:**

| Platform | How to Implement |
|----------|------------------|
| Meta | Use campaign holdout in Experiments |
| Google | Audience exclusion + separate tracking |
| Any platform | CRM-based exclusion list |

**Holdout Test Requirements:**

| Metric | Minimum |
|--------|---------|
| Control group size | 10,000+ users |
| Conversions in control | 100+ |
| Test duration | 2-4 weeks |
| Pre-test baseline | 2+ weeks |

---

### Step 4: Platform Conversion Lift Studies

**Meta Conversion Lift:**
- Native tool in Ads Manager (Experiments)
- Randomly splits audience into test/control
- Measures incremental lift in conversions
- Requires significant spend (~$10K+ over test period)

**Google Conversion Lift:**
- Available through Google rep
- Uses Google's user graph for holdout
- Measures brand search lift and conversions
- Typically requires larger budgets

**TikTok Brand Lift / Conversion Lift:**
- Available through rep
- Measures ad recall and conversion impact
- Newer, less proven methodology

**Platform Lift Test Considerations:**

| Pro | Con |
|-----|-----|
| Easy to set up | Black box methodology |
| Platform handles stats | May favor platform |
| Built-in reporting | Limited customization |
| No manual exclusions | Requires rep access |

---

### Step 5: Statistical Requirements

**Sample Size Calculation:**

To detect a X% lift with 80% power and 95% confidence:

| Baseline Conv Rate | 10% lift | 20% lift | 30% lift |
|--------------------|----------|----------|----------|
| 0.5% | 316,000 | 78,400 | 34,800 |
| 1% | 156,800 | 39,200 | 17,400 |
| 2% | 78,400 | 19,600 | 8,700 |
| 5% | 31,360 | 7,840 | 3,480 |

*Sample sizes are per group (test + control)*

**Test Duration Guidelines:**

| Factor | Consideration |
|--------|---------------|
| Minimum | 2 weeks (capture weekly patterns) |
| Ideal | 4-6 weeks (reduce noise) |
| Maximum | 8-12 weeks (avoid fatigue, market changes) |
| Seasonality | Avoid crossing major holidays |
| Business cycles | Align with natural purchase cycles |

**Power Analysis Framework:**

```
Inputs:
- Baseline conversion rate: X%
- Minimum detectable effect: Y%
- Significance level: 95% (α = 0.05)
- Power: 80% (β = 0.20)

Output:
- Required sample size per group
- Expected test duration given traffic
```

---

### Step 6: Pre-Test Validation

**Checklist Before Launch:**

| Check | Purpose | Pass Criteria |
|-------|---------|---------------|
| Randomization | Ensure groups are equivalent | No significant pre-test differences |
| Tracking | Conversions attributed correctly | Both groups tracked equally |
| Contamination | Control isn't exposed to treatment | No cross-group exposure |
| Sample size | Sufficient for detection | Meets power requirements |
| Duration | Long enough for significance | Covers business cycle |

**Pre-Test Analysis:**

Compare test vs control groups on:
- Historical conversion rate
- User demographics (if available)
- Time-series trends
- Seasonality alignment

**Expected:** No statistically significant differences pre-test

---

## Output Format

### Test Design Document

```
═══════════════════════════════════════════════════════════════════
INCREMENTALITY TEST DESIGN
═══════════════════════════════════════════════════════════════════
Test Name: [Descriptive Name]
Test Type: [Geo-Lift / Holdout / Platform Lift]
Channel: [Google / Meta / etc.]
Campaign: [Specific campaign or all]
Created: [Date]
═══════════════════════════════════════════════════════════════════

📋 TEST OVERVIEW
────────────────────────────────────────────────────────────────────

OBJECTIVE:
[What specific question are we trying to answer?]

HYPOTHESIS:
[Channel/Campaign] drives an incremental lift of [X-Y%] over organic conversions.

NULL HYPOTHESIS:
[Channel/Campaign] has no incremental impact on conversions.

BUSINESS DECISION:
If incremental lift is:
- >X%: [Action]
- Y-X%: [Action]
- <Y%: [Action]

═══════════════════════════════════════════════════════════════════

🔬 TEST DESIGN
────────────────────────────────────────────────────────────────────

TEST STRUCTURE:

| Group | Description | Size | Treatment |
|-------|-------------|------|-----------|
| Test | [Description] | [X%/regions] | Ads on |
| Control | [Description] | [X%/regions] | Ads off |

[For Geo-Lift Tests:]

REGION ASSIGNMENT:

| Test Regions | Control Regions |
|--------------|-----------------|
| [Region 1] | [Matched region] |
| [Region 2] | [Matched region] |
| [Region 3] | [Matched region] |
| ... | ... |

MATCHING CRITERIA:
- [Criterion 1]
- [Criterion 2]
- [Criterion 3]

[For Holdout Tests:]

AUDIENCE DEFINITION:
- Total audience: [X]
- Holdout percentage: [X%]
- Holdout selection: [Random / Stratified]
- Exclusion method: [Platform native / CRM list]

═══════════════════════════════════════════════════════════════════

📊 STATISTICAL PARAMETERS
────────────────────────────────────────────────────────────────────

| Parameter | Value |
|-----------|-------|
| Baseline conversion rate | [X%] |
| Minimum detectable effect | [X%] relative lift |
| Significance level (α) | 0.05 (95% confidence) |
| Statistical power (1-β) | 0.80 (80% power) |
| Required sample size | [X] per group |
| Expected daily volume | [X] conversions |
| Minimum test duration | [X] weeks |

POWER CURVE:

| Lift | Power | Detectable? |
|------|-------|-------------|
| 5% | [X%] | [Yes/No] |
| 10% | [X%] | [Yes/No] |
| 15% | [X%] | [Yes/No] |
| 20% | [X%] | [Yes/No] |

═══════════════════════════════════════════════════════════════════

📅 TEST TIMELINE
────────────────────────────────────────────────────────────────────

| Phase | Dates | Duration | Activities |
|-------|-------|----------|------------|
| Pre-test | [Date range] | [X weeks] | Baseline measurement |
| Ramp-up | [Date range] | [X days] | Implement test/control |
| Test | [Date range] | [X weeks] | Run experiment |
| Cooldown | [Date range] | [X days] | Lag conversions |
| Analysis | [Date] | [X days] | Calculate results |

TOTAL DURATION: [X weeks]

TIMING CONSIDERATIONS:
- [Holiday/event to avoid]
- [Seasonal factor]
- [Business cycle alignment]

═══════════════════════════════════════════════════════════════════

⚙️ IMPLEMENTATION GUIDE
────────────────────────────────────────────────────────────────────

PRE-TEST SETUP:

1. [ ] Define test and control groups
2. [ ] Validate group equivalence
3. [ ] Set up tracking infrastructure
4. [ ] Document baseline metrics
5. [ ] Create monitoring dashboard
6. [ ] Brief stakeholders

TEST LAUNCH:

1. [ ] Implement treatment (turn off ads for control)
2. [ ] Verify exclusions are working
3. [ ] Monitor for errors day 1
4. [ ] Confirm conversion tracking
5. [ ] Lock test parameters

DURING TEST:

⚠️ DO NOT:
- Change targeting
- Adjust budgets
- Add/remove creatives
- Modify audiences
- End test early (unless critical issue)

✅ DO:
- Monitor daily for anomalies
- Track external factors
- Document any incidents
- Maintain exclusions

═══════════════════════════════════════════════════════════════════

📈 ANALYSIS PLAN
────────────────────────────────────────────────────────────────────

PRIMARY METRIC:
[Conversion count / Conversion rate / Revenue]

INCREMENTALITY CALCULATION:

```
Incremental Conversions = Test Conversions - (Control Conversions × Scale Factor)

Incrementality Rate = Incremental Conversions / Test Conversions × 100

True CPA = Total Spend / Incremental Conversions
```

SECONDARY ANALYSES:
- Incrementality by [segment]
- Time-series of lift during test
- Confidence intervals
- Sensitivity analysis

STATISTICAL TESTS:
- [Test name]: [Purpose]
- [Test name]: [Purpose]

═══════════════════════════════════════════════════════════════════

⚠️ RISKS & MITIGATIONS
────────────────────────────────────────────────────────────────────

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Contamination | [H/M/L] | [H/M/L] | [Strategy] |
| Sample size insufficient | [H/M/L] | [H/M/L] | [Strategy] |
| External shock (competitor, news) | [H/M/L] | [H/M/L] | [Strategy] |
| Tracking failure | [H/M/L] | [H/M/L] | [Strategy] |
| Stakeholder pressure to end early | [H/M/L] | [H/M/L] | [Strategy] |

CONTINGENCY PLAN:
If [scenario], then [action].

═══════════════════════════════════════════════════════════════════

📋 SUCCESS CRITERIA
────────────────────────────────────────────────────────────────────

TEST VALIDITY CRITERIA:
- [ ] Both groups had minimum required sample
- [ ] No contamination detected
- [ ] No external shocks during test period
- [ ] Tracking confirmed accurate

ACTIONABLE RESULTS:
- Statistical significance reached: [Yes/No]
- Incrementality rate: [X%] ± [Y%] CI
- True CPA: $[X]
- Recommendation: [Scale / Maintain / Reduce / Cut]

═══════════════════════════════════════════════════════════════════
```

---

## Common Scenarios

### Scenario 1: "I want to test if my retargeting actually works"
**Recommendation:** Holdout test
**Design:**
- 10% holdout from all retargeting campaigns
- 4-week test duration
- Compare conversion rate of exposed vs holdout

**Why:** Retargeting often has lowest incrementality (users were already likely to convert). A holdout directly measures this.

### Scenario 2: "How do I know if brand search ads are worth it?"
**Recommendation:** Geo-lift test
**Design:**
- Turn off brand search in 5-10 test markets
- Keep brand search on in matched control markets
- Measure total conversions (not just search conversions)

**Why:** Brand search often has high attribution but unclear incrementality. Geo test captures cannibalization of organic.

### Scenario 3: "Is my prospecting actually finding new customers?"
**Recommendation:** Holdout + CRM analysis
**Design:**
- 10-15% holdout from prospecting audiences
- Track new customer acquisition in both groups
- Compare 30/60/90 day customer acquisition

**Why:** Prospecting attribution often wrong (users may have found you anyway). Holdout shows true acquisition.

### Scenario 4: "My boss wants results fast"
**Recommendation:** Platform conversion lift
**Design:**
- Use Meta or Google's native lift study
- Run for minimum 2 weeks
- Accept directional read vs. precise measurement

**Trade-off:** Faster but less rigorous. Use for directional decisions, not major budget reallocation.

### Scenario 5: "We don't have enough volume for significance"
**Options:**
1. Run longer test (more time = more data)
2. Accept lower power (risk missing real effects)
3. Test at channel level instead of campaign level
4. Use Bayesian methods (directional without strict significance)
5. Aggregate across markets or time periods

---

## Interpreting Results

### Incrementality Benchmarks

| Channel | Typical Incrementality | Notes |
|---------|------------------------|-------|
| Retargeting | 20-50% | Often lowest; users likely to convert anyway |
| Brand Search | 30-60% | Many would find you organically |
| Non-Brand Search | 50-80% | Generally higher incremental value |
| Social Prospecting | 40-70% | Varies by targeting quality |
| Display Prospecting | 20-50% | Often low; hard to reach incremental users |
| Video (Awareness) | 30-60% | Brand lift, not direct conversion |

### What Your Results Mean

| Incrementality | Interpretation | Action |
|----------------|----------------|--------|
| >80% | Highly incremental | Scale confidently |
| 50-80% | Solid incrementality | Maintain, optimize |
| 30-50% | Moderate incrementality | Question efficiency |
| <30% | Low incrementality | Consider cutting/reducing |

### Recalculating True CPA

```
Attributed CPA = $50
Incrementality Rate = 40%
True CPA = $50 / 0.40 = $125

If target CPA is $75, this channel is not efficient despite appearing efficient in attribution.
```

---

## Limitations

**I can provide:**
- Test design framework
- Statistical requirements
- Implementation guidance
- Analysis methodology
- Interpretation framework

**I cannot provide:**
- Actual power calculations (need statistical software)
- Platform-specific setup steps (changes frequently)
- Automated analysis
- Causal inference beyond basic methods

**For rigorous testing, also consider:**
- Hiring a measurement specialist
- Using synthetic control methods (advanced)
- Running marketing mix models alongside
- Engaging platform measurement teams

---

## Quality Checklist

Before finalizing test design:
- [ ] Test type matches question and constraints
- [ ] Sample size sufficient for desired power
- [ ] Test/control groups properly matched
- [ ] Duration accounts for business cycles
- [ ] Tracking infrastructure validated
- [ ] Contamination risks identified
- [ ] Analysis plan documented before test starts
- [ ] Success criteria defined before test starts
- [ ] Stakeholder alignment on methodology
- [ ] Contingency plans for common issues
