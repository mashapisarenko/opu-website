#!/usr/bin/env python3
"""
Publishes queued blog posts on their date, with no one at the keyboard.

A finished article waits in blog/_queue/<slug>.html together with a line in
blog/_queue/manifest.json.  On or after its date this script moves it into
blog/, adds its card to the blog index, its entry to the index's JSON-LD and
its URL to the sitemap, and takes it out of the queue.  Nothing is invented
here: every word of an article is written and checked before it is queued.

Run by .github/workflows/publish-blog.yml once a day.  Safe to run any number
of times: a post already published is simply no longer in the manifest.
"""
import sys
import json, re, sys, datetime, shutil, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent   # opu-website/
BLOG = ROOT / "blog"
QUEUE = BLOG / "_queue"
MANIFEST = QUEUE / "manifest.json"
INDEX = BLOG / "index.html"
SITEMAP = ROOT / "sitemap.xml"
SITE = "https://onlinepianouniversity.com"

# Las Vegas time: the day turns over for her, not for a server in Virginia.
TODAY = (datetime.datetime.now(datetime.timezone.utc)
         - datetime.timedelta(hours=7)).date()

MONTHS = ("January February March April May June July August September "
          "October November December").split()


def human(d):
    return "%s %d, %d" % (MONTHS[d.month - 1], d.day, d.year)


def esc(t):
    """Make a title safe inside HTML without mangling entities already in it."""
    t = re.sub(r"&(?!#?\w+;)", "&amp;", t)
    return t.replace("<", "&lt;").replace(">", "&gt;")


def card(entry, d):
    return (
        '      <a class="card" href="%s.html" style="display:block;'
        'text-decoration:none;margin-bottom:18px;padding:22px 24px">\n'
        '        <p class="eyebrow" style="margin:0 0 6px;color:#5b6478">%s</p>\n'
        '        <h3 style="margin:0 0 8px">%s</h3>\n'
        '        <p style="margin:0;color:#3d4557">%s</p>\n'
        '        <p style="margin:12px 0 0;font-weight:600">Read the article &rarr;</p>\n'
        '      </a>\n' % (entry["slug"], human(d), esc(entry["title"]), esc(entry["summary"])))


def jsonld(entry, d):
    return (
        '    {\n'
        '      "@type": "BlogPosting",\n'
        '      "headline": %s,\n'
        '      "url": "%s/blog/%s.html",\n'
        '      "datePublished": "%s",\n'
        '      "author": {\n'
        '        "@id": "%s/#maria"\n'
        '      }\n'
        '    },\n' % (json.dumps(entry["title"], ensure_ascii=False),
                      SITE, entry["slug"], d.isoformat(), SITE))


def sitemap_row(entry, d):
    return ('  <url><loc>%s/blog/%s.html</loc>\n'
            '    <lastmod>%s</lastmod><changefreq>yearly</changefreq>'
            '<priority>0.6</priority></url>\n' % (SITE, entry["slug"], d.isoformat()))


def insert_after(text, anchor, addition, what):
    i = text.find(anchor)
    if i < 0:
        sys.exit("could not find the %s anchor - publishing stopped, nothing changed" % what)
    i += len(anchor)
    return text[:i] + addition + text[i:]


def add_to_sitemap(sitemap, entry, d):
    """Refresh the blog index row's lastmod and put the new row right after it.
    Matched on the blog index block itself, never on a bare priority line -
    several pages share priority 0.8."""
    m = re.search(r'  <url><loc>%s/blog/</loc>\n    <lastmod>\d{4}-\d{2}-\d{2}</lastmod>'
                  r'[^\n]*\n' % re.escape(SITE), sitemap)
    if not m:
        sys.exit("could not find the blog index row in the sitemap - nothing changed")
    refreshed = re.sub(r'<lastmod>\d{4}-\d{2}-\d{2}</lastmod>',
                       '<lastmod>%s</lastmod>' % d.isoformat(), m.group(0), count=1)
    return sitemap[:m.start()] + refreshed + sitemap_row(entry, d) + sitemap[m.end():]


def main():
    if not MANIFEST.exists():
        print("no queue manifest - nothing to publish")
        return 0
    queue = json.loads(MANIFEST.read_text(encoding="utf-8"))
    due, keep = [], []
    for e in queue:
        d = datetime.date.fromisoformat(e["date"])
        (due if d <= TODAY else keep).append((e, d))

    if not due:
        print("nothing due today (%s); %d article(s) still waiting" % (TODAY, len(keep)))
        return 0

    index = INDEX.read_text(encoding="utf-8")
    sitemap = SITEMAP.read_text(encoding="utf-8")
    published = []

    for e, d in sorted(due, key=lambda x: x[1]):
        src = QUEUE / (e["slug"] + ".html")
        dst = BLOG / (e["slug"] + ".html")
        if dst.exists():
            print("already published, skipping: %s" % dst.name)
            published.append(e["slug"])
            continue
        if not src.exists():
            sys.exit("queued article missing on disk: %s" % src.name)
        shutil.move(str(src), str(dst))
        index = insert_after(index, '<div style="margin-top:30px">\n', card(e, d), "card list")
        index = insert_after(index, '"blogPost": [\n', jsonld(e, d), "JSON-LD list")
        sitemap = add_to_sitemap(sitemap, e, d)
        published.append(e["slug"])
        print("published: %s  (%s)" % (e["slug"], d.isoformat()))

    INDEX.write_text(index, encoding="utf-8")
    SITEMAP.write_text(sitemap, encoding="utf-8")
    MANIFEST.write_text(json.dumps([e for e, _ in keep], indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8")
    # Rebuild the "Read next" blocks so a newly published article is linked from the
    # others and links back. Internal linking was entirely absent until 2026-09-17;
    # doing it here means it can never be forgotten again.
    try:
        import subprocess
        r = subprocess.run([sys.executable, str(BLOG / "_related.py")],
                           capture_output=True, text=True, cwd=str(BLOG.parent))
        print((r.stdout or "").strip() or "read-next: nothing to do")
        if r.returncode:
            print("read-next WARNING:", (r.stderr or "").strip()[:300])
    except Exception as exc:                      # never let this break a publish
        print("read-next skipped:", exc)

    # Refresh the sitemap from git rather than appending to it - appending is how the
    # home page ended up listed twice and how 27 lastmod values went stale.
    try:
        r = subprocess.run([sys.executable, str(BLOG.parent / "refresh_sitemap.py")],
                           capture_output=True, text=True, cwd=str(BLOG.parent))
        print((r.stdout or "").strip() or "sitemap: nothing to do")
    except Exception as exc:
        print("sitemap refresh skipped:", exc)

    print("PUBLISHED=%s" % ",".join(published))
    return 0


if __name__ == "__main__":
    sys.exit(main())
