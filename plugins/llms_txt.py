"""Emit llms.txt, raw Markdown mirrors per article, and XSL stylesheet hook on index.xml."""

import re
from pathlib import Path

from bs4 import BeautifulSoup
from pelican import signals

_collected_articles: list = []
_XML_DECL_RE = re.compile(r'^(<\?xml\b[^?]*\?>\s*)', re.IGNORECASE)
_META_LINE_RE = re.compile(r'^[A-Za-z][A-Za-z0-9_-]*\s*:')


def _strip_html(value: str) -> str:
    return ' '.join(BeautifulSoup(value or '', 'html.parser').get_text(' ').split())


def _extract_markdown_body(source_path: Path) -> str:
    """Read raw Markdown body after Pelican key: value metadata header."""
    raw = source_path.read_text(encoding='utf-8')
    lines = raw.splitlines()
    idx = 0
    while idx < len(lines) and (
        _META_LINE_RE.match(lines[idx]) or (idx > 0 and lines[idx].startswith((' ', '\t')))
    ):
        idx += 1
    while idx < len(lines) and not lines[idx].strip():
        idx += 1
    return '\n'.join(lines[idx:]).strip()


def _article_md_dest(output_path: Path, article_url: str) -> Path:
    clean = article_url.lstrip('/')
    if clean.endswith('.html'):
        return output_path / Path(clean).parent / 'index.md'
    return output_path / clean / 'index.md'


def _article_md_url(base_url: str, article_url: str) -> str:
    clean = article_url.lstrip('/')
    if clean.endswith('.html'):
        parent = str(Path(clean).parent).strip('.')
        rel = f'{parent}/index.md' if parent else 'index.md'
    else:
        rel = f"{clean.rstrip('/')}/index.md"
    return f'{base_url}/{rel}' if base_url else f'/{rel}'


def collect_articles(article_generator) -> None:
    _collected_articles.clear()
    _collected_articles.extend(getattr(article_generator, 'articles', []))


def emit_outputs(pelican_obj) -> None:
    output_path = Path(pelican_obj.output_path)
    settings = pelican_obj.settings
    sitename = settings.get('SITENAME', '128bit.io')
    author = settings.get('AUTHOR', 'Anthony Scotti')
    bio = settings.get('BIO', '')
    siteurl = settings.get('SITEURL', '').rstrip('/')
    base_url = siteurl or 'https://128bit.io'

    sorted_articles = sorted(
        _collected_articles,
        key=lambda a: getattr(a, 'date', None),
        reverse=True,
    )

    # 1. Emit per-article raw Markdown mirrors at output/{article.url}index.md
    for article in sorted_articles:
        source = getattr(article, 'source_path', None)
        if not source:
            continue
        source_path = Path(source)
        if not source_path.is_file():
            continue

        dest = _article_md_dest(output_path, article.url)
        dest.parent.mkdir(parents=True, exist_ok=True)

        date_str = article.date.strftime('%Y-%m-%d') if getattr(article, 'date', None) else ''
        tags = ', '.join(t.name for t in (getattr(article, 'tags', None) or []))
        canonical = f"{base_url}/{article.url.lstrip('/')}"
        summary = _strip_html(getattr(article, 'summary', ''))
        body = _extract_markdown_body(source_path)

        header_lines = [
            f'# {article.title}',
            '',
            f'- **Author**: {author}',
            f'- **Date**: {date_str}',
        ]
        if tags:
            header_lines.append(f'- **Tags**: {tags}')
        header_lines.append(f'- **URL**: {canonical}')
        if summary:
            header_lines.append(f'- **Summary**: {summary}')
        header_lines.extend(['', '---', '', body, ''])

        dest.write_text('\n'.join(header_lines), encoding='utf-8')

    # 2. Emit curated output/llms.txt
    llms_lines = [
        f'# {sitename}',
        '',
        f'> {bio}' if bio else f'> Personal technical blog by {author}.',
        '',
        f'- **Site**: {base_url}/',
        f'- **Author**: {author}',
        f'- **Atom Feed**: {base_url}/index.xml',
        f'- **Sitemap**: {base_url}/sitemap.xml',
        '',
        '## Articles',
        '',
    ]

    for article in sorted_articles:
        date_str = article.date.strftime('%Y-%m-%d') if getattr(article, 'date', None) else ''
        md_url = _article_md_url(base_url, article.url)
        summary = _strip_html(getattr(article, 'summary', ''))
        line = f'- [{article.title}]({md_url}) ({date_str})'
        if summary:
            line = f'{line}: {summary}'
        llms_lines.append(line)

    llms_lines.append('')
    (output_path / 'llms.txt').write_text('\n'.join(llms_lines), encoding='utf-8')

    # 3. Inject XSL stylesheet processing instruction into output/index.xml
    feed_path = output_path / 'index.xml'
    if feed_path.is_file():
        xml_text = feed_path.read_text(encoding='utf-8')
        if '<?xml-stylesheet' not in xml_text:
            xsl_pi = '<?xml-stylesheet type="text/xsl" href="/feed.xsl"?>\n'
            if _XML_DECL_RE.match(xml_text):
                xml_text = _XML_DECL_RE.sub(rf'\1{xsl_pi}', xml_text, count=1)
            else:
                xml_text = xsl_pi + xml_text
            feed_path.write_text(xml_text, encoding='utf-8')


def register() -> None:
    signals.article_generator_finalized.connect(collect_articles)
    signals.finalized.connect(emit_outputs)
