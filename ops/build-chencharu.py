#!/usr/bin/env python3
"""Builds the whole chencharuyishun.sg site: every page, sitemap.xml, llms.txt, llms-full.txt, facts.json,
robots.txt, 404.html and the IndexNow key file. Run: python3 ops/build-chencharu.py, then commit the output.
Page bodies are in ops/chencharu_pages.py. Never hand-edit the generated HTML: the next build overwrites it."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]   # repo root; this script lives in ops/ (never served)
HOST = "https://chencharuyishun.sg"
CSS_V = "0"
UPDATED = "2026-11-18"          # facts last checked (byline); change only after re-verifying
PUBLISHED = "2026-11-18"
# dateModified / sitemap lastmod per page: bump only when that page's content materially changes (CLAUDE.md section 6)
MODIFIED = {"/": "2026-11-25", "/price/": "2026-11-21", "/facts/": "2026-11-25", "/faq/": "2026-11-25",
            "/location/": "2026-11-25", "/bus-interchange-hawker-centre/": "2026-11-25", "/vs-chencharu-bto/": "2026-11-25",
            "/launch-date/": "2026-11-23", "/news/": "2026-11-23",
            "/register/": "2026-11-21", "/review/": "2026-11-25",
            "/privacy/": "2026-11-22"}
INDEXNOW_KEY = "5d0c7a91e4b24f3c8a6e2b17f9d4c380"
ALIASES = ["Chencharu Close GLS", "Chencharu Close condo", "Chencharu Close Residences", "Chencharu condo",
           "Chencharu Close Residence", "Chencharu integrated development", "Khatib integrated condo",
           "Khatib new launch condo", "Chencharu Grand Residences", "Yishun new launch 2027"]
AKA = ", ".join(ALIASES[:-1]) + " and " + ALIASES[-1]
GEO = (1.41522, 103.82915)   # OneMap point for Chencharu Close (road), 21 Nov 2026
CHECKED = "18 November 2026"
PHONE = "+65 8062 1538"
WA = "https://wa.me/6580621538?text=Hi%20Jack%2C%20I%27d%20like%20the%20Chencharu%20Central%20Residences%20price%20list%20and%20floor%20plans%20when%20a%20developer%20list%20is%20out."

C = '<span class="chip c" title="From HDB, LTA, a company filing, or a named news report">Confirmed</span>'
R = '<span class="chip r" title="From an agency guide or one third-party report. It can change.">Reported</span>'
E = '<span class="chip e" title="Arithmetic on published figures, or an analyst comment. Not a price list.">Estimate</span>'

NAV = [
    ("/price/", "Price"),
    ("/floor-plans/", "Floor plans"),
    ("/site-plan/", "Site plan"),
    ("/location/", "Location"),
    ("/showflat/", "Showflat"),
    ("/review/", "Review"),
]
MORE = [
    ("/", "Overview"),
    ("/price/", "Price"),
    ("/floor-plans/", "Floor plans"),
    ("/site-plan/", "Site plan"),
    ("/bus-interchange-hawker-centre/", "Bus interchange & hawker"),
    ("/facilities/", "Facilities"),
    ("/location/", "Location"),
    ("/schools/", "Schools"),
    ("/showflat/", "Showflat"),
    ("/launch-date/", "Launch date"),
    ("/developer/", "Developer"),
    ("/review/", "Review"),
    ("/vs-chencharu-bto/", "Condo vs BTO"),
    ("/facts/", "Fact ledger"),
    ("/faq/", "FAQ"),
    ("/e-brochure/", "What the ebook is"),
    ("/news/", "Updates"),
]

LOGO = '''<svg viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="8" fill="currentColor"/><path d="M8 22V14M14 22V10M20 22V13" stroke="#F4F1EB" stroke-width="2.2" stroke-linecap="round"/><rect x="7" y="23" width="18" height="3" rx="1" fill="#8C6A3D"/></svg>'''


def form(name):
    return f'''<form name="{name}" method="POST" action="/thank-you/" data-netlify="true" netlify-honeypot="bot-field">
<input type="hidden" name="form-name" value="{name}">
<p hidden><label>Leave this empty <input name="bot-field"></label></p>
<div class="row2"><div><label for="{name}-name">Name</label><input id="{name}-name" name="name" type="text" autocomplete="name" required></div>
<div><label for="{name}-mobile">Mobile</label><input id="{name}-mobile" name="mobile" type="tel" autocomplete="tel" inputmode="tel" placeholder="8-digit number" required></div></div>
<div><label for="{name}-type">Unit you are considering</label><select id="{name}-type" name="unit"><option value="">Not sure yet</option><option>2-bedroom</option><option>3-bedroom</option><option>4-bedroom</option><option>5-bedroom</option></select></div>
<label class="consent"><input type="checkbox" name="consent" value="yes" required><span>Contact me about Chencharu Central Residences. I have read the <a href="/privacy/">privacy note</a>.</span></label>
<button class="btn" type="submit">Send me the price list when it is out</button>
<p class="fine">Name and mobile are required. The unit type is optional. No reservation is made. This is not the developer's site.</p>
</form>'''


def faq_ld(body):
    import re, json
    qs = []
    for q, a in re.findall(r'<details[^>]*><summary>(.*?)</summary><p>(.*?)</p></details>', body, re.S):
        a = re.sub(r'<span class="chip[^"]*"[^>]*>.*?</span>', '', a)
        a = re.sub(r'<[^>]+>', '', a).replace('&amp;', '&').strip()
        qs.append({"@type": "Question", "name": re.sub(r'<[^>]+>', '', q), "acceptedAnswer": {"@type": "Answer", "text": a}})
    return qs


PROJECT_LD = {
    "@type": ["ApartmentComplex", "Residence"], "@id": HOST + "/#project",
    "name": "Chencharu Central Residences", "alternateName": ALIASES,
    "description": ("Reported marketing name, not yet confirmed by the developer, for the 99-year leasehold mixed-use development "
                    "at Chencharu Close, Yishun (District 27), Singapore. HDB awarded the site on 26 September 2025 to Evia MCS, "
                    "Gamuda (Singapore) and H108. Homes are planned above a bus interchange, a hawker centre and shops, within "
                    "450 m of Khatib MRT (NS14). HDB estimated about 875 homes; the developer has not confirmed a number."),
    "url": HOST + "/",
    "address": {"@type": "PostalAddress", "streetAddress": "Chencharu Close", "addressLocality": "Yishun",
                "addressRegion": "District 27", "addressCountry": "SG"},
    "geo": {"@type": "GeoCoordinates", "latitude": GEO[0], "longitude": GEO[1]},
    "containedInPlace": {"@type": "Place", "name": "Chencharu, Yishun, Singapore"},
    "additionalProperty": [
        {"@type": "PropertyValue", "name": "Tenure", "value": "99-year leasehold (excludes the bus interchange and hawker centre land)"},
        {"@type": "PropertyValue", "name": "Land sale", "value": "Awarded by HDB on 26 September 2025 for S$1,012,588,989.89, about S$980 psf ppr"},
        {"@type": "PropertyValue", "name": "Landowners", "value": "Gamuda (Singapore) 50%, Evia MCS 30%, H108 20% (Gamuda Berhad filing, 29 September 2025)"},
        {"@type": "PropertyValue", "name": "Nearest MRT", "value": "Khatib (NS14), North-South Line; within 450 m per Gamuda's filing"},
        {"@type": "PropertyValue", "name": "Blocks", "value": "Not yet released by the developer"},
        {"@type": "PropertyValue", "name": "Expected launch", "value": "End of January 2027 (Reported, agency ebook); first-quarter 2027 target (Reported, The Star and EdgeProp Malaysia)"},
        {"@type": "PropertyValue", "name": "HDB project completion period", "value": "84 months from 26 September 2025, to September 2032"}],
}


def head(title, desc, path, crumbs_ld, body=""):
    import json
    url = HOST + path
    mod = MODIFIED.get(path, PUBLISHED)
    graph = [
        {"@type": "WebSite", "@id": HOST + "/#website", "url": HOST + "/", "name": "Chencharu Central Residences Guide", "inLanguage": "en-SG",
         "publisher": {"@id": HOST + "/#jack"}, "about": {"@id": HOST + "/#project"}},
        {"@type": "Person", "@id": HOST + "/#jack", "name": "Jack Leow", "telephone": PHONE, "jobTitle": "Property agent",
         "url": "https://sellingsgproperty.com", "sameAs": ["https://sellingsgproperty.com"],
         "identifier": {"@type": "PropertyValue", "propertyID": "CEA Registration", "value": "R074023I"}, "worksFor": {"@id": HOST + "/#agency"}},
        {"@type": "RealEstateAgent", "@id": HOST + "/#agency", "name": "PropNex Realty Pte Ltd",
         "identifier": {"@type": "PropertyValue", "propertyID": "CEA Licence", "value": "L3008022J"}, "areaServed": "Singapore"},
        PROJECT_LD,
        {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": title, "description": desc, "inLanguage": "en-SG",
         "datePublished": PUBLISHED, "dateModified": mod, "isPartOf": {"@id": HOST + "/#website"}, "about": {"@id": HOST + "/#project"},
         "author": {"@id": HOST + "/#jack"}, "breadcrumb": {"@type": "BreadcrumbList", "itemListElement": json.loads(crumbs_ld)}},
    ]
    faqs = faq_ld(body)
    if faqs:
        graph.append({"@type": "FAQPage", "@id": url + "#faq", "mainEntity": faqs})
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False).replace("</", "<\\/")
    return f'''<!doctype html>
<html lang="en-SG">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="author" content="Jack Leow, CEA R074023I">
<meta name="theme-color" content="#F4F1EB">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Chencharu Central Residences Guide">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="en_SG">
<meta property="og:image" content="{HOST}/assets/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Chencharu Central Residences independent guide: Chencharu Close, Yishun, near Khatib MRT">
<meta property="article:published_time" content="{PUBLISHED}">
<meta property="article:modified_time" content="{mod}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{HOST}/assets/og.jpg">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="/assets/fonts/hanken-grotesk-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css?v={CSS_V}">
<script type="application/ld+json">{ld}</script>
</head>
'''


def header(current):
    desk = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == current else ""
        desk.append(f'<a href="{href}"{cur}>{label}</a>')
    sheet = []
    for href, label in MORE:
        sheet.append(f'<a href="{href}">{label}</a>')
    return f'''<body>
<a class="skip" href="#main">Skip to content</a>
<header class="hdr"><div class="wrap">
<a class="logo" href="/">{LOGO}Chencharu Central</a>
<nav class="nav" aria-label="Main">{''.join(desk)}</nav>
<a class="btn" href="/register/">Get the price list</a>
</div></header>
<input id="nav-toggle" class="nav-toggle" type="checkbox" aria-label="Open the menu">
<label class="menubtn" for="nav-toggle"><span></span></label>
<nav class="sheet" aria-label="Mobile">{''.join(sheet)}<a class="btn" href="/register/">Get the price list</a><a class="btn wa" href="{WA}">WhatsApp Jack</a></nav>
<main id="main">
'''


def footer():
    return f'''</main>
<footer><div class="wrap">
<div><h2>About this guide</h2><p>An independent English guide to Chencharu Central Residences at Chencharu Close, Yishun. Written by Jack Leow, CEA R074023I, PropNex Realty Pte Ltd, licence L3008022J.</p><p><a href="tel:+6580621538">{PHONE}</a></p></div>
<div><h2>Decide</h2><ul><li><a href="/price/">Price</a></li><li><a href="/floor-plans/">Floor plans</a></li><li><a href="/showflat/">Showflat</a></li><li><a href="/launch-date/">Launch date</a></li><li><a href="/review/">Review</a></li></ul></div>
<div><h2>Check</h2><ul><li><a href="/facts/">Fact ledger</a></li><li><a href="/location/">Location</a></li><li><a href="/site-plan/">Site plan</a></li><li><a href="/schools/">Schools</a></li><li><a href="/developer/">Developer</a></li></ul></div>
<div><h2>Contact</h2><ul><li><a href="/register/">Register</a></li><li><a href="{WA}">WhatsApp</a></li><li><a href="/about/">About</a></li><li><a href="/privacy/">Privacy</a></li><li><a href="/faq/">FAQ</a></li></ul></div>
<p class="legal">Not the developer's website and not an offer of sale. Guide prices in the PropNex agency ebook are not a developer price list. Figures are labelled Confirmed, Reported or Estimate. Last checked {UPDATED}. PropNex Realty Pte Ltd, CEA licence L3008022J. Salesperson Jack Leow (Leow Thai Chee), CEA R074023I.</p>
</div></footer>
<div class="mbar"><a class="btn wa" href="{WA}">{{MBAR_LABEL}}</a><a class="call" href="tel:+6580621538" aria-label="Call Jack on {PHONE}"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path fill="currentColor" d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z"/></svg></a></div>
</body></html>
'''


WA_NAME = {"/": "home", "/price/": "price", "/floor-plans/": "floor plans", "/site-plan/": "site plan", "/location/": "location",
           "/showflat/": "showflat", "/launch-date/": "launch date", "/facilities/": "facilities", "/schools/": "schools",
           "/review/": "review", "/developer/": "developer", "/facts/": "fact ledger", "/faq/": "FAQ", "/register/": "registration",
           "/e-brochure/": "ebook", "/news/": "updates", "/about/": "about", "/privacy/": "privacy", "/thank-you/": "thank-you",
           "/404.html": "home",
           "/bus-interchange-hawker-centre/": "bus interchange", "/vs-chencharu-bto/": "condo vs BTO"}
ANCH = {"/price/": "Chencharu Central Residences price: land bid and agency guide prices", "/register/": "Register for the developer price list and floor plans",
        "/floor-plans/": "Unit mix: about 875 homes, 527 to 1,389 sq ft", "/site-plan/": "Site plan: the GFA split, podium and height limit",
        "/facilities/": "Bus interchange, hawker centre and reported facilities", "/location/": "Location: Khatib MRT and the Chencharu estate",
        "/schools/": "Schools named near Chencharu Close", "/showflat/": "Showflat: what has and has not been confirmed",
        "/launch-date/": "Launch date: the reported January 2027 window", "/review/": "Independent review: pros, cons and who it suits",
        "/developer/": "Developer: Gamuda, Evia and H108 shareholdings", "/facts/": "Fact ledger: every figure with its source",
        "/faq/": "Chencharu Central Residences FAQ", "/news/": "Latest updates, newest first", "/e-brochure/": "What the agency ebook is",
        "/bus-interchange-hawker-centre/": "Chencharu bus interchange and hawker centre", "/vs-chencharu-bto/": "Chencharu condo vs Chencharu BTO"}
REL = {"/price/": ["/floor-plans/", "/review/", "/developer/"], "/floor-plans/": ["/site-plan/", "/review/", "/facilities/"],
       "/site-plan/": ["/bus-interchange-hawker-centre/", "/facilities/", "/floor-plans/"], "/location/": ["/schools/", "/bus-interchange-hawker-centre/", "/vs-chencharu-bto/"],
       "/showflat/": ["/launch-date/", "/floor-plans/", "/news/"], "/launch-date/": ["/showflat/", "/news/", "/faq/"],
       "/facilities/": ["/bus-interchange-hawker-centre/", "/site-plan/", "/review/"], "/schools/": ["/location/", "/faq/", "/review/"],
       "/review/": ["/facts/", "/location/", "/floor-plans/"], "/developer/": ["/facts/", "/review/", "/news/"],
       "/facts/": ["/faq/", "/news/", "/review/"], "/faq/": ["/facts/", "/launch-date/", "/review/"],
       "/register/": ["/floor-plans/", "/launch-date/", "/review/"], "/e-brochure/": ["/facts/", "/floor-plans/", "/price/"],
       "/news/": ["/launch-date/", "/facts/", "/review/"],
       "/bus-interchange-hawker-centre/": ["/site-plan/", "/location/", "/review/"], "/vs-chencharu-bto/": ["/review/", "/floor-plans/", "/location/"], "/about/": ["/facts/", "/review/", "/news/"]}


def wa_url(path):
    from urllib.parse import quote
    ask = {"/price/": "Please WhatsApp me the price list when it's out.", "/floor-plans/": "Please send me the layouts in my budget."}.get(
        path, "I'd like the price list and floor plans when the developer releases them.")
    return "https://wa.me/6580621538?text=" + quote(f"Hi Jack, I'm on the Chencharu {WA_NAME[path]} page. {ask}", safe="")


def related(path):
    if path not in REL:
        return ""
    links = [k for k in ["/price/"] + REL[path] + ["/register/"] if k != path]
    return ('<section class="related"><div class="read"><h2>Related pages</h2><ul>'
            + "".join(f'<li><a href="{k}">{ANCH[k]}</a></li>' for k in links) + '</ul></div></section>\n')


def write_page(path, title, desc, crumb, body, current):
    crumbs = [
        {"@type": "ListItem", "position": 1, "name": "Chencharu Central Residences", "item": HOST + "/"}
    ]
    if path != "/":
        crumbs.append({"@type": "ListItem", "position": 2, "name": crumb, "item": HOST + path})
    import json
    if path not in ("/thank-you/", "/404.html"):
        assert 150 <= len(desc) <= 155, f"{path}: meta description is {len(desc)} characters; CLAUDE.md section 7 needs 150-155"
    label = {"/price/": "WhatsApp me the price list", "/floor-plans/": "Send me layouts in my budget"}.get(path, "WhatsApp Jack")
    html = head(title, desc, path, json.dumps(crumbs), body) + header(current) + body + related(path) + footer().replace("{MBAR_LABEL}", label)
    html = html.replace(WA, wa_url(path))
    if path in ("/thank-you/", "/404.html"):
        html = html.replace('content="index,follow,max-image-preview:large"', 'content="noindex"')
    if path == "/404.html":
        html = html.replace(f'<link rel="canonical" href="{HOST}/404.html">\n', "")
        dest = ROOT / "404.html"
    else:
        dest = ROOT / "index.html" if path == "/" else ROOT / path.strip("/") / "index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html, encoding="utf-8")
    return dest


def legend():
    return f'<p class="legend"><span>{C} HDB, LTA, a filing, or named press</span><span>{R} Agency guide or one report. It can change.</span><span>{E} Arithmetic or an analyst comment</span></p>'


def byline():
    return f'<p class="byline"><span>By <b>Jack Leow</b>, CEA R074023I</span><span>Last checked <time datetime="{UPDATED}">{CHECKED}</time></span></p>'


HOME = f'''
<section class="hero"><div class="wrap">
<p class="pill">Launch window reported for the end of January 2027</p>
<p class="eyebrow">Chencharu Close condo · Khatib · Yishun · District 27 · Outside Central Region</p>
<h1>Chencharu Central Residences</h1>
<p class="value">Read the land price, the unit mix and the corrections before you treat a guide price as a price list.</p>
<p class="lede">A 99-year leasehold mixed-use site at Chencharu Close, awarded by HDB on 26 September 2025 for $1,012,588,989.89. Homes are planned above a bus interchange, a hawker centre and shops, near Khatib MRT. No developer price list was found as of 18 November 2026.</p>
<div class="btns"><a class="btn wa" href="{WA}">WhatsApp Jack</a><a class="btn ghost" href="/price/">See the land price and guide prices</a></div>
<p class="reassure">Independent guide. Not the developer. Same new-launch list price is the usual market practice. Buyers pay no agent fee on a developer sale. {R}</p>
</div></section>
<div class="wrap"><div class="stats">
<div class="stat"><b>875</b><span>homes in the current guide {R}</span></div>
<div class="stat"><b>$980</b><span>land rate, psf ppr {C}</span></div>
<div class="stat"><b>NS14</b><span>Khatib, one stop to Yishun {C}</span></div>
<div class="stat"><b>End Jan 2027</b><span>ebook launch window {R}</span></div>
</div>
<p class="trust"><span>Every figure labelled</span><span>CEA R074023I</span><span>PropNex Realty Pte Ltd</span><span>No countdown, no popup</span></p>
<div class="tbl keyfacts"><table class="ledger"><caption>Key facts, checked {CHECKED}</caption><tbody>
<tr><th scope="row">Name</th><td>Chencharu Central Residences, the marketing name in use. Not yet confirmed by the developer. {R}</td></tr>
<tr><th scope="row">Also known as</th><td>{AKA}.</td></tr>
<tr><th scope="row">Tenure</th><td>99-year leasehold. The lease excludes the bus interchange and hawker centre land. {C}</td></tr>
<tr><th scope="row">Land price</th><td>$1,012,588,989.89, about $980 psf ppr, awarded by HDB on 26 September 2025. {C}</td></tr>
<tr><th scope="row">Landowners</th><td>Gamuda (Singapore) 50%, Evia MCS 30%, H108 20%. {C}</td></tr>
<tr><th scope="row">Homes</th><td>About 875. HDB's estimate, which it said may vary. {R}</td></tr>
<tr><th scope="row">Blocks</th><td>Not yet released by the developer. An agency ebook reports 11 blocks of 12 storeys. {R}</td></tr>
<tr><th scope="row">Nearest MRT</th><td>Khatib (NS14), within 450 m according to Gamuda's filing. {C}</td></tr>
<tr><th scope="row">Launch</th><td>End of January 2027, from an agency ebook. The Star and EdgeProp Malaysia report a first-quarter 2027 target. Not a developer date. {R}</td></tr>
<tr><th scope="row">Completion</th><td>HDB's project completion period runs to September 2032. No TOP date published. {C}</td></tr>
</tbody></table></div></div>

<section class="sec"><div class="wrap grid2">
<div><p class="eyebrow">Where this stands</p><h2>The podium is the product. The price is not proven yet.</h2></div>
<div><p>HDB sold this as the first private-housing site in the new Chencharu precinct, and required a bus interchange and a hawker centre on it. That is a different building from a normal condominium plot. <a href="/bus-interchange-hawker-centre/">What the bus interchange and hawker centre requirements say</a>.</p>
<p>What is not proven is the selling price. A PropNex agency ebook dated 16 November 2026 prints guide prices from about $1.3 million for a two-bedroom (agency guide, not a developer price list). Several agent sites are already presenting those figures as a developer price list.</p>
<p><a class="more" href="/review/">Read the review</a></p>{legend()}</div>
</div></section>

<section class="sec tint"><div class="wrap">
<div class="sec-head"><p class="eyebrow">Six pages that answer a search</p><h2>Price, floor plans, showflat, launch date, location and site plan</h2>
<p>Each is its own page, so a result can point at the question rather than a single sales screen.</p></div>
<div class="cards">
<a class="card" href="/price/"><b>Price</b><span>The $980 psf ppr land bid, the three-bid gap, and what the agency guide prices do and do not mean.</span><em>Read</em></a>
<a class="card" href="/floor-plans/"><b>Floor plans</b><span>875 homes in nine reported types, from 527 to 1,389 sq ft. No official plans yet.</span><em>Read</em></a>
<a class="card" href="/showflat/"><b>Showflat</b><span>No confirmed gallery address. One agent page names Yishun Ring Road and marks it TBC.</span><em>Read</em></a>
<a class="card" href="/launch-date/"><b>Launch date</b><span>Ebook: end of January 2027. Other pages disagree on 16 and 30 January.</span><em>Read</em></a>
<a class="card" href="/location/"><b>Location</b><span>Khatib NS14. Orchard is 8 stops. Raffles Place is 12, not 13.</span><em>Read</em></a>
<a class="card" href="/site-plan/"><b>Site plan</b><span>How the GFA splits between homes, shops, the hawker centre and the interchange.</span><em>Read</em></a>
</div></div></section>

<section class="sec"><div class="wrap">
<div class="sec-head"><p class="eyebrow">Do not copy these</p><h2>Claims already circulating that this guide will not repeat as fact</h2></div>
<div class="tbl"><table>
<thead><tr><th>Claim seen elsewhere</th><th>What the sources actually support</th></tr></thead>
<tbody>
<tr><td>13 stops from Khatib to Raffles Place</td><td>NS14 to NS26 is 12 stops: Yio Chu Kang, Ang Mo Kio, Bishan, Braddell, Toa Payoh, Novena, Newton, Orchard, Somerset, Dhoby Ghaut, City Hall, Raffles Place. {C}</td></tr>
<tr><td>North-South Corridor from 2029, cutting journeys by up to 30 minutes</td><td>LTA said in September 2026 that the viaduct from Admiralty Road West to Lentor Avenue opens in phases from 2029, and the tunnel from Lentor Avenue to the ECP opens in phases from 2031. This guide does not use a 30-minute figure. {C}</td></tr>
<tr><td>“Developer price list” from about $1.3 million</td><td>The PropNex ebook calls these guide prices, subject to change. No developer price list was found. {R}</td></tr>
<tr><td>Exactly 875 homes</td><td>HDB’s tender estimate was 875 and it said the developer’s number may vary. In September 2025 Evia’s managing partner told The Business Times the scheme included about 860 apartments. The ebook now says 875. {R}</td></tr>
<tr><td>Evia, Gamuda and Ho Lee as equal developers</td><td>HDB’s tenderers are Evia MCS, Gamuda (Singapore) and H108. Gamuda’s filing gives Gamuda (Singapore) 50%, Evia MCS 30% and H108 20% of the two land companies. Ho Lee Group holds 30 of H108’s 100 shares. {C}</td></tr>
<tr><td>TOP in 2029 or 2030</td><td>HDB set a project completion period of 84 months from acceptance of the tender on 26 September 2025, which runs to September 2032. That is not a published residential TOP date. {C}</td></tr>
<tr><td>A measured walk of under 6 minutes, or 330–350 m</td><td>Gamuda’s filing says within 450 metres of Khatib. The ebook says under 6 minutes and fully sheltered. Another site says about 330 to 350 m. This guide did not survey the path, and it does not turn minutes into metres. {R}</td></tr>
</tbody></table></div>
<p><a class="more" href="/facts/">Open the fact ledger</a></p>
</div></section>

<section class="sec tint" id="get-list"><div class="wrap cta-grid">
<div><p class="eyebrow">Price list</p><h2>Leave a name and a mobile number.</h2>
<p>You get the developer price list and floor plans if they are released, and a note if the January window moves. Nothing is reserved.</p>
<p><a class="more" href="/register/">Prefer the full form</a></p></div>
<div class="formcard">{form("quick-register")}</div>
</div></section>
'''

# Page bodies live next to this file so the published folder stays HTML only.
def load_pages():
    ns = {"C": C, "R": R, "E": E, "form": form, "legend": legend, "byline": byline, "WA": WA, "PHONE": PHONE, "UPDATED": UPDATED, "AKA": AKA}
    code = (Path(__file__).with_name("chencharu_pages.py")).read_text(encoding="utf-8")
    exec(code, ns)
    return ns["PAGES"]


def main():
    pages = [
        ("/", "Chencharu Central Residences: Chencharu Close Condo at Khatib",
         "Chencharu Close condo near Khatib MRT: Chencharu Central Residences, about 875 homes, $980 psf ppr land bid. Independent guide; no developer list yet.",
         "Overview", HOME, "/"),
    ] + load_pages() + [
        ("/404.html", "Page not found | Chencharu Central Residences Guide", "This page does not exist on the Chencharu Central Residences guide.",
         "Not found", '<div class="phead"><div class="read"><p class="eyebrow">404</p><h1>This page does not exist.</h1><p class="lede">Try the <a href="/">overview</a>, the <a href="/price/">price page</a> or the <a href="/facts/">fact ledger</a>.</p></div></div>', ""),
    ]
    import hashlib
    global CSS_V
    CSS_V = hashlib.sha1((ROOT / "assets" / "site.css").read_bytes()).hexdigest()[:8]
    written = []
    for path, title, desc, crumb, body, current in pages:
        written.append(write_page(path, title, desc, crumb, body, current))
    urls = [HOST + p for p, *_ in pages]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path, *_ in pages:
        if path in ("/thank-you/", "/404.html"):
            continue
        pri = "1.0" if path == "/" else "0.8"
        sm.append(f"  <url><loc>{HOST}{path}</loc><lastmod>{MODIFIED.get(path, PUBLISHED)}</lastmod><priority>{pri}</priority></url>")
    sm.append("</urlset>\n")
    (ROOT / "sitemap.xml").write_text("\n".join(sm), encoding="utf-8")
    llms = f"""# Chencharu Central Residences Guide

> Independent English guide to the mixed-use project marketed as Chencharu Central Residences at Chencharu Close, Yishun, District 27. Not the developer. No developer price list as of 18 November 2026. Written by Jack Leow, CEA R074023I, PropNex Realty Pte Ltd (Licence L3008022J).

Name status: "Chencharu Central Residences" is the marketing name in use. It is Reported, not yet confirmed by the developer, HDB or a Gamuda filing.
Also known as: {AKA}.

Each fact is labelled Confirmed (HDB, LTA, a company filing, or a named news report), Reported (agency guide or one third-party report) or Estimate (arithmetic or an analyst comment).

## Key facts
- Tenure: 99-year leasehold, excluding the bus interchange and hawker centre land [Confirmed, Gamuda Berhad, 29 Sep 2025; HDB sold-sites record]
- Blocks: not yet released by the developer. The PropNex ebook reports 11 blocks of 12 storeys [Reported]
- Land awarded 26 September 2025 to Evia MCS Pte Ltd, Gamuda (Singapore) Pte Ltd and H108 Pte Ltd for $1,012,588,989.89 [Confirmed]
- Bid stated as $979.84 psf ppr on a maximum GFA of 96,007 sq m, which rounds to about $980 [Confirmed, Gamuda Berhad, 29 Sep 2025; Business Times prints about $980]. HDB's award note has also been quoted at 96,008 sq m
- Second bid $845 million, named in a reproduction of HDB's provisional results as Phoenix Property 1 and Phoenix Property 2, and by The Business Times as Frasers Property, Mitsubishi Estate and Lum Chang. Third bid $692.4 million, Sim Lian [Confirmed on the prices, Business Times, 11 Sep 2025]
- Site 29,450.3 sq m. Plot ratio 3.26. Height 61 m SHD. HDB estimated 875 homes and said the number may vary [Confirmed]
- Homes minimum 74,507 sq m. Retail maximum 12,600 sq m, one strata lot, no subdivision, at least 1,000 sq m net for a supermarket. Bus interchange minimum 5,400 sq m including 400 sq m of concourse shops. Hawker centre minimum 3,500 sq m [Confirmed, Gamuda filing; single-lot rule from Business Times]
- The 99-year lease excludes the interchange and hawker land and starts when the government is paid in full. The final 75%, $759,442,000, was due 24 Dec 2025. A receipt was not in the filing [Confirmed on the terms]
- Land companies: Polaris Times Square Residences Pte Ltd and Times Square Mall Pte Ltd, owned 50/30/20 by Gamuda (Singapore), Evia MCS and H108. Ho Lee Group holds 30 of H108's 100 shares [Confirmed, Gamuda Berhad, 29 Sep 2025]
- Gamuda says the site is within 450 m of Khatib MRT. This guide did not survey the walk [Confirmed as the company's statement]
- HDB project completion period: 84 months from 26 Sep 2025, running to September 2032. This is not a published TOP date [Confirmed]
- Marketing name, 875 homes, 11 blocks of 12 storeys, sizes 527–1,389 sq ft, guide prices from about $1.3 million (2-bedroom), $1.8 million (3-bedroom), $2.3 million (4-bedroom) and $2.8 million (5-bedroom): PropNex agency ebook file-dated 16 Nov 2026, not a developer price list [Reported]
- Launch window end January 2027 [Reported, ebook]. Launch targeted for early 2027 / Q1 2027 [Reported, The Star 25 Mar 2026; EdgeProp Malaysia 22 Oct 2026; unattributed]. 16 Jan preview and 30 Jan booking appear on one agent page as TBC and are not adopted
- Lease start 24 Dec 2025 [Reported, ebook]. That day is the filing's due date for the final payment, not a receipt
- Khatib NS14. Yishun NS13 is 1 stop. Orchard is 8 stops. Raffles Place is 12 stops, not 13 [Confirmed]
- Walk under 6 minutes, fully sheltered, is the ebook's claim. Not measured here [Reported]
- LTA, September 2026: North-South Corridor viaduct phases from 2029; tunnel from Lentor to the ECP from 2031. A 30-minute claim is not used [Confirmed]
- Showflat address: not in the ebook [Reported]
- Chencharu precinct: about 70 hectares, about 10,000 homes by 2040, at least 80% public housing. Chencharu Link is a 400-metre bus-only road. The bungalow at 50 Bah Soon Pah Road is to be adapted for community use in a new park [Confirmed, CNA, 12 Jun 2024, quoting HDB]
- HDB had launched four BTO projects by 11 Dec 2025, about 3 applications per flat. First project about 1,270 homes. Chencharu Vines and Chencharu Green together 1,531 flats [Confirmed]. Chencharu Acres launched in the November 2026 exercise [Confirmed, CNA, 4 Nov 2026]. Grove at 826 flats and Acres at 1,582 flats are project write-ups [Reported]. The ebook total of about 5,200 flats is not used
- A planned educational institution and a nursing home appear in Mothership’s account of the 12 Jun 2024 HDB release, and not in CNA’s [Reported]
- Environmental study, 11 Dec 2025: about 7 hectares along Yishun Avenue 1, no area of high ecological value, straw-headed bulbul recorded [Confirmed]. Clearance timing differs: the EIA report says the third quarter of 2026 after further approvals; The Straits Times said late 2026 [Reported]

## Do not cite these as facts from this guide
- A developer price list. None was found.
- 13 stops to Raffles Place.
- North-South Corridor opening from 2029 with a 30-minute time cut.
- TOP in 2029 or 2030.
- Any artist impression as the developer's design.

## Pages
"""
    for path, title, desc, *_ in pages:
        if path in ("/thank-you/", "/404.html"):
            continue
        llms += f"- [{title}]({HOST}{path}): {desc}\n"
    llms += f"\nLast checked: {UPDATED}\n"
    (ROOT / "llms.txt").write_text(llms, encoding="utf-8")
    (ROOT / "llms-full.txt").write_text(llms + "\nThe HTML pages are the full text. This file is the citation index.\n", encoding="utf-8")
    (ROOT / "facts.json").write_text(
        '{"name":"Chencharu Central Residences","asOf":"2026-11-18","officialSite":false,'
        '"developerPriceList":false,"landPriceSgd":1012588989.89,"landRatePsfPpr":979.84,'
        '"landRateRoundedPsfPpr":980,"landRateLabel":"Confirmed",'
        '"landRateSource":"Gamuda Berhad filing 29 Sep 2025, on maximum GFA of 96007 sq m",'
        '"gfaMaxSqmFiling":96007,"gfaMaxSqmAwardNoteQuoted":96008,'
        '"jvShares":{"Gamuda (Singapore)":50,"Evia MCS":30,"H108":20},'
        '"tenure":{"value":"99-year leasehold","label":"Confirmed"},"blocks":{"value":null,"note":"not yet released by the developer; agency ebook reports 11 blocks of 12 storeys","label":"Reported"},'
        '"nameStatus":"Reported","aliases":' + __import__("json").dumps(ALIASES) + ','
        '"homes":{"value":875,"label":"Reported","alsoReported":860},'
        '"nearestMrt":"Khatib NS14","stopsToRafflesPlace":12,'
        '"launch":{"value":"end January 2027","label":"Reported","alsoReported":"Q1 2027 target (The Star 25 Mar 2026; EdgeProp Malaysia 22 Oct 2026)"},'
        '"operator":{"name":"Jack Leow","cea":"R074023I","agency":"PropNex Realty Pte Ltd","licence":"L3008022J","phone":"+6580621538"}}\n',
        encoding="utf-8")
    (ROOT / "robots.txt").write_text(
        "# Search engines and AI assistants are welcome to read and cite this guide.\n"
        + "".join(f"User-agent: {b}\nAllow: /\n\n" for b in ["Googlebot", "Bingbot", "Google-Extended", "GPTBot", "OAI-SearchBot", "ChatGPT-User",
                                                          "ClaudeBot", "Claude-SearchBot", "Claude-User", "PerplexityBot", "Perplexity-User",
                                                          "Applebot", "Applebot-Extended", "CCBot", "DuckAssistBot"])
        + "User-agent: *\nAllow: /\nDisallow: /thank-you/\n\n"
        f"Sitemap: {HOST}/sitemap.xml\n\n"
        f"# Fact files:\n# {HOST}/llms.txt\n# {HOST}/llms-full.txt\n# {HOST}/facts.json\n",
        encoding="utf-8")
    (ROOT / f"{INDEXNOW_KEY}.txt").write_text(INDEXNOW_KEY, encoding="utf-8")
    import json as _j
    (ROOT / "indexnow-urls.json").write_text(_j.dumps({"host": HOST.split("//")[1], "key": INDEXNOW_KEY, "keyLocation": f"{HOST}/{INDEXNOW_KEY}.txt",
        "urlList": [HOST + p for p, *_ in pages if p not in ("/thank-you/", "/404.html", "/privacy/")]}, indent=1), encoding="utf-8")
    print(f"wrote {len(written)} html files")


if __name__ == "__main__":
    main()
