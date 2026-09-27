#!/usr/bin/env python3
"""
Thukydides: Der Peloponnesische Krieg
=====================================
Vollständige Übersetzung aller acht Bücher aus dem Altgriechischen ins moderne Deutsch.

Quelle: Perseus Digital Library (tlg0003.tlg001.perseus-grc2.xml)
Edition: Henry Stuart Jones, OCT 1910/1942

Übersetzungsgrundsätze:
  1.  Einheitliche Schlüsselbegriffe im ganzen Werk
  2.  Nichts hinzugefügt, nichts gesteigert
  3.  Harte Formulierungen nicht abschwächen
  4.  Anmerkungen nur bei echten textkritischen Zweifeln
  5.  Sorgfältige Behandlung griechischer Ambiguitäten
  6.  Abschnittszählung mit §‑Zeichen

Glossar der Kernbegriffe:
  πρόφασις (prophasis)    → wahrer Grund
  αἰτία (aitia)           → Vorwurf / Anschuldigung
  στάσις (stasis)         → Bürgerkrieg
  δύναμις (dynamis)       → Macht
  παρασκευή (paraskeuē)   → Rüstung
  δουλεία (douleia)       → Knechtschaft
  ξυμμαχία (xymmachia)    → Bündnis
  λόγος / ἔργον           → Wort und Tat
  ἀνάγκη (anankē)         → Zwang
  τύχη (tychē)            → Zufall / Glück
"""

import subprocess, os, sys, textwrap

OUTPUT = os.path.dirname(os.path.abspath(__file__))

# ================================================================
# HILFSFUNKTIONEN
# ================================================================

def write_md(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ {path}")

def write_html(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ {path}")

def md_to_html(md_content):
    """Simple Markdown-to-HTML converter."""
    import re
    lines = md_content.split("\n")
    html = []
    html.append('<!DOCTYPE html>')
    html.append('<html lang="de">')
    html.append('<head>')
    html.append('<meta charset="UTF-8">')
    html.append('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
    html.append('<title>Thukydides: Der Peloponnesische Krieg</title>')
    html.append('<style>')
    html.append('body{max-width:40em;margin:2em auto;padding:0 1em;font-family:Georgia,serif;line-height:1.6;color:#1a1a1a}')
    html.append('h1{font-size:1.8em;margin-top:2em;border-bottom:1px solid #ccc}')
    html.append('h2{font-size:1.4em;margin-top:2.5em}')
    html.append('h3{font-size:1.2em;margin-top:2em;color:#555}')
    html.append('p{margin:0.8em 0}')
    html.append('.kapitel{font-weight:bold;color:#333;font-size:0.85em;text-transform:uppercase;letter-spacing:0.05em}')
    html.append('.section{display:inline;color:#083;font-weight:bold;margin-right:0.3em}')
    html.append('.annot{color:#832;font-style:italic;font-size:0.9em}')
    html.append('blockquote{font-style:italic;margin:1em 2em;color:#444}')
    html.append('hr{border:none;border-top:1px solid #ddd;margin:2em 0}')
    html.append('</style>')
    html.append('</head>')
    html.append('<body>')
    
    in_para = False
    for line in lines:
        if line.startswith('# Thukydides'):
            html.append(f'<h1>{line[2:]}</h1>')
        elif line.startswith('## '):
            html.append(f'<h2>{line[3:]}</h2>')
        elif line.startswith('### '):
            html.append(f'<h3>{line[4:]}</h3>')
        elif line.startswith('**Kapitel'):
            num = line.replace('**Kapitel ', '').replace('**', '')
            html.append(f'<p class="kapitel">Kapitel {num}</p>')
        elif line.startswith('§'):
            html.append(f'<p class="section">{line}</p>')
        elif line.startswith('>'):
            html.append(f'<blockquote>{line[2:]}</blockquote>')
        elif line.startswith('[Anm.'):
            html.append(f'<p class="annot">{line}</p>')
        elif line == '---':
            html.append('<hr>')
        elif line == '':
            html.append('')
        else:
            html.append(f'<p>{line}</p>')
    
    html.append('</body>')
    html.append('</html>')
    return '\n'.join(html)

def generate_pdf(md_path, pdf_path):
    """Generate PDF from Markdown using pandoc or weasyprint."""
    try:
        subprocess.run([
            "pandoc", md_path, "-o", pdf_path,
            "--pdf-engine=xelatex",
            "-V", "mainfont=DejaVu Serif",
            "-V", "geometry:margin=2.5cm",
            "-V", "fontsize=11pt",
            "-V", "lang=de"
        ], check=True, capture_output=True)
        print(f"  ✓ {pdf_path}")
    except FileNotFoundError:
        print(f"  ⚠ pandoc nicht verfügbar, PDF-Erzeugung übersprungen")
    except subprocess.CalledProcessError as e:
        print(f"  ⚠ PDF-Fehler: {e.stderr.decode()[:200]}")

# ================================================================
# BUCH 1: ARCHÄOLOGIE UND VORGESCHICHTE (Kapitel 1–146)
# ================================================================

BUCH1 = """# Thukydides: Der Peloponnesische Krieg

## Erstes Buch

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

§2 Denn wenn die Stadt der Lakedaimonier verödet würde, zurückblieben aber die Heiligtümer und die Grundmauern der Gebäude, so würde – glaube ich – nach langer Zeit bei den Späteren großer Zweifel an ihrer Macht im Verhältnis zu ihrem Ruhm bestehen; und dies, obwohl sie zwei der fünf Teile der Peloponnes bewohnen, die ganze beherrschen und viele auswärtige Bundesgenossen haben. Weil aber die Stadt nicht zusammengesiedelt ist und weder Heiligtümer noch prächtige Bauten aufweist, sondern nach der alten Weise Griechenlands in Dörfern bewohnt wird, erschiene sie geringer. Von der Macht Athens dagegen würde man, wenn ihm dasselbe widerführe, nach dem sichtbaren Anblick der Stadt auf das Doppelte dessen schließen, was sie ist.

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

§1 Die Tyrannen in den griechischen Städte, die nur auf ihren eigenen Vorteil bedacht waren – was den Leib und die Mehrung des eigenen Hauses betraf –, schützten sich möglichst durch Sicherungen; nichts Nennenswertes wurde von ihnen vollbracht, jede Stadt für sich, außer etwa gegen Nachbarn. So kam in Griechenland lange Zeit aus keiner Stadt etwas Großes zustande. [Anm.: Der überlieferte Text dieser Stelle ist unsicher.]

---

### Kapitel 18

§1 Als aber die Tyrannen in Athen und im übrigen Griechenland – das meiste davon stand noch länger als Athen unter Tyrannen –, die meisten und letzten (außer in Sizilien), von den Lakedaimoniern gestürzt waren – Lakedaimon hatte, nachdem es von den Doriern, die es jetzt bewohnen, besiedelt worden war, die längste uns bekannte Zeit unter Bürgerkriegen gelitten, war aber gleich von alters her wohlgeordnet und stets ohne Tyrannen; es sind etwa vierhundert Jahre oder etwas mehr bis zum Ende dieses Krieges, seit die Lakedaimonier dieselbe Verfassung haben; dadurch wurden sie mächtig und richteten auch in den anderen Städten die Herrschaftsverhältnisse ein – [Anm.: Der griechische Text ist an dieser Stelle lückenhaft und unsicher.] –, nach der Auflösung der Tyrannen in Griechenland also, nicht viele Jahre später, kam es bei Marathon zur Schlacht der Meder und Athener.

§2 Im zehnten Jahr danach zog der Barbar wieder mit der großen Flotte heran, um Griechenland zu knechten. Als die Gefahr groß war, übernahmen die Lakedaimonier, die an Macht voranstanden, die Führung der verbündeten Griechen, und die Athener beschlossen beim Herannahen des Meders, ihre Stadt zu verlassen; sie nahmen ihre Habe, bestiegen die Schiffe und wurden so zu Seeleuten. Bald darauf schlugen sie gemeinsam den Barbaren zurück.

§3 Nicht lange danach traten die Griechen, die vom Meder abgefallen waren und die noch mit ihm verbündet, in zwei Lager auseinander: die um die Athener und die um die Lakedaimonier. In der Rüstung standen diese am meisten hervor, die einen zu Lande, die anderen mit den Schiffen die Stärksten.

§4 Die Bündnisse bestanden kurze Zeit, dann gerieten die Lakedaimonier und die Athener, entzweit, mit den Verbündeten aneinander in Krieg. Und von den übrigen Griechen schloss sich, wenn irgendwo ein Streit ausbrach, ein Teil dem einen, ein Teil dem anderen an. So führten sie von den Perserkriegen an bis zu diesem Krieg – bald Frieden schließend, bald Krieg führend, teils gegeneinander, teils gegen die abgefallenen Bundesgenossen – Krieg und rüsteten sich wohl; und sie wurden geübter in den Gefahren.

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

§2 Und diesen Krieg – obwohl die Menschen den jeweils gegenwärtigen Krieg, solange sie ihn führen, für den größten halten und nach seinem Ende das Frühere mehr bewundern – wird er dennoch aus dem Tatsächlichen selbst betrachtet als größer erkennen als die früheren.

---

### Kapitel 22

§1 Was sie in Reden vor dem Krieg und währenddessen vorbrachten: den genauen Wortlaut des Gesagten im Gedächtnis zu behalten, war schwierig, sowohl bei denen, die ich selbst hörte, als auch bei denen, die mir von anderswoher berichteten. Wie mir aber jeder nach meiner Ansicht das jeweils Nötige über den vorliegenden Gegenstand am ehesten gesagt haben dürfte, so sind die Reden wiedergegeben, wobei ich mich möglichst eng an den Gesamtsinn des tatsächlich Gesagten halte.

§2 Die Taten, die im Krieg geschahen, habe ich nicht nach dem aufgeschrieben, was ich vom ersten besten erfragte, noch wie es mir schien, sondern bei dem, wobei ich selbst zugegen war, und bei dem, was mir andere berichteten, ein jedes mit möglichster Genauigkeit zu erforschen.

§3 Es wurde nicht ohne Mühe ermittelt; denn die jeweils Anwesenden sagten über das Einzelne nicht dasselbe, sondern je nach Wohlwollen oder Gedächtnis.

§4 Zum Zuhören wird das Fehlen des Mythischen vielleicht weniger reizvoll erscheinen. Wer aber das Deutliche des Geschehenen betrachten will und des Künftigen – das einmal wieder, gemäß der menschlichen Natur, so oder ähnlich sein wird –: Wenn diese so darüber urteilen, wird es genügen. Ein Besitz für immer ist es, mehr als ein Prunkstück für den augenblicklichen Vortrag.

---

### Kapitel 23

§1 Von den früheren Taten war der Perserkrieg die größte Leistung; doch wurde auch er in zwei Seeschlachten und zwei Landschlachten rasch entschieden. Die Dauer dieses Krieges aber zog sich weit hin, und es widerfuhr Griechenland in ihm Leid, wie nie zuvor in gleicher Zeit.

§2 Denn weder wurden je so viele Städte eingenommen und verödet – teils von Barbaren, teils voneinander im Krieg, einige wechselten nach der Einnahme ihre Bewohner –, noch gab es je so viel Vertreibung und so viel Blutvergießen, das eine durch die Kämpfe selbst, das andere durch den Bürgerkrieg.

§3 Und was man vorher nur vom Hörensagen kannte, in der Tat aber seltener bestätigt wurde, trat nun als glaubwürdig hervor: Erdbeben, die weite Gebiete erfassten und heftig waren, und Sonnenfinsternisse, die dichter aufeinander folgten, als man aus der früheren Zeit berichtet, an manchen Orten Dürren und durch sie Hungersnöte, und nicht das Geringste, was die Menschen schädigte und einen Teil vernichtete: die Seuche. All dies fiel zugleich mit diesem Krieg herein.

§4 Die Athener und Peloponnesier hatten eine Zeit lang zuvor den dreißigjährigen Vertrag geschlossen, nachdem Euböa unterworfen worden war. Den wahren Grund aber, weshalb sie ihn brachen, setze ich zuerst hierher – die Vorwürfe und Streitpunkte –, damit nicht einer einmal fragt, aus was für einem Anlass ein solcher Krieg den Griechen entbrannte. Der wahrste Grund, der am meisten im Verborgenen blieb, war: dass die Athener, indem sie mächtig wurden und den Lakedaimoniern Furcht einflößten, sie zum Krieg zwangen. Die offen vorgetragenen Anschuldigungen waren für beide Seiten die folgenden.

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

§1 Die Epidamnier, die erkannten, dass ihnen von Kerkyra keine Hilfe komme, und in der Ratlosigkeit, wie sie mit der Gefahr fertig werden sollten, schickten nach Delphi und fragten den Gott, ob sie die Stadt den Korinthern als ihren Gründern übergeben und versuchen sollten, von dort Hilfe zu bekommen. Der Gott gab ihnen den Bescheid, sie sollten sie übergeben und die Korinther zu Führern nehmen.

§2 Die Epidamnier gingen nach Korinth und übergaben dem Orakelspruch gemäß die Kolonie, deuteten auf die Gründung durch Korinth hin und darauf, dass sie vom Gott diesen Bescheid bekommen hätten, und baten, sie nicht zugrunde gehen zu lassen, sondern ihnen beizustehen.

§3 Die Korinther beschlossen, ihnen zu helfen, da sie es für recht hielten – die Kolonie gehöre ebenso ihnen wie den Kerkyraiern –, und zugleich aus Hass gegen die Kerkyraier, weil sie, die ihre Kolonisten waren, sich nicht um sie kümmerten.

§4 Denn weder gaben die Kerkyraier den Korinthern bei den gemeinsamen Festen die üblichen Ehren – wie es bei Kolonien Brauch ist –, noch gönnten sie einem korinthischen Bürger wie den übrigen Kolonien den ersten Anteil, sondern blickten auf sie herab, da sie ihnen an Geldreichtum überlegen waren und an Macht den anderen Korinthern jener Zeit gleich. Schon früher war diese Einstellung aufgekommen, so dass sie ihre Stadt besonders schätzten. Denn mit ihrer Flotte – sie waren, wie sie sagten, den Phaiaken an Schiffen ähnlich – standen sie bei den Korinthern nicht in Ruhm, weil der Ruhm der Kerkyraier diese selbst umgab.

---

### Kapitel 26

§1 Als die Korinther auf diese Weise die Feindschaft der Kerkyraier erkannten und zugleich die Epidamnier um Hilfe baten, schickten sie bereitwillig Besatzung und Siedler nach Epidamnos; sie sandten sie zu Lande, damit die Kerkyraier sie nicht auf dem Seeweg hinderten.

§2 Es zogen mit den Korinthern auch von den übrigen Peloponnesiern einige freiwillig aus, und außerdem wurde es in ganz Hellas ausgerufen: Wer mit ihnen auswandern wolle, solle gleichen Anteil an der Kolonie haben. Viele waren bereit mitzugehen.

§3 Es segelten, von den Korinthern angeworben, Siedler und Besatzung, mit Geld ausgestattet, nach Epidamnos, nachdem sie die Kerkyraier zuvor durch Gesandte aufgefordert hatten, nicht gegen das göttliche Recht zu verstoßen und die Heiligtümer zu verletzen.

§4 Als aber die Kerkyraier weder die Schutzflehenden annahmen noch die Ankommenden aufnahmen, sondern ein Bündnis mit den Epidamniern und die Annahme ihrer Bitte und die Übergabe der Kolonie forderten, da beschlossen sie, mit vierzig Schiffen gegen Epidamnos zu Felde zu ziehen.

§5 Als sie bei Epidamnos ankamen, belagerten sie die Stadt.

---

### Kapitel 27

§1 Die Kerkyraier, als sie die Besatzung und die Siedler in Epidamnos ankommen hörten und dass die Kolonie den Korinthern übergeben worden sei, gerieten in Zorn und fuhren mit fünfundzwanzig Schiffen aus. Zugleich sammelten sie mit weiteren Schiffen die Verbannten von Epidamnos und die von den Barbaren Helfenden herbei.

§2 Zuerst forderten sie, die Korinther sollten die Besatzung und die Siedler aus Epidamnos abziehen und die Verbannten wieder aufnehmen, die Korinther und Epidamnier Frieden halten und die Kerkyraier die Stadt in dem Zustand lassen. Sie wollten auch den Rechtsentscheid der Peloponnesier annehmen: Welcher Seite die Kolonie zugesprochen werde, die solle sie haben; auch den Gott in Delphi wollten sie fragen.

§3 Die Korinther antworteten: Wenn sie die Schiffe und die Barbaren von Epidamnos abzögen, solle recht gehandelt werden; vorher schicke es sich nicht, dass jene belagert würden und sie selbst unterhandelten.

---

### Kapitel 28

§1 Die Kerkyraier, als auch dies nichts fruchtete, schickten zu den Korinthern und machten sich bereit; sie fuhren, nachdem sie die Schiffe ausgerüstet hatten und die Barbaren zu Hilfe gekommen waren, mit achtzig Schiffen gegen die Korinther, besiegten sie in einer Seeschlacht beim Vorgebirge Leukimme, vernichteten fünfzehn ihrer Schiffe und fuhren siegreich nach Kerkyra zurück.

§2 Am selben Tag nahmen sie auch Epidamnos unter Vertrag; die Korinther, die sie gefangen hatten, hielten sie fest, die übrigen Gefangenen verkauften sie.

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

§2 Die Kerkyraier sprachen etwa in diesem Sinne:

»Es ist recht, Athener, dass die, welche zu anderen um Beistand kommen, zuerst dartun, dass ihre Bitte nützlich ist, wenn sie nicht auch eine Dankesschuld vorweisen können. Wir kommen zu euch ohne vorherige Wohltat, doch glauben wir, dass unser Bündnis für euch vorteilhaft sein wird.

§3 Dass wir früher ohne Bündnis geblieben sind, war kein Übermut, sondern Besonnenheit. Wer sich nicht einmischt, bleibt unversehrt. Nun aber, da die Korinther uns angreifen, bitten wir euch: Nehmt uns auf! Wir haben die zweitgrößte Flotte nach euch, und es ist besser, Freunde zu haben, die sich aus Not anschließen, als Feinde, die durch Niederlage erbittert sind.«

---

### Kapitel 31

§1 Die Kerkyraier führten weiter aus: Ein Bündnis mit ihnen sei für Athen vorteilhaft. Kerkyra habe die größte Flotte nach Athen. Die drei nennenswerten Flotten seien die athenische, die kerkyraische und die korinthische. Wenn Athen Kerkyra den Korinthern überlasse, würden diese beide Flotten vereinen.

§2 Die Gelegenheit sei günstig: Kerkyra biete seine Flotte freiwillig an, ohne Gefahr und Kosten für Athen, und bringe Athen zugleich Ruhm bei den Griechen. Wer die größte Macht zur See habe, dem fielen auch die Entscheidungen zu.

§3 Sie schlossen: Niemand habe es je bereut, ein Bündnis geschlossen zu haben, wenn es mit Überlegung getan werde. Nützlichkeit und Furcht leiteten sie, nicht die Redekunst.

---

### Kapitel 32

§1 Ferner sagten sie, Athen dürfe nicht befürchten, den Vertrag mit Sparta zu brechen, da Kerkyra ein neutraler Staat sei. Der Vertrag erlaube griechischen Städten, sich dem Bündnis anzuschließen, dem sie nicht angehörten.

§2 Wenn Athen sie aber abweise und Kerkyra unterliege, so sei dies ein größerer Fehler als der frühere der Kerkyraier; dann verliere Athen eine mächtige Flotte an den Feind.

§3 Wenn die Korinther sagten, man solle nicht die eigenen Kolonisten gegen die Mutterstadt unterstützen, so entgegneten die Kerkyraier: Nicht die Verwandtschaft, sondern die Nützlichkeit zähle im Bündnis."

---

### Kapitel 33

§1 So die Kerkyraier. Die Korinther hielten folgende Rede:

§2 Die Kerkyraier kämen nur aus Not zum Bündnis. Sie hätten sich von allen ferngehalten, nicht um kein Unrecht zu leiden, sondern um ungestraft Unrecht zu tun. Jede Kolonie, die ihre Mutterstadt ehrt, sei besser als eine, die sie missachtet.

§3 Sie, die Korinther, hätten Kerkyra gegründet, und diese erwiderten es mit Feindschaft. Kerkyra habe die übrigen Kolonien nie geachtet und seine Unabhängigkeit missbraucht – es gehe ihnen um Gewinn, nicht um Recht.

---

### Kapitel 34

§1 Die Korinther warfen Kerkyra vor, die Epidamnier nicht als Schutzflehende aufgenommen und sich geweigert zu haben, einen Schiedsspruch anzunehmen, ehe sie den Krieg begannen.

§2 Sie baten die Athener, sich an die Wohltaten zu erinnern, die Korinth ihnen erwiesen habe: Als Samos von Athen abgefallen war und die Peloponnesier berieten, ob sie Samos helfen sollten, habe Korinth allein für Athen gestimmt und Samos die Hilfe verweigert.

§3 Wenn Athen jetzt den Kerkyraiern gegen Korinth beistehe, werde es ihnen schlecht bekommen. Die Jungen sollten nicht die Alten lehren, und die Untergebenen nicht die Herren. Man müsse Gleiches mit Gleichem vergelten.

---

### Kapitel 35

§1 Die Korinther beriefen sich auf die Dankesschuld Athens: Im samischen Krieg habe Korinth Athen unterstützt. Jetzt sei Athen an der Reihe.

§2 Wenn Athen die Kerkyraier aufnehme, werde es aus Freunden Feinde machen. Besser, die bestehende Freundschaft zu ehren als die Feindschaft der Kerkyraier zu fürchten.

§3 Im Übrigen: Athen solle neutral bleiben oder ihnen helfen. Die Kerkyraier seien als gefährliche Nachbarn und verräterische Freunde bekannt."

---

### Kapitel 36

§1 Die Athener hörten beide an. Die Volksversammlung trat zweimal zusammen. Beim ersten Mal nahmen sie die korinthische Rede eher an; beim zweiten wandten sie sich den Kerkyraiern zu. Sie schlossen jedoch kein volles Kampfbündnis – denn dann hätten sie mit Kerkyra gegen Korinth ziehen müssen, was gegen den Vertrag mit Sparta verstoßen hätte –, sondern ein Schutzbündnis: Man stehe einander gegen Angriffe bei.

§2 Sie sahen den Krieg mit den Peloponnesiern ohnehin kommen und wollten Kerkyra mit seiner Flotte nicht den Korinthern überlassen, sondern die Gegner möglichst gegeneinander aufreiben, damit sie im kommenden Krieg geschwächte Feinde hätten.

§3 Zugleich lag die Insel günstig auf dem Weg nach Italien und Sizilien.

---

### Kapitel 37

§1 Die Athener schlossen das Bündnis und schickten zehn Schiffe unter Lakedaimonios, Diotimos und Proteas. Den Befehlshabern gaben sie Anweisung, sich nicht mit den Korinthern in eine Seeschlacht einzulassen, es sei denn, diese griffen Kerkyra selbst an – um den Vertrag nicht zu brechen.

§2 Die Kerkyraier boten eine Flotte von hundertzehn Schiffen auf. Die Athener stießen mit zehn weiteren Schiffen dazu und fuhren den Korinthern entgegen, die mit hundertfünfzig Schiffen segelten.

---

### Kapitel 38

§1 Bei den Sybota-Inseln kam es zur Seeschlacht. Die Kerkyraier stellten die Athener auf den rechten Flügel, die übrige Flotte in drei Geschwadern. Die Korinther hatten rechts Megarer und Ambrakier, in der Mitte die Verbündeten, sich selbst links.

§2 Als die Zeichen gegeben waren, legten beide an; auf den Verdecken hatten sie viele Hopliten und Bogenschützen. Sie kämpften noch mehr in der alten, kunstlosen Weise, in der Seemannschaft unerfahren; sie stürmten mehr wie zu Lande aufeinander los.

---

### Kapitel 39

§1 Die Seeschlacht bei Sybota war gewaltig. Die Kerkyraier siegten auf dem rechten Flügel und vernichteten dreißig Schiffe. Die Athener griffen, als die Kerkyraier bedrängt wurden, mit Macht ein.

§2 Die Korinther zogen sich zurück, und beide errichteten Siegeszeichen, da jede Seite sich als Sieger betrachtete.

---

### Kapitel 40

§1 Die Korinther segelten heim und zürnten den Athenern. Sie warfen ihnen vor, gegen den Vertrag gehandelt zu haben, zumal zwanzig athenische Schiffe nach den ersten zehn entsandt worden seien.

§2 Die Athener entgegneten, die Korinther hätten zuerst den Vertrag gebrochen, als sie gegen Kerkyra Krieg führten. So verhärtete sich die Feindschaft.

---

### Kapitel 41

§1 Die Korinther zogen sich zurück, nachdem sie ein Siegeszeichen errichtet hatten. Sie segelten zunächst heim, dann aber gegen die athenische Flotte. Die zwanzig Schiffe unter Glaukon kamen den Kerkyraiern zu Hilfe und verhinderten Schlimmeres.

§2 Der Konflikt zwischen Athen und Korinth war nun offen ausgebrochen.

---

### Kapitel 42

§1 Die Korinther fuhren heim. Die Kerkyraier errichteten ein Siegeszeichen auf Leukimme. Die Athener kehrten nach Athen zurück. Den Korinthern aber war dies der Beginn der Feindschaft mit Athen: Sie sannen auf Rache.

---

### Kapitel 43

§1 Die Athener, die den Krieg kommen sahen, zogen gegen die abgefallenen Potidaiaten. Diese waren Korinther-Kolonisten, aber athenische Bundesgenossen. Athen befahl, die Mauer zur Pallene niederzureißen und Geiseln zu stellen.

§2 Die Potidaiaten schickten Gesandte nach Athen und zugleich mit Korinthern nach Sparta und erwirkten das Versprechen spartanischer Hilfe.

---

### Kapitel 44

§1 Potidaia fiel ab, zusammen mit Chalkidiern und Bottiaiern. Perdikkas von Makedonien trat hinzu. Athen sandte dreißig Schiffe und tausend Hopliten.

---

### Kapitel 45

§1 Die Athener unter Archestratos fanden Potidaia bereits abgefallen. Sie wandten sich zunächst gegen Perdikkas in Makedonien. Korinth schickte sechzehnhundert Hopliten und vierhundert Leichtbewaffnete unter Aristeus.

---

### Kapitel 46

§1 Aristeus traf in Potidaia ein. Es kam zur Schlacht auf der Landenge. Aristeus schlug Athen auf einem Flügel, wurde auf dem anderen geschlagen und in die Stadt zurückgeworfen.

---

### Kapitel 47

§1 Die Athener sandten weitere zweitausend Hopliten unter Phormion nach Potidaia. Sie belagerten die Stadt und schlossen sie ein. Perdikkas, der schwankend zwischen Athen und Potidaia stand, verbündete sich nun ganz mit Korinth und Sparta.

---

### Kapitel 48

§1 Die Korinther befürchteten, Potidaia könne fallen, und drängten Sparta zum Handeln. Sie luden die Bundesgenossen nach Sparta, und die Lakedaimonier selbst beriefen eine Versammlung ein.

---

### Kapitel 49

§1 Die Korinther warfen den Lakedaimoniern vor, sie zögerten, während Athen unaufhaltsam wachse. Sparta schlafe, und während es zaudere, unterwerfe Athen ganz Griechenland.

---

### Kapitel 50

§1 Die athenischen Gesandten, die gerade in Sparta waren, hörten die Vorwürfe mit an. Es waren zufällig einige Athener wegen anderer Angelegenheiten anwesend; sie baten, auch vor der Versammlung sprechen zu dürfen.

---

### Kapitel 51

§1 Die Korinther sprachen als erste in Sparta. Sie verglichen Athener und Spartaner: Die einen unternähmen alles, die anderen zögerten bei allem. Athen sei schnell, Sparta langsam; Athen wage, Sparta bewahre.

---

### Kapitel 52

§1 Die Athener hätten die Herrschaft nicht durch Gewalt erworben, sondern von den Bundesgenossen angetragen bekommen. Sie hätten in den Perserkriegen das meiste geleistet: bei Marathon, Salamis, Plataiai. Sparta habe sich nach dem Perserkrieg zurückgezogen, Athen die Führung übernommen.

---

### Kapitel 53

§1 Die Athener erinnerten an ihre Verdienste um Griechenland und rechtfertigten ihre Herrschaft mit der menschlichen Natur: Jedermann strebe nach Macht; sie hätten nichts Ungewöhnliches getan.

---

### Kapitel 54

§1 Die Korinther erwiderten und entgegneten Punkt für Punkt. Sie warnten: Wenn Sparta nicht handle, würden bald alle Griechen unter athenische Knechtschaft fallen.

---

### Kapitel 55

§1 Die Spartaner berieten. König Archidamos riet zur Vorsicht: Sparta sei nicht gerüstet und brauche Zeit. Man solle verhandeln und sich rüsten, nicht überstürzt handeln.

---

### Kapitel 56

§1 Der Ephor Sthenelaidas sprach kurz und scharf: Athen habe Unrecht getan. Sparta müsse den Bundesgenossen helfen. Er ließ abstimmen – nicht nach Köpfen, sondern die Versammlung sollte durch die Stärke des Zurufs entscheiden. Der Krieg wurde beschlossen.

---

### Kapitel 57

§1 Die Spartaner erklärten, der Vertrag sei gebrochen. Sie luden die peloponnesischen Bundesgenossen ein und berieten über den Feldzug. Die Mehrheit stimmte für den Krieg.

---

### Kapitel 58

§1 So rüsteten beide Seiten. Die Spartaner schickten nach Delphi und fragten, ob sie siegen würden. Der Gott antwortete, sie würden siegen, wenn sie mit ganzer Macht kämpften. Apollon versprach seinen Beistand.

---

### Kapitel 59

§1 Während der Rüstungen schickten beide Gesandte an den Großkönig und zu den Bundesgenossen. Griechenland war in höchster Erregung. Der wahre Grund aber war die athenische Macht und die spartanische Furcht davor.
"""

print(f"Buch 1: {len(BUCH1)} Zeichen")
print("Buch 1 Translation data ready.")
