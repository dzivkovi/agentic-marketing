# Agentic Marketing

An open-source framework for understanding what marketing actually is, where AI agents help, and how to decide what to DIY, hire out, or buy - whether you're a solo broker or a global brand.

---

## What's Inside

Three things, each usable on its own:

1. **The Marketing Anatomy** - a framework that decomposes marketing into [7 commandments and 8 verbs](research/Marketing-Anatomy.md), scores 40+ activities by how much AI can help today, and maps each activity to a size tier (solo, SMB, enterprise). Start here if you need the map.
2. **The Awesome List** - a [curated index of open-source agent skills, tools, and resources](AWESOME-MARKETING-SKILLS.md) organised by the same 8 verbs. Every entry is hand-verified, not auto-generated. Start here if you want tools you can use today.
3. **The Tool Review Procedure** - a [reproducible methodology](specs/tool-review.md) to vet any marketing AI tool against the framework and produce a structured verdict in 20-40 minutes. Start here when a new vendor claims to have solved something and you want to cut through the noise.

Looking for the author's background, influences, and two-decade path from real estate marketing to enterprise AI? See [ABOUT.md](ABOUT.md).

---

## The 7 Commandments

Every recommendation in this framework is anchored to these non-negotiable principles - each one a reaction to a real failure mode, not an aspiration.

1. **Empathy before architecture.** Discovery and definition come before any boxes on a diagram.
2. **Catalyst, not blank page.** Arrive with working samples so stakeholders react, not stare.
3. **Co-Create - don't ping-pong.** Business owns the logic in plain text; IT owns the governance wrapper.
4. **Decouple logic from platform.** The Agentic Skill is the portable unit - avoid unnecessary vendor lock-in.
5. **Augment, don't replace.** Agents produce drafts; humans approve anything that changes state.
6. **Default-deny MCP writes.** Read-only by default. Write access requires explicit authorization.
7. **Observability is Day 1, not Day 2.** Guardrails, evals, and tracing ship with the first skill.

The full reasoning behind each commandment is in [Section 1 of the Anatomy](research/Marketing-Anatomy.md#1-the-7-commandments).

---

## The 8 Marketing Verbs

These eight activities recur across most marketing organizations, from solo operator to global enterprise. Each maps to scored activities and size-fit guidance in [the Anatomy](research/Marketing-Anatomy.md#2-the-marketing-x-ray-8-universal-verbs).

1. **SENSE** - Watch the market for signals.
2. **KNOW** - Build and maintain audience intelligence.
3. **DECIDE** - Choose what to say, to whom, when, for how much.
4. **MAKE** - Produce the assets and survive compliance review.
5. **SHIP** - Push to channels, on schedule, in the right language.
6. **MULTIPLY** - Reshape and personalize what you already made.
7. **MEASURE** - Attribute, dashboard, analyze.
8. **LEARN** - Close the loop, update the playbook.

---

## The Tool Review Procedure

Every week a new marketing AI tool claims to solve something. Most are noise, a few are real - and distinguishing them takes hours of research that every buyer redoes independently. This repo contains a **reproducible methodology** to evaluate any tool against the 8-verb Anatomy and produce a structured verdict in 20-40 minutes.

**What it produces:**

- **3-state verdict** - `Wrapper` (public API, skill-wrappable in a day), `Hybrid` (API + real orchestration needed), or `Hard` (proprietary moat, scraping-only, or enterprise-gated).
- **Persona-relative skill-gap** - `No gap` / `Partial` / `Yes`, evaluated per named audience. The same tool can be a no-gap for a GTM engineer and a partial-gap for a solo broker; the procedure forces you to name who you're evaluating for.
- **Verb fit** - which of the 8 Anatomy verbs the tool primarily serves, with secondary verbs where the output enables downstream work.
- **Vendor-official runtime check** - does the vendor already ship an MCP, CLI, or Agent Skill? If yes, the "should we wrap this ourselves?" question often collapses before it's asked.

**Two artifacts, one methodology:**

| Path | Role |
| --- | --- |
| [`specs/tool-review.md`](specs/tool-review.md) | The **procedure** - a 5-leg methodology (internal grep → docs → wrapper search → alternatives → verdict). Read this to understand or run the method manually. |
| [`.claude/commands/review-tool.md`](.claude/commands/review-tool.md) | The **slash command** - type `/review-tool <tool-name>` in Claude Code to invoke the procedure automatically and persist the output. |

Recipe (spec) vs. microwave button (command). The procedure is the canonical method; the command is the keyboard shortcut.

**Example:** a fresh review of ScrapeCreators (a multi-platform scraping API for 27+ social and search platforms) classified it as **Wrapper** with **No gap across four personas** - because the vendor already ships a hosted MCP, an official CLI, and an official Agent Skill. The full output lives at [`research/tool-reviews/scrapecreators.md`](research/tool-reviews/scrapecreators.md).

**Why this is in the repo:** the Anatomy tells you *what* to look for in a marketing tool; the procedure tells you *how* to look systematically. Together they let any reader - solo marketer, GTM engineer, or enterprise architect - independently vet a vendor and produce a verdict that's comparable to anyone else's. No more vendor-by-vendor guesswork.

---

## Where This Is Going

The framework maps the territory. The next step is **building the tools to work it.**

This project will grow to include actual [Agent Skills](https://agentskills.io) - portable SKILL.md files that any AI agent can use to execute real marketing workflows. Skills built here work across Claude Code, Claude Cowork, Microsoft Copilot, OpenAI Codex, Gemini CLI, Cursor, GitHub Copilot, and [30+ other compatible tools](https://agentskills.io). The goal: build once, run on any platform with a compatible agent.

For each skill, I'll map:

- **Deterministic logic** - rules, templates, checklists (the parts that never need LLM reasoning)
- **Non-deterministic logic** - creative judgment, synthesis (where the LLM reasons)
- **MCP connectors** - which APIs and systems the skill needs (CRM, CMS, DAM, analytics)
- **HITL gates** - where a human must review before anything changes state

The [skills roadmap](skills/README.md) lists the T1 Quick Wins targeted for first development. The [AWESOME-MARKETING-SKILLS.md](AWESOME-MARKETING-SKILLS.md) curates existing skills by others that you can use today - organized by the same 8 marketing verbs.

---

## Project Structure

| Path | What it is |
| --- | --- |
| [ABOUT.md](ABOUT.md) | The full origin story: from fishing to real estate marketing to enterprise AI architecture |
| [AWESOME-MARKETING-SKILLS.md](AWESOME-MARKETING-SKILLS.md) | Curated list of marketing agent skills, tools, and resources - organized by the 8 verbs |
| [CURATION-LOG.md](CURATION-LOG.md) | Editorial journal: caveats, gaps, patterns, and open questions discovered while curating the skills list |
| [CHANGELOG.md](CHANGELOG.md) | Release history: what shipped in each tagged version |
| [research/Marketing-Anatomy.md](research/Marketing-Anatomy.md) | The core framework: 7 commandments, 8 verbs, scored inventory, execution model, NFR defense |
| [research/Marketing-Vendors-By-Category.md](research/Marketing-Vendors-By-Category.md) | Living companion doc: vendors and tools per marketing verb, with size-tier fit |
| [skills/](skills/) | Roadmap and future home for SKILL.md files per marketing activity |
| [images/](images/) | Supporting images (Double Diamond diagram, certificate, fishing photo) |
| [research/](research/) | All research and reference documents |

---

## About the Author

I'm Daniel Zivkovic, an AI Architect based in Toronto. I spent a decade building marketing technology (CMS, SEO, lead scoring, audience segmentation) and another decade building enterprise AI systems (Nasdaq, Siemens, Google Cloud PSO). In 2026, those two threads converged. The full story is in [ABOUT.md](ABOUT.md).

If any of this resonates, I'd enjoy the conversation: [LinkedIn](https://www.linkedin.com/in/magmainc) | [magmainc.ca](https://magmainc.ca)

---

## License

Apache 2.0 - see [LICENSE](LICENSE) for details.

Use it, adapt it, challenge the scores, edit the verbs. If it helps you skip the blank-page problem, it did its job.
