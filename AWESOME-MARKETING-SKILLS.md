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

Install one skill, not the pack. "Terminal agents" below means Claude Code, Codex and their peers; "the Claude app" means the desktop or web app; a connector (MCP) is something your AI app signs in to. Every install command below pulls a whole repository; read `SKILL.md` for the one you want before you let an agent run it (see [How to vet a skill](#how-to-vet-a-skill-before-you-install-it)).

| Pack | Owner | What it covers | Verbs | Runs in, and how to install | Price gate | Checked 2026-11-04 |
| --- | --- | --- | --- | --- | --- | --- |
| [marketingskills](https://github.com/coreyhaines31/marketingskills) | Corey Haines | 53 skills across the whole cycle: research, positioning, copy, CRO, SEO, email, ads, analytics; plus guides for 60-plus CLI tools | all eight | Terminal agents (Claude Code, Codex) or the Claude app. `npx skills add coreyhaines31/marketingskills` (add `-a claude-code` when you run it from inside a Claude Code session, or it installs where Claude Code does not look); as a Claude plugin: `claude plugin marketplace add coreyhaines31/marketingskills` then `claude plugin install marketing-skills@marketingskills`; also a Codex plugin and per-skill zips. The shared context file every skill reads first is `.agents/product-marketing.md` | Free, MIT. Funded by disclosed partners; the author's paid layer is Magister (hosted agent with memory, from $99 a month), which the repo does not require | 58.5k stars, release v2.14.0 on 2026-10-30. v2.0 (May 2026) renamed 17 skills, which is what broke the April deep links |
| [knowledge-work-plugins: marketing](https://github.com/anthropics/knowledge-work-plugins/tree/main/marketing) | Anthropic | Brand review, campaign plan, competitive brief, content creation and drafting, email sequence, performance report, SEO audit; connectors for HubSpot, Ahrefs, Similarweb, Klaviyo, Canva, Figma, Slack, Notion, Amplitude, Supermetrics | DECIDE, MAKE, SHIP, MEASURE, SENSE | The Claude app and Claude Code. `claude plugin marketplace add anthropics/knowledge-work-plugins` then `claude plugin install marketing@knowledge-work-plugins` | Free, Apache 2.0; each connector needs its own vendor account | Active (last push September 2026). Its README lists commands that no longer match the tree; the skills are the source of truth. Its `seo-audit` skill has the same name as Corey Haines's, so both will answer an SEO-audit request if you install both |
| [knowledge-work-plugins: small-business](https://claude.com/marketplace/plugins/small-business) | Anthropic | 44 skills for running a small company, of which about a dozen are marketing: ad manager, Canva creator, content strategy, growth pulse, review reputation, SEO and AI visibility, social content engine, lead finder, outreach composer, brand style; a plain-English router and approval gates on anything that sends, posts or pays | SENSE, DECIDE, MAKE, SHIP, MEASURE | The Claude app (install from the marketplace page) or Claude Code (`claude plugin install small-business@knowledge-work-plugins`) | Free; 35 declared connectors (HubSpot, Mailchimp, Canva, Shopify, Stripe, Zapier and others) each need an account | Announced 2026-05-13; v1.35.1 in September 2026 |
| [gtm-cheat-codes](https://github.com/zapier/gtm-cheat-codes) | Zapier | 21 skills Zapier's own go-to-market teams use: campaign generator, brand guidelines builder, HTML mockup builder, campaign post-mortem, customer proof, story writer, recording-to-clip, plus sales and RevOps skills; approval gates built in | KNOW, DECIDE, MAKE, SHIP, MULTIPLY, LEARN | Any agent that reads skill folders (Claude Code, Codex, Cursor): copy the skill folder into your agent's skills directory; there is no one-line installer. Zapier's connector is optional, for actions | Free, MIT | 356 stars; last push 2026-07-13. No independent review found |
| [social-media-research-skills](https://github.com/ScrapeCreators/social-media-research-skills) | ScrapeCreators (vendor) | 13 research workflows over their scraping API: outlier-post finder, transcript intelligence, comment mining, competitor social research, ad-library teardown, trend discovery, influencer prospecting, audience research, content repurposing | SENSE, KNOW, MULTIPLY | Terminal agents: `npx skills add ScrapeCreators/social-media-research-skills` with `SCRAPECREATORS_API_KEY`; the vendor also ships a hosted connector (MCP) and a CLI | Pay as you go: 100 free credits, then from $47 | 5.6k stars; the vendor's pricing page offers 100 credits for a GitHub star. The API behind it was recommended by last30days's author in July 2026 ("the most valuable API key to get"); no independent review of the skills themselves found. The vendor's April `agent-skills` repo was last pushed 2026-04-09 |
| [newsjack](https://github.com/elvisun/newsjack) | Elvis Sun (Medialyst) | 33 PR skills in four lanes: detect (monitoring, triage, coverage tracking), act (angles, headlines, fact-check, journalist fit, media lists, crisis holding), strategize, and an AI-visibility lane; ships an ethics doctrine against mass blasts | SENSE, MAKE, SHIP, MEASURE | Terminal agents (skill folders) and the Claude app (plugin marketplace `elvisun/newsjack`); the project also offers a shell installer at newsjack.sh | Skills free, MIT. Live news search, journalist enrichment and media lists work best with the author's paid Medialyst account (from $149 a month); most skills run without it | 1.7k stars, 26 releases, last 2026-10-22. No independent review found |
| [semrush/skills](https://github.com/semrush/skills) | Semrush (vendor) | Technical SEO audit, internal-link audit, schema, keyword research, content brief, SERP analysis, backlink audit, competitor gap | SENSE, MEASURE, MAKE | Terminal agents: `npx skills add semrush/skills` | Needs a Semrush subscription with API access | Created 2026-09-14; small and new |
| [canva-skills](https://github.com/canva-sdks/canva-skills) | Canva (vendor) | Brand check, bulk create, edit design, design feedback, resize for social, a Canva CLI | MAKE, MULTIPLY | Claude Code (`/plugin marketplace add canva-sdks/canva-skills` then `/plugin install canva@canva-skills`); also Codex and Cursor marketplaces | Canva account; bulk create needs Canva Enterprise | Active since December 2025 |
| [agent-cli-skills](https://github.com/HubSpot/agent-cli-skills) | HubSpot (vendor) | 19 skills that drive the HubSpot agent CLI: bulk operations, audience targeting, CRM data quality, deal management, reporting, workflow automation. CRM and ops, not campaign craft | KNOW, SHIP, MEASURE | Terminal agents only: install HubSpot's `hubspot` CLI (beta) first, then `npx skills hubspot/agent-cli-skills` (HubSpot's README writes it without `add`) | Free, Apache 2.0; HubSpot account; the CLI is in beta | Created May 2026, last push 2026-10-28 |
| [DataForSEO MCP](https://github.com/dataforseo/mcp-server-typescript) and [skill templates](https://dataforseo.com/templates/ai-skills/) | DataForSEO (vendor) | Pay-per-call SEO and GEO data: SERPs including AI Overviews and AI Mode, keywords, backlinks, on-page, business data, and an AI Optimization API (LLM responses, mentions, AI keyword data). The templates are ready-made skills: AI visibility report, client SEO report, AI content plan, PPC keyword gap | SENSE, MEASURE | Any app that takes a connector: hosted MCP at `https://mcp.dataforseo.com/v3/mcp` (OAuth) or local `npx dataforseo-mcp-server@latest`; a SKILL.md for terminal agents; a Codex plugin (October 2026) | Pay as you go, self-serve: $1 free credit, $50 minimum top-up, balance never expires | MCP server Apache 2.0, v3 in 2026. Third-party skill packs built on it exist; several carry affiliate links |
| [adobe/skills](https://github.com/adobe/skills) | Adobe (vendor) | Official Adobe skills; grew from 17 AEM skills in April to about 89 across Adobe products | MAKE, SHIP | Terminal agents: skill folders | Adobe products | Active |
| [ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) | Eric Siu | Growth experiments, sales pipeline, content ops, outbound, SEO | SENSE, DECIDE, MAKE, SHIP, MEASURE | Terminal agents: skill folders | Free | 3.8k stars, last push November 2026 |
| [no-ai-slop](https://github.com/petergyang/no-ai-slop) | Peter Yang | One skill that strips 20-plus AI-writing patterns while keeping the author's voice; a detect-only mode | MAKE | Terminal agents: `npx skills add petergyang/no-ai-slop --skill no-ai-slop --global` (the README adds `--yes`; leave it off so you see what it installs) | Free, MIT | 13k stars since July 2026. Featured by Greg Isenberg (September 2026); one published critique argues that removing machine tells does not add a person's substance |
| [claude-seo](https://github.com/AgriciDaniel/claude-seo) | Daniel Agrici | 26 SEO sub-skills and 19 sub-agents: technical SEO, E-E-A-T, content, local, schema | SENSE, MAKE, MEASURE | Terminal agents: skill folders | Free | 26.7k stars, last push November 2026 |
| [last30days](https://github.com/mvanhorn/last30days-skill) | Matt Van Horn | Research any topic across Reddit, X, YouTube, Hacker News, Polymarket and the web into a cited brief | SENSE | Terminal agents: skill folder; also a Gemini extension | Free; source APIs optional | 66.6k stars, pushed November 2026 |

Smaller packs still alive on 2026-11-04, kept for completeness: [realjaymes/marketingagentskills](https://github.com/realjaymes/marketingagentskills) (34 skills, 68 stars), [pawbytes/skill-suites](https://github.com/pawbytes/skill-suites) (50-plus skills across marketing and creative suites, 117 stars), [CosmoBlk/email-marketing-bible](https://github.com/CosmoBlk/email-marketing-bible) (one deep email skill, 364 stars).

Not in the tables this time, with the fact that moved them: [BrianRWagner/ai-marketing-claude-code-skills](https://github.com/BrianRWagner/ai-marketing-claude-code-skills) (last push 2026-03-19), [wshuyi/x-article-publisher-skill](https://github.com/wshuyi/x-article-publisher-skill) (last push 2026-01-25), [ScrapeCreators/agent-skills](https://github.com/ScrapeCreators/agent-skills) (last push 2026-04-09; the vendor's newer repo is above). Not listed because the download needs a form or a paid subscription: HubSpot's "Marketer's Claude Skills Library" (10 skills) and "Marketer's Agent Skills Pack" (5 skills) sit behind lead forms; the "11-skill AI content team" page delivers one skill, with the rest behind a paid newsletter.

---

## By verb: where to look first

| Verb | Start with | Free first-party tools | Notes |
| --- | --- | --- | --- |
| SENSE | last30days for "what are people saying"; ScrapeCreators or DataForSEO for data at volume; newsjack for press monitoring | Google Trends, Google Search Console, the X feed | Collection is near-automatic now; picking what to act on is still your job |
| KNOW | Corey Haines's `product-marketing` context file (the one every other skill reads); the small-business plugin's brand style; Anthropic's `competitive-brief`. CRM hygiene: HubSpot `crm-data-quality`, small-business `crm-autopilot` | Your own folder of plain files: audience, brand, positioning, goals | Build this before any agent. It is the highest-leverage row in the Anatomy that is not a skill |
| DECIDE | Corey Haines's `content-strategy`, `launch`, `pricing`; Zapier's campaign generator; Anthropic's `campaign-plan` | | Agents propose, a separate judge ranks, you pick |
| MAKE | Anthropic's `draft-content` and `brand-review`; Corey Haines's copy and ads skills; Canva skills; no-ai-slop as the last pass | Canva free tier | Run a reviewer that is not the writer; keep the words that carry your name |
| SHIP | To write it: Corey Haines's `emails`, `social`, `ads`. To run it: HubSpot `workflow-automation` and `audience-targeting`, the Klaviyo and HubSpot connectors, the small-business plugin's approval-gated send skills | Meta Business Suite, LinkedIn Campaign Manager | Anything that sends, posts or pays gets a human gate |
| MULTIPLY | Corey Haines's `cro`; ScrapeCreators `content-repurposing`; Canva `resize-for-social-media`, `bulk-create`; Zapier's recording-to-clip | | The top-scored row in the Anatomy; also where automated volume gets accounts flagged |
| MEASURE | Campaign reporting: Anthropic's `performance-report` with the HubSpot and Supermetrics connectors, the small-business `report-builder`. Search and AI-answer data: DataForSEO templates, Semrush skills | Google Search Console AI Overviews and AI Mode reports (free, worldwide since August 2026), GA4 | See the GEO stack below |
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

1. **Read `SKILL.md` and every bundled file** (scripts, images, references) yourself, in a browser, before the agent does. Do not ask your agent whether a skill is safe: the injection is aimed at the agent. Anthropic's own guidance: use skills "only from trusted sources: those you created yourself or obtained from Anthropic", and audit everything else. Watch for network calls, file access outside the task, and instructions aimed at the agent rather than at you. Plugins can also bundle hooks and connector definitions (`.mcp.json`) that run without the model choosing to; read those too.
2. **Treat skills that fetch external URLs as high risk.** A trusted skill turns hostile the day its dependency changes.
3. **Run a scanner, read every finding it raises, and treat agreement between two scanners as a reason to look closer, not as a verdict.** Use a scanner's LLM mode where your data policy allows it: in Liatrio's August 2026 benchmark, no rules-only mode consistently beat a plain keyword search. Expect false alarms: the LLM modes flagged between 6 and 28 percent of clean skills depending on the scanner (table below), and every scanner Adversa tested in July 2026 was bypassed by rewording or translating the injected instructions. When two scanners disagree, read the flagged finding itself; when both are clear, the other checks on this list still apply. Keep the full report with the version you reviewed, because the same skill can score differently on two runs. A scanner is a filter, not a judgment.
4. **Do not trust star counts or download counts as safety.** Both can be bought or inflated.
5. **Keep a saved copy of the version you tested.** Install from a specific commit or release, no `--yes` flags and no auto-update, and put a business edit to a skill through the same review as any production change (Anatomy, Commandment 3 and Section 5.6).
6. **Contain the first run.** Try a new skill in a disposable workspace with synthetic data, no real API keys or OAuth tokens (scoped test credentials, revoked afterwards), the minimum permissions, and approval required for anything that sends, writes or spends, before it touches real accounts.
7. **The one-month rule.** If you did not reach for it again within a month, delete it. Unused skills bloat the agent's context, and two skills with similar descriptions will answer the same request.

If you cannot read the scripts, ask someone who can, or stay with prose-only skills, and follow your company's software approval process; a skill is software.

Scanner results from [Liatrio's benchmark](https://www.liatrio.ai/resources/blog/five-scanners-5000-ai-skills) (2026-08-12; LLM modes; two test sets, real-world / synthetic; the judge model was Sonnet 4.6 and the dollar figures are what the test cost, not list prices):

| Scanner | Caught malicious skills | Flagged clean skills | Cost per skill in the test | Notes |
| --- | --- | --- | --- | --- |
| [Snyk Agent Scan](https://github.com/snyk/agent-scan) | 89 / 93 percent | 6 / 9 percent | none at test time | Cloud analysis with a Snyk account; check your data-sharing policy and Snyk's current terms before use |
| [Cisco AI Skill Scanner](https://github.com/cisco-ai-defense/skill-scanner), LLM mode | 95 / 98 percent | 27 / 28 percent | about $0.05 | Apache 2.0; runs the judge on your own model key |
| [NVIDIA SkillSpector](https://github.com/NVIDIA/SkillSpector), LLM mode | 91 / 100 percent | 19 / 22 percent | about $0.53 / $0.26 | Apache 2.0, CLI and MCP; its 0 to 100 score is a sum of finding points and keeps findings that its own second-pass review marked as disputed, so read the findings, not the number |
| All three agree | 89 / 91 percent | 2 / 2 percent | about $0.58 | The rule for combining scanners moved the results more than the choice of scanners; agreement still missed about one malicious skill in ten |

The numbers behind this: Snyk's [ToxicSkills audit](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/) (February 2026) scanned 3,984 skills from two public registries and found a critical issue in 13.4 percent and 76 human-confirmed malicious payloads, 91 percent of which combined code with prompt injection written in Markdown; a second study of 31,132 skills ([Liu et al., "Agent Skills in the Wild", 2026](https://arxiv.org/abs/2601.10338)) found vulnerabilities in 26 percent and likely malicious intent in 5 percent; [Adversa](https://adversa.ai/blog/agent-skill-scanners-bypass-eight-tested/) (2026-07-30) got one malicious skill past all eight open-source scanners it tested, and paraphrased or translated injections beat every scanner that had caught the plain version. The Agentic AI Foundation's roadmap proposes vetting guidance for skill authors and installers; as of 2026-11-04 it was proposed, not published.

---

## Standards and protocols

| Standard | What it is | Status 2026-11-04 |
| --- | --- | --- |
| [Agent Skills](https://agentskills.io) | The open format for giving agents a capability as a `SKILL.md` folder | Donated by Anthropic to the Agentic AI Foundation (Linux Foundation) on 2026-10-22; Anthropic's announcement counts more than seventy supporting platforms, naming ChatGPT, Cursor, GitHub Copilot and VS Code, and Codex and Gemini CLI document support in their own docs. agentskills.io is the specification; it has no skill directory. (agenticskills.io is a separate third-party directory.) |
| [Model Context Protocol](https://modelcontextprotocol.io) | How agents reach tools and data | Under the same foundation since December 2025; current spec revision 2026-07-28. Authorization (OAuth 2.1) is specified in the protocol and marked optional, so a connection is as secure as your deployment |
| [AGENTS.md](https://agents.md) | The instruction-file convention agents read on start | A foundation project; the vendor-neutral instruction file that several agents read alongside their own |
| [A2A](https://github.com/a2aproject/A2A) | Agent-to-agent messaging | A project of the same foundation since August 2026 |
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
