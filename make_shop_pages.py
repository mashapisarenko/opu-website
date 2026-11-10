# -*- coding: utf-8 -*-
"""Builds the affiliate shop: shop/*.html, from _shop/products.json (outside the repo).

Run from opu-website/:  python3 make_shop_pages.py [path/to/products.json]
Rules baked in: no prices, no ratings or review counts, no Amazon images (cards use our own
type illustrations from images/shop/types/, mapped in shop_illus.py); every link is
https://www.amazon.com/dp/{ASIN}?tag=musicalgalaxi-20 with rel="sponsored nofollow noopener".
price_usd_seen is used only to bucket gift guides, and is never printed.
"""
import json, html, re, sys, pathlib, importlib.util, collections

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import shop_content as C, shop_notes as N, shop_depth as D, shop_illus as SI
from shop_text import ARTICLE, GUIDES, HUB

SITE = "https://onlinepianouniversity.com"
TAG = "musicalgalaxi-20"
DISC = ("As an Amazon Associate I earn from qualifying purchases. Some links on this page are affiliate links; "
        "buying through them costs you nothing extra.")
TIERS = [("budget", "Budget"), ("mid", "Mid-range"), ("premium", "Premium"), ("luxury", "Luxury")]
TIER_LABEL = dict(TIERS)
ILLUS_NOTE = "Illustrations show the type of product; see the exact item and its photos on Amazon."
OUT = HERE / "shop"
PRODUCTS = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE.parent / "_shop" / "products.json"

TPL = (HERE / "blog" / "russian-school-vs-american-piano-method.html").read_text(encoding="utf-8")
spec = importlib.util.spec_from_file_location("cb", HERE / "blog" / "_contact_blocks.py")
cb = importlib.util.module_from_spec(spec); spec.loader.exec_module(cb)
BLOCKS = cb._blocks()

def esc(s): return html.escape(s, quote=False)
def attr(s): return html.escape(s, quote=True)
def jd(o): return json.dumps(o, ensure_ascii=False).replace("</", "<\\/")

HEAD_PRE = TPL[:TPL.index("<title>")]
HEAD_MID = TPL[TPL.index('<link rel="manifest"'):TPL.index('<script type="application/ld+json">')]
HEAD_MID = HEAD_MID.replace('<link rel="stylesheet" href="../css/site.css">',
                            '<link rel="stylesheet" href="../css/site.css">\n<link rel="stylesheet" href="../css/shop.css">')
HEADER = TPL[TPL.index('<header class="site">'):TPL.index("</header>") + 9]
HEADER = HEADER.replace('<a href="../shop/index.html">Shop</a>', '<a href="../shop/index.html" class="active">Shop</a>')
HEADER = HEADER.replace('<a href="index.html">Blog</a>', '<a href="../blog/index.html">Blog</a>')
FOOTER = TPL[TPL.index('<footer id="footer">'):TPL.index("</footer>") + 9]
FOOTER = FOOTER.replace('<a href="index.html">Blog</a>', '<a href="../blog/index.html">Blog</a>')
FOOTER = re.sub(r'<p class="disclaimer"[^>]*>As an Amazon Associate I earn from qualifying purchases\.</p>',
                '<p class="shop-disc-foot">' + DISC + '</p>', FOOTER)
assert DISC in FOOTER
AUTHOR = ('<aside class="card" style="display:flex;gap:16px;align-items:center;margin:34px 0 0;padding:18px 20px">'
          '<img src="../images/blog/dr-maria-pisarenko-piano-concert-gown.jpg" alt="Dr. Maria Pisarenko, concert pianist" width="96" height="96" style="width:96px;height:96px;border-radius:50%;object-fit:cover" loading="lazy">'
          '<p style="margin:0"><strong>Dr. Maria Pisarenko, D.M.A.</strong> is a concert pianist and university piano professor. She teaches adults online at Online Piano University and chooses everything in this shop herself.</p></aside>')
CAPTURE = re.search(r'<section class="section" style="padding-top:0">\s*<div class="wrap">\s*<div class="capture">.*?</section>', TPL, re.S).group(0)
SCRIPTS = '<script src="../js/config.js" defer></script>\n<script src="../js/site.js" defer></script>\n<script src="../js/shop.js" defer></script>'

def load():
    data = json.loads(PRODUCTS.read_text(encoding="utf-8"))
    return data
DATA = load()
BY_ASIN = {}
for p in DATA:
    BY_ASIN.setdefault(p["asin"], p)

def url(p): return "https://www.amazon.com/dp/%s?tag=%s" % (p["asin"], TAG)

def card(p, i, cat, group=None, tier_tag=True):
    """Product card: our own type illustration on top (never an Amazon photo), the whole card clickable.
    tier_tag is kept for callers; the card now shows brand + product type under the picture."""
    b = N.brand_of(p)
    name = N.short_name(p)
    ty, label = SI.type_of(p)
    full = ((b + " ") if b else "") + name
    link = 'href="%s" rel="sponsored nofollow noopener" target="_blank" data-asin="%s" data-category="%s"' % (url(p), p["asin"], attr(cat))
    meta = '<span class="pbrand">%s</span>' % (esc(b) if b else "Online Piano University pick")
    meta += '<span class="ptype">%s</span>' % esc(label)
    img = ('<a class="pimg" %s><img src="../images/shop/types/%s.svg" width="600" height="450" loading="lazy" decoding="async" alt="%s"></a>'
           % (link, ty, attr(SI.alt_text(label, full))))
    return ('<article class="pcard">%s<div class="pmeta">%s</div><h3>%s</h3><p>%s</p>'
            '<a class="btn shop-btn" %s>Check today&#39;s price on Amazon</a></article>'
            % (img, meta, esc(name), esc(N.note(p, i, group)), link))

def item_list_ld(products, name):
    return {"@context": "https://schema.org", "@type": "ItemList", "name": name,
            "itemListElement": [{"@type": "ListItem", "position": k + 1,
                                 "name": ((N.brand_of(p) + " ") if N.brand_of(p) else "") + N.short_name(p),
                                 "url": url(p)} for k, p in enumerate(products)]}

def crumb_ld(label, slug):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Online Piano University", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Shop", "item": SITE + "/shop/"},
        {"@type": "ListItem", "position": 3, "name": label, "item": SITE + "/shop/" + slug + ".html"}]}

def faq_ld(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}

def faq_html(faqs):
    return "".join("<details><summary>%s</summary><p>%s</p></details>" % (esc(q), esc(a)) for q, a in faqs)

def related_html(slugs):
    names = {pg["slug"]: (pg["icon"], pg["label"], pg["blurb"]) for pg in C.PAGES}
    names.update({k: ("🎁", v["label"], v["blurb"]) for k, v in GUIDES.items()})
    names["which-digital-piano-to-buy"] = ("🎹", "Which Digital Piano to Buy", "A long guide for adult beginners.")
    cards = "".join('<a class="catcard" href="%s.html"><div class="ico">%s</div><h3>%s</h3><p>%s</p></a>' %
                    (s, names[s][0], esc(names[s][1]), esc(names[s][2])) for s in slugs)
    return '<div class="catgrid">%s</div>' % cards

OPU_PATH = """<section class="shop-cta"><h2>Your path into Online Piano University</h2>
<p>The shop exists to support your learning. The learning itself is free: all 41 lessons of my beginner course are published, and I give feedback on your playing at no charge.</p>
<p class="shop-links"><a class="btn" href="../free-course.html">&#9654; Start the free 41-lesson course</a> <a class="btn ghost" href="../submit.html">Send me your playing for feedback &rarr;</a> <a class="btn ghost" href="../gift-certificate.html">Give online piano lessons</a></p></section>"""

BANNER_LEAD = "Black Friday at Online Piano University"  # change to "Holiday gifts at Online Piano University" later
BANNER_REST = "lock in 2026 lesson prices. Prices increase January 1, 2027 \u2014 gift certificates bought by December 31 keep today's price."
BANNER = ('<aside class="bf-banner" role="note"><div class="wrap"><a href="../gift-certificate.html"><strong>%s:</strong> %s</a></div></aside>'
          % (BANNER_LEAD, BANNER_REST.replace("'", "&#39;")))

def page(slug, title, desc, h1, eyebrow, sub, body, lds, crumb, canon=None):
    assert len(title) <= 60, (slug, len(title), title)
    assert 110 <= len(desc) <= 155, (slug, len(desc), desc)
    canon = canon or "%s/shop/%s.html" % (SITE, slug)
    og = ('<title>%s</title>\n<meta name="description" content="%s">\n<link rel="canonical" href="%s">\n'
          '<meta property="og:title" content="%s">\n<meta property="og:description" content="%s">\n<meta property="og:type" content="website">\n'
          '<meta property="og:url" content="%s">\n<meta property="og:image" content="%s/images/og-adult-piano-lessons-dr-maria-pisarenko.jpg">\n'
          '<meta property="og:image:alt" content="Dr. Maria Pisarenko, DMA, concert pianist, at the piano. Online Piano University: piano lessons for adults.">\n'
          '<meta property="og:site_name" content="Online Piano University">\n<meta name="twitter:card" content="summary_large_image">\n'
          '<meta name="twitter:title" content="%s">\n<meta name="twitter:description" content="%s">\n<meta name="twitter:image" content="%s/images/og-adult-piano-lessons-dr-maria-pisarenko.jpg">\n'
          % (attr(title), attr(desc), canon, attr(title), attr(desc), canon, SITE, attr(title), attr(desc), SITE))
    ld = "\n".join('<script type="application/ld+json">%s</script>' % jd(o) for o in lds)
    crumbs = '<p class="shop-crumb"><a href="../index.html">Home</a> / %s</p>' % crumb
    hero = ('<section class="pagehero"><div class="wrap">%s<span class="eyebrow" style="color:var(--gold)">%s</span><h1>%s</h1>'
            '<p class="sub">%s</p><p class="aff-note" role="note"><strong>Affiliate disclosure.</strong> %s</p>'
            '<p class="illus-note">%s</p></div></section>'
            % (crumbs, esc(eyebrow), esc(h1), sub, DISC, ILLUS_NOTE))
    mid = BLOCKS["mid"]
    return (HEAD_PRE + og + HEAD_MID + ld + "\n</head>\n<body class=\"shop-page\">\n\n" + HEADER + "\n" + BLOCKS["top"] + hero + "\n" + BANNER + "\n" +
            body + "\n" + mid + "\n" + CAPTURE + "\n" + BLOCKS["ages"] + "\n" + BLOCKS["bottom"] + "\n" + cb.SCRIPT + "\n" + FOOTER +
            "\n\n" + SCRIPTS + "\n</body>\n</html>\n")

def section(inner, narrow=False):
    return '<section class="shop-section"><div class="wrap">%s</div></section>' % inner

def tiers_html(products, cat, group=None):
    out = []; idx = 0
    for key, label in TIERS:
        ps = [p for p in products if p["tier"] == key]
        if not ps: continue
        out.append('<div class="tier-head"><h2>%s</h2><span>%d picks</span></div><div class="pgrid">' % (label, len(ps)))
        for p in ps:
            out.append(card(p, idx, cat, group, tier_tag=False)); idx += 1
        out.append("</div>")
    return "".join(out)

def merged(cats):
    seen, out = set(), []
    for c in cats:
        for p in DATA:
            if p["category"] == c and p["asin"] not in seen:
                seen.add(p["asin"]); out.append(p)
    return out

REPORT = []

def build_category(pg):
    prods = merged(pg["cats"])
    if not prods: return None
    slug = pg["slug"]
    why = D.WHY_GIFT if slug in D.GIFT_SLUGS else D.WHY
    crit = "".join("<li>%s</li>" % c for c in pg["criteria"])
    links = D.LINKS.get(slug, [])
    morelinks = ""
    if links:
        morelinks = '<p class="shop-links">' + " ".join('<a class="btn dark" href="%s">%s</a>' % (h, esc(t)) for h, t in links) + "</p>"
    body = section(
        '<div class="shop-prose"><p class="lead">%s</p></div>' % esc(pg["intro"]) +
        '<div class="howbox"><h2>Why I recommend this gear</h2><p style="margin:0">%s</p></div>' % esc(why) +
        '<div class="howbox"><h2>How I choose</h2><ul>%s</ul></div>' % crit +
        '<div class="howbox"><h2>How this connects to your learning</h2><p style="margin:0">%s</p></div>' % esc(D.LEARN[slug].split(": ", 1)[1].capitalize() if False else D.LEARN[slug]) +
        tiers_html(prods, slug) +
        (('<div class="shop-prose">%s</div>' % D.DEPTH[slug]) if slug in D.DEPTH else "") +
        '<h2 style="margin-top:40px">Questions adults ask</h2><div class="shop-faq">%s</div>%s' % (faq_html(pg["faqs"]), morelinks) +
        '<h2 style="margin-top:40px">More from the shop</h2>' + related_html(pg["related"]) +
        OPU_PATH + AUTHOR)
    lds = [item_list_ld(prods, pg["h1"]), faq_ld(pg["faqs"]), crumb_ld(pg["label"], slug)]
    html_ = page(slug, pg["title"], pg["desc"], pg["h1"], "Chosen by a concert pianist", esc(pg["intro"]), body, lds,
                 '<a href="index.html">Shop</a> / %s' % esc(pg["label"]))
    (OUT / (slug + ".html")).write_text(html_, encoding="utf-8")
    REPORT.append((slug + ".html", pg["title"], len(prods)))
    return prods

def pick(asins):
    return [BY_ASIN[a] for a in asins if a in BY_ASIN]

def band_of(p):
    x = p["price_usd_seen"] or 0
    return x

def guide_sections(sections, cat):
    out = []; idx = 0; total = []
    for title, intro, prods in sections:
        if not prods: continue
        out.append('<div class="tier-head"><h2>%s</h2><span>%d picks</span></div>' % (esc(title), len(prods)))
        if intro: out.append('<p class="lead" style="margin:0 0 14px">%s</p>' % esc(intro))
        out.append('<div class="pgrid">')
        for p in prods:
            out.append(card(p, idx, cat, tier_tag=False)); idx += 1; total.append(p)
        out.append("</div>")
    return "".join(out), total

def band_sections(pool, bands, cap=9):
    res = []
    for label, lo, hi, intro in bands:
        ps = [p for p in pool if p["price_usd_seen"] and lo <= p["price_usd_seen"] < hi]
        by = collections.OrderedDict()
        for p in ps: by.setdefault(p["category"], []).append(p)
        picks = []
        while len(picks) < cap and any(by.values()):
            for k in list(by):
                if by[k] and len(picks) < cap: picks.append(by[k].pop(0))
        res.append((label, intro, picks))
    return res

def gift_pool(extra_asins):
    seen, out = set(), []
    for p in pick(extra_asins) + [p for p in DATA if p["use_case"] in ("gift", "home", "luxury")]:
        if p["asin"] not in seen:
            seen.add(p["asin"]); out.append(p)
    return out

def build_guide(slug):
    g = GUIDES[slug]
    sections = g["sections"](pick, gift_pool, band_sections)
    inner, total = guide_sections(sections, slug)
    body = section(
        '<div class="shop-prose">%s</div>' % g["intro_html"] +
        '<div class="howbox"><h2>Why this guide is here</h2><p style="margin:0">%s</p></div>' % esc(D.WHY_GIFT if g.get("gift", True) else D.WHY) +
        inner + '<h2 style="margin-top:40px">Questions</h2><div class="shop-faq">%s</div>' % faq_html(g["faqs"]) +
        '<h2 style="margin-top:40px">More from the shop</h2>' + related_html(g["related"]) + OPU_PATH + AUTHOR)
    lds = [item_list_ld(total, g["h1"]), faq_ld(g["faqs"]), crumb_ld(g["label"], slug)]
    html_ = page(slug, g["title"], g["desc"], g["h1"], g["eyebrow"], g["sub"], body, lds, '<a href="index.html">Shop</a> / %s' % esc(g["label"]))
    (OUT / (slug + ".html")).write_text(html_, encoding="utf-8")
    REPORT.append((slug + ".html", g["title"], len(total)))

def build_article():
    a = ARTICLE
    dp = [BY_ASIN[x] for x in a["picks"] if x in BY_ASIN]
    sections = [("Budget picks", None, [p for p in dp if p["tier"] == "budget"]),
                ("Mid-range picks", None, [p for p in dp if p["tier"] == "mid"]),
                ("Premium picks", None, [p for p in dp if p["tier"] == "premium"])]
    picks_html, total = guide_sections(sections, "which-digital-piano-to-buy")
    body = section('<div class="shop-prose">%s</div>' % a["html_before"] + picks_html +
                   '<div class="shop-prose">%s</div>' % a["html_after"] +
                   '<h2 style="margin-top:40px">Questions adults ask</h2><div class="shop-faq">%s</div>' % faq_html(a["faqs"]) +
                   '<h2 style="margin-top:40px">More from the shop</h2>' + related_html(a["related"]) + OPU_PATH + AUTHOR)
    lds = [item_list_ld(total, a["h1"]), faq_ld(a["faqs"]), crumb_ld(a["label"], "which-digital-piano-to-buy")]
    page_html = page("which-digital-piano-to-buy", a["title"], a["desc"], a["h1"], "A teacher's buying guide", a["sub"], body, lds,
                     '<a href="index.html">Shop</a> / %s' % esc(a["label"]))
    (OUT / "which-digital-piano-to-buy.html").write_text(page_html, encoding="utf-8")
    REPORT.append(("which-digital-piano-to-buy.html", a["title"], len(total)))
    words = len(re.sub(r"<[^>]+>", " ", a["html_before"] + a["html_after"]).split())
    print("article words (excluding product cards and FAQ):", words)

def build_hub():
    h = HUB
    cats = "".join('<a class="catcard" href="%s.html"><div class="ico">%s</div><h3>%s</h3><p>%s</p></a>' %
                   (pg["slug"], pg["icon"], esc(pg["label"]), esc(pg["blurb"]))
                   for pg in C.PAGES if merged(pg["cats"]))
    guides = "".join('<a class="catcard" href="%s.html"><div class="ico">%s</div><h3>%s</h3><p>%s</p></a>' %
                     (k, "🎁" if k != "holiday-gift-guide" else "🎄", esc(v["label"]), esc(v["blurb"])) for k, v in GUIDES.items())
    guides += '<a class="catcard" href="which-digital-piano-to-buy.html"><div class="ico">🎹</div><h3>Which Digital Piano to Buy</h3><p>A long guide for adult beginners.</p></a>'
    tops = pick(h["top"])
    top_html = '<div class="pgrid">' + "".join(card(p, i, "top-picks") for i, p in enumerate(tops)) + "</div>"
    body = (section('<div class="shop-prose"><p class="lead">%s</p></div>' % h["intro"] +
                    '<div class="howbox"><h2>Why I recommend this gear</h2><p style="margin:0">%s</p></div>' % esc(D.WHY) +
                    '<h2 style="margin-top:34px">Shop by category</h2><p class="muted">Each page starts with the question a buyer asks and ends with a way into the lessons.</p>' +
                    '<div class="catgrid">%s</div>' % cats) +
            section("<h2>Masha's top picks</h2><p class=\"muted\">Eight places to start, each described only by its own listing.</p>" + top_html) +
            section('<h2>Gift guides</h2><div class="catgrid">%s</div>' % guides +
                    '<div class="teaser" style="margin-top:20px"><div style="font-size:2.2rem" aria-hidden="true">🎼</div><h3>Online Piano University Collection &mdash; coming soon</h3>'
                    '<p style="margin:0">Things made for my own students, to go with the free course and the upcoming method books. Join the email list below to hear first.</p></div>') +
            section('<h2>Questions adults ask</h2><div class="shop-faq">%s</div>' % faq_html(h["faqs"])) +
            section('<h2>Learn before you buy</h2><p>You do not need to buy anything to begin. The course is free, and so is feedback on your playing.</p>'
                    '<p class="shop-links"><a class="btn" href="../free-course.html">&#9654; Free 41-lesson course</a> <a class="btn dark" href="../lessons.html">Private online lessons</a> <a class="btn dark" href="../submit.html">Free feedback on your playing</a> <a class="btn dark" href="../books.html">Books &amp; Gear</a></p>' +
                    OPU_PATH + AUTHOR))
    coll = {"@context": "https://schema.org", "@type": "CollectionPage", "name": h["h1"], "url": SITE + "/shop/", "description": h["desc"],
            "isPartOf": {"@type": "WebSite", "name": "Online Piano University", "url": SITE + "/"}}
    il = {"@context": "https://schema.org", "@type": "ItemList", "name": "Shop categories",
          "itemListElement": [{"@type": "ListItem", "position": k + 1, "name": pg["label"], "url": "%s/shop/%s.html" % (SITE, pg["slug"])}
                              for k, pg in enumerate([x for x in C.PAGES if merged(x["cats"])])]}
    bl = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Online Piano University", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Shop", "item": SITE + "/shop/"}]}
    html_ = page("index", h["title"], h["desc"], h["h1"], "Online Piano University shop", h["sub"], body, [coll, il, bl, faq_ld(h["faqs"])], "Shop",
                 canon=SITE + "/shop/")
    (OUT / "index.html").write_text(html_, encoding="utf-8")
    REPORT.append(("index.html", h["title"], len(tops)))

def main():
    OUT.mkdir(exist_ok=True)
    build_hub()
    for pg in C.PAGES: build_category(pg)
    for s in GUIDES: build_guide(s)
    build_article()
    for r in REPORT: print("%-40s %2d  %s" % (r[0], r[2], r[1]))

if __name__ == "__main__":
    main()
