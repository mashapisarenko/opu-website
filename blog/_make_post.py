#!/usr/bin/env python3
"""Builds a finished blog article from the shell of an existing one.

Every part that differs between articles is replaced explicitly; anything not
listed here (nav, footer, capture form, course CTA, analytics) is carried over
untouched, so a new article can never drift away from the rest of the site.
"""
import re, sys, json, datetime, pathlib

HERE = pathlib.Path(__file__).resolve().parent
TEMPLATE = HERE / "russian-school-vs-american-piano-method.html"
SITE = "https://onlinepianouniversity.com"
OLD_SLUG = "russian-school-vs-american-piano-method"
MONTHS = ("January February March April May June July August September "
          "October November December").split()


def build(spec, out_dir):
    t = TEMPLATE.read_text(encoding="utf-8")
    d = datetime.date.fromisoformat(spec["date"])
    human = "%s %d, %d" % (MONTHS[d.month - 1], d.day, d.year)

    old_title = ("What the Russian School Does Differently &mdash; and Why It Matters "
                 "to an American Adult Beginner").replace("&mdash;", "—")
    old_desc = ("The real difference between the Russian piano school and American method "
                "books, written by a concert pianist trained in Moscow who teaches in the "
                "United States — and what an adult beginner should take from each.")
    old_sub = ("I was trained in Moscow and I have taught in American universities for years. "
               "The two traditions are not better and worse. They are strong in different "
               "places, and an adult learning alone needs to know where.")

    for old, new in ((old_title, spec["title"]),
                     (old_desc, spec["description"]),
                     (old_sub, spec["sub"]),
                     (OLD_SLUG, spec["slug"]),
                     ("2026-09-14", spec["date"]),
                     ("September 14, 2026", human)):
        if old not in t:
            sys.exit("template anchor not found: %r" % old[:60])
        t = t.replace(old, new)

    # lead photograph
    t = re.sub(r'<img src="\.\./images/blog/[^"]+" alt="[^"]*"',
               '<img src="../images/blog/%s" alt="%s"' % (spec["image"], spec["image_alt"]),
               t, count=1)

    # the small course card under the title
    t = re.sub(r'<div class="card" style="margin:26px 0;padding:18px 20px"><p style="margin:0">.*?</p></div>',
               '<div class="card" style="margin:26px 0;padding:18px 20px"><p style="margin:0">'
               '<strong>%s</strong> <a href="%s" target="_blank" rel="noopener">%s</a></p></div>'
               % (spec["cta_text"], spec["cta_href"], spec["cta_link"]),
               t, count=1, flags=re.S)

    # the article body
    t = re.sub(r'(<article class="post">\n).*?(\n    </article>)',
               lambda m: m.group(1) + spec["body"].strip() + m.group(2),
               t, count=1, flags=re.S)

    out = pathlib.Path(out_dir) / (spec["slug"] + ".html")
    out.write_text(t, encoding="utf-8")
    return out


def main():
    specs = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
    out_dir = pathlib.Path(sys.argv[2]); out_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = out_dir / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else []
    known = {e["slug"] for e in manifest}
    for spec in specs:
        p = build(spec, out_dir)
        if spec["slug"] not in known:
            manifest.append({"slug": spec["slug"], "date": spec["date"],
                             "title": spec["title"], "summary": spec["sub"]})
        print("built %s  -> %s" % (p.name, spec["date"]))
    manifest.sort(key=lambda e: e["date"])
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
                             encoding="utf-8")
    print("queue now holds %d article(s)" % len(manifest))


if __name__ == "__main__":
    main()
