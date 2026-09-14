# -*- coding: utf-8 -*-
import json, pathlib

SPECS = [
{
 "slug": "why-adult-beginners-quit-piano",
 "date": "2026-09-16",
 "title": "Why Adult Beginners Quit Piano in the First Three Months",
 "description": "Adults almost never stop learning piano because they lack talent. They stop for four ordinary, predictable reasons — and a concert pianist explains how to design every one of them out before it happens.",
 "sub": "Almost nobody stops because they lack talent. They stop for four ordinary reasons, and every one of them can be designed out in advance.",
 "image": "lead-burgundy-sofa.jpg",
 "image_alt": "Dr. Maria Pisarenko, concert pianist and university professor",
 "cta_text": "The free course this is built on &mdash; forty-one lessons, from your first note:",
 "cta_href": "https://youtu.be/AzU01rYWHK8",
 "cta_link": "Start at Lesson 1 &rarr;",
 "body": """
<p>In thirty years of teaching I have watched a great many adults begin the piano, and I have watched a smaller number of them still be playing a year later. What separates the two groups is not talent, and it is not age. I can say that plainly, because I have taught both at university level and at kitchen-table level, and the people who last are not the ones who arrived gifted.</p>

<p>They are the ones who never hit one of four walls &mdash; or who saw the wall coming and walked round it.</p>

<p>Here are the four, in the order they usually arrive.</p>

<h2>Week two: the hands hurt, and you think it is your age</h2>

<p>This is the earliest one and the saddest, because it is entirely preventable. An adult sits down, plays for twenty minutes, and the forearm aches. The conclusion is immediate: <em>my hands are too old, too stiff, not made for this.</em></p>

<p>Almost always it is none of those things. It is a bench set too low, so the wrist sits below the level of the keys and the small muscles of the hand end up carrying work that belongs to the arm. A stiff hand at fifty is usually a hand doing the job of an arm.</p>

<p><strong>What to do instead:</strong> sit high enough that your forearm runs level with the tops of the keys, or a shade above &mdash; never below. Let the key go down with the weight of the arm behind a firm fingertip, and let go immediately after. If your dining chair is too low, sit on a folded towel. That is not a compromise; that is what an adjustable bench is for.</p>

<h2>Week four: you can only play in one spot, and it feels like a trap</h2>

<p>Most beginner books park the hand in a single five-finger position for many pages. That is a printing decision, not a musical one, and it has a cost: the student begins reading finger numbers rather than notes, and the moment the hand has to travel, everything falls apart. It feels like failure. It is not. It is a habit that was installed on purpose and simply needs undoing.</p>

<p><strong>What to do instead:</strong> take any three-note tune you already have and play it starting from three different places on the keyboard. Same shape, different home. Ten minutes of this in your first month saves you a year of the feeling that the piano is somehow bolted shut.</p>

<h2>Week six: nobody has heard you play</h2>

<p>This is the one I care about most, and it is the specifically American difficulty. A child learning in Europe or in Russia has an adult in the room every single week whose entire job is to hear them. An American adult typically has a book, a screen, and their own ears &mdash; and your own ears are the least reliable instrument in the house, because you hear what you intended, not what you played.</p>

<p>So errors set. Not big dramatic errors: a collapsing third finger, a wrist that rises at the end of every phrase, a habit of rushing whenever the notes get easier. Small things that take a minute to correct in week six and a season to correct in year two.</p>

<p><strong>What to do instead:</strong> film yourself. Once a week, one minute, phone on the music stand. You will see in ten seconds what you could not feel in a month. And if you want another musician's ears on it, send it to me &mdash; <a href="../submit.html">I read and answer recordings, and it costs nothing</a>.</p>

<h2>Week ten: life happens, and there was no plan for it</h2>

<p>A week goes by. Then a fortnight. The piano becomes slightly embarrassing furniture, and going back to it means admitting the gap. This is how most adults actually stop &mdash; not by deciding to, but by never quite restarting.</p>

<p>The people who last have one thing in common here. They practise small and they practise fixed. Fifteen honest minutes at the same hour every day beats two hours on a Sunday, and it beats it by a very large margin, because playing the piano is a physical skill and physical skills consolidate overnight. Six short sessions give you six nights of consolidation. One long session gives you one.</p>

<p><strong>What to do instead:</strong> decide now what your minimum is on a bad day. Mine for my students is five minutes. Not a good practice &mdash; a short one, deliberately. Five minutes keeps the thread. The thread is the whole thing.</p>

<h2>What the four have in common</h2>

<p>Not one of them is about music. Every one is about how the learning was set up: how you sit, how the hand moves, whether anyone hears you, and whether the habit was built to survive an ordinary bad week.</p>

<p>That is not an accident. The musical part of beginning the piano is genuinely not very hard &mdash; adults learn to read music faster than children do, because they already understand counting, patterns and symbols. What adults do not have is somebody standing next to the instrument saying <em>lift your wrist, listen to that note, again.</em></p>

<p>Which is exactly what my free course was built to be, and why I answer recordings myself. If you are inside your first three months right now, do not wait until something hurts or something stalls. Fix the bench, move the hand, film a minute, and pick your five-minute floor. Those four decisions are most of the difference between the two groups.</p>
"""
},
]

pathlib.Path("_specs_batch_01.json").write_text(json.dumps(SPECS, ensure_ascii=False, indent=1), encoding="utf-8")
print("specs written:", len(SPECS))
