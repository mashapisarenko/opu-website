# -*- coding: utf-8 -*-
# Written 2026-10-13: one article per decade, on the six free days of the queue,
# each pointing at its age page. Masha's rules: no gender split, real obstacles,
# her voice as the teacher, no invented numbers, US spelling.
import json, pathlib
L1 = "https://youtu.be/AzU01rYWHK8"
def spec(slug, date, title, desc, sub, image, alt, cta, body):
    return {"slug": slug, "date": date, "title": title, "description": desc, "sub": sub,
            "image": image, "image_alt": alt, "cta_text": cta, "cta_href": L1,
            "cta_link": "Start at Lesson 1 &rarr;", "body": body}

SPECS = [
spec("learning-piano-at-50", "2026-11-10",
 "Learning Piano at 50: What Changes, and What Does Not",
 "Starting piano at 50 is different from starting at 8, and in several ways it is easier. What actually changes for the hands, the eyes and the memory, and how to plan around it.",
 "Your hands need a little more warming up. Your understanding is far ahead of any child's. Here is how to use the second to help the first.",
 "lead-at-the-piano.jpg", "Dr. Maria Pisarenko at the piano",
 "Forty-one lessons in order, free, at your own pace:",
"""
<p>Many of the adults who write to me are in their fifties. The children are older, the calendar finally has a little room, and a song they have wanted to play for decades is still waiting. Almost every one of them asks the same question first: <em>is it too late?</em></p>

<p>It is not. But it is different from starting at eight, and pretending otherwise does not help anyone. So here is what genuinely changes, and what does not.</p>

<h2>What changes</h2>

<p><strong>The hands take longer to warm up.</strong> A child sits down and plays. An adult hand that has spent the day on a keyboard or a steering wheel needs five minutes of slow, easy playing before it is ready for anything difficult. That is not a weakness; it is simply the first five minutes of a good session.</p>

<p><strong>Small print is harder to read.</strong> Many method books are printed for children, small and crowded. Larger music, a good lamp and a bench at the right height do more for a fifty-year-old reader than any exercise.</p>

<p><strong>New movements need more repetitions to settle.</strong> You will understand a passage on the first day and play it comfortably on the tenth. Expect that gap, plan for it, and it stops being discouraging.</p>

<h2>What does not change</h2>

<p><strong>Your ear.</strong> You have been listening to music for fifty years. You know when a phrase is beautiful and when it is not, which is the hardest thing to teach a child.</p>

<p><strong>Your understanding.</strong> When I explain why a hand should rest its weight on the key instead of pushing, an adult understands in one sentence. That understanding shortens everything that follows.</p>

<p><strong>Your reason.</strong> Children practice because someone tells them to. You practice because you want to play <em>Clair de Lune</em>, or <em>Let It Be</em>, or <em>Time After Time</em>. A clear reason is the strongest teacher there is.</p>

<h2>A plan that fits a fifty-year-old life</h2>

<p>Twenty to thirty minutes a day, six days a week, is enough. Begin each session with something easy you already know, spend the middle on the one small spot that is not yet right, and end on something that sounds good. Keep a notebook of what you practiced.</p>

<p>Choose one piece now that you want to play by next year, and let everything else point at it. If you are not sure which, the page for <a href="../piano-lessons-for-adults-in-their-50s.html">adults in their 50s</a> lists the songs people your age most often want to play.</p>

<h2>The one thing you cannot do alone</h2>

<p>The hardest part of teaching yourself is that you cannot hear your own playing from the outside. You play the right notes and it still sounds wrong, and you cannot tell why. That is exactly why I read and answer recordings: send me a minute of your playing and I will tell you, in writing, the one thing to change first.</p>
"""),

spec("learning-piano-in-your-30s", "2026-11-12",
 "Learning Piano in Your 30s With Twenty Minutes a Day",
 "A job, a family and twenty free minutes is enough to learn the piano properly, if you know what to do with those minutes. A concert pianist's plan for adults in their thirties.",
 "Most people in their thirties have tried piano before. The problem was never talent. It was what to do with the twenty minutes you actually have.",
 "lead-seated-black.jpg", "Dr. Maria Pisarenko seated at the piano",
 "Each lesson fits a lunch break. Start with the first one:",
"""
<p>If you are in your thirties, there is a good chance a keyboard is already in a corner of your home. Bought during a lockdown, or for a child, or after watching someone play <em>Someone Like You</em> and thinking: I could do that. Then work and family filled every hour, and the keyboard became furniture.</p>

<p>The problem was not your talent and it was not your age. It was that nobody told you what to do with the little time you had.</p>

<h2>Twenty minutes is a real session</h2>

<p>Adults often treat a short session as a failed long one. It is not. The hand consolidates what it learned <em>between</em> sessions, so six short days do far more than one long Sunday. Twenty focused minutes, most days, is a complete practice routine.</p>

<h2>What to do with them</h2>

<p><strong>Five minutes: something you already play.</strong> Slowly, listening to the sound. This warms the hands and reminds you that you can play.</p>

<p><strong>Ten minutes: the smallest broken spot.</strong> Not the whole piece. The two bars that go wrong. Play them slowly, hands separately if needed, until they go right three times in a row. Then stop.</p>

<p><strong>Five minutes: something for joy.</strong> A melody by ear, a piece from your childhood, anything you enjoy. You should always leave the instrument wanting to come back.</p>

<h2>Practicing in a shared home</h2>

<p>Headphones on a digital piano solve most of it. A weighted 88-key instrument matters more than the brand. And there is a quiet benefit to playing where your family can hear you: children who see a parent practicing understand that learning is something adults do too.</p>

<h2>The guilt about taking time for yourself</h2>

<p>Many people in their thirties tell me they feel selfish spending twenty minutes on the piano. I would put it differently. Twenty minutes in which you are not answering anyone, not solving anyone's problem, is what lets you be patient with everyone else for the rest of the day.</p>

<p>If you want a list of what to aim for, the page for <a href="../piano-lessons-for-adults-in-their-30s.html">adults in their 30s</a> has the songs people your age most often want to play, from <em>A Thousand Miles</em> to <em>Merry-Go-Round of Life</em>.</p>
"""),

spec("learning-piano-in-retirement", "2026-11-14",
 "Learning Piano in Retirement: A Plan for Your 60s",
 "Retirement is one of the best times to learn piano. How to set up the instrument, the light and the routine, and what a realistic first year looks like in your sixties.",
 "For the first time in decades, nobody else sets your goals. A structured course gives the days a shape, and the piano gives them something beautiful.",
 "lead-burgundy-sofa.jpg", "Dr. Maria Pisarenko",
 "Unhurried, in order, and free. Begin with the first lesson:",
"""
<p>People in their sixties often tell me the same thing: <em>I always meant to learn, and there was never time.</em> Now there is. And retirement turns out to be one of the best moments in life to begin, for a simple reason: nobody else is setting your goals any more.</p>

<h2>Set up the room before you set up the routine</h2>

<p><strong>The light.</strong> Good, even light on the music stand makes more difference than people expect. Reading with tired eyes in a dim room is where many adult beginners quietly give up.</p>

<p><strong>The bench.</strong> Your forearms should be roughly level with the keys, and you should sit far enough back that your elbows can move freely. A bench that is too low makes the shoulders work and the hands tire quickly.</p>

<p><strong>The music.</strong> Choose editions with larger notation. There is no virtue in squinting.</p>

<h2>A daily shape</h2>

<p>Thirty minutes, at the same time each day, works better than an hour whenever you remember. Morning suits many people. Warm up gently with something easy, give the middle of the session to one new small thing, and end with a piece you enjoy. If you have any joint pain, ask your doctor before you increase your practice time; I am a pianist, not a physician.</p>

<h2>Memory works differently, not worse</h2>

<p>You may find that what you learned yesterday needs a short review today. That is normal. Begin each session by playing yesterday's new passage once, slowly, before you add anything. Over a few weeks, the review becomes shorter on its own.</p>

<h2>What a first year can look like</h2>

<p>By the end of a year of steady practice, most adults play simple pieces with both hands, read straightforward music, and have one or two pieces they can play for someone else. For many people in their sixties that piece is <em>Moon River</em>, <em>Yesterday</em>, <em>The Rose</em> or <em>Für Elise</em>. The page for <a href="../piano-lessons-for-adults-in-their-60s.html">adults in their 60s</a> lists the music people your age most want to play.</p>

<p>And there is a particular pleasure waiting at the end of that first year: sitting down at the piano at a family gathering, and playing.</p>
"""),

spec("learning-piano-in-your-20s", "2026-11-15",
 "Learning Piano in Your 20s: Beyond Falling-Bar Tutorials",
 "Falling-bar videos get you through one song. Here is what to add so you can read music, keep your hands healthy and actually play the anime, game and film themes you love.",
 "You can learn almost anything from a screen. Piano is the one skill where the screen can quietly teach your hands the wrong thing. Here is how to keep the speed and lose the habits.",
 "lead-pink-floor.jpg", "Dr. Maria Pisarenko at the grand piano",
 "Forty-one free lessons, in the right order:",
"""
<p>If you are in your twenties, you have probably learned a song from a video where colored bars fall onto a keyboard. That is a perfectly good way to get your first piece under your fingers. It also has three limits that nobody mentions.</p>

<h2>Limit one: you copy, you do not read</h2>

<p>Each falling-bar song is a separate project. You cannot take what you learned from <em>River Flows in You</em> and use it to learn <em>Merry-Go-Round of Life</em> faster, because you never learned what the notes are. Reading music is the skill that turns every new piece from a project into a variation. It takes weeks, not years, when it is taught in the right order.</p>

<h2>Limit two: the hand learns the wrong shape</h2>

<p>Playing on a small keyboard on a desk, with the wrists low and the shoulders lifted, feels fine for a month. Then the forearm starts to complain. The hand should rest its weight into the key, curved and relaxed, with the wrist level. That is the very first thing I teach, before any notes.</p>

<h2>Limit three: you want the beautiful pieces, and they need specific skills</h2>

<p>The music people in their twenties most often want to play &mdash; Joe Hisaishi's Ghibli themes, <em>Zelda's Lullaby</em>, Hans Zimmer's <em>Cornfield Chase</em>, Einaudi, Yiruma &mdash; is built on flowing left-hand patterns, the pedal and a singing melody on top. Those are learnable skills. Practiced in order, they bring the pieces within reach far sooner than trying each piece from scratch.</p>

<h2>What to keep from the videos</h2>

<p>The speed and the motivation. Keep learning songs you love; that energy is valuable. Just add, alongside it, twenty minutes a day of the foundations: reading, hand position, one new skill at a time.</p>

<p>The page for <a href="../piano-lessons-for-adults-in-their-20s.html">adults in their 20s</a> lists the pieces people your age most want to play, from Ghibli and game themes to Billie Eilish and Clair de Lune. Tell me which one you want, and I will point you to the lessons that lead to it.</p>
"""),

spec("starting-piano-again-at-40", "2026-11-17",
 "Starting Piano Again at 40: The Old Teacher in Your Head",
 "Coming back to the piano in your forties brings two obstacles nobody warns you about: the critical voice of a childhood teacher and a mind that understands faster than the hands can play.",
 "You understand music better than you did at ten. Your hands remember less than you hoped. And somewhere in your head, an old teacher is still frowning. All three can be worked with.",
 "lead-pink-gown.jpg", "Dr. Maria Pisarenko, concert pianist",
 "Start again from the first lesson, at your own pace:",
"""
<p>Many adults in their forties come back to the piano rather than starting it. They had lessons as children, quit at eleven or thirteen, and have regretted it quietly ever since. If that is you, you are in very large company.</p>

<p>Coming back brings two obstacles that beginners do not have.</p>

<h2>The old teacher is still in the room</h2>

<p>For many returning adults, the first wrong note brings back a voice: a sigh, a ruler, a <em>no, again</em>. That voice belongs to a different decade. It was never the best way to teach, and it certainly is not the right voice for an adult who chose, freely, to sit down at the piano.</p>

<p>Practice replacing it. When something goes wrong, the useful question is not <em>why can't I do this</em> but <em>which two notes went wrong, and what does my hand need to get them right</em>. A good lesson sounds like a calm conversation, and so should your practice.</p>

<h2>You understand faster than your hands can play</h2>

<p>At forty you can hear that a phrase should lean forward, understand a chord progression at a glance and know exactly how <em>Für Elise</em> or <em>Fallin'</em> should sound. Your hands cannot yet do it. That gap is frustrating, and it is also a gift: the hands only need to catch up with something you already understand, and they do, faster than they did when you were a child.</p>

<h2>What comes back, and what does not</h2>

<p>Reading usually comes back quickly. Hand position often does not, because many childhood lessons never taught it properly. Begin from the first lesson anyway, even if it feels too easy. A week of easy lessons costs nothing, and it often reveals the one habit that held you back the first time.</p>

<h2>Give yourself a goal</h2>

<p>Adults without a goal drift. Choose one piece to play by next summer. The page for <a href="../piano-lessons-for-adults-in-their-40s.html">adults in their 40s</a> lists the music people your age most often want to play, from <em>Canon in D</em> to <em>My Heart Will Go On</em>.</p>
"""),

spec("piano-for-seniors-keyboard-light-music", "2026-11-19",
 "Piano for Seniors: The Right Keyboard, Light and Music",
 "Piano for seniors starts before the first note: a comfortable keyboard, good light, a bench at the right height and music you already love. A concert pianist's practical setup guide.",
 "Lessons here are short, in order and unhurried. You set the pace, and the first piece you play can be one you have loved all your life.",
 "lead-concert-gown.jpg", "Dr. Maria Pisarenko, concert pianist",
 "Unhurried lessons you can pause and repeat:",
"""
<p>I am sometimes asked whether there is an age after which it makes no sense to begin. There is not, and I wrote about why in <a href="learning-piano-after-70.html">Learning Piano After 70</a>. This article is the practical half: how to set things up so that every session is comfortable and enjoyable from the first week.</p>

<h2>Choose the instrument for comfort</h2>

<p>A digital piano with full-size, weighted keys is a good choice: it never needs tuning, the volume can be turned down, and many have a setting that makes the keys a little lighter to press. Make sure the bench lets your forearms rest level with the keys.</p>

<h2>Choose music you already love</h2>

<p>The fastest way to keep going is to work toward a piece that means something to you. For many people in their seventies it is <em>Moon River</em>, <em>Edelweiss</em>, <em>Over the Rainbow</em>, <em>Amazing Grace</em> or a Chopin nocturne heard long ago. Because you already know how it should sound, your ear guides your hands.</p>

<h2>Short sessions, often</h2>

<p>Fifteen to twenty minutes is plenty, once or twice a day. Stop before your hands tire. If you have arthritis or any joint pain, ask your doctor first, and keep everything gentle; the piano should never hurt.</p>

<h2>Repeat without guilt</h2>

<p>Each lesson in the course can be paused and watched again as many times as you like. Repeating is not falling behind. It is exactly how musicians of every age learn.</p>

<h2>Large, clear music</h2>

<p>Read from editions with larger notation, or enlarge the music on a tablet. Good light on the stand matters.</p>

<h2>The reward</h2>

<p>Playing for your family in your own home turns you into the center of a moment that people remember. The page for <a href="../piano-lessons-for-adults-in-their-70s.html">adults in their 70s and beyond</a> lists the songs people your age most often want to play. And if you would like a personal answer, send me a recording; I listen to every one myself.</p>
"""),
]

if __name__ == "__main__":
    out = pathlib.Path(__file__).resolve().parent / "_specs_batch_09_ages.json"
    out.write_text(json.dumps(SPECS, indent=1, ensure_ascii=False), encoding="utf-8")
    print("wrote", out.name, len(SPECS))
