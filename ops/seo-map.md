# SEO map: one search intent, one page

From CLAUDE.md section 4, mapped to the pages that exist on 21 November 2026. Before adding a page, check that it
targets an intent not listed here and has unique substance; otherwise strengthen the mapped page. Pages are built by
`ops/build-chencharu.py` (home) and `ops/chencharu_pages.py` (all others).

| Intent / queries | Page | Notes |
|---|---|---|
| chencharu central residences, chencharu close condo, chencharu condo, chencharu yishun condo, khatib new launch, yishun new launch | `/` | Name status and "Also known as" in the key facts table; schema `alternateName` |
| price, price list, psf, how much | `/price/` | Price list section to pre-build, hidden until release (section 14) |
| floor plan, 2/3/4/5 bedroom, unit mix, sizes | `/floor-plans/` | |
| site plan, blocks | `/site-plan/` | Blocks: not released by the developer |
| facilities | `/facilities/` | |
| integrated development, mall, bus interchange, hawker centre, podium | `/site-plan/` + `/facilities/` for now | Backlog: a dedicated podium page only with real analysis (benchmarks vs Northpoint / Parktown) |
| showflat, preview, booking | `/showflat/` | |
| launch date | `/launch-date/` | |
| balance units, sales results | (create at launch) | Pre-build hidden |
| review, worth buying, pros and cons | `/review/` | |
| vs north park residences, vs chencharu BTO, vs EC, vs Lentor | (none yet) | Backlog: one page per comparison, only with real analysis |
| schools within 1km | `/schools/` | OneMap 1 km / 2 km bands still to add |
| Khatib MRT distance, location, chencharu estate, masterplan | `/location/` | Estate guide section is already on this page |
| developer, Evia, Gamuda Land, Ho Lee | `/developer/` | |
| chencharu close GLS, tender price, land rate | `/price/` (tender table) + `/developer/` | |
| ebook, brochure | `/e-brochure/` | |
| TOP, completion, tenure | `/faq/` + key facts table on `/` | |
| sources, fact check | `/facts/` | Mirrors `data-sources.md` |
| updates, news | `/news/` | |
| register | `/register/` | Conversion page |
| author | `/about/` | |

Not for search: `/privacy/`, `/thank-you/` (noindex), `/404.html` (noindex).
