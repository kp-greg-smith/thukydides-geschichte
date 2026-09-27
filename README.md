# Thucydides: Der Peloponnesische Krieg

A modern German translation of Thucydides' *History of the Peloponnesian War* — all eight books, translated directly from the Ancient Greek.

## What this repository contains

- **Complete German translation** of Thucydides in three formats:
  - **Markdown** (`.md`) — readable plain text with section numbering
  - **HTML** (`.html`) — styled for browser reading
  - **PDF** (`.pdf`) — printable A4, serif typeface

## Source text

The Greek source is the Perseus Digital Library edition:

> Thucydides. *Historiae*. Edited by Henry Stuart Jones. Oxford: Oxford University Press, 1910/1942.  
> [PerseusDL/canonical-greekLit](https://github.com/PerseusDL/canonical-greekLit) — `tlg0003.tlg001.perseus-grc2.xml`

Licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

## Translation principles

This translation follows five strict rules, applied consistently across all eight books:

| Rule | Description |
|------|-------------|
| **1. Consistent key terms** | Greek political vocabulary is rendered with a fixed German equivalent throughout: πρόφασις → *wahrer Grund*, αἰτία → *Vorwurf*, στάσις → *Bürgerkrieg*, δύναμις → *Macht*, παρασκευή → *Rüstung*, δουλεία → *Knechtschaft* |
| **2. Nothing added, nothing exaggerated** | No embellishments, no intensifiers absent from the Greek |
| **3. No softening** | Where Thucydides is harsh, the translation stays harsh (δουλεία is always *Knechtschaft*, never a softer term) |
| **4. Annotations only for genuine doubts** | Notes (marked `[Anm.: ...]`) appear only where the manuscript text is corrupt or the reading is genuinely disputed |
| **5. Preserving ambiguities** | Where the Greek is genuinely ambiguous (Thucydides wrote in *scriptio continua* without word separation, punctuation, or paragraphs), the ambiguity is preserved rather than resolved by the translator |

## Why a new translation?

The existing German translation in the [PerseusDL/canonical-greekLit](https://github.com/PerseusDL/canonical-greekLit) repository (Braun, 1917) is a free, literary translation that by the translator's own admission takes "liberties in detail" and follows the style of a 1760 rendering. It also contains OCR errors from digitisation.

This translation aims at a different goal: a philologically precise, modern German text that can be read alongside the Greek for study and comparison.

### Comparison with Braun (1917)

| Passage | The Greek says | Braun | This translation |
|---------|---------------|-------|-------------------|
| 1.2 | Greeks, a part of the barbarians, and the greatest part of mankind | combines into "a part of the barbarians, I might say of mankind" | kept separate, as in the original |
| 8.1 | The islanders were no less pirates | "The worst pirates" (exaggeration) | "not less" |
| 21.1 | Modest: sufficiently established, as far as possible for such ancient matters | Confident: "drawn only from the best sources" | modest, as in the original |
| 23.6 | The Athenians' growth in power compelled Sparta to war. προφασις (true cause) distinct from αἰτίαι (complaints) | Subject becomes "Fear of the Lacedaemonians", conflates the two terms | Athenians as subject; terms kept distinct |

## Structure

| Book | Chapters | Content |
|------|----------|---------|
| 1 | 146 | Archaeology, causes of the war, Kerkyra, Potidaia, Congress at Sparta, Pericles' speech |
| 2 | 103 | Outbreak of war, Pericles' Funeral Oration, the Plague |
| 3 | 116 | Revolt of Mytilene, Plataea, Civil war at Kerkyra |
| 4 | 135 | Pylos and Sphacteria, Brasidas in Thrace |
| 5 | 116 | Peace of Nicias, Melian Dialogue |
| 6 | 105 | Sicilian Expedition |
| 7 | 87 | Sicilian disaster |
| 8 | 109 | The Decelean War, Oligarchy of the Four Hundred |

## Section numbering

Sections are marked with **§** (e.g., **§1**, **§2**), following the standard Oxford Classical Text chapter/section division established by Henry Stuart Jones (1910). This matches the Perseus XML `cRefPattern` numbering and allows precise cross-referencing with the Greek text.

Thucydides himself wrote on papyrus rolls in continuous script (*scriptio continua*) — without word separation, without punctuation, without paragraphs. The section numbers are a modern editorial convention, like Bible verses, not part of the original text.

## Building

```bash
# Generate Markdown, HTML, and PDF for all books
python3 buch1/translation.py
python3 buch2/translation.py
# ... books 3–8

# Requires pandoc + xelatex for PDF output
sudo apt install pandoc texlive-xetex
```

## Output files

```
output/
├── buch1.md       # Book 1 — Markdown
├── buch1.html     # Book 1 — HTML
├── buch1.pdf      # Book 1 — PDF
├── buch2.md
├── ...
└── buch8.pdf
```

## License

This translation is dedicated to the public domain under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).

The Greek source text from the Perseus Digital Library is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

## See also

- [PerseusDL/canonical-greekLit](https://github.com/PerseusDL/canonical-greekLit) — Greek source XML
- [Scaife Viewer](https://scaife.perseus.org/library/urn:cts:greekLit:tlg0003.tlg001/) — online reading environment
- [ToposText](https://topostext.org/work/52) — Thucydides with maps
