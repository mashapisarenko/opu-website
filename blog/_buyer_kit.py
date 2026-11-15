# -*- coding: utf-8 -*-
"""Helpers for the buyer-intent article batch (2026-11-14). Renders quick-picks box, per-pick blocks,
spec tables, trust block and the closing links in one house style. Product facts live in _buyer_products.py
and come only from products.json (verified listings) and manufacturer spec pages opened on 2026-11-14."""
import html
from _buyer_products import P

TAG = "musicalgalaxi-20"
L1 = "https://youtu.be/AzU01rYWHK8"
UPDATED = "November 14, 2026"
BTN = ('style="display:inline-block;padding:9px 18px;margin:6px 0;background:#7a1f3d;color:#fff;border-radius:8px;'
       'font-weight:600;text-decoration:none;font-size:.95rem"')
TH = 'style="text-align:left;padding:8px 10px;border-bottom:2px solid #7a1f3d"'
TD = 'style="padding:8px 10px;border-bottom:1px solid #ddd;vertical-align:top"'
DISC = ('<p><em>As an Amazon Associate I earn from qualifying purchases. That never changes what I recommend: every item here '
        'is something I would tell my own adult students to look at. Check today&#39;s price on Amazon.</em></p>')


def url(asin): return "https://www.amazon.com/dp/%s?tag=%s" % (asin, TAG)
def A(asin, text): return '<a href="%s" rel="sponsored nofollow noopener" target="_blank">%s</a>' % (url(asin), text)
def esc(s): return s  # bodies are written with entities already


def meta_line():
    return ('<p style="margin:0 0 14px;font-size:.92rem;color:#5b6478"><strong>By Dr. Maria Pisarenko, DMA</strong> &middot; '
            'Last updated: %s &middot; Product details checked against the Amazon listing and the maker&#39;s page on that date.</p>' % UPDATED)


def quick(rows, title="Quick picks"):
    """rows: [(label, key, one_line)]"""
    li = "".join('<li style="margin:0 0 8px"><strong>%s:</strong> %s &mdash; %s</li>' % (lab, A(P[k]["a"], P[k]["n"]), line)
                 for lab, k, line in rows)
    return ('<div class="card" style="margin:22px 0;padding:20px 22px;border-left:4px solid #7a1f3d">'
            '<p style="margin:0 0 8px;font-size:.8rem;letter-spacing:.06em;text-transform:uppercase">%s</p>'
            '<ul style="margin:0;padding-left:20px">%s</ul></div>' % (title, li))


def how_i_choose(text):
    return ('<h2>How I choose</h2><p>%s I have not played every instrument or used every device in this guide, and I do not say that I have. '
            'What I give you is what I look for as a concert pianist who teaches adults, checked against what each Amazon listing '
            'and manufacturer page actually states.</p>' % text)


def pick(k, take, who=None, buy=None, skip=None, heading=None):
    p = P[k]
    pros = "".join("<li>%s</li>" % x for x in p["pro"])
    cons = "".join("<li>%s</li>" % x for x in p["con"])
    return ('<h3>%s</h3><p><strong>Who it is for:</strong> %s</p><p><strong>What the listing says:</strong> %s</p>'
            '<p><strong>What I look for:</strong> %s</p><p>%s</p>'
            '<div style="display:flex;gap:28px;flex-wrap:wrap"><div><strong>Pros</strong><ul style="margin:4px 0 0">%s</ul></div>'
            '<div><strong>Cons</strong><ul style="margin:4px 0 0">%s</ul></div></div>'
            '<p><strong>Buy it if</strong> %s <strong>Skip it if</strong> %s</p>'
            '<p><a href="%s" rel="sponsored nofollow noopener" target="_blank" %s>See it on Amazon &rarr;</a></p>'
            % (heading or A(p["a"], p["n"]), who or p["who"], p["f"], p["look"], take, pros, cons,
               buy or p["buy"], skip or p["skip"], url(p["a"]), BTN))


def table(headers, rows, first="Model"):
    th = "".join("<th %s>%s</th>" % (TH, h) for h in [first] + headers)
    tr = "".join("<tr>" + "".join("<td %s>%s</td>" % (TD, c) for c in r) + "</tr>" for r in rows)
    return ('<div style="overflow-x:auto;margin:18px 0"><table style="border-collapse:collapse;width:100%%;font-size:.95rem">'
            '<thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (th, tr))


def trows(keys, cols):
    """cols: list of dict keys in P[k]['t'] ; returns rows with linked names"""
    return [[A(P[k]["a"], P[k]["n"])] + [P[k]["t"].get(c, "Not stated on the listing") for c in cols] for k in keys]


def trust(what="gear"):
    return ('<h2>Why trust this guide</h2><p>I am Dr. Maria Pisarenko: a concert pianist with a Doctor of Musical Arts degree, trained in Moscow and now a university '
            'piano teacher. I teach adults who learn on their own, so I know what a student&#39;s hands and ears need from %s, and what is only decoration. '
            'I earn a commission when you buy through my links; I never take money to change a recommendation, and I list only products I have verified on Amazon.</p>' % what)


SHOPS = {
 "pianos": ('digital-pianos', 'portable digital pianos'), "home": ('home-digital-pianos', 'home digital pianos'),
}

def closing(shop_links, extra=""):
    """shop_links: [(slug,label)] -> closing paragraph with free course and gift certificate"""
    s = ", ".join('<a href="../shop/%s.html">%s</a>' % x for x in shop_links)
    return ('<h2>Where to go next</h2><p>The full lists are in my shop: %s. %s</p>'
            '<p>The piano is only half the plan. My <a href="../free-course.html">free 41-lesson course</a> is published in full, and when you have a recording, '
            '<a href="../submit.html">send it to me</a> and I will tell you what I hear, at no charge. If you are buying for someone else, '
            'a <a href="../gift-certificate.html">gift certificate for online piano lessons</a> is a gift that needs no assembly.</p>' % (s, extra))


def spec(slug, date, title, seo, desc, sub, body, faq):
    return {"slug": slug, "date": date, "title": title, "seo_title": seo, "description": desc, "sub": sub,
            "image": "lead-at-the-piano.jpg", "image_alt": "Dr. Maria Pisarenko at the piano",
            "cta_text": "Forty-one lessons in order, free, at your own pace:", "cta_href": L1,
            "cta_link": "Start at Lesson 1 &rarr;", "body": body, "faq": faq}
