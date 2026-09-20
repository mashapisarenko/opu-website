# -*- coding: utf-8 -*-
"""Rewrites sitemap.xml: one entry per URL, and lastmod taken from git.

Why this exists. On 2026-09-20 an audit found that 27 of the 28 entries carried
lastmod 2026-09-09 while the pages themselves had been rewritten on the 19th -
including every page whose title had just changed. lastmod is the hint a search
engine uses to decide what to re-crawl, so the sitemap was actively telling Google
that the newly rewritten pages were eleven days stale. It also found the home page
listed twice, identically.

lastmod comes from `git log -1 --format=%cs` for the file, so it can never be a
guess. Pages that are noindex, and 404.html, stay out.

Run from opu-website/:  python3 refresh_sitemap.py
"""
import pathlib, re, subprocess, sys, datetime

HERE = pathlib.Path(__file__).resolve().parent
SITE = "https://onlinepianouniversity.com"
SKIP = {"404.html", "studio.html", "googleed832eccb886831b.html"}

PRIORITY = {"": ("weekly", "1.0"), "free-course.html": ("monthly", "0.9"),
            "first-piece.html": ("monthly", "0.9"), "lessons.html": ("monthly", "0.9"),
            "submit.html": ("monthly", "0.8"), "blog/": ("weekly", "0.8")}
DEFAULT = ("monthly", "0.7")


def git_date(path):
    try:
        d = subprocess.run(["git", "log", "-1", "--format=%cs", "--", str(path)],
                           cwd=HERE, capture_output=True, text=True, timeout=20).stdout.strip()
    except Exception:
        d = ""
    if not d:
        d = datetime.date.fromtimestamp(path.stat().st_mtime).isoformat()
    return d


def indexable(p):
    t = p.read_text(encoding="utf-8", errors="replace")
    return "noindex" not in t


def main():
    entries = []
    for p in sorted(HERE.glob("*.html")):
        if p.name in SKIP or not indexable(p):
            continue
        rel = "" if p.name == "index.html" else p.name
        entries.append((rel, git_date(p)))
    blog_index = HERE / "blog" / "index.html"
    if blog_index.exists():
        entries.append(("blog/", git_date(blog_index)))
    for p in sorted((HERE / "blog").glob("*.html")):
        if p.name == "index.html" or not indexable(p):
            continue
        entries.append(("blog/" + p.name, git_date(p)))

    seen, rows = set(), []
    for rel, lm in entries:
        loc = f"{SITE}/{rel}"
        if loc in seen:
            continue
        seen.add(loc)
        cf, pr = PRIORITY.get(rel, DEFAULT)
        rows.append(f"  <url><loc>{loc}</loc>\n"
                    f"    <lastmod>{lm}</lastmod><changefreq>{cf}</changefreq>"
                    f"<priority>{pr}</priority></url>")

    out = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + "\n".join(rows) + "\n</urlset>\n")
    (HERE / "sitemap.xml").write_text(out, encoding="utf-8")
    print(f"sitemap.xml: {len(rows)} URL(s), lastmod from git, no duplicates")


if __name__ == "__main__":
    sys.exit(main())
