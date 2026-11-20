#!/usr/bin/env python3
"""Striking-distance SEO patch for LIVE blog articles (2026-11-20). Idempotent (markers).
Sets query-first title/description (head, og, twitter, JSON-LD), adds a Quick answer box, extra FAQs
(visible + FAQPage JSON-LD), a gift+lessons pairing box on the senior/retiree articles, and inline links
from related live articles. Run from blog/:  python3 _striking_patch.py"""
import re, json, html, pathlib, sys
HERE = pathlib.Path(__file__).parent
M = "<!--opu-striking-->"
def e(s): return html.escape(s, quote=False)
def a(s): return html.escape(s, quote=True)
def jstr(s): return json.dumps(s, ensure_ascii=False)[1:-1]

PAIR = ('<aside class="card" style="margin:26px 0;padding:18px 20px"><h2 style="margin:0 0 6px;font-size:1.25rem">Pair the gear with lessons</h2>'
        '<p style="margin:0 0 10px">The equipment makes practice comfortable. Lessons make it go somewhere. I teach adults of every age online, and a '
        '<a href="../gift-certificate.html">gift certificate for online piano lessons</a> can go to a parent, a grandparent or yourself, '
        'with the first lesson planned around the keyboard they already own.</p>'
        '<p style="margin:0"><a class="btn" href="../gift-certificate.html">Give online piano lessons &rarr;</a> '
        '<a href="../free-course.html">or start the free 41-lesson course</a></p></aside>')

ART = {
 "best-sustain-pedal-for-digital-piano": dict(
  title="Best Sustain Pedal for Digital Piano: FC4A or DP-10?",
  desc="Best sustain pedal for a digital piano, from a concert pianist: Yamaha FC4A or Roland DP-10, half-pedal, polarity and what suits your keyboard.",
  quick="The best sustain pedal for a digital piano is a piano-style pedal your keyboard supports: the Yamaha FC4A for Yamaha, the Roland DP-10 for Roland, or a pedal your manual names. You do not need to spend anywhere near $500; these pedals sit among the cheapest upgrades you can make, and my <a href=\"../shop/piano-pedals.html\">sustain pedal picks, budget to pro</a> are on the shop page.",
  faqs=[("What is the best sustain pedal under $500?", "You will not need to spend that much. A piano-style pedal made for your brand is the best choice, and the pedals I list sit far below that figure. Check today's price on Amazon."),
        ("Can I use a Yamaha pedal on a Roland piano?", "Sometimes, but connectors and polarity differ, and half-pedaling may not work. Use the pedal your manual names, or one described as compatible with your model."),
        ("Why does my sustain pedal work backwards?", "The polarity usually does not match. Switch the keyboard off, plug the pedal in with your foot off it, then switch the keyboard on again, or use the pedal's polarity switch if it has one.")]),
 "gifts-for-piano-teachers": dict(
  title="Gifts for Piano Teachers They Will Actually Use (2026)",
  desc="Gifts for piano teachers from a piano professor: music lights, metronomes, scores and thank-you notes teachers use, plus lessons as a gift.",
  quick="The best gifts for piano teachers are small, useful and personal: a music stand light, a good metronome, a score or book, or a music-themed accessory, with a handwritten note about what you have learned. A recording of your own playing is the gift almost every teacher keeps. For more ideas, see my <a href=\"../shop/gifts-for-piano-teachers.html\">piano teacher gifts shop page</a>.",
  faqs=[("What do piano teachers really want as a gift?", "Something that makes teaching easier, or something that shows you practiced: a stand light, a metronome, a book, or a note and a recording of your progress."),
        ("What should an adult student give their piano teacher?", "A thoughtful book or a small music accessory, and a note naming one piece you can now play. Adults are often surprised how much that note means."),
        ("Can I give lessons as a gift to a friend who plays or wants to start?", "Yes. A <a href=\"../gift-certificate.html\">gift certificate for online piano lessons</a> works at any adult level.")]),
 "gifts-for-seniors-learning-piano": dict(
  title="Piano Equipment for Seniors: Gifts That Help Them Play",
  desc="Piano equipment for seniors and grandparents from a concert pianist: light digital pianos, bench, headphones, lamp, plus lessons as the best gift.",
  quick="Piano equipment for seniors and grandparents comes down to five things: a digital piano with a comfortable touch, an adjustable bench, headphones, a good light on the page and a beginner book written for adults. The best gift pairs that gear with lessons, so I link a <a href=\"../gift-certificate.html\">gift certificate for online piano lessons</a> beside the equipment.",
  faqs=[("What piano equipment does a senior beginner need?", "A digital piano or keyboard with full-size keys, an adjustable bench, headphones for comfortable practice and a light on the music. A book written for adults completes it."),
        ("What is a good piano gift for a grandparent?", "A keyboard they can play at their own pace, a bench that fits them and lessons. The gear is the invitation and the lessons are what gets them playing."),
        ("Can I give a grandparent piano lessons as a gift?", "Yes. A <a href=\"../gift-certificate.html\">gift certificate for online lessons</a> works wherever they live, and I plan the first lesson around the instrument they own.")],
  pair=True),
 "piano-for-seniors-keyboard-light-music": dict(
  title="Piano Equipment for Retirees: Keyboard, Bench and Light",
  desc="Piano equipment for retirees and seniors from a concert pianist: the right keyboard touch, a bench, good light and music to enjoy from week one.",
  quick="Piano equipment for retirees means a keyboard with a comfortable touch, an adjustable bench, good light on the page and music you enjoy playing from week one. Set the room up first and practice stays easy. Lessons are the finishing touch: see my <a href=\"../gift-certificate.html\">gift certificate for online piano lessons</a>.",
  faqs=[("What piano equipment do retirees need?", "A keyboard with full-size keys, an adjustable bench, a light that falls evenly on the page and a stand at eye level. Headphones help you practice any hour."),
        ("What keyboard suits an older beginner?", "One with full-size keys and an even touch you find comfortable. Try a few if you can; if your hands tire, shorten the session rather than force it."),
        ("How should I light the music?", "Evenly across the whole page, without glare on a glossy cover, with the light coming from the side so your hand does not cast a shadow.")],
  pair=True),
 "learning-piano-in-retirement": dict(
  title="Piano Tips for Retirees: Equipment and Daily Routine",
  desc="Piano tips for retirees from a concert pianist: set up the room, the equipment you need and a daily practice routine for your first year.",
  quick="The best piano tips for retirees start before the first note: set up the bench, the light and the music stand, then practice a short, regular session every day. Equipment for retirees is simple: a keyboard with a comfortable touch, a bench and a light. Pair it with lessons if you want a teacher beside you.",
  faqs=[("What piano equipment do retirees need?", "A keyboard or digital piano, an adjustable bench, a light for the page and a music stand. Headphones help you practice whenever you like."),
        ("How long should a retiree practice each day?", "Start with 15 to 20 minutes and add time as it feels good. Short, regular sessions help you more than one long one."),
        ("Is retirement a good time to start piano?", "Yes. You have time to practice calmly, and an adult learns on purpose. The free course is made for exactly that.")],
  pair=True),
}

# inline links from other LIVE articles (target page, anchor text, sentence before, sentence after)
SHOP = "../shop/"
LINKS = {
 "best-digital-piano-for-adult-beginners": [("piano-pedals", "sustain pedal for a digital piano", "Once the piano is chosen, a proper ", " is the first thing to add, and it costs far less than the piano.")],
 "best-digital-piano-under-500": [("piano-pedals", "sustain pedal for a digital piano", "If the piano came with a switch-type pedal, a ", " is the cheapest improvement you can make.")],
 "yamaha-p145-vs-p225": [("piano-pedals", "best sustain pedal for a digital piano", "Whichever you choose, see my picks for the ", ", including the pedals each maker sells.")],
 "roland-fp30x-vs-yamaha-p225": [("piano-pedals", "sustain pedal for a digital piano", "Plan for a piano-style ", " from the start; both of these pianos take one.")],
 "piano-bench-height-posture": [("piano-benches-and-stands", "adjustable piano bench", "If your bench does not fit, an ", " solves it permanently."), ("music-stands", "music stand for piano practice", " To keep the page at eye level, add a ", ".")],
 "learning-piano-without-a-teacher": [("music-stands", "music stand", "Put your book on a steady ", " at eye level so your neck stays free.")],
 "gifts-for-adult-piano-beginners": [("music-stands", "best music stands for piano practice", "For a reading corner, see my picks of the ", ".")],
 "how-to-read-sheet-music-treble-clef-rhythm": [("music-stands", "music stand for home practice", "A steady ", " helps your eyes find the page without hunting.")],
 "best-keyboard-for-beginners": [("piano-accessories", "piano accessories", "Beyond the keyboard itself, see my short list of ", " you actually need.")],
 "61-vs-76-vs-88-keys": [("piano-accessories", "piano accessories for a digital piano", "Whichever size you pick, here are the ", " I suggest first.")],
 "best-headphones-for-digital-piano": [("piano-accessories", "pianist accessories", "Headphones are one of the six ", " I recommend first.")],
 "best-gifts-for-piano-players-2026": [("piano-accessories", "piano accessories", "For small gifts, browse my list of ", " a pianist uses every day.")],
 "piano-wrist-position-adults": [("piano-benches-and-stands", "adjustable piano bench", "Seat height decides your wrist position, so an ", " is worth the money.")],
 "does-piano-playing-hurt-hands": [("piano-benches-and-stands", "adjustable piano bench", "A comfortable ", " lets your arms hang naturally and takes strain off your hands.")],
 "how-to-choose-a-piano-teacher": [("gifts-for-piano-teachers", "gifts for piano teachers", "When you have found one, here are ideas for ", " that they will use.")],
 "christmas-gifts-for-musicians": [("gifts-for-piano-teachers", "gifts for piano teachers", "Giving to a teacher? See my guide to ", ".")],
 "stocking-stuffers-for-piano-players": [("gifts-for-piano-teachers", "gifts for piano teachers", "Small gifts also suit a teacher; see my ideas for ", ".")],
 "piano-and-the-aging-brain": [("gifts-for-seniors-learning-piano", "piano equipment for seniors", "To set up comfortably, see my guide to ", " and what to pair it with.")],
 "empty-nest-hobby-piano": [("piano-for-seniors-keyboard-light-music", "piano equipment for retirees", "If you are setting up a keyboard now, see my guide to ", ".")],
}
def resolve(t):
    return SHOP + t + ".html" if t in ("piano-pedals","piano-benches-and-stands","music-stands","piano-accessories") or t == "gifts-for-piano-teachers-SHOP" else t + ".html"

def patch_meta(t, A):
    st = A["title"]; ds = A["desc"]
    assert len(st) <= 60 and 70 <= len(ds) <= 160, (len(st), len(ds))
    old = re.search(r"<title>(.*?)</title>", t, re.S).group(1)
    t = re.sub(r"<title>.*?</title>", lambda m: "<title>%s</title>" % e(st), t, 1, flags=re.S)
    for n in ("og:title", "twitter:title"):
        t = re.sub(r'(<meta (?:property|name)="%s" content=")[^"]*(")' % n, lambda m: m.group(1) + a(st) + m.group(2), t, 1)
    for n in ("description", "og:description", "twitter:description"):
        t = re.sub(r'(<meta (?:property|name)="%s" content=")[^"]*(")' % n, lambda m: m.group(1) + a(ds) + m.group(2), t, 1)
    t = re.sub(r'(<h1[^>]*>)[^<]*(</h1>)', lambda m: m.group(1) + e(st) + m.group(2), t, 1)
    t = re.sub(r'("@type": "BlogPosting",\s*"headline": )"(?:[^"\\]|\\.)*"(,\s*"description": )"(?:[^"\\]|\\.)*"',
               lambda m: m.group(1) + '"' + jstr(st) + '"' + m.group(2) + '"' + jstr(ds) + '"', t, 1)
    # breadcrumb: last ListItem name equals the old title
    t = re.sub(r'("position": 3,\s*"name": )"(?:[^"\\]|\\.)*"', lambda m: m.group(1) + '"' + jstr(st) + '"', t, 1)
    return t

def patch_faq(t, extra):
    m = re.search(r'<script type="application/ld\+json">(\{"@context": "https://schema.org", "@type": "FAQPage".*?\})</script>', t, re.S)
    plain = lambda s: re.sub(r"<[^>]+>", "", s)
    if not m:  # article has no FAQ yet: create the JSON-LD and the visible block
        d = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": plain(an)}} for q, an in extra]}
        t = t.replace("</head>", '<script type="application/ld+json">%s</script>\n</head>' % json.dumps(d, ensure_ascii=False).replace("</", "<\\/"), 1)
        block = "<h2>Questions adults ask</h2>\n" + "".join("<details><summary>%s</summary><p>%s</p></details>\n" % (e(q), an) for q, an in extra)
        t, k = re.subn(r"(<h2>Where to go from here</h2>)", lambda mm: block + mm.group(1), t, 1)
        if not k: t = t.replace("    </article>", block + "    </article>", 1)
        return t
    d = json.loads(m.group(1))
    have = {q["name"] for q in d["mainEntity"]}
    new = [(q, an) for q, an in extra if q not in have]
    new_ld = [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": plain(an)}} for q, an in new]
    d["mainEntity"] = new_ld + d["mainEntity"]
    t = t.replace(m.group(0), '<script type="application/ld+json">%s</script>' % json.dumps(d, ensure_ascii=False).replace("</", "<\\/"), 1)
    block = "".join("<details><summary>%s</summary><p>%s</p></details>\n" % (e(q), an) for q, an in new)
    t, k = re.subn(r"(<h2>Questions adults ask</h2>\n)", lambda m: m.group(1) + block, t, 1)
    assert k, "no visible FAQ heading"
    return t

def run():
    n = 0
    for slug, A in ART.items():
        p = HERE / (slug + ".html"); t = p.read_text(encoding="utf-8")
        if M in t: continue
        t = patch_meta(t, A)
        box = '%s<div class="card" style="margin:0 0 22px;padding:16px 20px;border-left:4px solid var(--gold,#c9a24a)"><p style="margin:0"><strong>Quick answer.</strong> %s</p></div>\n' % (M, A["quick"])
        t, k = re.subn(r'(<article class="post">\n)', lambda m: m.group(1) + box, t, 1); assert k, slug
        t = patch_faq(t, A["faqs"])
        if A.get("pair"):
            t, k = re.subn(r"(<h2>Where to go from here</h2>)", lambda m: PAIR + "\n" + m.group(1), t, 1)
            if not k: t = t.replace("    </article>", PAIR + "\n    </article>", 1)
        p.write_text(t, encoding="utf-8"); n += 1
    for slug, items in LINKS.items():
        p = HERE / (slug + ".html"); t = p.read_text(encoding="utf-8")
        for target, anchor, pre, post in items:
            tag = "<!--opu-sl:%s-->" % target
            if tag in t: continue
            href = SHOP + target + ".html" if target in ("piano-pedals", "piano-benches-and-stands", "music-stands", "piano-accessories") else target + ".html"
            para = '<p>%s%s<a href="%s">%s</a>%s</p>\n' % (tag, pre, href, anchor, post)
            t, k = re.subn(r"(<h2>Where to go from here</h2>)", lambda m: para + m.group(1), t, 1)
            if not k:
                t, k = re.subn(r"(\n    </article>)", lambda m: "\n" + para.rstrip("\n") + m.group(1), t, 1)
            assert k, (slug, target)
            n += 1
        p.write_text(t, encoding="utf-8")
    print("patched", n)
run()
