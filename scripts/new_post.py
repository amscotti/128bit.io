#!/usr/bin/env python3
"""Scaffold a new 128bit.io Pelican Markdown post with validated frontmatter."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

POSTS_DIR = Path(__file__).resolve().parent.parent / 'content' / 'posts'
_SLUG_RE = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')


def slugify(title: str) -> str:
    slug = title.lower().strip()
    slug = re.sub(r'[^a-z0-9]+', '-', slug)
    slug = re.sub(r'-{2,}', '-', slug).strip('-')
    return slug


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Create a new blog post under content/posts/.')
    parser.add_argument('title', help='Title of the blog post')
    parser.add_argument('--slug', help='Custom lowercase hyphen-separated slug')
    parser.add_argument('--tags', default='', help='Comma-separated tags (e.g. "Python, Systems")')
    parser.add_argument('--summary', default='', help='Brief summary for listings and SEO')
    parser.add_argument('--draft', action='store_true', help='Mark post with Status: draft')
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    title = args.title.strip()
    if not title:
        print('Error: title must not be empty.', file=sys.stderr)
        return 1

    slug = (args.slug or slugify(title)).strip().lower()
    if not _SLUG_RE.match(slug):
        print(
            f'Error: invalid slug "{slug}". Use lowercase letters, digits, and single hyphens.',
            file=sys.stderr,
        )
        return 1

    dest = POSTS_DIR / f'{slug}.md'
    if dest.exists():
        print(f'Error: {dest} already exists.', file=sys.stderr)
        return 1

    tags = ', '.join(t.strip() for t in args.tags.split(',') if t.strip())
    summary = args.summary.strip() or f'Notes on {title}.'
    now = datetime.now().strftime('%Y-%m-%d %H:%M')

    lines = [
        f'Title: {title}',
        f'Date: {now}',
        f'Slug: {slug}',
        f'Tags: {tags}',
        f'Summary: {summary}',
    ]
    if args.draft:
        lines.append('Status: draft')

    lines.extend(['', 'Write your post here.', ''])

    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    dest.write_text('\n'.join(lines), encoding='utf-8')
    print(f'Created {dest.relative_to(POSTS_DIR.parent.parent)}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
