"""Read the current Markdown index; historical audit JSON is not the live catalog."""
import json
import pathlib
import re
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parents[1]
LINK = re.compile(r'\[([^\]]+)\]\((https?://[^\s)]+)\)')


def identity(url):
    p = urllib.parse.urlsplit(url)
    host = p.netloc.lower().removeprefix('www.')
    path = p.path.rstrip('/')
    if host == 'discord.gg':
        host, path = 'discord.com', '/invite' + path
    if host == 'github.com':
        path = path.lower()
    return host + path + ('?' + p.query if p.query else '') + ('#' + p.fragment if p.fragment else '')


def resources(root=ROOT):
    platform_data = json.loads((root / 'data/platforms.json').read_text())
    platforms = {identity(e['url']): e['platforms'] for e in platform_data}
    result = []
    for filename in ['README.md', 'COMMUNITIES.md']:
        section = region = ''
        for number, line in enumerate((root / filename).read_text().splitlines(), 1):
            if line.startswith('## '):
                section, region = line[3:].strip(), ''
            elif line.startswith('### '):
                region = line[4:].strip()
            if not line.startswith('- ['):
                continue
            links = LINK.findall(line)
            if not links:
                continue
            name, url = links[0]
            # Navigation with a later external link is not a resource row.
            if not line.startswith(f'- [{name}]({url})'):
                continue
            country = section if filename == 'COMMUNITIES.md' and section not in ['Project channels', 'Online communities'] else ''
            category = 'Communities' if filename == 'COMMUNITIES.md' else section
            if filename == 'README.md' and category in ['Contents', 'Start here', 'Communities', 'License and credit']:
                continue
            status = 'pending' if '[Verification pending]' in line else 'membership-unverified' if '[Membership not verified]' in line else 'listed'
            suffix = line[line.index(')') + 1:]
            suffix = LINK.sub(lambda m: m.group(1), suffix)
            suffix = re.sub(r'\*\*\[(?:Verification pending|Membership not verified)\]\*\*', '', suffix)
            description = re.sub(r'<[^>]+>', '', suffix).replace('**', '').strip(' —-· ')
            result.append({'name': name, 'url': url, 'description': description, 'category': category,
                           'country': country, 'region': region if country else '',
                           'platforms': platforms.get(identity(url), []), 'status': status,
                           'links': [{'name': label, 'url': u} for label, u in links[1:]],
                           'source': filename, 'line': number})
    return result


def public_urls(root=ROOT):
    """All HTTP references in live docs, excluding immutable audit evidence."""
    urls = set()
    for filename in ['README.md', 'COMMUNITIES.md', 'CONTRIBUTING.md', 'ATTRIBUTION.md']:
        for _, url in LINK.findall((root / filename).read_text()):
            urls.add(url)
    for path in (root / 'docs').glob('*.md'):
        urls.update(url for _, url in LINK.findall(path.read_text()))
    urls.update(e['source'] for e in json.loads((root / 'data/platforms.json').read_text()))
    return sorted(urls)
