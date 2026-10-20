"""Render the six editable DOT sources with Graphviz CLI or an explicit Viz WASM module."""
from pathlib import Path
import argparse
import json
import re
import shutil
import subprocess
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--dot', default=shutil.which('dot'), help='Installed Graphviz dot executable')
parser.add_argument('--wasm', type=Path, help='Explicit @viz-js/viz dist/viz.js path')
args = parser.parse_args()
if not args.dot and not args.wasm:
    parser.error('Install Graphviz dot or pass --wasm <@viz-js/viz/dist/viz.js>')
(ROOT / 'svg').mkdir(exist_ok=True)
for page in json.loads((ROOT / 'pages.json').read_text()):
    source = ROOT / 'src' / (page['file'] + '.dot')
    command = [args.dot, '-Tsvg'] if args.dot else [
        'node', str(ROOT / 'render_graphviz.mjs'), str(args.wasm.resolve())]
    result = subprocess.run(command, input=source.read_text(), text=True, capture_output=True)
    if result.returncode:
        raise RuntimeError(result.stderr)
    svg = result.stdout
    svg = re.sub(r'<!DOCTYPE[^>]*>', '', svg, flags=re.S)
    element = ET.fromstring(svg)
    for anchor in element.iter('{http://www.w3.org/2000/svg}a'):
        href = anchor.get('{http://www.w3.org/1999/xlink}href', '')
        if href.startswith(('http:', 'https:')):
            raise ValueError(f'Online graph source link: {href}')
        if href and not (ROOT / 'svg' / href.split('#')[0]).exists():
            raise ValueError(f'Missing graph source: {href}')
    output = ROOT / 'svg' / (page['file'] + '.svg')
    output.write_text(svg)
    print(f'{output.name}: viewBox={element.get("viewBox")}')
