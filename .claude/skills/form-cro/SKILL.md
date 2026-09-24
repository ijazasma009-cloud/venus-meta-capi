---
name: form-cro
description: "When the user needs to optimize any form for higher completion rates — lead capture forms, contact forms, demo request forms, checkout forms, or survey forms. Also use when the user mentions 'form optimization,' 'form conversions,' 'form friction,' 'form fields,' 'form completion rate,' 'form abandonment,' or 'lead form.' For signup/registration forms specifically, see signup-flow-cro."
---

# Form Conversion Optimization

You are an expert in form optimization who understands that every field you add is a tax on the user. Your job is to maximize completions while capturing the data that actually matters.

## The Form Truth

**Every field has a cost.**
- 3 fields: Baseline completion rate
- 4-6 fields: 10-25% reduction
- 7+ fields: 25-50%+ reduction

**The question isn't "what data would be nice to have?" It's "what data is absolutely essential before we can deliver value?"**

---

## Form Audit Framework

### Step 1: Define the Form's Purpose

**What type of form is this?**

| Form Type | Primary Goal | Typical Fields |
|-----------|--------------|----------------|
| Lead capture | Collect contact for follow-up | Email (+ maybe name) |
| Contact form | Enable communication | Name, email, message |
| Demo request | Schedule sales conversation | Name, email, company, role |
| Quote request | Provide pricing estimate | Contact + qualifying questions |
| Application | Evaluate fit | Extensive information |
| Checkout | Complete purchase | Billing, shipping, payment |
| Survey | Gather feedback | Various questions |

### Step 2: Field-by-Field Audit

**For each field, ask:**
1. Is this absolutely necessary BEFORE we can help them?
2. Can we get this information another way (enrichment, later)?
3. What would happen if we removed this field?
4. Is this field actually used in follow-up?

### Step 3: Measure Current Performance

**Key metrics:**
- Form view to start rate (did they engage?)
- Form start to complete rate (did they finish?)
- Field-level drop-off (where do they abandon?)
- Error rate by field
- Time to complete
- Mobile vs. desktop completion rates

---

## Field Optimization Guidelines

### Email Field

**Best practices:**
- Single field, no confirmation field
- Inline validation (real-time)
- Typo detection ("Did you mean gmail.com?")
- Proper mobile keyboard (type="email")
- Placeholder example: "name@company.com"

**Common mistakes:**
- Requiring email confirmation
- Validating too aggressively while typing
- Not handling + aliases (name+tag@gmail.com)

### Name Fields

**Single "Name" vs First/Last:**
| Approach | Pros | Cons |
|----------|------|------|
| Single "Full Name" | Lower friction, faster | Harder to personalize properly |
| First + Last | Better personalization | More fields, more friction |

**Recommendation:** Test single "Name" field first. Split only if personalization truly requires it.

### Phone Number

**Only require phone if you'll actually call.**

**If needed:**
- Explain why ("We'll text your confirmation code")
- Auto-format as they type
- Support international formats
- Proper mobile keyboard (type="tel")
- Make optional if possible

**If optional:**
- Clearly mark as optional
- Explain benefit of providing ("Faster response")

### Company/Organization

**Options:**
- Free text (flexible but messy data)
- Auto-suggest with clearance (faster, cleaner)
- Domain enrichment from email (get automatically)

**If you can enrich from email domain, consider removing this field entirely.**

### Job Title/Role

**Dropdown vs. free text:**
- Dropdown: Clean data, limits options
- Free text: Flexible, messy data
- Hybrid: Dropdown with "Other" option

**Consider making optional unless critical for routing.**

### Message/Free Text Fields

**Best practices:**
- Make optional unless truly required
- Set reasonable character limits
- Expand on focus
- Provide guidance on what to include
- Don't require minimum length

### Dropdown Selects

**Best practices:**
- "Select one..." placeholder (not blank)
- Searchable if >10 options
- Consider radio buttons if <5 options
- Include "Other" with free text option
- Logical order (alphabetical, most common first, or contextual)

---

## Multi-Step Forms

### When to Use Multi-Step

**Use multi-step when:**
- More than 5-6 fields required
- Logically distinct sections exist
- Conditional paths based on answers
- Complex forms (applications, quotes)
- High-value conversions worth the investment

**Don't use when:**
- Simple lead capture (email, name)
- Low-value micro-conversions
- Adding friction would kill completions

### Multi-Step Best Practices

**Progress indicators:**
- Show clear step progress (Step 2 of 4)
- Visual progress bar
- Step labels showing what's coming

**Flow design:**
- Start easy, end sensitive
- One logical topic per step
- Related fields grouped together
- Allow back navigation
- Save progress (don't lose data)

**Step sequencing:**
```
Step 1: Low friction (name, email) — Get commitment
Step 2: More detail (company, role) — Build investment
Step 3: Qualifying questions — Gather insight
Step 4: Preferences/details — Complete profile
```

### The Breadcrumb Technique

Show sunk cost to motivate completion:
- After step 1: "Great! Just 2 quick questions to personalize your results."
- After step 2: "Almost there! One more step."

---

## Error Handling

### Inline Validation

**Timing:**
- Validate on blur (when leaving field), not on keystroke
- Don't validate too aggressively while typing
- Show success state for valid inputs

**Visual indicators:**
- Green checkmark for valid
- Red border + message for invalid
- Icon + text (not just color for accessibility)

### Error Message Best Practices

**Good error messages:**
- Specific to the problem
- Tell them how to fix it
- Positioned near the field
- Don't blame the user

**Examples:**
| Bad | Good |
|-----|------|
| "Invalid input" | "Please enter a valid email (e.g., name@company.com)" |
| "Error" | "Phone number should be 10 digits" |
| "Required" | "We need your email to send your report" |

### On Submit Errors

- Scroll to first error
- Focus the error field
- Summarize errors if multiple
- Never clear their entered data
- Don't require re-entering password

---

## Submit Button Optimization

### Button Copy

**Weak:** Submit, Send, Continue, Next
**Strong:** [Action] + [What They Get]

**Examples:**
| Form Type | Weak | Strong |
|-----------|------|--------|
| Lead magnet | Submit | Get My Free Guide |
| Demo request | Send | Book My Demo |
| Contact | Submit | Send Message |
| Quote | Continue | Get My Custom Quote |
| Newsletter | Subscribe | Join 10,000+ Subscribers |

### Button Design

- High contrast with page
- Sufficient size (especially mobile)
- Clear visual affordance (looks clickable)
- Left-aligned with form fields
- Immediate feedback on click (loading state)

### Button Placement

- Immediately after last field
- Don't add excessive space
- Mobile: Consider sticky button
- Don't center-align (breaks eye flow)

---

## Trust & Friction Reduction

### Near Form Elements

**Privacy assurance:**
- "We'll never share your info"
- "No spam, ever"
- "Unsubscribe anytime"

**Security signals (when collecting sensitive data):**
- SSL/security badge
- Payment processor logos
- Compliance badges (GDPR, SOC 2)

**Social proof:**
- "Join 5,000+ marketers"
- Mini testimonial
- Star rating

### Reducing Perceived Effort

- "Takes 30 seconds"
- Field count indicator ("Just 3 questions")
- Show what they'll get after submitting
- Remove visual clutter around form
- Generous white space

---

## Mobile Form Optimization

### Mobile-Specific Checklist

- [ ] Tap targets 44px+ minimum
- [ ] Appropriate keyboard types per field
  - Email: `type="email"`
  - Phone: `type="tel"`
  - Number: `type="number"`
- [ ] Auto-focus first field (optional)
- [ ] Autofill support enabled
- [ ] Labels visible (not just placeholders)
- [ ] Error messages don't get cut off
- [ ] Submit button always accessible
- [ ] Single column layout only
- [ ] No zooming required to read

### Mobile-First Simplification

**If desktop form has 8 fields:**
- Can mobile version have 4?
- Can you progressive profile (get more later)?
- Can you use device capabilities (location, camera)?

---

## Form Types: Specific Guidance

### Lead Capture (Gated Content)

**Goal:** Minimum fields for maximum completions

**Recommended fields:**
- Email (required) — That's often enough
- Name (optional or combined in one)

**Post-submit strategy:**
- Ask additional questions on thank you page
- Progressive profile through email sequence
- Enrich data from email domain

### Demo Request

**Goal:** Qualify leads while maximizing requests

**Recommended fields:**
- Name (required)
- Email (required)
- Company (required or enriched)
- Job title (optional or dropdown)
- Use case question (optional, helps personalize)

**Consider:**
- Calendar embed to increase show rate
- "Preferred contact method" choice
- Company size (if critical for routing)

### Contact Form

**Goal:** Enable communication without creating friction

**Recommended fields:**
- Name (required)
- Email (required)
- Message (required, but reasonable)
- Phone (optional)
- Topic/department (optional, helps routing)

**Set expectations:**
- "We respond within 24 hours"
- "For urgent issues, call [number]"

### Quote/Estimate Request

**Goal:** Gather enough info to provide accurate quote

**Approach:** Multi-step works well
```
Step 1: Contact info
Step 2: Project/need basics
Step 3: Specific requirements
Step 4: Timeline/budget (optional)
```

**Save progress** — these forms get abandoned and revisited.

---

## Testing & Optimization

### What to Test

**High impact tests:**
1. Number of fields (reduce by 1-2)
2. Single step vs. multi-step
3. Field order
4. Button copy
5. Required vs. optional fields
6. Form placement on page
7. Social proof near form

### Testing Hypotheses

```
IF we [change]
THEN completion rate will [increase/decrease]
BECAUSE [insight]
```

**Example:**
```
IF we remove the phone number field
THEN form completions will increase 15%+
BECAUSE phone number creates friction without being used
```

### Lead Quality vs. Quantity

**More fields = fewer leads but potentially higher quality**

Test both:
- Conversion rate (quantity)
- Lead-to-customer rate (quality)
- Total customers generated (what matters)

Sometimes fewer, better leads wins. Sometimes volume wins.

---

## Form Analytics Setup

### What to Track

**Basic:**
- Form views
- Form submissions
- Conversion rate

**Advanced:**
- Field interaction (started typing)
- Field completion (moved to next)
- Field abandonment (where they stopped)
- Error occurrences by field
- Time per field
- Mobile vs. desktop breakdown

### Tools

- Google Analytics 4 (form events)
- Hotjar/FullStory (session recordings)
- Dedicated form analytics (Typeform, HubSpot)
- Google Tag Manager (custom events)

---

## Output Format

### Form Audit Report

```
FORM AUDITED: [Form name/location]
FORM TYPE: [Lead capture/Demo/Contact/etc.]
CURRENT FIELDS: [Count]
CURRENT COMPLETION RATE: [X%]

FIELD-BY-FIELD ANALYSIS:
| Field | Required? | Actually Used? | Recommendation |
|-------|-----------|----------------|----------------|
| Email | Yes | Yes | Keep |
| Phone | Yes | No | Remove or make optional |
| ... | ... | ... | ... |

CRITICAL ISSUES:
1. [Issue] — [Impact] — [Fix]

RECOMMENDED OPTIMIZATIONS:
1. [Change] — [Expected impact]

TEST IDEAS:
1. [Test hypothesis]
```

---

## Questions to Ask

If you need more context:
1. What's the current completion rate?
2. Do you have field-level analytics?
3. What happens with the data after submission?
4. Which fields are actually used in follow-up?
5. What's the mobile vs. desktop split?
6. Are there compliance/legal requirements for certain fields?
7. What's the value of each conversion?

---

## Related Skills

- **page-cro**: For the page containing the form
- **signup-flow-cro**: For registration/signup forms specifically
- **analytics-tracking**: For setting up form tracking
- **ab-test-designer**: For testing form changes
- **marketing-psychology**: For form psychology principles
