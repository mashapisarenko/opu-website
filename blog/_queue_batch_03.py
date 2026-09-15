# -*- coding: utf-8 -*-
import json, pathlib

SPECS = [
{
 "slug": "piano-wrist-position-adults",
 "date": "2026-09-23",
 "title": "Wrist Height: The Single Most Common Fault in Adult Beginners",
 "description": "A dropped wrist is the commonest fault a concert pianist sees in adult beginners, and it causes aching hands, a thin sound and uneven playing. How to find the right height in two minutes and check it yourself.",
 "sub": "One thing goes wrong more often than everything else put together, and it is not a musical mistake at all. It is the height of your wrist.",
 "image": "lead-seated-black.jpg",
 "image_alt": "Dr. Maria Pisarenko at the keyboard",
 "cta_text": "The free course begins with exactly this &mdash; how to sit before how to read:",
 "cta_href": "https://youtu.be/AzU01rYWHK8",
 "cta_link": "Start at Lesson 1 &rarr;",
 "body": """
<p>When someone sends me a recording, I usually know what I am going to say within the first five seconds, and it is almost never about notes. It is about a wrist sitting below the level of the keys.</p>

<p>I would put it this way: if you fixed only one thing about how you play, and never fixed anything else, fix this. It is upstream of most of the other complaints adults bring me.</p>

<h2>What a dropped wrist actually does</h2>

<p>The piano key does not care what pushes it down. It cares how much weight arrives and how it is released. Your arm is heavy; your fingers are not. When the wrist hangs below the keyboard, the arm's weight cannot travel forward into the key &mdash; the angle sends it into the wrist joint instead. So the finger has to press. And the finger, working alone, is a small and rather weak machine.</p>

<p>Everything downstream follows from that:</p>

<ul>
  <li><strong>Aching forearms after twenty minutes.</strong> Small muscles are doing a large muscle's job, and they fatigue exactly on schedule.</li>
  <li><strong>A thin, hard sound.</strong> A pressed key and a dropped key sound different. The pressed one has an edge at the front of the note and no body behind it.</li>
  <li><strong>Uneven playing.</strong> Each finger presses with a different amount of its own strength, so the notes come out at different volumes &mdash; and the fourth and fifth fingers, the weakest, come out quietest of all.</li>
  <li><strong>Nothing works above a certain speed.</strong> Pressing has to be repeated for every note. Weight and release can be passed along the hand. Only one of those scales.</li>
</ul>

<p>Adults nearly always read these four as evidence about themselves: <em>my hands are too old, too small, too stiff, not strong enough.</em> They are evidence about an angle.</p>

<h2>Finding the right height, in two minutes</h2>

<p>Sit at the instrument and let both arms hang loose at your sides. Completely loose &mdash; shake them once so the shoulders drop.</p>

<p>Now, without lifting your shoulders, bring your hands up onto the keys. Where the forearm naturally arrives is nearly the right height: <strong>the forearm running level with the tops of the white keys, or very slightly above &mdash; never below.</strong> The wrist is a flat continuation of the forearm, not a hinge that dips.</p>

<p>If your forearm comes to rest below the keys, the bench is too low. That is all it is. Nobody's anatomy requires a dropped wrist; a dining chair does.</p>

<p><strong>If the bench does not adjust:</strong> sit on a folded towel or a firm cushion and add thickness until the forearm is level. This is not a temporary bodge to be embarrassed about &mdash; it is precisely what an adjustable bench does, and the reason every serious pianist owns one.</p>

<h2>The test that tells you the truth</h2>

<p>Your own sense of your wrist is unreliable. Mine was, at your stage, and so was everyone's. So do not trust it &mdash; look.</p>

<p>Put your phone on the music stand, or on a shelf to your side, at roughly the height of the keyboard, and film thirty seconds of whatever you are working on. Watch it that evening. You are looking for one thing: <strong>does the line of the forearm run level into the hand, or does it dip down at the wrist?</strong></p>

<p>Almost everyone discovers the wrist drops at exactly one moment &mdash; the hard bar. The hand is fine and then the passage gets difficult and the wrist sinks. That is tension, arriving on cue, and now you know precisely where to look for it.</p>

<h2>The exercise, two minutes a day</h2>

<p>One note. Any note, third finger, right hand.</p>

<p>Raise the whole arm a little from the shoulder, keeping the wrist flat and the fingertip firm. Let it fall &mdash; not push, fall &mdash; so the key goes down with the arm's weight behind it. Then release immediately, letting the hand come back up as one piece.</p>

<p>Listen to the note until it dies away. You are listening for something round that carries, rather than something short and hard. Do it ten times with each hand, slowly, before you play anything else.</p>

<p>Two minutes a day, and within two weeks your ordinary playing starts to inherit it. This is the first thing I teach anyone, child or adult, and it is the first thing in my free course, before a single note is read.</p>

<h2>Two warnings</h2>

<p><strong>Level does not mean rigid.</strong> A wrist held stiffly flat is its own problem &mdash; it simply moves the tension somewhere else. The wrist should be level and free, able to float slightly up at the end of a phrase. Think of it as hanging from the forearm, not braced against it.</p>

<p><strong>And high is not better than level.</strong> A wrist carried well above the keys throws the fingers at the keyboard from above and produces its own hard sound. Level, or a shade above. That is the whole rule.</p>

<p>Adults tell me constantly that their hands are the problem. In thirty years of teaching I have met very few hands that were the problem. I have met a great many chairs.</p>

<p>Film your thirty seconds this week. If you want another musician to look at it with you, <a href="../submit.html">send it to me &mdash; I answer recordings myself and it costs nothing</a>.</p>
"""
},
{
 "slug": "digital-piano-vs-acoustic-beginner",
 "date": "2026-09-25",
 "title": "Digital or Acoustic: What Actually Matters When You Are Starting",
 "description": "A concert pianist on choosing a first instrument as an adult beginner — which features genuinely affect your playing, which are marketing, and why the wrong digital piano teaches a habit you will have to un-learn.",
 "sub": "Most of what is argued about here does not matter. Two things do, and one of them is not on the box.",
 "image": "lead-piano-strings.jpg",
 "image_alt": "Piano strings, photographed inside the instrument",
 "cta_text": "The free course works on any instrument you already have:",
 "cta_href": "https://youtu.be/AzU01rYWHK8",
 "cta_link": "Start at Lesson 1 &rarr;",
 "body": """
<p>This is the question I am asked before any other, usually by someone who has not yet played a note and is worried about choosing wrong before they begin.</p>

<p>So let me take the pressure off first: <strong>the instrument you already have is good enough to start.</strong> If there is a keyboard in the house, begin on it today. Do not wait for the right purchase; waiting is a far bigger risk to your playing than any instrument is.</p>

<p>That said, two things genuinely matter, and a great deal of what gets argued about does not.</p>

<h2>The two things that matter</h2>

<p><strong>1. Weighted keys that respond to how you play them.</strong> This is the whole question, and everything else is decoration.</p>

<p>On a real piano, a key pressed gently gives a quiet sound and a key played with the arm's weight gives a full one. That relationship is not a feature; it is what playing the piano <em>is</em>. Every physical thing I teach &mdash; weight, release, evenness, tone, phrasing &mdash; exists only because the instrument answers differently depending on how the key goes down.</p>

<p>An unweighted keyboard, where every key gives the same volume no matter what you do, cannot teach any of it. Worse, it teaches the opposite: it trains a hand to poke, because poking works there. That habit then has to be un-learned on a real instrument, and un-learning is far slower than learning.</p>

<p>The words to look for are <strong>weighted</strong>, <strong>hammer action</strong> or <strong>graded hammer action</strong>. The words that mean you are being sold something else are <em>touch-sensitive</em> alone, and <em>semi-weighted</em>.</p>

<p><strong>2. Enough keys that the music does not run out.</strong> More on this below, but briefly: a beginner's first months need far fewer keys than people think, and a beginner's second year needs more than a small keyboard has.</p>

<h2>What does not matter nearly as much as the shop suggests</h2>

<p><strong>The number of sounds.</strong> Six hundred voices is six hundred ways not to practise. You need one good piano sound.</p>

<p><strong>Built-in songs, light-up keys and learning modes.</strong> These teach you to follow a machine rather than to read. The skill you want is reading, and a light above a key is not reading.</p>

<p><strong>Brand loyalty arguments.</strong> Among the established makers, at a given price, the differences at beginner level are real but small, and much smaller than the difference between weighted and unweighted.</p>

<p><strong>Whether it is &ldquo;a real piano&rdquo;.</strong> A good digital instrument in a flat where you can play at eleven at night is worth more than an acoustic you are afraid to touch. I say this as someone who performs on concert grands.</p>

<h2>Digital or acoustic, honestly</h2>

<p><strong>A digital piano is the better choice for most adult beginners.</strong> It never goes out of tune, it costs nothing to maintain, it takes headphones so the household is not consulted about your practice hours, and a decent weighted one is cheaper than a year of tuning and repair on a neglected acoustic.</p>

<p><strong>An acoustic upright is the better choice if</strong> you have the space, the household, and either a good instrument already or the budget to have one chosen properly. The sound is richer, the action tells you more, and it rewards you as you improve in a way that a modest digital does not.</p>

<p><strong>What I would avoid:</strong> a free acoustic piano of unknown history. &ldquo;Free piano, you just have to move it&rdquo; is very often a piano that needs more work than it is worth, and moving it costs real money before you find out. Have anyone's free piano looked at by a tuner before it enters your house.</p>

<h2>How many keys</h2>

<p>The honest answer is that it depends how long you intend to keep playing.</p>

<p>Your first months will live in the middle of the keyboard and could be done on a very small instrument. But the repertoire an adult actually wants &mdash; the pieces people picture when they imagine themselves playing &mdash; reaches out to both ends, and a short keyboard starts refusing to play the music before your hands refuse to.</p>

<p>If you are buying once and keeping it, buy the full set of 88. If you are borrowing or starting on what is in the house, start there and do not think about it again for six months. I have written about this in more detail on my <a href="../books.html">instruments and books page</a>.</p>

<h2>Two things to buy that nobody mentions</h2>

<p><strong>An adjustable bench.</strong> This will do more for your playing than an extra two hundred dollars of instrument. Almost every fault I see in adult beginners &mdash; aching forearms, a thin sound, uneven fingers &mdash; begins with sitting too low, and a dining chair is nearly always too low. A bench that adjusts fixes it permanently in one purchase.</p>

<p><strong>A proper stand, if the instrument does not come with legs.</strong> A keyboard on a wobbling X-stand moves when you play with any weight, and a hand that feels the instrument move learns not to use weight. Something solid, at the right height, that does not travel.</p>

<h2>So: what to do this week</h2>

<p>If you have any keyboard at all, start on it, today, and come back to this question in three months when you know whether the habit is taking. If you are buying: weighted hammer action, 88 keys if you can, an adjustable bench, and ignore everything printed on the front panel in large type.</p>

<p>Then start. The instrument matters much less than the fact that you began.</p>
"""
},
{
 "slug": "does-piano-playing-hurt-hands",
 "date": "2026-09-28",
 "title": "Should Playing the Piano Hurt? No &mdash; and Here Is What Hurting Means",
 "description": "Aching hands, wrists or forearms after playing are not a normal part of learning the piano. A concert pianist explains what pain is telling you, the three causes she sees most often, and what to change.",
 "sub": "It should not hurt. Not at your age, not at any age, not even at the beginning. If it does, it is information &mdash; and it is usually about four specific things.",
 "image": "lead-pink-gown.jpg",
 "image_alt": "Dr. Maria Pisarenko, concert pianist and university professor",
 "cta_text": "The free course starts with the body, before a single note is read:",
 "cta_href": "https://youtu.be/AzU01rYWHK8",
 "cta_link": "Start at Lesson 1 &rarr;",
 "body": """
<p>Adults ask me this quietly, as though it might be an embarrassing question. It is not. It is one of the most important questions a beginner can ask, and the answer is short.</p>

<p><strong>No. Playing the piano should not hurt.</strong> Not a burning forearm, not an aching wrist, not sore knuckles, not a thumb that complains the next morning. Discomfort is not the price of learning and it is not a sign that you are working hard. It is information about how the work is being done.</p>

<p>Musicians are not, as a profession, unusually stoical about this. We are trained from childhood to treat pain as a fault in the playing, because a pianist who plays through it stops being a pianist. I would like adults to inherit that attitude rather than the sporting one.</p>

<h2>What hurting usually means</h2>

<p>In my teaching, aching hands in a beginner come from one of four things, and the first is far commoner than the other three together.</p>

<p><strong>1. The bench is too low.</strong> If your forearm sits below the level of the keys, the weight of your arm cannot reach the key &mdash; the angle is wrong &mdash; so the small muscles of the hand and forearm do work they are not built for. They ache on schedule, usually at fifteen to twenty minutes.</p>

<p>Sit so the forearm runs level with the tops of the white keys, or very slightly above. If the chair does not adjust, sit on a folded towel. This single change resolves most of the aching I am asked about.</p>

<p><strong>2. The hand is being held rather than hanging.</strong> Many adults arrive with an idea that the hand must be arranged into a shape and kept there. So it is held, continuously, by muscular effort &mdash; and holding anything for twenty minutes hurts, whatever it is.</p>

<p>The hand's shape at the piano should be the shape it already makes when your arm hangs loose at your side: fingers naturally curved, nothing arranged. Let it hang, then bring it to the keys without changing it.</p>

<p><strong>3. Nothing is being released.</strong> Beginners press a key and stay pressed until the next note. Pianists put weight in and take it out again, continuously. If your hand never lets go between notes, it is under load for the entire practice, and load without release is exactly the recipe for aching.</p>

<p>Practise this on one note: let the arm's weight down into the key, then release the moment the sound has begun. The note goes on sounding without you holding it down hard &mdash; the instrument does not need the pressure, only the descent.</p>

<p><strong>4. Too much, too suddenly.</strong> An adult who has never played sits down for ninety minutes because they finally have a free Sunday. That is a new physical activity done for ninety minutes without preparation, and the body responds as it would to any other.</p>

<p>Fifteen to twenty minutes a day, every day, builds hands far faster and with none of this. Six short sessions beat one long one for reasons that have nothing to do with willpower and everything to do with how physical skills consolidate overnight.</p>

<h2>Ordinary tiredness versus the kind you must not ignore</h2>

<p>There is a difference between a hand that feels worked and a hand that is telling you to stop, and beginners often cannot yet read it. So use these lines instead of your judgement:</p>

<p><strong>Stop the session now, and change something before the next one, if you have:</strong></p>

<ul>
  <li>Pain that is <strong>sharp</strong> rather than dull, or that arrives suddenly at a particular moment</li>
  <li>Anything in the wrist, rather than in the muscle of the forearm</li>
  <li><strong>Tingling or numbness</strong> in the fingers, at any time</li>
  <li>Discomfort that is still there the next morning</li>
  <li>Pain that appears earlier each session &mdash; twenty minutes this week, ten the next</li>
</ul>

<p>Any of those means something in the setup is wrong, and playing through it will make it worse rather than stronger. And any pain that persists after you have fixed the bench, the holding and the release is a matter for a medical professional rather than a piano teacher &mdash; I am not qualified to advise you on your body, and I would not want you to accept my guesses instead of an examination.</p>

<h2>What to change today, in order</h2>

<ol>
  <li><strong>Raise the seat</strong> until your forearm is level with the keys. Towel, cushion, adjustable bench &mdash; whatever gets you there.</li>
  <li><strong>Let the hand hang</strong> at your side, then bring it up unchanged. Stop arranging it.</li>
  <li><strong>Release after every note</strong> for two minutes a day on a single key, until it stops being a thought.</li>
  <li><strong>Cut the session to fifteen minutes</strong> and make it daily rather than occasional.</li>
</ol>

<p>Then, a week later, film thirty seconds of yourself playing and watch it. The wrist dipping below the keys, the hand braced into a shape, the arm never rising between notes &mdash; all three are visible in a way they are not feelable.</p>

<p>And if you would like another musician to look at those thirty seconds with you, <a href="../submit.html">send them to me</a>. Hearing and seeing yourself is the part of this you genuinely cannot do alone &mdash; and a small physical fault caught in month two takes a minute to correct, where the same fault caught in year two takes a season.</p>
"""
},
]

pathlib.Path("_specs_batch_03.json").write_text(json.dumps(SPECS, ensure_ascii=False, indent=1), encoding="utf-8")
print("specs:", len(SPECS))
