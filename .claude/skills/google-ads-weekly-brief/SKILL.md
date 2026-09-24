---
name: google-ads-weekly-brief
description: Generates professional weekly Google Ads performance reports for clients or stakeholders. Triggers when user needs a performance summary, client update, weekly report, or stakeholder brief. Transforms raw data into clear narratives with key metrics, wins, concerns, and recommended actions. Output ready for email, Slack, or presentation.
---

# Google Ads Weekly Brief

Transform campaign data into clear, actionable reports that clients actually read.

## Core Philosophy

**Executives don't want data—they want insights.**

**The 3 Questions Every Brief Must Answer:**
1. Are we on track? (Performance vs. goals)
2. What happened? (Key changes and why)
3. What's next? (Actions and recommendations)

**Tone:** Confident, clear, no jargon. Write like you're explaining to a smart person who doesn't live in Google Ads.

---

## Required Context

### Must Have

**1. Performance Data**
This week's metrics (minimum):
- Spend
- Conversions
- CPA or ROAS
- Clicks (optional but helpful)

Last week's metrics for comparison:
- Same metrics as above

**2. Time Period**
- Week dates (e.g., Jan 13-19, 2025)
- Comparison period (typically previous week)

### Strongly Recommended

**3. Goals/Targets**
- Target CPA: $___
- Target ROAS: ___
- Monthly budget: $___
- Monthly conversion goal: ___

Without goals, I'll report on trends but can't assess "on track" status.

**4. Audience Context**
Who is reading this?
- Executive (high-level only)
- Marketing manager (some detail)
- Client (explain everything)
- Internal team (can use jargon)

### Nice to Have

- Top campaigns by performance
- Any recent changes made
- External factors (seasonality, promos, market events)
- Previous week's recommendations (did we act on them?)

---

## Report Structure

### Section 1: The Headline

One sentence that captures the week. This is what gets read.

**Formula:** [Performance assessment] + [Key driver] + [Outlook]

**Examples:**
- "Strong week: conversions up 23% as new ad copy tests outperformed. On pace to beat monthly target."
- "Flat week: CPA held steady despite increased competition. Budget pacing on track."
- "Challenging week: CPA spiked 31% due to conversion tracking issue (now resolved). Expect recovery next week."

### Section 2: The Scorecard

Visual snapshot of key metrics.

```
METRIC          THIS WEEK    LAST WEEK    CHANGE    VS TARGET
─────────────────────────────────────────────────────────────
Spend           $X,XXX       $X,XXX       +X%       XX% of budget
Conversions     XXX          XXX          +X%       On/Off pace
CPA             $XX.XX       $XX.XX       +X%       ✓/✗ Target
ROAS            X.XX         X.XX         +X%       ✓/✗ Target
CTR             X.XX%        X.XX%        +X%       —
```

**Traffic Light System:**
- 🟢 Beating target by 10%+
- 🟡 Within 10% of target
- 🔴 Missing target by 10%+

### Section 3: What Happened (The Story)

**Wins** (2-3 bullets max)
What went well and why. Be specific.

❌ "Performance improved"
✓ "CPA dropped 18% after pausing underperforming broad match keywords identified last week"

**Concerns** (1-2 bullets if applicable)
What needs attention. Include context.

❌ "CTR is down"
✓ "CTR dropped 12% as we expanded to new audience segments. Expected during testing phase—monitoring conversion quality."

**Context** (if relevant)
External factors affecting performance.
- Seasonality
- Competitor activity
- Website/landing page changes
- Market events

### Section 4: Campaign Highlights

Top and bottom performers with brief context.

**Top Performer: [Campaign Name]**
- Conversions: XX at $XX CPA
- Why it's winning: [Brief explanation]
- Action: [Scale, maintain, or test]

**Needs Attention: [Campaign Name]**
- Conversions: XX at $XX CPA
- What's happening: [Brief explanation]
- Action: [Specific next step]

### Section 5: Actions & Next Steps

**Completed This Week:**
- [Action taken] → [Result if known]
- [Action taken] → [Result if known]

**Planned for Next Week:**
- [ ] [Specific action with expected impact]
- [ ] [Specific action with expected impact]

**Recommendations Requiring Approval:**
- [Recommendation] — [Why] — [Expected impact]

### Section 6: Month-to-Date Pacing

```
MONTHLY GOAL         ACHIEVED        PACE           PROJECTION
────────────────────────────────────────────────────────────
Conversions: XXX     XXX (XX%)       On/Behind      ~XXX
Budget: $X,XXX       $X,XXX (XX%)    On/Under       ~$X,XXX
Avg CPA: $XX         $XX.XX          At/Above       —
```

---

## Tone Guidelines

### For Executive Audience
- Lead with the headline
- Scorecard + 2-3 key points
- Skip tactical details
- Focus on business outcomes
- 200 words max

### For Marketing Manager
- Full structure
- Include tactical context
- More detail on actions
- 400-500 words

### For Client (Non-Expert)
- Explain metrics in plain language
- Add "what this means" after numbers
- Avoid acronyms or define them
- More context on actions
- 500-600 words

### For Internal Team
- Can use industry jargon
- Include tactical details
- More granular campaign data
- 400-600 words

---

## Writing Rules

### Numbers
- Always include direction (up/down) and magnitude (%)
- Round to meaningful precision ($45.23 → $45, 12.847% → 12.8%)
- Compare to something (last week, target, benchmark)

### Headlines
- Active voice
- No weak verbs (is, was, had)
- Lead with the insight, not the data

❌ "CPA was $47 this week"
✓ "CPA dropped 15% to $47 after bid adjustments"

### Bullets
- Start with action verbs or key metric
- One idea per bullet
- No bullet should require a follow-up question

### Recommendations
- Specific and actionable
- Include expected impact
- Distinguish between "doing" and "need approval"

---

## Output Formats

### Email Format (Default)
Subject line + formatted body ready to send.

**Subject Line Formula:**
`[Account] Weekly Brief: [Headline] | Week of [Date]`

Example: "Acme Corp Weekly Brief: Conversions Up 23% | Week of Jan 13"

### Slack Format
Condensed version with emoji indicators.
Uses code blocks for scorecard.
Thread-friendly structure.

### Slide Format
Key points as bullet slides.
Scorecard as visual.
1 insight per slide.

### Executive Summary
3 sentences max.
Headline + key metric + outlook.

---

## Handling Tough Weeks

### When Performance is Down

**Don't:**
- Make excuses
- Bury bad news
- Be defensive

**Do:**
- Lead with acknowledgment
- Explain the why
- Show the plan to fix it
- Put in context (one bad week ≠ crisis)

**Example:**
"CPA increased 25% this week to $62, above our $50 target. Primary driver: a landing page issue on Thursday caused conversions to drop for 18 hours. Issue resolved Friday—early signs show recovery. Expect return to target range next week."

### When You Don't Know Why

Be honest. Don't fabricate explanations.

**Example:**
"CTR dropped 8% without clear cause. No changes were made to ads or targeting. Investigating whether this is competitor activity or algorithm fluctuation. Will report findings next week."

### When Recommending Budget Changes

Frame in terms of opportunity cost.

**Increase:** "Recommend adding $2K to Campaign X—it's generating leads at $35 CPA vs. $50 target but capped by budget. ROI opportunity."

**Decrease:** "Recommend shifting $1K from Campaign Y (CPA: $78) to Campaign X (CPA: $35). Same budget, better results."

---

## Quality Checklist

Before delivering the brief:
- [ ] Headline answers "how did we do this week?"
- [ ] All numbers have comparison context
- [ ] Wins are specific, not generic
- [ ] Concerns include "what we're doing about it"
- [ ] Actions are executable (who, what, when)
- [ ] Tone matches audience
- [ ] No unexplained jargon
- [ ] Formatted for easy scanning
- [ ] Subject line would make you open the email

---

## Limitations

**I can provide:**
- Clear narrative from performance data
- Metric comparisons and trend identification
- Professional formatting for any audience
- Recommendations based on data patterns

**I cannot provide:**
- Competitor analysis (need auction insights data)
- Conversion quality assessment (need backend data)
- Attribution analysis (need cross-channel data)
- Future predictions (only projections based on pace)

**For richer briefs, also provide:**
- Auction insights data
- Backend lead/sale quality data
- Website analytics (GA4)
- Any qualitative feedback from sales team
