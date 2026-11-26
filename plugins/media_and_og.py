"""Enrich local <img> elements with dimensions/lazy attributes and generate OG cards."""

from pathlib import Path
from urllib.parse import unquote, urlparse

from bs4 import BeautifulSoup
from pelican import signals
from PIL import Image, ImageDraw, ImageFont

OG_WIDTH = 1200
OG_HEIGHT = 630

BG_PRIMARY = (13, 17, 23)
BG_SURFACE = (22, 27, 34)
BG_HEADER = (33, 38, 45)
BORDER_COLOR = (48, 54, 61)
TEXT_PRIMARY = (230, 237, 243)
TEXT_MUTED = (145, 152, 161)
ACCENT_PURPLE = (167, 139, 250)
DOT_RED = (248, 81, 73)
DOT_YELLOW = (210, 153, 34)
DOT_GREEN = (63, 185, 80)

_FONT_CANDIDATES = (
    '/usr/share/fonts/ttf-dejavu/DejaVuSansMono-Bold.ttf',
    '/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',
    '/usr/share/fonts/dejavu/DejaVuSansMono-Bold.ttf',
    '/usr/share/fonts/ttf-dejavu/DejaVuSansMono.ttf',
    '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf',
    '/System/Library/Fonts/SFNSMono.ttf',
    '/System/Library/Fonts/Menlo.ttc',
    '/System/Library/Fonts/Supplemental/Courier New Bold.ttf',
    '/System/Library/Fonts/Supplemental/Courier New.ttf',
)

_dim_cache: dict[Path, tuple[int, int] | None] = {}
_font_cache: dict[int, ImageFont.FreeTypeFont | ImageFont.ImageFont] = {}
_collected_articles: list = []


def _load_mono_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    cached = _font_cache.get(size)
    if cached is not None:
        return cached

    for candidate in _FONT_CANDIDATES:
        if Path(candidate).is_file():
            try:
                font = ImageFont.truetype(candidate, size=size)
                _font_cache[size] = font
                return font
            except OSError:
                continue

    font = ImageFont.load_default(size=size)
    _font_cache[size] = font
    return font


def _get_image_dimensions(img_path: Path) -> tuple[int, int] | None:
    if img_path in _dim_cache:
        return _dim_cache[img_path]

    if not img_path.is_file():
        _dim_cache[img_path] = None
        return None

    try:
        with Image.open(img_path) as img:
            width, height = img.size
            exif = img.getexif()
            if exif and exif.get(274) in (5, 6, 7, 8):
                width, height = height, width
            _dim_cache[img_path] = (width, height)
            return (width, height)
    except OSError:
        _dim_cache[img_path] = None
        return None


def _resolve_local_image(src: str, content_root: Path) -> Path | None:
    parsed = urlparse(src)
    if parsed.scheme in ('http', 'https', 'data'):
        return None

    path_str = unquote(parsed.path)
    for prefix in ('{static}/images/', '/images/', 'images/'):
        if path_str.startswith(prefix):
            rel = path_str[len(prefix) :].lstrip('/')
            return content_root / 'images' / rel

    return None


def enrich_images(instance) -> None:
    """Add width, height, loading='lazy', and decoding='async' to article images."""
    content = getattr(instance, '_content', None)
    if not content or '<img' not in content.lower():
        return

    content_root = Path(instance.settings.get('PATH', 'content'))
    soup = BeautifulSoup(content, 'html.parser')
    modified = False

    for img in soup.find_all('img'):
        if not img.get('loading'):
            img['loading'] = 'lazy'
            modified = True
        if not img.get('decoding'):
            img['decoding'] = 'async'
            modified = True

        src = img.get('src')
        if src and (not img.get('width') or not img.get('height')):
            local_path = _resolve_local_image(str(src), content_root)
            if local_path is not None:
                dims = _get_image_dimensions(local_path)
                if dims is not None:
                    img['width'] = str(dims[0])
                    img['height'] = str(dims[1])
                    modified = True

    if modified:
        instance._content = str(soup)


def _wrap_text(
    draw: ImageDraw.ImageDraw,
    text: str,
    font: ImageFont.FreeTypeFont | ImageFont.ImageFont,
    max_width: int,
    max_lines: int = 3,
) -> list[str]:
    words = text.split()
    if not words:
        return []

    lines: list[str] = []
    current = words[0]
    for word in words[1:]:
        candidate = f'{current} {word}'
        bbox = draw.textbbox((0, 0), candidate, font=font)
        if (bbox[2] - bbox[0]) <= max_width:
            current = candidate
        else:
            lines.append(current)
            current = word
            if len(lines) == max_lines:
                break
    else:
        lines.append(current)

    if len(lines) > max_lines:
        lines = lines[:max_lines]

    if len(lines) == max_lines and len(' '.join(lines)) < len(text):
        last = lines[-1]
        while last:
            candidate = f'{last}...'
            bbox = draw.textbbox((0, 0), candidate, font=font)
            if (bbox[2] - bbox[0]) <= max_width:
                lines[-1] = candidate
                break
            last = last[:-1].rstrip()

    return lines


def _render_og_card(
    dest: Path,
    prompt: str,
    title: str,
    meta_left: str,
    meta_right: str,
) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    img = Image.new('RGB', (OG_WIDTH, OG_HEIGHT), BG_PRIMARY)
    draw = ImageDraw.Draw(img)

    # Outer terminal window frame
    pad = 44
    box = (pad, pad, OG_WIDTH - pad, OG_HEIGHT - pad)
    draw.rounded_rectangle(box, radius=16, fill=BG_SURFACE, outline=BORDER_COLOR, width=2)

    # Top bar
    bar_bottom = pad + 52
    draw.rounded_rectangle(
        (pad, pad, OG_WIDTH - pad, bar_bottom),
        radius=16,
        fill=BG_HEADER,
        outline=BORDER_COLOR,
        width=2,
    )
    draw.rectangle((pad + 2, bar_bottom - 14, OG_WIDTH - pad - 2, bar_bottom), fill=BG_HEADER)
    draw.line((pad, bar_bottom, OG_WIDTH - pad, bar_bottom), fill=BORDER_COLOR, width=2)

    # Window traffic lights
    dot_y = pad + 26
    for idx, color in enumerate((DOT_RED, DOT_YELLOW, DOT_GREEN)):
        cx = pad + 28 + idx * 24
        draw.ellipse((cx - 7, dot_y - 7, cx + 7, dot_y + 7), fill=color)

    bar_font = _load_mono_font(20)
    draw.text((pad + 115, pad + 15), '128bit.io — terminal', font=bar_font, fill=TEXT_MUTED)

    # Terminal prompt line
    inner_left = pad + 44
    inner_width = (OG_WIDTH - pad - 44) - inner_left
    prompt_font = _load_mono_font(24)
    prompt_lines = _wrap_text(draw, prompt, prompt_font, inner_width, max_lines=1)
    draw.text(
        (inner_left, bar_bottom + 36),
        prompt_lines[0] if prompt_lines else prompt,
        font=prompt_font,
        fill=ACCENT_PURPLE,
    )

    # Title
    title_font = _load_mono_font(46)
    title_lines = _wrap_text(draw, title, title_font, inner_width, max_lines=3)
    y = bar_bottom + 104
    for line in title_lines:
        draw.text((inner_left, y), line, font=title_font, fill=TEXT_PRIMARY)
        y += 64

    # Footer separator & metadata
    footer_y = OG_HEIGHT - pad - 76
    draw.line(
        (inner_left, footer_y - 18, OG_WIDTH - pad - 44, footer_y - 18),
        fill=BORDER_COLOR,
        width=2,
    )
    meta_font = _load_mono_font(22)
    draw.text((inner_left, footer_y), meta_left, font=meta_font, fill=TEXT_MUTED)

    right_bbox = draw.textbbox((0, 0), meta_right, font=meta_font)
    right_w = right_bbox[2] - right_bbox[0]
    draw.text(
        (OG_WIDTH - pad - 44 - right_w, footer_y),
        meta_right,
        font=meta_font,
        fill=ACCENT_PURPLE,
    )

    img.save(dest, format='PNG', optimize=True)


def collect_articles(article_generator) -> None:
    _collected_articles.clear()
    _collected_articles.extend(getattr(article_generator, 'articles', []))


def generate_og_cards(pelican_obj) -> None:
    """Generate default and per-article 1200x630 terminal-styled PNG OG cards."""
    output_path = Path(pelican_obj.output_path)
    og_dir = output_path / 'og'
    settings = pelican_obj.settings
    sitename = settings.get('SITENAME', '128bit.io')
    author = settings.get('AUTHOR', 'Anthony Scotti')

    _render_og_card(
        dest=og_dir / 'default.png',
        prompt='[amscotti@128bit.io ~]# whoami',
        title=f'{sitename} — Software Engineering & Systems',
        meta_left=author,
        meta_right=sitename,
    )

    for article in _collected_articles:
        slug = str(getattr(article, 'slug', '')).strip('/')
        if not slug:
            continue
        short_slug = slug.split('/')[-1]
        if short_slug == 'index.html' and '/' in slug:
            short_slug = slug.split('/')[-2]

        date_str = article.date.strftime('%Y-%m-%d') if getattr(article, 'date', None) else ''
        tags = getattr(article, 'tags', []) or []
        tag_str = ' '.join(f'[{t.name}]' for t in tags[:4])
        meta_left = f'{date_str}  {tag_str}'.strip()

        _render_og_card(
            dest=og_dir / f'{slug}.png',
            prompt=f'[amscotti@128bit.io ~/posts]# cat {short_slug}.md',
            title=str(getattr(article, 'title', short_slug)),
            meta_left=meta_left,
            meta_right=sitename,
        )


def register() -> None:
    signals.content_object_init.connect(enrich_images)
    signals.article_generator_finalized.connect(collect_articles)
    signals.finalized.connect(generate_og_cards)
