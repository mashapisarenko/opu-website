# -*- coding: utf-8 -*-
"""Two more queued articles, written 2026-09-19, so the blog is covered past the
end of October. Both chosen because nothing on the site answers them and adults
type them into a search box: practising where other people can hear you, and
choosing the first piece."""
import json, pathlib

SPECS = [
{
 "slug": "practicing-piano-in-an-apartment",
 "date": "2026-10-30",
 "title": "Practicing Piano in an Apartment Without Annoying Anybody",
 "description": "How to practice piano in an apartment or a shared house: what the quiet hours actually are, when headphones help and when they quietly hurt your playing, and the practice that makes no sound at all.",
 "sub": "Thin walls are the reason a surprising number of American adults stop playing. Almost none of it is necessary, and some of the best practice there is makes no sound at all.",
 "image": "lead-seated-black.jpg",
 "image_alt": "Dr. Maria Pisarenko seated at the piano",
 "cta_text": "The free course is built in short lessons, which is exactly what a considerate practice needs:",
 "cta_href": "https://youtu.be/AzU01rYWHK8",
 "cta_link": "Start at Lesson 1 &rarr;",
 "body": """
<p>I have had adult students who practiced in a closet, in a garage in January, and once, memorably, in a car with a roll-up keyboard on the passenger seat during a lunch break. Every one of them was working around the same problem: other people can hear you, and you do not want to be the neighbor everybody talks about.</p>

<p>It is worth saying plainly that this is a real obstacle and not an excuse. A beginner repeats the same four bars twenty times, slowly, with mistakes. That is far harder to live next to than a competent pianist playing a whole piece. Adults sense this, and a great many of them quietly reduce their practice to the hours when the building is empty &mdash; which usually means no practice at all.</p>

<h2>First, find out what the rules actually are</h2>

<p>Most American leases and HOA documents define quiet hours, and they are usually narrower than people assume &mdash; commonly 10 p.m. to 7 or 8 a.m. on weekdays, with a later start at weekends. Outside those hours, ordinary domestic music at a reasonable volume is normal use of a home, not a nuisance.</p>

<p>I say this because the adults who suffer most are the ones who have never read the rule and are policing themselves against an imagined one. Read yours. You may find that the 6 p.m. practice you have been avoiding was never in question.</p>

<p>The other half of this is social rather than legal, and it works better than any technique: tell your immediate neighbors that you have started learning, that you will keep to certain hours, and that they should tell you if it becomes a problem. People are far more tolerant of a noise they have been warned about and that has a human being attached to it. I have never had a student regret that conversation.</p>

<h2>Headphones: what they fix and what they quietly break</h2>

<p>A digital piano with headphones solves the problem completely, and that is why most apartment-dwelling adults end up with one. But headphones change three things about your playing, and knowing which three lets you work around them.</p>

<p><strong>They flatter your tone.</strong> Headphone sound is close, even, and forgiving. A note you struck harshly sounds fine in there; the same note across a room would not. So once a week, take the headphones off and play the same passage out loud, even at low volume. That is the version your ear should be learning from.</p>

<p><strong>They hide the room.</strong> Playing is partly listening to a sound travel and decay in a space. In headphones there is no space, so the habit of listening to the <em>end</em> of a note &mdash; the single most useful habit an adult can build &mdash; is much harder to form.</p>

<p><strong>They encourage you to play louder than you think.</strong> Volume in headphones is set by a dial, not by your arm, so your hands lose the feedback that tells them how much weight they are actually using. If you play mostly in headphones, make a point of practicing quietly on purpose sometimes, and notice how much control that takes.</p>

<p>None of this is an argument against headphones. It is an argument for not letting them be the only way you ever hear yourself.</p>

<h2>The practice that makes no sound at all</h2>

<p>Here is the part that surprises adults, and it is the reason a thin wall does not have to cost you your progress. A significant share of real practice does not require the instrument to make a sound.</p>

<p><strong>Say the notes aloud, in rhythm, without playing.</strong> Take the line you are working on and name each note in time, as if you were reading it to someone. This is the exercise that turns counting-up-from-C into actual reading, and it is silent apart from your own voice.</p>

<p><strong>Tap the rhythm, hands on your knees, counting out loud.</strong> Right hand on the right knee, left on the left. Nearly every rhythm mistake an adult makes is visible here, without a single key being pressed, and fixing it here means it never reaches your hands.</p>

<p><strong>Play on a silent keyboard &mdash; a table.</strong> With the fingering written down, play the passage on a tabletop at the speed you wish you could. Your hand learns the shape and the order. This is not a substitute for sound, but for the mechanical part of a difficult passage it is genuinely effective, and it is how pianists work on trains.</p>

<p><strong>Read the music away from the piano.</strong> Sit with the page and work out what is happening: where the phrase goes, which hand has the tune, where the same figure comes back. Adults almost never do this, and it is the single biggest difference between practicing a piece and merely repeating it.</p>

<h2>If you have an acoustic piano</h2>

<p>An upright has a soft pedal &mdash; the left one &mdash; which on most uprights moves the hammers closer to the strings and takes real volume out. Use it while you learn notes, and release it once the passage is solid, because playing everything softly forever will train a timid hand.</p>

<p>Some uprights also have a middle practice pedal that drops a strip of felt between hammers and strings. It sounds muffled and slightly awful, and it is the most neighborly setting a piano has. Treat it the way you would treat headphones: fine for the hard bar, not for the whole session.</p>

<p>Where the piano stands matters more than people expect. Against a shared wall is the worst possible place; an inside wall, on a rug, with something soft behind the instrument, can take a surprising amount of the edge off what the neighbors receive.</p>

<h2>What I would actually do</h2>

<p>Twenty minutes, three parts. Five minutes silent &mdash; say the notes, tap the rhythm. Ten minutes on the hard bar, slowly, with the soft pedal or in headphones. Five minutes playing something you already know, out loud, at a normal volume, within the hours you are allowed. That last five minutes is the part your ear needs and the part your neighbors will actually enjoy, because it is the only part that sounds like music.</p>

<p>If you are not sure whether what you are doing sounds the way you think it does, <a href="../submit.html">send me a minute of it</a>. Hearing yourself is the one part of this you cannot do alone &mdash; and it is even harder in headphones.</p>
"""
},
{
 "slug": "choosing-your-first-piano-piece",
 "date": "2026-11-02",
 "title": "Choosing Your First Piece &mdash; and Why Most Adults Choose Wrong",
 "description": "How an adult beginner should choose a first piano piece: why the famous ones are traps, the three things that make a piece learnable, and what to do with the piece you actually want to play.",
 "sub": "Almost every adult picks the piece that made them want to play. It is the most natural choice in the world and it is usually the one that stops them.",
 "image": "lead-burgundy-sofa.jpg",
 "image_alt": "Dr. Maria Pisarenko",
 "cta_text": "Every piece in the free course was chosen to be learnable in the order it arrives:",
 "cta_href": "https://www.youtube.com/playlist?list=PLmHakdUcQbtSHDPhBQL8DLmiiKe3CsRzM",
 "cta_link": "See the course &rarr;",
 "body": """
<p>Ask an adult beginner what they want to play and you will hear the same handful of answers: the Moonlight Sonata, Clair de lune, River Flows in You, Comptine d'un autre &eacute;t&eacute;, the theme from a film they love. These are not silly choices. They are the reason the person is sitting at the piano at all, and I never treat them as a joke.</p>

<p>But I do have to say the awkward thing, because nobody else will: almost every one of those pieces is harder than it sounds, and several are harder than they look. The first movement of the Moonlight is slow and quiet, which makes beginners assume it is easy, and it requires a right hand that can voice a melody over triplets while the left hand holds a line underneath &mdash; a control problem, not a speed problem, and control is the last thing a beginner acquires.</p>

<p>So the question is not whether you may play the piece you love. The question is what you play <em>on the way there</em>, and how to keep the love in the room while you do it.</p>

<h2>Three things that make a piece learnable</h2>

<p><strong>One: your hand does not have to move much.</strong> For a first piece, the five fingers should stay over five neighboring keys, or move only a little and at obvious moments. Every hand shift is a small act of aim, and aiming accurately is a skill you have not built yet. This one criterion eliminates most of the famous pieces immediately.</p>

<p><strong>Two: the two hands do different amounts of work.</strong> A good beginner's piece gives the tune to one hand and something simple to the other &mdash; single long notes, a repeated pattern, silence. Two hands doing equally busy things is the hardest coordination in music and there is no reason to meet it in week three.</p>

<p><strong>Three: you already know how it goes.</strong> This is the one adults underrate most. If you can hum the tune, your ear knows when you are wrong before your eyes do, and you correct yourself without a teacher in the room. A piece you have never heard forces you to learn the notes and the sound at the same time, which is twice the work for no extra reward.</p>

<h2>Why the famous piece is still worth keeping</h2>

<p>Here is what I do with a student who wants Clair de lune in month two. I do not tell them to forget it. I write it at the top of the page and we work backwards: what does this piece actually require? Independent hands. A quiet, even touch. Reading two staves comfortably. The pedal. Then we find the small things that build each one, and the famous piece becomes a destination with a road to it rather than a wall.</p>

<p>Adults keep going when they can see the road. What makes them stop is being told to play studies for a year with no explanation of why &mdash; or, just as often, being allowed to fight a piece that is four years above them until they conclude they have no talent.</p>

<h2>A practical first list</h2>

<p>Every one of these fits the three rules, and every one is real music rather than an exercise:</p>

<ul>
<li><strong>The opening of Ode to Joy.</strong> Five fingers, no movement, and you already know it. This is where my own method begins, by ear before reading.</li>
<li><strong>Aura Lee.</strong> A left-hand tune in a five-finger position &mdash; it teaches the weaker hand to carry a melody, which pays for years.</li>
<li><strong>When the Saints Go Marching In.</strong> Simple, rhythmic, and it teaches you to keep going through a pickup without stopping.</li>
<li><strong>Bach's Minuet in G, the first eight bars.</strong> Genuinely beautiful, genuinely eighteenth-century, and the first phrase is within reach much earlier than people think.</li>
<li><strong>Erik Satie, Gymnop&eacute;die No. 1, slowly.</strong> Reachable sooner than the other famous ones because the hands move slowly and the texture is thin &mdash; and it sounds like the record.</li>
</ul>

<p>If the piece you love is on a film soundtrack, look for whether a genuine simplified edition exists &mdash; not a butchered one, but an arrangement made by someone who kept the harmony and reduced the texture. For a lot of modern piano music, one exists, and playing a good arrangement of the thing you love beats playing a bad approximation of it.</p>

<h2>The mistake underneath the mistake</h2>

<p>The choice of piece matters less than one habit: adults tend to learn a piece by playing it from the top, again and again, until the beginning is polished and the end never arrives. Whatever you choose, learn it in sections, learn the hard section first, and learn it slowly enough that it cannot go wrong. That is what makes a piece finishable, and a finished piece is what makes an adult believe the next one is possible.</p>

<p>When you have one, <a href="../submit.html">record a minute and send it to me</a>. I will tell you what I actually hear &mdash; including whether the next piece should be harder, or whether something in this one is not finished yet.</p>
"""
},
]

pathlib.Path("_specs_batch_03.json").write_text(json.dumps(SPECS, ensure_ascii=False, indent=1), encoding="utf-8")
print("specs written:", len(SPECS))
