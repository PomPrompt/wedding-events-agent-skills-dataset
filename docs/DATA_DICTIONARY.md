# PomPrompt Wedding & Events — Dataset 01 Data Dictionary

Snapshot date: **2026-10-31**. Dataset purpose: public-link discovery and provenance ONLY. No technical, licensing, execution, security, or compatibility audit.

## Record contract

The CSV follows `05_DATASET01_EMPTY_TEMPLATE.csv` in exact order, and the JSON is an array conforming to `06_DATASET01_SCHEMA.json`. The two files contain the same core records and identical values; CSV `tags` uses `|` separators and JSON `tags` uses string arrays. CSV is UTF-8 with a BOM for spreadsheet import; JSON is UTF-8.

| Field | Type | Meaning |
|---|---|---|
| `id` | string | Local stable identifier `WES-0001` onward. |
| `skill_name` | string | Name as identified from the public individual skill page; qualifying parentheses distinguish unrelated same-name projects. |
| `skill_url` | HTTPS URL | Preferred individual skill page or dedicated GitHub repository with identifiable SKILL.md. |
| `source_website` | string | Host/domain of the retained skill URL, not the skill author's name. |
| `discovery_page_url` | HTTPS URL | Public entry point to the exact skill; this snapshot often uses the individual Skill page itself because external keyword search results are not stable. |
| `primary_category` | `C01`–`C21` | One code from the source-provided category taxonomy. |
| `tags` | list of unique strings | Editorial lowercase topic tags; pipe-delimited in CSV. |
| `relevance_tier` | `A`, `B`, `C` | Core accepts A and B only. |
| `scope` | enum string | Explicit wedding specificity and applicable creative/event scope, per the attached JSON schema. |
| `short_description` | original English string | Concise editorial summary of public use case, not copied source instructions. |
| `discovered_at` | `YYYY-MM-DD` | Date the page was researched for this snapshot, **not** original publication date. |
| `link_check_status` | enum string | Exactly what link checking established; not an execution or security status. |
| `evidence_url` | HTTPS URL | Public individual page whose visible title/description supports inclusion. |
| `notes` | string | Concise factual observation and any alias / language / identity caveat. |

## Link statuses

- `page_observed`: a specific individual Skill page was opened and its content observed by the web research tool.
- `http_verified`: an independent successful HTTP response was checked. Not used for this snapshot.
- `search_result_only`: only an indexed excerpt or listing was observed; such candidates remain in leads.
- `inaccessible`: the individual candidate page could not be accessed, including a timeout; keep pending.
- `broken`: a failed/dead candidate URL observed, such as a 404; keep pending.

## Tier definitions and core inclusion

- **A**: a genuine Agent Skill primarily and explicitly about wedding workflow or wedding content.
- **B**: a genuine general-purpose Agent Skill whose public description specifically mentions wedding or directly wedding-related celebrations (engagement, bridal shower, bachelor/bachelorette).
- **C**: generic, adjacent, or uncertain wedding applicability; retain as leads, not core.

No bundle/index-only URL can be a core `skill_url`. Similar names do not prove identity: compare author, underlying repository/skill slug, visible source commit when available, and explicit declarations. Keep separate unrelated original Skills even when titles match. Probable but unproven duplicates remain pending. Redirect aliases are normalized to the observed preferred page. No runtime tests were performed.

## Category codes

| Code | Category |
|---|---|
| C01 | Wedding Planning & Checklists |
| C02 | Timelines & Run of Show |
| C03 | Wedding Budgeting |
| C04 | Guest Lists & RSVP |
| C05 | Seating & Tables |
| C06 | Wedding Invitation Design |
| C07 | Invitation Copywriting |
| C08 | Wedding Photography Planning |
| C09 | AI Wedding Image Creation |
| C10 | Wedding Video & Highlights |
| C11 | Wedding Decoration & Styling |
| C12 | Venues & Vendor Management |
| C13 | Contracts & Documents |
| C14 | Ceremony Scripts & Speeches |
| C15 | Menus & Catering |
| C16 | Wedding Websites & Digital Assets |
| C17 | Prewedding & Related Parties |
| C18 | Birthdays & Anniversaries |
| C19 | Baby Showers & Family Events |
| C20 | Event Marketing & Guest Communications |
| C21 | General Event Operations |


## Other file formats

- `SOURCES_USED.csv`: observed primary source domains and counted retained core records, plus collection/access notes.
- `LEADS_PENDING.csv`: `lead_id`, `skill_name`, `candidate_url`, `source_website`, `relevance_tier`, `link_check_status`, `reason`, `evidence_url`, `discovered_at`, `notes`. Leads may include URLs failing direct access and directory listings explicitly marked as such.
- `DUPLICATE_MAP.csv`: `duplicate_candidate_url`, `retained_skill_url`, `dedup_reason`, `evidence_url`, `discovered_at`. Counts listing aliases, not distinct source assets.

`null` or blanks indicate unknown data; never treat them as confirmed facts. The core schema requires all 14 keys, so optional unknown editorial notes are represented as empty strings when necessary. Missing required identifying URL or relevance evidence excludes a candidate from core.
