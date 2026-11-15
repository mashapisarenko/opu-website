# -*- coding: utf-8 -*-
"""Music tech and home studio departments (2026-11-14): audio interfaces, studio monitors, MIDI controllers,
keyboard amplifiers, cables and power, tablet stands and page turners, home-studio kits, stands and accessories.

Same rules as the rest of the shop: no prices, ratings, review counts or Amazon photos on the page; every link is the
tagged amazon.com/dp/ASIN URL; written as Dr. Pisarenko's recommendation ("what I look for", "why I would choose"),
never as a claim that she tested a product; every product was opened live on amazon.com on 2026-11-14.
"""
import re

TECH_SLUGS = ["audio-interfaces-for-home-recording", "studio-monitors-for-home-recording", "midi-keyboard-controllers",
              "keyboard-amplifiers", "music-cables-and-power", "ipad-music-stands-and-page-turners",
              "home-studio-starter-kits", "mic-stands-and-studio-accessories"]

TYPES_NEW = {
    "amplifier":    ("Keyboard amplifier", "a keyboard amplifier"),
    "cable":        ("Audio cable", "an audio cable"),
    "power-strip":  ("Surge protector", "a surge protector power strip"),
    "tablet-stand": ("Tablet holder", "a tablet on a stand"),
    "mic-stand":    ("Mic stand", "a microphone stand with a boom arm"),
}

RULES = [
    (r"^audio-interfaces$", r"", "audio-interface", "Audio interface"),
    (r"^studio-monitors$", r"", "studio-speakers", "Studio monitors"),
    (r"^home-studio-kits$", r"AG03MK2", "audio-interface", "Mixer and interface"),
    (r"^home-studio-kits$", r"", "audio-interface", "Recording bundle"),
    (r"^keyboard-amps$", r"PA Speaker", "amplifier", "PA speaker"),
    (r"^keyboard-amps$", r"", "amplifier", "Keyboard amplifier"),
    (r"^cables-and-power$", r"surge", "power-strip", "Surge protector"),
    (r"^cables-and-power$", r"Direct Box", "cable", "DI box"),
    (r"^cables-and-power$", r"USB MIDI", "cable", "USB MIDI cable"),
    (r"^cables-and-power$", r"USB-B", "cable", "USB cable"),
    (r"^cables-and-power$", r"MIDI Cable", "cable", "MIDI cable"),
    (r"^cables-and-power$", r"Headphone", "cable", "Headphone cable"),
    (r"^cables-and-power$", r"XLR", "cable", "XLR cable"),
    (r"^cables-and-power$", r"", "cable", "Instrument cable"),
    (r"^tablet-and-page-turners$", r"Page Turner|Pedal", "page-turner", "Page-turner pedal"),
    (r"^tablet-and-page-turners$", r"Floor Stand", "tablet-stand", "Tablet floor stand"),
    (r"^tablet-and-page-turners$", r"", "tablet-stand", "Tablet holder"),
    (r"^studio-stands-and-accessories$", r"Pop Filter", "mic-stand", "Pop filter"),
    (r"^studio-stands-and-accessories$", r"Isolation", "mic-stand", "Monitor isolation pads"),
    (r"^studio-stands-and-accessories$", r"Speaker Stands", "mic-stand", "Monitor stands"),
    (r"^studio-stands-and-accessories$", r"Keyboard Stand", "keyboard-stand", "Keyboard stand"),
    (r"^studio-stands-and-accessories$", r"Scissor|Studio Arm", "mic-stand", "Desk boom arm"),
    (r"^studio-stands-and-accessories$", r"", "mic-stand", "Mic stand"),
]

WHY_NEW = {
    "amplifier": ["An amplifier lets a keyboard fill a room, and I suggest one only when headphones and a pair of small speakers are not enough.",
                  "I want a keyboard amplifier to be simple and honest: it should make the instrument louder without changing what your hands did."],
    "cable": ["A cable is the least exciting purchase in a studio and the first thing to spoil a recording when it fails, so I choose plain, well-made ones.",
              "Good cables are cheap insurance: the sound you worked for should reach the interface or the speakers unchanged."],
    "power-strip": ["Protecting an instrument you have paid for costs very little, and a surge protector is the simplest way to do it."],
    "tablet-stand": ["Music at eye level lets your head and shoulders stay relaxed, and a tablet needs a firm stand to hold it there.",
                     "A tablet is only as useful as its position: I want it high enough to read without bending your neck."],
    "mic-stand": ["A recording is only as good as where the sound is captured, and small fittings like this keep the microphone or the speaker where it belongs.",
                  "I like fittings that stay out of the way: set them once and the recording habit becomes easier."],
}

PAGES = [
 dict(slug="audio-interfaces-for-home-recording", icon="🎛️", label="Audio Interfaces",
  blurb="USB audio interfaces for recording piano at home.",
  asins=["B00FFIGZF6", "B08Q1NJSBQ", "B08D8R6VFC", "B07664LMPQ", "B08Q1V77NR", "B084BGC5LR", "B09HL3GD7G", "B09J1W1TYN", "B0812B26TN", "B0DJCK64XX",
         "B09J1V6R6N", "B0C5JSHP7M", "B07QR6Z1JB", "B0FT4V7Z84", "B09J1TL1B8", "B0C5JRTS3Y", "B0C5JMFX6S"],
  h1="Best Audio Interfaces for Recording Piano at Home",
  title="Best Audio Interfaces for Recording Piano at Home",
  desc="USB audio interfaces for recording a digital or acoustic piano at home, from a first interface to a studio-grade one, chosen by a concert pianist.",
  answer="For most adults a two-input USB audio interface is enough: it takes a pair of microphones or the stereo outputs of a digital piano and sends clean sound to your computer. Start with two inputs and a headphone output, and add more only when you know why.",
  intro="An audio interface is the small box between your piano or microphones and your computer. It turns the sound into digital audio, powers condenser microphones, and gives you a headphone output with no delay. You do not need one to begin: a phone is enough for a first recording, and my feedback on your playing is free either way. Buy an interface when you want a recording that sounds like the piano in the room. I describe each interface by what its listing states, and I choose by how simple it is to set up and live with.",
  criteria=["<strong>Inputs.</strong> Two inputs cover a stereo pair of microphones or both outputs of a digital piano; one input is enough for a single microphone.",
            "<strong>Microphone preamps and phantom power.</strong> Condenser microphones need 48-volt phantom power, which the interface supplies.",
            "<strong>The connection.</strong> Check whether the interface uses USB-C or USB-A, and whether the cable you own fits your computer.",
            "<strong>A headphone output you can monitor on.</strong> You should hear yourself without a delay, through headphones, while you record.",
            "<strong>Software and support.</strong> Some interfaces come with recording software; check that your computer's system is supported before you buy."],
  faqs=[("Do I need an audio interface to record my digital piano?", "Not always. Many digital pianos have a USB port that sends audio or MIDI to a computer directly. An interface helps when you want to use microphones, record the line outputs of a piano with cables, or listen without delay."),
        ("How many inputs do I need to record piano?", "Two inputs are enough for most pianists: one for each microphone of a stereo pair, or one for each output of a stereo digital piano. A single input works for one microphone or a mono signal."),
        ("What is phantom power?", "A 48-volt supply that the interface sends down the microphone cable to power a condenser microphone. Dynamic microphones do not need it."),
        ("Which interface is the best for a beginner?", "The one you will really set up and use. For a first interface I choose a two-input model from a maker with a long record of software support, and I do not pay for channels I will not use.")],
  related=["microphones-and-audio-interfaces", "studio-monitors-for-home-recording", "music-cables-and-power", "home-studio-starter-kits"]),

 dict(slug="studio-monitors-for-home-recording", icon="🔊", label="Studio Monitors",
  blurb="Powered monitors for hearing your own piano touch.",
  asins=["B08KXTJX16", "B0C88ZB3D9", "B0DGXRC7MP", "B00CP4IJH0", "B09DKV849B", "B0GT2JFDD1", "B0FZLF2S8G", "B09MLT8C45", "B07BKVY3J1", "B077NHM2K6",
         "B00CFOX420", "B0CKTR88Y7", "B075Q5T7Q1", "B0CYM2RH6W"],
  h1="Best Studio Monitors for Home Recording and Piano Practice",
  title="Best Studio Monitors for Home Recording and Piano",
  desc="Powered studio monitors for a desk or a home studio, picked by a concert pianist for an honest sound that shows your touch, from small desktop pairs up.",
  answer="Choose powered studio monitors with a flat, honest sound, in a size that fits your desk and room: a pair of 4- to 5-inch monitors for a small room, and larger ones only when the room can carry them. Check whether the listing is one speaker or a pair.",
  intro="Studio monitors are speakers made to tell the truth about what you play. A digital piano's built-in speakers are made to sound pleasant; monitors are made to show you the unevenness of your touch and your rhythm, which is what a teacher listens for. They are also the right speakers for a desk where you record, listen back and work on music. I list monitors by what each listing says, and I note where a listing sells one speaker instead of a pair.",
  criteria=["<strong>One speaker or a pair.</strong> Several monitors are sold singly, so read the title and buy two for stereo.",
            "<strong>Size for the room.</strong> A small desk and a small room suit 3- to 5-inch monitors; a bigger speaker in a small room muddies the sound.",
            "<strong>The inputs.</strong> Look for balanced 1/4-inch or XLR inputs if you will connect an interface, and check what cable you need.",
            "<strong>Placement controls.</strong> Some monitors have switches that adjust the sound for a wall or a desk, which matters in a small room.",
            "<strong>Power and size.</strong> Powered monitors plug into a wall; check the space behind and beside the desk."],
  faqs=[("What is the difference between studio monitors and ordinary speakers?", "Studio monitors aim for a flat, accurate sound so you hear what is really in a recording. Ordinary speakers often add bass and sparkle to flatter the music."),
        ("Can I connect studio monitors to a digital piano?", "Yes, if the piano has line outputs. Connect them with balanced or instrument cables of the right plug type; the cables page in my shop lists the common ones."),
        ("Do I need monitors if I use headphones?", "No. Headphones are better for quiet practice. Monitors help when you want to hear the room, play for a listener, or mix a recording."),
        ("What size studio monitor should I buy?", "A 3- to 5-inch pair for a desk in a small room, and a 5- to 8-inch pair for a larger room. A bigger speaker is not better in a small room.")],
  related=["speakers-for-keyboards", "audio-interfaces-for-home-recording", "mic-stands-and-studio-accessories", "headphones-for-piano"]),

 dict(slug="midi-keyboard-controllers", cats=["midi-controllers"], icon="🎹", label="MIDI Keyboard Controllers",
  blurb="MIDI keyboards for software pianos, notation and music apps.",
  h1="Best MIDI Keyboard Controllers for Piano, Notation and Home Music",
  title="Best MIDI Keyboard Controllers for Pianists and Learners",
  desc="MIDI keyboard controllers from 25 to 88 keys for software pianos, notation and recording, chosen by a concert pianist who teaches adults.",
  answer="A MIDI controller makes no sound of its own; it plays software on your computer or tablet. Pianists who want real touch should choose weighted keys; everyone else can choose 49 keys and a short, clear layout.",
  intro="A MIDI keyboard controller is a keyboard that sends notes to software: a virtual piano, a notation program, a recording program or a learning app. It is a tool, not a replacement for a piano with weighted keys. I recommend one to an adult who already records or composes, or who wants a software piano on a desk. If you are choosing your first piano, start at my digital piano pages instead. I describe each controller by what its listing states.",
  criteria=["<strong>The keys.</strong> Weighted hammer-action keys feel like a piano; synth-action keys are lighter and suit software and composing.",
            "<strong>Key count.</strong> 25 and 37 keys fit a travel bag, 49 and 61 keys suit software, and 88 keys suit a pianist.",
            "<strong>No built-in sound.</strong> A controller needs a computer, a tablet or a sound module; check what your listing says it works with.",
            "<strong>The software it comes with.</strong> Some controllers include a virtual piano or recording software.",
            "<strong>Pads, knobs and sliders.</strong> Useful for producers and often not needed by a learner."],
  faqs=[("What is a MIDI keyboard controller?", "A keyboard that sends note and control messages to a computer or tablet but does not make sound itself. The software turns those notes into piano or any other sound."),
        ("Can I learn piano on a MIDI controller?", "Only if it has weighted, piano-style keys and you are also practicing technique. A small synth-action controller is a tool for software, not a piano."),
        ("Do I need to buy software with a MIDI controller?", "Many controllers include some software; check the listing. Computers and tablets also have free piano sounds and music programs."),
        ("How many keys should a MIDI controller have?", "49 keys cover most software uses; 88 keys with weighted action suit a pianist who wants the full range.")],
  related=["keyboards", "audio-interfaces-for-home-recording", "music-cables-and-power", "home-studio-starter-kits"]),

 dict(slug="keyboard-amplifiers", icon="📢", label="Keyboard Amplifiers",
  blurb="Amplifiers and PA speakers for a keyboard or stage piano.",
  asins=["B08L34HBWD", "B0C45Y7YTJ", "B081PSNDCV", "B004LRP56W", "B004LRP576", "B00NIE80A2", "B077KR6XG1", "B0794DH3VL"],
  h1="Best Keyboard Amplifiers for Digital Pianos and Stage Pianos",
  title="Best Keyboard Amplifiers for Digital and Stage Pianos",
  desc="Keyboard amplifiers and powered PA speakers for a stage piano or keyboard, picked by a concert pianist, for a clear sound in a living room or a small band.",
  answer="A keyboard amplifier is the right choice for a stage piano or a portable keyboard that has no speakers, or for playing with others. A home digital piano already has speakers, and headphones are better for practice.",
  intro="A stage piano or a small keyboard often has no speakers, because it is made to be plugged into something. A keyboard amplifier is that something: a small loudspeaker with inputs for a keyboard, and sometimes a microphone or a phone for backing tracks. I include them because adults who return to piano sometimes want to play with friends, in church or in a small band. For a quiet practice room, I send you to my headphones and speakers pages first.",
  criteria=["<strong>Watts and speaker size.</strong> Twenty to fifty watts is plenty for a living room; a band needs more.",
            "<strong>Inputs.</strong> A keyboard needs a stereo input or two inputs for left and right; a second channel lets you add a microphone or a phone.",
            "<strong>Stereo or mono.</strong> A stereo amplifier keeps the left and right of a piano sound; a mono amplifier mixes them.",
            "<strong>Battery power.</strong> A battery model is handy for playing outdoors or where there is no outlet.",
            "<strong>Weight.</strong> If you carry it to rehearsals, check the weight before you check the sound."],
  faqs=[("Do I need an amplifier for my digital piano?", "Not if the piano has built-in speakers. An amplifier is for stage pianos and portable keyboards without speakers, or when you need a louder sound than the built-in speakers give."),
        ("Can I use a PA speaker instead of a keyboard amplifier?", "Yes. A powered PA speaker also takes a line-level signal from a keyboard, and many are made for stage pianos. It is usually bigger and louder than a small keyboard amp."),
        ("What cable connects a keyboard to an amplifier?", "A 1/4-inch instrument or TRS cable in most cases; check the keyboard's output jacks and the amplifier's inputs. My cables page lists the common ones."),
        ("Mono or stereo amplifier?", "A stereo pair or a stereo amplifier keeps the piano's width. A mono amplifier is simpler and fine for a small room or a church.")],
  related=["stage-pianos", "speakers-for-keyboards", "music-cables-and-power", "keyboard-cases-and-covers"]),

 dict(slug="music-cables-and-power", icon="🔌", label="Music Cables and Power",
  blurb="Cables, adapters and surge protection for a piano corner.",
  asins=["B00BGDMIOG", "B000068NYH", "B006EE7FEA", "B000068NTZ", "B086ZHM1FC", "B000UD4LIY", "B08HMWJWDW", "B07R6TY6RQ", "B004TP4J7M", "B072DVLDKC", "B0002QPC28", "B000A8J3N2"],
  h1="Best Cables, Adapters and Surge Protectors for a Piano and Home Studio",
  title="Best Music Cables, Adapters and Surge Protectors",
  desc="Instrument and microphone cables, USB and MIDI cables, headphone adapters and surge protectors for a piano corner, chosen by a concert pianist.",
  answer="Buy the plug types your gear actually has: balanced 1/4-inch cables for a digital piano's outputs, XLR for microphones, a USB-B to USB-C cable for the computer, and a surge protector under it all. Plain cables from known makers are enough.",
  intro="Cables are the least glamorous part of a music corner and the part that most often fails. Most beginners need only a handful: a cable from the piano's outputs to an interface or speakers, a USB cable to the computer, a headphone adapter, and a surge protector. I choose plain, well-made cables, and I ask you to check the plug on each end against your own gear before you order.",
  criteria=["<strong>The plug on each end.</strong> Look at your piano, interface or speakers and match 1/4-inch TRS, XLR, 3.5 mm, USB-B, USB-C or five-pin MIDI exactly.",
            "<strong>Balanced or unbalanced.</strong> A balanced TRS or XLR cable keeps noise out over longer runs.",
            "<strong>Length.</strong> Buy the length you need, not the longest; a long extra loop picks up hum.",
            "<strong>Strain relief.</strong> A cable that bends sharply at the plug fails there first; look for a molded plug with a spring or boot.",
            "<strong>Surge protection.</strong> Count your outlets and check the protector's ratings in the listing."],
  faqs=[("What cable connects a digital piano to an audio interface?", "Usually two 1/4-inch cables, one for left and one for right, from the piano's line outputs to the interface's line inputs. Check your piano's output jacks first."),
        ("Do I need an expensive cable?", "No. A plain cable from a known maker with solid plugs is enough. Expensive cables do not make a digital piano sound better."),
        ("What is a USB-B cable used for?", "Many digital pianos, interfaces and MIDI keyboards have a square USB-B port. A USB-B to USB-C cable connects them to a modern laptop."),
        ("Do I need a surge protector?", "A surge protector is a cheap way to protect a piano and a computer. Plug the piano's power supply into it and check the listing for what it covers.")],
  related=["audio-interfaces-for-home-recording", "keyboard-amplifiers", "midi-keyboard-controllers", "piano-accessories"]),

 dict(slug="ipad-music-stands-and-page-turners", icon="📱", label="Tablet Stands and Page Turners",
  blurb="Tablet holders, floor stands and pedal page turners.",
  asins=["B0936P1MNB", "B0B4ZN2T8B", "B0DYJRQKCK", "B00L9EKJY8", "B09LH19QQJ", "B07JKKVPCV", "B01J1LS4PQ", "B0CXSX57G7", "B06XNW9LRP", "B09S247V3D", "B00ILVHBKC", "B09TX3VS59", "B06VT1C5ND"],
  h1="iPad Music Stands, Tablet Holders and Page-Turner Pedals",
  title="iPad Music Stands, Tablet Holders and Page Turners",
  desc="Tablet holders, floor stands and Bluetooth page-turner pedals for reading sheet music on an iPad, chosen by a concert pianist who teaches adults.",
  answer="To read sheet music from a tablet you need a firm holder at eye level and, if you want to keep both hands on the keys, a Bluetooth page-turner pedal that works with your music app. Check that the pedal is compatible with the app you use.",
  intro="Many adults now read their music from an iPad or a tablet. It is light, it holds a whole library, and it can be bright enough for a dim room. Two things make it work at the piano: a holder that keeps the tablet at the right height and angle, and a pedal that turns the page without lifting a hand. I describe each by its listing and ask you to check the size of your tablet and the app you use before you order.",
  criteria=["<strong>Holder type.</strong> A clamp for a microphone stand, a floor stand with a ball head, or a mount for a music stand; match it to the furniture you already have.",
            "<strong>Tablet size.</strong> Check the range of sizes the holder fits, and whether your tablet's case still fits.",
            "<strong>Stability.</strong> A tablet that wobbles while you play distracts; choose a firm base and a locking joint.",
            "<strong>Pedal compatibility.</strong> A page turner must work with your music app; check the listing and the app's own help page.",
            "<strong>Silent or clicking pedals.</strong> A silent pedal suits a recital or a quiet room."],
  faqs=[("What do I need to read sheet music from an iPad?", "A tablet holder or stand that keeps the screen at eye level, a music app that opens your scores, and optionally a Bluetooth page-turner pedal."),
        ("Do page-turner pedals work with every music app?", "No. Many apps support Bluetooth pedals, but you should check your app's help page and the pedal's listing before buying."),
        ("Can I use a microphone stand for a tablet?", "Yes. A tablet holder that clamps onto a microphone stand is a common solution, if the stand is heavy enough to hold the tablet without tipping."),
        ("Is a tablet better than paper music?", "It is lighter and easier to carry, and your whole library is in one place. Paper is easier to mark by hand and does not run out of battery. Many players use both.")],
  related=["music-stands", "stand-lights", "piano-books-and-sheet-music", "practice-tools"]),

 dict(slug="home-studio-starter-kits", icon="🎙️", label="Home Studio Starter Kits",
  blurb="Interface-and-microphone bundles for a first recording corner.",
  asins=["B0DB3WJDDG", "B0CSL4PXDV", "B09VTKC91H", "B08DBGNZT1", "B07TBF9D9N", "B0B823S1NR", "B0CSLDLKZJ", "B0C5JPJJ2M", "B0BQHHZ1QQ", "B0C5JTBK77", "B07YFGWG8G"],
  h1="Home Studio Starter Kits for Recording Piano and Music at Home",
  title="Home Studio Starter Kits for Recording Piano",
  desc="Starter recording bundles and simple kits for a first home studio: interface, microphone and software, chosen by a concert pianist who teaches online.",
  answer="A starter bundle gives you the interface, the cables and the software in one box, which is the easiest way into home recording. Choose a bundle from a maker with good software support, and expect to add headphones and a stand.",
  intro="A home studio kit is a way to start recording without choosing each piece alone. It usually contains an audio interface, a microphone and a way to monitor, and often some recording software. I include bundles and a few simpler alternatives, such as a handheld recorder or a USB microphone, because the best setup is the one an adult will really use every week. I describe each by its listing, and I ask you to read what is in the box before you buy.",
  criteria=["<strong>What is in the box.</strong> Read the listing for the interface, microphone, headphones, cables and software.",
            "<strong>One microphone or two.</strong> A single microphone is fine for a voice or a mono clip; a stereo pair suits a piano.",
            "<strong>Software.</strong> Check which recording software comes with it and whether it runs on your computer.",
            "<strong>Room to grow.</strong> An interface with two inputs lets you add a second microphone later.",
            "<strong>Simplicity.</strong> A handheld recorder or a USB microphone is a good first step if you do not want a computer in the room."],
  faqs=[("What do I need to start a home recording studio?", "A computer or a recorder, a way to capture sound (an interface and microphone, or a USB microphone), headphones, and some recording software. A bundle packs most of these into one purchase."),
        ("Is a bundle better than buying pieces?", "A bundle is simpler and often cheaper than buying each piece. Buying pieces gives you more choice of microphone and headphones."),
        ("Can I record a digital piano without a microphone?", "Yes. A digital piano can connect straight to an interface or a computer by cable or USB, with no microphone."),
        ("Do I need a studio to send you a recording?", "No. A phone is enough for my free feedback. A kit is for when you want to hear your playing as a listener does.")],
  related=["audio-interfaces-for-home-recording", "microphones-and-audio-interfaces", "studio-monitors-for-home-recording", "mic-stands-and-studio-accessories"]),

 dict(slug="mic-stands-and-studio-accessories", icon="🎚️", label="Mic Stands and Studio Accessories",
  blurb="Microphone stands, boom arms, pop filters and monitor pads.",
  asins=["B01N21H9WY", "B0F9WHKX2X", "B0CVXRXSPG", "B0C1NHTNN6", "B000978D58", "B00INKBI9Q", "B001D7UYBO", "B07574VQPQ", "B000TZVCWG"],
  h1="Best Mic Stands, Boom Arms and Small Studio Accessories",
  title="Best Mic Stands, Boom Arms and Studio Accessories",
  desc="Microphone stands, desk boom arms, pop filters, monitor pads and a keyboard stand for a home studio, chosen by a concert pianist who records and teaches.",
  answer="Match the stand to the job: a tripod boom stand for a microphone over an acoustic piano, a desk arm for a USB or XLR microphone at a computer, and small pads or stands to put speakers at ear level.",
  intro="Where you put the microphone changes the recording more than the price of the microphone. A good stand lets you place it above the piano or in front of you and leave it there. These are the small fittings I find most useful: stands, boom arms, pop filters for speech, pads for desktop speakers, and a firm keyboard stand. I describe each by its listing.",
  criteria=["<strong>Tripod base or desk clamp.</strong> A tripod stands on the floor; a desk arm clamps to a table and frees the desk.",
            "<strong>Reach and height.</strong> Check the maximum height and boom length for the piano you record.",
            "<strong>Weight capacity.</strong> A heavy microphone needs a heavier stand; read the listing.",
            "<strong>The thread.</strong> Most microphones attach with a standard thread; check the adapter that comes with the stand.",
            "<strong>Stability.</strong> A stand that tips or droops is worse than none."],
  faqs=[("Where should I place a microphone to record piano?", "On a boom stand a little above and in front of the instrument, pointing at the strings or the area above the keys. Record a short passage and listen back with headphones before you move it."),
        ("Do I need a pop filter for piano?", "No. A pop filter is for speech and singing. It is useful if you also record your voice for a lesson or a talk."),
        ("What are monitor isolation pads?", "Foam pads that sit between a desk and a speaker so the desk does not vibrate. They are a small, cheap fix for a boomy desk."),
        ("Can I use a keyboard stand for a digital piano?", "Yes, if it holds the weight and width of your instrument. Check the listing for the range of keyboards it fits.")],
  related=["microphones-and-audio-interfaces", "audio-interfaces-for-home-recording", "piano-benches-and-stands", "studio-monitors-for-home-recording"]),
]

Q_NEW = {
 "audio-interfaces-for-home-recording": ("What should I look for in an audio interface?", "How does recording help you learn?", "Which audio interface should I buy?", "What do pianists ask about audio interfaces?"),
 "studio-monitors-for-home-recording": ("What should I look for in studio monitors?", "How do monitors help you learn?", "Which studio monitors should I buy?", "What do pianists ask about studio monitors?"),
 "midi-keyboard-controllers": ("What should I look for in a MIDI keyboard controller?", "How can a MIDI controller help you learn?", "Which MIDI controller should I buy?", "What do learners ask about MIDI controllers?"),
 "keyboard-amplifiers": ("What should I look for in a keyboard amplifier?", "How does an amplifier help you play?", "Which keyboard amplifier should I buy?", "What do players ask about keyboard amplifiers?"),
 "music-cables-and-power": ("What should I look for in music cables?", "How do good cables help you?", "Which cables and adapters should I buy?", "What do players ask about cables and power?"),
 "ipad-music-stands-and-page-turners": ("What should I look for in a tablet stand?", "How does a tablet setup help you learn?", "Which tablet stand or page turner should I buy?", "What do readers ask about iPad music stands?"),
 "home-studio-starter-kits": ("What should I look for in a home studio kit?", "How does a recording kit help you learn?", "Which starter kit should I buy?", "What do students ask about home studio kits?"),
 "mic-stands-and-studio-accessories": ("What should I look for in a mic stand?", "How do good stands help your recordings?", "Which stand or accessory should I buy?", "What do students ask about mic stands?"),
}

LEARN_NEW = {
 "audio-interfaces-for-home-recording": "How this helps you learn: listening to a clean recording of yourself is the fastest way to hear uneven touch and rhythm, and a clear clip is all I need to give you feedback.",
 "studio-monitors-for-home-recording": "How this helps you learn: speakers that tell the truth let you hear what a teacher hears, the unevenness in your touch that built-in speakers politely hide.",
 "midi-keyboard-controllers": "How this helps you learn: a controller with piano touch lets you practice into notation or a software piano, and seeing your notes on a screen can show you where your rhythm drifts.",
 "keyboard-amplifiers": "How this helps you learn: an amplifier lets you play for another person, and playing for someone is the quickest way to find out what you really know.",
 "music-cables-and-power": "How this helps you learn: the right cables get your playing onto a recording without noise, and a recording you can trust is how you hear your own progress.",
 "ipad-music-stands-and-page-turners": "How this helps you learn: music at eye level keeps your head and shoulders relaxed, and turning pages with your foot keeps both hands on the keys.",
 "home-studio-starter-kits": "How this helps you learn: a simple kit that is always ready makes recording a habit, and a recording is the most honest teacher you have between lessons.",
 "mic-stands-and-studio-accessories": "How this helps you learn: a microphone that stays where you put it gives you recordings you can compare from week to week.",
}

DEPTH_NEW = {
"audio-interfaces-for-home-recording": """
<h2>How do I connect a digital piano to an audio interface?</h2>
<p>Look at the back of the piano. If it has two output jacks marked left and right, connect each to an input on the interface with a 1/4-inch cable, and set the interface's input to line level. If it has only a headphone jack, a 3.5 mm to 1/4-inch cable works for a clip, though the headphone output is not made for recording. If it has a USB port, you may not need an interface at all.</p>
<h3>Record a short test first</h3>
<p>Play eight bars, listen back through headphones and check that you hear no hiss and no clipping. Then move on to a whole piece.</p>
""",
"studio-monitors-for-home-recording": """
<h2>Where do I put studio monitors?</h2>
<p>Place the two speakers and your head at the corners of an equal-sided triangle, with the tweeters at ear height and angled toward you. Keep them a little away from the wall behind them. If they sit on a desk, a pair of foam pads or small stands from my accessories page stops the desk from buzzing.</p>
<h3>Give your ears a day</h3>
<p>Play a recording you know well. Honest monitors may sound less flattering than the speakers you are used to, and that is the point.</p>
""",
"ipad-music-stands-and-page-turners": """
<h2>How do I set up a tablet at the piano?</h2>
<p>Put the tablet where the music rest would be, tilted back so you read without lowering your head. Turn the screen's auto-lock off and keep the brightness comfortable. Pair a page-turner pedal over Bluetooth, and test the page turn on a piece you know before you need it in front of an audience.</p>
<h3>Keep a paper copy for a recital</h3>
<p>Batteries and Bluetooth connections fail at the worst time, so I suggest keeping a paper copy of any piece you will play for others.</p>
""",
}

BLOG_NEW = {
 "audio-interfaces-for-home-recording": ["best-microphone-for-recording-piano-at-home", "practicing-with-a-recording", "run-your-own-piano-lesson"],
 "studio-monitors-for-home-recording": ["best-headphones-for-digital-piano", "practicing-piano-in-an-apartment"],
 "midi-keyboard-controllers": ["digital-piano-vs-keyboard", "weighted-vs-semi-weighted-keys"],
 "keyboard-amplifiers": ["digital-piano-vs-keyboard", "practicing-piano-in-an-apartment"],
 "music-cables-and-power": ["you-got-a-keyboard-now-what", "best-microphone-for-recording-piano-at-home"],
 "ipad-music-stands-and-page-turners": ["how-to-start-sight-reading", "reading-music-or-playing-by-ear"],
 "home-studio-starter-kits": ["best-microphone-for-recording-piano-at-home", "run-your-own-piano-lesson"],
 "mic-stands-and-studio-accessories": ["best-microphone-for-recording-piano-at-home", "piano-bench-height-posture"],
}

NAV_ADD = [("audio-interfaces-for-home-recording", "Interfaces"), ("studio-monitors-for-home-recording", "Studio monitors"),
           ("midi-keyboard-controllers", "MIDI keyboards"), ("ipad-music-stands-and-page-turners", "Tablet stands")]

def apply(C, GUIDES, HUB, ARTICLE, D, S, N, SI):
    for k, v in TYPES_NEW.items():
        SI.TYPES[k] = v
    SI._RULES[0:0] = [(re.compile(c, re.I), re.compile(t, re.I), ty, lab) for c, t, ty, lab in RULES]
    N.WHY.update(WHY_NEW)
    for pg in PAGES:
        pg["q"] = Q_NEW[pg["slug"]]
        C.PAGES.append(pg)
    D.LEARN.update(LEARN_NEW)
    D.DEPTH.update(DEPTH_NEW)
    S.BLOG.update(BLOG_NEW)
