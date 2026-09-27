# Thukydides: Der Peloponnesische Krieg

[English](README.md) · [Deutsch](README_DE.md) · [Українська](README_UK.md) · [עברית](README_HE.md) · [Ἑλληνική](README_GRC.md)

Eine mehrsprachige HTML-Leseausgabe des altgriechischen Originals und direkter Übersetzungen ins Deutsche, Englische, Ukrainische und Hebräische. Das Ziel umfasst alle acht Bücher; die Übersetzungen sind noch nicht vollständig. Diese Erweiterung des Projektumfangs fügt keine neuen Übersetzungen hinzu.

[Leseportal öffnen](docs/index.html). Es zeigt den aktuellen Stand und verlinkt nur vorhandene Ausgaben.

## Vorhandene Ausgaben

| Sprache | Rolle | Vorhanden | Noch offen |
|---|---|---|---|
| Altgriechisch (`grc`) | **Original**, keine Übersetzung | [Bücher 1–8](docs/grc/book1.html), aus der angegebenen Edition übernommen | Weitere redaktionelle Prüfung; keine neue Transkription |
| Deutsch (`de`) | Übersetzung | [Buch 1](docs/de/book1.html): 146 Kapitel, 580 Abschnitte | Bücher 2–8 nicht begonnen |
| Englisch (`en`) | Übersetzung | Keine Bücher | Bücher 1–8 geplant |
| Ukrainisch (`uk`) | Übersetzung | Keine Bücher | Bücher 1–8 geplant |
| Hebräisch (`he`) | Übersetzung, von rechts nach links | Keine Bücher | Bücher 1–8 geplant |

„Vorhanden“ bezeichnet den Umfang, keine Fehlerfreiheit. Buch 1 hat eine bestehende Überarbeitungsgeschichte, einschließlich der am 27.09.2026 dokumentierten abschnittweisen Prüfung der Kapitel 31–117. Diese Umstellung erhält alle 580 deutschen Abschnitte; sie ist keine erneute philologische Prüfung. Übersetzte READMEs sind Projektdokumentation und zählen nicht als übersetzte Bücher.

## Übersetzungsgrundsätze

Sinngetreu und gut lesbar übersetzen, nicht Wort für Wort, und ausschließlich aus dem Altgriechischen. Braun, Hobbes, Crawley und andere Übersetzungen dürfen höchstens als Verständnishilfe dienen; sie sind weder Ausgangstext noch zu übernehmende Übersetzung.

1. **Einheitliche Entsprechung je Bedeutung.** Nicht ein deutsches Wort für jedes Vorkommen erzwingen. αἰτία kann Vorwurf, Ursache, Schuld oder Verantwortung bedeuten; eine kausale Übersetzung darf nicht ausgeschlossen werden, wenn der griechische Sinn sie verlangt.
2. **Nichts hinzufügen oder steigern.** Keine Erklärungen, Bilder, Behauptungen oder Hervorhebungen ergänzen, die im Griechischen fehlen.
3. **Nicht abschwächen.** Die Härte von Aussagen und politischem Vokabular bewahren; δουλεία bleibt in dieser Bedeutung *Knechtschaft*.
4. **Anmerkungen bei echten Zweifeln.** Kurze Anmerkungen bei textkritischer Unsicherheit, echten Deutungsfragen oder einem bedeutsamen Bedeutungswechsel eines Schlüsselbegriffs. Nicht auf beschädigten oder verderbten Text beschränken. Deutsch: `[Anm.: …]`; andere Sprachen verwenden eine entsprechende Kennzeichnung.
5. **Mehrdeutigkeiten bewahren.** Lässt der griechische Text mehrere Lesarten zu, diese Offenheit möglichst erhalten. Unvermeidliche Entscheidungen kurz erläutern.
6. **Besondere Sorgfalt bei Reden und indirekter Rede.** Sprecher, Adressat, Argumentation, wiedergegebene Sichtweise, Bedingungen, Verneinung, Modalität und Zeitverhältnisse erhalten. Berichtete Behauptungen nicht zu Aussagen des Erzählers machen.

### Glossar der vorhandenen deutschen Übersetzung

Die Tabelle enthält deutsche Entsprechungen, keine Vorgaben für englische, ukrainische oder hebräische Wörter. Für jede neue Sprache vorab ein eigenes Glossar nach Bedeutungen anlegen. Die Einträge beziehen sich auf die einschlägigen Bedeutungen im Werk; bei mehrdeutigen Wörtern entscheidet der Kontext.

| Griechisch | Deutsche Entsprechung je Bedeutung |
|---|---|
| πρόφασις (próphasis) | Grund; 1.23.6: ἀληθεστάτη: wahrster Grund |
| αἰτία (aitía) | Vorwurf / Anschuldigung; kausal: Ursache / Schuld / Verantwortung |
| ἔγκλημα (énklēma) | Beschuldigung |
| στάσις (stásis) | Bürgerkrieg |
| δύναμις (dýnamis) | Macht |
| παρασκευή (paraskeuḗ) | Rüstung |
| δουλεία (douleía) | Knechtschaft |
| λόγος / ἔργον (lógos / érgon) | Wort / Tat |
| χρήματα (chrḗmata) | Mittel |
| τεκμήριον (tekmḗrion) | Indiz |
| σημεῖον (sēmeîon) | Anzeichen |
| μαρτύριον (martýrion) | Zeugnis |
| λῃστεία (lēisteía) | Räuberei |
| τὸ μυθῶδες (tò mythōdes) | das Mythische |
| σπονδαί (spondaí) | Vertrag |
| διαφοραί (diaphoraí) | Streitpunkte |

## Arbeitsweise für weitere Bücher und Sprachen

1. **Höchstens zehn Kapitel pro Auftrag.** Vor Beginn Sprache, Buch, Kapitelbereich und Quelledition festhalten.
2. Den tatsächlichen griechischen Text **Abschnitt für Abschnitt** neben der Übersetzung führen; Kennung: Buch.Kapitel.Abschnitt. Jede Stelle gegen das Griechische prüfen, nicht nur gegen andere Übersetzungen.
3. Nach jedem Auftrag **Abschnittszahl und Kennungen, Längenverhältnis sowie möglicherweise abgebrochene Sätze automatisch prüfen**. Das unten genannte Prüfskript meldet fehlende oder doppelte Abschnitte als Fehler, auffällige Längen und Satzenden als Prüfhinweise.
4. Strukturelle Fehler beheben und jeden Prüfhinweis am Griechischen beurteilen. Länge und Satzzeichen sind nur Indikatoren, kein Qualitätsbeweis. Reden und indirekte Rede gesondert prüfen.
5. Nur vorhandene HTML-Ausgaben unter `docs/<Sprache>/book<N>.html` veröffentlichen. Abschnittskennungen erhalten; `lang="grc"`, `"de"`, `"en"`, `"uk"` oder `"he"` setzen, für Hebräisch zusätzlich `dir="rtl"`. Zeichenabdeckung prüfen. Keine Links auf leere Bücher anlegen.
6. Leseportal und alle fünf READMEs gemeinsam aktualisieren. Geplant, in Arbeit, vorhanden und geprüft unterscheiden; den genauen Umfang nennen. Alle sechs Regeln in neue Ausgaben übernehmen.

```bash
python3 scripts/check_translation.py --language de --book 1 --start 1 --end 10
python3 scripts/build_original.py
```

## Repository und Leseansicht

- `docs/index.html`: Leseportal und Sprachstatus.
- `docs/grc/book1.html` bis `book8.html`: altgriechisches **Original**.
- `docs/grc/source.xml` und `source.json`: unveränderter Quelltext und genaue Herkunft samt Prüfsumme.
- `docs/de/book1.html`: maßgebliche deutsche Ausgabe; `docs/buch1.html` leitet alte Links weiter.
- `docs/assets/`: gemeinsame Gestaltung und acht lokal gespeicherte OFL-Schriften.
- `scripts/`: Originaltext-Renderer und Prüfskript; `review/`: bestehende redaktionelle Notizen.
- `README.md`: englische Dokumentation; `README_DE.md`, `README_UK.md`, `README_HE.md`, `README_GRC.md`: Sprachfassungen.

Keine Markdown-Ausgabe des Werkes und kein Ordner `de_translations/` mehr. Markdown bleibt für Dokumentation und Prüfnotizen bestehen. Zum Lesen genügt `docs/index.html`; GitHub Pages veröffentlicht `docs/`. Schrift- und Farbauswahl werden gespeichert. Dunkelmodus: warmes Gelb auf Schwarz; heller Modus: gedämpftes Papyrus. Für Griechisch ist Source Serif 4 voreingestellt; Hebräisch benötigt RTL-Layout und passende Ersatzschriften.

## Quelle, Zuschreibung und Lizenzen

Das **Original** gibt den Text der genannten modernen Edition wieder, kein Autograf und keinen neu erstellten kritischen Text:

> Thukydides, *Historiae*, herausgegeben von Henry Stuart Jones. Oxford University Press, 1910; Nachdruck 1942. Digitaler Text: Perseus Digital Library, Tufts University, [PerseusDL/canonical-greekLit](https://github.com/PerseusDL/canonical-greekLit).

Revision, Quell-URL, SHA-256 und Umwandlung stehen in [source.json](docs/grc/source.json). Die HTML-Ausgabe vereinheitlicht Leerraum und ergänzt Überschriften, Abschnittskennungen und Navigation; der Wortlaut wird nicht modernisiert oder übersetzt. Quellenangabe und [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) für Quelle und griechische HTML-Ausgabe erhalten.

Die vorhandene deutsche Übersetzung steht unter [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/); die Lizenz künftiger Beiträge ausdrücklich dokumentieren. Die Schriften behalten ihre eigenen [SIL-OFL-1.1-Lizenzen und Copyright-Hinweise](docs/assets/fonts/README.md). Einbettung und Weitergabe mit dem Projekt sind unter diesen Bedingungen erlaubt.

## Aufbau des Werkes

| Buch | Kapitel | Griechische Abschnitte |
|---|---|---|
| 1 | 146 | 580 |
| 2 | 103 | 463 |
| 3 | 116 | 470 |
| 4 | 135 | 531 |
| 5 | 116 | 391 |
| 6 | 105 | 391 |
| 7 | 87 | 363 |
| 8 | 109 | 398 |

Buch 1: Frühgeschichte (1–23), Kerkyra (24–55), Potidaia und Sparta (56–88), Pentekontaetie (89–118), Korintherrede und Beratungen (119–125), Kylon, Pausanias und Themistokles (126–138), letzte Verhandlungen (139), Perikles-Rede (140–144), unmittelbare Vorkriegslage (145–146). Die Abschnittszählung folgt der genannten Edition; in der Leseansicht steht `§`.
