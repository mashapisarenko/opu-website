# -*- coding: utf-8 -*-
"""Pianos department layer for the OPU affiliate shop (added 2026-11-14).

New category pages built from _shop/products.json (digital pianos by type, hybrid and digital grand pianos, stage pianos,
microphones and interfaces, keyboard cases), the pianos hub, the "Start here" path, the international FAQ, and small
patches (display name and "I suggest it for" line can come from the product record).
Every product fact comes from the listing text recorded in products.json on 2026-11-14. No prices, ratings or images.
"""
import re
import shop_illus as SI

INTL_FAQ = ("Shopping outside the US? Do these links work in the UK, Canada, Australia or Europe?",
            "Yes. The links go to Amazon.com and open your local Amazon store when the model is sold there: the UK, Canada, Australia, Germany, France, Italy, Spain, the Netherlands, Poland, Sweden and Singapore. "
            "Models, voltages and plugs differ by country, so on your local listing check for the 230-volt or UK-plug version of a digital piano or a suitable mains adapter, and check that the "
            "sustain pedal, bench (keyboard stool) or keyboard stand you want is sold in your country. If a model is not sold locally, the page will say so.")

# ------------------------------------------------------------------ patches
def patch(N, S):
    _short = N.short_name
    N.short_name = lambda p: p.get("short") or _short(p)
    _who = S.who_for
    S.who_for = lambda p: p.get("who") or _who(dict(p, category="digital-pianos") if p["category"] in ("digital-pianos-home", "hybrid-digital-pianos", "stage-pianos") else p)
    N.CAT_GROUP.update({"digital-pianos-home": "home", "hybrid-digital-pianos": "hybrid", "stage-pianos": "stage",
                        "arranger-keyboards": "keyboard", "microphones-interfaces": "record", "cases-and-covers": "case"})
    N.LENS.update({
        "home": ["Measure the wall before you fall for the cabinet.", "The keys and the pedals matter more to me than the finish of the cabinet.", "A piano you can see from the sofa is a piano you will play.", "Check whether a bench comes with it."],
        "hybrid": ["At this level I listen to how the key returns, not to the list of sounds.", "Try the touch before you commit, because no listing replaces your hands.", "A serious touch deserves a good bench and a good pedal.", "It is an investment, so I would hear it in a shop first."],
        "stage": ["Check whether it has speakers, because many stage pianos have none.", "I look at the action first and the extra sounds second.", "You will also need a stand and a pedal.", "It suits playing out more than first lessons."],
        "case": ["Measure your keyboard against the inside size before you order.", "A good case protects an instrument you have already paid for.", "Padding matters more to me than pockets.", "Think about how you will carry it before you buy."]})
    rules = [
        (r"^digital-pianos-home$", r"", "digital-piano-console", None),
        (r"^hybrid-digital-pianos$", r"GP-3|DG30", "grand-piano", "Digital grand piano"),
        (r"^hybrid-digital-pianos$", r"", "digital-piano-console", "Wooden-key digital piano"),
        (r"^stage-pianos$", r"", "digital-piano-portable", "Stage piano"),
        (r"^arranger-keyboards$", r"", "keyboard-61", "Arranger keyboard"),
        (r"^headphones$", r"", "headphones", None),
        (r"^microphones-interfaces$", r"recorder|H6|H1 |DR-0|DR-4", "handheld-recorder", None),
        (r"^microphones-interfaces$", r"interface|Volt|UR22|M-Track", "audio-interface", None),
        (r"^microphones-interfaces$", r"MV88", "wireless-mic", "Phone microphone"),
        (r"^microphones-interfaces$", r"", "usb-microphone", "Microphone"),
        (r"^cases-and-covers$", r"", "piano-care", "Keyboard case"),
    ]
    SI._RULES[0:0] = [(re.compile(c, re.I), re.compile(t, re.I), ty, lab) for c, t, ty, lab in rules]
    for ty, lab in (("handheld-recorder", None),):
        pass

# ------------------------------------------------------------------ new category pages
FAQ_OUT = None

PAGES = [
 dict(slug="home-digital-pianos", cats=["digital-pianos-home"], icon="🏠", label="Home Digital Pianos",
  blurb="Console and upright-style pianos for the living room.",
  h1="Best Home Digital Pianos: Console and Upright-Style Models",
  title="Best Home Digital Pianos: Console and Upright Style",
  desc="Console and upright-style digital pianos for adults who want a piano corner at home, chosen by a concert pianist: Yamaha, Kawai, Casio, Roland, Korg.",
  answer="The best home digital piano for an adult has 88 weighted keys in a cabinet with its own stand and three pedals, and it should stand in the room like furniture. These console and upright-style models are my picks, from the Yamaha Arius to Kawai and Roland cabinets.",
  intro="A home digital piano is the one I picture when a student tells me they want a piano in the living room and not a keyboard on a stand. The cabinet carries its own pedals and keeps the instrument steady, the keys are weighted, and the whole thing looks like part of the house. It costs more than a portable, and it is the instrument I would buy once and keep. Each note below is based on what the listing states.",
  criteria=["<strong>Weighted, graded hammer keys.</strong> The touch is what you practice, so this comes first.",
            "<strong>Three pedals in the cabinet</strong>, because the pedal is part of a piano and a cabinet should include it.",
            "<strong>The room.</strong> Measure the wall. Compact upright-style cabinets exist for small apartments.",
            "<strong>A real piano sound</strong> with a headphone jack, so you can practice late.",
            "<strong>A bench in the price or in the budget.</strong> Check whether the listing includes one."],
  faqs=[("Is a console digital piano better than a portable one?", "Not better in sound, but better in furniture. A console has its own stand and pedals and stays put, which suits a home. A portable moves easily, which suits a small flat or a player who travels."),
        ("Do home digital pianos include a bench?", "Some listings include one and some do not. Read the listing, and plan for an adjustable bench if it is not included."),
        ("How wide is a digital piano cabinet?", "Most are about the width of an 88-key keyboard plus the cabinet sides. Check the dimensions on the listing against your wall before you order."),
        ("Can I use headphones with a home digital piano?", "Yes. Digital pianos have a headphone jack, which is the main reason many adults choose them over an acoustic piano in an apartment.")],
  related=["digital-pianos", "hybrid-and-digital-grand-pianos", "piano-benches-and-stands"]),

 dict(slug="hybrid-and-digital-grand-pianos", icon="🎼", label="Digital Grand and Wooden-Key Pianos",
  asins=["B0CJ5NPG1M", "B0FL3G4S3D", "B0CQCV986L", "B0C6BVT77Q", "B0FTRF67DM", "B0CSMM5M1Z", "B0D15QXV5B", "B0BSKN3HNT"],
  blurb="Wooden-key console and grand-style digital pianos.",
  h1="Digital Grand and Wooden-Key Pianos: Premium to Luxury",
  title="Digital Grand and Wooden-Key Pianos for Players",
  desc="Wooden-key digital pianos and digital grands, chosen by a concert pianist for returning and advanced players: Kawai, Roland, Casio and Yamaha.",
  answer="A wooden-key digital piano gives the closest touch to an acoustic piano that still has a volume control, and a digital grand puts a digital piano inside a grand-piano shape. A true hybrid, with a real hammer action, is a different instrument: I could not verify one sold by its maker or an authorized dealer on Amazon, so this page lists the wooden-key and digital-grand models I can.",
  intro="At this level the keys matter more than the sound. These pianos have long wooden-style keys and a graded hammer action, and the sound is made electronically so that you can use headphones. A digital grand goes one step further in appearance. True hybrid pianos, such as the Yamaha AvantGrand and N-series, the Kawai Novus and the Casio Celviano Grand Hybrid, add a real hammer mechanism; on November 14, 2026 I could not find them on Amazon sold by their maker or an authorized dealer, so for those I suggest a piano dealer. These are instruments for a returning player who knows what a good touch is, and they are an investment. I list what each listing states and leave the rest to your hands in a shop.",
  criteria=["<strong>Wooden keys or a hammer mechanism</strong> that the listing names, because that is what separates this class from a portable.",
            "<strong>Key length and weight.</strong> Longer keys, as on a grand, give you more control of soft playing.",
            "<strong>Triple pedals</strong>, including a soft pedal and a middle pedal, which advanced repertoire uses.",
            "<strong>Where it will stand.</strong> A digital grand needs the floor space of a small grand.",
            "<strong>Honest priorities.</strong> Try the touch in a shop if you can, because no description replaces your own hands."],
  faqs=[("What is a hybrid piano?", "A piano that combines an acoustic-style keyboard mechanism, often with wooden keys and hammers, with an electronic sound source. You get the touch of a piano and the convenience of headphones and no tuning."),
        ("Is a digital grand piano worth the money?", "It is worth it when you want the look and the footprint of a grand and the volume control of a digital. If you only need the touch, a wooden-key upright-style or portable hybrid gives you that for less."),
        ("Can I buy a true hybrid piano on Amazon?", "On November 14, 2026 I searched for the Yamaha AvantGrand and N-series, the Kawai Novus and the Casio Celviano Grand Hybrid and could not verify any as sold by the maker or an authorized dealer. The pianos on this page are wooden-key digital pianos and digital grands, which are not hybrids. For a hybrid, visit a piano dealer and play it first."),
        ("Do I need a hybrid piano as an adult beginner?", "No. A good digital piano with weighted keys is enough for the first years. I would consider a hybrid when you are returning after a long break or working on advanced repertoire."),
        ("Can I buy an acoustic upright or grand piano on Amazon?", "I searched Amazon by brand and model for uprights and grands on November 14, 2026 and found digital instruments and accessories, but no acoustic piano I could verify as sold and shipped there. A real piano should be played, delivered by movers and tuned, so I suggest a local piano dealer.")],
  related=["home-digital-pianos", "stage-pianos", "headphones-for-piano"]),

 dict(slug="stage-pianos", cats=["stage-pianos"], icon="🎹", label="Stage Pianos",
  blurb="88-key weighted keyboards for gigs and serious home practice.",
  h1="Best Stage Pianos: Weighted 88-Key Keyboards",
  title="Best Stage Pianos: 88-Key Weighted Keyboards",
  desc="Stage pianos and 88-key weighted keyboards for performing pianists and serious home players, chosen by a concert pianist: Roland, Yamaha, Korg, Nord.",
  answer="A stage piano is an 88-key weighted keyboard built to be played through an amplifier or a mixer, and it suits a pianist who plays out or who wants one instrument for piano and other sounds. Most beginners need a digital piano with speakers instead.",
  intro="A stage piano is a different tool from a home digital piano. It is built to be carried, to connect to an amplifier or a mixer, and to give a performer many sounds. Some have no speakers at all. I include them because adults who return to piano sometimes want to play in a band, in church or at a party, and because a few of these keyboards have excellent actions. The notes below follow each listing.",
  criteria=["<strong>The action.</strong> Weighted 88-key actions are the point of the category.",
            "<strong>Speakers or no speakers.</strong> Many stage pianos have none, so plan for headphones or an amplifier.",
            "<strong>Sounds beyond the piano.</strong> Electric piano, organ and synthesizer sounds suit a band, not practice.",
            "<strong>Weight and size</strong> if you will carry it.",
            "<strong>Pedal and stand.</strong> You need both, and a sustain pedal is often included."],
  faqs=[("What is the difference between a stage piano and a digital piano?", "A stage piano is made for performing and is often without speakers; a home digital piano is made for a living room, with speakers, a stand and pedals."),
        ("Do I need a stage piano as a beginner?", "No. An adult beginner is better served by a digital piano with speakers and a stand. Choose a stage piano if you plan to perform with a band."),
        ("Can I practice on a stage piano with headphones?", "Yes, if it has a headphone output, which the listings below describe. Check the jack size and bring an adapter if needed."),
        ("What else do I need with a stage piano?", "A stand, a sustain pedal, headphones or an amplifier, and a bench at the right height. My other shop pages cover each.")],
  related=["hybrid-and-digital-grand-pianos", "piano-pedals", "piano-benches-and-stands"]),

 dict(slug="microphones-and-audio-interfaces", cats=["microphones-interfaces", "recording-microphones-audio"], icon="🎙️", label="Microphones and Interfaces",
  blurb="Microphones, recorders and interfaces for recording piano.",
  h1="Best Microphones and Audio Interfaces for Recording Piano",
  title="Best Microphones and Interfaces to Record Piano",
  desc="Microphones, handheld recorders and USB audio interfaces for recording piano at home, chosen by a concert pianist who records and teaches online.",
  answer="To record a piano well you need a pair of small-diaphragm condenser microphones and a USB audio interface, or a handheld stereo recorder if you want something simpler. A digital piano can also be recorded with a cable from its output.",
  intro="Recording is the quickest way to hear yourself as a listener does, and it is how an adult learner sends a clip for feedback. A phone is enough to begin. When you want a better sound, there are three paths: a handheld recorder that does everything in one box, a USB microphone that plugs into a computer, or a pair of condenser microphones through an audio interface. I list each by what its listing states.",
  criteria=["<strong>Your instrument.</strong> An acoustic piano needs microphones; a digital piano can connect by cable.",
            "<strong>Stereo.</strong> A matched pair of microphones, or a stereo recorder, gives a piano its width.",
            "<strong>Simplicity.</strong> A handheld recorder is the easiest path to a clean clip.",
            "<strong>Interface inputs.</strong> Count the XLR inputs you need, and whether the microphone needs phantom power.",
            "<strong>Software.</strong> Some interfaces include recording software."],
  faqs=[("What do I need to record piano at home?", "A recorder or microphones for sound, and a phone or a camera for video. Begin with a handheld recorder or a USB microphone, then add an interface and a pair of condensers when you are recording every week."),
        ("What is an audio interface?", "A box that turns the signal of a microphone or instrument into digital audio for your computer, and sends the sound back to your headphones. It lets you use professional XLR microphones."),
        ("Do I need two microphones for piano?", "Two, as a matched pair, give a stereo image, which is how most pianists want a piano recorded. One microphone works for a simple clip."),
        ("Can I send a recording to my teacher?", "Yes. A clear clip is all I need for feedback, and my feedback is free: send me a video of your playing.")],
  related=["record-yourself-playing", "headphones-for-piano", "speakers-for-keyboards"]),

 dict(slug="keyboard-cases-and-covers", icon="🧳", label="Keyboard Cases and Covers",
  asins=["B09N98T135", "B0H6W9WQR7", "B0CJ57LXQS", "B0F9FD8XRR", "B0CH3SRHN7", "B0H45SRN1D", "B09CT9R46T", "B07PLV8MYY"],
  blurb="Gig bags, rolling cases, flight cases and dust covers.",
  h1="Keyboard Cases, Gig Bags and Dust Covers for 88-Key Pianos",
  title="Keyboard Cases, Gig Bags and Piano Dust Covers",
  desc="Gig bags, rolling cases, flight cases and dust covers for 88-key keyboards and portable digital pianos, chosen by a concert pianist who teaches adults.",
  answer="Match the case to the trip: a padded gig bag for lessons across town, a rolling case for regular moves, a hard flight case for air travel, and a dust cover for a keyboard that stays at home.",
  intro="A portable digital piano is only portable if you can carry it safely. A padded bag protects it on the way to a lesson, a hard case protects it in a car or a plane, and a cover keeps dust off the keys at home. I list each by what its listing states, and I ask you to check the inside size against your own keyboard before you order.",
  criteria=["<strong>The inside dimensions.</strong> Compare them with your keyboard, not just its key count.",
            "<strong>Padding and straps</strong> for a bag you will carry on your back.",
            "<strong>Wheels and latches</strong> for a case you will roll or ship.",
            "<strong>A cutout for the music stand</strong> on a dust cover, if you leave the stand on.",
            "<strong>Where it lives.</strong> A cover for the living room, a case for the car."],
  faqs=[("How do I know if a case fits my keyboard?", "Measure your keyboard's length, width and height and compare them with the interior size on the listing. Key count alone is not enough, because cabinets differ."),
        ("Gig bag or hard case?", "A gig bag is lighter and cheaper to carry to lessons. A hard case protects better for air travel and frequent moves."),
        ("Do I need a dust cover?", "If your keyboard stays out in a room, yes. Dust works into keys over time, and a cover is the simplest protection."),
        ("Can I fly with a digital piano?", "A hard flight case with foam and latches is built for transport, but check your airline's rules for size and weight before you book.")],
  related=["piano-care", "piano-accessories", "digital-pianos"]),
]

META_UPDATES = {
 "digital-pianos": dict(cats=["digital-pianos"],
   intro="A digital piano is the practical way for most adults to begin: it stays in tune, it has a volume control, and it fits in a living room. I teach adult beginners, and the first thing I check is the keys, because the way a key answers your hand is what you are really practicing. This page covers portable 88-key digital pianos from a careful first budget to premium models. For furniture-style cabinets, wooden-key hybrids and stage pianos, use the links in the piano department below.",
   related=["home-digital-pianos", "hybrid-and-digital-grand-pianos", "piano-pedals"]),
 "keyboards": dict(cats=["portable-keyboards", "arranger-keyboards", "midi-controllers"],
   intro="Not every adult needs a full digital piano on day one. A compact keyboard can be the right first step when space or budget is tight, an arranger keyboard suits someone who wants to play with a band-style accompaniment, and a MIDI controller suits someone who practices with apps or music software. I look at key count and touch response first, and I say plainly what each instrument is for."),
}

Q_NEW = {
 "home-digital-pianos": ("What should I look for in a home digital piano?", "How does a home digital piano help you learn?", "Which home digital piano should I buy?", "What do adults ask before buying a home digital piano?"),
 "hybrid-and-digital-grand-pianos": ("What should I look for in a wooden-key or digital grand piano?", "How does a wooden-key piano help you learn?", "Which wooden-key or digital grand piano should I consider?", "What do players ask about hybrid and digital grand pianos?"),
 "stage-pianos": ("What should I look for in a stage piano?", "How does a stage piano help you learn?", "Which stage piano should I buy?", "What do players ask about stage pianos?"),
 "microphones-and-audio-interfaces": ("What do I need to record piano?", "How does recording help you learn?", "Which microphone, recorder or interface should I buy?", "What do students ask about recording piano?"),
 "keyboard-cases-and-covers": ("What should I look for in a keyboard case?", "How does a good case help you practice?", "Which keyboard case or cover should I buy?", "What do owners ask about keyboard cases?"),
}

LEARN_NEW = {
 "home-digital-pianos": "How this helps you learn: an instrument that stands ready in the room is the one you will sit down at every day, and daily practice is what moves an adult forward fastest.",
 "hybrid-and-digital-grand-pianos": "How this helps you learn: a refined key mechanism lets you hear the difference between a soft touch and a very soft touch, which is the next step after the first year of lessons.",
 "stage-pianos": "How this helps you learn: if your goal is to play with others, a stage piano puts a good weighted action in a form you can carry to a rehearsal.",
 "microphones-and-audio-interfaces": "How this helps you learn: listening to a recording of yourself is the fastest way to hear uneven touch and rhythm, and a clear clip is all I need to give feedback.",
 "keyboard-cases-and-covers": "How this helps you learn: a protected, ready instrument is easier to start every day, and a case makes lessons away from home possible.",
}

DEPTH_NEW = {
"home-digital-pianos": """
<h2>How do I choose between a console and an upright-style digital piano?</h2>
<p>A console digital piano is a flat-topped cabinet, a little like a desk with keys. An upright-style cabinet looks like a small acoustic upright. Both carry their own pedals and keep the keys at the right height. The difference is mostly taste and space: a compact upright-style model takes less floor and suits a corner of an apartment, and a slim console fits under a window. In both, check three things on the listing: the key action, the pedals and whether a bench comes with it.</p>
<h3>What I would try first</h3>
<p>If you can, press the keys in a shop. Play one note softly and one note loudly, and listen for a clear difference. Then sit at the cabinet and see where your knees fall under the keyboard: you should not have to push them against the sides.</p>
""",
"hybrid-and-digital-grand-pianos": """
<h2>When is a wooden-key or digital grand piano worth it?</h2>
<p>I would not send a first-year adult beginner to this page. A good weighted digital piano teaches the first years well. A wooden-key instrument becomes worth it when your ear and your hands have grown enough to notice what a better key action gives you: more control over the softest sounds, a more even repeated note, and a key that returns the way an acoustic key does.</p>
<h3>Honest limits</h3>
<p>Even the best of these makes its sound with speakers or headphones, not strings. The advantages are quiet practice, no tuning and a volume control. If what you want is an acoustic piano in a room, the right place to look is a local piano dealer, where you can hear and touch an instrument and have it delivered and tuned.</p>
""",
"microphones-and-audio-interfaces": """
<h2>How do I record piano well at home?</h2>
<p>Start with where the sound comes from. A digital piano can go straight into a recorder or an interface by cable, with no microphone at all. An acoustic piano needs microphones: a matched pair of small-diaphragm condensers, placed a little above and in front of the instrument, gives a natural stereo picture. Record one short passage, listen back with headphones, and move the microphones until it sounds like what you hear sitting at the keys.</p>
<h3>Keep the setup small</h3>
<p>A handheld stereo recorder is the simplest path to a clean clip. When you are recording every week, add an interface and a pair of condensers. The best setup is the one you will use.</p>
""",
}

BLOG_NEW = {
 "home-digital-pianos": ["digital-piano-vs-acoustic-beginner", "best-digital-piano-for-adult-beginners"],
 "hybrid-and-digital-grand-pianos": ["digital-piano-vs-acoustic-beginner", "weighted-vs-semi-weighted-keys"],
 "stage-pianos": ["digital-piano-vs-keyboard", "weighted-vs-semi-weighted-keys"],
 "microphones-and-audio-interfaces": ["piano-apps-vs-a-real-teacher", "run-your-own-piano-lesson"],
 "keyboard-cases-and-covers": ["practicing-piano-in-an-apartment", "digital-piano-vs-keyboard"],
}

NAV_ADD = [("pianos", "Pianos"), ("home-digital-pianos", "Home pianos"), ("hybrid-and-digital-grand-pianos", "Grand &amp; wooden-key"),
           ("stage-pianos", "Stage pianos"), ("microphones-and-audio-interfaces", "Microphones"), ("keyboard-cases-and-covers", "Cases")]

def apply(C, GUIDES, HUB, ARTICLE, D, S, N, blog_extra=None):
    patch(N, S)
    for pg in PAGES:
        C.PAGES.append(pg)
    for pg in C.PAGES:
        if pg["slug"] in META_UPDATES:
            pg.update(META_UPDATES[pg["slug"]])
        if pg["slug"] in Q_NEW:
            pg["q"] = Q_NEW[pg["slug"]]
    D.LEARN.update(LEARN_NEW)
    D.DEPTH.update(DEPTH_NEW)
    S.BLOG.update(BLOG_NEW)
    for k, v in (blog_extra or {}).items():
        S.BLOG_TITLES[k] = v

# ------------------------------------------------------------------ blog articles written with this expansion (queued 2026-11-14)
NEW_ARTICLES = {
 "what-is-a-hybrid-piano": "What Is a Hybrid Piano? A Teacher's Guide for Adults",
 "best-premium-digital-pianos-for-returning-players": "Best Premium Digital Pianos for Returning Players",
 "are-digital-grand-pianos-worth-it": "Are Digital Grand Pianos Worth It? A Teacher's Answer",
 "best-digital-pianos-for-adult-beginners-in-the-uk": "Best Digital Pianos for Adult Beginners in the UK",
 "best-digital-pianos-for-adult-beginners-in-canada": "Best Digital Pianos for Adult Beginners in Canada",
}
HYB, PREM, GRAND, UK, CA = list(NEW_ARTICLES)
HPH = "best-headphones-for-digital-piano"            # already in the queue (2026-11-18)
MICA = "best-microphone-for-recording-piano-at-home"  # already in the queue (2026-11-21)
BLOG_MORE = {
 "pianos": [PREM, HYB, "best-digital-piano-for-adult-beginners", "digital-piano-vs-acoustic-beginner"],
 "digital-pianos": [PREM, UK, CA],
 "home-digital-pianos": [PREM],
 "hybrid-and-digital-grand-pianos": [HYB, GRAND, PREM],
 "headphones-for-piano": [HPH],
 "microphones-and-audio-interfaces": [MICA],
 "record-yourself-playing": [MICA],
 "keyboards": [],
}

# ------------------------------------------------------------------ hub, start-here path
START_HERE = """<div class="howbox start-here"><h2>Not sure which piano? Start here</h2>
<p style="margin:0 0 12px">Answer three questions and go straight to the page that fits.</p>
<ol class="start-q">
<li><strong>Where will the piano live?</strong><span class="start-links"><a class="btn dark" href="digital-pianos.html">Anywhere, or I move it: portable digital pianos</a><a class="btn dark" href="home-digital-pianos.html">In the living room: home digital pianos</a></span></li>
<li><strong>How much do you want to spend?</strong><span class="start-links"><a class="btn dark" href="digital-pianos.html#budget">A careful first budget</a><a class="btn dark" href="digital-pianos.html#mid">Buy once and keep</a><a class="btn dark" href="hybrid-and-digital-grand-pianos.html">The best touch I can get</a></span></li>
<li><strong>What kind of player are you?</strong><span class="start-links"><a class="btn dark" href="which-digital-piano-to-buy.html">A beginner, learning alone</a><a class="btn dark" href="hybrid-and-digital-grand-pianos.html">Returning after years away</a><a class="btn dark" href="stage-pianos.html">I play with others</a></span></li>
</ol></div>"""

def pianos_body(ctx):
    """Returns the HTML body of shop/pianos.html. ctx supplies helpers from make_shop_pages."""
    esc, section, faq_html, related_html, read_next, tiers_html, pick = (ctx[k] for k in ("esc", "section", "faq_html", "related_html", "read_next", "tiers_html", "pick"))
    ladder = pick(["B01DZXE9NC", "B07X9SD5JR", "B0CQ7VD34X", "B07MH391ZF", "B01LY8OUQW", "B09GG8SCBF", "B0FDPGR3LX", "B0CBN7HYKB", "B08SBZW46G", "B0GJX8NJS8", "B0DR38F47F", "B08SC23H65", "B0H27C52DP", "B077YT617Y", "B08V95SZD8", "B0CQCV986L", "B0C6BVT77Q", "B0FTRF67DM", "B0CSMM5M1Z", "B0BSKN3HNT", "B0D15QXV5B"])
    cards = [("digital-pianos", "🎹", "Portable Digital Pianos", "88 weighted keys that fit a small room. The place to start."),
             ("home-digital-pianos", "🏠", "Home Digital Pianos", "Console and upright-style cabinets with their own pedals."),
             ("hybrid-and-digital-grand-pianos", "🎼", "Digital Grand and Wooden-Key Pianos", "Wooden-key consoles and a grand-style digital."),
             ("stage-pianos", "🎤", "Stage Pianos", "Weighted 88-key keyboards for playing out."),
             ("keyboards", "🎛️", "Keyboards", "61-key, arranger and MIDI keyboards.")]
    catgrid = '<div class="catgrid">%s</div>' % "".join('<a class="catcard" href="%s.html"><div class="ico">%s</div><h3>%s</h3><p>%s</p></a>' % (s, i, esc(t), esc(b)) for s, i, t, b in cards)
    faqs = [("What is the best digital piano for an adult beginner?", "One with 88 weighted keys, a real piano sound, a sustain pedal and a headphone jack. After that, choose the one you can afford and fit in the room. My long answer is in the guide on which digital piano an adult beginner should buy."),
            ("What is the difference between a digital piano, a hybrid piano and a digital grand?", "A digital piano makes its sound electronically with weighted keys. A hybrid adds a wooden-key hammer mechanism for a touch closer to an acoustic piano. A digital grand puts digital technology inside a grand-piano shape. All three have a volume control and a headphone jack."),
            ("Can I buy an acoustic upright or grand piano on Amazon?", "I searched Amazon by brand and model for uprights and grands on November 14, 2026 and found digital instruments and accessories, but no acoustic piano I could verify as sold and shipped there. An acoustic piano should be played, delivered by movers and tuned, so I suggest a local piano dealer, and I list the digital models that Amazon does sell."),
            ("Should I buy a digital piano or a keyboard?", "A digital piano if you can: weighted keys are what teach touch. A keyboard if space or budget is tight, chosen with touch-sensitive keys and planned as a stepping stone."),
            ("What else do I need with a digital piano?", "A sustain pedal, an adjustable bench, headphones and a stand if the piano has no legs. I list each in its own shop page.")]
    html = (section(
        '<div class="shop-prose"><p class="lead">%s</p></div>' % esc("I am a concert pianist and a university piano professor, and when an adult asks me which piano to buy, the honest answer starts with the keys, not the brand. This department puts every kind of piano I can recommend in one place, from a careful first budget to the most expensive instruments Amazon sells, and each page says what the listing states and nothing more.") +
        START_HERE +
        '<h2 style="margin-top:34px">Which kind of piano are you shopping for?</h2>' + catgrid +
        '<h2 style="margin-top:40px">Which piano fits my budget, from a first piano to a luxury one?</h2><p class="muted">Piano picks from every department, in order of ladder: budget, mid-range, premium, luxury. Open any listing on Amazon to check today&#39;s price.</p>' +
        tiers_html(ladder, "pianos") +
        '<div class="shop-prose"><h2>How do I choose a piano as an adult?</h2>'
        '<p>I choose in this order. First the keys: weighted keys that answer differently to a soft and a loud touch. Second the sound, which should be a real piano sound before it is anything else. Third the pedals, because the sustain pedal is part of the instrument. Fourth the room: measure where it will stand, and decide whether a portable on a stand or a cabinet suits it. Last the extras, which are a bench at the right height and a pair of headphones.</p>'
        '<h3>Portable, console, hybrid or grand?</h3>'
        '<p>A portable digital piano is the practical start. A home console or upright-style cabinet is the piano to keep. A hybrid or wooden-key instrument is for a player who has outgrown the first touch, and a digital grand is a piano-shaped statement for a room that has space. A stage piano is for playing out. For acoustic pianos I send adults to a local dealer, where you can hear and touch the instrument.</p></div>' +
        '<h2 style="margin-top:40px">What do adults ask before buying a piano?</h2><div class="shop-faq">%s</div>' % faq_html(faqs) +
        read_next("pianos") +
        '<h2 style="margin-top:40px">What else might you need?</h2>' + related_html(["piano-benches-and-stands", "piano-pedals", "headphones-for-piano", "microphones-and-audio-interfaces", "keyboard-cases-and-covers", "piano-accessories"])))
    return html, faqs, ladder

def ARTICLE_PATCH(A):
    A["html_after"] += ('<h2>Where can I see more pianos, by type and budget?</h2>'
                        '<p>The guide above stays with the first piano. When you know what you want, the piano department goes further: '
                        '<a href="pianos.html">all pianos, budget to luxury</a>, <a href="digital-pianos.html">portable digital pianos</a>, '
                        '<a href="home-digital-pianos.html">home digital pianos</a>, <a href="hybrid-and-digital-grand-pianos.html">hybrid and digital grand pianos</a> '
                        'and <a href="stage-pianos.html">stage pianos</a>. For the accessories, see <a href="piano-benches-and-stands.html">benches</a>, '
                        '<a href="piano-pedals.html">pedals</a> and <a href="headphones-for-piano.html">headphones</a>.</p>')
    if "pianos" not in A["related"]:
        A["related"] = ["pianos"] + list(A["related"])
