# Tool Review Procedure

**Version:** 0.2 (2026-04-19)
**Status:** Revised after round 1 validation against 3 tools of varying difficulty (Firecrawl/easy, Clay/medium, HubSpot/hard). Three independent validation agents converged on the same gaps; this version addresses them.
**Prior version:** v0.1 (see git history — 2026-04-19 earlier commit)

## Purpose

Assess whether a tool or product has a skill-gap worth filling, classify its wrappability, and place it in the 8-verb Anatomy. Output is a structured file plus (optional) Vendor Companion and Curation Log updates.

## Input

A tool name, URL, or vendor reference. If ambiguous, ask for disambiguation.

## Output

- **Primary:** `work/tool-reviews/<slug>.md` (gitignored draft) or `research/tool-reviews/<slug>.md` (public final)
- **Optional:** Dated entry in `CURATION-LOG.md` for non-obvious findings
- **Optional:** New or updated row in `research/Marketing-Vendors-By-Category.md`

## Process — 5 legs, in order

### Leg 1 — Internal check [MANDATORY, do first]

Before touching the web, grep the repo for prior research:

- `AWESOME-MARKETING-SKILLS.md` — tool name, common aliases, URL fragments
- `research/Marketing-Vendors-By-Category.md` — vendor row may already exist
- `CURATION-LOG.md` — prior caveats, coverage gaps
- `work/tool-reviews/` and `research/tool-reviews/` — a review may already be underway

**New in v0.2:** Also do a **name-collision check**:
- Verify the tool's canonical homepage domain
- Check whether the tool name collides with other products (e.g., `clay.com` GTM platform vs. `clay.earth` personal CRM; `Notion` productivity vs. various unrelated products)
- Identify the authoritative GitHub org/owner — a namespace mismatch is a red flag

**Why first:** avoids duplicating past work, front-loads disambiguation before web cycles are burned on the wrong entity.

### Leg 2 — Tool docs [MANDATORY]

**Routing heuristics (new in v0.2, learned from round 1):**
- Big-vendor SaaS (HubSpot, Salesforce, Adobe, etc.): **skip WebFetch on landing and pricing pages** — they're marketing fluff. Go **straight to EXA** (`mcp__exa__web_search_exa`) for developer docs.
- Library / SDK: use **Context7** (`mcp__context7__resolve-library-id` then `query-docs`)
- Small/dev-first tool with public docs: WebFetch is fine
- GitHub presence: use **`gh api`** (via Bash), not WebFetch

**Extract:**
- Platforms / scope (what it covers)
- Auth model (API key? OAuth? free tier?)
- Pricing tiers (credits, monthly, enterprise-only?)
- Rate limits
- Main endpoints / features — **distinguish per surface** for multi-surface vendors (see Decision criteria below)
- Tier-gating (which features are Free vs. Pro vs. Enterprise?)
- ToS language for agent/LLM use (commercial, scraping)

### Leg 3 — Existing wrapper / runtime search [MANDATORY, three sub-steps]

**3a — Vendor-official agent runtime [NEW in v0.2, do first]**

Before searching community wrappers, check whether the vendor ships their own agent surface:
- Official MCP server (search `<vendor> MCP`)
- Official Claude/Codex/Gemini skill
- Vendor's own AI agent product (HubSpot Breeze, Salesforce Agentforce, Adobe Agent Orchestrator, Intercom Fin, etc.)
- Vendor's own SDK with agent/tool primitives

**Why this matters (round-1 finding):** if the vendor ships a first-class agent runtime, the skill-gap question changes from "does a wrapper exist?" to "does the vendor's runtime cover our persona's use case?" Missing this substep misroutes the whole gap analysis.

**3b — Community wrapper search**
- `WebSearch`: `<tool> SKILL.md claude agent wrapper 2026`
- Check registries:
  - `github.com/VoltAgent/awesome-agent-skills`
  - `github.com/alirezarezvani/claude-skills`
  - `skillsmp.com`
- **Record the searches you ran** — so "no wrapper found" is verifiable

**3c — Read the body [MANDATORY for every hit]**
For each wrapper found:
- `gh api repos/<owner>/<name>` for metadata (stars, last update, license)
- **Fetch the raw SKILL.md body** via WebFetch on `raw.githubusercontent.com/...` — do not trust the header or README summary
- If the skill has **multiple SKILL.md files** (tree-structured): read the router + 2 highest-traffic sub-skills + any `rules/` files. Don't read all of them.
- **Stub detection:** if the body is <1 KB, or contains TODO placeholders, or is a thin summary — mark it as a *skill stub*, not a real skill. Stubs in big repos are common false positives.

**Classify architecture:** wrapper-intelligence / hybrid / orchestration-intelligence. A 106 KB SKILL.md is orchestration; a 3 KB SKILL.md is a wrapper; a tree of 8 small SKILL.md files is a distributed wrapper.

### Leg 4 — Alternatives scan [OPTIONAL]

Skip for single-tool skill-gap checks. Use when doing a category survey or when the tool looks commoditized.

### Leg 5 — Synthesis [MANDATORY]

Write the verdict and meta-observations to `work/tool-reviews/<slug>.md`.

**Verdict structure — choose one:**

#### For single-surface tools
Use a single verdict table:

| Dimension | Content |
|---|---|
| Category | One-line descriptor |
| Platforms / Scope | What it covers |
| Auth / Pricing | Key operational details |
| Tier-gating | What's Free / Pro / Enterprise |
| 3-state | `Wrapper` / `Hybrid` / `Hard` (+ `tier-gated` flag if partial) |
| Split-endpoint note | If one endpoint is Wrapper and another is Hybrid, flag the heaviest endpoint + note the exception |
| Thin-skin / thick-core? | Flag if API is Wrapper-easy but value is Hard-moated (Clay pattern) |
| Verb fit | Primary + secondary Anatomy verbs, with **does/enables** heuristic: primary = what it *does*, secondary = what its output *enables* |
| Persona lens | Who is the skill for? (marketing operator, GTM engineer, consultant, data scientist, etc.) |
| Skill-gap status (per persona) | `No gap` / `Partial` / `Yes`, evaluated per named persona |
| Vendor-official runtime? | None / MCP / SDK / Full agent product. If vendor-official exists, skill-gap collapses to "does it cover our persona?" |
| Notes | Gotchas, ToS landmines, ecosystem signals |

#### For multi-surface vendors (new in v0.2)
Use **one row per surface**:

| Surface | 3-state | Tier-gating | Primary verb | Persona | Skill-gap |
|---|---|---|---|---|---|
| e.g., CRM read/write | Wrapper | Free+ | KNOW | GTM eng | No gap |
| e.g., Marketing automation | Hybrid | Pro+ | SHIP | Marketer | Yes |
| e.g., AI agent | Hard | Credit-metered | n/a | n/a | N/A |

Do not force a single-primary-verb for tools like HubSpot that span all 8 verbs.

**Meta-observations (free text):**
- What was surprising
- What's missing in this repo (Vendor Companion row? awesome-list entry? Curation Log note?)
- What a skill would have to add beyond the API (the *orchestration intelligence* layer)
- **Searches run** (explicit bullet list, so "no wrapper" is verifiable)

## Decision criteria

### 3-state classification

- **`Wrapper`** — public API, standard auth, pre-parsed structured output. A skill can wrap it in <1 day. Intelligence largely in the API.
- **`Hybrid`** — public API + meaningful procedure needed (orchestration across endpoints, synthesis rules, domain knowledge). Skill is real work beyond the wrap.
- **`Hard`** — proprietary data/model moat, closed API, enterprise-gated, or scraping-only. Wrapping adds little or is infeasible.

**Modifiers (new in v0.2):**
- `tier-gated` — functionality exists but requires Pro/Enterprise subscription (not a 3-state itself, a property)
- `thin-skin / thick-core` — API is Wrapper-easy but the value moat is Hard (vendor's negotiated provider pricing, proprietary index, etc.). Classic Clay pattern.
- `split-endpoint` — different endpoints warrant different classifications. Record the heaviest + flag the exceptions.

### Skill-gap status (persona-relative)

- **`No gap`** — a wrapper exists (or vendor-official runtime exists) AND covers the persona's primary use case
- **`Partial`** — wrapper exists but leaves surfaces uncovered, OR covers a different persona than ours
- **`Yes`** — no public wrapper, or existing wrappers miss the tool's primary capabilities for our persona
- **`N/A`** — tool has no public API or is proprietary AI

**Round-1 lesson:** skill-gap is persona-relative. Clay is "no gap" for GTM engineers (six active skill packs exist) but "partial gap" for marketing consultants (none framed via the 8-verb Anatomy). Always name the persona.

### Verb fit

- Primary = what the tool *does* (its core action)
- Secondary = what its output *enables* downstream
- For multi-surface vendors, assign per-surface verbs (don't flatten)

## Escape hatches for hard cases

When **Leg 2** returns marketing fluff:
- Skip WebFetch on landing/pricing pages — use EXA immediately
- Drill into developer-docs subdomains (`developers.<vendor>.com`, `<vendor>.dev`)
- Check `llms.txt` if vendor publishes one

When **Leg 3** finds nothing:
- Try alternate search vectors: `<vendor> MCP`, `<vendor> API wrapper`, `<vendor> integration`, `<vendor> agent runtime`
- Check GitHub topics: `claude-code`, `agent-skill`, `claude-skill`, `mcp-server`

When the **API isn't public**:
- Mark `Hard`, note "no public API as of <date>"
- Still produce the assessment — skill-gap status becomes `N/A (no API)` or `Yes (API would enable)`

When **claims don't match reality**:
- Flag in Curation Log with evidence (URL, date, what was claimed vs. what was found)

## Tool-call budget (new in v0.2)

Soft budgets for stopping when verdict stability is reached:
- **Easy cases (well-documented, known wrappers):** ~20 calls, 20 min
- **Medium cases (public API, unclear wrapper status):** ~30 calls, 30 min
- **Hard / multi-surface cases:** ~40 calls, 45 min — stop at 50

Verdict stability is usually reached before the budget; once reached, additional calls thicken evidence without changing the verdict. Stop.

## Persistence

1. Primary: `work/tool-reviews/<slug>.md`
2. Non-obvious findings: append dated entry to `CURATION-LOG.md`
3. Graduate to public: `mv work/tool-reviews/<slug>.md research/tool-reviews/<slug>.md`
4. Update Vendor Companion row if the tool belongs there

## Confidentiality

Per `specs/agent-rules.md` and CLAUDE.md Confidentiality Guardrail:
- No client identifiers (names, abbreviations, engagement context) anywhere
- Tool names themselves are public products; using them is fine
- "Private" designation of `work/tool-reviews/` is about **timing** (not signaling active research to competitors) or **draft quality**, not content secrecy

## Versioning

- **v0.1** (2026-04-19 earlier) — derived from ScrapeCreators case only
- **v0.2** (2026-04-19) — after round-1 validation on Firecrawl/Clay/HubSpot. Added: vendor-official runtime substep, persona lens, multi-surface vendor structure, thin-skin/thick-core modifier, name-collision check, tool-call budget, routing heuristics, stub detection, searches-run audit

## Known limitations of v0.2

- Still small sample (3 validation cases + 1 original)
- No guidance for pricing extraction when vendor hides pricing behind sales calls
- Round 2 should test whether these additions actually improve outputs on the same tools
