# -*- coding: utf-8 -*-
"""Buyer articles link to their most relevant shop pages near the top AND at the end.

Written 2026-11-14 (conversion audit). Markers: <!--opu-shoptop--> ... <!--/opu-shoptop--> after the first
paragraph of the article; the shop line of the closing 'Keep going' box (<!--opu-money-->) is replaced by the
same pages. A 'buyer article' is one that appears in _shop_map.json (written by make_shop_pages.py from the
shop's own article lists) or that already links to two different shop pages (or three times) in its body.
The pages are ranked by how often and how early the article itself links to them, so the top link is the
page the article is really about. Idempotent: rerunning replaces, never duplicates.

Run:  python3 blog/_shop_links.py   (from opu-website/; make_shop_pages.py does this automatically)
_make_post.py calls apply() for every new post, so future articles get it for free.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
MAPF = HERE / "_shop_map.json"
TOP_S, TOP_E = "<!--opu-shoptop-->", "<!--/opu-shoptop-->"
MONEY_S, MONEY_E = "<!--opu-money-->", "<!--/opu-money-->"
HREF = re.compile(r'href="\.\./shop/([a-z0-9-]+)\.html"')
FALLBACK = {"digital-pianos": "Digital pianos for adult learners", "pianos": "Pianos", "index": "The shop"}


def load_map():
    if MAPF.exists():
        return json.loads(MAPF.read_text(encoding="utf-8"))
    return {"labels": {}, "inverse": {}}


def _body(t):
    """Article body with our own boxes and the contact blocks stripped, so only editorial links are counted."""
    a = t.find('<article')
    b = t.rfind('</article>')
    body = t[a:b] if a != -1 and b != -1 else t
    body = re.sub(re.escape(TOP_S) + r".*?" + re.escape(TOP_E), "", body, flags=re.S)
    body = re.sub(re.escape(MONEY_S) + r".*?" + re.escape(MONEY_E), "", body, flags=re.S)
    return body


def pages_for(t, slug, m=None):
    """Ordered shop pages for an article, or [] when it is not a buyer article."""
    m = m or load_map()
    body = _body(t)
    found = {}
    for k in HREF.finditer(body):
        s = k.group(1)
        if s == "index":
            continue
        n, first = found.get(s, (0, k.start()))
        found[s] = (n + 1, first)
    inv = [p for p in m.get("inverse", {}).get(slug, []) if p != "index"]
    buyer = bool(inv) or len(found) >= 2 or sum(n for n, _ in found.values()) >= 3
    if not buyer:
        return []
    ranked = [s for s, _ in sorted(found.items(), key=lambda kv: (-kv[1][0], kv[1][1]))]
    out = ranked[:]
    for p in inv:
        if p not in out:
            out.append(p)
    labels = m.get("labels", {})
    return [p for p in out if p in labels][:2]


def _link(p, labels):
    return '<a href="../shop/%s.html">%s</a>' % (p, labels[p])


def apply(t, slug, m=None):
    m = m or load_map()
    labels = m.get("labels", {})
    pages = pages_for(t, slug, m)
    t = re.sub(r"\n*" + re.escape(TOP_S) + r".*?" + re.escape(TOP_E) + r"\n*", "\n\n", t, flags=re.S)
    if not pages:
        return t
    # top: after the first paragraph of the article
    box = (TOP_S + '\n<aside class="opu-shoptop" aria-label="Shop picks for this topic"><p><strong>Shopping for this?</strong> '
           'My picks, chosen by a concert pianist: ' + " and ".join(_link(p, labels) for p in pages) + '.</p></aside>\n' + TOP_E + "\n")
    a = t.find('<article')
    if a != -1:
        e = t.find("</p>", a)
        if e != -1:
            e += len("</p>")
            t = t[:e] + "\n\n" + box + t[e:]
    # end: put the computed shop pages (marked data-auto) at the top of the closing box's list. Hand-written
    # shop links already in the list are KEPT (2026-11-14 fix: the first version replaced them), except one that
    # duplicates a computed page. Idempotent: earlier auto items are removed and rebuilt each run.
    i, j = t.find(MONEY_S), t.find(MONEY_E)
    if i != -1 and j != -1:
        blk = t[i:j]
        m = re.search(r'<ul>\n', blk)
        if m:
            pos = m.end()
            head, rest = blk[:pos], blk[pos:]
            def _drop(mm):
                if 'data-auto="1"' in mm.group(0):
                    return ""
                return "" if mm.group(1) in pages else mm.group(0)
            rest = re.sub(r'[ ]*<li[^>]*><a href="\.\./shop/([a-z0-9-]+)\.html">[^<]*</a></li>[ ]*\n?', _drop, rest)
            new = "".join('    <li data-auto="1"><a href="../shop/%s.html">%s</a></li>\n' % (p, labels[p]) for p in pages)
            t = t[:i] + head + new + rest + t[j:]
    return t


def main():
    m = load_map()
    n_changed = n_buyer = 0
    files = sorted(HERE.glob("*.html")) + sorted((HERE / "_queue").glob("*.html"))
    for f in files:
        if f.name == "index.html":
            continue
        t = f.read_text(encoding="utf-8")
        t2 = apply(t, f.stem, m)
        if TOP_S in t2:
            n_buyer += 1
        if t2 != t:
            f.write_text(t2, encoding="utf-8")
            n_changed += 1
    print("shop links: %d buyer articles, %d files changed" % (n_buyer, n_changed))


if __name__ == "__main__":
    main()
