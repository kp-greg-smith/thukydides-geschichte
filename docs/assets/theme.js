(() => {
  const root = document.documentElement;
  const key = "thukydides-theme";
  const preference = window.matchMedia("(prefers-color-scheme: light)");
  let chosen;
  try { chosen = localStorage.getItem(key); } catch { /* Storage can be unavailable for local files. */ }
  if (chosen !== "light" && chosen !== "dark") chosen = null;
  const current = () => chosen || (preference.matches ? "light" : "dark");
  function apply() {
    root.dataset.theme = current();
    const button = document.getElementById("theme-toggle");
    if (button) button.setAttribute("aria-pressed", String(current() === "dark"));
  }
  apply();
  preference.addEventListener("change", apply);
  document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("theme-toggle");
    button.closest(".reader-toolbar").hidden = false;
    button.addEventListener("click", () => {
      chosen = current() === "dark" ? "light" : "dark";
      try { localStorage.setItem(key, chosen); } catch { /* Switching still works without persistence. */ }
      apply();
    });
    apply();
  });
})();
