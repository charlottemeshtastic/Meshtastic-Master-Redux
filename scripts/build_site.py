"""Build a standalone static directory from current Markdown and platform metadata."""
import argparse
import html
import json
import pathlib
import shutil
from catalog import ROOT, resources


def build(output=None, ref='main'):
    output = pathlib.Path(output or ROOT / 'site/dist'); output.mkdir(parents=True, exist_ok=True)
    catalog = resources()
    template = (ROOT / 'site/index.html').read_text()
    payload = json.dumps(catalog, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026')
    template = template.replace('@@DATA@@', payload).replace('@@COUNT@@', str(len(catalog)))
    template = template.replace('@@REPO@@', 'https://github.com/charlottemeshtastic/Meshtastic-Master-Redux/blob/' + html.escape(ref, quote=True))
    template = template.replace('<body>', '<body data-source-ref="' + html.escape(ref, quote=True) + '">')
    (output / 'index.html').write_text(template)
    (output / 'catalog.json').write_text(json.dumps(catalog, ensure_ascii=False, indent=2))
    for file in ['styles.css', 'filters.js', 'app.js']:
        shutil.copyfile(ROOT / 'site' / file, output / file)
    print(f'Built {len(catalog)} directory entries in {output}')
    return catalog


if __name__ == '__main__':
    parser = argparse.ArgumentParser(); parser.add_argument('--output'); parser.add_argument('--ref', default='main')
    args = parser.parse_args(); build(args.output, args.ref)
