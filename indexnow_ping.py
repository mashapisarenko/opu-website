# -*- coding: utf-8 -*-
"""IndexNow: tell Bing, Yahoo, DuckDuckGo (via Bing), Yandex, Seznam and Naver
that pages changed, without any account. The key file <key>.txt sits at the site
root; the engines fetch it to confirm the site is ours.

Run AFTER Push origin (the pages and the key file must be live):
    python3 indexnow_ping.py            # every URL in sitemap.xml
    python3 indexnow_ping.py URL ...    # just these
Needs network: run it from the cloud session or any machine with internet;
the Mac shell here has no outbound web.
"""
import json, pathlib, re, sys, urllib.request
HERE = pathlib.Path(__file__).resolve().parent
HOST = "onlinepianouniversity.com"
key = next(p.stem for p in HERE.glob("*.txt") if re.fullmatch(r"[0-9a-f]{32}", p.stem))
urls = sys.argv[1:] or re.findall(r"<loc>([^<]+)</loc>", (HERE / "sitemap.xml").read_text())
body = json.dumps({"host": HOST, "key": key, "keyLocation": f"https://{HOST}/{key}.txt",
                   "urlList": sorted(set(urls))}).encode()
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body,
                             headers={"Content-Type": "application/json; charset=utf-8"})
with urllib.request.urlopen(req, timeout=30) as r:
    print("IndexNow:", r.status, "for", len(set(urls)), "URL(s)")   # 200/202 = accepted
