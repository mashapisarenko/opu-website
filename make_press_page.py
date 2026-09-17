# -*- coding: utf-8 -*-
"""Builds /press.html - what has been written and broadcast about her.

Source: her own CV (Dr.MPisarenkoPianistCVOct2019.docx.pdf) plus her bio document.
EVERY external link below was fetched and confirmed live on 2026-09-17. Two items she
lists in the CV are quoted WITHOUT a link, on purpose:
  - Salt Lake Tribune: entertainment.sltrib.com no longer resolves at all.
  - Las Vegas Sun, 16 Feb 2009: the page answers 402 and could not be confirmed.
Nothing here is paraphrased or improved. A quote that could not be verified is not on
the page - per her standing rule, never invent a fact, a price, a date or a page number.

Same discipline as make_first_piece_page.py: cloned from a LIVE page so the head,
analytics, nav, footer and CSS cannot drift.

Run from opu-website/:  python3 make_press_page.py
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
SHELL = HERE / "free-course.html"
OUT = HERE / "press.html"

TITLE = "Press & Recognition - Dr. Maria Pisarenko, Concert Pianist"
DESC = ("What the press has written about concert pianist Dr. Maria Pisarenko, DMA - the Las Vegas "
        "Review-Journal, the Las Vegas Sun, This Is Reno, the Salt Lake Tribune - plus radio and "
        "television broadcasts, competition prizes and the Steinway Top Teacher Award.")

# (publication, year, url or None, quote or None, note or None)
PRESS = [
 ("Las Vegas Review-Journal", "2019",
  "https://www.reviewjournal.com/local/summerlin/las-vegas-musician-began-playing-piano-at-5-in-siberia-1685788/",
  "&ldquo;Music is language, and language is music,&rdquo; she said. &ldquo;They reflect history, "
  "traditions, beliefs. It helps us open our minds to new ideas, new ways of looking at the world.&rdquo;",
  "Feature: <i>Las Vegas musician began playing piano at 5 &mdash; in Siberia</i>"),
 ("Clark County, Nevada", "2019",
  "https://www.clarkcountynv.gov/public-communications/news/Pages/Russian-Seasons-in-Las-Vegas-Feb--9.aspx",
  "&ldquo;Dr. Maria (Masha) Pisarenko is actively involved in the cultural life &hellip; as a performer, "
  "educator and artistic director. She has performed on some of the most prestigious stages of the world, "
  "including in Russia, Asia, Europe, and the United States.&rdquo;", None),
 ("Salt Lake Tribune", None, None,
  "&ldquo;The Siberian-born artist has performed throughout Europe, and has won various competitions "
  "before coming to the United States. She has been a featured performer on Nevada Public Radio and a "
  "guest soloist with numerous orchestras.&rdquo;", None),
 ("Southern Utah University", None, None,
  "&ldquo;With a career that began with international acclaim at a young age and has continued to be "
  "successful &hellip; a mature, highly experienced performing artist, [she] is an individual that can "
  "render the sincere emotion and deep feelings of the composers.&rdquo;", None),
 ("This Is Reno", "2010",
  "https://thisisreno.com/2010/02/pianist-maria-pisarenko-wins-reno-chamber-orchestra-college-concerto-competition/",
  None,
  "<i>Pianist Maria Pisarenko wins Reno Chamber Orchestra College Concerto Competition</i> &mdash; "
  "the prize was to appear as featured soloist with the orchestra."),
 # This quote is NOT in the CV - it was taken from the Las Vegas Sun article itself,
 # fetched and read on 2026-09-17. Verbatim from the piece, not paraphrased.
 ("Las Vegas Sun", "2008",
  "https://lasvegassun.com/news/2008/sep/17/intimate-masterful-and-free/",
  "&ldquo;Siberian-born Pisarenko trained at the Russian Academy of Music and performed in Europe "
  "before moving to the States.&rdquo;",
  "<i>Intimate, masterful and free</i>"),
 ("Las Vegas Review-Journal", "2019",
  "https://neon.reviewjournal.com/music/russian-seasons-to-perform-next-month-in-las-vegas-1584818/",
  None,
  "<i>Russian Seasons to perform next month</i> &mdash; a program of Russian chamber and vocal "
  "music she presented and played."),
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


def card(pub, year, url, quote, note):
    head = f"<b>{pub}</b>" + (f' <span class="muted">&middot; {year}</span>' if year else "")
    body = f'<p style="margin:0 0 10px">{quote}</p>' if quote else ""
    n = f'<p class="muted" style="margin:0 0 10px;font-size:.93rem">{note}</p>' if note else ""
    link = (f'<a href="{url}" target="_blank" rel="noopener">Read it &rarr;</a>' if url
            else '<span class="muted" style="font-size:.88rem">Print archive &mdash; no live link</span>')
    return (f'      <div class="card">{body}{n}'
            f'<p style="margin:0;font-size:.93rem">{head}<br>{link}</p></div>')


BODY = """
<section class="pagehero">
  <div class="wrap">
    <span class="eyebrow">Press &amp; recognition</span>
    <h1>What has been written about my playing</h1>
    <p class="sub">Every quote below is from the publication named, and every link was checked before
      it went on this page. Where a paper&rsquo;s archive has gone offline the quote stands without a
      link rather than pointing at nothing.</p>
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
          <li><b>Steinway Top Teacher Award</b></li>
          <li>Southern Nevada Musical Arts Society &mdash; <i>&ldquo;In recognition of your graciously
            sharing your musical artistry&rdquo;</i></li>
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
    old_title = "Free University Piano Course for Beginners — Online Piano University"
    old_desc = ("The complete beginner piano course, in order, free — the same university curriculum "
                "Dr. Maria Pisarenko (DMA) teaches at colleges. 41 lessons on YouTube: reading music, "
                "chords, pedal, both hands.")
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
