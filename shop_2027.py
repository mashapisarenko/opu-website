# -*- coding: utf-8 -*-
"""New Year 2027 landing page: shop/start-piano-in-2027.html (written 2026-11-20).
Called from make_shop_pages.py (build(globals()) and strip(slug)). Edit here, then rebuild.
Rules: no prices, no ratings, no Amazon images, no claim of hands-on testing; adults learning alone; no Las Vegas."""
import html

SLUG = "start-piano-in-2027"
TITLE = "Start Piano in 2027: The Keyboard and Lessons You Need"
DESC = "Start piano in 2027: a first-month plan, the digital piano, headphones, bench and pedal to buy first, and online lessons with a concert pianist."
H1 = "Start Piano in 2027: The Keyboard and Lessons You Need"
ANSWER = ("To start piano in 2027 you need a keyboard with weighted keys, a bench at the right height, headphones, a sustain pedal and fifteen minutes a day. "
          "Here is the plan I would give an adult beginner, the gear I would buy first, and how to begin lessons with a concert pianist.")
ARTICLE = "learn-piano-in-2027-what-you-need-to-start"
LINKED_ARTICLES = [ARTICLE, "piano-goals-for-the-new-year-that-you-will-keep"]   # shop_seo.BLOG[SLUG]; queued, so linked on their day
STRIP_SLUGS = {"index", "pianos", "digital-pianos", "keyboards", "gifts-for-adult-beginners", "christmas-gifts-for-pianists", "gifts-for-pianists"}

TOP3 = [("Best value", "B01LY8OUQW"), ("Best overall", "B08SBZW46G"), ("Premium pick", "B08M3P4XL4")]
LADDER = [
 ("step-piano-budget", "Step 1: The piano, budget picks",
  "Start here if you want to spend carefully. Each has 88 keys with a weighted or graded action; read each listing for what it includes.",
  ["B01LY8OUQW", "B07MH391ZF", "B09GG8SCBF"]),
 ("step-piano-mid", "Step 1: The piano, mid-range picks",
  "A step up in sound and features, for a piano you will still want in five years.",
  ["B08SBZW46G", "B0CBN7HYKB"]),
 ("step-piano-premium", "Step 1: The piano, premium pick",
  "For an adult who knows this is for life and wants a more refined touch.",
  ["B08M3P4XL4"]),
 ("step-keyboard", "If you would rather begin with a keyboard",
  "A 61-key touch-sensitive keyboard will carry a first year, and it is the gentlest way to try piano before you commit. You will want weighted keys sooner than you think.",
  ["B07WN7NG5H"]),
 ("step-headphones", "Step 2: Headphones",
  "Closed-back headphones let you practice at any hour, which is what keeps a new habit alive.",
  ["B013WW8WRK", "B000AJIF4E", "B0006NL5SM"]),
 ("step-bench", "Step 3: A bench",
  "Your forearms should sit level with the keys. A bench you can adjust does that; a dining chair rarely does.",
  ["B06XF6NF5Y", "B07DTH552V", "B00I362NXU"]),
 ("step-pedal", "Step 4: A sustain pedal",
  "A piano-style pedal that moves and returns like a real one teaches your foot the right habit from the start.",
  ["B00PNG4BV0", "B00063678K", "B000OY0KWA"]),
 ("step-stand", "Step 5: A stand, if your piano has none",
  "Only needed for a portable piano. Choose one that does not rock when you play.",
  ["B07574VQPQ", "B01B15JPCQ"]),
]

PLAN = [
 ("Week 1: Set up and sit down.", "Place the keyboard where you will see it every day and set your bench so your forearms are level with the keys. Watch Lesson 1 of my free course, then play for ten minutes. The only goal is to do it again tomorrow."),
 ("Week 2: Find your hands.", "Learn where middle C is and place both hands around it. Fifteen minutes a day, slowly, with the lessons in order. Skip nothing; the order is what makes it easy."),
 ("Week 3: Play a real tune.", "Choose the first short piece from the course and count it out loud. Practice it in small pieces, hands separately first, and stop each session while it still feels good."),
 ("Week 4: Record and send.", "Record yourself on your phone and <a href=\"../submit.html\">send me the recording</a>; I read it and tell you what I hear, at no charge. Then decide what comes next: the free course alone, or private lessons with me."),
]

FAQS = [
 ("Is 2027 too late to start piano in my 40s, 50s or 60s?",
  "No. Adults learn differently from children, not worse: you can concentrate, you understand why a technique works and you can practice on purpose. I teach adults of every age, and the ones who improve are the ones who practice a little every day."),
 ("Should I start with a keyboard or a digital piano?",
  "If you can, start with a digital piano that has 88 weighted keys, because that touch is what you will keep learning on. A 61-key touch-sensitive keyboard will carry a first year if space or budget is tight. Avoid a keyboard with tiny keys or no touch response."),
 ("How long should I practice each day?",
  "Fifteen to twenty minutes a day is better than one long session a week. Short, regular practice builds the habit and lets your hands remember between sessions."),
 ("Can I learn piano with online lessons as an adult?",
  "Yes. Online lessons work well for adults: you play at your own piano, I hear and see your hands, and we work on what you actually need. My free 41-lesson course is a good way to begin before private lessons."),
 ("What is a good gift for someone starting piano in 2027?",
  "A gift certificate for online piano lessons, or a keyboard with a bench and headphones to go with it. The gift is the beginning: a teacher and an instrument ready on the first day."),
]

def _e(s): return html.escape(s, quote=False)

def strip(slug):
    if slug not in STRIP_SLUGS: return ""
    return ('<section class="shop-cta y27-strip"><h2><span aria-hidden="true">&#127878;</span> A new year, a new beginning: start piano in 2027</h2>'
            '<p>If this is the year you finally learn, I have written the plan: a first month, the gear to buy first, and where to find a teacher.</p>'
            '<p class="shop-links"><a class="btn" href="start-piano-in-2027.html">Start piano in 2027</a> '
            '<a class="btn ghost" href="../free-course.html">Free 41-lesson course</a></p></section>')

def build(g):
    card, section, faq_html, faq_ld, item_list_ld, crumb_ld = (g[k] for k in ("card", "section", "faq_html", "faq_ld", "item_list_ld", "crumb_ld"))
    pick, top3_html, related_html, blog_item, page, AUTHOR, REPORT, OUT, esc = (g[k] for k in ("pick", "top3_html", "related_html", "blog_item", "page", "AUTHOR", "REPORT", "OUT", "esc"))
    seen, allp = set(), []
    def uniq(ps):
        for p in ps:
            if p["asin"] not in seen:
                seen.add(p["asin"]); allp.append(p)
    top = [(lab, pick([a])[0]) for lab, a in TOP3]
    ladder_html = ""
    idx = 0
    for sid, head, intro, asins in LADDER:
        ps = pick(asins); uniq(ps)
        ladder_html += '<div class="tier-head" id="%s"><h3>%s</h3><span>%d picks</span></div><p class="lead" style="margin:0 0 14px">%s</p><div class="pgrid">' % (sid, _e(head), len(ps), _e(intro))
        for p in ps:
            ladder_html += card(p, idx, SLUG, tier_tag=False); idx += 1
        ladder_html += "</div>"
    uniq([p for _, p in top])
    plan = "".join("<li><strong>%s</strong> %s</li>" % (_e(a), b) for a, b in PLAN)
    lessons = ('<section class="shop-cta y27-lessons" id="lessons"><h2>Start with a concert pianist</h2>'
               '<p>A keyboard gets you to the first note. A teacher gets you to the tenth, the hundredth and the first piece you are proud of. '
               'I am Dr. Maria Pisarenko, D.M.A., a concert pianist and university piano professor, and I teach adults online, wherever they live. '
               'You can begin three ways, and none of them requires the others.</p>'
               '<ul class="shop-list"><li><strong>Free:</strong> my <a href="../free-course.html">41-lesson beginner course</a>, published in full, in order.</li>'
               '<li><strong>Private:</strong> <a href="../lessons.html">online piano lessons with me</a>, built around your hands, your piano and your goals.</li>'
               '<li><strong>As a gift:</strong> a <a href="../gift-certificate.html">gift certificate for online piano lessons</a> for someone who is starting this year.</li></ul>'
               '<p class="shop-links"><a class="btn" href="../lessons.html">See private online lessons</a> <a class="btn ghost" href="../free-course.html">&#9654; Start the free course</a> '
               '<a class="btn ghost" href="../gift-certificate.html">Give a lesson gift certificate</a></p>'
               '<div class="howbox" style="margin-top:16px"><h3 style="margin-top:0">From Christmas to the New Year</h3>'
               '<p style="margin:0">Giving lessons for Christmas, or starting your own in January? <!-- TODO 2027-01-01: remove this price line and the same line on the other shop pages (xmas_pair, BANNER_REST in make_shop_pages.py) once lesson prices have changed -->'
               'Gift certificates bought by December 31 keep today&#39;s price; lesson prices increase January 1, 2027.</p></div></section>')
    live_reads = [("how-long-to-practice-piano-each-day", "How long should you practice piano each day?"),
                  ("is-it-too-late-to-learn-piano-at-40-50-60", "Is it too late to learn piano at 40, 50 or 60?"),
                  ("weighted-vs-semi-weighted-keys", "Weighted or semi-weighted keys?"),
                  ("digital-piano-vs-acoustic-beginner", "Digital piano or acoustic piano for a beginner?")]
    reads = "".join(blog_item(b) for b in LINKED_ARTICLES) + "".join('<li><a href="../blog/%s.html">%s</a></li>' % (s, _e(t)) for s, t in live_reads)
    reads += '<li><a href="../shop/which-digital-piano-to-buy.html">Which digital piano to buy: my long guide</a></li><li><a href="../submit.html">Send me your playing for free feedback</a></li>'
    related = related_html(["digital-pianos", "headphones-for-piano", "piano-benches-and-stands", "piano-pedals", "keyboards", "gifts-for-adult-beginners"])
    body = section(
        '<div class="howbox quick-answer"><h2>Quick answer</h2><p style="margin:0">To start piano in 2027 you need a keyboard with weighted keys if you can have them (61 touch-sensitive keys will carry a first year), '
        'a bench at the right height, closed-back headphones and a sustain pedal. Then you need a plan and someone to hear you play. This page gives you both.</p></div>'
        '<div class="shop-prose"><p class="lead">A new year is a good moment to begin something you have wanted for a long time. If one of your dreams is to sit down and play, 2027 can be the year it starts. '
        'You do not need talent, a childhood of lessons or an expensive instrument. You need a keyboard, a small daily habit and a little guidance, and I will help with all three.</p></div>'
        '<h2 style="margin-top:34px" id="first-month">What does your first month of piano look like?</h2>'
        '<p class="muted">Four weeks, fifteen to twenty minutes a day. This is the plan I would give an adult who is learning alone.</p><ol class="shop-steps">%s</ol>' % plan +
        top3_html(None, SLUG, top) +
        '<h2 style="margin-top:40px" id="what-to-buy">What should you buy first?</h2>'
        '<p class="muted">Buy in this order. The piano matters most; everything after it is small and cheap by comparison. I list each item only by what its Amazon listing says, and I never print a price: open the listing to see today&#39;s.</p>' +
        ladder_html +
        lessons +
        '<h2 style="margin-top:40px">What do adults ask before they start piano in 2027?</h2><div class="shop-faq">%s</div>' % faq_html(FAQS) +
        '<h2 style="margin-top:40px">Where should you read next?</h2><ul class="readnext">%s</ul>' % reads +
        '<h2 style="margin-top:40px">What else might you need?</h2>' + related + AUTHOR)
    lds = [item_list_ld(allp, H1), faq_ld(FAQS), crumb_ld("Start Piano in 2027", SLUG)]
    out = page(SLUG, TITLE, DESC, H1, "A new beginning", esc(ANSWER), body, lds, '<a href="index.html">Shop</a> / Start Piano in 2027')
    (OUT / (SLUG + ".html")).write_text(out, encoding="utf-8")
    REPORT.append((SLUG + ".html", TITLE, DESC, len(allp)))
