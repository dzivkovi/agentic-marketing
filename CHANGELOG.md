# Changelog

All notable changes to this project are recorded here. Tag annotations remain minimal; narrative detail lives in this file. For editorial reasoning behind individual additions, see [CURATION-LOG.md](CURATION-LOG.md).

## v2.1 - GEO category formalized across MEASURE + SENSE + SHIP

AI-answer-engine visibility is becoming the new search visibility. When a prospect asks ChatGPT, Perplexity, or Google AI Overviews "what's the best X for Y?", being cited in the answer is rapidly becoming as consequential as ranking first on Google was a decade ago. Gartner is calling for a 25% drop in traditional-search volume in 2026 alone. Practitioners are reaching for a vocabulary to name the new discipline: GEO (Generative Engine Optimization), sometimes called AEO (Answer Engine Optimization).

Before this release, the Anatomy treated GEO as a content-optimization sub-activity under SHIP. That captured the "write for AI engines" side, but not the "track whether you're cited" (MEASURE) or "know what people are asking AI" (SENSE) sides. Marketing teams doing real GEO work had no named rows to map their work to, and tool reviewers had no structural guard against reporting a category as covered when only one of its verbs was. This release closes both gaps:

- Two new scored activities name the missing sides of GEO.
- A new Vendor Companion row + AWESOME list subsection give reviewers and readers a place to put AI-visibility tools.
- The Tool Review Procedure bumps to v0.3 with a category-coverage matrix that forces per-verb coverage checks before synthesis.
- A terminology house rule is codified: GEO is the taxonomy term; AEO is preserved where vendors use it for their own products.

The first review in the category (Profound) is held private pending sibling-vendor reviews and pricing re-verification.

Details:

- **Anatomy additions.** Two new rows in the scored inventory: SENSE `Prompt-demand sensing (GEO)` (U:30 x L:75 = 23, T3) and MEASURE `AI-visibility tracking (GEO)` (U:40 x L:80 = 32, T3). The existing SHIP row (`SEO / GEO content strategy`, T1 at 60) now cross-references both new rows so readers see the multi-verb picture. Scores are conservative starters; revisit as the category matures.
- **Tool Review Procedure v0.3.** Adds a **category-coverage matrix** in Leg 1: for tools in an emerging or multi-verb category, the reviewer checks each applicable verb separately (Anatomy / Vendor Companion / AWESOME) and reports per-verb coverage, not a single "category absent/present" claim. Leg 5 synthesis now requires naming any `N` or `Partial` cell explicitly. Driven by the Profound review's initial overstatement ("category absent" when SHIP was covered). See [`specs/tool-review.md`](specs/tool-review.md).
- **Vendor Companion additions.** Profound rows under MEASURE (primary) and SENSE (secondary, Prompt Volumes dataset). AEO is preserved as the vendor's preferred term in Notes; GEO is used for category-level descriptors.
- **Awesome list addition.** New cross-cutting subsection `AI Visibility (GEO)` seeded with Profound MCP (vendor-official hosted + local + Python + TypeScript SDKs, launched 2026-03-31).
- **Terminology house rule.** GEO is the primary house term (matches ~59% dominant usage among SEO influencers, Andreessen Horowitz's May 2025 thesis, Search Engine Land, academic origin). AEO is acknowledged as vendor-preferred (Profound, HubSpot) and preserved in vendor-specific notes; not adopted into the taxonomy.
- **First GEO-space tool review: Profound.** Held private in [`work/tool-reviews/profound.md`](work/tool-reviews/profound.md) pending sibling-vendor reviews (Peec AI, Promptwatch, Otterly, Scrunch) and pricing re-verification post-Series-C.

Editorial context: see the 2026-04-19 entries in [CURATION-LOG.md](CURATION-LOG.md) titled `Terminology decision: GEO adopted as house term over AEO`, `GEO formalized as a multi-verb category in the Anatomy`, `Procedure v0.3: category-coverage matrix after Profound self-correction`, and `Pattern: pricing-floor-as-persona-gate`.

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
