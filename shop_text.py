# -*- coding: utf-8 -*-
"""Hub, gift guides and the long digital-piano article for the OPU shop. No prices, ratings or images are ever printed."""
import json, pathlib
_P = json.loads((pathlib.Path(__file__).resolve().parent.parent / "_shop" / "products.json").read_text(encoding="utf-8"))

def _cat(*cats, tier=None, n=8, use=None):
    out = [p for p in _P if p["category"] in cats and (tier is None or p["tier"] in tier) and (use is None or p["use_case"] in use)]
    return out[:n]

HUB = dict(
 title="Piano Shop: Gear a Concert Pianist Recommends",
 desc="Digital pianos, keyboards, headphones, benches and recording gear chosen by concert pianist Dr. Maria Pisarenko, D.M.A., for adult piano students.",
 h1="The Online Piano University Shop",
 sub="Gear for adult piano students, chosen by a working concert pianist and professor. Every category tells you what to look for and how it helps you learn.",
 intro="This is not a general store. It is a short, curated list from Dr. Maria Pisarenko, D.M.A., concert pianist and university piano professor, of the instruments and tools my adult students actually need: a keyboard with a real touch, headphones for daily practice, a bench at the right height, a light to read by and a simple way to record yourself and send me your playing for free feedback.",
 faqs=[("What should an adult beginner buy first?", "An 88-key digital piano with weighted keys, a sustain pedal, an adjustable bench and a pair of closed-back headphones. Nothing else is needed to start."),
       ("Do I need to buy anything to use the free course?", "No. The 41-lesson course is free and so is feedback on your playing. The shop is for when you are ready for your own instrument."),
       ("Why is this shop different from a general store?", "Every category is chosen by a concert pianist who teaches adults and says why it helps you learn: touch, daily practice, correct height, reading music, and recording yourself."),
       ("Are these affiliate links?", "Yes. As an Amazon Associate I earn from qualifying purchases, at no extra cost to you. I do not print prices; open the listing on Amazon to check today's price.")],
 top=["B01LY8OUQW", "B08SBZW46G", "B0CBN7HYKB", "B00HVLUR54", "B00IT0IHOY", "B0B823S1NR", "B0CSLDLKZJ", "B07MH391ZF"],
)

def _gift_faq(who):
    return [("Where do the gift certificates fit in?", "If the person you are buying for would rather learn than own more things, give online piano lessons with me. Gift certificates bought by December 31 keep today's lesson price; prices increase January 1, 2027."),
            ("Do I need to buy anything before starting lessons?", "No. My 41-lesson beginner course is free, and so is feedback on your playing. Gear only helps once the habit is there."),
            ("Are these affiliate links?", "Yes. As an Amazon Associate I earn from qualifying purchases, at no extra cost to you. I list only items I would be glad to see in a student's home."),
            ("How do I check the price?", "Open the listing on Amazon. Prices change often, so I do not print them here.")]

def _gp_sections(pick, gift_pool, band_sections):
    pool = gift_pool([])
    return band_sections(pool, [("Small gifts", 0, 40, "Easy to give, easy to use every week."),
                                ("Mid-sized gifts", 40, 120, "A step up, still personal."),
                                ("Special-occasion gifts", 120, 100000, "For a birthday, a graduation or a milestone.")], 8)

def _gb_sections(pick, gift_pool, band_sections):
    return [("An instrument to start on", "A weighted keyboard is where touch and technique begin.", _cat("digital-pianos", tier=["budget", "mid"], n=6)),
            ("Headphones for daily practice", "Short sessions every day beat long ones once a week; headphones make that possible.", _cat("headphones", tier=["budget", "mid"], n=5)),
            ("A bench and a light", "Correct height and a clearly lit page.", _cat("benches-and-stands", n=4) + _cat("stand-lights", n=3)),
            ("Books for adults", "One good method book, worked through in order.", _cat("method-books", n=5))]

def _gt_sections(pick, gift_pool, band_sections):
    return [("Books for a teacher's shelf", "Reading about music and the brain.", _cat("books-for-music-lovers", n=2) + _cat("method-books", tier=["mid", "premium"], n=4)),
            ("Music-themed gifts", "Small, personal and useful.", _cat("music-textiles-small-gifts", n=5) + _cat("gifts-home-decor", n=3)),
            ("Listening and wellbeing", "Because teachers listen all day.", _cat("music-wellbeing", n=6)),
            ("Special-occasion gifts", "For a retirement, an anniversary or a thank-you that deserves one.", _cat("luxury-gifts", n=5))]

GUIDES = {
 "gifts-for-pianists": dict(label="Gifts for Pianists", blurb="Gift ideas for pianists by size of gift.",
   title="Gifts for Pianists: A Concert Pianist's Gift Guide",
   desc="Gift ideas for pianists at every budget, chosen by a concert pianist: small music gifts, headphones, home decor and special-occasion presents.",
   h1="Gifts for Pianists", eyebrow="Gift guide", sub="Ideas a concert pianist would be glad to receive, from a small thank-you to a special-occasion present.",
   intro_html="<p class=\"lead\">The best gift for a pianist is something that makes practice easier or listening better. Below are small gifts, mid-sized gifts and special-occasion gifts, each described only by its own listing.</p><p>If you would rather give an experience, give <a href=\"../lessons.html#book\">online piano lessons</a>. Gift certificates bought by December 31 keep today&#39;s lesson price.</p>",
   sections=_gp_sections, faqs=_gift_faq("pianists"), related=["gifts-for-adult-beginners", "gifts-for-piano-teachers", "music-home-decor"]),
 "gifts-for-adult-beginners": dict(label="Gifts for Adult Beginners", blurb="Starter gear for an adult learning piano.",
   title="Gifts for Adult Piano Beginners: What They Need",
   desc="Gift ideas for an adult learning piano, picked by a teacher of adults: a weighted keyboard, practice headphones, a bench, a light and a method book.",
   h1="Gifts for Adult Piano Beginners", eyebrow="Gift guide", sub="What a teacher of adults would put under the tree for someone starting piano.",
   intro_html="<p class=\"lead\">For an adult beginner, give the things that remove excuses: an instrument with weighted keys, headphones for late-night practice, a bench at the right height and a book written for adults.</p><p>Or give the lessons themselves: the 41-lesson course is free, and <a href=\"../lessons.html#book\">gift certificates for online piano lessons</a> bought by December 31 keep today's price.</p>",
   sections=_gb_sections, faqs=_gift_faq("beginners"), related=["gifts-for-pianists", "digital-pianos", "headphones-for-piano"]),
 "gifts-for-piano-teachers": dict(label="Gifts for Piano Teachers", blurb="Thoughtful thank-you gifts for a piano teacher.",
   title="Gifts for Piano Teachers: Thoughtful Thank-You Ideas",
   desc="Gift ideas for a piano teacher from a piano professor: books, music-themed gifts, listening gear and special-occasion presents students can give.",
   h1="Gifts for Piano Teachers", eyebrow="Gift guide", sub="What one piano professor would be happy to receive from a student.",
   intro_html="<p class=\"lead\">A teacher is rarely looking for something expensive. A book, a small music-themed gift or a good pair of headphones says that you noticed. A recording of your own playing, sent with a note, is better than any of it.</p>",
   sections=_gt_sections, faqs=_gift_faq("teachers"), related=["gifts-for-pianists", "music-and-wellbeing", "luxury-gifts-for-pianists"]),
}

_ART_PICKS = ["B01DZXE9NC", "B07X9SD5JR", "B01LY8OUQW", "B07MH391ZF", "B08SBZW46G", "B0CBN7HYKB", "B074FTTTMZ"]

ARTICLE = dict(label="Which Digital Piano to Buy", slug="which-digital-piano-to-buy",
 title="Which Digital Piano Should an Adult Beginner Buy?",
 desc="Which digital piano should an adult beginner buy? A concert pianist explains keys, touch, pedals and budget, with picks from budget to premium.",
 h1="Which Digital Piano Should an Adult Beginner Buy?",
 sub="Short answer: an 88-key digital piano with weighted keys, a real piano sound and a sustain pedal. Here is how to choose among them.",
 picks=_ART_PICKS,
 html_before="""<p class="lead"><strong>The short answer:</strong> buy the best 88-key digital piano with weighted keys that your budget allows, add a sustain pedal, an adjustable bench and headphones, and begin.</p>
<h2>Start with the keys, not the features</h2><p>A digital piano is mostly a keyboard. The way a key resists your finger and returns decides what your hand learns. Weighted keys answer differently to a light touch and to the weight of the arm; that difference is musical playing. Features such as hundreds of sounds, rhythm patterns and apps are secondary.</p>
<h2>Then the sound, the pedal and the furniture</h2><p>Choose a piano whose basic piano sound you enjoy listening to for an hour. Make sure a sustain pedal is included or supported, and plan for a stable stand and an adjustable bench, because sitting height changes how you sound. See the <a href="piano-benches-and-stands.html">benches and stands</a> page and my article on <a href="../blog/piano-bench-height-posture.html">bench height and posture</a>.</p>
<h2>Eighty-eight keys or fewer?</h2><p>If you are buying once, buy 88. My article on <a href="../blog/how-many-keys-do-i-need-piano.html">how many keys you need</a> gives the longer answer. For the digital-versus-acoustic question, read <a href="../blog/digital-piano-vs-acoustic-beginner.html">this comparison</a>.</p>
<h2>Picks by budget</h2><p>Each note below comes from the listing itself. Open the listing on Amazon to check today's price.</p>""",
 html_after="""<h2>My advice in order</h2><ol><li>Decide where the piano will live.</li><li>Choose 88 weighted keys if you can.</li><li>Add a piano-style sustain pedal.</li><li>Set the bench so your forearms are level with the keys.</li><li>Buy <a href="headphones-for-piano.html">closed-back headphones</a> for daily practice.</li><li>Begin the <a href="../free-course.html">free 41-lesson course</a>.</li></ol>""",
 faqs=[("Which digital piano should an adult beginner buy?", "An 88-key digital piano with weighted keys, a good piano sound and a sustain pedal. Within that, buy the best touch your budget allows."),
       ("Are semi-weighted keys good enough?", "They can carry a first year, but weighted or hammer-action keys build a touch that transfers to any piano."),
       ("Do I need a bench?", "Yes. An adjustable bench sets your forearms at the right height, which a dining chair rarely does."),
       ("Can I start on a keyboard and upgrade later?", "Yes, if a touch-sensitive keyboard is all that fits now. Plan to upgrade when you start reading real repertoire.")],
 related=["digital-pianos", "piano-benches-and-stands", "headphones-for-piano"])
