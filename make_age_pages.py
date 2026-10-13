# -*- coding: utf-8 -*-
"""Builds the by-age pages for Online Piano University and the site-wide contact bands.

Run from opu-website/:  python3 make_age_pages.py
Idempotent: pages are overwritten, bands are added once (marker data-opu="contact-top|contact-bottom"),
the footer link "Piano by Age" is added once.

Song titles are titles only (no lyrics, no notation). Nothing here is a survey claim:
the song lists are the music that defined each generation's teens and twenties.
"""
import pathlib, re, json, html

HERE = pathlib.Path(__file__).resolve().parent
SITE = "https://onlinepianouniversity.com"
EMAIL = "maria@onlinepianouniversity.com"

# ---------------------------------------------------------------- content
AGES = [
 dict(slug="piano-lessons-for-adults-in-their-20s", decade="20s", label="Your 20s",
  title="Learn Piano in Your 20s | Online Piano University",
  desc="Teaching yourself piano in your 20s? Skip the bad habits apps and tutorials teach. Free lessons from Dr. Maria Pisarenko, DMA, Online Piano University.",
  h1="Learn Piano in Your 20s, Without Teaching Yourself Bad Habits",
  sub="You can learn almost anything from a screen. Piano is the one skill where the screen quietly teaches your hands to do the wrong thing. Here is how to avoid that, for free.",
  intro=["You are probably learning from videos, an app, or both. That works for the first month. Then the same thing happens to almost everyone: you can follow the colored bars, you cannot read a page of music, and the pieces you actually want stay out of reach.",
         "I am Dr. Maria Pisarenko, a concert pianist and university professor, and Online Piano University is the free course I built for adults who teach themselves. It starts with the sound and the hand, so your first year is not something you have to undo later."],
  songs_title="Do you want to play these?",
  songs_sub="The music of your teens and early twenties, the pieces people in your decade most often hum at a keyboard.",
  songs=["Perfect (Ed Sheeran)","drivers license (Olivia Rodrigo)","when the party's over (Billie Eilish)","Ocean Eyes (Billie Eilish)","Love Story (Taylor Swift)","Someone You Loved (Lewis Capaldi)","Let Her Go (Passenger)","River Flows in You (Yiruma)","Cornfield Chase (Hans Zimmer, Interstellar)","One Summer's Day (Joe Hisaishi, Spirited Away)","Comptine d'un autre été (Yann Tiersen)","Hedwig's Theme (John Williams)","Merry-Go-Round of Life (Joe Hisaishi, Howl's Moving Castle)","Always With Me (Youmi Kimura, Spirited Away)","Zelda's Lullaby (Koji Kondo)","Megalovania (Toby Fox, Undertale)","Clair de Lune (Debussy)","Experience (Ludovico Einaudi)"],
  pains_title="What is actually in your way at 20-something",
  pains=[("Falling-bar videos teach you to copy, not to read","Tutorials where colored bars fall onto a keyboard get you through one song. They do not teach you the page, so every new piece starts from zero. Reading is a skill that takes weeks, not years, if it is taught in the right order."),
         ("Your wrists and shoulders learn the wrong shape","Hunching over a laptop keyboard or a cheap stand-alone keyboard sets the hand up to squeeze instead of to carry weight. It feels fine for a month and then your forearm tells you otherwise."),
         ("You want the pretty pieces, fast","That is a good instinct, and we use it. The free course gets you playing a real melody on day one, and it builds the specific skills (finger independence, pedal, a singing line) that Clair de Lune and River Flows in You need."),
         ("No room, no budget, no noise allowed","A weighted 88-key digital piano with headphones is enough. I list what I recommend, and why, on the Books and Gear page. You do not need an acoustic piano."),
         ("Motivation that comes and goes","Short daily practice beats weekend marathons. The course is built in twenty-minute lessons so that missing a day never costs you the thread.")],
  plan=[("Week 1","Lesson 1 of the free course. Learn to sit, to find any note, and to play your first melody by ear."),
        ("Weeks 2 to 4","Lessons 2 to 8: the staff, note values, both hands. Practice twenty minutes a day, six days a week."),
        ("Month 2","Record yourself and send the recording for written feedback. Choose one piece from the list above as your goal.")],
  faq=[("Can I learn piano in my 20s with just YouTube and an app?","You can start that way, and many people do. The risk is that nothing corrects your hand position or your reading as you go. The free course here is built so that the lessons come in a fixed order, and you can send a recording of your playing for feedback."),
       ("What is the fastest way to learn pop songs on piano?","Learn chords and a steady left hand first, then add the melody. The course covers chords, so the pop songs on this page stop being separate projects and become variations on one skill."),
       ("Do I need an expensive keyboard?","No. A digital piano with 88 weighted keys is the right target, and a good one costs far less than an acoustic piano. The gear page lists the ones I recommend.")]),

 dict(slug="piano-lessons-for-adults-in-their-30s", decade="30s", label="Your 30s",
  title="Learn Piano in Your 30s | Online Piano University",
  desc="Learning piano in your 30s with a job, family and twenty free minutes? A clear free course by Dr. Maria Pisarenko, DMA, Online Piano University, plus feedback.",
  h1="Learn Piano in Your 30s With a Job, a Family and Twenty Minutes",
  sub="You do not need an hour a day. You need twenty focused minutes and someone who tells you what to do with them.",
  intro=["Most people in their thirties have tried piano already: an app, a keyboard bought during a lockdown, a few lessons as a kid. The keyboard is probably still in a corner. The problem was never talent. It was a plan.",
         "Online Piano University is a free, ordered course for adults who learn on their own. Each lesson fits in a lunch break, and you can send me a recording and get a written answer, so you are not guessing whether you are improving."],
  songs_title="Do you want to play these?",
  songs_sub="The songs and themes that were everywhere when you were growing up.",
  songs=["Someone Like You (Adele)","All of Me (John Legend)","Viva la Vida (Coldplay)","Clocks (Coldplay)","A Thousand Miles (Vanessa Carlton)","How to Save a Life (The Fray)","Let It Go (Idina Menzel)","Hallelujah (Leonard Cohen)","Love Song (Sara Bareilles)","Comptine d'un autre été (Yann Tiersen)","Hedwig's Theme (John Williams)","He's a Pirate (Pirates of the Caribbean)","Bella's Lullaby (Carter Burwell)","Nuvole Bianche (Ludovico Einaudi)","Merry-Go-Round of Life (Joe Hisaishi, Howl's Moving Castle)","Zelda's Lullaby (Koji Kondo)"],
  pains_title="What is actually in your way in your thirties",
  pains=[("Fifteen minutes is all you have","Fifteen to twenty focused minutes, six days a week, beats one long session. The trick is knowing exactly what to do in them: five minutes slowly on one thing, ten on the smallest broken spot, five playing something you already enjoy."),
         ("Apps keep you busy and do not make you better","An app can tell you that you hit the right note. It cannot tell you your hand is tight, your rhythm is rushed or your sound is thin. That is what feedback on a real recording is for."),
         ("You quit last time and you do not trust yourself","Almost every adult who quits does so in the first three months, usually because the pieces were too hard or the plan was unclear. We start with a melody on day one so you win early."),
         ("You are practicing in a shared home","Digital piano plus headphones solves the noise. The free course is built so that you can practice quietly and still develop real touch."),
         ("Guilt about spending time on yourself","Twenty minutes is small enough to protect. Put it at the same time every day and it stops being a decision.")],
  plan=[("Week 1","Lesson 1. Set up your keyboard height and play your first melody by ear."),
        ("Weeks 2 to 6","Follow the course in order, twenty minutes a day. Keep a one-line log of what you practiced."),
        ("Week 6","Send a recording for feedback and pick your first goal piece from the list above.")],
  faq=[("How long does it take to learn piano as an adult in your 30s?","With twenty minutes of focused practice a day, most adults are playing simple pieces with both hands within a few months. Pieces like Someone Like You or All of Me come when chords, rhythm and reading are each reasonably steady, which the course builds in order."),
       ("Is it better to take lessons or learn online?","Both work. A structured free course plus occasional written feedback covers most of what a beginner needs. If you want a live teacher on Zoom, I also teach private lessons."),
       ("Can I learn piano if I can't read music?","Yes. You start by ear and by shape, and reading comes in step by step once your hand knows what to do.")]),

 dict(slug="piano-lessons-for-adults-in-their-40s", decade="40s", label="Your 40s",
  title="Learn Piano in Your 40s | Online Piano University",
  desc="Starting piano or returning in your 40s? Dr. Maria Pisarenko, DMA, teaches adults who quit as kids or never began. Free course and feedback, Online Piano University.",
  h1="Learn Piano in Your 40s: Start Again, Properly",
  sub="If you stopped at twelve, or never started, this is the right moment. You understand music better than you did then, and you can practice without anyone standing over you.",
  intro=["A lot of adults in their forties come back to the piano with an old wound: a teacher who was impatient, a recital that went badly, a parent who decided when you were done. You can leave all of that behind.",
         "Online Piano University is built for adults who teach themselves. It is free, it is in order, and the person on the other side of your recordings is a teacher who understands exactly that fear."],
  songs_title="Do you want to play these?",
  songs_sub="The music of your high school and college years, plus the classical pieces everybody half-remembers.",
  songs=["Fallin' (Alicia Keys)","If I Ain't Got You (Alicia Keys)","Angel (Sarah McLachlan)","Mad World (Gary Jules)","My Immortal (Evanescence)","Because of You (Kelly Clarkson)","Bad Day (Daniel Powter)","Hallelujah (Leonard Cohen)","My Heart Will Go On (Celine Dion)","Clocks (Coldplay)","Canon in D (Pachelbel)","Für Elise (Beethoven)","Gymnopédie No. 1 (Satie)","Moonlight Sonata, first movement (Beethoven)"],
  pains_title="What is actually in your way in your forties",
  pains=[("The old teacher is still in the room","Many adults flinch at a wrong note because someone once flinched for them. The cure is a practice style where mistakes are information, and a teacher whose feedback is specific and calm."),
         ("Perfectionism","You want the piece to be good immediately, and you notice every flaw. The method here slows you down on purpose, so you build the piece in small parts that are right."),
         ("You understand the music faster than your hands can play it","That gap is normal for adults and it is not a sign something is wrong. It closes with the right exercises, not with more hours."),
         ("Your hands are tight after a day at a desk","Tension is the most common reason a hand aches at the keyboard. The lessons show where the weight comes from, and the blog covers it in detail. If anything hurts sharply, see a doctor; I am a pianist, not a physician."),
         ("No goal, no recital, no exam","Adult learners often drift because nothing is due. Pick one piece from the list as your goal, set a date, and record it.")],
  plan=[("Week 1","Lesson 1. Learn how to sit and where your weight goes, then play a melody by ear."),
        ("Weeks 2 to 8","Work through the course in order. Twenty minutes a day. Notice what changes when you play slowly."),
        ("Month 3","Send a recording for feedback. Pick the piece you stopped playing at twelve and finish it.")],
  faq=[("Is 45 too old to start piano?","No. Adults learn differently from children, and some things are harder and some are easier. What decides the outcome is whether you are taught the sound and the hand from the first lesson."),
       ("I played as a child. Will it come back?","Often faster than you expect. The notes are not gone, but habits are, so we rebuild posture and reading first, then your old pieces."),
       ("Can I learn Canon in D or Für Elise as an adult beginner?","Yes, after you can read the page and keep a steady rhythm in both hands. The free course builds those skills in order, and both pieces are common first goals.")]),

 dict(slug="piano-lessons-for-adults-in-their-50s", decade="50s", label="Your 50s",
  title="Learn Piano in Your 50s | Online Piano University",
  desc="Learning piano in your 50s, on your own? Free step-by-step lessons from Dr. Maria Pisarenko, DMA, plus written feedback on your playing. Online Piano University.",
  h1="Learn Piano in Your 50s: Play the Music You Grew Up With",
  sub="The children are older, the calendar has room, and the song you have wanted to play for years is still waiting. This is the course built for you.",
  intro=["Adults in their fifties are the people I built Online Piano University for: never played, or quit around twelve, and now learning alone. Nobody is standing next to you, so the lessons have to do the job a teacher would do at your shoulder.",
         "That means sound before notes, small steps in the right order, and feedback on a recording of your own playing. It is free on YouTube, and you move at your own pace."],
  songs_title="Do you want to play these?",
  songs_sub="The songs from your teens and twenties, and the classical pieces that never left you.",
  songs=["Piano Man (Billy Joel)","Vienna (Billy Joel)","Your Song (Elton John)","Rocket Man (Elton John)","Don't Stop Believin' (Journey)","Listen to Your Heart (Roxette)","Bohemian Rhapsody (Queen)","Against All Odds (Phil Collins)","Right Here Waiting (Richard Marx)","Let It Be (The Beatles)","Hey Jude (The Beatles)","Chariots of Fire (Vangelis)","The Entertainer (Scott Joplin)","Moonlight Sonata (Beethoven)","Clair de Lune (Debussy)"],
  pains_title="What is actually in your way in your fifties",
  pains=[("Teaching yourself with nobody to say what is wrong","You can play all the right notes and it still sounds wrong, and you cannot tell why. That is the exact gap the feedback service closes."),
         ("Stiff hands and reading small print","Larger-print music and a good bench and lamp help more than people expect. Warm up gently, and if you have joint pain, ask your doctor first; I am a pianist, not a physician."),
         ("A method book written for children","Many first books are slow, babyish or both. The course here follows an adult method book, lesson by lesson, with explanations that treat you as an adult."),
         ("The feeling that it is too late","It is not. Adults can learn to read, to play with both hands and to make a real sound at any age. The pace is different and the results are real."),
         ("Having no goal","Choose one piece from the list above. Everything you practice in the next three months can point at it.")],
  plan=[("Week 1","Lesson 1. Sit correctly, find any note and play the opening of a melody by ear."),
        ("Months 1 to 3","Follow the 41 lessons in order, twenty to thirty minutes a day. Use a notebook for what you practiced."),
        ("Month 3","Send a recording for written feedback and choose your first real piece from the list.")],
  faq=[("Is it too late to learn piano at 55?","No. The free course is designed for adults of any age, and the first lesson already has you playing a real melody. Progress takes patience, not talent."),
       ("What is the best way to learn piano by yourself at 50?","A structured course in a fixed order, a decent weighted keyboard, twenty minutes a day and a way to get feedback. Those four things matter more than any app."),
       ("Can I learn Piano Man or Let It Be as a beginner?","Yes. Both are built on chords and a steady left hand, which the course teaches. Many adults pick one of them as their first goal.")]),

 dict(slug="piano-lessons-for-adults-in-their-60s", decade="60s", label="Your 60s",
  title="Learn Piano in Your 60s | Online Piano University",
  desc="Learning piano in your 60s or in retirement? Gentle, ordered free lessons and personal feedback from Dr. Maria Pisarenko, DMA, at Online Piano University.",
  h1="Learn Piano in Your 60s: It Is Not Too Late, and Here Is the Plan",
  sub="Retirement gives you the one thing a pianist needs most: unhurried time. This course gives you the order in which to use it.",
  intro=["People begin in their sixties because there is finally time, or because a parent's piano is now in their living room, or because they have wanted to play for fifty years. All three are good reasons.",
         "The lessons are free, in order, and unhurried. You can pause, repeat and come back next week without losing anything, and when you are ready you can send a recording and hear from me in writing."],
  songs_title="Do you want to play these?",
  songs_sub="The songs that were the soundtrack of your youth, and the pieces you have always loved to listen to.",
  songs=["Let It Be (The Beatles)","Hey Jude (The Beatles)","Yesterday (The Beatles)","Imagine (John Lennon)","Rocket Man (Elton John)","Tiny Dancer (Elton John)","You've Got a Friend (Carole King)","Bridge Over Troubled Water (Simon & Garfunkel)","(They Long to Be) Close to You (Carpenters)","Desperado (Eagles)","Just the Way You Are (Billy Joel)","Moon River (Henry Mancini)","Clair de Lune (Debussy)","Für Elise (Beethoven)","Canon in D (Pachelbel)"],
  pains_title="What is actually in your way in your sixties",
  pains=[("Fingers that are slower than you want","Speed is the last thing to arrive and the least important. The first goals are an even sound and a relaxed hand, and both are achievable at any age. If a joint hurts, check with your doctor first."),
         ("Reading music with tired eyes","Choose editions with large print, put a lamp on the music and stand the book higher. Reading is learned in small steps, and the course introduces each symbol only when you need it."),
         ("Remembering what you learned yesterday","Short daily practice beats long weekly sessions. A one-line log of what you practiced keeps the thread."),
         ("Worry that it is too late","It is not. Adult beginners in their sixties and seventies play real music with real expression. The goal is not a concert career; it is playing the music you love."),
         ("A keyboard that is wrong for you","Weighted keys and a sturdy bench make a bigger difference than people expect. My gear page explains what to choose and what to avoid.")],
  plan=[("Week 1","Lesson 1, no pressure. Sit comfortably, find the notes and play your first melody by ear."),
        ("Months 1 to 3","One lesson at a time. Twenty minutes a day is enough. Rewatch freely."),
        ("Month 3","Send a recording for feedback. Choose a piece from the list that you have always wanted to play.")],
  faq=[("Is it too late to start piano at 65?","No. Many adults start in their sixties and play real pieces within months. The course moves at your pace and nothing in it is timed."),
       ("What is the easiest way to start learning piano in retirement?","Follow a structured course in order, use a weighted keyboard, practice a little every day and get feedback on a recording. That sequence works better than random videos."),
       ("Can I play Let It Be or Moon River as a beginner?","Yes, after the first stages of the course. Both rely on chords and a calm left hand, and both are very common first goals.")]),

 dict(slug="piano-lessons-for-adults-in-their-70s", decade="70s", label="Your 70s and beyond",
  title="Learn Piano in Your 70s and Beyond | Online Piano University",
  desc="Never too late to play. Free, unhurried piano lessons for adults in their 70s and older, with personal feedback from Dr. Maria Pisarenko, DMA. Online Piano University.",
  h1="Learn Piano in Your 70s and Beyond: Play the Songs You Have Always Loved",
  sub="At this age you know exactly which music matters to you. The piano can be the way to make it yours.",
  intro=["Adults past seventy bring things a younger beginner does not: they know exactly which music matters to them, they listen deeply, and they are not trying to impress anyone.",
         "Online Piano University is free and unhurried. There is no timetable, no test and no one to compete with. You can start with a single lesson today, repeat it as many times as you like and ask me a question whenever you need to."],
  songs_title="Do you want to play these?",
  songs_sub="The songs and melodies that many people in their seventies carry with them, on a piano they can play slowly and beautifully.",
  songs=["Yesterday (The Beatles)","Moon River (Henry Mancini)","Fly Me to the Moon (Bart Howard)","Summertime (George Gershwin)","Can't Help Falling in Love (Elvis Presley)","Unchained Melody (Alex North)","Edelweiss (Rodgers and Hammerstein)","Amazing Grace","The Sound of Silence (Simon & Garfunkel)","As Time Goes By (Herman Hupfeld)","Brahms' Lullaby","Ave Maria (Schubert)","Gymnopédie No. 1 (Satie)","Nocturne in E-flat, Op. 9 No. 2 (Chopin)","Clair de Lune (Debussy)"],
  pains_title="What is actually in your way past seventy",
  pains=[("Hands that tire or stiffen","Short, gentle sessions work best, with rests built in. Warm hands first. If you have arthritis or any pain, ask your doctor what is right for you; I am a pianist, not a physician."),
         ("Eyesight and the size of the music","Large-print editions, good light and a music stand at the right height make a real difference. We start with very little notation and add only what you need."),
         ("Memory and repetition","Play a little, then rest, then play again tomorrow. A short notebook entry after each session keeps your place."),
         ("Feeling out of place in a world of apps","You do not need an app. A keyboard, headphones and a browser are enough. The lessons are videos that you can pause as often as you like."),
         ("Being told it is too late","It is not. You can learn to play a piece you love, and play it for your family. That is a real musical achievement.")],
  plan=[("Week 1","Lesson 1. Sit comfortably, find middle C and play your first melody by ear. Stop when you are tired."),
        ("Months 1 to 3","One lesson a week is perfectly fine. Rewatch as often as you like."),
        ("Month 3","Choose one song from the list and send me a recording of your first attempt.")],
  faq=[("Can you learn piano at 75?","Yes. Adults of every age learn to play, and the course is designed to be paused, repeated and returned to. Your goal can be as simple as one favorite song."),
       ("Is playing piano good for older adults?","Many people find it enjoyable and calming. I am a pianist and a teacher, not a physician, so for any health question please ask your doctor."),
       ("What keyboard should an older beginner choose?","One with 88 weighted keys, a stable stand or bench and headphones if you want quiet. The gear page has my recommendations.")]),
]

BOOK_BLOCK = """<section style="background:var(--paper);padding:36px 0"><div class="wrap" style="max-width:820px">
<span class="eyebrow">Coming soon</span>
<h2>My method book and a practice app are on the way</h2>
<p>I am writing a piano method book for adults who teach themselves, built on the same order as these lessons: sound first, then the hand, then the page. A free note-reading practice app is also in development. Both are works in progress, and anyone on my email list hears first. <a href="#guide">Join the list</a> or <a href="books.html">see the books and gear I recommend now</a>.</p>
</div></section>"""

CONTACT_CSS = """
/* --- contact bands and by-age pages (added by make_age_pages.py) --- */
.contactband{background:#f4f1ea;border-bottom:1px solid var(--line);font-size:.9rem}
.contactband .wrap{display:flex;flex-wrap:wrap;gap:6px 22px;justify-content:center;align-items:center;padding:9px 22px}
.contactband a{color:var(--navy);font-weight:600;text-decoration:none;border-bottom:1px solid rgba(0,0,0,.25)}
.contactfull{background:#1a2540;color:#fff;padding:42px 0}
.contactfull h2{color:#fff;margin:0 0 6px}
.contactfull .cols2{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:26px;margin-top:18px}
.contactfull a{color:#f2d58f}
.contactfull .btn{color:#1a2540}
.contactfull .btn.ghost{color:#fff;border:1px solid #fff;background:transparent}
.contactfull form.opu-capture{display:flex;gap:8px;flex-wrap:wrap}
.contactfull form.opu-capture input{flex:1 1 200px;padding:11px 12px;border-radius:8px;border:0}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:16px 0 0;padding:0;list-style:none}
.chips li{background:#fff;border:1px solid var(--line);border-radius:999px;padding:7px 14px;font-size:.92rem}
.agegrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:16px;margin-top:20px}
.agegrid a.card{text-decoration:none;color:inherit}
.agegrid a.card:hover{border-color:var(--gold)}
.pain{margin:0 0 18px}.pain h3{margin:0 0 4px;font-size:1.08rem}.pain p{margin:0;color:#3d4557}
.plan{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin-top:14px}
"""

def esc(s): return html.escape(s, quote=True)

def read(name): return (HERE / name).read_text(encoding="utf-8")

def contact_top(prefix=""):
    return ('<div class="contactband" data-opu="contact-top"><div class="wrap">'
            '<span>Questions? <a href="mailto:%s">%s</a></span>'
            '<a href="%scontact.html">Send me a message</a>'
            '<a href="%ssubmit.html">Send your playing for feedback</a></div></div>' % (EMAIL, EMAIL, prefix, prefix))

def contact_full(prefix=""):
    return ('<section class="contactfull" data-opu="contact-bottom"><div class="wrap">'
            '<h2>Talk to Dr. Maria Pisarenko</h2>'
            '<p style="color:#d7dbe8;margin:0;max-width:62ch">Online Piano University is run by one teacher. I read every message and every recording myself.</p>'
            '<div class="cols2">'
            '<div><p><b>Write or send your playing</b></p>'
            '<p><a href="mailto:%s">%s</a></p>'
            '<p><a class="btn" href="%scontact.html">Send me a message</a></p>'
            '<p><a class="btn ghost" href="%ssubmit.html">Send a recording for feedback</a></p></div>'
            '<div><p><b>Get the free Starter Guide</b></p>'
            '<form class="opu-capture"><input type="email" name="email_address" placeholder="Your email" required aria-label="Your email">'
            '<button class="btn" type="submit">Send me the guide</button></form>'
            '<p class="form-ok">&#10003; Thank you &mdash; check your inbox!</p>'
            '<p style="color:#aeb5cb;font-size:.85rem">No spam &mdash; just piano. Unsubscribe anytime.</p></div>'
            '<div><p><b>Follow along</b></p>'
            '<p><a href="https://www.youtube.com/@ONLINEPIANOUNIVERSITY" target="_blank" rel="noopener">YouTube</a> &middot; '
            '<a href="https://www.instagram.com/online_piano_university/" target="_blank" rel="noopener">Instagram</a> &middot; '
            '<a href="https://www.facebook.com/OnlinePianoUniversity/" target="_blank" rel="noopener">Facebook</a> &middot; '
            '<a href="https://www.tiktok.com/@online.piano.university" target="_blank" rel="noopener">TikTok</a> &middot; '
            '<a href="https://www.pinterest.com/OnlinePianoUniversity/" target="_blank" rel="noopener">Pinterest</a></p>'
            '<p><a href="%sfree-course.html">Free 41-lesson course</a><br><a href="%spiano-lessons-by-age.html">Piano lessons by age</a></p></div>'
            '</div></div></section>') % (EMAIL, EMAIL, prefix, prefix, prefix, prefix)


def shell_parts():
    fc = read("free-course.html")
    head_start = fc.index("<!doctype html>")
    head_end = fc.index("<title>")
    head_pre = fc[head_start:head_end]                         # doctype..viewport+gtag
    hdr = fc[fc.index('<header class="site">'):fc.index("</header>") + len("</header>")]
    hdr = hdr.replace(' class="active"', "")
    hdr = hdr.replace('<a class="btn" href="#playlist">▶ Start the Free Course</a>', '<a class="btn" href="free-course.html">▶ Start the Free Course</a>')
    foot = fc[fc.index('<footer id="footer">'):]
    return head_pre, hdr, foot


def page_head(title, desc, canon, extra_ld, og_title=None):
    og_title = og_title or title
    return f'''<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta property="og:site_name" content="Online Piano University">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(og_title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{SITE}/{canon}">
<meta property="og:image" content="{SITE}/images/og-adult-piano-lessons-dr-maria-pisarenko.jpg">
<meta property="og:image:alt" content="Dr. Maria Pisarenko, DMA, concert pianist, at the piano. Online Piano University: piano lessons for adults.">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(og_title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{SITE}/images/og-adult-piano-lessons-dr-maria-pisarenko.jpg">
<link rel="canonical" href="{SITE}/{canon}">
<link rel="manifest" href="manifest.json">
<meta name="theme-color" content="#1e2a44">
<link rel="icon" href="images/icon-192.png" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/site.css">
{extra_ld}
</head>
<body>
'''

def ld(obj): return '<script type="application/ld+json">%s</script>' % json.dumps(obj, ensure_ascii=False)

def breadcrumb(items):
    return ld({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":i+1,"name":n,"item":SITE+"/"+u if u else SITE+"/"} for i,(n,u) in enumerate(items)]})

FAQ_CSS = '<style>.faq-q{border:1px solid rgba(0,0,0,.12);border-radius:8px;padding:0;margin:0 0 10px;background:#fff}.faq-q>summary{cursor:pointer;padding:14px 18px;font-weight:600;list-style:none}.faq-q>summary::-webkit-details-marker{display:none}.faq-q>summary::before{content:"+ ";color:#A8781C;font-weight:700}.faq-q[open]>summary::before{content:"\\2212 "}.faq-q>p{margin:0;padding:0 18px 16px;color:#3d4557;line-height:1.6}</style>'

def build_age(a, head_pre, hdr, foot):
    others = [x for x in AGES if x is not a]
    pains = "".join('<div class="pain"><h3>%s</h3><p>%s</p></div>' % (esc(t), esc(b)) for t, b in a["pains"])
    chips = "".join("<li>%s</li>" % esc(s) for s in a["songs"])
    plan = "".join('<div class="card"><h3>%s</h3><p class="muted">%s</p></div>' % (esc(t), esc(b)) for t, b in a["plan"])
    faq = "".join('<details class="faq-q"><summary>%s</summary><p>%s</p></details>' % (esc(q), esc(an)) for q, an in a["faq"])
    faq_ld = ld({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":an}} for q, an in a["faq"]]})
    page_ld = ld({"@context":"https://schema.org","@type":"WebPage","name":a["h1"],"url":f"{SITE}/{a['slug']}.html",
        "description":a["desc"],"isPartOf":{"@type":"WebSite","name":"Online Piano University","url":SITE+"/"},
        "author":{"@type":"Person","name":"Dr. Maria Pisarenko","honorificSuffix":"DMA"},
        "audience":{"@type":"PeopleAudience","audienceType":"Adult piano learners in their "+a["decade"]}})
    bc = breadcrumb([("Online Piano University",""),("Piano Lessons by Age","piano-lessons-by-age.html"),(a["label"],a["slug"]+".html")])
    other_links = " &middot; ".join('<a href="%s.html">%s</a>' % (o["slug"], esc(o["label"])) for o in others)
    body = f'''{hdr}
{contact_top()}
<section class="pagehero"><div class="wrap">
  <span class="eyebrow" style="color:var(--gold)">Piano lessons for adults &middot; {esc(a["label"])}</span>
  <h1>{esc(a["h1"])}</h1>
  <p class="sub">{esc(a["sub"])}</p>
  <div class="cta" style="margin-top:24px;display:flex;gap:14px;flex-wrap:wrap">
    <a class="btn" href="free-course.html">&#9654; Start the free course</a>
    <a class="btn ghost" href="submit.html">Send me your playing &rarr;</a>
  </div>
</div></section>
<div class="strip"><div class="wrap"><span>Free &amp; in order: <b>41 lessons</b></span><span>Taught by <b>Dr. Maria Pisarenko, DMA</b></span><span>Written feedback on your own playing</span></div></div>

<section><div class="wrap" style="max-width:820px">
  <p>{esc(a["intro"][0])}</p>
  <p>{esc(a["intro"][1])}</p>
</div></section>

<section style="background:var(--paper)"><div class="wrap" style="max-width:900px">
  <span class="eyebrow">Songs for your decade</span>
  <h2>{esc(a["songs_title"])}</h2>
  <p class="muted">{esc(a["songs_sub"])}</p>
  <ul class="chips">{chips}</ul>
  <p style="margin-top:18px">Tell me which one you want and I will point you to the lessons that lead to it. <a href="contact.html">Write to me</a> or <a href="free-course.html">start the course</a> and aim at it from day one. Titles are named for reference; the sheet music for each is published by its own rights holders.</p>
</div></section>

<section><div class="wrap" style="max-width:820px">
  <span class="eyebrow">Be honest about the obstacles</span>
  <h2>{esc(a["pains_title"])}</h2>
  {pains}
</div></section>

<section style="background:var(--paper)"><div class="wrap" style="max-width:900px">
  <span class="eyebrow">A realistic start</span>
  <h2>Your first three months</h2>
  <div class="plan">{plan}</div>
  <p style="margin-top:18px"><a class="btn" href="free-course.html">&#9654; Begin with Lesson 1</a></p>
</div></section>

<section><div class="wrap" style="max-width:820px">
  <span class="eyebrow">Your teacher</span>
  <h2>Who is teaching you</h2>
  <p>I am <a href="about.html">Dr. Maria Pisarenko, DMA</a>, a concert pianist and university professor. I trained in the Russian school at the Central Music School of the Moscow Conservatory and the Gnessin Academy, and I teach at the college level. My work with adult beginners is the reason this course exists. You can read what the press and students say on the <a href="press.html">press</a> and <a href="reviews.html">reviews</a> pages.</p>
</div></section>

{BOOK_BLOCK}

<section id="guide" style="padding-bottom:0"><div class="wrap">
  <div class="capture">
    <span class="eyebrow" style="color:var(--gold)">Free guide</span>
    <h2>Get the Adult Beginner's Piano Starter Guide</h2>
    <p style="color:#d7dbe8;max-width:52ch;margin:6px auto 0">The first steps, the right instrument and how to practice, in one free PDF from Online Piano University.</p>
    <form class="opu-capture"><input type="email" name="email_address" placeholder="Your email" required aria-label="Your email"><button class="btn" type="submit">Send me the guide</button></form>
    <p class="form-ok">&#10003; Thank you &mdash; check your inbox!</p>
    <p class="note">No spam &mdash; just piano. Unsubscribe anytime.</p>
  </div>
</div></section>

{FAQ_CSS}
<section id="faq-section" class="section"><div class="wrap" style="max-width:820px">
  <h2>Questions adults ask in their {esc(a["decade"])}</h2>
  <div style="margin-top:18px">{faq}</div>
  <p style="margin-top:22px">Other decades: {other_links} &middot; <a href="piano-lessons-by-age.html">All ages</a></p>
</div></section>

{contact_full()}
{faq_ld}
'''
    return head_pre + page_head(a["title"], a["desc"], a["slug"] + ".html", page_ld + "\n" + bc + "\n" + "") + body + foot


def build_hub(head_pre, hdr, foot):
    title = "Piano Lessons for Adults by Age | Online Piano University"
    desc = "Piano lessons for adults in their 20s, 30s, 40s, 50s, 60s and 70s: songs for your decade, real obstacles, a plan. Dr. Maria Pisarenko, DMA, Online Piano University."
    cards = "".join('<a class="card" href="%s.html"><h3>%s</h3><p class="muted">%s</p><span class="btn dark" style="margin-top:8px;display:inline-block">Read this page &rarr;</span></a>' % (
        a["slug"], esc(a["label"]), esc(a["sub"])) for a in AGES)
    faq = [("Is there a best age to start learning piano?","The best age is the one you are in. Children and adults learn differently, and adults bring focus, patience and a clear idea of the music they love."),
           ("Can adults really learn piano from free online lessons?","Yes, if the lessons are in order and teach the sound and the hand, not only which key to press. The free course here has 41 lessons, and you can send a recording for feedback."),
           ("Will the website tell me which songs I can learn?","Each age page lists music from that decade. Tell me the one you want and I will point you to the lessons that lead to it.")]
    faq_html = "".join('<details class="faq-q"><summary>%s</summary><p>%s</p></details>' % (esc(q), esc(an)) for q, an in faq)
    faq_ld = ld({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":an}} for q, an in faq]})
    bc = breadcrumb([("Online Piano University",""),("Piano Lessons by Age","piano-lessons-by-age.html")])
    page_ld = ld({"@context":"https://schema.org","@type":"CollectionPage","name":"Piano Lessons for Adults by Age","url":SITE+"/piano-lessons-by-age.html","description":desc,
                  "hasPart":[{"@type":"WebPage","name":a["h1"],"url":f"{SITE}/{a['slug']}.html"} for a in AGES]})
    body = f'''{hdr}
{contact_top()}
<section class="pagehero"><div class="wrap">
  <span class="eyebrow" style="color:var(--gold)">Piano lessons for adults &middot; every age</span>
  <h1>Piano Lessons for Adults, by Age</h1>
  <p class="sub">Your twenties and your seventies need different encouragement, different songs and a different plan. Choose your decade, and start the free course whenever you are ready.</p>
  <div class="cta" style="margin-top:24px"><a class="btn" href="free-course.html">&#9654; Start the free course</a></div>
</div></section>
<div class="strip"><div class="wrap"><span>Free &amp; in order: <b>41 lessons</b></span><span>Taught by <b>Dr. Maria Pisarenko, DMA</b></span><span>Written feedback on your own playing</span></div></div>
<section><div class="wrap" style="max-width:980px">
  <h2>Where are you in life?</h2>
  <div class="agegrid">{cards}</div>
</div></section>
<section style="background:var(--paper)"><div class="wrap" style="max-width:820px">
  <h2>What every adult learner has in common</h2>
  <p>Whatever your age, you are learning without a teacher beside you, you have limited time, and you want to play real music soon. Online Piano University is built around exactly that: a free, ordered course, twenty-minute lessons, and feedback on your own playing from a teacher who has spent a career with adult beginners.</p>
  <p>I am <a href="about.html">Dr. Maria Pisarenko, DMA</a>. If you are not sure where to start, <a href="contact.html">write to me</a>.</p>
</div></section>
{BOOK_BLOCK}
<section id="guide" style="padding-bottom:0"><div class="wrap"><div class="capture">
  <span class="eyebrow" style="color:var(--gold)">Free guide</span>
  <h2>Get the Adult Beginner's Piano Starter Guide</h2>
  <form class="opu-capture"><input type="email" name="email_address" placeholder="Your email" required aria-label="Your email"><button class="btn" type="submit">Send me the guide</button></form>
  <p class="form-ok">&#10003; Thank you &mdash; check your inbox!</p><p class="note">No spam &mdash; just piano. Unsubscribe anytime.</p>
</div></div></section>
{FAQ_CSS}
<section id="faq-section" class="section"><div class="wrap" style="max-width:820px"><h2>Questions about learning piano as an adult</h2><div style="margin-top:18px">{faq_html}</div></div></section>
{contact_full()}
{faq_ld}
'''
    return head_pre + page_head(title, desc, "piano-lessons-by-age.html", page_ld + "\n" + bc) + body + foot


def add_footer_link_and_bands():
    changed = 0
    for p in list(HERE.glob("*.html")) + list((HERE / "blog").glob("*.html")):
        n = p.name
        if n in {"404.html", "studio.html", "googleed832eccb886831b.html"}:
            continue
        in_blog = p.parent.name == "blog"
        pre = "../" if in_blog else ""
        t = p.read_text(encoding="utf-8")
        o = t
        if "</header>" in t and 'data-opu="contact-top"' not in t:
            t = t.replace("</header>", "</header>\n" + contact_top(pre), 1)
        if '<footer id="footer">' in t and 'data-opu="contact-bottom"' not in t and n != "contact.html":
            t = t.replace('<footer id="footer">', contact_full(pre) + '\n<footer id="footer">', 1)
        if "piano-lessons-by-age.html" not in t.split('<footer id="footer">')[-1]:
            t = re.sub(r'(<p><a href="(?:\.\./)?press\.html">Press</a></p>)',
                       lambda m: m.group(1) + '\n      <p><a href="%spiano-lessons-by-age.html">Piano by Age</a></p>' % pre, t, count=1)
        if t != o:
            p.write_text(t, encoding="utf-8"); changed += 1
    return changed


def main():
    css = HERE / "css" / "site.css"
    c = css.read_text(encoding="utf-8")
    if ".contactband" not in c:
        css.write_text(c.rstrip() + "\n" + CONTACT_CSS, encoding="utf-8")
    head_pre, hdr, foot = shell_parts()
    # the age pages must not carry the (already-injected) bands twice: build first, then run the band pass
    for a in AGES:
        (HERE / (a["slug"] + ".html")).write_text(build_age(a, head_pre, hdr, foot), encoding="utf-8")
    (HERE / "piano-lessons-by-age.html").write_text(build_hub(head_pre, hdr, foot), encoding="utf-8")
    print("pages written:", len(AGES) + 1)
    print("pages touched by band/footer pass:", add_footer_link_and_bands())

if __name__ == "__main__":
    main()
