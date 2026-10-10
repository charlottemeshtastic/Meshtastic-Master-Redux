# Maintaining the index

[Back to the index](../README.md) · [Website build](../site/README.md)

The current Markdown files are the resource source. `audit/` preserves dated evidence; it must not be used as the current website catalog or silently rewritten to look recent.

## Every pull request

The validation workflow checks local files/headings, canonical resource uniqueness, platform evidence, preserved license/audit integrity, checker regression tests and directory filter behavior. It builds the static site and uploads a `searchable-directory` artifact. No external network check is required to pass a PR.

## Weekly link checks

The link-check workflow runs weekly on Monday at 09:00 UTC and can also be started manually after it reaches the default branch. It checks URLs in the live index, guides, attribution and platform evidence. Reports are attached to the workflow run and summarized there. This workflow does not edit entries, open issues or send external messages.

| Result | Meaning | Maintainer action |
| --- | --- | --- |
| reachable | A successful public response | Review content when a description changes |
| redirected | A successful response at another URL | Check whether the canonical entry should change |
| membership-unverified | A public social page responded | Confirm invite/member access manually if necessary |
| blocked | Login, CAPTCHA, 401/403 or rate limit | Retain and investigate; do not label removed |
| unverified | DNS, TLS, timeout, other server error or prohibited/local address | Recheck from another environment |
| review | A parked, coming-soon or soft-404 page | Verify relevance before retaining |
| broken | HTTP 404/410 confirmed twice | Find a replacement or propose a removal |

Only confirmed `broken` results fail the weekly workflow. Reports are dated and do not imply functional tests of software or validation of private-group membership. Redirect targets must resolve to public HTTP/HTTPS addresses; the checker does not follow local/private destinations. URL fragments are not checked.

Run a full manual check with `python3 scripts/check_links.py`; use `--only-new` to check references absent from the initial audit. Put fresh release evidence in a new dated report rather than changing the initial report.

## Hosted directory updates

The website source and build are part of the repository. A static build can be hosted anywhere. A hosted copy must be published separately; repository pushes do not publish it automatically. Rebuild and publish a matching version when releasing a site update. Scheduled GitHub reports also do not rewrite a hosted site's status badges: those labels describe the listed Markdown entry, not a live health monitor.
