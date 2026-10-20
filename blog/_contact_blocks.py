#!/usr/bin/env python3
"""Puts the standard three contact/feedback forms (top, middle, bottom) into a blog article.

Masha's standing rule (2026-10-13): every OPU page carries the contact/submission
form three times. Articles queued before that rule existed were built without the
blocks, and every one of them went live without them. This module copies the exact
blocks from the article template and inserts them where they sit in every other
article. It is idempotent: an article that already has the blocks is left alone.

Used by _make_post.py (new articles) and _publish.py (safety net on publish).
Run directly to fix every live and queued article:  python3 blog/_contact_blocks.py
"""
import re, sys, pathlib

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "russian-school-vs-american-piano-method.html"

_PATS = {
    "top": r'<!--opu-top-->.*?<!--/opu-top-->',
    "mid": r'<!--opu-mid-->.*?<!--/opu-mid-->',
    "ages": r'<!--opu-ages-->.*?</section>',
    "bottom": r'<section class="contactfull" data-opu="contact-bottom">.*?</section>',
}
SCRIPT = '<script src="../js/opu-form.js" defer></script>'


def _blocks():
    t = SOURCE.read_text(encoding="utf-8")
    out = {}
    for k, p in _PATS.items():
        m = re.search(p, t, re.S)
        if not m:
            sys.exit("contact blocks: %s block missing from %s" % (k, SOURCE.name))
        out[k] = m.group(0)
    return out


def ensure(text, blocks=None):
    """Return the article with all three forms present. Raises ValueError if an anchor is missing."""
    b = blocks or _blocks()
    if 'data-opu="contact-top"' not in text:
        if "</header>\n" not in text:
            raise ValueError("no </header> anchor")
        text = text.replace("</header>\n", "</header>\n" + b["top"], 1)
    if 'data-opu="contact-mid"' not in text:
        anchor = '</section>\n\n<section class="section" style="padding-top:0">\n  <div class="wrap">\n    <div class="capture">'
        if anchor not in text:
            raise ValueError("no anchor for the middle form")
        text = text.replace(anchor, '</section>' + b["mid"] + anchor[len('</section>\n'):], 1)
    tail = ""
    if 'data-opu="age-links-auto"' not in text:
        tail += b["ages"] + "\n"
    if 'data-opu="contact-bottom"' not in text:
        tail += b["bottom"] + "\n"
    if SCRIPT not in text:
        tail += SCRIPT + "\n"
    if tail:
        if '<footer id="footer">' not in text:
            raise ValueError("no footer anchor")
        text = text.replace('<footer id="footer">', tail + '<footer id="footer">', 1)
    return text


def main():
    b = _blocks()
    files = sorted(HERE.glob("*.html")) + sorted((HERE / "_queue").glob("*.html"))
    changed = 0
    for f in files:
        if f.name == "index.html":
            continue
        t = f.read_text(encoding="utf-8")
        n = ensure(t, b)
        if n != t:
            f.write_text(n, encoding="utf-8")
            changed += 1
            print("forms added:", f.relative_to(HERE))
    print("contact forms: %d article(s) updated" % changed)


if __name__ == "__main__":
    main()
