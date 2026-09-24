# Cinematic scroll: the Apple and Rolex pattern

What those sites actually do, and how to build it on any stack.

## What the pattern is

A tall section (300 to 600vh) holds a `position: sticky` stage that fills the viewport. Scroll position, not time, drives what the stage shows. The visitor is the playhead. Copy fades in and out at set scroll ranges. One idea per scene, a lot of empty space, slow heavy easing, no bounce.

Five devices cover nearly everything on those sites:
1. **Image-sequence scrub**: a product or scene rotates, opens or travels as you scroll. 60 to 150 frames drawn to a `<canvas>`.
2. **Pinned scene with copy stages**: the stage holds still while 3 to 5 lines of copy swap.
3. **Scale and mask reveals**: an image grows from a card to full-bleed, or a headline is a window onto video (`mix-blend-mode` or `background-clip: text`).
4. **Horizontal pan**: vertical scroll drives a horizontal track of case studies or products.
5. **Parallax depth**: foreground, subject and background move at different rates. Two or three layers, small distances.

## The engine

- **Lenis** for smooth scrolling (momentum and consistency across devices). One instance, site-wide.
- **GSAP + ScrollTrigger** for pin and scrub. GSAP is free for commercial use. Drive ScrollTrigger from Lenis's RAF so they never fight.
- Native **CSS scroll-driven animations** (`animation-timeline: view()` / `scroll()`) for simple reveals, with an IntersectionObserver fallback for browsers without support.
- One system per site. Do not mix three scroll libraries.

```js
const lenis = new Lenis({ lerp: 0.085, smoothWheel: true });
lenis.on('scroll', ScrollTrigger.update);
gsap.ticker.add((t) => lenis.raf(t * 1000));
gsap.ticker.lagSmoothing(0);
```

Pinning rules that prevent the usual bugs: `start: "top top"`, `pin: true`, `scrub: 1` (a number, for smoothing), `end: "+=300%"` or a function, `invalidateOnRefresh: true`. Wrap everything in `gsap.context()` and revert on teardown.

## Image-sequence scrub, done properly

- Export frames from the real source film with ffmpeg: `ffmpeg -i in.mp4 -vf "fps=24,scale=1600:-2" -q:v 4 seq/%04d.jpg`, then convert to WebP or AVIF. Aim for 40 to 90 KB a frame on desktop and a half-size set for mobile.
- Draw to canvas with cover-fit maths. Preload frame 1 immediately, the next 10 eagerly, the rest in idle time. Draw the nearest loaded frame if the exact one is not ready.
- Scrubbing `video.currentTime` is tempting and unreliable: it stutters on most mobile browsers because seeking is not frame accurate. Use it only for short desktop-only moments with an all-keyframe encode (`-g 1`).
- Always render a static poster under the canvas so the section works with JavaScript off and for crawlers.

## Pace and copy

- Slow is the luxury signal. Give each scene at least 100vh of scroll. Ease with `power2.out` or `expo.out`. Nothing overshoots.
- Each scene gets one short line (8 words or fewer) and at most one supporting sentence. The real paragraphs live in normal sections between the cinematic ones.
- Alternate intensity: a pinned cinematic scene, then a calm readable section, then another scene. Wall to wall scroll-jacking exhausts people and kills conversion.
- Keep the primary call to action reachable at all times (sticky header button). Never trap a visitor in a long pin with no way to act.

## Performance budget

- LCP under 2.5s: the hero poster is a real `<img>` with `fetchpriority="high"`, preloaded. Attach hero video after load.
- Do not let a lazy-loader or cache plugin lazy-load the logo or hero image. Exclude them.
- Frames load progressively and only when the section is within about two viewports.
- Animate `transform` and `opacity` only. `will-change` on the pinned stage only.
- Test on a mid-range Android phone, not only a laptop. On small screens swap sequences for a single poster plus simple fades when the frame rate drops.

## Accessibility and SEO

- `prefers-reduced-motion: reduce`: no pinning, no scrub, no Lenis. Show posters and let content flow normally.
- Every word is in the initial HTML as real text. The canvas is `aria-hidden`. AI crawlers and search engines do not run the animation.
- Pinned sections must remain keyboard reachable: focusable links inside a scene should not be hidden off-screen by transforms.

## Common failures

- Trigger fires mid-screen: `start` was `"top center"`. Use `"top top"`.
- Jumpy scrub: `scrub: true` with no smoothing. Use `scrub: 1`.
- Layout jump on mobile: used `100vh`. Use `100dvh` or `100svh`.
- Black rectangles: videos with no poster. Extract a poster frame for every film.
- Janky scroll: a `window.addEventListener('scroll')` handler somewhere. Remove it.
- Feels cheap: bounce easing, fast durations, too many things moving at once, or motion with no idea behind it.
