# -*- coding: utf-8 -*-
# Written 2026-10-18 after the adult-motives audit (Project doc
# claude/OPU_Blog_Audit_Adult_Motives_2026-10-18.md): ten articles for the motives
# the blog had not yet answered on their own page - brain health, stress, apps vs
# a teacher, arthritis, choosing a method book, burnout, embarrassment, the empty
# nest, online vs in-person, duets. Queued one a day after the last queued date.
# Her rules: first person, never "I was a beginner too", no invented students,
# numbers, prices or dates about her, no parent/child audience, US spelling.
# Research figures are only those verified at the source (listed in the audit doc).
import json, pathlib
L1 = "https://youtu.be/AzU01rYWHK8"
def spec(slug, date, title, desc, sub, image, alt, cta, body, seo_title=None):
    d = {"slug": slug, "date": date, "title": title, "description": desc, "sub": sub,
         "image": image, "image_alt": alt, "cta_text": cta, "cta_href": L1,
         "cta_link": "Start at Lesson 1 &rarr;", "body": body}
    if seo_title:
        d["seo_title"] = seo_title
    return d

SPECS = [
spec("piano-and-the-aging-brain", "2027-01-30",
 "Does Playing Piano Keep Your Brain Sharp? What Research Says",
 "Does learning piano help the aging brain? What controlled studies of older adults found, what they did not, and how to practice if brain health is your reason.",
 "Keeping the mind sharp is one of the best reasons to start. It is also the reason most often oversold. Here is what the studies show, and how to practice so the work counts.",
 "lead-at-the-piano.jpg", "Dr. Maria Pisarenko at the piano",
 "Structured lessons, in order, free:",
"""
<p>"I want to keep my mind sharp." Adults give me this reason more often than almost any other, and after fifty it comes up in nearly every first conversation. It is a very good reason to sit down at the piano. It is also the reason that attracts the most exaggeration online, so before anything else I want to separate what researchers have actually found from what gets promised in advertisements.</p>

<h2>Why the piano asks so much of the brain</h2>

<p>Think about what happens in a single bar of easy music. Your eyes read two lines of notation at once. You translate each note into a key and a finger. Your two hands do different things at the same moment, and often at different speeds. You keep a steady count. You listen to the sound you just made and adjust the next one. And while all of that is happening, your eyes are already a beat or two ahead, preparing what comes next.</p>

<p>Very few activities combine reading, fine movement of ten fingers, timing, listening and planning in one continuous moment. That is exactly why neuroscientists find the piano so interesting, and why so many studies of learning in later life use it.</p>

<h2>What the research has found</h2>

<p><strong>A year of piano lessons, compared with a year of listening.</strong> Research teams in Geneva and Hannover followed 156 healthy older adults who had never had musical training. They were randomly assigned either to piano lessons or to a music-listening course, and tested over a full year. The results, published in the <em>European Journal of Neuroscience</em> in 2023, showed that the piano group improved more in fine motor control, and probably in working memory, and that changes in the hands went together with changes in the motor areas of the brain. The authors put their conclusion plainly: playing an instrument "promotes motor, cognitive and neural development into older age."</p>

<p><strong>Piano training and the thinking skills that organize everything else.</strong> As early as 2007, Jennifer Bugos and her colleagues reported that individualized piano instruction improved executive functioning and working memory in older adults. A randomized controlled trial published in <em>The Journals of Gerontology</em> in 2022, summarized by AARP, reported gains in working memory, processing speed and verbal fluency in adults between 60 and 80 after piano training.</p>

<p><strong>Playing an instrument and dementia.</strong> A 2022 review in <em>BMC Neurology</em> pooled long-term studies and found that older adults who played a musical instrument were less likely to develop dementia. This is an association, not proof: people who play may differ from people who do not in many other ways. AARP's Global Council on Brain Health reached a similarly careful conclusion in 2020: making music is associated with better attention, thinking and mood.</p>

<h2>What this does and does not mean</h2>

<p>It does <em>not</em> mean the piano is a medicine, or that it can prevent any illness. Nobody can honestly promise that, and I will not.</p>

<p>It does mean that learning the piano is one of the most complete workouts a healthy adult brain can be given, and that the benefits measured in these studies came from <em>learning</em> &mdash; from structured, progressive lessons in which something new and slightly difficult appeared every week. Playing the same three pieces from memory every evening is a pleasure, and I am all for it. But it is not the part of piano that asks the brain to grow.</p>

<h2>How to practice if your brain is part of the reason</h2>

<p><strong>Read the music; do not only copy it.</strong> Reading is the most demanding part of playing, and it is the part that self-taught adults most often skip by copying hands from a video. If your reason is cognitive, reading is where the work is. Start with <a href="how-to-read-piano-notes-grand-staff.html">the grand staff, explained properly</a>, and if you have been stuck for a while, read <a href="why-you-still-cannot-read-music-fluently.html">why reading stays slow and what fixes it</a>.</p>

<p><strong>Let the hands become independent gradually.</strong> Two hands doing two different things is the exact skill that challenges coordination and attention. It does not come by force; it comes by a sequence of small steps, which I explain in <a href="why-your-hands-will-not-do-two-things-at-once.html">why your hands will not do two things at once</a>.</p>

<p><strong>Memorize short pieces.</strong> Memorizing music uses several kinds of memory at once: the sound, the hand movement, the picture of the page and the structure of the harmony. <a href="how-to-memorize-a-piece-of-music.html">The four kinds of memory</a> shows how to use all of them.</p>

<p><strong>Keep something new on the music stand.</strong> A new piece, a new key, a new rhythm. Novelty is what the brain responds to. A structured course takes care of this for you, because each lesson adds one thing you have not done before.</p>

<p><strong>Practice a little every day.</strong> Twenty or thirty minutes most days does more than two hours once a week, because the brain consolidates what it learned between sessions. If time is the obstacle, <a href="practicing-piano-when-you-have-no-time.html">this is how to practice with twenty minutes</a>.</p>

<h2>Questions adults ask me about this</h2>

<p><strong>Is it too late for the benefits?</strong> The people in the Geneva and Hannover study were older adults who had never played an instrument, and they still changed over a single year. The brain stays able to learn throughout life. It learns a little more slowly than a child's, and a sensible plan simply allows for that.</p>

<p><strong>Does listening to music count?</strong> Listening is a pleasure and good for the mood, and I would never discourage it. But in that study, listening was the comparison: the group that learned to play improved more in fine motor control than the group that listened. Making music asks more of the brain than hearing it.</p>

<p><strong>Can I teach myself, or do I need structure?</strong> The people in these studies followed structured instruction, with something new each week in a sensible order. That structure is what guarantees the brain keeps meeting new challenges at the right size. A course that builds one skill at a time gives you that; a random collection of tutorials rarely does.</p>

<p><strong>How soon will I notice anything?</strong> I will not give you a number for your brain. What you will notice within weeks is easier to describe: a line of music takes less time to read, and your hands begin to do what you ask of them. That is learning, and you can see it happening.</p>

<h2>The part the studies cannot measure</h2>

<p>Working memory and processing speed can be tested in a laboratory. What cannot be tested is the feeling of sitting down in the evening and playing <em>Moon River</em> for the first time from the page, with both hands, for someone you love. Adults who come to the piano for their brain usually stay for the music.</p>

<p>If you are in your sixties or beyond, read <a href="learning-piano-after-70.html">what changes and what does not after 70</a>, and see the page for <a href="../piano-lessons-for-adults-in-their-60s.html">adults in their 60s</a>. And if you would like to begin properly, in order, from the first lesson, <a href="../start.html">start here</a>.</p>
"""),

spec("piano-for-stress-relief", "2027-01-31",
 "Piano for Stress Relief: Why Playing Quiets a Busy Mind",
 "Why playing piano is real stress relief for busy adults, the habits that quietly turn it into more stress, and a short session built to calm the mind.",
 "For twenty minutes, your hands, eyes and ears are fully occupied. There is no room left for the day you have had. Here is how to keep it that way.",
 "lead-seated-black.jpg", "Dr. Maria Pisarenko seated at the piano",
 "Short lessons you can take after work:",
"""
<p>The reason adults give me most often for starting the piano is not a particular piece, and it is not ambition. It is something like this: <em>I need something in my day that is not work, not a screen, and not somebody else's problem.</em></p>

<p>The piano is very good at this. But it can also, without anyone intending it, turn into one more place where you are judged and found wanting. So here is why playing calms the mind, and how to protect that.</p>

<h2>Why it works</h2>

<p><strong>It takes all of your attention.</strong> Reading a line of music, finding the keys, keeping time and listening to the sound use the eyes, the hands, the ears and the planning mind together. A worried mind tends to loop on the same thought. At the piano there is simply no spare attention left for the loop. Many adults describe their practice as the only twenty minutes of the day when their head is quiet, and this is the reason.</p>

<p><strong>The challenge can be set exactly right.</strong> The psychologist Mihaly Csikszentmihalyi described "flow" &mdash; the absorbed state in which time disappears &mdash; as what happens when a task is just slightly harder than your current skill. Too easy, and the mind wanders back to its worries. Too hard, and you feel anxious. At the piano you can choose the difficulty to the bar: a passage slowed down, one hand alone, a short phrase. That is a rare kind of control.</p>

<p><strong>The body lets go.</strong> Good piano playing depends on releasing the weight of the arm into the key instead of pushing with the fingers. Learning that release, over weeks, teaches the shoulders and hands what relaxed actually feels like. Many adults discover at the piano just how much tension they have been carrying all day.</p>

<p><strong>You make something.</strong> At the end of a session there is a sound that did not exist before, made by you. After a day of meetings and messages, that is no small thing.</p>

<h2>How the piano quietly becomes more stress</h2>

<p><strong>Turning practice into a performance review.</strong> If every session ends with a list of what went wrong, you have brought your office home. Mistakes are information, not verdicts. Notice them, choose one to work on, and let the rest go until tomorrow.</p>

<p><strong>Choosing music far above your level.</strong> A piece that is three years away produces exactly the anxiety you came to the piano to escape. Choose a goal piece, by all means, but practice music that is a single step ahead of you. <a href="choosing-your-first-piano-piece.html">How to choose a piece you will actually finish</a> explains how to tell the difference.</p>

<p><strong>Practicing fast.</strong> Hurrying is tension made audible. Slow practice is not only better for learning; it is calmer. <a href="how-to-practice-slowly.html">Here is how to practice slowly without it becoming meaningless</a>.</p>

<p><strong>Practice guilt.</strong> Missing a day is not a failure. Coming back tomorrow is the whole skill.</p>

<h2>A twenty-minute session built to calm the mind</h2>

<p><strong>Arrive (three minutes).</strong> Sit, put your phone in another room, and let your arms hang loosely at your sides for a few breaths. Then play single, slow notes in the middle of the keyboard, one hand at a time. Let the weight of the arm drop into each key and listen to the sound until it fades completely. This is not a warm-up exercise to get through. It is the moment you leave the day behind.</p>

<p><strong>Work (twelve minutes).</strong> Choose one small spot: two bars, one hand, one rhythm. Play it slowly until it goes right three times in a row. Then stop, even if you could keep going. Finishing on success is part of the method.</p>

<p><strong>Play (five minutes).</strong> End with something you already play and love, purely for the sound. No correcting, no counting mistakes. This is the part your mind will remember tomorrow when it decides whether to come back.</p>

<p>Evenings suit many people, as a boundary between the working day and the rest of the evening. Headphones on a digital piano make it possible at any hour; if you share walls, <a href="practicing-piano-in-an-apartment.html">this is how to practice in an apartment</a>.</p>

<h2>What to play on a hard day</h2>

<p>On a day when your mind is especially loud, do not open the new, difficult piece. Choose music that is slow, sustained and familiar. Play a single melody with one hand and let every note sing until it fades. Repeat one short phrase several times, each time listening for a rounder, warmer sound. Ten minutes of slow melody on a bad day does more for you, and for your playing, than an hour of fighting with something too hard.</p>

<p>Keep a short list on the music stand of two or three pieces you love and can play without effort. On hard days, those are the session.</p>

<h2>Let the phrase breathe</h2>

<p>Musicians talk about a phrase "breathing," and it is not only a metaphor. A singer takes a breath before each phrase; a pianist can do the same. Breathe in during the rest before a phrase, and let the phrase ride on the slow breath out. It shapes the music naturally, and it slows your breathing down without your having to think about it. <a href="the-silence-before-the-first-chord.html">The silence before the first chord</a> is about that moment of stillness before you begin.</p>

<h2>If your shoulders rise when you play</h2>

<p>Tension at the piano is common, and it is not a personal failing; it is a technical problem with a technical answer. Read <a href="why-your-hands-get-tense-at-the-piano.html">why your hands get tense and how to stop</a>. If tension is something you carry everywhere, the piano can help you notice it, but it is not a treatment for anxiety, and a doctor is the right person to talk to about that.</p>

<h2>A calm that you build</h2>

<p>The calm the piano gives is not passive, like scrolling or watching. You build it, note by note, and that is why it lasts after you close the lid. If you are in your thirties or forties and short on time, see the page for <a href="../piano-lessons-for-adults-in-their-40s.html">adults in their 40s</a>, or <a href="../start.html">start here</a> with the first lesson.</p>
"""),

spec("piano-apps-vs-a-real-teacher", "2027-02-01",
 "Piano Apps vs a Real Teacher: What an App Cannot Hear",
 "Piano apps like Simply Piano and flowkey check notes and timing. What they cannot see or hear, and how to use one without building habits you must undo.",
 "An app knows whether you pressed the right key at the right time. It does not know how you pressed it. That second question is most of what playing the piano is.",
 "lead-pink-floor.jpg", "Dr. Maria Pisarenko at the grand piano",
 "Lessons in the order musicians are taught:",
"""
<p>Many adults who write to me have already tried an app. Simply Piano, flowkey, Playground Sessions, Skoove: they are well made, they are encouraging, and for a few weeks they work. Then something stalls. The songs get harder, the hands get tired, and the progress bar stops telling you anything useful.</p>

<p>I am not against apps. I want you to know exactly what they do well and what they cannot do, so you can use one without paying for it later.</p>

<h2>What apps do well</h2>

<p><strong>They get you started.</strong> The first sound, the first song, the first small victory. For an adult who has been putting off the piano for years, that matters enormously.</p>

<p><strong>They check notes and timing.</strong> Through your device's microphone, or a cable from a digital piano, an app can tell whether you played the right key at roughly the right moment. That is real feedback, and it is available at eleven at night.</p>

<p><strong>They keep you coming back.</strong> Streaks, stars and levels are designed by people who understand motivation very well. Used lightly, they help.</p>

<h2>What an app cannot see</h2>

<p><strong>Your hand.</strong> Whether the fingers are curved or collapsed, whether the thumb hangs off the keyboard, whether the wrist has sunk below the keys. An app hears that the note was correct. It does not see that you played it with a flat finger and a locked wrist. Those habits feel fine for months and then cap your progress, and sometimes they hurt. <a href="piano-wrist-position-adults.html">The wrist is the most common adult fault</a>, and no app I know of can see it.</p>

<p><strong>Your shoulders.</strong> Tension is silent to a microphone. It shows up as a raised shoulder, a held breath, a forearm that aches after twenty minutes. You may not notice it yourself; that is exactly why it needs eyes from the outside.</p>

<h2>What an app cannot hear</h2>

<p><strong>The sound itself.</strong> Two people can press the same key at the same moment and produce completely different sounds: one harsh and thin, one round and singing. An app counts both as correct. A trained ear hears the difference instantly, and that difference is what people mean when they say someone "really plays." I wrote about this in <a href="right-notes-still-sounds-wrong.html">you can play all the right notes and it still sounds wrong</a>.</p>

<p><strong>The balance between the hands.</strong> The melody should sing above the accompaniment. An app hears both hands as a list of correct notes.</p>

<p><strong>The reason for a mistake.</strong> An app can tell you that bar twelve went wrong. It cannot tell you that it went wrong because your fourth finger was preparing too late, two bars earlier. A teacher's job is the <em>why</em>.</p>

<h2>What an app usually skips</h2>

<p>Most apps teach song by song. You follow colored notes, or a highlighted key, and you play. It is efficient for the first song and inefficient for the hundredth, because you never learn to read music independently, and every new piece starts again from zero. Reading takes weeks, not years, when it is taught in the right order. That order matters more than most adults realize, which is why <a href="russian-school-vs-american-piano-method.html">different schools of teaching</a> spend so much thought on it.</p>

<h2>How to use an app well, if you use one</h2>

<p><strong>Treat it as a practice partner, not a teacher.</strong> Use it for drilling notes and rhythm. Get your hand position, your sound and your reading from somewhere that can actually see and hear you.</p>

<p><strong>Film your hands once a week.</strong> Prop your phone at the side of the keyboard, level with the keys, and record a minute. Watch it with the sound off. Are the fingers curved? Is the wrist level? Do the shoulders stay down? You will learn more from that minute than from a week of stars.</p>

<p><strong>Learn to read alongside it.</strong> Twenty minutes of the app, ten minutes of real reading, every day. <a href="how-to-read-piano-notes-grand-staff.html">Start with the grand staff</a>.</p>

<p><strong>Stop chasing the streak when your hands hurt.</strong> No streak is worth a strained tendon. If something aches, read <a href="does-piano-playing-hurt-hands.html">what hand pain at the piano means</a>.</p>

<h2>Signs an app has stopped helping you</h2>

<p><strong>You can play songs, but you cannot read a new one.</strong> If every new piece needs the app to show you the keys, you have learned songs, not music.</p>

<p><strong>You only play in "wait" mode.</strong> Some apps offer a mode that waits for the correct note before moving on. It is useful for learning notes and harmful for rhythm if it becomes the only way you play, because real music never waits.</p>

<p><strong>Your forearm aches after practice.</strong> That is a technique problem, and no score on a screen will show it.</p>

<p><strong>You have been stuck on the same level for weeks.</strong> A plateau is normal; <a href="piano-plateau-month-four.html">here is why month four feels like going backwards</a>. But if the only advice available is "try again," you need a different kind of help.</p>

<p><strong>Your playing sounds mechanical.</strong> Correct and even, but not like music. That is the moment to start working on sound, and sound is learned from a musician.</p>

<h2>The one thing you cannot do alone</h2>

<p>The hardest part of learning without a trained musician beside you is that you cannot hear yourself from the outside. That is not a weakness of yours; it is true of every pianist, at every level, including me. It is why I read and answer recordings: <a href="../submit.html">send me a minute of your playing</a> and I will tell you, in writing, the one thing to change first. And if you want to learn in the order musicians are taught, from the first lesson, <a href="../start.html">start here</a>.</p>

<p>For more on what you can and cannot fix on your own, read <a href="learning-piano-without-a-teacher.html">learning piano without a teacher</a>.</p>
"""),

spec("learning-piano-with-arthritis", "2027-02-02",
 "Learning Piano With Arthritis or Stiff Hands",
 "Can you learn piano with arthritis or stiff fingers? A concert pianist's guide to warming up, touch, fingering, repertoire and the one pain rule that matters.",
 "Stiff hands change how you practice, not whether you can play. Here is how to work with them instead of against them.",
 "lead-burgundy-sofa.jpg", "Dr. Maria Pisarenko",
 "Gentle, unhurried lessons you can pause:",
"""
<p>"Can I still learn with my hands the way they are?" Adults in their sixties and seventies ask me this, often while looking at their knuckles. Some have arthritis; many simply have hands that are stiffer in the morning than they used to be.</p>

<p>First, the honest part: I am a pianist, not a physician. If you have arthritis, talk to your doctor before you begin, and if you can, see a hand therapist; they can tell you what movements suit your particular joints. What I can tell you is how pianists protect their hands, because good piano technique is, above all, the art of playing without strain. Those principles help stiff hands more than anyone.</p>

<h2>Warm hands play better</h2>

<p>Cold, stiff joints and a difficult passage are a poor combination. Before you sit down, hold your hands in warm water for a minute or two, or wrap them around a warm mug. Then begin with slow, easy playing: single notes, a few gentle five-finger patterns, nothing fast and nothing wide. The first five minutes of every session belong to the hands, not to the piece. <a href="five-minute-piano-warm-up.html">A five-minute warm-up that is actually worth doing</a> shows exactly what to play.</p>

<h2>Weight, not force</h2>

<p>The most important thing I teach any adult is that the sound comes from the weight of the arm dropping into the key, not from the finger pushing. For stiff hands this is not a detail; it is the whole approach. A finger that pushes works its small joints hard. A finger that simply transmits the arm's weight barely works at all.</p>

<p>Try this: let your arm hang at your side, completely loose. Lift it, place a slightly curved finger on a key, and let the arm's weight sink through it. The key goes down. You did not press. That is the touch to build everything on.</p>

<h2>Curved, but never clawed</h2>

<p>The hand should be gently rounded, as if resting on a ball. It should not be gripped into a claw. Let the fingers be as curved as is comfortable for <em>your</em> joints, not as curved as a picture in a book. <a href="piano-hand-position-curved-fingers.html">Why curved fingers matter</a> explains the principle; your comfort sets the degree.</p>

<h2>Choose the instrument for your hands</h2>

<p>The weight of the keys matters. Many digital pianos let you adjust touch sensitivity, so that a lighter stroke produces a full sound. Try several instruments in a store if you can, and choose one whose keys feel comfortable to play for ten minutes, not just for one chord. <a href="piano-for-seniors-keyboard-light-music.html">The right keyboard, light and music</a> covers the rest of the setup, and the bench matters too: <a href="piano-bench-height-posture.html">here is how to set its height</a>.</p>

<h2>Fingering is yours to adjust</h2>

<p>Printed fingering is a recommendation for an average hand. If a finger is sore or a stretch is uncomfortable, change it. Use a stronger finger, shift the hand instead of stretching, or share a passage between the hands. Pianists do this constantly; the music only cares that the right note sounds well.</p>

<h2>Avoid wide stretches, at least at first</h2>

<p>Octaves and large chords put the most strain on the hand. Early on, choose music that stays within a five-note position. When a chord is too wide, roll it gently from bottom to top instead of grabbing all the notes at once. It is a perfectly musical solution, and many great pianists with smaller hands have used it.</p>

<h2>Short sessions, more often</h2>

<p>Three ten-minute sessions spread through the day are kinder to stiff joints than one half hour, and the brain learns just as well from them. Stop before the hands are tired, not after.</p>

<h2>Music that suits stiff hands</h2>

<p>Some music is kind to the joints and some is not. Slow, lyrical pieces, where the melody moves from note to neighboring note and the hand stays in one area of the keyboard, are ideal. Fast repeated notes, octaves played one after another, and wide leaps put the most strain on the hand, so leave them for later or for never; there is more beautiful music without them than anyone could play in a lifetime.</p>

<p>When you choose a goal piece, play through the first page slowly before you commit to it. If any spot asks your hand to do something uncomfortable, it is fine to choose a different arrangement, or a different piece. <a href="choosing-your-first-piano-piece.html">How to choose a piece you will actually finish</a> has more on this.</p>

<p>And if you send me a recording, tell me about your hands. It changes the advice I give.</p>

<h2>The pain rule</h2>

<p>A mild feeling of having worked, like after a walk, is normal. Sharp pain, pain that lingers into the next day, numbness or tingling are not; stop, and speak to your doctor. Never play through pain to finish a piece. <a href="does-piano-playing-hurt-hands.html">What hand pain at the piano means</a> describes the difference in more detail.</p>

<h2>On difficult days, practice without the keys</h2>

<p>On days when the hands say no, the music does not have to stop. Read through tomorrow's piece and name the notes. Listen to a good recording of it with the score in front of you. Tap the rhythm lightly on your knee. Play it in your mind, hearing each note. This is real practice, and it makes the next day at the keyboard noticeably easier.</p>

<h2>What the piano gives back</h2>

<p>Many adults find that gentle, regular playing becomes one of the things that keeps their hands moving. I cannot promise that it will help your joints, and I will not. I can promise that stiff hands do not shut you out of music. They ask you to play the way the best pianists play anyway: with weight instead of force, with patience, and with care.</p>

<p>For more on hand care, read <a href="caring-for-your-hands-as-a-pianist.html">caring for your hands as a pianist</a>. If you are in your seventies, see <a href="learning-piano-after-70.html">what changes and what does not after 70</a> and the page for <a href="../piano-lessons-for-adults-in-their-70s.html">adults in their 70s</a>, or <a href="../start.html">start here</a> with the first lesson.</p>
"""),

spec("piano-method-book-for-adult-beginners", "2027-02-03",
 "How to Choose a Piano Method Book for Adult Beginners",
 "What to look for in a piano method book for adult beginners: real music, reading taught properly, every symbol explained first, and an author who can play.",
 "A method book is a teacher you take home. Most adults choose one by its cover. Here is what a trained musician looks at instead.",
 "lead-piano-strings.jpg", "Inside a grand piano",
 "Free lessons that go with any good method:",
"""
<p>If you are learning on your own, your method book is doing a teacher's work. It decides what you learn first, what you learn next, and what you never learn at all. Yet most adults choose one the way they choose a novel at an airport: by the cover and the first page.</p>

<p>When I open a method book, I look at different things. Here is the checklist I use.</p>

<h2>1. Is it written for adults?</h2>

<p>Not just labeled "adult," but actually written for you. Children's methods move slowly, explain little and decorate a great deal. Adults understand quickly and want to know why. A good adult book explains in a sentence what a child's book hides behind a cartoon, and moves on. It also uses music adults want to play, not songs about puppies.</p>

<h2>2. Is the print large and clear?</h2>

<p>This sounds trivial and is not. Crowded pages with small notes exhaust adult eyes, and tired eyes read badly. Open the book at a page in the middle, put it on a music stand and step back to the bench distance. Can you read it easily?</p>

<h2>3. Does it teach you to read, or only to find positions?</h2>

<p>Many beginner books place the hands on fixed positions and label the notes with finger numbers. It feels fast at first. Then the music moves to a new position and the reader is lost, because they learned "thumb on middle C" instead of reading the notes. A good book teaches you to recognize notes by where they sit on the staff and by the distance between them, so that reading grows into a skill you can take to any piece. If reading is your sticking point, read <a href="how-to-read-piano-notes-grand-staff.html">the grand staff, explained properly</a>.</p>

<h2>4. Does every symbol appear only after it has been explained?</h2>

<p>This is the test that most books fail somewhere. Turn the pages and look for a sign that appears before the book has taught it: a dot after a note, a tie, a sharp, a pedal marking, a word in Italian. For a child sitting next to a teacher, that is a small thing; the teacher explains. For an adult alone, every unexplained symbol is a moment of doubt, and doubt is where adults stop practicing. A carefully built book keeps a strict order: nothing appears before its page.</p>

<h2>5. Is the left hand treated as an equal?</h2>

<p>Many methods give the right hand the melody for months, while the left hand plays a note or two. The result is an adult whose left hand cannot read the bass clef and cannot move. Look for left-hand melodies early and the bass clef taught with the same care as the treble. I wrote about this in <a href="how-to-read-the-bass-clef.html">the bass clef is not harder, it is just later</a>.</p>

<h2>6. Does it teach how to make a sound, not only which key?</h2>

<p>Most method books teach which key to press. Few teach how to press it: the weight of the arm, the shape of the hand, the difference between a harsh sound and a singing one. In the tradition I was trained in, this comes first, before any notes, because it shapes everything after. <a href="russian-school-vs-american-piano-method.html">What the Russian school does differently</a> explains why, and <a href="what-european-music-schools-teach-that-american-adults-missed.html">what European music schools teach</a> goes further.</p>

<h2>7. Is the music real music?</h2>

<p>Exercises have their place, but adults need pieces that sound like music, early. Look at the repertoire: is there anything by Bach, Mozart, Tchaikovsky, Kabalevsky, or folk melodies arranged with taste? Or is it page after page of tunes written only to drill one skill? Pieces that sound beautiful are what keep an adult at the piano through the hard weeks.</p>

<h2>8. Does it count?</h2>

<p>Rhythm is where self-taught adults struggle most, often without knowing it. A good book asks you to count out loud from the first page, and shows you how. <a href="how-to-count-music-out-loud.html">Here is how to count without losing your place</a>.</p>

<h2>9. Who wrote it?</h2>

<p>Turn to the author's biography. Did they train as a performer? Do they play publicly, and can you hear them? Do they teach adults? A method book carries its author's understanding of the instrument, and you cannot learn more from a book than its author knows. That is why I care so much about <a href="who-taught-the-person-teaching-you.html">who taught the person teaching you</a>.</p>

<h2>10. Is there sound and video to go with it?</h2>

<p>Reading a description of a movement is not the same as seeing it. A book with recordings and video demonstrations lets you check what a page should sound and look like. If yours has none, the <a href="../free-course.html">free course on this site</a> shows each step at the piano.</p>

<h2>Signs you chose the wrong book</h2>

<p><strong>You keep skipping pages.</strong> If you regularly skip a page because it is confusing or dull, the book's order does not fit you.</p>

<p><strong>New symbols keep surprising you.</strong> If you often meet signs you were never taught, the book is relying on a teacher you do not have.</p>

<p><strong>After three months, you still need finger numbers to find the notes.</strong> Your book has taught positions, not reading.</p>

<p><strong>You never want to play anything in it for anyone.</strong> If none of the pieces sound like music you would share, motivation will run out long before the book does.</p>

<p>None of these mean you failed. They mean the book did. Changing to a better one after a month is not wasted time; staying with the wrong one for a year is.</p>

<h2>One book is enough</h2>

<p>Adults often buy three methods and finish none of them. Choose one good book and work through it in order, page by page. Add pieces you love alongside it; <a href="choosing-your-first-piano-piece.html">here is how to choose one you will actually finish</a>. For the books and keyboards I currently recommend, see <a href="../books.html">recommended books</a>, and to begin at the first lesson, <a href="../start.html">start here</a>.</p>
"""),

spec("piano-as-a-hobby-for-burnout", "2027-02-04",
 "Piano for Burnout: A Skill That Belongs Only to You",
 "Why piano is a good hobby for burned-out professionals: visible progress, no one grading you, no screen. And how to keep it from becoming another job.",
 "At work, effort disappears into other people's priorities. At the piano, every honest minute stays with you. That is why so many tired professionals end up here.",
 "lead-pink-gown.jpg", "Dr. Maria Pisarenko, concert pianist",
 "Each lesson fits a lunch break:",
"""
<p>Many of the adults who start the piano in their thirties and forties are successful at work, and tired in a way that sleep does not fix. They are not looking for one more thing to be good at. They are looking for something that is <em>theirs</em>.</p>

<p>I think the piano is unusually well suited to that, and I want to explain why, and also how to stop it from turning into the very thing you came to escape.</p>

<h2>Why the piano helps a tired mind</h2>

<p>Psychologists Edward Deci and Richard Ryan spent decades studying what keeps people motivated without rewards or pressure. Their answer, known as self-determination theory, names three needs: <strong>autonomy</strong> (you choose), <strong>competence</strong> (you get better at something real) and <strong>relatedness</strong> (you are connected to other people). Burnout often comes from work that starves all three. The piano feeds each of them.</p>

<p><strong>Autonomy.</strong> Nobody assigns you the piano. Nobody sets your deadline or reviews your quarter. You choose the piece, the hour and the pace. After a week of other people's priorities, that alone is restorative.</p>

<p><strong>Competence you can hear.</strong> At work, effort often vanishes into a project that someone else finishes, or into a metric that moves for reasons you do not control. At the piano, the connection between effort and result is direct. You practice a passage on Monday, and on Friday it sounds better. That clear, earned progress is one of the most satisfying experiences an adult can have, and it is rare in a modern job.</p>

<p><strong>Relatedness.</strong> Music is meant to be shared. Even the first simple piece played for a partner or a friend reconnects you to people in a way that has nothing to do with your title.</p>

<h2>Why it is not just another screen</h2>

<p>Most of what we do to rest still happens on a screen: streaming, scrolling, messages. The piano asks for your hands, your eyes on the page, and your ears, and it gives back a sound in the room. Put your phone in another room for twenty minutes, and notice how different that feels from twenty minutes of anything else.</p>

<h2>How high achievers ruin it</h2>

<p>I say this with respect, because the qualities that make people good at their jobs often make them impatient beginners.</p>

<p><strong>Turning it into a KPI.</strong> Streaks, minutes logged, pieces completed per month. Measuring is fine; worshipping the measure is how the piano becomes a second job. Track what you worked on, not how long.</p>

<p><strong>Skipping the foundations.</strong> Capable adults want to jump straight to the impressive piece. The foundations &mdash; hand position, reading, counting &mdash; feel slow, and they are what makes everything after them fast. <a href="how-to-practice-piano-a-method-not-more-minutes.html">A method, not more minutes</a> explains how to practice efficiently instead of heroically.</p>

<p><strong>Perfectionism.</strong> Stopping at every wrong note, starting over, never finishing a piece. That is not high standards; it is a habit that blocks learning. <a href="why-you-stop-every-time-you-make-a-mistake.html">Here is how to stop stopping</a>.</p>

<p><strong>Comparing yourself to people on the internet.</strong> The person playing Chopin in a video has a history you cannot see. Your only fair comparison is with yourself a month ago.</p>

<h2>Twenty minutes that belong to you</h2>

<p>You do not need an hour. Twenty minutes most days is a complete practice routine, if you use it well: five minutes on something you already play, ten on the smallest broken spot of the new piece, five on something purely for joy. <a href="practicing-piano-when-you-have-no-time.html">Practicing with a job, a family and twenty minutes</a> walks through it.</p>

<p>Keep a small notebook on the piano. One line a day: what you worked on, what improved. In a month you will have something work rarely gives you, a written record of your own progress.</p>

<h2>On the days you have nothing left</h2>

<p>Some evenings you will sit down with no energy at all. Have a minimum ready for those days: ten minutes, one piece you already play, slowly, for the sound. No new material, no fixing. The point of the minimum is not progress; it is keeping the thread unbroken, so that the piano stays part of your life on the hard weeks too. <a href="practicing-on-days-you-do-not-feel-like-it.html">What to practice on a day you do not feel like practicing</a> has more ideas.</p>

<h2>Make the progress visible</h2>

<p>Once a month, record the piece you are working on, with the date in the file name. Do not listen back the same day. Listen to all of them together at the end of three months. For people whose work rarely shows them clear progress, hearing their own improvement on a recording is one of the most powerful things the piano gives.</p>

<h2>A word of honesty</h2>

<p>The piano can make your days better, and for many people it becomes the part of the day they protect most fiercely. It is not a treatment for exhaustion that has become depression, and if you are there, a doctor is the first call. Music can sit beside that help, not replace it.</p>

<h2>Something that is yours</h2>

<p>Your job can change, your title can change, your company can be bought. The ability to sit at a piano and play something beautiful, once you have built it, stays with you for life. If you would like a calmer kind of session, read <a href="piano-for-stress-relief.html">piano for stress relief</a>. If you are in your thirties, see <a href="learning-piano-in-your-30s.html">learning piano with twenty minutes a day</a>, or the page for <a href="../piano-lessons-for-adults-in-their-40s.html">adults in their 40s</a>. And to begin at the beginning, properly, <a href="../start.html">start here</a>.</p>
"""),

spec("embarrassed-to-be-an-adult-piano-beginner", "2027-02-05",
 "Embarrassed to Be an Adult Piano Beginner? Read This",
 "Feeling self-conscious as an adult piano beginner? Where the embarrassment comes from, and how to learn with your dignity intact.",
 "You are competent at many things, and at the piano you are not yet. That feeling is uncomfortable, it is normal, and it passes faster than you expect.",
 "lead-concert-gown.jpg", "Dr. Maria Pisarenko, concert pianist",
 "Learn privately, at your own pace:",
"""
<p>Adults rarely say it directly, but I hear it in how they apologize before they play: <em>I know this is very simple. Sorry, I'm terrible. Please don't laugh.</em> Behind it is embarrassment, and it is one of the main reasons adults quit, or never start.</p>

<p>Researchers who study adult piano learners describe the same thing: a strong inner critic, self-consciousness about being heard, and frustration born of judging oneself too harshly. Let me take each source of that feeling seriously, because each one has an answer.</p>

<h2>"I am good at other things"</h2>

<p>This is the heart of it. You run a team, or a household, or a practice. You have not been a beginner at anything in decades, and the feeling is unfamiliar. Being bad at something in public, even a public of one, threatens a picture of yourself that you have worked hard to earn.</p>

<p>Here is a different picture. Choosing to learn something difficult, as an adult, by choice, is itself a mark of competence. Children are made to learn. You decided to. And the qualities that made you good at your work &mdash; understanding quickly, analyzing a problem, working consistently &mdash; are exactly the qualities that make adults learn the piano well. <a href="adults-learn-piano-differently.html">Adults learn differently from children, and mostly better</a>.</p>

<h2>"The pieces are so simple"</h2>

<p>Simple is not the same as childish. Some of the most beautiful music ever written for the piano is simple: a Bach minuet, a Schumann miniature, Tchaikovsky's short pieces. Concert pianists play them, and teach them to students at every level, because they are hard to play <em>well</em>. When you play a simple piece with a singing sound and a shaped phrase, you are doing what musicians do. Read <a href="tchaikovsky-childrens-album-for-adults.html">Tchaikovsky's Album for the Young, for adults</a>, and you will see why I do not consider any of this beneath anyone.</p>

<p>What matters is how you are taught. You deserve to be taught the way musicians are taught: properly, with explanations, with real music, and without being talked down to. That is a question of dignity, and it is the standard I hold myself to.</p>

<h2>"Someone might hear me"</h2>

<p>A family member in the next room. A neighbor. Practice sounds unfinished, because it is unfinished; that is what practice is. Headphones on a digital piano solve the practical side. For the rest: the people who love you are not listening critically. They are mostly glad you are doing something you wanted to do. <a href="playing-piano-for-other-people.html">Why you freeze when someone listens</a> explains the psychology of being heard, and how to get used to it gradually.</p>

<h2>"I remember an old teacher"</h2>

<p>Many adults who quit as children still carry a critical voice from an old lesson: the sigh, the ruler, the "not again." That voice is from another time, and it is not the voice of the teaching you will get now. <a href="starting-piano-again-at-40.html">The old teacher in your head</a> is about exactly this.</p>

<h2>"Everyone on the internet is better"</h2>

<p>The young pianists playing Liszt in online videos usually started as small children, practice for hours a day, and post their best take, not their first. Comparing your third month to their tenth year is not a fair comparison; it is a trap. The only comparison that tells you anything is with yourself a month ago. <a href="how-to-tell-if-you-are-actually-improving.html">How to tell if you are actually improving</a> shows how to make that comparison honestly.</p>

<h2>What I actually hear when an adult plays for me</h2>

<p>Adults often imagine that a trained musician listening to them is quietly judging every wrong note. That is not what happens. When an adult plays for me, I am listening for one thing: what single change would help most. A wrist that has dropped, a melody that is too quiet, a rhythm that is rushing. Wrong notes are usually the least interesting part, because they tend to fix themselves once the real cause is found.</p>

<p>I also hear what is good, and there is always something: a phrase that sings, a careful count, a hand that is clearly learning to relax. Part of my job is to tell you that too, because adults rarely hear it from themselves. <a href="what-a-piano-teacher-hears-that-you-do-not.html">What a piano teacher hears that you do not</a> describes this in more detail.</p>

<h2>Mistakes are information</h2>

<p>The most useful change an embarrassed adult can make is to stop treating a wrong note as a verdict on themselves. A wrong note tells you where to look. It says: this spot needs slower practice. That is all. Professional musicians make mistakes in practice constantly; the difference is that we have stopped taking them personally. <a href="why-you-stop-every-time-you-make-a-mistake.html">Why you stop at every mistake</a> shows how to change the habit.</p>

<h2>Small, private steps</h2>

<p><strong>Record yourself, and listen alone.</strong> Hearing your own playing from the outside is uncomfortable the first time and useful every time after.</p>

<p><strong>Play for one safe person.</strong> One short piece, for someone kind, without apology. Say "I've been learning this" instead of "sorry, I'm terrible."</p>

<p><strong>Keep a record of progress.</strong> Date your recordings. In three months, listen to the first one. Embarrassment does not survive that comparison.</p>

<h2>It is not too late, and it is not beneath you</h2>

<p>If the deeper worry is age, read <a href="is-it-too-late-to-learn-piano-at-40-50-60.html">is it too late to learn piano at 40, 50 or 60?</a> If you want to learn privately, at your own pace, with the explanations an adult deserves, <a href="../start.html">start here</a>.</p>
"""),

spec("empty-nest-hobby-piano", "2027-02-06",
 "Empty Nest Hobby: Why the Piano Is Worth Starting Now",
 "When the house goes quiet, many adults finally start the piano. Why it is such a good empty nest hobby, how to set up, and a realistic plan for the first year.",
 "For years your evenings belonged to everyone else. Now the house is quiet, the calendar has room, and the piano in the corner is waiting.",
 "lead-at-the-piano.jpg", "Dr. Maria Pisarenko at the piano",
 "Begin with the first lesson, at your own pace:",
"""
<p>There is a particular silence in a house after the last of the children moves out. For some people it is relief, for others it is loss, and for most it is a bit of both. And very often, somewhere in that house, there is a piano that someone once took lessons on, or a keyboard in a closet, or simply a wish that was postponed for twenty years.</p>

<p>Adults in their forties and fifties tell me the same thing in many different words: <em>I spent years making time for everyone else. Now I want something that is mine.</em> The piano is one of the best answers I know.</p>

<h2>Why now is a good time</h2>

<p><strong>You finally have the evenings.</strong> Not hours and hours, perhaps, but regular, predictable time. That regularity matters more for learning the piano than the amount.</p>

<p><strong>You have a reason.</strong> Children practice because they are told to. You will practice because you want to play a particular piece, for yourself, or for the family when they come home for the holidays.</p>

<p><strong>You understand quickly.</strong> An adult grasps in one sentence what a child needs a month to absorb. That is why adults often move through the first stages faster than they expect. <a href="learning-piano-at-50.html">What changes at 50, and what does not</a> describes this in detail.</p>

<p><strong>It fills the quiet with something you build.</strong> A quiet house can feel empty, or it can feel like room. Music changes which one it is.</p>

<h2>You are far from alone in wanting this</h2>

<p>A survey of 2,000 adults in the United Kingdom, commissioned by the orchestra London Concertante, found that about one in three regretted giving up music, and learning an instrument was the activity they regretted most. If you stopped lessons as a child, or never had the chance, the wish has probably not gone anywhere. <a href="returning-to-piano-as-an-adult.html">Coming back to the piano after twenty years away</a> is for those who played before.</p>

<h2>The piano that is already in the house</h2>

<p>If there is an acoustic piano at home that nobody has played for years, have a piano technician look at it before you start. A piano that has been neglected may need tuning, or more; a technician can tell you whether it is worth restoring. If it is not, or if you have no instrument at all, a digital piano with 88 weighted keys is a perfectly good beginning. <a href="digital-piano-vs-acoustic-beginner.html">Digital or acoustic</a> explains what actually matters.</p>

<h2>Make the room yours</h2>

<p>Put the instrument where you will see it every day, not in the room nobody uses. Good light on the music stand, a bench at the right height, the lid open. A piano behind a closed door gets played rarely. A piano you walk past, with music open on the stand, invites you to sit down for five minutes, and five minutes often becomes twenty.</p>

<h2>Choose your piece now</h2>

<p>Before you play a note, choose one piece you would love to play by the end of the first year. Write its name on a card and put it on the music stand. It does not matter whether it is <em>Moon River</em>, a hymn you remember from long ago or a Beatles song. Everything in the first months points toward it, and on the days when practice feels slow, the card reminds you why you started.</p>

<h2>A first-year plan</h2>

<p><strong>Months one to three.</strong> The foundations: how to sit, how to shape the hand, how to make a good sound, how to find any note, how to read the treble clef and count out loud. Twenty to thirty minutes a day. <a href="what-the-first-year-of-piano-actually-looks-like.html">What the first year actually looks like</a> is honest about this stage.</p>

<p><strong>Months four to six.</strong> Both clefs, both hands together, your first complete pieces. This is also when many adults hit <a href="piano-plateau-month-four.html">the plateau</a>; knowing it is coming takes most of its power away.</p>

<p><strong>Months seven to twelve.</strong> Pieces that sound like real music. A first piece played for someone. A goal piece chosen for the end of the year.</p>

<h2>The obstacles nobody mentions</h2>

<p><strong>The habit of putting yourself last.</strong> After years of arranging your schedule around other people, it can feel strange, even selfish, to protect half an hour for yourself. Put it on the calendar like any other appointment, and keep it.</p>

<p><strong>Restlessness.</strong> A quiet house can make it hard to settle. The first few minutes at the piano are the hardest; begin with something easy and pleasant, and the restlessness usually passes.</p>

<p><strong>Doubting it is worth it at this age.</strong> It is. Read <a href="is-it-too-late-to-learn-piano-at-40-50-60.html">is it too late to learn piano at 40, 50 or 60?</a> for the honest version of that answer.</p>

<p><strong>Wanting to go too fast.</strong> Adults who finally have time sometimes try to make up for lost years in a month, practice for two hours, and end up with sore forearms. Thirty minutes a day, every day, will take you further. If you are in your forties, the page for <a href="../piano-lessons-for-adults-in-their-40s.html">adults in their 40s</a> lists the music people your age most often want to play.</p>

<h2>Play for them when they come home</h2>

<p>There is a very particular pleasure waiting at the end of that first year. The family comes home for a holiday, and after dinner you sit down and play. Not perfectly, not for long, but really. Read <a href="playing-for-a-small-audience-at-home.html">playing for a small audience at home</a> when the time comes.</p>

<h2>This is for you</h2>

<p>For years you were the one who made room for everyone else's music lessons, sports and plans. This one is yours. See the page for <a href="../piano-lessons-for-adults-in-their-50s.html">adults in their 50s</a> for the music people your age most want to play, and when you are ready, <a href="../start.html">start here</a>.</p>
"""),

spec("online-piano-lessons-vs-in-person", "2027-02-07",
 "Online Piano Lessons vs In-Person: An Honest Comparison",
 "Are online piano lessons as good as in-person lessons for adults? What each format does well, where online falls short, and how to make online learning work.",
 "The question is not online or in person. It is who is teaching you, and whether anyone is actually listening to your playing.",
 "lead-seated-black.jpg", "Dr. Maria Pisarenko seated at the piano",
 "Free, online, in order:",
"""
<p>Adults weighing piano lessons usually ask me some version of this: <em>Is learning online really as good as having someone in the room?</em> It is a fair question, and the honest answer is that each has things it does better. What matters more than the format is who is teaching you, and whether anyone is actually hearing your playing.</p>

<h2>What in-person lessons do well</h2>

<p><strong>The hand can be touched.</strong> A teacher in the room can rest a hand on your wrist and let you feel what "lower" or "looser" means. Some corrections are faster by touch than by any explanation.</p>

<p><strong>The sound is heard directly.</strong> In the same room, every shade of tone reaches the teacher's ear as it really is, without a microphone in between.</p>

<p><strong>You can play together.</strong> Duets, accompanying, the teacher playing a phrase on a second instrument and you answering it. Over the internet, the small delay in the connection makes this nearly impossible.</p>

<h2>What online learning does well</h2>

<p><strong>Access to the level of teaching you want.</strong> This is the biggest advantage, and the one adults underestimate. In person, your choice is limited to whoever lives within driving distance. Online, you can learn from a performer trained in a great tradition, wherever you live. For a skill that you will build on for the rest of your life, the quality of the first teaching matters enormously. <a href="who-taught-the-person-teaching-you.html">Who taught the person teaching you</a> explains why.</p>

<p><strong>Your own instrument.</strong> You learn on the piano you practice on, with your own bench and your own light. What you are taught works at home, because it was taught at home.</p>

<p><strong>Lessons you can replay.</strong> A demonstration in a room happens once. A recorded lesson can be watched ten times, slowed down, and returned to a month later when the same problem comes back.</p>

<p><strong>Your pace, your hours.</strong> Adults with jobs and families rarely have the same free hour every week. Online learning fits around a real life.</p>

<h2>Where online falls short, and how to fix it</h2>

<p><strong>The camera sees only what you show it.</strong> A laptop on the music stand shows your face and the top of the keys. It hides the wrist, the thumb and the shoulders, which are exactly what a teacher most needs to see. Place the camera at the side of the keyboard, level with the keys, so that one hand, wrist and forearm are visible in profile. A second view from slightly above and behind is ideal.</p>

<p><strong>The microphone flattens the sound.</strong> Built-in laptop microphones compress the piano's sound, especially soft playing. A phone placed a short distance from the instrument, not on it, often records better than a laptop. For a digital piano, a direct audio cable is better still.</p>

<p><strong>Live video is not always better than a recording.</strong> A live video call has delay and sound dropouts. A recording, made when you are ready and sent for detailed comments, often gives a teacher more to work with: they can listen twice, at full quality, and think before they answer.</p>

<h2>The three kinds of online learning</h2>

<p><strong>Pre-recorded courses.</strong> Lessons in order, at your own pace. Excellent for structure and for seeing every movement up close. Their weakness is that nobody hears <em>you</em>.</p>

<p><strong>Live video lessons.</strong> Closest to the traditional lesson, with the limits of camera and connection described above.</p>

<p><strong>Feedback on recordings.</strong> You send a short recording; a trained musician listens and tells you, in detail, what to change. Combined with a structured course, this closes the gap that self-teaching leaves open. It is exactly why I answer recordings: <a href="../submit.html">send me a minute of your playing</a>, and I will tell you the one thing to change first.</p>

<h2>A setup checklist for learning online</h2>

<p><strong>A steady stand for your phone or camera.</strong> A small tripod or a stack of books, so the view does not move.</p>

<p><strong>Light from the front or side, not behind you.</strong> A window behind you turns your hands into a silhouette.</p>

<p><strong>Headphones for watching lessons.</strong> You will hear demonstrations more clearly and pick up details of sound you would miss through laptop speakers.</p>

<p><strong>The lesson screen near the music stand.</strong> If you must turn around to see the video, you will stop watching it while you play.</p>

<p><strong>A notebook.</strong> One line after each lesson: what to practice, and what to listen for. Online learning gives you freedom; the notebook gives you continuity.</p>

<h2>Questions to ask about any lessons, online or not</h2>

<p><strong>Who is teaching, and how were they trained?</strong> Look for real musical training and real teaching experience, not just enthusiasm.</p>

<p><strong>Can you hear them play?</strong> A teacher of piano should be able to show you, on video, what the music is supposed to sound like.</p>

<p><strong>Will anyone ever look at your hands and listen to your playing?</strong> If the answer is no, you are buying a library, not lessons. A library is useful, but it is not the same thing.</p>

<p><strong>Is there an order?</strong> A collection of unrelated videos is not a course. Skills should build on each other, one at a time.</p>

<p>For a longer checklist, read <a href="how-to-choose-a-piano-teacher.html">how to choose a piano teacher</a>, and for what you genuinely cannot fix on your own, <a href="learning-piano-without-a-teacher.html">learning piano without a teacher</a>.</p>

<h2>The format matters less than the ear</h2>

<p>In the end, an adult learns the piano well when the teaching is in the right order, the explanations make sense, and a trained ear hears their playing often enough to catch problems early. All three are possible online. The course on this site gives you the first two from the first lesson; <a href="../start.html">start here</a>. And <a href="what-a-piano-teacher-hears-that-you-do-not.html">what a piano teacher hears that you do not</a> explains the third.</p>
"""),

spec("piano-duets-for-adult-beginners", "2027-02-08",
 "Piano Duets for Adult Beginners: Music Is Better Shared",
 "Piano duets for adult beginners: why playing with a partner or friend speeds learning, what music to start with, and how to keep going together.",
 "Most adults learn the piano alone. Playing with one other person changes how you listen, how you count, and how much you enjoy it.",
 "lead-burgundy-sofa.jpg", "Dr. Maria Pisarenko",
 "Lessons you can work through together:",
"""
<p>Most adults learn the piano alone: in the evening, in an empty room, often with headphones. That solitude is part of the pleasure. But the piano was never meant to be only a solitary instrument, and some of the happiest moments adults describe to me involve one other person on the bench beside them.</p>

<h2>Why playing with someone helps you learn</h2>

<p><strong>You cannot stop.</strong> Alone, an adult stops at every wrong note and starts again. With a partner, the music keeps going and you must find your way back in. That one habit, keeping going, is among the most valuable a pianist can build. <a href="why-you-stop-every-time-you-make-a-mistake.html">Why you stop every time you make a mistake</a> explains why it matters so much.</p>

<p><strong>You learn to count for real.</strong> A metronome is patient. A partner is not. When two people play together, a shared pulse is not optional, and counting stops being an exercise and becomes the thing that holds the music together.</p>

<p><strong>You start to listen.</strong> Playing your part while hearing someone else's teaches balance: when to be the melody, when to step back. That is the beginning of real musicianship.</p>

<p><strong>You come back.</strong> It is easy to skip practice when nobody is waiting. It is much harder when someone is expecting you on Thursday evening.</p>

<h2>Who to play with</h2>

<p>A spouse or partner who also plays, or is learning. A friend from work who had lessons as a child. A grown child who still remembers some of their own lessons. A neighbor. For many adults in retirement, a weekly duet is also a weekly appointment with another person, and that companionship is worth as much as the music.</p>

<p>The two players do not need to be at the same level. In fact, some of the best duet music is written for exactly that situation.</p>

<h2>Music to start with</h2>

<p><strong>Duets with an easy part.</strong> Many duet collections are written so that one part is very simple, often in a single five-note position, while the other part fills in the harmony. Anton Diabelli's <em>Melodious Exercises</em>, Op. 149, were written exactly this way, and they are real music, not drills.</p>

<p><strong>Accompaniments in your method book.</strong> Many adult courses print an optional second part above or below the beginner's line. If yours does, ask your partner to play it; your simple melody suddenly sounds like a complete piece.</p>

<p><strong>Your own arrangement.</strong> One person plays a melody you both love; the other plays the bass note of each chord. That is a duet too, and a good way to start.</p>

<h2>How to play together without falling apart</h2>

<p><strong>Agree on the tempo before you start, and choose a slow one.</strong> Count one full bar out loud together before the first note.</p>

<p><strong>Decide who leads.</strong> One person breathes or nods at the start and at any pause. Usually it is the player with the melody.</p>

<p><strong>Decide who pedals.</strong> In music for four hands on one piano, the lower part, the <em>secondo</em>, usually pedals, because that player's foot is nearer the pedals and their part needs it most. Agree in advance, and only one of you pedals. <a href="when-should-you-start-using-the-piano-pedal.html">When to start using the pedal</a> explains the basics.</p>

<p><strong>Never stop for a mistake.</strong> If you get lost, keep counting, find the next downbeat and come back in. Afterwards, practice the spot separately.</p>

<p><strong>Practice your part alone first.</strong> Duet time is for playing together, not for learning notes.</p>

<p><strong>Use a metronome together at first.</strong> It gives you both something neutral to follow. <a href="what-the-metronome-is-actually-for.html">What the metronome is actually for</a> shows how.</p>

<h2>Playing with a partner at a different level</h2>

<p>Many duets happen between people at different stages: a spouse who played for years and one who is just starting, or two friends a year apart. It works beautifully with a few agreements.</p>

<p><strong>The stronger player supports.</strong> Their job is not to show off, but to make the other part sound good: a steady pulse, a soft accompaniment, patience at the hard spots.</p>

<p><strong>Take turns choosing the music.</strong> Both of you should be playing something you want to play.</p>

<p><strong>Do not teach each other during the duet.</strong> Corrections between partners, especially married ones, are where duets go wrong. Play it through, then each of you practices your own part. If something keeps going wrong, agree to slow down rather than to explain.</p>

<p><strong>Celebrate the first complete run.</strong> The first time you both reach the end together without stopping is a real achievement. Record it.</p>

<h2>Sitting together</h2>

<p>On one piano, sit far enough apart that your elbows do not collide, and check that both of you have the right height. A long bench works; two chairs of the right height work too. On two instruments, place them where you can see each other's hands.</p>

<h2>If you have no partner yet</h2>

<p>Play along with a recording of the other part. It teaches many of the same skills. <a href="practicing-with-a-recording.html">Practicing with a recording</a> explains when it helps and when it hurts. Over the internet, live duets are nearly impossible, because of the small delay in every connection, so recordings are the practical substitute.</p>

<h2>Music, shared</h2>

<p>Duets are where many adults first feel like musicians instead of students: two people, one sound. When you are ready to go further, read <a href="playing-for-a-small-audience-at-home.html">playing for a small audience at home</a> and <a href="chamber-music-playing-with-strings.html">chamber music with violin and cello</a>. If you are in retirement, see <a href="learning-piano-in-retirement.html">a plan for your 60s</a>, and to begin at the first lesson, <a href="../start.html">start here</a>.</p>
"""),
]

if __name__ == "__main__":
    out = pathlib.Path(__file__).resolve().parent / "_specs_batch_10_motives.json"
    out.write_text(json.dumps(SPECS, indent=1, ensure_ascii=False), encoding="utf-8")
    print("wrote", out.name, len(SPECS))
