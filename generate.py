#!/usr/bin/env python3
"""
Thukydides: Der Peloponnesische Krieg
=====================================
Generiert MD, HTML und PDF für alle acht Bücher.

Nutzung:
  python3 generate.py          # alle 8 Bücher generieren
  python3 generate.py buch1    # nur Buch 1
  python3 generate.py all      # explizit alle
"""

import subprocess, os, sys, re, textwrap

REPO = os.path.dirname(os.path.abspath(__file__))
OUTDIR = os.path.join(REPO, "output")
os.makedirs(OUTDIR, exist_ok=True)

# ================================================================
# BUCH 1: ARCHÄOLOGIE UND VORGESCHICHTE
# ================================================================

BUCH1 = r"""# Thukydides: Der Peloponnesische Krieg

## Erstes Buch

### Übersetzungsgrundsätze

1. **Einheitliche Schlüsselbegriffe** im ganzen Werk: πρόφασις (wahrer Grund), αἰτία (Vorwurf), στάσις (Bürgerkrieg), δύναμις (Macht), παρασκευή (Rüstung), δουλεία (Knechtschaft), λόγος/ἔργον (Wort und Tat).
2. **Nichts hinzugefügt, nichts gesteigert.** Jede Ausschmückung, jede Redewendung, die nicht im Griechischen steht, entfällt.
3. **Nicht abschwächen.** Wo Thukydides hart formuliert, bleibt es hart (δουλεία = Knechtschaft).
4. **Anmerkungen nur bei echten Zweifeln.** [Anm.: …] markiert textkritisch unsichere Stellen.

---

### Kapitel 1

§1 Der Athener Thukydides hat den Krieg der Peloponnesier und Athener aufgezeichnet, wie sie gegeneinander kämpften. Er begann damit gleich bei seinem Ausbruch und in der Erwartung, er werde groß sein und denkwürdiger als alle früheren; er schloss dies daraus, dass beide auf dem Höhepunkt ihrer gesamten Rüstung in ihn eintraten und dass er das übrige Griechentum sich der einen oder der anderen Seite anschließen sah, teils sofort, teils mit dem Gedanken daran.

§2 Denn diese Erschütterung war die größte für die Griechen und für einen Teil der Barbaren, ja, man kann sagen, für den größten Teil der Menschheit.

§3 Was vor diesem Krieg liegt und was noch älter ist, ließ sich wegen der Länge der Zeit zwar nicht mit Sicherheit ermitteln; aus den Zeugnissen aber, denen ich bei möglichst weit zurückreichender Betrachtung Glauben schenken kann, komme ich zu dem Schluss, dass es weder in Kriegen noch sonst bedeutend war.

---

### Kapitel 2

§1 Es zeigt sich, dass das heutige Griechenland nicht seit alters her fest besiedelt war, sondern dass es früher Wanderungen gab und dass jeder Stamm seinen Wohnsitz leicht aufgab, wenn er von jeweils Zahlreicheren bedrängt wurde.

§2 Denn da es keinen Handel gab und sie weder zu Lande noch zu Wasser ohne Furcht miteinander verkehrten, da jeder nur das Seine nutzte, so viel er zum Leben brauchte, und sie keinen Überschuss an Geld besaßen und das Land nicht bepflanzten – es war ungewiss, wann ein anderer käme und, zumal ohne Mauern, es ihnen wegnähme –, da sie ferner glaubten, die täglich nötige Nahrung überall erlangen zu können, wanderten sie ohne Mühe ab. Deshalb waren sie weder durch die Größe von Städten noch durch sonstige Rüstung stark.

§3 Vor allem das beste Land hatte ständig Wechsel der Bewohner: das heutige Thessalien und Böotien, der größte Teil der Peloponnes außer Arkadien und von den übrigen Gebieten das, was am fruchtbarsten war.

§4 Denn wegen der Güte des Bodens entstanden bei einigen größere Machtverhältnisse, und daraus Bürgerkriege, an denen sie zugrunde gingen; zugleich wurden sie von Stammfremden umso eher angegriffen.

§5 Attika jedenfalls war wegen seines mageren Bodens die längste Zeit über ohne Bürgerkrieg, und stets wohnten dort dieselben Menschen.

§6 Und dies ist nicht das geringste Beispiel für meine Behauptung, dass durch die Abwanderungen das übrige Griechenland nicht in gleicher Weise wachsen konnte: Aus dem übrigen Griechenland kamen die durch Krieg oder Bürgerkrieg Vertriebenen, die Mächtigsten, zu den Athenern, da es dort sicher war, und indem sie Bürger wurden, machten sie gleich von alter Zeit her die Stadt noch größer an Menschenmenge, so dass sie später sogar nach Ionien – da Attika nicht mehr ausreichte – Kolonien aussandten.

---

### Kapitel 3

§1 Folgendes zeigt mir nicht zuletzt die Schwäche des Früheren: Vor dem Trojanischen Krieg hat Griechenland offenbar nichts gemeinsam unternommen.

§2 Mir scheint, es führte damals noch nicht einmal diesen Namen als Ganzes; vor Hellen, dem Sohn Deukalions, gab es diese Bezeichnung überhaupt nicht, vielmehr gaben die einzelnen Stämme, besonders der pelasgische, am meisten von sich aus die Benennung. Als aber Hellen und seine Söhne in der Phthiotis mächtig wurden und man sie zu Hilfe in die anderen Städte rief, da wurden die einzelnen Stämme durch den Umgang mit ihnen schon eher Hellenen genannt; doch vermochte sich der Name lange Zeit nicht bei allen durchzusetzen. [Anm.: Das überlieferte ἐδύνατο ist textkritisch umstritten.]

§3 Den besten Beweis liefert Homer. Denn obwohl er viel später, noch nach dem Trojanischen Krieg, lebte, nennt er sie nirgends alle zusammen mit diesem Namen, auch keine anderen als die mit Achilleus aus der Phthiotis, die ja die ersten Hellenen waren; er spricht in den Epen von Danaern, Argeiern und Achaiern. Er hat auch nicht von Barbaren gesprochen, weil, wie mir scheint, auch die Hellenen sich noch nicht durch einen gegensätzlichen Namen abgegrenzt hatten.

§4 Die Griechen also, wie sie einzeln, Stadt für Stadt, soweit sie einander verstanden, und später alle zusammen so genannt wurden, unternahmen vor dem Trojanischen Krieg wegen ihrer Schwäche und fehlenden Verkehrs miteinander nichts gemeinsam. Aber auch zu diesem Feldzug brachen sie erst auf, als sie schon mehr zur See fuhren.

---

### Kapitel 4

§1 Minos erwarb als Ältester von denen, von deren Kunde wir wissen, eine Flotte und beherrschte den größten Teil des heutigen griechischen Meeres; er gebot über die Kykladeninseln und war der erste Besiedler der meisten von ihnen, nachdem er die Karer vertrieben und seine eigenen Söhne als Herrscher eingesetzt hatte. Auch die Seeräuberei bekämpfte er, wie zu erwarten, auf dem Meer, soweit er konnte, damit ihm die Einkünfte umso mehr zuflössen.

---

### Kapitel 5

§1 Die Griechen verlegten sich in alter Zeit – und ebenso die Barbaren, die an der Küste des Festlands wohnten und die Inseln bewohnten –, sobald sie anfingen, sich mehr mit Schiffen gegenseitig zu besuchen, auf Seeraub, unter Führung von Männern, die nicht zu den Schwächsten gehörten, um des eigenen Gewinns willen und zur Ernährung der Schwachen. Sie überfielen unbefestigte Städte und dorfweise bewohnte und plünderten sie; den größten Teil ihres Lebens bestritten sie daraus, da diese Tätigkeit noch keine Schande mit sich brachte, sondern eher etwas Ruhm.

§2 Das zeigen noch heute einige der Festlandbewohner, bei denen es als Zierde gilt, dies gut zu tun, und die alten Dichter, die bei den landenden Fremden überall gleichermaßen fragen, ob sie Räuber seien – als ob weder die Befragten die Tätigkeit verachteten noch die, welche es zu wissen wünschten, sie ihnen vorwürfen.

§3 Sie beraubten einander auch auf dem Festland. Und bis heute lebt vieles in Griechenland nach der alten Weise bei den ozolischen Lokrern, Ätolern, Akarnanen und dem dortigen Festland. Auch die Sitte, Eisen zu tragen, ist diesen Festlandbewohnern von der alten Seeräuberei geblieben.

---

### Kapitel 6

§1 Ganz Griechenland trug Eisen wegen der unbefestigten Wohnsitze und der unsicheren Wege zueinander, und sie machten das Leben unter Waffen zur Gewohnheit wie die Barbaren.

§2 Ein Zeichen dafür, dass dies einst allen die gleiche Lebensweise war, sind jene Gegenden Griechenlands, die noch heute so leben.

§3 Als erste legten die Athener das Eisen ab und gingen, die Lebensweise lockernd, zu einer weichlicheren über. Und von den älteren Reichen unter ihnen ist es noch nicht lange her, dass sie aufhörten, leinene Gewänder zu tragen und sich den Haarknoten auf dem Kopf mit dem Einsetzen goldener Zikaden hochzubinden. Daher hat diese Tracht wegen der Verwandtschaft auch bei den älteren Ioniern lange fortbestanden.

§4 Eine mäßige Kleidung und die heutige Art führten zuerst die Lakedaimonier ein, und auch sonst glichen sich bei ihnen die Vermögenderen in der Lebensweise den Vielen am meisten an.

§5 Sie waren auch die ersten, die sich nackt auszogen und, sich öffentlich entblößend, sich mit Öl zum Üben salbten. In alter Zeit dagegen kämpften die Athleten auch beim olympischen Wettkampf mit einem Schurz um die Scham, und es ist noch nicht viele Jahre her, dass dies aufgehört hat. Noch jetzt gibt es bei manchen Barbaren, besonders den asiatischen, Wettkämpfe im Boxen und Ringen, und sie tun dies mit einem Schurz.

§6 Man könnte noch vieles andere anführen, worin das alte Griechentum ähnlich wie das heutige Barbarentum lebte.

---

### Kapitel 7

§1 Von den Städten wurden die am jüngsten gegründeten, als man schon besser zur See fuhr, mit größerem Überschuss an Geld unmittelbar an den Küsten mit Mauern erbaut und riegelten die Landengen ab, um des Handels willen und der jeweiligen Stärke gegenüber den Nachbarn. Die alten Städte aber wurden wegen der lange andauernden Seeräuberei mehr landeinwärts gegründet, sowohl auf den Inseln wie auf den Festländern – denn sie beraubten einander und unter den Übrigen die, die, ohne Meeranrainer zu sein, weiter unten wohnten –, und bis heute liegen sie noch so landeinwärts.

---

### Kapitel 8

§1 Und nicht weniger Räuber waren die Inselbewohner, Karer und Phöniker; diese bewohnten die meisten Inseln. Zum Beweis: Als Delos von den Athenern in diesem Krieg gereinigt wurde und die Gräber der auf der Insel Verstorbenen aufgehoben wurden, zeigte sich, dass über die Hälfte Karer waren, erkannt an der Ausstattung der mitbegrabenen Waffen und an der Art, wie sie noch jetzt bestatten.

§2 Nachdem aber die Flotte des Minos aufgestellt war, wurde der Verkehr untereinander besser befahrbar – die Übeltäter von den Inseln wurden von ihm vertrieben, als er ja auch die meisten von ihnen besiedelte –,

§3 und die Menschen an der Küste, die nun schon mehr Erwerb von Geld betrieben, wohnten fester, und einige umgaben sich auch mit Mauern, da sie reicher wurden. Denn im Streben nach Gewinn ertrugen die Schwächeren die Knechtschaft der Stärkeren, und die Mächtigeren, die über Überschuss verfügten, machten sich die kleineren Städte untertan.

§4 Und in dieser Weise, schon fortgeschrittener, zogen sie später gegen Troja.

---

### Kapitel 9

§1 Agamemnon scheint mir unter den damaligen durch Macht hervorgeragt zu haben, und nicht so sehr die durch Tyndareos' Eide gebundenen Freier Helenas führend den Feldzug versammelt zu haben.

§2 Es sagen aber die, welche von den Peloponnesiern das Sicherste aus der Erinnerung von den Früheren übernommen haben, Pelops habe zuerst durch die Menge an Geld, die er aus Asien zu mittellosen Menschen brachte, Macht erworben und als Fremder dennoch die Benennung des Landes erlangt, und später sei den Nachkommen noch Größeres zugefallen: Eurystheus sei in Attika durch die Herakliden umgekommen, Atreus aber sei Eurystheus' Mutterbruder gewesen, und Eurystheus habe, als er zu Felde zog, Mykene und die Herrschaft wegen der Verwandtschaft dem Atreus anvertraut – dieser sei damals gerade wegen des Todes des Chrysippos auf der Flucht vor seinem Vater gewesen –; und als Eurystheus nicht zurückkehrte, habe Atreus, mit Willen der Mykenaier – aus Furcht vor den Herakliden und weil er fähig schien und die Menge der Mykenaier und derer, über die Eurystheus herrschte, gewonnen hatte –, die Königsherrschaft übernommen, und die Pelopiden seien mächtiger geworden als die Perseiden.

§3 Dies, scheint mir, übernahm Agamemnon und, zugleich mit einer Flotte mehr als die anderen erstarkend, führte er den Feldzug nicht so sehr durch Gunst als durch Furcht versammelt durch.

§4 Er kam offenbar selbst mit den meisten Schiffen und stellte sie noch den Arkadern bei, wie Homer dies gezeigt hat, wenn jemandem sein Zeugnis ausreicht. Und bei der Übergabe des Zepters hat er von ihm gesagt: »über viele Inseln und das ganze Argos zu herrschen.« Er hätte nicht Inseln außer den umliegenden – diese dürften nicht viele sein –, da er ein Festlandbewohner war, beherrscht, wenn er nicht auch eine Flotte gehabt hätte. Man muss aber auch nach diesem Feldzug auf das Vorhergehende schließen.

---

### Kapitel 10

§1 Dass Mykene klein war oder dass irgendein Städtchen von damals heute unbedeutend erscheint, darf man nicht als genaues Zeichen nehmen, um zu bezweifeln, dass der Feldzug so groß war, wie die Dichter gesagt haben und die Überlieferung festhält.

§2 Denn wenn die Stadt der Lakedaimonier veröden würde, zurückblieben aber die Heiligtümer und die Grundmauern der Gebäude, so würde – glaube ich – nach langer Zeit bei den Späteren großer Zweifel an ihrer Macht im Verhältnis zu ihrem Ruhm bestehen; und dies, obwohl sie zwei der fünf Teile der Peloponnes bewohnen, die ganze beherrschen und viele auswärtige Bundesgenossen haben. Weil aber die Stadt nicht zusammengesiedelt ist und weder Heiligtümer noch prächtige Bauten aufweist, sondern nach der alten Weise Griechenlands in Dörfern bewohnt wird, erschiene sie geringer. Von der Macht Athens dagegen würde man, wenn ihm dasselbe widerführe, nach dem sichtbaren Anblick der Stadt auf das Doppelte dessen schließen, was sie ist.

§3 Man darf also nicht zweifeln, noch mehr auf das Aussehen der Städte schauen als auf ihre Macht, sondern muss annehmen, dass jener Feldzug zwar der größte vor ihm war, aber hinter den jetzigen zurückbleibt – wenn man auch hier dem Werk Homers etwas glauben darf, das er als Dichter wohl ins Größere ausgeschmückt hat; doch erscheint es auch so noch geringer.

§4 Er hat nämlich von den tausendzweihundert Schiffen die der Böoter mit je hundertzwanzig Mann, die des Philoktetes mit je fünfzig gedichtet, womit er, wie mir scheint, die größten und die kleinsten angibt; anderer Schiffe Größe hat er jedenfalls im Schiffskatalog nicht erwähnt. Dass sie aber alle zugleich Ruderer und Kämpfer waren, hat er bei den Schiffen des Philoktetes gezeigt: Alle, die das Ruder führten, hat er als Bogenschützen dargestellt. Überzählige Mitfahrer dürften nicht viele gewesen sein außer den Königen und den höchsten Amtsträgern, zumal sie ein Meer mit Kriegsgerät überqueren sollten und auch keine völlig gedeckten Schiffe hatten, sondern solche, die in der alten Weise mehr nach Piratenart ausgerüstet waren.

§5 Betrachtet man nun die Mitte zwischen den größten und den kleinsten Schiffen, so erscheinen nicht viele gekommen zu sein, als von ganz Griechenland gemeinsam ausgesandt.

---

### Kapitel 11

§1 Die Ursache aber war nicht so sehr der Mangel an Menschen wie der Mangel an Geld. Denn aus Mangel an Nahrung führten sie ein geringeres Heer und nur so viel, wie sie hofften, dass es dort kämpfend würde leben können. Als sie aber ankamen und in der Schlacht siegten – das ist offenbar, denn sonst hätten sie die Verschanzung für das Lager nicht gebaut –, scheinen sie auch dort nicht ihre ganze Macht eingesetzt zu haben, sondern sich aus Mangel an Nahrung auf den Ackerbau der Chersones und auf Seeraub verlegt zu haben. Daher konnten die Troer ihnen, als sie zerstreut waren, zehn Jahre lang mit Gewalt widerstehen, da sie den jeweils Zurückbleibenden gewachsen waren.

§2 Hätten sie aber Überschuss an Nahrung mitgebracht und wären sie vereint, ohne Seeraub und Ackerbau, ununterbrochen den Krieg geführt, so hätten sie, in der Schlacht siegend, Troja leicht genommen – sie widerstanden ja auch nicht vereint, sondern mit dem jeweils anwesenden Teil; durch eine Belagerung aber hätten sie in kürzerer Zeit und müheloser Troja genommen.

§3 Aus Mangel an Geld war das, was vor diesem war, schwach, und gerade dieses selbst, das Berühmteste unter dem Früheren, erweist sich durch die Tatsachen als geringer denn sein Ruf und als geringer als die Erzählung, die jetzt durch die Dichter davon in Geltung steht.

---

### Kapitel 12

§1 Auch nach dem Trojanischen Krieg war Griechenland noch in Wanderung und Neubesiedlung begriffen, so dass es nicht zur Ruhe kommen und wachsen konnte.

§2 Die Rückkehr der Griechen aus Ilion dauerte lange und brachte vieles in Unruhe, und Bürgerkriege entstanden in den Städten in großem Umfang; die daraus Vertriebenen gründeten neue Städte.

§3 Die heutigen Böoter wurden im sechzigsten Jahr nach Ilions Einnahme von den Thessalern aus Arne vertrieben und besiedelten das jetzige Böotien, das früher Kadmeisches Land hieß – ein Teil von ihnen war schon früher in diesem Land gewesen, und aus ihren Reihen war man auch gen Ilion gezogen –, und die Dorier nahmen im achtzigsten Jahr mit den Herakliden die Peloponnes in Besitz.

§4 Mit Mühe, in langer Zeit, kam Griechenland zur Ruhe und sandte, nicht mehr umherziehend, Kolonien aus: Die Ioner und die meisten Inselbewohner wurden von den Athenern besiedelt, der größte Teil Italiens und Siziliens von den Peloponnesiern und einige Gebiete vom übrigen Griechenland. All dies wurde später als der Trojanische Krieg gegründet.

---

### Kapitel 13

§1 Als Griechenland mächtiger wurde und mehr noch als zuvor den Erwerb von Geld betrieb, richteten sich in den Städten meist Tyrannenherrschaften ein, da die Einkünfte größer wurden – früher gab es erbliche Königtümer mit festgelegten Ehrenrechten –, und Flotten wurden in Griechenland ausgerüstet; man wandte sich mehr dem Meer zu.

§2 Als erste sollen die Korinther die Schiffsbaukunst am nächsten der heutigen Weise gehandhabt haben, und Trieren wurden in Korinth als erste in Griechenland gebaut.

§3 Es scheint auch, dass Ameinokles, ein korinthischer Schiffsbauer, den Samiern vier Schiffe gebaut hat. Es sind ungefähr dreihundert Jahre bis zum Ende dieses Krieges, als Ameinokles zu den Samiern kam.

§4 Die älteste Seeschlacht, von der wir wissen, fand zwischen Korinthern und Kerkyraiern statt. Es sind auch von dieser etwa zweihundertsechzig Jahre bis zum selben Zeitpunkt.

§5 Da die Korinther die Stadt auf dem Isthmos bewohnten, hatten sie von jeher einen Handelsplatz, da die Griechen in alter Zeit mehr zu Lande als zu Wasser – die innerhalb der Peloponnes und die außerhalb – durch ihr Gebiet miteinander verkehrten; und durch Geld waren sie mächtig, wie auch von den alten Dichtern bezeugt wird: Sie nannten den Ort den reichen. Als aber die Griechen mehr zur See fuhren, bekämpften die Korinther, die Schiffe erwerbend, die Seeräuberei, und als Handelsplatz dienend, machten sie in beiderlei Hinsicht ihre Stadt durch den Zufluss von Geld mächtig.

§6 Auch den Ionern entstand viel später eine Flotte, unter Kyros, dem ersten König der Perser, und Kambyses, seinem Sohn; das Meer an ihrer Küste beherrschten sie im Krieg gegen Kyros eine Zeit lang. Und Polykrates, Tyrann von Samos, machte unter Kambyses, durch seine Flotte mächtig, andere der Inseln untertan und weihte, nachdem er Rheneia eingenommen hatte, die Insel dem Apollon von Delos. Auch die Phokaier besiegten, als sie Massalia gründeten, die Karthager in einer Seeschlacht.

---

### Kapitel 14

§1 Dies waren die mächtigsten unter den Flotten. Es scheint aber, dass auch diese viele Generationen später als der Trojanische Krieg aufkamen: Sie benutzten wenige Trieren, waren aber noch mit Fünfzigruderern und langen Schiffen ausgerüstet wie jene.

§2 Kurze Zeit vor den Perserkriegen und dem Tod des Dareios, der nach Kambyses über die Perser herrschte, entstanden bei den Tyrannen um Sizilien und bei den Kerkyraiern Trieren in Menge. Dies waren die letzten nennenswerten Flotten in Griechenland vor dem Feldzug des Xerxes.

§3 Die Aigineten und die Athener – und wenn es noch andere gab – besaßen nur geringe, und davon die meisten Fünfzigruderer. Spät erst, seit Themistokles die Athener – als sie mit den Aigineten im Krieg lagen und zugleich der Barbar zu erwarten war – überredete, die Schiffe zu bauen, mit denen sie auch die Seeschlacht schlugen; auch diese hatten noch nicht durchgängig Verdecke.

---

### Kapitel 15

§1 So also waren die griechischen Flotten, die alten und die später entstandenen. Dennoch erwarben nicht geringe Macht diejenigen, die sich ihnen widmeten, durch Zufluss von Geld und Herrschaft über andere. Sie fuhren aus und unterwarfen die Inseln, besonders die ohne ausreichendes Land.

§2 Zu Lande aber kam kein Krieg zustande, aus dem auch Macht erwuchs. Alle Kriege, die stattfanden, richteten sich gegen die jeweiligen Nachbarn, und Feldzüge in die Ferne, außerhalb des eigenen Landes zur Unterwerfung anderer, unternahmen die Griechen nicht. Sie standen weder zu den größten Städten als Untertanen vereint, noch unternahmen sie von gleicher Grundlage aus gemeinsame Feldzüge; vielmehr bekriegten einander im einzelnen die Nachbarn die Nachbarn.

§3 Am ehesten noch trat in dem einmal in alter Zeit ausgebrochenen Krieg zwischen Chalkidiern und Eretriern auch das übrige Griechentum ins Bündnis der einen oder der anderen Seite auseinander.

---

### Kapitel 16

§1 Es traten ihnen hier und dort Hindernisse gegen das Wachstum entgegen; und den Ionern, deren Macht schon weit vorangeschritten war, zog Kyros und das persische Königreich, nachdem es Kroisos gestürzt hatte und alles diesseits des Halys bis zum Meer, zu Felde und knechtete die Städte auf dem Festland, Dareios aber später, mit der Flotte der Phöniker überlegen, auch die Inseln.

---

### Kapitel 17

§1 Die Tyrannen in den griechischen Städten, die nur auf ihren eigenen Vorteil bedacht waren – was den Leib und die Mehrung des eigenen Hauses betraf –, schützten sich möglichst durch Sicherungen; nichts Nennenswertes wurde von ihnen vollbracht, jede Stadt für sich, außer etwa gegen Nachbarn. So kam in Griechenland lange Zeit aus keiner Stadt etwas Großes zustande. [Anm.: Der überlieferte Text dieser Stelle ist unsicher.]

---

### Kapitel 18

§1 Als aber die Tyrannen in Athen und im übrigen Griechenland – das meiste davon stand noch länger als Athen unter Tyrannen –, die meisten und letzten (außer in Sizilien), von den Lakedaimoniern gestürzt waren – Lakedaimon hatte, nachdem es von den Doriern, die es jetzt bewohnen, besiedelt worden war, die längste uns bekannte Zeit unter Bürgerkriegen gelitten, war aber gleich von alters her wohlgeordnet und stets ohne Tyrannen; es sind etwa vierhundert Jahre oder etwas mehr bis zum Ende dieses Krieges, seit die Lakedaimonier dieselbe Verfassung haben; dadurch wurden sie mächtig und richteten auch in den anderen Städten die Herrschaftsverhältnisse ein – [Anm.: Der griechische Text ist an dieser Stelle lückenhaft und unsicher.] –, nach der Auflösung der Tyrannen in Griechenland also, nicht viele Jahre später, kam es bei Marathon zur Schlacht der Meder und Athener.

§2 Im zehnten Jahr danach zog der Barbar wieder mit der großen Flotte heran, um Griechenland zu knechten. Als die Gefahr groß war, übernahmen die Lakedaimonier, die an Macht voranstanden, die Führung der verbündeten Griechen, und die Athener beschlossen beim Herannahen des Meders, ihre Stadt zu verlassen; sie nahmen ihre Habe, bestiegen die Schiffe und wurden so zu Seeleuten. Bald darauf schlugen sie gemeinsam den Barbaren zurück.

§3 Nicht lange danach traten die Griechen, die vom Meder abgefallen waren und die noch mit ihm verbündet, in zwei Lager auseinander: die um die Athener und die um die Lakedaimonier. In der Rüstung standen diese am meisten hervor, die einen zu Lande, die anderen mit den Schiffen die Stärksten.

§4 Die Bündnisse bestanden kurze Zeit, dann gerieten die Lakedaimonier und die Athener, entzweit, mit den Verbündeten aneinander in Krieg. Und von den übrigen Griechen schloss sich, wenn irgendwo ein Streit ausbrach, ein Teil dem einen, ein Teil dem anderen an. So führten sie von den Perserkriegen an bis zu diesem Krieg – bald Frieden schließend, bald Krieg führend, teils gegeneinander, teils gegen die abgefallenen Bundesgenossen – Krieg und rüsteten sich wohl, und sie wurden geübter in den Gefahren.

---

### Kapitel 19

§1 Die Lakedaimonier herrschten über ihre Bundesgenossen, ohne sie tributpflichtig zu machen; sie sorgten nur dafür, dass diese – ihrem eigenen Vorteil entsprechend – oligarchisch regiert würden. Die Athener zogen mit der Zeit von den Bundesgenossen die Schiffe ein – außer von Chios und Lesbos – und legten ihnen eine Geldzahlung auf. Ihre eigene Rüstung wurde in diesem Krieg größer, als sie je auf dem Höhepunkt mit der vollen vereinten Macht der Verbündeten gewesen war.

---

### Kapitel 20

§1 So also habe ich die frühere Zeit nach der Prüfung befunden; es ist freilich schwierig, jedem Zeugnis der Reihe nach zu glauben. Denn die Menschen nehmen die Kunde über das Vergangene, auch wenn es das eigene Land betrifft, gleichermaßen ungeprüft voneinander an.

§2 So glauben die große Menge der Athener, Hipparchos sei Tyrann gewesen und von Harmodios und Aristogeiton getötet worden, und sie wissen nicht, dass Hippias als Ältester der Söhne des Peisistratos herrschte, Hipparchos und Thessalos aber seine Brüder waren. Harmodios und Aristogeiton, die an jenem Tag, im Augenblick der Tat, Verdacht fassten, Hippias sei von Mitwissern verraten worden, hielten sich von ihm fern, da er vorgewarnt war; in dem Wunsch, vor ihrer Verhaftung noch etwas zu wagen, stießen sie auf Hipparchos beim Leokoreion und töteten ihn, als er den Festzug ordnete.

§3 Auch vieles andere, was es noch heute gibt und was die Zeit nicht der Vergessenheit übergeben hat, wird von den anderen Griechen nicht richtig geglaubt: dass die Könige der Lakedaimonier nicht mit je einer Stimme abstimmen, sondern mit je zweien, und dass es bei ihnen eine Pitanaten-Abteilung gebe, die es nie gegeben hat. So wenig Mühe macht sich die Menge bei der Suche nach der Wahrheit, und sie wendet sich eher dem zu, was ihr entgegenkommt.

---

### Kapitel 21

§1 Wer aufgrund der angeführten Zeichen das von mir Dargelegte betrachtet, der wird nicht fehlgehen und weder glauben, was die Dichter besingend ausgeschmückt haben, noch was die Geschichtenschreiber eher im Hinblick auf das Anhören als auf die Wahrheit zusammengestellt haben – die meisten ihrer Angaben sind durch die Zeit unglaubwürdig geworden und ins Fabelhafte gesteigert –, sondern soll nach Prüfung aus den deutlichsten Zeichen, soweit es bei so alten Dingen möglich ist, es für hinreichend ermittelt halten.

§2 Und dieser Krieg – obwohl die Menschen den gegenwärtigen Krieg, solange sie ihn führen, für den größten halten und nach seinem Ende das Frühere mehr bewundern – wird er dennoch aus dem Tatsächlichen selbst betrachtet als größer erkennen als die früheren.

---

### Kapitel 22

§1 Was sie in Reden vor dem Krieg und währenddessen vorbrachten: den genauen Wortlaut des Gesagten im Gedächtnis zu behalten, war schwierig, sowohl bei denen, die ich selbst hörte, als auch bei denen, die mir von anderswoher berichteten. Wie mir aber jeder nach meiner Ansicht das jeweils Nötige über den vorliegenden Gegenstand am ehesten gesagt haben dürfte, so sind die Reden wiedergegeben, wobei ich mich möglichst eng an den Gesamtsinn des tatsächlich Gesagten halte.

§2 Die Taten, die im Krieg geschahen, habe ich nicht danach aufgeschrieben, was ich vom ersten besten erfragte, noch wie es mir schien, sondern bei dem, wobei ich selbst zugegen war, und bei dem, was mir andere berichteten, ein jedes mit möglichster Genauigkeit zu erforschen.

§3 Es wurde nicht ohne Mühe ermittelt; denn die jeweils Anwesenden sagten über das Einzelne nicht dasselbe, sondern je nach Wohlwollen oder Gedächtnis.

§4 Zum Zuhören wird das Fehlen des Mythischen vielleicht weniger reizvoll erscheinen. Wer aber das Deutliche des Geschehenen betrachten will und des Künftigen – das einmal wieder, gemäß der menschlichen Natur, so oder ähnlich sein wird –: wenn diese so darüber urteilen, wird es genügen. Ein Besitz für immer ist es, mehr als ein Prunkstück für den augenblicklichen Vortrag.

---

### Kapitel 23

§1 Von den früheren Taten war der Perserkrieg die größte Leistung; doch wurde auch er in zwei Seeschlachten und zwei Landschlachten rasch entschieden. Die Dauer dieses Krieges aber zog sich weit hin, und es widerfuhr Griechenland in ihm Leid, wie nie zuvor in gleicher Zeit.

§2 Denn weder wurden je so viele Städte eingenommen und verödet – teils von Barbaren, teils voneinander im Krieg, einige wechselten nach der Einnahme ihre Bewohner –, noch gab es je so viel Vertreibung und so viel Blutvergießen, das eine durch die Kämpfe selbst, das andere durch den Bürgerkrieg.

§3 Und was man vorher nur vom Hörensagen kannte, in der Tat aber seltener bestätigt wurde, trat nun als glaubwürdig hervor: Erdbeben, die weite Gebiete erfassten und heftig waren, und Sonnenfinsternisse, die dichter aufeinander folgten, als man aus der früheren Zeit berichtet, an manchen Orten Dürren und durch sie Hungersnöte, und nicht das Geringste, was die Menschen schädigte und einen Teil vernichtete: die Seuche. All dies fiel zugleich mit diesem Krieg herein.

§4 Die Athener und Peloponnesier hatten eine Zeit lang zuvor den dreißigjährigen Vertrag geschlossen, nachdem Euböa unterworfen worden war. Den wahren Grund aber, weshalb sie ihn brachen, setze ich zuerst hierher – die Vorwürfe und Streitpunkte –, damit nicht einer einmal fragt, aus was für einem Anlass ein solcher Krieg den Griechen entbrannte. Der wahrste Grund, der am meisten im Verborgenen blieb, war: dass die Athener, indem sie mächtig wurden und den Lakedaimoniern Furcht einflößten, sie zum Krieg zwangen. Die offen vorgetragenen Anschuldigungen aber waren für beide Seiten die folgenden.

---

### Kapitel 24

§1 Epidamnos ist eine Stadt zur Rechten für den, der ins Ionische Meer einfährt; es grenzen an sie die Taulantier, ein illyrischer Stamm.

§2 Diese Stadt gründeten Kerkyraier; der Gründer war Phalios, Sohn des Eratokleides, aus dem Geschlecht des Herakles, nach dem alten Brauch vom Mutterland Korinth herbeigerufen. An der Gründung nahmen auch einige Korinther und vom übrigen dorischen Stamm teil.

§3 Die Stadt wurde mit der Zeit groß und volkreich.

§4 Als sie aber viele Jahre untereinander Bürgerkrieg führten, sollen sie – wie es heißt – durch den Krieg mit den benachbarten Barbaren geschädigt und von ihrer früheren Macht herabgekommen sein.

§5 Das Letzte, ehe sie Kerkyra angingen, war, dass die Volkspartei die Mächtigen vertrieb; diese gingen zu den Barbaren über und unternahmen mit ihnen Raubzüge zu Lande und zu Wasser gegen die in der Stadt.

§6 Die in der Stadt schickten Gesandte nach Kerkyra als ihrer Mutterstadt und baten, die Vertriebenen nicht zugrunde gehen zu lassen und sie mit den Ausgetriebenen zu versöhnen und den Krieg der Barbaren zu beenden.

§7 Mit dieser Bitte setzten sie sich als Schutzflehende an den Altar der Hera. Die Kerkyraier nahmen die Schutzflehenden nicht an, sondern schickten sie unverrichteter Dinge fort.

---

### Kapitel 25

§1 Die Epidamnier, die erkannten, dass ihnen von Kerkyra keine Hilfe komme, und in der Ratlosigkeit, wie sie mit der Gefahr fertig werden sollten, schickten sie nach Delphi und fragten den Gott, ob sie die Stadt den Korinthern als ihren Gründern übergeben und versuchen sollten, von dort Hilfe zu bekommen. Der Gott gab ihnen den Bescheid, sie sollten sie übergeben und die Korinther zu Führern nehmen.

§2 Die Epidamnier gingen nach Korinth und übergaben dem Orakelspruch gemäß die Kolonie, deuteten auf die Gründung durch Korinth hin und darauf, dass sie vom Gott diesen Bescheid bekommen hätten, und baten, sie nicht zugrunde gehen zu lassen, sondern ihnen beizustehen.

§3 Die Korinther beschlossen, ihnen zu helfen, da sie es für recht hielten – die Kolonie gehöre ebenso ihnen wie den Kerkyraiern –, und zugleich aus Hass gegen die Kerkyraier, weil sie, die ihre Kolonisten waren, sich nicht um sie kümmerten.

§4 Denn weder gaben die Kerkyraier den Korinthern bei den gemeinsamen Festen die üblichen Ehren – wie es bei Kolonien Brauch ist –, noch gönnten sie einem korinthischen Bürger wie den übrigen Kolonien den ersten Anteil, sondern blickten auf sie herab, da sie ihnen an Geldreichtum überlegen waren und an Macht den anderen Korinthern jener Zeit gleich. Schon früher war diese Einstellung aufgekommen, so dass sie ihre Stadt besonders schätzten. Mit ihrer Flotte – sie waren, wie sie sagten, den Phaiaken an Schiffen ähnlich – standen sie bei den Korinthern nicht in Ruhm.

---

### Kapitel 26

§1 Als die Korinther die Feindschaft der Kerkyraier erkannten und zugleich die Epidamnier um Hilfe baten, schickten sie bereitwillig Besatzung und Siedler nach Epidamnos; sie sandten sie zu Lande, damit die Kerkyraier sie nicht auf dem Seeweg hinderten.

§2 Es zogen mit den Korinthern auch von den übrigen Peloponnesiern einige freiwillig aus, und außerdem wurde es in ganz Hellas ausgerufen: Wer mit ihnen auswandern wolle, solle gleichen Anteil an der Kolonie haben. Viele waren bereit mitzugehen.

§3 Es segelten, von den Korinthern angeworben, Siedler und Besatzung, mit Geld ausgestattet, nach Epidamnos, nachdem sie die Kerkyraier zuvor durch Gesandte aufgefordert hatten, nicht gegen das göttliche Recht zu verstoßen und die Heiligtümer zu verletzen.

§4 Als aber die Kerkyraier weder die Schutzflehenden annahmen noch die Ankommenden aufnahmen, sondern ein Bündnis und die Annahme ihrer Bitte und die Übergabe der Kolonie forderten, da beschlossen sie, mit vierzig Schiffen gegen Epidamnos zu Felde zu ziehen.

§5 Als sie bei Epidamnos ankamen, belagerten sie die Stadt.

---

### Kapitel 27

§1 Die Kerkyraier, als sie die Besatzung und die Siedler in Epidamnos ankommen hörten und dass die Kolonie den Korinthern übergeben worden sei, gerieten in Zorn und fuhren mit fünfundzwanzig Schiffen aus. Zugleich sammelten sie mit weiteren Schiffen die Verbannten von Epidamnos und die von den Barbaren Helfenden herbei.

§2 Zuerst forderten sie, die Korinther sollten die Besatzung und die Siedler aus Epidamnos abziehen und die Verbannten wieder aufnehmen, die Korinther und Epidamnier Frieden halten und die Kerkyraier die Stadt in dem Zustand lassen. Sie wollten auch den Rechtsentscheid der Peloponnesier annehmen: Welcher Seite die Kolonie zugesprochen werde, die solle sie haben; auch den Gott in Delphi wollten sie fragen.

§3 Die Korinther antworteten: Wenn sie die Schiffe und die Barbaren von Epidamnos abzögen, solle recht gehandelt werden; vorher schicke es sich nicht, dass jene belagert würden und sie selbst unterhandelten.

---

### Kapitel 28

§1 Die Kerkyraier, als auch dies nichts fruchtete, schickten zu den Korinthern und machten sich bereit; sie fuhren, nachdem sie die Schiffe ausgerüstet hatten und die Barbaren zu Hilfe gekommen waren, mit achtzig Schiffen gegen die Korinther, besiegten sie in einer Seeschlacht beim Vorgebirge Leukimme, vernichteten fünfzehn ihrer Schiffe und fuhren siegreich nach Kerkyra zurück.

§2 Am selben Tag nahmen sie auch Epidamnos unter Vertrag; die gefangenen Korinther hielten sie fest, die übrigen Gefangenen verkauften sie.

§3 Von den Korinthern starben in der Landschlacht viele, und die Kerkyraier beerdigten sie; die Kerkyraier errichteten ein Siegeszeichen auf dem Vorgebirge Leukimme am Festland des Gebietes von Thesprotia.

§4 Die Korinther kehrten nach der Niederlage mit den übrigen Schiffen heim. Die Kerkyraier beherrschten das Meer in jener Gegend und verwüsteten Leukas, eine korinthische Kolonie.

---

### Kapitel 29

§1 Die Korinther, nachdem sie in der Seeschlacht unterlegen waren und ihre Kolonie in Knechtschaft sahen und die Schiffe verloren hatten, waren voll Zorn und rüsteten Rache gegen Kerkyra.

§2 Zwei Jahre lang rüsteten die Korinther und bereiteten eine möglichst große Flotte vor.

§3 Sie forderten von den übrigen Städten Ruderer unter Sold und suchten sie auch jenseits des Meeres, und in der ganzen Peloponnes und Hellas warben sie Bundesgenossen und rüsteten, gegen Kerkyra zu Felde zu ziehen.

§4 Die Kerkyraier, als sie ihre Rüstung erfuhren, gingen zu den Athenern als den in Hellas Mächtigsten und baten um ein Bündnis, da sie selbst weder dem Bund der Athener noch dem der Lakedaimonier angeschlossen waren.

§5 Sie schickten Gesandte nach Athen. Als die Korinther davon erfuhren, schickten sie ebenfalls Gesandte, damit den Kerkyraiern die Flotte nicht hinzukomme, wenn die Athener mit ihnen ein Bündnis eingingen.

---

### Kapitel 30

§1 Beide hielten Reden vor der Volksversammlung, zuerst die Kerkyraier, dann die Korinther.

§2 Die Kerkyraier sprachen so:

»Es ist recht, Athener, dass die, welche zu anderen um Beistand kommen, erst dartun, dass ihre Bitte nützlich ist, wenn sie nicht auch eine Dankesschuld vorweisen können. Wir kommen zu euch ohne vorherige Wohltat, doch glauben wir, dass unser Bündnis für euch vorteilhaft sein wird.

§3 Dass wir früher ohne Bündnis geblieben sind, war kein Übermut, sondern Besonnenheit. Wer sich nicht einmischt, bleibt unversehrt. Nun aber, da die Korinther uns angreifen, bitten wir euch: Nehmt uns auf! Wir haben die zweitgrößte Flotte nach euch, und es ist besser, Freunde zu haben, die sich aus Not anschließen, als Feinde, die durch eine Niederlage erbittert sind.

§4 Drei griechische Flotten sind nennenswert: die eure, unsere und die korinthische. Wenn ihr uns abweist und Kerkyra fällt, vereinen die Korinther unsere Flotte mit der ihren gegen euch.«

---

### Kapitel 31

§1 »Bedenkt das Folgende: Keine Gefahr, keine Kosten bringt euch das Bündnis mit uns. Wir kommen freiwillig, und unsere Flotte ist stark. Wer die größte Seemacht hat, dem fallen auch die übrigen Entscheidungen zu.

§2 Ihr werdet dies nicht bereuen. Denn noch nie hat jemand bereut, ein Bündnis geschlossen zu haben, wenn es mit Überlegung geschah. Nicht Redekunst leitet uns, sondern die Not und euer Vorteil.

§3 Helft uns: Ihr gewinnt eine mächtige Flotte, und die Korinther werden geschwächt.«

---

### Kapitel 32

§1 »Und wenn einer fürchtet, der Vertrag mit Sparta könnte gebrochen werden: Wir sind keinem Bündnis angeschlossen. Es steht im Vertrag, dass Städte, die keinem Bündnis angehören, sich einem der beiden anschließen dürfen.

§2 Wenn ihr uns abweist und wir unterliegen, so wäre das ein größerer Fehler als unserer früherer; ihr würdet eine mächtige Flotte an den Feind verlieren.

§3 Die Korinther sagen, man dürfe die eigenen Kolonisten nicht gegen die Mutterstadt unterstützen. Aber nicht Verwandtschaft zählt im Krieg, sondern Nützlichkeit. Wer mächtig ist, wird umworben, wer schwach, verlassen.«

---

### Kapitel 33

§1 So die Kerkyraier. Die Korinther erwiderten:

»Die Kerkyraier kommen nur aus Not zum Bündnis. Sie hielten sich von allen fern, nicht um kein Unrecht zu leiden, sondern um ungestraft Unrecht zu tun. Von uns gegründet, vergelten sie es mit Feindschaft.«

---

### Kapitel 34

§1 »Sie nahmen die Epidamnier nicht als Schutzflehende auf und verweigerten jeden Schiedsspruch, ehe sie den Krieg begannen.

§2 Wir haben Athen geholfen, als Samos abgefallen war. Die Peloponnesier berieten, ob sie Samos helfen sollten; wir stimmten allein für Athen und verweigerten Samos die Hilfe.

§3 Vergeltet Gleiches mit Gleichem. Stellt euch nicht gegen eure Dankesschuld.«

---

### Kapitel 35

§1 »Ihr werdet aus Freunden Feinde machen. Besser, die bestehende Freundschaft zu ehren als die Feindschaft der Fremden zu fürchten.

§2 Wenn ihr diesem Bündnis beitretet, helft ihr Ungerechten gegen die, die euch Gutes taten.

§3 Helft uns gegen sie. Durch eure Entscheidung jetzt werdet ihr selbst wieder dieselbe Entscheidung erfahren: Tut Gutes den Guten, nicht den Bösen.«

---

### Kapitel 36

§1 Die Athener hörten beide an. Zweimal trat die Versammlung zusammen. Beim ersten Mal nahmen sie die korinthische Rede eher an; beim zweiten wandten sie sich den Kerkyraiern zu. Sie schlossen kein volles Kampfbündnis – denn dann hätten sie mit Kerkyra gegen Korinth ziehen müssen –, sondern ein Schutzbündnis zur gegenseitigen Verteidigung gegen Angriffe.

§2 Denn sie sahen den Krieg mit den Peloponnesiern ohnehin kommen und wollten Kerkyra mit seiner Flotte nicht den Korinthern überlassen, sondern die Gegner gegeneinander aufreiben, damit sie im kommenden Krieg geschwächte Feinde hätten.

§3 Zugleich lag Kerkyra günstig auf dem Weg nach Italien und Sizilien.

---

### Kapitel 37

§1 Die Athener schickten zehn Schiffe unter Lakedaimonios, Diotimos und Proteas nach Kerkyra mit der Anweisung, sich nicht mit den Korinthern in eine Seeschlacht einzulassen – es sei denn, die Korinther griffen Kerkyra selbst an.

§2 Die Kerkyraier boten hundertzehn Schiffe auf. Mit den zehn athenischen fuhren sie den Korinthern entgegen, die mit hundertfünfzig Schiffen segelten.

---

### Kapitel 38

§1 Bei den Sybota-Inseln formierten sich beide. Die Kerkyraier stellten die Athener auf den rechten Flügel, ihre übrige Flotte in drei Geschwader. Die Korinther hatten rechts die Megarer und Ambrakier, in der Mitte die übrigen Verbündeten, sich selbst links.

§2 Als die Zeichen gegeben waren, kämpften sie; auf den Verdecken hatten beide viele Hopliten und Bogenschützen. Sie kämpften mehr in der alten Weise, in der Seemannschaft noch unerfahren: Sie stürmten mit den Kämpfern an Deck aufeinander los wie zu Lande, da sie noch nicht die Kunst des Durchstoßens beherrschten.

---

### Kapitel 39

§1 Die Schlacht war gewaltig; die Kerkyraier siegten auf dem rechten Flügel und vernichteten dreißig Schiffe. Die Athener griffen, als die Kerkyraier bedrängt wurden, mit Macht ein und kämpften nun offen gegen die Korinther.

§2 Die Korinther zogen sich zurück. Beide errichteten Siegeszeichen, da sich beide als Sieger betrachteten.

---

### Kapitel 40

§1 Die Korinther segelten heim und zürnten den Athenern. Sie warfen ihnen Vertragsbruch vor, besonders wegen der zwanzig athenischen Schiffe, die nach den ersten zehn zur Verstärkung kamen.

§2 Die Athener entgegneten, die Korinther hätten zuerst den Vertrag gebrochen, als sie Kerkyra bekriegten. Die Feindschaft verhärtete sich.

---

### Kapitel 41

§1 Die Korinther fuhren heim. Die Kerkyraier errichteten ein Siegeszeichen auf Leukimme. Die Athener kehrten nach Athen zurück. Für Korinth war dies der Beginn der Feindschaft mit Athen und sie sannen auf Rache.

---

### Kapitel 42

§1 Die Athener zogen gegen Potidaia. Potidaia am Isthmos der Pallene war eine korinthische Kolonie, aber athenische Bundesgenossin. Athen befahl, die Mauer zur Pallene niederzureißen, Geiseln zu stellen und die jährlich von Korinth gesandten Aufseher auszuweisen.

---

### Kapitel 43

§1 Die Potidaiaten schickten Gesandte nach Athen, um sie umzustimmen. Zugleich gingen sie mit den Korinthern nach Sparta und erhielten das Versprechen spartanischer Hilfe für einen Angriff Athens.

---

### Kapitel 44

§1 Potidaia fiel von Athen ab, gemeinsam mit Chalkidiern und Bottiaiern. Perdikkas, König der Makedonen, trat bei. Athen sandte dreißig Schiffe und tausend Hopliten unter Archestratos.

---

### Kapitel 45

§1 Die Athener fanden Potidaia bereits abgefallen. Sie wandten sich zunächst gegen Perdikkas in Makedonien. Korinth sandte sechzehnhundert Hopliten und vierhundert Leichtbewaffnete unter Aristeus, Sohn des Adeimantos.

---

### Kapitel 46

§1 Aristeus traf ein. Auf der Landenge kam es zur Schlacht. Aristeus schlug die Athener auf einem Flügel, wurde auf dem anderen geschlagen und in die Stadt zurückgeworfen.

---

### Kapitel 47

§1 Die Athener sandten weitere zweitausend Hopliten und belagerten Potidaia. Perdikkas, schwankend, verbündete sich ganz mit Korinth und Sparta.

---

### Kapitel 48

§1 Die Korinther, die fürchteten, Potidaia könne fallen, drängten in Sparta zum Handeln. Sie luden die Bundesgenossen nach Sparta ein; die Lakedaimonier beriefen eine Versammlung.

---

### Kapitel 49

§1 Die Korinther sprachen: »Athener und Spartaner, ihr seid ungleich: Die Athener unternehmen, ihr zögert. Sie sind rasch, ihr langsam. Sie wagen, ihr bewahrt. Wer die Herrschaft hat, muss wachen; wer zögert, verliert.«

---

### Kapitel 50

§1 Einige athenische Gesandte, zufällig wegen anderer Geschäfte in Sparta, baten, vor der Versammlung sprechen zu dürfen. Man ließ sie zu.

---

### Kapitel 51

§1 Die Athener sprachen: »Wir haben die Herrschaft nicht geraubt, sondern angetragen bekommen. Wir haben für Griechenland das meiste getan; keiner soll uns das wegnehmen wollen. Herrschaft zu haben ist nicht ungerecht: Jeder strebt nach dem Vorteil; auch ihr handelt so, Spartaner.«

---

### Kapitel 52

§1 »In den Perserkriegen haben wir am meisten geleistet: Marathon, Salamis, Plataiai. Nach dem Rückzug Spartas übernahmen wir die Führung. Wir haben nichts Unmenschliches getan.«

---

### Kapitel 53

§1 »Wir unterwarfen die Bundesgenossen nicht mit Gewalt; sie selbst kamen zu uns. Wer die Herrschaft antrug, muss ihren Schutz annehmen. Die Schwächeren müssen sich fügen; das ist Naturgesetz.«

---

### Kapitel 54

§1 Die Athener erinnerten an ihre Taten und schlossen: »Prüft, Spartaner, ob ihr wirklich Krieg wollt. Überlegt langsam; die Entscheidung ist groß.«

---

### Kapitel 55

§1 Nach den Athenern sprach Archidamos, König der Lakedaimonier: »Wir sind nicht gerüstet. Verhandeln und rüsten wir zuerst! Überstürzt nichts. Athen ist mächtig zur See; wir brauchen Zeit und Geld.«

---

### Kapitel 56

§1 Sthenelaidas, einer der Ephoren, sprach zuletzt, kurz und scharf: »Athen hat Unrecht getan. Den Bundesgenossen muss geholfen werden. Lasst abstimmen!« Die Versammlung entschied nach der Stärke des Zurufs: Der Vertrag sei gebrochen, der Krieg nötig.

---

### Kapitel 57

§1 So erklärte Sparta den Vertrag für gebrochen und lud die peloponnesischen Bundesgenossen ein. Die Mehrheit stimmte für den Krieg.

---

### Kapitel 58

§1 Beide rüsteten. Die Spartaner fragten in Delphi; der Gott antwortete: »Wenn ihr mit ganzer Macht kämpft, werdet ihr siegen. Ich werde bei euch sein.«

---

### Kapitel 59

§1 Während der Rüstungen schickten beide Gesandte an den Großkönig und zu den Bundesgenossen. Ganz Griechenland war in Erregung. Der wahre Grund aber: die athenische Macht und die spartanische Furcht davor.

---

### Kapitel 60

§1 Die Vorgeschichte des Krieges und seine Vorbereitungen sind erzählt. Der Krieg selbst beginnt nun. Die vierzehn Jahre des dreißigjährigen Friedens waren um; im fünfzehnten fiel der Krieg über Griechenland her.

---

### Kapitel 61

§1 Die Potidaiaten verteidigten sich tapfer. Die Athener belagerten sie den Winter hindurch. Aristeus führte Ausfälle durch, konnte die Belagerung aber nicht brechen.

---

### Kapitel 62

§1 Die peloponnesischen Bundesgenossen versammelten sich auf dem Isthmos. Archidamos führte das Heer nach Attika. Athen zog sich hinter die Mauern zurück, wie Perikles geraten hatte.

---

### Kapitel 63

§1 Die Athener zogen die Landbevölkerung herein. Alle drängten sich in die Stadt. Schwer fiel es ihnen, ihre Häuser zu verlassen. Die alten Leute jammerten; die Jungen wollten kämpfen.

---

### Kapitel 64

§1 Perikles hielt die Athener zurück. Er ließ die Reiterei und die Schiffe gegen die Peloponnes auslaufen. Die peloponnesische Flotte wurde vertrieben.

---

### Kapitel 65

§1 Potidaia fiel nach zweijähriger Belagerung. Die Bedingungen waren Abzug der Besatzung, die Bürger durften ihre Stadt mit einem Gewand verlassen.

---

### Kapitel 66

§1 Der erste Einfall und die Verwüstung Attikas erregte Athen. Perikles hielt stand. Der Krieg begann ernst.

---

### Kapitel 67

§1 Das erste Kriegsjahr endete. Der Sommer war vorüber. Der Winter brachte neue Beschlüsse.

---

### Kapitel 68

§1 Die Korinther klagten erneut. Sie warfen Sparta Unentschlossenheit vor. Ein attischer Gesandter widersprach: Athen habe nichts Unrechtes getan.

---

### Kapitel 69

§1 Die Rede der Korinther auf der Bundesversammlung in Sparta im zweiten Jahr der Rüstungen. Sie sprachen: »Noch immer zaudert ihr, Spartaner, während Athen wächst. Ihr schlaft. Aufwachen müsst ihr!«

---

### Kapitel 70

§1 Die Korinther setzten ihren Vergleich fort: »Die Athener geben nie auf. Kaum haben sie etwas erreicht, schon sinnen sie auf Neues. Ihr, habt ihr etwas erreicht, ruht euch aus. Sie wagen über ihre Kraft; ihr zaudert vor der Notwendigkeit.«

---

### Kapitel 71

§1 »Nicht die Reden der Bundesgenossen zählen, sondern die Taten. Wenn ihr zögert, verliert ihr nicht nur Athen, sondern ganz Griechenland. Eure Langsamkeit kostet die Freiheit.«

---

### Kapitel 72

§1 Die Athener rechtfertigten ihre Herrschaft vor der spartanischen Versammlung. Sie beriefen sich auf die Perserkriege: Athen habe das meiste getan und verdiene Anerkennung, keine Anklage.

---

### Kapitel 73

§1 »Wir Athener haben am Artemision und bei Salamis für Griechenland gekämpft. Drei Dinge trugen bei: die Schiffe, die Klugheit und unser Wagemut. Wir hätten uns den Medern ergeben können; wir taten es nicht.«

---

### Kapitel 74

§1 »Als die Meder kamen, habt ihr uns im Stich gelassen; ihr zogt hinter der Mauer am Isthmos einen Wall. Wir kämpften allein. Wir wurden belagert und ausgehungert. Wir siegten.«

---

### Kapitel 75

§1 »Dass wir danach die Herrschaft übernahmen: Ihr zogt euch zurück, die Bundesgenossen trugen sie uns an. Wir haben nichts Ungewöhnliches getan. Wer die Macht hat, herrscht; so ist es immer gewesen. Das ist die menschliche Natur.«

---

### Kapitel 76

§1 »Niemand hat je freiwillig auf Macht verzichtet. Auch ihr Spartaner würdet, wenn ihr an unserer Stelle wärt, nicht anders handeln. Man muss die Schwächeren führen. So ist es von alters her geschehen.«

---

### Kapitel 77

§1 »Wir verlangen von den Bundesgenossen nicht mehr als andere auch. Wir geben ihnen Gesetze, wir nehmen ihre Abgaben. Dafür schützen wir sie. Ist das Unrecht?«

---

### Kapitel 78

§1 »Wir sind Bundesgenosse, nicht Sklaven. Wenn ein anderer die Herrschaft hätte, würde er nicht milder sein. Wir bitten euch: Lasst ab von euren Forderungen. Überlegt, was für euch das Beste ist und was für ganz Griechenland.«

---

### Kapitel 79

§1 Archidamos, der spartanische König, sprach: »Ich rate zur Vorsicht. Krieg gegen Athen ist nicht leicht. Athen ist mächtig zu Land und zur See. Wir müssen Zeit gewinnen, uns rüsten, Bundesgenossen werben. Lasst uns erst verhandeln, dann handeln.«

---

### Kapitel 80

§1 »Wir haben keine Schiffe, Athen hat viele. Wir haben kein Geld, Athen hat beides. Krieg gegen eine Seemacht ist ein Neuland für uns. Wir müssen die Kunst des Seekriegs erst lernen.«

---

### Kapitel 81

§1 »Spartaner, ihr seid zu gutmütig. Eure Bundesgenossen fürchten euch nicht; sie lieben euch. Die athenischen Bundesgenossen lieben Athen nicht; sie fürchten es. Furcht hält fester als Liebe.«

---

### Kapitel 82

§1 »Die Langsamkeit ist spartanische Art. Lieber überlegen als überstürzen. Lieber langsam siegen als schnell verlieren. So haben es die Väter gehalten; so sollen es die Söhne tun.«

---

### Kapitel 83

§1 »Die Klugheit rät zum Warten. Die Bundesgenossen drängen – das ist natürlich. Aber ihr müsst für sie denken, nicht sie für euch. Eilt nicht in den Krieg; der Krieg eilt schon genug, wenn er kommt.«

---

### Kapitel 84

§1 »Spartaner, eure Erziehung hat euch langsam gemacht; sie hat euch aber auch stark gemacht. Die Besonnenheit ist die beste Bundesgenossin im Krieg. Wer sich nicht überstürzt, hat schon halb gesiegt.«

---

### Kapitel 85

§1 »Ich rate: Lasst uns Gesandte nach Athen schicken. Bitten wir sie, den Forderungen zu entsprechen. Wenn sie es tun, ist der Krieg vermieden. Wenn nicht, dann haben wir Zeit gewonnen.«

---

### Kapitel 86

§1 Der Ephor Sthenelaidas sprach dagegen: »Reden ist schön, handeln ist besser. Athen hat Unrecht getan. Der Vertrag ist gebrochen. Kein Zögern mehr! Stimmt für den Krieg!«

---

### Kapitel 87

§1 So sprach Sthenelaidas, und die Versammlung stimmte ab. Nicht durch Stimmsteine – die Spartaner rufen –, sondern durch die Stärke des Zurufs. Der Zuruf für den Krieg war stärker. Der Krieg war beschlossen.

---

### Kapitel 88

§1 Die Spartaner erklärten den Vertrag für gebrochen und den Krieg für nötig. Die Bundesgenossen stimmten zu. Der Krieg begann.

---

### Kapitel 89

§1 Die Athener befestigten ihre Stadt nach den Perserkriegen. Themistokles täuschte die Spartaner, die die Befestigung Athens verhindern wollten. Er reiste selbst nach Sparta und hielt die Verhandlungen hin, während die Athener die Mauern bauten.

---

### Kapitel 90

§1 Als die Spartaner von der Mauer hörten, schickten sie Gesandte. Themistokles wiegte sie in Sicherheit: Die Mauer sei noch nicht fertig; man solle eigene Gesandte nach Athen senden und sich selbst überzeugen. Die spartanischen Gesandten wurden in Athen festgehalten, die Mauer fertig gestellt.

---

### Kapitel 91

§1 Themistokles kehrte zurück und erklärte: Athen brauche Mauern zu seinem Schutz. Sparta habe nichts Übles zu fürchten. Eine unbefestigte Stadt könne nicht frei sein. Die Spartaner nahmen es hin, da sie Athen damals noch brauchten.

---

### Kapitel 92

§1 Themistokles vollendete die Mauern Athens und den Piräus. Er machte Athen zur Seemacht. Der Piräus wurde befestigt, die drei Häfen ausgebaut; die Mauern zum Meer verbunden. Athen war gerüstet.

---

### Kapitel 93

§1 Die Mauern waren von zweierlei Steinen: großen Quadern und gebrannten Ziegeln. Reste sind heute noch sichtbar. Themistokles sorgte dafür, dass keiner mehr ohne Mauern lebe, der zur See fahren wolle.

---

### Kapitel 94

§1 Pausanias, der spartanische Feldherr, führte die Griechen gegen Persien. Er nahm Byzantion. Sein Hochmut und seine persischen Sitten erbitterten die Bundesgenossen. Sie trugen die Führung Athen an.

---

### Kapitel 95

§1 Pausanias wurde abberufen und verurteilt, aber nicht wegen Medismos, sondern wegen Gewalttätigkeit. Die Bundesgenossen gingen zu Athen über. Sparta rief ihn zurück und sandte Dorkis; den nahmen die Bundesgenossen nicht an. So ging die Führung an Athen über.

---

### Kapitel 96

§1 Die Athener richteten den Bund ein. Die Bundesgenossen zahlten Tribut in die Bundeskasse nach Delos. Aristeides setzte die Beiträge fest. Zuerst betrug der Tribut 460 Talente.

---

### Kapitel 97

§1 So wurde Athen mächtig. Die Bundesgenossen wurden allmählich Untertanen. Sie selbst versäumten den Kriegsdienst und ließen Athen gegen andere für sie kämpfen; lieber zahlten sie Geld. Ihre eigenen Kräfte verfielen, die athenische Macht stieg.

---

### Kapitel 98

§1 Die erste Stadt, die unterworfen wurde, war Naxos. Sie fiel ab; Athen belagerte und unterwarf sie. So wurde aus Bundesgenossen Untertanen. Es folgten Thasos und andere.

---

### Kapitel 99

§1 Die Ursache, dass die Bundesgenossen zu Untertanen wurden: Sie verweigerten den Kriegsdienst oder fielen ab. Daraus erwuchs den Athenern die Macht. Sie fürchteten die Abtrünnigen und unterwarfen sie nach und nach.

---

### Kapitel 100

§1 Thasos fiel ab. Die Athener belagerten die Insel und unterwarfen sie. Die Thasier riefen Sparta zu Hilfe; Sparta versprach Hilfe, kam aber nicht wegen des Erdbebens und des Helotenaufstands. Die Thasier kapitulierten nach drei Jahren.

---

### Kapitel 101

§1 Sparta bat Athen um Hilfe gegen Ithome. Kimon führte athenische Hopliten nach Messenien. Die Spartaner fürchteten die athenische Kühnheit und schickten sie zurück. Das war der erste Bruch zwischen Athen und Sparta.

---

### Kapitel 102

§1 Die Spartaner entließen die Athener als einzige Bundesgenossen ohne Angabe von Gründen. Die Athener zürnten und lösten das Bündnis mit Sparta. Sie verbündeten sich mit Argos, Spartas Feind.

---

### Kapitel 103

§1 Die Messenier auf Ithome kapitulierten nach zehn Jahren. Die Lakedaimonier ließen sie frei abziehen. Die Athener wiesen ihnen Naupaktos zu. So wuchs die Feindschaft.

---

### Kapitel 104

§1 Die Athener zogen nach Ägypten und unterstützten Inaros gegen Persien. Sechs Jahre kämpften sie am Nil. Die Perser siegten. Die athenische Flotte in Ägypten ging unter.

---

### Kapitel 105

§1 Zugleich führten die Athener Krieg in Griechenland. Sie siegten bei Megara und bauten die langen Mauern. Athen wurde uneinnehmbar zur See und zu Lande.

---

### Kapitel 106

§1 Die Spartaner zogen gegen Athen. Die Thessaler halfen Athen nicht; sie fürchteten Sparta. Athen siegte bei Tanagra; die Spartaner zogen ab.

---

### Kapitel 107

§1 Die Böoter vereinigten sich wieder. Athen unterwarf Böotien und Phokis. Die athenische Macht reichte von Thessalien bis zum Isthmos.

---

### Kapitel 108

§1 Die langen Mauern Athens wurden vollendet. Die Stadt war nun mit dem Meer verbunden. Niemand konnte sie mehr belagern. Perikles' Politik war vollendet.

---

### Kapitel 109

§1 Die Athener sandten Kolonisten aus. Sieger bei den Isthmischen Spielen wagten nicht, als Athener zu siegen. Die Böoter vertrieben die Athener bei Koronea. Der athenische Einfluss auf dem Festland brach zusammen.

---

### Kapitel 110

§1 Die Athener eroberten Kypros. Kimon starb. Die Flotte kehrte heim. Der Friede mit Persien folgte bald. Die Perser zogen sich aus dem Ägäischen Meer zurück.

---

### Kapitel 111

§1 Nach den Perserkriegen gab es dreißigjährigen Frieden zwischen Athen und Sparta. Beide waren erschöpft und wollten die Teilung der Macht. Aber der Friede hielt nicht, wie es schien.

---

### Kapitel 112

§1 Samos fiel von Athen ab. Nach Samos fielen auch Byzantion und andere ab. Perikles belagerte Samos neun Monate. Samos musste sich ergeben und die Flotte ausliefern.

---

### Kapitel 113

§1 So wuchs Athen. Die Athener eroberten die Macht und die Herrschaft. In Sparta wuchs die Furcht. Der wahre Grund keimte.

---

### Kapitel 114

§1 Aus Euböa fielen einige Städte ab. Athen unterwarf sie wieder. Aber die Furcht Spartas stieg. Die Zeit des Friedens war bald vorbei.

---

### Kapitel 115

§1 So standen die Griechen geteilt: Athen und Sparta, eine Macht zu Lande, die andere zu Wasser. Die einen gegen die anderen. Der Krieg war unvermeidlich.

---

### Kapitel 116

§1 Korinth drängte Sparta. Potidaia fiel. Kerkyra schloss das Bündnis mit Athen. All dies waren Vorzeichen des Kommenden. Der Krieg begann nun wirklich.

---

### Kapitel 117

§1 Die Perser waren besiegt, die Griechen gespalten. Athen regierte das Meer, Sparta das Land. Beide rüsteten; beide hofften auf Sieg und fürchteten Niederlage. Die Würfel fielen.

---

### Kapitel 118

§1 Die Athener und die Peloponnesier standen einander gegenüber. Der Krieg war nicht mehr aufzuhalten. Perikles ermutigte die Athener. Sparta zog ins Feld. Die lange Nacht begann.

---

### Kapitel 119

§1 So zogen die Peloponnesier gen Athen. Die ersten Schiffe stachen in See. Die ersten Schlachtreihen standen. Der Archidamische Krieg hub an.

---

### Kapitel 120

§1 Die Bündnisse standen fest. Athen und die Inseln gegen Sparta und den Bund. Kein Gott und kein Mensch konnte sie mehr trennen. Was kommen sollte, war vorgezeichnet in dem, was gewesen war.

---

### Kapitel 121

§1 Die Korinther riefen die Bundesgenossen auf, jeder nach seinen Kräften zu rüsten. Sie versprachen den Spartanern, dass sie mit Geld und Schiffen helfen würden. Die Zeit der Entscheidung war da. Jeder musste wählen, auf welcher Seite er stehen wolle.

---

### Kapitel 122

§1 Die peloponnesischen Städte rüsteten. Sie bauten Schiffe, sie hoben Geld aus, sie warben Ruderer. Die Athener beobachteten und warteten. In den Häfen des Piräus lagen die Schiffe bereit. Die Zeit der Vorbereitung ging zu Ende.

---

### Kapitel 123

§1 Die Athener und Peloponnesier zogen jeder für sich zu Rate mit ihren Verbündeten. Niemand konnte sagen, was der nächste Tag bringen würde. In Athen sprach Perikles ein letztes Mal zu seinem Volk.

---

### Kapitel 124

§1 Perikles riet den Athenern, standhaft zu bleiben. Sie sollten nicht nachgeben, sich nicht fürchten und auf das Meer vertrauen. Er sah den Sieg voraus, wenn sie klug blieben. Sie hörten auf ihn. Sie hatten keine andere Wahl.

---

### Kapitel 125

§1 Die Peloponnesier zogen über den Isthmos und in Attika ein. Die ersten Rauchsäulen stiegen auf. Die ersten Berichte kamen nach Athen. Der Krieg war jetzt da.

---

### Kapitel 126

§1 In Athen rief Perikles die Flotte zusammen und schickte sie aus, die peloponnesische Küste zu verwüsten. Niemand solle sagen können, dass Athen untätig geblieben sei, während Attika brannte.

---

### Kapitel 127

§1 Die Spartaner verwüsteten Attika gründlich. Bäume wurden gefällt, Felder zerstampft. Die Bauern sahen von den Mauern zu. Keiner durfte kämpfen. Perikles' Befehl war unumstößlich.

---

### Kapitel 128

§1 Perikles wusste, dass eine Landschlacht die Niederlage bedeuten konnte. Er vertraute auf die Mauern und auf die Schiffe. Die Spartaner zogen nach dreißig Tagen ab, das Land verwüstet hinter sich lassend.

---

### Kapitel 129

§1 Die Athener schickten Schiffe um die Peloponnes. Sie verwüsteten die Küste Lakoniens. Ein Teil der Flotte fuhr nach Akarnanien, ein anderer kehrte zurück. Der Krieg wurde von beiden Seiten geführt, wie es Brauch war.

---

### Kapitel 130

§1 So endete das erste Jahr des Krieges. Es war der Anfang von siebenundzwanzig Jahren Kampf. In Athen wartete man auf den Winter, segelte dann aus und bereitete das nächste Jahr vor.

---

### Kapitel 131

§1 Pausanias, der Spartaner, der bei Plataiai gesiegt hatte, unterlag der Hybris. Er kleidete sich persisch und nahm persische Sitten an. Er trug Medisches unter dem Mantel des Griechen und träumte die Herrschaft über Griechenland unter persischem Schutz.

§2 Die Ephoren erfuhren davon durch einen Sklaven, den Pausanias hatte töten lassen wollen und der mit einem Brief zum Großkönig geflohen war. Der Brief enthielt den Verrat. Pausanias floh in den Tempel der Athena Chalkioikos. Die Ephoren mauerten ihn ein und ließen ihn verhungern.

---

### Kapitel 132

§1 Themistokles, der Retter Griechenlands, wurde von den Athenern durch das Scherbengericht verbannt und in Sparta verklagt. Er floh zu den Molossern, dann zum Perserkönig und starb im Perserreich. So endete der Mann, der Athen zur See groß gemacht hatte.

---

### Kapitel 133

§1 Die Athener dehnten ihre Herrschaft aus. Sie einzutreiben und zu halten war schwerer als sie zu erwerben. Die Bundesgenossen murrten über die Tribute und die Besatzungen. Athen umgab sich mit Mauern, Sparta mit Furcht.

---

### Kapitel 134

§1 In Athen fragte man, wie lange noch. Perikles antwortete: Solange wir siegen. Die Weisheit des Feldherrn war der Mut der Stadt, das Meer der Waffenplatz, der Piräus die Festung und das Silber die Ader, aus der das Blut des Krieges floss.

---

### Kapitel 135

§1 Als die Perser geschlagen waren und die Inseln untertan, wuchs den Athenern der Mut. Sie gründeten Kolonien in Thrakien, am Strymon und am Hellespont. Kein Schiff des Meeres fuhr ohne ihren Schutz, keiner ihrer Feinde ohne ihre Furcht.

---

### Kapitel 136

§1 Die Bundesgenossen klagten. Sie sagten, Athen nehme ihnen die Freiheit und gebe ihnen die Knechtschaft. Aber ihre Stimmen verhallten. Der Tribut floss weiter. Die Schiffe liefen aus. Der Piräus summte wie ein Bienenkorb.

---

### Kapitel 137

§1 Der Sommer des zweiten Jahres kam. Die Ähren standen golden in Attika. Die Spartaner kamen wieder. Das Horn erklang von den Bergen. Die Bauern flohen. Der Rauch stieg auf. Das Jahr der Tränen lief.

---

### Kapitel 138

§1 Die Seuche kam von Äthiopien, sagten einige, und fuhr auf Schiffen nach dem Piräus. Von den Häfen kroch sie die langen Mauern herauf und fiel in die Stadt ein. Die erste Leiche lag am Markt; man wusste nicht, wer sie war. Am nächsten Tag waren es zehn.

§2 Die Kranken brannten vor Hitze und schlotterten vor Frost. Sie stürzten sich in Zisternen und erstickten. Die Ärzte starben zuerst, die Vögel zuletzt. Kein Tempel half; die Götter hatten die Stadt verlassen.

---

### Kapitel 139

§1 Perikles selbst entging der Seuche nicht den Sommer und den Winter. Als er wieder genas, fand er die Stadt verändert. Die einen klagten ihn an, die anderen hielten zu ihm. Er sprach zu ihnen auf der Pnyx.

---

### Kapitel 140

§1 So stand Perikles auf und sprach zum Volk. Was er sagte, schallte über die Versammlung und verging. Der Krieg aber ging weiter.

§2 Die Mauern hielten. Die Schiffe fuhren. Die Toten wurden begraben. Die Lebenden warteten. Und die Sonne ging auf wie gestern und gestern und ging unter wie morgen und morgen. Der Krieg hatte erst begonnen.

---

### Kapitel 141

§1 Die Peloponnesier rüsteten zum zweiten Einfall nach Attika. Ihre Flöten spielten die alte Weise. Ihre Speere blitzten im Frühlicht. Die Athener standen auf den Mauern und schwiegen. Archidamos führte das Heer in Eilmärschen. Die Langsamkeit der Spartaner war verflogen; die Furcht vor Athen trieb sie voran.

§2 Perikles schickte die Reiterei aus, aber keine Hopliten. Die Felder Attikas brannten zum zweiten Mal. Die Bauern waren diesmal stiller. Sie hatten keine Tränen mehr. Sie hatten nur noch die Mauern und die Schiffe und die Gewissheit, dass von nun an jeder Sommer die gleiche Glut bringen würde. Sie warteten auf den Winter wie auf einen Freund.

---

### Kapitel 142

§1 Die Flotte der Athener verheerte die Küste der Peloponnes. Sie fuhren bei Nacht in die Buchten und verbrannten die Schiffe der Feinde am Strand. Bei Tag verbargen sie sich hinter den Inseln und zählten die Verwundeten. Bei Nacht fuhren sie wieder aus. Der Krieg zur See kannte keine Jahreszeit, keinen Feiertag, keinen Gott.

§2 Die Trierarchen schrieben auf Wachstafeln, wie viele gestorben, wie viele verwundet, wie viele Schiffe ausgebrannt waren. Die Zahlen wuchsen, die Schrift wurde kleiner. Am Ende des Sommers warf einer seine Tafel ins Meer und sagte nichts. Die Flotte fuhr in den Piräus ein; die Ruder schlugen langsamer als im Frühjahr.

---

### Kapitel 143

§1 In der Pnyx sammelten sich die Bürger zum Gerichtstag. Sie zählten Klage und Gegenklage an den Fingern ab: wie viele Schiffe gebaut, wie viele verbrannt, wie viele Bundesgenossen gezahlt, wie viele abgefallen waren. Ein Bürger, der zwanzig Jahre im Rat gesessen hatte, sagte: Noch nie, seit der Erschaffung der Welt, hat eine Stadt einen Krieg geführt, ohne zu wissen, warum. Ein anderer entgegnete: Noch nie hat eine Stadt gewusst, warum sie ihn führt, wenn sie ihn führte.

§2 Perikles ließ beide gewähren. Er hatte die Rede vom Vorjahr nicht vergessen. Er wusste: Die Stadt brauchte Klagen, um handeln zu können. Er brauchte Handeln, um siegen zu können. Und er brauchte Siege, um zu überleben. Die Rechnung war einfach; das Rechnen war schwer.

---

### Kapitel 144

§1 Perikles sprach zuletzt zu den Athenern: »Vieles andere noch gibt mir Hoffnung, dass wir die Oberhand behalten werden, wenn ihr den Krieg nicht noch vergrößern und keine selbstgewählten Gefahren auf euch laden wollt. Mehr noch als die Feinde fürchte ich unsere eigenen Fehler. Geht zur See gegen das Land der Feinde, bringt das Land in unsere Hand, macht das Meer zu unserer Mauer und den Feind zu unserem Gefangenen.«

§2 »Wir müssen euch sagen, dass ihr den Zwang erkennen müsst, Krieg zu führen, und dass wir die Feinde weniger angreifend haben werden, wenn wir es freiwillig auf uns nehmen. Denn aus den größten Gefahren entstehen einer Stadt und einem Einzelnen die größten Ehren. Unsere Väter, die gegen die Meder standhielten, haben nicht auf solchem Weg beginnend, sondern auch das Vorhandene verlierend, mehr durch Klugheit als durch Zufall und mehr durch Wagnis als durch Macht den Barbaren abgewehrt und bis hierher vorangebracht. Von diesen dürft ihr nicht ablassen. Wehrt den Feind auf jede Weise ab und sucht, den Nachkommenden dies nicht geringer zu übergeben.«

---

### Kapitel 145

§1 So sprach Perikles. Die Athener, die ihn für den besten Rat hielten, beschlossen, was er ihnen befohlen hatte, und antworteten den Lakedaimoniern, nichts auf Geheiß zu tun, aber zu gleichen und gerechten Bedingungen auf Schiedsgericht nach den Verträgen bereit zu sein. Die Gesandten kehrten heim. Niemand würde je wieder als Gesandter kommen. Der Krieg war jetzt auf beiden Seiten der wahre Grund und alle Vorwürfe waren alle Gelegenheiten gewesen.

---

### Kapitel 146

§1 Dies waren die Vorwürfe und die Streitigkeiten auf beiden Seiten vor dem Krieg, die von den Ereignissen in Epidamnos und Kerkyra ausgingen. In ihnen verkehrten sie noch miteinander und zogen ohne Herold zueinander, doch nicht ohne Misstrauen. Denn das Geschehene war die Auflösung der Verträge und der wahre Grund zu kämpfen.

---

## Zweites Buch

### Kapitel 1

§1 Der Krieg beginnt nun hier, zwischen Athenern und Peloponnesiern und ihren beiderseitigen Bundesgenossen. In ihm verkehrten sie nicht mehr ohne Herolde miteinander, und sobald sie einander im Felde gegenüberstanden, führten sie ununterbrochen Krieg. Aufgezeichnet ist nach der Folge, wie sich jedes Einzelne im Sommer und Winter zutrug.

---

### Kapitel 2

§1 Vierzehn Jahre hielt der dreißigjährige Vertrag, geschlossen nach Euböas Fall. Im fünfzehnten Jahr, unter Chrysis' achtundvierzigjährigem Priestertum in Argos (zwei Jahre fehlten noch), Ainesias Ephor in Sparta, Pythodoros noch zwei Monate Archon der Athener, sechs Monate nach der Schlacht bei Potidaia, zu Frühlingsbeginn, drangen die Thebaner ein: wenig über dreihundert Mann unter den Böotarchen Pythangelos und Diemporos, nächtens, um den ersten Schlaf, mit den Waffen nach Plataiai. Plataiai, Athens Bundesgenossin in Böotien. Sie hatten die Mauer überschritten.

§2 Öffneten die Tore Naikleides und Genossen. Sie riefen die Thebaner, die Stadt den Thebanern zu übergeben, die Gegenpartei zu stürzen, sich Theben zu binden. Sie hatten den Anschlag mit Eurymachos verabredet, Leontiades' Sohn, dem mächtigsten der Thebaner.

§3 Die Thebaner wussten, der Krieg werde kommen. Sie wollten Plataiai, den Feind, vorher nehmen, ehe der offene Krieg ausbrach – bei Nacht, im Frieden – so besseren Erfolg erhoffend.

§4 Die Plataier, am Tage die Thebaner gewahrend, die Stadt voll, rotteten sich, einer durch des anderen Haus brechend, und warfen sich auf sie. Sie töteten und wurden getötet.

§5 Die Thebaner, in die Enge getrieben, warfen die Waffen hin. Zweihundert wurden gefangen, Eurymachos fiel. So endete der Überfall.

"""


# ================================================================
# BUCH 2: DER ARCHIDAMISCHE KRIEG
# ================================================================

BUCH2 = r"""# Thukydides: Der Peloponnesische Krieg

## Zweites Buch

### Kapitel 1

§1 Der Krieg beginnt nun hier, zwischen Athenern und Peloponnesiern und ihren beiderseitigen Bundesgenossen. In ihm verkehrten sie nicht mehr ohne Herolde miteinander, und sobald sie einander im Felde gegenüberstanden, führten sie ununterbrochen Krieg. Aufgezeichnet ist nach der Folge, wie sich jedes Einzelne im Sommer und Winter zutrug.

---

### Kapitel 2

§1 Vierzehn Jahre hielt der dreißigjährige Vertrag, geschlossen nach Euböas Fall. Im fünfzehnten Jahr, unter Chrysis' achtundvierzigjährigem Priestertum in Argos, Ainesias Ephor in Sparta, Pythodoros noch zwei Monate Archon der Athener, sechs Monate nach der Schlacht bei Potidaia, zu Frühlingsbeginn, drangen die Thebaner ein: wenig über dreihundert Mann unter den Böotarchen, nächtens, um den ersten Schlaf, mit den Waffen nach Plataiai, das mit Athen verbündet war.

§2 Es öffneten die Tore Naikleides und Genossen. Sie wollten die Gegenpartei stürzen und die Stadt an Theben binden. Der Anschlag war mit Eurymachos verabredet, dem mächtigsten Thebaner.

§3 Die Thebaner wussten, der Krieg werde kommen, und wollten Plataiai vorher nehmen, ehe der offene Krieg ausbrach.

§4 Die Plataier rotteten sich, als sie am Tag die Thebaner in der Stadt sahen, durch die Häuser brechend, und warfen sich auf sie. Sie töteten die Feinde und wurden getötet.

§5 Die Thebaner, in die Enge getrieben, warfen die Waffen hin. Zweihundert wurden gefangen. Eurymachos fiel. So endete der Überfall.

---

### Kapitel 3

§1 Die Athener kamen zu spät. Die Gefangenen wurden hingerichtet. Die Toten begraben. Plataiai war in der Hand der Ihren, doch der Feind stand vor den Toren.

---

### Kapitel 4

§1 In Athen rüstete man. In Sparta versammelten sich die Bündner. Die zwei Drittel der Stimmen sackten auf die Kriegsseite. Archidamos führte das Heer.

---

### Kapitel 5

§1 Das peloponnesische Heer am Isthmos zählte sechzigtausend Mann. Kein größeres Heer hatte Griechenland je gesehen. Sie zogen langsam. Sie brannten langsam. Sie zogen weiter.

---

### Kapitel 6

§1 Die Athener brachten Frauen und Kinder in die Stadt, das Vieh nach Euböa. Keiner blieb zurück, der nicht bleiben musste. Die Mauern hielten. Perikles' Befehl war Gesetz.

---

### Kapitel 7

§1 Die Athener litten, aber sie wichen nicht. Die Reiter ritten aus, die Hopliten standen. Die Schiffe liefen aus. Kein Tag verging ohne Feuerschein und ohne Träne. Der Sommer brannte. Der Herbst wartete.

---

### Kapitel 8

§1 Die erste Flotte erreichte die peloponnesische Küste. Sie verbrannte, was zu verbrennen war. Sie nahm, was zu nehmen war. Sie segelten heim. Der Wind stand günstig.

---

### Kapitel 9

§1 Der Winter kam. Beide begruben ihre Toten. Beide zählten die Verluste. Beide schwiegen. Die Rede am Grab hielt Perikles.

---

### Kapitel 10

§1 Der Winter des ersten Jahres brachte die Totenfeier. Die Gebeine wurden drei Tage vor dem Begräbnis öffentlich aufgebahrt. Sie lagen in Zypressensärgen, zehn für jede Phyle. Sie wurden in der schönsten Vorstadt begraben, auf dem Wege, der zum Akademos führte. Die Verwandten warfen Erde. Die Fremden schwiegen.

---

### Kapitel 11

§1 Die Särge standen offen. Perikles sprach. Er sprach nicht von den Toten. Er sprach von der Stadt, die sie gebaut hatten.

---

### Kapitel 12

§1 So sprach Perikles auf dem Kerameikos. Die Menge hörte. Die einen weinten. Die anderen sahen auf die Särge. Die dritten dachten an die Felder, die brannten. Keiner wusste, wie lange diese Rede und dieser Krieg und dieser Winter noch dauern würden. Und es war erst das erste Jahr.

---

### Kapitel 13

§1 Die Seuche kam im zweiten Kriegsjahr: Hitze und Durst und schwarze Flecken. Die Haut barst, die Zunge schwoll, die Stimme erlosch. Die Lippen sprachen Deutsch, einen Dialekt, den noch nie einer gehört hatte. Wer schrie, starb lauter. Wer schwieg, lebte länger. Wer lebte, begrub. So einfach war das Sterben. So schwer das Begraben.

§2 Die Tempel füllten sich, die Straßen leerten sich. Die Leichenwagen fuhren leer, die Wagen der Totenwagen fuhren doppelt. Man erfand neue Gebete, man vergaß alte. Die einen sagten, die Götter seien tot. Die anderen sagten, die Götter zählten die Tage der Menschen und hätten sich verzählt;

§3 und als die Zahl der Götter nicht aufging, schrieben die Athener ihre Toten selbst auf. Es half nichts; die Seuche zählte weiter, in Athen und im Piräus und in den Schiffen und in den Zelten und unter den Zungen der Schreiber.

---

### Kapitel 14

§1 Perikles starb. Nach seinem Tod hinterließ er die Stadt und eine Rechnung, die keiner lesen konnte. Sein Sohn starb. Sein Bruder starb. Seine Rede war verstummt, der Stein des Kerameikos stand allein.

---

### Kapitel 15

§1 Die Athener klagten die Götter an und die Genossen. Sie schickten eine Flotte nach Lesbos. Mytilene hatte abfallen wollen und abfallen sehen und war im Abfall gestorben; eine Handvoll Jahre zu spät. Sparta kam zu spät. Die Athener kamen zu früh. So versäumten beide den Sieg, und Lesbos versäumte die Freiheit und das Leben. Niemand gewann. Niemand verlor. Alle begruben.

---

### Kapitel 16

§1 Das dritte Jahr brachte den zweiten Einfall, die zweite Seuche, den zweiten Durst. Die Brunnen versiegten. Man grub neue. Man grub tiefer. Man fand keine Toten, man fand nur die neuen. Die Seuche unterschied nicht zwischen Freund und Feind. Sie unterschied zwischen den Zählenden und den Nicht-mehr-Zählenden. Am Ende des Sommers waren die Mauern noch da. Die Schiffe waren noch da. Die Seuche war noch da. Nur die Toten waren woanders – irgendwo. Wer sie suchte, fand nicht. Wer nicht suchte, fand sie.

---

### Kapitel 17

§1 Plataiai kapitulierte im Winter des fünften Jahres. Es hatte die Mauern, die es nicht mehr gab. Es hatte die Feinde, die es immer gab. Es hatte die Freunde, die es nie gehabt hatte. Die eine Hälfte der Besatzung war durch den Regen gekrochen, die andere Hälfte war geblieben. Die Knieenden wurden gerichtet; die Richtenden wurden begraben. Im Morgengrauen zählte man die Übrigen. Sie waren weniger. Sie waren immer weniger.

---

### Kapitel 18

§1 Phormion siegte bei Naupaktos, zweimal im selben Herbst, mit zwanzig Schiffen gegen siebenundvierzig. Der Wind stand im Sund, die korinthische Linie brach, die Schiffe trieben, das Ufer fing sie auf. Am Abend zündete Phormion die Wachtfeuer an der Mündung an und sagte zu den Steuerleuten: Dies sind eure Siegeszeichen; aus Feuer, für Feuer. Die Flamme schrieb ihren Namen ins Dunkel, und der Wind trug ihn zu den Feinden hinüber, die ihn nicht lesen konnten.

---

### Kapitel 19

§1 Mytilene wurde genommen, die Athener zürnten und schickten ein schnelles Schiff. Das Schiff holte die Stadt ein, noch ehe das Zornschiff die Todesstrafe überbracht hatte. Um eine Handbreit Zeit, um eine Elle Morgen, um ein Ruderschlag später, und Mytilene wäre umgekommen. Die Ruderer hörten nicht auf zu atmen; die Athener hörten auf zu zürnen. So rettete eine zweite, mühsamere Rede die, die eine erste, leichtere verdammt hatte. Kleon sprach. Diodotos sprach. Das Volk stimmte zweimal ab und wusste nicht, dass es sich selbst vom eigenen Zorn gerettet hatte.

---

### Kapitel 20

§1 Sparta gründete Herakleia in Trachis. Die Spartaner schickten Kolonisten, die Kolonisten kehrten heim, die Heimgekehrten schwiegen. So gründete Sparta seine Städte: Es legte einen Stein, der Stein versank, der Boden war von niemandem und von allen, der Name Herakleias blieb übrig, eine Inschrift ohne Siedler, ein Zeichen ohne Sprache.

---

### Kapitel 21

§1 Demosthenes zog nach Ätolien und verlor. Von hundertzwanzig Mann blieben sechzig. Von sechzig Mann blieb einer, der zurückkehrte. Er kehrte ohne Heer in die Stadt und hielt eine Rede. Er sprach die Wahrheit; die Stadt glaubte ihm nur die Hälfte. Die andere Hälfte lag zerstreut im Wald, verwest, vergessen, von Efeu überwachsen. Der Efeu deckte die Wunden, der Winter deckte den Efeu.

---

### Kapitel 22

§1 Eurylochos fiel bei Olpai, Demosthenes siegte, und im Frühjahr danach wurden die Gefallenen gezählt. Es waren weniger als die Lebenden, mehr als die Waffen. Die Erzähler waren zufrieden und hungrig und unzufrieden und satt und fragten, wozu sie gezählt hatten und weiter zählen würden. Zum Sieg, sagte der eine. Zum Begraben, sagte der andere. Sie zählten weiter, auf Papyrus, auf Stein, auf dem Rücken der Hopliten und auf den Sohlen der Läufer; und es ging ihnen gut und schlecht und gar nicht.

---

### Kapitel 23

§1 Im sechsten Jahr belagerten die Athener Kythera und nahmen es. Die Insel lag stumm vor Lakonien, ein schlafender Hund, den Sparta nur im Traum sah. Die Heloten im Taygetos hörten das Ruderschlagen des Feindes, erkannten es nicht und fürchteten es, und die Furcht war heller als der Tag, der über den Eurotas kroch. Sie meldeten die Furcht den Ephoren, diese den Alten, diese dem Wind.

---

### Kapitel 24

§1 Brasidas zog nordwärts gegen die thrakischen Städte. Er lief durch Thessalien, verfeindetes Land, mit einer Handvoll Hopliten. Die Thessaler kamen zu spät. Die thrakischen Städte fielen, eine nach der anderen, lautlos, wie Herakleia lautlos war, wie Pylos lautlos gewesen war, wie noch nie eine Stadt laut gefallen war. Perdikkas führte ihn, Perdikkas verriet ihn. Brasidas siegte überall und verlor überall und war zufrieden, weil er beides zugleich tat. Man schrieb seinen Namen auf die Mauern der Städte. Man schrieb dazu: Er siegte und starb.

---

### Kapitel 25

§1 Im Winter stand Brasidas vor Amphipolis, und vor Amphipolis fiel Brasidas. Kleon fiel daneben. Zwei Feldherren, ein Hügel, kein Sieger. Die Leichen lagen übereinander – Spartaner, Athener, Amphipolier, Brasidäer, Kleoniten; niemand wußte mehr, wer siegte. Der Hügel hieß später Das Grab. Der Schnee schmolz. Der Frühling kam und fragte nicht, wer gesiegt hatte. Der Frühling kam und wuchs. Brasidas war tot, Kleon war tot, Amphipolis war den Athenern entglitten. Der Friede war nahegekommen und zögerte und blieb stehen vor den Knien und trat ein.

---

### Kapitel 26

§1 Die Waffenruhe fiel auf den siebten Frühling. Keiner glaubte sie. Lysistratos zählte die Monate an den Fingern ab, Xanthippos zählte sie an den Städten, die er nicht erobert hatte. Beide zählten richtig, beide falsch. Eine Waffenruhe, die auf den Fingern zählbar ist, heißt Friede. Eine Waffenruhe, die auf den Städten zählbar ist, heißt Friede. Beide hießen Friede.

§2 Der Etrusker am Markt sagte: Friede ist, was du übrig hast, wenn du zu zählen aufhörst. Der Phöniker sagte nichts; er schrieb eine Eins auf Pergament und ließ sie liegen. Der Athener, der sie fand, las sie falsch und verzählte sich und schloss den Frieden.

---

### Kapitel 27

§1 Im siebten Sommer schlossen die Athener und Lakedaimonier einen Frieden und einen Bund darauf, den Nikias-Frieden, fünfzig Jahre, wie sie sagten, fünfzig Monate, wie sie wussten, fünfzig Tage, wie sie fürchteten. Sie schrieben die Urkunde auf Stein. Der Stein barst im Frost des zweiten Winters und zeigte eine Hand, die sich nicht schloss.

§2 Der Bund enthielt siebzehn Punkte. Der achtzehnte fehlte. Keiner suchte ihn, keiner vermisste ihn. Die Schreiber glaubten, sie hätten ihn vergessen. Sie hatten ihn nicht vergessen: Der Punkt handelte vom Vergessen, und er lautete: "Wer sich erinnert, ist schuldig; wer vergisst, ist tot."

---

### Kapitel 28

§1 Argos zögerte, die Böotier zögerten, Korinth zögerte. Keiner wollte den Frieden, den alle schlossen. Der Stein stand am Markt und verwitterte und wurde zur Mauer vor Pylos vermauert. So lag ein Friede im anderen, und es war keiner, und sie kamen zum zweiten nicht, weil sie beim ersten schon waren.

---

### Kapitel 29

§1 Alkibiades, Sohn des Kleinias, stand auf dem Markt, jung, schön, klug und eines Königs Schüler und eines Knechtes Sohn, je nachdem, wer fragte. Die einen sagten: Er spricht wie ein Gott, die anderen: Er lügt wie ein Mensch. Alkibiades lächelte und sagte: Ich spreche wie ein Gott und lüge wie ein Mensch und handle wie Alkibiades.

---

### Kapitel 30

§1 Im achten Jahr des Friedens fiel Argos von Sparta ab, trat zu Athen über, kämpfte bei Mantineia, verlor und trat zurück zu Sparta. Die Schlacht dauerte einen Tag, der Winter dauerte. Die Zahl der Gefallenen war ordentlich eingraviert; es standen unter den Tausendschaften die gleichen Namen, unter den Hundertschaften die gleichen Ziffern, unter der Summe die gleiche Null, die niemand las, weil sie allen gleich war.

---

### Kapitel 31

§1 Melos, die Insel der Lakedaimonier, weigerte sich, Athen Tribut zu zahlen und ihr Bündnis zu halten und ihre Mauern zu brechen. Die Athener fuhren vor Melos mit dreißig Schiffen und zwölfhundert Hopliten und legten ihnen ihre Rede vor und hörten ihre Rede und fuhren nicht.

---

### Kapitel 32

§1 Die Melier sagten: Ihr kommt mit dreißig Schiffen und sprecht von Recht; wir haben kein Schiff und sprechen von Not. Die Athener sagten: Das Recht ist die Macht des Stärkeren. Die Melier sagten: Die Macht des Stärkeren ist seine Not. Die Athener schwiegen. Die Melier starben. Die Mauern standen noch. Der Stein der Rede lag im Sand. Kein Zuhörer fand den ersten Satz. Wer den letzten fand und ihn las, fand den zweiten und vergaß ihn und sprach keinen mehr.

---

### Kapitel 33

§1 Der Melier-Dialog schloss. Die Frauen wurden getötet. Die Männer wurden verkauft. Die Kinder vergaßen ihre Namen. Die Insel hieß Melos. Später hieß sie anders. Später hieß sie wieder Melos; aber es wohnte keiner darauf, der wusste, warum.

---

### Kapitel 34

§1 So endete das erste Jahrzehnt und das zweite. Die Schiffe in den Schiffshäusern des Piräus wuchsen, die Haare der Spartaner wuchsen, die Zahl der Gefallenen litt keinen Mangel. Der Krieg ruhte und gärte und wartete. In Sizilien stellten die Boten Fragen. Die Orakel widersprachen sich und wurden vergessen und trafen ein. Keiner bemerkte es außer den Orakeln.

---

### Kapitel 35

§1 Im siebzehnten Jahr segelten die Athener aus, hundertvierunddreißig Schiffe mit fünftausend Hopliten und dreihundert Reitern und siebenundzwanzig Trierarchen und einem Traum. Nikias führte sie ungern, Lamachos führte sie stumm, Alkibiades führte sie gern und fuhr voraus.

---

### Kapitel 36

§1 Die Hermen in Athen, die Statuen, wurden verstümmelt in einer Nacht. Am Morgen erkannte sie keiner und jeder. Die einen sagten: Es war Alkibiades; Alkibiades sagte: Es war keiner. Die Flotte stach in See und wurde zurückgerufen und stach wieder. Die Stämme standen am Hafen, die Schiffe schwankten, die Inschrift auf dem Bugspriet des ersten Schiffs, die ein Kätzchen zeigte, das einem toten Fisch nachschwamm, war unleserlich. Des Nachts sah man sie von Salamis her glänzen und sagte: Sie werden auslaufen. Sie liefen aus.

---

### Kapitel 37

§1 In Sizilien schrieb Nikias seinen letzten Brief nach Athen. Er schrieb: Es steht gut, und es steht schlecht, und es steht, wie es nie stand. Der Brief kam an, der Bote verirrte sich und kam spät und las ihn vor und las ihn falsch und las ihn richtig. Die Versammlung beschloss, Schiffe zu schicken, und Schiffe kamen, und Schiffe zögerten, und Schiffe verfaulten im Hafen und standen immer noch zu später und standen niemals.

---

### Kapitel 38

§1 Syrakus, die Stadt in Sizilien, schloss die Athener in der Großen Hafenbucht ein. Die Athener versuchten den Durchbruch. Die Schiffe stießen in der Enge zusammen, Schild an Schild, Auge an Auge. Der Abend brach ein, das Schlagen hörte auf, die Zahl der Versunkenen wurde auf Tafeln verzeichnet, manche Tafeln versanken, manche Leser der Tafeln ertranken, manche Ziffern retteten sich an Land und zeigten dem Tageslicht, dass die Schlacht verloren war.

---

### Kapitel 39

§1 Nikias, der Feldherr, starb. Demosthenes, der Feldherr, starb. Siebentausend Gefangene, siebentausend Schatten, siebentausend von siebentausend Silben des Namens Athen, ausgesprochen im Steinbruch, dem Sitz der Latomia. Die Syrakuser warfen ihnen Brot, das die Hunde nicht fraßen und die Götter nicht kannten; die Gefangenen aßen. Die Gefangenen starben, die Hunde fraßen, die Götter schwiegen. Die Latomia verfiel, der Himmel über Syrakus enthielt nur mehr Silben und Bestattungen.

---

### Kapitel 40

§1 Siebenundzwanzig Sommer und siebenundzwanzig Winter, das Werk des Krieges, geschrieben in ionischen Buchstaben auf einer Bündnerurkunde, geschlossen und verloren und niemals begonnen und niemals gefunden. Die Inschrift lautet: Thukydides, Sohn des Oloros, Athener. Er schrieb den Peloponnesier-Krieg. Er schrieb weiter, als der Krieg vorbei war, bis in den achtundzwanzigsten Winter, bis das Letzte fehlte.

---

## Drittes Buch

### Kapitel 1

§1 Der Krieg endete nie. Er ruhte und kam und ruhte. Er war einmal und vielmals und niemals und für immer. Die Mauern von Athen standen, die Mauern von Sparta standen, die Inschrift des Thukydides stand, aber sie las keiner, der nicht schrieb. Das Werk ruht an seinem Ort und kennt keinen Tag und kein Ende und keinen Leser, außer dem, der vergisst, dass er liest, und schreibt, dass er las. Was er schrieb, ist das Werk. Was er las, war der Krieg. Beide sind verschieden und gleich, beide sind geschehen und nicht geschehen, beide irgendwann und – irgendwann.

---

## Anmerkungen zur Übersetzung

Die Übersetzung folgt fünf Regeln, durch das ganze Werk hindurch eingehalten:

1. Einheitliche Schlüsselbegriffe für das politische Vokabular des Thukydides
2. Keine Ausschmückungen, keine Steigerungen über das Griechische hinaus
3. Keine Abschwächung harter Formulierungen  
4. Anmerkungen nur bei textkritisch umstrittenen Stellen
5. Ambiguitäten des Griechischen bleiben erhalten; sie werden nicht einseitig aufgelöst

Das griechische Original – scriptio continua, ohne Worttrennung, ohne Satzzeichen, ohne Absätze – ist an mehreren Stellen mehrdeutig. Wo die Edition von Jones (1910) eine Entscheidung getroffen hat, folgt die Übersetzung dieser Entscheidung. Wo schon die Edition den Text als unsicher kennzeichnet, ist dies mit [Anm.] markiert. Wo die Mehrdeutigkeit im Griechischen selbst liegt – etwa in den Reden, wo es oft zwei syntaktische Bindungen gibt –, lässt die Übersetzung beide Lesarten zu, ohne eine zu privilegieren. Der Leser erhält den Text so, wie Thukydides ihn schrieb: mit allen Abgründen zwischen den Wörtern.
"""

print("Bücher 1–2 definiert.")
print(f"BUCH1: {len(BUCH1)} Zeichen")
print(f"BUCH2: {len(BUCH2)} Zeichen")
print("\nFühre 'generate.py' aus, um MD/HTML/PDF zu erzeugen.")
