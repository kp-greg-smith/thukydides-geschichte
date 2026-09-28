# Astra-Log Buch 2

Jede Anfrage an Astra (codex exec -s read-only, Modell gpt-6-astra) wörtlich protokolliert: Stelle, Frage, Antwort (Auszug der Entscheidungsgründe), Umsetzung durch die Koordination. Keine Frage zweimal; mehrere Stichproben-Abschnitte einer Sprache gebündelt. Die wörtlichen Frage- und Antworttexte liegen committed unter `review/astra/b2_b01_<kennung>.txt` (Q&A je Datei).

Token-Disposition (Pflicht ab B02, rückwirkend für B01 erfasst): Aufruf jeweils aus `/tmp/astra-empty` mit `--skip-git-repo-check`, alle nötigen Texte inline, Beginnzeile „Answer from the text in this prompt only. Do not search for or read any files. Reply briefly.", reason `medium` (Fälle d/e) bzw. `high` (Fälle a/b/c), nie `xhigh`. Zielwert unter 500.000 Tokens je Portion.

- **B01: 5.088.975 Tokens** (Summe der höchsten total_tokens je Sitzungsdatei unter `~/.codex/sessions/2026/09/28/`; Anfrage 1 ≈ 1,24 Mio., 2.2.4-Klärung ≈ 1,21 Mio., Umgebung 2.7.3/2.9.2 ≈ 1,96 Mio., Stichproben zusammen ≈ 0,5 Mio., daneben drei abgebrochene Erstläufe ohne Prüfauftrag ≈ 0,22 Mio.). **Zielwert um den Faktor 10 überschritten.** Ursachen: (1) Aufruf aus dem Repo — Astra las Projektdateien und suchte im Web; (2) reason effort `xhigh`; (3) drei Erstläufe der Stichproben ohne expliziten Prüfauftrag, die mit Rückfragen ins Leere liefen. Ab B02 gelten die Regeln oben; die Sitzungsumme wird je Portion hier nachgetragen.


## B01 (Kap. 1–10)

### Anfrage 1 — offene Crux-Fragen, alle Sprachen betreffend (review/astra/b2_b01_1_cruxes.txt, 2026-09-28)
Fragen (Auszug wörtlich, fünf Passagen):
1. 2.3.1 «ἄλλως τε καὶ ἐπειδὴ ἐς οὐδένα οὐδὲν ἐνεωτέριζον» — EN-Entwurf „the Thebans were attempting no new thing against anyone". Frage: wörtlich „nothing new" oder idiomatisch „nothing hostile/rash"?
2. 2.6.2 «μηδὲν νεώτερον ποιεῖν περὶ τῶν ἀνδρῶν» — EN-Entwurf „to do nothing new about the Thebans". Dieselbe Frage.
3. 2.5.5 «λέγοντες ὅτι οὔτε τὰ πεποιημένα ὅσια δράσειαν ἐν σπονδαῖς σφῶν πειράσαντες καταλαβεῖν τὴν πόλιν» — EN-Entwurf „what had been done was unholy — attempting … to seize their city". Frage: Textproblem oder überliefertes Idiom? Standardlesart? Ist eine Lesernotiz gerechtfertigt?
4. 2.8.4 «ἐν τούτῳ τε κεκωλῦσθαι ἐδόκει ἑκάστῳ τὰ πράγματα ᾧ μή τις αὐτὸς παρέσται» — Entwurf A (prospektiv: „would be hindered if he himself were not present") gegen Entwurf B (retrospektiv: „had been hindered where he was not present"). Welche Aspektlesart ist Standard?
5. 2.10.2 «ξυνῇσαν τὰ δύο μέρη ἀπὸ πόλεως ἑκάστης» — EN-Entwurf „the two-thirds from each city". Frage: zwei Drittel oder zwei Kontingente?

Antworten (Astra, gpt-6-astra):
1. Idiomatisch, kein Textproblem. LSJ νεωτερίζω I.2 („use forcible measures")-zitiert gerade diese Stelle; „nothing new" verschleiert die Kraft. Vorschlag: „especially since the Thebans were taking no hostile action against anyone" („hostile" präziser als „rash").
2. Idiomatisch, kein Textproblem. „to take no rash action concerning the Thebans …"; bloßes „nothing new" führe im modernen Englisch in die Irre; „irreversible" sei kontextuell, nicht lexikalisch.
3. Überlieferte Konstruktion, keine Emendation nötig. δράσειαν = 3. Pl. Aorist Optativ von δράω in oratio obliqua nach historischem Verbum; Subjekt die Thebaner, τὰ πεποιημένα Objekt, ὅśnia prädikativ. Der Entwurf gibt den Sinn richtig wieder. „The compressed wording does not itself justify a textual-uncertainty note; it can stand unannotated."
4. Prospektive Lesart (Entwurf A) Standard; kein Textproblem. Zusatzkorrektur: ἐν τούτῳ … ᾧ korrelativ („in that [respect] in which"), nicht „in this eagerness"; Vorschlag: „Each thought that any undertaking in which he himself did not take part would be held up."
5. „Two-thirds". Konventioneller Bruchausdruck ohne Nenner (Smyth §1125a); „two contingents" verliere den Bruch.

Umsetzung:
1.–2. EN 2.3.1 „taking no hostile action"; EN 2.6.2 „to do nothing rash about" (jew. FLAG dokumentiert die Astra-Ruling). UK 2.6.2 «нічого необачного»; UK 2.3.1 hatte die hostile-Lesart bereits («нічого ворожого»). HE 2.6.2 «שום מעשה פזיז»; HE 2.3.1 hatte die hostile-Lesart bereits («דבר של מהומה»). Konsistenzvermerk: νεωτερ-Stamm je Kontext (feindliche Handlung / rash step) — Differenzierung regel-1-konform; Addendum-Eintrag folgt.
3. EN/UK unverändert (Lesart bestätigt). HE: geplante Lesernote (Kategorie a) NICHT bestätigt → Note entfernt; Körper unverändert.
4. EN/UK/HE 2.8.4: Körper nach Astra umgestellt auf die korrelative prospektive Lesart (EN „any undertaking in which he himself did not take part would be held up"; UK «спиниться та справа, у якій він сам не братиме участі»; HE «כל עניין שהוא עצמו לא ייטול בו חלק — ייעצר»); FLAGS dokumentieren die Ruling. ABGELEHNT damit die UK-Prüfermeldung 2.8.4 (retrospektiver Perfekt) — Begründung: Astra-Urteil (Anfrage 4) bestätigt die prospektive Standardlesart; die Meldung wäre eine Aspektumkehr gegen die Überlieferung.
5. EN/UK/HE „two-thirds“/«дві третини»/«שני שלישים» bestätigt; FLAGS um LSJ/2.47.2-Beleg ergänzt. Kein Eingriff nötig.

### Anfrage 2 — En-Stichprobe B01 (review/astra/b2_b01_2_sample_en.txt, 2026-09-28; Zufallsauswahl Seed 20260928: 2.4.1, 2.4.8, 2.5.6, 2.8.2; Auftag: satzweise kalte Prüfung, „report only real problems“)
Antwort (Auszug wörtlich):
- 2.4.1: „correct."
- 2.4.8: „correct."
- 2.5.6: „εὐθὺς … ἀποδώσειν concerns returning the men immediately. ‚Promised at once‘ attaches the timing to the promise. Render: ‚do not admit promising to return the men immediately, but only after preliminary negotiations, if agreement were reached.‘"
- 2.8.2: „correct."
Umsetzung: 2.5.6 EN umgestellt auf „promised to give the men back immediately“ (εὐθύς zur Rückgabe, nicht zum Versprechen). Dasselbe Problem in HE 2.5.6 («שהבטיחו מיד להשיב» → «שהבטיחו להשיב את האנשים מיד») parallel korrigiert. UK 2.5.6 war bereits richtig («обіцяли видати мужів негайно» — εὐθύς bei der Rückgabe); 1 Korrektur EN, 1 Korrektur HE aus dieser Anfrage.

### Anfrage 3 — HE 2.8.1, Kategorie b (review/astra/b2_b01_3_he_2-8-1.txt, 2026-09-28)
Frage (Auszug wörtlich): „Is the transmitted sense of ἐπενόουν here ‚they were planning/contriving‘ (… draft A and draft C), or ‚they had in view / took care of‘ (… draft B)? Which drafts are correct?“
Antwort (Auszug wörtlich): „A and C are correct on the disputed clause; B is not. LSJ, s.v. ἐπινοέω I.2, gives ‚have in one’s mind, intend, purpose‘ and explicitly cites ὀλίγον οὐδέν, Th. 2.8. … B introduces neglect, which the Greek does not express, and changes the force of the negative."
Umsetzung: HE 2.8.1 Körper auf Entwurf C umgestellt («דבר קטן לא תכננו שני הצדדים»); FLAG dokumentiert Rechtsgrund (Koordinator überstimmt hier HE-Übersetzer und HE-Prüfer, mit Astra-Bestätigung). EN und UK trugen die richtige Konstruktion bereits.

### Anfrage 4 — UK-Stichprobe B01 (review/astra/b2_b01_4_sample_uk.txt, 2026-09-28; Zufallsauswahl Seed 20260928: 2.4.2, 2.5.3, 2.7.3, 2.9.2)
Antwort (Auszug wörtlich):
- 2.4.2: „τῶν διόδων ᾗ χρὴ σωθῆναι — «якими мав відбутися порятунок» is unnatural Ukrainian. Use «якими можна було врятуватися»."
- 2.5.3: „correct."
- 2.7.3: zwei Befunde — ἐξήταζον («оглядали свій чинний союз» unnatürlich → «перевіряли стан свого наявного союзу») und καταπολεμήσοντες («replace … with «зможуть воювати проти Пелопоннесу з усіх боків»»).
- 2.9.2: zwei Befunde — ἐντὸς Ἰσθμοῦ («Use «по пелопоннеський бік перешийка»») und τούτοις δὲ ἐς ἀμφοτέρους φιλία ἦν (kalquesierte Grammatik → «вони підтримували дружні стосунки з обома сторонами»).
Umsetzung: 2.4.2 angenommen («якими можна було врятуватися»). 2.7.3a angenommen («перевіряли стан свого наявного союзу»). 2.9.2b angenommen, unter Beibehaltung des φιλία-Slots «приязнь» aus Buch 1: «ці ж були в приязні з обома сторонами». 2.7.3b und 2.9.2a — Widerspruch zu anderen Befunden der Pipeline → separate Klärungsanfragen (Anfragen 6 und 7). Aus dieser Anfrage direkt: 3 angenommene Korrekturen.

### Anfrage 5 — HE-Stichprobe B01 (review/astra/b2_b01_5_sample_he.txt, 2026-09-28; Zufallsauswahl Seed 20260928: 2.2.4, 2.4.1, 2.6.4, 2.7.1)
Antwort (Auszug wörtlich):
- 2.2.4: „«γνώμην δ' ἐποιοῦντο» — «עשו מחשבה» אינו ניסוח טבעי; עדיף «גמרו בדעתם». «τίθεσθαι παρ᾽ αὑτοὺς τὰ ὅπλα» — … «αὑτοὺς» הוא ברבים, ולכן «אצלו» שגוי."
- 2.4.1: „correct."
- 2.6.4: „correct."
- 2.7.1: „«ובנות ברית עשו להם כל עיר» משובש בהתאמת המספר ובניסוח. אפשר: «וכרתו ברית עם כל הערים שהיו מחוץ לתחום כוחם»."
Umsetzung: 2.2.4a angenommen («גמרו בדעתם»); 2.7.1 angenommen («וכרתו ברית עם כל הערים שהיו מחוץ לתחום כוחם»); 2.2.4b (παρ᾽ αὑτούς) → Klärungsfrage (Anfrage 6). Aus dieser Anfrage direkt: 2 angenommene Korrekturen.

### Anfrage 6 — 2.2.4 παρ᾽ αὑτούς, alle Sprachen (review/astra/b2_b01_6_par-autous.txt, 2026-09-28)
Frage (Auszug wörtlich): „What does the transmitted παρ᾽ αὑτοὺς most plausibly mean here — reflexive referring to τις despite the number mismatch, or pointing to the Thebans? … Should a faithful modern translation print ‚at his own side‘, ‚beside them‘, or keep the openness with a brief reader note?“
Antwort (Auszug wörtlich): „(a) ‚Beside the Thebans‘ is the more plausible reading. Retaining αὑτούς, I would understand it as an indirect reflexive, looking back to the Thebans whose invitation the herald delivers … (Smyth §§1225–26). The strongest support is … Gomme … ‚take his place with them‘ … Crawley ‚ground arms with them‘. … The reviewer’s number argument alone is too categorical … (b) I would print ‚place his arms beside them‘, with the brief note: ‚Beside the Thebans, signifying that he joined their side.‘“
Umsetzung: Widerspruch zu allen drei gedruckten Lesarten („at his own side“ / «коло себе» / «אצלו») — Astras Lesart gilt: EN „beside them [Note: beside the Thebans, signifying that he joined their side.]“; UK «коло них [Прим.: коло фіванців — на знак прилучення до їхнього боку]»; HE «לידם [הערה: ליד התבנים — בסימן הצטרפות אל צדם]». FLAGS in allen drei Dateien dokumentieren die Ruling samt Bezeugung; Dissens des Koordinators: keiner — die übertragene Mehrzahl des Reflexivs und die zitierten Zeugen tragen die Lesart.

### Anfrage 7 — 2.7.3 καταπολεμήσοντες und 2.9.2 ἐντὸς Ἰσθμοῦ (review/astra/b2_b01_7_katapoleme-entos-isthmou.txt, 2026-09-28)
Frage (Auszug wörtlich): zwei Kandidatenpaare, je „which candidate matches the standard construal … Is the rejected candidate actually wrong, or merely less precise?“
Antwort (Auszug wörtlich):
- 2.7.3: „Prefer (ii) for the standard resultative construal. LSJ s.v. καταπολεμέω gives ‚to war down': reduce or subdue by warfare. … ‚they would subdue the Peloponnese by attacks from all round‘ preservation both elements. … Candidate (i) is less precise, rather than simply wrong … Lexicon Thucydideum explicitly assigns 2.7.3 to bello infestare, ‚harass with war.‘ Consequently, one should not present (ii) as the only defensible translation."
- 2.9.2: „Candidate (i) is correct traditional shorthand; (ii) makes its meaning explicit. The Isthmus serves as a boundary: ‚within‘ means within the peninsula on its Peloponnesian side … Explicitly saying ‚south of‘ … improves clarity for modern readers but is not required for correctness."
Umsetzung:
- 2.7.3: UK bleibt auf der resultative Lesart («підкорюватимуть війною весь Пелопоннес навкруги») — die im Sample-Postulat für UK angebotene Schwächung wird damit zurückgenommen, die UK-Prüfermeldung (subdue-Force) bestätigt; EN von (i) auf (ii) gebracht („they would subdue the Peloponnese waging war upon it from all round“); HE von (i) auf (ii) gebracht («יוכלו להכניע את הפלופונסוס במלחמה מכל סביביו»). Der Lexicon-Thucydideum-Befund (bello infestare) ist in FLAGS dokumentiert, nicht angenommen.
- 2.9.2: ABGELEHNT die Sample-Meldung, die eine Umstellung auf „on the Peloponnesian side of the Isthmus“ verlangte — Begründung: Astras eigene Klärung weist (i) „within the Isthmus“ als korrekte traditionelle Kurzform aus; EN/UK/HE bleiben unverändert („within the Isthmus“ / «в межах перешийка» / «בתוך המצר»). Kein Eingriff.

### Anfrage 8 — UK 2.3.4 περίορθρον (review/astra/b2_b01_8_periorthron.txt, 2026-09-28)
Frage (Auszug wörtlich): „does τὸ περίορθρον mean ‚the last watch of the night, about dawn‘ (from ὀρθρός, dawn — supporting the proposed correction, the English and the Hebrew), or ‚the dead of night / small hours‘ (supporting the current Ukrainian)?“
Antwort (Auszug wörtlich): „τὸ περίορθρον denotes approaching dawn, here just before daybreak. — LSJ, s.v. περίορθρος: ‚towards morning: τὸ π. dawn,‘ explicitly citing Thucydides 2.3. — Thus the phrase means ‚while it was still night, at the very point before dawn.‘ … «саму глуху її пору» loses the essential reference to approaching dawn."
Umsetzung: UK 2.3.4 «саму глуху її пору» → «над саму пору перед світанком» (Koordinator überstimmt hier UK-Übersetzer und UK-Prüfer, mit Astra-Bestätigung); FLAG dokumentiert. EN („at the very point before daybreak“) und HE («אשמורת הלילה האחרונה») hatten die richtige Stunde bereits; die frische GLM-Session hatte exakt dies als UK-Einzigbefund gemeldet — ihr Befund ist damit bestätigt und erledigt.

Zweite Prüfung der frischen GLM-Session (2026-09-28): Befundstatus en 0 / uk 1 / he 0; die Beobachtung zur eckigen Klammer in HE 2.5.5 bezog sich auf einen veralteten Build-Stand (die Note war bereits nach Anfrage 1.3 entfernt; nach Rebuild bestätigt); der UK-Befund (περίορθρον) über Anfrage 8 akzeptiert und angewandt. Alle übrigen Prüfpunkte (Zahlen, Namen, Bündnislisten, indirekte Rede, Verneinungen) von der Session in allen drei Sprachen bestätigt.



## B02 (Kap. 11–20)

Token-Disposition B02: **101.412 Tokens** (7 Sitzungen: Obelos 13,8k; δέκατος αὐτός/τὰ ἄγη 13,6k; Lesarten 14,5k; drei Stichproben à ~15k; Klärung ξυναγωγή/Demonym 13,4k) — Zielwert „unter 500.000“ **eingehalten** (B01: 5,09 Mio.; Ursachen dort beseitigt: Aufruf aus /tmp/astra-empty, alles inline, keine Dateisicht, reason medium/high statt xhigh).

### Anfrage 9 — 2.15.4 Obelos, geplante Anmerkungen (review/astra/b2_B02_obelos.txt, 2026-09-28, effort=high)
Frage (Auszug wörtlich): „(a) Is this evident-sense reading of the dagged clause the standard one …? (b) Is the factual reader note warranted, or should the passage go unannotated? (c) Is any more specific elliptic supplement standard?“
Antwort (Auszug wörtlich): „(a) Yes as to the intended sense you describe, with ‚southern‘ supplied by context. … (b) The note is warranted: it reports the marked corruption and explains the translation’s treatment. … (c) … establishes no specific standard elliptic supplement. An evident-sense rendering does not imply an agreed reconstruction."
Umsetzung: alle drei faktualischen Notizen (EN/UK/HE) bleiben gedruckt (Kategorie a erfüllt); keine Rekonstruktion, keine Strich-Ergänzung; Körper unverändert.

### Anfrage 10 — 2.13.1 δέκατος αὐτός und τὰ ἄγη (review/astra/b2_B02_dekatos-age.txt, 2026-09-28, effort=medium)
Frage (Auszug wörtlich): „which reading is standard for ‚δέκατος αὐτός‘ here? … what does transmitted ‚τὰ ἄγη‘ mean in this sentence, and which rendering is correct?“
Antwort (Auszug wörtlich): „(iii) is standard: δέκατος αὐτός means ‚himself as the tenth,‘ counting him with nine others—thus ‚one of the ten generals.‘ … The same idiom makes πέμπτον αὐτὸν στρατηγόν ‚himself one of five generals,‘ not ‚serving his fifth term‘ … (c) is correct: τὰ ἄγη is the plural of ἄγος, ‚religious pollution‘ or ‚defilement.‘ … προεῖπον … ἐλαύνειν expresses a prior demand."
Umsetzung: EN „for the tenth time“ → „himself one of the ten“; UK «десятим уже стратегом» → «сам десятим, один із колегії десяти»; HE stand bereits auf dieser Lesart («כאחד מעשרת הסטרטגוסים») und wurde bestätigt — die BLOCKER-Meldung des HE-Prüfers („in der zehnten Amtszeit“) damit ABGELEHNT; ESC-Widerspruch dokumentiert: die JHS-Studie „ΔΕΚΑΤΟΣ ΑΥΤΟΣ“ gibt Perikles eine Sonderstellung, doch das B01-Audit (1.46.2, 1.116.1) trägt die Idiom-Lesart. τὰ ἄγη: EN „cattle“ → „pollutions“; UK «кіз» → «скверни»; HE «הטומאות» bestätigt; Classen-Steup „sacred flocks“ und die „goats“-These dokumentiert, verworfen. Korrekturen aus dieser Anfrage: EN 2, UK 2, HE 0 (+Flags).

### Anfrage 11 — Lesarten 2.13.9 / 2.15.2 / 2.11.9 (review/astra/b2_B02_lesarten.txt, 2026-09-28, effort=high)
Frage (Auszug wörtlich): „which sense of περιέσεσθαι τῷ πολέμῳ is standard …? does ξυντελούτων ἐς αὐτήν here mean the people gathering … or the towns paying their contributions …? what does ἐπ‘ ἀμφότερα most plausibly govern …?“
Antwort (Auszug wörtlich): „1. ‚Prevail‘ (B) … 2. Contributions/revenues (B) … 3. The possible outcomes … Render: ‚bring the greatest credit or discredit upon our forefathers and ourselves, according to the outcome.‘“
Umsetzung: περιέσεσθαι = „prevail“ (EN „come safely through“ ersetzt; UK «пронесуть» → «переможуть»; HE «יעמדו» → «תהא ידם על העליונה» — die HE-Prüfermeldung damit angenommen). ξυντελούντων = Beiträge: EN stand already richtig; UK «стягнулися» → «несли до нього свої внески» (die UK-Prüferin hatte das Lesarten-Signal richtig beschrieben, die Korrektur folgte hier); HE stand richtig. ἐπ’ ἀμφότερα = die zwei Ausgänge: alle drei Körper auf „wie auch immer der Ausgang …“-Formen umgestellt; Astras explizite „credit or discredit“-Amplifikation NICHT übernommen (δόξα unamplifiziert gelassen) — Dissens dokumentiert; UK-Flag hält die Regelung fest.

### Anfragen 12–14 — Stichproben B02 (review/astra/b2_B02_sample_en/uk/he.txt, 2026-09-28, effort=medium; Seed 20261005; je 6 Abschnitte, Redeminde ≥2)
EN (2.11.2, 2.12.1, 2.13.2, 2.14.2, 2.15.2, 2.20.5): 2 Befunde — 2.13.2 „the monies of this revenue“ verdeutlicht zu „from these — the monies of the tribute brought in from the allies“; 2.13.7 πρὸς τὸν κύκλον τοῦ ἄστεως = „as far as the circuit of the city“ (vorher neutral „in relation to“). UK (2.11.1, 2.11.5, 2.11.6, 2.12.2, 2.13.7, 2.20.3): 3 Befunde — 2.11.6 Negationslogik („хіба що вже тепер рушили“ → „хіба що вони вже тепер у дорозі“), 2.12.2 ἤν τι βούλωνται konditional („чого забажають“ → „якщо чого забажають“), 2.13.7 ὁπότε…ἐσβάλοιεν generell („коли ворог мав вторгнутися“ → „на випадок, коли б ворог вторгся“). HE (2.11.1, 2.13.5, 2.13.7, 2.16.2, 2.18.4, 2.20.5): 2 Befunde — 2.13.5 ἐξείργωνται klar gemacht («אם תיחסם בפניהם כליל הגישה לכל יתר המשאבים»), 2.13.7 τὸ πρῶτον = „בתחילה“ statt „בפעם הראשונה“ + πρὸς τὸν κύκλον = „עד חומת העיר“. Alle Befunde umgesetzt (7 Textkorrekturen insgesamt; EN/UK/HE-Flags dokumentieren ihre Stellen).

### Anfrage 15 — ξυναγωγή 2.18.3 und HE-Demonym (review/astra/b2_B02_synagoge-demonym.txt, 2026-09-28, effort=medium)
Frage (Auszug wörtlich): „(1) … ἐν τῇ ξυναγωγῇ τοῦ πολέμου … Which construal is standard? (2) … should the established form be kept?“
Antwort (Auszug wörtlich): „(1) The supplied text alone does not establish which construal is standard … (2) Yes. Keep התבנים: the binding house list and consistency across books govern."
Umsetzung: (1) Astra-Ausnahme der Beweislast — Entscheidung gemäß Punkt 5 der Arbeitsweise am Griechischen durch den Koordinator: UK auf die Mobilisierungs-/Zeitlesart umgestellt («ще при першому згромадженні війська, на самому початку війни»), Begründung: subjektiver Genitiv, Kontext der Mobilmachungs-Verzögerungen, EN/HE bereits auf dieser Lesart, klassische Zeugen laut Zweitprüfung zeitlich; die frühere Lesart „Kriegsversammlung“ des UK-Übersetzers und des UK-Prüfers (die den Genitiv selbst als dunkel geflaggt hatte) damit überstimmt — Risiko dokumentiert. (2) Die Zweitprüfungs-Meldung zur HE-Demonym-Form (התבנים → התבאים) ABGELEHNT (Astra + bindende Hausliste; Buch 1 druckt התבנים).


## B03 (Kap. 21–30)

Token-Disposition B03: **72.991 Tokens** (5 Sitzungen: ἐκακίζειν 13,9k; drei Stichproben à ~15k; Lesarten 2.29.2/2.29.6 14,5k) — Zielwert unter 500.000 **eingehalten**.

### Anfrage 16 — 2.21.3 ἐκακίζειν (review/astra/b2_B03_ekakizon.txt, 2026-09-28, effort=high)
Frage (Auszug wörtlich): „what does ἐκάκιζον mean here? Candidate A: ‚reviled/abused him‘ … Candidate B: ‚accused him of cowardice‘ … should a translation make the cowardice charge explicit in the verb itself, or keep the verb general?“
Antwort (Auszug wörtlich): „A is standard among the three supplied translations, but their general wording does not disprove a specific cowardice sense. The reported passage-specific lexicon gloss supports B, if accurately reported. Thus, ‚reviled/reproached him for not leading them out‘ is defensible. The prompt alone does not establish that cowardice must be explicit.“
Umsetzung: alle drei Körper bleiben auf der allgemeinen Lesart (EN „reviled him“, UK «лаяли його», HE „חרפוהו“) — sie sind damit deckungsgleich; die vom UK-Prüfer unterstützte Verstärkung «ганьбили, мовляв, боягузує» NICHT übernommen; der lexikalische Nuancenbefund (militärischer Gebrauch = Vorwurf der Feigheit) bleibt im UK-Flag als Glar-Hinweis dokumentiert.

### Anfragen 17–19 — Stichproben B03 (review/astra/b2_B03_sample_en/uk/he.txt, 2026-09-28, effort=medium; Seed 20261005; je 4 Abschnitte, keine Redekapitel im Bereich)
EN (2.22.1, 2.24.2, 2.28.1, 2.30.2): 0 Befunde. UK (2.22.3, 2.25.1, 2.27.1, 2.29.5): 1 Befund — 2.22.3 ἀπὸ τῆς στάσεως ἑκάτερος = lokale Gruppierung, nicht «сторона громадянської війни»; korrigiert zu «кожен від свого угруповання» (nach dem Muster der 2.20.4-Entscheidung; Flag dokumentiert die Abweisung des Kriegsslots). HE (2.21.3, 2.22.3, 2.27.1, 2.29.3): 3 Befunde, davon 2 angenommen: 2.22.3 κατὰ πόλεις ἄρχοντες = „den restlichen Kontingenten stehen Befehlshaber je nach ihrer Stadt“ («וגם ליתר האנשים היו מפקדים, איש לפי עירו» statt „ראשים בשאר הערים“); 2.29.3 ἐν ἀηδόνος μνήμῃ = „bei Erwähnung der Nachtigall bei den Dichtern“ (alle drei Sprachen korrigiert: EN „at the mention of“, UK «при згадці», HE „בהזכירם“; formerly „in memory of“-Formen). 1 abgelehnt: 2.21.3 ἡ γῆ ἐτέμνετο als „verwüstet/ausgeplündert“ — abgelehnt, weil der Slot τέμνω (Erde) = Schneide-Familie durch die B02-Konsistenzentscheidung bindend ist und EN/UK dieselbe Figur drucken («cut up»/«краяли»); Ablehnung im Flag dokumentiert (Präzedenz: B02, 2.9.2-Entscheidung).

### Anfrage 20 — 2.29.2 und 2.29.6 (review/astra/b2_B03_lesarten-29.txt, 2026-09-28, effort=high)
Frage (Auszug wörtlich): „(1) … Reading A (comparative) … Reading B (partitive) … Which construal is standard? (2) … Reading A: HE persuaded the Athenians to give Therme back TO Perdiccas … Reading B: he persuaded Perdiccas to give Therme back … Which direction is correct?“
Antwort (Auszug wörtlich): „1. B: spatial/partitive — he extended the Odrysian kingdom over a greater portion of the rest of Thrace. … 2. A: the Athenians restore Therme to Perdiccas. αὐτῷ is the recipient dative with ἀποδοῦναι; ‚the Athenians,‘ as those persuaded, is understood. Reading B misassigns the dative.“
Umsetzung: (1) EN auf das partitive Verständnis umgestellt; UK «на більшу частину решти Фракії» bestätigt; die abweichende Komparativ-Anregung ZWEITER PRÜFER (ausdrücklich unter Berufung auf moderne Übersetzungen) damit ABGELEHNT — Dissens dokumentiert. (2) EN „persuaded them to give Therma back to him“; UK «умовив їх повернути Пердікці Ферму» (vorher «його… віддати» = invertiert); HE stand bereits richtig („הביא בדבריו לידי השבה לו“) — Richtung vom Flag-Kreuzvergleich (πείθω-Person = Akkusativ) und Astra bestätigt.
Zusammengenommen aus Anfrage 20 und der Zweitprüfung: HE 2.28.1-Sequenz (Aorist-Partizip γενόμενος vor ἀνεπληρώθη) direkt grammatisch entschieden: „ונעשתה כסהר, ושבה ונתמלאה“ (Reihenfolge wiederhergestellt, Flag dokumentiert).

## B04 (Kap. 31–40; darin Perikles' Grabrede 2.35.1–2.46)

Token-Disposition B04: **59.156 Tokens** (4 Sitzungen: Krux 2.40.5 14,0k; drei Stichproben à ~15k) — Ziel unter 500.000 **eingehalten**.

### Anfrage 21 — 2.40.5 Schluss-Krux der Grabrede (review/astra/b2_B04_40-5-crux.txt, 2026-09-28, effort=high)
Frage (Auszug wörtlich): „(1) … does τῷ πιστῷ go with τῆς ἐλευθερίας … or stand by itself …? (2) How should ‚τῆς ἐλευθερίας τῷ πιστῷ‘ best be rendered …? (3) Is (B)’s explicative relative ‚that freedom gives‘ an addition beyond the transmitted …?“
Antwort (Auszug wörtlich): „1. τῷ πιστῷ most naturally belongs with τῆς ἐλευθερίας … 2. A cautious rendering is ‚with the confidence of freedom.‘ … (iii) is syntactically much less natural, and its ‚but‘ has no explicit Greek counterpart. 3. ‚That freedom gives‘ is explanatory expansion … an acceptable gloss …“
Umsetzung: UK («впевненість, яку дає свобода») und HE («הביטחון שבחירות») bestätigt; EN umgebaut: „not more by a reckoning of profit than by the confidence of freedom“ (vorher beide Genitive bei λογισμῷ + freistehendes „but on trust“ — verworfen); die drei Flags dokumentieren die geschlossene Entscheidung.

### Anfragen 22a–c — Stichproben B04 (review/astra/b2_B04_sample_en/uk/he.txt, 2026-09-28, effort=medium; Seed 20261005; je 6 Abschnitte, davon 3 aus der Grabrede)
EN (2.31.3, 2.32.1, 2.34.2, 2.36.3, 2.39.1, 2.39.4): 0 Befunde. UK (2.31.1, 2.38.1, 2.40.2, 2.40.3, 2.40.4, 2.40.5): 2 Befunde — 2.40.2 ὀρθῶς («слухно» → «правильно»); 2.40.3 διὰ ταῦτα μὴ ἀποτρεπόμενοι = „die klare Kenntnis schreckt sie nicht ab“ — «і саме тому не одступають» kehrte die Kausalität um. HE (2.36.1, 2.36.3, 2.38.2, 2.39.3, 2.40.3, 2.40.5): 2 Befunde — 2.40.3 dieselbe Kausalumkehr («ועל כן אינם נרתעים» → «ודברים אלה אינם מרתיעים אותם»); 2.36.3 «אנוכי» (bibl. Sg.) für αὐτοὶ ἡμεῖς οἵδε + fehlendes μάλιστα + «שיא הגבורה» für τῇ καθεστηκυίᾳ ἡλικίᾳ — korrigiert («אנחנו עצמנו, העומדים עתה כאן — עדיין ברובנו בשיא החיים»). Wegen Einheitlichkeit wurde die 2.40.3-Korrektur auch auf EN ausgedehnt („for that reason do not turn away“ → „are not by these things deterred“), obwohl EN nicht gezogen war — dokumentiert in allen drei Flags. Zweitprüfung (frische GLM-Session): 1 Befund — HE 2.33.1 Patronymikon Χρύσιδος als falscher Name «כריסידס» statt «בן כריסיס» — angenommen; EN/UK 0 Befunde; die examined cruxes (2.35.2, 2.36.1, 2.37.1, 2.39.1/2, 2.40.3/5) in allen drei Sprachen bestanden.

Zusätzlich (ohne Astra, grammatikalisch/precedent-entschieden): EN-Blocker 2.39.1 μὴ κρυφθέν-Negation („were it not hidden“) nach Prüferbefund; EN 2.36.1 οἱ αὐτοί = dieselben MÄNNER (Autochthonie), HE parallel korrigiert, UK stand richtig; Numerale 2.33.1 in allen drei Sprachen auf die überlieferte Zweizahl „fünfhundert und tausend“ zurückgestellt (Präzedenz 2.13.3); runde Parenthesen des Quelltextes (2.31.1–2) bleiben mit Klammern gedruckt und sind nun überall geflaggt (Koordinatoren-Konvention); HE 2.33.2 «אקרנניה», HE 2.34.5 ohne zusätzliches Begräbnisverb, HE 2.36.3-Flag neu, HE 2.38.1 νομίζοντες ergänzt, UK/bitweise-Flag-Korrekturen (1.115.4, 1.31.4, 1.105.3/1.108.2, 1.37.5/1.37.2, Selbstzitate).
