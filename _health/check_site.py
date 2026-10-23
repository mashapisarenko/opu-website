#!/usr/bin/env python3
"""
OPU site check - everything about onlinepianouniversity.com that can be verified
from the repository alone. Runs on GitHub (.github/workflows/health-check.yml) on
every push and every night, so a broken page is caught even when no Mac is on.

    python3 _health/check_site.py            # from the repo root, or from anywhere
    python3 _health/check_site.py --repo DIR # check another checkout

Standard library only. Three levels:
    BROKEN  - a real fault on the site; the run exits 1
    NOTICE  - known, someone's decision is pending (empty PAY_ slots and the like)
    OK      - checked and fine
Every check runs on its own: a check that crashes is reported as BROKEN with its
name and the rest still run. Nothing here ever needs the web.

Ported 2026-10-22 from the project's Mac-side _health/daily_check.py (the parts
that look at the site repo only), plus the checks the 2026-10-22 audits asked for:
raw "&" in <meta>, JSON-LD that does not parse, sitemap lastmod vs git, queue /
noindex parity, the three form blocks per article, og:image files, and the video
sitemap measured from each page's <iframe src>.
"""
import argparse, collections, datetime, glob, html as _html, json, os, re, subprocess, sys, traceback
import xml.etree.ElementTree as ET

HOST = "https://onlinepianouniversity.com/"
TODAY = datetime.date.today()
SITE = None  # set in main()

broken, notice, ok = [], [], []


def B(m): broken.append(m)
def N(m): notice.append(m)
def K(m): ok.append(m)


REAL_PRICES = ["$100", "$60", "$360", "$200", "$850", "$450"]
FORBIDDEN = ["10% Welcome Discount", "$85 trial", "$29 per review", "$79 a month", "$79/month",
             "sweet-truffle", "netlify.app"]
# press.html: "Las Vegas Review-Journal" / "Las Vegas Sun" are newspaper names (credentials).
GEO_ALLOWED = {"about.html", "privacy.html", "terms.html", "press.html"}
NOT_CONTENT = {"googleed832eccb886831b.html", "studio.html", "404.html"}
RAW_AMP = re.compile(r'&(?![a-zA-Z][a-zA-Z0-9]*;|#[0-9]+;|#x[0-9a-fA-F]+;)')
LD_RX = re.compile(r'<script type="application/ld\+json"[^>]*>(.*?)</script>', re.S)
FORM_MARKERS = ("contact-top", "contact-mid", "contact-bottom")

# Copied from the project's _health/daily_check.py (American spelling is a standing rule).
BRITISH = {
    r"\bpractis(e|es|ed|ing)\b": "practice / practices / practiced / practicing",
    r"\bcolour(s|ed|ing|ful)?\b": "color",
    r"\bcentre(s|d)?\b": "center",
    r"\banalys(e|es|ed|ing)\b": "analyze",
    r"\bmemoris(e|es|ed|ing)\b": "memorize",
    r"\borganis(e|es|ed|ing|ation|ations)\b": "organize / organization",
    r"\brecognis(e|es|ed|ing)\b": "recognize",
    r"\bfavourite(s)?\b": "favorite",
    r"\bpedalling\b": "pedaling",
    r"\bprogramme(s)?\b": "program",
    r"\btravelling\b": "traveling",
    r"\bapologis(e|es|ed|ing)\b": "apologize",
    r"\brealis(e|es|ed|ing)\b": "realize",
    r"\brealisations?\b": "realization",   # missed until 2026-09-30 (a YouTube description)
    r"\bbehaviour(s|al)?\b": "behavior",
    r"\bneighbour(s|hood|ing)?\b": "neighbor",
    r"\bhonour(s|ed|able)?\b": "honor",
    r"\blabour(s|ed)?\b": "labor",
    r"\bdefence\b": "defense",
    r"\bgrey\b": "gray",
    r"\bwhilst\b": "while",
    r"\bamongst\b": "among",
    r"\btowards\b": "toward",
    r"\bcancelled\b": "canceled",
    r"\bmodelling\b": "modeling",
    r"\blabelled\b": "labeled",
    r"\bfulfil\b": "fulfill",
    r"\bskilful\b": "skillful",
    # --- added 2026-09-15: the forms that shipped live despite this check ---
    r"\brecognisab(le|ly)\b": "recognizable / recognizably",
    r"\borganisab(le|ly)\b": "organizable",
    r"\bfortnight(ly|s)?\b": "two weeks / every two weeks",
    r"\bspeciality\b": "specialty",
    r"\blearnt\b": "learned",
    r"\bspelt\b": "spelled",
    r"\bburnt\b": "burned",
    r"\bdreamt\b": "dreamed",
    r"\bmetre(s)?\b": "meter",
    r"\btheatre(s)?\b": "theater",
    r"\bfibre(s)?\b": "fiber",
    r"\benrol\b": "enroll",
    r"\binstalment(s)?\b": "installment",
    r"\bmarvellous\b": "marvelous",
    r"\btraveller(s)?\b": "traveler",
    r"\bcounsellor(s)?\b": "counselor",
    r"\bjewellery\b": "jewelry",
    r"\bmoustache(s)?\b": "mustache",
    r"\bmaths\b": "math",
    r"\bneighbour(s|ing|hood|hoods)?\b": "neighbor / neighboring",
    r"\bapologis(e|es|ed|ing)\b": "apologize",
}

# A prefix on a British stem hid "reorganises" from \borganis... on 2026-09-15.
# This catches ANY word ending in a British suffix; ALLOW_ISE lists the real English
# words that legitimately end that way, so only genuine faults are reported.
BRITISH_SUFFIX = re.compile(
    r"\b[A-Za-z]{3,}(?:is(?:e|es|ed|ing|ation|ations|able)|ys(?:e|es|ed|ing))\b")
ALLOW_ISE = {
    "advertise","advertises","advertised","advertising","exercise","exercises","exercised",
    "exercising","surprise","surprises","surprised","surprising","promise","promises","promised",
    "promising","raise","raises","raised","raising","comprise","comprises","comprised","precise",
    "revise","revises","revised","revising","supervise","supervises","supervised","disguise",
    "franchise","merchandise","compromise","uncompromising","compromising","compromised","compromises","otherwise","likewise",
    "expertise","paradise","arise","arises","arising","cruise","improvise","improvises",
    "improvised","improvising","premise","premises","advise","advises","advised","advising",
    "devise","devises","devised","wise","rise","rises","rising","noise","noises","praise",
    "praises","praised","praising","elise","despise","despises","chastise","televise",
    "televised","enterprise","enterprises","demise","concise","excise","incise","paraphrase",
    # Added 2026-09-21: the generic -ise sweep flagged these in correct American text.
    # "imprecise" and "stepwise" appeared in the queued pedal article and failed the
    # morning check on text that is right - the fault was the list, not the article.
    "imprecise","precisely","stepwise","clockwise","counterclockwise","crosswise",
    "lengthwise","edgewise","sidewise","anticlockwise","turnwise","piecewise",
    "poise","poised","noisewise","bruise","bruised","bruises","guise","appraise",
    "appraised","appraises","reprise","valise","treatise","expertise",
    # 2026-10-15: improvisation is the American spelling too (no -ization form).
    "improvisation","improvisations","improvisational",
}



# ---------------------------------------------------------------- helpers
def read(p):
    with open(p, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def rel(p):
    return os.path.relpath(p, SITE).replace(os.sep, "/")


def public_pages():
    """Every .html GitHub Pages serves as a site page: not .git, not blog/_*, not _health."""
    out = []
    for dirpath, dirs, files in os.walk(SITE):
        r = os.path.relpath(dirpath, SITE).replace(os.sep, "/")
        parts = [] if r == "." else r.split("/")
        if any(x.startswith(".") for x in parts) or (parts and parts[0] == "_health") \
                or any(x.startswith("_") for x in parts):
            continue
        out += [os.path.join(dirpath, f) for f in files if f.endswith(".html")]
    return sorted(out)


def queued_pages():
    return sorted(glob.glob(os.path.join(SITE, "blog", "_queue", "*.html")))


def live_articles():
    return [f for f in sorted(glob.glob(os.path.join(SITE, "blog", "*.html")))
            if os.path.basename(f) != "index.html"]


def is_noindex(text):
    return bool(re.search(r'<meta name="robots" content="[^"]*noindex', text))


def page_for_url(u):
    p = u.replace(HOST, "", 1)
    if p == "" or p.endswith("/"):
        p += "index.html"
    return os.path.join(SITE, p)


def url_for(relpath):
    if relpath == "index.html":
        return HOST
    if relpath.endswith("/index.html"):
        return HOST + relpath[:-len("index.html")]
    return HOST + relpath


def git(*args):
    return subprocess.run(["git", *args], cwd=SITE, capture_output=True, text=True,
                          timeout=60).stdout.strip()


def meta_contents(text):
    for m in re.finditer(r'<meta\b[^>]*>', text):
        c = re.search(r'\bcontent="([^"]*)"', m.group(0))
        if c:
            yield m.group(0), c.group(1)


def manifest():
    return json.loads(read(os.path.join(SITE, "blog", "_queue", "manifest.json")))


# ---------------------------------------------------------------- checks
def check_internal_links():
    missing = []
    for f in public_pages():
        for m in re.findall(r'(?:href|src)="([^"]+)"', read(f)):
            if m.startswith(("#", "mailto:", "data:", "tel:", "http", "//", "javascript:")):
                continue
            t = os.path.normpath(os.path.join(os.path.dirname(f), m.split("#")[0].split("?")[0]))
            if m.split("#")[0].split("?")[0] and not os.path.exists(t):
                missing.append(f"{rel(f)} -> {m}")
    if missing:
        B(f"{len(missing)} broken internal link(s):\n      " + "\n      ".join(missing[:15]))
    else:
        K("internal links: none broken")


def check_youtube_ids():
    bad = set()
    for f in public_pages() + queued_pages():
        for m in re.findall(r'(?:youtu\.be/|youtube(?:-nocookie)?\.com/(?:embed/|watch\?v=))([A-Za-z0-9_-]+)', read(f)):
            if not m.startswith("videoseries") and len(m) != 11:
                bad.add(f"{rel(f)} -> {m} ({len(m)} chars, a YouTube id is always 11)")
    if bad:
        B(f"{len(bad)} malformed YouTube id(s):\n      " + "\n      ".join(sorted(bad)))
    else:
        K("YouTube ids: all 11 characters")


def check_metadata():
    thin = []
    for f in public_pages():
        name, s = rel(f), read(f)
        if is_noindex(s) or os.path.basename(name) in NOT_CONTENT:
            continue
        gaps = [g for g, ok_ in (("title", re.search(r"<title>.+?</title>", s, re.S)),
                                 ("description", 'name="description"' in s),
                                 ("canonical", 'rel="canonical"' in s),
                                 ("open graph", 'property="og:' in s),
                                 ("analytics tag", "G-DZSNWWT4S4" in s)) if not ok_]
        if gaps:
            thin.append(f"{name}: no {', '.join(gaps)}")
    if thin:
        N(f"{len(thin)} page(s) missing metadata:\n      " + "\n      ".join(thin))
    else:
        K("metadata: every indexable page has title, description, canonical, OG and the GA tag")


def check_meta_raw_ampersand():
    """A bare "&" (or "<") inside a <meta content="..."> - press.html shipped two."""
    bad = []
    for f in public_pages() + queued_pages():
        for tag, c in meta_contents(read(f)):
            if RAW_AMP.search(c) or "<" in c:
                bad.append(f"{rel(f)}: {tag[:110]}")
    if bad:
        B(f"{len(bad)} <meta> tag(s) with a raw & or < in content (escape as &amp;):\n      "
          + "\n      ".join(bad[:12]))
    else:
        K("meta tags: no raw & or < in any content attribute (live and queued)")


def check_meta_lengths():
    long_d = []
    for f in public_pages():
        s = read(f)
        if is_noindex(s):
            continue
        m = re.search(r'<meta name="description" content="([^"]*)"', s)
        if m and len(_html.unescape(m.group(1))) > 160:
            long_d.append(f"{rel(f)} ({len(_html.unescape(m.group(1)))})")
    if long_d:
        B("meta description(s) over 160 characters (cut in search): " + ", ".join(long_d[:10]))
    else:
        K("meta descriptions: every indexable page within 160 characters")


def check_jsonld():
    bad, n = [], 0
    for f in public_pages() + queued_pages():
        for blk in LD_RX.findall(read(f)):
            n += 1
            try:
                json.loads(blk)
            except Exception as e:
                bad.append(f"{rel(f)}: {str(e)[:70]}")
    if bad:
        B("JSON-LD that does not parse (Google ignores the page's rich data):\n      "
          + "\n      ".join(bad[:12]))
    else:
        K(f"structured data: all {n} JSON-LD blocks parse (live and queued)")


def check_future_dates():
    future = []
    for f in public_pages() + [os.path.join(SITE, "sitemap.xml")]:
        if not os.path.exists(f):
            continue
        for m in re.findall(r"(?:datePublished|dateModified|uploadDate|<lastmod>)\"?>?\s*:?\s*\"?(\d{4}-\d{2}-\d{2})", read(f)):
            try:
                d = datetime.date.fromisoformat(m)
            except ValueError:
                continue
            # one day of grace: GitHub's clock is UTC, the site's dates are Pacific
            if d > TODAY + datetime.timedelta(days=1):
                future.append(f"{rel(f)}: {m}")
    if future:
        B(f"{len(future)} date(s) in the future:\n      " + "\n      ".join(sorted(set(future))[:12]))
    else:
        K("dates: nothing dated in the future")


def check_sitemap():
    sm = os.path.join(SITE, "sitemap.xml")
    if not os.path.exists(sm):
        B("sitemap.xml is missing"); return
    ET.parse(sm)
    text = read(sm)
    pairs = re.findall(r"<loc>(.*?)</loc>\s*<lastmod>(.*?)</lastmod>", text, re.S)
    locs = re.findall(r"<loc>([^<]+)</loc>", text)
    gone = [u for u in locs if not os.path.exists(page_for_url(u))]
    dupes = sorted({u for u in locs if locs.count(u) > 1})
    noidx = [u for u in locs if os.path.exists(page_for_url(u)) and is_noindex(read(page_for_url(u)))]
    if gone: B("sitemap lists URLs with no file:\n      " + "\n      ".join(gone))
    if dupes: B("sitemap lists the same URL more than once: " + ", ".join(dupes[:5]))
    if noidx: B("sitemap lists noindex page(s): " + ", ".join(noidx[:5]))
    # every indexable public page should be in it
    listed = set(locs)
    absent = [rel(f) for f in public_pages()
              if os.path.basename(f) not in NOT_CONTENT and not is_noindex(read(f))
              and url_for(rel(f)) not in listed]
    if absent:
        B("indexable page(s) missing from sitemap.xml (run refresh_sitemap.py): " + ", ".join(absent[:8]))
    # lastmod must match git (refresh_sitemap.py writes git log -1 --format=%cs)
    stale = []
    shallow = git("rev-parse", "--is-shallow-repository") == "true"
    for loc, lm in pairs:
        f = page_for_url(loc)
        if not os.path.exists(f):
            continue
        d = git("log", "-1", "--format=%cs", "--", rel(f))
        if d and d > lm.strip():
            stale.append(f"{rel(f)}: sitemap says {lm.strip()}, last changed {d}")
    if stale:
        B(f"{len(stale)} sitemap lastmod(s) older than the file's last commit - run "
          f"`python3 refresh_sitemap.py`:\n      " + "\n      ".join(stale[:8]))
    if shallow:
        N("sitemap lastmod vs git: shallow clone, dates may be approximate (use fetch-depth: 0)")
    if not (gone or dupes or noidx or absent or stale):
        K(f"sitemap: {len(locs)} URLs, all resolve, no duplicates or noindex, every indexable "
          f"page listed, every lastmod matches git")


def check_video_sitemap():
    """Measured from each page's <iframe src> only - a nearby playlist LINK is not an embed."""
    vs = os.path.join(SITE, "sitemap-video.xml")
    if not os.path.exists(vs):
        B("sitemap-video.xml is missing"); return
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9",
          "v": "http://www.google.com/schemas/sitemap-video/1.1"}
    root = ET.parse(vs).getroot()
    listed = {}
    for u in root.findall("s:url", ns):
        loc = u.find("s:loc", ns).text.strip()
        ids = set()
        for v in u.findall("v:video", ns):
            pl = (v.find("v:player_loc", ns).text or "") if v.find("v:player_loc", ns) is not None else ""
            m = re.search(r"/embed/([A-Za-z0-9_-]{11})", pl)
            if m: ids.add(m.group(1))
            for req in ("thumbnail_loc", "title", "description"):
                if v.find("v:" + req, ns) is None or not (v.find("v:" + req, ns).text or "").strip():
                    B(f"sitemap-video.xml: an entry for {loc} has no {req}")
        listed[loc] = ids
    missing, playlists, stray = [], [], []
    for f in public_pages():
        s = read(f)
        if is_noindex(s) or os.path.basename(f) in NOT_CONTENT:
            continue
        srcs = re.findall(r'<iframe\b[^>]*\bsrc="([^"]+)"', s)
        single = set()
        for src in srcs:
            if "youtube" not in src:
                continue
            m = re.search(r"/embed/([A-Za-z0-9_-]{11})(?:[?\"]|$)", src)
            if m and "list=" not in src and "videoseries" not in src:
                single.add(m.group(1))
            else:
                playlists.append(rel(f))
        u = url_for(rel(f))
        lack = single - listed.get(u, set())
        if lack:
            missing.append(f"{rel(f)}: embeds {', '.join(sorted(lack))}, not in sitemap-video.xml")
    for loc, ids in listed.items():
        f = page_for_url(loc)
        if not os.path.exists(f):
            stray.append(f"{loc}: no such page")
            continue
        s = read(f)
        for i in ids:
            if i not in s:
                stray.append(f"{loc}: lists video {i} the page does not carry")
    if missing: B("embedded video(s) missing from the video sitemap:\n      " + "\n      ".join(missing))
    if stray: B("video sitemap entr(ies) that do not match their page:\n      " + "\n      ".join(stray))
    if playlists:
        N("page(s) whose embed is a playlist, not one video (a video sitemap cannot list it - "
          "her decision, M8): " + ", ".join(sorted(set(playlists))))
    if not (missing or stray):
        K(f"video sitemap: {sum(len(v) for v in listed.values())} video(s) on {len(listed)} page(s), "
          f"every single-video <iframe> listed")


def check_og_images():
    gone = []
    for f in public_pages():
        for m in re.finditer(r'<meta (?:property|name)="(?:og:image|twitter:image)" content="([^"]+)"', read(f)):
            u = _html.unescape(m.group(1))
            if not u.startswith(HOST):
                continue
            p = os.path.join(SITE, u[len(HOST):].split("?")[0].split("#")[0])
            if not os.path.isfile(p):
                gone.append(f"{rel(f)} -> {u}")
    if gone:
        B(f"{len(gone)} og:image/twitter:image pointing at a file not in the repo:\n      "
          + "\n      ".join(sorted(set(gone))[:12]))
    else:
        K("share images: every og:image / twitter:image on this domain exists in the repo")


def check_forms():
    """Masha's rule 2026-10-13: the contact/feedback form three times on every article -
    each block found by its own marker (a count of data-opu was blind: there are four)."""
    bad, n = [], 0
    for f in live_articles() + queued_pages():
        n += 1
        s = read(f)
        lack = [m for m in FORM_MARKERS if 'data-opu="%s"' % m not in s]
        if lack:
            bad.append(f"{rel(f)}: no {', '.join(lack)}")
    if bad:
        B(f"{len(bad)} article(s) without all three form blocks (run python3 blog/_contact_blocks.py):\n      "
          + "\n      ".join(bad[:12]))
    else:
        K(f"forms: all {n} live and queued articles carry contact-top, contact-mid and contact-bottom")
    pages = []
    for f in public_pages():
        if "/blog/" in "/" + rel(f) or os.path.basename(f) in NOT_CONTENT or os.path.basename(f) == "index.html" and rel(f) != "index.html":
            continue
        s = read(f)
        if is_noindex(s):
            continue
        lack = [m for m in FORM_MARKERS if 'data-opu="%s"' % m not in s]
        if lack:
            pages.append(f"{rel(f)} (no {', '.join(lack)})")
    if pages:
        N("site page(s) without all three form blocks: " + ", ".join(pages))


def check_queue():
    q = os.path.join(SITE, "blog", "_queue")
    man = manifest()
    slugs = [e["slug"] for e in man]
    files = {os.path.basename(f)[:-5] for f in queued_pages()}
    no_file = [s for s in slugs if s not in files]
    no_entry = sorted(files - set(slugs))
    dup = sorted({s for s in slugs if slugs.count(s) > 1})
    live = {os.path.basename(f)[:-5] for f in live_articles()}
    both = sorted(set(slugs) & live)
    bad_dates = []
    ahead = []
    for e in man:
        try:
            d = datetime.date.fromisoformat(e["date"])
            if d >= TODAY: ahead.append(d)
        except Exception:
            bad_dates.append(f"{e.get('slug')}: {e.get('date')!r}")
    if no_file: B("queue manifest lists article(s) with no file: " + ", ".join(no_file[:8]))
    if no_entry: B("queued file(s) the manifest does not list (they never publish): " + ", ".join(no_entry[:8]))
    if dup: B("queue manifest lists a slug twice: " + ", ".join(dup))
    if both: B("slug(s) both live and still queued (would publish twice): " + ", ".join(both[:8]))
    if bad_dates: B("queue manifest bad date(s): " + ", ".join(bad_dates))
    noidx_q = [os.path.basename(f) for f in queued_pages()
               if '<meta name="robots" content="noindex">\n' not in read(f)]
    if noidx_q: B("queued article(s) without the exact noindex line _publish.py strips: " + ", ".join(noidx_q[:8]))
    noidx_live = [rel(f) for f in live_articles() if is_noindex(read(f))]
    if noidx_live: B("published article(s) still carrying noindex: " + ", ".join(noidx_live))
    if not ahead:
        B("the blog queue is EMPTY - nothing left to publish")
    else:
        last = max(ahead); days = (last - TODAY).days
        if days < 7:
            B(f"the blog queue runs out on {last} ({days} day(s) of cover)")
        elif days < 14:
            N(f"blog queue covered only to {last} ({days} days)")
        dates = {e["date"] for e in man}
        d = TODAY + datetime.timedelta(1); gaps = []
        while d <= last:
            if d.isoformat() not in dates: gaps.append(d.isoformat())
            d += datetime.timedelta(1)
        if gaps:
            N(f"blog queue: {len(gaps)} day(s) with no article before {last}: " + ", ".join(gaps[:8]))
    if not (no_file or no_entry or dup or both or bad_dates or noidx_q or noidx_live) and ahead:
        K(f"blog queue: {len(man)} article(s) to {max(ahead)}, manifest and files match 1:1, "
          f"noindex on every queued draft and on no published article")


def check_blog_meta():
    seen = collections.defaultdict(list); long_t = []
    for f in live_articles() + queued_pages():
        t = read(f)
        m = re.search(r"<title>(.*?)</title>", t, re.S)
        ti = _html.unescape(m.group(1).strip()) if m else ""
        if len(ti) > 60: long_t.append(f"{rel(f)} ({len(ti)})")
        d = re.search(r'name="description" content="([^"]*)"', t)
        d = _html.unescape(d.group(1)) if d else ""
        if not d: B(f"blog: {rel(f)} has no meta description")
        seen[d].append(rel(f))
    shared = [fs for d, fs in seen.items() if d and len(fs) > 1]
    for fs in shared:
        B(f"blog: {len(fs)} articles share one meta description: {', '.join(fs)}")
    if long_t:
        N("blog titles over 60 characters (cut in search): " + ", ".join(long_t))
    if not shared and not long_t:
        K("blog meta: titles within 60, every description unique")


def check_read_next():
    arts = live_articles()
    inbound = collections.Counter(); noblock = []
    for f in arts:
        t = read(f)
        m = re.search(r"<!-- read-next -->(.*?)</div>", t, re.S)
        if not m:
            if "read-next: nothing live to link yet" not in t:
                noblock.append(rel(f))
            continue
        for slug in re.findall(r'href="([a-z0-9-]+\.html)"', m.group(1)):
            inbound[slug] += 1
    for f in queued_pages():
        t = read(f)
        if "<!-- read-next -->" not in t and "read-next: nothing live to link yet" not in t:
            noblock.append(rel(f))
    orphans = [os.path.basename(f) for f in arts if inbound[os.path.basename(f)] == 0]
    if noblock: N("article(s) with no 'Read next' block (python3 blog/_related.py): " + ", ".join(noblock[:8]))
    if len(orphans) > 2: N(f"{len(orphans)} live article(s) nothing links to yet: " + ", ".join(orphans[:5]))
    if not noblock and len(orphans) <= 2:
        K(f"read-next: every live and queued article carries the block")


def check_canonicals():
    faults = []
    for f in public_pages():
        name = rel(f)
        if os.path.basename(f) in NOT_CONTENT:
            continue
        s = read(f)
        want = url_for(name)
        m = re.search(r'<link rel="canonical" href="([^"]+)"', s)
        if not m or is_noindex(s):
            continue
        if m.group(1) != want:
            faults.append(f"{name}: canonical {m.group(1)}")
        og = re.search(r'<meta property="og:url" content="([^"]+)"', s)
        if og and og.group(1) != want:
            faults.append(f"{name}: og:url {og.group(1)}")
    if faults:
        B("page(s) whose canonical or og:url names a different page:\n      " + "\n      ".join(faults[:8]))
    else:
        K("canonicals: every indexable page names itself")


def check_prices_and_strings():
    lessons = os.path.join(SITE, "lessons.html")
    if os.path.exists(lessons):
        gone = [p for p in REAL_PRICES if p not in read(lessons)]
        if gone: B(f"lessons.html is missing real price(s): {', '.join(gone)}")
        else: K("prices: all six real prices present on lessons.html")
    hits = []
    for f in public_pages() + queued_pages():
        low = read(f).lower()
        hits += [f"{rel(f)}: “{b}”" for b in FORBIDDEN if b.lower() in low]
    if hits: B("cancelled or forbidden string(s):\n      " + "\n      ".join(hits[:10]))
    else: K("no cancelled prices or retired hosts anywhere on the site")


def check_till():
    cfg = os.path.join(SITE, "js", "config.js")
    if not os.path.exists(cfg):
        B("js/config.js is missing"); return
    s = read(cfg)
    empty = re.findall(r'(PAY_[A-Z_0-9]+):\s*""', s)
    if empty:
        N(f"the cash register is still closed - {len(empty)} empty payment slot(s): {', '.join(empty)}")
    else:
        K("payment links: all slots filled")
    if "opu-engine.onrender.com" not in s:
        B("config.js no longer points at the feedback engine")


def check_images_alt():
    noalt = [rel(f) for f in public_pages() for tag in re.findall(r"<img [^>]*>", read(f)) if "alt=" not in tag]
    if noalt: N(f"{len(noalt)} <img> without alt text: " + ", ".join(sorted(set(noalt))[:8]))
    else: K("images: every <img> has alt text")


def check_brand_split():
    leaks = []
    for f in public_pages():
        name, low = rel(f), read(f).lower()
        pats = (("yelp.com", "Yelp link"), ("maps.google.com", "Google Maps link"))
        if name not in GEO_ALLOWED:
            pats += (("las vegas", "the words “Las Vegas”"),)
        for p, why in pats:
            if p in low and not (p == "las vegas" and "university of nevada, las vegas" in low):
                leaks.append(f"{name}: {why}")
    if leaks: N("Las Vegas signal outside about/privacy/terms/press (her decision is open):\n      "
                + "\n      ".join(sorted(set(leaks))[:10]))
    else: K("brand split: no Las Vegas signal outside about/privacy/terms/press")


def check_required_files():
    gone = [m for m in ("privacy.html", "terms.html", "CNAME", "robots.txt",
                        "googleed832eccb886831b.html", "sitemap.xml", "sitemap-video.xml",
                        "sitemap-images.xml", "blog/_queue/manifest.json") if not os.path.exists(os.path.join(SITE, m))]
    key = [p for p in glob.glob(os.path.join(SITE, "*.txt")) if re.fullmatch(r"[0-9a-f]{32}", os.path.basename(p)[:-4])]
    if not key: gone.append("IndexNow key file <32 hex>.txt")
    if gone: B("required file(s) missing from the repo: " + ", ".join(gone))
    else: K("required files: privacy, terms, CNAME, robots, Search Console + IndexNow keys, all three sitemaps")
    cname = os.path.join(SITE, "CNAME")
    if os.path.exists(cname) and read(cname).strip() != "onlinepianouniversity.com":
        B(f"CNAME is {read(cname).strip()!r}, not onlinepianouniversity.com - the domain would break")


def check_xml_files():
    bad = []
    for f in sorted(glob.glob(os.path.join(SITE, "*.xml"))):
        try: ET.parse(f)
        except ET.ParseError as e: bad.append(f"{rel(f)}: {e}")
    if bad: B("XML file(s) that do not parse: " + "; ".join(bad))
    else: K("XML: every sitemap parses")


def check_american_spelling():
    faults = []
    for f in public_pages() + queued_pages():
        text = read(f)
        for rx, fix in BRITISH.items():
            for m in re.finditer(rx, text, flags=re.IGNORECASE):
                faults.append((rel(f), text.count("\n", 0, m.start()) + 1, m.group(0), fix))
        for m in BRITISH_SUFFIX.finditer(text):
            w = m.group(0)
            if w.lower() in ALLOW_ISE or any(x[0] == rel(f) and x[2].lower() == w.lower() for x in faults):
                continue
            faults.append((rel(f), text.count("\n", 0, m.start()) + 1, w,
                           w.lower().replace("ise", "ize").replace("yse", "yze")))
    if faults:
        B(f"{len(faults)} British spelling(s):\n      " + "\n      ".join(
            f"{p}:{ln} - “{w}” -> {fx}" for p, ln, w, fx in faults[:12]))
    else:
        K("spelling: American throughout - site, blog and queue")


def check_english_only():
    cyr = re.compile(r"[Ѐ-ӿ]")
    faults = []
    for f in public_pages() + queued_pages():
        t = read(f); m = cyr.search(t)
        if m:
            faults.append(f"{rel(f)}:{t.count(chr(10), 0, m.start()) + 1}")
    if faults: B(f"{len(faults)} page(s) contain Cyrillic - everything public is English: " + ", ".join(faults[:8]))
    else: K("language: English throughout, no Cyrillic")


def check_audience():
    off = re.compile(r"\b(your child|their child|a child's|your son|your daughter|"
                     r"your kid|your teacher will|ask your teacher|find a teacher)\b", re.I)
    faults = [f"{rel(f)} ({len(off.findall(read(f)))})" for f in live_articles() + queued_pages()
              if len(off.findall(read(f))) >= 3]
    if faults: B("article(s) written for a parent/child/someone with a teacher: " + ", ".join(faults[:6]))
    else: K("audience: every article addresses an adult learning alone")


def check_press_stamp():
    gen = os.path.join(SITE, "make_press_page.py")
    if not os.path.exists(gen):
        return
    m = re.search(r'LINKS_VERIFIED\s*=\s*"(\d{4}-\d{2}-\d{2})"', read(gen))
    if not m:
        N("press page: no LINKS_VERIFIED stamp in make_press_page.py"); return
    age = (TODAY - datetime.date.fromisoformat(m.group(1))).days
    if age > 30:
        N(f"press page links last opened {m.group(1)} ({age} days ago) - re-open them and bump LINKS_VERIFIED")
    else:
        K(f"press links: opened and read {m.group(1)} ({age} days ago)")


def check_robots():
    p = os.path.join(SITE, "robots.txt")
    if not os.path.exists(p):
        return
    t = read(p)
    lack = [d for d in ("/blog/_queue/", "/_health/") if f"Disallow: {d}" not in t]
    sm = [s for s in ("sitemap.xml", "sitemap-video.xml", "sitemap-images.xml") if s not in t]
    if re.search(r"^Disallow:\s*/\s*$", t, re.M):
        B("robots.txt disallows the whole site")
    if lack: N("robots.txt does not disallow: " + ", ".join(lack))
    if sm: N("robots.txt does not list: " + ", ".join(sm))
    if not lack and not sm: K("robots.txt: queue and _health disallowed, all three sitemaps listed")


CHECKS = [check_required_files, check_xml_files, check_internal_links, check_youtube_ids,
          check_metadata, check_meta_raw_ampersand, check_meta_lengths, check_jsonld,
          check_future_dates, check_sitemap, check_video_sitemap, check_og_images, check_forms,
          check_queue, check_blog_meta, check_read_next, check_canonicals,
          check_prices_and_strings, check_till, check_images_alt, check_brand_split,
          check_american_spelling, check_english_only, check_audience, check_press_stamp,
          check_robots]


def main(argv=None):
    global SITE
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    help="the opu-website checkout to check (default: this file's repo)")
    a = ap.parse_args(argv)
    SITE = os.path.abspath(a.repo)
    print(f"OPU SITE CHECK - {TODAY} - {SITE}")
    head = git("log", "-1", "--format=%h %cs %s")
    if head: print(f"at {head}")
    print()
    for c in CHECKS:
        try:
            c()
        except Exception as e:
            B(f"[{c.__name__}] the check itself failed: {type(e).__name__}: {e}\n      "
              + traceback.format_exc().strip().splitlines()[-2].strip()[:150])
    for title, rows, mark in (("BROKEN - fix today", broken, "x"), ("NOTICE - known, decision pending", notice, "!"),
                              ("OK", ok, "+")):
        if rows:
            print(title)
            for m in rows: print(f"  {mark} {m}")
            print()
    print(f"{len(broken)} broken - {len(notice)} notice - {len(ok)} ok")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
