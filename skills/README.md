# Marketing Skills Roadmap

> This folder will contain SKILL.md files — one per marketing activity from the [scored inventory](../research/Marketing-Anatomy.md#3-the-scored-inventory-table). Each skill follows the [Agent Skills](https://agentskills.io) open standard and works across Claude Code, Codex, Gemini CLI, Cursor, and 30+ other compatible tools.

**Status:** Planned. No skills have been written yet. The [AWESOME-MARKETING-SKILLS.md](../AWESOME-MARKETING-SKILLS.md) file links to existing skills by others that you can use today.

---

## What a marketing skill contains

Each skill will be a folder with a `SKILL.md` file following this anatomy:

| Section | What it covers |
| --- | --- |
| **Context** | Persona, goal, and background — drawn from the Anatomy verb description |
| **Deterministic logic** | Rules, templates, checklists, scoring rubrics — the parts that never need LLM reasoning |
| **Non-deterministic logic** | Creative judgment, synthesis, interpretation — the parts where the LLM reasons |
| **Tools / MCP connectors** | Which APIs and systems the skill needs access to (CRM, CMS, DAM, analytics) |
| **Actions** | What the skill can do — drafts, reports, audits, recommendations |
| **HITL gates** | Where a human must review before anything changes state |
| **Size Fit** | Which tiers this skill serves (Solo / SMB / Enterprise) |
| **Portability notes** | Tested on which agent platforms; any platform-specific considerations |

---

## Planned skills — T1 Quick Wins

These are the highest-scoring activities from the [scored inventory](../research/Marketing-Anatomy.md#3-the-scored-inventory-table). They're the first candidates for SKILL.md files.

| Priority | Activity | Verb | Score | Size Fit |
| --- | --- | --- | --- | --- |
| 1 | Brand-aligned copy drafting | MAKE | 85 | S:● SMB:● E:● |
| 2 | Omnichannel repurposing from core asset | SHIP | 81 | S:◐ SMB:● E:�� |
| 3 | Trend / viral signal monitoring | SENSE | 76 | S:◐ SMB:◐ E:● |
| 4 | At-scale creative variations | MAKE | 72 | S:◐ SMB:● E:● |
| 5 | Campaign launch asset bundling | SHIP | 72 | S:— SMB:● E:● |
| 6 | Competitive intelligence | SENSE | 71 | S:◐ SMB:● E:● |
| 7 | Audience profiling / ICP definition | KNOW | 70 | S:● SMB:● E:● |
| 8 | Content enrichment | MAKE | 68 | S:◐ SMB:● E:● |
| 9 | Localization & regional adaptation | SHIP | 64 | S:— SMB:◐ E:● |
| 10 | Performance-driven lookalike analysis | DECIDE | 64 | S:— SMB:◐ E:● |
| 11 | Campaign ideation from research synthesis | DECIDE | 62 | S:● SMB:● E:● |
| 12 | SEO / GEO content strategy | SHIP | 60 | S:● SMB:● E:● |
| 13 | Customer advocacy / case study generation | SHIP | 60 | S:● SMB:● E:● |
| 14 | Voice of Customer capture | SENSE | 60 | S:● SMB:● E:● |
| 15 | Performance dashboarding | MEASURE | 60 | S:● SMB:● E:● |

---

## How skills relate to existing repos

Many of the T1 activities already have skills written by others (see [AWESOME-MARKETING-SKILLS.md](../AWESOME-MARKETING-SKILLS.md)). The skills in this folder will:

1. **Reference, not duplicate** — link to existing skills where they exist and are good
2. **Fill gaps** — build skills for activities no one has covered (e.g., localization, compliance review, brand stewardship)
3. **Add the enterprise layer** — existing skills are mostly Solo/SMB-focused. Our skills will include HITL gates, MCP connector specs, and compliance considerations for regulated enterprise environments
4. **Map the connectors** — for each skill, explicitly document which MCP servers or APIs are needed, so an IT team knows exactly what to build

---

*This roadmap is a plan, not a promise. Skills will be built as the framework matures and real client engagements validate which activities deliver the most value.*
