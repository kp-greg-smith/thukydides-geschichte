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

## Offene und unsichere Stellen (Stand 27.09.2026)

- 1.6.3 — wie pipeline-einheitlich (הראשונים).
- 1.7.1 — Lesartentscheidung dokumentiert.
- 1.9.4/1.10.4 — wie EN/UK (sinngemäß mit Anmerkung).
- 1.18.1 — gestörte Überlieferung, sinngemäß mit Anmerkung.

## Zahlen (Stand 27.09.2026)

- Übersetzte Abschnitte: 65 in den Kapiteln 1–20 (Hebrew); insgesamt Buch 1 hat 146 Kapitel / 580 Abschnitte.
- Durch Zweitprüfung geprüft: sämtliche 65 veröffentlichten Abschnitte (jede Portion durch einen unabhängigen Subagenten, jede Meldung durch die Koordination am griechischen Text entschieden; automatische Strukturprüfung je Portion ohne Fehler).
- Vom Prüfer beanstandet: kumuliert 40 Fundstellen (3 Blocker, 37 Minor).
- Geändert: sämtliche angenommenen Fundstellen im Textkorpus umgesetzt; abgelehnte Meldungen: keine dokumentiert; gegenstandslose Erhebungen: 0.
- Offen bzw. unsicher: die oben verzeichneten Stellen (Zeileneinträge mit „offen“/crux); keine davon blockiert die Veröffentlichung, alle Entscheidungen sind im Text oder in der Anmerkung sichtbar.
- Nicht veröffentlicht, obwohl work in progress: Kapitel 41–50: Übersetzung abgeschlossen, Zweitprüfung ausstehend; Kapitel 51–60: Übersetzung im Gang; Kapitel 61–146 noch nicht begonnen.
- Keine Behauptung von Fehlerfreiheit: geprüft heißt nicht fehlerfrei; künftige Portionen und Nachprüfungen können weitere Befunde bringen.
