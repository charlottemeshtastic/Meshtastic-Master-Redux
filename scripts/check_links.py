"""Check current public references without rewriting content or historical evidence."""
import argparse
import collections
import concurrent.futures
import datetime
import ipaddress
import json
import pathlib
import re
import socket
import subprocess
import sys
import time
import urllib.parse
from catalog import ROOT, public_urls

SOCIAL = ('discord.com', 'discord.gg', 'facebook.com', 'instagram.com', 'linkedin.com', 't.me', 'matrix.to')


def classify(code, error='', title='', url='', final=''):
    if error:
        return 'unverified'
    if code in (404, 410):
        return 'broken'
    if code in (401, 403, 429) or any(term in title.lower() for term in ('just a moment', 'attention required', 'access denied', 'captcha', 'sign in', 'log in')):
        return 'blocked'
    if 200 <= code < 400:
        if any(term in title.lower() for term in ('coming soon', 'domain for sale', '404 not found')):
            return 'review'
        host = (urllib.parse.urlsplit(url).hostname or '').lower().removeprefix('www.')
        if host in SOCIAL:
            return 'membership-unverified'
        return 'redirected' if final and final != url else 'reachable'
    return 'unverified'


def public_target(url):
    """Do not let submitted links or redirects probe local/private network addresses."""
    p = urllib.parse.urlsplit(url)
    if p.scheme not in ('http', 'https') or not p.hostname or p.username or p.password or p.port not in (None, 80, 443):
        return False
    try:
        addresses = socket.getaddrinfo(p.hostname, p.port or (443 if p.scheme == 'https' else 80), type=socket.SOCK_STREAM)
        return bool(addresses) and all(ipaddress.ip_address(a[4][0]).is_global for a in addresses)
    except (socket.gaierror, ValueError):
        return False


def request(url, timeout):
    result = subprocess.run(['curl', '--silent', '--show-error', '--max-time', str(timeout), '--max-filesize', '2097152',
                             '--proto', '=http,https', '--user-agent', 'Meshtastic-Master-Redux-LinkCheck/1.0',
                             '--dump-header', '-', '--write-out', '\nCHECK%{http_code}', url],
                            capture_output=True, text=True, errors='replace', timeout=timeout + 3)
    payload, _, code = result.stdout.rpartition('\nCHECK')
    return int(code) if code.isdigit() else 0, payload, result.stderr[:300], result.returncode


def check_one(url, timeout=15, requester=request, target_check=public_target):
    current, hops, payload, code, error = url, [], '', 0, ''
    try:
        for _ in range(9):
            if not target_check(current):
                return {'url': url, 'status': 'unverified', 'code': None, 'final': current, 'detail': 'Target did not resolve to a permitted public address', 'redirects': hops}
            code, payload, error, returncode = requester(current, timeout)
            if returncode:
                error = error or f'curl exited with status {returncode}'
                break
            if code in (301, 302, 303, 307, 308):
                blocks = re.split(r'\r?\n\r?\n', payload)
                headers = []
                for block in blocks:
                    if not block.startswith('HTTP/'):
                        break
                    headers.append(block)
                header = headers[-1] if headers else ''
                location = re.search(r'^location:\s*(.+)$', header, re.I | re.M)
                if not location:
                    error = 'Redirect without Location header'; break
                next_url = urllib.parse.urljoin(current, location.group(1).strip())
                hops.append(next_url); current = next_url
                continue
            # Confirm a removal status with a second request rather than a transient response.
            if code in (404, 410):
                time.sleep(0.1)
                second, body, err, rc = requester(current, timeout)
                if second != code or rc:
                    error = 'Removal status was not confirmed by a second request'
                else:
                    payload = body
            break
        else:
            error = 'Too many redirects'
    except (subprocess.TimeoutExpired, ValueError) as exc:
        error = str(exc)
    title = re.search(r'<title[^>]*>(.*?)</title>', payload, re.I | re.S)
    title = re.sub(r'\s+', ' ', title.group(1)).strip()[:240] if title else ''
    status = classify(code, error, title, url, current)
    return {'url': url, 'status': status, 'code': code, 'final': current, 'title': title, 'detail': error, 'redirects': hops}


def markdown_report(results, checked):
    counts = collections.Counter(r['status'] for r in results)
    lines = ['# Current link check', '', f'Checked: {checked}', '', f'{len(results)} URLs: '+', '.join(f'{k}: {v}' for k, v in sorted(counts.items())), '',
             'Only twice-confirmed HTTP 404/410 responses fail this check. Blocked pages, private group shells, DNS failures, TLS errors, timeouts and other server failures remain inconclusive. Page functionality and URL fragments are not tested.', '',
             '| Status | URL | HTTP | Detail |', '| --- | --- | --- | --- |']
    for r in results:
        if r['status'] in ('reachable', 'redirected'):
            continue
        detail = (r.get('detail') or r.get('title', '')).replace('|', '\\|').replace('\n', ' ')
        # Escape all submitted content: report text cannot close the table or inject HTML.
        import html
        url = html.escape(r['url']).replace('|', '%7C').replace('`', '&#96;')
        lines.append(f"| {r['status']} | {url} | {r.get('code') or '—'} | {html.escape(detail)} |")
    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='work/link-checks')
    parser.add_argument('--only-new', action='store_true', help='Check URLs absent from the original audit URL list')
    parser.add_argument('--limit', type=int, help='Bounded smoke check; omitted checks the full current index')
    args = parser.parse_args()
    urls = public_urls()
    if args.only_new:
        historical = {r['url'] for r in json.loads((ROOT / 'audit/links.json').read_text())['results']}
        urls = [u for u in urls if u not in historical]
    if args.limit is not None:
        urls = urls[:args.limit]
    checked = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(check_one, urls))
    output = pathlib.Path(args.output); output.mkdir(parents=True, exist_ok=True)
    (output / 'results.json').write_text(json.dumps({'checked_utc': checked, 'results': results}, indent=2))
    report = markdown_report(results, checked)
    (output / 'report.md').write_text(report)
    print(report.split('\n\n')[2])
    return 1 if any(r['status'] == 'broken' for r in results) else 0


if __name__ == '__main__':
    sys.exit(main())
