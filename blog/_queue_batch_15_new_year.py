# -*- coding: utf-8 -*-
"""Batch 15 (2026-11-20): one New Year buyer article, queued for 2026-12-26.
Build:  python3 blog/_queue_batch_15_new_year.py   then   python3 blog/_make_post.py blog/_specs_batch_15_new_year.json blog/_queue
Rules: first person, adults who learn alone, no prices/ratings/Amazon images, no claim of hands-on testing, no Las Vegas signal,
links only to LIVE articles (no forward links to later queued articles)."""
import json, pathlib

BODY = """
<p>If learning piano is on your list for 2027, here is the good news: you need much less than the internet suggests. A keyboard you can sit at, a bench at the right height, a pair of headphones, and about fifteen minutes a day will take you further in a month than a drawer full of gear. I put the plan and my picks on one page, <a href="../shop/start-piano-in-2027.html">Start Piano in 2027</a>; this article explains the thinking behind it.</p>

<h2>What do you actually need to learn piano in 2027?</h2>

<p>Four things, in this order.</p>

<p><strong>An instrument with a real touch.</strong> If you can, choose a digital piano with 88 weighted keys, because that is the feel you will keep learning on. If space or budget is tight, a 61-key keyboard with touch-sensitive keys will carry a first year. I explain the difference in <a href="weighted-vs-semi-weighted-keys.html">weighted vs semi-weighted keys</a> and <a href="how-many-keys-do-i-need-piano.html">how many keys you need</a>, and my <a href="../shop/digital-pianos.html">digital piano picks</a> and <a href="../shop/keyboards.html">keyboard picks</a> are grouped from budget to premium.</p>

<p><strong>A way to sit correctly.</strong> A bench or stool you can adjust, so your forearms sit level with the keys. A dining chair is nearly always wrong. See <a href="piano-bench-height-posture.html">how to set your bench height</a>.</p>

<p><strong>Headphones and a sustain pedal.</strong> Headphones let you practice at any hour, which is what protects a new habit, and a piano-style pedal teaches your foot the right movement from the start. Both are small purchases next to the piano.</p>

<p><strong>Someone to hear you.</strong> This is the one thing gear cannot give you. My <a href="../free-course.html">free 41-lesson course</a> is published in full, and when you have a recording, <a href="../submit.html">send it to me</a> and I will tell you what I hear, at no charge.</p>

<h2>What do you not need?</h2>

<p>You do not need an acoustic piano to begin; <a href="digital-piano-vs-acoustic-beginner.html">a digital piano is a sound first choice</a>. You do not need a studio, a recording setup, or a second keyboard. You do not need talent, which is a word people use for what practice looks like from the outside. And you do not need to have played as a child. If you are wondering whether you are too late, read <a href="is-it-too-late-to-learn-piano-at-40-50-60.html">whether it is too late at 40, 50 or 60</a>. It is not.</p>

<h2>What should your first month look like?</h2>

<p>Keep it small. In week one, set up the keyboard where you will see it every day and play for ten minutes. In week two, find middle C and place both hands around it. In week three, play your first short piece and count it out loud. In week four, record yourself and send me the recording. Fifteen to twenty minutes a day is enough; <a href="how-long-to-practice-piano-each-day.html">here is how I think about practice time</a>. The full four-week plan is on the <a href="../shop/start-piano-in-2027.html#first-month">2027 start page</a>.</p>

<h2>Keyboard or digital piano?</h2>

<p>Choose the digital piano if you can, and the keyboard if you must. The weighted keys of a digital piano train the strength and control your fingers will need later, and a keyboard with unweighted keys can feel fine for a month and then hold you back. A good keyboard is still far better than waiting. If you are unsure, start with the one you can afford today and move up when you outgrow it.</p>

<h2>When do lessons help?</h2>

<p>Start with the free course; for many adults it is enough for a first stretch. Add a teacher when you want someone to hear your hands, correct a habit before it sets, or decide what to play next. I teach adults online, wherever they live, and you can <a href="../lessons.html">read how my private lessons work</a>. If you are buying for someone else, a <a href="../gift-certificate.html">gift certificate for online piano lessons</a> needs no assembly.</p>

<h2>My advice for January</h2>

<p>Choose the instrument this week, not in March. Put it where you will pass it every day. Play for ten minutes tomorrow, and for ten minutes the day after. A year from now you will not remember how good the keyboard was; you will remember that you started.</p>
"""

FAQ = [
 ["Is it too late to learn piano in 2027?", "No. Adults of every age begin piano, and starting in your 40s, 50s or 60s works well because you can practice with focus and understand why each technique matters."],
 ["What do I need to start learning piano as an adult?", "A keyboard with weighted keys if you can, or a 61-key touch-sensitive keyboard for a first year; a bench at the right height; headphones; a sustain pedal; and fifteen to twenty minutes a day."],
 ["Is learning piano a good New Year's resolution?", "Yes, if you make it small and specific: fifteen minutes a day, one lesson at a time. A resolution you can check every Sunday is a resolution you can keep."],
]

S = [{"slug": "learn-piano-in-2027-what-you-need-to-start", "date": "2026-12-26",
      "title": "Learn Piano in 2027: What You Need to Start (and What You Don't)",
      "seo_title": "Learn Piano in 2027: What You Need (and What You Don't)",
      "description": "Learn piano in 2027: what an adult beginner needs to start, what you can skip, a four-week first month and when lessons help, from a concert pianist.",
      "sub": "A keyboard, a bench, headphones and fifteen minutes a day. Here is what you need to start piano in the new year, and what you can leave in the shop.",
      "image": "lead-at-the-piano.jpg", "image_alt": "Dr. Maria Pisarenko at the piano",
      "cta_text": "Forty-one lessons in order, free, at your own pace:", "cta_href": "https://youtu.be/AzU01rYWHK8", "cta_link": "Start at Lesson 1 &rarr;",
      "body": BODY.strip(), "faq": FAQ}]

if __name__ == "__main__":
    p = pathlib.Path(__file__).resolve().parent / "_specs_batch_15_new_year.json"
    p.write_text(json.dumps(S, indent=1, ensure_ascii=False), encoding="utf-8")
    print("wrote", p.name, len(S), "desc len", len(S[0]["description"]), "seo", len(S[0]["seo_title"]))
