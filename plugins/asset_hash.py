"""Fingerprint main theme CSS/JS assets with SHA-256 content hashes."""

import hashlib
import shutil
from pathlib import Path

from pelican import signals

_ASSETS = (
    ('MAIN_CSS_URL', 'static/css/main.css', 'theme/css/main', '.css'),
    ('MAIN_JS_URL', 'static/js/terminal.js', 'theme/js/terminal', '.js'),
)


def _short_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:8]


def compute_asset_urls(pelican_obj) -> None:
    """Populate MAIN_CSS_URL and MAIN_JS_URL settings before templates render."""
    theme_dir = Path(pelican_obj.settings.get('THEME', 'theme/minimal128'))
    for setting_key, rel_src, out_prefix, suffix in _ASSETS:
        src_path = theme_dir / rel_src
        if src_path.is_file():
            digest = _short_sha256(src_path)
            pelican_obj.settings[setting_key] = f'{out_prefix}.{digest}{suffix}'
        else:
            pelican_obj.settings[setting_key] = f'{out_prefix}{suffix}'


def copy_hashed_assets(pelican_obj) -> None:
    """Copy built static assets to their fingerprinted paths alongside originals."""
    output_path = Path(pelican_obj.output_path)
    for setting_key, _rel_src, out_prefix, suffix in _ASSETS:
        original_rel = f'{out_prefix}{suffix}'
        hashed_rel = pelican_obj.settings.get(setting_key, original_rel)
        if hashed_rel == original_rel:
            continue

        src = output_path / original_rel
        dst = output_path / hashed_rel
        if src.is_file():
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)


def register() -> None:
    signals.initialized.connect(compute_asset_urls)
    signals.finalized.connect(copy_hashed_assets)
