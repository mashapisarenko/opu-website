# -*- coding: utf-8 -*-
"""Which original illustration each shop product gets (images/shop/types/<type>.svg).

The illustrations are drawn by us, one per product TYPE; they never copy an Amazon or
manufacturer photo. Mapping = category + title keywords. Rules are checked in order and
the first match wins; anything unmatched falls back to the gift box.
"""
import re

# type -> (default label shown on the card, noun phrase for alt text)
TYPES = {
    "digital-piano-console":  ("Digital piano", "a digital piano with cabinet stand"),
    "digital-piano-portable": ("Digital piano", "an 88-key digital piano"),
    "keyboard-61":            ("Portable keyboard", "a portable keyboard"),
    "midi-controller":        ("MIDI controller", "a MIDI keyboard controller"),
    "piano-bench":            ("Piano bench", "a piano bench"),
    "keyboard-stand":         ("Keyboard stand", "a keyboard stand"),
    "sustain-pedal":          ("Sustain pedal", "a sustain pedal"),
    "headphones":             ("Headphones", "headphones"),
    "usb-microphone":         ("USB microphone", "a USB microphone"),
    "audio-interface":        ("Audio interface", "an audio interface"),
    "handheld-recorder":      ("Portable recorder", "a handheld recorder"),
    "wireless-mic":           ("Wireless microphone", "a wireless microphone kit"),
    "webcam":                 ("Webcam", "a webcam"),
    "phone-tripod":           ("Phone tripod", "a phone tripod"),
    "ring-light":             ("Ring light", "a ring light"),
    "stand-light":            ("Music stand light", "a music stand light"),
    "music-stand":            ("Music stand", "a music stand"),
    "metronome":              ("Metronome", "a metronome"),
    "page-turner":            ("Page-turner pedal", "a page-turner pedal"),
    "method-book":            ("Piano book", "a piano book"),
    "piano-care":             ("Piano care", "piano care products"),
    "studio-speakers":        ("Speakers", "speakers"),
    "turntable":              ("Turntable", "a turntable"),
    "singing-bowl":           ("Singing bowl", "a singing bowl"),
    "textile":                ("Music-themed textile", "a music-themed textile"),
    "wall-art":               ("Wall art", "music wall art"),
    "mug-gift":               ("Music gift", "a music-themed gift"),
    "jewelry":                ("Jewelry", "music jewelry"),
    "wellbeing":              ("Book & journal", "a book and journal"),
    "grand-piano":            ("Piano keepsake", "a grand piano keepsake"),
    "gift-box":               ("Gift", "a gift"),
}

# (category regex, title regex, type, label override or None)
RULES = [
    (r"digital-pianos|acoustic-and-hybrid", r"console|PX-770|YDP|DDP-|upright", "digital-piano-console", None),
    (r"digital-pianos|acoustic-and-hybrid", r"", "digital-piano-portable", None),
    (r"portable-keyboards", r"88-Key", "digital-piano-portable", "88-key keyboard"),
    (r"portable-keyboards", r"", "keyboard-61", None),
    (r"midi-controllers", r"", "midi-controller", None),
    (r"benches-and-stands", r"stand and bench", "piano-bench", "Stand & bench set"),
    (r"benches-and-stands", r"bench", "piano-bench", None),
    (r"benches-and-stands", r"stand", "keyboard-stand", None),
    (r"pedals", r"pedal unit", "sustain-pedal", "Pedal unit"),
    (r"pedals", r"foot switch", "sustain-pedal", "Foot switch"),
    (r"pedals", r"", "sustain-pedal", None),
    (r".", r"headphone", "headphones", None),
    (r".", r"audio interface", "audio-interface", None),
    (r".", r"recorder", "handheld-recorder", None),
    (r".", r"page turner|bluetooth pedal", "page-turner", None),
    (r".", r"turntable", "turntable", None),
    (r".", r"wireless (lavalier|microphone|mic\b)|lavalier|\bDJI Mic\b|\bLark\b|RODE Wireless", "wireless-mic", None),
    (r".", r"usb microphone|condenser", "usb-microphone", None),
    (r".", r"webcam", "webcam", None),
    (r".", r"ring light", "ring-light", None),
    (r".", r"video light|light panel", "ring-light", "Video light"),
    (r".", r"overhead|magic arm|phone mount", "phone-tripod", "Overhead phone mount"),
    (r".", r"tripod", "phone-tripod", None),
    (r"stand-lights", r"piano (light|lamp)", "stand-light", "Piano lamp"),
    (r"stand-lights", r"book light", "stand-light", "Clip-on light"),
    (r"stand-lights", r"desk lamp", "stand-light", "Clamp lamp"),
    (r"stand-lights", r"", "stand-light", None),
    (r"piano-care", r"humidifier", "piano-care", "Piano humidifier care"),
    (r"piano-care", r"hygrometer", "piano-care", "Hygrometer"),
    (r"piano-care", r"cover", "piano-care", "Keyboard cover"),
    (r"piano-care", r"", "piano-care", "Piano care kit"),
    (r".", r"metronome", "metronome", None),
    (r".", r"music stand", "music-stand", None),
    (r".", r"manuscript paper", "wellbeing", "Manuscript paper"),
    (r".", r"journal|manuscript|practice record", "wellbeing", "Music journal"),
    (r"method-books", r"course|adventures|piano book|bastien", "method-book", "Method book"),
    (r"method-books", r"theory", "method-book", "Theory book"),
    (r"method-books", r"", "method-book", "Sheet music"),
    (r"books-for-music-lovers|music-wellbeing", r"musicophilia|brain|secret chord", "wellbeing", "Book"),
    (r"sheet-music-holders|luxury-gifts", r"folder|holder|clip|storage", "method-book", "Sheet music accessory"),
    (r".", r"speaker|echo dot|sonos|monitor", "studio-speakers", None),
    (r".", r"singing bowl", "singing-bowl", None),
    (r".", r"grand piano|piano music box|baby grand|magic piano", "grand-piano", None),
    (r".", r"mug", "mug-gift", "Mug"),
    (r".", r"socks", "textile", "Socks"),
    (r".", r"blanket", "textile", "Throw blanket"),
    (r".", r"rug\b", "textile", "Rug"),
    (r".", r"pillow", "textile", "Pillow covers"),
    (r".", r"comforter|bedding|fitted sheet", "textile", "Bedding"),
    (r".", r"towel", "textile", "Kitchen towel"),
    (r".", r"oven mitt", "textile", "Oven mitts"),
    (r".", r"apron", "textile", "Apron"),
    (r".", r"shower curtain", "textile", "Shower curtain"),
    (r".", r"wall art|canvas|poster|wall decor|painting|wall sign", "wall-art", None),
    (r"jewelry", r"necklace and earrings", "jewelry", "Necklace & earrings"),
    (r"jewelry", r"cufflink", "jewelry", "Cufflinks"),
    (r"jewelry", r"earring", "jewelry", "Earrings"),
    (r"jewelry", r"bracelet", "jewelry", "Bracelet"),
    (r"jewelry", r"", "jewelry", "Necklace"),
    (r".", r"coaster|keychain|key chain|magnet|phone case|iphone", "mug-gift", "Small gift"),
    (r"luxury-gifts", r"glenn gould|michelangeli|barenboim|recordings|collection", "gift-box", "Recording box set"),
    (r"luxury-gifts", r"fountain pen", "gift-box", "Fountain pen"),
    (r".", r"kalimba", "gift-box", "Kalimba"),
    (r".", r"figurine", "gift-box", "Figurine"),
    (r".", r"night light", "gift-box", "Night light"),
    (r".", r"tote|book bag", "textile", "Tote bag"),
    (r".", r"record wall mount|wall mount shelves", "wall-art", "Record display shelves"),
    (r".", r"bookend|book end", "gift-box", "Bookends"),
    (r".", r"clock", "gift-box", "Wall clock"),
    (r".", r"", "gift-box", None),
]
_RULES = [(re.compile(c, re.I), re.compile(t, re.I), ty, lab) for c, t, ty, lab in RULES]


def type_of(p):
    """Return (type, label) for a product dict with 'category' and 'title'."""
    for c, t, ty, lab in _RULES:
        if c.search(p["category"]) and t.search(p["title"]):
            return ty, (lab or TYPES[ty][0])
    return "gift-box", TYPES["gift-box"][0]


MASS = {"bookends", "record display shelves", "bedding", "sheet music", "wall art", "jewelry", "piano care", "manuscript paper",
        "piano humidifier care", "sheet music accessory"}


def label_phrase(label):
    """'Digital piano' -> 'a digital piano'; keeps acronyms (MIDI, USB) upper-case."""
    words = label.split(" ")
    acronym = words[0].isupper() and len(words[0]) > 1
    if not acronym:
        words[0] = words[0].lower()
    l = " ".join(words)
    if l.lower() in MASS and l.lower() != "sheet music accessory":
        return l
    if l.endswith("s") and not l.endswith(("ss", "us")) and "&" not in l:
        return l
    art = "an" if (not acronym and (l[0].lower() in "aeiou" or l.startswith(("8", "11", "18")))) else "a"
    return "%s %s" % (art, l)


def alt_text(label, name):
    return "Illustration of %s \u2014 %s" % (label_phrase(label), name)
