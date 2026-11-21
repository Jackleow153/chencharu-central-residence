# Speed baseline

Measured 21 November 2026 on the live site, before the Phase 1 changes: headless Chrome, 390 px phone viewport,
cache disabled, no network throttling (LCP is a floor, not a field value). KB = compressed bytes over the wire.

| Page | Requests | Total KB | HTML KB | JS KB | Images KB | Fonts KB | Third-party KB | LCP ms | CLS |
|---|---|---|---|---|---|---|---|---|---|
| / | 5 | 43.8 | 5.0 | 0.0 | 0.0 | 34.1 | 0.0 | 1332 | 0 |
| /price/ | 4 | 42.6 | 4.1 | 0.0 | 0.0 | 34.0 | 0.0 | 1008 | 0 |
| /floor-plans/ | 4 | 41.2 | 3.2 | 0.0 | 0.0 | 34.0 | 0.0 | 836 | 0 |
| /launch-date/ | 4 | 41.2 | 3.1 | 0.0 | 0.0 | 34.0 | 0.0 | 640 | 0 |
| /showflat/ | 4 | 40.9 | 2.9 | 0.0 | 0.0 | 34.0 | 0.0 | 592 | 0 |
| /review/ | 4 | 41.6 | 3.6 | 0.0 | 0.0 | 34.0 | 0.0 | 816 | 0 |
| /location/ | 4 | 42.6 | 4.5 | 0.0 | 0.0 | 34.0 | 0.0 | 564 | 0 |
| /faq/ | 4 | 41.7 | 3.5 | 0.0 | 0.0 | 34.0 | 0.0 | 556 | 0 |
| /register/ | 4 | 40.7 | 2.6 | 0.0 | 0.0 | 34.0 | 0.0 | 572 | 0 |

## What the numbers say
- No JavaScript, no third-party requests, no images on the pages. The font (34 KB, self-hosted, cached a year) is most of the weight.
- Keep it that way: no analytics or tag manager without Jack's decision (CLAUDE.md section 15).

## Changes since the baseline
- 21 Nov 2026 (Phase 1): project schema, FAQ schema, key facts table, related links. HTML grows about 1.1-1.3 KB compressed per page (home 4.8 -> 6.0 KB, price 3.9 -> 5.0 KB); site.css 3.9 -> 4.0 KB. About +3% of total page weight. The share image `assets/og.jpg` (88 KB) is fetched only by social and search previews, not by the pages.

## Limits for future changes
- HTML of a key page: no more than about 10% above the post-Phase-1 size unless the extra is real content.
- No new scripts. Images only as WebP/AVIF with width, height and lazy loading below the fold.
