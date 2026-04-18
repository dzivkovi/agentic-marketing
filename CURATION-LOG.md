# Curation Log

Editorial notes, caveats, and research leads from curating the [Awesome Marketing Skills](AWESOME-MARKETING-SKILLS.md) list.

This is where compound learning lives. Each entry captures something we noticed during research: a caveat about a tool, a gap in coverage, a pattern across categories, a lead worth following. The curated list shows what we recommend; this log shows *why*, and what questions remain open.

As the skill ecosystem grows, so does the uncertainty about how to organize it. This log accumulates the editorial judgment and open threads that inform future reshuffles and reorganizations. The only certain thing is uncertainty - so this log is positioned to make that uncertainty productive rather than paralyzing.

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
