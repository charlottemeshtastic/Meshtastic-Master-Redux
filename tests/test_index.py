import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'scripts'))
from catalog import ROOT, identity, resources
from build_site import build
from check_links import check_one, classify, markdown_report


class CatalogTests(unittest.TestCase):
    def test_current_index_includes_sources_and_new_references(self):
        entries = resources()
        self.assertEqual(sum(r['category'] == 'Communities' for r in entries), 296)
        self.assertGreater(len(entries), 403)
        urls = {r['url'] for r in entries}
        self.assertIn('https://meshtastic.org/docs/meshtasticd/', urls)
        self.assertIn('https://meshtastic.org/docs/software/mpwrd-os/', urls)
        self.assertEqual(len(urls), len(entries))
        canada = [r for r in entries if r['country'] == 'Canada']
        self.assertTrue(any(r['region'] == 'Alberta' for r in canada))
        self.assertFalse(any('web.archive.org' in r['url'] for r in entries))

    def test_invite_aliases_and_host_case(self):
        self.assertEqual(identity('https://discord.gg/AbC/'), identity('https://discord.com/invite/AbC'))
        self.assertEqual(identity('https://gitHub.com/Meshtastic/Python/'), identity('https://github.com/meshtastic/python'))
        self.assertNotEqual(identity('https://t.me/GroupA'), identity('https://t.me/GroupB'))

    def test_build_has_full_catalog_and_safe_json(self):
        with tempfile.TemporaryDirectory() as directory:
            entries = build(directory, 'enhance/guides-directory-maintenance')
            page = (pathlib.Path(directory) / 'index.html').read_text()
            self.assertIn(str(len(entries)) + ' curated entries', page)
            self.assertNotIn('@@', page)
            self.assertIn('data-source-ref="enhance/guides-directory-maintenance"', page)
            self.assertTrue((pathlib.Path(directory) / 'filters.js').is_file())
            # Only the data script's closing tag appears, even if a name contained HTML.
            self.assertIn('type="application/json">', page)
            self.assertIn('filters.js', page)


class LinkCheckTests(unittest.TestCase):
    def test_uncertain_responses_do_not_mean_removed(self):
        for status in [401, 403, 429]:
            self.assertEqual(classify(status), 'blocked')
        self.assertEqual(classify(522), 'unverified')
        self.assertEqual(classify(200, 'certificate failure'), 'unverified')
        self.assertEqual(classify(200, title='Just a moment...'), 'blocked')
        self.assertEqual(classify(200, title='Example — Coming Soon'), 'review')
        self.assertEqual(classify(200, url='https://discord.gg/abc'), 'membership-unverified')

    def test_removal_requires_two_matching_checks(self):
        calls = []
        def request(url, timeout):
            calls.append(url)
            return 404, 'HTTP/2 404\n\n<title>Not found</title>', '', 0
        r = check_one('https://example.org/missing', requester=request, target_check=lambda _: True)
        self.assertEqual(r['status'], 'broken')
        self.assertEqual(len(calls), 2)
        responses = iter([(404, '', '', 0), (200, '', '', 0)])
        r = check_one('https://example.org/flaky', requester=lambda *_: next(responses), target_check=lambda _: True)
        self.assertEqual(r['status'], 'unverified')

    def test_public_redirect_with_proxy_headers(self):
        responses = iter([(301, 'HTTP/1.1 200 Connection established\n\nHTTP/2 301\nlocation: /new\n\n', '', 0), (200, '<title>Project</title>', '', 0)])
        r = check_one('https://example.org/old', requester=lambda *_: next(responses), target_check=lambda _: True)
        self.assertEqual(r['status'], 'redirected')
        self.assertEqual(r['final'], 'https://example.org/new')

    def test_private_redirect_is_not_requested(self):
        calls = []
        def request(url, timeout):
            calls.append(url)
            return 302, 'HTTP/2 302\nlocation: http://127.0.0.1/private\n\n', '', 0
        r = check_one('https://example.org/', requester=request, target_check=lambda u: '127.0.0.1' not in u)
        self.assertEqual(r['status'], 'unverified')
        self.assertEqual(calls, ['https://example.org/'])

    def test_report_escapes_submitted_html(self):
        report = markdown_report([{'url':'https://example.org/<script>', 'status':'blocked', 'code':403, 'detail':'<img>|bad\ntext'}], 'now')
        self.assertNotIn('<script>', report)
        self.assertNotIn('<img>', report)
        self.assertIn('&lt;img&gt;', report)


if __name__ == '__main__':
    unittest.main()
