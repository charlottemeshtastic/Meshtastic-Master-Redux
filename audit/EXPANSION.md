# Index expansion — 2026-10-09

This follow-up adds 16 official documentation resources, bringing the current index to 419 entries (123 resources and 296 community entries). It leaves the original CC0 license, source repositories and initial audit unchanged.

Added first-message navigation, configuration/troubleshooting guidance, Linux/Raspberry Pi references, deployment planning and a solar-energy worksheet. Guidance links to current official references; hardware performance, private-group membership and regulatory compliance are not certified by this index.

The static directory is generated from live Markdown with explicit, sourced platform tags. It includes search, combined filters, pagination, empty states and shareable views. Resource additions do not require editing the historical audit or maintaining a duplicate website list.

Contribution forms cover new resources, broken links and community changes. PR validation and weekly link-check workflows use read-only repository permissions, pinned action revisions, no secrets and no automatic issue/content edits. The weekly workflow is active once this PR is merged into the default branch.

## Validation

- Offline structural checks: PASS for 419 unique current entries, Markdown files/headings, platform evidence, original source-row accounting and exact CC0 license blob.
- Eight Python regression tests: PASS, including confirmed removals, transient responses, proxy redirect headers and private-address redirect refusal.
- Directory filter regression checks and JavaScript syntax: PASS.
- Static build: PASS; the preview server returned HTTP 200.
- Full current network check: 446 URLs. 265 reachable, 29 redirected, 135 public social shells with membership unverified, 6 blocked, 11 inconclusive and **zero confirmed broken links**. See [raw results](EXPANSION_LINKS.json).
- The initial Python documentation path returned a confirmed 404 during verification; it was replaced with the official `/docs/software/python/cli/` page before the successful full check.
- Browser automation had no available browser surface. Visual layout, keyboard focus and interaction in a real browser remain unverified; automated filter/build checks passed.

The new audit checker reads the current index and guides. Blocked responses and errors are retained as inconclusive; only twice-confirmed HTTP 404/410 responses fail the scheduled check. Private Sites access and the GitHub issue form may require sign-in and are expected to appear blocked to an unauthenticated checker.

Hosted publishing remains pending because the upload tool rejected the required sandbox approval. The complete static build is available as a downloadable deliverable.
