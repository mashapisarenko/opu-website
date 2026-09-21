# -*- coding: utf-8 -*-
"""Builds /press.html - what has been written and broadcast about her.

Source: her own CV (Dr.MPisarenkoPianistCVOct2019.docx.pdf) plus her bio document.
EVERY external link below was opened in a real browser and confirmed on 2026-09-21.
What changed on that re-check:
  - Clark County, NV (2019): the county has since RETIRED the page - it now answers 404.
    Replaced with the Internet Archive's permanent capture of 17 Jul 2019, whose text was
    read and matches the quote word for word.
  - Las Vegas Sun, 16 Feb 2009: previously quoted WITHOUT a link because the page answered
    402 to an automated fetch. Opened in a browser on 2026-09-21: the full profile is live
    and free to read. Now linked.
  - Prescott Pops Symphony (Arizona): her guest-artist page on the orchestra's own site,
    found and confirmed live on 2026-09-21. Added.
Still quoted WITHOUT a link, on purpose:
  - Salt Lake Tribune: entertainment.sltrib.com no longer resolves, and no archived copy
    of the piece has been located.
  - Southern Utah University: this is from a letter, not a published article.
Nothing here is paraphrased or improved. A quote that could not be verified is not on
the page - per her standing rule, never invent a fact, a price, a date or a page number.

Same discipline as make_first_piece_page.py: cloned from a LIVE page so the head,
analytics, nav, footer and CSS cannot drift.

Run from opu-website/:  python3 make_press_page.py
"""
import pathlib, re, sys

# The day every external link on this page was last opened in a real browser.
# The daily check reads this and complains when it goes stale.
LINKS_VERIFIED = "2026-09-21"  # 9 press links + 11 video links, all opened 2026-09-21

HERE = pathlib.Path(__file__).resolve().parent
SHELL = HERE / "free-course.html"
OUT = HERE / "press.html"

TITLE = "Press & Recognition - Dr. Maria Pisarenko, Concert Pianist"
DESC = ("Press, radio and awards for Dr. Maria Pisarenko, DMA - Review-Journal, Las Vegas Sun, This Is Reno, Salt Lake Tribune, Channel One Russia, Steinway.")

# (publication, year, url or None, quote or None, note or None, linklabel or None)
PRESS = [
 ("Las Vegas Review-Journal", "2019",
  "https://www.reviewjournal.com/local/summerlin/las-vegas-musician-began-playing-piano-at-5-in-siberia-1685788/",
  "&ldquo;Music is language, and language is music,&rdquo; she said. &ldquo;They reflect history, "
  "traditions, beliefs. It helps us open our minds to new ideas, new ways of looking at the world.&rdquo;",
  "Feature: <i>Las Vegas musician began playing piano at 5 &mdash; in Siberia</i>", None),
 ("Las Vegas Sun", "2009",
  "https://lasvegassun.com/news/2009/feb/16/masha-pisarenko/",
  "&ldquo;Masha Pisarenko began playing the piano at age 5 in a small town in Siberia.&rdquo;",
  "<i>People in the Arts</i> &mdash; the paper&rsquo;s weekly profile of a working artist in the "
  "valley, by Kristen Peterson. Photograph by Sam Morris.", None),
 ("Las Vegas Sun", "2008",
  "https://lasvegassun.com/news/2008/sep/17/intimate-masterful-and-free/",
  "&ldquo;Siberian-born Pisarenko trained at the Russian Academy of Music and performed in Europe "
  "before moving to the States.&rdquo;",
  "<i>Intimate, masterful and free</i>", None),
 ("This Is Reno", "2010",
  "https://thisisreno.com/2010/02/pianist-maria-pisarenko-wins-reno-chamber-orchestra-college-concerto-competition/",
  None,
  "<i>Pianist Maria Pisarenko wins Reno Chamber Orchestra College Concerto Competition</i> &mdash; "
  "the prize was to appear as featured soloist with the orchestra.", None),
 ("Clark County, Nevada", "2019",
  "https://web.archive.org/web/20190717052607/http://www.clarkcountynv.gov/public-communications/news/Pages/Russian-Seasons-in-Las-Vegas-Feb--9.aspx",
  "&ldquo;Dr. Maria (Masha) Pisarenko is actively involved in the cultural life of Las Vegas as a "
  "performer, educator and artistic director &hellip; She has performed on some of the most "
  "prestigious stages of the world, including in Russia, Asia, Europe, and the United States.&rdquo;",
  "The county&rsquo;s own announcement, <i>Russian Seasons in Las Vegas</i>. Clark County has since "
  "retired the page; this is the Internet Archive&rsquo;s permanent capture of it.",
  "Read the county&rsquo;s archived page &rarr;"),
 ("Las Vegas Review-Journal", "2019",
  "https://neon.reviewjournal.com/music/russian-seasons-to-perform-next-month-in-las-vegas-1584818/",
  None,
  "<i>Russian Seasons to perform next month</i> &mdash; a program of Russian chamber and vocal "
  "music she presented and played.", None),
 ("Prescott Pops Symphony", None,
  "https://prescottpops.com/masha-pisarenko/",
  None,
  "The Arizona orchestra&rsquo;s own guest-artist page.", "See the orchestra&rsquo;s page &rarr;"),
 ("Salt Lake Tribune", None, None,
  "&ldquo;The Siberian-born artist has performed throughout Europe, and has won various competitions "
  "before coming to the United States. She has been a featured performer on Nevada Public Radio and a "
  "guest soloist with numerous orchestras.&rdquo;", None, None),
]

# Letters, citations and institutional endorsements - not newspaper articles.
ENDORSEMENTS = [
 ("Southern Utah University",
  "&ldquo;With a career that began with international acclaim at a young age and has continued to be "
  "successful &hellip; a mature, highly experienced performing artist, [she] is an individual that can "
  "render the sincere emotion and deep feelings of the composers.&rdquo;",
  "From a letter held in her file."),
 ("Southern Nevada Musical Arts Society",
  "&ldquo;In recognition of your graciously sharing your musical artistry.&rdquo;",
  "Citation accompanying the society&rsquo;s recognition."),
 ("Steinway &amp; Sons",
  None,
  "<b>Steinway Top Teacher Award</b> &mdash; awarded for her teaching."),
]

BROADCASTS = [
 ("Nevada Public Radio (88.9 KNPR)", "Interview &mdash; November 2012, and again November 2009"),
 ("Reno Public Radio (KUNR FM)", "Interview &mdash; February 2010; Mozart&rsquo;s Piano Concerto No. 21 "
  "with the Reno Chamber Orchestra, broadcast March 2010"),
 ("Channel One Russia", "National television &mdash; performance and interview at the First "
  "International Tchaikovsky Youth Competition"),
 ("Radio of Russia, Irkutsk", "Interviews &mdash; 2016 and 2004"),
 ("Angarsk Radio", "Interview"),
 ("Vesti Irkutsk", "Solo recital at the Irkutsk Philharmonic, and Grieg&rsquo;s Piano Concerto with the "
  "Irkutsk Philharmonic Orchestra &mdash; broadcast, with interview"),
]


# Every id below was resolved through YouTube's oEmbed endpoint on 2026-09-21 and came
# back with a real title. All of them live on the LAS VEGAS PIANO SCHOOL channel - that
# is where she published them years ago, and it is stated on the page rather than hidden.
TEACHING = [
 ("rBFtvaVzHao", "Masterclass &mdash; Southern Utah University"),
 ("dYG3BpAfvg0", "Masterclass &mdash; Southern Utah University"),
 ("wTivVH7kgW4", "Masterclass &mdash; College of Southern Nevada"),
 ("6XSnGz8EJ3E", "Masterclass &mdash; Dixie State University"),
 ("7oCPAmZ7ZNw", "Group music theory class &mdash; University of Nevada, Las Vegas"),
]
PLAYING = [
 ("-qdfCD3HkDM", "Grieg &mdash; Piano Concerto in A minor, with the UNLV Symphony Orchestra"),
 ("nHnkxR2ZVWY", "Mozart &mdash; Piano Concerto No. 21, K. 467, with orchestra"),
 ("EgFVoXjRwBc", "Beethoven &mdash; Choral Fantasy, Op. 80, with orchestra and chorus"),
 ("bUlj5NvPVlw", "Solo recital &mdash; Bach, Beethoven, Brahms, Chopin, Scriabin"),
 ("ZwyCmQZjgSQ", "Solo recital &mdash; Bach, Mozart, Schumann, Liszt, Prokofiev, Gershwin"),
 ("BBZP-fcnki0", "Chamber recital &mdash; Mozart, Mendelssohn and Shostakovich piano trios"),
]


# Scanned documents, on letterhead and signed. Every one was read in full on 2026-09-21
# before it went on the page, and private data was PAINTED OUT of the image first:
# Weller's home address, Peterson's home address and phone, her OWN home address on the
# UNLV letter, Victor Alvarez's email, Damaris Morales-Alvarez's direct line. Redaction is
# a filled rectangle burned into the JPEG, not a CSS overlay - an overlay can be removed
# by anyone with a browser. The redacted images are the only ones in the repository.
#
# Two documents in her folder are deliberately NOT here:
#   - William Epstein's letter is a GRADE APPEAL to another school, describing a disputed
#     grade and a departmental conflict. It argues for her, but publishing it broadcasts
#     the dispute. It would cost her trust, not build it.
#   - "BusinessRate TOP 3 of 2026" is an award-mill mailer that sells plaques off Google
#     reviews. Placed beside Steinway and ABRSM it devalues them.
# (slug, who, role, year, pull quote, one line of context)
LETTERS = [
 ("weller-2010", "Harold Weller",
  "Founding Music Director &amp; Conductor Laureate, The Las Vegas Philharmonic", "2010",
  "&ldquo;On February 14th Masha performed brilliantly, eliciting an instant standing ovation "
  "from the 1,200 in attendance and playing the <i>Concerto</i> as if it had been part of her "
  "repertory for many years.&rdquo;",
  "He invited her as guest soloist for Rachmaninov&rsquo;s Second Piano Concerto &mdash; a work, "
  "he writes, &ldquo;she had not yet studied or performed.&rdquo; Earlier in the same letter: "
  "&ldquo;an exceptionally gifted pianist&rdquo; whose &ldquo;ease, fluidity, and poetic "
  "interpretation&rdquo; reminded him of Valentina Lisitsa."),
 ("suu-2012", "Dr. Christian Bohnenstengel, NCTM",
  "Director of Keyboard Studies, Southern Utah University", "2012",
  "&ldquo;One of our finest piano majors commented enthusiastically &hellip; and noted that this "
  "may have been the best recital he has ever attended. Another audience member perceived each "
  "note as having a life of its own and noted Ms. Pisarenko&rsquo;s ability to make the notes "
  "&lsquo;dance with each other.&rsquo;&rdquo;",
  "After a recital and a masterclass with four piano majors: &ldquo;The students appreciated "
  "Ms. Pisarenko&rsquo;s musical insights, technical advice, as well as her patient and helpful "
  "demeanor.&rdquo;"),
 ("csn-morales-2017", "D&aacute;maris Morales-Alvarez",
  "Piano Program Coordinator, College of Southern Nevada", "2017",
  "&ldquo;Ms. Pisarenko is also in charge of teaching some of our music Piano Major students and "
  "for preparing them for recitals and juries. In this task she has always done a remarkable "
  "work. <b>Her students demonstrate solid technic and musicianship.</b>&rdquo;",
  "Written by the colleague who observed and evaluated her classes: &ldquo;knowledgeable and "
  "diligent in the classroom &hellip; an excellent role model for our piano students.&rdquo;"),
 ("peterson-2017", "Dr. Douglas R. Peterson",
  "Music Director, Southern Nevada Musical Arts Society", "2017",
  "&ldquo;I have only the highest praise for pianist Masha Pisarenko &hellip; Her performances in "
  "both the Beethoven <i>Choral Fantasia</i> and the <i>Mozart Concerto</i> were accorded standing "
  "ovations!&rdquo;",
  "After four programs together over four years. He closes: &ldquo;Now that she has her doctorate "
  "I predict Masha can also look forward to an outstanding career in the educational field.&rdquo;"),
 ("csn-alvarez-2012", "Dr. Victor Hugo Alvarez",
  "Music Professor and founder of the CSN Piano Concerto Competition", "2012",
  "&ldquo;As a lead jury, you showed experience and sensitivity to each of the young pianist that "
  "were select to play for you; all our participants were very enthusiastic with the Master Class "
  "you offer and <b>wanted more time with you</b>.&rdquo;",
  "Written after she sat as lead juror at the twelfth CSN Piano Concerto Competition."),
 ("suu-2013", "Dr. Christian Bohnenstengel, NCTM",
  "Director of Keyboard Studies, Southern Utah University", "2013",
  "&ldquo;One of my colleagues commented enthusiastically on the performance of the <i>Toccata in "
  "E Minor</i> by Bach, admiring Ms. Pisarenko&rsquo;s ability to convey the complex polyphonic "
  "texture by giving each voice its own distinct color (e.g. bassoon, violin, etc.).&rdquo;",
  "Her second invitation to Southern Utah University in as many years, again for a recital and a "
  "masterclass."),
 ("peterson-2010", "Dr. Douglas R. Peterson",
  "Music Director, Southern Nevada Musical Arts Society", "2010",
  "&ldquo;Masha&rsquo;s piano skills are formidable and her interpretations sensitive. She was "
  "extremely well-prepared in all three programs &hellip; and I found her a pleasure to work "
  "with.&rdquo;",
  "The earlier of his two letters, written while she was still working toward the doctorate."),
 ("bowers-unlv-2010", "Michael W. Bowers, Ph.D.",
  "Executive Vice President &amp; Provost, University of Nevada, Las Vegas", "2010",
  "&ldquo;Congratulations to you on becoming First Prize Winner of the Reno Chamber Orchestra "
  "Concerto Competition &hellip; It appears that you are on your way to a very prominent artistic "
  "career.&rdquo;",
  "From the provost&rsquo;s office of her own university."),
]

# (slug, title, issuer, year, one line)
CERTIFICATES = [
 ("abrsm-2026", "Letter of Appreciation", "ABRSM &mdash; the Associated Board of the Royal Schools of Music", "2026",
  "For teachers whose students earned a <b>Distinction</b> in an ABRSM examination and played at "
  "the High Scorers&rsquo; Concert. Signed by the Chief Executive. Nevada, 1 May 2026."),
 ("abrsm-2025", "Letter of Appreciation", "ABRSM &mdash; the Associated Board of the Royal Schools of Music", "2025",
  "The same recognition the year before. Two consecutive years of students taking a Distinction "
  "in the examinations of a London board that has graded players since 1889."),
 ("steinway-2018", "Top Music Teacher", "Steinway &amp; Sons", "2018",
  "&ldquo;Steinway &amp; Sons is pleased to recognize Dr. Maria Pisarenko &mdash; 2018 Top Music "
  "Teacher.&rdquo; Signed by the Chief Executive Officer of Steinway Musical Instruments."),
 ("snmas-2013", "Certificate of Appreciation", "Southern Nevada Musical Arts Society", "2013",
  "Presented in the society&rsquo;s fiftieth-anniversary year: &ldquo;In recognition of your "
  "graciously sharing your musical artistry.&rdquo;"),
]


def letter(slug, who, role, year, quote, context):
    return (
      f'      <div class="card" style="padding:0;overflow:hidden">'
      f'<a href="images/letters/{slug}.jpg" target="_blank" rel="noopener" '
      f'style="display:block;background:#e9e6df;border-bottom:1px solid var(--line)">'
      f'<img src="images/letters/{slug}-thumb.jpg" loading="lazy" '
      f'alt="Letter from {who}, {year}, on official letterhead" '
      f'style="display:block;width:100%;height:230px;object-fit:cover;object-position:top"></a>'
      f'<div style="padding:15px 16px">'
      f'<p style="margin:0 0 10px">{quote}</p>'
      f'<p class="muted" style="margin:0 0 10px;font-size:.9rem">{context}</p>'
      f'<p style="margin:0;font-size:.93rem"><b>{who}</b> <span class="muted">&middot; {year}</span>'
      f'<br><span class="muted" style="font-size:.9rem">{role}</span>'
      f'<br><a href="images/letters/{slug}.jpg" target="_blank" rel="noopener">Read the letter itself &rarr;</a>'
      f'</p></div></div>')


def certificate(slug, title, issuer, year, note):
    return (
      f'      <div class="card" style="padding:0;overflow:hidden">'
      f'<a href="images/letters/{slug}.jpg" target="_blank" rel="noopener" '
      f'style="display:block;background:#e9e6df;border-bottom:1px solid var(--line)">'
      f'<img src="images/letters/{slug}-thumb.jpg" loading="lazy" '
      f'alt="{title} from {issuer}, {year}" '
      f'style="display:block;width:100%;height:210px;object-fit:contain;padding:10px"></a>'
      f'<div style="padding:15px 16px">'
      f'<p style="margin:0 0 8px;font-size:1.02rem"><b>{title}</b> '
      f'<span class="muted">&middot; {year}</span></p>'
      f'<p class="muted" style="margin:0 0 10px;font-size:.9rem">{note}</p>'
      f'<p style="margin:0;font-size:.93rem">{issuer}'
      f'<br><a href="images/letters/{slug}.jpg" target="_blank" rel="noopener">See the document &rarr;</a>'
      f'</p></div></div>')


def clip(vid, label):
    """A still with a play badge, not an embed: eleven autoplay-capable iframes would make
    the page crawl, and an embed also lets YouTube set cookies before anyone clicks.
    hqdefault is 4:3 with black bars, so the box is 16:9 and the image is cropped to it.
    A thumbnail that fails to load leaves a dark box, not a broken-image icon."""
    return (
      f'      <a class="card" style="text-decoration:none;display:block;padding:0;overflow:hidden" '
      f'href="https://www.youtube.com/watch?v={vid}" target="_blank" rel="noopener">'
      f'<span style="display:block;position:relative;aspect-ratio:16/9;background:#14213d">'
      f'<img src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt="" loading="lazy" '
      f'style="display:block;width:100%;height:100%;object-fit:cover">'
      f'<span aria-hidden="true" style="position:absolute;inset:0;display:flex;align-items:center;'
      f'justify-content:center"><span style="width:54px;height:54px;border-radius:50%;'
      f'background:rgba(20,33,61,.78);border:2px solid rgba(255,255,255,.9);display:flex;'
      f'align-items:center;justify-content:center"><span style="display:block;width:0;height:0;'
      f'margin-left:4px;border-left:15px solid #fff;border-top:9px solid transparent;'
      f'border-bottom:9px solid transparent"></span></span></span></span>'
      f'<span style="display:block;padding:12px 14px;font-size:.93rem">{label}'
      f'<br><span class="muted" style="font-size:.86rem">Watch on YouTube &rarr;</span></span></a>')



def card(pub, year, url, quote, note, linklabel=None):
    head = f"<b>{pub}</b>" + (f' <span class="muted">&middot; {year}</span>' if year else "")
    body = f'<p style="margin:0 0 10px">{quote}</p>' if quote else ""
    n = f'<p class="muted" style="margin:0 0 10px;font-size:.93rem">{note}</p>' if note else ""
    label = linklabel or "Read it &rarr;"
    link = (f'<a href="{url}" target="_blank" rel="noopener">{label}</a>' if url
            else '<span class="muted" style="font-size:.88rem">Print archive &mdash; no live link</span>')
    return (f'      <div class="card">{body}{n}'
            f'<p style="margin:0;font-size:.93rem">{head}<br>{link}</p></div>')


def endorsement(who, quote, note):
    body = f'<p style="margin:0 0 10px">{quote}</p>' if quote else ""
    n = f'<p class="muted" style="margin:0 0 10px;font-size:.93rem">{note}</p>' if note else ""
    return (f'      <div class="card">{body}{n}'
            f'<p style="margin:0;font-size:.93rem"><b>{who}</b></p></div>')


BODY = """
<section class="pagehero">
  <div class="wrap">
    <span class="eyebrow">Press &amp; recognition</span>
    <h1>What has been written about my playing</h1>
    <p class="sub">None of this is my own copy. Every quote below is from the publication named,
      and every link on this page was opened and read in a browser on 21 September 2026 before it was
      allowed to stay. Where a paper has taken its archive offline, the quote stands without a link, or
      points at the Internet Archive&rsquo;s permanent capture &mdash; never at nothing.
      The letters below are scans of the originals: open any of them and read the whole page.</p>
  </div>
</section>

<section class="course">
  <div class="wrap">
    <h2>In the press</h2>
    <div class="grid cols-2" style="margin-top:20px;gap:18px;align-items:start">
__PRESS__
    </div>
  </div>
</section>

<section class="course" style="background:var(--paper)">
  <div class="wrap">
    <h2>What conductors and university faculty have written about me</h2>
    <p class="sub" style="max-width:72ch">These are not quotes I typed out. Each one is a letter on
      the institution&rsquo;s own letterhead, signed. <b>Click any letter to read the whole thing.</b>
      The only marks on them are gray rectangles where a private home address or a direct phone
      number used to be &mdash; mine and theirs. Nothing else has been touched.</p>
    <div class="grid cols-2" style="margin-top:22px;gap:20px;align-items:start">
__LETTERS__
    </div>
  </div>
</section>

<section class="course">
  <div class="wrap">
    <h2>Awards and certificates</h2>
    <p class="sub" style="max-width:72ch">The documents themselves, not a list.</p>
    <div class="grid cols-2" style="margin-top:22px;gap:20px;align-items:start">
__CERTIFICATES__
    </div>
  </div>
</section>

<section class="course">
  <div class="wrap">
    <h2>Radio and television</h2>
    <div class="grid cols-2" style="margin-top:20px;gap:18px;align-items:start">
__BROADCASTS__
    </div>
  </div>
</section>

<section class="course">
  <div class="wrap">
    <h2>Watch me teach</h2>
    <p class="sub" style="max-width:70ch">Anyone can describe their own playing. These are recordings
      of me doing the work &mdash; masterclasses at three universities and a theory class, filmed by
      the schools themselves.</p>
    <div class="grid cols-3" style="margin-top:20px;gap:18px;align-items:start">
__TEACHING__
    </div>

    <h2 style="margin-top:44px">And hear me play</h2>
    <p class="sub" style="max-width:70ch">Concertos with orchestra, solo recitals and chamber music.
      These recordings live on my Las Vegas Piano School channel, where I first published them.</p>
    <div class="grid cols-3" style="margin-top:20px;gap:18px;align-items:start">
__PLAYING__
    </div>
  </div>
</section>

<section class="course">
  <div class="wrap">
    <h2>Prizes, awards and teaching</h2>
    <div class="grid cols-2" style="margin-top:20px;gap:18px;align-items:start">
      <div class="card">
        <h3>Competitions won</h3>
        <ul class="muted" style="padding-left:18px;margin:.4rem 0 0;line-height:1.7">
          <li>2nd Prize &mdash; International Piano Competition in Memory of <b>Sviatoslav Richter</b>,
            Paris, 1997</li>
          <li>2nd Prize &mdash; <b>Fr&eacute;d&eacute;ric Chopin</b> International Competition,
            Rome, 1996</li>
          <li><b>First International Tchaikovsky Youth Competition</b>, Moscow, 1992 &mdash; aged twelve</li>
          <li><b>New Names</b> Charitable Foundation, Moscow, 1992</li>
          <li>Winner &mdash; Reno Chamber Orchestra Concerto Competition, 2010</li>
          <li>Winner &mdash; UNLV Concerto Competition, 2012</li>
          <li>Grand Prix &mdash; Irkutsk Regional Piano Competition, 1990; Governor of the Irkutsk
            Region Award, 1990</li>
        </ul>
      </div>

      <div class="card">
        <h3>Invited to judge</h3>
        <p class="muted" style="margin:.4rem 0 0">Sitting on a jury is the profession&rsquo;s own test
          of a teacher: you are asked because other teachers trust your ear.</p>
        <ul class="muted" style="padding-left:18px;margin:.4rem 0 0;line-height:1.7">
          <li>Northern Nevada Music Teachers Association Reno Piano Festival, 2019</li>
          <li>Irkutsk Regional Piano Competition &mdash; 2010, 2012, 2016</li>
          <li>College of Southern Nevada Piano Concerto Competition, 2012</li>
          <li>National Federation of Music Clubs, 2009</li>
          <li>Silver State Competition, 2007</li>
        </ul>
      </div>

      <div class="card">
        <h3>Masterclasses given</h3>
        <ul class="muted" style="padding-left:18px;margin:.4rem 0 0;line-height:1.7">
          <li>Southern Utah University &mdash; 2012, 2013</li>
          <li>Dixie State University, Utah &mdash; 2013</li>
          <li>College of Southern Nevada &mdash; 2012</li>
          <li>Irkutsk College of Music &mdash; 2014, 2015, 2016</li>
          <li>Angarsk School of Music &mdash; 1997&ndash;2017</li>
          <li>Moscow schools of music &mdash; 1995&ndash;2005</li>
        </ul>
      </div>

      <div class="card">
        <h3>Stages played</h3>
        <p class="muted" style="margin:.4rem 0 0;line-height:1.7">The Royal Academy of Music, London
          &middot; the University of Oxford &middot; the Paris Conservatory &middot; the Santa Cecilia
          Conservatory, Rome &middot; the Benedetto Marcello Conservatory, Venice &middot; the Moscow
          State Conservatory &middot; The Smith Center, Las Vegas &middot; the Irkutsk, Krasnoyarsk,
          Novosibirsk, Kharkov and Zaporozhye philharmonics &middot; Bangkok &middot; Pamukkale,
          Turkey.</p>
      </div>
      <div class="card">
        <h3>Also on file</h3>
        <p class="muted" style="margin:.4rem 0 0">Southern Utah University, on a letter in my file:
          <i>&ldquo;With a career that began with international acclaim at a young age and has
          continued to be successful &hellip; a mature, highly experienced performing artist, [she]
          is an individual that can render the sincere emotion and deep feelings of the
          composers.&rdquo;</i></p>
      </div>

      <div class="card">
        <h3>Teaching and recognition</h3>
        <ul class="muted" style="padding-left:18px;margin:.4rem 0 0;line-height:1.7">
          <li>University faculty &mdash; College of Southern Nevada and Southern Utah University</li>
          <li><b>D.M.A. in Piano Performance</b>, University of Nevada Las Vegas &mdash; and a second
            doctorate, a <b>Ph.D. in Linguistics and English-language teaching</b>, whose dissertation
            was on how children who learn differently are taught. I do not teach in my first
            language by accident; I studied how to do it.</li>
          <li>My own students have placed in the Silver State and Legacy competitions, 2016&ndash;2019</li>
          <li>My students have taken <b>Distinctions</b> in ABRSM examinations and played at the
            ABRSM High Scorers&rsquo; Concert in 2025 and again in 2026 &mdash; the letters are above</li>
          <li>I prepare students for <b>ABRSM</b> (levels 1&ndash;8 and the ARSM, LRSM and FRSM diplomas),
            <b>Trinity College London</b>, the <b>Royal Conservatory of Music</b>, <b>London College of
            Music</b> and the <b>AMEB</b>, and for conservatory entrance examinations</li>
        </ul>
      </div>
    </div>
    <p class="muted" style="margin-top:20px;max-width:70ch">The full account of my training &mdash;
      the Central Music School of the Moscow Conservatory, the Gnessins Academy, the doctorate, and the
      teaching line that runs back to Liszt &mdash; is on the
      <a href="about.html">about page</a>.</p>
  </div>
</section>

<section class="capture-band">
  <div class="wrap">
    <div class="capture">
      <span class="eyebrow" style="color:var(--gold)">Now let me teach you</span>
      <h2>The same training, from your very first note</h2>
      <p style="color:#d7dbe8;max-width:54ch;margin:6px auto 0">Forty-one video lessons, in order, free.
        No sign-up, no catch.</p>
      <p style="margin-top:16px"><a class="btn" href="free-course.html">&#9654; Start the free course</a></p>
    </div>
  </div>
</section>
"""


def main():
    if not SHELL.exists():
        sys.exit("shell page not found: %s" % SHELL)
    t = SHELL.read_text(encoding="utf-8")
    old_title = "Free Piano Course for Adult Beginners — 41 Lessons in Order"
    old_desc = ("Forty-one free piano lessons for adults, in order - reading, chords, pedal, both "
                "hands. The university curriculum Dr. Maria Pisarenko, DMA, teaches at college.")
    for old, new in ((old_title, TITLE + " | Online Piano University"),
                     (old_desc, DESC),
                     ("free-course.html", "press.html")):
        if old not in t:
            sys.exit("anchor not found in the shell: %r" % old[:50])
        t = t.replace(old, new)
    # only the canonical and og:url may become press.html - the nav must keep pointing at the course
    t = t.replace('href="press.html"', 'href="free-course.html"')
    t = t.replace('"https://onlinepianouniversity.com/free-course.html"',
                  '"https://onlinepianouniversity.com/press.html"')
    for k in ('rel="canonical" href="https://onlinepianouniversity.com/free-course.html"',
              'property="og:url" content="https://onlinepianouniversity.com/free-course.html"'):
        t = t.replace(k, k.replace("free-course.html", "press.html"))

    body = (BODY.replace("__PRESS__", "\n".join(card(*p) for p in PRESS))
                .replace("__LETTERS__", "\n".join(letter(*l) for l in LETTERS))
                .replace("__CERTIFICATES__", "\n".join(certificate(*c) for c in CERTIFICATES))
                .replace("__TEACHING__", "\n".join(clip(*c) for c in TEACHING))
                .replace("__PLAYING__", "\n".join(clip(*c) for c in PLAYING))
                .replace("__BROADCASTS__", "\n".join(
                    f'      <div class="card"><p style="margin:0 0 6px"><b>{n}</b></p>'
                    f'<p class="muted" style="margin:0;font-size:.93rem">{d}</p></div>'
                    for n, d in BROADCASTS)))
    # the shell's nav marks Free Course as the current page - this is not that page
    t = t.replace('class="active"', '').replace(' active"', '"').replace('="active ', '="')
    # the blanket free-course.html swap above also hit the footer's own Press link -
    # put it back. (Found by rendering the page and looking at the footer.)
    t = t.replace('<p><a href="free-course.html">Press</a></p>',
                  '<p><a href="press.html">Press</a></p>')
    # the shell's footer already carries the Press link; do not add a second one
    t = re.sub(r'(\n\s*<p><a href="press\.html">Press</a></p>)+',
               '\n      <p><a href="press.html">Press</a></p>', t)

    i = t.index("</header>") + len("</header>")
    j = t.index('<footer id="footer">')
    t = t[:i] + "\n" + body.strip() + "\n\n" + t[j:]
    OUT.write_text(t, encoding="utf-8")
    print("wrote", OUT.name, OUT.stat().st_size, "bytes")


if __name__ == "__main__":
    main()
