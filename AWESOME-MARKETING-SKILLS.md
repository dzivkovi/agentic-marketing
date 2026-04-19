# Awesome Marketing Skills

> Curated skills, tools, and resources for AI-powered marketing - organized by the [8 marketing verbs](research/Marketing-Anatomy.md#2-the-marketing-x-ray-8-universal-verbs). Built on the [Agent Skills](https://agentskills.io) open standard.

This is a living list. It grows as the ecosystem grows. Contributions welcome.

---

## Skill Repositories

Complete marketing skill collections that work with Claude Code, Codex, Gemini CLI, Cursor, and other [Agent Skills-compatible tools](https://agentskills.io).

| Repo | Skills | What it covers | Stars |
| --- | --- | --- | --- |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | 33 | CRO, SEO, copywriting, growth, analytics + 60 CLI tools + MCP via Composio | 21.8k |
| [ericosiu/ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) | 25+ | Growth experiments, sales pipeline, content ops, outbound, SEO. Author's own framing: "battle-tested on real revenue" | 1.9k |
| [realjaymes/marketingagentskills](https://github.com/realjaymes/marketingagentskills) | 25 | Strategy, content, CRO, automation, agent-skill-builder meta-skill | 23 |
| [pawbytes/skill-suites](https://github.com/pawbytes/skill-suites) | 59 (23 marketing) | Five "skill suites" (marketing, creative, prodig, webinar, tools) under `src/`. Marketing skills live at `src/marketing/paw-mkt-*/`. | 22 |
| [adobe/skills](https://github.com/adobe/skills) | 17 | Official Adobe skills repo. Currently AEM Edge Delivery Services (content development, migration, discovery). Structured to grow across Adobe products | 36 |
| [BrianRWagner/ai-marketing-claude-code-skills](https://github.com/BrianRWagner/ai-marketing-claude-code-skills) | 17 | Cold outreach, homepage audit, social cards, and more | 236 |
| [CosmoBlk/email-marketing-bible](https://github.com/CosmoBlk/email-marketing-bible) | 1 | 55K-word email marketing guide as an AI skill | 140 |

---

## By Verb

Skills and tools mapped to the [8 marketing verbs](research/Marketing-Anatomy.md#2-the-marketing-x-ray-8-universal-verbs) from the Anatomy framework. Each verb represents a recurring activity that spans marketing organizations of every size.

### SENSE: Watch the water for signals

| Skill / Tool | Source | What it does |
| --- | --- | --- |
| [customer-research](https://github.com/coreyhaines31/marketingskills/tree/main/skills/customer-research) | Corey Haines | Structured customer research workflows - surveys, interviews, signal extraction |
| [competitor-alternatives](https://github.com/coreyhaines31/marketingskills/tree/main/skills/competitor-alternatives) | Corey Haines | Competitive intelligence and positioning against alternatives |
| [last30days](https://github.com/mvanhorn/last30days-skill) | mvanhorn | Cross-platform trend research - aggregates Reddit, X, YouTube, HN, Polymarket, and 7 more into cited briefs |
| [ScrapeCreators/agent-skills](https://github.com/ScrapeCreators/agent-skills) | ScrapeCreators (vendor-official) | Official Claude Agent Skill for the ScrapeCreators scraping API - 27+ social/search platforms (TikTok, IG, YT, LinkedIn, X, Reddit, Threads, Bluesky, Pinterest) plus FB/Google/LinkedIn ad libraries. Teaches endpoint routing, pagination, credit awareness, platform quirks. Vendor also ships hosted MCP at `api.scrapecreators.com/mcp` and npm CLI `@scrapecreators/cli` |
| [Google Trends](https://trends.google.com) | Google (free) | Real-time search interest and trending topics; the simplest SENSE tool |
| [X / Twitter](https://x.com) | X (free to browse) | Real-time public conversation - trending topics, hashtag monitoring, high-volume signal feed |

### KNOW: Build and maintain audience intelligence

| Skill / Tool | Source | What it does |
| --- | --- | --- |
| [marketing-psychology](https://github.com/coreyhaines31/marketingskills/tree/main/skills/marketing-psychology) | Corey Haines | Behavioral science and persuasion frameworks for audience understanding |
| [icp-persona](https://github.com/realjaymes/marketingagentskills/tree/main/skills/icp-persona) | James (MIA) | ICP and persona builder from product marketing context |
| [customer-segments](https://github.com/realjaymes/marketingagentskills/tree/main/skills/customer-segments) | James (MIA) | Audience segmentation skill |
| [SparkToro](https://sparktoro.com) | Rand Fishkin | Audience intelligence - who they follow, read, listen to |

### DECIDE: Choose what to say, to whom, when, for how much

| Skill / Tool | Source | What it does |
| --- | --- | --- |
| [content-strategy](https://github.com/coreyhaines31/marketingskills/tree/main/skills/content-strategy) | Corey Haines | Content strategy planning and editorial direction |
| [pricing-strategy](https://github.com/coreyhaines31/marketingskills/tree/main/skills/pricing-strategy) | Corey Haines | Pricing page optimization, packaging, and positioning |
| [marketing-ideas](https://github.com/coreyhaines31/marketingskills/tree/main/skills/marketing-ideas) | Corey Haines | Creative marketing idea generation from constraints |
| [launch-strategy](https://github.com/coreyhaines31/marketingskills/tree/main/skills/launch-strategy) | Corey Haines | Product launch planning and GTM execution |
| [product-positioning](https://github.com/realjaymes/marketingagentskills/tree/main/skills/product-positioning) | James (MIA) | Positioning and messaging framework |
| [marketing-sostac](https://github.com/pawbytes/skill-suites/tree/main/src/marketing/paw-mkt-sostac) | pawbytes | SOSTAC strategic marketing plan builder |

### MAKE: Produce the assets

| Skill / Tool | Source | What it does |
| --- | --- | --- |
| [copywriting](https://github.com/coreyhaines31/marketingskills/tree/main/skills/copywriting) | Corey Haines | Write and rewrite marketing copy for landing pages, homepages, ads |
| [copy-editing](https://github.com/coreyhaines31/marketingskills/tree/main/skills/copy-editing) | Corey Haines | Edit and improve existing marketing copy |
| [ad-creative](https://github.com/coreyhaines31/marketingskills/tree/main/skills/ad-creative) | Corey Haines | Generate, iterate, and scale ad creative across formats |
| [lead-magnets](https://github.com/coreyhaines31/marketingskills/tree/main/skills/lead-magnets) | Corey Haines | Create lead magnets that convert |
| [email-marketing-bible](https://github.com/CosmoBlk/email-marketing-bible) | CosmoBlk | Comprehensive email marketing skill (55K words) |
| [content-ops](https://github.com/ericosiu/ai-marketing-skills/tree/main/content-ops) | Eric Osiu | Content quality scoring and production pipeline |
| [Canva](https://canva.com) | Canva | Design templates, brand kit - the solo/SMB design standard |
| [Midjourney](https://midjourney.com) / [DALL-E](https://openai.com/dall-e) | Various | AI image generation - use with brand guidelines as constraints |

### SHIP: Push to channels, on schedule, in the right language

| Skill / Tool | Source | What it does |
| --- | --- | --- |
| [email-sequence](https://github.com/coreyhaines31/marketingskills/tree/main/skills/email-sequence) | Corey Haines | Build email sequences, drip campaigns, lifecycle flows |
| [cold-email](https://github.com/coreyhaines31/marketingskills/tree/main/skills/cold-email) | Corey Haines | Cold email outreach sequences |
| [social-content](https://github.com/coreyhaines31/marketingskills/tree/main/skills/social-content) | Corey Haines | Social media content creation and scheduling |
| [paid-ads](https://github.com/coreyhaines31/marketingskills/tree/main/skills/paid-ads) | Corey Haines | Paid advertising strategy and execution |
| [programmatic-seo](https://github.com/coreyhaines31/marketingskills/tree/main/skills/programmatic-seo) | Corey Haines | Programmatic SEO page generation at scale |
| [outbound-engine](https://github.com/ericosiu/ai-marketing-skills/tree/main/outbound-engine) | Eric Osiu | Cold outbound automation pipeline |
| [marketing-email](https://github.com/pawbytes/skill-suites/tree/main/src/marketing/paw-mkt-email) | pawbytes | Email marketing skill with lifecycle orchestration |
| [marketing-social](https://github.com/pawbytes/skill-suites/tree/main/src/marketing/paw-mkt-social) | pawbytes | Social media marketing and publishing |
| [marketing-paid-ads](https://github.com/pawbytes/skill-suites/tree/main/src/marketing/paw-mkt-paid-ads) | pawbytes | Paid advertising strategy and management |
| [x-article-publisher](https://github.com/wshuyi/x-article-publisher-skill) | wshuyi | Publish articles to X/Twitter |

### MULTIPLY: Reshape and personalize what you already made

| Skill / Tool | Source | What it does |
| --- | --- | --- |
| [page-cro](https://github.com/coreyhaines31/marketingskills/tree/main/skills/page-cro) | Corey Haines | Landing page conversion rate optimization |
| [signup-flow-cro](https://github.com/coreyhaines31/marketingskills/tree/main/skills/signup-flow-cro) | Corey Haines | Signup flow optimization |
| [form-cro](https://github.com/coreyhaines31/marketingskills/tree/main/skills/form-cro) | Corey Haines | Form conversion optimization |
| [popup-cro](https://github.com/coreyhaines31/marketingskills/tree/main/skills/popup-cro) | Corey Haines | Popup conversion optimization |
| [onboarding-cro](https://github.com/coreyhaines31/marketingskills/tree/main/skills/onboarding-cro) | Corey Haines | User onboarding flow optimization |
| [paywall-upgrade-cro](https://github.com/coreyhaines31/marketingskills/tree/main/skills/paywall-upgrade-cro) | Corey Haines | Paywall and upgrade conversion optimization |
| [ab-test-setup](https://github.com/coreyhaines31/marketingskills/tree/main/skills/ab-test-setup) | Corey Haines | A/B test design, setup, and analysis |
| [marketing-cro](https://github.com/pawbytes/skill-suites/tree/main/src/marketing/paw-mkt-cro) | pawbytes | Conversion rate optimization suite |
| [experimentation](https://github.com/realjaymes/marketingagentskills/tree/main/skills/experimentation) | James (MIA) | Experiment design and growth testing |

### MEASURE: Attribute, dashboard, analyze

| Skill / Tool | Source | What it does |
| --- | --- | --- |
| [analytics-tracking](https://github.com/coreyhaines31/marketingskills/tree/main/skills/analytics-tracking) | Corey Haines | Analytics setup, tracking plans, event architecture |
| [marketing-analytics](https://github.com/pawbytes/skill-suites/tree/main/src/marketing/paw-mkt-analytics) | pawbytes | Measurement and tracking skill |
| [revenue-intelligence](https://github.com/ericosiu/ai-marketing-skills/tree/main/revenue-intelligence) | Eric Osiu | Gong-based sales call insights + attribution pipeline |
| [Google Analytics 4](https://analytics.google.com) | Google (free) | Universal web analytics starting point |
| [Google Search Console](https://search.google.com/search-console) | Google (free) | Organic search performance and SEO health |

### LEARN: Close the loop, update the playbook

| Skill / Tool | Source | What it does |
| --- | --- | --- |
| [referral-program](https://github.com/coreyhaines31/marketingskills/tree/main/skills/referral-program) | Corey Haines | Referral and word-of-mouth program design |
| [churn-prevention](https://github.com/coreyhaines31/marketingskills/tree/main/skills/churn-prevention) | Corey Haines | Churn analysis and retention strategy |
| [marketing-retention](https://github.com/pawbytes/skill-suites/tree/main/src/marketing/paw-mkt-retention) | pawbytes | Churn reduction and win-back skill |
| [revops](https://github.com/coreyhaines31/marketingskills/tree/main/skills/revops) | Corey Haines | Revenue operations - bridging marketing, sales, and CS |

---

## SEO & Discovery (cross-cutting)

SEO spans SENSE (keyword research), DECIDE (content strategy), MAKE (content creation), and SHIP (publishing). These skills treat it as a unified discipline.

| Skill / Tool | Source | What it does |
| --- | --- | --- |
| [seo-audit](https://github.com/coreyhaines31/marketingskills/tree/main/skills/seo-audit) | Corey Haines | Comprehensive SEO audit workflow |
| [ai-seo](https://github.com/coreyhaines31/marketingskills/tree/main/skills/ai-seo) | Corey Haines | AI-native SEO content strategy |
| [schema-markup](https://github.com/coreyhaines31/marketingskills/tree/main/skills/schema-markup) | Corey Haines | Structured data and schema markup |
| [site-architecture](https://github.com/coreyhaines31/marketingskills/tree/main/skills/site-architecture) | Corey Haines | Site structure and information architecture for SEO |
| [claude-seo](https://github.com/AgriciDaniel/claude-seo) | AgriciDaniel | Universal SEO skill for website analysis and optimization |
| [seo-ops](https://github.com/ericosiu/ai-marketing-skills/tree/main/seo-ops) | Eric Osiu | SEO intelligence - content attack briefs, trend scouting, GSC integration |
| [marketing-seo](https://github.com/pawbytes/skill-suites/tree/main/src/marketing/paw-mkt-seo) | pawbytes | SEO and organic search skill |

---

## Standards & Protocols

The infrastructure layer that makes marketing skills portable and connectable.

| Standard | What it is | Why it matters |
| --- | --- | --- |
| [Agent Skills spec](https://agentskills.io) | Open format for giving agents new capabilities (SKILL.md files) | Compatible with 30+ tools listed on agentskills.io, including Claude Code, Claude, Cursor, VS Code, GitHub Copilot, OpenAI Codex, Gemini CLI, Goose, OpenHands, and Kiro. Build once, run everywhere. [Adobe has adopted the spec](https://developer.adobe.com/app-builder/docs/resources/ai-use-cases) for App Builder integrations (AEM, Workfront, Target, Marketo). |
| [Model Context Protocol (MCP)](https://modelcontextprotocol.io) | Open standard for connecting AI models to external tools and data sources | The nervous system: how agents securely reach your CMS, CRM, DAM, analytics. |
| [A2A](https://github.com/a2aproject/A2A) | Agent-to-Agent protocol for cross-framework communication | Agents talking to agents: emerging standard for multi-agent orchestration. Originated at Google, now maintained under the `a2aproject` organization. |
| [Composio MCP](https://composio.dev) | OAuth-heavy app integrations exposed via MCP (Composio advertises 500+ tools) | HubSpot, Salesforce, Slack, and similar made agent-accessible. Used by Corey Haines' marketingskills. |

---

## Awesome Lists by Others

Curated lists maintained by the community. Each covers a slice of the marketing + AI agent ecosystem.

| List | Focus | Stars |
| --- | --- | --- |
| [awesome-ai-marketing](https://github.com/jmedia65/awesome-ai-marketing) (jmedia65) | AI marketing tools with honest context on when each works | 3 |
| [awesome-ai-marketing](https://github.com/alternbits/awesome-ai-marketing) (alternbits) | AI tools for marketing professionals by category | 124 |
| [awesome-agentic-advertising](https://github.com/jshorwitz/awesome-agentic-advertising) | MCP servers for ad platforms - Google, Meta, LinkedIn, TikTok, X | 15 |
| [awesome-ai-seo](https://github.com/best-of-ai/awesome-ai-seo) | AI SEO tools, platforms, prompts, and resources | 212 |
| [awesome-ai-gtm](https://github.com/hculap/awesome-ai-gtm) | AI Go-to-Market stack - ideation through customer success | 4 |
| [awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) (VoltAgent) | 1000+ agent skills from official dev teams, includes marketing section | 16.2k |
| [awesome-llm-skills](https://github.com/Prat011/awesome-llm-skills) | LLM skills across all domains, includes marketing category | 1.1k |
| [awesome-ai-agents-2026](https://github.com/caramaschiHG/awesome-ai-agents-2026) | 340+ AI agents, frameworks, and tools across 20+ categories | 318 |

---

## Meta-Skills & Orchestration

Skills that coordinate other skills or help build new ones.

| Skill | Source | What it does |
| --- | --- | --- |
| [marketing-agency](https://github.com/pawbytes/skill-suites/tree/main/src/marketing/paw-mkt-agency) | pawbytes | Coordinator agent: routes any marketing task to the right specialist skill |
| [agent-skill-builder](https://github.com/realjaymes/marketingagentskills/tree/main/skills/agent-skill-builder) | James (MIA) | Create new skills from scratch or translate ChatGPT projects into Agent Skills format |
| [product-marketing-context](https://github.com/coreyhaines31/marketingskills/tree/main/skills/product-marketing-context) | Corey Haines | Shared context file read by all skills: reduces repetitive questions across workflows |
| [growth-engine](https://github.com/ericosiu/ai-marketing-skills/tree/main/growth-engine) | Eric Osiu | Autonomous marketing experiments that run, measure, and optimize themselves |

---

*Star counts approximate as of April 2026. Links verified against public GitHub repos. If you find a broken link or want to suggest an addition, open an issue or PR.*
