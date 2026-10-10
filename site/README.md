# Searchable directory

The static website is generated from the current root `README.md` and `COMMUNITIES.md`; do not maintain a second resource list in the website. Explicit, sourced platform tags live in `data/platforms.json`.

Features include text search, combined category/platform/country filters, resource/community views, result counts, pagination, shareable filter URLs, empty states, keyboard access and a small-screen layout. Entries are rendered as text rather than trusted HTML. There are no application accounts, analytics, third-party scripts or runtime data requests.

## Build and preview

From the repository root:

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests
python3 scripts/build_site.py
python3 -m http.server 8000 --directory site/dist
```

Open `http://localhost:8000`. The generated `site/dist` directory can be hosted by a static host. For a branch preview, use `python3 scripts/build_site.py --ref BRANCH_NAME`; guide and source-entry links then point to that branch. The static output is not committed.

## Hosted copy

The static directory is ready to build and host. Hosted publishing is pending: the upload tool rejected the required sandbox approval in this session. No live deployment is claimed. Repository changes do not automatically publish a hosted copy.

The repository validation workflow builds and uploads a `searchable-directory` artifact for every PR and main-branch update. Downloading that artifact gives the exact generated website for that commit. To host publicly on GitHub Pages or another provider, deploy those static files using that provider's hosting configuration.

## Maintaining filters

Add a platform only when the project documents support and include the evidence URL in `data/platforms.json`. Untagged entries stay searchable and appear with “All platforms”; they do not imply incompatibility. Country and region come from the community headings, not from guessed IP locations. The original merge audit remains dated evidence rather than the live data source.
