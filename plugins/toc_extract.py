"""Extract a clean HTML <ul> Table of Contents for articles with >= 3 headings."""

from html import escape

from bs4 import BeautifulSoup
from pelican import signals

MIN_HEADINGS = 3


def _heading_text(tag) -> str:
    clone = BeautifulSoup(str(tag), 'html.parser')
    for anchor in clone.select('a.heading-anchor, a.headerlink'):
        anchor.decompose()
    return clone.get_text(' ', strip=True)


def _build_toc_html(items: list[tuple[int, str, str]]) -> str:
    parts: list[str] = ['<ul>']
    in_nested = False

    for level, hid, text in items:
        safe_id = escape(hid, quote=True)
        safe_text = escape(text)
        if level == 2:
            if in_nested:
                parts.append('</ul></li>')
                in_nested = False
            elif len(parts) > 1:
                parts.append('</li>')
            parts.append(f'<li><a href="#{safe_id}">{safe_text}</a>')
        else:
            if not in_nested:
                if len(parts) == 1:
                    parts.append('<li>')
                parts.append('<ul>')
                in_nested = True
            parts.append(f'<li><a href="#{safe_id}">{safe_text}</a></li>')

    if in_nested:
        parts.append('</ul></li>')
    elif len(parts) > 1:
        parts.append('</li>')

    parts.append('</ul>')
    return '\n'.join(parts)


def extract_toc(instance) -> None:
    """Populate article.toc with HTML <ul> when >= 3 h2/h3 headings have IDs."""
    content = getattr(instance, '_content', None)
    if not content:
        instance.toc = None
        return

    soup = BeautifulSoup(content, 'html.parser')
    headings: list[tuple[int, str, str]] = []

    for tag in soup.find_all(['h2', 'h3']):
        hid = tag.get('id')
        if not hid:
            continue
        text = _heading_text(tag)
        if text:
            headings.append((int(tag.name[1]), str(hid), text))

    if len(headings) < MIN_HEADINGS:
        instance.toc = None
        return

    instance.toc = _build_toc_html(headings)


def register() -> None:
    signals.content_object_init.connect(extract_toc)
