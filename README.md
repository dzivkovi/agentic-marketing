# Agentic Marketing

An open-source framework for understanding what marketing actually is, where AI agents help, and how to decide what to DIY, hire out, or buy - whether you're a solo broker or a global brand.

---

## From Fishing to Marketing

Around 2005, my wife became a real estate agent and I became her marketing department. At the time, I was an avid fisherman - and I quickly realized I was solving the same problem in both pursuits: **"What do they bite on?"**

Different bait for different species; different messages for different audiences. You can't force a bite; you present the right thing at the right time and wait. I didn't know any of this had names or frameworks. I just knew that SEO, content, email campaigns, and analytics felt like fishing with better tools.

My first real lesson came from targeting. I advertised my wife as a "Greater Toronto Area" real estate agent - five million people, zero leads. When I sharpened the hook to "Richmond Hill Real Estate" and "North York Condos," the leads started flowing. She ended up selling outside those areas anyway. In fishing terms: sharper the hook, better the catch. In marketing terms: specificity beats reach. I've watched enterprise brands make the same mistake at a different scale.

When I earned my **Inbound Marketing University** certification in 2009 (signed by Brian Halligan, HubSpot's CEO), it was the first time I realized the patterns I'd discovered empirically had an entire industry behind them.

![HubSpot Inbound Marketing Certificate](<images/IMU-Certificate.jpg>)

Then the enterprise world pulled me in. At **HOOPP** (Healthcare of Ontario Pension Plan), I spent four and a half years building their marketing technology stack: CMS vendor selection, website redesign with deliberate SEO ranking preservation, CRM and email marketing platform evaluation. The director of marketing taught me a lesson I carry to every engagement: *"Daniel, show me what you have and I'll tell you what I want."* Marketers don't hand you requirements from a blank page - they need a catalyst, a draft, a prototype to react to. That principle became Commandment #2 in this project's framework.

At **Tangerine Bank**, after their independence from ING, I helped unify two disparate web properties (the main banking site and their blog site) into a single platform with lead scoring and audience segmentation built in from day one. A colleague from that engagement later described the value I brought as *"an uncanny ability to translate business needs, shield us from the complexity of the back end, and work to provide solutions that benefit all stakeholders"* - the bridge between marketing and IT that most organizations struggle to build.

![Fishing - where it all started](<images/fishing.jpg>)

I was never the closer. I built the pipeline - the system that found the right people and got them to the table. Two decades later, that's exactly what I'm doing at enterprise scale: decomposing marketing into [8 operating verbs](research/Marketing-Anatomy.md#2-the-marketing-x-ray-8-universal-verbs), scoring 40+ activities by how much AI can help, and mapping the skills that make agentic marketing real - from solo operator to global enterprise.

---

## What This Project Is

This is my personal Anatomy of marketing AI architecture - and I'm keeping it open source. The goal is twofold:

1. **If you're figuring out marketing AI on your own**, this gives you the map: what every marketer does (8 marketing verbs), which activities AI can help with today, and whether you should DIY, hire, or buy at your size.
2. **If you're considering working with me**, this shows you how I think about the problem before we ever meet - so our first conversation starts with substance, not a blank page.

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
