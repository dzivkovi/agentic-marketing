# Curation Log

Editorial notes, caveats, and research leads from curating the [Awesome Marketing Skills](AWESOME-MARKETING-SKILLS.md) list.

This is where compound learning lives. Each entry captures something we noticed during research: a caveat about a tool, a gap in coverage, a pattern across categories, a lead worth following. The curated list shows what we recommend; this log shows *why*, and what questions remain open.

As the skill ecosystem grows, so does the uncertainty about how to organize it. This log accumulates the editorial judgment and open threads that inform future reshuffles and reorganizations. The only certain thing is uncertainty - so this log is positioned to make that uncertainty productive rather than paralyzing.

---

## 2026-07-20

### Editorial reset: maps, not report cards

Three months of applied practice (2026-04 to 2026-07) settled an editorial question this log had been circling: this repo's public artifacts map the field (who does what, which verb, what size fit) and do not grade it. An internal April research batch had grown two draft procedures for comparing community-curated lists and formally scoring standards; both were retired before publication. The comparison work produced verdict-shaped output about named volunteer maintainers (read-first / skip / merge recommendations), and that is not this repo's place - comparative verdicts belong in paid engagements or in future us-vs-alternatives contexts where the maintainer has skin in the game. The retired batch still produced durable field findings; they are preserved below on their own merit, with the procedural apparatus stripped. The standing test before building any new research machinery here: would a reader pay for the output, or only be impressed by the machinery?

### The free GEO measurement stack: GA4 and GSC expose AI Overviews asymmetrically

Google's two free tools take opposite positions on AI traffic visibility. GA4: AI Overviews / AI Mode pass no distinct referrer - AI-driven visits fold into Organic/Direct and are invisible as a segment, even as AI referral traffic grows triple-digit YoY. GSC: AI Overviews ARE isolatable via the `Search appearance = AI Overview` filter (UI rolled out 2025-06, broadened Feb 2026; API: `dimensions=['searchAppearance']`). Same company, opposite exposure - the search team's narrative ("we still send you AI traffic") wins in GSC, the analytics team's default ("AI Overviews are still Google") wins in GA4. The practical free GEO MEASURE stack is therefore: GSC for pre-click AI visibility + GA4 for post-click behavior (AI-blind), with paid cross-engine citation tracking as the optional third layer. The AWESOME GEO section should make this stack explicit.

### Knowledge surface vs execution surface

A framing that clarified vendor-readiness patterns across the April research: MCP servers and CLIs are execution surfaces (how agents reach tools); SKILL.md is the knowledge surface (what agents know how to do with them). Vendors shipping both see materially higher agent-ecosystem adoption than vendors shipping execution only. GA4 is the canonical gap case: Google ships a mature official MCP but no skill - the agent-readable knowledge layer (when to use which Data API call, sampled-vs-unsampled interpretation, AI-traffic channel-group setup, `AI_OVERVIEW` isolation) is left to the ecosystem. GSC and GA4 knowledge-surface skills are direct candidates for this repo's `skills/` roadmap.

### The agent-readiness stack composes: Skills x MCP x A2A

By Q1 2026 the three core agent standards are consistently framed as layered, not competing: Agent Skills = knowledge surface (what agents know how to do), MCP = vertical tool access (how agents reach tools and data), A2A = horizontal agent-to-agent communication. Spec-level evidence of deliberate composition exists (a Skills-over-MCP working group). Governance milestones worth recording as foundational context: A2A's handoff to the Linux Foundation (a2aproject) completed 2025-06-23; MCP was donated to the LF Agentic AI Foundation 2025-12-09. Agent Skills remains Anthropic-led with no formal governance declared - the outlier of the three. The Anatomy's execution model (section 4.3) already pairs Skills with MCP; extending that framing to include A2A is queued.

### Corey Haines's skill pack is the keystone of the public marketing-skills layer

Cross-list research surfaced a structural fact about the public ecosystem: the marketing coverage inside the large community skill catalogs traces overwhelmingly to one source - `coreyhaines31/marketingskills` (absorbed into bigger aggregate lists, sometimes with attribution only visible at YAML level). Remove that single pack and skills-layer coverage of DECIDE / MULTIPLY / LEARN across the public awesome-list ecosystem thins out overnight. This is credit, not critique: one curator is carrying the field's marketing-skills layer. It also means the field has a single point of dependency, which is both a fragility worth naming and an open invitation - there is ample room for more contributors, this repo included. A deeper corpus study of Corey's themes and their reach across the creator ecosystem is at [research/2026-07-21-corey-haines-marketing-skills-corpus-research.md](research/2026-07-21-corey-haines-marketing-skills-corpus-research.md).

### Frontier gap: strategy ships as advice, never as skills

No public list ships strategy, positioning, or ICP work as portable Agent Skills; the closest neighbor is idea-generation. MEASURE-as-skill (analytics interpretation) and SENSE-as-skill (research / listening / intent detection) are similarly thin everywhere. For this repo's `skills/` roadmap: DECIDE-verb skills (positioning, ICP articulation, pricing strategy) built Anatomy-aligned would enter uncontested space. This is the single most actionable finding the April batch produced.

### Star count decouples from curation depth in community lists

Observed repeatedly: 3-4 star lists with 9-10 of 12 categories substantively covered, next to a 124-star list covering 5 of 12. Discovery in the awesome-list ecosystem rewards SEO-fit titles and freshness, not curation depth. Editorial implication for AWESOME Section F readers: do not rank community lists by stars.

### Editorial convention adopted: disclose author affiliation

One reviewed skill package interleaved genuinely useful curation with repeated recommendations of the author's own commercial product, disclosed only obliquely. Not disqualifying - but going forward, AWESOME list rows should note author affiliation whenever a skill author has a commercial interest in the space they document. Readers deserve to know when the librarian owns a bookstore.

---

## 2026-04-19

### Terminology decision: GEO adopted as house term over AEO

2026-04 market signal: "GEO" is dominant across SEO influencers (~59% reference per industry surveys), Andreessen Horowitz's May 2025 thesis, Search Engine Land, Frase, academic literature (Aggarwal 2023 GEO paper), and Wikipedia. "AEO" is favored by platform vendors: Profound published [`AEO vs GEO: why we prefer AEO`](https://www.tryprofound.com/blog/aeo-vs-geo); HubSpot shipped "AEO" features into its platform. "AIO" is ambiguous (AI Optimization generic, or Google's AI Overviews feature) and dropped as a confusion hazard. House decision: **GEO as the house taxonomy term**, AEO acknowledged as vendor-preferred and preserved in vendor-specific notes (Profound's own "AEO" self-description is not rewritten). Aligns with majority market usage and the pronunciation preference of the maintainer.

### GEO formalized as a multi-verb category in the Anatomy

A fresh Anatomy grep surfaced the gap: GEO had a SHIP-verb row (`SEO / GEO content strategy`, T1 at 60, notes: "2026 frontier") for content optimization, but no MEASURE or SENSE representation. Two new scored rows added in this release:

- **SENSE / Prompt-demand sensing (GEO)** — U:30 x L:75 = 23 (T3 Transformation). Agent: "Prompt-Demand Sensor". Size fit S:— SMB:◐ E:●. Emerging but growing; vendor data-moats (Profound Prompt Volumes) dominate; high consumption leverage, low DIY.
- **MEASURE / AI-visibility tracking (GEO)** — U:40 x L:80 = 32 (T3 Transformation). Agent: "AI-Visibility Monitor". Size fit S:— SMB:◐ E:●. Gartner predicts 25% traditional-search drop in 2026; vendor-first-party runtimes (Profound MCP + SDKs) dominate consumption; Enterprise paid-floor gates Solo.

The existing SHIP row (`SEO / GEO content strategy`) notes were updated to cross-reference both new rows so readers see the multi-verb picture. Both scores are conservative starters; revisit as the category matures.

### Procedure v0.3: category-coverage matrix after Profound self-correction

The 2026-04-19 Profound review initially wrote "AEO/GEO as a category is absent from this repo's Anatomy, Vendor Companion, and AWESOME list." The maintainer pushed back. A re-grep showed the SHIP-verb row `SEO / GEO content strategy` did cover the content-optimization side; MEASURE and SENSE were the actual gaps. Procedure bumped to v0.3: Leg 1 now requires a **category-coverage matrix** across applicable verbs (not a single-verb grep) and Leg 5 requires per-verb gap reporting. Lesson: multi-verb categories (GEO, agentic ops, CDP, attribution) slip through single-verb greps; the matrix forces per-verb coverage to be explicit before synthesis hardens a wrong claim. See [`specs/tool-review.md`](specs/tool-review.md) v0.3 diff.

### Pattern: pricing-floor-as-persona-gate

Profound is the first vendor reviewed where the *pricing floor* creates a persona-gap larger than the skill-gap. Vendor-official MCP + SDKs are excellent; API access is Enterprise-tier only. Solo and SMB cannot meaningfully consume the runtime regardless of quality. The existing 3-state classification (`Wrapper` / `Hybrid` / `Hard`) does not encode this dimension. Flagged for v0.4 procedure work: whether to promote "paid-floor persona-incompatibility" from an ad-hoc Notes observation to a first-class review dimension. Carries over to sibling vendors in the GEO space (Peec AI, Otterly, Scrunch, Promptwatch) pending their own reviews.

### ScrapeCreators skill-gap: closed via vendor-official trifecta

The 2026-04-13 entry left open whether ScrapeCreators' paid-API dependency effectively excluded Solo marketers. Fresh procedure-driven research (see [`research/tool-reviews/scrapecreators.md`](research/tool-reviews/scrapecreators.md)) answers the question three times over: the vendor ships a **hosted MCP** at `api.scrapecreators.com/mcp`, an **official CLI** `@scrapecreators/cli` on npm (with `scrapecreators agent add {cursor,claude,codex}` auto-config), and an **official Agent Skill** at `github.com/ScrapeCreators/agent-skills` — a 16 KB SKILL.md teaching endpoint routing, pagination, credit awareness, and platform quirks (no-`@`, no-`#`, FB 3-per-page, Threads 20-30 cap). Pricing: Free 100 credits → $47 Freelance (25k credits) → $497 Business (500k) → custom Enterprise. Credits never expire. No rate limits. For the Solo-tier question specifically: the **$47 Freelance tier** is the lowest-viable working spend and covers months of ordinary cross-channel monitoring. Gap is real but narrow; vendor tiering closes it at a price even solo consultants can amortize. Vendor Companion row now added under SENSE at **S:● SMB:● E:◐**.

### Procedure validation: vendor-official-first ordering prevented a wrong public verdict

A separate ad-hoc baseline (preserved but marked superseded at `work/2026-04-19/01-scrapecreators-skill-gap-verdict.md`) concluded **"Partial gap"** on the premise that ad-library / Amazon Shop / SERP endpoints had no wrapper. That baseline never asked whether the vendor ships its own agent surface — pure intuition jumping straight to community wrappers. The fresh procedure-driven run (under [`specs/tool-review.md`](specs/tool-review.md) v0.2) mandated a vendor-official check **before** community wrapper search and caught the trifecta in two `gh api` calls. Net finding: **the vendor-official-first ordering isn't procedural polish; it prevents a full-context, intelligent reader from arriving at a factually wrong verdict.** Without the forcing function, intuition skips past the vendor's own agent surfaces every time the community-wrapper question is interesting.

### Emerging signal: ecosystem-membership declarations in SKILL.md frontmatter

The ScrapeCreators official SKILL.md declares `metadata.openclaw` in its frontmatter. GitHub code search surfaces `openclaw/skills`, `skills.sh`, and an `orth` CLI as related artifacts — suggesting an emerging agent-skill installer ecosystem that sits outside npm/GitHub as a distribution rail. Worth tracking because **ecosystem-membership declarations are a leading indicator**: a vendor declaring participation before the ecosystem has name recognition is an early-signal worth noting. Queued in the v0.3 tool-review backlog as a new signal class: when a SKILL.md declares `metadata.<ecosystem>`, that ecosystem itself may warrant a separate review.

---

## 2026-04-18

### Second deep audit pass: regulated-enterprise screening of the curated ecosystem

Ran a second deep audit pass (following the 2026-04-17 adversarial audit). Method: four parallel research streams (Adobe Summit ecosystem, Adobe 72-skills catalogue deep-dive, practitioner-sourced rubric from six named authorities, regulatory-grounded enterprise screen), screening of the 29-skill shortlist plus Adobe's 16 marketing-adjacent skills, gap analysis against six regulated-enterprise jobs-to-be-done. Findings summarised as patterns below; the detailed scorecard and briefing package stay private per the editorial decision that internal scorecards are gitignored while pattern-level observations are public.

### Pattern 1: catalog counts drift fast when the source repo is moving

The awesome list's Adobe entry cited 17 skills. The actual clone on 2026-04-17 had 72 skills. This is not a miscount; it is a fast-moving repo that added plugin bundles since the awesome list was last refreshed. Mirrors the earlier star-drift observation from the 2026-04-17 adversarial audit. Refresh catalogue counts at publish time via `gh api` or a local clone walk; do not treat last month's count as current.

### Pattern 2: spec compliance is a variance axis within "reputable" authors

Not all reputable authors keep their SKILL.md frontmatter complete. One author in the ecosystem shipped 13 of 21 skills without a populated `description` field at audit time. This is surprisingly common among authors who prioritise executable code over metadata. Treat frontmatter completeness as an independent axis when ranking; do not let overall repo quality halo over per-skill structural compliance.

### Pattern 3: near-duplicate skill families appear both in open and vendor repos

A well-known open-source author ships three CRO skills (onboarding, page, paywall-upgrade) that follow an identical structure with the topic noun swapped. Adobe does the same thing at much larger scale: seven workflow skills and seven dispatcher skills mirrored across AEM 6.5 LTS and Cloud Service. Open authors fork for topic variation; Adobe forks for platform version. Both produce shortlists that over-count unique capability and under-count real coverage.

Lesson: when counting, collapse near-duplicates before reporting. When tiering, one slot per template family is usually enough.

### Pattern 4: star count correlates with visibility, not enterprise-readiness

Applying a 10-point regulatory-grounded enterprise screen (OSFI B-10, PCI-DSS 4.0, EU AI Act Articles 14 and 50, NIST AI RMF, Gartner, Forrester) to the 29-skill shortlist produced results where 22-star and 5k-star repos scored within 1 gate of 21.8k-star market leaders on governance rigor. The best-scoring skill overall (10 of 10 gates) was a customer-research skill inside the largest repo; the next tier included a 5k-star solo-author SEO skill ahead of several 22k-star siblings because its SKILL.md explicitly cited Google's March 2024 Scaled Content Abuse enforcement policy.

Lesson: star count is a visibility filter, not a governance filter. For regulated-enterprise selection, the screen does useful work that popularity does not.

### Pattern 5: Agent Skills is on track to be the de-facto cross-vendor standard

As of April 2026 the spec has three credible commercial adopters:

- Adobe (`adobe/skills`, Apache 2.0, 72 skills across AEM + App Builder plus separate Commerce and Express bundles).
- Salesforce (TDX 2026 April 14-15 announcements: ADLC skills, open-sourced Agent Script, 30 coding skills, Agentforce Vibes skill directory at `.a4drules/skills/`).
- Vercel (referenced by Adobe's README as a peer ecosystem).

Adobe's Commerce skill installer explicitly targets 9 agent directories including Cursor, Windsurf, Gemini CLI, Codex, Antigravity, Cline, Kilo Code, Claude Code, and Copilot. HubSpot took the opposite bet (proprietary Breeze Studio). Optimizely has no public signal.

MCP was donated to the Linux Foundation's Agentic AI Foundation on 2025-12-09, alongside AGENTS.md. The standards landscape (MCP, A2A, NLWeb, AGENTS.md, Agent Skills) is consolidating faster than most enterprise buyers track.

### Pattern 6: vendor catalogues and open catalogues are solving different jobs

Walked Adobe's 72 SKILL.md files. Zero are marketer-facing. The entire catalog is developer / ops tooling for AEM (dispatcher, workflow, replication, authoring, migration). The marketing story inside Adobe runs through Agent Orchestrator inside AEP (Audience Agent, Journey Agent, CJA Data Insights Agent: deployable today per Merkle's March 2026 pre-Summit analysis).

Independent authors in the same ecosystem are solving the marketer-facing skills gap directly: customer-research, copy-editing, social-content, CRO flavours, psychology with ethical gates, dashboards as runnable code. The two tracks are complementary, not competitive. Adobe's Agent Orchestrator plus open-ecosystem skills covers more ground than either alone.

### Pattern 7: regulatory grounding is what separates "safe pilot" from "worth auditing"

Four regulatory sources consistently surface criteria that the implicit "reasonable enterprise" frame misses: EU AI Act Article 14 (human oversight designation), Article 50 (end-user AI disclosure, effective August 2026), OSFI B-10 (third-party subprocessor disclosure, exit strategies), PCI-DSS 4.0 (Req 6.3 prompt-injection defence, Req 10 automated-system logging). Gartner's 2026 AI Governance Platforms guide and Forrester's AEGIS framework both require a named AI inventory as a precondition to deployment.

Lesson for future curation: when a skill claims to be "enterprise-ready," check whether it satisfies the named-approval-point, end-user-disclosure-hook, and per-run-log-line requirements. These are usually the three gates where open-source skills fail quietly.

### Open question: does the practitioner-sourced rubric converge with the regulatory-grounded screen?

This pass produced two independent evaluation instruments: a 7-axis rubric harvested from Haines, Fishkin, Dunford, Osiu, Moesta, Flanagan (evidence over assertion, customer-language fidelity, positioning-context prerequisite, workflow specificity, outcome tie-in, struggle-trigger anchor, humility and safe failure), and a 10-point enterprise screen grounded in OSFI / PCI / EU AI Act / NIST sources. The two were not jointly applied to the same skills in this pass.

Hypothesis worth testing in the next round: a skill that scores high on the practitioner rubric (humility, workflow specificity, outcome tie-in) should correlate with high enterprise-screen pass rates (human approval, eval harness, draft-only first run). If they diverge, the divergence itself is the finding: practitioners care about slightly different things than regulators, and the rubric needs a bridge axis. Worth a small controlled test on 6-8 skills where both scores are already inferrable.

---

## 2026-04-17

### Adversarial audit pass: what looked like fabrication was usually drift or author voice

Ran parallel adversarial audits on [AWESOME-MARKETING-SKILLS.md](AWESOME-MARKETING-SKILLS.md) and [Marketing-Vendors-By-Category.md](research/Marketing-Vendors-By-Category.md). Most "suspicious" items fell into three patterns, not fabrication.

**Star-count drift is not fabrication.** In this ecosystem a six-day-old GitHub number can be 10-30% stale. Refresh at publish time with `gh api repos/OWNER/REPO --jq '.stargazers_count'`; keep the "approximate as of [month]" hedge.

**Author voice can read as AI hedging.** "James (MIA)" is `realjaymes`'s own repo framing, and "battle-tested on real revenue" is `ericosiu`'s own README copy. Curated lists should speak in the curator's voice; echoing the author's marketing blurs that line and invites false "fabrication" flags. Quote with attribution, or paraphrase neutrally.

**Hedge-to-root is a diagnostic signal.** When every entry for a repo links to the root rather than a specific `/tree/main/.../<name>` subpath, concentrate verification there. In this pass, the `realjaymes`, `ericosiu`, and `pawbytes` groups all showed this pattern; all three turned out to have real subfolders, but finding them required opening each repo.

### New editorial rule: Gartner / MQ claims require a public citation or get removed

Several vendor rows carried "Gartner DXP Leader" language from a prior deep-research pass, not first-hand Gartner access. Kept Acquia and Aprimo with year-scoped phrasing; removed Contentstack and Sitecore. Going forward: no "Leader" or "#1" claim without a year and a verifiable link.

### `pawbytes/skill-suites` uses a suite layout, not flat skills

Five suites live under `src/` (marketing, creative, prodig, webinar, tools), with a `paw-<suite>-<skill>/` folder pattern and a `marketing-agency` coordinator skill that routes tasks to specialists. Deep-linking to an individual marketing skill therefore means `src/marketing/paw-mkt-<skill>/`. Worth remembering when scanning other skill collections for reorg risk.

### Revision-tracking scatter collapsed to one source

Three overlapping mechanisms (git tags, a `### v1.1` block in Marketing-Anatomy.md, and this log) had drifted into answering the same "what shipped" question. Fixed: [CHANGELOG.md](CHANGELOG.md) owns the reader-facing release trail, tag annotations stay terse, this log stays editorial-only. Release Process codified in CLAUDE.md.

### Consolidations and renames caught during the pass

- Heap was acquired by Contentsquare (Dec 2023); file had listed it as independent.
- Dynamic Yield advertises ~300 global brands on its own pages, not the "400+" we had.
- `BrianRWagner/ai-marketing-skills` was renamed to `ai-marketing-claude-code-skills`.
- `google/A2A` moved to `a2aproject/A2A`.

Vendor and open-source landscapes move faster than the doc. Habit for next pass: flag anything acquired in the last ~18 months for a quick re-check before citing.

---

## 2026-04-13

### last30days-skill: API tier caveat

Added [last30days](https://github.com/mvanhorn/last30days-skill) to SENSE (21.5k stars, MIT, Agent Skill spec compliant).

Free tier covers Reddit, HN, Polymarket, GitHub. X, YouTube, and TikTok require API keys or a ScrapeCreators subscription. This is a common pattern for signal-aggregation tools: the free tier gives you a useful subset, paid APIs unlock the full picture.

**Open question:** Does the free tier alone deliver enough value for a Solo marketer, or is this effectively SMB+ without the paid APIs? The 3-tier sizing model (S/SMB/E) may need a nuance here: free-tier Solo, paid-tier SMB+.

### Observation: SENSE category is light on aggregators

Before adding last30days, SENSE had four entries: two Corey Haines skills (customer-research, competitor-alternatives) and two raw platforms (Google Trends, X). The gap was cross-platform synthesis - a tool that pulls signals from many sources and synthesizes them. last30days fills that gap, but it's the only aggregator. Worth watching for more.
