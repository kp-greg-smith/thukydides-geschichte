# Buch 1 (uk): Übersetzungs- und Prüfprotokoll

Grundlage ist ausschließlich der griechische Text (`docs/grc/source.xml`, Oxford-Ausgabe H. S. Jones). Jede Portion von höchstens zehn Kapiteln wurde durch einen Übersetzungs-Subagenten angefertigt, sodann durch einen zweiten, unabhängigen Subagenten abschnitts- und satzweise am Griechischen geprüft; jede Meldung wurde durch die Koordination am griechischen Text entschieden, bevor die Portion gebaut und veröffentlicht wurde. Automatische Strukturprüfung (`scripts/check_translation.py`) je Portion: 0 Fehler in allen hier verzeichneten Portionen.

## Festlegungen (bindend für die ukrainische Ausgabe)

- Modernes Standardukrainisch nach geltender Orthographie; griechische Namen nach der üblichen ukrainischen altertumswissenschaftlichen Wiedergabe (Керкіра, Потідея, Егіна).
- Anmerkungen im Lauftext als `[Прим.: …]`, nur für echte Zweifel.
- Reden über mehrere Abschnitte ohne umschließende Anführungszeichen; « » nur für kurze eingebettete Zitate. Beschluss vom 27.09.: kurze einabschnittige Direktreden (wie 1.53) behalten ihre Anführungszeichen.
- Zahlen werden ausgeschrieben. τὰ Μηδικά = мідійська війна (однина). House-Standard vom 27.09.: durchgängig «вже» statt «уже».
- Interne `!! FLAG`-Vermerke der Arbeitskopien sind Herausgebernotizen der Pipeline; sie erscheinen nicht im veröffentlichten HTML.

## Glossar (feste Entsprechung je Bedeutung; der Kontext entscheidet)

| Грецька | Значення | Українська |
|---|---|---|
| πρόφασις | названий привід дії | привід; 1.23.6 = найправдивіший привід |
| αἰτία | обвинувачення / причина / вина / відповідальність | обвинувачення / причина / вина / відповідальність |
| ἔγκλημα | офіційна скарга | скарга |
| διαφορά | предмет суперечки | розбіжність |
| στάσις | внутрішній збройний конфлікт | громадянська війна |
| δύναμις | сила, могутність | сила; військо (одиниця) |
| παρασκευή | військова підготовка | підготовка; озброєння (конкретне споряджене військо) |
| δουλεία | підданство господареві | рабство (не пом'якшувати) |
| λόγος / ἔργον | протиставлення слова і діла | слово / діло; промова, аргумент, переказ — за змістом |
| χρήματα | фінансові ресурси | кошти; гроші; конкретне майно (з 5-го пакета): майно |
| τεκμήριον | тверда підстава висновку | доказ |
| σημεῖον | знак, вказівка | ознака; військовий сигнал (з 5-го пакета): сигнал |
| μαρτύριον | свідчення | свідчення |
| λῃστεία | грабунок морем / на суші | піратство / розбій |
| τὸ μυθῶδες | казковий елемент | міфічність |
| σπονδαί | освячена угода про перемир'я | перемир'я |
| ἐκεχειρία / ἀνοκωχή | формальне припинення воєнних дій | священне перемир'я / припинення воєнних дій |
| ξύμμαχοι / ξυμμαχία | союзники / союз | союзники / союз |
| ἐπίκουρος / ἐπικουρία / βοήθεια | військова допомога | допомога |
| ἀρχή | панування | панування; не м'якше за «лідерство», коли йдеться про підданих |
| ὑπήκοος | підданий | підданий |
| αὐτονομία | автономія | автономія / автономний |
| τυραννίς / τύραννος | тиранія / тиран | тиранія / тиран |
| βάρβαροι | негрецькі народи | варвари |
| ναυτικόν | флот | флот |
| στρατηγός | афінський командувач | стратег |
| οἰκιστής | засновник колонії | засновник |
| ἱκέτης / ἱκετεία | той, хто шукає захисту | той, хто шукає захисту в святилищі / благання |
| τιμωρία | відплата метрополії скривдженій колонії | відплата (каральна сила збережена) |
| ἐπιτήδευμα | лінія поведінки | лінія поведінки |
| μαρτύριον / κρίσις / δίκη | рішення зброєю / суд | свідчення / суд (міждержавний: суд чи арбітраж) |

## Namen

1. Стам-лист (витяг обов'язкових форм): Еллада та елліни; Керкіра, Коринф, Афіни, Спарта/Лакедемон, Потідея, Егіна, Епідамн, Мегара, Фіви, Мілет, Самос, Лесбос, Хіос, Тасос, Пелопоннес, перешийок, Іонічна затока, Сібота, Левкімма, Хімерій, Феспротія, Анакторій, Підна, Ферма, Паллена; Дельфи; Сицилія, Італія, Карфаген; мідяни/Мідія, перси; пеласги, Еллін, данайці, аргівяни, ахейці, троянці, фінікійці; Мінос, Агамемнон, Менелай, Нестор, Аякс, Ахілл, Олена, Тіндарей, Мікени, Пелоп, Тантал, Еврісфен, Прокл, Темен, Фідон Аргоський, Гесіод, Гомер, Крит, Опунт, Фессалія; Кілон, Пісістрат; Навпакт.
2.–6. Ухвалені іменні доповнення (пакети 1–6) повністю в координаційній вкладці (`work/instructions_uk.md`); у тексті серед іншого: Херсонес, Арна, Кадміда, Амінокл, Кір/Камбіз/Дарій, Полікрат, Ренея, фокейці, Массалія, річка Галис, Марафон, Гіппій, Гіппарх, Гармодій, Аристогітон, Леокоріон, Панафінейська процесія, Пітана/Пітанський лох, Аркадія/аркади, тауланти, Фалій, Ератоклеїд, Герайон, Апулонія, Кефаленія, Пала, Епідавр, Ерміона, Трезен, Фліунт, Еліда/елейці, Сікіон, Амбракія, фаяки, Арістей, Пелліх, Ісархід, Ісарх, Актій, Аполлон, Левкас/левкадяни, Ефира, Елеатида, Ахерусійське озеро, річка Ахерон, річка Тіяміс, Кестрина, Закінф/закінфяни, Анакторій/анакторійці, Мікіад, Есімід, Еврібат, Ксеноклід син Евтікла, Лакедемоній син Кімона, Діотім син Стромбіха, Протей син Епікла; Главк син Ліагра, Андокід син Леогора, Фракія, Александр, Філіп, Дердас, Пердікка, халкідяни (у Фракії), боттієйці, Архестрат син Лікомеда, Мігдонія, озеро Больбе, Адімант.

## Portionen und Prüfungen

### Kap. 1–10 (Batch 01) — 37 Abschnitte
Zweitprüfung: work/uk/review/batch01.md. Meldungen: 20 in 19 Abschnitten (2 Blocker, 18 Minor).
- Blocker 1.3.4 (δι᾽ ἀσθένειαν καὶ ἀμειξίαν: gemeinsames Handeln korrekt gefasst) und 1.10.3 (ὅμως δὲ … ἐνδεεστέρα — Wertung nicht umgekehrt).
- Ausgewählte Fixes: 1.1.3, 1.2.1, 1.2.3/1.2.6, 1.3.2/1.3.3 (Δαναοί, Reihenfolge), 1.5.1 (кέρδους/τροφή), 1.6.2, 1.6.5, 1.7.1, 1.8.3, 1.10.4.
- Namen: Аркадія, фінікійці, Тіндарей/Олена, Мікени/Геракліди/Пелопіди/Персейди/Хрисипп, Філоктет — als genehmigt übernommen.
- Entscheidung: 1.6.3 wie in den anderen Sprachen (gemeinsame Pipeline-Entscheidung, „першими“).
Alle Meldungen angenommen.

### Kap. 11–20 (Batch 02) — 28 Abschnitte
Zweitprüfung: work/uk/review/batch02.md. Meldungen: 24 (0 Blocker, 24 Minor).
- Ausgewählte Fixes: 1.11.1/1.11.2 (Geometrie des Chersones- Sprechens; λῃστεία/γεωργία), 1.12.3 (60. Jahr nach Ilion), 1.13.1 (флот), 1.13.2 (триєри), 1.13.5 (Corinth am Isthmus; ἀφνειόν), 1.16.1, 1.17.1, 1.18.1/1.18.2 (Tyrannis-Passagen; διεκρίθησαν offengehalten), 1.18.3, 1.19.1 (oligarchische Klausel der Symmachie), 1.20.2, 1.20.3 (Пітанський лох).
- Namen: Амінокл, Кір/Камбіз/Дарій, Полікрат, Ренея, фокейці, Массалія, карфагеняни, річка Галис, хіосці/лесбосці — in die Listen übernommen.
Alle Meldungen angenommen.

### Kap. 21–30 (Batch 03) — 44 Abschnitte
Zweitprüfung: work/uk/review/batch03.md. Meldungen: 24 in 19 Abschnitten (2 Blocker, 22 Minor).
- Blocker 1.29.3 (Actium: verbindlicher Locativ „у Актії“, Ankerplatz vor dem Heiligtum) und 1.29.4 (Rechenexempel: achtzig Schiffe, vierzig vor Epwdamnos belagernd).
- Ausgewählte Fixes: 1.21.1, 1.23.3 (σεισμοί), 1.24.1 (βάρβαροι), 1.24.2 (Фалій син Ератоклеїда), 1.24.5, 1.25.1, 1.25.4 (Rechtschreibung «епairόμενοс/довідавшись»-Normen; κλέος perifrase), 1.26.3, 1.27.1, 1.27.2 (ethnische Formen), 1.28.1, 1.28.3 (ὠφέλія), 1.28.5, 1.29.2 (Арістей син Пелліха), 1.29.5, 1.30.4.
Entscheidungen wie pipeline-einheitlich: 1.23.6 (найправдивіший привід), τιμωρία = відплата, 1.25.4/1.26.5 Anakoluthon-Typografie.
Alle Meldungen angenommen.

### Kap. 31–40 (Batch 04) — 45 Abschnitte
Zweitprüfung: work/uk/review/batch04.md. Meldungen: 19 in 28 Abschnitten (3 Blocker, 16 Minor).
- Blocker 1.33.3: φόβῳ τῷ ὑμετέρῳ = Lakonen ziehen aus Angst VOR den Athenern in den Krieg («страх перед вами») — Richtung war invertiert.
- Blocker 1.36.2: Dativus commodi — von dort (Unteritalien/Sizilien) kommt eine Flotte ZUM NUTZEN der Peloponnesier; der geographische Zusammenhang wiederhergestellt.
- Blocker 1.37.5: ἀληπτότεροι = «недосяжніші» (ἀ-ληπτος, „unfassbar“); die Vergleichsrichtung war invertiert.
- Ausgewählte Minor-Fixes: 1.31.1 (μισθῷ πείθοντες = «наймаючи за платню»), 1.32.2/1.32.3 («прохання», «невигідною»), 1.32.5, 1.33.1/1.33.2, 1.33.3 (δυοῖν φθάσαι ἁμάρτωσιν), 1.34.3, 1.35.3 (δεινόν = «ганебно»), 1.35.5 (εἰ δύνασθε), 1.36.1 («завчасу» entfernt), 1.37.5 (δεχομένοις τὰ δίκαια crux mit Vermerk), 1.38.4 (ἐκπρεπῶς mit Vermerk), 1.38.6 (τιμωρία = «відплата»), 1.39.2 (δίκη = «показний суд»), 1.40.2 (εἰ σωφρονοῦσι als Bedingung).
- Eine Erhebung erwies sich als gegenstandslos (1.37.5 ἀρετή war bereits einheitlich «чеснота»): 18 angenommen, 1 gegenstandslos.

### Kap. 41–50 (Batch 05) — 41 Abschnitte
Zweitprüfung: work/uk/review/batch05.md. Meldungen: 7 in 7 Abschnitten (1 Blocker, 6 Minor).
- Blocker 1.44.2: ἀσθενεστέροις οὖσιν — die Schwäche gehört den Korinthern und den anderen Flottenbesitzern; die verdoppelte Partizip-Wiedergabe mit hängendem «уже послабленими» wurde korrigiert.
- Minor: 1.42.2 (ἐν ᾧ = «рішенням», nicht Person), 1.45.3 (ein ἀποβαίνειν für beide Alternativen: «висадитися на Керкірі чи на якійсь із володінь»), 1.46.4 (genehmigte Namensformen «Ефира», «річка Ахерон», «річка Тіяміс» angewandt), 1.49.2 (Zusatz «зіткнення впритул» entfernt), 1.49.5 («все» entfernt), Orthograph Vereinheitlichung «уже» → «вже» ausgabenweit (Kap. 1–50).
Offene unsichere Stellen aus dieser Portion: 1.46.2 πέμπτος αὐτός (dunkel, wörtlich belassen); 1.49.2 τῇ μὲν τέχνῃ οὐχ ὁμοίως (überlieferte Doppeldeutigkeit bewahrt); 1.50.5 Paian-Sänger wie im Griechischen unbenannt gelassen.
Alle Meldungen angenommen.

### Kap. 51–60 (Batch 06) — 31 Abschnitte
Zweitprüfung: work/uk/review/batch06.md. Meldungen: 13 in 11 Abschnitten (0 Blocker, 13 Minor).
- Namensfixes gemäß sechstem Addendum: «Главк, син Ліагра» (1.51.4), «Філіп» (1.57.3, 1.59.2 — davor «Філіппом»), «халкідяни» und «боттієйці» (1.57.5, 1.58.1, 1.58.2 — davor «халкідейці/боттійці»), «озеро Больбе» (1.58.2 — davor «Больби»).
- Ethnikon-Flexion «керкіряни» vereinheitlicht: «керкірам» → «керкірянам» (1.53.4), «керкірів» → «керкірян» (1.55.1, ×2).
- ἀποσία-/ἀφίσταμαι-Wortsippe einheitlich «відпадіння/відпали» statt «відступлення/відступили» (1.57.4, 1.57.5, 1.57.6, 1.58.1), im Einklang mit 1.56.2/1.59.1/1.60.3.
- ἀντιπλέειν feindlich: «не випливли проти них із Сібот» (1.54.2); προσποιεῖσθαι = «приписували собі перемогу» (1.54.2).
- Weitere Fixes: 1.51.5 («вже»-Zusatz getilgt; «стали на якір»), 1.52.1 (Kasus-Konstruktion), 1.52.2 («вишикувавшись», «у безлюднім місці»), 1.53.2 («здіймаючи зброю»), 1.58.1 (κατὰ τὸν καιρὸν = «у цю пору»), 1.55.1 (FLAG zu δυνάμει = «за впливом» ergänzt).
- Bestätigt: Kurzreden 1.53 in « » und so stenographisch knapp wie das Griechische; τιμωρία allgemein = «карати», metropolis-colony = «відплата»; alle Zahlen korrekt (20; 30×3; ~70/≥1000; ~30; 800+250; 1000; †10† wie überliefert; 1600+400; vierzigster Tag); «вже»-Hausstandard; «Сіботи» (Plural) einheitlich mit 1.47/1.50.
Alle 13 Meldungen angenommen (12 mit Texteingriff, 1 als Vermerksergänzung).

### Kap. 61–70 (Batch 07) — 45 Abschnitte
Zweitprüfung: work/uk/review/batch07.md. Meldungen: 29 in 24 Abschnitten (4 Blocker, 25 Minor).
- Blocker 1.63.1: διὰ τῆς θαλάσσης = «через саме море» — der Weg des Aristeus führte durchs Meer, nicht «берегом моря» über Land.
- Blocker 1.69.3: περιορᾶν = «дивитеся і нічого не втручаєтесь» — der Kontrast „wissen und nicht handeln" wiederhergestellt.
- Blocker 1.69.4: das ausgefallene καταλύοντες im zweiten Glied ergänzt («а руйнуєте, лише коли воно подвоїться»).
- Blocker 1.69.5: doppelte Inversion korrigiert — περιγεγενημένους = «брали ми гору», ἁμαρτήμασιν αὐτῶν = die Verfehlungen der Athener.
- Namens-/Glossarfixes: «Фермою» (1.61.2), «ринок» statt «торг» (1.62.1, 1.67.4), «серміляни» (1.65.2), «довгі стіни» (1.69.1), ἔκπλους = «вихід у море» (1.65.1).
- Weitere Minor-Fixes: 1.62.3 (καί koordinierend, nicht appositiv; «затиснути ворогів посеред них самих»), 1.62.6 (τρέπειν = «звернуло до втечі»), 1.65.2 (Richtung ἐς Πελοπόννησον), 1.66.1 («воїни» getilgt), 1.67.5 (Wortstellung), 1.68.1 (Genitiv τὸ πιστόν = «Надійність»), 1.68.2 (ohne Einfügung «на з'їзді»), 1.68.4 («для фракійських справ»), 1.69.1 (ἀξίωσιν φέρειν ohne «мовби»), 1.69.4 (τινά = «нікого не обороняючи»), 1.69.5 (ἐς τύχας = «покладаючись хіба що на випадок»; πολλῷ = «значно»; τινάς πού = «декого»; περιορᾶτε vereinheitlicht; Tippfehler «гіршого—»), 1.70.1 (eigenes Recht statt Konditional), 1.70.2 (ἐπιγνῶναι μηδέν = «розпізнають»; «усе, що вирішать»), 1.70.6 (ohne «владно»), 1.70.7 (ὁμοίως = «одні лише мають стільки, скільки задумують»; Doppelung «неначе втратили» getilgt), 1.70.8 (Nominativ nach «ніж»).
- Vermerks-Ergänzungen: 1.63.1 ὁποτέρωσε, 1.68.3 Kasus-Crux τοῖς ἐπιβουλεύοντας, 1.69.2 Kasus-Anomalie οὐ μέλλοντες, 1.69.4 τινά + Anakoluthon, 1.70.2, 1.70.3, 1.70.7 (τυχεῖν/πράξαντες); Revisionen: 1.61.3 (falsche Verderbnisbehauptung entfernt — der einzige Nachweis des ch_062-Zwischenfalls, Vorlage selbst intakt), 1.65.2, 1.67.4, 1.69.5 №2 (athenische Attribution).
- ch_062-Zwischenfall: keine Spuren in Übersetzung oder Quellbasis (Prüfer verglich alle 45 griechischen Abschnitte erneut mit source.xml — 100 %, «τὴν παρὰ Περδίκκου» einmal wie überliefert).
Alle 29 Meldungen angenommen (26 mit Texteingriff, 3 reine Vermerks-Fälle; zusätzlich 4 bestehende Vermerke revidiert).

### Kap. 71–80 (Batch 08) — 43 Abschnitte
Zweitprüfung: work/uk/review/batch08.md. Meldungen: 14 in 14 Abschnitten (4 Blocker, 10 Minor).
- Blocker 1.71.5: πρὸς + Gen. = «на суді / в очах» — die Einsichtigen sind Richter, nicht die Geschädigten.
- Blocker 1.74.3: ἐπὶ τῷ + Inf. = Zielkonstruktion «з прицілом утримати рештку» (nicht temporal «як дійшло до поділу решти»); der eigennützige Beweggrund der spartanischen Hilfe wiederhergestellt.
- Blocker 1.75.4: das ausgefallene überlieferte Satzgefüge «καὶ γὰρ ἂν αἱ ἀποστάσεις πρὸς ὑμᾶς ἐγίγνοντο» am Abschnittsende ergänzt («адже і відпадіння міст відбувалися б тоді у ваш бік») + Vermerk zur ἄν-mit-Imperfekt-Anomalie.
- Blocker 1.77.6: die Apodosis «ὁμοῖα καὶ νῦν γνώσεσθε» als eigene Prognose gelöst («такі самі ви і нині виявитеся» statt in den Protasis gefaltet), γνώσεσθε nicht mehr als «викажете».
- Vorab verfügte Prüfungen sauber umgesetzt: 1.71.2 (подібним до вас самих — a-fortiori-Bedingung trat NICHT ein) und 1.73.1 («промови бо — ні наші, ні цих людей — не відбувалися б у вас, як перед суддями»); Quellbasis erneut zeichenweise mit source.xml verprobt (10/10).
- Minorfixes: 1.71.3 (ohne «у всякому», ohne «помітно»), 1.73.2 («радше в тягар», grammatische Glättung), 1.73.3 (странное «борня» → «з яким же містом випаде вам боротися»), 1.74.1 (idiomatische Gruppierung «трохи менш як чотириста, тобто трохи менш як дві частини»; Lesernotiz präzisiert: «як співвідносяти обидва числа»), 1.76.4 (εἴ τι = «якщо», nicht «чи»), 1.77.3 (Doppelverneinung eindeutig), 1.78.2 («обертається»), 1.80.4 (Vergleichsbasis «ніж у кораблях»).
- Vermerks-Ergänzungen: 1.75.4 (ἄν + Imperfekt), 1.77.2 (Kasus-Anomalie bei σκοπεῖ), 1.77.3 (παρὰ τὸ μὴ οἴεσθαι χρῆναι); Vermerks-Sync: 1.77.6, 1.71.3.
- 1.74.1-Lesernotiz: vom Prüfer bestätigt — kurz, faktisch (beide Zahlen stehen überliefert nebeneinander; die antike Kontroverse über die Flottenzahlen ist bezeugt) und nötig; Wortlaut präzisiert.
- Glossar-Vorschläge geprüft und unterstützt: ξυνθήκη = «умова», ἐπιείκεια = «поблажливість», ἐπιτήδεύματα = «повадки», παράλογος, μοῖρα offen; der εἰκότως-Kontrast 1.76.4/1.77.5 bleibt als dokumentierte Zweilesarigkeit bewusst stehen.
Alle 14 Meldungen angenommen (12 mit Texteingriff, 2 reine Vermerks-Fälle; dazu 1 Notiz-Präzisierung, 3 Vermerks-Ergänzungen, 2 Vermerks-Syncs).

### Kap. 81–90 (Batch 09) — 42 Abschnitte
Zweitprüfung: work/uk/review/batch09.md. Meldungen: 21 in 21 Abschnitten (2 Blocker, 19 Minor).
- Blocker 1.81.3: die Hilfs-Inversion korrigiert — δεήσει [ἡμῖν] τούτοις ναυσὶ βοηθεῖν = «доведеться нам і цим союзникам допомагати кораблями» (nicht „diesen Verbündeten müsste man zu Hilfe kommen“) — Archidamos’ Insel-Argument wiederhergestellt; das ausgefallene καί ergänzt.
- Blocker 1.90.5: θαυμάζειν zurück unter ἔφη («і що він, мовляв, дивується») — keine freie Erzählung mehr; das ausgefallene μέντοι («втім») ergänzt.
- Sonderprüfungen: 1.87-Stimmenzahl bestanden (πολλῷ πλείους wie überliefert, keine Betrügerei-Glosse, nichts ausgelassen); 1.83.3 echtes Verderbnis bestätigt (Objekt «про них» statt «про неї» korrigiert); 1.82.2 ἴμεν ohne Vermerk — Vermerk mit beiden Lesarten ergänzt; 1.86.2 die οἱ-Offenheit war STILL zugunsten der ALLIIERTEN aufgelöst — Wahl jetzt dokumentiert (Athener als Alternative); 1.84.3 ἀμαθέστερον geglättet zu «занадто просто» — korrigiert zu «з недолею навчання» und das Vermerks-Resümee korrigiert (es hatte die Glättung als „общепринятый смысл“ ausgegeben); τὸ κοινόν 1.90.5 = «громадські справи».
- Minorfixes (Auswahl): 1.81.4 (без «самі»), 1.81.5 (δόξομεν = Eindruck der anderen + Vermerk zur καταλύεσθαι-Doppellesung), 1.81.6 (Antezedens «війну» + καί = «аж»: «лишити війну аж нашим дітям»), 1.82.1 («ставитися до них» statt normwidrigem «стояти до них»; Vermerk zur zweiten Öffnungslasche der Archidamus-Rede im Quelltext), 1.82.2 (πεφραγμένοι = «укріплені»; ἢν δοκῇ = «якщо розсудимо за добре»), 1.82.3 (Präsens-Partizip + potentialer Optativ «поступилися б»), 1.82.4 (ἀληπτοτέρους = «недосяжнішими», nicht «некерованішими»), 1.84.2 («не піддаємося потісі»), 1.84.3 («доброрадні» statt unkodifiziertem «добрерадні»), 1.85.2 («а проти того, хто його дає»; βουλεύσεσθε = «порадите»), 1.86.2 («а вони ж таки»), 1.87.4 (σφίσι ergänzt: «кривдять їх самих»), 1.90.1 (τε…καί = «і… і», nicht Alternativen; «чисельності» statt «численности»), 1.90.3 (Kasus + Konstruktion), 1.90.5-κοινόν.
- Vermerks-Ergänzungen: 1.81.5, 1.82.1 (Quell-Anomalie der Rede-Grenzen), 1.82.2, 1.86.2, 1.87.5 (Anakoluth ohne Hauptverb), 1.89.3 (Zahl-Diskordanz bei τὸ κοινόν); Vermerks-Revisionen: 1.83.3, 1.84.3.
- Übersetzervorschläge verifiziert: τὰ Εὐβοϊκά = «після здобуття Евбеї» nach dem identischen 1.23.1-Vorbild (bestätigt); ὑπεκτίθημι = «вивезено в безпеку» (mit «звідти» statt «звідусіль»); «спільна справа» 1.90.5 verworfen («громадські справи»), «загал афінян» 1.89.3 bestätigt; ἐξαρτύειν/ἐκπορίζειν-Unterscheidung bestätigt.
- Hinweis: 1.86.3 «з усієї сили» stand bereits normgerecht im Text (die Reviewer-Quote «з усією сили» traf nicht zu) — keine Änderung; als erledigt vermerkt.
Alle 21 Meldungen angenommen (20 mit Texteingriff; 6 Vermerks-Ergänzungen, 2 Vermerks-Revisionen, 1 als bereits korrekt).

### Kap. 91–100 (Batch 10) — 39 Abschnitte
Zweitprüfung: work/uk/review/batch10.md. Meldungen: 10 in 10 Abschnitten (1 Blocker, 9 Minor).
- Blocker 1.92.1: die Richtung der Zuneigung wiederhergestellt — προσφιεῖς ὄντες gehört anakoluthisch zu den AFENIENSU (deren Medien-Eifer erklärt die Zurückhaltung der Lakedaimonier); der Druck hatte Adressat und Basis verkehrt („die Lakedaimonier seien den Athenern die liebsten wegen ihres spartanischen Eifers“); jetzt: „афіняни… були їм наймиліші“ — parallel zur bereits korrekten HE-Fassung; Anakoluthon per Vermerk dokumentiert.
- Spiegel 1.100.2→3 wiederhergestellt: die erfundene Vollpunkt-Tilgung wie im HE-Fall — Abschnitt endet auf Komma, Fortsetzung mit Konnektor; dokumentierender Vermerk ergänzt (Vergleich: das exakte Spiegel 1.93.3→4).
- Vermerk-Fehler behoben: 1.96.2 behauptete eine Leseranmerkung, die seit der Elft-Addendum-Regelung nicht mehr existiert (der Übersetzer hatte sie noch getragen; ich selbst hatte sie vor der Prüfung entfernt, dankte aber irreführenderweise in einem Vermerk, der den alten Zustand beschrieb) — jetzt dokumentierend neu gefasst; 1.93.2 abgeschwächt („окремі видавці“ statt „звичайно“ — unser quellenloses Jones-Druck kann stärkere Apparat-Behauptungen nicht tragen); 1.94.2 um die nachträglich verfügte Elft-Addendum-Referenz ergänzt.
- Weitere Fixes: 1.91.2 (μᾶλλον…ἢ wiederhergestellt statt „так“; zugesetztes „ВСЕ“ getilgt), 1.91.4 (πρεσβεύεσθαι = „посилати послів“, nicht „доручати посольствами“), 1.93.3-Cluster („звідти“ getilgt; „прегарне“ → „гарне“; „з'їзди союзників“ → „з'їзди“), 1.98.4 („спіткало те саме“ → elliptisches „спіткало“ — ξυνέβη bleibt, die Erfindung geht), 1.99.1 („точно й невідступно“ → „точно“; „чимало й інших“ → „бувало й інших“), 1.99.2 (Litotes bereinigt: „не складно“ → positives „легко“), 1.93.4 (δύναμις auf den Glossar-Slot „сила“ ausgerichtet — „надбання могутності“ → „надбання сили“; das mitten-im-Satz-Spiegel bleibt intakt), 1.95.6 („начальником“ → „воєначальником“, der Spartaner-Slot), 1.100.1 („полонили трієри“ → „захопили“ — Schiffe nimmt man nicht gefangen), 1.100.2 (ἀντιπέρας geglättet: „у Фракії, що лежить навпроти“).
- Sonderprüfungen sauber: die Neun-Wege-Apposition ohne Klammern und Notiz auf dem Druck (der EN-Blocker kehrte NICHT wieder); «Насамперед» öffnet 1.98.1; keine Strafklausel in 1.99.1 (in source.xml verifiziert); die Themistocles-Adresse endet exakt am überlieferten ἔφη; Ἕλληνες-Linie durchgehend; alle Zahlen exakt (два вози — carts, nicht chariots; до половини висоти; 460 Talente; двісті; десять тисяч).
- Übersetzervorschläge verifiziert: διαχείρισις = „каральне придушення“ unterstützt; ἐνεῖδον = „дізнулися“ unterstützt; ἀνθεκτέα = „слід покладатися на море“ funktional unterstützt; ἀντιπέρας sinngemäß unterstützt (Form geglättet).
Alle 10 Meldungen angenommen (alle mit Text- oder Vermerkseingriff).

### Kap. 101–110 (Batch 11) — 42 Abschnitte
Zweitprüfung: work/uk/review/batch11.md. Meldungen: 6 in 6 Abschnitten (2 Blocker, 4 Minor).
- Blocker 1.105.1: das ausgefallene Satzgefüge wiederhergestellt — der Seekampf bei Cecryphalia mit den peloponnesischen Schiffen und der athenische Sieg fehlten im Druck komplett; jetzt «а пізніше афіняни дали морський бій біля Кекрифалі… — і перемогли афіняни»; der zugehörige Vermerk war dreifach falsch (behauptete den Druck des fehlenden Namens; verlegte die Stelle ins „nächste Kapitel“; zitierte eine nicht überlieferte Form Κεκρυφαλέα — 0 Vorkommen) — komplett neu gefasst; zusätzlich der verlangte Галії-Dokumentationsvermerk ergänzt.
- Blocker 1.107.6: die stille Auflösung der Dreier-Ellipse («афіняни не знають, як пробратися») wider den Erzählgang (die Passagefrage ist lakedaimonisch: 1.107.4/1.107.3/1.108.2) ersetzt durch wiederhergestellte Offenheit — «вирішивши, що виходу пройти далі нема, рушили на них походом» — parallel zum committeten EN, das keine Partei nennt; der Vermerk dokumentiert alle drei Lesungen mit Begründung.
- Zeitpolitik entschieden: alle historischen Präsentien normalisiert (πέμπει ×2 → «надіслав»; γίγνεται → «відбулася»; ἀφικνοῦνται → «прибули») — EN-kongruent, in-Batch-Einheitlichkeit hergestellt; die «цар»-Ergänzung bleibt korrekt.
- Minorfixes: 1.102.3-Cluster («з цього ж походу» statt «спільної»; «знову» getilgt; «тоді» getilgt), 1.110.4 (πλέουσαι… ἔσχον → «приплили»), 1.106.1-Vermerkszitat an den Druck angeglichen («в обійстя»), 1.107.3-Zitat um καὶ ταύτῃ vervollständigt, die Konjektur-Behauptung von 1.106.2 abschwächend umformuliert («висловлювалися правлення»), das νεωτεροποιία-Lemma korrigiert.
- Vermerks-Ergänzungen nach Addendum 12 und EN-Parität: die κέρας-Metapher (1.110.4), αἱ δ' ἐλάσσους, πολλαὶ ἰδέαι πολέμων (1.109.1), ἀνεσταυρώθη mit beiden Alternativen («розп'ятий» / «посаджено на кіл»), der Ἕλληνες-Vermerk gelöst-dokumentierend.
- Verifiziert sauber: τειχομαχεῖν byte-bestätigt (Tau; die πειχομαχεῖν-Panne kehrte NICHT wieder); «Біла стіна» nahtlos (unsere Quelle druckt ohnehin ohne Klammern — die Klammer-Prämisse meines Prompts wurde zurückgenommen); Zahlenaudit komplett (siebzig, dreihundert, 1500+10000, 62. Tag, zwölf Tage, hundert Geiseln, Jahr und sechs Monate, sechs Jahre, FÜNFZIG Trieren); der Sprungspiegel bei 1.108.2→3 intakt; sämtliche Addendum-Namen auf dem Druck.
- Methodennotiz: der Prüfer verifizierte vier koordinatoreigene Vorgaben gegen die Paralleltexte und bestätigte die τειχομαχεῖν-Prüfung — keine einzige falsche Variantenbehauptung in diesem Batch.
Alle 6 Meldungen angenommen (jeweils Text- oder Vermerkseingriff).

## Offene und unsichere Stellen (Stand 27.09.2026)

- 1.6.3 — wie pipeline-einheitlich («першими»).
- 1.7.1 ἀνῳκισμένοι — Lesartentscheidung mit Dokumentation.
- 1.9.4/1.10.4 — wie EN (gemeinsame Entscheidungen, sinngemäß mit Anmerkung).
- 1.18.1 — gestörte Überlieferung, sinngemäß mit Anmerkung.
- 1.25.4→1.26.1, 1.26.5→1.27.1 — Anakoluthon-Typografie wie in der deutschen Referenz.
- 1.31.3 τὸ αὐτῶν — auf die athenische Flotte bezogen, Alternative dokumentiert.
- 1.32.2 μετὰ τῆς ξυμμαχίας τῆς αἰτήσεως — crux, gewählte Satzteilung dokumentiert.
- 1.36.3 τῷδ᾿ ἂν μὴ προέσθαι — auf «не відпускати нас» festgelegt, Alternativen dokumentiert.
- 1.37.3 ἀνάγκῃ καταίροντας δέχεσθαι — ungrammatisch; nach evidentem Sinn.
- 1.37.5 δεχομένοις τὰ δίκαια δεικνύναι — zwei mögliche Bezüge; adverbiale Lesart gewählt, crux dokumentiert.
- 1.38.4 ἐκπρεπῶς μὴ καὶ διαφερόντως — spätere Lesart als Vermerk dokumentiert, Text belassen.
- 1.46.2 πέμπτος αὐτός — dunkel, wörtlich belassen.
- 1.49.2 τῇ μὲν τέχνῃ οὐχ ὁμοίως — Doppeldeutigkeit bewahrt.

## Zahlen (Stand 27.09.2026)

- Übersetzte Abschnitte: 437 in den Kapiteln 1–110 (Ukrainian); insgesamt Buch 1 hat 146 Kapitel / 580 Abschnitte.
- Durch Zweitprüfung geprüft: sämtliche 437 veröffentlichten Abschnitte (jede Portion durch einen unabhängigen Subagenten, jede Meldung durch die Koordination am griechischen Text entschieden; automatische Strukturprüfung je Portion ohne Fehler).
- Vom Prüfer beanstandet: kumuliert 187 Fundstellen (21 Blocker, 166 Minor).
- Geändert: sämtliche angenommenen Fundstellen im Textkorpus umgesetzt; abgelehnte Meldungen: keine dokumentiert; gegenstandslose Erhebungen: 1.
- Offen bzw. unsicher: die oben verzeichneten Stellen (Zeileneinträge mit „offen“/crux); keine davon blockiert die Veröffentlichung, alle Entscheidungen sind im Text oder in der Anmerkung sichtbar.
- Nicht veröffentlicht, obwohl work in progress: Kapitel 111–120: Übersetzung im Gang; Kapitel 121–146 noch nicht begonnen.
- Keine Behauptung von Fehlerfreiheit: geprüft heißt nicht fehlerfrei; künftige Portionen und Nachprüfungen können weitere Befunde bringen.
