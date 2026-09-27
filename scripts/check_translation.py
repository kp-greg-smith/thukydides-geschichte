#!/usr/bin/env python3
"""Check a translation batch against the pinned Greek source.

Structure errors fail the check. Length and sentence-ending warnings require
human review and do not establish whether a translation is correct.
"""
import argparse
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
NS = {"t": "http://www.tei-c.org/ns/1.0"}


class Sections(HTMLParser):
    def __init__(self):
        super().__init__()
        self.sections = []
        self.current = None
        self.text = []
        self.language = None
        self.direction = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'html':
            self.language = attrs.get('lang')
            self.direction = attrs.get('dir')
        if tag == 'p':
            match = re.fullmatch(r'section-(\d+)-(\d+)-(\d+)', attrs.get('id', ''))
            self.current = tuple(map(int, match.groups())) if match else None
            self.text = []

    def handle_data(self, data):
        if self.current is not None:
            self.text.append(data)

    def handle_endtag(self, tag):
        if tag == 'p' and self.current is not None:
            self.sections.append((self.current, ''.join(self.text)))
            self.current = None


def check(language, book, start, end):
    source = ET.parse(ROOT / 'docs/grc/source.xml')
    greek_book = source.find(f'.//t:div[@subtype="book"][@n="{book}"]', NS)
    if greek_book is None:
        raise ValueError('Book not present in the source')
    chapters = greek_book.findall('t:div[@subtype="chapter"]', NS)
    if not 1 <= start <= end <= len(chapters):
        raise ValueError(f'Chapter range must be inside 1–{len(chapters)}')
    if end - start + 1 > 10:
        raise ValueError('Each assignment/check must cover at most ten chapters')
    path = ROOT / f'docs/{language}/book{book}.html'
    if not path.is_file():
        raise ValueError(f'Translation not available: {path.relative_to(ROOT)}')
    expected = {}
    for chapter in chapters:
        c = int(chapter.attrib['n'])
        if start <= c <= end:
            for section in chapter.findall('t:div[@subtype="section"]', NS):
                key = (book, c, int(section.attrib['n']))
                expected[key] = ' '.join(''.join(section.itertext()).split())
    parser = Sections()
    parser.feed(path.read_text())
    errors, warnings = [], []
    if parser.language != language:
        errors.append(f'Expected html lang="{language}", got {parser.language!r}')
    if language == 'he' and parser.direction != 'rtl':
        errors.append('Hebrew HTML must have dir="rtl"')
    selected = [(k, v) for k, v in parser.sections if start <= k[1] <= end]
    counts = Counter(k for k, _ in selected)
    for key in sorted(expected.keys() - counts.keys()):
        errors.append(f'Missing section {key}')
    for key in sorted(counts.keys() - expected.keys()):
        errors.append(f'Unexpected section {key}')
    for key, count in counts.items():
        if count != 1:
            errors.append(f'Duplicate section {key}: {count} copies')
    if [key for key, _ in selected] != list(expected):
        errors.append('Section order/count differs from the Greek source')
    ratios = []
    for key, text in selected:
        if key not in expected:
            continue
        # Notes and section labels must not mask an empty or truncated translation.
        translated = re.sub(r'^\s*§\d+\s*', '', text)
        translated = re.sub(r'\[[^\]]*\]', '', translated).strip()
        source_text = expected[key]
        size = sum(c.isalpha() for c in translated)
        source_size = sum(c.isalpha() for c in source_text)
        if not size:
            errors.append(f'Empty translation {key}')
            continue
        ratio = size / max(1, source_size)
        ratios.append(ratio)
        if not 0.45 <= ratio <= 3.5:
            warnings.append(f'{key}: unusual letter-count ratio {ratio:.2f} (translation/Greek)')
        source_end = source_text.rstrip(' ”’«»‹›\"\'）)]')
        translated_end = translated.rstrip(' ”’«»‹›\"\'）)]')
        if source_end.endswith(('.', ';', '·', ';', '?', '!')) and not translated_end.endswith(('.', ';', ':', '·', ';', '?', '!', '…', '׃')):
            warnings.append(f'{key}: possibly unfinished sentence: {translated[-90:]}')
    return {
        'language': language, 'book': book, 'chapters': [start, end],
        'expected_sections': len(expected), 'actual_sections': len(selected),
        'letter_ratio_range': [round(min(ratios), 3), round(max(ratios), 3)] if ratios else None,
        'errors': errors, 'review_warnings': warnings,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--language', required=True, choices=['de', 'en', 'uk', 'he'])
    ap.add_argument('--book', type=int, required=True)
    ap.add_argument('--start', type=int, required=True)
    ap.add_argument('--end', type=int, required=True)
    ap.add_argument('--report', type=Path, help='Optional JSON report, including every warning')
    args = ap.parse_args()
    try:
        result = check(args.language, args.book, args.start, args.end)
    except ValueError as exc:
        ap.error(str(exc))
    if args.report:
        args.report.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(f"{result['actual_sections']}/{result['expected_sections']} sections; "
          f"{len(result['errors'])} errors; {len(result['review_warnings'])} review warnings; "
          f"letter ratios {result['letter_ratio_range']}")
    for message in result['errors']:
        print('ERROR:', message)
    for message in result['review_warnings'][:10]:
        print('REVIEW:', message)
    if len(result['review_warnings']) > 10:
        print('Use --report FILE.json to save all review warnings.')
    return 1 if result['errors'] else 0


if __name__ == '__main__':
    sys.exit(main())
