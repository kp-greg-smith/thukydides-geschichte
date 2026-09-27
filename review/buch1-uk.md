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

## Offene und unsichere Stellen (Stand 27.09.2026)

- 1.6.3 — wie pipeline-einheitlich («першими»).
- 1.7.1 ἀνῳκισμένοι — Lesartentscheidung mit Dokumentation.
- 1.9.4/1.10.4 — wie EN (gemeinsame Entscheidungen, sinngemäß mit Anmerkung).
- 1.18.1 — gestörte Überlieferung, sinngemäß mit Anmerkung.
- 1.25.4→1.26.1, 1.26.5→1.27.1 — Anakoluthon-Typografie wie in der deutschen Referenz.

## Zahlen (Stand 27.09.2026)

- Übersetzte Abschnitte: 109 in den Kapiteln 1–30 (Ukrainian); insgesamt Buch 1 hat 146 Kapitel / 580 Abschnitte.
- Durch Zweitprüfung geprüft: sämtliche 109 veröffentlichten Abschnitte (jede Portion durch einen unabhängigen Subagenten, jede Meldung durch die Koordination am griechischen Text entschieden; automatische Strukturprüfung je Portion ohne Fehler).
- Vom Prüfer beanstandet: kumuliert 68 Fundstellen (4 Blocker, 64 Minor).
- Geändert: sämtliche angenommenen Fundstellen im Textkorpus umgesetzt; abgelehnte Meldungen: keine dokumentiert; gegenstandslose Erhebungen: 1.
- Offen bzw. unsicher: die oben verzeichneten Stellen (Zeileneinträge mit „offen“/crux); keine davon blockiert die Veröffentlichung, alle Entscheidungen sind im Text oder in der Anmerkung sichtbar.
- Nicht veröffentlicht, obwohl work in progress: Kapitel 51–60: Übersetzung abgeschlossen, Zweitprüfung ausstehend; Kapitel 61–146 noch nicht begonnen.
- Keine Behauptung von Fehlerfreiheit: geprüft heißt nicht fehlerfrei; künftige Portionen und Nachprüfungen können weitere Befunde bringen.
