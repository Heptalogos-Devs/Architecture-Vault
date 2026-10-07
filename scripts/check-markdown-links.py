#!/usr/bin/env python3
"""Check local inline Markdown links in tracked documents without network calls."""
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
INLINE_LINK = re.compile(r'!?\[[^\]\n]+\]\((<[^>]+>|[^\s)]+)(?:\s+"[^"]*")?\)')


def heading_anchors(path):
    anchors = set()
    counts = Counter()
    for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', path.read_text(), re.MULTILINE):
        slug = re.sub(r'[^\w\s\-\u0080-\U0010ffff]', '', heading.lower()).replace(' ', '-')
        anchors.add(f'{slug}-{counts[slug]}' if counts[slug] else slug)
        counts[slug] += 1
    return anchors


def main():
    tracked = subprocess.check_output(['git', 'ls-files', '-z', '*.md'], cwd=ROOT).decode().split('\0')
    files = [ROOT / name for name in tracked if name]
    errors = []
    links = 0
    for path in files:
        for match in INLINE_LINK.finditer(path.read_text()):
            href = match.group(1).strip('<>')
            url = urlsplit(href)
            if url.scheme or href.startswith('//'):
                continue
            links += 1
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            error = None
            if not target.exists():
                error = 'missing target'
            elif url.fragment and target.suffix == '.md' and unquote(url.fragment) not in heading_anchors(target):
                error = 'missing heading anchor'
            if error:
                line = path.read_text()[:match.start()].count('\n') + 1
                errors.append(f'{path.relative_to(ROOT)}:{line}: {error}: {href}')
    print(f'Checked {links} local links across {len(files)} tracked Markdown documents.')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print('All local Markdown links resolve.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
