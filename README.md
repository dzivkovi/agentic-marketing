# Agentic Marketing

Before you buy an AI tool for marketing, know which of the eight kinds of marketing work it does. Most vendors are selling you one verb and calling it the whole job.

This repository is a method, not a tool list. It decomposes marketing into eight verbs that every marketing organization performs, from a solo operator to a global brand, scores forty-plus activities by how much an AI agent can actually do today, and says which ones are worth doing yourself, hiring out, or buying. It was written from practice and is used in production every month.

**Start here: [MARKETING-ANATOMY.md](MARKETING-ANATOMY.md)**, the whole method in one document. The rest of this page is the short version.

---

## The 8 Marketing Verbs

These eight activities recur across most marketing organizations. Each maps to scored activities and size-fit guidance in [section 2 of the Anatomy](MARKETING-ANATOMY.md#2-the-marketing-x-ray-8-universal-verbs).

1. **SENSE** - Watch the market for signals. What changed this week: trends, competitors, regulators, search demand, what customers are saying. Continuous.
2. **KNOW** - Build and maintain audience intelligence. Who you are talking to and what they bite on: ICPs, personas, jobs to be done, journey maps, vocabulary. Infrastructure: built once, refreshed quarterly, reused by every campaign. Know is only the reader; a verified market fact is Sense, a voice rule is Make.
3. **DECIDE** - Choose what to say, to whom, when, for how much. Where Sense meets Know.
4. **MAKE** - Produce the assets and survive compliance review.
5. **SHIP** - Push to channels, on schedule, in the right language.
6. **MULTIPLY** - Reshape and personalize what you already made.
7. **MEASURE** - Attribute, dashboard, analyze.
8. **LEARN** - Close the loop, update the playbook.

The Sense/Know split is the one line no established framework draws, and it is the one that matters most for agents: Sense is an always-running skill, Know is a quarterly-refresh asset. In one breath: Sense is the sonar, Know is the chart, Decide is where you cast. How the verbs map to Kotler, SOSTAC, RACE and the 4Ps, and where those frameworks have no equivalent, is [section 2.9](MARKETING-ANATOMY.md#29-mapping-to-established-frameworks).

---

## What it looks like in use

One worked example, running monthly since mid-2026 for a solo real-estate practice in a large metro market:

- **SENSE** runs without a human. A scheduled cloud agent watches the regional board's data release and emails the operator the morning it lands. Feeds, five listening corpora (what buyers and owners are actually saying), a search-demand snapshot, and a fact gate that verifies every number against its primary source before anyone decides anything.
- **KNOW** is read, not run. A one-page compass holds the reader profile and the persona; every stage consults it, nothing rewrites it mid-month.
- **DECIDE** is the first human moment. The agents build a three-angle menu with receipts; the operator picks one.
- **MAKE** drafts to a format spec and passes three gates: a logic-and-slop review, a persona-and-compliance review, and an independent second-model check on every number and legal claim.
- **SHIP** stages a private preview the operator reads on a phone, then a production deploy that runs only on an explicit yes.
- **MULTIPLY** turns the article into a carousel, a four-card social gallery and a short video, built from one text file. An agent fills the social composer; the human presses Post.
- **MEASURE and LEARN** write back what shipped, what each angle earned, and what the next run should do differently.

Eleven stages, four human moments, zero numbers published without a primary source. The method is the same at enterprise scale; only the instrumentation, budget and governance change.

---

## The 7 Commandments

Every recommendation in this framework is anchored to these principles, each one a reaction to a real failure mode, not an aspiration.

1. **Empathy before architecture.** Discovery and definition come before any boxes on a diagram.
2. **Catalyst, not blank page.** Arrive with working samples so stakeholders react, not stare.
3. **Co-Create - don't ping-pong.** Business owns the logic in plain text; IT owns the governance wrapper.
4. **Decouple logic from platform.** The Agentic Skill is the portable unit - avoid unnecessary vendor lock-in.
5. **Augment, don't replace.** Agents produce drafts; humans approve anything that changes state.
6. **Default-deny MCP writes.** Read-only by default. Write access requires explicit authorization.
7. **Observability is Day 1, not Day 2.** Guardrails, evals, and tracing ship with the first skill.

The full reasoning behind each commandment is in [section 1 of the Anatomy](MARKETING-ANATOMY.md#1-the-7-commandments).

---

## When a vendor claims to have solved something

You do not need to review every marketing AI tool. You need a 20-minute way to review the one in front of you. [specs/tool-review.md](specs/tool-review.md) is that procedure: five legs, ending in a three-state verdict (`Wrapper`, `Hybrid`, `Hard`), a persona-relative skill-gap call, the verb fit, and a check whether the vendor already ships an MCP, CLI or Agent Skill, which often ends the "should we wrap this ourselves" question before it starts. In Claude Code, `/review-tool <name>` runs it ([.claude/commands/review-tool.md](.claude/commands/review-tool.md)).

Worked reviews and the vendor-by-verb companion live in [research/](research/README.md), dated. Tools change monthly; the verbs do not. [AWESOME-MARKETING-SKILLS.md](AWESOME-MARKETING-SKILLS.md) is a hand-verified list of open-source agent skills and tools by verb, for readers who want something they can use today.

---

## Where this is going

[ROADMAP.md](ROADMAP.md) holds the candidate futures for this repository, each with the trigger that would make it the next move and the reasons it is not yet. Skills are built where they are used, inside the operating repositories that run real marketing; the ones that prove general will be published here.

---

## Project Structure

| Path | What it is |
| --- | --- |
| [MARKETING-ANATOMY.md](MARKETING-ANATOMY.md) | The method: 7 commandments, 8 verbs, scored inventory, execution model, NFR defense |
| [ROADMAP.md](ROADMAP.md) | Candidate futures with triggers; what this repo refuses to become |
| [ABOUT.md](ABOUT.md) | The origin story: from fishing to real estate marketing to enterprise AI architecture |
| [CHANGELOG.md](CHANGELOG.md) | Release history: what shipped in each tagged version |
| [specs/tool-review.md](specs/tool-review.md) | The 20-minute tool review procedure |
| [AWESOME-MARKETING-SKILLS.md](AWESOME-MARKETING-SKILLS.md) | Curated, hand-verified list of marketing agent skills and tools, by verb |
| [CURATION-LOG.md](CURATION-LOG.md) | Editorial journal behind the list: caveats, gaps, patterns, open questions |
| [research/](research/README.md) | Dated evidence: worked tool reviews, the vendor-by-verb companion, practitioner corpus studies |
| [images/](images/) | Supporting images |

---

## About the Author

I'm Daniel Zivkovic, an AI Architect based in Toronto. I spent a decade building marketing technology (CMS, SEO, lead scoring, audience segmentation) and another decade building enterprise AI systems (Nasdaq, Siemens, Google Cloud PSO). In 2026, those two threads converged. The full story is in [ABOUT.md](ABOUT.md).

If any of this resonates, I'd enjoy the conversation: [LinkedIn](https://www.linkedin.com/in/magmainc) | [magmainc.ca](https://magmainc.ca)

---

## License

Apache 2.0 - see [LICENSE](LICENSE) for details.

Use it, adapt it, challenge the scores, edit the verbs. If it helps you skip the blank-page problem, it did its job.
