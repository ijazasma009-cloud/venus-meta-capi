---
name: photoshoot-factory
description: "Reference-led product and brand photography for ANY brand. Builds and uses a swipe library of REAL brand photoshoots as art direction, then produces either (a) a studio shot list and lighting brief for a real shoot, or (b) photoreal recreated assets when the owner allows AI imagery. Use for 'we need a photoshoot like this competitor', 'product photography', 'email hero image', 'ad creative stills', 'content for the brand', 'recreate this look for our product', 'swipe file', 'moodboard', or when a website or campaign lacks imagery."
---

# Photoshoot Factory

The idea, from the way strong e-commerce teams actually work: nobody invents a great product photograph from a blank page. They screenshot work they admire, send it to a creative director, and recreate the idea for their own product. This skill makes that a system.

## 0. Check the owner's imagery rule first

Read memory and any brand file. Owners fall into three groups:
- **Real only**: no AI imagery at all. Use **Mode A** only.
- **AI allowed if it passes as real**: use Mode A or **Mode B**, and apply the photoreal test below.
- **No rule stated**: ask once, then record the answer in memory.

Never pass off generated imagery as a real photograph of a real event, person or result.

## 1. Build the swipe library (real photographs only)

A reference is only useful if it is a real shoot by a real brand. Collect from brand sites, brand Instagram, ad libraries (Meta Ad Library, TikTok Creative Center), and campaign case studies.
For every reference record: brand, category, source URL, date saved, and tags:
- **Shot type**: hero packshot, in-hand, on-body, flat lay, ingredient or material story, lifestyle scene, scale shot, detail macro, group or range shot, before and after, UGC-style
- **Lighting**: hard sun, soft window, studio softbox, rim or backlight, coloured gel, low key, high key
- **Surface and set**: seamless paper, stone, linen, water, acrylic riser, foliage, architectural, in-context room
- **Colour story** and **crop** (1:1, 4:5, 9:16, 16:9, 3:2)
- **Where it works**: email hero, PDP gallery, paid social, organic feed, website section background

Store as `swipe/<category>/<brand>-<n>.jpg` plus one `swipe/index.json`. References are for direction only. Never publish another brand's photograph.

## 2. Pick references against the job

Start from the placement, not the mood: "email hero, 3:2, needs empty space on the left for a headline" narrows a library fast. Choose 3 to 5 references and write one sentence each on what exactly is being borrowed: the light, the surface, the crop, the prop logic. If you cannot say what you are borrowing, it is not a reference, it is a vibe.

## 3A. Mode A: real shoot brief (default for owners with a studio)

Produce a one-page brief the studio can shoot from:
- **Shot list**: numbered, each with placement, crop, reference image, and the single idea of the frame
- **Set**: surface, backdrop, props with quantities, product count and variants
- **Light**: key position and quality, fill, any rim or gel, time of day if natural
- **Camera**: lens range, height and angle, depth of field
- **Deliverables**: ratios needed per shot, negative-space requirement for text, file naming
- **Do not**: text or logos in frame for background use, mixed colour temperature, props that upstage the product
Group shots so the set changes as few times as possible. A good half-day yields 20 to 40 usable frames.

## 3B. Mode B: recreation with AI (only when the owner allows it)

- Feed the generator the **real product photograph** as the identity reference and the swipe image as the style reference. The product must stay identical: shape, label, colour, proportions. Reject any set where the product drifts between frames.
- Prompt in photographic language: lens, light direction and quality, surface, depth of field, time of day. End with an explicit "no text, no letters, no logos, no watermark" when the image is a background.
- **Photoreal test, every image**: skin with pores not plastic, eyes alive, hands with five fingers, physics-correct shadows and reflections, legible real label or none, no melted props. One failure rejects the image.
- Check the cost before generating a batch and tell the owner what was spent.
- Label generated assets in the file name (`-gen`) and in the asset log so nobody later mistakes them for a shoot.

## 4. Fit for placement

- Website section backgrounds: no text in frame, a calm area where copy will sit, at least 1600px on the long edge, exported as WebP or AVIF under about 250 KB.
- Email heroes: 1200px wide, key subject inside the centre 80 percent, works with images-off alt text.
- Paid social: make 1:1, 4:5 and 9:16 from the same set so the campaign matches.
- Always write alt text that describes the image, and keep a log: asset, source or shoot date, licence or ownership, where it is used.

## 5. For agencies

When the images are for an agency's own site or deck, the brand shown is the client's. Use the client's own photography with permission, spread across the whole roster, and credit nothing you did not make.
