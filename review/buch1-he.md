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

### Kap. 51–60 (Batch 06) — 31 Abschnitte
Zweitprüfung: work/he/review/batch06.md. Meldungen: 10 in 11 Abschnitten (1 Blocker, 8 Minor + 1 Vokabular-Entscheid).
- Blocker 1.58.1: τιμωρία im Metropole-Kolonie-Kontext = «כדי שיהיה להם סעד מוכן» wiederhergestellt — vorgeschriebener Slot mit Hilfe-Komponente und externer Bereitstellung durch Sparta (EN „redress", UK «відплата»); die Ersatzwurzel היפרע verlor beide.
- Wurzelentscheid: τιμωρέομαι/τιμωρία allgemein = להעניש (1.53.2, 1.56.2; deckungsgleich EN „punish"/UK «карати»), Metropole-Kolonie = סעד (1.58.1); Lexikon-Vorschlag היפרע nicht übernommen; Zusatzimagination «למצוא דרכים» (1.56.2) getilgt.
- Weitere Minor-Fixes: 1.53.1 (Worterklärungs-Notiz entfernt — Regel 4), feindliches ἐπί+akk. = על wiederhergestellt (1.53.2, 1.53.4; 1.57.6; 1.58.1; 1.59.2 — die Pointe der Waffenstillstandskontroverse), 1.55.1 («היושבת על» statt «החולשת על»; «ואירע» statt wayyiqtol «ויצא»), 1.55.2 (αἰτία-Interstate-Slot ההאשמה als Echo zu 1.23.5–6), 1.57.2 (ἐπεπολέμωτο passivisch: «הותקף על ידיהם» — Athen als Aggressor), 1.60.1 («מקרבם» statt «von ihren Söhnen» suggerierendem «מבניהם»).
- Bestätigt: Kurzreden 1.53 in Anführungszeichen und stenographisch; Zwanzig/Dreißig-Widerspruch wie überliefert; †Ἀνδοκίδης†/†zehn† wie überliefert; [ἔπρασσον] ohne Notiz; ἐπιδημιουργοί-Transliteration mit Selbsterklärung im Folgevers; ἀναχωρήσαντες-Offenheit; περιγίγνεται neutral; ἄνωθεν; Litotes 1.60.2; alle Zahlen; Regel-6-Sweep sauber; nichts gemildert.
- Vermerksrevisionen: 1.56.2, 1.57.2 (falsche Prämisse «פרדיקאס»), 1.58.1, 1.59.2 (erledigt).
Alle 10 Meldungen angenommen (alle mit Texteingriff außer den Vermerksrevisionen).

### Kap. 61–70 (Batch 07) — 45 Abschnitte
Zweitprüfung: work/he/review/batch07.md. Meldungen: 12 in 12 Abschnitten (2 Blocker, 10 Minor).
- Blocker 1: Namensschreibung כליאס an allen drei Stellen (1.61.1, 1.62.4, 1.63.3) gemäß siebtem Addendum — abgesetzt vom gleichnamigen קליאס in 1.29.2.
- Blocker 2 (1.70.2): νεωτεροποιοί = מחדשים (genehmigte Erweiterung) statt freier Umschreibung «בעלי חידושים».
- Regressive Namensform פרדיקס in 1.61.3/1.62.2/1.62.3 wiederhergestellt (Kap. 56–59 hatten die korrekte Form).
- Sinn-Fixes: 1.63.1 (ὡς ἐς ἐλάχιστον χωρίον gehört zur Zusammenziehung des Haufens, nicht zum Durchbruchspunkt), 1.65.3 (erfundenes «מבוצרות» getilgt), 1.69.1 (einfaches Prädikat statt Doppelung; εἴπερ καί = «בפרט שהוא גם»), 1.69.2 (βεβουλευμένοι = «ועצתם כבר נעשתה מראש»), 1.69.3 (überliefertes „weniger“ lesbar: «פחות הם בוטחים בעצמם»), 1.69.5 (ἁμαρτήματα = טעויותיהם statt unleserlichem «מעידותיהם»), 1.62.3 (ἐπιτηρεῖν = יפקח עין — «לשמור על» läse sich als „beschützen“), 1.65.2 (biblischem «ובארבו» durch modernes «והטמין מארב» ersetzt).
- Vermerks-Ergänzung: 1.69.4 (überliefertes gestrandetes τινά + gewählte Lesart); Vermerks-Revisionen: 1.68.3 und 1.69.5 (beide hatten Wiedergaben beschrieben, die so nicht im Text stehen — jetzt textgetreu).
- Formatbereinigung: acht FLAG-Zeilen des Drafts waren in Backticks gehüllt und wären durch den Build-Filter gefallen — normalisiert; der Filter wurde zusätzlich gehärtet.
- Bestätigt: alle Zahlen wie überliefert in Worten; πέμπτον αὐτὸν στρατηγόν offen; מלחמת מדי; כיתור-Reihe; יציאה לים; מזח; תוכחה/האשמה-Kontrast; עונש; ἧσσον θαρσοῦσι ohne Konjektur; [τεῖχος] nahtlos; alle siebten-Addendum-Namen; Korintherrede typografisch offen bis 1.70.9 in 1.71 hinein; Regel 6 voll gewahrt.
Alle 12 Meldungen angenommen (11 mit Texteingriff; 1 als Vermerks-Ergänzung; 2 Vermerks-Revisionen).

### Kap. 71–80 (Batch 08) — 43 Abschnitte
Zweitprüfung: work/he/review/batch08.md. Meldungen: 12 in 12 Abschnitten (4 Blocker, 8 Minor).
- Blocker 1.73.2: στερισκώμεθα ist deklarativer Indikativ («נשלל מאיתנו») — der imperativische Weg an Sparta („אל תיתנו…“) war eine Satzmodus- und Adressatenumkehr; der Zusatz «הזכות» für τοῦ λόγου durch שכר הדברים ersetzt; die echten Knoten (Suspension τοῦ λόγου μὴ παντός, μή-Modus) bleiben sedimentiert.
- Blocker 1.73.4: πρὸς ναῦς πολλὰς adversativ — „מול אוניות רבות“, nicht instrumental („באוניות רבות“); das ἂν-Potential des ἀδυνάτων ἂν ὄντων wiederhergestellt.
- Blocker 1.74.1: Themistocles als athenischer στρατηγός = סטרטגוס (Slot-Verletzung behoben); die Schiffszahl-Crux selbst war korrekt offen gehalten — der Vermerk dokumentiert jetzt die Alternativ-Lesarten (zwei Drittel des Gesamtfleet / doppelter Anteil) und die Entscheidung: die gedruckte Apposition bleibt.
- Blocker 1.77.6: die ausgefallene Apodosis ὁμοῖα καὶ νῦν γνώσεσθε als eigene Prognose ergänzt («דומים תחוו גם עתה»).
- Vorab-Prüfungen bestanden: 1.71.2 (kein Athen-Bezug — ὁμοίᾳ unangheftet wie überliefert), 1.73.1 (Richternegation exakt, keine Doppelinversion), 1.74.1-Crux (beide Elemente nebeneinander), 1.74.3 (Flag ehrlich), 1.76.2 〈τριῶν〉 nahtlos.
- Minorfixes: δῠ́ναμις an zwei Stellen auf den Glossar-Slot כוח ausgerichtet (editionweiter עוצמה/כוח-Split als offener Harmonisierungspunkt für den Schlussdurchgang vermerkt: 1.15/1.33/1.36), τεκμήριον μέγιστον = «ראיה הגדולה ביותר», 1.76.2 (Doppelverneinung unter einem οὐδείς), 1.76.4 (εἴ τι-Vorbehalt wiederhergestellt), 1.77.2 («פועל בכוח הזרוע» statt opakem «כופה את ידו»), 1.79.2 (Einstieg «ונגש אליהם»; σώφρων = «שקול ומאוזן»), 1.80.3 (falscher Distanz-Anker «מהם» → «מאיתנו»).
- Vermerks-Ergänzungen: 1.74.4 (περὶ τῇ χώρᾳ Dativ-Anomalie), 1.74.1 (Alternativ-Konstruktionen + Entscheidung).
- Bestätigt: alle Reden ohne Klammer und ohne Bruch; Archidamus am Batch-Rand offen in 1.81; Regel 6 überall; σπονδαί = הסכם/הסכמים mit ξυνθήκη = אמנה getrennt; ἀρχή = שלטון achtmal ungemildert; δουλεύω ungemildert; alle Zahlen in Worten; die Glossarvorschläge (התחכמות/קנאה/חובבי משפטים) am Griechischen verifiziert und vertretbar.
Alle 12 Meldungen angenommen (10 mit Texteingriff, 2 reine Vermerks-Fälle; dazu 2 Vermerks-Revisionen).

### Kap. 81–90 (Batch 09) — 42 Abschnitte
Zweitprüfung: work/he/review/batch09.md. Meldungen: 11 in 10 Einträgen (2 Blocker, 9 Minor).
- Blocker 1.86.2: die Rache-Konstruktion zielt wieder auf die Täter («ולא נאחר את הנקמה בעושי העוול בהם») — zuvor wies «בהם» auf die verbündeten Opfer; zugleich wurde die falsche Offenheitsbehauptung des Vermerks (Subjekt und Futur sind im Druck festgelegt) in eine dokumentierte Wahl umgeschrieben.
- Blocker 1.84.3: die Schwelle von σωφρονέστερον ἢ ὥστε ἀνηκουστεῖν wiederhergestellt — Disziplin «גדול מכדי למרוד בהם» (zu groß zum Ungehorsam), nicht «עולה על כדי» (mehr als genug zum Aufstand); der zentrale Erziehungs-Satz war invertiert; der Vermerk zitiert jetzt den reparierten Text.
- Harmonisierung der ἀδικ-Stellen (1.86.1–1.87.4): sechs Vorkommen der Wurzel עושק auf die editionsweit festgelegte עוול-Linie gebracht (vgl. 1.67.2, 1.77.4, 1.79.2, 1.85.2) — darunter der Redeschluss «על עושי העוול» statt «על העושקים» (= die Unterdrückten), der die Marschrichtung verkehrt hätte.
- Namensregression behoben: Λακεδαίμονα zweimal als לקדמון wiederhergestellt (1.90.3, 1.90.5); ספרטה bleibt Σπάρτη vorbehalten. Der eigene 1.87.2-Vermerk korrigiert: fünf σπονδ-Vorkommen (nicht sechs) und «מניין הקולות» statt des Tippfehlers.
- Weitere Fixes: 1.84.1 (Hauptklausel ist überliefert intakt — die echte Anomalie ist ἀπαράσκευοι, jetzt vermerkt; direkte Anrede statt gnomischer 3. Person), 1.82.2-Vermerk ergänzt (ἴμεν), 1.83.3 (Zusatz «ראשית» getilgt; Vermerk um die αἰτία=מחלוקת-Kontextualisierung ergänzt), 1.90.2 (μᾶλλον und εἱστήκει wiederhergestellt — «חומות ההיקף העומדות כבר»; ἐχυροῦ-Vermerk), 1.90.3 (πρὸς ἑαυτῷ-Vermerk; «במהירות האפשרית»), 1.90.1-Vermerk (Partizipial-Paar), Kleinkram: 1.82.3 (ἤδη), 1.82.5 (נחתוך), 1.84.4 (ἀσφαλῶς), 1.87.1 (αὐτός), 1.87.2 (ἑαυτούς als «לכל אחד… בגלוי»), 1.89.2 («ולקח עמו»; ὑπεξέθεντο = הוצאו), 1.89.3 (רובם ohne Übertreibung), 1.90.5 (בקרוב ohne ממש).
- Bestätigt: σπονδ- = הסכם an allen fünf Vorkommen (die Vorab-Fixes des Koordinators hielten der Prüfung stand); Stimmenzählung wie überliefert, keine importierte Glosse; Themistocles’ θαυμάζειν bleibt unter ἔφη; Archidamus schließt am griechischen Marker (1.85.2/1.85.3); Sthenelaidas unmarkiert; alle Neun-Addendum-Namen auf dem Druck; מלך פרס-Disentangling dokumentiert; καταπροδιδόναι/τὸ κοινόν/μελέται-Vorschläge verifiziert und unterstützt.
- Buchhaltungskorrektur: kumulierter Abschnittszähler Batch 08 von 357 auf 314 berichtigt (271+43 — Rechenfehler des Koordinators im Emitter; UK/EN geprüft und fehlerfrei).
Alle 11 Meldungen angenommen (jeweils Text- oder Vermerkseingriff).

### Kap. 91–100 (Batch 10) — 39 Abschnitte
Zweitprüfung: work/he/review/batch10.md. Meldungen: 12 Minor in 15 Einträgen (0 Blocker).
- Spiegel-Treue: der über 1.100.2→3 erfundene Punkt über der überlieferten Mitten-komma getilgt — der Abschnitt endet jetzt wie der exemplarische Spiegel 1.93.3→4 mitten im Satz (komma-offen); die Wahl per Vermerk dokumentiert.
- Eigener Vorwurf angenommen: mein Global-Replace («באותה הגמוניה»→«באותו פיקוד») hatte die erste Zitatform im 1.94.2-Vermerk mitverändert, sodass er dieselbe Form als Wiedergabe und als „Alternative“ führte — nach dem Vorschlag des Prüfers neu gefasst; ebenso der 1.96.2-Vermerk, der die per Elft-Addendum ausgeschlossene Form «טלנט» noch vormerksweise vorschlug, auf „geklärt“ gesetzt.
- Drei fehlende Anomalie-Vermerke ergänzt: 1.95.4 (Doppel-τε-Koordination), 1.95.5 (μὴ ἀδικεῖν Präsens statt Aorist), 1.95.7 (ἐνεῖδον epische Form) + die Spiegel-Dokumentation 1.100.2; die Σanktion ἀνάγκαι = חיובים per Vermerk fixiert; die nicht gegen unsere quellenlose Datei verifizierbare ἀκινοῦντες-Konjektur aus dem 1.93.2-Vermerk entfernt.
- Register-Fixes: «דלוס הייתה להם לאוצרת» → «לאוצר» (הנון „curatrix“-Lesart weg), «בוצרו» → «הובצרו» + die Stimme von «ואת היתר התקינו» ins Passiv zurück (κατεσκευάζοντο), ἤχθοντο zweimal vereinheitlicht («התמרמרו בסתר»), 1.98.4 das baumelnde Subjekt geschlossen («והאתונאים יצאו עליהם»), 1.91 σαφῶς = «בבירור» (an 1.91.3 angeglichen) + zugesetztes «עוד» getilgt + «הדיה לשמור» → «במידה המספיקה לשמור», 1.97.2 λόγος = Erzählung («ממהלך הדברים») + die ausschließende Kraft von ὅσπερ καὶ und ἐπεμνήσθη wiederhergestellt («ורק הלניקוס הזכירם אף הוא»), 1.95.7 «לרועץ» → «גרועים מהם», 1.99.3 «מס כסף» → «תשלומי כסף» (der Tribut-Begriff bleibt φόρος vorbehalten).
- Bestätigt: sämtliche Sonderprüfungen bestanden — «In erster Linie» öffnet 1.98.1 (die parallele Auslassung existiert hier nicht), [Ἐννέα ὁδοί] dreifach als schlichte Apposition («תשע הדרכים», ohne Klammern, ohne Notiz), 1.99.1 keine Strafklausel importiert, Themistocles-Rede durchgängig indirekt bis zum überlieferten ἔφη, 1.93.3→4 exakt; die zwei Amts-Lesungen stehen exakt an 1.93.3/1.96.2, sonst שלטון ungeschönt; «באותו פיקוד» im Körper; Versklavungen ungeschönt; alle Zahlen (460 כיכר etc.); sämtliche Zehnt/Elft-Addendum-Namen im Druck, לקדמון ohne Regression.
- Vermerks-Hausordnung: von den fünf per Elft-Addendum obsoleten Namens-Proposal-Vermerken bleiben die vier bewilligenden als Dokumentation stehen (der Widerspruchsfall 1.96.2-טלנט behoben); die Vorlagen ἀνάγκαι/διαχείρισις/ξύνοδοι/ξυνεστράτευον vom Prüfer am Griechischen verifiziert und unterstützt.
Alle 12 Meldungen angenommen (11 mit Text- oder Vermerkseingriff; 1 als Spiegel-Dokumentation ergänzt).

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

- Übersetzte Abschnitte: 395 in den Kapiteln 1–100 (Hebrew); insgesamt Buch 1 hat 146 Kapitel / 580 Abschnitte.
- Durch Zweitprüfung geprüft: sämtliche 395 veröffentlichten Abschnitte (jede Portion durch einen unabhängigen Subagenten, jede Meldung durch die Koordination am griechischen Text entschieden; automatische Strukturprüfung je Portion ohne Fehler).
- Vom Prüfer beanstandet: kumuliert 139 Fundstellen (7 Blocker, 132 Minor).
- Geändert: sämtliche angenommenen Fundstellen im Textkorpus umgesetzt; abgelehnte Meldungen: keine dokumentiert; gegenstandslose Erhebungen: 0.
- Offen bzw. unsicher: die oben verzeichneten Stellen (Zeileneinträge mit „offen“/crux); keine davon blockiert die Veröffentlichung, alle Entscheidungen sind im Text oder in der Anmerkung sichtbar.
- Nicht veröffentlicht, obwohl work in progress: Kapitel 101–110: Übersetzung im Gang; Kapitel 111–146 noch nicht begonnen.
- Keine Behauptung von Fehlerfreiheit: geprüft heißt nicht fehlerfrei; künftige Portionen und Nachprüfungen können weitere Befunde bringen.
