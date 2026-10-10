# Merge audit — 2026-10-09

554 source resource rows → 413 normalized entries; 141 duplicate rows consolidated. 403 entries retained in the main index/community directory; 10 moved to the review queue.

## Link checks

471 unique source URLs checked: {'local-only': 1, 'reachable': 453, 'http-error': 6, 'unverified': 11}.

Checks use GET and system certificate validation with redirects and a 25-second timeout. Results reflect this environment and this date. HTTP 403/429, timeouts, certificate errors and login walls are inconclusive, not proof of removal. Social shells may return 200 despite an expired invite. URL fragments and application functionality were not tested. Repository titles/descriptions and official documentation were checked; third-party capability claims were shortened where they could not be substantiated. This is a resource audit, not a code/security/hardware test.

## Decisions

- Preserve CC0 license verbatim; credit ShakataGaNai, SignalGap and their contributors. Source repositories remain unchanged.
- Normalize host case, trailing slashes and Discord invite aliases. Consolidate duplicate App Store links, store landing pages and Hackaday numeric project IDs; retain distinct contact channels and secondary source links.
- Sort resources by task; separate the country/region community directory. Preserve distinct MeshLink and MeshLinkBeta repositories.
- Correct Android/Apple confusion by replacing platform prose with official documentation guidance. Remove unsupported vendor quality, price, ranking and privacy promises.
- Omit legacy RawGit badge, inherited branded media and source workflows requiring secrets or sending notifications.
- Do not adopt the unfinished Contributor Covenant contact placeholder; provide a small local contribution policy.
- Move definite HTTP 404/410 responses, parked pages and existing archival records into a review queue. Retain blocked links with visible status.
- A local meshtastic.local URL only works on a suitable local device/network; use official web-client documentation to determine support.

## Review queue

- [Israel Meshtastic Club](https://www.mesh-il.com) — **marked historical by source 2** (Israel).
- [AltaMesh](https://altamesh.net/) - Altadena, CA — **marked historical by source 2** (United States / California).
- [Southern Indiana Mesh Network](http://simnetwork.org/) — **parked/coming soon page** (United States / Indiana).
- [Served directly from an ESP32 based node](http://meshtastic.local) — **local device address; documented in contribution notes, not a public resource** (Official resources).
- ~~Israel Meshtastic Club~~ [Archived](https://web.archive.org/web/20250813160138/https://www.mesh-il.com/) — **historical archive** (Israel).
- ~~Meshtastic Latvija~~ [Archived](https://web.archive.org/web/20250125044231/https://mesh.dodies.lv/) — **historical archive** (Latvia).
- ~~TRMesh~~ - [Archived](https://web.archive.org/web/20241207225721/http://trmesh.org/) - (Website) — **historical archive** (Türkiye).
- ~~WiKi Meshtastic UA~~ - [Archived](https://web.archive.org/web/20241012101501/https://wikimesh.pp.ua/uk/home) — **historical archive** (Ukraine).
- ~~AltaMesh~~ - [Archived](https://web.archive.org/web/20250122193410/https://altamesh.net/) — **historical archive** (United States / California).
- ~~Shenandoah Valley Mesh~~ - [Archived](https://web.archive.org/web/20250216025925/https://svmesh.org/) — **historical archive** (United States / Virginia).

## Evidence

- [Added and normalized link checks](added-links.json): 46 URLs checked after editing; all returned HTTP 200.
- [Raw link results](links.json): every source URL, status, final URL and page title.
- [Resource provenance and duplicate decisions](resources.json): source file/line for every merged entry.
- [Official repository metadata](repository-metadata.json): archive status and project licenses.
- [Pinned sources and attribution](../ATTRIBUTION.md).

## Validation

Structural validation checks unique primary resource identities, local file targets, Markdown heading anchors, source-row coverage and license integrity. Network verification limitations are recorded above.

Validation result: PASS. All 554 source rows are accounted for across 413 identities and 141 duplicate decisions; all local Markdown targets and heading anchors resolve; the CC0 license matches the original Git blob exactly.

GitHub relocation redirects were applied for Meshinfo, the Matrix relay, the Discord bot, the Home Assistant entity builder and Harbor integration. Meshtastic-MQTT-Connect redirects to Connect and is consolidated into one entry. Stable releases/latest links remain unpinned.
