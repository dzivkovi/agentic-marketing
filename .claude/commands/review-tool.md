---
description: Research a tool or product for skill-gap, architecture, and verb-fit per the Anatomy framework
argument-hint: <tool-name-or-URL>
---

# Review a tool against the Agentic Marketing Anatomy

Execute the tool-review procedure at `specs/tool-review.md` (current version) on the following target:

**Target:** $ARGUMENTS

If `$ARGUMENTS` is empty or ambiguous, ask the user which tool they want reviewed and what URL or canonical name identifies it.

## Execution

Follow the procedure's 5 legs **in order**:

1. **Leg 1 — Internal check** (mandatory first)
2. **Leg 2 — Tool docs** (use v0.2 routing heuristics: EXA-first for big vendors, Context7 for libraries, gh for GitHub)
3. **Leg 3 — Wrapper / runtime search** (Leg 3a = vendor-official runtime FIRST, then 3b community search, then 3c read-the-body)
4. **Leg 4 — Alternatives** (skip for single-tool reviews)
5. **Leg 5 — Synthesis** (verdict table per procedure; multi-surface table if vendor spans many surfaces)

## Persistence

Save output to `work/tool-reviews/<slug>.md` using a kebab-case slug derived from the tool name. Include the full verdict table + meta-observations + searches-run audit.

## Summary to user

After writing the file, report back concisely (<400 words):

- **3-state verdict** (or multi-surface table if applicable) with any modifiers (tier-gated, thin-skin/thick-core, split-endpoint)
- **Vendor-official runtime finding** (MCP / SDK / full agent product / none)
- **Persona-named skill-gap** (e.g., "No gap for GTM engineers, Partial for marketing consultants")
- **Top 3 surprises or gaps in this repo's coverage** (Vendor Companion row missing? Awesome-list entry needed? Curation Log entry warranted?)
- **Graduation recommendation:** is the review ready to move from `work/tool-reviews/` to `research/tool-reviews/` (public)?
- **Telemetry:** tool-call count + wall time

## Budget

Apply the v0.2 tool-call budget based on difficulty:
- Easy cases (well-documented + likely wrapped): ~20 calls, 20 min
- Medium cases (public API, unclear wrapper): ~30 calls, 30 min
- Hard / multi-surface cases: ~40 calls, 45 min; stop at 50

Verdict stability usually arrives before the budget. When stable, stop — extra calls thicken evidence without changing the verdict.

## Confidentiality

Comply with `specs/agent-rules.md` and CLAUDE.md Confidentiality Guardrail — no client identifiers, tool names themselves are public and fine to use.
