/* ---- OPU gift certificate order form (rendered into <div data-gift-form>, gift-certificate.html only) ----
   Posts to the SAME backend endpoint as the generic form (/contact): need=gift, with a structured message block. */
(function () {
  var holder = document.querySelector("[data-gift-form]");
  if (!holder) return;
  var backend = ((window.OPU && window.OPU.BACKEND_URL) || "").replace(/\/$/, "");
  var MAIL = (window.OPU && window.OPU.EMAIL) || "maria@onlinepianouniversity.com";

  var PACKAGES = [
    { key: "850", label: "10 × 60 minutes", price: 850 },
    { key: "450", label: "10 × 30 minutes", price: 450 },
    { key: "360", label: "4 × 60 minutes", price: 360 },
    { key: "200", label: "4 × 30 minutes", price: 200 },
    { key: "100", label: "1 × 60 minutes", price: 100 },
    { key: "60", label: "1 × 30 minutes", price: 60 }
  ];
  var DESIGNS = [
    { v: "Christmas", img: "christmas" },
    { v: "New Year", img: "newyear" },
    { v: "Winter Holidays", img: "winter" },
    { v: "Classic", img: "classic" }
  ];
  var PAYMENTS = [
    { v: "paypal", t: "PayPal or card" },
    { v: "venmo", t: "Venmo" },
    { v: "cashapp", t: "Cash App" },
    { v: "zelle", t: "Zelle" },
    { v: "applecash", t: "Apple Cash" },
    { v: "invoice", t: "Send me a PayPal invoice" }
  ];
  var PAYNAME = {}; PAYMENTS.forEach(function (p) { PAYNAME[p.v] = p.t; });
  var HANDLES = {
    venmo: "Venmo: @Maria-Pisarenko",
    cashapp: "Cash App: $MariaPisarenko555",
    zelle: "Zelle: (702) 809-7576 (Maria Pisarenko)",
    applecash: "Apple Cash: (702) 809-7576 or masha.pisarenko@gmail.com"
  };
  var FOUND = [
    ["youtube", "YouTube"], ["google", "Google or another search engine"], ["instagram", "Instagram"],
    ["facebook", "Facebook"], ["tiktok", "TikTok"], ["pinterest", "Pinterest"],
    ["blog", "An article on this site"], ["friend", "A friend or a recommendation"],
    ["concert", "A concert, or mariapisarenko.com"], ["other", "Somewhere else"]
  ];

  // PayPal links are read from the #pay section so the page stays the single source of truth.
  function paypalFor(key) {
    var links = document.querySelectorAll("#pay .paylist a[href*='paypal.com']");
    for (var i = 0; i < links.length; i++) {
      if (links[i].href.indexOf("amount=" + key + ".00") > -1) return links[i].href;
    }
    return "";
  }
  function pkgByKey(k) { for (var i = 0; i < PACKAGES.length; i++) if (PACKAGES[i].key === k) return PACKAGES[i]; return null; }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  var opts = '<option value="">Choose a package</option>' + PACKAGES.map(function (p) {
    return '<option value="' + p.key + '">' + p.label + " — $" + p.price + "</option>";
  }).join("");
  var designs = DESIGNS.map(function (d, i) {
    return '<label class="gdesign"><input type="radio" name="design" value="' + d.v + '"' + (i === 0 ? " required" : "") + ">" +
      '<img src="images/gift/opu-gift-certificate-' + d.img + '.jpg" width="1200" height="776" loading="lazy" alt="' + d.v + ' certificate design">' +
      "<span>" + d.v + "</span></label>";
  }).join("");
  var pays = '<option value="">Choose one</option>' + PAYMENTS.map(function (p) { return '<option value="' + p.v + '">' + p.t + "</option>"; }).join("");
  var found = '<option value="">Choose one</option>' + FOUND.map(function (f) { return '<option value="' + f[0] + '">' + f[1] + "</option>"; }).join("");

  holder.innerHTML =
    '<form class="ofrm giftfrm" novalidate>' +
    '<h4 class="gsub">1. The gift</h4>' +
    '<div class="ofrow"><div><label for="g-rname">Recipient&rsquo;s name *</label><input id="g-rname" name="recipient_name" autocomplete="off" placeholder="As it should appear on the certificate"></div>' +
    '<div><label for="g-from">From *</label><input id="g-from" name="from_line" autocomplete="off" placeholder="e.g. With love, Anna and Mark"></div></div>' +
    '<label id="g-dlabel">Certificate design *</label><div class="gdesigns" role="radiogroup" aria-labelledby="g-dlabel">' + designs + "</div>" +
    '<div class="ofrow"><div><label for="g-pkg">Package *</label><select id="g-pkg" name="package">' + opts + "</select></div>" +
    '<div><label for="g-date">Delivery date <span>(optional)</span></label><input id="g-date" name="deliver_on" type="date"><small class="ghint">Send it on this date. Leave empty to send it as soon as it is ready.</small></div></div>' +
    '<label for="g-remail">Recipient&rsquo;s email <span>(optional)</span></label><input id="g-remail" name="recipient_email" type="email" autocomplete="off" placeholder="If you would like me to send it to them directly on the date you choose">' +
    '<h4 class="gsub">2. About you</h4>' +
    '<div class="ofrow"><div><label for="g-name">Your name *</label><input id="g-name" name="buyer_name" autocomplete="name"></div>' +
    '<div><label for="g-email">Your email *</label><input id="g-email" name="email" type="email" autocomplete="email"></div></div>' +
    '<div class="ofrow"><div><label for="g-phone">Your phone <span>(optional)</span></label><input id="g-phone" name="phone" type="tel" autocomplete="tel"></div>' +
    '<div><label for="g-found">How did you find us? *</label><select id="g-found" name="found_via">' + found + "</select></div></div>" +
    '<h4 class="gsub">3. Payment</h4>' +
    '<label for="g-pay">Payment method *</label><select id="g-pay" name="payment">' + pays + "</select>" +
    '<label for="g-msg">A message <span>(optional)</span></label><textarea id="g-msg" name="message" placeholder="Anything you would like me to know, or a short note for the certificate"></textarea>' +
    '<div class="ofhp" aria-hidden="true"><label>Leave this empty<input name="website" tabindex="-1" autocomplete="off"></label></div>' +
    '<div class="ofact"><button class="btn" type="submit">Send my gift order</button><span class="ofalt">Or email <a href="mailto:' + MAIL + '">' + MAIL + "</a></span></div>" +
    '<p class="ofmsg err" role="alert" style="display:none"></p></form>' +
    '<div class="gthanks" tabindex="-1" style="display:none"></div>';

  var f = holder.querySelector("form"), err = f.querySelector(".ofmsg.err"), btn = f.querySelector("button[type=submit]"), thanks = holder.querySelector(".gthanks");
  function v(name) { var e = f.elements[name]; return e && e.value ? e.value.trim() : ""; }
  (function () { var d = new Date(), z = function (n) { return (n < 10 ? "0" : "") + n; }; f.elements.deliver_on.min = d.getFullYear() + "-" + z(d.getMonth() + 1) + "-" + z(d.getDate()); })();
  function design() { var c = f.querySelector("input[name=design]:checked"); return c ? c.value : ""; }
  function fail(m, el) { err.textContent = m; err.style.display = "block"; if (el && el.focus) el.focus(); return false; }
  var EMAILRE = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;

  function validate() {
    err.style.display = "none";
    if (!v("recipient_name")) return fail("Please enter the recipient’s name as it should appear on the certificate.", f.elements.recipient_name);
    if (!v("from_line")) return fail("Please enter the From line, for example “With love, Anna and Mark”.", f.elements.from_line);
    if (!design()) return fail("Please choose a certificate design.", f.querySelector("input[name=design]"));
    if (!v("package")) return fail("Please choose a package.", f.elements["package"]);
    if (v("deliver_on") && v("deliver_on") < f.elements.deliver_on.min) return fail("The delivery date is in the past. Please choose today or a later date, or leave it empty.", f.elements.deliver_on);
    if (v("recipient_email") && !EMAILRE.test(v("recipient_email"))) return fail("The recipient’s email does not look right. Leave it empty if you prefer.", f.elements.recipient_email);
    if (!v("buyer_name")) return fail("Please enter your name.", f.elements.buyer_name);
    if (!EMAILRE.test(v("email"))) return fail("Please enter your email so I can send the receipt and the certificate.", f.elements.email);
    if (!v("payment")) return fail("Please choose a payment method.", f.elements.payment);
    if (!v("found_via")) return fail("Please tell me how you found us.", f.elements.found_via);
    return true;
  }

  function block() {
    var p = pkgByKey(v("package"));
    return [
      "GIFT CERTIFICATE ORDER",
      "Package: " + p.label + " online piano lessons",
      "Amount: $" + p.price,
      "Design: " + design(),
      "Recipient: " + v("recipient_name"),
      "From: " + v("from_line"),
      "Recipient email: " + (v("recipient_email") || "(none)"),
      "Deliver on: " + (v("deliver_on") || "as soon as ready"),
      "Payment method: " + PAYNAME[v("payment")],
      "Buyer: " + v("buyer_name") + " / " + v("email") + " / " + (v("phone") || "(no phone)"),
      "Note: " + (v("message") || "(none)")
    ].join("\n");
  }
  function mailto() {
    return "mailto:" + MAIL + "?subject=" + encodeURIComponent("Gift certificate order") + "&body=" + encodeURIComponent(block());
  }

  function showThanks(viaMail) {
    var p = pkgByKey(v("package")), pay = v("payment"), h = "";
    h += "<h3>" + (viaMail ? "Almost done: send the email" : "Thank you, your order is in") + "</h3>";
    if (viaMail) h += "<p>Your email app should have opened with the order filled in. Press Send to place the order. If nothing opened, write to <a href=\"mailto:" + MAIL + "\">" + MAIL + "</a>.</p>";
    h += "<p><b>" + esc(p.label) + "</b> for <b>" + esc(v("recipient_name")) + "</b>, " + esc(design()) + " design, <b>$" + p.price + "</b>.</p>";
    if (pay === "paypal") {
      var link = paypalFor(p.key);
      h += "<p>Last step: pay now. Any credit or debit card works, and no PayPal account is needed.</p>";
      if (link) h += '<p><a class="btn gpaybtn" href="' + esc(link) + '" target="_blank" rel="noopener">Pay $' + p.price + " with PayPal or card &rarr;</a></p>";
      else h += '<p><a class="btn gpaybtn" href="#pay">See how to pay &darr;</a></p>';
    } else if (pay === "invoice") {
      h += "<p>I will email you a PayPal invoice shortly. Nothing else to do until it arrives.</p>";
    } else {
      h += "<p>Last step: send <b>$" + p.price + "</b> by " + esc(PAYNAME[pay]) + ".</p><p class=\"gpayhandle\">" + esc(HANDLES[pay]) + "</p>" +
        '<p>The QR code and the exact details are in <a href="#pay">How to pay</a> above. Please put the recipient’s name and “gift certificate” in the payment note.</p>';
    }
    h += "<p><b>Your certificate arrives by email within 24 hours after payment.</b></p>";
    thanks.innerHTML = h;
    f.style.display = "none"; thanks.style.display = "block";
    try { thanks.scrollIntoView({ behavior: "smooth", block: "start" }); thanks.focus({ preventScroll: true }); } catch (e) {}
    if (window.gtag) gtag("event", "gift_order_sent", { package: p.label + " ($" + p.price + ")", design: design(), value: p.price, currency: "USD" });
  }

  f.addEventListener("submit", function (ev) {
    ev.preventDefault();
    if (!validate()) return;
    if (!backend) { window.location.href = mailto(); showThanks(true); return; }
    btn.disabled = true; btn.textContent = "Sending...";
    var fd = new FormData();
    fd.append("name", v("buyer_name")); fd.append("email", v("email")); fd.append("phone", v("phone"));
    fd.append("found_via", v("found_via")); fd.append("found_other", ""); fd.append("need", "gift");
    fd.append("message", block()); fd.append("website", v("website"));
    fetch(backend + "/contact", { method: "POST", body: fd }).then(function (r) { return r.json(); }).then(function (d) {
      if (!(d && d.ok)) throw new Error((d && d.error) || "failed");
      showThanks(false);
    }).catch(function (e) {
      btn.disabled = false; btn.textContent = "Send my gift order";
      err.innerHTML = (e && e.message && e.message !== "failed" && e.message !== "Failed to fetch" ? esc(e.message) + " " : "The form could not send just now. ") +
        '<a href="' + mailto() + '">Send the same order by email</a>.';
      err.style.display = "block";
    });
  });

  // Package buttons on the page preselect the package here.
  function preselect(key) {
    if (!pkgByKey(key)) return false;
    f.elements["package"].value = key; return true;
  }
  document.addEventListener("click", function (ev) {
    var a = ev.target.closest && ev.target.closest("a"); if (!a) return;
    var key = "", m;
    if (a.hasAttribute("data-gift-pkg") && (m = a.getAttribute("data-gift-pkg").match(/\$(\d+)\)\s*$/))) key = m[1];
    else if (a.closest("#pricing") && (m = (a.getAttribute("href") || "").match(/amount=(\d+)\.00/)) && a.href.indexOf("paypal.com") > -1) key = m[1];
    if (!key || !preselect(key)) return;
    if (a.hasAttribute("data-gift-pkg")) {
      ev.preventDefault();
      thanks.style.display = "none"; f.style.display = "";
      var t = document.getElementById("order"); if (t) t.scrollIntoView({ behavior: "smooth", block: "start" });
      try { history.replaceState(null, "", "#order"); } catch (e) {}
    } else if (!v("payment")) { f.elements.payment.value = "paypal"; } // PayPal button opens in a new tab; the form stays ready behind it
  });

  if (backend) { try { fetch(backend + "/health", { mode: "cors" }).catch(function () {}); } catch (e) {} }
})();
