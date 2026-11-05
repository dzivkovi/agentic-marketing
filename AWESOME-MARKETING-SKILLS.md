# Awesome Marketing Skills

> A short, checked list of agent skills, plugins and tools for marketing work, organized by the [8 marketing verbs](MARKETING-ANATOMY.md#2-the-marketing-x-ray-8-universal-verbs). Built on the open [Agent Skills](https://agentskills.io) standard. **Checked 2026-11-04** with [scripts/check_links.py](scripts/check_links.py): every repository below was alive and pushed to within the previous six months on that date unless its row says otherwise. Star counts are from that day and will drift.

## Why this list got shorter

The first version of this page (April 2026) was wide: seven skill packs, fifty-one deep links into individual skills, tools under every verb. Six months later eighteen of those fifty-one links were dead, because maintainers rename and merge skills faster than any list is edited, and the practitioners I follow had reached the same conclusion I had about wide lists:

- Most skills people install are "cool for about a day, but then I never used them again" (Rick Mulready). "Generic skills are extremely worthless" (Austin Marchese). People collect skill repos "like Pokémon cards" (Nate B. Jones).
- Of the skills one security vendor scanned in early 2026, 13 percent had a critical issue and 76 were confirmed malicious. No marketing skill made the most-installed top ten on the largest registry.
- The habit that holds up: take one skill from a pack, read it, run it on real work, keep it only if you reached for it again within a month.

This is a map, not my tested stack: I run a small subset of it alongside workflows I built myself, and I have not run every entry end to end. You do not need the whole list; you need the two or three rows that match the verb you are stuck on.

So this list now does three jobs. It names the packs and vendor surfaces that were alive on the check date, with whatever third-party use or review the research found (it varies by entry, and the row says so when there is none). It maps them to the verbs so you can find the one you need. And it tells you how to vet anything else yourself, because the next good skill will appear after this page was last checked.

What this list does not do: grade volunteer maintainers. Rows carry facts (what it does, the verb, the agent surface, the price gate, the last check). A repository that left the tables left because its last push was more than six months old or the owner published a replacement, not because it was judged.

---

## Skill packs and plugins

Install one skill, not the pack. Every install command below pulls a whole repository; read `SKILL.md` for the one you want before you let an agent run it (see [How to vet a skill](#how-to-vet-a-skill-before-you-install-it)).

| Pack | Owner | What it covers | Verbs | Agent surface and install | Price gate | Checked 2026-11-04 |
| --- | --- | --- | --- | --- | --- | --- |
| [marketingskills](https://github.com/coreyhaines31/marketingskills) | Corey Haines | 53 skills across the whole cycle: research, positioning, copy, CRO, SEO, email, ads, analytics; plus guides for 60-plus CLI tools | all eight | `npx skills add coreyhaines31/marketingskills`, or as a Claude plugin (`claude plugin install marketing-skills@marketingskills`), Codex plugin, per-skill zips. The shared context file every skill reads first is `.agents/product-marketing.md` | Free, MIT. Funded by disclosed partners; the author's paid layer is Magister (hosted agent with memory, from $99 a month), which the repo does not require | 58.5k stars, release v2.14.0 on 2026-10-30. v2.0 (May 2026) renamed 17 skills, which is what broke the April deep links |
| [knowledge-work-plugins: marketing](https://github.com/anthropics/knowledge-work-plugins/tree/main/marketing) | Anthropic | Brand review, campaign plan, competitive brief, content creation and drafting, email sequence, performance report, SEO audit; connectors for HubSpot, Ahrefs, Similarweb, Klaviyo, Canva, Figma, Slack, Notion, Amplitude, Supermetrics | DECIDE, MAKE, SHIP, MEASURE, SENSE | Claude plugin: `claude plugin marketplace add anthropics/knowledge-work-plugins` then `claude plugin install marketing@knowledge-work-plugins`; runs in Claude and Claude Code | Free, Apache 2.0; each connector needs its own vendor account | Active (last push September 2026). Its README lists commands that no longer match the tree; the skills are the source of truth. Its `seo-audit` and `content-strategy` skills share names with Corey Haines's, so expect both to answer the same request if you install both |
| [knowledge-work-plugins: small-business](https://claude.com/marketplace/plugins/small-business) | Anthropic | 44 skills for running a small company, of which about a dozen are marketing: ad manager, Canva creator, content strategy, growth pulse, review reputation, SEO and AI visibility, social content engine, lead finder, outreach composer, brand style; a plain-English router and approval gates on anything that sends, posts or pays | SENSE, DECIDE, MAKE, SHIP, MEASURE | Claude plugin from the marketplace page or `claude plugin install small-business@knowledge-work-plugins` | Free; 35 declared connectors (HubSpot, Mailchimp, Canva, Shopify, Stripe, Zapier and others) each need an account | Announced 2026-05-13; v1.35.1 in September 2026 |
| [gtm-cheat-codes](https://github.com/zapier/gtm-cheat-codes) | Zapier | 21 skills Zapier's own go-to-market teams use: campaign generator, brand guidelines builder, HTML mockup builder, campaign post-mortem, customer proof, story writer, recording-to-clip, plus sales and RevOps skills; approval gates built in | KNOW, DECIDE, MAKE, SHIP, MULTIPLY, LEARN | SKILL.md pack; copy the skill folder into your agent's skill directory (no one-line installer). Zapier MCP optional for actions | Free, MIT | 356 stars; last push 2026-07-13. No independent review found |
| [social-media-research-skills](https://github.com/ScrapeCreators/social-media-research-skills) | ScrapeCreators (vendor) | 13 research workflows over their scraping API: outlier-post finder, transcript intelligence, comment mining, competitor social research, ad-library teardown, trend discovery, influencer prospecting, audience research, content repurposing | SENSE, KNOW, MULTIPLY | `npx skills add ScrapeCreators/social-media-research-skills` with `SCRAPECREATORS_API_KEY`; the vendor also ships a hosted MCP and a CLI | Pay as you go: 100 free credits, then from $47 | 5.6k stars; the vendor's pricing page offers 100 credits for a GitHub star. No independent review found. Replaces the vendor's April `agent-skills` repo (last push 2026-04-09) |
| [newsjack](https://github.com/elvisun/newsjack) | Elvis Sun (Medialyst) | 33 PR skills in four lanes: detect (monitoring, triage, coverage tracking), act (angles, headlines, fact-check, journalist fit, media lists, crisis holding), strategize, and an AI-visibility lane; ships an ethics doctrine against mass blasts | SENSE, MAKE, SHIP, MEASURE | SKILL.md pack and Claude plugin (marketplace `elvisun/newsjack`); the project also offers a shell installer at newsjack.sh, which, like any remote script, you read before you run | Skills free, MIT. Live news search, journalist enrichment and media lists work best with the author's paid Medialyst account (from $149 a month); most skills run without it | 1.7k stars, 26 releases, last 2026-10-22. Usage figures come from the vendor's own pages; no independent review found |
| [semrush/skills](https://github.com/semrush/skills) | Semrush (vendor) | Technical SEO audit, internal-link audit, schema, keyword research, content brief, SERP analysis, backlink audit, competitor gap | SENSE, MEASURE, MAKE | `npx skills add semrush/skills` | Needs a Semrush subscription with API access | Created 2026-09-14; small and new |
| [canva-skills](https://github.com/canva-sdks/canva-skills) | Canva (vendor) | Brand check, bulk create, edit design, design feedback, resize for social, a Canva CLI | MAKE, MULTIPLY | `/plugin marketplace add canva-sdks/canva-skills` then `/plugin install canva@canva-skills`; also Codex and Cursor marketplaces | Canva account; bulk create needs Canva Enterprise | Active since December 2025 |
| [agent-cli-skills](https://github.com/HubSpot/agent-cli-skills) | HubSpot (vendor) | 19 skills that drive the HubSpot agent CLI: bulk operations, audience targeting, CRM data quality, deal management, reporting, workflow automation. CRM and ops, not campaign craft | KNOW, SHIP, MEASURE | `npx skills hubspot/agent-cli-skills` | Free, Apache 2.0; HubSpot account; the CLI is in beta | Created May 2026, last push 2026-10-28 |
| [DataForSEO MCP](https://github.com/dataforseo/mcp-server-typescript) and [skill templates](https://dataforseo.com/templates/ai-skills/) | DataForSEO (vendor) | Pay-per-call SEO and GEO data: SERPs including AI Overviews and AI Mode, keywords, backlinks, on-page, business data, and an AI Optimization API (LLM responses, mentions, AI keyword data). The templates are ready-made skills: AI visibility report, client SEO report, AI content plan, PPC keyword gap | SENSE, MEASURE | Hosted MCP (`https://mcp.dataforseo.com/v3/mcp`, OAuth) or local `npx dataforseo-mcp-server@latest`; a SKILL.md for CLI agents; a Codex plugin (October 2026) | Pay as you go, self-serve: $1 free credit, $50 minimum top-up, balance never expires | MCP server Apache 2.0, v3 in 2026. Third-party skill packs built on it exist; several carry affiliate links |
| [adobe/skills](https://github.com/adobe/skills) | Adobe (vendor) | Official Adobe skills; grew from 17 AEM skills in April to about 89 across Adobe products | MAKE, SHIP | SKILL.md pack | Adobe products | Active |
| [ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) | Eric Siu | Growth experiments, sales pipeline, content ops, outbound, SEO | SENSE, DECIDE, MAKE, SHIP, MEASURE | SKILL.md pack | Free | 3.8k stars, last push November 2026 |
| [no-ai-slop](https://github.com/petergyang/no-ai-slop) | Peter Yang | One skill that strips 20-plus AI-writing patterns while keeping the author's voice; a detect-only mode | MAKE | `npx skills add petergyang/no-ai-slop --skill no-ai-slop --global --yes` | Free, MIT | 13k stars since July 2026. One published critique argues that removing machine tells does not add a person's substance |
| [claude-seo](https://github.com/AgriciDaniel/claude-seo) | Daniel Agrici | 26 SEO sub-skills and 19 sub-agents: technical SEO, E-E-A-T, content, local, schema | SENSE, MAKE, MEASURE | SKILL.md pack | Free | 26.7k stars, last push November 2026 |
| [last30days](https://github.com/mvanhorn/last30days-skill) | Matt Van Horn | Research any topic across Reddit, X, YouTube, Hacker News, Polymarket and the web into a cited brief | SENSE | SKILL.md; also a Gemini extension | Free; source APIs optional | 66.6k stars, pushed November 2026 |

Smaller packs still alive on 2026-11-04, kept for completeness: [realjaymes/marketingagentskills](https://github.com/realjaymes/marketingagentskills) (34 skills, 68 stars), [pawbytes/skill-suites](https://github.com/pawbytes/skill-suites) (50-plus skills across marketing and creative suites, 117 stars), [CosmoBlk/email-marketing-bible](https://github.com/CosmoBlk/email-marketing-bible) (one deep email skill, 364 stars).

Not in the tables this time, with the fact that moved them: `BrianRWagner/ai-marketing-claude-code-skills` (last push 2026-03-19), `wshuyi/x-article-publisher-skill` (last push 2026-01-25), `ScrapeCreators/agent-skills` (replaced by the vendor's newer repo, above). Gated giveaways not listed: HubSpot's "Marketer's Claude Skills Library" (10 skills) and "Marketer's Agent Skills Pack" (5 skills) sit behind a lead form with company-size fields; the "11-skill AI content team" page delivers one skill, with the rest behind a paid newsletter. They may be good; they are not open.

---

## By verb: where to look first

| Verb | Start with | Free first-party tools | Notes |
| --- | --- | --- | --- |
| SENSE | last30days for "what are people saying"; ScrapeCreators or DataForSEO for data at volume; newsjack for press monitoring | Google Trends, Google Search Console, the X feed | Collection is near-automatic now; picking what to act on is still your job |
| KNOW | Corey Haines's `product-marketing` context file (the one every other skill reads); the small-business plugin's brand style; Anthropic's `competitive-brief` | Your own folder of plain files: audience, brand, positioning, goals | Build this before any agent. It is the highest-leverage row in the Anatomy that is not a skill |
| DECIDE | Corey Haines's `content-strategy`, `launch`, `pricing`; Zapier's campaign generator; Anthropic's `campaign-plan` | | Agents propose, a separate judge ranks, you pick |
| MAKE | Anthropic's `draft-content` and `brand-review`; Corey Haines's copy and ads skills; Canva skills; no-ai-slop as the last pass | Canva free tier | Run a reviewer that is not the writer; keep the words that carry your name |
| SHIP | Corey Haines's `emails`, `social`, `ads`; HubSpot CLI skills for CRM operations; Klaviyo and HubSpot MCP connectors | Meta Business Suite, LinkedIn Campaign Manager | Anything that sends, posts or pays gets a human gate |
| MULTIPLY | Corey Haines's `cro`; ScrapeCreators `content-repurposing`; Canva `resize-for-social-media`, `bulk-create`; Zapier's recording-to-clip | | The top-scored row in the Anatomy; also where automated volume gets accounts flagged |
| MEASURE | Anthropic's `performance-report`; DataForSEO AI visibility templates; Semrush skills | Google Search Console AI Overviews and AI Mode reports (free, worldwide since August 2026), GA4 | See the GEO stack below |
| LEARN | Zapier's campaign post-mortem; Corey Haines's `ab-testing` and `referrals` | A lessons file your agent proposes additions to, and you approve | |

---

## The GEO measurement stack

GEO (generative engine optimization, some vendors say AEO) is showing up in AI answers. The free stack first, then pay only if you need cross-engine tracking:

| Layer | Tool | Cost | What it shows |
| --- | --- | --- | --- |
| Pre-click visibility | Google Search Console, Search appearance filter and the generative-AI performance reports | Free | Impressions and clicks from AI Overviews and AI Mode, per page and query. All sites worldwide since 2026-08-31 |
| Post-click behaviour | Google Analytics 4 | Free | What AI-referred visitors do. Note: GA4 does not separate AI Overview visits from organic, so it is blind to the source |
| First look at your brand in AI answers | HubSpot AI Search Grader; Semrush AI Search Visibility Checker | Free, capped | A one-time read of whether answer engines mention you |
| Cross-engine tracking | Peec (from $95 a month, MCP included, per its pricing page); Semrush AI Visibility Toolkit (about $99 a month, secondary source); DataForSEO AI Optimization API (pay per call) | Under $100 a month or per call, as checked 2026-11-04 | Prompt-list visibility across ChatGPT, Perplexity, Gemini, AI Overviews over time |
| Enterprise AEO platforms | Conductor (AEO and SEO platform with an MCP server, apps in ChatGPT and Copilot, a data API; no public price); Profound (prompt-volume dataset and citation tracking; trial then enterprise) | Contact sales | Share of voice, sentiment, fan-out queries, crawler analytics across a large site estate |

The Anatomy scores AI-visibility tracking at T2 and warns that tracking alone does not change the answer; pair it with agent-readable pages (SHIP).

---

## How to vet a skill before you install it

A skill is software that runs with your agent's permissions, written in a format where the payload can be plain prose. Treat it like installing software.

1. **Read `SKILL.md` and every bundled file** (scripts, images, references) before the agent does. Anthropic's own guidance: use skills "only from trusted sources: those you created yourself or obtained from Anthropic", and audit everything else. Watch for network calls, file access outside the task, and instructions aimed at the agent rather than at you.
2. **Treat skills that fetch external URLs as high risk.** A trusted skill turns hostile the day its dependency changes.
3. **Run a scanner, then still read it.** [SkillSpector](https://github.com/NVIDIA/SkillSpector) (NVIDIA, Apache 2.0, CLI and MCP) catches planted malice and scores risk 0 to 100, but independent tests found most of its findings on legitimate skills were false positives, and two scanners run on the same corpus agreed only weakly. A scanner is a filter, not a judgment.
4. **Do not trust star counts or download counts as safety.** Both can be bought or inflated; one vendor on this page pays credits for a star.
5. **Pin what you keep.** Install from a specific commit or release, keep your own copy, and put a business edit to a skill through the same review as any production change (Anatomy, Commandment 3 and Section 5.6).
6. **Contain the first run.** Try a new skill in a disposable workspace with synthetic data and the minimum permissions, with approval required for anything that sends, writes or spends, before it touches real accounts.
7. **The one-month rule.** If you did not reach for it again within a month, delete it. Unused skills bloat the agent's context and compete for the same triggers.

The numbers behind this: Snyk's ToxicSkills audit (February 2026) scanned 3,984 skills from two public registries and found a critical issue in 13.4 percent and 76 human-confirmed malicious payloads, 91 percent of which combined code with prompt injection written in Markdown; a second study of 31,132 skills found vulnerabilities in 26 percent and likely malicious intent in 5 percent. The Agentic AI Foundation has announced vetting guidance for skill authors and installers; as of this check it is planned, not published.

---

## Standards and protocols

| Standard | What it is | Status 2026-11-04 |
| --- | --- | --- |
| [Agent Skills](https://agentskills.io) | The open format for giving agents a capability as a `SKILL.md` folder | Originated by Anthropic in December 2025; donated to the Agentic AI Foundation (Linux Foundation) on 2026-10-22 with more than seventy supporting platforms, including Claude, Codex, Gemini CLI, Cursor, VS Code and GitHub Copilot. agentskills.io is the specification; it has no skill directory. (agenticskills.io is a separate third-party directory.) |
| [Model Context Protocol](https://modelcontextprotocol.io) | How agents reach tools and data | Under the same foundation since December 2025; current spec revision 2026-07-28. Authentication is specified but optional, so a connection is as secure as your deployment |
| [AGENTS.md](https://agents.md) | The instruction-file convention agents read on start | A foundation project; the portable twin of `CLAUDE.md` |
| [A2A](https://github.com/a2aproject/A2A) | Agent-to-agent messaging | Announced in August 2026 that it was joining the same foundation; spec v1.0 |
| [Composio](https://composio.dev) | Hosted OAuth integrations exposed to agents (1,500-plus toolkits) | Still the integration layer behind several packs; free hobby tier, paid from $29 a month, pricing changed several times in 2026 |

---

## Lists by others

| List | Focus | Stars (2026-11-04) |
| --- | --- | --- |
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | 1,000-plus agent skills from official teams and the community, with a marketing section | 36.9k |
| [awesome-ai-seo](https://github.com/best-of-ai/awesome-ai-seo) | AI SEO tools, platforms, prompts | 324 |
| [awesome-agentic-advertising](https://github.com/jshorwitz/awesome-agentic-advertising) | MCP servers for ad platforms: Google, Meta, LinkedIn, TikTok, X | 46 |
| [awesome-llm-skills](https://github.com/Prat011/awesome-llm-skills) | LLM skills across domains, marketing category included | 1.8k |
| [awesome-ai-gtm](https://github.com/hculap/awesome-ai-gtm) | AI go-to-market stack, ideation through customer success | 21 |
| [awesome-ai-marketing](https://github.com/alternbits/awesome-ai-marketing) | AI tools for marketers by category | 147 |

One independent roundup worth reading before you pick a pack: Mission Growth's October 2026 review of 29 marketing skill repositories, each with a "skip it if" note.

---

*Checked 2026-11-04. To re-check: `python scripts/check_links.py` (needs the GitHub CLI) writes a dated report under `research/`. If a link is dead or a pack is missing, open an issue or a pull request.*

*If you're bringing AI into a marketing team and want someone who has lived on both sides of that gap (engineering and the business), let's talk about what's in the way: [linkedin.com/in/magmainc](https://www.linkedin.com/in/magmainc).*
