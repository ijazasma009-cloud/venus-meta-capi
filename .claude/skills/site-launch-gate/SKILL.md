---
name: site-launch-gate
description: "Universal pre-launch gate for ANY website or web app, on any stack (WordPress, Shopify, Next.js, static). Runs four checklists with evidence: legal and trust, launch essentials, performance and scale, deployment safety, plus an optional authorized security test. Use before launching or relaunching a site, after a rebuild or migration, when asked 'is this ready to go live', 'pre-launch check', 'launch checklist', 'will this get me sued', 'why is my site slow', or 'pre-deployment checklist'."
---

# Site Launch Gate

A site is not finished when it looks finished. This gate decides whether it can go live.
It is stack-agnostic. Work out the stack first, then check each item the way that stack allows.

## How to run it

1. **Identify the stack and the business type** (brochure site, lead-gen, e-commerce, SaaS/app). Several items only apply to some types. Decide N/A up front and say why.
2. **Check every item with evidence.** Fetch the page, read the header, run the query, open the file. Never mark PASS from memory or from what the code "should" do.
3. **Report as a table**: `Item | Status | Evidence | Fix`. Status is PASS, FAIL, N/A (with reason) or UNVERIFIED (say what access is missing).
4. **Fix the FAILs**, highest risk first, then **re-verify each one on the live URL**, not in the editor.
5. Give a one-line verdict: GO, GO WITH KNOWN ISSUES (list them), or NO GO.

Rules that apply to every section:
- A crawl of every published URL beats spot checks. Status code, title, meta description, H1 count, og:image, broken links and broken images can all be checked in one pass.
- Count things properly. `grep -c` counts lines, not matches. Validate a crawl with a control term before trusting a "clean" result.
- Do not invent a policy, a business detail, a review or a number to make an item pass. Ask the owner.

## A. Legal and trust (20)

| # | Item | How to verify |
|---|------|---------------|
| 1 | Privacy policy | Page exists, linked in footer, names the real data collected and the real processors |
| 2 | Terms of service | Page exists, linked, names the real legal entity |
| 3 | Refund policy | Required if anything is sold. N/A for pure lead-gen, say so |
| 4 | Cookie policy | Lists the cookies actually set. Check with the browser, not the plugin's claims |
| 5 | Cookie consent banner | Non-essential cookies and pixels must not fire before consent. Test in a clean session |
| 6 | Form consents | Every form says what happens to the data. No pre-ticked marketing boxes |
| 7 | No unnecessary data | Each field must have a use. Remove the ones that do not |
| 8 | Third-party SDK audit | List every external script host loaded. Each one is a data processor |
| 9 | No dark patterns | No fake countdowns, no confirm-shaming, no hidden decline |
| 10 | No hidden fees | The price shown is the price charged, including shipping and tax rules |
| 11 | No fake reviews | Every testimonial traceable to a real client who agreed |
| 12 | No unsupported claims | Every number, badge, certification and "partner" logo must be evidenced. Theme demo badges are a common offender |
| 13 | Alt text | Meaningful alt on content images, empty alt on decorative ones |
| 14 | Colour contrast | WCAG AA: 4.5:1 body text, 3:1 large text and UI |
| 15 | Keyboard navigation | Tab through the whole page. Visible focus, no traps, skip link |
| 16 | Business details | Legal name, address, contact. Required in many jurisdictions |
| 17 | Age consent | Only if children's data could be collected. Usually N/A, say so |
| 18 | Unsubscribe link | Every marketing email, working, one click |
| 19 | Licensed fonts and images | Proof of licence for every font and every image. Stock left over from a theme demo is not licensed to the site owner by default |
| 20 | Data deletion request | A stated route for a person to have their data removed |

## B. Launch essentials (20)

1 Privacy policy page. 2 Terms page. 3 **Secrets off the frontend** (search built JS and HTML for keys, tokens, passwords, service URLs with credentials). 4 Force HTTPS (HTTP must 301, check HSTS). 5 Cookie consent banner. 6 Meta titles and descriptions on every URL, unique. 7 **Social preview image** and og:title that match the current positioning, not a leftover. 8 Favicon. 9 Sitemap and robots.txt, sitemap listed in robots, no accidental `Disallow: /`. 10 Alt text. 11 Compress images (modern format, sized to display). 12 Page load speed measured, not assumed. 13 Colour contrast. 14 Mobile friendly at 375px with no horizontal scroll. 15 Custom 404 page that helps. 16 Broken links and broken images: zero. 17 Form validation, client and server. 18 Spam protection (honeypot plus rate limit is enough for small forms). 19 **Analytics installed and receiving data**, plus Search Console verified. 20 **One clear call to action** per page, the same destination throughout.

## C. Performance and scale (20)

Front end: compress images, lazy-load below the fold, split code into chunks, minify JS and CSS, defer non-critical scripts, remove unused dependencies, loading skeletons, debounce input handlers, avoid unnecessary re-renders, paginate large lists.
Delivery: CDN in front and confirm cache HITs (a first request is often a MISS, test twice), server-side caching, cache API responses, compress API payloads.
Data: index the columns the main queries filter on, fix N+1 queries, cache expensive computed results, connection pooling, load balancer when traffic justifies it.
Then **run a Lighthouse audit** on mobile and record LCP, CLS, INP before and after.

Diagnose before optimising. Separate payload size from latency: a 5 KB file that takes 2 seconds is a TTFB or connection problem, not an image problem. Measure HTML weight separately from asset weight. A local `curl` without HTTP/2 overstates per-request latency compared with a real browser.

## D. Deployment safety (10)

1. **Data isolation**: logged in as user A, can you read user B's records? Test it, do not reason about it.
2. **Password reset links expire** (30 minutes is a sane ceiling) and are single use.
3. **Every input sanitised**: parameterised queries, output escaping. SQL injection and XSS tested on every field.
4. **API not open to the world**: CORS restricted to your own origins, auth on every non-public route.
5. **Rate limiting** on login, forms, and any endpoint that costs money.
6. **Custom error screens** for every failure state. No stack traces to users.
7. **Indexes on the high-traffic queries**, and only those.
8. **Logging and monitoring** flowing, with alerts on critical failures.
9. **Rollback plan**: a tested way back (blue-green, previous release, or a verified backup). For WordPress that means a database and files backup taken before the change, and a restore you have actually tried.
10. **Backups exist and restore.**

## E. Security test (optional, authorized targets only)

[Strix](https://github.com/usestrix/strix) is an open-source AI penetration tester: agents attack the running app, prove each finding with a working proof of concept, and propose fixes.

Hard rules:
- Run it **only against systems the user owns or has written permission to test**. Get that confirmation in the conversation first.
- Prefer a **staging copy**. Active testing can create junk records, trigger emails, lock accounts and trip a host's firewall.
- Never point it at a client's production site, a payment flow or a third-party service.
- Treat its output as leads to verify, not as facts. Confirm each finding before reporting it.

Install when needed: `pipx install strix-agent` (needs Docker and an LLM key). It is not installed by default.

## Output

End with the table, the verdict, and the three fixes that matter most. If anything was UNVERIFIED, name the access needed to verify it.
