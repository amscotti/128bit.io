"""Lightweight YouTube embed plugin replacing pelican-liquid-tags."""

import re

from pelican import signals

_YOUTUBE_TAG = r'\{%\s*youtube\s+([A-Za-z0-9_-]{6,32})(?:\s+\d+%?\s+\d+%?)?\s*%\}'
_P_ONLY_RE = re.compile(rf'<p>\s*{_YOUTUBE_TAG}\s*</p>', re.IGNORECASE)
_P_LEAD_RE = re.compile(rf'<p>\s*{_YOUTUBE_TAG}\s*(?:\r?\n|<br\s*/?>)+', re.IGNORECASE)
_RAW_RE = re.compile(_YOUTUBE_TAG, re.IGNORECASE)


def _iframe_html(video_id: str) -> str:
    return (
        '<div class="video-embed">'
        f'<iframe src="https://www.youtube-nocookie.com/embed/{video_id}" '
        'title="YouTube video" '
        'loading="lazy" '
        'referrerpolicy="strict-origin-when-cross-origin" '
        'allow="accelerometer; autoplay; clipboard-write; encrypted-media; '
        'gyroscope; picture-in-picture" '
        'allowfullscreen></iframe>'
        '</div>'
    )


def replace_youtube_tags(instance) -> None:
    """Expand {% youtube ID [width height] %} tags into privacy-enhanced iframes."""
    content = getattr(instance, '_content', None)
    if not content or 'youtube' not in content.lower():
        return

    updated = _P_ONLY_RE.sub(lambda m: _iframe_html(m.group(1)), content)
    updated = _P_LEAD_RE.sub(lambda m: f'{_iframe_html(m.group(1))}\n<p>', updated)
    updated = _RAW_RE.sub(lambda m: _iframe_html(m.group(1)), updated)
    instance._content = updated


def register() -> None:
    signals.content_object_init.connect(replace_youtube_tags)
