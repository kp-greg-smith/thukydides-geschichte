# Buch 2 (he): Übersetzungs- und Prüfprotokoll

Grundlage ist ausschließlich der griechische Text (`docs/grc/source.xml` / `docs/grc/book2.html`, Oxford-Ausgabe H. S. Jones; Extrakt `work/grc/b2/ch_NNN.txt`). Jede Portion von höchstens zehn Kapiteln (B01 = 1–10 … B11 = 101–103) wird durch einen Übersetzungs-Subagenten angefertigt, sodann durch einen zweiten, unabhängigen Subagenten abschnitts- und satzweise am Griechischen geprüft; zusätzlich prüft nach jeder Portion eine neue GLM-Session ohne Zugang zu `work/` und `review/` (nur griechisches HTML plus die drei Übersetzungs-HTML) nach demselben Prüfauftrag. Jede Meldung wird durch die Koordination am griechischen Text entschieden; Eskalationen an Astra (codex, `gpt-6-astra`, read-only) nach dem Astra-Protokoll, wörtlich protokolliert in `review/buch2-astra-log.md`. Automatische Strukturprüfung (`scripts/check_translation.py --language he --book 2`) je Portion.

Festlegungen, Glossar und Namensformen aus Buch 1 (`review/buch1-he.md`, `work/instructions_he.md`) bleiben verbindlich. Kennung in Buch 2: `2.Kapitel.Abschnitt`. Buch-2-Addenda (Glossar, Namen, Festlegungen) werden unten je Portion verzeichnet und am Ende in die READMEs nachgetragen.

## Festlegungen (Buch 2, bindend für die hebräische Ausgabe)

- Britische Rechtschreibung mit Oxford-„-ize“; latinisierte Namensformen; Anmerkungen als `[Note: …]`; Reden über mehrere Abschnitte ohne umschließende Anführungszeichen, kurze eingebettete Zitate mit „ “; Zahlen ausgeschrieben; `!! FLAG` nur intern. (Wie Buch 1.)
- Kapitel 35–46 (Grabrede des Perikles), 60–64 (letzte Rede), 71–74 (Plataier/Archidamos), 87, 89 (Kriegsrat/Phormion) gelten als Reden im Sinne der Stichprobenregel (6 statt 4 Stichproben je Sprache und Portion).
- Kein Rückgriff auf `docs/de/` (existiert für Buch 2 nicht) und keine moderne Übersetzung als Vorlage.

## Buch-2-Addenda

**השלמה חמישה־עשרה, פרקים 1–10 (B01, צורות מאושרות):** שמות: כריסיס (הכוהנת בארגוס); איינסיוס (אפור) — שיטתי לפי כלל αι→יי (הרכז העדיף על פני "אינסיוס" שהוצע); פיתודורוס (ארכון); פיתאנגלוס; פילידס; דימפורוס (הרכז הכריע: לא "דיאמפורוס", כדי שלא יישמע כ-δια-); אוניטורידס; נאוקלידס; אורימכוס; לאונטיאדס (מגזרת Λέων, נימוק המתרגם תוקן); נהר אסופוס; פלנה, אנשי פלנה; מילוס; תירה. אתניקונים: הלאוקדים, אנשי אנקטוריון. מילון: בויאוטארך (βοιωτάρχος); νεωτερείν ἐς τινά = מעשה מהומה/אלימות (2.3.1), μηδὲν νεώτερον ποιε῝ν = שום מעשה פזיז (2.6.2; הכרעת Astra, הבחנה לפי הקשר כדין כלל 1); ὀλίγον ἐπενόουν οὐδέν = "דבר קטן לא תכננו" (LSJ ἐπινοέω I.2 מצטט צירוף זה ממש; Astra); τὰ δύο μέρη = שני שלישים (LSJ מצטט את 2.10.2; מקבילה 2.47.2); מזמרי נבואות (χρησμολόγοι); דברי נבואה (λόγια); עוקץ הכידון (στυράκιον), היתד (βάλανος), בריח (μοχλός); אשמורת הלילה האחרונה (περίορθρον, hapax); בחסות הפסקת לחימה (ὑποσπόνδιος). הכרעות: 2.8.4 ἐν τούτῳ … ᾧ קורלטיבי ורפרפקט פרוספקטיבי (Astra); 2.5.5 δράσειαν בניין מסור תקין ללא הערה (Astra ביטל את ההערה שהוצעה); 2.5.6 εὐθύס חל על ההשבה, לא על ההבטחה (Astra); κῆρυξ = כרוז כצורה העומדת בספר 2 ("מטה חצרן" שב-1.53.1 נותר כפי שנדפס בספר 1, מחוץ לסמכות שינוי); ἀγορά = שוק (יישום ההרחבה המאושרת מספר 1).

## Portionen und Prüfungen

### פרקים 1–10 (חבילה B01) — 45 סעיפים
תרגום: סוכן משנה, 45/45 (1, 4, 4, 8, 7, 4, 3, 5, 6, 3); המבנה נבדק מכונית מול source.xml (כל המזהים קיימים, בסדר המקור). בדיקה: סוכן משנה עצמאי, דוח ב-`work/he/b2/review/batch01.md` — 12 ממצאים (2 חוסמים, 10 מינוריים). הכרעות הרכז:
- 2.2.1 תעתוק איינסיוס/דימפורוס → התקבל (הכרעת שמות שיטתית, ראו השלמה).
- 2.2.3 נימוק הדגל (Λέων/Λεωνίδας) → התקבל (דגל בלבד).
- 2.2.4 "באגורה" → "בשוק" → התקבל; בנוסף הרכז ביטל את תוספת "שדחקו בהם" בניגוד למתרגם ולבודק כאחד — הועבר לבדיקה קרה של Astra במסגרת הסטירה (2.2.4 נכלל בה), וממצא ה-παρ᾽ αὑτούס תלוי בשאילת ההבהרה (הכרעה תירשם ביומן Astra).
- 2.4.2 גנטיב תוצאה + דגל → התקבל ("— כך שלא נותרה להם דרך להימלט").
- 2.4.3 חוסם: סעיף התוצאה חסר + רומח→כידון → התקבל ("— כך שלא נותר עוד מוצא גם מדרך זו").
- 2.5.5 עדות שגויה בדגל → התקבל (דגל בלבד); הערת הקורא שהוצעה → נדחתה: Astra אישר שהקריאה כהאשמה תקינה ואינה דורשת הערה (יומן Astra).
- 2.6.3 ἐπέστελλον → התקבל ("הוסיפו לשגר את הוראתם").
- 2.6.4 סופרלטיב → התקבל ("חסרי התועלת שבאנשים").
- 2.7.2 חוסם: ייחוס האוניות הקיימות → התקבל ("בנוסף לאוניות שהיו להם שם"); בינוני-פועל ἑλομένοις → התקבל ("את אלה ... שבחרו בצדם").
- 2.8.1 "בכל מאודם", "בסערה" → התקבל (בוטלו/הוחלפו ב"תלויה ונרגשת"); הליטוטס → הרכז שינה נגד מתרגם ובודק כאחד ל"דבר קטן לא תכננו שני הצדדים" — אושר מפורשות בשאילת Astra (יומן Astra).
- 2.8.2 העברת ריבוי מן האנשים אל הדברים → התקבל ("ומזמרי הנבואות שרו רבות").
Astra B01: שאילת ה-cruxes: 2.6.2 "שום מעשה פזיז" (התקבל); 2.8.4 קורלטיבי ("כל עניין שהוא עצמו לא ייטול בו חלק — ייעצר"); 2.5.5 — הערת הקורא בוטלה, הקריאה אושרה; 2.10.2 אושר. סטירה (Seed 20260928: 2.2.4, 2.4.1, 2.6.4, 2.7.1): 2.4.1 תקין; 2.6.4 תקין; 2.2.4 "גמרו בדעתם" (התקבל) + ה-παρ᾽ αὑτοὺס (תלוי שאילת הבהרה); 2.7.1 "וכרתו ברית עם כל הערים" (התקבל).
הודעות שנדחו: 1 חלקית — 2.5.5 הערת הקורא (Astra: הקריאה תקינה ואינה טעונת הערה); תיעוד ביומן Astra.
בדיקה שנייה (הפעלת GLM חדשה, יוונית + שלושת קובצי ה-HTML בלבד): תתווסף להלן.
מקומות פתוחים: ה-παρ᾽ αὑτοὺס שב-2.2.4 ושני סעיפי הבקשה האוקראינית — ממתינים לתשובות Astra; יירשמו מיד עם ההכרעה (יומן Astra).

## Offene und unsichere Stellen

(wird je Portion nachgetragen)

## Zahlen

(wird am Ende vervollständigt: übersetzte Abschnitte, beanstandete, geänderte, abgelehnte Meldungen, Astra-Anfragen mit Korrekturen, offene unsichere Stellen)
