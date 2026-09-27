(() => {
  const root = document.documentElement;
  const key = "thukydides-theme";
  const fontKey = "thukydides-font";
  const fonts = ["unifrakturmaguntia", "pirataone", "medievalsharp", "almendra", "ebgaramond", "crimsontext", "sourceserif4", "sourcesans3"];
  const defaultFont = root.lang === "grc" ? "sourceserif4" : root.lang === "he" ? "sourcesans3" : "almendra";
  let font;
  try { font = localStorage.getItem(fontKey); } catch { /* Use default without storage. */ }
  if (!fonts.includes(font)) font = defaultFont;
  root.dataset.font = font;
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
    const fontSelect = document.getElementById("font-select");
    fontSelect.value = font;
    fontSelect.addEventListener("change", () => {
      font = fonts.includes(fontSelect.value) ? fontSelect.value : defaultFont;
      root.dataset.font = font;
      try { localStorage.setItem(fontKey, font); } catch { /* Selection works without persistence. */ }
    });
    button.closest(".reader-toolbar").hidden = false;
    button.addEventListener("click", () => {
      chosen = current() === "dark" ? "light" : "dark";
      try { localStorage.setItem(key, chosen); } catch { /* Switching still works without persistence. */ }
      apply();
    });
    apply();
  });
})();
