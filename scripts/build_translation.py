#!/usr/bin/env python3
"""Build a translated book edition (de/en/uk/he) from the fragment files in work/.

Fragments: work/<lang>/ch_NNN.md, written by the translation subagents:

    # 1.<chapter>
    ## 1.<chapter>.<section>
    <translated paragraph, possibly with inline [Note: ...] labels>
    !! FLAG 1.<chapter>.<section>: <coordinator note>   (excluded from output)

The build mirrors docs/de/book1.html: same section IDs, chapter headings,
front matter with the translation principles, and <hr> separators.
"""
import argparse
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NS = {'t': 'http://www.tei-c.org/ns/1.0'}
NOTE_RE = re.compile(r'\[(Note|Прим\.|הערה|Anm\.): [^\]]*\]')


def html_escape(text):
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


BOOK_TITLES = {
    1: {
        'de': 'Buch 1', 'de_h2': 'Erstes Buch',
        'en': 'Book 1', 'en_h2': 'Book One',
        'uk': 'Книга 1', 'uk_h2': 'Перша книга',
        'he': 'ספר 1', 'he_h2': 'הספר הראשון',
    },
    2: {
        'de': 'Buch 2', 'de_h2': 'Zweites Buch',
        'en': 'Book 2', 'en_h2': 'Book Two',
        'uk': 'Книга 2', 'uk_h2': 'Друга книга',
        'he': 'ספר 2', 'he_h2': 'הספר השני',
    },
}

LANG_FRAMES = {
    'de': {
        'title': 'Thukydides: Der Peloponnesische Krieg',
        'nav': 'Alle Sprachen und Status',
        'nav_aria': 'Ausgaben',
        'grc': 'Ancient Greek — Original',
        'h1': 'Thukydides: Der Peloponnesische Krieg',
        'principles_h': 'Übersetzungsgrundsätze',
        'principles_intro': 'Sinngetreu und gut lesbar übersetzen, nicht Wort für Wort, und ausschließlich aus dem Altgriechischen. Braun, Hobbes, Crawley und andere Übersetzungen dürfen höchstens als Verständnishilfe dienen; sie sind weder Ausgangstext noch zu übernehmende Übersetzung.',
        'sprache': '<strong>Sprache.</strong> Die Bedeutung des griechischen Textes muss vollständig erhalten bleiben. Die deutsche Sprache soll dabei so modern und natürlich wie möglich klingen, wie ein heutiger Autor denselben Inhalt formulieren würde. Der griechische Satzbau ist kein Vorbild. Entscheidend sind die Verständlichkeit des Zusammenhangs und die Genauigkeit der Aussage; feste Vorgaben zur Satzlänge oder zu einzelnen Satzformen ersetzen dieses Urteil nicht.',
        'rules': [
            'Einheitliche Entsprechung je Bedeutung. Nicht ein deutsches Wort für jedes Vorkommen erzwingen. αἰτία kann Vorwurf, Ursache, Schuld oder Verantwortung bedeuten; eine kausale Übersetzung darf nicht ausgeschlossen werden, wenn der griechische Sinn sie verlangt.',
            'Nichts hinzufügen oder steigern. Keine Erklärungen, Bilder, Behauptungen oder Hervorhebungen ergänzen, die im Griechischen fehlen.',
            'Nicht abschwächen. Die Härte von Aussagen und politischem Vokabular bewahren; δουλεία bleibt in dieser Bedeutung Knechtschaft.',
            'Anmerkungen bei echten Zweifeln. Kurze Anmerkungen bei textkritischer Unsicherheit, echten Deutungsfragen oder einem bedeutsamen Bedeutungswechsel eines Schlüsselbegriffs. Nicht auf beschädigten oder verderbten Text beschränken. Deutsch: `[Anm.: …]`; andere Sprachen verwenden eine entsprechende Kennzeichnung.',
            'Mehrdeutigkeiten bewahren. Lässt der griechische Text mehrere Lesarten zu, diese Offenheit möglichst erhalten. Unvermeidliche Entscheidungen kurz erläutern.',
            'Besondere Sorgfalt bei Reden und indirekter Rede. Sprecher, Adressat, Argumentation, wiedergegebene Sichtweise, Bedingungen, Verneinung, Modalität und Zeitverhältnisse erhalten. Berichtete Behauptungen nicht zu Aussagen des Erzählers machen.',
        ],
        'doc_p': 'Das vollständige Glossar und die Arbeitsweise stehen in der <a href="https://github.com/kp-greg-smith/thukydides-geschichte/blob/main/README_DE.md">deutschen Projektdokumentation</a>.',
        'chapter': 'Kapitel {n}',
        'toolbar': 'de',
    },
    'en': {
        'title': 'Thucydides: The Peloponnesian War',
        'nav': 'All languages and status',
        'grc': 'Ancient Greek — Original',
        'h1': 'Thucydides: The Peloponnesian War',
        'principles_h': 'Translation principles',
        'principles_intro': 'Translate faithfully and readably, not word for word, and directly from the Ancient Greek. Hobbes, Crawley, Jowett and other translations may only help with understanding; they are neither the source text nor a translation to be taken over.',
        'rules': [
            'A stable equivalent for each meaning. Do not force one word for every occurrence. αἰτία may mean accusation, cause, blame, or responsibility; a causal rendering is not excluded where the Greek sense requires it.',
            'Nothing added, nothing exaggerated. No explanations, imagery, claims, or emphasis absent from the Greek.',
            'Nothing softened. The force of harsh statements and of political vocabulary is preserved; δουλεία remains <em>slavery</em> in that sense.',
            'Notes for genuine uncertainty. Brief notes for textual uncertainty, genuine interpretive questions, or a significant change in a key term’s sense. Notes are not limited to damaged or corrupt text.',
            'Ambiguity preserved. Where the Greek allows more than one reading, that openness is kept where possible; unavoidable choices are explained in a brief note.',
            'Extra care with speeches and indirect speech. Speaker, addressee, argument, reported viewpoint, conditions, negation, modality, and temporal relations are preserved. Reported claims do not become the narrator’s assertions.',
        ],
        'doc_link': ('https://github.com/kp-greg-smith/thukydides-geschichte/blob/main/README.md',
                     'English project documentation on glossary and workflow'),
        'chapter': 'Chapter {n}',
        'doc_lang': 'en',
    },
    'uk': {
        'title': 'Фукідід: Пелопоннеська війна',
        'nav': 'Усі мови та статус',
        'grc': 'Ancient Greek — Original',
        'h1': 'Фукідід: Пелопоннеська війна',
        'h2': 'Перша книга',
        'principles_h': 'Принципи перекладу',
        'principles_intro': 'Перекладати точно і читацько, не слово в слово, і лише з давньогрецької. Переклади Хоббса, Кроулі, Джоветта та інші можуть слугувати лише для розуміння; вони не є ані вихідним текстом, ані перекладом для відтворення.',
        'rules': [
            'Стала відповідність для кожного значення. Не нав’язувати одне слово на кожне вживання. αἰτία може означати обвинувачення, причину, вину чи відповідальність; каузальний переклад не виключається, якщо грецький зміст його вимагає.',
            'Нічого не додано, нічого не перебільшено. Жодних пояснень, образів, тверджень чи акцентів, яких немає в грецькому тексті.',
            'Нічого не пом’якшено. Зберігається сила гострих висловлювань і політичної лексики; δουλεία в цьому значенні лишається <em>рабством</em>.',
            'Примітки лише при справжній невизначеності. Короткі примітки при текстологічній невизначеності, справжніх інтерпретаційних питаннях чи істотній зміні значення ключового терміна. Примітки не обмежено пошкодженим текстом.',
            'Двозначність збережено. Якщо грецький текст допускає кілька читань, ця відкритість зберігається настільки, наскільки можливо; неминучі рішення коротко пояснюються в примітці.',
            'Особлива обережність із промовами та непрямою мовою. Зберігаються мовець, адресат, аргументація, передана позиція, умови, заперечення, модальність і часові відношення. Передані твердження не стають твердженнями оповідача.',
        ],
        'doc_link': ('https://github.com/kp-greg-smith/thukydides-geschichte/blob/main/README_UK.md',
                     'українська проектна документація про глосарій і порядок роботи'),
        'chapter': 'Розділ {n}',
        'doc_lang': 'uk',
    },
    'he': {
        'title': 'תוקידידס: המלחמה הפלופונסית',
        'nav': 'כל השפות והמצב',
        'grc': 'Ancient Greek — Original',
        'h1': 'תוקידידס: המלחמה הפלופונסית',
        'h2': 'הספר הראשון',
        'principles_h': 'עקרונות התרגום',
        'principles_intro': 'לתרגם בנאמנות ובשטף קריא, לא מילה במילה, ורק מן היוונית העתיקה. תרגומי הובס, קרולי, ג׳ווט ואחרים יכולים לשמש רק כעזרה להבנה; הם אינם המקור ואינם נלקחים כתרגום.',
        'rules': [
            'מקבילה קבועה לכל מובן. לא לכפות מילה אחת על כל הופעה. αἰτία יכול לומר האשמה, סיבה, אשם ואחריות; תרגום סיבתי אינו נפסל כשהמובן היווני דורש אותו.',
            'לא להוסיף ולא להגזים. בלי הסברים, דימויים, טענות או הדגשות שאינם ביוונית.',
            'לא לרכך. נשמרת חריפות הדברים הקשים ושל האוצר הפוליטי; δουλεία במובן זה נשאר <em>עבדות</em>.',
            'הערות רק בספק אמיתי. הערות קצרות לחוסר ודאות טקסטואלית, שאלות פרשנות אמיתיות או שינוי משמעותי במובנו של מונח מפתח. ההערות אינן מוגבלות לטקסט פגום.',
            'דו משמעות נשמרת. היכן שהיוונית מאפשרת יותר מקריאה אחת, הפתיחות נשמרת ככל האפשר; הכרעות בלתי נמנעות מתוארות בקצרה בהערה.',
            'זהירות יתרה בנאומים ובדיבור עקיף. נשמרים הדובר, הנמען, הטיעון, העמדה המדווחת, התנאים, השלילה, המודאליות ויחסי הזמן. טענות מדווחות אינן הופכות לטענות המספר.',
        ],
        'doc_link': ('https://github.com/kp-greg-smith/thukydides-geschichte/blob/main/README_HE.md',
                     'התיעוד העברי של המילון וסדר העבודה'),
        'chapter': 'פרק {n}',
        'doc_lang': 'he',
    },
}


def parse_fragments(lang_dir, book):
    chapters = {}
    for path in sorted(lang_dir.glob('ch_*.md')):
        m = re.fullmatch(r'ch_(\d+)\.md', path.name)
        if not m:
            continue
        c = int(m.group(1))
        current = None
        sections = []
        buf = []
        for raw in path.read_text().splitlines():
            line = raw.strip()
            if line.lstrip('`').startswith('!!'):   # coordinator flag (allow stray markdown backticks), not part of text
                continue
            m2 = re.fullmatch(rf'# {book}\.(\d+)', line)
            if m2:
                if int(m2.group(1)) != c:
                    raise ValueError(f'{path}: chapter header {line} does not match file name')
                continue
            m3 = re.fullmatch(rf'## {book}\.(\d+)\.(\d+)', line)
            if m3:
                if current is not None:
                    sections.append((current, ' '.join(buf).strip()))
                current = (c, int(m3.group(2)))
                buf = []
                continue
            if line:
                buf.append(line)
        if current is not None:
            sections.append((current, ' '.join(buf).strip()))
        seen = {}
        for key, text in sections:
            if not text:
                raise ValueError(f'{path}: section {key} has empty translation')
            if key in seen:
                raise ValueError(f'{path}: duplicate section {key}')
            seen[key] = text
        chapters[c] = seen
    return chapters


def expected_structure(book):
    source = ET.parse(ROOT / 'docs/grc/source.xml')
    greek_book = source.find(f'.//t:div[@subtype="book"][@n="{book}"]', NS)
    expected = {}
    for chapter in greek_book.findall('t:div[@subtype="chapter"]', NS):
        c = int(chapter.attrib['n'])
        expected[c] = [int(s.attrib['n']) for s in chapter.findall('t:div[@subtype="section"]', NS)]
    return expected


def render(lang, book, chapters):
    f = LANG_FRAMES[lang]
    bt = BOOK_TITLES[book]
    out = []
    rtl = ' dir="rtl"' if lang == 'he' else ''
    out.append('<!DOCTYPE html>')
    out.append(f'<html lang="{lang}"{rtl}>')
    out.append('<head>')
    out.append('<meta charset="UTF-8">')
    out.append('<meta name="viewport" content="width=device-width,initial-scale=1">')
    out.append(f'<title>{html_escape(f["title"] + " — " + bt[lang])}</title>')
    out.append('<script src="../assets/theme.js"></script>')
    out.append('<link rel="stylesheet" href="../assets/reader.css">')
    out.append('</head>')
    out.append('<body>')
    out.append('<div class="reader-toolbar" hidden>')
    if f.get('toolbar') == 'de':
        out.append('<label for="font-select">Schrift</label>')
        out.append('<select id="font-select">')
        out.append('  <optgroup label="Historisch">')
        out.append('    <option value="unifrakturmaguntia">UnifrakturMaguntia</option>')
        out.append('    <option value="pirataone">Pirata One</option>')
        out.append('    <option value="medievalsharp">MedievalSharp</option>')
        out.append('    <option value="almendra" selected>Almendra</option>')
        out.append('  </optgroup>')
        out.append('  <optgroup label="Gut lesbar">')
        out.append('    <option value="ebgaramond">EB Garamond</option>')
        out.append('    <option value="crimsontext">Crimson Text</option>')
        out.append('    <option value="sourceserif4">Source Serif 4</option>')
        out.append('    <option value="sourcesans3">Source Sans 3</option>')
        out.append('  </optgroup>')
        out.append('</select>')
    else:
        out.append('<label for="font-select">Font</label>')
        out.append('<select id="font-select">')
        out.append('  <optgroup label="Reading">')
        out.append('    <option value="ebgaramond">EB Garamond</option>')
        out.append('    <option value="crimsontext">Crimson Text</option>')
        out.append('    <option value="sourceserif4" selected>Source Serif 4</option>')
        out.append('    <option value="sourcesans3">Source Sans 3</option>')
        out.append('  </optgroup>')
        out.append('</select>')
    out.append('<button id="theme-toggle" type="button" aria-pressed="false">Dark Mode</button></div>')
    out.append('')
    out.append(f'<nav aria-label="{html_escape(f.get("nav_aria", f["nav"]))}"><a href="../index.html">{html_escape(f["nav"])}</a><a href="../grc/book{book}.html" lang="en">{html_escape(f["grc"])}</a></nav>')
    out.append(f'<h1>{html_escape(f["h1"])}</h1>')
    out.append('')
    out.append(f'<h2>{html_escape(bt[lang + "_h2"])}</h2>')
    out.append('')
    out.append(f'<h3>{html_escape(f["principles_h"])}</h3>')
    out.append(f'<p>{html_escape(f["principles_intro"])}</p>')
    if f.get('sprache'):
        out.append(f'<p>{f["sprache"]}</p>')
    out.append('<ol>')
    for rule in f['rules']:
        out.append(f'<li>{rule}</li>')
    out.append('</ol>')
    if f.get('doc_p'):
        out.append(f'<p>{f["doc_p"]}</p>')
    else:
        href, label = f['doc_link']
        out.append(f'<p><a href="{href}">{html_escape(label)}</a></p>')
    out.append('')
    out.append('<hr>')
    out.append('')
    for c, sections in sorted(chapters.items()):
        out.append(f'<h3 id="chapter-{c}">{html_escape(f["chapter"].format(n=c))}</h3>')
        out.append('')
        for (cc, ss), text in sorted(sections.items()):
            escaped = html_escape(text)

            def wrap(match):
                return f'<span class="anm">{match.group(0)}</span>'
            text = NOTE_RE.sub(wrap, escaped)
            out.append(f'<p id="section-{book}-{cc}-{ss}">§{ss} {text}</p>')
            out.append('')
        out.append('<hr>')
        out.append('')
    out.append('</body>')
    out.append('</html>')
    return '\n'.join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--language', required=True, choices=['de', 'en', 'uk', 'he'])
    ap.add_argument('--book', type=int, default=1)
    ap.add_argument('--end', type=int, default=None,
                    help='publish only chapters up to this number (fragments beyond stay unpublished)')
    args = ap.parse_args()
    lang_dir = ROOT / 'work' / args.language
    if args.book != 1:
        lang_dir = lang_dir / f'b{args.book}'
    if not lang_dir.is_dir():
        sys.exit(f'No fragments yet: {lang_dir}')
    chapters = parse_fragments(lang_dir, args.book)
    if args.end is not None:
        chapters = {c: s for c, s in chapters.items() if c <= args.end}
    if not chapters:
        sys.exit('No chapter fragments found')
    expected = expected_structure(args.book)
    problems = []
    for c in sorted(chapters):
        if c not in expected:
            problems.append(f'chapter {c} not in source')
            continue
        missing = [s for s in expected[c] if (c, s) not in chapters[c]]
        extra = [k[1] for k in chapters[c] if k not in {(c, s) for s in expected[c]}]
        if extra:
            problems.append(f'chapter {c}: unexpected sections {extra}')
    covered = sorted(chapters)
    gaps = [c for c in range(1, max(covered) + 1) if c not in covered]
    if gaps:
        problems.append(f'chapters missing in range: {gaps}')
    for p in problems:
        print('PROBLEM:', p, file=sys.stderr)
    html = render(args.language, args.book, chapters)
    out_path = ROOT / 'docs' / args.language / f'book{args.book}.html'
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html + '\n')
    total = sum(len(v) for v in chapters.values())
    print(f'built {out_path} from chapters {covered[0]}–{covered[-1]}; {total} sections')


if __name__ == '__main__':
    main()
