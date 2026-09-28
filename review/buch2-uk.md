# Buch 2 (uk): Übersetzungs- und Prüfprotokoll

Grundlage ist ausschließlich der griechische Text (`docs/grc/source.xml` / `docs/grc/book2.html`, Oxford-Ausgabe H. S. Jones; Extrakt `work/grc/b2/ch_NNN.txt`). Jede Portion von höchstens zehn Kapiteln (B01 = 1–10 … B11 = 101–103) wird durch einen Übersetzungs-Subagenten angefertigt, sodann durch einen zweiten, unabhängigen Subagenten abschnitts- und satzweise am Griechischen geprüft; zusätzlich prüft nach jeder Portion eine neue GLM-Session ohne Zugang zu `work/` und `review/` (nur griechisches HTML plus die drei Übersetzungs-HTML) nach demselben Prüfauftrag. Jede Meldung wird durch die Koordination am griechischen Text entschieden; Eskalationen an Astra (codex, `gpt-6-astra`, read-only) nach dem Astra-Protokoll, wörtlich protokolliert in `review/buch2-astra-log.md`. Automatische Strukturprüfung (`scripts/check_translation.py --language uk --book 2`) je Portion.

Festlegungen, Glossar und Namensformen aus Buch 1 (`review/buch1-uk.md`, `work/instructions_uk.md`) bleiben verbindlich. Kennung in Buch 2: `2.Kapitel.Abschnitt`. Buch-2-Addenda (Glossar, Namen, Festlegungen) werden unten je Portion verzeichnet und am Ende in die READMEs nachgetragen.

## Festlegungen (Buch 2, bindend für die ukrainische Ausgabe)

- Britische Rechtschreibung mit Oxford-„-ize“; latinisierte Namensformen; Anmerkungen als `[Note: …]`; Reden über mehrere Abschnitte ohne umschließende Anführungszeichen, kurze eingebettete Zitate mit „ “; Zahlen ausgeschrieben; `!! FLAG` nur intern. (Wie Buch 1.)
- Kapitel 35–46 (Grabrede des Perikles), 60–64 (letzte Rede), 71–74 (Plataier/Archidamos), 87, 89 (Kriegsrat/Phormion) gelten als Reden im Sinne der Stichprobenregel (6 statt 4 Stichproben je Sprache und Portion).
- Kein Rückgriff auf `docs/de/` (existiert für Buch 2 nicht) und keine moderne Übersetzung als Vorlage.

## Buch-2-Addenda

**П'ятнадцяте доповнення, розділи 1–10 (B01, ухвалені форми):** імена: Хрисіда (жриця в Аргосі); Енесій (ефор); Піфодор (архонт); Піфангел; Філід; Діемпор; Онеторід; Навклід; Евримах; Леонтід; річка Асоп; Пеллена, пелленці; Мілос; Фера. Етнікони: левкадяни, анакторійці (від ухвалених Левкас, Анакторіон). Глосарій: βοιωτάρχος = беотарх; νεωτερείν ἐς τινά = «чини ворожі дії» (2.3.1), μηδὲν νεώτερον ποιεῖν = «не роби нічого необачного» (2.6.2; ухвала Astra B01 — диференціація за контекстом, як вимагає правило 1); ὀλίγον ἐπενόουν οὐδέν = «не замислювали нічого малого» (LSJ ἐπινοέω I.2; Astra B01); τὰ δύο μέρη = дві третини (LSJ з посил. на 2.10.2; паралель 2.47.2); χρησμολόγοι = тлумачі оракулів; λόγια = пророцтва; περίορθρον = найглухіша пора ночі (hapax у Фукідіда); ὑποσπόνδιος = під захистом перемир'я; ἀκηρυκτεί = без герольдів. Ухвали: 2.8.4 ἐν τούτῳ … ᾧ корелятивне, перфект проспективний (Astra B01); 2.5.5 δράσειαν — передана конструкція без виправлення, без примітки (Astra B01); 2.5.6 εὐθύς належить поверненню, не обіцянці (Astra B01; УК вже було правильно). κῆρυξ = герольд (як у Книзі 1).

## Portionen und Prüfungen

### Розділи 1–10 (порція B01) — 45 абзаців
Переклад: субагент, 45/45 (1, 4, 4, 8, 7, 4, 3, 5, 6, 3); структуру машинно звірено з source.xml (усі ідентифікатори наявні, у порядку джерела). Перевірка: незалежний субагент, звіт `work/uk/b2/review/batch01.md` — 12 повідомлень (1 блокер, 11 мінор). Рішення координації:
- 2.2.4 додане «і хто радив» + пряма мова герольда без лапок → ПРИЙНЯТО: непряма мова за грецьким; «...не слухалися тих, хто їх упровадив, — щоб негайно взятися до діла й іти на будинки ворогів».
- 2.3.1 ξύμβασις «погодилися на перемови» → ПРИЙНЯТО: «пішли на згоду» (консистентно з 2.2.4).
- 2.3.4 кома в цитаті прапорця → ПРИЙНЯТО (тільки прапорець; зміст рішення звірений і правдивий).
- 2.4.3/2.4.4 «засів» → «засув» → ПРИЙНЯТО (мовна виправа; «засів» = сівба).
- 2.6.4 «найменш дієздатних» → «найдаремніших» → ПРИЙНЯТО (ἀχρειοτάτους без пом'якшення).
- 2.7.3 καταπολεμήσοντες → спершу ПРИЙНЯТО як «підкорюватимуть війною весь Пелопоннес навкруги»; рішення ПЕРЕВІРЯЄТЬСЯ Astra (контрзапит, див. журнал Astra) — остаточний стан див. нижче в цьому файлі та в журналі Astra.
- 2.8.1 БЛОКЕР «не вважали нічого за надто мале» → ПРИЙНЯТО: «не замислювали нічого малого, а рвалися до війни — і недаремно».
- 2.8.2 «залюбки» → вилучено, ПРИЙНЯТО.
- 2.5.7 термінологія прапорця (πράσσω πρός τινα, LSJ III.6) → ПРИЙНЯТО (тільки прапорець; переклад підтверджено).
- 2.9.4 хибний прапорець (джерело має родовий Ἀκαρνάνων) → ПРИЙНЯТО, прапорець виправлено.
- 2.10.2 посилання прапорця (2.47.2 замість 3.15.1) → ПРИЙНЯТО, прапорець виправлено.
- 2.8.4 ретроспективний перфект → ВІДХИЛЕНО (Astra B01, запит 1.4: проспективне читання стандартне; тіло лишене проспективним).
Astra B01: запит 1 (cruxes): 2.6.2 «нічого необачного» (ПРИЙНЯТО); 2.3.1 — тіло вже правильне («нічого ворожого»); 2.8.4 корелятивна переробка «спиниться та справа, у якій він сам не братиме участі» (ПРИЙНЯТО); 2.5.5, 2.10.2 підтверджено. Запит-стіхроза (Seed 20260928: 2.4.2, 2.5.3, 2.7.3, 2.9.2): 2.4.2 «якими можна було врятуватися» (ПРИЙНЯТО); 2.5.3 правильно; 2.7.3 ἐξήταζον «перевіряли стан свого наявного союзу» (ПРИЙНЯТО); 2.9.2 «ці ж були в приязні з обома сторонами» (ПРИЙНЯТО); два дискусійні пункти (καταπολεμήσοντες, ἐντὸς Ἰσθμοῦ) — контрзапит Astra, рішення в журналі Astra; виконано відповідно.
Відхилені повідомлення: 1 (2.8.4 ретроспективний перфект) — з обґрунтуванням через Astra.
Друга перевірка (нова GLM-сесія без доступу до `work/` і `review/`, лише `docs/grc/book2.html` плюс три HTML перекладів): висновок сесії — en 0/uk 1/he 0. УК-звернення: 2.3.4 «τὸ περίορθρον» передано «саму глуху її пору» («мертва година ночі»), тоді як ΕΝ і НЕ читають останню годину перед світанком; контрзапит Astra (див. журнал Astra, Anfrage 8) вирішив на користь світанкового читання (LSJ, s.v. περίορθρον, цитує саме Th. 2.3); виправлено на «над саму пору перед світанком» — єдина корекція цієї сесії, застосована. Усі числа, імена, списки, непряма мова і заперечення звірені сесією і підтверджені. Підсумок УК-Б01: 45 абзаців перекладено; 12 повідомлень перевіряча (1 блокер, 11 мінор), з них 11 прийнято, 1 відхилено (2.8.4, з обґрунтуванням Astra); корекцій від Astra в УК: 7 (2.6.2, 2.8.4, 2.2.4, 2.4.2, 2.7.3a, 2.9.2b, 2.3.4-після-контрзапиту); відхилено також 1 повідомлення з Astra-стіхрози (2.9.2a ἐντὸς Ἰσθμοῦ — з роз'ясненням Astra Anfrage 7, залишено традиційну форму).

## Offene und unsichere Stellen

(wird je Portion nachgetragen)

## Zahlen

(wird am Ende vervollständigt: übersetzte Abschnitte, beanstandete, geänderte, abgelehnte Meldungen, Astra-Anfragen mit Korrekturen, offene unsichere Stellen)
