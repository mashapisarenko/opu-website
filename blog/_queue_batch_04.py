# -*- coding: utf-8 -*-
import json, pathlib

SPECS = [
{
 "slug": "how-to-read-the-bass-clef",
 "date": "2026-09-30",
 "title": "The Bass Clef Is Not Harder &mdash; It Is Just Later",
 "description": "Adult beginners find the bass clef difficult for one reason only: they have had far less practice with it. A concert pianist explains what the clef actually does and gives the landmark method that makes it readable.",
 "sub": "Adults tell me the bass clef is the hard one. It is not harder. You have simply seen it a tenth as often, and there is a fix for that.",
 "image": "lead-concert-gown.jpg",
 "image_alt": "Dr. Maria Pisarenko, concert pianist",
 "cta_text": "The free course reaches the bass clef in order, at the right moment:",
 "cta_href": "https://youtu.be/AzU01rYWHK8",
 "cta_link": "Start at Lesson 1 &rarr;",
 "body": """
<p>Every adult beginner I have taught has said some version of this: the treble clef is fine now, but the bass clef will not stick.</p>

<p>It is worth saying plainly that there is nothing harder about it. The symbols are the same symbols, the lines are the same lines, and the logic is identical. What is different is exposure. Melodies live in the treble clef, so by the time a beginner meets the bass clef in earnest they have read perhaps five hundred treble notes and forty bass ones. That is not a difficulty of the clef. It is a difficulty of arithmetic.</p>

<h2>What a clef actually does</h2>

<p>This is the part that is rarely explained, and it makes everything afterwards easier.</p>

<p>Five lines on their own mean nothing at all. They are a grid with no address. A clef is the symbol that fixes one specific note to one specific line, and from that single anchor every other line and space follows automatically.</p>

<p>The treble clef curls around the second line from the bottom, and that line is <strong>G above middle C</strong>. The bass clef's two dots sit either side of the second line from the top, and that line is <strong>F below middle C</strong>.</p>

<p>That is the whole job of a clef: one note, nailed down. Everything else is counting from it. So the bass clef is not a new alphabet &mdash; it is the same staff with the anchor moved.</p>

<h2>Why the piano needs two of them</h2>

<p>A piano covers a very wide range. Written on one staff, the low notes would need so many extra little lines below it that the page would be unreadable.</p>

<p>So we use two staves joined by a brace &mdash; the grand staff &mdash; with the treble clef above for the higher range and the bass clef below for the lower. Middle C sits exactly between them, which is why it gets its own small line in both: it is the hinge.</p>

<p>Once you see the two staves as one continuous keyboard with a gap in the middle for middle C, the relationship between them stops being arbitrary.</p>

<h2>Three landmarks, and stop counting</h2>

<p>The common advice is a mnemonic for every line and space. I would rather you learned three positions solidly and worked outward from them, because that is what fluent readers actually do &mdash; a reader does not count up from the bottom line, they recognise a neighbourhood.</p>

<p><strong>1. Middle C</strong> &mdash; the note on its own little line just above the bass staff. It is the hinge between the hands and the first thing to know cold.</p>

<p><strong>2. F on the fourth line</strong> &mdash; the line the bass clef's two dots point at. This is why the bass clef is also called the F clef, and it is the anchor the symbol itself is telling you about.</p>

<p><strong>3. The low G on the first line</strong> &mdash; the bottom line of the bass staff.</p>

<p>Learn those three so that you know them without thinking. Then read every other note as a step or a skip from the nearest one: <em>one above F, two below middle C.</em> That is faster than counting from the bottom, and it is the habit that eventually turns into simply seeing the note.</p>

<h2>The exercise that actually works</h2>

<p>The reason the bass clef does not stick is exposure, so the cure is exposure &mdash; but of a specific kind.</p>

<p><strong>Say the note names aloud, without playing.</strong> Take the left-hand line of whatever you are working on and read the names out loud, in rhythm, hands off the keyboard. Thirty seconds, twice a day.</p>

<p>Saying the name out loud does something that silent looking does not: it forces you to commit to an answer, and you find out immediately whether you knew it or were guessing. Silent reading lets you skate. This is ordinary practice in European music schools, where children sing note names from their first lessons, and it is the single reason their reading is faster.</p>

<p>Add one more thing: <strong>read the bass line first</strong> when you open a new piece. Most people read the melody first every time, which is precisely why the treble clef gets five hundred repetitions and the bass clef gets forty. Reverse the order for a month and the gap closes on its own.</p>

<h2>What not to do</h2>

<p><strong>Do not write the letter names under the notes.</strong> I know why it is tempting. But once the letters are there, your eye reads the letters and never learns the notes &mdash; and the pencil marks have to come off eventually, at which point you are back where you started, with lost time. If a passage is genuinely beyond you, the answer is an easier passage, not a translation.</p>

<p><strong>Do not learn it by finger number either.</strong> &ldquo;Third finger&rdquo; is not a note. It works until the hand moves, and then nothing works.</p>

<h2>How long this takes</h2>

<p>Less time than you fear, if the practice is daily and out loud. Adults who read their bass line aloud for half a minute twice a day generally stop thinking about the bass clef within about a month. Adults who wait for it to happen through ordinary playing can wait a year, because ordinary playing keeps handing the left hand the same few notes.</p>

<p>It was never the harder clef. It was the one you had barely met.</p>

<p>If you would like to know whether your reading is genuinely fluent or fast guessing &mdash; the two look identical from the inside &mdash; <a href="../submit.html">send me a minute of you playing, and I will tell you which it is</a>.</p>
"""
},
{
 "slug": "returning-to-piano-as-an-adult",
 "date": "2026-10-02",
 "title": "Coming Back to the Piano After Twenty Years Away",
 "description": "Returning adult pianists are not beginners, and should not be taught as if they were. A concert pianist on what actually comes back, what does not, and the first six weeks of a sensible return.",
 "sub": "You are not starting from nothing, whatever it feels like in the first week. But you are also not starting from where you left off, and knowing the difference saves a year.",
 "image": "lead-burgundy-sofa.jpg",
 "image_alt": "Dr. Maria Pisarenko, concert pianist and university professor",
 "cta_text": "The free course, if you would rather rebuild the foundation properly:",
 "cta_href": "https://youtu.be/AzU01rYWHK8",
 "cta_link": "Start at Lesson 1 &rarr;",
 "body": """
<p>A particular kind of student writes to me. They played as a child &mdash; four years, seven years, up to some exam &mdash; and then school ended, or a teacher moved, or life did what life does. Twenty or thirty years later there is a piano in the house again, and they sit down, and what comes out is so far below what they remember that they close the lid.</p>

<p>If that is you, the most useful thing I can tell you is that the first week is lying to you, in both directions.</p>

<h2>What genuinely comes back, and fast</h2>

<p><strong>Reading.</strong> Note-reading is stored like reading words, and it returns startlingly quickly &mdash; days, not months, for someone who read fluently as a child. It will feel rusty for two weeks and then simply be there.</p>

<p><strong>The pieces your hands learned deeply.</strong> Anything you played hundreds of times is not gone. It is often under your fingers before you consciously recall it, which is why returning adults so often find one old piece arriving nearly intact while everything else is a mess.</p>

<p><strong>Your ear.</strong> Whatever musical judgement you developed is fully intact, and in fact it has gone on developing through thirty years of listening. This is the great asset of a returner &mdash; and, in the first weeks, the great misery, because your ear is now far ahead of your hands and it tells you so with every note.</p>

<h2>What does not come back on its own</h2>

<p><strong>The physical condition of the hand.</strong> Speed, endurance and evenness are trained states, not knowledge, and they fade like any other trained state. This is what makes the first week feel catastrophic. It is also the part that rebuilds fastest, given daily work &mdash; usually far faster than it was built the first time.</p>

<p><strong>Anything you never actually had.</strong> Here is the uncomfortable part, and the reason I write about returners separately from beginners. Most children learn piano without ever being taught how the sound is produced: weight, release, wrist, the hand travelling. If nobody taught you that at nine, it did not vanish &mdash; it was never there. And when a returner assumes the problem is rust, they practise harder at a technique that was always missing, and plateau.</p>

<p><strong>Habits, which come back perfectly.</strong> Including the bad ones. A wrist that dropped in 1998 drops now. Rust fades; habits do not.</p>

<h2>The mistake almost every returner makes</h2>

<p>They go straight to the hardest piece they ever played.</p>

<p>It is completely understandable &mdash; that piece is the proof that you could do this. But it was learned over months, by a hand in training, probably with a teacher, and it is now being attempted by a hand that has not worked in twenty years. The result is a piece played badly, which is exactly the experience most likely to close the lid again.</p>

<p>Start two levels below what you think you can play. Not one &mdash; two. Play things that are easy enough to sound genuinely good, because your ear is ahead of your hands and it needs feeding. The hard piece will be there in three months, and by then it will be playable rather than survivable.</p>

<h2>The first six weeks</h2>

<p><strong>Weeks one and two &mdash; the body only.</strong> Fifteen minutes a day. Bench height first: forearm level with the tops of the keys, never below. Then two minutes daily on a single note, letting the arm's weight down through a firm fingertip and releasing at once. Then easy pieces, slowly, listening.</p>

<p>This feels like a waste of a returner's time. It is not. If nobody taught you the physical side at nine, these two weeks are the thing that makes the next twenty years different from the first four.</p>

<p><strong>Weeks three and four &mdash; reading, deliberately.</strong> Something new and easy every day, read at sight, badly, without stopping to fix it. Your reading is in there; it needs traffic, not study.</p>

<p><strong>Weeks five and six &mdash; one real piece.</strong> Now choose something you want, and work it the way a professional does: the difficult bar first, slowly, hands separately, five clean repetitions before the tempo goes up at all. Not from the top every time.</p>

<h2>One thing you must do that you did not do at nine</h2>

<p>Film yourself, one minute, once a week.</p>

<p>As a child you had somebody in the room whose entire job was to notice the wrist, the collapsing finger, the rushing. As a returning adult you almost certainly do not, and your own ear &mdash; excellent as it is &mdash; hears what you intended. The camera does not.</p>

<p>This is also where a returner has an advantage a child never has: you can be told something once and act on it. Most of what a weekly lesson gave you at nine was noticing, not explaining, and noticing can be replaced by a phone on the music stand and a pair of outside ears now and then.</p>

<p>If you would like those outside ears, <a href="../submit.html">send me the minute &mdash; I answer recordings myself and it is free</a>. Tell me what you played as a child and where you stopped; it changes what I look for.</p>

<p>You are not starting again. You are restarting with an adult's understanding, an adult's ear and thirty years of listening behind you &mdash; and, this time, the chance to be taught the half nobody taught you the first time.</p>
"""
},
{
 "slug": "learning-piano-without-a-teacher",
 "date": "2026-10-05",
 "title": "Learning Piano Without a Teacher: What You Can and Cannot Diagnose Alone",
 "description": "A concert pianist is honest about self-teaching the piano — the parts an adult can genuinely do alone, the four faults that are almost impossible to catch in yourself, and how to cover the gap without weekly lessons.",
 "sub": "Most of learning the piano can now be done alone, and done well. Four specific things cannot &mdash; and knowing which four is the whole difference.",
 "image": "lead-pink-floor.jpg",
 "image_alt": "Dr. Maria Pisarenko, concert pianist and university professor",
 "cta_text": "Forty-one lessons, in order, free &mdash; built for exactly this situation:",
 "cta_href": "https://youtu.be/AzU01rYWHK8",
 "cta_link": "Start at Lesson 1 &rarr;",
 "body": """
<p>I teach at university level and I take private students, so you would expect me to tell you that self-teaching does not work. I am not going to, because it is not true &mdash; and saying it would be a way of selling lessons rather than answering the question.</p>

<p>A great deal of learning the piano can be done alone now, and done properly. But not all of it, and the part that cannot is specific enough to name. Once you know which four things you are blind to, you can cover them deliberately instead of hoping.</p>

<h2>What you can genuinely do alone</h2>

<p><strong>Reading music.</strong> Entirely. It is a knowledge skill: the page tells you whether you were right, immediately and without opinion. Adults learn to read faster than children do, because counting, patterns and symbols are already familiar.</p>

<p><strong>Theory.</strong> Key signatures, intervals, chords, why a piece goes where it goes. All of it is learnable from good material, and adults tend to enjoy it more than children because they want the reasons.</p>

<p><strong>Rhythm and counting.</strong> Mostly. Counting aloud is self-correcting &mdash; if you cannot count aloud and play at once, you are going too fast, and that is a test you can administer to yourself.</p>

<p><strong>Learning the notes of a piece.</strong> Absolutely. This is the bulk of practice time, and it needs patience rather than supervision.</p>

<p><strong>Building the habit.</strong> Which is, in the end, the thing most likely to decide whether you are playing in a year.</p>

<h2>The four things you cannot diagnose in yourself</h2>

<p>Every one of these has the same shape: it is invisible from the inside, because you hear and feel what you intended rather than what happened.</p>

<p><strong>1. Tension.</strong> You cannot feel your own tension until it has become pain. A wrist that drops on the hard bar, a shoulder that lifts, a thumb clamped against the side of the hand &mdash; these are the most consequential faults in adult playing and the least available to introspection. By the time they announce themselves, they are months old.</p>

<p><strong>2. Your own sound.</strong> You hear the sound you meant to make. Sitting at the instrument, with the keys under your hands and the intention still in your head, you are the worst-placed listener in the room. A recording of yourself is a genuine shock the first time, for everyone, including professionals.</p>

<p><strong>3. Unevenness.</strong> Almost every beginner plays the fourth and fifth fingers more quietly than the others and does not hear it, because the brain helpfully corrects the volume of notes it expected. This is not a flaw in you; it is how listening works.</p>

<p><strong>4. What to do next.</strong> Not what to learn next &mdash; a good course sequences that. What to <em>do</em>: whether a passage needs slower practice, separate hands, a fingering change, or leaving alone for a week. A teacher's real value is rarely the explanation. It is the diagnosis.</p>

<h2>How to cover the gap without weekly lessons</h2>

<p><strong>Film yourself once a week, one minute, and watch it that evening.</strong> Phone on the music stand, roughly at keyboard height so the wrist line is visible. This covers a surprising amount of items one and three: a dipping wrist and a lifting shoulder are obvious on video and invisible in the moment. Watch it the same day &mdash; if you wait, you will be watching a stranger.</p>

<p><strong>Listen back with your eyes shut.</strong> Play the audio of that minute without watching, and listen for one thing only: are all the notes the same weight? You will hear the fourth and fifth fingers disappear. You cannot hear it while playing; you can hear it on a recording almost at once.</p>

<p><strong>Use a real course, in order, rather than a playlist.</strong> The ordering is most of what a curriculum is. Jumping between videos by topic gives you gaps you will not know you have &mdash; and gaps in the first year are exactly what produces a plateau in the second.</p>

<p><strong>Get outside ears occasionally.</strong> Not weekly. A handful of times a year is enough to catch a fault before it sets. That is why I read and answer recordings people send me, and why it is free: the point is that a small physical fault caught in month two takes a minute to correct, and the same fault caught in year two takes a season.</p>

<h2>What I would say if you asked me straight</h2>

<p>Teach yourself. Use a proper sequence, do fifteen honest minutes a day, film one minute a week, and send it to somebody who can hear what you cannot every few months.</p>

<p>An adult doing that will get further in a year than most people with a weekly lesson and no practice between them. The lesson was never the magic. The noticing was &mdash; and noticing can be arranged.</p>

<p>When it is worth paying for a teacher is a narrower question than the internet suggests: when you have a physical problem that recording has not solved, when you want to play something genuinely difficult, or when you have plateaued and cannot see why. Those are diagnosis problems, and diagnosis is the thing a book, a video and your own ear cannot give you.</p>

<p>If you would like me to look at where you are now, <a href="../submit.html">send me a minute of your playing</a>. And if you have not started, <a href="../free-course.html">the whole forty-one-lesson course is free and in order</a> &mdash; begin at the beginning, not with the piece you want to play.</p>
"""
},
]

pathlib.Path("_specs_batch_04.json").write_text(json.dumps(SPECS, ensure_ascii=False, indent=1), encoding="utf-8")
print("specs:", len(SPECS))
