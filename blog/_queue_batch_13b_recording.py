# -*- coding: utf-8 -*-
# Written 2026-11-14: buyer-intent batch 13, part B (recording gear, gifts). Same rules as part A.
from _buyer_kit import *
def lk(s, t): return '<a href="%s.html">%s</a>' % (s, t)
S = []

# 12 gifts: recording hobbyist ------------------------------------
S.append(spec("best-gifts-for-a-home-recording-hobbyist", "2026-11-17",
 "Best Gifts for a Home Recording Hobbyist (2026): A Pianist's Guide",
 "Best Gifts for a Home Recording Hobbyist (2026)",
 "Gift ideas for someone who records music at home, chosen by a concert pianist: interfaces, handheld recorders and headphones that suit a pianist or a singer.",
 "Choosing a gift for someone who records their own music is easier than it looks. Here are the pieces I would give a pianist.",
 meta_line() + """
<p>The best gifts for a home recording hobbyist are the ones that remove a step between them and a good recording: an audio interface such as the Focusrite Scarlett Solo, a handheld recorder such as the Zoom H4 Essential, or a pair of closed-back studio headphones. I chose these from what Amazon listed on November 14, 2026.</p>
""" + DISC + quick([("Best overall gift", "solo4", "a simple interface for a microphone or a piano&#39;s line out"),
 ("Best for a pianist", "h4ess", "a handheld recorder with XY microphones and 32-bit float"),
 ("Best small gift", "hd280", "closed-back studio headphones")]) +
 how_i_choose("A good gift fits what the person already owns. If you do not know, a handheld recorder and headphones are safe, because neither needs another device to work.") + """
<h2>The gifts</h2>""" +
 pick("solo4", "A good gift for someone who already has a microphone. Check they own a computer with a USB-C port or an adaptor.") +
 pick("h4ess", "A safe gift because it works without a computer. Include a microSD card.") +
 pick("hd280", "A pair of closed-back headphones is a gift almost every recordist uses.") + """
<h2>Comparison</h2>""" +
 table(["Type", "Key feature"], [[A(P[k]["a"], P[k]["n"]), P[k]["t"].get("type", ""), P[k]["t"].get("feat", "Closed-back studio headphones (listing)")] for k in ["solo4", "h4ess", "hd280"]]) + """
<h2>How to choose a gift</h2>
<ul><li>If they record piano, a handheld recorder or a stereo pair is more useful than a single microphone.</li><li>If they record voice, an interface with a microphone preamp is the better gift.</li><li>If you are unsure, a gift certificate for a lesson, or a """ + '<a href="../gift-certificate.html">gift certificate for online piano lessons</a>' + """, needs no guesswork.</li></ul>
<p>For more ideas, see """ + lk("best-gifts-for-piano-players-2026", "best gifts for piano players") + """ and """ + lk("best-microphone-for-recording-piano-at-home", "the best microphone for recording piano at home") + """.</p>""" +
 closing([("record-yourself-playing", "gear to record yourself playing"), ("audio-interfaces-for-home-recording", "audio interfaces"), ("gifts-for-pianists", "gifts for pianists")]) + trust("a gift for a recordist"),
 [("What is a good first gift for someone who records at home?", "A handheld recorder or a simple audio interface. Both remove a step from recording."),
  ("What if I do not know what they own?", "Closed-back studio headphones are used by almost every recordist and need nothing else."),
  ("Is a gift certificate for lessons a good idea?", "Yes, for someone who plays. It needs no guesswork about gear.")]))

# 13 birthday gifts pianist ---------------------------------------
S.append(spec("best-birthday-gifts-for-a-pianist", "2026-11-18",
 "Best Birthday Gifts for a Pianist (2026): A Concert Pianist's List",
 "Best Birthday Gifts for a Pianist (2026)",
 "Birthday gift ideas for an adult who plays the piano, chosen by a concert pianist: a stand light, a pedal, headphones, a practice journal and a book.",
 "A pianist is easy to give a gift to once you know what they use every day. These are the things I would give.",
 meta_line() + """
<p>The best birthday gifts for an adult pianist are small things used every day: a clip-on music stand light, a better sustain pedal for a digital piano, a practice journal, or a good book. I chose these from what Amazon listed on November 14, 2026, and I avoided anything that depends on knowing which piano they own.</p>
""" + DISC + quick([("Best everyday gift", "glocusent", "a clip-on stand light for evening practice"),
 ("Best for a digital piano owner", "dp10", "a pedal with half-pedal control"),
 ("Best for a thinker", "musicophilia", "a book on music and the brain")]) +
 how_i_choose("The best gift for a pianist is one that makes practice easier, not one that adds clutter. I think about what a student reaches for every evening.") + """
<h2>The gifts</h2>""" +
 pick("glocusent", "Evening is when many adults practice; a light on the page helps the eyes.") +
 pick("dp10", "Check first that their piano accepts a continuous pedal.") +
 pick("journal", "A practice record helps an adult see progress.") +
 pick("musicophilia", "A gift for the reader who also plays.") + """
<h2>Comparison</h2>""" +
 table(["Type"], [[A(P[k]["a"], P[k]["n"]), P[k]["t"].get("type", "")] for k in ["glocusent", "dp10", "journal", "musicophilia"]]) + """
<h2>How to choose</h2>
<ul><li>If you do not know their piano, avoid anything that must fit it; choose a light, a journal or a book.</li><li>If you do, a pedal or a bench is the more valuable gift.</li><li>A <a href="../gift-certificate.html">gift certificate for online piano lessons</a> is a gift of time with a teacher.</li></ul>
<p>More ideas: """ + lk("best-gifts-for-piano-players-2026", "best gifts for piano players") + """ and """ + lk("gifts-for-adult-piano-beginners", "gifts for adult piano beginners") + """.</p>""" +
 closing([("gifts-for-pianists", "gifts for pianists"), ("stand-lights", "stand lights"), ("piano-pedals", "pedals")]) + trust("a gift for a pianist"),
 [("What do pianists really want for their birthday?", "Things that make practice easier: a stand light, a good pedal, a bench that fits, a practice journal."),
  ("What if they do not own a piano yet?", "A gift certificate for lessons, or a book, avoids any guesswork about the instrument."),
  ("Is a book a good gift?", "Yes, for a reader. Musicophilia is a well-known book on music and the brain.")]))

# 14 handheld recorder ---------------------------------------------
S.append(spec("best-handheld-recorder-for-piano-practice", "2026-11-23",
 "Best Handheld Recorder for Piano Practice (2026): A Teacher's Picks",
 "Best Handheld Recorder for Piano Practice (2026)",
 "The best handheld recorders for recording your piano practice, chosen by a concert pianist: Zoom, TASCAM, what to look for and where to put the recorder.",
 "Recording your practice is the fastest way to hear what a teacher hears. Here are the handheld recorders I would look at.",
 meta_line() + """
<p>The best handheld recorder for piano practice is the Zoom H4 Essential if you want a safety margin on loud chords: Zoom lists 32-bit float WAV recording, built-in XY stereo microphones and XLR inputs. The Zoom H1n is the simplest stereo recorder, the TASCAM DR-05XP is a low-cost 32-bit float option, and the Zoom H5 offers changeable microphone capsules.</p>
""" + DISC + quick([("Best overall", "h4ess", "32-bit float, XY stereo microphones, XLR inputs"),
 ("Simplest", "h1n", "onboard stereo microphones"),
 ("Budget 32-bit float", "dr05", "32-bit float with a USB-C audio interface")]) +
 how_i_choose("A practice recording needs to be easy enough that you actually make one. I look for built-in stereo microphones, a safety margin on level, and simple controls.") + """
<h2>The picks</h2>""" +
 pick("h4ess", "The float recording is the feature that saves a take when a loud chord comes.") +
 pick("h1n", "If you want the simplest device, this is it.") +
 pick("dr05", "A lower-cost way to get 32-bit float.") +
 pick("h5", "More expandable, and a good choice if you may later add other capsules.") + """
<h2>Comparison</h2>""" +
 table(["Type", "Key feature"], trows(["h4ess", "h1n", "dr05", "h5"], ["type", "feat"])) + """
<h2>Where to put the recorder</h2>
<p>Place it on a stand a few feet from the piano, pointing at the middle of the instrument, never on the lid where it picks up vibration. Record a short phrase, listen on headphones, move it, listen again. The distance matters more than the model. See """ + lk("practicing-with-a-recording", "practicing with a recording") + """ and """ + lk("best-microphone-for-recording-piano-at-home", "the best microphone for recording piano at home") + """.</p>""" +
 closing([("record-yourself-playing", "gear to record yourself playing"), ("microphones-and-audio-interfaces", "microphones and audio interfaces"), ("mic-stands-and-studio-accessories", "stands and accessories")]) + trust("recording"),
 [("What is the best recorder for recording piano?", "For most adults, the Zoom H4 Essential or the simpler Zoom H1n. The most important thing is where you place it."),
  ("What does 32-bit float mean?", "A recording format designed so that a take recorded too loud or too quiet can be corrected afterward."),
  ("Do I need a memory card?", "Yes. These recorders store files on a microSD or SD card; check the listing for the card type.")]))

# 15 audio interface beginners -------------------------------------
S.append(spec("best-audio-interface-for-beginners", "2026-11-24",
 "Best Audio Interface for Beginners (2026): A Pianist's Guide",
 "Best Audio Interface for Beginners (2026)",
 "The best audio interfaces for beginners who record piano or voice, chosen by a concert pianist: Focusrite, Audient, Arturia, with what each listing says.",
 "An audio interface is the box between your microphone and your computer. Here is how to choose a first one, and the ones I would look at.",
 meta_line() + """
<p>The best audio interface for a beginner is the Focusrite Scarlett Solo 4th Gen if you record one microphone, and the Scarlett 2i2 4th Gen if you want two. The Audient EVO 4 is a simple alternative, and the Arturia MiniFuse 2 adds MIDI and software.</p>
""" + DISC + quick([("Best overall", "solo4", "simple, bus-powered USB-C"),
 ("Best for stereo recording", "i2i2", "two microphone preamps"),
 ("Simple alternative", "evo4", "a compact 2-in 2-out with a clear layout")]) +
 how_i_choose("A beginner needs an interface that is quiet and simple. I count the microphone preamps, because one decides whether you can record in stereo.") + """
<h2>The picks</h2>""" +
 pick("solo4", "The one I recommend to a student who wants to record one microphone or the line out of a digital piano.") +
 pick("i2i2", "If you want to record a piano with two microphones, you need two preamps.") +
 pick("evo4", "A good choice for the beginner who wants things simple.") +
 pick("minifuse2", "Includes recording software and MIDI connections, per the listing.") + """
<h2>Comparison</h2>""" +
 table(["Type", "Inputs", "Key feature"], trows(["solo4", "i2i2", "evo4", "minifuse2"], ["type", "inputs", "feat"])) + """
<h2>How to choose</h2>
<ul><li>Count the microphones you will use: one preamp for one microphone, two for a stereo pair.</li><li>Check the connection: USB-C is common now.</li><li>Check whether it gives phantom power, which condenser microphones need.</li></ul>
<p>See also """ + lk("best-audio-interface-under-200", "the best audio interface under $200") + """ and """ + lk("focusrite-scarlett-solo-vs-2i2", "Scarlett Solo vs 2i2") + """.</p>""" +
 closing([("audio-interfaces-for-home-recording", "audio interfaces"), ("microphones-and-audio-interfaces", "microphones and interfaces"), ("music-cables-and-power", "cables")]) + trust("recording"),
 [("Do I need an audio interface to record piano?", "If you record a digital piano by USB you may not. For a microphone you need one."),
  ("How many inputs do I need?", "One for a single microphone, two for a stereo pair."),
  ("What is phantom power?", "A small voltage sent through the microphone cable that powers condenser microphones.")]))

# 16 interface under 200 --------------------------------------------
S.append(spec("best-audio-interface-under-200", "2026-11-24",
 "Best Audio Interface Under $200 (2026): A Pianist's Picks",
 "Best Audio Interface Under $200 (2026)",
 "The best audio interfaces under $200 for recording piano and voice, chosen by a concert pianist: Focusrite, Audient, Behringer, MOTU and more.",
 "You do not need to spend a lot to record well. These are the interfaces under $200 that I would look at.",
 meta_line() + """
<p>Under $200, the Focusrite Scarlett Solo 4th Gen is my first choice for one microphone, and the Audient EVO 4 for two inputs in a simple layout. The Behringer UMC22 is the lowest-cost two-input option. I chose these by the prices the listings showed on November 14, 2026; check today&#39;s price.</p>
""" + DISC + quick([("Best overall", "solo4", "bus-powered USB-C with Air mode and phantom power"),
 ("Best two-input", "evo4", "a compact 2-in 2-out with a clear layout"),
 ("Lowest cost", "umc22", "a 2-in 2-out with a Midas-designed preamp")]) +
 how_i_choose("Under $200 I look for a quiet preamp, phantom power and a headphone output.") + """
<h2>The picks</h2>""" +
 pick("solo4", "A simple choice for one microphone.") + pick("evo4", "If you want two inputs without a large unit.") +
 pick("umc22", "A very low entry cost. Check the preamp on quiet passages.") + pick("motum2", "At the top of this price band, built for clean, quiet recordings.") + """
<h2>Comparison</h2>""" +
 table(["Type", "Inputs", "Key feature"], trows(["solo4", "evo4", "umc22", "motum2"], ["type", "inputs", "feat"])) + """
<h2>How to choose</h2>
<ul><li>One microphone: the Solo. Two: the EVO 4, UMC22 or M2.</li><li>If quiet piano passages matter, spend toward the top of the band.</li></ul>
<p>See """ + lk("best-audio-interface-for-beginners", "the best audio interface for beginners") + """.</p>""" +
 closing([("audio-interfaces-for-home-recording", "audio interfaces"), ("music-cables-and-power", "cables"), ("home-studio-starter-kits", "starter kits")]) + trust("recording"),
 [("Can I get a good interface under $200?", "Yes. The Focusrite Scarlett Solo 4th Gen and Audient EVO 4 are both within the range at the prices I saw."),
  ("Is a cheap interface noisy?", "Some are. Check the preamp on quiet passages."),
  ("What else do I need?", "A microphone, an XLR cable and a stand.")]))

# 17 recording bundle under 300 ------------------------------------
S.append(spec("best-recording-bundle-under-300", "2026-11-25",
 "Best Recording Bundle Under $300 (2026): A Pianist's Picks",
 "Best Recording Bundle Under $300 (2026)",
 "The best home recording bundles under $300 for a pianist or singer, chosen by a concert pianist: PreSonus, Behringer, Focusrite and Yamaha, with what to check.",
 "A bundle puts an interface and extras in one box. Here are the ones under $300 I would look at, and what to check on each listing.",
 meta_line() + """
<p>Under $300, the bundles I would look at are the Focusrite Scarlett Solo Studio 4th Gen for the best interface, the PreSonus AudioBox USB 96 Studio bundle for software and accessories, and the PreSonus AudioBox Go Creator bundle for the lowest cost. I chose these by the prices the listings showed on November 14, 2026. Check the listing for what is in each box.</p>
""" + DISC + quick([("Best interface", "solostudio", "built around the Scarlett Solo"),
 ("Best all-in-one", "ab96s", "interface, Fender Studio Pro software and more"),
 ("Lowest cost", "abgo", "built around the AudioBox Go")]) +
 how_i_choose("A bundle is only a good value if you need everything in it. I read the box contents on each listing, not the title.") + """
<h2>The picks</h2>""" +
 pick("solostudio", "The interface is the best part; check the microphone it comes with.") + pick("ab96s", "A broad starter bundle with software included, per the title.") +
 pick("abgo", "A small, inexpensive way to start.") + pick("ag03", "A mixer plus USB interface; useful if you add more sources.") + """
<h2>Comparison</h2>""" +
 table(["Type", "Note"], trows(["solostudio", "ab96s", "abgo", "ag03"], ["type", "note"])) + """
<h2>How to choose</h2>
<ul><li>If you will only record one voice or microphone, the Solo bundle is enough.</li><li>If you want everything in one box, the AudioBox bundles.</li><li>If you already own headphones, a bundle without them is cheaper.</li></ul>
<p>Next: """ + lk("home-recording-corner-on-a-budget", "how to build a home recording corner on a budget") + """.</p>""" +
 closing([("home-studio-starter-kits", "home studio starter kits"), ("audio-interfaces-for-home-recording", "audio interfaces"), ("mic-stands-and-studio-accessories", "stands and accessories")]) + trust("recording"),
 [("Is a recording bundle worth it?", "If you need everything in it, yes. Check the contents on the listing."),
  ("Which bundle is best for piano?", "The Scarlett Solo bundle for one microphone; for stereo recording you need an interface with two preamps."),
  ("What else do I need?", "A computer, headphones and a stand.")]))

# 18 home recording corner ------------------------------------------
S.append(spec("home-recording-corner-on-a-budget", "2026-11-25",
 "How to Build a Home Recording Corner on a Budget (2026)",
 "How to Build a Home Recording Corner on a Budget",
 "How a pianist builds a simple home recording corner: the few pieces that matter, in order, chosen by a concert pianist, with verified products for each.",
 "You do not need a studio to record your playing. You need a corner, five pieces of gear and a habit.",
 meta_line() + """
<p>A home recording corner for a pianist needs five things in this order: a way to capture the sound (a handheld recorder, or an interface with a microphone), closed-back headphones, a stand that holds the gear steady, a way to read your score, and a quiet time of day. You can begin with one handheld recorder and add the rest as you go.</p>
""" + DISC + quick([("Start here", "h4ess", "a handheld recorder with XY stereo microphones"),
 ("Then add", "solo4", "an interface for a microphone or a digital piano&#39;s line out"),
 ("And", "hd280", "closed-back headphones to hear what you captured")]) +
 how_i_choose("The corner should make recording easy enough to repeat. I think about the steps between sitting down and pressing record: the fewer, the better.") + """
<h2>Step by step</h2>
<ol><li><strong>Choose the spot.</strong> A corner with a soft surface, a rug or a curtain, sounds better than a bare room.</li>
<li><strong>Capture the sound.</strong> Begin with a handheld recorder, which needs no computer.</li>
<li><strong>Listen.</strong> Closed-back headphones show you what you recorded.</li>
<li><strong>Grow.</strong> Add an interface and a microphone pair later.</li></ol>""" +
 pick("h4ess", "The one device I would buy first.") + pick("solo4", "The next step, when you want to record to a computer.") + pick("hd280", "Closed-back headphones keep your piano out of the recording and let you listen critically.") + """
<h2>Where it all goes</h2>
<p>Keep the recorder on a stand a few feet from the piano; for a laptop or tablet score, see """ + lk("best-tablet-for-sheet-music", "tablet stands for sheet music") + """. For a complete bundle, see """ + lk("best-recording-bundle-under-300", "the best recording bundle under $300") + """.</p>""" +
 closing([("home-studio-starter-kits", "home studio starter kits"), ("record-yourself-playing", "gear to record yourself playing"), ("mic-stands-and-studio-accessories", "stands and accessories")]) + trust("recording"),
 [("What do I need to record piano at home?", "At minimum, a handheld recorder. Add an interface, microphones and headphones as you grow."),
  ("Do I need acoustic treatment?", "A soft surface helps. You do not need a treated room to start."),
  ("What should I buy first?", "A handheld recorder: it works with no computer.")]))

# 19 page turner pedal ----------------------------------------------
S.append(spec("best-page-turner-pedal-for-ipad", "2026-11-26",
 "Best Page Turner Pedal for iPad (2026): A Pianist's Picks",
 "Best Page Turner Pedal for iPad (2026)",
 "The best Bluetooth page-turner pedals for reading sheet music on an iPad, chosen by a concert pianist: AirTurn, PageFlip and lower-cost options.",
 "If you read music from an iPad, a pedal turns the page while your hands stay on the keys. Here are the ones I would look at.",
 meta_line() + """
<p>The best page-turner pedal for most pianists is the AirTurn BT500S-2, a two-pedal Bluetooth model that turns forward and back. The PageFlip Dragonfly has four pedals, the AirTurn DUO 500 is described as silent, and the JOYO is a low-cost way to try the idea. Check that your sheet-music app supports Bluetooth page turners before you buy.</p>
""" + DISC + quick([("Best overall", "bt500", "two pedals: forward and back"),
 ("Most pedals", "dragonfly", "four pedals for sheet-music apps"),
 ("Quietest", "duo500", "a silent Bluetooth pedal")]) +
 how_i_choose("A page turner should disappear. I look for reliable Bluetooth, a base that does not slide, and a pedal that does not click.") + """
<h2>The picks</h2>""" +
 pick("bt500", "Two pedals are enough for most adults: forward and back.") + pick("dragonfly", "If you want to jump between pages as well.") +
 pick("duo500", "The one for recitals and recordings.") + pick("joyo", "To try the idea at the lowest cost.") + """
<h2>Comparison</h2>""" +
 table(["Type", "Pedals"], trows(["bt500", "dragonfly", "duo500", "joyo"], ["type", "pedals"])) + """
<h2>How to choose</h2>
<ul><li>Check that your app supports Bluetooth page turners.</li><li>Place the pedal where your foot can find it without looking.</li><li>If you use the sustain pedal too, check your foot has room for both.</li></ul>
<p>See also """ + lk("best-tablet-for-sheet-music", "stands for reading sheet music on a tablet") + """ and """ + lk("how-to-start-sight-reading", "how to start sight-reading") + """.</p>""" +
 closing([("ipad-music-stands-and-page-turners", "tablet stands and page turners"), ("music-stands", "music stands"), ("piano-accessories", "piano accessories")]) + trust("reading music"),
 [("Do page-turner pedals work with an iPad?", "Bluetooth page turners work with many sheet-music apps. Check your app&#39;s settings."),
  ("How many pedals do I need?", "Two: forward and back."),
  ("Will it interfere with my sustain pedal?", "They are separate pedals; make sure you have room for both feet.")]))

# 20 tablet ----------------------------------------------------------
S.append(spec("best-tablet-for-sheet-music", "2026-11-26",
 "Best Tablet for Sheet Music: What to Look For and the Stands I Trust",
 "Best Tablet for Sheet Music (2026): What to Look For",
 "How to choose a tablet for reading sheet music at the piano, from a concert pianist, plus the tablet stands and holders I would look at.",
 "I do not recommend one tablet, because I could not verify a specific model on Amazon. Here is what a pianist should look for, and the stands I would use.",
 meta_line() + """
<p><strong>A note first.</strong> I am not recommending a particular tablet in this guide, because I did not verify a specific tablet product for my shop. What I can do is tell you what a pianist should look for in one, and which stands and holders I would use to put it where you can read it.</p>
<p>What to look for: the largest screen you can comfortably hold or mount, because small screens make the notes small; a screen that is not glossy under your lamp; and a sheet-music app that supports a Bluetooth page-turner pedal. The stand matters as much as the tablet.</p>
""" + DISC + quick([("Best floor stand", "elitefloor", "a 72-inch floor stand for a tablet score"),
 ("Best for a microphone stand", "iklip3", "fits iPads and Android tablets"),
 ("Tilting holder", "km19790", "a tilting tablet holder for a microphone stand")]) +
 how_i_choose("The tablet should sit where your eyes rest, above the keys, not over them. A stand that wobbles is worse than paper.") + """
<h2>The picks</h2>""" +
 pick("elitefloor", "If your piano&#39;s music desk is too small or too low, a floor stand lets you set the angle.") +
 pick("xxzu", "Has a ball head for tilt.") + pick("iklip3", "If you already own a microphone stand.") + pick("km19790", "Tilts for the angle of your eyes.") + """
<h2>Comparison</h2>""" +
 table(["Type", "Mount"], trows(["elitefloor", "xxzu", "iklip3", "km19790"], ["type", "mount"])) + """
<h2>How to choose</h2>
<ul><li>Choose the stand for the position you need: floor, or microphone stand.</li><li>Check the holder fits your tablet in its case.</li><li>Add a page-turner: """ + lk("best-page-turner-pedal-for-ipad", "best page-turner pedal for iPad") + """.</li></ul>""" +
 closing([("ipad-music-stands-and-page-turners", "tablet stands and page turners"), ("music-stands", "music stands"), ("stand-lights", "stand lights")]) + trust("reading music"),
 [("What is the best tablet for sheet music?", "I do not recommend a specific model. Choose the largest comfortable screen and an app that supports a page-turner."),
  ("Do I need a stand for a tablet?", "Yes. A tablet on a music desk can slide; a stand or holder keeps it at the right angle."),
  ("Is paper better?", "For some, yes. A tablet is more portable and can hold a whole library.")]))

# 21 studio monitors under 300 ---------------------------------------
S.append(spec("best-studio-monitors-under-300", "2026-11-27",
 "Best Studio Monitors Under $300 (2026): A Pianist's Picks",
 "Best Studio Monitors Under $300 (2026)",
 "The best pairs of studio monitors under $300 for a pianist, chosen by a concert pianist: PreSonus, M-Audio and what to check, with the listings&#39; own facts.",
 "A pair of monitors lets you hear your digital piano or your recordings without headphones. These are the pairs under $300 I would look at.",
 meta_line() + """
<p>Under $300, the pair I would look at first is the PreSonus Eris E5, 5.25-inch two-way near-field monitors. The M-Audio BX4 is the smallest and lowest-cost pair; the M-Audio BX5BT adds Bluetooth. I chose these by the prices the listings showed on November 14, 2026, and by whether they are sold as a pair; check today&#39;s price.</p>
""" + DISC + quick([("Best overall", "e5pair", "a pair of 5.25-inch two-way near-field monitors"),
 ("Best for a small desk", "bx4", "a pair of 4.5-inch powered monitors"),
 ("Best for streaming too", "bx5bt", "5-inch desktop monitors with Bluetooth")]) +
 how_i_choose("A monitor should tell you the truth about your playing. I check size, whether the listing is for a pair, and what the maker says about its use.") + """
<h2>The picks</h2>""" +
 pick("e5pair", "The one I would pick for a pianist who wants to hear the middle of the piano clearly.") + pick("bx4", "For a very small desk.") + pick("bx5bt", "If you also want to stream music.") + """
<h2>Comparison</h2>""" +
 table(["Type", "Size", "Sold as"], trows(["e5pair", "bx4", "bx5bt"], ["type", "size", "sold"])) + """
<p>I do not print wattage or frequency range, because I could not open a maker page with those figures on November 14, 2026. Check the listing.</p>
<h2>How to choose</h2>
<ul><li>Make sure the listing is for a pair, as these are. Many monitors are sold singly.</li><li>Place them at ear height, forming a triangle with your head.</li><li>If you only use headphones, you do not need monitors: see """ + lk("best-headphones-for-digital-piano", "headphones for digital piano") + """.</li></ul>""" +
 closing([("studio-monitors-for-home-recording", "studio monitors"), ("speakers-for-keyboards", "speakers for keyboards"), ("music-cables-and-power", "cables")]) + trust("listening"),
 [("Do I need studio monitors for a digital piano?", "Not if you play on headphones. They help when you want to hear recordings or share the sound."),
  ("Are these sold as pairs?", "Yes, the three here are listed as pairs. Many monitors on Amazon are sold singly."),
  ("What cables do I need?", "Check the monitor inputs and your piano&#39;s outputs; see my shop page on music cables.")]))

# 22 Solo vs 2i2 -----------------------------------------------------
solo2i2 = [["Microphone preamps", "1", "2"], ["Instrument inputs", "1", "2"], ["Line inputs", "1", "2"],
 ["Line outputs", "2 balanced", "2 balanced"], ["Headphone outputs", "1", "1"], ["Converters", "24-bit/192 kHz", "24-bit/192 kHz"],
 ["Phantom power", "Yes", "Yes"], ["Loopback", "Yes", "Yes"], ["Air mode", "Yes", "Yes"], ["Auto Gain and Clip Safe", "Not listed on the specification page", "Yes"],
 ["Connection", "USB-C, bus-powered", "USB-C, bus-powered"], ["Dimensions", "46.5 x 143 x 96 mm", "47.5 x 180 x 117 mm"], ["Weight", "0.382 kg", "0.595 kg"]]
S.append(spec("focusrite-scarlett-solo-vs-2i2", "2026-11-27",
 "Focusrite Scarlett Solo vs 2i2 (4th Gen): Which Should a Pianist Buy?",
 "Focusrite Scarlett Solo vs 2i2 (4th Gen) for Pianists",
 "Focusrite Scarlett Solo or 2i2 (4th Gen) for recording piano? A concert pianist compares inputs, preamps and features from Focusrite&#39;s own specifications.",
 "One microphone preamp or two? That is the real difference. Here is the full comparison and which a pianist should buy.",
 meta_line() + """
<p>Buy the Scarlett 2i2 if you want to record a piano with two microphones in stereo, or a microphone and a digital piano at the same time. Buy the Solo if you will only record one microphone or the line out of a digital piano. The Solo lists one microphone preamp; the 2i2 lists two and adds Auto Gain and Clip Safe.</p>
""" + DISC + quick([("For stereo piano recording", "i2i2", "two microphone preamps"),
 ("For one microphone", "solo4", "one preamp, simple and smaller")], title="Quick verdict") + """
<h2>Scarlett Solo vs 2i2: specifications</h2>""" +
 table(["Scarlett Solo 4th Gen", "Scarlett 2i2 4th Gen"], solo2i2, first="Specification (as listed by Focusrite)") + """
<p>Source: Focusrite&#39;s specification pages for each interface, opened on November 14, 2026. Neither page lists MIDI.</p>
<h2>The difference that matters for piano</h2>
<p>A piano is a wide instrument. A single microphone records one point of view; a stereo pair records the width, which is why most serious piano recordings use two. If you plan to learn stereo recording, the 2i2 is the one to buy. See """ + lk("best-microphone-for-recording-piano-at-home", "the best microphone for recording piano at home") + """.</p>
<h2>Which should you buy?</h2>
<p>If you only record a digital piano by its line output, or sing with one microphone, the Solo is enough. Otherwise, the 2i2.</p>""" +
 pick("i2i2", "My choice for a pianist who wants to grow into stereo recording.") + pick("solo4", "My choice for the simplest setup.") +
 closing([("audio-interfaces-for-home-recording", "audio interfaces"), ("microphones-and-audio-interfaces", "microphones and interfaces"), ("music-cables-and-power", "cables")]) + trust("recording"),
 [("What is the difference between the Solo and the 2i2?", "The Solo has one microphone preamp; the 2i2 has two, plus Auto Gain and Clip Safe, per Focusrite&#39;s pages."),
  ("Which is better for piano?", "The 2i2, if you want to record in stereo with two microphones."),
  ("Do I need phantom power?", "For condenser microphones, yes. Both list it.")]))

# 23 stereo mics ------------------------------------------------------
S.append(spec("best-stereo-microphones-for-piano", "2026-11-28",
 "Best Pair of Microphones for Piano (Stereo, 2026): A Pianist's Picks",
 "Best Pair of Microphones for Piano (Stereo, 2026)",
 "The best matched pairs of microphones for recording piano in stereo, chosen by a concert pianist: RODE, sE, LEWITT and what you need to plug them in.",
 "A pair of small-diaphragm condenser microphones is the classic way to record a piano. Here are the pairs I would look at.",
 meta_line() + """
<p>The best pair of microphones for recording piano depends on your budget: the RODE M5 matched pair is the lowest-cost pair I would look at, the LEWITT LCT 040 MATCH pair is praised for acoustic instruments, and the RODE NT5 pair is a step up. You also need an audio interface with two microphone preamps and phantom power, such as the Scarlett 2i2.</p>
""" + DISC + quick([("Best value pair", "m5", "a matched pair of small-diaphragm cardioid condensers"),
 ("Best for acoustic instruments", "lct040", "excellent transient response, per the listing"),
 ("Step up", "nt5", "a matched pair with 1/2-inch cardioid capsules")]) +
 how_i_choose("A pair has to be matched, so both microphones sound the same. I choose small-diaphragm condensers because they follow the attack of a note.") + """
<h2>The picks</h2>""" +
 pick("m5", "A sensible first pair.") + pick("lct040", "A pair the listing describes for acoustic instruments.") + pick("se7", "A pair the listing names for pianos.") + pick("nt5", "For a step up in capsule quality.") + """
<h2>Comparison</h2>""" +
 table(["Type", "Key feature"], trows(["m5", "lct040", "se7", "nt5"], ["type", "feat"])) + """
<h2>What else you need</h2>
<p>An interface with two preamps and phantom power (see """ + lk("focusrite-scarlett-solo-vs-2i2", "Solo vs 2i2") + """), two XLR cables, two stands and a bar or stereo mount. Place the pair facing the open lid, about an arm&#39;s length away, and move them until it sounds like the piano in the room. See """ + lk("best-microphone-for-recording-piano-at-home", "my recording guide") + """.</p>""" +
 closing([("microphones-and-audio-interfaces", "microphones and interfaces"), ("mic-stands-and-studio-accessories", "stands and accessories"), ("music-cables-and-power", "cables")]) + trust("recording"),
 [("What microphones do I need for piano?", "A matched pair of small-diaphragm condensers, an interface with two preamps and phantom power, and two stands."),
  ("Do I need a matched pair?", "For stereo recording, yes. Matched means both microphones respond the same way."),
  ("Where do I put the microphones?", "Facing the open lid, about an arm&#39;s length away; move them until it sounds right.")]))

# 24 midi controller --------------------------------------------------
S.append(spec("best-88-key-weighted-midi-controller", "2026-11-28",
 "Best 88-Key Weighted MIDI Controller for Pianists (2026)",
 "Best 88-Key Weighted MIDI Controller (2026)",
 "The best 88-key weighted MIDI controllers for pianists who play software pianos, chosen by a concert pianist: M-Audio, and what to buy instead.",
 "A MIDI controller is a keyboard with no sound of its own. For a pianist the question is the action. Here is what I would look at.",
 meta_line() + """
<p>The best 88-key weighted MIDI controller I verified is the M-Audio Hammer 88: the listing says an 88-key weighted hammer-action controller with no sound of its own. The M-Audio Keystation 88 MK3 is a lower-cost 88-key option with semi-weighted keys. If you want a controller that is also a piano, a stage piano such as the Yamaha CP88 has sounds of its own and weighted wooden keys.</p>
""" + DISC + quick([("Best weighted controller", "hammer88", "88 weighted hammer-action keys, no sound of its own"),
 ("Lower-cost 88 keys", "ks88", "88 semi-weighted keys for apps and software"),
 ("If you want a piano too", "cp88", "weighted wooden keys with its own sounds")]) +
 how_i_choose("A controller is only as good as its action. I read for the words weighted and hammer action, because that is what teaches touch.") + """
<h2>The picks</h2>""" +
 pick("hammer88", "My first choice if software pianos are your plan.") + pick("ks88", "Choose it only if touch is not your priority.") + pick("cp88", "A different category: a stage piano that works as a controller as well. Check the listing for MIDI connections.") + """
<h2>Comparison</h2>""" +
 table(["Type", "Key action", "Sound"], trows(["hammer88", "ks88", "cp88"], ["type", "action", "sound"])) + """
<h2>Do you need a controller at all?</h2>
<p>If you only want to practice, a digital piano is simpler: it has the keys and the sound. A controller makes sense when you will use software pianos or recording software on a computer. See """ + lk("how-to-connect-a-digital-piano-to-a-computer", "how to connect a digital piano to a computer") + """ and """ + lk("best-digital-piano-for-adult-beginners", "the best digital piano for adult beginners") + """.</p>""" +
 closing([("midi-keyboard-controllers", "MIDI keyboard controllers"), ("stage-pianos", "stage pianos"), ("music-cables-and-power", "cables")]) + trust("a MIDI keyboard"),
 [("What is a MIDI controller?", "A keyboard that sends note information to a computer or tablet but makes no sound of its own."),
  ("Do I need weighted keys?", "For learning piano, yes: weighted keys teach touch."),
  ("Can a digital piano be a MIDI controller?", "Many can, by USB. Check your model&#39;s specifications.")]))

# 25 2i2 review -------------------------------------------------------
S.append(spec("focusrite-scarlett-2i2-4th-gen-review", "2026-11-29",
 "Focusrite Scarlett 2i2 (4th Gen) Review: A Pianist's Assessment (2026)",
 "Focusrite Scarlett 2i2 4th Gen: A Pianist's Assessment",
 "An assessment of the Focusrite Scarlett 2i2 4th Gen by a concert pianist: what Focusrite lists, what I look for when recording piano, and who it suits.",
 "I have not used this interface for weeks and I will not claim to. Here is what its specifications tell a pianist, and who I would recommend it to.",
 meta_line() + """
<p><strong>A note on method.</strong> This is an assessment, not a hands-on test. I have not used this unit for weeks. I read Focusrite&#39;s specifications and the Amazon listing as a pianist and teacher, and tell you what I look for and whether I would recommend it.</p>
<p><strong>My verdict:</strong> I would recommend the Scarlett 2i2 to a pianist who wants to record in stereo with two microphones, or a microphone and a digital piano at the same time. If you will only record one microphone, the Solo is enough.</p>
""" + DISC + quick([("Verdict", "i2i2", "two microphone preamps, Auto Gain and Clip Safe, USB-C bus power")], title="In short") + """
<h2>What Focusrite says</h2>
<p>Focusrite lists two microphone preamps, two instrument inputs and two line inputs, two balanced line outputs, one headphone output, 24-bit/192 kHz converters, phantom power, loopback, Air mode with Presence and Harmonic Drive, Auto Gain and Clip Safe, USB-C bus power, 4 x 2 simultaneous input and output, and a bundled software package that includes Ableton Live Lite, Pro Tools Intro+ and Cubase LE. It measures 47.5 x 180 x 117 mm and weighs 0.595 kg. The page does not list MIDI.</p>
<h2>What I look for, and how it answers</h2>
<ul><li><strong>Two preamps.</strong> They allow a stereo pair of microphones, the classic way to record piano.</li>
<li><strong>Clip Safe and Auto Gain.</strong> They protect against a loud chord, a common beginner problem.</li>
<li><strong>Phantom power.</strong> Condenser microphones need it.</li>
<li><strong>Low noise.</strong> A piano has a wide dynamic range; I would listen for hiss on a pianissimo.</li>
<li><strong>Simplicity.</strong> The fewer decisions, the more often you will record.</li></ul>""" +
 pick("i2i2", "I would recommend it to a student who tells me they want to record their playing properly.") + """
<h2>Who should look elsewhere</h2>
<p>If you only need one microphone, read """ + lk("focusrite-scarlett-solo-vs-2i2", "Solo vs 2i2") + """. For a pair of microphones to go with it, see """ + lk("best-stereo-microphones-for-piano", "the best pair of microphones for piano") + """.</p>""" +
 closing([("audio-interfaces-for-home-recording", "audio interfaces"), ("microphones-and-audio-interfaces", "microphones and interfaces"), ("music-cables-and-power", "cables")]) + trust("recording"),
 [("Is the Scarlett 2i2 good for recording piano?", "In my assessment, yes, because two preamps allow a stereo pair of microphones."),
  ("Does the 2i2 have MIDI?", "Focusrite&#39;s specification page does not list MIDI."),
  ("Has Dr. Pisarenko tested the 2i2?", "No. This is an assessment based on the specifications and what a pianist looks for, not a hands-on test.")]))

# 26 connect piano to computer ----------------------------------------
S.append(spec("how-to-connect-a-digital-piano-to-a-computer", "2026-11-29",
 "How to Connect a Digital Piano to a Computer (USB, MIDI, Audio)",
 "How to Connect a Digital Piano to a Computer",
 "How to connect a digital piano to a computer or tablet by USB, MIDI or audio cable, explained by a concert pianist, with the gear you may need.",
 "There are three ways to connect a digital piano to a computer. Here is what each does, and what you need to buy.",
 meta_line() + """
<p>There are three ways to connect a digital piano to a computer: by USB, which carries MIDI and sometimes audio; by a MIDI cable and an interface; or by an audio cable from the headphone or line output into an audio interface. Most modern digital pianos have a USB port, so a single cable is usually enough.</p>
""" + DISC + """
<h2>Option 1: USB</h2>
<p>Most digital pianos have a USB port for connecting to a computer. Roland lists a USB Type B &quot;Computer&quot; port on the FP-10 and FP-30X, Casio lists USB Type A and B on the PX-S1100, and Yamaha lists a stereo USB audio interface on the P-145BT. USB carries MIDI, which lets software know which notes you played, and on some pianos it carries audio too. Check your piano&#39;s manual.</p>
<h2>Option 2: MIDI cable</h2>
<p>An older piano or a stage piano may have 5-pin MIDI ports. You then need an interface with MIDI connections, such as the """ + A("B09HL3GD7G", "Arturia MiniFuse 2") + """ (the listing says it is a USB audio and MIDI interface).</p>
<h2>Option 3: audio cable</h2>
<p>If you want to record the sound, run a cable from the piano&#39;s line output or headphone output into an audio interface, such as the """ + A("B0C5JSHP7M", "Focusrite Scarlett Solo") + """, which lists a line input. Use the piano&#39;s line output if it has one.</p>
<h2>What you may need to buy</h2>
<ul><li>A USB cable of the right type for your piano.</li><li>An audio interface if you want to record the sound or use a microphone: see """ + lk("best-audio-interface-for-beginners", "the best audio interface for beginners") + """.</li><li>Software: a notation or recording app.</li></ul>
<p>If you want a keyboard with no sound of its own, read """ + lk("best-88-key-weighted-midi-controller", "the best 88-key weighted MIDI controller") + """.</p>""" +
 pick("solo4", "If you want to record your digital piano&#39;s sound, this is a simple interface with a line input.") +
 closing([("audio-interfaces-for-home-recording", "audio interfaces"), ("music-cables-and-power", "cables and power"), ("midi-keyboard-controllers", "MIDI keyboard controllers")]) + trust("connecting a piano"),
 [("Can I connect my digital piano to my computer with USB?", "Most can. Check that your piano has a computer USB port."),
  ("Do I need an audio interface?", "Only if you want to record the sound from the piano&#39;s audio output or use a microphone."),
  ("Which cable do I need?", "A USB cable with the connector your piano uses; the manual says which.")]))

# 27 KRK vs HS5 --------------------------------------------------------
S.append(spec("krk-rokit-5-vs-yamaha-hs5", "2026-11-30",
 "KRK Rokit 5 vs Yamaha HS5: A Pianist&#39;s Comparison (2026)".replace("&#39;", "'"),
 "KRK Rokit 5 vs Yamaha HS5 for Pianists (2026)",
 "KRK Rokit 5 G5 or Yamaha HS5 for monitoring piano? A concert pianist compares what the listings say and what to listen for, with honest limits on the data.",
 "Two famous five-inch monitors. I could not verify all their specifications, so here is what I can tell you and how I would choose.",
 meta_line() + """
<p>For monitoring piano I would choose the Yamaha HS5 if you want the plainest, least flattering sound, and the KRK Rokit 5 G5 if you want the more familiar, bass-forward character it is known for. Both are 5-inch powered monitors. Amazon lists the KRK as a pair and the HS5 as a single speaker or as a matched pair, so check which you are buying.</p>
<p><strong>A note on data.</strong> On November 14, 2026 I could not open a maker page that listed full specifications for both, so I do not print wattage or frequency ranges. What I say about sound is reputation and what I listen for, not measurement.</p>
""" + DISC + quick([("Plainest sound", "hs5pair", "a matched pair of 5-inch monitors"),
 ("More familiar bass-forward character", "krk", "a pair of fifth-generation 5-inch powered monitors")], title="Quick verdict") + """
<h2>What the listings say</h2>""" +
 table(["Yamaha HS5", "KRK Rokit 5 G5"], [["Listing (pair)", "A matched pair of 5-inch monitors", "A pair of fifth-generation 5-inch powered monitors"],
  ["Listing (single)", "A 5-inch powered monitor is also sold singly", "Listed as a pair"], ["Size", "5-inch", "5-inch"]], first="Item") + """
<h2>What I listen for in a monitor for piano</h2>
<ul><li><strong>The middle.</strong> A piano&#39;s melody lives between roughly the middle of the keyboard and the treble; a monitor must keep it clear.</li>
<li><strong>The bass.</strong> A monitor that flatters the bass makes you play the left hand too softly in your own recordings.</li>
<li><strong>The treble.</strong> Harshness here tires your ears.</li></ul>""" +
 pick("hs5pair", "The Yamaha&#39;s reputation is for being plain; that is what a teacher wants.") + pick("krk", "A reputation for a fuller low end; check it does not flatter.") + """
<h2>Which should you buy?</h2>
<p>Listen if you can. If you cannot, the HS5 is the safer choice for a pianist. For a lower-cost pair, see """ + lk("best-studio-monitors-under-300", "the best studio monitors under $300") + """.</p>""" +
 closing([("studio-monitors-for-home-recording", "studio monitors"), ("speakers-for-keyboards", "speakers for keyboards"), ("music-cables-and-power", "cables")]) + trust("listening"),
 [("Is the Yamaha HS5 good for piano?", "In my assessment, yes: its reputation is for a plain, honest sound."),
  ("Is the KRK Rokit 5 good for piano?", "It can be. Its reputation is for a fuller low end, so check it does not flatter your left hand."),
  ("Are these sold as pairs?", "Check each listing. Amazon lists the HS5 both singly and as a pair.")]))

# 28 HS5 vs Eris ------------------------------------------------------
S.append(spec("yamaha-hs5-vs-presonus-eris-e5", "2026-11-30",
 "Yamaha HS5 vs PreSonus Eris E5: A Pianist's Comparison (2026)",
 "Yamaha HS5 vs PreSonus Eris E5 for Pianists (2026)",
 "Yamaha HS5 or PreSonus Eris E5 for monitoring piano? A concert pianist compares what the listings say, the size, and what to listen for.",
 "Two popular five-inch monitors at different prices. Here is what the listings say and how I would choose.",
 meta_line() + """
<p>The PreSonus Eris E5 is the better value for most pianists: Amazon lists a pair of 5.25-inch two-way near-field monitors at a lower cost than a pair of Yamaha HS5. The Yamaha HS5 is the one to choose if you want its plain, flat reputation and are willing to pay for it. Neither verdict is a measurement; I could not open a maker page with full specifications on November 14, 2026.</p>
""" + DISC + quick([("Better value", "e5pair", "a pair of 5.25-inch two-way near-field monitors"),
 ("Plainer reputation", "hs5pair", "a matched pair of 5-inch monitors")], title="Quick verdict") + """
<h2>What the listings say</h2>""" +
 table(["Yamaha HS5 (pair)", "PreSonus Eris E5 (pair)"], [["Listing", "A matched pair of 5-inch monitors", "A pair of 5.25-inch two-way near-field monitors"], ["Sold as", "Pair", "Pair"]], first="Item") + """
<h2>How I would choose</h2>
<ul><li>If budget matters, the Eris E5 pair.</li><li>If you want the flattest sound by reputation, the HS5.</li><li>If you can, listen to both with a recording you know well.</li></ul>""" +
 pick("e5pair", "The one I would buy first for a pianist on a budget.") + pick("hs5pair", "The one I would choose for accuracy.") + """
<p>See also """ + lk("krk-rokit-5-vs-yamaha-hs5", "KRK Rokit 5 vs Yamaha HS5") + """ and """ + lk("best-studio-monitors-under-300", "the best studio monitors under $300") + """.</p>""" +
 closing([("studio-monitors-for-home-recording", "studio monitors"), ("speakers-for-keyboards", "speakers for keyboards"), ("music-cables-and-power", "cables")]) + trust("listening"),
 [("Which is better, the HS5 or the Eris E5?", "For most pianists, the Eris E5 for value. The HS5 for a plainer reputation."),
  ("Do I need a pair?", "Yes, for stereo. Both listings here are pairs."),
  ("Do I need monitors if I use headphones?", "No. Monitors are for listening without headphones.")]))

# 29 Zoom --------------------------------------------------------------
zoom_rows = [["Microphones", "Onboard stereo microphones (listing)", "Built-in 90-degree XY stereo microphones", "XYH-5 XY capsule, changeable"],
 ["External inputs", "Not stated on the listing", "Two XLR/TRS combo inputs plus a 3.5 mm input", "Two XLR/TRS combo inputs"],
 ["Phantom power", "Not stated on the listing", "Yes, on the XLR inputs", "Yes, selectable"],
 ["Recording format", "Not stated on the listing", "WAV, 32-bit float, up to 96 kHz", "WAV, 16- or 24-bit, up to 96 kHz"],
 ["Storage", "Not stated on the listing", "microSDHC 4-32 GB, microSDXC 64 GB-1 TB", "SD or SDHC, up to 32 GB"],
 ["Power", "Not stated on the listing", "Two AA batteries, AC adaptor or USB", "Two AA batteries, USB or AC adaptor"],
 ["USB audio interface", "Not stated on the listing", "Yes, USB-C", "Yes"], ["Weight", "Not stated on the listing", "243 g with batteries", "Not stated on Zoom&#39;s page"]]
S.append(spec("zoom-h1n-vs-h4-essential-vs-h5", "2026-12-01",
 "Zoom H1n vs H4 Essential vs H5: Which Recorder for Piano?",
 "Zoom H1n vs H4 Essential vs H5 for Piano (2026)",
 "Zoom H1n, H4 Essential or H5 for recording piano practice? A concert pianist compares microphones, inputs, recording format and storage from Zoom&#39;s own pages.",
 "Three Zoom handheld recorders for recording your piano. Here is the comparison, and which I would choose.",
 meta_line() + """
<p>For recording piano practice I would choose the Zoom H4 Essential: Zoom lists built-in XY stereo microphones, XLR inputs and 32-bit float WAV recording. The H1n is the simplest, with onboard stereo microphones. The H5 offers changeable microphone capsules but records at 16- or 24-bit. I did not find a Zoom page with H1n specifications on November 14, 2026, so its column uses the Amazon listing only.</p>
""" + DISC + quick([("Best overall", "h4ess", "XY microphones, XLR inputs, 32-bit float"),
 ("Simplest", "h1n", "onboard stereo microphones"),
 ("Most expandable", "h5", "changeable microphone capsules")], title="Quick verdict") + """
<h2>Specifications</h2>""" +
 table(["Zoom H1n", "Zoom H4 Essential", "Zoom H5"], zoom_rows, first="Specification (as listed)") + """
<p>Sources: Zoom&#39;s pages for the H4 Essential and the H5, and the Amazon listing for the H1n, opened on November 14, 2026.</p>
<h2>What matters for piano</h2>
<p>The built-in microphones decide most of the sound; the distance from the piano decides the rest. 32-bit float is a safety net for a take recorded too loud. XLR inputs matter if you later add a pair of microphones: see """ + lk("best-stereo-microphones-for-piano", "the best pair of microphones for piano") + """. For a longer list, read """ + lk("best-handheld-recorder-for-piano-practice", "the best handheld recorder for piano practice") + """.</p>""" +
 pick("h4ess", "My choice for most students.") + pick("h1n", "My choice for the student who wants the simplest.") + pick("h5", "My choice if you will change capsules.") +
 closing([("record-yourself-playing", "gear to record yourself playing"), ("microphones-and-audio-interfaces", "microphones and interfaces"), ("mic-stands-and-studio-accessories", "stands and accessories")]) + trust("recording"),
 [("Which Zoom recorder is best for piano?", "The H4 Essential, for most students: XY microphones, XLR inputs and 32-bit float."),
  ("What is the difference between the H4 Essential and H5?", "The H5 has changeable capsules and records at 16- or 24-bit; the H4 Essential records 32-bit float, per Zoom."),
  ("Is the H1n enough?", "For simple practice recordings, yes.")]))

# 30 bookshelf speakers -------------------------------------------------
S.append(spec("best-bookshelf-speakers-for-classical-music", "2026-12-01",
 "Best Bookshelf Speakers for Classical Music (2026): A Pianist's Picks",
 "Best Bookshelf Speakers for Classical Music (2026)",
 "The best powered bookshelf speakers for classical music, chosen by a concert pianist: what to listen for in a piano recording and the pairs I would look at.",
 "Listening to classical music well needs a clear middle and no harshness. Here is how I choose speakers, and the ones I would look at.",
 meta_line() + """
<p>The best bookshelf speakers for classical music are the ones that make a piano sound like a piano: clear in the middle, steady in the bass and smooth in the treble. The Edifier R1280T is a powered bookshelf pair with RCA inputs, the PreSonus Eris E5 is a pair of 5.25-inch near-field monitors, and the M-Audio BX5BT adds Bluetooth.</p>
""" + DISC + quick([("Best for the living room", "r1280t", "powered bookshelf speakers with RCA inputs"),
 ("Most accurate", "e5pair", "a pair of 5.25-inch two-way near-field monitors"),
 ("Best with Bluetooth", "bx5bt", "5-inch desktop monitors with Bluetooth")]) +
 how_i_choose("I listen to a solo piano recording I know well and ask three questions: is the melody clear, are the bass notes steady, and does the treble stay smooth at forte.") + """
<h2>The picks</h2>""" +
 pick("r1280t", "A pair for a shelf, not a studio.") + pick("e5pair", "A studio monitor works well as a listening speaker if you want accuracy.") + pick("bx5bt", "For streaming from a phone.") + """
<h2>Comparison</h2>""" +
 table(["Type", "Size"], trows(["r1280t", "e5pair", "bx5bt"], ["type", "size"])) + """
<h2>How to choose</h2>
<ul><li>Decide whether you want a living-room speaker or an accurate monitor.</li><li>Check the inputs match your source.</li><li>Place them at ear height, away from walls.</li></ul>
<p>See also """ + lk("best-studio-monitors-under-300", "the best studio monitors under $300") + """ and """ + lk("a-holiday-listening-list-ten-piano-pieces", "a holiday listening list of ten piano pieces") + """.</p>""" +
 closing([("speakers-for-keyboards", "speakers for keyboards"), ("studio-monitors-for-home-recording", "studio monitors"), ("music-and-wellbeing", "music and wellbeing")]) + trust("listening"),
 [("What speakers are best for classical music?", "Ones with a clear middle and a smooth treble. Listen to a piano recording you know."),
  ("Do I need powered speakers?", "Powered speakers have the amplifier built in, so you only need a source."),
  ("Bookshelf speakers or studio monitors?", "Bookshelf speakers for a living room; studio monitors for accuracy at a desk.")]))
