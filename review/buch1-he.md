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

### Kap. 101–110 (Batch 11) — 42 Abschnitte
Zweitprüfung: work/he/review/batch11.md. Meldungen: 14 in 15 Einträgen (1 Blocker, 13 Minor).
- Blocker 1.101.1 (Vermerksebene): der Vermerk behauptete das Gegenteil unserer Bytes — die Quelle druckt ἐσβαλόντας (Akkusativ, byte-verifiziert; die echten ἐσβαλόντες stehen andernorts, z. B. 1.123.3); der Vermerk stellte den fehlenden Nominativ als „überliefert" und unseren Druck als „Konjektur" dar — nach der Regel „kein zitierter Variante ohne Byte-Beweis" FALSCH; komplett neu gefasst; der Körper war unschuldig. Mein Review-Prompt trug dieselbe Fehlprämisse (vom Übersetzer-Report übernommen) — dokumentiert.
- 1.108.2→3-Seam: erfundener Punkt über dem überlieferten Komma getilgt (Ende auf Komma wie die twice-bewährten Spiegel 1.93.3→4 und 1.100.2→3) + dokumentierender Vermerk; 1.109.3→4 (überliefertes Hochpunkt) korrekt belassen.
- Slot-Regression behoben: στρατηγοῦντος an allen fünf Stellen auf den athenischen סטרטגוס-Slot zurückgestellt (batch10-konsistent: 1.98.1/1.100.1); der alte Vermerk, das Γlosear „stehe nicht im Original", war falsch und ist neu gefasst.
- Λακεδαίμονα-Regression: «שלח לספרטה» → «שלח ללקדמון» (ספרטה bleibt Σπαρτιᾶται vorbehalten).
- Register/Grammatik: «בבלי» ×2 → «מבלי» (Majoritätsform der Edition; 1.36/1.90 als Schlussdurchgangs-Kandidaten vermerkt); 1.105.3 die Kausativ-Krücke («יגרמו להם») zur schlichten Notwendigkeit («ייאלצו להסתלק»); die überlieferten Parenthesen 1.104.2/1.105.6 von Gedankenstrichen zurück auf ( ) (batch10-Parallele 1.92.1); 1.107.2 die Alters-Klammer auf Pleistoanax umgehängt («פליסטואנקס — שעודנו היה נער — בן המלך פאוסניאס»); 1.110.3 das Umschreibungs-Bauplock («הוצא להורג על צליבה») zum schlichten Verb («נצלב»).
- Vermerks-Pflege: zwei fehlende Anomalie-Vermerke ergänzt (1.106.2 κατέλευσαν; 1.107.6 τοῦ δήμου καταλύσεως ὑποψίᾳ) + der Seam-Vermerk; vier Vermerks-Rewrites (1.101.1; 1.102.3-νεωτερ — der behauptete Wortstamm existierte im Druck nicht; 1.105-στρατηγοῦντος; 1.107.2-νέου — die „unentschiedene" Anbindung hätte die historisch unmögliche Lesart gedruckt); 1.110.3 benennt jetzt beide lebenden Lesarten; die ὁπλίτης-Liste korrigiert (1.107.5 strichbefreit); das unübliche «(Ἁλιαῖς)» aus dem 1.105.1-Vermerk getilgt.
- Bestätigt: ALLE Sonderprüfungen bestanden — Halieis im Körper (die EN-Panne fehlt hier), White Wall wie verordnet, historische Präsens einheitlich Präteritum (EN-konsistent, kein Nebeneinander), fünfzig Trieren, כוח חילופין, לשון המנדס, die ἔσχον-Doppellesart vorbildlich dokumentiert; Geheimversprechen an überlieferter Stelle; alle Zahlen (300, 70, 200, 1500+10000, 1000/14000, 62. Tag, ~12 Tage, 100 Geiseln, Jahr½, sechs Jahre, 50); sämtliche Zwölf/Dreizehn-Addendum-Namen auf dem Druck.
Alle 14 Meldungen angenommen (alle mit Text- oder Vermerkseingriff).

### Kap. 111–120 (Batch 12) — 35 Abschnitte
Zweitprüfung: work/he/review/batch12.md. Meldungen: 16 in 10 Einträgen (1 Blocker, 15 Minor).
- Blocker 1.120.2: ἐνηλλάγησαν — das einzige Vorkommen der Wurzel im ganzen Quelltext (byte-verifiziert; der Abschlussbericht des Übersetzers hatte die Existenz des Verbs geleugnet — die Falschmeldung dokumentiert) — von „באו עמם במגע“ auf die Unrecht-Seite gestellt („ומקרבנו — כל שכבר נעשה להם עוול בידי האתונאים — אינם צריכים לימוד“), der gestrandete Partitiv wieder auf die Verbündeten bezogen, der Crux-Vermerk mit byte-genaue Zitat ergänzt; die Konstruktion trägt jetzt den a-fortiori der Bündnisrede.
- 1.120.1 die οὐ-Skala korrigiert: beide Adjuncta stehen unter dem einzigen ὡς οὐ („ושלא קיבצו אותנו עתה“ als zurückgenommene Anklage, nicht als zweiter Schuldgrund); Crux-Vermerk (ὡς οὐ + das harte ἐψηφισμένοι… εἰσι) ergänzt; mein eigener Regel-Vermerk war im Griechischen korrumpiert (τὸ statt überliefert τὰ, προσκοπεῖν in hebräischen Buchstaben mitten im Griechischen — vom Prüfer codepunkt-verifiziert) — sauber neu geschrieben; der Reden-Kontinuitäts-Vermerk ergänzt (das Quellen-Anführungszeichen schließt außerhalb von Kap. 120; alle fünf ’ im Kapitel sind Elisionsapostrophe — verifiziert).
- 1.120.2-Rest: „אם יעדיפו הארצות שבחוף“ → „אם תיאבדנה“ (πρόοιντο = verloren gehen, nicht wählen); τοῖς κάτω von der Gebiets- auf die Personen-Lesung harmonisiert („אנשי החוף“ — parallel zu EN „those below“ und UK „тих, що внизу“); der Vermerk inventarisiert jetzt τοῖς κάτω, τὰ κάτω und μὴ ἐν πόρῳ wörtlich, die schwächere Lesart „לא במרחק מן הים“ bleibt gelebt dokumentiert.
- 1.114.2: τὸ πλέον wiederhergestellt („בעיקרו של דבר לא התקדמו עוד“) — die absolute Lesart („gar nicht mehr vorgerückt“) beseitigt; Vermerks-Anhang zur Ausführung.
- 1.116.1: die Boten-Inversion behoben („להודיע שיבואו לעזור“ — der Hilferuf, nicht die Selbstansage); ἐς προσκοπὴν τῶν Φοινισσῶν νεῶν vom Wächter-Duktus auf den Überfall-Sinn („לארוב לאוניות הפיניקיות“); der δεκάτου auf die Datum-Bewahrung angehoben („פריקלס — „העשירי“ — סטרטגוס“ + Regel-4-Notiz; die frühere Konstrual „בפעם העשירית לו“ war eine stille Lösung) — damit tri-sprachig deckungsgleich mit EN und UK; ἀπὸ Μιλήτου-Vermerk ergänzt (der Doppelantäzedenz bleibt offen).
- 1.118.2: ἰσχύς auf den Editions-Slot עוצמה rückgestellt (כוח bleibt δῠ́ναμις vorbehalten; der Prüfer verifizierte neun frühere עוצמה-Stellen — der Batch-08-Ledger damit editionweit geschlossen); μάλιστα → „לכל היותר“; die beiden fehlenden Vermerke ergänzt (σαφῶς ᾔρετο mit der Aufstiegs-Lesart = EN/UK-paritätisch, die Gegensatz-Lesart dokumentiert; die zeitliche ἀρχή).
- Vermerks-Ergänzungen: περὶ τῇ Ποτειδαίᾳ (1.119.1 — das Kapitel trug gar keinen Vermerk); εὖ δὲ παρασχὸν ἐκ πολέμου πάλιν ξυμβῆναι (1.120.3, die überlieferte Dunkelheit dokumentiert; der Körper auf „ומשעמדו יפה“ geglättet); das Register-Haar השליטים → הפקידים (τοὺς ἄρχοντας = die Beamten, nicht „Herrscher“).
- Namens-Adjudikation: „אנשי ביזנטיון“ genehmigt (Muster אנשי+Stadt wie אנשי סאמוס; mein eigener Vorschlag הביזנטים zurückgezogen; kein früheres Byzanz-Vorkommen im Buch, das anders entscheiden könnte — verifiziert); die drei Review-Proposals הקפריסאים/הדלפים/פריינה bewilligt; Priene wie Прієна/Priene ins Vierzehn-Addendum aller drei Briefings nachgetragen — der im EN fehlende Priene-Vermerk post facto ergänzt und für das nächste EN-Protokoll notiert.
- Bestätigt: der στρατηγοῦντος-Slot ×5 als סטרטגוס (eine Batch-11-Reparatur ohne Regression); σπονδ- und ὁμολογ- eindeutig getrennt (Fortschritt gegenüber den Batches 10–11); die Naht 1.115.4→5 auf dem überlieferten Komma gespiegelt; beide historischen Präsentien normalisiert; alle Zahlen wörtlich exakt; Regel 6 dicht (Milesier-Klage, samische Motive, Pissuthnes, Perikles, die Kongress-Rede an die Verbündet gerichtet — die zwei Verzerrungen behoben).
Alle 16 Meldungen angenommen (jeweils Text- oder Vermerkseingriff).
Nachtrag (Fable-Audit, 27.09.2026, über den geschlossenen Stand 1–120): zwei Batch-12-Adjudikationen des Koordinators ZURÜCKGEWIESEN und rückgängig gemacht — (1) τὸ πλέον 1.114.2 ist adverbial („בלי להתקדם עוד“); die Lesart „בעיקרו של דבר“ war eine mechanische Übertragung aus τὸ πλέον τοῦ χρόνου (1.118.2; Crawley: „and without advancing further returned home“) — der hebräische Entwurf hatte recht, sein Wortlaut wiederhergestellt. (2) ἐνηλλάγησαν 1.120.2 = „עמדו עמם במגע“ (LSJ-Medium; Crawley: „all who have already had dealings with the Athenians“); die Lesart „נעשה להם עוול“ war eine über die Koordinationsprompts getragene Überinterpretation — zurückgenommen; die legitime Reparatur des Partitiv-Bezugs bleibt erhalten („ומקרבנו — כל שעמדו עם האתונאים במגע — אינם צריכים לימוד כדי להישמר מהם“). Prozesseintrag wie im EN-Nachtrag.

### Kap. 121–130 (Batch 13) — 43 Abschnitte
Zweitprüfung: work/he/review/batch13.md. Meldungen: 6 MINOR in 10 Einträgen (0 Blocker; alle angenommen, plus eine vom Koordinator verfügte Schärfung).
- Alle drei Adjudikationsersuchen des Übersetzers zugunsten des Entwurfs entschieden: (1) «סעד» steht — das Etikett «גמול» in meinem rekonstruierten Fünfzehnten Addendum war ein Benennungsartefakt; der Prüfer bewies die gedruckten Slot-Stationen (1.25.1, 1.25.3) und das Dativ-Idiom; das Briefing ist berichtigt. (2) «מפקד ספרטה» steht — der militärische Slot; ein singulärer Selbsttitel in einem Kanzleibrief an den König schließt die Allianz-Vorstehens-Lesart von 1.120.1 (Plural) aus. (3) «מפיקודו» für ἀρχή 1.128.3 steht — die 1.95.6-ἄρχοντα-Präzedenz am Druck verifiziert, die 1.95.5-Kreuzreferenz des Vermerks wahr, und dieselbe Sektion druckt das Herrschafts-Wort getrennt als שלטון.
- Naht: die überlieferte Abschnittsnaht 1.121.2 auf 1.121.3 (Satzmitte) spiegelt jetzt ihr Schlusskomma (das 1.108.2-Muster); die vier Mittel-Punkt-Enden (1.122.2, 1.124.1, 1.128.4, 1.129.2) drucken als Punkte, ihre Fortsetzungen lexikalisch geführt («אלא», «שכן») — nichts abgetrennt, keine Änderung (Haar, hier dokumentiert).
- Vermerke: 44/44 wahr, jede griechische Zitation byte-exakt — der erste fehlerfreie Vermerk-Batch der Gesamtrechnung; drei Ergänzungen: das ναυτικὸν-Abstraktum 1.121.4 («ענייני הים»), die μονάρχους-Rückführung dokumentiert (1.122.3), die δῠ́ναμις-Slot-Kreuzung 1.127.3 gegen die batch-12-Gleichung (ἰσχύς = עוצמה, δῠ́ναμις = כוח) repariert und geflaggt.
- Rückführungen: μονάρχους 1.122.3 in den Plural («ואת השליטים בעיר בודדת») — die many-vs-one-Schneide des Arguments; τὸ πρῶτον 1.128.3 erste Station («בראשונה»); die beiden historischen Präsentien 1.129.1 normalisiert («ושלח … וציווה») — die einzige Zeitpolitik-Abweichung des Pakets.
- Schärfung: ἐκπεσόντος 1.127.1 «יוסר» zu «ייגרש» — der Prüfer nannte es Haar; der Koordinator schärfte der EN/UK-Sinnesparität wegen (LSJ ἐκπίπτω 4: banished).
- Formel-Station: mein Prüfauftrag nannte 1.36.3 — die τοιαῦτα-Station ist 1.36.4; der eigene Vermerk des Entwurfs zitiert richtig, mein Zitatfehler hier dokumentiert. Das Schlussformular byte-identisch mit 1.72.1; die Familie 1.79.1 / 1.53.3 bestätigt.
- Glossar: der dritte τιμωρία-Sinn (נקם למען נפגע, «נקם לאלים», 1.127.1) ins Briefing eingetragen; die beiden ersten Tiers am Druck verifiziert.
- Verifiziert: Xerxes wie überliefert (ארתחשסתא nirgends); beide Briefe je genau ein Zeichen-Paar, die Überschrift ὧδε λέγει in voller Länge; die drei Editor-Eingriffe nahtlos und klammerlos; alle Zahlen in Wörtern (die neun Archonten zweimal); der Ὀλυμπίᾳ-Ort gegen die Spiele scharf; Regel 6 an allen drei Rahmens — die Erzähler-Scharniere («כפי שנמצא לאחר מכן», «וזה מה שהעיד הכתוב») und das spartanische Erdbeben-Glaube («כך הם מאמינים») als ihre.
Alle 6 Meldungen angenommen; alle drei Adjudikationen für den Entwurf.

### Kap. 131–140 (Batch 14) — 38 Abschnitte
Zweitprüfung: work/he/review/batch14.md. Meldungen: 1 Blocker + 7 Minor in 13 Einträgen; sämtliche angenommen.
- Der Blocker ist getilgt: 1.135.1 — das überlieferte neutrale αὐτό meint die Unreinheit selbst; der Druck trug «לגרש אותו» (maskulin — der längst bestattete Pausanias), exakt die Lesart, die die EN-Prüfung eine Runde früher ersetzte; Ein-Wort-Fix «לגרש את הטומאה» plus neuer αὐτό-Vermerk mit der klassischen Bezeugung.
- Die fünf Adjudikationsersuchen: (1) Vers-Zeichen — am Griechischen BESTÄTIGT (kein Anführungszeichen im ganzen Kapitel 132, alle vier Apostrophe Elisionen); die Zeichen bleiben als besessene Konvention, geflaggt. (2) Die τιμωρία-Spaltung 1.136.4 — BESTÄTIGT: beide Vorkommen requital-of-the-wronged; «לנקום/נקם» richtig, die Abweichung geflaggt (EN-konvergent). (3) Die τόδε-Rahmenklausel 1.132.2 — MIT HALT, mit das hängende «דבק» existiert im Griechischen nicht («ἐπὶ τὸν τρίποδά ποτε τὸν ἐν Δελφοῖς … ἠξίωσεν ἐπιγράψασθαι»); die Klausel neu gefasst («וגם משום שעל הטריפוד שבדלפי …»). (4) εὐνοία-Offenheit — HALT (Haar unbeanstandet). (5) γράψας — die EN-Analyse stimmt byte-mäßig: Nominativ, verträglich mit dem Ich-Brief; προσεποιήσατο ist die eigentliche Anomalie; der Schreiber selbst der einzige tragfähige Bezug (Herodot 8.110); das uniforme Dritte-Person des Entwurfs übernormalisierte ein Verb — das Partizip in die erste Person zurückgevoziert («שכן כתבתי …»), das dritte Person «אשר בדה בשקר» bleibt roh, der Vermerk neu gefasst.
- Register: die biblischen Vayyiqtol-Ketten des Kapitels 134 kapitelweit normalisiert (בא/ונח; לכדוהו/גדרו/ישבו/והכריעוהו; יצא ומת; עשו/והקדישו — der 1.134.2-Vermerk mit dem neuen Druck-Wortlaut mitgeführt) plus die verstreuten Instanzen (135.3 ושלחו; 137.2–3 עשה/ונט/ושילם; 138.1 ואמר; 138.4 וחלה ומת; 139.3סection והחליטו; 139.4 בא וייעץ) — die Neuhebräisch-Regel des Briefings durchgesetzt; in den Kapiteln 100–119 kommt Vayyiqtol nach Prüfer-Suche nicht vor.
- Nikud: die rund fünfzehn punktierten Wörter aus allen Körpern entfernt, mit zwei Ersetzungen, wo die unpointierte Form holprig läse («מִטְעָמִים» → «מעדנים»; «הֻשַּׁחַד» → «נשוחד»); Vermerke bleiben ausgenommen; plus zwei Altkorpus-Strickler nachgeholt (ch. 21 «בהּ», ch. 73 «מעשהָ») — Reiter dieses Baues.
- Feinheiten: 1.132.5 «רשם» → «נרשם» (endliches Aktiv gegen den Reflexiv-Sinn des überlieferten ηὗρεν ἐγγεγραμμένον); 1.137.1 die Weigerungs-Wendung neu grammatisiert («לא מסר אותו; אלא שלח אותו») — das Admetus-Singular-Subjekt wiederhergestellt; 1.138.3 «ולא עמל-לימודים» → «ובמעט עמל-לימודים» (βραχύτητι heißt wenig, nicht keins — Sinnesparität mit EN/UK); der 1.138.2-Vermerk: das hebräische «טוֹ» durch das echte τὸ ersetzt; die 1.140.2-Vertragsformel-Personenverschiebung jetzt dokumentiert (normalisiert wie EN, Vermerk ergänzt).
- Vermerks-Bilanz: 62/62 wahr und byte-exakt; zwei Ergänzungen (αὐτό; die Vertragsformel), zwei Neufassungen (γράψας; die 1.134.2-Druckpassung), eine-call Präzisierung (τὸ).
- Die EN-Claims am HE: gehalten — die Herold-Konstruktion, ἔτι mit μᾶλλον, die Crux-Trios, die Ergänzungsnähte, die Perikles-Rahmen samt Kontinuität (die Schluss-Station jenseits der Partie bei 1.145.1 verifiziert), die Gesandten-Zeichen, sämtliche Zahlen, die historischen Präsentien (der erste reine Durchlauf eines Bereichs), der ἦρχε-Herrenz-Slot, δουλ- unweichlich. Gescheitert: 1.135.1 (der Blocker). Halb gehalten: 1.140.2 (normalisiert, aber undokumentiert — nun geflaggt).
- Registriert: die Lesernote 1.133.1 als gerechtfertigter echter Zweifelsfall, die einzige des Bereichs; Figur-Befunde (fünfzig Kikkar, die zwei Statuen, zwei Leiber für einen, das andre Meer, kein Grieche vor ihm).
- Glossar-Vorschläge des Übersetzers, übernommen wie gedruckt: סקיטלה; אוסטרקיזם; אוניית סוחר; בעל האונייה; מיטיב; אהובו (das längere אהוב-נעורים blieb unvermerkt optional); ὄψוד nun «מעדנים».
Der Blocker getilgt, alle 8 Meldungen angenommen; das Register erzogen und das Nikud aus den Körpern verbannt.

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

- Übersetzte Abschnitte: 553 in den Kapiteln 1–140 (Hebrew); insgesamt Buch 1 hat 146 Kapitel / 580 Abschnitte.
- Durch Zweitprüfung geprüft: sämtliche 553 veröffentlichten Abschnitte (jede Portion durch einen unabhängigen Subagenten, jede Meldung durch die Koordination am griechischen Text entschieden; automatische Strukturprüfung je Portion ohne Fehler).
- Vom Prüfer beanstandet: kumuliert 183 Fundstellen (10 Blocker, 173 Minor).
- Geändert: sämtliche angenommenen Fundstellen im Textkorpus umgesetzt; abgelehnte Meldungen: keine dokumentiert; gegenstandslose Erhebungen: 0.
- Offen bzw. unsicher: die oben verzeichneten Stellen (Zeileneinträge mit „offen“/crux); keine davon blockiert die Veröffentlichung, alle Entscheidungen sind im Text oder in der Anmerkung sichtbar.
- Nicht veröffentlicht, obwohl work in progress: Kapitel 141–146: Übersetzung im Gang.
- Keine Behauptung von Fehlerfreiheit: geprüft heißt nicht fehlerfrei; künftige Portionen und Nachprüfungen können weitere Befunde bringen.
