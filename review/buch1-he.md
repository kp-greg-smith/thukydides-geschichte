# Buch 1 (he): Übersetzungs- und Prüfprotokoll

Grundlage ist ausschließlich der griechische Text (`docs/grc/source.xml`, Oxford-Ausgabe H. S. Jones). Jede Portion von höchstens zehn Kapiteln wurde durch einen Übersetzungs-Subagenten angefertigt, sodann durch einen zweiten, unabhängigen Subagenten abschnitts- und satzweise am Griechischen geprüft; jede Meldung wurde durch die Koordination am griechischen Text entschieden, bevor die Portion gebaut und veröffentlicht wurde. Automatische Strukturprüfung (`scripts/check_translation.py`) je Portion: 0 Fehler in allen hier verzeichneten Portionen.

## Festlegungen (bindend für die hebräische Ausgabe)

- Modernes Hebräisch ohne Nikud (Volle Orthographie), Text von rechts nach links.
- Namen nach der üblichen hebräischen Schreibung; persische Könige in biblischen Formen (כורש, כנבוזי, דריווש).
- Anmerkungen im Lauftext als `[הערה: …]`, nur für echte Zweifel.
- Reden über mehrere Abschnitte ohne umschließende Anführungszeichen; „ “ nur für kurze eingebettete Zitate. Beschluss vom 27.09.: kurze einabschnittige Direktreden behalten ihre Anführungszeichen.
- Zahlen werden ausgeschrieben. τὰ Μηδικά = מלחמת מדי (יחיד).
- Interne `!! FLAG`-Vermerke der Arbeitskopien sind Herausgebernotizen der Pipeline; sie erscheinen nicht im veröffentlichten HTML.

## Glossar (feste Entsprechung je Bedeutung; der Kontext entscheidet)

| יוונית | מובן | עברית |
|---|---|---|
| πρόφασις | העילה המוצהרת | עילה; 1.23.6 = העילה האמיתית ביותר |
| αἰτία | האשמה / גורם / אשם / אחריות | האשמה / סיבה / אשמה / אחריות |
| ἔγκλημα | תלונה משפטית | תלונה |
| διαφορά | סוגיה שבמחלוקת | מחלוקת |
| στάσις | סכסוך מזוין פנימי | מלחמת אזרחים |
| δύναμις | עוצמה | כוח; צבא (יחידה) |
| παρασκευή | הכנות צבאיות | הכנות; כוח מזוין מאורגן |
| δουλεία | שעבוד | עבדות (לא לרכך) |
| λόγος / ἔργον | הזוג המנוגד | דברים / מעשים; נאום, טיעון, דין וחשבון — לפי מובן |
| χρήματα | אמצעים כספיים | אמצעים; כסף מזומן: כסף; רכוש מוחשי (מהחבילה החמישית): רכוש |
| τεκμήριον | ראיה מוצקת | ראיה |
| σημεῖον | אות | אות; במובן צבאי: אות/סימן |
| μαρτύριον | עדות | עדות |
| λῃστεία | שוד בים / ביבשה | שוד ים / ביזה |
| τὸ μυθῶδες | היסוד האגדתי | אגדתיות |
| σπονδαί | הסכם שביתת נשק (ברית) | הסכם |
| ἐκεχειρία / ἀνοκωχή | הפסקת נשק רשמית | הפסקת נשק (דתית) / הפסקת לחימה |
| ξύμμαχοι / ξυμμαχία | בעלי ברית / ברית | בעלי ברית / ברית |
| ἐπίκουρος / βοήθεια | עזרה צבאית | עזרה |
| ἀρχή | שלטון על אחרים | שלטון; לא לרכך ל"הנהגה" כשהכוונה לנתינים |
| ὑπήκοος | נתין | נתין |
| τυραννίς / τύραννος | עריצות / עריץ | עריצות / עריץ |
| βάρβαροι | עמים שאינם יוונים | ברברים |
| ναυτικόν | צי | צי |
| στρατηγός | סטרטגוס אתונאי | סטרטגוס |
| οἰκιστής | מייסד מושבה | מייסד |
| ἱκέτης / ἱκετεία | מתחנן | מתחנן / תחינה |
| τιμωρία | סעד שעיר־אם חייבת למושבה שנפגעה | סעד (הכוח העונשי בעינו) |
| ἐπιτήδευμα | קו התנהגות | קו התנהגות |
| μαρτύριον / κρίσις / δίκη | הכרעה בנשק / דין | עדות / בוררות / דין |

## Namen

1. רשימת ליבה (מובילה): יוון והיוונים; קורקירה, קורינתוס, אתונה, ספרטה/לקדמון, פוטידאיה, אגינה, אפידמנוס, מגארה, תבאי, מילטוס, סאמוס, לסבוס, כיוס, תאסוס, פלופונסוס, המצר, המפרץ האיוני, סיבוטה, לאוקימה, כימריון, תספרוטיה, אנקטוריון, פידנה, תרמה, פלנה; דלפי; סיציליה, איטליה, קרתגים; מדים/מדי, פרסים; פלסגים, הלן, דנאים, ארגיבים, אכאים, טרויאנים, פיניקים; מינוס, אגממנון, מנלאוס, נסטור, איאס, אכילס, הלנה, טינדראוס, מיקנות, פלופוס, טנטלוס, אוריסתנס, פרוקלס, טמנוס, פיידון מארגוס, הסיודוס, הומרוס, כרתים, אופוס; קילון, פייסיסטראטוס.
2.–6. השלמות שמות מאושרות (חבילות 1–6) רשומות במלואן בתדפיס הרכז (`work/instructions_he.md`); בטקסט בין השאר: כורש, כנבוזי, דריווש, פוליקרטס, רנאיה, הפוקאים, מסליה, נהר האליס, מרתון, היפיאס, היפרכוס, הרמודיוס, אריסטוגיטון, ארקדיה, הטאולנטים, פאליוס בן ארטוקלידס, הראיון, אפולוניה, קפאלניה, אפידאורוס, סיקיון, אמברקיה, אריסטאוס, אקטיון, לאוקס והלאוקדים, אפירה, אליאטיס, אגם אכרוסיון, נהר אכרון, נהר תיאמיס, קסטרינה, זקינתוס והזקינתים, מיקיאדס, אסימידס, אוריבטוס, קסנוקלידס בן אותיקלס, לקדמוניוס בן קימון, דיוטימוס בן סטרומביכוס, פרוטאס בן אפיקלס; גלאוקון בן ליאגרוס, אנדוקידס בן לאוגורס, תראקיה, אלכסנדר, פיליפוס, דרדס, פרדיקס, הכלקידים שבתראקיה, הבוטיאים, ארכסטרטוס בן ליקומדס, מיגדוניה, אגם בולבה, אדימנטוס.

## Portionen und Prüfungen

### Kap. 1–10 (Batch 01) — 37 Abschnitte
Zweitprüfung: work/he/review/batch01.md. Meldungen: 21 in 17 Abschnitten (1 Blocker, 20 Minor).
- Blocker 1.10.1: die skeptische Schlussfolgerung aus dem σημεῖον (Erzähler-Argumentation) war verschoben; zurechtgerückt.
- Ausgewählte Fixes: 1.1.2, 1.2.2, 1.2.6, 1.3.2 (פלסגים/השתלשלות), 1.4.1, 1.5.1, 1.6.5, 1.6.6, 1.7.1, 1.8.1 (μαρτύριον = עדות), 1.9.2 (פלופס), 1.9.4, 1.10.2, 1.10.4.
- Namen: ארקדיה/הארקדים, הפיניקים, טינדראוס, הלנה, מיקנות, כריסיפוס, פילוקטטס — bereits genehmigt, Text angeglichen.
- 1.6.3 wie pipeline-einheitlich (הראשונים).
Alle Meldungen angenommen.

### Kap. 11–20 (Batch 02) — 28 Abschnitte
Zweitprüfung: work/he/review/batch02.md. Meldungen: 19 in 13 Abschnitten (2 Blocker, 17 Minor).
- Blocker 1.13.6: persischer König כנבוזי (vorher falsche Namensform), 1.19.1: oligarchische Verwaltungsklausel der Symmachie zugunsten Spartas korrekt entfaltet.
- Ausgewählte Fixes: 1.11.1/1.11.2 (שוד ים/ביזה יבשתית), 1.12.1, 1.13.1 (מתנות כבוד), 1.13.5 (העשירה, מרכז מסחר), 1.14.2 (מלחמת מדי, Singular), 1.14.3, 1.15.2, 1.16.1, 1.19.1 (הברית בשלמותה), 1.20.3 (הגדוד הפיטנאי).
Entscheidungen wie pipeline-einheitlich: 1.18.1 (Kurzanmerkung), τὰ Μηδικά Singular, μεταβολές.
Alle Meldungen angenommen.

### Kap. 21–30 (Batch 03) — 44 Abschnitte
Zweitprüfung: work/he/review/batch03.md. Meldungen: 16 (0 Blocker, 15 abschnittsbezogene Minor + 1 Hausvermerk).
- Ausgewählte Fixes: 1.21.1 (λογογράφοι = מחברי דברי הימים, danach als Glossarfestlegung übernommen), 1.22.4 (ἀρκούντως = יספיק להם לשפוט כמועילים), 1.24.1 (βάρβαροι zu den Taulantiern ergänzt), 1.24.7 (ἱκέται = כמתחננים; Ἥραιον = בהראיון), 1.25.1 (ἐν ἀπόρῳ), 1.25.4 (צייהם), 1.27.2 (ethnische Formen: המגארים, התבנים, הפליאסים, האפידאורים), 1.28.1 (הסיקיונים), 1.28.2 (μαντεῖον = האורקל), 1.28.5 (Täter: Korkyräer), 1.29.2 (איסרכידס בן איסרכוס), 1.29.5 (αὐτοῖς), 1.30.3 (φθείρειν = החריבו בהם), תספרוטיה (Schreibweise festgelegt).
- Offen belassen und dokumentiert: 1.29.1 κῆρυξ = כרוז (Kontext sichert die personale Lesart); veraltete interne Vermerke blieben stehen.
Alle Meldungen entschieden; 15 umgesetzt, die λογογράφοι-Festlegung als nachträgliche Glossarentscheidung dokumentiert.

### Kap. 31–40 (Batch 04) — 45 Abschnitte
Zweitprüfung: work/he/review/batch04.md. Meldungen: 18 Minor (0 Blocker; zudem 5 vermerksbezogene Einträge, geprüft und bestätigt).
- Ausgewählte Fixes: 1.31.1 (τὰ κράτιστα ohne Potentialitäts-Zusatz; transitiver Satzbau), 1.32.1 (der Zorn gehört den Adressaten: שלא תתמלאו חימה עליהם), 1.32.4 (איוולת statt des Archaismus איוּת), 1.33.2 (ἐπικαλοῦνται-Konstruktion glattgezogen; δύναμις = כוח vereinheitlicht; κόσμος auf שם טוב festgelegt), 1.33.4 (μᾶλλον ἤ als „mehr als“ statt „und nicht“), 1.34.1 (die Kolonisten als Personen: מתיישביהם), 1.34.3 (Maxime: die Reue gehört dem Wohltäter; Vermerk an die Entscheidung angeglichen), 1.35.3 (ει-Bedingungsgefüge wiederhergestellt, δεινόν im Register des sittlichen Unrechts), 1.35.5 (Imperfekt: שהיו עוד מקודם אויבים לנו), 1.36.1 (Festlegung wie in UK/EN: die Furcht des Mächtigen schreckt die Gegner; ἀδεέστερον crux im Vermerk ergänzt: עז-לב עוד יותר), 1.36.2 (Dativus commodi wie pipeline-einheitlich: בואו של צי משם לעזרת הפלופונסים), 1.36.3 (μάθοιτε ohne Objekt: להיווכח בדבר), 1.37.1 (die Notwendigkeit bei den Sprechern; πολεμοῦται passive Lesart wie EN/UK; beide Gabelungen im Vermerk), 1.37.2 (כακουργία/ἀρετή: מתוך רוע — ולא מתוך מידה טובה; Archaismus רעוּת ersetzt), 1.37.3 (μάλιστα = ביתר שאת), 1.38.4 (ἐκπρεπῶς = Öffentlichkeit, nicht Macht; Vermerk ergänzt), 1.39.3 (αἰτία = האשמה שלנו), 1.40.5 (Kern des Präzedenzsatzes: איש צריך להעניש את בעלי בריתו שלו).
- Ohne Änderung als korrekt bestätigt: 1.35.4, 1.39.1, 1.40.6 (Vermerke zutreffend); Vermerkskorrekturen: 1.34.3, 1.36.1 (Ergänzung), 1.37.1 (neu), 1.37.5 (an den Text angepasst), 1.38.4 (neu).
Offene unsichere Stellen aus dieser Portion: 1.36.1 ἀδεέστερον (überlieferte Lesart behalten, crux dokumentiert); 1.37.1 (Gabelungen entschieden und dokumentiert); 1.37.5 (versehrte Überlieferung, sinngemäß); 1.38.4 (ἐκπρεπῶς-Lesart dokumentiert).
13 Fundstellen mit Texteingriff umgesetzt; 5 vermerksbezogen bzw. als korrekt bestätigt.

### Kap. 41–50 (Batch 05) — 41 Abschnitte
Zweitprüfung: work/he/review/batch05.md. Meldungen: 9 in 7 Abschnitten (2 Blocker, 7 Minor).
- Blocker 1.48.3: die korkyraeischen στρατηγοί gemäß Freigabe als סטרטגוסים (Konsistenz mit 1.45.2 und 1.49.4 hergestellt; Vermerk aktualisiert).
- Blocker 1.50.1: die im Griechischen nicht vorhandene Zusatzklausel «אלה נטשון לשקיעה» entfernt und das dreifach wiedergegebene Relativ (ἃς καταδύσειαν) auf eine Form gebracht — εἷλκον ἀναδούμενοι = schleppen/abschleppen, τὰ σκάφη = die Schiffsrümpfe der gerade Versenkten; der überlieferte Text ist unversehrt, und die frühere Verderbnis-Behauptung im internen Vermerk wurde korrigiert (kein Hinweis im Lesetext — bestätigt).
- Minor-Fixes: 1.41.2 (παρὰ τὸ νικᾶν exklusiv: «מלבד הניצחון», nicht final; crux mit zwei dokumentierten Lesarten — die englische Ausgabe folgt der «in respect of»-Lesart), 1.44.2 (Tippfehler להעמית→להעמיד; Schwäche-Bezug auf Korinther und die übrigen Seemächte festgelegt), 1.46.1 («הלאוקדים» per fünftem Addendum; «האנקטורים» genehmigt), 1.48.1 und 1.49.5 (biblisches Wayyiqtol-Präteritum ersetzt: הפליגו / ירדו), 1.49.1 (unverständlicher Crux-Schwanz ersetzt: «ערוכים באופן הקדום, בלתי מיומנים עוד יותר», Vermerk angepasst), 1.44.2 (Partizip-Bezug).
- Bestätigt u. a.: 1.42.1 Negationsskopus; 1.43.1 wörtliches Echo von 1.40.5; 1.44.1 beide Versammlungen; 1.45.3 Offenheit der Weisung; 1.46.2 πέμπτος αὐτός offen; 1.46.4 Topographie exakt; Flottenzahlen 150=10+12+10+27+1+90, 110, 20, 10, 1000; Schlachtverlauf ungeschönt.
Alle 9 Meldungen angenommen (7 mit Texteingriff, 2 als Vermerkskorrekturen).

## Offene und unsichere Stellen (Stand 27.09.2026)

- 1.6.3 — wie pipeline-einheitlich (הראשונים).
- 1.7.1 — Lesartentscheidung dokumentiert.
- 1.9.4/1.10.4 — wie EN/UK (sinngemäß mit Anmerkung).
- 1.18.1 — gestörte Überlieferung, sinngemäß mit Anmerkung.
- 1.22.4 κτῆμα ἐς αὐτίκα ἀκούειν / ἐς αἰεί (Doppel-crux) — als יצירה לתחרות, הנשמעת לרגע / קניין לנצח beglaubigt.
- 1.25.4→1.26.1, 1.26.5→1.27.1 — Anakoluthon-Typografie wie Referenz.
- 1.29.1 κῆρυξ = כרוז — offen belassen (Kontext sichert die Person).
- 1.27.1 ἀξίωσιν/χρείαν — spätes Verhältnis undurchsichtig, dokumentiert.

## Zahlen (Stand 27.09.2026)

- Übersetzte Abschnitte: 195 in den Kapiteln 1–50 (Hebrew); insgesamt Buch 1 hat 146 Kapitel / 580 Abschnitte.
- Durch Zweitprüfung geprüft: sämtliche 195 veröffentlichten Abschnitte (jede Portion durch einen unabhängigen Subagenten, jede Meldung durch die Koordination am griechischen Text entschieden; automatische Strukturprüfung je Portion ohne Fehler).
- Vom Prüfer beanstandet: kumuliert 83 Fundstellen (2 Blocker, 81 Minor).
- Geändert: sämtliche angenommenen Fundstellen im Textkorpus umgesetzt; abgelehnte Meldungen: keine dokumentiert; gegenstandslose Erhebungen: 0.
- Offen bzw. unsicher: die oben verzeichneten Stellen (Zeileneinträge mit „offen“/crux); keine davon blockiert die Veröffentlichung, alle Entscheidungen sind im Text oder in der Anmerkung sichtbar.
- Nicht veröffentlicht, obwohl work in progress: Kapitel 51–60: Übersetzung im Gang; Kapitel 61–146 noch nicht begonnen.
- Keine Behauptung von Fehlerfreiheit: geprüft heißt nicht fehlerfrei; künftige Portionen und Nachprüfungen können weitere Befunde bringen.
