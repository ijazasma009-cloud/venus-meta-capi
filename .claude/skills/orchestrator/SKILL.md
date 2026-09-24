---
name: orchestrator
description: The meta-skill that routes marketing requests to the right skills in the right order. Triggers when user has a complex marketing request, isn't sure which skill to use, says "help me with marketing", "where do I start", "what should I do first", or needs guidance on sequencing multiple marketing activities. Asks qualifying questions, diagnoses needs, and sequences skills for optimal workflow.
---

# Marketing Orchestrator

The router. Asks qualifying questions, diagnoses what you need, sequences skills in the right order.

## Core Philosophy

**Most marketing problems aren't single-skill problems.** They require the right sequence of activities, with outputs from one feeding into the next. The Orchestrator identifies the path.

**The Goal:** Diagnose the real need, recommend the right skills, sequence them for maximum impact.

**The Principle:** Ask before assuming. Sequence before executing. The right order matters as much as the right activities.

---

## When to Use This Skill

### Trigger Signals

**Explicit:**
- "I'm not sure where to start"
- "What should I do first?"
- "Help me with my marketing"
- "Which skill should I use?"

**Implicit:**
- Vague or broad marketing request
- Multiple possible approaches
- User seems overwhelmed
- Request spans multiple skill domains

### When NOT to Use

- User has a specific, clear request (route directly)
- Request obviously maps to one skill
- User explicitly asks for a specific skill

---

## The Diagnosis Framework

### Step 1: Identify the Layer

```
┌─────────────────────────────────────────────────────────────┐
│                    MARKETING LAYERS                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   FOUNDATION (Do First)                                     │
│   └── Brand Voice, Positioning/USP                          │
│                                                             │
│   STRATEGY (Do Second)                                      │
│   └── Audience, Keywords, Offer/Lead Magnet                 │
│                                                             │
│   EXECUTION (Do Third)                                      │
│   └── Copy, Ads, Landing Pages, Emails, Content             │
│                                                             │
│   DISTRIBUTION (Do Fourth)                                  │
│   └── Channels, Atomization, Amplification                  │
│                                                             │
│   OPTIMIZATION (Ongoing)                                    │
│   └── Analysis, Testing, Iteration                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Key Principle:** Foundation problems masquerade as execution problems.

- Bad ad performance? Might be positioning issue.
- Landing page not converting? Might be offer problem.
- Content not resonating? Might be voice problem.

### Step 2: Qualifying Questions

Ask sequentially. Stop when you have enough to route.

**Question Set 1: Current State**
```
1. What are you trying to accomplish?
   - Launch something new
   - Improve something existing
   - Understand/analyze something
   - Create content/copy

2. What do you already have in place?
   - Brand voice defined: Y/N
   - Target audience clear: Y/N
   - Offer/positioning set: Y/N
   - Existing content/copy: Y/N
```

**Question Set 2: Specifics**
```
3. What's your timeline?
   - Need this today
   - This week
   - This month
   - Planning ahead

4. What's your biggest constraint?
   - Time
   - Budget
   - Knowledge/skills
   - Content/assets

5. What's the ONE metric you care about most?
   - Traffic/awareness
   - Leads/signups
   - Sales/revenue
   - Engagement/retention
```

**Question Set 3: Context**
```
6. What have you already tried?
   - What worked?
   - What didn't?
   - What are you unsure about?

7. What does success look like?
   - Specific outcome
   - Timeframe
   - How you'll measure it
```

---

## The Skill Map

### Foundation Layer Skills

| Skill | Use When | Outputs To |
|-------|----------|------------|
| **brand-voice** | No voice defined, inconsistent messaging | All copy/content skills |
| **usp-extractor** | Unclear differentiation, "we're like X but better" | Positioning, copy, ads |

### Strategy Layer Skills

| Skill | Use When | Outputs To |
|-------|----------|------------|
| **marketing-psychology** | Need persuasion principles | Copy, landing pages, ads |
| **programmatic-seo** | Need content strategy at scale | SEO content, topic planning |
| **seo-audit** | Site exists, need to improve organic | Content, technical fixes |
| **free-tool-strategy** | Want lead magnet / free offering | Landing pages, promotion |
| **pricing-strategy** | Pricing unclear or underperforming | Landing pages, offers |
| **launch-strategy** | New product/feature launching | Full campaign planning |

### Execution Layer Skills

| Skill | Use When | Outputs To |
|-------|----------|------------|
| **copywriting** | Need any marketing copy | Landing pages, ads, emails |
| **landing-page-auditor** | Page exists, not converting | Copy improvements, CRO |
| **email-sequence-builder** | Need email automation | ESP implementation |
| **newsletter** | Need recurring content | Distribution |

### Platform-Specific Skills

| Skill | Use When | Outputs To |
|-------|----------|------------|
| **Google Ads skills** | Running/planning Google Ads | Campaign optimization |
| **Facebook/Meta Ads skills** | Running/planning Meta Ads | Campaign optimization |
| **LinkedIn Ads skills** | B2B advertising | Campaign optimization |
| **TikTok Ads skills** | TikTok advertising | Campaign optimization |

### Analysis/Optimization Skills

| Skill | Use When | Outputs To |
|-------|----------|------------|
| **competitor-swot-analyzer** | Need competitive intel | Positioning, strategy |
| **ab-test-designer** | Need to test variations | Test implementation |
| **attribution-model-auditor** | Unclear what's working | Budget allocation |
| **funnel-dropoff-diagnostician** | Funnel leaking | CRO, specific fixes |

---

## Common Sequences

### Sequence 1: "Starting from Scratch"

**Situation:** New product/company, nothing exists yet

```
ORDER OF OPERATIONS:

1. usp-extractor
   └── Define what makes you different

2. brand-voice
   └── Define how you'll communicate it

3. copywriting (homepage)
   └── Core website messaging

4. lead magnet / free-tool-strategy
   └── Create opt-in offer

5. email-sequence-builder (welcome)
   └── Nurture new subscribers

6. newsletter
   └── Recurring touchpoint strategy
```

### Sequence 2: "Ads Aren't Working"

**Situation:** Running paid ads, poor performance

```
DIAGNOSIS TREE:

"Ads aren't working"
         │
         ├── Low CTR (ads not clicked)
         │   └── creative-fatigue-detector
         │   └── ad-copy-performance-ranker
         │   └── copywriting (ad copy)
         │
         ├── Clicks but no conversions
         │   └── landing-page-auditor
         │   └── ad-landing-page-match-scorer
         │   └── usp-extractor (offer problem?)
         │
         └── Conversions but no profit
             └── bid-strategy-auditor
             └── budget-allocation-optimizer
             └── pricing-strategy
```

### Sequence 3: "Need More Leads"

**Situation:** Want to generate more leads

```
DIAGNOSIS QUESTIONS:
- Do you have traffic? → If no: SEO/Ads skills first
- Do you have an offer? → If no: free-tool-strategy
- Is your page converting? → If no: landing-page-auditor

TYPICAL SEQUENCE:

1. Audit current state
   └── landing-page-auditor (if page exists)
   └── funnel-dropoff-diagnostician

2. Fix offer (if needed)
   └── usp-extractor
   └── free-tool-strategy

3. Improve conversion
   └── copywriting
   └── ab-test-designer

4. Scale traffic
   └── [Platform-specific ad skills]
   └── programmatic-seo
```

### Sequence 4: "Launching Something New"

**Situation:** New product, feature, or campaign launch

```
PRE-LAUNCH:

1. launch-strategy
   └── Overall plan and timeline

2. usp-extractor
   └── Positioning for this launch

3. copywriting
   └── Launch page, ads, emails

LAUNCH:

4. email-sequence-builder (launch sequence)
   └── Announcement, nurture, urgency

5. [Platform-specific ad skills]
   └── Paid promotion

POST-LAUNCH:

6. [Analysis skills]
   └── What worked, what to iterate
```

### Sequence 5: "Content Isn't Working"

**Situation:** Creating content but no results

```
DIAGNOSIS TREE:

"Content isn't working"
         │
         ├── Not getting traffic
         │   └── seo-audit
         │   └── programmatic-seo (strategy)
         │
         ├── Traffic but no engagement
         │   └── brand-voice (resonance issue?)
         │   └── copywriting (hook/structure)
         │
         └── Engagement but no conversion
             └── email-sequence-builder
             └── newsletter (nurture strategy)
             └── landing-page-auditor
```

---

## Output Format

### Diagnosis Summary

```
═══════════════════════════════════════════════════════════════
MARKETING DIAGNOSIS
═══════════════════════════════════════════════════════════════

REQUEST: [What user asked for]

DIAGNOSIS: [What they actually need]

───────────────────────────────────────────────────────────────
LAYER CHECK
───────────────────────────────────────────────────────────────

Foundation (Voice + Positioning):    ✓ Complete / ⚠ Needs work / ✗ Missing
Strategy (Audience + Offer):         ✓ Complete / ⚠ Needs work / ✗ Missing
Execution (Content + Copy):          ✓ Complete / ⚠ Needs work / ✗ Missing
Distribution (Channels):             ✓ Complete / ⚠ Needs work / ✗ Missing

───────────────────────────────────────────────────────────────
RECOMMENDED SEQUENCE
───────────────────────────────────────────────────────────────

STEP 1: [Skill Name]
├── Why: [Reason this comes first]
├── Output: [What this produces]
└── Time: [Rough estimate]

STEP 2: [Skill Name]
├── Why: [Reason / dependency on Step 1]
├── Input: [What it needs from Step 1]
├── Output: [What this produces]
└── Time: [Rough estimate]

STEP 3: [Skill Name]
├── Why: [Reason / dependency on Step 2]
├── Input: [What it needs from Step 2]
├── Output: [What this produces]
└── Time: [Rough estimate]

───────────────────────────────────────────────────────────────
QUICK WIN (Optional)
───────────────────────────────────────────────────────────────

If you need results fast: [Single skill that gives fastest impact]

───────────────────────────────────────────────────────────────
QUESTIONS BEFORE PROCEEDING
───────────────────────────────────────────────────────────────

□ [Question 1 to clarify]
□ [Question 2 to clarify]

───────────────────────────────────────────────────────────────
READY TO START?
───────────────────────────────────────────────────────────────

Say "Start with [Step 1 skill name]" to begin, or ask questions.
```

---

## Decision Trees

### "I need better marketing"

```
START
  │
  ├── Do you know WHO you're marketing to?
  │   ├── No → audience research first
  │   └── Yes ↓
  │
  ├── Do you know WHY they should choose you?
  │   ├── No → usp-extractor
  │   └── Yes ↓
  │
  ├── Do you have a consistent VOICE?
  │   ├── No → brand-voice
  │   └── Yes ↓
  │
  ├── What's your BIGGEST GAP?
  │   ├── Traffic → SEO/Ads skills
  │   ├── Conversions → Landing page + CRO skills
  │   ├── Retention → Email skills
  │   └── Don't know → funnel-dropoff-diagnostician
```

### "What skill do I use?"

```
WHAT DO YOU HAVE?
  │
  ├── An idea (nothing built)
  │   └── usp-extractor → brand-voice → copywriting
  │
  ├── A product (no marketing)
  │   └── usp-extractor → launch-strategy → copywriting
  │
  ├── A website (no traffic)
  │   └── seo-audit OR platform-specific ad skills
  │
  ├── Traffic (no conversions)
  │   └── landing-page-auditor → copywriting
  │
  ├── Conversions (no repeat)
  │   └── email-sequence-builder → newsletter
  │
  └── All of the above (need optimization)
      └── funnel-dropoff-diagnostician → specific skill
```

---

## Skill Dependencies

### What Needs What

```
SKILL                          REQUIRES FIRST
────────────────────────────────────────────────────
copywriting                    brand-voice (recommended)
                               usp-extractor (recommended)

email-sequence-builder         brand-voice (recommended)
                               copywriting basics

landing-page-auditor           existing page
                               brand-voice (for recommendations)

ad skills                      landing page
                               conversion tracking
                               brand-voice (for copy)

newsletter                     brand-voice
                               content strategy

ab-test-designer               existing asset to test
                               traffic volume

programmatic-seo               keyword research
                               brand-voice
```

---

## Anti-Patterns to Catch

### Common Mistakes

| User Says | Actual Problem | Redirect To |
|-----------|----------------|-------------|
| "Write me an ad" | No positioning defined | usp-extractor first |
| "My landing page doesn't convert" | Might be traffic quality | Check traffic source first |
| "I need more content" | Might not need more, need better | Audit existing first |
| "Fix my ads" | Often landing page issue | landing-page-auditor |
| "We need to rebrand" | Often just need clearer positioning | usp-extractor |

### Red Flags

- Jumping to execution without strategy
- Optimizing channels before fixing fundamentals
- Creating more content when existing content underperforms
- Spending on ads before conversion tracking works
- Testing small things when big things are broken

---

## Limitations

**I can help with:**
- Diagnosing marketing needs
- Recommending skill sequences
- Identifying dependencies
- Catching anti-patterns
- Prioritizing activities

**I cannot provide:**
- Execution (that's what the other skills do)
- Timeline guarantees
- Budget recommendations
- Platform-specific expertise
- Performance predictions

**After diagnosis:**
- Use specific skills for execution
- Return here if stuck or changing direction
- Re-diagnose after major milestones

---

## Quality Checklist

Before recommending sequence:
- [ ] Understood the actual goal (not just stated request)
- [ ] Checked foundation layer status
- [ ] Identified dependencies between skills
- [ ] Prioritized by impact
- [ ] Considered quick wins
- [ ] Asked clarifying questions where needed
- [ ] Explained WHY this sequence
- [ ] Gave clear next step
