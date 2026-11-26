# Executed by build-chencharu.py. Names C, R, E, form, legend, byline and WA are provided.

def article(eyebrow, h1, lede, inner):
    return f'''<div class="phead"><div class="read"><nav class="crumbs" aria-label="Breadcrumb"><a href="/">Chencharu Central Residences</a> / {eyebrow}</nav>
<p class="eyebrow">{eyebrow}</p><h1>{h1}</h1>
<p class="lede">{lede}</p>{byline()}</div></div>
<div class="read article">{inner}</div>'''


# ---- Launch-window sections (CLAUDE.md section 14). Pre-built and hidden: each renders NOTHING until its data is
# filled in from a developer price list or a reported sales result, so no placeholder is ever published or indexed.
# To go live: fill the dict, set "source" and "date" (e.g. "Developer price list, 16 Jan 2027"), set MODIFIED for the page,
# rebuild. Prices are the developer's figures only; never an agency guide quantum or a masked figure (section 10).
PRICE_LIST = {"source": "", "date": "", "rows": [
    # ("2-bedroom", "527 to 678", "$1,3xx,000", "$2,4xx"),   # (type, size sq ft, from price, from psf) -- full figures only
]}
SALES = {"source": "", "date": "", "sold": None, "released": None, "avg_psf": None}

def price_list_section():
    if not (PRICE_LIST["rows"] and PRICE_LIST["source"] and PRICE_LIST["date"]):
        return ""
    trs = "".join(f'<tr><td>{t}</td><td>{sz}</td><td class="num">{pr}</td><td class="num">{psf}</td></tr>'
                  for t, sz, pr, psf in PRICE_LIST["rows"])
    return (f'<section id="price-list"><h2>Developer price list, {PRICE_LIST["date"]}</h2>'
            f'<div class="tbl"><table><thead><tr><th>Type</th><th>Size (sq ft)</th><th class="num">From</th>'
            f'<th class="num">From psf</th></tr></thead><tbody>{trs}</tbody>'
            f'<caption>Source: {PRICE_LIST["source"]}. Prices change as units sell. Confirmed</caption></table></div></section>')

def sales_section():
    if not (SALES["sold"] and SALES["source"] and SALES["date"]):
        return ""
    share = f' of {SALES["released"]} released, about {round(100 * SALES["sold"] / SALES["released"])}%' if SALES["released"] else ""
    psf = f' at an average of about ${SALES["avg_psf"]:,} psf' if SALES["avg_psf"] else ""
    return (f'<section id="sales-results"><h2>Sales results</h2><p><strong>{SALES["sold"]:,} homes sold{share}{psf}'
            f', as of {SALES["date"]}.</strong> Source: {SALES["source"]}. Balance units change daily; '
            f'ask for the current list.</p></section>')

PAGES = []

PAGES.append(("/price/",
"Chencharu Close Condo Price: Chencharu Central Residences",
"Chencharu Central Residences price: land sold at about $980 psf ppr. Agency guide prices from about $1.3 million are not a developer price list as yet.",
"Price",
article("Price", "Chencharu Close condo price: there is no developer price list yet.",
"<strong>No developer price list has been released as of 18 November 2026. The land sold for $1,012,588,989.89, about $980 per square foot per plot ratio.</strong> A PropNex agency ebook prints guide prices from about $1.3 million for a two-bedroom. That is an agency guide, not a developer price list.",
f'''{price_list_section()}{sales_section()}<section><h2>The tender</h2>
<p>HDB awarded the Chencharu Close mixed commercial and residential site on 26 September 2025 to Evia MCS Pte Ltd, Gamuda (Singapore) Pte Ltd and H108 Pte Ltd. The Business Times described that consortium as entities of Evia Real Estate, Gamuda and Ho Lee Group. {C}</p>
<div class="tbl"><table>
<thead><tr><th>Bidder</th><th class="num">Price</th><th class="num">About psf ppr</th></tr></thead>
<tbody>
<tr><td>Evia MCS, Gamuda (Singapore), H108</td><td class="num">$1,012,588,989.89</td><td class="num">$980</td></tr>
<tr><td>Phoenix Property 1 and Phoenix Property 2. The Business Times names Frasers Property, Mitsubishi Estate and Lum Chang at this price.</td><td class="num">$845 million</td><td class="num">$818</td></tr>
<tr><td>Sim Lian Land and Sim Lian Development</td><td class="num">$692.4 million</td><td class="num">$670</td></tr>
</tbody>
<caption>Top price from HDB’s award note. The second and third prices are in The Business Times, 11 September 2025, and in a reproduction of HDB’s provisional tender results that day. The Phoenix names are from that reproduction. The top bid was about 20% above the second.</caption>
</table></div>
<p>Gamuda’s 29 September 2025 filing states the bid as $979.84 psf ppr, using a maximum gross floor area of 96,007 square metres. HDB’s award note has been quoted at 96,008 square metres. Dividing the award price by either area still rounds to about $980, which is the rate The Business Times printed. {C}</p>
</section>
<section><h2>What the agency guide prices mean</h2>
<p>The PropNex ebook, file-dated 16 November 2026, prints a star beside “guide price, subject to change”. It does not print a psf, a stack, or a storey. Several competing pages now call the same numbers a developer price list. This guide does not. {R}</p>
<div class="tbl"><table>
<thead><tr><th>Group in the ebook</th><th class="num">Homes</th><th>Sizes in the ebook</th><th>Guide price (agency ebook, not a developer price list)</th></tr></thead>
<tbody>
<tr><td>2-bedroom, Premium, and + Study</td><td class="num">228</td><td>527 to 678 sq ft</td><td>From about $1.3 million</td></tr>
<tr><td>3-bedroom, Premium, and + Study</td><td class="num">395</td><td>797 to 958 sq ft</td><td>From about $1.8 million</td></tr>
<tr><td>4-bedroom and + Study</td><td class="num">180</td><td>980 to 1,194 sq ft</td><td>From about $2.3 million</td></tr>
<tr><td>5-bedroom</td><td class="num">72</td><td>1,270 to 1,389 sq ft</td><td>From about $2.8 million</td></tr>
</tbody>
<caption>Counts are this guide’s sum of the ebook’s nine rows. 228 + 395 + 180 + 72 = 875. The quantum applies to the group, not to every size inside it.</caption>
</table></div>
<p>The ebook prints each figure with its second decimal hidden, for example “$1.3x million”. Read strictly, that is a figure from $1.30 million to $1.39 million. On the 527 sq ft two-bedroom, $1.30 million is about $2,467 psf and $1.39 million is about $2,638 psf. That arithmetic is only a way to read an incomplete number. It is not a forecast. {E}</p>
</section>
<section><h2>Older analyst comments</h2>
<p>On 11 September 2025, the day the tender closed, Knight Frank’s Leonard Tay told The Business Times the residences “could possibly be above $2,300 psf”. CBRE’s Tricia Song pointed at Parktown Residence in Tampines, the last similarly equipped site: 1,041 of 1,193 homes, 87%, at an average $2,360 psf on its February 2025 launch weekend. Those sentences are a year old. They are not a 2026 price list. {C}</p>
<p>A September 2025 comment and a November 2026 guide quantum can both be in the market at once. They are not the same kind of number. Wait for the developer’s list before treating either as the price you will pay.</p>
<p><a class="more" href="/floor-plans/">See the nine reported types</a></p>
<div class="icta" style="display:flex;justify-content:space-between;gap:16px;align-items:center;flex-wrap:wrap;background:#1F1C18;color:#F4F1EB;border-radius:14px;padding:18px 20px;margin-top:28px"><div><b>Want the list the day it exists?</b><br><span style="color:#C9C1B6">Name and mobile. Nothing is reserved.</span></div><a class="btn light" href="/register/">Register</a></div>
</section>'''),
"/price/"))

PAGES.append(("/floor-plans/",
"Chencharu Condo Floor Plans & Unit Mix (Chencharu Central)",
"Chencharu Central Residences unit mix: about 875 homes in nine reported types, 527 to 1,389 sq ft, from an agency ebook. No official floor plans as yet.",
"Floor plans",
article("Floor plans", "Chencharu condo floor plans: no official plans have been released.",
"<strong>The only unit table in hand is from a PropNex ebook, and it is marked subject to change.</strong> It lists 875 homes in nine types, from 527 to 1,389 sq ft. It is not a set of floor plans.",
f'''<section><h2>The nine reported types</h2>
<div class="tbl"><table>
<thead><tr><th>Type</th><th class="num">Homes</th><th>Size (sq ft)</th><th>Share</th></tr></thead>
<tbody>
<tr><td>2-bedroom</td><td class="num">36</td><td>527</td><td>4%</td></tr>
<tr><td>2-bedroom Premium</td><td class="num">108</td><td>603</td><td>12%</td></tr>
<tr><td>2-bedroom + Study</td><td class="num">84</td><td>657 to 678</td><td>10%</td></tr>
<tr><td>3-bedroom</td><td class="num">119</td><td>807</td><td>14%</td></tr>
<tr><td>3-bedroom Premium</td><td class="num">192</td><td>797 to 872</td><td>22%</td></tr>
<tr><td>3-bedroom + Study</td><td class="num">84</td><td>893 to 958</td><td>10%</td></tr>
<tr><td>4-bedroom</td><td class="num">72</td><td>980 to 1,044</td><td>8%</td></tr>
<tr><td>4-bedroom + Study</td><td class="num">108</td><td>1,076 to 1,194</td><td>12%</td></tr>
<tr><td>5-bedroom</td><td class="num">72</td><td>1,270 to 1,389</td><td>8%</td></tr>
<tr><td>Total</td><td class="num">875</td><td>527 to 1,389</td><td>100%</td></tr>
</tbody>
<caption>PropNex “Chencharu Central, Great Location Edition”, file-dated 16 November 2026. Shares are this guide’s rounding of each row over 875. {R}</caption>
</table></div>
<p>Two-bedroom types are 228 homes, 26%. Three-bedroom types are 395 homes, 45%. Four-bedroom types are 180 homes, 21%. Five-bedroom types are 72 homes, 8%. Three- and four-bedroom types together are 575 homes, about two-thirds of the table. {E}</p>
</section>
<section><h2>What this table cannot tell you</h2>
<ul>
<li>There is no plan, no bay window note, no balcony, no facing, and no stack.</li>
<li>The 3-bedroom Premium starts at 797 sq ft, which is smaller than the 807 sq ft 3-bedroom. “Premium” here is a name in the ebook, not a proven larger layout.</li>
<li>HDB’s own estimate was about 875 homes, and HDB said the number the developer builds may vary. In September 2025 Evia’s managing partner told The Business Times the proposal was about 860 apartments. {R}</li>
<li>The ebook’s illustrations are artists’ impressions. The file says they are not the final product.</li>
</ul>
<p>When a developer brochure exists, check three things before the price: the strata area against this table, which rooms are in the strata area, and whether the study has a window.</p>
<p><a class="more" href="/price/">How the guide quanta sit on these sizes</a></p>
</section>'''),
"/floor-plans/"))

PAGES.append(("/site-plan/",
"Chencharu Close Site Plan, Blocks & Podium",
"Chencharu Close site plan: a 29,450 sq m site, 96,007 sq m maximum GFA, homes above shops, a hawker centre and a bus interchange. Blocks not yet confirmed.",
"Site plan",
article("Site plan", "Chencharu Close site plan: the plan that matters is the GFA split.",
"<strong>HDB’s site is 29,450.3 square metres, with a 61-metre height limit.</strong> Gamuda’s filing sets the maximum gross floor area at 96,007 square metres. At least 74,507 square metres has to be homes. Shops are capped. A bus interchange and a hawker centre are required.",
f'''<section><h2>What the award documents fix</h2>
<div class="tbl"><table class="ledger"><tbody>
<tr><th scope="row">Site area</th><td>29,450.3 sq m, about 7.3 acres. Lot 04195V, Mukim 19. {C}</td></tr>
<tr><th scope="row">Maximum GFA</th><td>Gamuda’s filing says 96,007 sq m, which it converts as 1,033,410.7 sq ft. HDB’s award note has been quoted at 96,008 sq m. The gap is 1 sq m. Minimum GFA in the filing is 86,407 sq m. {C}</td></tr>
<tr><th scope="row">Plot ratio</th><td>3.26, stated in Gamuda’s filing and in The Business Times when the tender was launched. {C}</td></tr>
<tr><th scope="row">Height</th><td>61 metres Singapore Height Datum on the HDB particulars. Gamuda calls it a technical height control of 61 metres. {C}</td></tr>
<tr><th scope="row">Homes</th><td>Minimum 74,507 sq m, which is 801,986 sq ft and about 78% of the maximum. {C}</td></tr>
<tr><th scope="row">Retail GFA</th><td>Maximum 12,600 sq m, which is 135,625 sq ft. At least 1,000 sq m net floor area is for a supermarket. The Business Times says the commercial component is one strata lot and cannot be subdivided. {C}</td></tr>
<tr><th scope="row">Bus interchange and hawker centre</th><td>Minimum 5,400 sq m for the interchange, including 400 sq m of commercial space in the concourse, and minimum 3,500 sq m for the hawker centre. In square feet those minimums are 58,125 and about 37,674. Added to the housing minimum and the retail cap, they equal Gamuda’s 96,007 sq m maximum. The 400 sq m is already inside the 5,400. {C}</td></tr>
<tr><th scope="row">Lease of the interchange and hawker land</th><td>Gamuda’s 29 September 2025 announcement says the 99-year lease does not include the land those two uses sit on. {C}</td></tr>
</tbody></table></div>
</section>
<section><h2>What is only in the ebook</h2>
<p>The ebook says 875 homes in 11 residential blocks of 12 storeys, an air-conditioned bus interchange, a 40-stall hawker centre of about 720 seats, and a mall of supermarket, retail and food under the homes. It names architect P&amp;T Consultants, landscape Tinderbox and interior Index Design. None of that is in the HDB award note. Treat it as the current marketing scheme. {R}</p>
<p>Twelve storeys under a 61-metre cap is plausible. It is not proof. A podium for buses, stalls and shops will take a share of that height.</p>
<p>There is no dimensioned site plan in the ebook. The map in it is a location sketch, and the file says the drawings are artists’ impressions.</p>
<p><a class="more" href="/facilities/">Facilities named in the ebook</a> &nbsp; <a class="more" href="/location/">Where the site sits</a></p>
</section>'''),
"/site-plan/"))

PAGES.append(("/location/",
"Chencharu Close Condo Location: Khatib MRT (NS14)",
"Chencharu Central Residences location: Chencharu Close, Yishun (D27), within 450 m of Khatib MRT (NS14). Orchard is 8 stops; Raffles Place is 12 stops.",
"Location",
article("Location", "Chencharu Close location: Khatib is one stop from Yishun, and the city is further than some guides say.",
"<strong>The site is at Chencharu Close, Yishun, District 27.</strong> The nearest MRT named by every serious source is Khatib, NS14, on the North-South Line.",
f'''<section><h2>Stops you can count</h2>
<p>Station numbers below are the North-South Line codes. Orchard is NS22, so Khatib to Orchard is 8 stops. Raffles Place is NS26, so Khatib to Raffles Place is 12 stops. The PropNex ebook says 13. This guide uses 12. {C}</p>
<ol class="stops">
<li><b>NS13</b><span>Yishun, one stop north. Northpoint City is at this station. {C}</span></li>
<li><b>NS14</b><span>Khatib. The station this site is described against. {C}</span></li>
<li><b>NS22</b><span>Orchard, 8 stops south. {C}</span></li>
<li><b>NS26</b><span>Raffles Place, 12 stops south. {C}</span></li>
</ol>
<p>The walk itself is not a surveyed distance. Gamuda’s 29 September 2025 filing says the site is within 450 metres of Khatib MRT. {C} The ebook says a fully sheltered walk of under 6 minutes. Another project site says about 330 to 350 metres. A listing has used about 460 metres. Gamuda Land’s project page, checked 25 November 2026, says “5-minutes to Khatib MRT” without saying whether that is on foot. This guide did not measure the path, and it does not turn the minutes into metres. The sheltered link is part of a project that is not built. {R}</p>
</section>
<section><h2>Khatib new launch: where this condo sits</h2>
<p>If you are looking for a new condo near Khatib MRT, this is the private project at Chencharu Close. Gamuda’s filing puts the site within 450 metres of Khatib (NS14). {C} The launch is reported for the end of January 2027. {R} It sits over a bus interchange and a hawker centre that HDB required on the land: see <a href="/bus-interchange-hawker-centre/">the bus interchange and hawker centre</a>.</p>
</section>
<section><h2>The North-South Corridor has moved</h2>
<p>The ebook says the corridor opens from 2029 and aims to cut northern journeys by up to 30 minutes. That is not the timeline LTA published in September 2026.</p>
<ul>
<li>The viaduct from Admiralty Road West to Lentor Avenue is now expected in phases from 2029, not 2027. {C}</li>
<li>The tunnel from Lentor Avenue to the East Coast Parkway is now expected in phases from 2031, not 2029. The city-bound section is this tunnel. {C}</li>
<li>This guide does not repeat a 30-minute saving. LTA’s September 2026 notices used here do not state that figure.</li>
</ul>
<p>Yishun already has the North-South Line. The corridor is a future road project, not the way residents reach Khatib MRT.</p>
</section>
<section><h2>The town around the site</h2>
<p>The Business Times, quoting PropNex research at the tender, named Peiying Primary, Chung Cheng High (Yishun), Naval Base Primary, Naval Base Secondary, Orchid Park Secondary and Yishun Innova Junior College as schools near the plot. It also named Khatib Polyclinic, Yishun Stadium and Sports Hall, and Lower Seletar Reservoir Park. None of those was given as a measured walk. {C}</p>
<p>The ebook adds Northland Primary, HomeTeamNS Khatib, and a “minutes walk” to Lower Seletar Reservoir and the Khatib Bongsu mangroves. Those minutes are not used here as distances. {R}</p>
<p>Chencharu is a new precinct inside Yishun. HDB’s 12 June 2024 plan, reported by CNA and The Business Times, is about 70 hectares bounded by Yishun Avenue 1, Yishun Avenue 2 and Sembawang Road, about 10,000 homes by 2040, and at least 80% of them public housing. Gamuda’s filing repeats about 10,000 homes by 2040. {C} The ebook’s “fewer than 2,000 private homes” is tighter than “at least 80% public”, which allows up to about 2,000 private homes. This guide does not treat the two sentences as the same claim.</p>
<p>HDB said Chencharu Link, running north-south through the estate, is a 400-metre bus-only road. A community avenue runs east-west from a new park to the existing neighbourhood park near Khatib. The bungalow at 50 Bah Soon Pah Road, a plantation house about 100 years old and likely built in the early 1910s by the Bukit Sembawang Rubber Company, is to be adapted for community use inside that park, with a heritage trail, gardens and storyboards. Cycling links are planned toward Sembawang and Lower Seletar Reservoir. {C}</p>
<p>HDB also said Ground-Up Initiative and the Live Turtle and Tortoise Museum will move to a site next to HomeTeamNS Khatib. That is a plan to relocate them. It is not a statement that they have already moved. {C}</p>
<p>Mothership, citing that same HDB release, adds a planned educational institution and a nursing home. CNA’s account of the day does not. {R}</p>
<p>Public flats already launched are a separate count from this private project. HDB said in its 11 December 2025 gazette notice that four BTO projects had been launched, with about three applications for each available flat. The first, announced in June 2024, was about 1,270 homes. The Business Times put the two February 2025 projects, Chencharu Vines and Chencharu Green, at 1,531 flats together. {C}</p>
<p>Project pages put the October 2025 launch, Chencharu Grove, at 826 flats. {R} HDB then launched a fifth project, Chencharu Acres, in the November 2026 sales exercise. CNA reported that launch on 4 November 2026. {C} Write-ups of Chencharu Acres put it at 1,582 flats. {R}</p>
<p>The ebook’s “about 5,200 flats from five BTO projects” is not used as a total. The launches are now five, and the counts above are not added into one figure here. {R}</p>
<p>On 11 December 2025 HDB published an environmental study of a vegetated patch of about 7 hectares along Yishun Avenue 1, south of Yishun Walk. The study found no area of high ecological value. HDB said about 60% of the patch is scrubland and urban vegetation. The straw-headed bulbul was among the species recorded. Feedback ran to 7 January 2026. {C} The Straits Times, citing the report, said about 40% is forest on abandoned plantation land. {C} The report expects clearance to start in the third quarter of 2026, after an environmental management plan and approvals. The Straits Times described that clearance as late 2026. {R}</p>
<p><a class="more" href="/schools/">Schools, without invented distances</a></p>
</section>'''),
"/location/"))

PAGES.append(("/showflat/",
"Chencharu Central Residences Showflat: Location & Preview",
"Chencharu Central Residences showflat: no confirmed address as of 18 Nov 2026. One agent page says Yishun Ring Road, near Wisteria Mall, and marks it TBC.",
"Showflat",
article("Showflat", "Chencharu Central Residences showflat: there is no confirmed address yet.",
"<strong>The PropNex ebook does not name a gallery, a road, or an appointment date.</strong> One Huttons page, updated 15 November 2026, says a showflat along Yishun Ring Road opposite Wisteria Mall, and marks both the address and the dates TBC.",
f'''<section><h2>What is actually said</h2>
<div class="tbl"><table class="ledger"><tbody>
<tr><th scope="row">PropNex ebook, 16 Nov 2026</th><td>No showflat street. Launching end of January 2027. {R}</td></tr>
<tr><th scope="row">lihyuan.com, updated 15 Nov 2026</th><td>Yishun Ring Road, opposite Wisteria Mall. Preview 16 January 2027 and booking day 30 January 2027, both marked TBC. {R}</td></tr>
<tr><th scope="row">TeeCo, October 2026</th><td>Preview start estimated 16 January 2027. Prices not announced. {R}</td></tr>
<tr><th scope="row">PropertyNet, 13 Nov 2026</th><td>Preview date not announced. {R}</td></tr>
</tbody></table></div>
<p>Three write-ups in the same month do not agree. This guide will not pick 16 January as the date.</p>
</section>
<section><h2>What to ask for when a gallery does open</h2>
<ul>
<li>The developer price list, not a guide quantum.</li>
<li>Floor plans with strata area, for the type you are comparing with the ebook table.</li>
<li>Which block faces the bus interchange and the hawker centre, and which faces the other way.</li>
<li>Whether the 40 stalls and the mall are in the same strata you are buying. The retail cap is one lot and cannot be subdivided. You are not buying a shop. {C}</li>
</ul>
<p>Register if you want a message when a street address is actually published. A form does not hold a unit.</p>
<p><a class="more" href="/launch-date/">The launch window, and where the dates disagree</a></p>
</section>'''),
"/showflat/"))

PAGES.append(("/launch-date/",
"Chencharu Close Condo Launch Date: Chencharu Central Residences",
"Chencharu Central Residences launch date: an agency ebook reports end January 2027. Preview and booking days are not yet confirmed by the developer itself.",
"Launch date",
article("Launch date", "Chencharu Central Residences launch date: end January 2027 is a reported window, not a booking day.",
"<strong>The ebook cover says “launching end January 2027”.</strong> Two Malaysian business papers, The Star (25 March 2026) and EdgeProp Malaysia (22 October 2026), report the same window as early 2027 and the first quarter of 2027. Neither names a preview Saturday or a booking day, and pages that do are not consistent with each other.",
f'''<section><h2>Timeline that is on paper</h2>
<ol class="tl">
<li class="done"><time>26 Sep 2024</time><b>Tender launched</b> HDB put Chencharu Close out with the Sembawang Road executive condominium site. {C}</li>
<li class="done"><time>11 Sep 2025</time><b>Tender closed, three bids</b> Top bid about $1.01 billion. The Business Times reported the result the same afternoon. {C}</li>
<li class="done"><time>26 Sep 2025</time><b>Awarded</b> HDB accepted Evia MCS, Gamuda (Singapore) and H108 at $1,012,588,989.89. {C}</li>
<li class="done"><time>29 Sep 2025</time><b>Gamuda announcement</b> Letter of award dated 26 September. The land is to be held through Polaris Times Square Residences Pte Ltd and Times Square Mall Pte Ltd. {C}</li>
<li><time>24 Dec 2025</time><b>Final land payment fell due</b> Gamuda’s filing set 75% of the price, $759,442,000, due on this day. {C} The lease starts when the government receives the full price, and it excludes the bus-interchange and hawker-centre land. The ebook prints 99 years from this date. No receipt was in the documents checked here. {R}</li>
<li><time>25 Mar 2026</time><b>The Star: due to launch early next year</b> In a Gamuda Land profile, The Star describes the project as 875 private residences above commercial space, a hawker centre and a bus depot, “due to launch early next year”. The paper does not attribute the timing to a named person. {R}</li>
<li><time>22 Oct 2026</time><b>EdgeProp Malaysia: targeted for the first quarter of 2027</b> Reporting on Gamuda’s results, EdgeProp says the Chencharu Close development is targeted for launch in the first quarter of 2027. The sentence is not attributed to a speaker or a filing. {R}</li>
<li><time>End Jan 2027</time><b>Ebook launch window</b> Inside the first quarter that both papers report. Not a published developer sales date. {R}</li>
<li><time>Sep 2032</time><b>End of HDB’s 84-month completion period</b> Counted from acceptance on 26 September 2025. This is the contractual period for the project, not a residential TOP date. No TOP was found on the HDB award page. {C}</li>
</ol>
</section>
<section><h2>Dates this guide is not adopting</h2>
<p>A 16 January 2027 preview and a 30 January 2027 booking day appear on one agent site and are marked TBC. Another site says the preview has not been announced. Completion years of 2029 and 2030 appear on other agent sites without an HDB source. They are not used as the date of this project.</p>
<p><a class="more" href="/showflat/">Showflat claims</a></p>
</section>'''),
"/launch-date/"))

PAGES.append(("/facilities/",
"Chencharu Central Residences Facilities and Podium",
"Chencharu Central Residences facilities: HDB requires a bus interchange, a hawker centre and shops. Club facilities like a 50 m pool are from an ebook.",
"Facilities",
article("Facilities", "Chencharu Central Residences facilities: separate the podium HDB required from the ebook’s club list.",
"<strong>A bus interchange, a hawker centre and commercial space are conditions of the land.</strong> The 50-metre pool, the gym and the courts are a list in the PropNex ebook, marked subject to change.",
f'''<section><h2>On the land sale</h2>
<ul>
<li>Bus interchange, minimum 5,400 sq m. That minimum includes 400 sq m of commercial space in the concourse. {C}</li>
<li>Hawker centre, minimum 3,500 sq m. {C}</li>
<li>Commercial space, maximum 12,600 sq m. At least 1,000 sq m of net floor area is for a supermarket. The Business Times says this commercial component is one strata lot and cannot be subdivided. {C}</li>
</ul>
<p>Gamuda Land’s own project page, checked 25 November 2026, adds a BCA Green Mark Platinum Super Low Energy (SLE) rating and says the project will be designed in line with Singapore’s Green Plan 2030. {C} That is the company’s statement about a building not yet built. This guide has not found a BCA certificate for it.</p>
<p>The ebook is more specific: an air-conditioned interchange, 40 stalls and about 720 seats, and a mall with shops and food directly under the homes. The stall count and the air-conditioning are Reported. The supermarket minimum is already in the land filing. {R}</p>
</section>
<section><h2>Club facilities named only in the ebook</h2>
<p>The page is headed “The Ownership Advantage”. It is not a developer facilities schedule. {R}</p>
<ul>
<li>50 m grand lap pool</li>
<li>HYROX-ready gym</li>
<li>Indoor air-conditioned racquet hall</li>
<li>Padel court and two pickleball courts</li>
<li>Boxing ring</li>
<li>Yoga and dance studio</li>
<li>KTV and movie room</li>
<li>Bath house, hot and cold plunge</li>
<li>Seven function rooms</li>
<li>Pet corner, described as including a pool for pets</li>
<li>Putting green, written as 2/6-hole</li>
</ul>
<p>Until these are in a developer brochure or a written specification, they can be redesigned. Do not choose a stack because a court is drawn next to it in an agency ebook.</p>
</section>'''),
"/facilities/"))

PAGES.append(("/schools/",
"Schools Near Chencharu Close Condo: Peiying, Naval Base",
"Schools near Chencharu Close named in press reports: Peiying Primary, Naval Base Primary and Secondary, Chung Cheng High (Yishun). Distances unmeasured.",
"Schools",
article("Schools", "Schools near Chencharu Close: the names are published, the walking distances are not.",
"<strong>No source checked for this guide gives a measured distance from the site boundary to a school gate.</strong> A primary-school distance priority is a MOE rule applied to a finished address. This project has no postal address yet.",
f'''<section><h2>Named by PropNex research in The Business Times</h2>
<p>On 11 September 2025 Wong Siew Ying, PropNex head of research, listed these as near the Chencharu Close plot. The article does not say “within 1 km”. {C}</p>
<ul>
<li>Peiying Primary School</li>
<li>Naval Base Primary School</li>
<li>Naval Base Secondary School</li>
<li>Chung Cheng High School (Yishun)</li>
<li>Orchid Park Secondary School</li>
<li>Yishun Innova Junior College</li>
</ul>
</section>
<section><h2>Added by the ebook, not in that Business Times list</h2>
<p>The ebook also names Northland Primary. It does not give metres. {R}</p>
<p>Do not plan a Primary 1 application on an agency map. When a house number exists, check MOE’s distance tool for that year. School names and programmes change.</p>
<p><a class="more" href="/location/">MRT stops and the corridor</a></p>
</section>'''),
"/schools/"))

PAGES.append(("/review/",
"Chencharu Central Residences Review: Pros, Cons, Who It Suits",
"Independent Chencharu Central Residences review: the bus interchange and hawker podium is the real difference, and the price is not proven. Pros and cons.",
"Review",
article("Review", "Chencharu Central Residences review: worth shortlisting for own-stay, not worth pricing off a guide quantum.",
"<strong>Buyers who want daily uses under a new private home in Yishun have a real product here.</strong> Buyers who need a number to underwrite should wait. The land fact is solid. The selling price is not.",
f'''<section>
<div class="pc"><div class="pro"><h3>What holds up</h3><ul>
<li>HDB required the interchange, the hawker centre and the shops. This is not a slogan added later.</li>
<li>The land rate is about $980 psf ppr, and the top bid cleared the second bid by about 20%.</li>
<li>Khatib is on the North-South Line, one stop from Yishun and Northpoint City.</li>
<li>It is the first private-housing GLS site in the Chencharu precinct.</li>
</ul></div>
<div class="con"><h3>What does not</h3><ul>
<li>No developer price list, no floor plans, no confirmed showflat.</li>
<li>875 and about 860 are both in the record.</li>
<li>The ebook’s 13 stops to Raffles Place, and its North-South Corridor timing, are wrong against LTA.</li>
<li>HDB’s completion period runs to September 2032. You are buying a long build on a working interchange site.</li>
</ul></div></div>
</section>
<section><h2>Our verdict on price</h2>
<p><strong>For a 3-bedroom: buy at or below about $2,190 psf (about $1.93 million for 880 sq ft); walk away above about $2,300 psf (about $2.02 million).</strong> We compare like for like by size: its closest competitors (The Estuary within 1 km, then North Park Residences, The Wisteria and The Essence) work out to about $2,190 psf for a 3-bedroom as a brand-new integrated launch, after adding 5% for the older floor-area rules and the 33% premium that launches outside the city centre are charging over same-size resales. The Estuary's 3-bedroom-size resales averaged about $1,344 psf over the last 12 months. At the $2,300 to $2,450 psf analysts expect, a 3-bedroom is above our walk-away price, though the base case still makes about 14% in total by 2032 after stamp duty and selling costs. Family sizes are what most buyers here want, but Yishun's HDB upgraders would need some savings on top of their flat sale for a 3-bedroom, and there are few landed homes nearby, so resale buyers for the bigger units are fewer. For the widest appeal, choose a 3- or 4-bedroom of about 1,000 sq ft or more. {E} The full working is in our <a href="https://www.sellingsgproperty.com/condo-analysis/chencharu-central-residences/">Chencharu analysis on sellingsgproperty.com</a>.</p>
</section>
<section><h2>Who it suits</h2>
<p>An owner-occupier in the north who wants a new 99-year condo, can live with a 2030s completion, and cares more about the hawker centre, the buses and Khatib than about being the first resale in the precinct. The family sizes are the bulk of the reported mix: 395 three-bedroom homes and 180 four-bedroom homes.</p>
<p>It is a weak fit if you need a psf you can defend this month, if you want a shop as part of the purchase, or if you are treating an agency guide price of “from about $1.3 million” as a cheque amount. The retail is one strata lot. You are buying a home.</p>
</section>
<section><h2>Risks to price in, not to skip past</h2>
<ul>
<li>The second bid was $845 million. The winner paid about $168 million more. That premium has to come back in the selling price or in a reading of the podium that the under-bidders did not share.</li>
<li>Marcus Chu, CEO of ERA, said on 11 September 2025 that the land rate reflects the hawker centre and bus interchange, not a cheap Outside Central Region plot. He also said the cost of building those two uses is likely to be reimbursed. That reimbursement is his comment. It is not a sentence in the Gamuda filing. {R}</li>
<li>The lease starts when the government receives the full land price. Gamuda set the final 75% due on 24 December 2025, and the ebook uses that day as the lease start. A receipt was not in the filing. If the money was received then, the 99-year clock is already running while HDB’s completion period runs to September 2032.</li>
<li>HDB’s plan for Chencharu, reported by The Business Times in June 2024, is about 10,000 homes by 2040, at least 80% of them public. The private home is early. The estate around it is not finished.</li>
<li>Facilities in the ebook can be redrawn.</li>
</ul>
{legend()}
<p style="margin-top:18px"><a class="more" href="/facts/">Sources for each of these points</a></p>
</section>'''),
"/review/"))

PAGES.append(("/developer/",
"Chencharu Close Developer: Gamuda Land, Evia & Ho Lee",
"Chencharu Central Residences developer: Gamuda (Singapore) 50%, Evia MCS 30% and H108 20%, per Gamuda's Bursa filing. HDB awarded the site on 26 Sep 2025.",
"Developer",
article("Developer", "Chencharu Close developer: Gamuda Land, Evia and Ho Lee. The filing sets the shares.",
"<strong>The successful tenderers on HDB’s award are Evia MCS Pte Ltd, Gamuda (Singapore) Pte Ltd and H108 Pte Ltd.</strong> Gamuda’s exchange filing then says who owns the two companies that take the land.",
f'''<section><h2>Who holds the land</h2>
<p>Gamuda Berhad’s announcement of 29 September 2025 says the letter of award is dated 26 September 2025, and the land will be acquired through Polaris Times Square Residences Pte Ltd and Times Square Mall Pte Ltd. Both companies were incorporated on 23 September 2025. Each has the same shareholders. {C}</p>
<div class="tbl"><table>
<thead><tr><th>Shareholder of both land companies</th><th class="num">Shares</th></tr></thead>
<tbody>
<tr><td>Gamuda (Singapore) Pte Ltd</td><td class="num">50</td></tr>
<tr><td>Evia MCS Pte Ltd</td><td class="num">30</td></tr>
<tr><td>H108 Pte Ltd</td><td class="num">20</td></tr>
</tbody>
<caption>Gamuda Berhad, 29 September 2025. Out of 100 shares in each company. {C}</caption>
</table></div>
<p>Evia MCS was incorporated on 29 August 2025. Its shares are held by Evia Real Estate (12) Pte Ltd, 2 of 3, and MCSL Pte Ltd, 1 of 3. H108 was incorporated on 17 March 2025. Its 100 shares are held by Atad Investment, 30, Ho Lee Group Pte Ltd, 30, Ideal Plumbing Holding, 20, and OES Holdings, 20. Ho Lee is a shareholder of H108. It is not a one-third partner in the land companies. {C}</p>
<p>The same announcement says the fresh 99-year lease starts when the government receives the full price, and that the lease does not include the bus interchange and hawker centre land. It also said the scheme was not final: up to 875 homes, and a preliminary main construction cost of about $448 per square foot excluding land. That figure is a cost comment, not a selling price. {C}</p>
<p>The ebook’s line “Evia Real Estate, Gamuda Land and Ho Lee Group” is the market name for that consortium. The Business Times used the same description. It is not the share table. {R}</p>
</section>
<section><h2>What The Business Times recorded about their other work</h2>
<p>Evia’s managing partner Vincent Ong told The Business Times that the same three parties developed the OLA executive condominium in Sengkang, completed the year before the tender, and that Evia and Gamuda developed Gem Residences in Toa Payoh. He also said the Chencharu scheme they had in mind was about 860 apartments plus a retail mall at street level and basement 1. {C}</p>
<p>About 860 was a tender-time description. The ebook, a year later, says 875, which is also HDB’s estimate. Both stay in the ledger until the developer publishes one number.</p>
<p>Consultants named only in the ebook: P&amp;T Consultants, Tinderbox, Index Design. {R}</p>
</section>'''),
"/developer/"))

PAGES.append(("/facts/",
"Chencharu Central Residences Fact Ledger: Sources & Labels",
"Chencharu Central Residences fact ledger: every figure on this guide with its source and a Confirmed, Reported or Estimate label, plus the name status.",
"Fact ledger",
article("Fact ledger", "Chencharu Central Residences fact ledger: a row without a second source stays Reported.",
"<strong>The name Chencharu Central Residences is Reported, not confirmed. What is confirmed: HDB sold the 99-year leasehold site on 26 September 2025 for $1,012,588,989.89, about $980 psf ppr.</strong> Confirmed means HDB, LTA, Gamuda’s exchange announcement, or a named article in The Business Times. The PropNex ebook is an agency guide. Its figures stay Reported even where other agent sites repeat them.",
f'''<section>
<div class="tbl"><table>
<thead><tr><th>Fact</th><th>Status</th><th>Source</th></tr></thead>
<tbody>
<tr><td>Project name “Chencharu Central Residences”</td><td>{R}</td><td>Marketing name in the PropNex agency ebook, 16 Nov 2026. Gamuda Land, one of the three developer groups, lists the project as “Chencharu Central” on its own website (checked 25 Nov 2026), without “Residences”. The condo’s full name is not yet confirmed by the developer, HDB or a Gamuda filing. Also used: {AKA}. “Chencharu Grand Residences” appears on an agent marketing site; the developer has not used it</td></tr>
<tr><td>Tenure: 99-year leasehold</td><td>{C}</td><td>Gamuda Berhad, 29 Sep 2025; HDB’s sold-sites record</td></tr>
<tr><td>Site awarded 26 Sep 2025 for $1,012,588,989.89 to Evia MCS, Gamuda (Singapore) and H108</td><td>{C}</td><td>HDB award note</td></tr>
<tr><td>Site area 29,450.3 sq m; height 61 m SHD; about 875 homes, number may vary. Maximum GFA quoted as 96,008 sq m on the award note and 96,007 sq m in Gamuda’s filing</td><td>{C}</td><td>HDB award note; Gamuda Berhad, 29 Sep 2025</td></tr>
<tr><td>Plot ratio 3.26. Bid stated as $979.84 psf ppr, which rounds to about $980</td><td>{C}</td><td>Gamuda Berhad, 29 Sep 2025. The Business Times prints about $980.</td></tr>
<tr><td>Second bid $845 million, about $818 psf ppr. Third bid $692.4 million, about $670 psf ppr</td><td>{C}</td><td>The Business Times, 11 Sep 2025</td></tr>
<tr><td>Homes minimum 74,507 sq m. Retail maximum 12,600 sq m, including at least 1,000 sq m net for a supermarket, and one strata lot with no subdivision. Bus interchange minimum 5,400 sq m, including 400 sq m of concourse shops. Hawker centre minimum 3,500 sq m</td><td>{C}</td><td>Gamuda Berhad, 29 Sep 2025. The single-lot rule is The Business Times, 11 Sep 2025.</td></tr>
<tr><td>Lease excludes the interchange and hawker land, and starts when the price is paid in full. Final 75%, $759,442,000, was due 24 Dec 2025</td><td>{C}</td><td>Gamuda Berhad, 29 Sep 2025. A receipt of that payment was not in the filing.</td></tr>
<tr><td>Land companies Polaris Times Square Residences and Times Square Mall, owned 50 / 30 / 20 by Gamuda (Singapore), Evia MCS and H108</td><td>{C}</td><td>Gamuda Berhad, 29 Sep 2025</td></tr>
<tr><td>Project completion period 84 months from acceptance, to Sep 2032</td><td>{C}</td><td>HDB tender condition, counted from the award date</td></tr>
<tr><td>Khatib NS14. Yishun NS13 is 1 stop. Orchard NS22 is 8. Raffles Place NS26 is 12</td><td>{C}</td><td>North-South Line station numbers</td></tr>
<tr><td>NSC viaduct from 2029; city tunnel from 2031</td><td>{C}</td><td>LTA, September 2026</td></tr>
<tr><td>875 homes, 11 blocks of 12 storeys. Sizes 527 to 1,389 sq ft. Guide prices from about $1.3, $1.8, $2.3 and $2.8 million by bedroom group</td><td>{R}</td><td>PropNex agency ebook, file-dated 16 Nov 2026. Not a developer price list. The developer has not released blocks or storeys</td></tr>
<tr><td>99 years from 24 Dec 2025</td><td>{R}</td><td>Ebook. That day is the filing’s due date for the final payment, not a receipt</td></tr>
<tr><td>Launch at the end of January 2027</td><td>{R}</td><td>Ebook. Not a developer sales notice</td></tr>
<tr><td>Launch targeted for early 2027 / the first quarter of 2027</td><td>{R}</td><td>The Star, 25 Mar 2026; EdgeProp Malaysia, 22 Oct 2026. Neither attributes the date to a speaker or a filing. Not a developer sales notice</td></tr>
<tr><td>Showflat at Yishun Ring Road, 16 and 30 Jan 2027</td><td>{R}</td><td>One agent page, marked TBC. Not in the ebook. Other write-ups disagree</td></tr>
<tr><td>Within 450 m of Khatib MRT</td><td>{C}</td><td>Gamuda’s prospects paragraph, 29 Sep 2025. Not a survey by this guide</td></tr>
<tr><td>Walk under 6 minutes, fully sheltered</td><td>{R}</td><td>Ebook. Not measured for this guide</td></tr>
<tr><td>Gamuda Land’s project page, “Chencharu Central”: up to 875 homes, 12,600 sq m commercial, “5-minutes to Khatib MRT”, integrated bus interchange, BCA Green Mark Platinum Super Low Energy (SLE) rating</td><td>{C}</td><td>gamudaland.com.my developments page, checked 25 Nov 2026. The company’s statement: it does not say whether 5 minutes is on foot, and this guide has not found a BCA certificate for the project</td></tr>
<tr><td>40 stalls, about 720 seats, air-conditioned interchange, facility list, P&amp;T, Tinderbox, Index Design</td><td>{R}</td><td>Ebook only</td></tr>
<tr><td>About 70 hectares, about 10,000 homes by 2040, at least 80% public housing. Chencharu Link is a 400 m bus-only road. Bungalow at 50 Bah Soon Pah Road kept for community use in a new park</td><td>{C}</td><td>CNA, 12 Jun 2024, quoting HDB. The Business Times the same day. Gamuda repeats the 10,000 homes</td></tr>
<tr><td>Planned educational institution and nursing home</td><td>{R}</td><td>Mothership, 12 Jun 2024, citing HDB’s release. Not in CNA’s account of the same day</td></tr>
<tr><td>Ground-Up Initiative and the Live Turtle and Tortoise Museum to relocate next to HomeTeamNS Khatib</td><td>{C}</td><td>CNA, 12 Jun 2024, quoting HDB. A plan, not a completed move</td></tr>
<tr><td>Four BTO projects launched by 11 Dec 2025, about 3 applications per flat. First project about 1,270 homes. Vines and Green together 1,531 flats</td><td>{C}</td><td>HDB gazette notice, 11 Dec 2025. CNA for the first project. The Business Times, 10 Feb 2025, for the pair</td></tr>
<tr><td>Fifth project, Chencharu Acres, launched in the November 2026 BTO exercise</td><td>{C}</td><td>CNA, 4 Nov 2026, quoting HDB’s media release</td></tr>
<tr><td>Chencharu Grove, October 2025, 826 flats. Chencharu Acres, 1,582 flats. Ebook total of about 5,200 flats from five projects</td><td>{R}</td><td>Project write-ups for 826 and 1,582. The 5,200 figure is the ebook and is not added up here</td></tr>
<tr><td>Environmental study of about 7 hectares along Yishun Avenue 1, south of Yishun Walk. No area of high ecological value. About 60% scrubland and urban vegetation. Straw-headed bulbul recorded</td><td>{C}</td><td>HDB gazette and EIA report, 11 Dec 2025. Feedback to 7 Jan 2026. HDB’s post the same day states the 60%</td></tr>
<tr><td>About 40% of that patch is forest on abandoned plantation land</td><td>{C}</td><td>The Straits Times, 11 Dec 2025, citing the HDB report</td></tr>
<tr><td>Clearance expected in the third quarter of 2026, after an environmental management plan and approvals. The Straits Times said late 2026</td><td>{R}</td><td>The EIA report’s schedule, and The Straits Times, 11 Dec 2025. The two wordings are not the same date</td></tr>
<tr><td>Knight Frank: possibly above $2,300 psf. Parktown: 1,041 of 1,193 at $2,360 psf in Feb 2025</td><td>{C}</td><td>The Business Times, 11 Sep 2025. Dated comments, not a price list</td></tr>
<tr><td>$1.30 million on 527 sq ft is about $2,467 psf</td><td>{E}</td><td>This guide’s arithmetic on the bottom of an unstated digit</td></tr>
</tbody></table></div>
<p>PropNex research quoted in The Business Times is a source. It is not the operator of this guide. The operator is Jack Leow of PropNex Realty Pte Ltd, which is a separate fact and is on the about page.</p>
</section>'''),
"/facts/"))

PAGES.append(("/faq/",
"Chencharu Condo FAQ: Launch, Price, TOP, Developer",
"Chencharu Central Residences FAQ: launch, price, tenure, developer, homes, Khatib MRT, showflat, TOP and other names, each tied to a source and a label.",
"FAQ",
article("FAQ", "Chencharu Central Residences FAQ: short answers, with the sources in the ledger.",
"<strong>This is not the official project website.</strong> HDB sold the land. A developer price list was not found on 18 November 2026.",
f'''<div class="faq">
<details open><summary>When does it launch?</summary><p>The PropNex ebook says the end of January 2027, and The Star (March 2026) and EdgeProp Malaysia (October 2026) report a launch target of early 2027, the first quarter. None names a booking day. A 16 January preview and a 30 January booking day are one agent’s TBC dates, and other write-ups do not share them. {R}</p></details>
<details><summary>What is the price?</summary><p>No developer price list. The land was $1,012,588,989.89, about $980 psf ppr. The PropNex agency ebook prints guide prices from about $1.3 million for the two-bedroom group. That is an agency guide, not a developer price list. {R}</p></details>
<details><summary>Who is the developer?</summary><p>HDB awarded the site to Evia MCS Pte Ltd, Gamuda (Singapore) Pte Ltd and H108 Pte Ltd. Gamuda’s filing gives Gamuda (Singapore) 50%, Evia MCS 30% and H108 20% of Polaris Times Square Residences and of Times Square Mall. Ho Lee Group holds 30 of H108’s 100 shares. It is not a one-third partner. {C}</p></details>
<details><summary>What is the tenure?</summary><p>99-year leasehold. The lease starts when the government receives the full land price, and it excludes the bus interchange and hawker centre land. {C}</p></details>
<details><summary>Is it called anything else?</summary><p>Chencharu Central Residences is the marketing name in use, and the developer has not confirmed it yet. Gamuda Land, one of the three developer groups, lists the project as “Chencharu Central” on its own website, without “Residences”. {C} Also known as {AKA}. “Chencharu Grand Residences” appears on an agent marketing site; the developer has not used that name either. {R}</p></details>
<details><summary>Is there a new launch condo near Khatib MRT?</summary><p>Yes. This project at Chencharu Close is within 450 metres of Khatib MRT (NS14), according to Gamuda’s filing. {C} Its launch is reported for the end of January 2027. {R} See <a href="/location/">the location page</a>.</p></details>
<details><summary>Should I buy the Chencharu condo or a Chencharu BTO flat?</summary><p>They serve different buyers. A 4-room flat at Chencharu Acres, HDB’s November 2026 BTO, is $353,000 to $428,000 before grants, with income and ownership rules. {C} The condo has no developer price list yet; agency guide prices start from about $1.8 million for a three-bedroom. {R} See <a href="/vs-chencharu-bto/">the full comparison</a>.</p></details>
<details><summary>How many homes?</summary><p>HDB estimated 875 and said the number may vary. Evia described about 860 apartments to The Business Times in September 2025. The ebook now says 875 in 11 blocks of 12 storeys. The developer has not released block or storey counts. {R}</p></details>
<details><summary>How far is the MRT?</summary><p>Khatib is NS14. Yishun and Northpoint City are one stop. Orchard is 8 stops. Raffles Place is 12 stops, not 13. {C} Gamuda’s filing says within 450 metres, the ebook says a sheltered walk under 6 minutes, and Gamuda Land’s project page says 5 minutes without naming the mode. This guide did not measure the path. {R}</p></details>
<details><summary>Where is the showflat?</summary><p>Not stated in the ebook. One agent page says Yishun Ring Road opposite Wisteria Mall and marks it TBC. {R}</p></details>
<details><summary>When is TOP?</summary><p>No TOP date was found. HDB’s project completion period is 84 months from 26 September 2025, which runs to September 2032. {C}</p></details>
<details><summary>Do I pay more through an agent?</summary><p>On a normal Singapore developer sale the list price is the same and the developer pays the agent. The Chencharu developer has not published that sentence. Treat it as the market practice, not as a term of this project, until the appointment letter says it. {R}</p></details>
<details><summary>Is the mall for sale as shops?</summary><p>The Business Times reported that the commercial space is capped and must be held as a single strata lot. Buyers of homes are not buying strata shops. {C}</p></details>
</div>'''),
"/faq/"))

PAGES.append(("/register/",
"Register for the Chencharu Central Residences Price List",
"Register for the Chencharu Central Residences developer price list and floor plans. Name and mobile only; nothing is reserved. Jack Leow, CEA R074023I.",
"Register",
article("Register", "Register for the Chencharu Central Residences developer price list.",
"<strong>Name and mobile, plus an optional unit type. That is the form.</strong> You will be contacted about this project only. No guide price is attached, because it is not a price list.",
f'''<section><div class="formcard">{form("register")}</div>
<p class="fine" style="margin-top:14px">Or <a href="{WA}">WhatsApp {PHONE}</a>. Jack Leow, CEA R074023I, PropNex Realty Pte Ltd, licence L3008022J.</p>
</section>'''),
"/register/"))

PAGES.append(("/e-brochure/",
"Chencharu Central Residences E-Brochure: What the Ebook Is",
"What the Chencharu Central ebook is: a PropNex agency guide dated 16 Nov 2026, with guide prices and a unit table. Not the developer's brochure or list.",
"Ebook",
article("Ebook", "Chencharu Central Residences ebook: an agency guide, not the developer brochure.",
"<strong>The file is a seven-page PropNex ebook titled Chencharu Central, Great Location Edition.</strong> Its properties date it 16 November 2026. The cover says launching end January 2027. The disclaimer says the drawings are artists’ impressions and not the final product.",
f'''<section><h2>What was taken from it</h2>
<ul>
<li>The marketing name, the nine-row unit table, and the four guide quanta. {R}</li>
<li>11 blocks of 12 storeys, the 40-stall hawker note, and the club-facility list. {R}</li>
<li>The under-6-minute walk, kept as a claim and not converted into metres. {R}</li>
<li>The precinct figures that match HDB’s 12 June 2024 plan: about 70 hectares, about 10,000 homes by 2040, the 400-metre bus-only road, and the bungalow at 50 Bah Soon Pah Road kept for community use in a new park. {C}</li>
<li>The ebook’s “about 5,200 flats from five BTO projects” was not used as a total. {R}</li>
<li>HDB had launched four BTO projects by 11 December 2025, and launched Chencharu Acres in November 2026. {C}</li>
</ul>
<h2>What was not taken from it</h2>
<ul>
<li>“13 stops to Raffles Place.” The count is 12.</li>
<li>A North-South Corridor opening from 2029 that cuts journeys by up to 30 minutes. LTA’s September 2026 timeline is different, and the 30 minutes is not used.</li>
<li>Any illustration, presented as the building.</li>
<li>The slogans on the cover. They are not facts.</li>
</ul>
<p>The PDF is not hosted here. When the developer issues a brochure, this page should be replaced with that file’s name, date and contents.</p>
</section>'''),
"/e-brochure/"))

PAGES.append(("/news/",
"Chencharu Central Residences News and Updates",
"Chencharu Central Residences updates, newest first: the HDB award, the LTA corridor revision, the Chencharu BTO launches and the agency ebook. No list yet.",
"Updates",
article("Updates", "Chencharu Central Residences updates: what changed, and what did not.",
"<strong>As of 18 November 2026 there is still no developer price list, no official floor plan and no confirmed showflat address.</strong>",
f'''<section><ol class="tl">
<li><time>25 Nov 2026</time><b>Gamuda Land lists the project as “Chencharu Central”</b> Its developments page names it “Chencharu Central”, without “Residences”, with up to 875 homes, 12,600 sq m of commercial space, “5-minutes to Khatib MRT” and a BCA Green Mark Platinum Super Low Energy rating. {C} The condo’s full name is still not confirmed, so this guide keeps the name Reported. {R}</li>
<li><time>18 Nov 2026</time><b>HDB’s June 2024 precinct plan was checked against CNA</b> The 400-metre bus road and the bungalow at 50 Bah Soon Pah Road are in this guide as HDB’s plan. The ebook’s 5,200 flats is not used as a total. There is still no developer price list.</li>
<li><time>18 Nov 2026</time><b>Gamuda’s seven-page Bursa filing was read in full</b> The land companies are owned 50% by Gamuda (Singapore), 30% by Evia MCS and 20% by H108. The floor-area minimums, the $979.84 psf ppr rate and the 24 December 2025 final-payment date are now in this guide.</li>
<li><time>4 Nov 2026</time><b>HDB launches Chencharu Acres</b> A fifth Chencharu BTO, in the November 2026 exercise. CNA reported the launch. {C} Write-ups put the project at 1,582 flats. That count is not added into a precinct total here. {R}</li>
<li><time>11 Dec 2025</time><b>HDB publishes the Chencharu environmental study</b> About 7 hectares along Yishun Avenue 1. No area of high ecological value. Feedback ran to 7 January 2026. {C} The report expects clearance in the third quarter of 2026, after further approvals. The Straits Times said late 2026. {R}</li>
<li><time>17 Nov 2026</time><b>The ebook was checked against HDB, Business Times and LTA</b> The 13-stop claim and the corridor timing were not adopted. Guide quanta stay labelled as guide quanta.</li>
<li><time>22 Oct 2026</time><b>EdgeProp Malaysia: first-quarter 2027 target</b> The Chencharu Close development is reported as targeted for launch in the first quarter of 2027, matching The Star’s “early next year” of 25 March 2026. Not a developer sales notice. {R}</li>
<li><time>16 Nov 2026</time><b>PropNex ebook file date</b> Unit table, guide quanta, facilities list, end-January 2027 window. {R}</li>
<li><time>Sep 2026</time><b>LTA revises the North-South Corridor</b> Viaduct phases from 2029. Tunnel to the ECP from 2031. {C}</li>
<li><time>26 Sep 2025</time><b>HDB awards Chencharu Close</b> $1,012,588,989.89. {C}</li>
<li><time>11 Sep 2025</time><b>Three bids reported</b> Second bid $845 million. Knight Frank comments above $2,300 psf. {C}</li>
</ol>
<p>A new row belongs here on the day a developer price list, a floor plan or a showflat address is published. Not before.</p>
</section>'''),
"/news/"))

PAGES.append(("/about/",
"About This Chencharu Central Residences Guide",
"Written by Jack Leow, CEA R074023I, PropNex Realty Pte Ltd, licence L3008022J. An independent guide. Not the developer of Chencharu Central Residences.",
"About",
article("About", "Who writes this, and what it will not do.",
"<strong>Jack Leow, salesperson registration R074023I, with PropNex Realty Pte Ltd, estate agent licence L3008022J.</strong> Phone +65 8062 1538.",
f'''<section><p>PropNex also appears in the sources, because its research was quoted by The Business Times and because the ebook used here is a PropNex file. Those citations are not a second identity for this site. The operator is the salesperson named above.</p>
<h2>Standards</h2>
<ul>
<li>English only.</li>
<li>Confirmed, Reported and Estimate on figures that can move a decision.</li>
<li>No claim that this is the official project site.</li>
<li>No bought links, no hidden text, no popup, no countdown, no tracker stack.</li>
<li>A page is updated when a sourced fact changes, not to match a competitor’s higher number.</li>
</ul>
<p>You can check the registration on the CEA Public Register. Search Leow Thai Chee or R074023I.</p>
</section>'''),
""))

PAGES.append(("/privacy/",
"Privacy | Chencharu Central Residences Guide",
"How this Chencharu Central Residences guide uses the name and mobile number you send, under the PDPA. Enquiries go only to Jack Leow of PropNex Realty.",
"Privacy",
article("Privacy", "What the form stores.",
"<strong>The form asks for a name, a mobile number, an optional unit type, and consent.</strong> It is used to reply about Chencharu Central Residences.",
f'''<section>
<ul>
<li>Enquiries sent through the form are stored by Netlify Forms for this site, chencharuyishun.sg, and read by Jack Leow of PropNex Realty Pte Ltd.</li>
<li>Jack Leow of PropNex Realty Pte Ltd reads the enquiry. It is not sold as a list.</li>
<li>You can ask for the enquiry to be deleted by writing to the same mobile number, +65 8062 1538.</li>
<li>The thank-you page is not indexed.</li>
</ul>
</section>'''),
""))

PAGES.append(("/thank-you/",
"Enquiry received | Chencharu Central Residences",
"Your Chencharu Central Residences enquiry was recorded. Nothing is reserved.",
"Sent",
article("Sent", "Received.",
"<strong>Nothing is reserved.</strong> If a developer price list or a floor plan is released, Jack will use the mobile number you gave.",
f'''<section><p><a class="btn" href="/">Back to the guide</a></p></section>'''),
""))


PAGES.append(("/bus-interchange-hawker-centre/",
"Chencharu Bus Interchange & Hawker Centre at Chencharu Close",
"Chencharu bus interchange and hawker centre: HDB requires at least 5,400 sq m and 3,500 sq m under the Chencharu Close condo. What is fixed, what is not.",
"Bus interchange",
article("Bus interchange", "Chencharu bus interchange and hawker centre: what HDB fixed, and what is still a drawing.",
"<strong>A new bus interchange and a hawker centre are conditions of the land at Chencharu Close.</strong> HDB’s sale requires at least 5,400 square metres for the interchange and 3,500 square metres for the hawker centre, under the condo’s homes and shops. No separate completion date has been published for either.",
f'''<section><h2>What the land sale fixes</h2>
<div class="tbl"><table class="ledger"><tbody>
<tr><th scope="row">Bus interchange</th><td>At least 5,400 sq m, about 58,125 sq ft, including 400 sq m of commercial space in the concourse. {C}</td></tr>
<tr><th scope="row">Hawker centre</th><td>At least 3,500 sq m, about 37,674 sq ft. {C}</td></tr>
<tr><th scope="row">Shops</th><td>At most 12,600 sq m, with at least 1,000 sq m net for a supermarket. One strata lot that cannot be subdivided. {C}</td></tr>
<tr><th scope="row">Homes</th><td>At least 74,507 sq m of the maximum 96,007 sq m GFA. About 875 homes. {C}</td></tr>
<tr><th scope="row">Lease</th><td>The condo’s 99-year lease does not include the land the interchange and hawker centre sit on. {C}</td></tr>
</tbody></table></div>
<p class="fine">Sources: Gamuda Berhad’s announcement of 29 September 2025; The Business Times, 11 September 2025, for the single strata lot. Full rows in the <a href="/facts/">fact ledger</a>.</p>
</section>
<section><h2>What is only in the marketing so far</h2>
<p>The PropNex agency ebook describes an air-conditioned interchange and a 40-stall hawker centre of about 720 seats, with a mall of supermarket, shops and food under the homes. None of that detail is in the HDB award. Treat it as the current scheme, not a commitment. {R}</p>
</section>
<section><h2>When will the Chencharu bus interchange be ready?</h2>
<p>No date has been published for the interchange or the hawker centre on their own. HDB’s tender gives the whole project a completion period of 84 months from the award on 26 September 2025, which runs to September 2032. {C} That is the outer limit for the development, not an opening date for the buses.</p>
<p>HDB’s 2024 plan for the Chencharu estate also includes Chencharu Link, a 400-metre bus-only road running north to south through the new estate. {C}</p>
</section>
<section><h2>A Yishun integrated development: what it means day to day</h2>
<ul>
<li><b>Buses and food downstairs.</b> Residents will live over an interchange, a hawker centre and a supermarket, within 450 metres of Khatib MRT. {C}</li>
<li><b>Footfall and noise.</b> An interchange and a hawker centre bring buses and crowds from the whole new estate. When floor plans are out, check which blocks face the interchange and the hawker centre.</li>
<li><b>You are buying a home, not the podium.</b> The shops are one strata lot and the interchange and hawker land sit outside the condo’s lease. Ask the developer how the costs of the podium are shared before you buy.</li>
<li><b>Price.</b> The land rate of about $980 psf ppr reflects these uses. The <a href="/price/">price page</a> sets out what is known.</li>
</ul>
<p><a class="more" href="/site-plan/">How the GFA splits</a> &nbsp; <a class="more" href="/facilities/">Club facilities in the ebook</a></p>
</section>'''),
"/bus-interchange-hawker-centre/"))

PAGES.append(("/vs-chencharu-bto/",
"Chencharu Condo vs Chencharu BTO: Price, Size, Wait Compared",
"Chencharu condo vs Chencharu BTO: Chencharu Acres 4-room flats from $353,000 before grants, against agency guide prices for the condo. Price, size, wait.",
"Condo vs BTO",
article("Condo vs BTO", "Chencharu condo vs Chencharu BTO: two different purchases in the same estate.",
"<strong>A 4-room flat at Chencharu Acres, HDB’s November 2026 BTO, costs $353,000 to $428,000 before grants.</strong> The Chencharu Close condo has no developer price list yet; an agency ebook prints guide prices from about $1.8 million for a three-bedroom. Most buyers will qualify for only one of the two.",
f'''<section><h2>Side by side</h2>
<div class="tbl"><table>
<thead><tr><th></th><th>Chencharu Acres BTO (Nov 2026)</th><th>Chencharu Close condo</th></tr></thead>
<tbody>
<tr><td>Price</td><td>3-room $297,000 to $355,000; 4-room $353,000 to $428,000; 5-room $484,000 to $604,000, before grants {C}</td><td>No developer price list. Agency guide from about $1.3 million (2-bedroom), $1.8 million (3-bedroom), $2.3 million (4-bedroom) {R}</td></tr>
<tr><td>Size</td><td>3-room about 69 sq m; 4-room about 93 sq m; 5-room about 113 sq m (estimated) {C}</td><td>527 to 1,389 sq ft, about 49 to 129 sq m, in the agency ebook {R}</td></tr>
<tr><td>Homes</td><td>1,582 flats {C}</td><td>About 875 {R}</td></tr>
<tr><td>Tenure</td><td>99-year lease</td><td>99-year leasehold {C}</td></tr>
<tr><td>Wait</td><td>39 or 41 months, depending on the block {C}</td><td>HDB’s completion period for the project runs to September 2032 {C}</td></tr>
<tr><td>Minimum occupation</td><td>5 years (Standard project) {C}</td><td>None. Seller’s stamp duty applies if you sell within 4 years</td></tr>
<tr><td>Who can buy</td><td>HDB eligibility: citizenship, family nucleus, household income ceiling, no private property</td><td>Anyone; additional buyer’s stamp duty depends on residency and homes already owned</td></tr>
<tr><td>Downstairs</td><td>Estate amenities</td><td>A bus interchange, a hawker centre and shops in the podium {C}</td></tr>
</tbody></table></div>
<p class="fine">BTO figures: HDB’s November 2026 sales exercise as published by CNA and reported by Stacked Homes and Home &amp; Decor, 4 to 5 November 2026. Condo figures: see the <a href="/facts/">fact ledger</a>. Check eligibility on HDB’s website for your own case.</p>
</section>
<section><h2>How to think about it</h2>
<ul>
<li><b>If you qualify for the BTO and the price matters most,</b> the BTO is the far cheaper way into the same estate. A 4-room flat of about 93 sq m costs less than a quarter of the condo’s agency guide for a three-bedroom of 74 to 89 sq m.</li>
<li><b>If you already own an HDB flat past its minimum occupation period,</b> or earn above the BTO income ceiling, the condo is the new home you can buy in Chencharu.</li>
<li><b>If you own private property,</b> a BTO flat is not open to you.</li>
<li><b>The condo’s extra cost buys</b> condo facilities, no minimum occupation period, the interchange and hawker centre downstairs, and a home you can sell or rent on the open market. Whether that is worth the gap depends on the developer’s real price, which is not out yet.</li>
</ul>
<p><a class="more" href="/price/">What is known about the condo price</a> &nbsp; <a class="more" href="/location/">The Chencharu estate plan</a></p>
</section>'''),
"/vs-chencharu-bto/"))
