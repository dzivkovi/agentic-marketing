# Changelog

All notable changes to this project are recorded here. Tag annotations remain minimal; narrative detail lives in this file. For editorial reasoning behind individual additions, see [CURATION-LOG.md](CURATION-LOG.md).

## v2.4 - The list got shorter, and it checks itself

The April awesome list was wide: seven skill packs, fifty-one deep links into individual skills, tools under every verb. Re-checked against the GitHub API on 2026-11-04, all twenty repositories were alive, but eighteen of the fifty-one deep links were dead, because maintainers rename and merge skills faster than a list is edited (one pack alone renamed seventeen skills in May). Six months of practitioner talk said the same thing about wide lists from the reader's side: skills that are "cool for about a day", repos collected "like Pokémon cards", and no marketing skill in the most-installed top ten of the largest registry. So the page was rebuilt around three jobs instead of coverage.

- **Packs and plugins, one table.** What is alive, what someone other than the vendor has used or reviewed, with the agent surface and install command, the price gate, and the facts from the check (stars, last push, release). Per-skill deep links are gone. Added since April: Anthropic's marketing and small-business plugins, Zapier's `gtm-cheat-codes`, ScrapeCreators' successor repo, newsjack, Semrush and Canva skill packs, HubSpot's CLI skills, DataForSEO's MCP and skill templates, `no-ai-slop`, `claude-seo`. Kept with refreshed facts: Corey Haines's `marketingskills` (now 53 skills, with the paid Magister layer disclosed), Eric Siu's pack, Adobe's. Three smaller packs kept on one line; three that went quiet named with their last-push month; gated giveaways described and not listed.
- **By verb, one table** that says where to look first, replacing eight per-verb tables of individual skills.
- **The GEO measurement stack**, free layers first (Search Console's AI reports, GA4 with its blindness noted, the free graders), then paid tracking under $100 a month, then the enterprise platforms including Conductor and Profound.
- **How to vet a skill before you install it**: seven rules and the numbers behind them (Snyk's ToxicSkills audit, the 31,000-skill study, SkillSpector's hit and false-positive rates). This section is the list's answer to the Anatomy's new 5.6 supply-chain rule.
- **Standards table updated**: Agent Skills under the Agentic AI Foundation with seventy-plus platforms, MCP's 2026-07-28 revision and its optional authentication, AGENTS.md, A2A's move, Composio's current shape. The April "AgenticSkills.io" label corrected, and agentskills.io distinguished from the third-party directory with the similar name.
- **`scripts/check_links.py`**: re-checks every GitHub link in the list (stars, last push, archived or renamed, dead deep links) and writes a dated report under `research/`. The list's "Checked" date is backed by a run, not a promise. The CURATION-LOG rule from July stands: the script reports facts; it does not grade.
- **The page says why it got shorter**, in the author's words, and ends with the same invitation the README now carries.

## v2.3 - First revalidation: scores re-checked against six months of practice

The scores were set in April 2026 and labelled estimates. Six months later they were tested against what practitioners did between May and October 2026: a corpus of recorded talks and tutorials read with timestamps, the newsletters of the creators the Anatomy cites, a web check of every external claim, and an independent review by a second model with no stake in the result. The dated evidence, quote by quote, is in [research/2026-11-04-six-month-revalidation.md](research/2026-11-04-six-month-revalidation.md). The method held; the numbers and three rules moved.

- **A date on the document.** The Anatomy now says "current as of 2026-11-04" under its title and on the scored table, with the next check set for April 2027, so a printout dates itself.
- **The scoring contract.** AI Leverage is now defined as net human effort saved per accepted deliverable, counting briefing, verification and rework. The Priority Score is named for what it is: an automation-opportunity index, not an investment priority.
- **Section 3.0, changed assumptions.** A short dated panel of the six things April took for granted that practice moved (writing as the easiest win, targeting as a marketer decision, approval on every action, audience intelligence as a quarterly asset, learning as a slow retrospective, the buyer as a person), each pointed at the verb it changes.
- **Thirteen scores moved, eleven up.** Competitive intelligence, voice of customer, audience profiling, persona mapping, ideation, the content calendar, planning, brand stewardship, video production, media buying, CRO, dashboarding and retrospectives rose. Content enrichment fell. The copy-drafting row, the April top score at 85, was split: drafts and variants from approved inputs keep 80; publishable copy under a named voice gets 55, because the practitioners with the largest audiences pulled AI out of the words that carry their name during 2026. Omnichannel repurposing is now the top row.
- **Eleven rows added**, each with two or more independent sources: the context layer (KNOW), the agent-readiness audit (SENSE), agent-readable pages and creator partnerships run with AI (SHIP), the taste profile as a ranking rubric (DECIDE), the brand design system as a skill and the anti-slop review pass (MAKE), AI-referral measurement and measuring the agents themselves (MEASURE), supervised learnings capture (LEARN), and the publishable-copy row above. The table now holds 49 activities. Eight single-source candidates are listed in Section 3.9 and held back.
- **MULTIPLY gets its transformations back.** Repurposing and localization moved from SHIP to MULTIPLY, which Section 2.6 had defined by them all along. Scores unchanged; the home changed.
- **Three commandments reworded from absolutes to operating rules.** Commandment 4: portable by design, proven by a run on a second host (the April "total portability" was contradicted by the cited creators' own migrations). Commandment 5: agents act within explicit authority and budgets; a human approves what cannot be undone (per-action approval decays into rubber-stamping at volume, and an approval instruction can be lost when an agent compacts its context). Commandment 7: observability plus limits; native platform tooling is preferred, not the acceptance test. Section 5 follows: 5.1 and 5.3 rewritten, agent identity and field separation added to 5.2, drift and memory integrity added to 5.5, a new 5.6 on operating limits (spend, turn and wall-clock caps, sandboxes, compensation actions, audit questions, agent-buyer validation).
- **KNOW owns the context layer.** Section 2.2 now says so, and drops "refresh quarterly": the files are revised from evidence on every run while a human curates what sticks. The tempo test from v2.2 stays as a classification test.
- **The agent reader.** One paragraph in Section 2: shopping agents that compare and buy have shipped in limited form, and an agent is moved by proof, prices and policies, not affinity.
- **Attributions re-checked.** Kieran Flanagan's and Grace Leung's held and grew. Chase AI's held, with two of the author's own slips corrected: "content cascade" is his term and was never retired, and Google Trends is not among his sources. Rick Mulready's six credits had been written from a summary of one video; checked against his transcripts, four hold under his own names (Launch-Ready plugin, Content Flywheel, brand-voice enforcer, Weekly Marketing Ops Automation), one was added (the Testimonial-to-Content Engine) and the brand-stewardship credit was dropped. Kieran Flanagan's title updated.
- **External facts.** Agent Skills is the standard's name (not "AgenticSkills.io") and it moved to the Agentic AI Foundation on 2026-10-22 with more than seventy platforms behind it. The body no longer names execution platforms (two of April's product names were already stale when published); current names live in the research file. The GEO pricing note ("enterprise paid-floor gates Solo") was corrected: basic AI-visibility tracking is now free to about $100 a month. Gartner's 25 percent figure is dated as a February 2024 forecast.
- **Three July 2026 recommendations finally applied**, from `research/2026-07-21-haines-flanagan-venn-vs-anatomy.md`: the context-layer rule, the human-curated refinement row, and the rule that usage rates are not a success metric.
- **README** carries the same KNOW wording and commandment summaries. **ROADMAP** marks the revalidation done and sets the next trigger.

What did not change: the eight verbs, the seven commandments as principles, the three size tiers, the Double Diamond and the co-creation model, Section 2.9's framework mapping, and the Section 6 exclusions (ENGAGE stays parked on its trigger; the Chase AI trim was narrowed to the reply automation).

## v2.2 - The Sense/Know line drawn, framework mapping, skills roadmap withdrawn

Six months of using the eight verbs in production surfaced one recurring confusion, and it was the author's own: when explaining the method to a room, KNOW kept blurring into SENSE. The verbs were right; the explanation was thin. This release fixes the explanation, adds the mapping to established frameworks that readers kept asking for, and removes the one part of the repo that promised more than it delivered.

- **The Sense/Know line.** Section 2.2 of the Anatomy now states the test that separates the two: tempo, not topic. Sense answers "what changed this week"; Know answers "who are we talking to and what do they bite on", and that answer should still hold next quarter. Two things that look like Know but are not are named: a verified market fact (a central-bank rate, a regulator's deadline, a published statistic) is Sense checked against its primary source, and brand voice or compliance rules are Make's guardrails. Know is only the reader. The README verb list carries the same line in one clause each for Sense, Know and Decide, and ABOUT.md gives all eight verbs in the fishing terms the method came from. The ruling was tested against an independent second model before it was written down, and it changed how an operating repo classifies its own fact-checking stage (from Know to Sense).
- **Section 2.9, mapping to established frameworks.** Kotler, SOSTAC, RACE and the 4Ps, verb by verb, with the gaps marked. The three gaps are the point: MAKE has no clean equivalent anywhere, the Sense/Know split exists in no established framework, and MULTIPLY is absent from all four. Added 2026-04-29 with the ENGAGE exclusion (section 6).
- **Skills roadmap withdrawn.** `skills/` held a roadmap and no skills, which a reader correctly reads as abandonment. Skills are built where they are used, inside the operating repos that run real marketing; the ones that prove general will be published here. Until then the repo makes no promise it is not keeping.
- **Research additions.** `research/2026-07-21-corey-haines-marketing-skills-corpus-research.md` and `research/2026-07-21-haines-flanagan-venn-vs-anatomy.md`: two public practitioner corpora read against the Anatomy, with the overlaps and the gaps on each side. Both dated; both research, not method.
- **Wording.** Public-tree files describe the method's origin in environment-neutral terms.
- **The method moved out of research/.** `research/Marketing-Anatomy.md` is now `MARKETING-ANATOMY.md` at the repository root, beside README, ABOUT and CHANGELOG, because it is the method and not a draft. A stub at the old path keeps older links alive; section anchors are unchanged. README now leads with the problem the method solves, the eight verbs, and one worked example of the method running monthly in production, with the tool procedure and the awesome list demoted to "when a vendor claims to have solved something". `research/README.md` labels that folder as dated evidence. New `ROADMAP.md` holds the candidate futures with their triggers and the futures this repo refuses, so "what next" has a written answer.

What did not change: the eight verbs, the seven commandments, the scored inventory and its tiers. The scores still carry their April 2026 assessment date and are estimates, as section 3 says.

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
