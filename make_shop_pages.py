# -*- coding: utf-8 -*-
"""Builds the affiliate shop: shop/*.html, from _shop/products.json (outside the repo).

Run from opu-website/:  python3 make_shop_pages.py [path/to/products.json]
Rules baked in: no prices, no ratings or review counts, no Amazon images (cards use our own
type illustrations from images/shop/types/, mapped in shop_illus.py); every link is
https://www.amazon.com/dp/{ASIN}?tag=musicalgalaxi-20 with rel="sponsored nofollow noopener".
price_usd_seen is used only to bucket gift guides, and is never printed.

2026-11-10: SEO + store layer (shop_seo.py) - answer-first hero lines, buyer-question H2s,
new pages (accessories, metronomes, music stands, music lovers, Christmas + Hanukkah, stocking
stuffers), shop-by-need / shop-by-budget / holiday rows on the hub, department nav, a "who it's
for" line on every card, read-next links, and the international note behind ONELINK_ACTIVE.
"""
import json, html, re, sys, pathlib, importlib.util, collections

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import shop_content as C, shop_notes as N, shop_depth as D, shop_illus as SI
from shop_text import ARTICLE, GUIDES, HUB
import shop_seo as S

SITE = "https://onlinepianouniversity.com"
TAG = "musicalgalaxi-20"
DISC = ("As an Amazon Associate I earn from qualifying purchases. Some links on this page are affiliate links; "
        "buying through them costs you nothing extra.")
TIERS = [("budget", "Budget picks"), ("mid", "Mid-range picks"), ("premium", "Premium picks"), ("luxury", "Luxury picks")]
TIER_LABEL = dict(TIERS)
ILLUS_NOTE = "Illustrations show the type of product; see the exact item and its photos on Amazon."
OUT = HERE / "shop"
PRODUCTS = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE.parent / "_shop" / "products.json"

# International buyers. Amazon OneLink is NOT active on the musicalgalaxi-20 account yet, so the
# visible line only says the links go to Amazon.com. Once OneLink is live, set this to True and
# regenerate: the OneLink sentence replaces the visible line on every shop page.
ONELINK_ACTIVE = False
INTL_VISIBLE = "Links go to Amazon.com; Amazon ships many items internationally."
INTL_ONELINK = "Shopping from the UK, Canada, Germany or Australia? Amazon links open your local store when available."

def intl_note():
    if ONELINK_ACTIVE:
        return '<p class="intl-note">%s</p>' % INTL_ONELINK
    return ('<!-- ONELINK placeholder (switch on with ONELINK_ACTIVE = True in make_shop_pages.py): %s -->'
            '<p class="intl-note">%s</p>' % (INTL_ONELINK, INTL_VISIBLE))

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

S.apply(C.PAGES, GUIDES, HUB, ARTICLE, D)

def url(p): return "https://www.amazon.com/dp/%s?tag=%s" % (p["asin"], TAG)

def card(p, i, cat, group=None, tier_tag=True):
    """Product card: our own type illustration on top (never an Amazon photo), the whole card clickable,
    the listing-based note, and a "who it's for" line."""
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
            '<p class="pfor"><strong>I suggest it for</strong> %s</p>'
            '<a class="btn shop-btn" %s>Check today&#39;s price on Amazon</a></article>'
            % (img, meta, esc(name), esc(N.note(p, i, group)), esc(S.who_for(p)), link))

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
    names.update({k: (v.get("icon", "🎁"), v["label"], v["blurb"]) for k, v in GUIDES.items()})
    names["which-digital-piano-to-buy"] = ("🎹", "Which Digital Piano to Buy", "A long guide for adult beginners.")
    cards = "".join('<a class="catcard" href="%s.html"><div class="ico">%s</div><h3>%s</h3><p>%s</p></a>' %
                    (s, names[s][0], esc(names[s][1]), esc(names[s][2])) for s in slugs)
    return '<div class="catgrid">%s</div>' % cards

def read_next(slug):
    items = "".join('<li><a href="../blog/%s.html">%s</a></li>' % (b, esc(S.BLOG_TITLES[b])) for b in S.BLOG.get(slug, []))
    items += ('<li><a href="../gift-certificate.html">Give online piano lessons as a gift</a></li>'
              '<li><a href="../lessons.html">Private online piano lessons with me</a></li>')
    return '<h2 style="margin-top:40px">Where should you read next?</h2><ul class="readnext">%s</ul>' % items

OPU_PATH = """<section class="shop-cta"><h2>Would you rather learn than buy more gear?</h2>
<p>The shop exists to support your learning. The learning itself can start free: all 41 lessons of my beginner course are published, and I give feedback on your playing at no charge. When you want a teacher, I take private students online.</p>
<p class="shop-links"><a class="btn" href="../free-course.html">&#9654; Start the free 41-lesson course</a> <a class="btn ghost" href="../lessons.html">Private online lessons</a> <a class="btn ghost" href="../submit.html">Send me your playing for feedback &rarr;</a> <a class="btn ghost" href="../gift-certificate.html">Give online piano lessons</a></p></section>"""

GIFT_CARD = ('<a class="giftcard" href="../gift-certificate.html"><div class="gc-art" aria-hidden="true">🎁</div><div>'
             '<span class="gc-eyebrow">Featured gift</span><h3>Gift online piano lessons</h3>'
             '<p>Private online lessons with me, Dr. Maria Pisarenko, D.M.A., concert pianist and professor. A gift certificate suits an adult beginner, '
             'a returning player, or a parent who always wanted to learn, wherever they live.</p>'
             '<span class="btn">Give online lessons &rarr;</span></div></a>')

BANNER_LEAD = "Black Friday at Online Piano University"  # change to "Holiday gifts at Online Piano University" later
BANNER_REST = "lock in 2026 lesson prices. Prices increase January 1, 2027 — gift certificates bought by December 31 keep today's price."
BANNER = ('<aside class="bf-banner" role="note"><div class="wrap"><a href="../gift-certificate.html"><strong>%s:</strong> %s</a></div></aside>'
          % (BANNER_LEAD, BANNER_REST.replace("'", "&#39;")))

# department nav shown under the banner on every shop page
NAV = [("index", "Shop home"), ("digital-pianos", "Digital pianos"), ("keyboards", "Keyboards"), ("piano-accessories", "Accessories"),
       ("headphones-for-piano", "Headphones"), ("piano-benches-and-stands", "Benches"), ("piano-pedals", "Pedals"),
       ("music-stands", "Music stands"), ("metronomes-and-tuners", "Metronomes"), ("stand-lights", "Piano lamps"),
       ("piano-books-and-sheet-music", "Books"), ("record-yourself-playing", "Recording"), ("music-home-decor", "Decor"),
       ("gifts-for-pianists", "Gifts"), ("christmas-gifts-for-pianists", "Christmas")]

def shop_nav(slug):
    lis = "".join('<li><a href="%s.html"%s>%s</a></li>' % (s, ' aria-current="page"' if s == slug else "", esc(t)) for s, t in NAV)
    return '<nav class="shop-nav" aria-label="Shop departments"><div class="wrap"><ul>%s</ul></div></nav>' % lis

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
            '<p class="sub">%s</p><p class="aff-note" role="note"><strong>Affiliate disclosure.</strong> %s</p>%s'
            '<p class="illus-note">%s</p></div></section>'
            % (crumbs, esc(eyebrow), esc(h1), sub, DISC, intl_note(), ILLUS_NOTE))
    mid = BLOCKS["mid"]
    return (HEAD_PRE + og + HEAD_MID + ld + "\n</head>\n<body class=\"shop-page\">\n\n" + HEADER + "\n" + BLOCKS["top"] + hero + "\n" + BANNER + "\n" +
            shop_nav(slug) + "\n" +
            body + "\n" + mid + "\n" + CAPTURE + "\n" + BLOCKS["ages"] + "\n" + BLOCKS["bottom"] + "\n" + cb.SCRIPT + "\n" + FOOTER +
            "\n\n" + SCRIPTS + "\n</body>\n</html>\n")

def section(inner, narrow=False):
    return '<section class="shop-section"><div class="wrap">%s</div></section>' % inner

def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def tiers_html(products, cat, group=None):
    out = []; idx = 0
    for key, label in TIERS:
        ps = [p for p in products if p["tier"] == key]
        if not ps: continue
        out.append('<div class="tier-head" id="%s"><h3>%s</h3><span>%d picks</span></div><div class="pgrid">' % (key, label, len(ps)))
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

def pick(asins):
    missing = [a for a in asins if a not in BY_ASIN]
    assert not missing, ("ASIN(s) not in products.json", missing)
    return [BY_ASIN[a] for a in asins]

def prods_of(pg):
    return pick(pg["asins"]) if pg.get("asins") else merged(pg["cats"])

REPORT = []

def build_category(pg):
    prods = prods_of(pg)
    if not prods: return None
    slug = pg["slug"]
    assert len(prods) >= 6, (slug, "thin page", len(prods))
    look, learn, pickq, faqq = pg["q"]
    why = D.WHY_GIFT if slug in D.GIFT_SLUGS else D.WHY
    crit = "".join("<li>%s</li>" % c for c in pg["criteria"])
    links = D.LINKS.get(slug, [])
    morelinks = ""
    if links:
        morelinks = '<p class="shop-links">' + " ".join('<a class="btn dark" href="%s">%s</a>' % (h, esc(t)) for h, t in links) + "</p>"
    body = section(
        '<div class="shop-prose"><p class="lead">%s</p></div>' % esc(pg["intro"]) +
        '<div class="howbox"><h2>Why trust a concert pianist&#39;s picks?</h2><p style="margin:0">%s</p></div>' % esc(why) +
        '<div class="howbox"><h2>%s</h2><ul>%s</ul></div>' % (esc(look), crit) +
        '<div class="howbox"><h2>%s</h2><p style="margin:0">%s</p></div>' % (esc(learn), esc(D.LEARN[slug])) +
        '<h2 style="margin-top:40px">%s</h2>' % esc(pickq) +
        tiers_html(prods, slug) +
        (('<div class="shop-prose">%s</div>' % D.DEPTH[slug]) if slug in D.DEPTH else "") +
        '<h2 style="margin-top:40px">%s</h2><div class="shop-faq">%s</div>%s' % (esc(faqq), faq_html(pg["faqs"]), morelinks) +
        read_next(slug) +
        '<h2 style="margin-top:40px">What else might you need?</h2>' + related_html(pg["related"]) +
        OPU_PATH + AUTHOR)
    lds = [item_list_ld(prods, pg["h1"]), faq_ld(pg["faqs"]), crumb_ld(pg["label"], slug)]
    html_ = page(slug, pg["title"], pg["desc"], pg["h1"], "Chosen by a concert pianist", esc(pg["answer"]), body, lds,
                 '<a href="index.html">Shop</a> / %s' % esc(pg["label"]))
    (OUT / (slug + ".html")).write_text(html_, encoding="utf-8")
    REPORT.append((slug + ".html", pg["title"], pg["desc"], len(prods)))
    return prods

def band_of(p):
    x = p["price_usd_seen"] or 0
    return x

def guide_sections(sections, cat):
    out = []; idx = 0; total = []
    for sec in sections:
        title, intro, prods = sec[0], sec[1], sec[2]
        sid = sec[3] if len(sec) > 3 else slugify(title)
        if not prods: continue
        out.append('<div class="tier-head" id="%s"><h3>%s</h3><span>%d picks</span></div>' % (sid, esc(title), len(prods)))
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
    assert len(total) >= 6, (slug, "thin page", len(total))
    body = section(
        '<div class="shop-prose">%s</div>' % g["intro_html"] +
        (GIFT_CARD if g.get("gift_card") else "") +
        '<div class="howbox"><h2>%s</h2><p style="margin:0">%s</p></div>' % (esc(g.get("q_why", "Why trust a concert pianist's list?")),
                                                                           esc(D.WHY_GIFT if g.get("gift", True) else D.WHY)) +
        '<h2 style="margin-top:40px">%s</h2>' % esc(g["q_pick"]) + inner +
        '<h2 style="margin-top:40px">%s</h2><div class="shop-faq">%s</div>' % (esc(g["q_faq"]), faq_html(g["faqs"])) +
        read_next(slug) +
        '<h2 style="margin-top:40px">What else might you like?</h2>' + related_html(g["related"]) + OPU_PATH + AUTHOR)
    lds = [item_list_ld(total, g["h1"]), faq_ld(g["faqs"]), crumb_ld(g["label"], slug)]
    html_ = page(slug, g["title"], g["desc"], g["h1"], g["eyebrow"], esc(g["answer"]), body, lds, '<a href="index.html">Shop</a> / %s' % esc(g["label"]))
    (OUT / (slug + ".html")).write_text(html_, encoding="utf-8")
    REPORT.append((slug + ".html", g["title"], g["desc"], len(total)))

def build_article():
    a = ARTICLE
    dp = [BY_ASIN[x] for x in a["picks"] if x in BY_ASIN]
    sections = [("Budget picks", None, [p for p in dp if p["tier"] == "budget"]),
                ("Mid-range picks", None, [p for p in dp if p["tier"] == "mid"]),
                ("Premium picks", None, [p for p in dp if p["tier"] == "premium"])]
    picks_html, total = guide_sections(sections, "which-digital-piano-to-buy")
    body = section('<div class="shop-prose">%s</div>' % a["html_before"] + picks_html +
                   '<div class="shop-prose">%s</div>' % a["html_after"] +
                   '<h2 style="margin-top:40px">What else do adults ask about buying a digital piano?</h2><div class="shop-faq">%s</div>' % faq_html(a["faqs"]) +
                   read_next("which-digital-piano-to-buy") +
                   '<h2 style="margin-top:40px">What else might you need?</h2>' + related_html(a["related"]) + OPU_PATH + AUTHOR)
    lds = [item_list_ld(total, a["h1"]), faq_ld(a["faqs"]), crumb_ld(a["label"], "which-digital-piano-to-buy")]
    page_html = page("which-digital-piano-to-buy", a["title"], a["desc"], a["h1"], "A teacher's buying guide", a["sub"], body, lds,
                     '<a href="index.html">Shop</a> / %s' % esc(a["label"]))
    (OUT / "which-digital-piano-to-buy.html").write_text(page_html, encoding="utf-8")
    REPORT.append(("which-digital-piano-to-buy.html", a["title"], a["desc"], len(total)))
    words = len(re.sub(r"<[^>]+>", " ", a["html_before"] + a["html_after"]).split())
    print("article words (excluding product cards and FAQ):", words)

# ---------------------------------------------------------------- hub
NEEDS = [("Start learning", "digital-pianos", "digital-piano-portable", "A piano with weighted keys."),
         ("Practice quietly", "headphones-for-piano", "headphones", "Headphones for any hour."),
         ("Sit correctly", "piano-benches-and-stands", "piano-bench", "Benches at the right height."),
         ("Record yourself", "record-yourself-playing", "usb-microphone", "Microphones, mounts, light."),
         ("Gifts", "gifts-for-pianists", "gift-box", "Gift ideas by size of gift."),
         ("Home & decor", "music-home-decor", "wall-art", "Piano decor for a music corner."),
         ("Wellbeing", "music-and-wellbeing", "singing-bowl", "Listening gear and books.")]

# words only, never numbers; groups come from the products.json tier field
BUDGETS = [("budget-small", "Small gifts", "Clips, journals, metronomes and music socks: small things used every week.", ("budget",),
            ["0793584744", "B07DK7PDFH", "B0B12CJC6G", "B0DGNV226S"]),
           ("budget-mid", "Mid-range", "A better pedal, a bench, studio headphones or a classic metronome.", ("mid",),
            ["B00HVLUR54", "B000K19HYY", "B0D945K8FN", "B0C7GR2YKZ"]),
           ("budget-splurge", "Splurge", "A digital piano to keep, reference headphones or a great box set.", ("premium", "luxury"),
            ["B0CBN7HYKB", "B08J9MVB6W", "B0086WQNZ0", "B07N3S4X3P"])]

HOLIDAY = [("🎄", "Christmas gifts for pianists", "christmas-gifts-for-pianists.html"),
           ("🕎", "Hanukkah gifts for musicians", "christmas-gifts-for-pianists.html#hanukkah-gifts-for-musicians"),
           ("🧦", "Stocking stuffers for musicians", "stocking-stuffers-for-musicians.html"),
           ("🎶", "Gifts for music lovers", "gifts-for-music-lovers.html"),
           ("🍎", "Gifts for music teachers", "gifts-for-piano-teachers.html"),
           ("🎹", "Gifts for adult beginners", "gifts-for-adult-beginners.html")]

HUB_FAQS = [("Is this an online piano store?", "Yes, a curated one: it is my store of recommendations. You browse here, and every purchase happens on Amazon, which sells, ships and handles returns. I choose each item as a concert pianist who teaches adults."),
            ("What should an adult beginner buy first?", "An 88-key digital piano with weighted keys, a sustain pedal, an adjustable bench and a pair of closed-back headphones. Nothing else is needed to start."),
            ("Which piano accessories do I really need?", "A piano-style sustain pedal, an adjustable bench, headphones and a light for the page. A metronome, a book clip and a dust cover come next."),
            ("Can I buy from outside the US?", "The links go to Amazon.com, and Amazon ships many items internationally. Check delivery to your country on the listing before you order."),
            ("Are these affiliate links?", "Yes. As an Amazon Associate I earn from qualifying purchases, at no extra cost to you. I do not print prices; open the listing on Amazon to check today's price.")]

def build_hub():
    h = HUB
    cat_pages = [pg for pg in C.PAGES if prods_of(pg)]
    cat_guides = [(k, v) for k, v in GUIDES.items() if v.get("category")]
    gift_guides = [(k, v) for k, v in GUIDES.items() if not v.get("category")]
    catcard = lambda s, ico, lab, bl: '<a class="catcard" href="%s.html"><div class="ico">%s</div><h3>%s</h3><p>%s</p></a>' % (s, ico, esc(lab), esc(bl))
    cats = "".join(catcard(k, v["icon"], v["label"], v["blurb"]) for k, v in cat_guides)
    cats += "".join(catcard(pg["slug"], pg["icon"], pg["label"], pg["blurb"]) for pg in cat_pages)
    guides = "".join(catcard(k, v.get("icon", "🎁"), v["label"], v["blurb"]) for k, v in gift_guides)
    guides += catcard("which-digital-piano-to-buy", "🎹", "Which Digital Piano to Buy", "A long guide for adult beginners.")
    needs = "".join('<a class="needcard" href="%s.html"><img src="../images/shop/types/%s.svg" width="600" height="450" loading="lazy" decoding="async" '
                    'alt="Illustration for %s: %s"><h3>%s</h3><p>%s</p></a>'
                    % (s, ty, attr(lab.lower()), attr(TYPES_ALT(ty)), esc(lab), esc(bl)) for lab, s, ty, bl in NEEDS)
    brow = "".join('<a class="budgetcard" href="#%s"><span class="lvl">Shop by budget</span><h3>%s</h3><p>%s</p></a>' % (bid, esc(lab), esc(bl))
                   for bid, lab, bl, tiers, _ in BUDGETS)
    bgroups = ""; k = 0
    for bid, lab, bl, tiers, asins in BUDGETS:
        ps = pick(asins)
        assert all(p["tier"] in tiers for p in ps), (bid, [(p["asin"], p["tier"]) for p in ps])
        bgroups += '<div class="tier-head" id="%s"><h3>%s</h3><span>%d picks</span></div><div class="pgrid">' % (bid, esc(lab), len(ps))
        for p in ps:
            bgroups += card(p, k, "budget-" + bid); k += 1
        bgroups += "</div>"
    hol = "".join('<a href="%s"><span aria-hidden="true">%s</span>%s</a>' % (href, ico, esc(t)) for ico, t, href in HOLIDAY)
    hol += '<a href="../gift-certificate.html"><span aria-hidden="true">🎁</span>Gift online lessons</a>'
    tops = pick(h["top"])
    top_html = '<div class="pgrid">' + "".join(card(p, i, "top-picks") for i, p in enumerate(tops)) + "</div>"
    body = (section('<div class="shop-prose"><p class="lead">%s</p></div>' % esc(h["intro"]) +
                    '<h2 style="margin-top:30px">What do you need today?</h2><p class="muted">Shop by need: start with the problem you want to solve.</p>' +
                    '<div class="needgrid">%s</div>' % needs +
                    GIFT_CARD +
                    '<div class="holiday-strip"><h2>Which holiday gift should you give a musician?</h2>'
                    '<p>Christmas, Hanukkah and small gifts for the stocking, chosen by a concert pianist.</p><div class="holrow">%s</div></div>' % hol) +
            section('<h2>Which department are you shopping for?</h2><p class="muted">Each page starts with the question a buyer asks and ends with a way into the lessons.</p>'
                    '<div class="catgrid">%s</div>' % cats +
                    '<div class="howbox"><h2>Why trust a concert pianist&#39;s store?</h2><p style="margin:0">%s</p></div>' % esc(D.WHY)) +
            section("<h2>Where should a new pianist start?</h2><p class=\"muted\">My top picks: eight places to start, each described only by its own listing.</p>" + top_html) +
            section('<h2>How much do you want to spend?</h2><p class="muted">Shop by budget, described in words. Open any listing on Amazon to see today&#39;s price.</p>'
                    '<div class="budgetgrid">%s</div>' % brow + bgroups) +
            section('<h2>Which gift guide fits the person you are shopping for?</h2><div class="catgrid">%s</div>' % guides +
                    '<div class="teaser" style="margin-top:20px"><div style="font-size:2.2rem" aria-hidden="true">🎼</div><h3>Online Piano University Collection &mdash; coming soon</h3>'
                    '<p style="margin:0">Things made for my own students, to go with the free course and the upcoming method books. Join the email list below to hear first.</p></div>') +
            section('<h2>What do buyers ask about this online piano store?</h2><div class="shop-faq">%s</div>' % faq_html(HUB_FAQS)) +
            section('<h2>Do you need to buy anything to begin?</h2><p>No. The course is free, and so is feedback on your playing.</p>'
                    '<p class="shop-links"><a class="btn" href="../free-course.html">&#9654; Free 41-lesson course</a> <a class="btn dark" href="../lessons.html">Private online lessons</a> <a class="btn dark" href="../submit.html">Free feedback on your playing</a> <a class="btn dark" href="../books.html">Books &amp; Gear</a></p>' +
                    read_next("index") + OPU_PATH + AUTHOR))
    coll = {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Online Piano Store", "alternateName": h["h1"],
            "url": SITE + "/shop/", "description": h["desc"],
            "about": "Piano gear, piano accessories and music gifts recommended by Dr. Maria Pisarenko, D.M.A.",
            "isPartOf": {"@type": "WebSite", "name": "Online Piano University", "url": SITE + "/"},
            "publisher": {"@type": "Organization", "name": "Online Piano University", "url": SITE + "/"}}
    allpages = [(k, v["label"]) for k, v in cat_guides] + [(pg["slug"], pg["label"]) for pg in cat_pages] + [(k, v["label"]) for k, v in gift_guides] + \
               [("which-digital-piano-to-buy", "Which Digital Piano to Buy")]
    il = {"@context": "https://schema.org", "@type": "ItemList", "name": "Online piano store departments",
          "itemListElement": [{"@type": "ListItem", "position": k + 1, "name": lab, "url": "%s/shop/%s.html" % (SITE, s)}
                              for k, (s, lab) in enumerate(allpages)]}
    bl = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Online Piano University", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Shop", "item": SITE + "/shop/"}]}
    html_ = page("index", h["title"], h["desc"], h["h1"], "Online piano store", esc(h["answer"]), body, [coll, il, bl, faq_ld(HUB_FAQS)], "Shop",
                 canon=SITE + "/shop/")
    (OUT / "index.html").write_text(html_, encoding="utf-8")
    REPORT.append(("index.html", h["title"], h["desc"], len(tops)))

def TYPES_ALT(ty):
    return SI.TYPES[ty][1]

def main():
    OUT.mkdir(exist_ok=True)
    build_hub()
    for pg in C.PAGES: build_category(pg)
    for s in GUIDES: build_guide(s)
    build_article()
    for r in REPORT: print("%-38s %3d  %2d | %-55s %3d | %s" % (r[0], r[3], len(r[1]), r[1], len(r[2]), r[2]))
    t = [r[1] for r in REPORT]; d = [r[2] for r in REPORT]
    assert len(set(t)) == len(t), "duplicate titles"
    assert len(set(d)) == len(d), "duplicate descriptions"

if __name__ == "__main__":
    main()
