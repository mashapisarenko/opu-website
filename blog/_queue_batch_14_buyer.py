# -*- coding: utf-8 -*-
"""Batch 14 (2026-11-16): ten buyer-intent articles, one per day 30 Jan - 8 Feb 2027, from _shop/topic_map_2026-11-14.md
(explainers, how-tos, comparisons and one Australian buyer guide that no live or queued article covers).
Product facts: _buyer_products.py (listing facts checked 2026-11-14) plus manufacturer pages opened 2026-11-16, noted below.
Build with:  python3 blog/_queue_batch_14_buyer.py   then   python3 blog/_make_post.py blog/_specs_batch_14_buyer.json blog/_queue
Rules: first person, adults who learn alone, no prices/ratings/Amazon images, no claim of hands-on testing, no Las Vegas signal."""
import json, pathlib
import _buyer_kit as K
from _buyer_kit import *
from _buyer_products import P, add

K.UPDATED = "November 16, 2026"
def lk(s, t): return '<a href="%s.html">%s</a>' % (s, t)
def meta():
    return ('<p style="margin:0 0 14px;font-size:.92rem;color:#5b6478"><strong>By Dr. Maria Pisarenko, DMA</strong> &middot; '
            'Last updated: November 16, 2026 &middot; Product details checked against the Amazon listing and the maker&#39;s page on that date or on November 14, 2026.</p>')
def top3(rows): return quick(rows, title="My top 3 picks")
S = []

# ---- facts opened on the makers' own pages, 2026-11-16 -------------------------------------------------------
add("evo4", "Audient EVO 4", "B084BGC5LR", "A beginner who wants two microphone inputs, so a stereo pair of microphones fits, in a small bus-powered box.",
 "Audient lists two microphone preamps, two inputs of which one is a JFET instrument input, two outputs, a headphone output, SmartGain, loopback, USB bus power and a USB-C connection. Its tech-spec page lists 48 V phantom power, a 360 g unit and a 1 m USB-C to USB-A cable in the box. I did not find MIDI on the pages I read.",
 "A layout I can read at a glance, and two microphone preamps. Two preamps are what let me recommend a stereo pair of microphones on a piano, which a one-preamp box cannot do.",
 ["Two microphone preamps, so a stereo pair fits", "SmartGain sets the input levels for you, which helps a beginner"],
 ["Audient's overview page does not state sample rate or bit depth", "I did not find MIDI on the pages I read"],
 "you may want to record a piano with two microphones.", "you will only ever record one microphone or one cable from a piano.",
 dict(type="2x2 USB-C interface", pre="2", inst="One of the two inputs", phones="One output", power="USB bus power", sw="Bundled software via ARC (titles not named on the overview page)", wt="360 g (Audient)"))
add("solo4", "Focusrite Scarlett Solo 4th Gen", "B0C5JSHP7M", "A pianist who records one microphone, or the stereo line from a digital piano, and wants a simple box.",
 "Focusrite lists one microphone preamp, one instrument input and one line input, two balanced line outputs, one headphone output, 24-bit/192 kHz converters, phantom power, loopback, Air mode, USB-C bus power, and software including Ableton Live Lite, Pro Tools Intro+ and Cubase LE. Its spec page does not list MIDI.",
 P["solo4"]["look"], P["solo4"]["pro"], P["solo4"]["con"], P["solo4"]["buy"], P["solo4"]["skip"],
 dict(type="2x2 USB-C interface", pre="1", inst="One instrument input and one line input", phones="One output", power="USB-C bus power", sw="Ableton Live Lite, Pro Tools Intro+, Cubase LE", wt="Not stated on the pages I read"))
add("bt500", "AirTurn BT500S-2", "B09S247V3D", "A pianist with sheet-music apps on an iPad or tablet who wants a dependable two-pedal turner.",
 "The Amazon listing says a two-pedal Bluetooth page turner. AirTurn lists a stompbox-style foot switch with quiet steel switches, Bluetooth for phones, tablets and computers with Bluetooth 4 or higher, an operating range of more than 200 feet, a rechargeable battery with more than 200 hours of play time per charge, seven built-in modes that store commands for hundreds of apps, a free AirTurn Manager app for custom commands, and a weight of 0.17 kg. AirTurn's page does not state the number of switches.",
 P["bt500"]["look"], P["bt500"]["pro"], ["Another device to charge and pair", "Pedal placement takes practice"], P["bt500"]["buy"], P["bt500"]["skip"],
 dict(type="Two-pedal Bluetooth (listing)", power="Rechargeable, 200+ hours (AirTurn)", conn="Bluetooth", wt="0.17 kg (AirTurn)"))
add("dragonfly", "PageFlip Dragonfly", "B06VT1C5ND", "A pianist who wants four pedals for more actions, or who prefers batteries to charging.",
 "The Amazon listing says a four-pedal Bluetooth page turner for sheet-music apps. PageFlip lists four illuminated pedals, Bluetooth 4.0 or a wired USB-C cable, two AA batteries said to last about 200 hours or about 200,000 page flips, a size of 7.0 x 6.7 x 2.2 inches and a weight of 488 g.",
 P["dragonfly"]["look"], ["Four illuminated pedals", "Takes ordinary AA batteries; can also be wired by USB-C"], ["Larger and heavier than a two-pedal unit", "More pedals than most adults will use"], P["dragonfly"]["buy"], P["dragonfly"]["skip"],
 dict(type="Four-pedal Bluetooth", power="Two AA batteries (PageFlip)", conn="Bluetooth 4.0 or USB-C cable", wt="488 g (PageFlip)"))
add("cdps360", "Casio CDP-S360", "B09S3XB13K", "A budget-minded adult beginner who wants a graded action, a pedal in the box and a light body.",
 "Casio lists 88 keys with Scaled Hammer Action Keyboard II, three touch-sensitivity levels plus off, 128-note polyphony, 700 tones, two oval 13 x 7 cm speakers with 8 W + 8 W output, one stereo mini headphone jack that also serves as an output, USB Type A and Type B ports, an SP-3 sustain pedal with a connector for the optional SP-34 three-pedal unit, a weight of 10.9 kg, and power from six AA batteries (about four hours) or the AC adaptor.",
 "That the bass keys feel heavier than the treble keys, the way a real piano does, that quiet notes answer at the touch I meant, and that fast repeated notes sound clean. The numbers cannot tell me that; the keys have to.",
 ["Scaled hammer action in a light body", "A sustain pedal is in the box, and the batteries make it portable"],
 ["One headphone jack, which also serves as the output, so a teacher cannot listen alongside you", "Plainer than the Roland and Yamaha pages in how much it explains"],
 "you want a graded action and a slim body at a modest cost.", "you want two headphone jacks or a wooden-key feel.",
 dict(type="Slim portable, 88 keys", action="Scaled Hammer Action Keyboard II", poly="128", phones="One (also the output)", weight="10.9 kg (Casio)"))


def AUurl(a): return "https://www.amazon.com.au/dp/%s?tag=musicalgalaxi-22" % a
def au(s):
    import re
    s = re.sub(r"https://www\.amazon\.com/dp/([A-Z0-9]+)\?tag=musicalgalaxi-20", lambda m: AUurl(m.group(1)), s)
    return s.replace("See it on Amazon &rarr;", "See it on Amazon Australia &rarr;")

SOURCES = {
 "evo": "<!-- Specs sources, opened 2026-11-16: Audient EVO 4 https://audient.com/products/audio-interfaces/evo-4/overview/ and https://audient.com/products/audio-interfaces/evo-4/tech-specs/ ; Focusrite Scarlett Solo 4th Gen spec page as opened 2026-11-14 -->",
 "turn": "<!-- Specs sources, opened 2026-11-16: AirTurn BT500S-2 https://www.airturn.com/products/airturn-bt500s-2-controller ; PageFlip Dragonfly https://pageflip.com/products/dragonfly -->",
 "casio": "<!-- Specs source, opened 2026-11-16: Casio CDP-S360 https://www.casio.com/us/electronic-musical-instruments/product.CDP-S360BK/ -->",
}

# 1 ---------------------------------------------------------------------------------------------------------
S.append(spec("do-i-need-an-audio-interface-for-a-digital-piano", "2027-01-30",
 "Do I Need an Audio Interface for a Digital Piano?",
 "Do I Need an Audio Interface for a Digital Piano?",
 "Do you need an audio interface for a digital piano? A concert pianist explains when USB or a cable is enough, and when an interface is worth buying.",
 "Most adults do not need one. Here is how to tell, and which three I would look at if you do.",
 meta() + """
<p>You do not need an audio interface to play a digital piano, to hear it through headphones, or to use it with most piano apps. You need one when you want to record the piano's sound with good quality, or to add a microphone, and your piano cannot send audio over its own USB cable. If you only want to practice, stop here and save your money.</p>
""" + DISC + top3([("Simplest", "solo4", "one microphone preamp and a line input for the piano"),
 ("Most room to grow", "evo4", "two microphone preamps, so a stereo pair fits"),
 ("If you own MIDI gear", "minifuse2", "a USB audio and MIDI interface")]) +
 how_i_choose("The question is not which interface is best. It is whether you need one at all, so I start with what you want to do, and only then with the box.") + """
<h2>What an audio interface actually does</h2>
<p>An audio interface is a small box that turns sound into a signal your computer can record, and turns the computer's signal back into sound for your headphones. It has inputs for microphones and instruments, a headphone output, and a USB cable to the computer. A digital piano already makes its own sound, so for a piano with a line output or a headphone jack, an interface is the clean way to get that sound into a recording program.</p>
<h2>When you do not need one</h2>
<ul>
<li><strong>You only practice.</strong> Headphones plugged into the piano are enough.</li>
<li><strong>You use a piano app or notation software.</strong> USB carries MIDI, which tells the software which notes you played. Many pianos have a computer USB port; Roland lists one on the FP-10, and Casio lists USB Type A and Type B ports on the CDP-S360. See """ + lk("how-to-connect-a-digital-piano-to-a-computer", "how to connect a digital piano to a computer") + """.</li>
<li><strong>Your piano sends audio over USB.</strong> Yamaha lists a 24-bit stereo USB audio interface on the P-225, which means a single cable can carry the piano's sound into a recording program. Check your manual for the same feature on your model.</li>
</ul>
<h2>When you do</h2>
<ul>
<li><strong>You want to record the sound, and your piano has no USB audio.</strong> Run a cable from the piano's line output into an interface.</li>
<li><strong>You want to record a microphone</strong>, for your voice or for an acoustic piano. A microphone needs a preamp, and an interface has one.</li>
<li><strong>You want to record a second instrument or a stereo pair of microphones.</strong> You then need two microphone inputs. Read """ + lk("best-audio-interface-for-beginners", "the best audio interface for beginners") + """.</li>
</ul>
<h2>What I would look at, in order</h2>
<p>First, the number of microphone preamps: one is enough for a digital piano's line output and a voice; two are needed for a stereo pair. Second, whether the headphone output is clear and quiet, because you will listen to your own playing on it. Third, whether it runs from the computer's USB cable, so there is no power brick. After those, I do not care about the feature list. A student who finds the box simple will record more often, and recording yourself is how you hear what your teacher would hear.</p>""" +
 pick("solo4", "The simplest answer for most adults, and the one I would suggest for a digital piano's line output.") +
 pick("evo4", "The one to buy if you think you will record an acoustic piano with two microphones one day.") +
 pick("minifuse2", "Worth a look if your keyboard has 5-pin MIDI ports as well as a line output.") + """
<h2>Comparison</h2>""" + SOURCES["evo"] +
 table(["Type", "Microphone preamps"], [[A("B0C5JSHP7M", "Focusrite Scarlett Solo 4th Gen"), "2x2 USB-C interface", "1"], [A("B084BGC5LR", "Audient EVO 4"), "2x2 USB-C interface", "2"],
  [A("B09HL3GD7G", "Arturia MiniFuse 2"), "USB audio and MIDI interface", "Not stated on the listing"]]) + """
<p>Once you have one, you need a place to put it. My guide to <a href="home-recording-corner-on-a-budget.html">a home recording corner on a budget</a> shows the small things that make it work, and """ + lk("best-microphone-for-recording-piano-at-home", "the best microphone for recording piano at home") + """ covers the next purchase.</p>""" +
 closing([("audio-interfaces-for-home-recording", "audio interfaces"), ("microphones-and-audio-interfaces", "microphones and interfaces"), ("music-cables-and-power", "cables and power")]) + trust("recording"),
 [("Do I need an audio interface to record my digital piano?", "Not always. If your piano sends audio over USB you can record with one cable. If it does not, an interface lets you record its line output cleanly."),
  ("Do I need an audio interface for MIDI?", "No. MIDI travels over a USB cable on most digital pianos, and the computer reads it directly."),
  ("Is a USB microphone a substitute?", "For a voice, often yes. For a stereo recording of a piano, an interface with two preamps and two microphones gives you more control.")]))

# 2 ---------------------------------------------------------------------------------------------------------
S.append(spec("how-to-record-a-digital-piano-without-a-microphone", "2027-02-01",
 "How to Record a Digital Piano Without a Microphone",
 "How to Record a Digital Piano Without a Microphone",
 "Three ways to record your digital piano with no microphone: USB audio, a cable to an interface, or a phone. A concert pianist explains what each needs.",
 "A digital piano already makes its own sound, so you can record it cleanly without a microphone. Here are three ways.",
 meta() + """
<p>You can record a digital piano without a microphone in three ways: over USB if the piano sends audio, with a cable from its output into an audio interface, or, for a quick practice take, by playing the sound through a phone's recorder. The first two give you the piano's own sound with none of the room in it, which is often what you want when you are checking notes and rhythm.</p>
""" + DISC + top3([("Simplest cable setup", "solo4", "a line input and a headphone output in one small box"),
 ("Lowest cost", "umc22", "a 2-in 2-out USB interface"),
 ("Most flexible", "evo4", "two microphone preamps if you add microphones later")]) +
 how_i_choose("A piano is sound before it is anything else, so I choose the route that keeps the piano's sound clean and the steps few. The fewer the steps, the more often a student actually records.") + """
<h2>Why record without a microphone at all?</h2>
<p>A microphone records the piano and everything near it: the room, the chair, the kettle in the next room. A digital piano's output carries only the instrument. For an adult learning alone this is an advantage. You hear your touch, your timing and your wrong notes without anything softening them, and that is the point of recording yourself. If you later want the sound of a room, that is a different tool; I cover it in """ + lk("how-to-record-an-acoustic-piano-with-two-microphones", "how to record an acoustic piano with two microphones") + """.</p>
<h2>Way 1: USB audio</h2>
<p>Some digital pianos send their sound over the USB cable as well as MIDI. Yamaha lists a 24-bit stereo USB audio interface on the P-225, for example, so one cable to your computer can carry the sound into a free recording program. Check your piano's manual for the words USB audio, not just USB MIDI. If the manual says MIDI only, the cable will tell the computer which notes you played but will not carry the sound.</p>
<h2>Way 2: a cable to an audio interface</h2>
<p>If your piano has a line output or a headphone output, you can run a cable from it to an interface and plug the interface into the computer. Use the line output if there is one, because the headphone output is shaped for headphones and can sound a little harsh when recorded. Focusrite lists one instrument input and one line input on the Scarlett Solo, which is why I suggest it here, and the interface's headphone output lets you listen without a delay. If you have never connected a piano to a computer, read """ + lk("how-to-connect-a-digital-piano-to-a-computer", "how to connect a digital piano to a computer") + """ first.</p>
<h2>Way 3: a phone for a quick take</h2>
<p>For a practice take that only you will hear, a phone's voice recorder held near the piano's speakers will do. It will not sound like a recording, but it will tell you whether your left hand came in on time. If you want to send me a recording for feedback, the free route on my site is the <a href="../submit.html">submit page</a>.</p>
<h2>What to listen for in your recording</h2>
<ul><li><strong>Evenness.</strong> Are the notes of a scale the same volume? Uneven notes mean uneven fingers.</li>
<li><strong>Rhythm.</strong> Are the long notes held to their full length? Count aloud as you listen.</li>
<li><strong>Pedal.</strong> Does the sound blur where the harmony changes?</li></ul>
<p>My guide to <a href="practicing-with-a-recording.html">practicing with a recording</a> explains how to use these takes without letting them replace your own listening.</p>""" +
 pick("solo4", "The box I would suggest for a digital piano's line output. It takes the stereo line and gives you a clear headphone output.") +
 pick("umc22", "A lower-cost route for a first recording. Check the listing for the cable it needs.") +
 pick("evo4", "If you might add microphones later, this keeps the door open.") + """
<p>For other ways to put these pieces together, see """ + lk("do-i-need-an-audio-interface-for-a-digital-piano", "do I need an audio interface for a digital piano?") + """ and """ + lk("best-recording-bundle-under-300", "the best recording bundle under $300") + """.</p>""" +
 closing([("audio-interfaces-for-home-recording", "audio interfaces"), ("record-yourself-playing", "gear to record yourself playing"), ("music-cables-and-power", "cables and power")]) + trust("recording"),
 [("Can I record a digital piano directly into a computer?", "Yes, if the piano sends audio over USB, or through an audio interface from its line or headphone output."),
  ("Why does my recording sound harsh?", "A headphone output is shaped for headphones. If your piano has a line output, use it instead."),
  ("Do I need to record at all?", "It helps. Listening to your own playing is one of the quickest ways to hear what needs work.")]))

# 3 ---------------------------------------------------------------------------------------------------------
S.append(spec("how-to-record-an-acoustic-piano-with-two-microphones", "2027-01-31",
 "How to Record an Acoustic Piano with Two Microphones",
 "How to Record an Acoustic Piano with Two Microphones",
 "How to record an acoustic piano in stereo with two microphones: the gear you need, where to place them, and what to listen for, from a concert pianist.",
 "Two matched microphones and a two-input interface give a piano its width. Here is the setup and the first placement to try.",
 meta() + """
<p>To record an acoustic piano in stereo you need two matching small-diaphragm condenser microphones, two stands, two XLR cables and an audio interface with two microphone preamps and phantom power. Put the pair a little above the strings, pointing at the hammers, listen on headphones, and move them until the middle of the piano sounds like a piano and not like a box.</p>
""" + DISC + top3([("A first matched pair", "m5", "small-diaphragm cardioid condensers, XLR"),
 ("Listed for pianos", "se7", "a stereo pair the listing names for pianos"),
 ("Interface with two preamps", "i2i2", "the box to plug a pair into")]) +
 how_i_choose("A stereo piano recording is a listening problem more than a gear problem. I start with a matched pair and a quiet room, and I trust my ears over any chart.") + """
<h2>What you need</h2>
<ul><li><strong>Two microphones of the same model.</strong> A matched pair has the same character on both sides, which a stereo image needs.</li>
<li><strong>An interface with two microphone preamps and phantom power.</strong> Condenser microphones need phantom power. Focusrite lists two microphone preamps and phantom power on the Scarlett 2i2, and Audient lists two on the EVO 4. A one-preamp box cannot do this.</li>
<li><strong>Two stands and two XLR cables.</strong> See <a href="../shop/mic-stands-and-studio-accessories.html">stands and accessories</a>.</li>
<li><strong>Headphones</strong> that let you hear what the microphones hear: """ + lk("best-headphones-for-digital-piano", "headphones for practice") + """.</li></ul>
<h2>Where to put them</h2>
<p>There is no single right place, and any numbers in a magazine are a starting point, not a rule. I begin with the lid up, the microphones a little above the strings and pointing down toward the hammers, one nearer the treble and one nearer the bass, and far enough back that I can hear the whole piano and not just the loudest strings. Then I play a slow chord progression, listen on headphones, and move one microphone at a time. If the bass booms, move back. If the treble is sharp, move out of line with the hammers.</p>
<h2>Check the middle of the piano</h2>
<p>The most common beginner mistake is a hole in the middle: the bass on the left, the treble on the right, and nothing between. Play a scale up the keyboard and listen for whether the sound travels smoothly from left to right. If it jumps, bring the microphones closer together or farther back. This is also where a matched pair earns its keep.</p>
<h2>The room matters as much as the microphones</h2>
<p>A bare room adds echo that no interface can remove. Soft furniture, curtains and a rug help more than a more expensive microphone. If you can, record when the house is quiet, and turn off anything that hums. For a first recording, my guide to <a href="home-recording-corner-on-a-budget.html">a home recording corner on a budget</a> shows what to change first.</p>
<h2>What if I only want a simple recording?</h2>
<p>A handheld stereo recorder is easier; read """ + lk("best-handheld-recorder-for-piano-practice", "the best handheld recorder for piano practice") + """. For a longer list of microphones, see """ + lk("best-stereo-microphones-for-piano", "the best pair of microphones for piano") + """.</p>""" +
 pick("m5", "A sensible first pair if you want to record in stereo and do not mind buying stands and cables separately.") +
 pick("se7", "I like that the maker names pianos in the listing, though I would still listen before trusting any claim.") +
 pick("i2i2", "The interface I would suggest to go with either pair: two preamps, phantom power and a clear headphone output.") + """
<p>If you want a step up in microphones, the """ + A("B0002PZ01C", "RODE NT5 matched pair") + """ and the """ + A("B07MZXKZVG", "LEWITT LCT 040 MATCH pair") + """ are the two I would look at next.</p>""" +
 closing([("microphones-and-audio-interfaces", "microphones and interfaces"), ("mic-stands-and-studio-accessories", "stands and accessories"), ("audio-interfaces-for-home-recording", "audio interfaces")]) + trust("recording"),
 [("Do I need two microphones to record a piano?", "No, but a stereo pair gives you width and a more natural sound than one microphone in the middle."),
  ("Can I use any interface?", "You need one with two microphone preamps and phantom power. A one-preamp box will not fit a pair."),
  ("Where do I put the microphones?", "Start a little above the strings, pointing toward the hammers, and move one at a time while you listen on headphones.")]))

# 4 ---------------------------------------------------------------------------------------------------------
add("keylab49", "Arturia KeyLab Essential 49 mk3", "B0C325NVBQ", "A player who wants a compact 49-key controller for software and apps, with more controls than a bare keyboard.",
 "The listing says a 49-key USB MIDI keyboard controller.",
 "At 49 keys it is not a piano, so I would use it for software, apps and ear training, not for learning repertoire. I would check that the keys have a firm, even touch.",
 ["49 keys in a compact body", "Made for software and apps"], ["Not 88 keys, so not for piano repertoire", "The listing gives few details"],
 "you want to use software and apps on a small desk.", "you want to learn piano pieces that use the whole keyboard.",
 dict(type="49-key controller", action="Not stated on the listing", sound="None of its own"))
add("mpkmini4", "Akai MPK Mini IV", "B0FT3N7TK1", "Someone who wants the smallest, cheapest way to play software instruments and has no plans to learn piano repertoire on it.",
 "The listing says a 25-key USB MIDI keyboard controller.",
 "With 25 keys it is a controller, not a piano. I would suggest it only for software and apps, not as a first instrument.",
 ["25 keys, very small", "Fits any desk"], ["Far too small to learn piano on", "The listing gives few details"],
 "you want to try software instruments and need the smallest keyboard.", "you want to learn to play the piano.",
 dict(type="25-key controller", action="Not stated on the listing", sound="None of its own"))
S.append(spec("how-to-use-a-midi-keyboard-with-a-laptop-or-ipad", "2027-02-02",
 "How to Use a MIDI Keyboard with a Laptop or iPad",
 "How to Use a MIDI Keyboard with a Laptop or iPad",
 "How to connect a MIDI keyboard to a laptop or iPad, which cable and adapter you may need, and what software to use, explained by a concert pianist.",
 "A MIDI keyboard makes no sound on its own. Here is how to connect one to a laptop or an iPad, and which keyboard I would choose.",
 meta() + """
<p>To use a MIDI keyboard with a laptop you usually need only the USB cable that comes with it. With an iPad you need the right adapter for the iPad's port, or a keyboard that connects by Bluetooth. Either way the keyboard sends notes to an app or program, and the app makes the sound. A MIDI keyboard on its own is silent.</p>
""" + DISC + top3([("Best touch for a pianist", "hammer88", "88 weighted hammer-action keys, no sound of its own"),
 ("Lower-cost 88 keys", "ks88", "88 semi-weighted keys for apps and software"),
 ("Compact desk keyboard", "keylab49", "49 keys for software and apps")]) +
 how_i_choose("A MIDI keyboard has no sound of its own, so what I judge is the keys, because the keys are what you will practice on. The software can change tomorrow; your hands will remember the touch.") + """
<h2>What MIDI is, in one paragraph</h2>
<p>MIDI is not sound. It is a message that says which key you pressed, how hard and for how long. The computer or tablet reads those messages and plays a piano sound it already holds. That is why a MIDI keyboard is called a controller, and why it needs software or an app. My guide <a href="weighted-vs-semi-weighted-keys.html">weighted vs semi-weighted keys</a> explains why the keys matter for a pianist.</p>
<h2>With a laptop</h2>
<ol><li>Plug the keyboard's USB cable into the laptop. Most laptops recognize it with no driver.</li>
<li>Open the app or program you want to play, and check its settings for the MIDI input. Choose your keyboard.</li>
<li>Play a note. If you hear nothing, check that the program has a piano sound loaded and that the laptop's volume is up.</li></ol>
<h2>With an iPad</h2>
<ol><li>Check the iPad's port. Some have USB-C and need only a USB-C cable; older ones use a Lightning port and need an adapter.</li>
<li>If the keyboard needs more power than the iPad can give, use a powered adapter or a powered USB hub.</li>
<li>Open your app and choose the keyboard as the MIDI input.</li></ol>
<p>I have not listed the exact adapter for each iPad here, because the right one depends on your iPad and your keyboard; check Apple's page for your model before you buy.</p>
<h2>Which software should I use?</h2>
<p>Start with a free program. Many piano-learning apps, notation programs and recording programs accept a MIDI keyboard. If you are learning from my <a href="../free-course.html">free 41-lesson course</a>, you do not need software at all; a MIDI keyboard becomes useful when you want to record yourself or use an app to practice reading notes.</p>
<h2>Which keyboard should I buy?</h2>
<p>If you want to learn piano repertoire on it, choose 88 keys with a weighted action. If you want a small desk keyboard for software only, 49 keys will do. A 25-key keyboard is a toy for a pianist; it is for sound design, not for learning to play. If a keyboard that makes its own sound is better for you, read """ + lk("best-88-key-weighted-midi-controller", "the best 88-key weighted MIDI controller") + """ and """ + lk("best-digital-piano-for-adult-beginners", "my digital piano guide for adult beginners") + """.</p>""" +
 pick("hammer88", "The one I would suggest if you want a silent, weighted keyboard that connects to a computer or tablet.") +
 pick("ks88", "A lower-cost way to have 88 keys for apps, but check that you are happy with the lighter touch.") +
 pick("keylab49", "For software and apps on a small desk, when learning repertoire is not the goal.") + """
<p>For a keyboard that is also a piano, see """ + lk("best-digital-pianos-2026", "my digital piano list for 2026") + """.</p>""" +
 closing([("midi-keyboard-controllers", "MIDI keyboard controllers"), ("keyboards", "keyboards and MIDI"), ("music-cables-and-power", "cables and power")]) + trust("a MIDI keyboard"),
 [("Do I need a driver for a MIDI keyboard?", "Most laptops and tablets recognize a MIDI keyboard without one. Check the maker's page if yours does not appear."),
  ("Can I connect a MIDI keyboard to an iPad?", "Yes, with the right cable or adapter for your iPad's port, or by Bluetooth if the keyboard supports it."),
  ("Why is my MIDI keyboard silent?", "A MIDI keyboard makes no sound of its own. Open an app with a piano sound loaded and turn up the volume.")]))

# 5 ---------------------------------------------------------------------------------------------------------
add("dt770x", "beyerdynamic DT 770 Pro X (48 Ohm)", "B0F13TRHXS", "A pianist who wants a closed-back studio headphone that a phone or a piano's headphone jack can drive.",
 "The listing says closed-back studio headphones rated at 48 ohms.",
 "Comfort for an hour, a clear middle, and a bass that does not hide the left hand. I would also check that a low-impedance model is loud enough from my piano's headphone jack.",
 ["Closed-back, so little sound leaks", "48 ohms is easier for a piano or a phone to drive"], ["Higher cost than the entry pairs", "The listing gives few details"],
 "you want a studio headphone for long practice sessions.", "you want the lowest cost.",
 dict(type="Closed-back studio, 48 ohm (listing)"))
S.append(spec("best-closed-back-headphones-for-piano-practice", "2027-02-03",
 "Best Closed-Back Headphones for Piano Practice (2027)",
 "Best Closed-Back Headphones for Piano Practice",
 "The best closed-back headphones for piano practice, chosen by a concert pianist: why closed-back suits a digital piano, and three pairs to look at.",
 "Closed-back headphones keep the sound in and the room out. Here is why I prefer them for practice, and three I would look at.",
 meta() + """
<p>For piano practice I recommend closed-back headphones, because they keep the sound of the piano in your ears and out of the room, and they keep the room out of your ears. The three I would look at first are the Sennheiser HD 280 Pro, the Audio-Technica ATH-M50x and the beyerdynamic DT 770 Pro X. This is a pianist's assessment of what the listings say, not a hands-on test.</p>
""" + DISC + top3([("Quiet and plain", "hd280", "closed-back studio headphones"),
 ("A well-known classic", "m50x", "closed-back studio monitor headphones"),
 ("Easy to drive", "dt770x", "closed-back studio headphones rated at 48 ohms")]) +
 how_i_choose("Headphones are what you hear your own touch through, so I look at comfort first, then whether the middle of the sound is clear, then whether the bass is steady, and last at whether the leakage is low.") + """
<h2>Why closed-back?</h2>
<p>Open-back headphones let sound pass through the earcups. They can sound airy, but they let the sound out and the room in, which defeats the purpose if you practice at night, in an apartment, or with other people in the house. Closed-back headphones seal the sound in. On a digital piano, that means the piano is the only thing you hear, and nobody else hears it. If you live in a small space, read """ + lk("practicing-piano-in-an-apartment", "how to practice piano in an apartment") + """.</p>
<h2>What I look for</h2>
<ul><li><strong>Comfort for an hour.</strong> You will wear them for as long as a lesson.</li>
<li><strong>A clear middle.</strong> A piano's melody lives there. Headphones that scoop the middle make the melody harder to follow.</li>
<li><strong>Steady bass.</strong> Boomy bass makes you play the left hand too softly.</li>
<li><strong>Whether your piano can drive them.</strong> A high-impedance pair can sound quiet from a piano's headphone jack. A lower figure, such as the 48 ohms in the DT 770 Pro X listing, is easier to drive.</li>
<li><strong>A cable that is long enough</strong> to reach the piano from your bench.</li></ul>
<h2>A note on adapter plugs</h2>
<p>Many digital pianos have a quarter-inch jack and many headphones have a small plug with an adapter, or the other way round. Check what is in the box. For the longer list, see """ + lk("best-headphones-for-digital-piano", "the best headphones for digital piano") + """ and the <a href="../shop/headphones-for-piano.html">headphones page in my shop</a>.</p>""" +
 pick("hd280", "A plain closed-back pair that I would suggest to a pianist who practices at night.") +
 pick("m50x", "A well-known choice; I would try the earcups for comfort over an hour before deciding.") +
 pick("dt770x", "A step up in cost and the one I would choose if I wanted a lower-impedance pair for a piano's headphone jack.") + """
<h2>What about the lower-cost pair?</h2>
<p>The """ + A("B00HVLUR18", "Audio-Technica ATH-M20x") + """ is a closed-back pair at a lower cost. Audio-Technica's own page, which I opened on November 16, 2026, lists 40 mm drivers, 47 ohms and a 15 to 20,000 Hz response, and also says the model is currently unavailable from the maker, so check the Amazon listing is new stock before you buy.</p>
<!-- Source for the ATH-M20x figures, opened 2026-11-16: https://www.audio-technica.com/en-us/ath-m20x -->
<h2>How to try them at home</h2>
<p>Put the headphones on and play something slow that you know well, such as a hymn or the first piece in your course. Listen for three things. Can you hear the quiet notes at the end of a phrase, or do they vanish? Does the left hand sound like a supporting voice, or does it boom? And after twenty minutes, are your ears and the top of your head still comfortable? A pair that passes those three tests is the right pair, whatever the label says. If your piano has a second jack, ask a friend to put the other pair on and tell you what they hear.</p>
<h2>Which should you buy?</h2>
<p>If you want the plain choice, the HD 280 Pro. If you want a classic you can find in many studios, the M50x. If your piano's jack seems quiet, the DT 770 Pro X. Whichever you choose, buy from a seller with a return policy, so you can wear them for an evening before you decide.</p>""" +
 closing([("headphones-for-piano", "headphones for piano"), ("piano-accessories", "piano accessories"), ("music-cables-and-power", "cables and power")]) + trust("headphones"),
 [("Are closed-back headphones better for piano practice?", "For most adults, yes. They keep the sound in and the room out, which suits an apartment or night practice."),
  ("Do I need expensive headphones?", "No. Comfort and a clear middle matter more than the price."),
  ("Do headphones change how I play?", "They change what you hear. A pair with a boomy bass can make the left hand sound louder than it is, so try yours with a recording you know.")]))

# 6 ---------------------------------------------------------------------------------------------------------
S.append(spec("best-music-gifts-under-100-for-pianists", "2027-02-04",
 "Best Music Gifts Under $100 for Pianists (Teacher's Picks)",
 "Best Music Gifts Under $100 for Pianists",
 "Useful gifts under $100 for someone who plays piano, chosen by a concert pianist: a stand light, a metronome, headphones, a book clip and a book.",
 "Six gifts under $100 that a pianist will use every week, with what to check on each before you buy.",
 meta() + """
<p>The best gifts under $100 for a pianist are the ones they will use every week: a light for the music stand, a metronome, a pair of closed-back headphones, a clip that holds a music book open, and a good book about music. When I checked on November 14, 2026, each item below was listed under $100 on Amazon; prices move, so check today's price before you order.</p>
""" + DISC + top3([("A light for the music desk", "mightybright", "an orchestra-style stand light"),
 ("A dependable metronome", "korgkdm3", "a digital metronome with memory backup"),
 ("A book to read", "musicophilia", "a book on music and the brain")]) +
 how_i_choose("I choose a gift for how often it will be used and how little it asks of the person receiving it. A gift that needs setting up, or that duplicates what they already own, becomes clutter.") + """
<h2>For the pianist who practices in the evening</h2>""" +
 pick("mightybright", "A well-known stand light. A good light matters more than people expect, because a dim music desk makes reading tiring.") +
 pick("glocusent", "A lower-cost alternative that clips on. Check that the clip fits the music desk before you buy.") + """
<h2>For the pianist who wants to keep time</h2>""" +
 pick("korgkdm3", "A dependable, plain metronome. A student who plays with a metronome learns to hear a steady pulse. My guide to <a href=\"what-the-metronome-is-actually-for.html\">what the metronome is actually for</a> explains how to use it.") + """
<h2>For the pianist who needs a book to stay open</h2>""" +
 pick("bookclip", "A very small gift that solves a real problem: a thick book that will not stay open. Check it fits the book's thickness.") + """
<h2>For the pianist who practices at night</h2>""" +
 pick("hd280", "A plain closed-back pair. See <a href=\"best-closed-back-headphones-for-piano-practice.html\">the best closed-back headphones for piano practice</a> for the others I would look at.") + """
<h2>For the pianist who likes to read</h2>""" +
 pick("musicophilia", "A book about music and the brain, not about technique. It suits a person who enjoys ideas more than exercises.") + """
<h2>How to choose</h2>
<ul><li>If the pianist plays at night, the light or the headphones.</li><li>If they practice with a book, the clip.</li><li>If you do not know what they have, the book.</li></ul>
<p>For something that needs no guesswork, a <a href="../gift-certificate.html">gift certificate for online piano lessons</a> is a gift they can use when they are ready. For more ideas, read """ + lk("best-birthday-gifts-for-a-pianist", "the best birthday gifts for a pianist") + """ and my <a href="../shop/gifts-for-pianists.html">gifts page</a>.</p>""" +
 closing([("gifts-for-pianists", "gifts for pianists"), ("gifts-for-music-lovers", "gifts for music lovers"), ("practice-tools", "practice tools")]) + trust("a gift"),
 [("What is a good gift for a pianist under $100?", "A stand light, a metronome, closed-back headphones, a book clip or a book about music."),
  ("What if I do not know what they own?", "Choose something small and consumable, such as the book clip, or give a gift certificate for lessons."),
  ("Are these prices fixed?", "No. They were each under $100 when I checked on November 14, 2026. Check today's price on Amazon.")]))

# 7 ---------------------------------------------------------------------------------------------------------
S.append(spec("airturn-bt500s-2-vs-pageflip-dragonfly", "2027-02-05",
 "AirTurn BT500S-2 vs PageFlip Dragonfly: Which Page Turner?",
 "AirTurn BT500S-2 vs PageFlip Dragonfly",
 "AirTurn BT500S-2 or PageFlip Dragonfly for turning pages on an iPad? A concert pianist compares pedals, power, size and apps from the makers' own pages.",
 "Two Bluetooth page turners for an iPad or tablet. Here is how they differ, and which one I would choose.",
 meta() + """
<p>For most adults who read sheet music from an iPad, I would choose the AirTurn BT500S-2: it is small, quiet, and has a rechargeable battery that AirTurn says lasts more than 200 hours. The PageFlip Dragonfly is the one to choose if you want four pedals, ordinary AA batteries, or a wired option. This is an assessment of the makers' pages, not a hands-on test.</p>
""" + DISC + top3([("Simplest", "bt500", "two pedals, rechargeable battery"),
 ("Most pedals", "dragonfly", "four illuminated pedals, AA batteries"),
 ("For the stand", "hercules", "an adaptive holder for a tablet or phone")]) +
 how_i_choose("A page turner has one job: to let you keep both hands on the piano. So I choose the one that is quietest under the foot, easiest to forget about, and least likely to need an hour's setup.") + """
<h2>Specifications</h2>""" + SOURCES["turn"] +
 table(["AirTurn BT500S-2", "PageFlip Dragonfly"], [["Pedals", "Two (listing); AirTurn's page does not state the number", "Four illuminated pedals"],
  ["Connection", "Bluetooth 4 or higher host, range 200+ feet", "Bluetooth 4.0 or wired USB-C cable"],
  ["Power", "Rechargeable, 200+ hours per charge", "Two AA batteries, about 200 hours or 200,000 page flips"],
  ["Apps", "Seven built-in modes covering hundreds of apps; free AirTurn Manager app", "iOS: forScore, OnSong, Newzik and more; Android: MobileSheets, SongBook and more"],
  ["Size and weight", "115 x 70 x 48 mm, 0.17 kg", "7.0 x 6.7 x 2.2 in, 488 g"]], first="Item") + """
<h2>What I look for</h2>
<ul><li><strong>Quiet pedals.</strong> A click that the microphone or the audience can hear is a cost.</li>
<li><strong>Stays put.</strong> A pedal that slides on a wooden floor is worse than none.</li>
<li><strong>Battery you will not forget.</strong> A rechargeable battery is only good if you remember to charge it; AA batteries are easy to replace.</li>
<li><strong>Works with your app.</strong> Check that your sheet-music app is on the maker's list.</li></ul>
<h2>How do they differ?</h2>
<p>The AirTurn is the smaller and lighter of the two, and AirTurn says the battery lasts more than 200 hours per charge. The Dragonfly is bigger, with four pedals that can do more than turn pages forward and back, and it takes ordinary AA batteries. For an adult who only needs forward and back, more pedals are more to learn. For a player who wants to jump to a marked place, they are useful. I would pair either with a good tablet holder; see """ + lk("best-tablet-for-sheet-music", "the best tablet for sheet music") + """ and """ + lk("best-page-turner-pedal-for-ipad", "the best page-turner pedal for iPad") + """.</p>""" +
 pick("bt500", "My choice for most adults: small, quiet to the eye, and easy to leave in the case.") +
 pick("dragonfly", "My choice if you want four actions or prefer replacing AA batteries to charging.") +
 pick("hercules", "Not a page turner, but the holder I would suggest for keeping a tablet or a phone where you can see it.") + """
<p>If you have never used an app for sheet music, read """ + lk("how-to-start-sight-reading", "how to start sight-reading") + """ first; reading is the skill, and the pedal only helps it.</p>""" +
 closing([("ipad-music-stands-and-page-turners", "tablet stands and page turners"), ("music-stands", "music stands"), ("practice-tools", "practice tools")]) + trust("page turning"),
 [("Which page turner is better, AirTurn or PageFlip?", "AirTurn for simplicity and size; PageFlip if you want four pedals or AA batteries."),
  ("Do page turners work with every app?", "No. Check that your app is on the maker's compatibility list."),
  ("Do I need a page turner?", "Only if you read from a tablet and want both hands free. Paper music does not need one.")]))

# 8 ---------------------------------------------------------------------------------------------------------
S.append(spec("audient-evo-4-vs-focusrite-scarlett-solo", "2027-02-06",
 "Audient EVO 4 vs Focusrite Scarlett Solo: Which Interface?",
 "Audient EVO 4 vs Focusrite Scarlett Solo",
 "Audient EVO 4 or Focusrite Scarlett Solo 4th Gen for recording piano? A concert pianist compares preamps, inputs and power from the makers' pages.",
 "Two small USB interfaces. The key difference for a pianist is how many microphones each can record at once.",
 meta() + """
<p>The difference that matters for a pianist is the number of microphone preamps. Audient lists two on the EVO 4, so a stereo pair of microphones fits. Focusrite lists one on the Scarlett Solo, which is enough for a digital piano's line output or a single microphone, but not for a stereo pair. If you may ever record an acoustic piano in stereo, choose the EVO 4; if you will only record a digital piano or your voice, the Solo is enough.</p>
""" + DISC + top3([("For a stereo pair", "evo4", "two microphone preamps"),
 ("For a digital piano or one microphone", "solo4", "one preamp, one instrument and one line input"),
 ("If you want a third option", "i2i2", "two preamps, plus Auto Gain and Clip Safe")]) +
 how_i_choose("I compare what each interface lets you plug in, because that decides what you can record. Sound quality at this level matters less than whether the box can do what you need.") + """
<h2>Specifications</h2>""" + SOURCES["evo"] +
 table(["Audient EVO 4", "Focusrite Scarlett Solo 4th Gen"], [["Microphone preamps", "Two", "One"],
  ["Other inputs", "One of the two inputs is a JFET instrument input", "One instrument input and one line input"],
  ["Outputs", "Two, plus a headphone output", "Two balanced line outputs and one headphone output"],
  ["Phantom power", "48 V, per Audient's tech specs", "Yes"],
  ["Power and connection", "USB bus power, USB-C", "USB-C bus power"],
  ["Software", "Bundled software via ARC (titles not named on the overview page)", "Ableton Live Lite, Pro Tools Intro+, Cubase LE"],
  ["MIDI", "Not found on the pages I read", "Not listed"],
  ["Weight", "360 g", "Not stated on the pages I read"]], first="Item") + """
<h2>What this means for a pianist</h2>
<p>If you own a digital piano, the Solo's line input takes the piano's stereo output and gives you a clean recording and a clear headphone output. If you own an acoustic piano and want to record it, a pair of microphones needs two preamps, which is the EVO 4. Both interfaces run from the computer's USB cable, so there is no power brick to find. Audient says SmartGain sets the level on both inputs for you, and Focusrite lists Air mode; I cannot tell you how either sounds, and I would not choose on a feature name. Read the other guides if you are still deciding: """ + lk("best-audio-interface-for-beginners", "the best audio interface for beginners") + """, """ + lk("focusrite-scarlett-solo-vs-2i2", "Scarlett Solo vs 2i2") + """ and """ + lk("do-i-need-an-audio-interface-for-a-digital-piano", "do I need an audio interface for a digital piano?") + """.</p>""" +
 pick("evo4", "My choice if there is any chance you will record an acoustic piano with two microphones.") +
 pick("solo4", "My choice if you will record a digital piano or a single microphone.") +
 pick("i2i2", "The Focusrite model with two preamps, if you prefer that maker and want a stereo pair.") +
 closing([("audio-interfaces-for-home-recording", "audio interfaces"), ("microphones-and-audio-interfaces", "microphones and interfaces"), ("home-studio-starter-kits", "home studio starter kits")]) + trust("recording"),
 [("How many microphones can the EVO 4 record at once?", "Audient lists two microphone preamps on the EVO 4, so two."),
  ("Is the Scarlett Solo enough for a digital piano?", "Yes. It has an instrument input and a line input, which suit a digital piano's output."),
  ("Which is better for a beginner?", "Either is simple. The EVO 4 gives you room to grow; the Solo is the simplest box for one source.")]))

# 9 ---------------------------------------------------------------------------------------------------------
S.append(spec("casio-cdp-s360-review", "2027-02-07",
 "Casio CDP-S360 Review: A Piano Teacher's Assessment",
 "Casio CDP-S360 Review: A Piano Teacher's Assessment",
 "A concert pianist assesses the Casio CDP-S360 for adult beginners: key action, pedal, headphones, speakers and batteries, from Casio's own specifications.",
 "I have not played this piano for weeks and I do not claim to. Here is what its specifications tell a teacher, and who I would suggest it to.",
 meta() + """
<p><strong>A note on method.</strong> This is an assessment, not a hands-on test. I have not played the CDP-S360 for weeks and I do not claim to. I read Casio's specification page and the Amazon listing as a pianist and teacher, and tell you what I look for and whether I would recommend it.</p>
<p><strong>My verdict:</strong> I would recommend the CDP-S360 to an adult beginner who wants a graded action, a sustain pedal in the box and a light body at a modest cost. I would not choose it if you want two headphone jacks, so that a teacher can listen alongside you, or if you want a wooden-key feel.</p>
""" + DISC + top3([("Verdict", "cdps360", "scaled hammer action, 128-note polyphony, pedal in the box"),
 ("A step up in sound", "fp30x", "a stronger speaker system"),
 ("Lower-cost alternative", "fp10", "a compact piano with escapement")]) + """
<h2>What Casio says</h2>""" + SOURCES["casio"] + """
<p>Casio lists 88 keys with Scaled Hammer Action Keyboard II, three touch-sensitivity levels plus off, 128-note polyphony, 700 tones, two oval 13 x 7 cm speakers with 8 W + 8 W output, one stereo mini headphone jack that also serves as an output, USB Type A and Type B ports, an SP-3 sustain pedal with a connector for the optional SP-34 three-pedal unit, and a weight of 10.9 kg. It can run on six AA batteries, which Casio says last about four hours, or on the AC adaptor.</p>
<h2>What I look for, and how it answers</h2>
<ul><li><strong>A graded action.</strong> Scaled hammer action means the bass keys are heavier than the treble keys, the way a real piano is. That is the most important line on the page.</li>
<li><strong>A pedal in the box.</strong> A sustain pedal is where many first purchases fall short. Casio lists one with the piano. For a better one later, read """ + lk("best-sustain-pedal-for-digital-piano", "the best sustain pedals for digital piano") + """.</li>
<li><strong>Polyphony.</strong> 128 notes is enough for most beginner and early-intermediate pieces with the pedal down. See my explanation in """ + lk("best-digital-pianos-2026", "my digital piano list") + """.</li>
<li><strong>Headphones.</strong> One jack is the limit. If you want a second person to listen, it will not do.</li>
<li><strong>Touch sensitivity.</strong> Three levels plus off lets you match the response to your hands.</li></ul>
<h2>Who it is for</h2>
<p>It suits a student who wants an affordable first piano with a proper action and who will practice with headphones. A light body means it is easy to move to a table or a stand, and the batteries allow practice where there is no socket, though only for a few hours. If you want to record or connect to an app, the USB ports are there, but check my guide to """ + lk("how-to-connect-a-digital-piano-to-a-computer", "connecting a digital piano to a computer") + """ before assuming it sends audio over USB; Casio's page lists the ports, not the audio feature.</p>
<h2>Who should look elsewhere</h2>
<p>If you want two headphone jacks, look at the Yamaha P-225. If you want a larger sound from the speakers, look at the Roland FP-30X. If you need the smallest and lightest option, read """ + lk("best-portable-digital-piano", "the best portable digital piano") + """.</p>""" +
 pick("cdps360", "I would recommend it to a first-year adult beginner who wants a graded action at a modest cost.") +
 pick("fp30x", "The step up in sound I would look at if you will not always wear headphones.") +
 pick("fp10", "A compact alternative with a good key feel.") +
 closing([("digital-pianos", "portable digital pianos"), ("piano-pedals", "pedals"), ("piano-benches-and-stands", "benches and stands")]) + trust("a first piano"),
 [("Is the Casio CDP-S360 good for beginners?", "In my assessment, yes, because it has a graded hammer action, a sustain pedal in the box and a light body."),
  ("Does the CDP-S360 have two headphone jacks?", "No. Casio lists one stereo mini jack, which also serves as an output."),
  ("Has Dr. Pisarenko played the CDP-S360?", "No. This is an assessment based on the specifications and what a pianist looks for, not a hands-on test.")]))

# 10 --------------------------------------------------------------------------------------------------------
S.append(spec("best-digital-piano-for-adult-beginners-in-australia", "2027-02-08",
 "Best Digital Piano for Adult Beginners in Australia",
 "Best Digital Piano for Adult Beginners in Australia",
 "Digital pianos for Australian adult beginners, chosen by a concert pianist: five models with listings on Amazon Australia, and what to check before you order.",
 "If you live in Australia, here are the beginner digital pianos I found listed on Amazon Australia, and what I would check on each page.",
 meta() + """
<p>The best digital piano for an adult beginner in Australia is the same as anywhere: 88 weighted keys, a real piano sound, a sustain pedal and a headphone jack. The question for an Australian buyer is whether the model is sold on Amazon Australia. On November 16, 2026 I searched Amazon Australia for each model below and found a listing with the same code as the US page. My links below go to Amazon Australia.</p>
""" + au(DISC) + au(top3([("Best key feel", "fp10", "a PHA-4 Standard keyboard with escapement"),
 ("Best for a small flat", "pxs1100", "a slim, light body"),
 ("Best sound", "fp30x", "256-note polyphony and a stronger speaker system")])) +
 how_i_choose("Australian buyers are choosing from the same pianos as everyone else, so I start with the key action, then the pedal, then the headphone jacks, and leave the feature list for last.") + """
<h2>What should an Australian buyer check?</h2>
<p>Check the power supply. Australia uses 230 V with its own plug, so the listing for your country should say that the power supply in the box suits Australian sockets; if it does not, ask the seller before you order. Check delivery for a large box to your state, and decide where the piano will stand before it arrives. A bench is sometimes called a piano stool in Australia; choose one that adjusts so your forearms sit level with the keys. A sustain pedal is the same everywhere.</p>
<h2>Which digital pianos did I find on Amazon Australia?</h2>
<p>I looked for the models in my US lists and kept the five whose Amazon Australia listing has the same code as the US page. The Yamaha P-225 and P-145BT are sold in Australia, but under different listing codes from my US pages, so I have left them out rather than send you to a page I had not matched.</p>""" +
 au(pick("fp10", "The best touch I can point to for a modest budget, in a compact body.")) +
 au(pick("pxs1100", "A good answer to a small flat. It is slim, and it has two headphone jacks.")) +
 au(pick("fp30x", "A bigger sound than the compact models. It is heavier, so it suits a piano that stays put.")) +
 au(pick("p45", "A sensible first piano if you want a Yamaha. Read the listing carefully, because it states few specifications.")) +
 """
<h2>Comparison</h2>
<p>The fifth model in the table, the Casio CDP-S360, has a light body and a pedal in the box; I explain what I look for in it in my <a href="casio-cdp-s360-review.html">assessment of the CDP-S360</a>.</p>""" +
 au(table(["Type", "Key action", "Polyphony", "Headphone jacks"], trows(["fp10", "fp30x", "pxs1100", "p45", "cdps360"], ["type", "action", "poly", "phones"]))) + """
<p>Not every model in my US shop is sold in Australia, and a listing code that is the model you want in the US can be missing, or can be a different model, on Amazon Australia. When you click a link, check that the page that opens is the model you expect.</p>
<h2>How to choose</h2>
<ul><li><strong>Start with the keys.</strong> Read """ + lk("weighted-vs-semi-weighted-keys", "weighted vs semi-weighted keys") + """.</li>
<li><strong>Then the number of keys.</strong> Read """ + lk("how-many-keys-do-i-need-piano", "how many keys do I need on a piano?") + """.</li>
<li><strong>Then the pedal and the bench.</strong> See """ + lk("best-sustain-pedal-for-digital-piano", "the best sustain pedals") + """.</li>
<li><strong>Then the headphones.</strong> See """ + lk("best-closed-back-headphones-for-piano-practice", "closed-back headphones for piano practice") + """.</li></ul>
<p>I have also written guides for readers in <a href="best-digital-pianos-for-adult-beginners-in-canada.html">Canada</a> and <a href="best-digital-pianos-for-adult-beginners-in-the-uk.html">the UK</a>. The longer lists are in the shop: <a href="../shop/digital-pianos.html">portable digital pianos</a>, <a href="../shop/home-digital-pianos.html">home digital pianos</a> and the <a href="../shop/pianos.html">pianos department</a>.</p>""" +
 closing([("digital-pianos", "portable digital pianos"), ("piano-benches-and-stands", "benches and stands"), ("headphones-for-piano", "headphones")]) + trust("a first piano"),
 [("Do these links go to Amazon Australia?", "Yes. The product links in this guide open the Amazon Australia page for each model. Check that the page that opens is the model you expect."),
  ("Which digital piano should an Australian adult beginner buy?", "One with 88 weighted keys, a real piano sound and a sustain pedal. The Roland FP-10 is a simple start, and the Roland FP-30X is a step up in sound."),
  ("Will the power supply fit Australian sockets?", "Check the listing for your country. Australia uses a 230 V supply and its own plug, so ask the seller if the page does not say.")]))

if __name__ == "__main__":
    p = pathlib.Path(__file__).resolve().parent / "_specs_batch_14_buyer.json"
    p.write_text(json.dumps(S, indent=1, ensure_ascii=False), encoding="utf-8")
    print("wrote", p.name, len(S))
