# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## System Instructions

Before executing any task, you MUST read and strictly adhere to the constraints defined in `specs/agent-rules.md`. This file governs all content you write, every commit you make, and how you communicate with me. Read it before doing anything else.

## What This Repo Is

An open-source knowledge repository (being renamed from `agentic-marketing-skills` to `agentic-marketing`) containing a marketing AI architecture framework, a curated awesome list, and a roadmap for building portable Agent Skills. The primary deliverables are structured Markdown documents, not software. There are no build steps, test suites, or linters.

The core documents:

- **`research/Marketing-Anatomy.md`** - The framework itself: 7 commandments, 8 universal marketing verbs (Sense, Know, Decide, Make, Ship, Multiply, Measure, Learn), a scored inventory of ~40 activities, an execution model (Double Diamond, Co-Creation, Skills/MCP), and an NFR appendix. This is the "what and why."
- **`research/Marketing-Vendors-By-Category.md`** - Living vendor companion organized by the same 8 verbs. This is the "who sells what." It grows independently of the Anatomy.
- **`AWESOME-MARKETING-SKILLS.md`** - Curated list of open-source marketing agent skills, tools, and resources organized by the 8 verbs. This is hand-curated, not auto-generated. Every link should be verified against a real public repo or URL before adding. Do not hallucinate repos.
- **`CURATION-LOG.md`** - Editorial journal that accumulates compound learning from curating the skills list. Contains caveats about tools, coverage gaps, cross-category patterns, and open questions. When adding or reorganizing skills, check this log first for prior observations that should inform the decision. When you discover something noteworthy during research (a caveat, a gap, a pattern, a lead), add a dated entry here.
- **`skills/README.md`** - Roadmap for future SKILL.md files that will be built per marketing activity. The `skills/` folder will eventually contain actual Agent Skills (agentskills.io spec) organized by verb.

All documents share the same 3-tier sizing model (Solo / SMB / Enterprise) and notation: `S:` Solo, `SMB:` SMB, `E:` Enterprise, with symbols `●` essential, `◐` helpful, `—` skip.

## Confidentiality Guardrail

This repo was distilled from a private consulting engagement. All client-specific references have been scrubbed. The following must NEVER appear in any committed file:

- Client names or abbreviations from the original engagement
- AI tool names used during the original synthesis (e.g., "Gemini")
- "ARB" or "Architectural Review Board" (use "architectural review" generically)
- Line counts, message counts, or fingerprint strings that identify the source conversation
- "the chat", "Source Chat", or "Daniel's instruction" as attribution (use "earlier research", "synthesis", or "common frameworks")

When editing the Anatomy or Vendor Companion, use generic industry terms in Source columns (e.g., "Research Agent pattern", "enterprise additions", "flagged in red-team review").

## Gitignored Content

- `consolidated_chat.md` - Private source material. Never commit regardless of path.
- `print/` - Generated PDFs.
- `work/` - Session logs and change explanations.
- Binary formats: `.pdf`, `.docx`, `.xlsx`, `.pptx`, `.zip`, `.tar.gz`, `.log`, `.tmp`, `.mp4`, `.m4a`

## Document Scoring System

The scored inventory in the Anatomy uses dual-axis numeric scoring:

- **Universality %** - How common is this activity across marketing organizations (0-100)
- **AI Leverage %** - How much can agentic AI help today (0-100)
- **Priority Score** = Universality x Leverage / 100
- **Tier** - T1 Quick Win (score >= 60), T2 Core (40-59), T3 Transformation (20-39), T4 Patient (high universality, low leverage)

When adding or modifying rows, maintain the formula. Do not change existing scores without explicit instruction - they are informed estimates, not measurements.

## Editing the Vendor Companion

Each table is organized under one of the 8 verbs. Every vendor row must include: Vendor/Tool, Capability, Size Fit (using the 3-tier notation), DIY viable?, and Notes. The "DIY viable?" column is the most important - it answers whether an AI agent can replicate the vendor's core value.

## README Structure

The README contains a personal origin story ("From Fishing to Marketing") that grounds the project. This personal narrative is intentionally separate from the industry-universal Anatomy. Do not merge personal anecdotes into the Anatomy, and do not strip the personal voice from the README.

## Reminder

The rules in `specs/agent-rules.md` apply to every task in this repo without exception. When in doubt, re-read them. If a rule here in `CLAUDE.md` conflicts with `specs/agent-rules.md`, `CLAUDE.md` wins because it is project-specific (this override is stated at the top of `specs/agent-rules.md`).
