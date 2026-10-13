
/* ---- OPU contact + recording form (rendered into every <div data-opu-form>) ---- */
(function () {
  var holders = document.querySelectorAll("[data-opu-form]");
  if (!holders.length) return;
  var backend = ((window.OPU && window.OPU.BACKEND_URL) || "").replace(/\/$/, "");
  var MAIL = "maria@onlinepianouniversity.com";
  if (backend) { try { fetch(backend + "/health", { mode: "cors" }).catch(function () {}); } catch (e) {} } // wake the engine

  var lessons = "";
  for (var i = 1; i <= 41; i++) lessons += '<option value="' + i + '">Lesson ' + i + "</option>";

  holders.forEach(function (h, n) {
    var p = "of" + n + "-";
    h.innerHTML =
      '<form class="ofrm" novalidate>' +
      '<div class="ofrow"><div><label for="' + p + 'name">Your name</label><input id="' + p + 'name" name="name" autocomplete="name"></div>' +
      '<div><label for="' + p + 'email">Email *</label><input id="' + p + 'email" name="email" type="email" autocomplete="email" required></div></div>' +
      '<div class="ofrow"><div><label for="' + p + 'phone">Phone <span>(optional)</span></label><input id="' + p + 'phone" name="phone" type="tel" autocomplete="tel"></div>' +
      '<div><label for="' + p + 'found">How did you find us?</label><select id="' + p + 'found" name="found_via"><option value="">Choose one</option>' +
      '<option value="youtube">YouTube</option><option value="google">Google or another search engine</option><option value="instagram">Instagram</option>' +
      '<option value="facebook">Facebook</option><option value="tiktok">TikTok</option><option value="pinterest">Pinterest</option>' +
      '<option value="blog">An article on this site</option><option value="friend">A friend or a recommendation</option>' +
      '<option value="concert">A concert, or mariapisarenko.com</option><option value="other">Somewhere else</option></select></div></div>' +
      '<div class="ofrow"><div><label for="' + p + 'need">What can I help with?</label><select id="' + p + 'need" name="need">' +
      '<option value="feedback">Feedback on my playing</option><option value="lessons">Private 1-on-1 lessons on Zoom</option>' +
      '<option value="returning">I played as a child and want to come back</option><option value="course">A question about the free course</option>' +
      '<option value="book">A question about a book</option><option value="press">Press, concerts or collaboration</option><option value="other">Something else</option></select></div>' +
      '<div><label for="' + p + 'where">Where exactly? <span>(optional)</span></label><input id="' + p + 'where" name="found_other" placeholder="e.g. the video on middle C"></div></div>' +
      '<label for="' + p + 'msg">Your message</label><textarea id="' + p + 'msg" name="message" placeholder="What would you like to play, and what feels hard?"></textarea>' +
      '<div class="ofrec"><label for="' + p + 'file"><b>Attach a recording of your playing</b> <span>(optional; audio alone is enough)</span></label>' +
      '<input id="' + p + 'file" type="file" name="file" accept="audio/*,video/*,.m4a,.mp3,.wav,.mp4,.mov">' +
      '<div class="ofrecmore" style="display:none"><label for="' + p + 'lesson">Which lesson did you play?</label><select id="' + p + 'lesson" name="lesson"><option value="">Choose a lesson</option>' + lessons + '</select>' +
      '<label class="ofchk"><input type="checkbox" name="consent" value="on"> I am sending this recording so Dr. Pisarenko can give me written feedback by email.</label></div></div>' +
      '<div class="ofhp" aria-hidden="true"><label>Leave this empty<input name="website" tabindex="-1" autocomplete="off"></label></div>' +
      '<div class="ofact"><button class="btn" type="submit">Send</button><span class="ofalt">Or email <a href="mailto:' + MAIL + '">' + MAIL + '</a></span></div>' +
      '<p class="ofmsg ok" style="display:none">Thank you. It is on its way to me, and I read and answer every one myself. Feedback on a recording arrives by email.</p>' +
      '<p class="ofmsg err" style="display:none"></p></form>';

    var f = h.querySelector("form"), file = f.querySelector('input[type="file"]'), more = f.querySelector(".ofrecmore");
    var ok = f.querySelector(".ofmsg.ok"), err = f.querySelector(".ofmsg.err"), btn = f.querySelector("button");
    file.addEventListener("change", function () { more.style.display = file.files.length ? "block" : "none"; });
    function v(name) { var e = f.elements[name]; return e ? (e.value || "").trim() : ""; }
    function mailto() {
      var body = "Name: " + v("name") + "\nPhone: " + v("phone") + "\nHow I found you: " + v("found_via") + "\n\n" + v("message");
      return "mailto:" + MAIL + "?subject=" + encodeURIComponent("Website message") + "&body=" + encodeURIComponent(body);
    }
    function post(path, fd) {
      return fetch(backend + path, { method: "POST", body: fd }).then(function (r) { return r.json(); });
    }
    f.addEventListener("submit", function (ev) {
      ev.preventDefault(); err.style.display = "none";
      if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(v("email"))) { err.textContent = "Please enter your email so I can reply."; err.style.display = "block"; return; }
      var hasFile = file.files.length > 0;
      if (hasFile && (!v("lesson") || !f.elements.consent.checked)) { err.textContent = "For a recording, please choose the lesson and tick the box."; err.style.display = "block"; return; }
      if (!backend) { window.location.href = mailto(); return; }
      btn.disabled = true; btn.textContent = "Sending...";
      var fd = new FormData();
      ["name", "email", "found_via", "found_other", "need", "message", "website"].forEach(function (k) { fd.append(k, v(k)); });
      fd.append("phone", v("phone"));
      var jobs = [post("/contact", fd)];
      if (hasFile) {
        var sd = new FormData();
        sd.append("email", v("email")); sd.append("lesson", v("lesson")); sd.append("consent", "on");
        sd.append("note", v("message").slice(0, 500)); sd.append("file", file.files[0]);
        jobs.push(post("/submit", sd));
      }
      Promise.all(jobs).then(function (res) {
        var bad = res.filter(function (d) { return !(d && d.ok); })[0];
        if (bad) throw new Error(bad.error || "failed");
        f.querySelectorAll("input,select,textarea,button").forEach(function (x) { x.disabled = true; });
        ok.style.display = "block";
        if (window.gtag) gtag("event", "opu_form_sent", { found_via: v("found_via"), recording: hasFile ? 1 : 0 });
      }).catch(function (e) {
        btn.disabled = false; btn.textContent = "Send";
        err.innerHTML = (e && e.message && e.message !== "failed" && e.message !== "Failed to fetch" ? e.message + " " : "The form could not send just now. ") +
          '<a href="' + mailto() + '">Send the same message by email</a>.';
        err.style.display = "block";
      });
    });
  });

  // top band toggle
  document.querySelectorAll("[data-opu-toggle]").forEach(function (b) {
    b.addEventListener("click", function () {
      var panel = document.querySelector(".contactpanel"); if (!panel) return;
      var open = panel.style.display === "block"; panel.style.display = open ? "none" : "block";
      b.setAttribute("aria-expanded", open ? "false" : "true");
    });
  });
})();
