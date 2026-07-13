/* ============================================================
   OPU site config — ALL future hookups live here.
   When a product/service comes online, fill in the value below
   and the whole site updates. Nothing else to edit.
   ============================================================ */
window.OPU = {
  // Email provider form endpoint (MailerLite / Beehiiv / Kit).
  // Replace with the real form "action" URL from the provider.
  FORM_ACTION: "https://app.kit.com/forms/9663491/subscriptions", // Kit form "OPU Starter Guide" (connected 2026-07-09)

  // The free course (live now)
  COURSE_URL: "https://www.youtube.com/playlist?list=PLmHakdUcQbtSHDPhBQL8DLmiiKe3CsRzM",
  LESSON1_URL: "https://www.youtube.com/watch?v=AzU01rYWHK8",

  // Future products (placeholders until they ship)
  APP_URL: "",                           // ← Maestra app (future)
  BOOK_URL: "",                          // ← Masha's own method book (future)

  // Student submissions ("Send me your playing")
  SUBMIT_EMAIL: "",                      // ← dedicated address later (falls back to EMAIL)
  SUBMIT_FORM_URL: "",                   // ← hosted upload form (Tally etc., legacy option)
  BACKEND_URL: "https://opu-engine.onrender.com", // OPU Engine (Render, LIVE 2026-07-11) — upload form on submit.html active

  // Contact
  EMAIL: "maria@onlinepianouniversity.com",

  // Social
  YOUTUBE: "https://www.youtube.com/@ONLINEPIANOUNIVERSITY",
  INSTAGRAM: "https://www.instagram.com/online_piano_university/",
  FACEBOOK: "https://www.facebook.com/OnlinePianoUniversity/",
  TIKTOK: "https://www.tiktok.com/@online.piano.university",
  PINTEREST: "https://www.pinterest.com/OnlinePianoUniversity/"
};
