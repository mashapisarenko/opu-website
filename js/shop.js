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
