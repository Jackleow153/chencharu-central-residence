# CLAUDE.md — chencharuyishun.sg

Permanent brief for every Claude session on this repo, including the scheduled daily run.
Owner: Jack Leow · PropNex Realty Pte Ltd · CEA R074023I · +65 8062 1538

ALERT_EMAIL: questrepreneur@gmail.com

---

## 1. Mission (priority order)

1. Rank #1 on Google Singapore for this project's name(s) and every related search. The name currently in use is "Chencharu Central Residences" (see section 3C). Related searches include "Chencharu Close condo", "Chencharu condo", "Chencharu Yishun new launch", "Khatib new launch" and "Yishun integrated development".
2. Be the source AI assistants (Google AI Overviews / Gemini, ChatGPT, Claude, Perplexity, Copilot) cite and recommend for this project.
3. Keep price, floor plans, availability and project facts current and verified.
4. Turn visitors into WhatsApp / call / register enquiries to Jack.
5. Never slow the site down. Speed and UX beat every other change. If a change would cost speed, do not ship it. Log it under "Needs Jack's decision".

---

## 2. Project context

Starting point only. Re-verify before relying on any of it. The site's fact ledger is the source of truth.

- **Site:** mixed commercial and residential GLS site at Chencharu Close, Yishun (D27, OCR). HDB is the seller, not URA.
- **Award:** about S$1.013b, which is S$980 psf ppr. Awarded to Evia MCS, Gamuda (Singapore) and H108, trading as Evia Real Estate, Gamuda Land and Ho Lee Group.
- **Tenure and size:** 99-year leasehold. About 875 homes (estimate) above a commercial podium, near Khatib MRT (NS14). Reported to integrate a bus interchange and hawker centre (verify).
- **First mover:** the first private condo in the new Chencharu HDB estate, which plans about 10,000 homes by 2040, at least 80% of them public housing.
- **Previous launches nearby:** the last condo near Khatib was The Estuary (2010). The Wisteria (2016) is mixed-use. The last Yishun launch was The Essence (2019).
- **Price:** analyst estimates range from about S$2,300 to S$2,550 psf. Always label these "Estimate".
- **Launch:** reported for January 2027. Label "Reported" until the developer confirms.

---

## 3. How we win

Google and AI engines reward the source with the most original, accurate, fresh and well-organised information from a credible person. Most competing pages are portal listings and agent pages saying "price coming soon", and several carry conflicting data. Our edge comes from five things.

### A. First and right on every update

Launch is reported for weeks away, not months. When the developer, HDB or the press releases anything, our page is updated, verified and pinged to search engines before anyone else. That includes the official name, preview / showflat dates, price list, floor plans, unit mix, podium details, sales results and balance units.

### B. Information gain specific to this project

- **The integrated hub is the story.** Cover what is in the podium (retail, bus interchange, hawker centre, other facilities) and what it means for daily convenience, rental demand and resale. Benchmark against other integrated OCR projects: North Park Residences / Northpoint City (Yishun) and Parktown Residence (Tampines).
- **Price analysis.** Compare against The Estuary, The Wisteria and North Park Residences, plus recent D26/D27 new launches (Lentor cluster) and nearby EC supply.
- **Upgrader maths.** Yishun and Chencharu HDB owners are the core buyers. Show affordability by unit type, and condo vs BTO vs EC trade-offs.
- **First-hand, measured facts.** Jack supplies these: the timed walk to Khatib MRT (sources currently conflict on the distance), showflat notes and photos, and podium observations. School distances come from OneMap (1 km / 2 km bands for P1 registration).
- **The fact ledger and the "claims we won't repeat as fact" section.** Keep both, and extend them whenever new claims circulate.

Rewording what portals already say is not information gain.

### C. Name and entity protocol (critical for this project)

- Treat "Chencharu Central Residences" as **Reported** until the developer confirms it. Show the name's status in the fact ledger.
- **Aliases** (`ALIASES` in `ops/build-chencharu.py`): Chencharu Close GLS, Chencharu Close condo, Chencharu Close Residences, Chencharu condo, Chencharu Close Residence, Chencharu integrated development, Khatib integrated condo, Khatib new launch condo, Chencharu Grand Residences (an agent marketing name, never used by the developer), Yishun new launch 2027.
  - Put them in one "Also known as" line on the home page.
  - Add one FAQ entry for them.
  - List them in schema `alternateName`.
- **Titles and H1s** pair the reported name with the names people actually search (Google SG autocomplete, 25 Nov 2026): "Chencharu Close condo", "Chencharu condo", "Khatib". Google suggests nothing after "chencharu central residences", so never drop the searched names from titles while the name is unconfirmed. H1s lead with the topic, then the editorial line.
- **Rename protocol.** The moment the developer confirms the official name, or a different name, do all of this in the same run:
  - Update the title tags, H1s, schema `name`, meta descriptions, `llms.txt` and FAQ.
  - Keep every previous name as an alias ("previously referred to as…").
  - The domain does not contain a project name, so URLs never need to change.
  - Push to `main` if the name is confirmed by the developer or HDB, or by 2 reputable sources. Email Jack.
- **Correct circulating errors neutrally.** Portals show conflicting figures (for example 864 vs about 875 units, "1 block", different developer entity names).
  - State the verified figure, its source and its label.
  - Never name or disparage other agents or portals.

### D. Machine-readable

- All key facts are in server-rendered HTML, never only inside JavaScript.
- JSON-LD is on every page.
- Facts are identical everywhere: site, schema, `llms.txt`, fact ledger.
- Every figure carries a date and a source.

### E. Credible author

Jack is visible as the expert: author box on analysis pages, About page, the CEA register verification link, and Person schema with `sameAs` links (sellingsgproperty.com, social profiles, YouTube).

---

## 4. Search demand map

Map each intent to ONE existing page and record the mapping in `ops/seo-map.md`. Before creating a page, confirm it targets a distinct intent and has unique substance. Otherwise strengthen the existing page. No thin, doorway or near-duplicate pages.

| Intent / queries | Page |
|---|---|
| chencharu central residences, chencharu close condo, chencharu condo, chencharu yishun condo, khatib new launch, yishun new launch | Home |
| price, price list, psf, how much | Price |
| floor plan, 2/3/4/5 bedroom, unit mix, sizes | Floor plans and unit mix |
| site plan, facilities, blocks | Site plan / Facilities |
| integrated development, mall, bus interchange, hawker centre, podium, chencharu bus interchange completion date | `/bus-interchange-hawker-centre/` (live 25 Nov 2026) |
| showflat, preview, launch date, booking | Showflat / Launch date |
| balance units, sales results, how many sold | Balance units (create at launch) |
| review, worth buying, pros and cons | Review |
| vs chencharu BTO, chencharu bto price | `/vs-chencharu-bto/` (live 25 Nov 2026; update BTO prices with each Chencharu BTO launch) |
| vs north park residences, vs EC, vs Lentor launches | Comparison pages (one per distinct comparison, only with real analysis) |
| schools within 1km, Khatib MRT distance, location | Schools / Location and MRT |
| developer, Evia, Gamuda Land, Ho Lee | Developer |
| chencharu close GLS, tender price, land rate | GLS / land page or Developer |
| chencharu estate, chencharu masterplan, chencharu yishun | Location (estate guide section) |
| ebook, brochure | What the ebook is |
| TOP, completion, tenure | FAQ + key facts table |

---

## 5. Accuracy rules

- **Primary sources:**
  - the developer's official material
  - HDB (the seller of this site) and URA
  - Gamuda Berhad's announcements on Bursa Malaysia (a listed partner, so its filings carry project details)
- **Otherwise,** a fact must match in 2 independent reputable sources: Business Times, Straits Times, EdgeProp, Stacked Homes, 99.co editorial, PropertyGuru editorial, ERA / PropNex / CBRE research.
- **Portal project pages and agent listings are NOT sources.** For this project they already conflict on units, blocks and developer.
- **Labels:** every fact is Confirmed / Reported / Estimate, consistent with the fact ledger.
- **Record** source and date for every changed figure in the commit message and in `data-sources.md`.
- **If sources conflict or are unclear,** do NOT publish that item. Treat it per section 13.

---

## 6. Freshness rules

- Update "Last checked", `dateModified` and sitemap `lastmod` ONLY when the page content materially changed.
- Never bump dates to fake freshness. Google treats that as manipulation.
- Put month + year in a title only for time-sensitive pages that truly changed that month.

---

## 7. Technical SEO and AI-visibility checklist

- **JSON-LD on every page**, matching the visible content:
  - `WebSite`
  - `RealEstateAgent` + `Person` for Jack
  - `ApartmentComplex` / `Residence` for the project: name, `alternateName`, address, geo, `numberOfAccommodationUnits` (only when Confirmed), developer, tenure in description
  - `BreadcrumbList`
  - `FAQPage` where there are FAQs
  - `Event` for preview / launch, only once official dates are Confirmed
- **Validate** JSON-LD parses as valid JSON on every build.
- **Meta tags:**
  - Meta descriptions 150–155 characters.
  - Unique `og:description` where useful.
  - A compressed 1200×630 `og:image`.
  - Twitter card `summary_large_image`.
  - Consistent nav labels.
- **robots.txt** must allow Googlebot, Bingbot, Google-Extended, OAI-SearchBot, GPTBot, ChatGPT-User, ClaudeBot, Claude-SearchBot, Claude-User, PerplexityBot and Applebot-Extended.
- **Discovery:**
  - `sitemap.xml` with accurate `lastmod`
  - IndexNow key file at the site root; ping IndexNow after each deploy (Bing's index feeds several AI assistants)
  - `/llms.txt` with the key facts table, name status, aliases and links to the fact ledger, price, floor plans and FAQ
- **Canonical** tag on every page. No duplicate content across pages.
- **Internal links:** every page links to Price, Register and its two or three most related pages, with descriptive anchor text.
- **Answer-first writing:** each page opens with a 2–3 sentence direct answer containing the key figure and its date, then the detail. FAQs answer in the first sentence.
- **Never deploy internal files:** `CLAUDE.md`, `seo-backlog.md`, `data-sources.md` and `ops/` must never be publicly served. Use the Netlify publish directory or a 404 rule.

---

## 8. Speed rules (non-negotiable)

- Baseline is recorded in `ops/perf-baseline.md`: page weight per key page, number of requests, JS size.
- No change may make a page meaningfully heavier than baseline. New content images are fine if optimised.
- Targets on mobile: LCP < 2.5 s, CLS < 0.1, INP < 200 ms.
- No new JS frameworks, libraries, trackers, chat widgets or third-party embeds unless Jack approves.
- **Images:** WebP/AVIF, explicit width and height, `srcset`, lazy-load below the fold, preload only the hero.
- **Maps:** static image linking to Google Maps, never an iframe on load.
- **Video:** click-to-load facade, never a YouTube iframe on load.
- **Fonts:** system fonts, or self-hosted woff2 with `font-display: swap`.
- **CSS/JS:** inline critical CSS. Defer all JS. Calculators and forms must not block rendering, and the content must read fine without JS.

---

## 9. Conversion rules

- **CTA:** WhatsApp is the primary CTA, in a sticky bottom bar on mobile (pure HTML/CSS). The pre-filled message names the page, e.g. "Hi Jack, I'm on the Chencharu price page…".
- **CTA wording** matches page intent: Price page → "WhatsApp me the price list when it's out". Floor plans → "Send me the layouts in my budget".
- **Repetition:** the same CTA appears at most once per screen. Repeated identical CTAs read as noise.
- **Forms:** 3 fields maximum. The copy must match the form (never say "two fields" over four inputs).
- **Never gate key facts** behind registration or the ebook, because Google and AI can't read gated content.
- **Keep visible:** the CEA verification link and the "independent site, not the developer, not an offer of sale" disclaimer.

---

## 10. Trust and compliance

- Never claim or imply this is the developer's official site.
- Agent details on every page: Jack Leow, PropNex Realty Pte Ltd, CEA R074023I, agency licence L3008022J, +65 8062 1538.
- No exaggerated claims ("guaranteed", "best investment", "confirm profit").
- Analysis is balanced, with pros AND cons. The site's voice is "the price is not proven yet": evidence first, never hype.
- Never present a masked or partial figure ("$1.3x million") as if it were data. Show the reported figure with its source and label, e.g. "from about S$1.3 million (agent guide, not a developer price list)", or leave it out.

---

## 11. Linking between Jack's sites

- Link to this site from sellingsgproperty.com with contextual links inside relevant articles, not sitewide footers.
- No sitewide cross-links between Jack's project microsites. That pattern looks like a link scheme. Link to another project site only where it is genuinely relevant to the reader.

---

## 12. Daily update procedure (the scheduled task runs this)

1. Read this file, `data-sources.md`, `ops/flags.md` and `seo-backlog.md`.
2. **Research** the latest on this project: official name, developer announcements, Gamuda Bursa filings, HDB updates, preview / showflat / launch dates, price list and psf, floor plans and unit mix, podium / bus interchange / hawker centre details, units sold and balance units, TOP / completion, news. Search under every name and alias in section 3C.
3. **Name check:** if an official name is confirmed or has changed, run the rename protocol (section 3C). Also look for the name on primary records: the developer's housing developer licence (one report says it was issued on 30 September 2026) and URA's developer sales records. A name on a licence or URA record counts as confirmed by a primary source.
4. **Compare** with what the site currently says.
5. **Verify** every difference per section 5.
6. **Apply** verified changes: page content, fact ledger, key facts table, schema, FAQ, `llms.txt`, `data-sources.md`, dates and `lastmod` (per section 6).
7. **Check:** run the build if there is one. Confirm it passes, JSON-LD parses, and page weight is within the speed rules.
8. **Push:**
   - Every change verified and every check passes → commit and push to `main`.
   - Anything unverified, or any check fails → push to a `claude/` branch and leave `main` untouched.
9. **After pushing to `main`:**
   - Fetch the live page until it shows the change (retry for up to 10 min).
   - Ping IndexNow with the changed URLs.
10. **Mondays only, SEO step:**
    - Web-search the core queries from section 4 and note who ranks and what they cover that we don't.
    - Update `seo-backlog.md`.
    - Then ship ONE highest-impact, speed-safe backlog item. That counts as a change.
11. **Email** per section 13.

**Commit format:** `data: <what changed> (source: <name>, <date>)` or `seo: <what changed>`.

---

## 13. Email rule (Jack's instruction: email ONLY when there are changes to be made)

**Send an email to ALERT_EMAIL via the Gmail connector ONLY when:**
- a change was pushed to `main`, or
- a change is waiting on a `claude/` branch for Jack's approval. This includes a figure on the site that sources now contradict: propose the correction on a branch.

**NEVER send** "no changes", status, summary or "all good" emails. Changes only to internal files (`seo-backlog.md`, `data-sources.md`, `ops/`) do not count.

A conflict or open question with no proposed change goes in `ops/flags.md`. Include it in the next change email.

**Email format:**
- Subject: `Chencharu site: <n> change(s)`
- Body: each change as old → new, page URL, source links. Then what's waiting on a branch and why. Then open flags.

---

## 14. Launch-window playbook (launch reported for January 2027, so this starts now)

**Now:**
- Pre-build empty, ready-to-fill sections for the price list, balance units and sales results, so each can go live within an hour of release.
- Keep them hidden until there is real data. No placeholder pages indexed.

**When a preview date is Confirmed:** in that change email, remind Jack to switch the schedule to every 2–3 hours (`/schedule update`) from the week before preview until the weekend after booking day. Then switch back to daily.

**Launch day:** publish the sales take-up ("X% sold at an average $Y psf") as soon as the developer or the press reports it, with the source. Compare it with the launch-weekend take-up of other integrated projects.

**After launch:**
- Balance units weekly.
- Monthly transaction analysis from URA caveat data: price by stack and floor, psf vs North Park Residences and other D27 comparables.

---

## 15. Needs Jack's decision (log in `ops/flags.md`, never do automatically)

- Adding or removing third-party scripts, analytics or tags
- Paid tools or services
- Changing the domain, URL structure or redirects
- Deleting pages
- Anything legal or compliance-related
- Using developer logos, renders or brochure content when permission is unclear

---

## 16. Phase 1 (one-time, run when this file is first added)

1. Audit the whole site against this file.
2. Record the speed baseline in `ops/perf-baseline.md`.
3. Build `ops/seo-map.md` (section 4).
4. Make sure internal files are not publicly served (section 7).
5. Fix these known issues:
   - no JSON-LD
   - no `og:image`; Twitter card is "summary" with no title, description or image
   - meta description too long
   - "Four pages…" heading above six cards
   - form copy says "Two fields" over four inputs
   - inconsistent nav labels ("Floor plans" vs "Floor plans and unit mix", "Location" vs "Location and MRT")
   - tenure not stated (verify and add)
   - blocks not stated (add, or mark "not yet released")
   - masked "$1.3x million" price (fix per section 10)
   - no machine-readable published / modified dates
   - name status not shown in the fact ledger
6. Also fix everything else that is safe now: alias line, answer-first openings, internal links, `robots.txt`, `llms.txt`, IndexNow key, sticky WhatsApp bar, CTA de-duplication.
7. Put everything else in `seo-backlog.md`, ranked by expected impact. Mark items that need Jack, such as first-hand MRT walk timing and showflat photos.
8. Show the diff before committing.
