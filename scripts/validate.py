"""Validate the current index and preserve the initial merge audit (no network needed)."""
import hashlib
import json
import pathlib
import re
import sys
import urllib.parse
from catalog import identity, resources

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
# The historical audit is immutable; validate current entries separately so edits,
# removals and additions do not require rewriting a dated source snapshot.
current = resources()
seen = {}
for entry in current:
    key = identity(entry['url'])
    if key in seen:
        errors.append(f"Duplicate live entry: {entry['url']} ({seen[key]})")
    seen[key] = entry['source']
    parsed = urllib.parse.urlsplit(entry['url'])
    if parsed.scheme not in ('https', 'http') or not parsed.hostname or parsed.hostname.endswith('.local') or parsed.username or parsed.password:
        errors.append(f"Not a public resource URL: {entry['url']}")
allowed = {'Android', 'Apple', 'Linux', 'macOS', 'Windows', 'Web', 'Python'}
platforms = json.loads((root / 'data/platforms.json').read_text())
platform_keys = set()
for record in platforms:
    key = identity(record['url'])
    if key in platform_keys or key not in seen:
        errors.append(f"Duplicate or orphan platform metadata: {record['url']}")
    platform_keys.add(key)
    if not record['platforms'] or not set(record['platforms']) <= allowed:
        errors.append(f"Invalid platform tags: {record['url']}")
    if not record['source'].startswith('https://'):
        errors.append(f"Missing platform evidence URL: {record['url']}")
license_bytes = (root / 'LICENSE').read_bytes()
blob = hashlib.sha1(b'blob ' + str(len(license_bytes)).encode() + b'\0' + license_bytes).hexdigest()
if blob != '0e259d42c996742e9e3cba14c677129b2c1b6311':
    errors.append('CC0 license differs from original source blob')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'PASS: {len(current)} live resources, unique URLs, platform evidence, Markdown files/anchors, immutable source audit and original CC0 license.')
