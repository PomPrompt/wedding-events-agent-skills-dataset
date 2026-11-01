# Wedding & Events AI Agent Skills — Discovery Dataset 01

[![License: CC BY 4.0](https://img.shields.io/badge/data%20%26%20docs-CC%20BY%204.0-lightgrey.svg)](LICENSE.md)

**Publisher:** PomPrompt · **Research snapshot:** 2026-10-31 · **Dataset version:** 1.0.0 (first release planned)

> A source-linked **discovery dataset**, **not** a collection of downloadable third-party Skills and **not** a ranking or security audit. This repository is separate from [PomPrompt's eight first-party wedding Skills](https://github.com/PomPrompt/wedding-events-agent-skills-). The two repositories serve different purposes and must not be merged.

## What is included

The dataset indexes individually published AI Agent Skill pages whose public descriptions explicitly connect to weddings or associated celebration workflows. Records contain source/evidence links and original short English summaries. They do **not** include third-party `SKILL.md` files, scripts, media, guest data, or copyrighted source assets.

| Snapshot metric | Count |
| --- | ---: |
| Unique core Skill links | **45** |
| A — Wedding-specific | **19** |
| B — Explicit wedding application | **26** |
| Pending leads (outside core) | **16** |
| Deduplicated alternative URLs | **5** |
| Primary source domains | **6** |
| Historical `page_observed` status | **45** |
| Independently `http_verified` in data | **0** |

The 100–200 record goal was **not** met; no placeholders were added. The recorded `page_observed` status describes what the original collection process saw on **2026-10-31**, **not** a promise that every page currently opens or returns HTTP 200. Some pages could not be re-opened during a later spot review; no blanket re-verification is claimed.

## Canonical research and archive

- **Original PomPrompt research page (planned; verify its deployment):** https://pomprompt.com/datasets/wedding-events-agent-skills/
- **Technical repository (suggested destination; verify creation):** https://github.com/PomPrompt/wedding-events-agent-skills-dataset
- **Zenodo DOI:** _not assigned as part of this package._ Add only the actual DOI after a successful public deposit.

**Do not cite a DOI, GitHub Release, or website page as live until it actually exists.** The PomPrompt site is intended to explain methodology, caveats, findings, visualizations and corrections; GitHub contains machine-readable data and version history; Zenodo is the versioned archival copy.

## Download the data

| File | Purpose |
| --- | --- |
| [Core CSV](data/WEDDING_EVENTS_SKILLS_DATASET01.csv) | 45 records × 14 columns, tags separated by `|` in CSV |
| [Core JSON](data/WEDDING_EVENTS_SKILLS_DATASET01.json) | Same records with `tags` arrays |
| [Sources used](data/SOURCES_USED.csv) | Primary source domain and count evidence |
| [Pending leads](data/LEADS_PENDING.csv) | Unconfirmed/adjacent/inaccessible candidates |
| [Duplicate map](data/DUPLICATE_MAP.csv) | Supported alternative listings |
| [Data dictionary](docs/DATA_DICTIONARY.md) | Field definitions and categories |
| [Arabic collection report](docs/COLLECTION_REPORT.md) | Research methods, evidence limits and detailed counts |
| [Next queries](docs/NEXT_RESEARCH_QUERIES.md) | Gaps and search backlog |
| [JSON Schema](schema/06_DATASET01_SCHEMA.json) | Official validation contract |
| [Category taxonomy](schema/02_CATEGORY_TAXONOMY.csv) | 21 classification categories |

## Methodology and data limits

**Inclusion tiers:** A = wedding-specific; B = public description explicitly connects a general event/creative Skill with weddings; C = adjacent or unconfirmed, **excluded from core**. A search hit, homepage or directory category is never substituted for a specific Skill page. Identity-based deduplication keeps unrelated authors' similarly named Skills separate. Alternative listings are recorded independently.

**Verification is only discovery:** Inclusion does not mean that a Skill was installed, executed, inspected for malicious behavior, audited for license compatibility, endorsed, or proven to work on a particular AI agent. Do not reuse third-party Skill assets solely because a link appears here. Individual source sites may change or go offline. See [Collection Report](docs/COLLECTION_REPORT.md) and [Data Dictionary](docs/DATA_DICTIONARY.md).

## How to validate the dataset locally

Run with Python 3.10+:

```bash
python3 -m pip install 'jsonschema>=4,<5'
python3 scripts/validate_dataset.py
```

The validator checks JSON Schema Draft 2020-12 (when the dependency is present), record IDs and duplicates, URL syntax, correct date formats, CSV/JSON equivalence, allowed categories, counts by source and matching copies in `site/data`. **It does not fetch the web or execute any third-party Agent Skill.** A read-only GitHub Actions workflow runs the same checks on pushes and pull requests.

## Repository layout

```text
README.md · LICENSE.md · LICENSE_SCOPE.md · CITATION.cff · CHANGELOG.md
CONTRIBUTING.md · .gitignore
data/                 Primary CSV/JSON and source/leads/duplicate tables
docs/                 Research report, dictionary, follow-up queries, publication checklist
schema/               Official JSON Schema and category taxonomy
scripts/              Offline validator and its separate MIT license
.github/              Data-correction issue form and CI validation
site/                 Optional website page source and its matching static download assets
```

The files under `site/data` intentionally mirror selected records and reports in `data`/`docs` **for optional static hosting**, not to create another dataset. The validator checks that each mirror is byte-for-byte equal. If PomPrompt.com is deployed from another codebase, these `site/` files are **optional** and should not be copied into the live Skills repository.

## Rights and licenses

**Original PomPrompt data compilation, short editorial summaries, reports and original webpage:** [CC BY 4.0](LICENSE.md), **only** to the extent PomPrompt controls the rights. **Validator script:** [MIT](scripts/LICENSE). Read [exact license scope](LICENSE_SCOPE.md).

The independent third-party Skills, their names, source websites, `SKILL.md` contents, scripts, images and trademarks are **not** licensed by PomPrompt. Facts and links are cited as provenance, not claimed as exclusive property. Public GitHub visibility is not itself a license.

**Publisher check before public release:** confirm authorship and permission to license original material under CC BY 4.0 and the validator under MIT; if rights are uncertain, do not treat this notice as authority to license third-party materials.

## Cite and contribute

See [CITATION.cff](CITATION.cff) for machine-readable citation metadata. Snapshot date is **2026-10-31**, not necessarily publication date. Add the true release date at the time of the GitHub Release and the actual Zenodo DOI after publication.

To report a correction or propose a new link, follow [CONTRIBUTING.md](CONTRIBUTING.md) or open the [data correction issue template](.github/ISSUE_TEMPLATE/data-correction.md). **Never** include private wedding guest details, personal photographs or third-party source file dumps.
