#!/usr/bin/env python3
"""Rewrites the 'Latest from the blog' block on index.html from the six newest cards
in blog/index.html. Run by blog/_publish.py after each publish; safe to run any time."""
import re, pathlib, html
ROOT = pathlib.Path(__file__).resolve().parent.parent
blog = (ROOT / "blog" / "index.html").read_text(encoding="utf-8")
cards = re.findall(
    r'<a class="card" href="([a-z0-9-]+\.html)"[^>]*>\s*<p class="eyebrow"[^>]*>([^<]+)</p>\s*'
    r'<h3[^>]*>(.*?)</h3>\s*<p[^>]*>(.*?)</p>', blog, flags=re.S)[:6]
if len(cards) < 3:
    raise SystemExit("could not parse blog cards")
def short(t, n=150):
    t = re.sub(r"<[^>]+>", "", t).replace("&mdash;", "—").strip()
    return t if len(t) <= n else t[:n].rsplit(" ", 1)[0] + "…"
rows = []
for href, date, title, desc in cards:
    rows.append(
        '      <a href="blog/%s"><div class="card"><p class="muted" style="margin:0 0 6px;font-size:.85rem">%s</p>'
        '<h3 style="margin:0 0 8px;font-size:1.02rem;line-height:1.35">%s</h3>'
        '<p class="muted" style="margin:0;font-size:.92rem">%s</p></div></a>\n'
        % (href, date.strip(), title.strip(), short(desc)))
p = ROOT / "index.html"
s = p.read_text(encoding="utf-8")
pat = re.compile(r'(<div class="grid cols-3" style="margin-top:22px;text-align:left">\n)(.*?)(    </div>\n    <p style="margin-top:16px"><a href="blog/index\.html">)', re.S)
if not pat.search(s):
    raise SystemExit("home blog block not found")
s2 = pat.sub(lambda m: m.group(1) + "".join(rows) + m.group(3), s, count=1)
if s2 != s:
    p.write_text(s2, encoding="utf-8")
    print("home blog block refreshed:", [c[0] for c in cards])
