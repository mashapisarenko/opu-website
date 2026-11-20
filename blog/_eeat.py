# -*- coding: utf-8 -*-
"""E-E-A-T layer (2026-11-20): the 'Recommended by Dr. Maria Pisarenko' box and her Person JSON-LD.

Used by the shop generator (make_shop_pages.page) and by blog/_shop_links.apply, so every shop page and every
buyer/gear article, live or queued, gets the same box. Every credential line below is already published on
about.html / press.html; nothing new is claimed. No Review or AggregateRating schema, ever.
Markers make it idempotent: <!--opu-eeat--> ... <!--/opu-eeat-->.
"""
import json, re

SITE = "https://onlinepianouniversity.com"
S, E = "<!--opu-eeat-->", "<!--/opu-eeat-->"
SAME = ["https://www.mariapisarenko.com", "https://www.linkedin.com/in/mariapisarenko/",
        "https://www.youtube.com/@ONLINEPIANOUNIVERSITY", "https://www.facebook.com/OnlinePianoUniversity",
        "https://www.instagram.com/online_piano_university/", "https://www.tiktok.com/@online.piano.university",
        "https://www.pinterest.com/OnlinePianoUniversity/"]
PERSON = {"@type": "Person", "name": "Dr. Maria Pisarenko", "honorificSuffix": "DMA",
          "jobTitle": "Concert Pianist and Piano Teacher", "url": SITE + "/about.html", "sameAs": SAME}

BOX = (S + '<aside class="opu-eeat" aria-label="Who recommends these picks" style="display:flex;gap:14px;align-items:center;'
       'margin:18px 0;padding:14px 16px;border:1px solid #e4dfd2;border-left:4px solid #b8923a;border-radius:12px;background:#fffdf8">'
       '<img src="../images/blog/dr-maria-pisarenko-piano-teacher-author.jpg" alt="Dr. Maria Pisarenko, concert pianist and piano teacher" '
       'width="56" height="56" loading="lazy" decoding="async" style="width:56px;height:56px;border-radius:50%;object-fit:cover;flex:0 0 56px">'
       '<div style="font-size:.93rem;line-height:1.45"><p style="margin:0 0 3px"><strong>Recommended by Dr. Maria Pisarenko, DMA</strong> '
       '&mdash; concert pianist and piano teacher</p>'
       '<p style="margin:0 0 3px;color:#3d4557">Doctor of Musical Arts in piano performance; trained at the Central Music School of the Moscow '
       'Tchaikovsky Conservatory and the Gnessin Academy; international competition prizewinner (Paris, Rome) and Steinway Top Teacher.</p>'
       '<p style="margin:0"><a href="../about.html">About Dr. Pisarenko</a> &middot; <a href="../press.html">Press and awards</a></p></div></aside>' + E)

_RE = re.compile(r"\n*" + re.escape(S) + r".*?" + re.escape(E) + r"\n*", re.S)


def strip(t):
    return _RE.sub("\n\n", t)


def apply(t, anchor_end="<!--/opu-shoptop-->"):
    """Insert the box right after the shop-top box of a buyer article (idempotent)."""
    t = strip(t)
    i = t.find(anchor_end)
    if i == -1:
        return t
    i += len(anchor_end)
    return t[:i] + "\n" + BOX + "\n" + t[i:]


def blogposting(t):
    """Give the BlogPosting JSON-LD the full Person as author and reviewedBy (idempotent)."""
    def fix(m):
        try:
            d = json.loads(m.group(2))
        except ValueError:
            return m.group(0)
        if d.get("@type") != "BlogPosting":
            return m.group(0)
        d["author"] = dict(PERSON)
        d["reviewedBy"] = dict(PERSON)
        return m.group(1) + json.dumps(d, indent=2, ensure_ascii=False).replace("</", "<\\/") + m.group(3)
    return re.sub(r'(<script type="application/ld\+json">\n?)(.*?)(\n?</script>)', fix, t, flags=re.S)
