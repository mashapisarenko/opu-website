# -*- coding: utf-8 -*-
"""SEO and store layer for the OPU affiliate shop (added 2026-11-10).

What lives here, and wins over shop_content.py / shop_text.py when the generator runs:
  META      per-page title, meta description, H1 and the answer-first hero line
  Q         the buyer-question H2s on each category page
  NEW_PAGES category pages built from explicit ASIN lists (metronomes, music stands)
  NEW_GUIDES guide pages (accessories hub, music lovers, Christmas + Hanukkah, stocking stuffers)
  BLOG      which published buyer posts each shop page links to
  who_for() the "I suggest it for" line on every product card

Query research behind it (US SERPs, 2026-11-10): retailers and publishers rank dedicated pages
for "piano accessories", "metronome for piano", "music stand", "gifts for music lovers",
"christmas gifts for pianists", "stocking stuffers for musicians", "hanukkah gifts for adults",
"piano gifts for adults" and "gifts for music teachers". Every product fact still comes only
from _shop/products.json (title and listing reason). No prices, ratings or review counts.
"""
import re
import shop_illus as SI

# ---------------------------------------------------------------- published buyer posts
BLOG_TITLES = {
 "black-friday-digital-piano-and-keyboard-guide-2026": "Black Friday Digital Piano and Keyboard Guide 2026",
 "best-gifts-for-piano-players-2026": "Best Gifts for Piano Players 2026: Small to Big",
 "christmas-gifts-for-musicians": "Christmas Gifts for Musicians: A Pianist's List",
 "hanukkah-gifts-for-music-lovers": "Hanukkah Gifts for Music Lovers: Eight Nights",
 "stocking-stuffers-for-piano-players": "Stocking Stuffers for Piano Players: Small Gifts",
 "gifts-for-adult-piano-beginners": "Gifts for Adult Piano Beginners: A Teacher's List",
 "gifts-for-seniors-learning-piano": "Gifts for Seniors Learning Piano: A Teacher's Guide",
 "gifts-for-piano-teachers": "Gifts for Piano Teachers: What They Will Use",
 "how-to-choose-a-piano-teacher": "How to Choose a Piano Teacher: What Actually Matters",
 "how-many-keys-do-i-need-piano": "How Many Keys Does a Beginner Keyboard Need? 61, 76, 88",
 "digital-piano-vs-acoustic-beginner": "Digital or Acoustic: What Actually Matters When You Are Starting",
 "piano-bench-height-posture": "How to Sit at the Piano: Bench Height and Distance",
 "piano-wrist-position-adults": "Wrist Height: The Most Common Fault in Adult Beginners",
 "practicing-piano-in-an-apartment": "How to Practice Piano in an Apartment Without Annoying Anyone",
 "how-long-to-practice-piano-each-day": "How Long Should You Practice Piano Each Day?",
 "playing-piano-for-other-people": "Why You Freeze When Someone Listens",
 "run-your-own-piano-lesson": "How to Run Your Own Piano Lesson",
 "right-notes-still-sounds-wrong": "You Can Play All the Right Notes and It Still Sounds Wrong",
 "piano-method-book-for-adult-beginners": "Best Piano Book for Adult Beginners: How to Choose",
 "easy-piano-songs-for-adult-beginners": "Easy Piano Songs for Adult Beginners",
 "how-to-read-piano-notes-grand-staff": "How to Read Piano Notes: A Beginner's Guide",
 "how-to-practice-piano-a-method-not-more-minutes": "Piano Practice Routine for Adults: A Daily Method",
 "how-to-count-music-out-loud": "How to Count Rhythm in Piano Music: Count Out Loud",
 "80-20-rule-for-piano-practice": "The 80/20 Rule for Piano Practice",
 "how-to-read-sheet-music-treble-clef-rhythm": "How to Read Sheet Music: The Staff, Treble Clef and Your First Rhythm",
 "why-you-still-cannot-read-music-fluently": "Why You Still Cannot Read Music Fluently",
 "piano-for-stress-relief": "Piano for Stress Relief: Why Playing Quiets a Busy Mind",
 "piano-and-the-aging-brain": "Is Playing Piano Good for Your Brain? What Research Says",
 "returning-to-piano-as-an-adult": "Returning to Piano as an Adult After Years Away",
}

BF, GIFTS26, XMAS, HANUK, STOCK = ("black-friday-digital-piano-and-keyboard-guide-2026", "best-gifts-for-piano-players-2026",
                                   "christmas-gifts-for-musicians", "hanukkah-gifts-for-music-lovers", "stocking-stuffers-for-piano-players")
BLOG = {
 "index": [BF, GIFTS26, XMAS, "how-many-keys-do-i-need-piano"],
 "digital-pianos": [BF, "digital-piano-vs-acoustic-beginner", "how-many-keys-do-i-need-piano"],
 "keyboards": [BF, "how-many-keys-do-i-need-piano", "digital-piano-vs-acoustic-beginner"],
 "piano-benches-and-stands": ["piano-bench-height-posture", "piano-wrist-position-adults", BF],
 "piano-pedals": [BF, "digital-piano-vs-acoustic-beginner"],
 "headphones-for-piano": ["practicing-piano-in-an-apartment", "how-long-to-practice-piano-each-day", BF],
 "record-yourself-playing": ["playing-piano-for-other-people", "run-your-own-piano-lesson"],
 "speakers-for-keyboards": ["right-notes-still-sounds-wrong", "practicing-piano-in-an-apartment"],
 "piano-books-and-sheet-music": ["piano-method-book-for-adult-beginners", "easy-piano-songs-for-adult-beginners", "how-to-read-piano-notes-grand-staff"],
 "practice-tools": ["how-to-practice-piano-a-method-not-more-minutes", "how-to-count-music-out-loud", "80-20-rule-for-piano-practice"],
 "metronomes-and-tuners": ["how-to-count-music-out-loud", "how-to-practice-piano-a-method-not-more-minutes", "how-long-to-practice-piano-each-day"],
 "music-stands": ["how-to-read-sheet-music-treble-clef-rhythm", "piano-bench-height-posture"],
 "stand-lights": ["why-you-still-cannot-read-music-fluently", "how-to-read-piano-notes-grand-staff"],
 "piano-care": ["digital-piano-vs-acoustic-beginner", "returning-to-piano-as-an-adult"],
 "music-and-wellbeing": ["piano-for-stress-relief", "piano-and-the-aging-brain", HANUK],
 "music-home-decor": [GIFTS26, XMAS, STOCK],
 "luxury-gifts-for-pianists": [GIFTS26, XMAS],
 "gifts-for-pianists": [GIFTS26, XMAS, HANUK],
 "gifts-for-adult-beginners": ["gifts-for-adult-piano-beginners", "gifts-for-seniors-learning-piano", BF],
 "gifts-for-piano-teachers": ["gifts-for-piano-teachers", "how-to-choose-a-piano-teacher", STOCK],
 "which-digital-piano-to-buy": [BF, "how-many-keys-do-i-need-piano", "digital-piano-vs-acoustic-beginner"],
 "piano-accessories": [BF, "piano-bench-height-posture", "practicing-piano-in-an-apartment"],
 "gifts-for-music-lovers": [HANUK, XMAS, "piano-for-stress-relief"],
 "christmas-gifts-for-pianists": [XMAS, HANUK, STOCK, GIFTS26],
 "stocking-stuffers-for-musicians": [STOCK, XMAS, "gifts-for-piano-teachers"],
}

# ---------------------------------------------------------------- titles, descriptions, H1, answer-first line
META = {
 "index": dict(title="Online Piano Store: Pianos, Accessories & Music Gifts",
   desc="An online piano store curated by concert pianist Dr. Maria Pisarenko: digital pianos, keyboards, piano accessories, books and music gifts for adults.",
   h1="Online Piano Store: Pianos, Accessories and Music Gifts",
   intro="I am Dr. Maria Pisarenko, D.M.A., a concert pianist and university piano professor, and every item here is something I would be glad to see in a student's home: a keyboard with a real touch, headphones for daily practice, a bench at the right height, a light to read by, a simple way to record yourself and send me your playing for free feedback, and gifts for the musicians in your life. Amazon sells and ships everything; I choose it.",
   answer="This online piano store is my own list of recommendations: digital pianos, keyboards, piano accessories, sheet music books and music gifts, each chosen by a concert pianist who teaches adults. Browse by need, budget or holiday, then buy on Amazon."),
 "digital-pianos": dict(title="Digital Piano Store: Best Digital Pianos for Adults",
   desc="Shop digital pianos for adult beginners, picked by a concert pianist: 88 weighted keys, a real piano sound and a sustain pedal, from budget to premium.",
   answer="The best digital piano for an adult beginner has 88 weighted keys, a real piano sound and a sustain pedal. These are my picks, grouped from budget to premium, each described only by what its listing states."),
 "keyboards": dict(title="Keyboard Store: Best Keyboards and MIDI Controllers",
   desc="Shop portable keyboards and USB MIDI controllers for adult beginners, chosen by a concert pianist: key count, touch response and what each is for.",
   answer="For a beginner, the best keyboard has full-size, touch-sensitive keys, and 61 keys will carry a first year. A MIDI controller only makes sense if you play into an app or music software. Here are my picks of both."),
 "piano-benches-and-stands": dict(title="Best Piano Bench for Adults: Adjustable Benches & Stands",
   answer="The best piano bench for an adult is one you can adjust, so your forearms sit level with the keys. Pair it with a keyboard stand that does not wobble. These benches, duet benches and stands are my picks."),
 "piano-pedals": dict(title="Best Sustain Pedal for Digital Piano and Keyboard",
   answer="The best sustain pedal for a digital piano is a piano-style pedal that moves and returns like a real one and suits your keyboard. Start there; half-pedal control and three-pedal units come later."),
 "headphones-for-piano": dict(title="Best Headphones for Piano Practice on a Digital Piano",
   answer="The best headphones for piano practice are wired, comfortable for an hour and honest in sound: closed-back if others are nearby, open-back if you practice alone. These are my picks for a digital piano."),
 "record-yourself-playing": dict(
   answer="To record yourself playing piano you need clean sound first, from a USB microphone or a handheld recorder, then a phone mount over the keys and even light. These are the simple setups I suggest to adult students."),
 "speakers-for-keyboards": dict(
   answer="Powered studio monitors or powered bookshelf speakers, connected to your digital piano's line output, give it more body than built-in speakers. Check the inputs, and whether a listing is one speaker or a pair."),
 "piano-books-and-sheet-music": dict(title="Best Piano Books for Adults and Sheet Music Books",
   h1="Best Piano Books for Adults and Sheet Music Books",
   desc="Piano books for adults and sheet music books, chosen by a concert pianist who teaches adults: method books, theory, technique studies and classic editions.",
   answer="The best piano book for an adult beginner is one method written for adults, worked through in order; add theory and classic sheet music books beside it. Below are the methods and editions I would choose."),
 "practice-tools": dict(title="Piano Practice Tools: Metronomes, Stands, Journals",
   answer="Good piano practice needs a metronome, a stand that holds the page at eye level, a light and a practice record. These are the small practice tools I suggest to adult students, each described by its own listing."),
 "stand-lights": dict(title="Piano Lamps and Music Stand Lights for Reading Music",
   h1="Best Piano Lamps and Music Stand Lights",
   desc="Piano lamps and clip-on music stand lights for reading sheet music in the evening, chosen by a concert pianist who teaches adult beginners online.",
   answer="A good piano lamp or music stand light puts even, glare-free light across the whole page and attaches securely to your stand or music rest. These are the lights I suggest for evening practice."),
 "piano-care": dict(
   answer="Piano care at home comes down to three things: a dust cover for the keys, a hygrometer to watch the room's humidity and a polish made for your piano's finish. Here is what I would keep on hand."),
 "music-and-wellbeing": dict(
   answer="For people who live with music, the best gear is good listening gear: headphones, a turntable or speakers, plus a book on music and the brain. I make no medical claims; these simply help you listen."),
 "music-home-decor": dict(title="Piano Decor and Music-Themed Gifts for the Home",
   h1="Piano Decor and Music Gifts for the Home",
   desc="Piano decor and music-themed gifts for the home, chosen by a concert pianist: wall art, clocks, rugs, pillows, jewelry and small gifts for music lovers.",
   answer="The best piano decor is small and personal: wall art, a piano-key clock, a rug for the practice corner or a music-note blanket. Here are home gifts and jewelry for pianists and music lovers."),
 "luxury-gifts-for-pianists": dict(
   desc="Luxury gifts for pianists and serious music lovers, chosen by a concert pianist: reference headphones, great recordings and fine keepsakes.",
   intro="For a special occasion, the best gift for a musician is something that improves how they hear. I keep this list short on purpose. It holds reference-grade and wireless headphones, complete recordings by great pianists, a fountain pen and a few piano keepsakes, each described only by its own listing.",
   answer="The best luxury gift for a pianist improves how they hear: reference headphones, a complete box set of a great pianist's recordings, or a fine keepsake. I keep this list short on purpose."),
 "gifts-for-pianists": dict(title="Gifts for Pianists: Piano Gifts for Adults by Budget",
   desc="Gifts for pianists and piano gifts for adults, chosen by a concert pianist: small gifts, mid-sized gifts and special-occasion presents, by budget.",
   answer="The best gift for a pianist makes practice easier or listening better. Below are piano gifts for adults in three sizes, small, mid-sized and special-occasion, each chosen by a concert pianist."),
 "gifts-for-adult-beginners": dict(
   answer="Give an adult piano beginner the things that remove excuses: a keyboard with weighted keys, headphones for late practice, an adjustable bench, a light and a method book written for adults."),
 "gifts-for-piano-teachers": dict(title="Gifts for Music Teachers and Piano Teachers",
   h1="Gifts for Music Teachers and Piano Teachers", label="Gifts for Music Teachers",
   blurb="Thank-you gifts for a music or piano teacher.",
   desc="Gifts for music teachers and piano teachers, chosen by a piano professor: books, jewelry, music-themed gifts, listening gear and thank-you presents.",
   answer="A music teacher rarely wants something expensive. A good book, a piece of music jewelry, a music-themed mug or a good pair of headphones says you noticed, and a recording of your own playing says the most."),
}

# buyer-question H2s on category pages: (look, learn, pick, faq)
Q = {
 "digital-pianos": ("What should I look for in a digital piano?", "How does a digital piano help you learn?", "Which digital piano should I buy?", "What do adults ask before buying a digital piano?"),
 "keyboards": ("What should I look for in a keyboard?", "How does a keyboard help you learn piano?", "Which keyboard or MIDI controller should I buy?", "What do beginners ask about keyboards?"),
 "piano-benches-and-stands": ("What makes a good piano bench?", "How does the right bench help you play better?", "Which piano bench or stand should I buy?", "What do adults ask about piano benches?"),
 "piano-pedals": ("What should I look for in a sustain pedal?", "How does a real sustain pedal help you learn?", "Which sustain pedal should I buy?", "What do players ask about sustain pedals?"),
 "headphones-for-piano": ("What makes good headphones for piano?", "How do headphones help you practice?", "Which headphones should I buy for piano?", "What do players ask about piano headphones?"),
 "record-yourself-playing": ("What do I need to record myself playing?", "How does recording yourself help you learn?", "Which recording gear should I buy?", "What do students ask about recording?"),
 "speakers-for-keyboards": ("What should I look for in speakers for a digital piano?", "How do better speakers help you learn?", "Which speakers should I buy?", "What do players ask about keyboard speakers?"),
 "piano-books-and-sheet-music": ("What makes a good piano book for adults?", "How does the right book help you learn?", "Which piano books should I buy?", "What do adults ask about piano books?"),
 "practice-tools": ("What practice tools does a pianist need?", "How do practice tools help you learn?", "Which practice tools should I buy?", "What do students ask about practice tools?"),
 "stand-lights": ("What makes a good piano lamp or stand light?", "How does a good light help you read music?", "Which piano lamp should I buy?", "What do players ask about stand lights?"),
 "piano-care": ("What does a piano need to stay in good shape?", "How does piano care help you practice?", "Which piano care products should I buy?", "What do owners ask about piano care?"),
 "music-and-wellbeing": ("What makes good listening gear?", "How does listening help you learn piano?", "Which listening gear or book should I choose?", "What do music lovers ask?"),
 "music-home-decor": ("What makes a good piano gift for the home?", "How does a music corner help you practice?", "Which piano decor or gift should I choose?", "What do gift buyers ask about piano decor?"),
 "luxury-gifts-for-pianists": ("What makes a luxury gift worth it for a pianist?", "How does great listening gear help a pianist?", "Which luxury gift should I choose?", "What do buyers ask about luxury music gifts?"),
 "metronomes-and-tuners": ("What should I look for in a metronome?", "How does a metronome help you learn piano?", "Which metronome should I buy?", "What do students ask about metronomes?"),
 "music-stands": ("What should I look for in a music stand?", "How does a music stand help you practice?", "Which music stand should I buy?", "What do players ask about music stands?"),
}

RELATED = {
 "digital-pianos": ["piano-accessories", "piano-pedals", "piano-benches-and-stands"],
 "keyboards": ["digital-pianos", "piano-accessories", "headphones-for-piano"],
 "practice-tools": ["metronomes-and-tuners", "music-stands", "stand-lights"],
 "stand-lights": ["music-stands", "practice-tools", "piano-books-and-sheet-music"],
 "piano-books-and-sheet-music": ["practice-tools", "music-stands", "gifts-for-adult-beginners"],
 "music-home-decor": ["gifts-for-music-lovers", "stocking-stuffers-for-musicians", "luxury-gifts-for-pianists"],
 "luxury-gifts-for-pianists": ["gifts-for-music-lovers", "gifts-for-pianists", "headphones-for-piano"],
 "music-and-wellbeing": ["gifts-for-music-lovers", "headphones-for-piano", "music-home-decor"],
 "gifts-for-pianists": ["christmas-gifts-for-pianists", "stocking-stuffers-for-musicians", "gifts-for-music-lovers"],
 "gifts-for-adult-beginners": ["piano-accessories", "digital-pianos", "christmas-gifts-for-pianists"],
 "gifts-for-piano-teachers": ["gifts-for-music-lovers", "stocking-stuffers-for-musicians", "gifts-for-pianists"],
}

# ---------------------------------------------------------------- new category pages (explicit ASINs from products.json)
NEW_PAGES = [
 dict(slug="metronomes-and-tuners", cats=[], icon="⏱️", label="Metronomes and Tuners", blurb="Mechanical and digital metronomes.",
  asins=["B0B12CJC6G", "B07ZGMNLVW", "B000RVWVAY", "B0798NC7V9", "B0CSGYTQH4", "B000K19HYY", "B000ATOFS4"],
  h1="Best Metronomes for Piano Practice",
  title="Best Metronomes for Piano Practice, Plus Tuners",
  desc="Metronomes for piano practice, chosen by a concert pianist: mechanical and digital metronomes, tuner-metronome combos and a rhythm-training metronome.",
  answer="The best metronome for piano is the one you will switch on every day: a mechanical metronome if you want no screen at the piano, a digital one if you want memory and extra sounds. Tuner combinations suit homes with other instruments.",
  intro="Rhythm is the part of reading music that adults find hardest to fix alone, because a pulse that drifts feels steady from the inside. A metronome is the honest witness. I use it with students to check counting, not to chase speed, and the models below cover a classic mechanical metronome, simple digital ones and two tuner combinations, each described only by its own listing.",
  criteria=["<strong>A clear, audible click</strong> you can hear over the piano at a moderate volume.",
            "<strong>Easy tempo changes</strong>, because you will move the setting up and down every session.",
            "<strong>Mechanical or digital.</strong> A pendulum needs no screen; digital models add memory and extra sounds.",
            "<strong>A tuner as well</strong>, only if someone in the house plays a string or wind instrument.",
            "<strong>Power.</strong> Rechargeable, battery or wind-up: pick the one you will never have an excuse about."],
  faqs=[("Do I need a metronome to learn piano?", "Yes. A steady pulse is what makes written rhythm readable, and a metronome tells you honestly whether yours is steady. Use it to check your counting, then turn it off and keep the beat yourself."),
        ("Mechanical or digital metronome: which is better for piano?", "Neither plays better. A mechanical metronome such as the Wittner Taktell listed here needs no battery and has no screen. Digital models add memory, extra sounds or rhythm training, as their listings describe."),
        ("Is a metronome app on my phone enough?", "It works, but a phone at the piano brings messages with it. A separate metronome keeps practice time quiet, which is why I suggest one to adult students."),
        ("Do I need a tuner for a digital piano?", "No. A digital piano stays in tune. A tuner-metronome combination is useful when someone in the house also plays a string or wind instrument."),
        ("What tempo should I start at?", "Slow enough to play the passage without a single stop. Raise the setting a little only when it feels easy three times in a row.")],
  related=["practice-tools", "music-stands", "piano-books-and-sheet-music"]),

 dict(slug="music-stands", cats=[], icon="🎼", label="Music Stands", blurb="Folding, symphony and tablet stands.",
  asins=["B018FCZBMG", "B07WVVXXVX", "B083FPFZJG", "B0872TGQQT", "B07D5KK26W", "B0983DJGNN", "B08HYJ33RX", "B09LH19QQJ", "B0002FOBJY", "B09QM63SGR", "B0002E3AHE"],
  h1="Best Music Stands for Home Practice",
  title="Best Music Stands for Piano and Home Practice",
  desc="Music stands for home practice and lessons, chosen by a concert pianist: folding portable stands, Manhasset symphony stands and a tablet floor stand.",
  answer="The best music stand for home practice holds your music steady at eye level: a folding stand for small spaces and lessons away from home, or a Manhasset symphony stand for a permanent music corner.",
  intro="A piano has its own music rest, so why would a pianist buy a music stand? Because the rest is often too small for an open album, because a tablet score needs a steady holder, and because many adults also sing, accompany or practice away from the piano. I list folding stands, solid-desk symphony stands and a tablet floor stand, each described only by its own listing.",
  criteria=["<strong>Stability.</strong> The page should not move when you turn it.",
            "<strong>Height</strong> that brings the music to eye level, so your neck stays free.",
            "<strong>A solid desk or a wire frame.</strong> A solid desk holds a heavy album; a wire frame folds small.",
            "<strong>Portability</strong>, if you carry it to lessons or put it away after practice.",
            "<strong>Tablet support</strong>, if you read scores from an iPad."],
  faqs=[("Do I need a music stand if my piano has a music rest?", "Usually not for one book. A separate stand helps when the rest is too small for an open album, when you read from a tablet, or when you sing or practice another instrument."),
        ("What is the most stable kind of music stand?", "A solid-desk orchestral stand, such as the Manhasset models listed here, is built to stay put. Folding wire stands are lighter and easier to carry."),
        ("Which music stand suits a small apartment?", "A folding stand that packs away after practice. Several listings below describe folding or portable designs."),
        ("Can a music stand hold an iPad?", "A floor stand made for tablets, like the elitehood listing, holds a tablet at reading height. Check your tablet's size against the listing.")],
  related=["stand-lights", "metronomes-and-tuners", "practice-tools"]),
]
NEW_LEARN = {
 "metronomes-and-tuners": "How this helps you learn: steady counting. A metronome shows you where the pulse drifts, so the rhythm you read on the page becomes the rhythm you actually play.",
 "music-stands": "How this helps you learn: reading at eye level. A stand that holds the page steady keeps your neck free and your eyes on the music instead of on a sliding book.",
}

# ---------------------------------------------------------------- new guide pages
def _acc(pick, *_):
    return [("A sustain pedal", "The pedal is part of the instrument; start with a piano-style one.", pick(["B00063678K", "B00PNG4BV0", "B000OY0KWA"]), "sustain-pedal"),
            ("A bench at the right height", "Forearms level with the key tops, or slightly above.", pick(["B00I362NXU", "B0BRYJQTG5", "B0B5LZNWGM"]), "piano-bench"),
            ("Headphones for daily practice", "Closed-back for shared homes, wired for an instant response.", pick(["B00HVLUR18", "B00IT0IHOY", "B00HVLUR54"]), "headphones"),
            ("Light, rhythm and the page", "A lamp for the page, a metronome for the pulse, a clip for the book.", pick(["B0D3D5HTWR", "B081ZYJ76D", "B0CSGYTQH4", "B000K19HYY", "B07DK7PDFH"]), "light-rhythm-page"),
            ("Care for the keys", "A cover keeps dust off between practice sessions.", pick(["B09CT9R46T", "B07WCR5Y4B"]), "care")]

def _lovers(pick, *_):
    return [("For listening at home", "A record on in the evening is part of a musician's education.", pick(["B07N3XJ66N", "B07N3S4X3P", "B089T77WK2", "B0BW34LCB8", "B0D6WD2QSQ"]), "listening-at-home"),
            ("For listening on the go", "Noise-cancelling headphones for travel; open-back for a quiet room.", pick(["B0863TXGM3", "B0D4Z9C562", "B08J9MVB6W"]), "listening-on-the-go"),
            ("Books and great recordings", "Reading about music, and hearing it played at the highest level.", pick(["1400033535", "0452288525", "1324110589", "B0086WQNZ0", "B01I4CK604", "B08GRQ8SCB"]), "books-and-recordings"),
            ("For a music lover's home", "Small pieces of music for a shelf, a wall or a sofa.", pick(["B0063XLGN8", "B0D945K8FN", "B0C492J1DY", "B07RZLZLNN", "B0CVXMG4S8", "B094XTV5SZ"]), "music-lovers-home"),
            ("Small music gifts", "Easy to wrap, easy to give.", pick(["B01N8P8Q9Q", "B00NK40T9A", "B0DGNV226S", "B0CCP4888Z"]), "small-music-gifts")]

def _xmas(pick, *_):
    return [("Practical gifts a pianist will use every day", "The most welcome gifts disappear into daily practice.", pick(["B00IT0IHOY", "B00063678K", "B0D3D5HTWR", "B000K19HYY", "B00I362NXU"]), "practical-gifts"),
            ("Gifts for a pianist's ears", "Great recordings and headphones that let them through.", pick(["B08J9MVB6W", "B0086WQNZ0", "B01I4CK604", "B08GRQ8SCB"]), "gifts-for-the-ears"),
            ("Piano gifts for the home", "Keepsakes and a few festive touches.", pick(["B0063XLGN8", "B00X7GCQEM", "B004JIQV52", "B0C7GR2YKZ", "B0D945K8FN", "B09SV78JZQ", "B0DHKWX74F"]), "piano-gifts-for-the-home"),
            ("Hanukkah gifts for musicians: one for each night", "Eight small gifts, one for each night of Hanukkah.", pick(["B0DGNV226S", "B072JNCY6M", "B0768YHXFT", "B00QP5HMPA", "0793584744", "0452288525", "B092CQXTHT", "B01HDM6RRM"]), "hanukkah-gifts-for-musicians")]

def _stock(pick, *_):
    return [("For the piano bench", "Small things a pianist uses every week.", pick(["B07DK7PDFH", "B00QP5HMPA", "0793584744", "1441306595", "0881884995", "B0B12CJC6G", "B000RVWVAY"]), "for-the-piano-bench"),
            ("Wearable and pocket-size", "Socks, keychains and a little music jewelry.", pick(["B0CCP4888Z", "B072JNCY6M", "B0768YHXFT", "B0FG3HRM14", "B00NK40T9A", "B091DR14B4", "B07ZQ4S2BP"]), "wearable"),
            ("For the kitchen and the desk", "A touch of music for every day.", pick(["B0DGNV226S", "B09XMQ8L3N", "B01HDM6RRM", "B0063XLGN8", "B092CQXTHT"]), "kitchen-and-desk")]

_AFF = ("Are these affiliate links?", "Yes. As an Amazon Associate I earn from qualifying purchases, at no extra cost to you. I do not print prices; open the listing on Amazon to check today's price.")

NEW_GUIDES = {
 "piano-accessories": dict(category=True, gift=False, icon="🧰", label="Piano Accessories", blurb="Pedal, bench, headphones, light: the essentials.",
   title="Piano Accessories: What Every Digital Piano Needs",
   desc="The piano accessories a concert pianist says you actually need: a sustain pedal, an adjustable bench, headphones, a light, a metronome and a dust cover.",
   h1="Piano Accessories for Digital Pianos and Keyboards", eyebrow="Accessories",
   answer="The piano accessories you actually need are a piano-style sustain pedal, an adjustable bench, closed-back headphones and a light on the page. A metronome, a book clip and a dust cover come next.",
   intro_html="<p class=\"lead\">A new digital piano arrives with almost nothing around it, and that is where adults lose their first months: a chair that is too low, a switch pedal that feels like a doorbell, practice that stops when the house goes to sleep. The accessories below fix exactly those problems. Each is described only by its own listing, and each links to a deeper page in the shop.</p>",
   q_why="Why trust a concert pianist's list of accessories?", q_pick="Which piano accessories do I need first?", q_faq="What do new owners ask about piano accessories?",
   sections=_acc,
   faqs=[("What accessories do I need for a digital piano?", "A piano-style sustain pedal, an adjustable bench, closed-back headphones and a light for the page. Those four change how you practice. Everything else can wait."),
         ("Does a digital piano come with a pedal?", "Many include a small switch pedal and some include none. Check your listing, and plan to upgrade to a piano-style pedal for a more natural feel under the foot."),
         ("Do I need a stand for my keyboard?", "If it has no legs, yes, and the stand must not wobble. My benches and stands page explains what to look for."),
         ("Which piano accessories make good gifts?", "A stand light, a book clip, a metronome or headphones. Each is useful from the first week, and only the pedal has to suit a specific instrument."),
         ("Can I buy these accessories from outside the US?", "The links go to Amazon.com, and Amazon ships many items internationally. Check delivery to your country on the listing before you order.")],
   related=["piano-pedals", "piano-benches-and-stands", "headphones-for-piano"]),

 "gifts-for-music-lovers": dict(icon="🎶", label="Gifts for Music Lovers", blurb="Music gifts for adults who love to listen.",
   title="Gifts for Music Lovers: Music Gifts for Adults",
   desc="Gifts for music lovers and music gifts for adults, chosen by a concert pianist: turntables, headphones, great recordings, books and music-themed decor.",
   h1="Gifts for Music Lovers", eyebrow="Gift guide",
   answer="The best gifts for music lovers help them listen: a turntable, good headphones, a box set of great recordings or a book on music and the brain. For someone who has always wanted to play, give lessons.",
   intro_html="<p class=\"lead\">Some of the people who love music most have never played a note. For them I choose gifts that open the ears: a way to play records, headphones for a quiet hour, a recording I would want in my own collection, and a few small, cheerful things for the home.</p><p>If the music lover on your list has always wanted to play, give <a href=\"../gift-certificate.html\">online piano lessons</a> instead.</p>",
   q_why="Why trust a concert pianist's gift list?", q_pick="What do you give someone who loves music?", q_faq="What do people ask about gifts for music lovers?",
   sections=_lovers,
   faqs=[("What do you give someone who loves music but does not play?", "Something that helps them listen: a turntable, good headphones, a great recording or a book on how music works in the brain. If they have always wanted to play, give lessons."),
         ("What is a good music gift for adults?", "A complete box set of a great performer's recordings lasts for years. Glenn Gould's Bach is my first suggestion for anyone who loves the piano."),
         ("Are noise-cancelling headphones a good gift for a music lover?", "For travel and busy homes, yes. For piano practice I prefer wired studio headphones."),
         ("Can I give online piano lessons as a gift?", "Yes. A gift certificate for private online lessons with me suits a music lover who has always wanted to play, at any age."),
         _AFF],
   related=["music-and-wellbeing", "luxury-gifts-for-pianists", "music-home-decor"]),

 "christmas-gifts-for-pianists": dict(icon="🎄", label="Christmas Gifts for Pianists", blurb="Christmas picks, plus eight Hanukkah ideas.", gift_card=True,
   title="Christmas Gifts for Pianists, Plus Hanukkah Ideas",
   desc="Christmas gifts for pianists, chosen by a concert pianist: practical gear, great recordings, piano decor and eight Hanukkah gift ideas for musicians.",
   h1="Christmas Gifts for Pianists", eyebrow="Holiday gift guide",
   answer="The best Christmas gifts for pianists are things they will use: practice headphones, a piano-style pedal, a stand light, a great recording or a piano keepsake. Below are my picks, plus eight Hanukkah gifts for musicians.",
   intro_html="<p class=\"lead\">Every December, students ask me what to give the pianist in their family. My answer is always the same: something that disappears into daily practice, or something that makes listening a pleasure. Below are practical gifts, gifts for the ears, piano keepsakes for the home and, for families who celebrate Hanukkah, eight small gifts for eight nights.</p>",
   q_why="Why trust a concert pianist's Christmas list?", q_pick="What should I give a pianist for Christmas?", q_faq="What do holiday shoppers ask?",
   sections=_xmas,
   faqs=[("What is a good Christmas gift for a pianist?", "Something they will use every day: practice headphones, a piano-style sustain pedal, a stand light or a metronome. For a pianist who has everything, a box set of great recordings."),
         ("What are good Hanukkah gifts for musicians?", "Small gifts for each night work well: music coasters, music socks, a piano keychain, a page clip, a practice journal, a book on music and the brain, a crystal music note and a musician's mug. They are listed together above."),
         ("When should I order Christmas gifts from Amazon?", "Earlier than you think. Delivery dates appear on each Amazon listing, and they move as December fills up."),
         ("What if I would rather give lessons?", "A gift certificate for online lessons with me works for any level. Gift certificates bought by December 31 keep today's lesson price."),
         _AFF],
   related=["stocking-stuffers-for-musicians", "gifts-for-pianists", "gifts-for-music-lovers"]),

 "stocking-stuffers-for-musicians": dict(icon="🧦", label="Stocking Stuffers for Musicians", blurb="Small gifts for pianists and music students.",
   title="Stocking Stuffers for Musicians and Pianists",
   desc="Stocking stuffers for musicians and piano players, chosen by a concert pianist: book clips, practice journals, metronomes, music socks and small gifts.",
   h1="Stocking Stuffers for Musicians", eyebrow="Holiday gift guide",
   answer="Good stocking stuffers for musicians are small and useful: a clip that holds a book open, a practice journal, a pocket metronome, music socks or a piano keychain. These are the small gifts I would give.",
   intro_html="<p class=\"lead\">The best small gifts for a musician are the ones they reach for every week. A clip that keeps a new book open on the music rest, a journal for practice notes, a metronome that fits in a bag: none of them costs much attention to choose, and all of them get used. I add a few cheerful music-themed pieces for fun.</p>",
   q_why="Why trust a concert pianist's list of small gifts?", q_pick="What fits in a musician's stocking?", q_faq="What do people ask about stocking stuffers for musicians?",
   sections=_stock,
   faqs=[("What are good stocking stuffers for musicians?", "Small things used every week: a book clip, a practice journal, manuscript paper, a pocket metronome, music socks or a keychain."),
         ("What is a good small gift for a piano student?", "A practice record journal or a clip that keeps the book open on the music rest. Both help practice from the first day."),
         ("What small gift suits a music teacher?", "A music mug, coasters, or music-note earrings or cufflinks: small, personal and easy to give at the last lesson before the holidays."),
         ("How do I check the price?", "Open the listing on Amazon. Prices change often, so I do not print them here."),
         _AFF],
   related=["christmas-gifts-for-pianists", "gifts-for-piano-teachers", "music-home-decor"]),
}

EXTRA_GUIDE_FAQ = {
 "gifts-for-pianists": ("What do you get a pianist who has everything?", "A box set of a great pianist's recordings, a reference pair of headphones or online lessons. Few pianists own every recording they love."),
 "gifts-for-adult-beginners": ("What is the best first gift for an adult learning piano?", "A keyboard with weighted keys if they have none; otherwise closed-back headphones and an adjustable bench. Those three make daily practice possible."),
 "gifts-for-piano-teachers": ("What is a good gift for a music teacher with many students?", "Something they use at work: a music mug, a stand light for the studio, a music-note bracelet or a book on music and the brain."),
}
GUIDE_Q = {
 "gifts-for-pianists": ("Why trust a concert pianist's gift list?", "Which gift should I give a pianist?", "What do gift buyers ask?"),
 "gifts-for-adult-beginners": ("Why trust a teacher of adults?", "What should I give an adult who is learning piano?", "What do gift buyers ask about adult beginners?"),
 "gifts-for-piano-teachers": ("Why trust a piano professor's list?", "What can I give my music teacher?", "What do students ask about teacher gifts?"),
}

def _teacher_sections(orig):
    def f(pick, gift_pool, band_sections):
        s = orig(pick, gift_pool, band_sections)
        jew = ("Jewelry a music teacher will wear", "Recital and thank-you jewelry with a musical motif.",
               pick(["B00NMRZPFS", "B0BM7HHBZ4", "B01CKN37FE", "B01N8P8Q9Q"]))
        return [s[0], jew] + list(s[1:])
    return f

ARTICLE_H2 = [("<h2>Start with the keys, not the features</h2>", "<h2>Which matters most: the keys or the features?</h2>"),
              ("<h2>Then the sound, the pedal and the furniture</h2>", "<h2>What about the sound, the pedal and the furniture?</h2>"),
              ("<h2>Eighty-eight keys or fewer?</h2>", "<h2>Do I need 88 keys or fewer?</h2>"),
              ("<h2>Picks by budget</h2>", "<h2>Which digital piano fits my budget?</h2>"),
              ("<h2>My advice in order</h2>", "<h2>What should I do first, in order?</h2>")]
DEPTH_H2 = {"A teacher's guide to choosing a digital piano": "How do I choose a digital piano?",
            "A teacher's guide to keyboards and controllers": "Keyboard or MIDI controller: which do I need?",
            "A teacher's guide to practice headphones": "How do I choose headphones for piano practice?",
            "A teacher's guide to recording yourself": "How do I record myself playing piano?"}


def apply(PAGES, GUIDES, HUB, ARTICLE, D):
    """Merge this layer into the content modules (in place). Idempotent per process."""
    if getattr(apply, "done", False):
        return
    apply.done = True
    for pg in NEW_PAGES:
        PAGES.append(pg)
    for pg in PAGES:
        pg.update(META.get(pg["slug"], {}))
        if pg["slug"] in RELATED:
            pg["related"] = RELATED[pg["slug"]]
        pg["q"] = Q[pg["slug"]]
    D.LEARN.update(NEW_LEARN)
    for k, v in list(D.DEPTH.items()):
        for a, b in DEPTH_H2.items():
            v = v.replace("<h2>%s</h2>" % a, "<h2>%s</h2>" % b)
        D.DEPTH[k] = v
    for slug, g in GUIDES.items():
        g.update(META.get(slug, {}))
        if slug in RELATED:
            g["related"] = RELATED[slug]
        if slug in EXTRA_GUIDE_FAQ:
            g["faqs"] = [EXTRA_GUIDE_FAQ[slug]] + list(g["faqs"])
        if slug in GUIDE_Q:
            g["q_why"], g["q_pick"], g["q_faq"] = GUIDE_Q[slug]
    GUIDES["gifts-for-piano-teachers"]["sections"] = _teacher_sections(GUIDES["gifts-for-piano-teachers"]["sections"])
    GUIDES.update(NEW_GUIDES)
    HUB.update(META["index"])
    for a, b in ARTICLE_H2:
        ARTICLE["html_before"] = ARTICLE["html_before"].replace(a, b)
        ARTICLE["html_after"] = ARTICLE["html_after"].replace(a, b)


# ---------------------------------------------------------------- "I suggest it for ..." on every card
def _has(s, *words):
    return any(w in s for w in words)

def who_for(p):
    """Who the product suits, in her voice. Built from category, our type mapping and the listing title/reason only."""
    t = (p["title"] + " " + p["reason"]).lower()
    c = p["category"]
    ty, label = SI.type_of(p)
    tier = p["tier"]
    if c in ("digital-pianos", "acoustic-and-hybrid-pianos"):
        if "semi-weighted" in t: return "a first budget for an adult beginner, with a plan to move to fully weighted keys later."
        if ty == "digital-piano-console": return "a returning player, or a family that wants the piano to sit in the room like furniture."
        if "compact" in t: return "an adult beginner in a small apartment who still wants 88 keys."
        if "bluetooth" in t: return "an adult beginner who practices with apps on a phone or tablet."
        if tier in ("premium", "luxury"): return "a returning player who wants a better touch to grow into for years."
        if tier == "mid": return "an adult beginner who wants to buy once and keep it."
        return "an adult beginner on a careful first budget who still wants 88 keys."
    if ty == "midi-controller":
        if "25" in t: return "making music on a laptop or tablet; it is a tool, not a piano for building technique."
        return "a learner who records or composes on a computer and wants keys to play into."
    if c == "portable-keyboards":
        if "88" in t: return "a small apartment, or a player who moves the instrument from room to room."
        if "electric piano" in t: return "a returning player who wants a small electric piano for a desk or a trip."
        if "learning" in t: return "a parent or grandparent who is curious about music and wants built-in learning tools."
        if "touch" in t: return "an adult testing the waters before buying a digital piano."
        return "a first try at the keys when space or budget is tight."
    if c == "benches-and-stands":
        if "duet" in t: return "a teacher sitting beside a student, or two people in the family who play together."
        if "stand and bench" in t or "bench set" in t: return "setting up a first keyboard corner in one purchase."
        if ty == "keyboard-stand":
            if "fp-10" in t or "fp10" in t: return "an owner of the Roland FP-10 who wants the matching stand."
            return "a keyboard without legs that must stay still when you play with the weight of the arm."
        if "adjustable" in t and "storage" in t: return "a home where more than one person plays, with books kept under the seat."
        if "adjustable" in t: return "a home where more than one person plays, so each can set their own height."
        if "fixed" in t: return "a single player whose height it already suits."
        if "storage" in t: return "a student who wants method books within reach of the bench."
        return "an adult beginner replacing a dining chair that sits too low."
    if c == "pedals":
        if "pedal unit" in t: return "the owner of a digital piano built to accept a three-pedal unit."
        if "foot switch" in t: return "a spare or second pedal; for daily playing I prefer a piano-style pedal."
        if _has(t, "real-feel", "half"): return "a returning player who wants finer pedaling on an instrument that supports it."
        if _has(t, "piano-style", "piano style", "fc4a"): return "any beginner whose keyboard came with a small square switch pedal."
        return "a beginner adding a sustain pedal to a keyboard for the first time."
    if ty == "headphones":
        if _has(t, "noise cancel", "noise-cancel", "quietcomfort") or re.search(r"\banc\b", t): return "listening on a plane, a train or in a busy home, rather than piano practice."
        if _has(t, "wireless", "bluetooth"): return "music listening away from the piano; for practice I prefer a cable."
        if _has(t, "open-back", "open back", "reference", "audiophile"):
            if tier in ("luxury",) or c == "luxury-gifts": return "a serious listener, or a pianist who practices alone in a quiet room."
            return "practicing alone, when you want the most natural piano sound."
        if "semi-open" in t: return "practicing alone or with one quiet listener nearby."
        if "closed" in t: return "late practice in an apartment or a shared home."
        return "an adult who practices daily and wants an honest sound for recording later."
    if ty == "usb-microphone": return "recording yourself on a computer to send me a clip for feedback."
    if ty == "audio-interface": return "a student ready to grow a home recording setup with other microphones."
    if ty == "handheld-recorder": return "recording a whole practice session or lesson without a computer."
    if ty == "wireless-mic": return "speaking to the camera, as a teacher or a performer introducing a piece does."
    if ty == "webcam": return "online lessons on a laptop or desktop computer."
    if label == "Overhead phone mount" or "overhead" in t: return "filming your hands on the keys for a teacher."
    if ty == "ring-light": return "filming lessons or performances in a dim room."
    if ty == "phone-tripod": return "a phone beside the keyboard for a first recording."
    if ty == "turntable": return "a music lover with a record collection, or one who is starting one."
    if ty == "studio-speakers":
        if _has(t, "echo dot", "sonos", "smart speaker"): return "streaming music around the house; it is not a monitor for a piano."
        if _has(t, "portable", "waterproof", "soundlink"): return "music on the go; it is not a speaker for a digital piano."
        if "pair" in t: return "a digital piano in a living room that needs full stereo sound."
        if "monitor" in t: return "a desk setup where you want to hear your own touch clearly."
        return "playing for family in the living room."
    if ty == "singing-bowl": return "a quiet moment of listening before or after practice."
    if c in ("method-books", "books-for-music-lovers") or (c == "music-wellbeing" and ty == "wellbeing"):
        if _has(t, "brain", "musicophilia", "secret chord"): return "a music lover who reads, or a teacher's bookshelf."
        if "theory" in t: return "a learner who wants to understand what they are reading, page by page."
        if "junior hanon" in t: return "short daily finger exercises once reading is under way."
        if _has(t, "hanon", "virtuoso pianist", "op. 599", "velocity", "dexterity", "czerny"): return "a returning player rebuilding finger technique, once reading is comfortable."
        if _has(t, "progressive pieces", "sonatina"): return "a student finishing a first method book and ready for real pieces."
        if "first book of chopin" in t: return "an adult who dreams of Chopin and wants a way in at an easier level."
        if _has(t, "chopin", "bach", "beethoven", "nocturne", "waltz", "etude", "sonata", "well-tempered"): return "a returning player who wants the real repertoire in a good edition."
        if _has(t, "book 2", "classics", "books set"): return "an adult who has finished a first method book and wants the next step."
        if _has(t, "adult", "all-in-one", "for adults"): return "an adult beginner starting from the very first page."
        return "an adult learner building a small home music library."
    if ty == "metronome":
        if _has(t, "taktell", "mechanical"): return "a player who wants no screen at the piano, only a steady beat."
        if "rhythm coach" in t: return "a returning player or a teacher who wants rhythm training built in."
        if "tuner" in t: return "a home where someone also plays a string or wind instrument."
        if "memory" in t: return "a student who keeps several practice tempos for different pieces."
        if "rechargeable" in t: return "an adult beginner who wants a simple beat and no batteries to buy."
        return "a beginner learning to count steadily."
    if ty == "page-turner": return "reading scores from a tablet with both hands on the keys."
    if ty == "music-stand":
        if "manhasset" in t: return "a teacher's studio or a serious home music room."
        if _has(t, "ipad", "tablet"): return "reading music from a tablet at eye level."
        if _has(t, "portable", "folding", "2 in 1", "dual-use"): return "lessons away from home, or a small apartment where it folds away after practice."
        return "a home practice corner."
    if ty == "stand-light":
        if label == "Piano lamp": return "reading music at an upright or digital piano in the evening."
        if label == "Clamp lamp": return "a desk, or a digital piano with an edge to clamp it to."
        if "orchestra" in t: return "a music stand in a dim room or at an evening rehearsal."
        if _has(t, "wide", "88-led", "81 led", "81-led"): return "lighting a wide open album, two pages at once."
        if "rechargeable" in t: return "evening practice without a cable across the piano."
        return "evening practice from a printed book."
    if label == "Manuscript paper" or "manuscript paper" in t: return "a student learning to write notes and rhythms by hand."
    if label == "Music journal" or _has(t, "journal", "practice record"): return "an adult beginner building a daily practice habit."
    if c == "sheet-music-holders" or label == "Sheet music accessory":
        if _has(t, "clip", "bookmark", "page holder"): return "keeping a new method book open on the music rest."
        return "a student carrying music to lessons and keeping pages in order."
    if c == "piano-care":
        if "cover" in t: return "a keyboard that stays out in a living room between practice sessions."
        if "hygrometer" in t: return "an acoustic piano owner who wants to see what the room's humidity does through the seasons."
        if "humidifier" in t: return "an owner of a piano humidity-control system that uses these pads."
        return "the owner of a gloss-finish acoustic piano."
    if ty == "jewelry":
        if "cufflink" in t: return "a pianist dressing for a recital or a concert."
        if "teacher" in t: return "a thank-you to a music teacher at the end of the year."
        return "a recital gift for a student, or a birthday gift for a pianist."
    if label in ("Socks", "Small gift") or _has(t, "keychain", "key chain", "magnet", "coaster"):
        return "a stocking stuffer for a student, a teacher or a whole studio."
    if label == "Mug": return "a teacher's desk or a student's practice break."
    if ty == "textile":
        if label == "Tote bag": return "carrying books to lessons."
        if label == "Rug": return "a practice corner at home."
        return "a gift for a parent or grandparent who loves music."
    if ty == "wall-art" or label in ("Wall clock", "Bookends"): return "decorating a practice corner or a music room at home."
    if label == "Recording box set": return "a pianist building a library of great recorded playing."
    if label == "Fountain pen": return "a composer, or a teacher who still writes by hand."
    if ty == "grand-piano" or label == "Figurine":
        if "puzzle" in t: return "an adult who loves building things by hand."
        return "a grandparent who played as a child, or a student's first recital."
    if label == "Kalimba": return "a music lover who does not play yet and wants something to try."
    if label == "Night light": return "a gift for a music lover's bedside."
    return "a music lover on your gift list."
