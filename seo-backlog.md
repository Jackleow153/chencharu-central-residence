# SEO backlog

Ranked by expected impact on the mission (CLAUDE.md section 1). **[Jack]** = needs Jack's decision or input (section 15);
the daily run must not do these alone. Mondays: ship the top speed-safe item without [Jack]. Created 21 November 2026 from the Phase 1 audit.

## Ranked
1. **Pre-build launch sections** (section 14, launch reported for January 2027): price list table on `/price/`, sales results and balance units, all hidden until real data, so each goes live within an hour of release.
2. **[Jack] Privacy page correction** (`ops/flags.md`): approve the proposed wording so the page matches the live site.
3. **[Jack] Timed walk to Khatib MRT** and photos of the route: settles the 330 m / 450 m / 460 m / 6-minute conflict with a first-hand, dated measurement.
4. **Podium / integrated hub analysis** (section 3B): what the bus interchange, 40-stall hawker centre and mall mean for daily life, rents and resale, benchmarked against North Park Residences / Northpoint City and Parktown Residence. Strengthen `/site-plan/` and `/facilities/` first; a separate page only if the analysis is substantial.
5. **School distances from OneMap** (1 km / 2 km bands) on `/schools/`, labelled as measured from the site boundary point, with the MOE caveat.
6. **Price comparison** on `/price/`: The Estuary, The Wisteria, North Park Residences, recent D26/D27 launches and nearby EC supply, from URA caveats.
7. **Upgrader maths** (section 3B): affordability by unit type for Yishun / Chencharu HDB owners; condo vs BTO vs EC trade-offs.
8. **[Jack] Showflat notes and photos** at the preview.
9. **[Jack] Person `sameAs`**: social profiles and YouTube for the author schema.
10. **`Event` schema** for preview and booking once Confirmed.
11. **Comparison pages** (vs North Park Residences, vs EC, vs Lentor launches): only with real analysis, one per comparison.
12. **Contextual link from sellingsgproperty.com** (section 11): from the Chencharu Central Residences Condo Analysis file or a relevant article, not a sitewide footer.
13. **IndexNow**: key file is live at the root after Phase 1; confirm Bing Webmaster Tools accepts submissions.

## Done in Phase 1 (21 Nov 2026)
- Internal files (`CLAUDE.md`, `seo-backlog.md`, `data-sources.md`, `ops/` including the site generator) return 404 via `netlify.toml`; the `chencharu/` working folder (agency ebook PDF, old draft) is git-ignored and never published.
- Generator moved to `ops/` (`build-chencharu.py` + `chencharu_pages.py`); it now refuses to build if a meta description is outside 150-155 characters.
- Project schema (`ApartmentComplex`, aliases, address, geo, tenure, landowners, blocks "not yet released"), `FAQPage` on the FAQ, `datePublished` / `dateModified` on every page and per-page sitemap `lastmod`.
- `og:image` (1200x630, 88 KB text card, no developer imagery), `twitter:card` summary_large_image with title, description and image.
- All meta descriptions 150-155 characters.
- "Four pages" heading fixed to six; form copy matches the form (name and mobile required, unit type optional); nav labels consistent ("Floor plans", "Location" everywhere).
- Tenure added (99-year leasehold, Confirmed); blocks marked "not yet released by the developer" (ebook's 11 blocks of 12 storeys stays Reported).
- Masked "$1.3x million" replaced with "from about $1.3 million (agency guide, not a developer price list)"; only the price page still quotes the ebook's notation to explain it.
- Name status row in the fact ledger; "Also known as" in the home key facts table; FAQ entries for other names and tenure.
- Answer-first openings on the price page and the fact ledger.
- Related pages links (Price, Register, 2-3 related) on 16 pages; robots.txt lists every crawler in section 7; IndexNow key file; 404 page; site.css now versioned (`?v=`).
- Mobile bar: WhatsApp primary (label by page intent) plus a call button; the hero's WhatsApp button hides on phones so the same CTA is never shown twice on one screen; every WhatsApp message names the page.
- Fixed a 2 px sideways scroll on the FAQ page (rotated arrow icon).
