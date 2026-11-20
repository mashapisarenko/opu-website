/* OPU shop: send a GA4 event when an affiliate button is clicked. Harmless if gtag is missing. */
(function () {
  "use strict";
  document.addEventListener("click", function (e) {
    try {
      var a = e.target && e.target.closest ? e.target.closest("a[data-asin]") : null;
      if (!a || typeof window.gtag !== "function") return;
      window.gtag("event", "affiliate_click", {
        category: a.getAttribute("data-category") || "",
        asin: a.getAttribute("data-asin") || ""
      });
    } catch (err) { /* never break the link */ }
  });
})();

/* 2026-11-20: lite YouTube embed. The thumbnail loads first; the player loads only on click (keeps pages fast). */
(function () {
  "use strict";
  document.addEventListener("click", function (e) {
    var a = e.target && e.target.closest ? e.target.closest("a.opu-yt[data-yt]") : null;
    if (!a) return;
    e.preventDefault();
    var f = document.createElement("iframe");
    f.src = "https://www.youtube-nocookie.com/embed/" + a.getAttribute("data-yt") + "?autoplay=1&rel=0";
    f.title = a.getAttribute("aria-label") || "Video";
    f.allow = "accelerometer; autoplay; encrypted-media; picture-in-picture";
    f.allowFullscreen = true;
    a.innerHTML = "";
    a.appendChild(f);
  });
})();
