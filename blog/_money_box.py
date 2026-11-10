# -*- coding: utf-8 -*-
"""The 'Keep going' money-link box that closes every blog post (marker <!--opu-money-->).

apply(html, slug, title) inserts it just before the Read-next block (or the author card, or
</article>) and is idempotent: an existing box is replaced, so rerunning never duplicates it.
_make_post.py calls it, so every future post gets it automatically.
"""
import re

START, END = "<!--opu-money-->", "<!--/opu-money-->"

# first matching rule wins; order is Masha's keyword list
RULES = [
    (r"pedal", "piano-pedals", "Piano pedals, chosen by a concert pianist"),
    (r"bench|posture|\bsit\b|\bsitting\b|elbow", "piano-benches-and-stands", "Piano benches and stands"),
    (r"record|video|\bfilm", "record-yourself-playing", "Gear to record yourself playing"),
    (r"headphone|practice at night|practice-at-night", "headphones-for-piano", "Headphones for piano practice"),
    (r"\bbooks?\b|alfred|sheet.music|method", "piano-books-and-sheet-music", "Piano books and sheet music"),
    (r"metronome|practic", "practice-tools", "Practice tools"),
    (r"keyboard|digital.piano|\bkeys\b", "digital-pianos", "Digital pianos for learning"),
]
DEFAULT = ("index", "Shop: gear a concert pianist recommends")


def pick(slug, title):
    s = (slug.replace("-", " ") + " " + title).lower()
    for pat, page, label in RULES:
        if re.search(pat, s):
            return page, label
    return DEFAULT


def box(slug, title):
    page, label = pick(slug, title)
    return (
        START + "\n"
        '<aside class="opu-money" aria-label="Keep going">\n'
        '  <p class="eyebrow">Keep going</p>\n'
        '  <p class="opu-money-lead"><a href="../gift-certificate.html">Give the gift of music: online piano lessons with Dr. Maria Pisarenko</a><br>'
        'Lesson prices increase January 1, 2027 &mdash; buy by December 31 to keep 2026 prices.</p>\n'
        '  <ul>\n'
        '    <li><a href="../shop/%s.html">%s</a></li>\n'
        '    <li><a href="../lessons.html">Private online lessons</a></li>\n'
        '  </ul>\n'
        '</aside>\n' % (page, label) + END + "\n")


ANCHORS = ("<!-- read-next -->", "<!-- read-next: nothing live",
           '<aside class="card" style="display:flex;gap:16px;align-items:center;margin:34px 0 0;padding:18px 20px">',
           "    </article>", "</article>")


def apply(t, slug, title):
    t = re.sub(re.escape(START) + r".*?" + re.escape(END) + r"\n?", "", t, flags=re.S)
    b = box(slug, title)
    for a in ANCHORS:
        if a in t:
            return t.replace(a, b + "\n" + a, 1) if not a.startswith("    ") else t.replace(a, b + "\n" + a, 1)
    raise ValueError("no anchor for money box in " + slug)
