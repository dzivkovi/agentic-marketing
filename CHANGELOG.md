# Changelog

All notable changes to this project are recorded here. Tag annotations remain minimal; narrative detail lives in this file. For editorial reasoning behind individual additions, see [CURATION-LOG.md](CURATION-LOG.md).

## v2.0 - Tool-review methodology and README repositioning

Two threads land in this release. First, a reproducible procedure for assessing marketing AI tools against the 8-verb Anatomy was developed, validated across four vendors, and published with its first public review. Second, the README shifts from origin-story-first to framework-first, surfacing the methodology as the rare asset the repo now offers.

- **Tool Review Procedure (v0.2).** A 5-leg methodology (internal grep → tool docs → wrapper/runtime search → alternatives → verdict) that produces a 3-state classification (`Wrapper` / `Hybrid` / `Hard`), persona-relative skill-gap, verb fit, and vendor-official runtime check. Invocable as `/review-tool <name>` via the slash-command at [`.claude/commands/review-tool.md`](.claude/commands/review-tool.md); full methodology at [`specs/tool-review.md`](specs/tool-review.md).
- **First public tool review: ScrapeCreators.** Classified **Wrapper** with **No gap across four personas** (marketing consultant, solo creator, GTM engineer, MMM analyst) because the vendor ships a first-class agent trifecta — hosted MCP, official CLI, and Agent Skill. Published at [research/tool-reviews/scrapecreators.md](research/tool-reviews/scrapecreators.md).
- **Vendor companion and awesome list additions.** SENSE tier now includes ScrapeCreators (multi-platform scraping API, 27+ platforms incl. Meta/Google/LinkedIn ad libraries). The awesome list adds the vendor-authored [ScrapeCreators/agent-skills](https://github.com/ScrapeCreators/agent-skills) next to last30days-skill.
- **README repositioning.** "What This Project Is" becomes "What's Inside" — a three-asset inventory (Anatomy / Awesome List / Tool Review Procedure) with self-routing entry points. A prominent new section surfaces the Tool Review Procedure and explains the spec-vs-command distinction. The "From Fishing to Marketing" origin story moves entirely to [ABOUT.md](ABOUT.md), where the fuller narrative already lived. Fishing photo and IMU certificate images follow.
- **Riders of AI.** A two-sentence bridge in ABOUT.md names the hybrid role this framework is meant to serve: product-minded technologists and tech-savvy product managers who learn to direct agents rather than build them.

Editorial context: see the 2026-04-19 entries in [CURATION-LOG.md](CURATION-LOG.md).

## v1.2 - Audit-driven content pass

Parallel adversarial audits of the v1.1 content surfaced star-count drift, author-voice-vs-curator-voice leakage, unverified Gartner claims, and overlapping revision-tracking mechanisms. This release hardens all three.

- **Revision tracking consolidated.** `CHANGELOG.md` now owns the release trail, tag annotations stay terse, [CURATION-LOG.md](CURATION-LOG.md) keeps its editorial-journal role. Release Process codified in `CLAUDE.md`.
- **Awesome list hardened.** Star counts refreshed via the GitHub API; repo-root links converted to deep links for `realjaymes`, `ericosiu`, and `pawbytes`; URL moves applied (`BrianRWagner/ai-marketing-claude-code-skills`, `a2aproject/A2A`); puffery quoted-and-attributed or neutralized; unverifiable "Linux Foundation MCP" and `gnoviawan` provenance notes dropped.
- **Vendor companion corrected.** Heap flagged as Contentsquare-acquired (Dec 2023); Dynamic Yield "400+" softened to "~300 per vendor's own pages"; WordPress 43%-of-sites and ~60%-CMS-share figures separated; Contentstack and Sitecore Gartner claims removed as unverifiable; enterprise size-fit bumped to E:● for vendors with explicit enterprise tiers (WordPress VIP, Shopify Plus, Canva Enterprise, HubSpot Enterprise); new Stack Notes and Out of Scope sections call out Adobe/Salesforce integration and intentional omissions.

Editorial context: see the 2026-04-17 entries in [CURATION-LOG.md](CURATION-LOG.md).

## v1.1 - Curation log, verb visibility, SENSE expansion

- Surface the 8 marketing verbs directly in README so readers see the framework without clicking through to the Anatomy.
- Add [CURATION-LOG.md](CURATION-LOG.md): editorial journal for compound learning during skill curation (caveats, gaps, patterns, open questions).
- Add `last30days-skill` to SENSE (cross-platform trend aggregator).
- Register the curation log in CLAUDE.md and the README project structure.

Editorial context: see the 2026-04-13 entries in [CURATION-LOG.md](CURATION-LOG.md).

## v1.0 - Peer-reviewed Agentic AI Marketing framework

Initial public release of the Anatomy, vendor companion, and awesome list.

- 7 commandments, 8 universal marketing verbs, scored inventory of 40+ activities.
- 3-tier sizing model (Solo / SMB / Enterprise) applied across every row.
- Awareness to affinity to trust to transaction framing in Section 2.
- Size Fit column across every row of the scored inventory using the `●` essential / `◐` helpful / `-` skip notation (Section 3).
- Sourcing Cheat Sheet per tier in Section 3.10 so a reader can locate themselves and know whether to DIY, augment, or buy.
- Vendor listings split out into [research/Marketing-Vendors-By-Category.md](research/Marketing-Vendors-By-Category.md) so the Anatomy stays clean and the vendor list can grow independently.
- [AWESOME-MARKETING-SKILLS.md](AWESOME-MARKETING-SKILLS.md) seeded with open-source skills organized by the 8 verbs.
