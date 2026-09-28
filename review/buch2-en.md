# Buch 2 (en): Übersetzungs- und Prüfprotokoll

Grundlage ist ausschließlich der griechische Text (`docs/grc/source.xml` / `docs/grc/book2.html`, Oxford-Ausgabe H. S. Jones; Extrakt `work/grc/b2/ch_NNN.txt`). Jede Portion von höchstens zehn Kapiteln (B01 = 1–10 … B11 = 101–103) wird durch einen Übersetzungs-Subagenten angefertigt, sodann durch einen zweiten, unabhängigen Subagenten abschnitts- und satzweise am Griechischen geprüft; zusätzlich prüft nach jeder Portion eine neue GLM-Session ohne Zugang zu `work/` und `review/` (nur griechisches HTML plus die drei Übersetzungs-HTML) nach demselben Prüfauftrag. Jede Meldung wird durch die Koordination am griechischen Text entschieden; Eskalationen an Astra (codex, `gpt-6-astra`, read-only) nach dem Astra-Protokoll, wörtlich protokolliert in `review/buch2-astra-log.md`. Automatische Strukturprüfung (`scripts/check_translation.py --language en --book 2`) je Portion.

Festlegungen, Glossar und Namensformen aus Buch 1 (`review/buch1-en.md`, `work/instructions_en.md`) bleiben verbindlich. Kennung in Buch 2: `2.Kapitel.Abschnitt`. Buch-2-Addenda (Glossar, Namen, Festlegungen) werden unten je Portion verzeichnet und am Ende in die READMEs nachgetragen.

## Festlegungen (Buch 2, bindend für die englische Ausgabe)

- Britische Rechtschreibung mit Oxford-„-ize“; latinisierte Namensformen; Anmerkungen als `[Note: …]`; Reden über mehrere Abschnitte ohne umschließende Anführungszeichen, kurze eingebettete Zitate mit „ “; Zahlen ausgeschrieben; `!! FLAG` nur intern. (Wie Buch 1.)
- Kapitel 35–46 (Grabrede des Perikles), 60–64 (letzte Rede), 71–74 (Plataier/Archidamos), 87, 89 (Kriegsrat/Phormion) gelten als Reden im Sinne der Stichprobenregel (6 statt 4 Stichproben je Sprache und Portion).
- Kein Rückgriff auf `docs/de/` (existiert für Buch 2 nicht) und keine moderne Übersetzung als Vorlage.

## Buch-2-Addenda

**Fünfzehntes Addendum, Kapitel 1–10 (B01, gebilligt).** Namen (EN): Chrysis (priestess at Argos); Aenesius (Spartan ephor); Pythodorus (Athenian archon); Pythangelus son of Phyleides; Diemporus; Onetorides; Naucleides; Eurymachus; Leontiades; the river Asopus; Pellene, the men of Pellene; Melos; Thera. Abgeleitete Ethnika: the Leucadians, the Anactorians (von den gebilligten Toponymen Leucas, Anactorium). Glossar: βοιωτάρχος = boeotarch; ἐπινόω / ὀλίγον ἐπενόουν οὐδέν = "designs … nothing small" (LSJ ἐπινοέω I.2, Astra B01); νεωτερίζειν ἐς τινά = hostile action (2.3.1), μηδὲν νεώτερον ποιεῖν = rash step (2.6.2; A B01-Astra-Ruling — kontextabhängige Differenzierung nach Regel 1); τὰ δύο μέρη = two-thirds (LSJ s.v. μέρος zitiert 2.10.2 selbst; Parallele 2.47.2); χρησμολόγοι = oracle-mongers; λόγια = prophetic sayings; περίορθρον = the dead of night (hapax); ὑποσπόνδιος = under truce; ἀκηρυκτεί = unheralded. Festlegungen: 2.8.4 ἐν τούτῳ … ᾧ korrelativ + κεκωλῦσθαι prospektiv (Astra-B01); 2.5.5 δράσειαν überliefert-defensible Konstruktion, keine Lesernote (Astra-B01); 2.5.6 εὐθύς gehört zur Rückgabe (= immediately), nicht zum Versprechen (Astra-B01).

## Portionen und Prüfungen

### Kap. 1–10 (Portion B01) — 45 Abschnitte
Übersetzung: Subagent, 45/45 Abschnitte (1, 4, 4, 8, 7, 4, 3, 5, 6, 3), Struktur maschinell gegen `docs/grc/source.xml` verifiziert (alle IDs vollständig, in Quellordnung). Prüfung: unabhängiger Subagent, Bericht `work/en/b2/review/batch01.md` — 6 Meldungen (0 Blocker, 6 Minor):
- 2.2.4 ἐχθρῶν gemildert zu „the men opposed to them“ → ANGENOMMEN: „their enemies“ (Regel 1/3; Variation gegen ὑπεναντίους 2.2.2).
- 2.3.4 Flag-Fehlzitat (ὥστε statt ὅπως μή) → ANGENOMMEN (nur FLAG korrigiert; die Lesart selbst blieb — Subjekt der ὦσι-Klausel = die Thebaner, σφετέρας auf die Plataeans; Mainstream-Lesart).
- 2.5.5 δείσαντες περὶ τοῖς ἔξω eingeengt zu „their people outside“ → ANGENOMMEN: „those outside“ (Menschen und Habe, vgl. 2.5.4).
- 2.7.2 Flag-Fehlzitat (αὑτοῦ statt überliefertem αὐτοῦ; νηί statt νηὶ) → ANGENOMMEN (nur FLAG; Wiedergabe korrekt).
- 2.8.1 ἔρρωντο zu flach („went into“) + fehlendes FLAG → ANGENOMMEN: „pressed eagerly into the war not unreasonably“ (Konsistenz mit 2.8.4); FLAG nachgetragen.
- 2.10.2 fehlendes FLAG zur zwei-Drittel-Lesart → ANGENOMMEN (FLAG mit LSJ-Beleg nachgetragen; Lesart bestätigt durch Astra B01 Anfrage 1.5).
Astra B01: Anfrage 1 (Cruxes; work/astra/b01_cruxes.txt): 2.3.1 „taking no hostile action“ statt „attempting no new thing“ (ANGENOMMEN); 2.6.2 „do nothing rash“ statt „nothing new“ (ANGENOMMEN); 2.5.5 Lesart bestätigt, keine Note (EN hatte keine); 2.8.4 korrelativ-prospektive Umstellung (ANGENOMMEN: „any undertaking in which he himself did not take part would be held up“); 2.10.2 two-thirds bestätigt. Anfrage 2 (Stichprobe Seed 20260928: 2.4.1, 2.4.8, 2.5.6, 2.8.2): 2.4.1/2.4.8/2.8.2 korrekt; 2.5.6 εὐθύς zur Rückgabe → ANGENOMMEN („promised to give the men back immediately“). Aus den Astra-Anfragen: 3 Körperkorrekturen (2.3.1, 2.6.2, 2.8.4, zählt als 3) + 2.5.6; rein flagseitig: 2.10.2-Beleg, 2.8.4-Dokumentation.
Zweitprüfung (neue GLM-Session ohne Zugang zu `work/` und `review/`, nur `docs/grc/book2.html` plus die drei Übersetzungs-HTML): Prüfbericht der Session: en 0 Befunde; spezifisch geprüft und bestätigt: sämtliche Zahlen (vierzehn/fünfzehntes Jahr, achtundvierzig = fünfzig weniger zwei, zwei Monate, sechster Monat, dreihundert-plus, zweimal-dreimal, siebzig Stadien, einhundertachtzig, fünfhundert, zwei Drittel, „not many“), sämtliche Namen und Bündnislisten, indirekte Rede 2.5.5–2.5.6 und 2.6.2–2.6.3, alle Verneinungen. EN-B01 damit abgeschlossen: 45 Abschnitte übersetzt; 6 Prüfermeldungen (0 Blocker, 6 Minor), alle angenommen; Astra-Anfragen mit EN-Korrekturen: 6 (2.3.1, 2.6.2, 2.5.6, 2.8.4, 2.2.4, 2.7.3); abgelehnte Meldungen: 0; offene unsichere Stellen: keine.
ABGELEHNT: keine EN-Meldung abgelehnt in B01.
Offen/unsicher (EN, B01): keine offen; die überlieferten Cruxes (2.5.5 δράσειαν; 2.8.5 〈ἐν〉) sind im TEXT bzw. unbezeichnet gelöst, Astra hat beide bestätigt bzw. Regel 4 greift (〈ἐν〉 ändert nichts am Sinn), keine offenen Stellen verbleiben.

## Offene und unsichere Stellen

(wird je Portion nachgetragen)

## Zahlen

(wird am Ende vervollständigt: übersetzte Abschnitte, beanstandete, geänderte, abgelehnte Meldungen, Astra-Anfragen mit Korrekturen, offene unsichere Stellen)
