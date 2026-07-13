/* ============================================================
   OPU shared site behavior: nav, email forms, exit-intent, PWA
   ============================================================ */
(function () {
  "use strict";
  var C = window.OPU || {};

  // ----- mobile nav -----
  var toggle = document.querySelector(".nav-toggle");
  var links = document.querySelector(".nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      links.classList.toggle("open");
      toggle.setAttribute("aria-expanded", links.classList.contains("open"));
    });
  }

  // ----- email capture forms -----
  // Flow: email → the Starter Guide downloads IMMEDIATELY from this site,
  // and the address is quietly saved to the Kit list in the background.
  // No "confirm your subscription" step, no leaving the page.
  var GUIDE_PATH = "downloads/OPU_Piano_Starter_Guide.pdf";
  function ensureSink() {
    if (!document.getElementById("opu_sink")) {
      var f = document.createElement("iframe");
      f.name = "opu_sink"; f.id = "opu_sink";
      f.style.display = "none"; f.setAttribute("aria-hidden", "true");
      document.body.appendChild(f);
    }
  }
  function bindCapture(form) {
    // Real form POST to Kit into a hidden iframe (immune to fetch/CORS blocking),
    // while the user stays on the page: guide downloads instantly + success note.
    if (C.FORM_ACTION) {
      ensureSink();
      form.setAttribute("action", C.FORM_ACTION);
      form.setAttribute("method", "post");
      form.setAttribute("target", "opu_sink");
    }
    form.addEventListener("submit", function (e) {
      if (!C.FORM_ACTION) e.preventDefault();
      var input = form.querySelector('input[type="email"]');
      var ok = form.parentElement.querySelector(".form-ok");
      if (!input || !input.value) return;
      var a = document.createElement("a");
      a.href = GUIDE_PATH;
      a.download = "Piano_Starter_Guide_by_Dr_Maria_Pisarenko.pdf";
      document.body.appendChild(a);
      a.click();
      a.remove();
      if (ok) {
        ok.innerHTML = "✓ Your guide is downloading now — and a copy is on its way to your inbox! (If the download didn't start, <a href='" + GUIDE_PATH + "' download style='color:#bfe0c0;text-decoration:underline'>click here</a>.)";
        ok.style.display = "block";
      }
      setTimeout(function () { form.reset(); }, 2500);
    });
  }
  document.querySelectorAll("form.opu-capture").forEach(bindCapture);

  // ----- exit-intent popup (once per visit, desktop only) -----
  var shown = false;
  function exitPopup() {
    if (shown || sessionStorage.getItem("opu-exit-shown")) return;
    shown = true;
    try { sessionStorage.setItem("opu-exit-shown", "1"); } catch (e) {}
    var d = document.createElement("div");
    d.style.cssText = "position:fixed;inset:0;background:rgba(20,28,50,.72);z-index:200;display:grid;place-items:center;padding:20px";
    d.innerHTML =
      '<div class="capture" style="max-width:520px;position:relative">' +
      '<button aria-label="Close" style="position:absolute;top:10px;right:16px;background:none;border:none;color:#c9cee0;font-size:1.5rem;cursor:pointer">×</button>' +
      '<span class="eyebrow" style="color:var(--gold)">Before you go</span>' +
      "<h3 style='margin:.4rem 0'>Take the free Starter Guide with you</h3>" +
      '<p style="color:#d7dbe8;font-size:.95rem">The Adult Beginner’s Piano Starter Guide — start the right way, no bad habits to un-learn.</p>' +
      '<form class="opu-capture"><input type="email" name="email_address" placeholder="Your email" required aria-label="Your email">' +
      '<button class="btn" type="submit">Send me the guide</button></form>' +
      '<p class="form-ok">✓ Thank you — check your inbox!</p></div>';
    document.body.appendChild(d);
    d.querySelector("button[aria-label=Close]").addEventListener("click", function () { d.remove(); });
    d.addEventListener("click", function (e) { if (e.target === d) d.remove(); });
    bindCapture(d.querySelector("form"));
  }
  document.addEventListener("mouseout", function (e) {
    if (!e.relatedTarget && e.clientY <= 0) exitPopup();
  });

  // ----- future-product links (hidden until URLs exist) -----
  document.querySelectorAll("[data-opu-link]").forEach(function (el) {
    var url = C[el.getAttribute("data-opu-link")];
    if (url) { el.setAttribute("href", url); }
    else if (el.hasAttribute("data-opu-hide-empty")) { el.style.display = "none"; }
  });

  // ----- reveal-on-scroll animations -----
  var revealables = document.querySelectorAll("section .card, section h2, .videowrap, .kbwidget, .capture, .badges");
  if ("IntersectionObserver" in window && revealables.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.12 });
    revealables.forEach(function (el) { el.classList.add("reveal"); io.observe(el); });
  }

  // ----- PWA service worker -----
  if ("serviceWorker" in navigator && location.protocol === "https:") {
    navigator.serviceWorker.register("/sw.js").catch(function () {});
  }
})();
