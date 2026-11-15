# -*- coding: utf-8 -*-
# Written 2026-11-14: buyer-intent batch 13, part A (digital pianos). Topics from _shop/topic_map_2026-11-14.md.
# Rules: first person, adults who learn alone, no prices or ratings, no invented specs, "what I look for" not "I tested".
from _buyer_kit import *
def lk(s, t): return '<a href="%s.html">%s</a>' % (s, t)
S = []

# 1 ---------------------------------------------------------------
S.append(spec("best-digital-pianos-2026", "2026-11-17",
 "Best Digital Pianos for Adults in 2026: A Concert Pianist's Picks",
 "Best Digital Pianos for Adults in 2026",
 "The best digital pianos for adult learners in 2026, chosen by a concert pianist: five portable models from Yamaha, Roland, Casio, with what to check on each.",
 "My master list of the digital pianos I would point an adult learner to in 2026, and how to choose between them.",
 meta_line() + """
<p>The best digital piano for most adults in 2026 is the Yamaha P-225 if you want one instrument for years, and the Yamaha P-145BT if you want the same style of keys for less. Roland&#39;s FP-30X is the one I would choose for a bigger sound, the Casio PX-S1100 for a small room, and the Yamaha P-525 for a returning player who wants wooden keys. I refresh this page when the listings change.</p>
""" + DISC + quick([("Best overall", "p225", "the same graded keyboard type as the P-145BT with headroom for years"),
 ("Best value", "p145", "the right keys without paying for extra voices"),
 ("Premium", "p525", "a wooden-key action for a returning player")]) +
 how_i_choose("A digital piano is a key action first and a sound engine second. I look at the action, the polyphony (how many notes can sound at once), the pedal and the headphone jacks, in that order.") + """
<h2>The five I would look at</h2>""" +
 pick("p145", "If your goal is to learn to play, the key action is the part you cannot upgrade later. This one has the right kind.") +
 pick("p225", "Choose this over the P-145BT if you play long pedaled pieces or want a teacher to listen on a second jack.") +
 pick("fp30x", "The stronger speakers make a difference in a room with a hard floor. It is the one I suggest if you will not always wear headphones.") +
 pick("pxs1100", "A good answer to a small apartment. It can run on batteries, and it has two headphone jacks.") +
 pick("p525", "This is the odd one out: not a first piano, but the portable I would point a returning player to if wooden keys matter.") + """
<h2>Comparison of the five</h2>""" +
 table(["Type", "Key action", "Polyphony", "Headphone jacks"], trows(["p145", "p225", "fp30x", "pxs1100", "p525"], ["type", "action", "poly", "phones"])) + """
<p>The figures come from the makers&#39; own specification pages or the Amazon listing. Where a source did not give a figure, the table says so rather than guess.</p>
<h2>How to choose</h2>
<ul><li><strong>Start with the keys.</strong> Weighted, graded keys (heavier in the bass) are what teach touch. Read my guide to """ + lk("weighted-vs-semi-weighted-keys", "weighted and semi-weighted keys") + """.</li>
<li><strong>Then the pedal.</strong> Most come with a switch; a real piano-style pedal is a small upgrade. See """ + lk("best-sustain-pedal-for-digital-piano", "the best sustain pedals") + """.</li>
<li><strong>Then the space.</strong> Measure where it will stand. A portable needs a stand and a bench; a cabinet needs floor space.</li>
<li><strong>Last, the sound.</strong> You will play on headphones more than you think. See """ + lk("best-headphones-for-digital-piano", "headphones for digital piano") + """.</li></ul>
<p>If you are comparing the two Yamahas directly, read """ + lk("yamaha-p145-vs-p225", "Yamaha P-145 vs P-225") + """; for the three-way decision, my """ + lk("best-digital-piano-for-adult-beginners", "guide for adult beginners") + """ goes further.</p>""" +
 closing([("digital-pianos", "portable digital pianos"), ("home-digital-pianos", "home digital pianos"), ("index", "the shop")]) + trust("a first piano"),
 [("What is the best digital piano for an adult in 2026?", "For most adults, the Yamaha P-225 for one instrument that lasts, or the Yamaha P-145BT for the same type of keys at a lower cost. The best one for you is the one whose keys you like and whose size fits your room."),
  ("How many keys do I need?", "88 keys if you can. It covers all standard piano music and costs little more than 76. My guide to how many keys you need explains the trade-offs."),
  ("Do I need a digital piano with speakers?", "If you will play without headphones, yes. If you play mainly at night, the speakers matter less than the keys and the headphone jack.")]))

# 2 ---------------------------------------------------------------
S.append(spec("best-digital-piano-under-1000", "2026-11-18",
 "Best Digital Piano Under $1000 (2026): A Teacher's Picks",
 "Best Digital Piano Under $1000 (2026)",
 "The best digital pianos under $1000 for adult learners, chosen by a concert pianist: portable and cabinet models, with what a teacher checks on each.",
 "If your budget tops out at $1000, here are the digital pianos I would look at, what each is for, and where to be careful.",
 meta_line() + """
<p>Under $1000, the digital pianos I would look at first are the Yamaha P-225, the Roland FP-30X and the Casio PX-S1100 for portable models, and the Casio PX-870 if you want a console cabinet. Prices on Amazon move, so I chose these by what the listings showed on November 14, 2026; check today&#39;s price before you buy.</p>
""" + DISC + quick([("Best overall", "p225", "graded keys and 192-note polyphony"),
 ("Best sound", "fp30x", "256-note polyphony and a stronger speaker system"),
 ("Best for a cabinet", "px870", "a console piano with a scaled hammer action")]) +
 how_i_choose("Under $1000 you can have a real piano action, so I do not recommend anything with semi-weighted keys. I check the action, the pedal, the headphone jacks and the weight.") + """
<h2>The picks</h2>""" +
 pick("p225", "The one I would buy for an adult who plans to stay. It has headroom for pedaled pieces and two headphone jacks.") +
 pick("fp30x", "I like the PHA-4 action and the speaker power; it is heavier than the Yamaha pianos, so it suits a piano that stays put.") +
 pick("pxs1100", "The slim body and battery option make it the best answer to a small flat.") +
 pick("px870", "The only cabinet in this guide. Console pianos feel steadier under forceful playing and look like furniture.") + """
<h2>Comparison</h2>""" +
 table(["Type", "Key action", "Polyphony", "Headphone jacks"], trows(["p225", "fp30x", "pxs1100", "px870"], ["type", "action", "poly", "phones"])) + """
<h2>How to choose under $1000</h2>
<ul><li><strong>If you are tight on space:</strong> the PX-S1100.</li><li><strong>If you want the strongest sound from a portable:</strong> the FP-30X.</li>
<li><strong>If you want one for the long haul:</strong> the P-225.</li><li><strong>If a piano must look like furniture:</strong> the PX-870.</li></ul>
<p>Budget for a bench and a pedal as well: see """ + lk("how-to-choose-a-piano-bench-and-sit-at-the-right-height", "how to choose a piano bench") + """. For a lower budget, read """ + lk("best-digital-piano-under-500", "the best digital piano under $500") + """; for a higher one, see """ + lk("best-premium-digital-pianos-for-returning-players", "premium digital pianos for returning players") + """.</p>""" +
 closing([("digital-pianos", "portable digital pianos"), ("home-digital-pianos", "home digital pianos"), ("piano-benches-and-stands", "benches and stands")]) + trust("a first piano"),
 [("Is a digital piano under $1000 good enough for an adult beginner?", "Yes. At this level you can have weighted, graded keys and a good sound, which is what an adult needs for years of study."),
  ("Portable or console?", "Portable if you need to move it or have little room; console if the piano will stay in one room and you want a steadier feel."),
  ("Do I need to spend more than $1000?", "Not to learn well. Spend more if you are a returning player who wants a wooden-key action or a cabinet with three pedals.")]))

# 3 ---------------------------------------------------------------
S.append(spec("best-digital-piano-under-500", "2026-11-19",
 "Best Digital Piano Under $500 (2026): Honest Picks for Adults",
 "Best Digital Piano Under $500 (2026)",
 "The best digital pianos under $500 for adult beginners, chosen by a concert pianist, with what each listing says and what a teacher checks.",
 "Under $500 you can still get weighted keys. Here are the models I would look at, and the one trap to avoid.",
 meta_line() + """
<p>Under $500 I would look at the Roland FP-10 for the best key feel, the Yamaha P-45 for the lowest-cost weighted piano from a major maker, and the Donner DEP-20 if the budget is tighter still. I chose these by the prices the Amazon listings showed on November 14, 2026; check today&#39;s price. The trap to avoid is a keyboard with semi-weighted keys sold as a piano.</p>
""" + DISC + quick([("Best overall", "fp10", "the PHA-4 Standard keyboard with escapement"),
 ("Best value", "p45", "weighted keys from a major maker at a low entry point"),
 ("Tightest budget", "dep20", "88 full-size weighted keys, though with less detail on the listing")]) +
 how_i_choose("At this level the key action decides everything. I look for the words weighted, graded or hammer action in the listing, and I treat semi-weighted as a different instrument.") + """
<h2>The picks</h2>""" +
 pick("fp10", "The best touch I can point to under this ceiling, in a compact body.") +
 pick("p45", "A sensible first piano if you want a Yamaha. Read the listing carefully, because it states few specifications.") +
 pick("dep20", "Worth considering only when the budget is firm. I would choose a major maker if I could stretch.") + """
<h2>Comparison</h2>""" +
 table(["Type", "Key action", "Polyphony", "Headphone jacks"], trows(["fp10", "p45", "dep20"], ["type", "action", "poly", "phones"])) + """
<h2>What about semi-weighted keyboards?</h2>
<p>Several 88-key keyboards at this level, such as the """ + A("B01DZXE9NC", "Alesis Recital") + """ and the """ + A("B0BCXGQL45", "Korg Liano") + """, have semi-weighted keys. They are lighter and springier than a piano&#39;s hammer action. They will teach notes and rhythm; they teach less about control of soft and loud. Read """ + lk("weighted-vs-semi-weighted-keys", "weighted vs semi-weighted keys") + """ before you choose.</p>
<h2>How to choose under $500</h2>
<ul><li>Choose weighted keys over a longer feature list.</li><li>Choose 88 keys over 61 if you can; see """ + lk("how-many-keys-do-i-need-piano", "how many keys you need") + """.</li><li>Save a little for a bench and a pedal.</li></ul>
<p>If you can stretch, the """ + lk("yamaha-p145-vs-p225", "Yamaha P-145BT and P-225") + """ are the next step up.</p>""" +
 closing([("digital-pianos", "portable digital pianos"), ("piano-pedals", "pedals"), ("piano-benches-and-stands", "benches and stands")]) + trust("a first piano"),
 [("Can I learn piano on a digital piano under $500?", "Yes, if it has weighted keys. That is the feature that matters most for an adult building a real technique."),
  ("Is semi-weighted good enough?", "For learning notes and rhythm, yes. For learning touch, a weighted or graded action is better."),
  ("What should I buy with it?", "A sustain pedal, an adjustable bench and a pair of closed-back headphones.")]))

# 4 ---------------------------------------------------------------
S.append(spec("best-digital-piano-under-300", "2026-11-22",
 "Best Digital Piano Under $300 (2026): What You Can and Cannot Get",
 "Best Digital Piano Under $300 (2026)",
 "What a digital piano under $300 can and cannot do for an adult learner, from a concert pianist, with the 88-key models I found and what to check.",
 "Under $300 the honest answer is a semi-weighted 88-key keyboard. Here is what that gets you, and when to stretch.",
 meta_line() + """
<p>Under $300, what Amazon offers is mostly 88-key keyboards with semi-weighted keys, such as the Alesis Recital, not true weighted pianos. They are a fair way to start if the alternative is no instrument. If you can stretch a little, the Yamaha P-45 and the Donner DEP-20 have weighted keys. I chose these by the prices the listings showed on November 14, 2026; check today&#39;s price.</p>
""" + DISC + quick([("Best to start", "alesis", "88 semi-weighted keys at the lowest cost here"),
 ("Best speakers", "liano", "semi-weighted keys with built-in bass-reflex speakers"),
 ("Worth stretching to", "dep20", "88 full-size weighted keys")], title="Quick picks") +
 how_i_choose("Under $300 the choice is a trade-off, and I say so plainly. Semi-weighted keys teach notes and rhythm. They do not teach control of soft and loud as well as a piano action does.") + """
<h2>The picks</h2>""" +
 pick("alesis", "If your budget is firm, this is the one I would use to begin, with the plan to move to a weighted piano within a year or two.") +
 pick("liano", "The built-in speakers are the attraction. The key action is the same trade-off.") +
 pick("dep20", "If you can stretch to this, you gain weighted keys. I would choose it over a semi-weighted keyboard.") + """
<h2>Comparison</h2>""" +
 table(["Type", "Key action", "Polyphony", "Headphone jacks"], trows(["alesis", "liano", "dep20"], ["type", "action", "poly", "phones"])) + """
<h2>How to choose at this budget</h2>
<ul><li>If you can stretch, weighted keys are the single best upgrade. See """ + lk("best-digital-piano-under-500", "the best digital piano under $500") + """.</li>
<li>If you cannot, learn on the semi-weighted keyboard and play a real piano whenever you can, so your hands learn the difference.</li>
<li>Buy a pedal and a bench; they matter more than extra sounds.</li></ul>
<p>My guide to """ + lk("digital-piano-vs-keyboard", "digital piano versus keyboard") + """ explains the difference in detail.</p>""" +
 closing([("keyboards", "keyboards"), ("digital-pianos", "portable digital pianos"), ("piano-benches-and-stands", "benches and stands")]) + trust("a first instrument"),
 [("Is there a weighted digital piano under $300?", "Prices move, so check the listing. On November 14, 2026 the models I found with weighted keys were just above this ceiling."),
  ("Is a semi-weighted keyboard bad for learning?", "No. It is a fair way to learn notes and rhythm. It is less helpful for learning control of soft and loud, which is why I suggest a weighted action when you can."),
  ("What is the first upgrade?", "A weighted piano, and a sustain pedal that grips the floor.")]))

# 5 ---------------------------------------------------------------
S.append(spec("best-portable-digital-piano", "2026-11-19",
 "Best Portable Digital Piano for Adults (2026): A Teacher's Picks",
 "Best Portable Digital Piano for Adults (2026)",
 "The best portable digital pianos for adult learners in 2026, chosen by a concert pianist: light 88-key models with weights from the makers&#39; own pages.",
 "A portable piano should be light enough to move and good enough to learn on. These are the ones I would look at.",
 meta_line() + """
<p>The best portable digital piano for most adults is the Yamaha P-145BT: Yamaha lists it at 11.1 kg, with 88 graded keys. The Casio PX-S1100 is the lightest and slimmest I verified, at 11.2 kg and able to run on batteries, and the Roland FP-10 is the compact choice, at 12.6 kg. The Roland FP-30X is the strongest-sounding portable, at 14.8 kg with the music rest.</p>
""" + DISC + quick([("Best overall", "p145", "11.1 kg with 88 graded keys"),
 ("Best for tiny spaces", "pxs1100", "slim, 11.2 kg, battery option"),
 ("Strongest sound", "fp30x", "256-note polyphony, 14.8 kg with the music rest")]) +
 how_i_choose("Portable should not mean toy. I check that the keys are weighted, then the weight, then whether it needs a stand and a bench that are also portable.") + """
<h2>The picks</h2>""" +
 pick("p145", "The lightest of the Yamaha pianos here, with the keys I want a beginner to learn on.") +
 pick("pxs1100", "If you carry the piano between rooms, or have no table to rest it on, this one is hard to beat.") +
 pick("fp10", "Roland&#39;s compact model has the escapement action in a small footprint.") +
 pick("fp30x", "Heavier, but the sound is stronger. Better for a piano that moves rarely.") + """
<h2>Comparison</h2>""" +
 table(["Type", "Key action", "Weight", "Headphone jacks"], trows(["p145", "pxs1100", "fp10", "fp30x"], ["type", "action", "weight", "phones"])) + """
<h2>How to choose a portable</h2>
<ul><li>Weigh what you will actually carry: the piano, a stand and a bench.</li><li>Check where the music rest and pedal go when you pack up.</li>
<li>If you will mostly leave it set up, a heavier model with a stronger sound is fine.</li></ul>
<p>For the stand and bench, see """ + lk("how-to-choose-a-piano-bench-and-sit-at-the-right-height", "how to choose a bench") + """.</p>""" +
 closing([("digital-pianos", "portable digital pianos"), ("piano-benches-and-stands", "benches and stands"), ("keyboard-cases-and-covers", "cases and covers")]) + trust("a first piano"),
 [("What is the lightest 88-key digital piano?", "From the models I verified, the Yamaha P-145BT at 11.1 kg and the Casio PX-S1100 at 11.2 kg without batteries, per their makers&#39; pages."),
  ("Can I run a digital piano on batteries?", "The Casio PX-S1100 can, with six AA batteries according to Casio. Check each model&#39;s page."),
  ("Do I need a stand?", "Yes. A stable stand and an adjustable bench matter for your posture as much as the piano.")]))

# 6 ---------------------------------------------------------------
S.append(spec("best-digital-piano-for-classical-music", "2026-11-20",
 "Best Digital Piano for Classical Music (2026): A Concert Pianist's Picks",
 "Best Digital Piano for Classical Music (2026)",
 "The best digital pianos for classical repertoire, chosen by a concert pianist: what to check in the action, pedals and polyphony, and which models to see.",
 "Classical music asks more of a digital piano than pop does: a graded action, real half-pedaling and enough polyphony. Here is what I would look at.",
 meta_line() + """
<p>For classical music I look for a graded action, three pedals if possible, a pedal that can be pressed halfway, and enough polyphony that long pedaled passages do not cut notes off. The Yamaha P-225, Roland FP-30X and Casio PX-S1100 are the portable models I would look at first; the Yamaha Arius YDP-146 is the cabinet with three pedals; and for a returning player, the Yamaha P-525 offers a wooden-key action.</p>
""" + DISC + quick([("Best portable", "fp30x", "PHA-4 action with escapement and 256-note polyphony"),
 ("Best cabinet", "ydp146", "three pedals and the CFX concert grand sound"),
 ("Best for a returning player", "p525", "wooden-key GrandTouch-S action")]) +
 how_i_choose("Classical repertoire is made of control: soft playing, sustained harmony, pedal blends. I listen for these things, so I check the action, the half-pedal and the polyphony.") + """
<h2>The picks</h2>""" +
 pick("fp30x", "Escapement lets you feel the let-off of a key, which helps with quiet playing. With a better pedal it handles Bach, Mozart and early Romantic pieces well.") +
 pick("p225", "192 notes of polyphony means the pedal can stay down in a Chopin nocturne without notes dropping.") +
 pick("ydp146", "Three pedals matter for Debussy and Ravel, which use the soft and middle pedals. This is the cabinet I would choose for them.") +
 pick("p525", "For a returning player with technique, a wooden-key action is the closest a portable gets.") + """
<h2>Comparison</h2>""" +
 table(["Type", "Key action", "Polyphony", "Headphone jacks"], trows(["fp30x", "p225", "ydp146", "p525"], ["type", "action", "poly", "phones"])) + """
<h2>What to check for classical playing</h2>
<ul><li><strong>Half-pedaling.</strong> A pedal that can sit halfway lets you blend harmonies without blurring. See """ + lk("best-sustain-pedal-for-digital-piano", "the best sustain pedals") + """.</li>
<li><strong>Three pedals.</strong> Portable pianos usually have one pedal jack; a cabinet gives you the soft and middle pedals.</li>
<li><strong>Polyphony.</strong> At 64 notes a long pedaled passage can cut off notes; 192 or more gives headroom.</li></ul>
<p>For a pianist stepping up, my guide to """ + lk("best-premium-digital-pianos-for-returning-players", "premium digital pianos for returning players") + """ goes further.</p>""" +
 closing([("digital-pianos", "portable digital pianos"), ("home-digital-pianos", "home digital pianos"), ("piano-pedals", "pedals")]) + trust("classical repertoire"),
 [("What is the best digital piano for classical music?", "One with a graded action, real half-pedaling and enough polyphony. For most adults, the FP-30X or P-225; for a cabinet with three pedals, the YDP-146."),
  ("Do I need three pedals?", "For much Romantic and Impressionist music, the soft and middle pedals are useful. A cabinet provides them; a portable usually needs an extra pedal unit."),
  ("Is polyphony important?", "Yes, if you use the pedal a lot. Sustained notes keep counting after your fingers leave the keys.")]))

# 7 ---------------------------------------------------------------
S.append(spec("best-88-key-weighted-keyboard-for-beginners", "2026-11-20",
 "Best 88-Key Weighted Keyboard for Beginners (2026): A Teacher's Picks",
 "Best 88-Key Weighted Keyboard for Beginners",
 "The best 88-key weighted keyboards for adult beginners, chosen by a concert pianist: Yamaha, Roland, Casio and Donner, with what each listing actually says.",
 "If you want 88 weighted keys to learn on, these are the ones I would look at and the key facts for each.",
 meta_line() + """
<p>An 88-key weighted keyboard is the sensible starting point for an adult who wants to learn piano. The ones I would look at are the Yamaha P-145BT, Roland FP-10 and Yamaha P-45, with the Casio CDP-S360 and Donner DDP-300 as alternatives. All are described by their listings as weighted or hammer-action.</p>
""" + DISC + quick([("Best overall", "p145", "88 keys on a GHC keyboard"),
 ("Best key feel", "fp10", "PHA-4 Standard keyboard with escapement"),
 ("Best budget alternative", "ddp300", "88 graded hammer-action keys with stated polyphony")]) +
 how_i_choose("I check that the listing says weighted, graded or hammer action, because the words semi-weighted and weighted are easy to confuse.") + """
<h2>The picks</h2>""" +
 pick("p145", "The one I recommend most often to adults.") +
 pick("fp10", "A compact option with the best-known Roland action.") +
 pick("p45", "A lower-cost way into a Yamaha weighted action.") +
 pick("cdps360", "A scaled hammer action in a slim body.") +
 pick("ddp300", "A budget alternative that states its polyphony clearly.") + """
<h2>Comparison</h2>""" +
 table(["Type", "Key action", "Polyphony", "Headphone jacks"], trows(["p145", "fp10", "p45", "cdps360", "ddp300"], ["type", "action", "poly", "phones"])) + """
<h2>How to choose</h2>
<ul><li>Read """ + lk("weighted-vs-semi-weighted-keys", "weighted vs semi-weighted keys") + """.</li><li>Choose 88 keys: """ + lk("how-many-keys-do-i-need-piano", "how many keys you need") + """.</li><li>Add a sustain pedal and an adjustable bench.</li></ul>""" +
 closing([("digital-pianos", "portable digital pianos"), ("piano-pedals", "pedals"), ("piano-benches-and-stands", "benches and stands")]) + trust("a first piano"),
 [("What does weighted mean on a keyboard?", "Weighted keys resist your finger the way a piano&#39;s hammer action does, so you learn to control volume with touch."),
  ("Are all 88-key keyboards weighted?", "No. Some are semi-weighted or unweighted. Read the listing for the words weighted, graded or hammer action."),
  ("Is 88 keys necessary?", "For most piano music, yes. It costs little more than 76 and avoids limits later.")]))

# 8 ---------------------------------------------------------------
fp10_p145_rows = [["Keyboard", "PHA-4 Standard, escapement, ivory-feel white keys", "GHC keyboard, matte black keytops"],
 ["Keys", "88", "88"], ["Touch settings", "Five key touch types, plus fixed", "Hard / medium / soft / fixed"],
 ["Polyphony", "96", "64"], ["Tones / voices", "36 (15 on the front panel)", "10"],
 ["Speakers", "Two 12 cm, 6 W each", "Oval (12 cm x 8 cm) x 2, 7 W x 2"],
 ["Headphone jacks", "One", "One"], ["Bluetooth", "Bluetooth MIDI (may not be included, depending on country of purchase)", "Bluetooth audio (varies by area)"],
 ["Pedal in the box", "Pedal switch", "Footswitch"], ["Weight", "12.6 kg (music rest detached)", "11.1 kg"]]
S.append(spec("roland-fp-10-vs-yamaha-p-145bt", "2026-11-21",
 "Roland FP-10 vs Yamaha P-145BT: A Piano Teacher's Comparison",
 "Roland FP-10 vs Yamaha P-145BT (2026)",
 "Roland FP-10 or Yamaha P-145BT for an adult beginner? A concert pianist compares keys, polyphony, speakers and connections from the makers&#39; own specifications.",
 "Two entry-level pianos from the two big makers. Here is the spec-by-spec comparison and which I would choose for an adult learning alone.",
 meta_line() + """
<p>For an adult beginner, I would choose the Roland FP-10 if key feel is your priority, and the Yamaha P-145BT if you want a lighter body and Bluetooth audio. Both have 88 keys and a pedal switch in the box. The FP-10 has 96-voice polyphony and the escapement action; the P-145BT has 64-note polyphony and weighs 11.1 kg to the FP-10&#39;s 12.6 kg.</p>
""" + DISC + quick([("If key feel matters most", "fp10", "PHA-4 Standard keys with escapement"),
 ("If weight and Bluetooth audio matter", "p145", "11.1 kg and Bluetooth audio")], title="Quick verdict") + """
<h2>Roland FP-10 vs Yamaha P-145BT: specifications</h2>""" +
 table(["Roland FP-10", "Yamaha P-145BT"], fp10_p145_rows, first="Specification (as listed by the maker)") + """
<p>Sources: Roland&#39;s FP-10 specification page and Yamaha&#39;s P-145 specifications, both checked on November 14, 2026.</p>
<h2>The keys</h2>
<p>Both are graded: heavier in the bass, lighter in the treble. The FP-10 adds escapement, a small notch you feel as the key lets go, and ivory-feel white keys. These help with quiet playing and repeated notes. The Yamaha&#39;s GHC keyboard is simpler, and a beginner will not miss what they have never felt.</p>
<h2>Polyphony and sound</h2>
<p>Polyphony counts how many notes can sound at once. At 96 the FP-10 has more room than the P-145BT&#39;s 64. For first-year pieces neither will run out; for long pedaled passages, the FP-10 has more headroom. For more, see """ + lk("yamaha-p145-vs-p225", "Yamaha P-145 vs P-225") + """.</p>
<h2>Connections</h2>
<p>The P-145BT offers Bluetooth audio, so you can play along with a recording through the piano&#39;s speakers. The FP-10 has Bluetooth MIDI, which works with apps, though Roland notes it may not be included depending on the country of purchase.</p>""" +
 pick("fp10", "My choice if you will be on headphones and the touch is the priority.") +
 pick("p145", "My choice if you also play along with recordings and carry the piano.") + """
<h2>Which should you buy?</h2>
<p>If you can only try one in a shop, try the FP-10 first, then choose by feel. If you cannot try either, the P-145BT is the safer first piano because it is lighter and plays audio. Whichever you choose, add an adjustable bench and a proper pedal.</p>""" +
 closing([("digital-pianos", "portable digital pianos"), ("piano-benches-and-stands", "benches and stands"), ("piano-pedals", "pedals")]) + trust("a first piano"),
 [("Which is better for a beginner, the FP-10 or the P-145BT?", "Both have 88 graded keys and are good first pianos. The FP-10 has the more refined key action; the P-145BT is lighter and has Bluetooth audio."),
  ("Do either come with a pedal?", "Both come with a pedal switch. A proper piano-style pedal is a small upgrade."),
  ("Do I need Bluetooth?", "Not to learn. It is convenient for playing along with a recording.")]))

# 9 ---------------------------------------------------------------
S.append(spec("roland-fp-10-review", "2026-11-21",
 "Roland FP-10 Review: A Piano Teacher's Assessment (2026)",
 "Roland FP-10 Review: A Piano Teacher's Assessment",
 "An assessment of the Roland FP-10 by a concert pianist who teaches adults: what the specifications say, what I look for, and who I would recommend it to.",
 "I have not tested every piano I write about, and I say so. Here is what the FP-10 specifications tell a teacher, and who it suits.",
 meta_line() + """
<p><strong>A note on method.</strong> This is an assessment, not a hands-on test. I have not set up and used this particular unit for weeks, and I will not claim to. What I can do is read Roland&#39;s specifications and the Amazon listing as a piano teacher, tell you what I look for in a first piano, and say whether I would recommend this to a student.</p>
<p><strong>My verdict:</strong> I would recommend the Roland FP-10 to an adult beginner who wants a real graded action in a small body. Its limits are 96-voice polyphony and one headphone jack.</p>
""" + DISC + quick([("Verdict", "fp10", "a good first piano for a small room, with limits on polyphony and headphone jacks")], title="In short") + """
<h2>What Roland says</h2>
<p>Roland lists 88 keys on the PHA-4 Standard keyboard with escapement and ivory-feel white keys, five key touch types plus a fixed option, 96-voice polyphony, 36 tones (15 selectable on the front panel), two 12 cm speakers rated at 6 W each, a single headphone jack, a pedal switch in the box and a weight of 12.6 kg with the music rest detached. Bluetooth MIDI is listed, though Roland notes it may not be included depending on your country of purchase.</p>
<h2>What I look for, and how the FP-10 answers</h2>
<ul><li><strong>Graded action.</strong> Heavier keys in the bass, lighter in the treble, as on an acoustic piano. The PHA-4 Standard is Roland&#39;s keyboard for this.</li>
<li><strong>Escapement.</strong> A small notch you feel when the key releases the hammer, helpful for soft playing and repeated notes.</li>
<li><strong>Polyphony.</strong> At 96 voices, the piano can run out when you hold the pedal through a long passage. For first-year music it is enough.</li>
<li><strong>Headphone jack.</strong> One, so a teacher cannot listen alongside you; use the speakers or a splitter if you need it.</li>
<li><strong>Pedal.</strong> A switch comes with it; I would add a proper pedal. See """ + lk("best-sustain-pedal-for-digital-piano", "the best sustain pedals") + """.</li></ul>""" +
 pick("fp10", "I would recommend it to the student who asks me for one piano that feels right and does not need to do everything.") + """
<h2>Who should look elsewhere</h2>
<p>If you will play pedal-heavy Romantic pieces soon, or want a second headphone jack, step up to the """ + A("B08SBZW46G", "Roland FP-30X") + """, which Roland lists at 256-note polyphony and two jacks. For a Yamaha comparison, see """ + lk("roland-fp-10-vs-yamaha-p-145bt", "Roland FP-10 vs Yamaha P-145BT") + """.</p>""" +
 closing([("digital-pianos", "portable digital pianos"), ("piano-benches-and-stands", "benches and stands"), ("piano-pedals", "pedals")]) + trust("a first piano"),
 [("Is the Roland FP-10 good for beginners?", "In my assessment, yes: a graded action with escapement in a compact body. Its limits are 96-voice polyphony and one headphone jack."),
  ("Does the FP-10 come with a pedal?", "Roland lists a pedal switch in the box. A piano-style pedal is a small upgrade."),
  ("Has Dr. Pisarenko tested the FP-10?", "No. This is an assessment based on the specifications and what a teacher looks for, not a hands-on test.")]))

# 10 --------------------------------------------------------------
px_rows = [["Keyboard", "GHC keyboard, matte black keytops", "Smart Scaled Hammer Action"],
 ["Keys", "88", "88"], ["Touch settings", "Hard / medium / soft / fixed", "Five levels, plus off"],
 ["Polyphony", "64", "192"], ["Tones / voices", "10", "18"],
 ["Amplifiers", "7 W x 2", "8 W + 8 W"], ["Headphone jacks", "One", "Two"],
 ["Bluetooth", "Bluetooth audio (varies by area)", "Bluetooth 5.0 audio, and MIDI with the included adaptor"],
 ["Pedal in the box", "Footswitch", "SP-3 damper pedal"],
 ["Width x depth", "1,326 mm x 268 mm", "1,322 mm x 232 mm (without music stand)"],
 ["Weight", "11.1 kg", "11.2 kg (without batteries)"], ["Power", "Not stated in the specifications I checked", "Six AA batteries, or the adaptor"]]
S.append(spec("yamaha-p-145bt-vs-casio-px-s1100", "2026-11-22",
 "Yamaha P-145BT vs Casio PX-S1100: A Piano Teacher's Comparison",
 "Yamaha P-145BT vs Casio PX-S1100 (2026)",
 "Yamaha P-145BT or Casio Privia PX-S1100? A concert pianist compares keys, polyphony, headphone jacks, pedals and weight from the makers&#39; own specifications.",
 "Two light portable pianos for adult learners. Here is how they compare, spec by spec, and which I would choose.",
 meta_line() + """
<p>For most adults I would choose the Casio PX-S1100 over the Yamaha P-145BT if you want more headroom: it lists 192-note polyphony to the Yamaha&#39;s 64, two headphone jacks to one, and a real damper pedal in the box. Choose the P-145BT if you prefer Yamaha&#39;s keyboard and a simpler instrument. They weigh almost the same, 11.1 and 11.2 kg.</p>
""" + DISC + quick([("More headroom and a pedal in the box", "pxs1100", "192-note polyphony, two jacks, battery option"),
 ("Simpler Yamaha keyboard", "p145", "GHC keyboard with Bluetooth audio")], title="Quick verdict") + """
<h2>Yamaha P-145BT vs Casio PX-S1100: specifications</h2>""" +
 table(["Yamaha P-145BT", "Casio PX-S1100"], px_rows, first="Specification (as listed by the maker)") + """
<p>Sources: Yamaha&#39;s P-145 specifications and Casio&#39;s PX-S1100 specifications, both checked on November 14, 2026.</p>
<h2>The keys</h2>
<p>Both are graded, with heavier keys in the bass. I would play both slowly and listen for an even sound from the first note to the last. The Casio&#39;s slimmer body is a difference of space, not of feel.</p>
<h2>Polyphony, headphones and pedal</h2>
<p>The Casio&#39;s larger numbers matter in daily life: long pedaled passages are safer at 192 notes, two headphone jacks let a teacher sit alongside you, and a damper pedal in the box is better than a switch. See """ + lk("best-sustain-pedal-for-digital-piano", "my pedal guide") + """.</p>
<h2>Which should you buy?</h2>
<p>I lean to the PX-S1100 for flexibility, and to the P-145BT if Yamaha&#39;s keys are your preference or you want the simplest option. You can also compare with the """ + lk("yamaha-p145-vs-p225", "Yamaha P-225") + """.</p>""" +
 pick("pxs1100", "The one I would pick for a small room.") + pick("p145", "The one I would pick for simplicity.") +
 closing([("digital-pianos", "portable digital pianos"), ("piano-pedals", "pedals"), ("piano-benches-and-stands", "benches and stands")]) + trust("a first piano"),
 [("Which has more polyphony, the P-145BT or the PX-S1100?", "The PX-S1100: Casio lists 192 notes, Yamaha lists 64 for the P-145BT."),
  ("Which is lighter?", "They are almost the same: Yamaha lists 11.1 kg and Casio 11.2 kg without batteries."),
  ("Can the PX-S1100 run on batteries?", "Casio says it runs on six AA batteries or the AC adaptor.")]))

# 11 --------------------------------------------------------------
S.append(spec("casio-privia-px-s1100-review", "2026-11-23",
 "Casio Privia PX-S1100 Review: A Piano Teacher's Assessment (2026)",
 "Casio Privia PX-S1100 Review: A Teacher's Assessment",
 "An assessment of the Casio Privia PX-S1100 by a concert pianist who teaches adults: what Casio lists, what I look for, and who I would recommend it to.",
 "I have not tested this piano and I will not pretend to. Here is what Casio&#39;s specifications tell a teacher, and who it suits.",
 meta_line() + """
<p><strong>A note on method.</strong> This is an assessment, not a hands-on test. I have not used this particular piano for weeks. I read Casio&#39;s specification page and the Amazon listing as a piano teacher, and tell you what I look for and whether I would recommend it.</p>
<p><strong>My verdict:</strong> I would recommend the PX-S1100 to an adult who has a small room, shares a space, or wants to run a piano on batteries. The slim body is the reason to buy it; check the stability of the keyboard under firm chords if you can.</p>
""" + DISC + quick([("Verdict", "pxs1100", "a good choice for small spaces, with two headphone jacks and a damper pedal in the box")], title="In short") + """
<h2>What Casio says</h2>
<p>Casio lists 88 keys with Smart Scaled Hammer Action, five touch sensitivity levels plus off, 192-note polyphony, 18 tones from its AiR sound source, 8 W plus 8 W amplifiers, two headphone jacks, USB type A and B, Bluetooth 5.0 audio (and MIDI via the included wireless adaptor), an SP-3 damper pedal in the box, and a weight of 11.2 kg without batteries. It measures 1,322 x 232 x 102 mm without the music stand, and runs on six AA batteries or an adaptor.</p>
<h2>What I look for, and how it answers</h2>
<ul><li><strong>Scaled action.</strong> Heavier bass keys, lighter treble keys, like a piano. Casio&#39;s Smart Scaled Hammer Action is its answer.</li>
<li><strong>Polyphony.</strong> 192 is plenty for a pedal-heavy nocturne.</li>
<li><strong>Two headphone jacks.</strong> Good for lessons side by side.</li>
<li><strong>A real pedal in the box.</strong> An SP-3 is better than a switch.</li>
<li><strong>Stability.</strong> A very slim body can feel less solid under forceful playing. A good stand helps.</li></ul>""" +
 pick("pxs1100", "I would suggest it to a student who has told me that space is the problem they need to solve.") + """
<h2>Who should look elsewhere</h2>
<p>If you want a three-pedal setup on the original stand, note that Casio lists one damper pedal jack, with an optional three-pedal unit. For a Yamaha comparison, see """ + lk("yamaha-p-145bt-vs-casio-px-s1100", "Yamaha P-145BT vs Casio PX-S1100") + """.</p>""" +
 closing([("digital-pianos", "portable digital pianos"), ("piano-benches-and-stands", "benches and stands"), ("piano-pedals", "pedals")]) + trust("a first piano"),
 [("Is the Casio PX-S1100 good for beginners?", "In my assessment, yes, especially for small spaces: scaled hammer action, two headphone jacks and a pedal in the box."),
  ("Does the PX-S1100 run on batteries?", "Casio lists six AA batteries as an option, with about four hours of continuous play, or an AC adaptor."),
  ("Has Dr. Pisarenko tested the PX-S1100?", "No. This is an assessment based on the specifications and what a teacher looks for, not a hands-on test.")]))
