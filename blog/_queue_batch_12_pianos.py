# -*- coding: utf-8 -*-
# Written 2026-11-14 with the piano-department expansion of the shop. Five buyer articles for queries the blog did not answer:
# hybrid pianos, premium digital pianos, digital grands, and the UK and Canada versions of the first-piano guide.
# Rules: first person, adults who learn alone, no invented numbers or prices, every product fact from the Amazon listing opened
# on 2026-11-14, links in the standard affiliate format, US spelling, no Las Vegas.
import json, pathlib
L1 = "https://youtu.be/AzU01rYWHK8"
TAG = "musicalgalaxi-20"
DISC = ('<p><em>As an Amazon Associate I earn from qualifying purchases. That never changes what I recommend: every item here is something I would tell my own '
        'adult students to look at. Check today&#39;s price on Amazon.</em></p>')
BTN = ('style="display:inline-block;padding:9px 18px;margin:6px 0;background:#7a1f3d;color:#fff;border-radius:8px;font-weight:600;text-decoration:none;font-size:.95rem"')

def url(asin): return "https://www.amazon.com/dp/%s?tag=%s" % (asin, TAG)
def A(asin, text): return '<a href="%s" rel="sponsored nofollow noopener" target="_blank">%s</a>' % (url(asin), text)
def item(asin, name, who, text):
    return ('<h3>%s</h3><p><strong>Who it is for:</strong> %s</p><p>%s</p><p><a href="%s" rel="sponsored nofollow noopener" target="_blank" %s>See it on Amazon &rarr;</a></p>'
            % (A(asin, name), who, text, url(asin), BTN))
def spec(slug, date, title, desc, sub, body, faq, seo_title=None):
    d = {"slug": slug, "date": date, "title": title, "description": desc, "sub": sub, "image": "lead-at-the-piano.jpg",
         "image_alt": "Dr. Maria Pisarenko at the piano", "cta_text": "Forty-one lessons in order, free, at your own pace:",
         "cta_href": L1, "cta_link": "Start at Lesson 1 &rarr;", "body": body, "faq": faq}
    if seo_title: d["seo_title"] = seo_title
    return d

OUT = ('<p>The piano is only half the plan. The other half is a teacher who hears you. My <a href="../free-course.html">free 41-lesson course</a> is published in full, '
       'and when you have a recording, <a href="../submit.html">send it to me</a> and I will tell you what I hear, at no charge.</p>')

SPECS = []

SPECS.append(spec("what-is-a-hybrid-piano", "2026-11-22",
 "What Is a Hybrid Piano? A Teacher's Guide for Adults",
 "What a hybrid piano is, how it differs from a digital and an acoustic piano, and which adults should consider one, with four models checked on Amazon.",
 "A hybrid piano promises the touch of an acoustic piano with the volume control of a digital one. Here is what that means, and who should pay for it.",
 """
<p>A hybrid piano is a digital piano whose keyboard is built like an acoustic piano's: wooden keys, and a hammer mechanism under each key, with the sound made electronically so that you can wear headphones. It is not a first instrument for most adults. It is the instrument for a player who has outgrown the touch of a good portable digital piano and wants to hear and feel the difference between a soft note and a very soft one.</p>
""" + DISC + """
<h2>How is a hybrid piano different from a digital piano and an acoustic piano?</h2>
<p>An acoustic piano makes sound with strings, hammers and a soundboard, and it needs a technician to keep it in tune. A digital piano makes sound from recordings and electronics, and its keys are weighted to resemble a piano's. A hybrid sits between them: the keys and the action are closer to the acoustic mechanism, and the sound is electronic. You keep the volume control, the headphone jack and the freedom from tuning.</p>
<p>The word &ldquo;hybrid&rdquo; is used loosely by makers, so I trust the listing text instead of the word. Look for wooden keys, a named hammer or graded-hammer action, and key tops that feel like ivory and ebony. Then try it, if you can.</p>

<h2>Who should consider a hybrid piano?</h2>
<p>A returning player who studied seriously as a child and wants a better touch; an adult who has played for a few years and has started to feel the limits of the instrument; or anyone preparing repertoire where soft playing and repeated notes matter. If you are in your first year, a good weighted digital piano is enough, and I would spend the difference on lessons and a good bench. Read <a href="weighted-vs-semi-weighted-keys.html">weighted vs semi-weighted keys</a> and <a href="digital-piano-vs-acoustic-beginner.html">digital or acoustic for a beginner</a> first.</p>

<h2>Which hybrid and wooden-key pianos can I buy on Amazon?</h2>
<p>I opened each of these listings on November 14, 2026. I describe only what the listing says.</p>
""" + item("B0CJ5NPG1M", "Yamaha P-525", "A returning player who wants a wooden-key touch in a portable body.",
 "The listing names a GrandTouch-S keyboard action that replicates the detailed tonal variations of a grand piano, and updated CFX and Bösendorfer samples. It has wooden keys and a music rest, and a sustain foot switch is included.") +
 item("B0C6BVT77Q", "Kawai CA501 Digital Concert Piano", "A serious player who wants a home instrument with a hammer-action wooden keyboard.",
 "Kawai lists an 88-key digital piano with a grade-weighted hammer-action wooden-key keyboard and built-in speakers, in a rosewood cabinet. It is the most expensive piano in this guide, and it is a cabinet, so measure the room.") +
 item("B07MV2B48Q", "Yamaha CP88", "A performing pianist who wants Yamaha's stage action.",
 "The listing says 88 natural wood keys with synthetic ebony and ivory key tops and a Graded Hammer (GH3) action, three premium grand pianos, two upright pianos and five electric pianos, and a sustain pedal included. It is a stage piano, so it has no cabinet.") +
 item("B07FRVJ54X", "Kawai MP11SE", "A pianist who wants a wooden-key stage piano.",
 "Kawai describes a class-leading Grand Feel wooden-key keyboard action, with SK-EX, SK-5 and EX acoustic grand piano sounds. Like the CP88, it is built for stage and studio use.") + """
<p>For more, see the shop's page on <a href="../shop/hybrid-and-digital-grand-pianos.html">hybrid and digital grand pianos</a> and the longer list of <a href="../shop/home-digital-pianos.html">home digital pianos</a>.</p>

<h2>What are the honest limits of a hybrid piano?</h2>
<p>The sound still comes from speakers or headphones, not strings, and no listing can tell you whether the touch suits your hands. If you can play one in a shop, do. I also looked for acoustic uprights and grands on Amazon and did not find an acoustic piano I could verify as sold and shipped there. A real piano should be played, delivered by movers and tuned, so for that I suggest a local piano dealer.</p>
""" + OUT,
 [("What is a hybrid piano?", "A digital piano with an acoustic-style keyboard mechanism, usually wooden keys with hammers, and an electronic sound source. You get a touch close to an acoustic piano and a headphone jack."),
  ("Is a hybrid piano better than a digital piano?", "It has a more refined touch, which matters to an advanced or returning player. For a first-year adult beginner, a good weighted digital piano is enough."),
  ("Do hybrid pianos need tuning?", "No. The sound is electronic, so the instrument stays in tune. That is one of the reasons many adults prefer it to an acoustic piano.")]))

SPECS.append(spec("best-premium-digital-pianos-for-returning-players", "2026-11-23",
 "Best Premium Digital Pianos for Returning Players",
 "Premium digital pianos for adults returning to piano, chosen by a concert pianist from what Amazon sells: Yamaha, Kawai, Casio and Roland, checked November 14.",
 "If you studied piano as a child and want an instrument worth keeping, these are the premium digital pianos I would look at, and what each listing actually says.",
 """
<p>A returning player is easier to buy for than a beginner, because your hands already know what they want. You want a graded weighted action, a sound you can believe, three pedals and a cabinet that looks like part of the house. The premium digital pianos below are the ones I would look at on Amazon, with only what each listing states.</p>
""" + DISC + """
<h2>What makes a digital piano premium?</h2>
<p>Three things, in order. The action: a graded hammer action, where the low keys feel heavier than the high ones, with a key surface that does not slip. The sound: a concert grand sampled in detail, with the resonance of the strings and the pedal. And the cabinet: three pedals, speakers that fill a room and a body that stands steady. A bench and good headphones come last, and cost less than people think.</p>

<h2>Which premium digital pianos should I look at?</h2>
""" + item("B077YT617Y", "Yamaha YDP-184", "A returning player who wants a console piano to keep for decades.",
 "Yamaha lists a Graded Hammer 3 (GH3) action with synthetic ivory key tops and the CFX Premium Grand Piano voice.") +
 item("B0C6BVTKH4", "Kawai CN201", "A player who wants a Kawai cabinet.",
 "The listing says an 88-key digital piano with 19 sounds and built-in speakers, in a premium satin black cabinet.") +
 item("B0FLF823ZQ", "Kawai CX102", "A home player who values the sound of a concert grand.",
 "Kawai lists the Shigeru Kawai SK-EX concert grand piano sound with Harmonic Imaging technology.") +
 item("B0DR38F47F", "Casio Celviano AP-S200", "A living room that wants a slim console.",
 "Casio lists a new concert grand piano tone with damper and sympathetic resonance and a smart scaled hammer action with 88 fully weighted keys, in a slim console.") +
 item("B08SC23H65", "Roland FP-60X", "A player who wants a portable piano with a strong built-in amplifier.",
 "The listing calls it the midrange model of the FP-X series, a compact and elegant instrument with a powerful built-in amplifier.") +
 item("B08M3P4XL4", "Kawai ES920", "A returning player who wants a good action in a portable piano.",
 "Kawai lists an 88-key digital piano with Responsive Hammer III action and an onboard stereo speaker system.") + """
<h2>Where are the Clavinova, Roland LX and Kawai CA?</h2>
<p>You may be looking for the big names of the dealer showroom. On November 14, 2026 I searched Amazon for the Yamaha Clavinova CLP series and the Roland LX and HP series and did not find them, though I did find the Kawai CA501, which I describe in my article on <a href="what-is-a-hybrid-piano.html">hybrid pianos</a>. If one of those is the piano you want, a piano dealer is the right place to hear it.</p>
<p>My longer <a href="../shop/home-digital-pianos.html">home digital pianos page</a> lists more cabinets, and <a href="../shop/pianos.html">the pianos department</a> ranges from a first piano to a luxury one. When you buy, add a <a href="../shop/piano-benches-and-stands.html">bench that adjusts</a> and a <a href="../shop/headphones-for-piano.html">pair of headphones</a>.</p>
""" + OUT,
 [("What is the best premium digital piano for a returning player?", "The one whose keys you like under your hands. From the list, I would start with the Yamaha YDP-184 or the Kawai CN201 as cabinets, and the Roland FP-60X or Kawai ES920 as portables."),
  ("Do I need three pedals?", "For much classical repertoire, yes. A cabinet with three pedals, such as the ones listed, gives you the soft and middle pedals as well as the sustain pedal."),
  ("Is a premium digital piano worth it?", "If you will play most days for years, yes, because the key action is what you practice. If you are unsure you will keep playing, begin with a good portable and move up later.")]))

SPECS.append(spec("are-digital-grand-pianos-worth-it", "2026-11-24",
 "Are Digital Grand Pianos Worth It? A Teacher's Answer",
 "Is a digital grand piano worth the money for an adult? A concert pianist explains who it suits, what it costs you in space, and what to buy instead.",
 "A digital grand looks like a grand piano and has the volume control of a digital one. Whether it is worth it depends on a few honest questions.",
 """
<p>A digital grand piano is a digital piano in the shape of a small grand. It is worth it if you want the look and the footprint of a grand in a room, you want headphones and no tuning, and you have decided that a luxury purchase is right for you. It is not worth it if what you want is a better touch, because a wooden-key upright-style or portable instrument gives you that for less.</p>
""" + DISC + """
<h2>What do you really get with a digital grand?</h2>
<p>The grand shape, mostly. The keys, the sound and the pedals are what matter for playing, and many digital pianos have them. A digital grand adds the lid, the legs and a presence in the room. For some adults, that presence is the reason they will sit down every evening, and that is a good reason. It is just not a musical one, so be honest with yourself about which you are paying for.</p>
<h3><a href="https://www.amazon.com/dp/B0BSKN3HNT?tag=musicalgalaxi-20" rel="sponsored nofollow noopener" target="_blank">Roland GP-3</a></h3>
<p><strong>Who it is for:</strong> A home that wants a grand-shaped piano without an acoustic one.</p>
<p>Roland describes the GP-3 as the most compact and affordable grand in its digital grand line, with Roland technologies in a compact grand piano design. It is the one digital grand I found on Amazon on November 14, 2026 that I could verify as available.</p>
<p><a href="https://www.amazon.com/dp/B0BSKN3HNT?tag=musicalgalaxi-20" rel="sponsored nofollow noopener" target="_blank" """ + BTN + """>See it on Amazon &rarr;</a></p>

<h2>What should I consider instead of a digital grand?</h2>
<p>If you want the best touch for the money, look at wooden-key models such as the <a href="what-is-a-hybrid-piano.html">hybrid pianos in my guide</a>, or at a premium cabinet from my list of <a href="best-premium-digital-pianos-for-returning-players.html">premium digital pianos</a>. If you want a piano that costs less and still serves a first few years, begin with a <a href="../shop/digital-pianos.html">portable digital piano</a>. If you want a real acoustic grand, go to a piano dealer, because I could not verify one sold and shipped on Amazon.</p>

<h2>How do I decide?</h2>
<p>Measure the room first: a grand-shaped instrument needs floor space and a clear wall. Then ask whether you would play it more because it is beautiful. If yes, and the cost is comfortable, it can be a good choice. If you are still unsure, spend less now, keep playing, and revisit the question when your hands can tell you which touch you want.</p>
""" + OUT,
 [("Is a digital grand piano better than a digital piano?", "It is not better to play. It looks like a grand and fills a room like one. For touch and sound, a good wooden-key digital piano can match it for less."),
  ("Do digital grand pianos have the same keys as acoustic grands?", "I cannot say that for any model. Read what the listing says about the keyboard, and play one if you can."),
  ("Can I buy an acoustic grand piano on Amazon?", "I searched on November 14, 2026 and did not find an acoustic grand I could verify as sold and shipped there. A local piano dealer is the safer route.")]))

SPECS.append(spec("best-digital-pianos-for-adult-beginners-in-the-uk", "2026-11-25",
 "Best Digital Pianos for Adult Beginners in the UK",
 "Digital pianos for UK adult beginners, chosen by a concert pianist: models I found on Amazon UK on November 14, with what to check about plugs and delivery.",
 "If you are in the UK, here are the beginner digital pianos I found on Amazon UK, what I would check on each listing, and why weighted keys come first.",
 """
<p>The best digital piano for an adult beginner in the UK is the same as anywhere: 88 weighted keys, a real piano sound, a sustain pedal and a headphone jack. The question for a UK buyer is whether the model is sold on Amazon UK. I searched Amazon UK on November 14, 2026 for each model below and found it listed. My links go to Amazon.com and open your local Amazon store when the model is sold there.</p>
""" + DISC + """
<h2>What should a UK buyer check?</h2>
<p>Check the plug and the power supply. A digital piano bought for the UK should come with a UK plug or a suitable adapter, and the listing will say. Check delivery times for a large box, and decide where it will stand before it arrives. For furniture, note that a bench is called a piano stool in the UK, and a keyboard stand is sold separately. A sustain pedal is the same everywhere.</p>

<h2>Which digital pianos did I find on Amazon UK?</h2>
""" + item("B0CBN7HYKB", "Yamaha P-225", "An adult beginner who wants to buy once and keep it.",
 "The Amazon.com listing describes a portable 88-key digital piano with weighted keys, a music rest, a sustain foot switch and built-in speakers. Amazon UK lists the P-225 digital piano with 88 graded hammer compact keys.") +
 item("B07MH391ZF", "Roland FP-10", "An adult beginner in a small room.",
 "A compact 88-note digital piano with SuperNATURAL piano tones. Amazon UK lists the FP-10.") +
 item("B08SC23H65", "Roland FP-60X", "A player who wants more sound from a portable.",
 "The listing describes a pro performance 88-note digital piano with a powerful built-in amplifier. Amazon UK lists the FP-60X.") +
 item("B09GG8SCBF", "Casio Privia PX-S1100", "A small flat where a slim piano helps.",
 "The listing describes 88 touch-responsive weighted keys in an ultra-portable slim body. Amazon UK lists the PX-S1100 as a stage piano in black and white.") +
 item("B0G2YQP8KL", "Alesis Recital Pro", "A careful first budget with fully weighted keys.",
 "The listing says 88 weighted hammer-action keys with adjustable touch response. Amazon UK lists the Recital Pro.") +
 item("B0GJX8NJS8", "Yamaha Arius YDP-105", "A family that wants a cabinet piano.",
 "An upright-style cabinet with graded hammer action. Amazon UK lists the Arius YDP-105.") + """
<p>Not every model in my US shop is sold in the UK; the Roland FP-30X, for example, did not appear in my search on Amazon UK. When you click a link, check that the page that opens is the model you expect. For the longer shop lists, see <a href="../shop/digital-pianos.html">portable digital pianos</a>, <a href="../shop/home-digital-pianos.html">home digital pianos</a> and the <a href="../shop/pianos.html">pianos department</a>. Then add a <a href="../shop/piano-benches-and-stands.html">bench</a>, a <a href="../shop/piano-pedals.html">pedal</a> and <a href="../shop/headphones-for-piano.html">headphones</a>.</p>
""" + OUT,
 [("Do these links work in the UK?", "Yes. They go to Amazon.com and open Amazon UK when the model is sold there. Check the page that opens is the model you expect."),
  ("What is a piano stool in the UK?", "The same thing as a piano bench in the US. Choose an adjustable one so your forearms sit level with the keys."),
  ("Do I need a UK-plug digital piano?", "You need the right power supply for UK sockets. The listing for your country will state what comes in the box; if it does not, buy a suitable adapter.")]))

SPECS.append(spec("best-digital-pianos-for-adult-beginners-in-canada", "2026-11-26",
 "Best Digital Pianos for Adult Beginners in Canada",
 "Digital pianos for Canadian adult beginners, chosen by a concert pianist: eight models I found on Amazon Canada on November 14, from Yamaha, Roland and Donner.",
 "If you live in Canada, these are the beginner digital pianos I found on Amazon Canada, what each is for, and what to check before you order.",
 """
<p>The best digital piano for an adult beginner in Canada has 88 weighted keys, a real piano sound, a sustain pedal and a headphone jack. I searched Amazon Canada on November 14, 2026 for each model below and found it listed, most with the same listing code as the US page. My links go to Amazon.com and open Amazon Canada when the model is sold there.</p>
""" + DISC + """
<h2>What should a Canadian buyer check?</h2>
<p>Check delivery to your province, especially for a large box in winter, and check that a sustain pedal and a power supply for North American sockets come in the box. A bench is a bench in Canada as in the US; choose one that adjusts.</p>

<h2>Which digital pianos did I find on Amazon Canada?</h2>
""" + item("B00UJ9LNDK", "Yamaha P-45", "An adult beginner who wants weighted keys on a plain, reliable piano.",
 "The listing describes an 88-key weighted portable digital piano with a music rest, a sustain foot switch and built-in speakers. Amazon Canada lists the P-45.") +
 item("B0F9H3SHFJ", "Yamaha P-145BT", "An adult beginner who plays along with apps.",
 "The listing describes an 88-key digital piano with weighted keys, a compact design and Bluetooth. Amazon Canada lists the P-145BT.") +
 item("B0CBN7HYKB", "Yamaha P-225", "An adult beginner who wants to buy once and keep it.",
 "A portable 88-key digital piano with weighted keys. Amazon Canada lists the P-225.") +
 item("B07MH391ZF", "Roland FP-10", "A small room.",
 "A compact 88-note digital piano with SuperNATURAL piano tones. Amazon Canada lists the FP-10.") +
 item("B08SBZW46G", "Roland FP-30X", "A beginner who wants a stronger sound.",
 "An 88-note digital piano with a built-in amplifier. Amazon Canada lists the FP-30X.") +
 item("B08SC23H65", "Roland FP-60X", "A player who wants to grow into a bigger sound.",
 "A pro performance 88-note digital piano with a powerful built-in amplifier. Amazon Canada lists the FP-60X.") +
 item("B0893VW8MV", "Donner DDP-300", "A careful budget with weighted keys.",
 "The listing says 88 graded hammer-action weighted keys with 10 grand piano timbres and 128-note polyphony. Amazon Canada lists the DDP-300.") +
 item("B0GJX8NJS8", "Yamaha Arius YDP-105", "A family that wants a cabinet piano.",
 "An upright-style cabinet with graded hammer action. Amazon Canada lists the Arius YDP-105.") + """
<p>The longer lists are in the shop: <a href="../shop/digital-pianos.html">portable digital pianos</a>, <a href="../shop/home-digital-pianos.html">home digital pianos</a> and the <a href="../shop/pianos.html">pianos department</a>. Add a <a href="../shop/piano-benches-and-stands.html">bench</a>, a <a href="../shop/piano-pedals.html">sustain pedal</a> and <a href="../shop/headphones-for-piano.html">headphones</a>, and read my guide to <a href="how-many-keys-do-i-need-piano.html">how many keys you need</a> before you decide.</p>
""" + OUT,
 [("Do these links work in Canada?", "Yes. They go to Amazon.com and open Amazon Canada when the model is sold there. Check that the page that opens is the model you expect."),
  ("Which digital piano should a Canadian adult beginner buy?", "One with 88 weighted keys, a real piano sound and a sustain pedal. The Yamaha P-45 and Roland FP-10 are simple starts, and the P-225 and FP-30X are steps up."),
  ("Will the power supply fit Canadian sockets?", "Canada uses the same sockets as the US, so a North American power supply fits. Check what comes in the box.")]))

if __name__ == "__main__":
    out = pathlib.Path(__file__).resolve().parent / "_specs_batch_12_pianos.json"
    out.write_text(json.dumps(SPECS, indent=1, ensure_ascii=False), encoding="utf-8")
    print("wrote", out.name, len(SPECS))
