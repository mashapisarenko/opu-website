"""Striking-distance SEO layer (2026-11-20): query-first titles/descriptions, a Quick answer box and
query-specific FAQs for the shop pages Search Console shows near the top with ~0 clicks.
Applied by make_shop_pages.py after every other layer. Edit here, then rebuild."""
import html

def _e(s): return html.escape(s, quote=False)

OVR = {
 "piano-pedals": dict(
  title="Sustain Pedal for Digital Piano: Budget to Pro Picks",
  desc="Best sustain pedals for digital pianos and keyboards, budget to pro, chosen by a concert pianist: piano-style, universal and half-pedal.",
  h1="Best Sustain Pedal for Digital Piano: Budget to Pro Picks",
  answer="The best sustain pedal for a digital piano is a piano-style pedal that suits your instrument: it moves and returns like a real one, fits your jack and, if your piano allows, gives half-pedal control. A good pedal is one of the most affordable upgrades a pianist can make.",
  quick=("A sustain pedal is one of the cheapest upgrades you can make, so you will not need a big budget: the pedals on this page are modest purchases (check today's price on Amazon). "
         "Choose a piano-style pedal made for your brand or marked universal, read your manual for the jack and polarity, and move up to a three-pedal unit only if your piano is built to take one."),
  faqs=[("What is the best sustain pedal under $500?",
         "You do not need a large budget for a sustain pedal. The one that matters most is the one shaped like a piano pedal and made for your keyboard. Prices change, so check Amazon."),
        ("What is the difference between a sustain pedal and a footswitch?",
         "A footswitch is a small on-off button. A piano-style sustain pedal is shaped and weighted like a real piano pedal, so your foot learns the right movement from the start."),
        ("Why does my sustain pedal work backwards?",
         "Usually the polarity does not match your keyboard. Unplug the pedal, switch the keyboard on without your foot on it, then plug the pedal in again. Some pedals have a polarity switch."),
        ("Can I use any sustain pedal with a Yamaha or Roland digital piano?",
         "Many universal pedals work, but not all support half-pedaling. Use the pedal your manual names, or a piano-style pedal described as compatible with your model.")],
  see=[("best-sustain-pedal-for-digital-piano", "my full sustain pedal buying guide"), ("when-should-you-start-using-the-piano-pedal", "when to start using the pedal")]),
 "music-stands": dict(
  title="Best Music Stands for Piano and Home Practice",
  desc="Best music stands for piano practice and lessons, chosen by a concert pianist: sturdy Manhasset, folding and tablet stands for every budget.",
  h1="Best Music Stands for Piano Practice and Lessons",
  answer="The best music stand for piano practice holds the page steady at eye level: a Manhasset-style desk stand for a permanent corner, a folding stand for small spaces and lessons away from home. A good stand is a modest purchase that lasts for years.",
  quick=("Whether you need the best music stand under $500 or under $1,000, the answer is the same: a solid desk and a steady base matter far more than a high price. "
         "For a desk or study corner, choose a sturdy stand that adjusts to eye level. For travel and lessons, choose one that folds flat. For a tablet score, choose a stand made to hold one."),
  faqs=[("What is the best music stand under $500?",
         "A solid-desk orchestral stand such as the Manhasset models on this page is built to last and sits well under that figure. A folding wire stand is lighter and cheaper if you carry it around. Prices change, so check Amazon."),
        ("What is the best music stand for students, desk work or writers?",
         "Choose a stand that adjusts in height and tilts, with a desk wide enough for an open book. A solid-desk stand holds heavy albums and notebooks steadily, and it keeps your neck level so you do not hunch."),
        ("What music stand do I need for practice and lessons?",
         "A folding stand is the easiest to carry to lessons and put away after practice. For a permanent music corner at home, a solid-desk orchestral stand does not wobble when you turn a page."),
        ("How high should a music stand be?",
         "At a height where you read the page without tilting your head, so the top of the music sits roughly at eye level. Adjust it sitting down, in your playing position.")],
  see=[("piano-bench-height-posture", "bench height and posture")]),
 "piano-accessories": dict(
  title="Piano Accessories: 6 Essentials for Every Pianist",
  desc="The piano accessories every pianist and digital piano owner needs, chosen by a concert pianist: pedal, bench, headphones, lamp, metronome, cover.",
  h1="Piano Accessories: The Essentials Every Pianist Needs",
  answer="The piano accessories you actually need are a piano-style sustain pedal, an adjustable bench, closed-back headphones and a light on the page. A metronome, a book clip and a dust cover come next.",
  quick=("Pianist accessories fall into two groups. First, the four that change how you play: a piano-style sustain pedal, an adjustable bench, headphones and a light for the page. "
         "Second, the small things that keep practice going: a metronome, a music stand, a book clip and a dust cover. Start with the first group."),
  faqs=[("What accessories does a pianist need?",
         "A sustain pedal, an adjustable bench, headphones and a light on the page do the most. A metronome, a music stand and a dust cover follow."),
        ("What accessories do I need for a digital piano?",
         "A piano-style sustain pedal, a stand and bench at the right height, and headphones for quiet practice. Check your manual for the pedal jack and for the stand your model needs."),
        ("What are good piano accessories as a gift for a pianist?",
         "A metronome, a music stand light, a book clip, a piano-themed bag or good headphones. The accessories most pianists use every day are the practical ones."),
        ("Which piano accessories are worth buying first?",
         "A bench you can adjust and a real sustain pedal. Both change your posture and your sound immediately, and both cost far less than the piano.")],
  see=[("piano-bench-height-posture", "bench height and posture")]),
 "piano-benches-and-stands": dict(
  title="Adjustable Piano Bench: Best Picks for Adult Players",
  desc="The best adjustable piano benches and keyboard stands for adults, chosen by a concert pianist: set your seat height so forearms sit level with the keys.",
  h1="Best Adjustable Piano Bench and Keyboard Stands for Adults",
  answer="The best adjustable piano bench for an adult is one whose height you can set, so your forearms sit level with the keys. Pair it with a keyboard stand that does not wobble. These benches, duet benches and stands are my picks.",
  quick=("An adjustable piano bench lets you set your seat so your forearms are level with the keys and your feet are flat on the floor. "
         "Choose a hydraulic or screw-adjust bench if several people play, a solid padded bench with storage if you want a fixed height you set once, and a stand that does not rock if you play on a keyboard."),
  faqs=[("What is the best adjustable piano bench for an adult?",
         "One with a firm padded seat that goes high and low enough for you, and that does not wobble when you lean. Hydraulic and screw-adjust benches both work; I list both kinds below."),
        ("How high should my piano bench be?",
         "High enough that your forearms are roughly level with the keys and your elbows slightly in front of your body, with your feet flat on the floor. If you cannot reach the floor, add a footrest."),
        ("Do I need a bench or can I use a chair?",
         "A dining chair is nearly always too low and too deep. A proper bench or an adjustable stool puts you at the right height and leaves your arms free."),
        ("Can I use an adjustable bench with a digital piano or keyboard?",
         "Yes. An adjustable bench is the most useful pairing for a keyboard stand, because stand height and seat height both change with the player.")],
  see=[("piano-bench-height-posture", "how to set your bench height")]),
 "gifts-for-piano-teachers": dict(
  title="Piano Teacher Gifts 2026: Music Teacher Gift Ideas",
  desc="Piano teacher gifts and music teacher gift ideas from a piano professor: books, jewelry, headphones and thank-you presents a teacher will use.",
  h1="Piano Teacher Gifts: Music Teacher Gift Ideas for 2026",
  answer="A piano teacher rarely wants something expensive. A good book, a piece of music jewelry, a music-themed mug or a good pair of headphones says you noticed, and a recording of your own playing says the most.",
  quick=("The best piano teacher gifts are small, useful and personal: a music book, a stand light, a music-themed mug or piece of jewelry, a good pair of headphones, plus a note about what you have learned. "
         "If you are a student, a recording of your own playing is the one gift that is always welcome."),
  faqs=[("What do you give a piano teacher as a gift?",
         "Something small and useful, with a handwritten note: a music book, a stand light, a metronome or a music-themed accessory. A teacher hears every week how you have grown, so a personal word means most."),
        ("What is a good inexpensive piano teacher gift?",
         "A book clip, a piano-themed mug or coasters, or a handwritten note. Check today's price on Amazon for each."),
        ("What is a good end-of-year or Christmas gift for a piano teacher?",
         "A practical gift such as a music light or book, plus a note that names one thing you can now play. Gift cards are welcome too."),
        ("Can I give lessons as a gift?",
         "Yes. A gift certificate for online lessons suits any adult level, and it is the gift that produces playing.")],
  see=[("gift-certificate", "give online piano lessons as a gift")]),
}

def apply(PAGES, GUIDES):
    for pg in list(PAGES) + list(GUIDES.values()):
        o = OVR.get(pg.get("slug") or "")
        if not o: continue
        for k in ("title", "desc", "h1", "answer"):
            pg[k] = o[k]
        pg["faqs"] = list(o["faqs"]) + [f for f in pg["faqs"] if f[0] not in {q for q, a in o["faqs"]}]
    for slug, g in GUIDES.items():
        o = OVR.get(slug)
        if o:
            for k in ("title", "desc", "h1", "answer"): g[k] = o[k]
            g["faqs"] = list(o["faqs"]) + [f for f in g["faqs"] if f[0] not in {q for q, a in o["faqs"]}]

def quick_box(slug):
    o = OVR.get(slug)
    if not o: return ""
    return '<div class="howbox quick-answer"><h2>Quick answer</h2><p style="margin:0">%s</p></div>' % _e(o["quick"])

def see_also(slug):
    o = OVR.get(slug)
    if not o or not o.get("see"): return ""
    out = []
    for target, anchor in o["see"]:
        href = "../gift-certificate.html" if target == "gift-certificate" else "../blog/%s.html" % target
        out.append('<a href="%s">%s</a>' % (href, _e(anchor)))
    return '<p class="shop-links" style="margin-top:18px">Related: ' + " &middot; ".join(out) + '.</p>'
