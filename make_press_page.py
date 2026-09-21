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
LINKS_VERIFIED = "2026-09-21"

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
      points at the Internet Archive&rsquo;s permanent capture &mdash; never at nothing.</p>
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
    <h2>Letters, citations and awards</h2>
    <p class="muted" style="max-width:70ch;margin:.4rem 0 0">These are not newspaper articles. They
      are written by the institutions themselves and are held in my file.</p>
    <div class="grid cols-2" style="margin-top:20px;gap:18px;align-items:start">
__ENDORSEMENTS__
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
    <h2>Prizes, awards and teaching</h2>
    <div class="grid cols-2" style="margin-top:20px;gap:18px;align-items:start">
      <div class="card">
        <h3>International competitions</h3>
        <ul class="muted" style="padding-left:18px;margin:.4rem 0 0;line-height:1.7">
          <li>2nd Prize &mdash; International Piano Competition in Memory of <b>Sviatoslav Richter</b>, Paris</li>
          <li>2nd Prize &mdash; <b>Fr&eacute;d&eacute;ric Chopin</b> International Competition, Rome</li>
          <li><b>First International Tchaikovsky Youth Competition</b>, Moscow</li>
          <li>Winner &mdash; Reno Chamber Orchestra College Concerto Competition</li>
          <li>Winner &mdash; UNLV Concerto Competition</li>
        </ul>
      </div>
      <div class="card">
        <h3>Teaching and recognition</h3>
        <ul class="muted" style="padding-left:18px;margin:.4rem 0 0;line-height:1.7">
          <li>University faculty &mdash; College of Southern Nevada and Southern Utah University</li>
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
                .replace("__ENDORSEMENTS__", "\n".join(endorsement(*e) for e in ENDORSEMENTS))
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
