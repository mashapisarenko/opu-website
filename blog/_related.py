# -*- coding: utf-8 -*-
"""'Read next' - internal links between articles.

Why this exists: on 2026-09-17 an audit found that not one of the fourteen live
articles linked to any other article. Every one of them was a dead end for a reader
and an orphan for a search engine. Internal linking between related pages is one of
the few on-site things that measurably moves ranking, and it was entirely absent.

The map is hand-made, not computed from keywords: each article points at the three
a real reader would want next. TITLES are pulled live from the files and the queue
manifest, so a title can never go stale here.

Run:  python3 blog/_related.py          (from opu-website/)
"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
QUEUE = HERE / "_queue"

RELATED = {
 # --- reading music ---
 "how-to-read-sheet-music-treble-clef-rhythm": ["what-the-treble-clef-means", "how-to-read-piano-notes-grand-staff", "how-to-count-music-out-loud"],
 "what-the-treble-clef-means": ["how-to-read-piano-notes-grand-staff", "how-to-read-the-bass-clef", "how-to-read-sheet-music-treble-clef-rhythm"],
 "how-to-read-piano-notes-grand-staff": ["how-to-read-the-bass-clef", "what-the-treble-clef-means", "how-to-find-any-note-on-the-piano"],
 "how-to-read-the-bass-clef": ["how-to-read-piano-notes-grand-staff", "what-the-treble-clef-means", "reading-music-or-playing-by-ear"],
 "how-to-count-music-out-loud": ["how-to-read-sheet-music-treble-clef-rhythm", "right-notes-still-sounds-wrong", "how-to-practice-piano-a-method-not-more-minutes"],
 "how-to-find-any-note-on-the-piano": ["how-to-read-piano-notes-grand-staff", "piano-hand-position-curved-fingers", "how-to-read-sheet-music-treble-clef-rhythm"],
 "reading-music-or-playing-by-ear": ["what-european-music-schools-teach-that-american-adults-missed", "how-to-read-sheet-music-treble-clef-rhythm", "russian-school-vs-american-piano-method"],
 # --- the body ---
 "piano-hand-position-curved-fingers": ["why-your-hands-get-tense-at-the-piano", "piano-wrist-position-adults", "piano-bench-height-posture"],
 "why-your-hands-get-tense-at-the-piano": ["piano-wrist-position-adults", "does-piano-playing-hurt-hands", "piano-hand-position-curved-fingers"],
 "piano-wrist-position-adults": ["piano-hand-position-curved-fingers", "why-your-hands-get-tense-at-the-piano", "piano-bench-height-posture"],
 "piano-bench-height-posture": ["piano-wrist-position-adults", "piano-hand-position-curved-fingers", "why-your-hands-get-tense-at-the-piano"],
 "does-piano-playing-hurt-hands": ["why-your-hands-get-tense-at-the-piano", "piano-wrist-position-adults", "piano-bench-height-posture"],
 # --- practice ---
 "how-to-practice-piano-a-method-not-more-minutes": ["practicing-piano-when-you-have-no-time", "how-long-to-practice-piano-each-day", "run-your-own-piano-lesson"],
 "how-long-to-practice-piano-each-day": ["how-to-practice-piano-a-method-not-more-minutes", "why-adult-beginners-quit-piano", "practicing-piano-when-you-have-no-time", "piano-plateau-month-four"],
 "practicing-piano-when-you-have-no-time": ["how-to-practice-piano-a-method-not-more-minutes", "how-long-to-practice-piano-each-day", "run-your-own-piano-lesson"],
 "run-your-own-piano-lesson": ["learning-piano-without-a-teacher", "how-to-practice-piano-a-method-not-more-minutes", "how-to-choose-a-piano-teacher"],
 "piano-plateau-month-four": ["why-adult-beginners-quit-piano", "how-long-to-learn-piano-adult", "how-to-practice-piano-a-method-not-more-minutes"],
 # --- the adult learner ---
 "is-it-too-late-to-learn-piano-at-40-50-60": ["why-adults-learn-piano-your-reason-matters", "why-adult-beginners-quit-piano", "learning-piano-after-70", "adults-learn-piano-differently"],
 "learning-piano-after-70": ["is-it-too-late-to-learn-piano-at-40-50-60", "adults-learn-piano-differently", "does-piano-playing-hurt-hands"],
 "adults-learn-piano-differently": ["is-it-too-late-to-learn-piano-at-40-50-60", "what-european-music-schools-teach-that-american-adults-missed", "learning-piano-without-a-teacher"],
 "why-adults-learn-piano-your-reason-matters": ["is-it-too-late-to-learn-piano-at-40-50-60", "returning-to-piano-as-an-adult", "how-to-practice-piano-a-method-not-more-minutes"],
 "returning-to-piano-as-an-adult": ["why-adults-learn-piano-your-reason-matters", "adults-learn-piano-differently", "piano-plateau-month-four"],
 "why-adult-beginners-quit-piano": ["piano-plateau-month-four", "practicing-piano-when-you-have-no-time", "how-long-to-learn-piano-adult"],
 "how-long-to-learn-piano-adult": ["piano-plateau-month-four", "how-to-practice-piano-a-method-not-more-minutes", "why-adult-beginners-quit-piano"],
 "playing-piano-for-other-people": ["piano-plateau-month-four", "why-your-hands-get-tense-at-the-piano", "how-to-practice-piano-a-method-not-more-minutes"],
 # --- teaching, method, gear ---
 "learning-piano-without-a-teacher": ["run-your-own-piano-lesson", "how-to-choose-a-piano-teacher", "right-notes-still-sounds-wrong"],
 "how-to-choose-a-piano-teacher": ["learning-piano-without-a-teacher", "run-your-own-piano-lesson", "russian-school-vs-american-piano-method"],
 "russian-school-vs-american-piano-method": ["what-european-music-schools-teach-that-american-adults-missed", "right-notes-still-sounds-wrong", "reading-music-or-playing-by-ear"],
 "what-european-music-schools-teach-that-american-adults-missed": ["russian-school-vs-american-piano-method", "reading-music-or-playing-by-ear", "adults-learn-piano-differently"],
 "right-notes-still-sounds-wrong": ["russian-school-vs-american-piano-method", "how-to-count-music-out-loud", "why-your-hands-get-tense-at-the-piano"],
 "digital-piano-vs-acoustic-beginner": ["how-many-keys-do-i-need-piano", "piano-bench-height-posture", "is-it-too-late-to-learn-piano-at-40-50-60"],
 "how-many-keys-do-i-need-piano": ["digital-piano-vs-acoustic-beginner", "piano-bench-height-posture", "how-to-find-any-note-on-the-piano"],
}

ANCHOR = '<aside class="card" style="display:flex;gap:16px;align-items:center;margin:34px 0 0;padding:18px 20px">'
MARK = "<!-- read-next -->"


def titles():
    """slug -> (title, live?) taken from the real files and the real queue."""
    out = {}
    for p in HERE.glob("*.html"):
        if p.name == "index.html":
            continue
        m = re.search(r"<h1[^>]*>(.*?)</h1>", p.read_text(encoding="utf-8", errors="replace"), re.S)
        if m:
            out[p.stem] = (re.sub(r"<[^>]+>", "", m.group(1)).strip(), True)
    man = QUEUE / "manifest.json"
    if man.exists():
        for a in json.loads(man.read_text(encoding="utf-8")):
            out.setdefault(a["slug"], (a["title"], False))
    return out


def block(slug, T, from_queue):
    """The read-next markup.

    ONLY LIVE ARTICLES may be linked. A live page that links a queued one is a 404 on
    her site - which is exactly what the first version of this script produced, and the
    morning check caught it. _publish.py re-runs this after every publish, so a queued
    article joins the web the day it goes live and nothing is lost by waiting.

    If fewer than three of an article's own picks are live, it is topped up from the
    articles that name IT as related - a real relation, not a filler link."""
    live_only = {s for s, (_, is_live) in T.items() if is_live}
    cand = list(RELATED.get(slug, []))
    cand += [s for s, rel in RELATED.items() if slug in rel and s not in cand]
    seen, picks = set(), []
    for s in cand:
        if s != slug and s in live_only and s not in seen:
            seen.add(s); picks.append(s)
    picks = picks[:3]
    if not picks:
        return ""
    pre = "" if from_queue else ""
    li = "\n".join(
        f'    <li style="margin:0 0 8px"><a href="{pre}{s}.html">{T[s][0]}</a></li>' for s in picks)
    return (f'{MARK}\n<div class="card" style="margin:34px 0 0;padding:18px 20px">\n'
            f'  <p style="margin:0 0 10px;font-weight:600">Read next</p>\n'
            f'  <ul style="margin:0;padding-left:20px">\n{li}\n  </ul>\n</div>\n')


def apply_to(path, slug, T, from_queue):
    """Insert before the author card when there is one; otherwise before </article>.
    Not every article carries the author aside, and two live ones did not - which is
    exactly the kind of thing that makes a 'it worked' report untrue."""
    t = path.read_text(encoding="utf-8")
    t = re.sub(re.escape(MARK) + r".*?</div>\n", "", t, flags=re.S)   # idempotent
    t = t.replace("<!-- read-next: nothing live to link yet; _publish.py rebuilds this -->\n", "")
    b = block(slug, T, from_queue)
    if not b:
        # No live article to point at yet. Write the CLEANED text anyway, or a stale
        # block from an earlier run survives and keeps pointing at an unpublished page.
        # Leave a marker so the morning check knows this is waiting, not forgotten.
        note = "<!-- read-next: nothing live to link yet; _publish.py rebuilds this -->\n"
        if note not in t:
            for anchor in (ANCHOR, "    </article>", "</article>"):
                if anchor in t:
                    t = t.replace(anchor, note + anchor, 1)
                    break
        path.write_text(t, encoding="utf-8")
        return False
    for anchor in (ANCHOR, "    </article>", "</article>"):
        if anchor in t:
            path.write_text(t.replace(anchor, b + "\n" + anchor, 1), encoding="utf-8")
            return True
    return False


def main():
    T = titles()
    n = 0
    for p in sorted(HERE.glob("*.html")):
        if p.name != "index.html" and apply_to(p, p.stem, T, False):
            n += 1
    q = 0
    for p in sorted(QUEUE.glob("*.html")):
        if apply_to(p, p.stem, T, True):
            q += 1
    missing = sorted(s for s in T if s not in RELATED)
    print(f"read-next added to {n} live article(s) and {q} queued article(s)")
    if missing:
        print("NO MAP ENTRY (fix before they publish):", ", ".join(missing))
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
