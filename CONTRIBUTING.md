# Contributing

Use the [resource, broken-link and community templates](https://github.com/charlottemeshtastic/Meshtastic-Master-Redux/issues/new/choose), or submit a [pull request](https://github.com/charlottemeshtastic/Meshtastic-Master-Redux/pulls) to add, correct or remove a resource. Use this repository as the maintenance point for the merged index.

- Choose the appropriate README category or community country/region.
- Use `- [Name](https://example.org/) — A short factual description.` and sort entries alphabetically within their section.
- Prefer the maintainer's canonical HTTPS URL. Check redirects, titles and existing entries before adding another link.
- Keep distinct source-code and contact channels when they serve different purposes. Avoid duplicate landing pages and invite aliases.
- State whether a resource is official, community maintained, archived or related inspiration. Vendor links are not endorsements.
- Provide a public source for capability, platform, location or license claims. Avoid unverified prices, performance guarantees and rankings.
- If a link is blocked or requires login, record the limitation rather than declaring it dead. Historical resources belong in the audit review queue.
- Update the audit evidence when resolving an entry and run `python3 scripts/validate.py` from the repository root.

The audit records the initial source merge and is a dated snapshot. Later additions should document their source and check date in the PR; do not alter historical audit results to imply they were checked later.

Contributions to the index are released under CC0, as described in [attribution](ATTRIBUTION.md). Do not copy linked code or media without checking its separate license. Keep discussions respectful, useful and free of harassment or private information.

`meshtastic.local` is a local network/device address, not a public website. Consult [official web-client documentation](https://meshtastic.org/docs/software/web-client/) for current local client support.

## Website and checks

The directory builds from the current Markdown index. Add platform tags and their evidence URL in `data/platforms.json` when documented. Run the validator, tests and [website build](site/README.md) after changing resources. See [maintenance](docs/MAINTENANCE.md) for weekly link reports and release steps.
