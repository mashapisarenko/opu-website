/* ============================================================
   OPU Virtual Keyboard v2 — self-contained widget module.
   The first module of the future Maestra app.

   - Click / tap / drag to play (Web Audio piano tone)
   - Note names on the keys (beginner-friendly)
   - Computer keyboard: A S D F G H J K = white keys, W E T Y U = black
   - Web MIDI: plug in a digital piano and it plays + lights up
   - ● Record your melody → ▶ play it back (create songs!)
   - ♫ Demo: plays "Ode to Joy" with keys lighting up
   ============================================================ */
(function () {
  "use strict";

  // ---------- data: 2 octaves, C4..B5 ----------
  var NOTES = [];
  var NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"];
  for (var oct = 4; oct <= 5; oct++) {
    for (var i = 0; i < 12; i++) {
      NOTES.push({ name: NAMES[i], oct: oct, midi: 12 * (oct + 1) + i, black: NAMES[i].indexOf("#") > -1 });
    }
  }
  var KEYMAP = { a: 60, w: 61, s: 62, e: 63, d: 64, f: 65, t: 66, g: 67, y: 68, h: 69, u: 70, j: 71, k: 72, o: 73, l: 74, p: 75 };

  // Public-domain songs — [midi, beats]
  var SONGS = {
    joy: { name: "Ode to Joy", by: "Beethoven", bpm: 132, seq: [
      [64,1],[64,1],[65,1],[67,1],[67,1],[65,1],[64,1],[62,1],
      [60,1],[60,1],[62,1],[64,1],[64,1.5],[62,.5],[62,2],
      [64,1],[64,1],[65,1],[67,1],[67,1],[65,1],[64,1],[62,1],
      [60,1],[60,1],[62,1],[64,1],[62,1.5],[60,.5],[60,2]
    ]},
    elise: { name: "Für Elise", by: "Beethoven", bpm: 120, seq: [
      [76,.5],[75,.5],[76,.5],[75,.5],[76,.5],[71,.5],[74,.5],[72,.5],[69,1.5],
      [60,.5],[64,.5],[69,.5],[71,1.5],[64,.5],[68,.5],[71,.5],[72,1.5],
      [64,.5],[76,.5],[75,.5],[76,.5],[75,.5],[76,.5],[71,.5],[74,.5],[72,.5],[69,2]
    ]},
    bday: { name: "Happy Birthday", by: "", bpm: 120, seq: [
      [67,.75],[67,.25],[69,1],[67,1],[72,1],[71,2],
      [67,.75],[67,.25],[69,1],[67,1],[74,1],[72,2],
      [67,.75],[67,.25],[79,1],[76,1],[72,1],[71,1],[69,2],
      [77,.75],[77,.25],[76,1],[72,1],[74,1],[72,2]
    ]}
  };

  // ---------- audio engine ----------
  var Audio = {
    ctx: null,
    ensure: function () {
      if (!this.ctx) {
        var AC = window.AudioContext || window.webkitAudioContext;
        if (!AC) return null;
        this.ctx = new AC();
      }
      if (this.ctx.state === "suspended") this.ctx.resume();
      return this.ctx;
    },
    freq: function (midi) { return 440 * Math.pow(2, (midi - 69) / 12); },
    play: function (midi, vel) {
      var ctx = this.ensure();
      if (!ctx) return;
      vel = vel || 0.9;
      var t = ctx.currentTime;
      var f = this.freq(midi);
      var master = ctx.createGain();
      var lp = ctx.createBiquadFilter();
      lp.type = "lowpass";
      lp.frequency.setValueAtTime(Math.min(f * 7, 9500), t);
      lp.frequency.exponentialRampToValueAtTime(Math.min(f * 2.5, 4000), t + 1.2);
      master.connect(lp); lp.connect(ctx.destination);
      var partials = [
        { mult: 1, gain: 1.0, type: "triangle", detune: 0 },
        { mult: 1, gain: 0.35, type: "sine", detune: 3 },
        { mult: 2, gain: 0.30, type: "sine", detune: 0 },
        { mult: 3, gain: 0.12, type: "sine", detune: 0 },
        { mult: 4, gain: 0.05, type: "sine", detune: 0 }
      ];
      var dur = 2.6;
      master.gain.setValueAtTime(0, t);
      master.gain.linearRampToValueAtTime(0.3 * vel, t + 0.006);
      master.gain.exponentialRampToValueAtTime(0.12 * vel, t + 0.25);
      master.gain.exponentialRampToValueAtTime(0.0001, t + dur);
      partials.forEach(function (p) {
        var o = ctx.createOscillator(), g = ctx.createGain();
        o.type = p.type;
        o.frequency.value = f * p.mult;
        if (p.detune) o.detune.value = p.detune;
        g.gain.value = p.gain;
        o.connect(g); g.connect(master);
        o.start(t); o.stop(t + dur);
      });
    }
  };

  // ---------- build the DOM ----------
  function build(container) {
    var kb = document.createElement("div");
    kb.className = "kb";
    kb.setAttribute("role", "group");
    kb.setAttribute("aria-label", "Playable piano keyboard, two octaves from C4");
    var whites = NOTES.filter(function (n) { return !n.black; });
    var whiteW = 100 / whites.length;
    var wIndex = 0;
    NOTES.forEach(function (n) {
      if (n.black) return;
      var k = document.createElement("div");
      k.className = "white";
      k.dataset.midi = n.midi;
      k.setAttribute("role", "button");
      k.setAttribute("aria-label", "Piano key " + n.name + n.oct);
      var lbl = document.createElement("span");
      lbl.className = "label" + (n.name === "C" && n.oct === 4 ? " mid" : "");
      lbl.textContent = (n.name === "C" && n.oct === 4) ? "middle C" : n.name;
      k.appendChild(lbl);
      kb.appendChild(k);
      n._wIndex = wIndex++;
    });
    NOTES.forEach(function (n) {
      if (!n.black) return;
      var prevWhite = null;
      for (var j = NOTES.indexOf(n) - 1; j >= 0; j--) {
        if (!NOTES[j].black) { prevWhite = NOTES[j]; break; }
      }
      var k = document.createElement("div");
      k.className = "black";
      k.dataset.midi = n.midi;
      k.setAttribute("role", "button");
      k.setAttribute("aria-label", "Piano key " + n.name + n.oct);
      k.style.left = ((prevWhite._wIndex + 1) * whiteW - 3.5) + "%";
      kb.appendChild(k);
    });
    container.appendChild(kb);
    return kb;
  }

  // ---------- state ----------
  var recording = false, recStart = 0, recNotes = [];
  var playbackTimers = [];

  function stopPlayback() {
    playbackTimers.forEach(clearTimeout);
    playbackTimers = [];
  }

  function press(kb, el, silent) {
    if (!el || !el.dataset.midi) return;
    var midi = parseInt(el.dataset.midi, 10);
    if (!silent) Audio.play(midi);
    el.classList.add("down");
    setTimeout(function () { el.classList.remove("down"); }, 200);
    if (recording) recNotes.push({ m: midi, t: Date.now() - recStart });
  }
  function light(kb, midi, on, silent) {
    var el = kb.querySelector('[data-midi="' + midi + '"]');
    if (!el) return;
    if (on) { el.classList.add("down"); if (!silent) Audio.play(midi); }
    else el.classList.remove("down");
  }
  function playSequence(kb, seq, doneCb) {
    stopPlayback();
    seq.forEach(function (n) {
      playbackTimers.push(setTimeout(function () {
        Audio.play(n.m);
        var el = kb.querySelector('[data-midi="' + n.m + '"]');
        if (el) { el.classList.add("down"); setTimeout(function(){ el.classList.remove("down"); }, 200); }
      }, n.t));
    });
    var end = seq.length ? seq[seq.length - 1].t + 400 : 0;
    playbackTimers.push(setTimeout(function () { if (doneCb) doneCb(); }, end));
  }
  function songSequence(song) {
    var beat = 60000 / song.bpm, t = 0, seq = [];
    song.seq.forEach(function (n) { seq.push({ m: n[0], t: t }); t += n[1] * beat; });
    return seq;
  }

  function init() {
    var mount = document.getElementById("opu-keyboard");
    if (!mount) return;
    var kb = build(mount);

    // pointer (mouse + touch + glissando)
    var pointerDown = false, lastKey = null;
    kb.addEventListener("pointerdown", function (e) {
      pointerDown = true; lastKey = e.target.closest("[data-midi]");
      press(kb, lastKey);
      e.preventDefault();
    });
    kb.addEventListener("pointermove", function (e) {
      if (!pointerDown) return;
      var el = document.elementFromPoint(e.clientX, e.clientY);
      var key = el && el.closest ? el.closest("[data-midi]") : null;
      if (key && key !== lastKey) { lastKey = key; press(kb, key); }
    });
    window.addEventListener("pointerup", function () { pointerDown = false; lastKey = null; });

    // computer keyboard
    var held = {};
    window.addEventListener("keydown", function (e) {
      if (e.repeat || e.metaKey || e.ctrlKey || e.altKey) return;
      var tag = (document.activeElement && document.activeElement.tagName) || "";
      if (tag === "INPUT" || tag === "TEXTAREA") return;
      var midi = KEYMAP[e.key.toLowerCase()];
      if (midi && !held[midi]) {
        held[midi] = true;
        press(kb, kb.querySelector('[data-midi="' + midi + '"]'));
      }
    });
    window.addEventListener("keyup", function (e) {
      var midi = KEYMAP[e.key.toLowerCase()];
      if (midi) held[midi] = false;
    });

    // Web MIDI
    var midiStatus = document.getElementById("kb-midi-status");
    if (navigator.requestMIDIAccess) {
      navigator.requestMIDIAccess().then(function (access) {
        function hook() {
          var found = false;
          access.inputs.forEach(function (input) {
            found = true;
            input.onmidimessage = function (msg) {
              var cmd = msg.data[0] & 0xf0, note = msg.data[1], vel = msg.data[2];
              if (cmd === 0x90 && vel > 0) {
                light(kb, note, true);
                if (recording) recNotes.push({ m: note, t: Date.now() - recStart });
              }
              if (cmd === 0x80 || (cmd === 0x90 && vel === 0)) light(kb, note, false, true);
            };
          });
          if (midiStatus) midiStatus.innerHTML = found
            ? "🎹 <b>MIDI piano connected</b> — play on your instrument!"
            : "Have a digital piano? Connect it by USB and it plays this keyboard.";
        }
        access.onstatechange = hook;
        hook();
      }, function () {});
    }

    // ---------- control buttons ----------
    var btnRec = document.getElementById("kb-rec");
    var btnPlay = document.getElementById("kb-play");
    var hint = document.getElementById("kb-hint");

    function setHint(msg) { if (hint) hint.innerHTML = msg; }

    if (btnRec) btnRec.addEventListener("click", function () {
      Audio.ensure();
      if (!recording) {
        recording = true; recNotes = []; recStart = Date.now();
        btnRec.textContent = "■ Stop";
        btnRec.classList.add("rec-on");
        if (btnPlay) btnPlay.disabled = true;
        setHint("Recording… play some keys, then press ■ Stop.");
      } else {
        recording = false;
        btnRec.textContent = "● Record";
        btnRec.classList.remove("rec-on");
        if (btnPlay) btnPlay.disabled = recNotes.length === 0;
        setHint(recNotes.length
          ? "Recorded <b>" + recNotes.length + " notes</b> — press ▶ to hear your melody!"
          : "Nothing recorded yet — press ● and play some keys.");
      }
    });

    if (btnPlay) {
      btnPlay.disabled = true;
      btnPlay.addEventListener("click", function () {
        if (!recNotes.length) return;
        Audio.ensure();
        setHint("Playing your melody…");
        var base = recNotes[0].t;
        playSequence(kb, recNotes.map(function (n) { return { m: n.m, t: n.t - base }; }),
          function () { setHint("That's <b>your</b> music. Ready to learn for real?"); });
      });
    }

    document.querySelectorAll("[data-kb-song]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var song = SONGS[btn.getAttribute("data-kb-song")];
        if (!song) return;
        Audio.ensure();
        setHint((song.by ? song.by + " — " : "") + "<b>" + song.name + "</b>. Watch the keys…");
        playSequence(kb, songSequence(song), function () {
          setHint("You could play this after a few lessons. <a href='free-course.html'>Start free →</a>");
        });
      });
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
