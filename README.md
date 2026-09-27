# Thucydides: History of the Peloponnesian War

[English](README.md) · [Deutsch](README_DE.md) · [Українська](README_UK.md) · [עברית](README_HE.md) · [Ἑλληνική](README_GRC.md)

A multilingual HTML reading edition of the Ancient Greek original and direct translations into German, English, Ukrainian, and Hebrew. The goal covers all eight books; the translations are not yet complete. This scope update adds no new translations.

[Open the reading portal](docs/index.html). It lists the current status and links only to editions that exist.

## Available editions

| Language | Role | Books available | Remaining work |
|---|---|---|---|
| Ancient Greek (`grc`) | **Original**, not a translation | [Books 1–8](docs/grc/book1.html), imported from the cited edition | Further editorial checks; no new transcription claimed |
| German (`de`) | Translation | [Book 1](docs/de/book1.html): 146 chapters, 580 sections | Books 2–8 not started |
| English (`en`) | Translation | None | Books 1–8 planned |
| Ukrainian (`uk`) | Translation | None | Books 1–8 planned |
| Hebrew (`he`) | Translation, right-to-left | None | Books 1–8 planned |

“Available” describes coverage, not a guarantee that no corrections remain. German Book 1 has an existing revision history, including the section-by-section review of chapters 31–117 recorded on 2026-09-27. This scope update preserves all 580 German sections; it does not claim a new philological review. Translated READMEs describe the project and do not count as translated books.

## Translation policy

Translate faithfully and readably, not word for word, and directly from Ancient Greek. Braun, Hobbes, Crawley, and other translations may only help with understanding; they must not serve as the source text or be copied as the translation.

1. **Consistency by sense.** Use a stable equivalent for each meaning, not a single equivalent for every occurrence of a word. In particular, αἰτία may mean accusation, cause, blame, or responsibility; do not prohibit a causal rendering where the Greek requires it.
2. **No additions or exaggeration.** Do not introduce explanations, imagery, claims, or emphasis absent from the Greek.
3. **No softening.** Preserve the force of harsh statements and political vocabulary; for example, German δουλεία remains *Knechtschaft* in that sense.
4. **Notes for genuine uncertainty.** Add a brief note for textual uncertainty, genuine interpretive questions, or a significant change in a key term’s sense. Notes are not limited to damaged or corrupt text. German notes use `[Anm.: …]`; other languages use an equivalent label.
5. **Preserve ambiguity.** Where the Greek allows more than one reading, retain that openness where possible rather than silently choosing one. Explain unavoidable choices in a brief note.
6. **Extra care with speeches and indirect speech.** Preserve the speaker, addressee, argument, reported viewpoint, conditions, negation, modality, and temporal relations. Do not turn reported claims into the narrator’s assertions.

### Language-specific glossaries

The existing [German glossary](README_DE.md#glossar-der-vorhandenen-deutschen-übersetzung) is documented in the German README. English, Ukrainian, and Hebrew glossaries have not yet been established. Before translating into each language, define consistent equivalents by meaning directly from the Greek; context governs words with multiple senses.

## Workflow for future books and languages

1. Work on **at most ten chapters per assignment**. State the language, book, chapter range, and source edition before starting.
2. Keep the actual Greek source beside the translation **section by section**, using book.chapter.section identifiers. Check every passage against Greek, not only against another translation.
3. After each batch, run an **automatic check of section counts/identifiers, source-to-translation length ratios, and potentially unfinished sentences**. The local checker below reports missing/duplicate sections as errors and unusual ratios or sentence endings as review warnings.
4. Resolve structural errors and manually inspect every warning against the Greek. Length and punctuation checks are heuristics, not proof of translation quality. Review speeches and indirect speech separately.
5. Publish only existing HTML editions under `docs/<language>/book<N>.html`. Retain section IDs, set `lang="grc"`, `"de"`, `"en"`, `"uk"`, or `"he"`; Hebrew also needs `dir="rtl"`. Add tested glyph coverage for the language. Do not create empty book links.
6. Update the reading portal and all five READMEs in the same change. Record exact coverage and distinguish planned, in-progress, available, and reviewed work. Preserve all six rules when adding an edition.

```bash
python3 scripts/check_translation.py --language de --book 1 --start 1 --end 10
python3 scripts/build_original.py
```

## Repository and reader

- `docs/index.html`: reading portal and language status.
- `docs/grc/book1.html` … `book8.html`: Ancient Greek **Original**.
- `docs/grc/source.xml` and `source.json`: unmodified source and pinned provenance/hash.
- `docs/de/book1.html`: the authoritative German edition; `docs/buch1.html` redirects old links.
- `docs/assets/`: shared reader controls and eight locally bundled OFL fonts.
- `scripts/`: original-text renderer and batch checker; `review/`: existing editorial notes.
- `README.md`: English project documentation; `README_DE.md`, `README_UK.md`, `README_HE.md`, `README_GRC.md`: localized documentation.

There is no Markdown edition of the work and no `de_translations/` directory. Markdown remains in use for documentation and review notes. No build is required to read the HTML: open `docs/index.html` or serve `docs/` with GitHub Pages. The reader offers saved font and light/dark choices; dark mode uses warm yellow on black, light mode muted papyrus. Greek defaults to Source Serif 4; Hebrew editions must use RTL layout and suitable glyph fallbacks.

## Source, attribution, and licenses

The **Original** reproduces the text of the cited modern edition, not an autograph or an independently established critical text:

> Thucydides, *Historiae*, edited by Henry Stuart Jones. Oxford University Press, 1910; reprint 1942. Digital text: Perseus Digital Library, Tufts University, [PerseusDL/canonical-greekLit](https://github.com/PerseusDL/canonical-greekLit).

The exact revision, source URL, SHA-256, and transformation are recorded in [source.json](docs/grc/source.json). The HTML normalizes whitespace and adds headings, section IDs, and navigation; it does not modernize or translate the wording. Preserve the source attribution and [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) for the source and the derived Greek HTML.

The existing German translation is released under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/); document the licensing of future contributions explicitly. Fonts retain their own [SIL OFL 1.1 licenses and copyright notices](docs/assets/fonts/README.md), separate from text licenses. Embedding and redistribution with the project are permitted under those terms.

## Book structure

| Book | Chapters | Greek sections |
|---|---|---|
| 1 | 146 | 580 |
| 2 | 103 | 463 |
| 3 | 116 | 470 |
| 4 | 135 | 531 |
| 5 | 116 | 391 |
| 6 | 105 | 391 |
| 7 | 87 | 363 |
| 8 | 109 | 398 |

Book 1: early history (1–23), Corcyra (24–55), Potidaea and Sparta (56–88), Pentekontaetia (89–118), Corinthian speech and deliberations (119–125), Cylon, Pausanias, and Themistocles (126–138), final negotiations (139), Pericles’ speech (140–144), and the final pre-war situation (145–146). Section numbers follow the cited edition; use `§` in the reader.
