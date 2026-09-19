#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Builds /first-piece.html — the landing page for the giveaway sheet.

Same discipline as blog/_make_post.py: the page is cloned from a LIVE page
(free-course.html) so the head, analytics, nav, footer and scripts can never
drift from the rest of the site. Only the metadata and the body between
</header> and <footer> are replaced.

Run from opu-website/:  python3 make_first_piece_page.py
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
SHELL = HERE / "free-course.html"
OUT = HERE / "first-piece.html"
SITE = "https://onlinepianouniversity.com"

TITLE = "Your First Piece, Free — Play Ode to Joy by Ear Today"
DESC = ("One page from an adult piano method: the opening of Ode to Joy by ear, five fingers that never move, nothing to decode. Free from a concert pianist.")

BODY = """
<section class="pagehero">
  <div class="wrap">
    <span class="eyebrow">Free &middot; one page from the method</span>
    <h1>Play your first real piece today &mdash; by ear</h1>
    <p class="sub">Most piano books put a month of reading between you and anything that sounds like
      music. This is the page that comes first in mine: the opening of Beethoven&rsquo;s
      <em>Ode to Joy</em>, five fingers that never move, and nothing on the sheet to decode.</p>
  </div>
</section>

<section class="course">
  <div class="wrap">
    <div class="grid cols-2" style="align-items:start;gap:28px">
      <div>
        <h2>What you get</h2>
        <ul style="line-height:1.7;margin-top:10px">
          <li><strong>The sheet</strong> &mdash; one page, print it or keep it on a tablet.</li>
          <li><strong>The hand position</strong>, shown on a keyboard diagram: how to find it in
            about ten seconds, on any piano.</li>
          <li><strong>The tune in four short phrases</strong> &mdash; the letter is the key, the small
            number is the finger. No staff, no clef, nothing to look up.</li>
          <li><strong>Four steps</strong> that decide whether it sounds like music or like typing.</li>
          <li><strong>What to do when it sounds wrong</strong> &mdash; and it is almost never your ear.</li>
        </ul>
        <p class="muted" style="margin-top:14px">It is genuinely one page. You can be playing in the
          time it takes to read it.</p>
      </div>
      <div>
        <h2>Why by ear, and why first</h2>
        <p style="margin-top:10px">I was trained in the Russian school, where a child plays for months
          before meeting a printed note. The reason is not tradition. It is that the ear has to lead the
          hand, and if reading comes first the hand learns to obey the page instead of the sound.</p>
        <p>Adults are almost never taught this way, and it is the single biggest difference I hear
          between someone who plays and someone who presses the right keys.</p>
        <p>You already know how this tune goes. That is the whole advantage, and this page spends it.</p>
      </div>
    </div>
  </div>
</section>

<section style="padding-bottom:0">
  <div class="wrap">
    <div class="capture">
      <span class="eyebrow" style="color:var(--gold)">Free download</span>
      <h2>Send it to me</h2>
      <p style="color:#d7dbe8;max-width:52ch;margin:6px auto 0">Your first piece, by ear &mdash; one page,
        free. You will also get the occasional letter from me about learning the piano as an adult.</p>
      <form class="opu-capture" data-download="downloads/OPU_Your_First_Piece.pdf"
            data-filename="Your_First_Piece_by_Dr_Maria_Pisarenko.pdf">
        <input type="email" name="email_address" placeholder="Your email" required aria-label="Your email">
        <button class="btn" type="submit">Send me the piece</button>
      </form>
      <p class="form-ok">&#10003; Thank you &mdash; check your inbox!</p>
      <p class="note">No spam &mdash; just piano. Unsubscribe anytime.</p>
    </div>
  </div>
</section>

<section class="course">
  <div class="wrap">
    <span class="eyebrow">Who is teaching you</span>
    <h2>Dr. Maria Pisarenko</h2>
    <p style="max-width:66ch;margin-top:10px">Doctor of Musical Arts, concert pianist and international
      competition laureate, trained at the Moscow school and the Gnessin Academy, doctorate in the
      United States. I teach piano at university level and privately, and I write for adults who are
      learning on their own.</p>
    <div class="grid cols-2" style="margin-top:20px;gap:18px">
      <div class="card">
        <h3>The free course</h3>
        <p class="muted">Forty-one video lessons, in order, from the first sound to reading with both
          hands. Free on YouTube, no sign-up.</p>
        <a class="btn dark" href="https://www.youtube.com/playlist?list=PLmHakdUcQbtSHDPhBQL8DLmiiKe3CsRzM"
           target="_blank" rel="noopener">Start at Lesson 1 &rarr;</a>
      </div>
      <div class="card">
        <h3>Send me your playing</h3>
        <p class="muted">Record a few minutes and I will write you back about what I actually hear &mdash;
          the specific thing, where it happens, and what to do. Free while the pilot runs.</p>
        <a class="btn dark" href="submit.html">Send a recording &rarr;</a>
      </div>
    </div>
  </div>
</section>
"""


def main():
    if not SHELL.exists():
        sys.exit("shell page not found: %s" % SHELL)
    t = SHELL.read_text(encoding="utf-8")

    old_title = ("Free Piano Course for Adult Beginners — 41 Lessons in Order")
    old_desc = ("Forty-one free piano lessons for adults, in order - reading, chords, pedal, both "
                "hands. The university curriculum Dr. Maria Pisarenko, DMA, teaches at college.")
    for old, new in ((old_title, TITLE + " | Online Piano University"),
                     (old_desc, DESC)):
        if old not in t:
            sys.exit("anchor not found in the shell: %r" % old[:50])
        t = t.replace(old, new)

    # ONLY the canonical and og:url change page. Replacing every occurrence of
    # "free-course.html" also rewrites the nav link and the footer link, which
    # pointed the whole site's "Free Course" menu item at this page (found and
    # fixed 2026-09-15, by looking at the rendered page).
    t = t.replace('<meta property="og:url" content="%s/free-course.html">' % SITE,
                  '<meta property="og:url" content="%s/first-piece.html">' % SITE)
    t = t.replace('<link rel="canonical" href="%s/free-course.html">' % SITE,
                  '<link rel="canonical" href="%s/first-piece.html">' % SITE)
    # the nav must not mark Free Course as the current page here
    t = t.replace('<a href="free-course.html" class="active">', '<a href="free-course.html">')
    if '"%s/first-piece.html"' % SITE not in t:
        sys.exit("canonical was not rewritten - the shell's head markup changed")

    # swap the body between </header> and <footer
    i, j = t.index("</header>") + len("</header>"), t.index('<footer id="footer">')
    t = t[:i] + "\n" + BODY.strip() + "\n\n" + t[j:]

    OUT.write_text(t, encoding="utf-8")
    print("wrote", OUT.name, OUT.stat().st_size, "bytes")


if __name__ == "__main__":
    main()
