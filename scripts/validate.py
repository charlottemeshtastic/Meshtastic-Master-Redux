"""Validate index structure and the preserved initial merge audit (no network needed)."""
import hashlib
import json
import pathlib
import re
import sys
import urllib.parse

root = pathlib.Path(__file__).resolve().parents[1]
errors = []

def anchors(text):
    counts = {}
    result = set()
    for heading in re.findall(r'^#{1,6} (.+)$', text, re.M):
        slug = re.sub(r'[^\w\s-]', '', heading.lower()).replace(' ', '-')
        n = counts.get(slug, 0)
        counts[slug] = n + 1
        result.add(slug + (f'-{n}' if n else ''))
    return result

for file in root.rglob('*.md'):
    text = file.read_text()
    for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', text):
        if urllib.parse.urlsplit(target).scheme:
            continue
        path, _, fragment = target.partition('#')
        destination = (file.parent / urllib.parse.unquote(path)).resolve() if path else file
        if not destination.is_file():
            errors.append(f'{file.relative_to(root)}: missing file {target}')
        elif fragment and fragment not in anchors(destination.read_text()):
            errors.append(f'{file.relative_to(root)}: missing anchor {target}')
    if '[INSERT CONTACT METHOD]' in text:
        errors.append(f'{file}: unfinished contact placeholder')

audit = json.loads((root / 'audit/resources.json').read_text())
entries = audit['active'] + audit['quarantined']
assert len({e['url'] for e in entries}) == len(entries), 'Duplicate primary resource URLs'
assert len(entries) == 413, 'Initial merge must account for all 413 identities'
assert sum(len(e['sources']) for e in entries) == 554, 'Initial merge must account for all 554 source rows'
assert len(audit['deduplicated']) == 141
assert len({(s['source'], s['line']) for e in entries for s in e['sources']}) == 554
for entry in audit['active']:
    file = root / ('COMMUNITIES.md' if entry['category'] == 'Communities' else 'README.md')
    if '- ' + entry['rendered'] not in file.read_text():
        errors.append(f"Missing audited entry: {entry['url']}")
    if entry['url'] == 'http://meshtastic.local':
        errors.append('Local device address in public index')
license_bytes = (root / 'LICENSE').read_bytes()
blob = hashlib.sha1(b'blob ' + str(len(license_bytes)).encode() + b'\0' + license_bytes).hexdigest()
if blob != '0e259d42c996742e9e3cba14c677129b2c1b6311':
    errors.append('CC0 license differs from original source blob')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print('PASS: Markdown file/anchor targets, 554 source rows, 413 identities, 141 duplicate decisions, active entries and original CC0 license.')
