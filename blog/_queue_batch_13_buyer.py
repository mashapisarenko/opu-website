# -*- coding: utf-8 -*-
"""Batch 13 (2026-11-14): thirty buyer-intent articles from _shop/topic_map_2026-11-14.md, two per day from 17 Nov to 1 Dec 2026
alongside the existing daily article (_publish.py publishes every article due on a date). Writes _specs_batch_13_buyer.json;
build with:  python3 blog/_make_post.py blog/_specs_batch_13_buyer.json blog/_queue"""
import json, pathlib
import _queue_batch_13a_pianos as A, _queue_batch_13b_recording as B

ORDER = [  # (date, slug): holiday and highest score first, before Black Friday (27 Nov) and Cyber Monday (30 Nov)
 ("2026-11-17", "best-digital-pianos-2026"), ("2026-11-17", "best-gifts-for-a-home-recording-hobbyist"),
 ("2026-11-18", "best-digital-piano-under-1000"), ("2026-11-18", "best-birthday-gifts-for-a-pianist"),
 ("2026-11-19", "best-digital-piano-under-500"), ("2026-11-19", "best-portable-digital-piano"),
 ("2026-11-20", "best-digital-piano-for-classical-music"), ("2026-11-20", "best-88-key-weighted-keyboard-for-beginners"),
 ("2026-11-21", "roland-fp-10-vs-yamaha-p-145bt"), ("2026-11-21", "roland-fp-10-review"),
 ("2026-11-22", "best-digital-piano-under-300"), ("2026-11-22", "yamaha-p-145bt-vs-casio-px-s1100"),
 ("2026-11-23", "casio-privia-px-s1100-review"), ("2026-11-23", "best-handheld-recorder-for-piano-practice"),
 ("2026-11-24", "best-audio-interface-for-beginners"), ("2026-11-24", "best-audio-interface-under-200"),
 ("2026-11-25", "best-recording-bundle-under-300"), ("2026-11-25", "home-recording-corner-on-a-budget"),
 ("2026-11-26", "best-page-turner-pedal-for-ipad"), ("2026-11-26", "best-tablet-for-sheet-music"),
 ("2026-11-27", "best-studio-monitors-under-300"), ("2026-11-27", "focusrite-scarlett-solo-vs-2i2"),
 ("2026-11-28", "best-stereo-microphones-for-piano"), ("2026-11-28", "best-88-key-weighted-midi-controller"),
 ("2026-11-29", "focusrite-scarlett-2i2-4th-gen-review"), ("2026-11-29", "how-to-connect-a-digital-piano-to-a-computer"),
 ("2026-11-30", "krk-rokit-5-vs-yamaha-hs5"), ("2026-11-30", "yamaha-hs5-vs-presonus-eris-e5"),
 ("2026-12-01", "zoom-h1n-vs-h4-essential-vs-h5"), ("2026-12-01", "best-bookshelf-speakers-for-classical-music")]

if __name__ == "__main__":
    by = {s["slug"]: s for s in A.S + B.S}
    assert len(by) == 30 and set(by) == {s for _, s in ORDER}, set(by) ^ {s for _, s in ORDER}
    out = []
    for d, s in ORDER:
        by[s]["date"] = d
        out.append(by[s])
    p = pathlib.Path(__file__).resolve().parent / "_specs_batch_13_buyer.json"
    p.write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    print("wrote", p.name, len(out))
