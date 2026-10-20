#!/usr/bin/env python3
"""Keeps live articles free of links to articles that are not published yet.

When articles are re-dated (the ten adult-motive articles of 2026-10-18 moved from
February to October), their bodies can link to articles that are still waiting in the
queue - a 404 for a reader. This pass, run on every publish, turns such a link into
<span data-link-pending="slug">text</span>, and turns it back into the real link on the
day the target article is published. Nothing is lost; no link ever points at a 404.
Run directly to apply now:  python3 blog/_pending_links.py
"""
import re, pathlib

HERE = pathlib.Path(__file__).resolve().parent
LINK = re.compile(r'<a href="([a-z0-9-]+)\.html">(.*?)</a>', re.S)
PENDING = re.compile(r'<span data-link-pending="([a-z0-9-]+)">(.*?)</span>', re.S)


def main():
    live = {p.stem for p in HERE.glob("*.html")}
    queued = {p.stem for p in (HERE / "_queue").glob("*.html")}
    changed = 0
    for p in sorted(HERE.glob("*.html")):
        if p.name == "index.html":
            continue
        t = p.read_text(encoding="utf-8")
        n = LINK.sub(lambda m: m.group(0) if (m.group(1) in live or m.group(1) not in queued)
                     else '<span data-link-pending="%s">%s</span>' % (m.group(1), m.group(2)), t)
        n = PENDING.sub(lambda m: '<a href="%s.html">%s</a>' % (m.group(1), m.group(2))
                        if m.group(1) in live else m.group(0), n)
        if n != t:
            p.write_text(n, encoding="utf-8")
            changed += 1
            print("pending links updated:", p.name)
    print("pending links: %d live article(s) updated" % changed)


if __name__ == "__main__":
    main()
