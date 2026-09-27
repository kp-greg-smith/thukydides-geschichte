#!/usr/bin/env python3
"""Render the pinned Perseus TEI source as eight local Original HTML books.

The source file is unmodified. Only XML markup and whitespace are transformed;
all section text, including speakers and verse, is retained in document order.
"""
from pathlib import Path
import hashlib
import html
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
NS = {"t": "http://www.tei-c.org/ns/1.0"}


def normalized_text(element):
    return " ".join("".join(element.itertext()).split())


def build():
    source = ROOT / "docs/grc/source.xml"
    provenance = json.loads((source.parent / "source.json").read_text())
    if hashlib.sha256(source.read_bytes()).hexdigest() != provenance["sha256"]:
        raise ValueError("Source differs from its recorded SHA-256; check provenance before rendering")
    tree = ET.parse(source)
    books = tree.findall('.//t:div[@subtype="book"]', NS)
    if len(books) != 8:
        raise ValueError("Expected eight source books")
    toolbar = (ROOT / "docs/assets/toolbar.html").read_text().replace('value="almendra" selected', 'value="almendra"').replace('value="sourceserif4"', 'value="sourceserif4" selected')
    for book in books:
        number = int(book.attrib["n"])
        parts = [f'''<!DOCTYPE html>
<html lang="grc"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Θουκυδίδου Ἱστορίαι — {number} · Original</title>
<script src="../assets/theme.js"></script><link rel="stylesheet" href="../assets/reader.css"></head><body>
<div lang="en">{toolbar}</div>
<nav lang="en" aria-label="Editions"><a href="../index.html">All languages and status</a>''']
        if number == 1:
            parts.append('<a href="../de/book1.html" lang="de">Deutsche Übersetzung · Buch 1</a>')
        parts.append(f'</nav><h1>Θουκυδίδου Ἱστορίαι</h1><h2>Βιβλίον {number}</h2>')
        parts.append('''<p class="source-note" lang="en"><strong>Ancient Greek — Original.</strong> Henry Stuart Jones, Oxford University Press, 1910 (reprint 1942). Digital text: Perseus Digital Library, Tufts University. Rendered from TEI XML; whitespace normalized and navigation added, wording unchanged.
<a href="source.xml">Source XML</a> · <a href="source.json">Provenance</a> · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>.</p>
<nav lang="en" aria-label="Original books">''')
        for n in range(1, 9):
            current = ' aria-current="page"' if n == number else ''
            parts.append(f'<a href="book{n}.html"{current}>Book {n}</a>')
        parts.append('</nav><main>')
        for chapter in book.findall('t:div[@subtype="chapter"]', NS):
            c = int(chapter.attrib['n'])
            parts.append(f'<h3 id="chapter-{c}">Κεφάλαιον {c}</h3>')
            for section in chapter.findall('t:div[@subtype="section"]', NS):
                s = int(section.attrib['n'])
                parts.append(f'<p id="section-{number}-{c}-{s}">§{s} {html.escape(normalized_text(section))}</p>')
        parts.append('</main></body></html>\n')
        (source.parent / f'book{number}.html').write_text('\n'.join(parts))
    print('Rendered all eight Original books from the pinned source.')


if __name__ == '__main__':
    build()
