# Marketing Vendor & Tool Companion

*Companion to [Marketing-Anatomy.md](Marketing-Anatomy.md). This is a living document - vendors enter, consolidate, and exit fast. Treat every entry as a starting point for your own due diligence, not as an endorsement.*

*Vendor landscape as of knowledge cutoff May 2025 - verify currency before citing or purchasing.*

**How to read the table:**

- **Size Fit** uses the same 3-tier notation as the Anatomy: **S** (Solo), **SMB**, **E** (Enterprise). Symbols: ● target buyer, ◐ usable, — overkill or not available.
- **DIY viable?** flags whether a solo or SMB user could reasonably replicate the core capability with an AI agent instead of buying.

---

## SENSE: Watch the water for signals

| Vendor / Tool | Capability | Size Fit | DIY viable? | Notes |
| --- | --- | --- | --- | --- |
| Google Trends | Free trend/search interest tracking | S:● SMB:● E:◐ | N/A - already free | Starting point for any size; limited depth |
| Google Alerts | Free keyword-based web monitoring | S:● SMB:● E:◐ | N/A - already free | Set up in 2 minutes; no historical data |
| Brandwatch | Social listening, trend analysis, sentiment | S:— SMB:◐ E:● | Partially - AI can scrape public feeds but lacks Brandwatch's historical index | Enterprise-grade; acquired by Cision |
| Sprout Social | Social listening + management | S:— SMB:● E:● | Partially - publishing yes, listening depth no | Strong SMB on-ramp; includes scheduling |
| Talkwalker | AI-powered consumer intelligence | S:— SMB:◐ E:● | No - proprietary data lake | Competes with Brandwatch at enterprise |
| Meltwater | Media monitoring, PR analytics | S:— SMB:◐ E:● | No - proprietary media database | Strongest for earned media / PR tracking |
| X (Twitter) | Real-time trending topics, hashtag monitoring, public conversation | S:● SMB:● E:● | Partially - free to browse; AI can scrape, but X's firehose API is the enterprise play | Real-time public conversation at volume; every marketer should be watching it |
| Reddit | Community signals, niche sentiment, product feedback | S:● SMB:● E:◐ | Partially - free to browse; subreddit monitoring is AI-friendly | Increasingly important for authentic voice-of-customer signals |
| ScrapeCreators | Multi-platform scraping API (27+ platforms, 110+ endpoints — TikTok, IG, YT, LinkedIn, FB, X, Reddit, Threads, Bluesky, Pinterest, Snapchat, Twitch, Google SERPs, Amazon Shop, plus FB/Google/LinkedIn ad libraries) | S:● SMB:● E:◐ | No - the moat is keeping 27+ platforms un-blocked; but consumption is agent-native (vendor ships MCP + CLI + official SKILL.md) | Pay-as-you-go: Free 100 / $47 Freelance (25k credits) / $497 Business (500k) / custom Enterprise. No rate limits. Credits never expire. Hosted MCP at `api.scrapecreators.com/mcp`, CLI `@scrapecreators/cli`, Agent Skill at `ScrapeCreators/agent-skills`. Full review: [tool-reviews/scrapecreators.md](tool-reviews/scrapecreators.md) |
| Profound (Prompt Volumes) | Demand-side GEO intelligence: what millions ask AI chat engines, aggregated across ChatGPT / Perplexity / AI Overviews / Gemini / Claude | S:— SMB:◐ E:● | No - proprietary dataset, vendor moat; Enterprise-tier only | Companion dataset to Profound's Answer Engine Insights. Vendor calls the category AEO (Answer Engine Optimization); house term is GEO. Full review: [tool-reviews/profound.md](tool-reviews/profound.md) |

## KNOW: Build and maintain audience intelligence

| Vendor / Tool | Capability | Size Fit | DIY viable? | Notes |
| --- | --- | --- | --- | --- |
| HubSpot (CRM + personas) | Contact management, basic persona tools | S:◐ SMB:● E:● | Partially - AI can build persona docs, but CRM data layer is the value | Free tier available; grows with you. Enterprise tier is now a real segment, not an afterthought |
| Segment (Twilio) | Customer data platform (CDP) | S:— SMB:◐ E:● | No - infrastructure play | The plumbing that unifies audience data. Twilio retained Segment in 2024 after reviewing divestment |
| Bloomreach | CDP + personalization engine | S:— SMB:— E:● | No - deep commerce integration | Strong in e-commerce / retail verticals |
| Adobe Experience Platform (AEP) | Real-time CDP, unified customer profiles, journey orchestration | S:— SMB:— E:● | No - enterprise real-time identity resolution at scale | The backbone of Adobe's enterprise stack; feeds Target, Campaign, Journey Optimizer |
| Salesforce CRM | Contact/account management, lead tracking, opportunity pipeline | S:◐ SMB:● E:● | Partially - a spreadsheet + AI works for solo, but CRM is the system of record at scale | The enterprise default; everything else in the Salesforce ecosystem rides on this |
| Salesforce Data Cloud | CDP, unified profiles, real-time data activation | S:— SMB:— E:● | No - enterprise data unification layer | Salesforce's answer to AEP; connects CRM + Marketing Cloud + Commerce |
| Typeform / Tally | Survey + form builder | S:● SMB:● E:◐ | Partially - AI can draft surveys, but distribution is the value | Solo-friendly for primary research |
| SparkToro | Audience research (who they follow, read, listen to) | S:● SMB:● E:◐ | Partially - AI can approximate but lacks SparkToro's crawl index | Rand Fishkin's tool; great for solo/SMB |
| LinkedIn (audience tools) | Professional demographics, job titles, company size, industry targeting | S:● SMB:● E:● | No - LinkedIn's professional graph is proprietary and unique | The only platform with reliable B2B audience data at scale |
| Meta (Audience Insights) | Interest-based segments, lookalike audiences, behavioral data | S:◐ SMB:● E:● | No - Meta's behavioral graph is proprietary | Facebook + Instagram combined audience intelligence |

## DECIDE: Choose what to say, to whom, when, for how much

| Vendor / Tool | Capability | Size Fit | DIY viable? | Notes |
| --- | --- | --- | --- | --- |
| Notion / Coda | Editorial calendar, planning wiki | S:● SMB:● E:◐ | Yes - AI + a spreadsheet works | The simplest viable content calendar. Notion also appears under LEARN for knowledge-base use |
| CoSchedule | Marketing calendar + workflow | S:◐ SMB:● E:◐ | Partially - scheduling is DIY-able, cross-team coordination isn't | Purpose-built for content teams |
| HubSpot Marketing Hub | Campaign planning, automation, calendar | S:— SMB:● E:● | Partially - planning yes, automation engine no | The SMB workhorse |
| Marketo (Adobe) | Enterprise marketing automation | S:— SMB:— E:● | No - deep enterprise integration | Complex setup; powerful at scale |

## MAKE: Produce the assets

| Vendor / Tool | Capability | Size Fit | DIY viable? | Notes |
| --- | --- | --- | --- | --- |
| Adobe Creative Cloud | Professional design, video, photo | S:— SMB:◐ E:● | No - professional-grade tooling | Industry standard for enterprise creative |
| AEM Assets (Adobe DAM) | Digital asset management, metadata, rights, renditions | S:— SMB:— E:● | No - enterprise asset governance | The single source of truth for brand assets at scale; integrates with AEM Sites |
| Cloudinary | Image/video management, optimization, transformation, AI tagging | S:◐ SMB:● E:● | Partially - API-first and has an MCP server; AI features rival standalone tools | Developer-focused; already MCP-ready for agentic workflows. Generative fill, smart crop, auto-tag |
| Aprimo | Enterprise DAM + content operations, AI-powered workflows | S:— SMB:— E:● | No - enterprise content governance at Fortune 500 scale | Named a Leader in the 2025 Gartner Magic Quadrant for DAM. Positions itself as an "agentic DAM" with AI agents for compliance, tagging, planning |
| Bynder | Brand asset management, creative workflows, brand guidelines | S:— SMB:◐ E:● | No - brand portal + approval workflows are the moat | Strong for brand consistency at scale; lighter than Aprimo |
| Canva | Design, templates, brand kit, AI image generation | S:● SMB:● E:● | Partially - AI image tools compete, but Canva's templates are the real value | The solo/SMB design standard; Canva Enterprise (SSO, compliance) makes it viable at large orgs |
| Jasper | AI copy + brand voice | S:◐ SMB:● E:● | Yes - an AI agent with a brand voice SOP replicates core Jasper | Early mover in AI copy; enterprise features |
| Writer | Enterprise AI writing + style guide enforcement | S:— SMB:◐ E:● | Partially - AI can enforce style, but Writer's governance layer is the moat | Strong compliance / brand governance |
| Typeface | AI content generation with brand controls | S:— SMB:◐ E:● | Partially - the brand-safe generation pipeline is hard to replicate | Image Agent category leader (verify currency before engaging) |
| Copy.ai | AI copy workflows + templates | S:● SMB:● E:◐ | Yes - comparable output from a well-prompted agent | Good entry point; less enterprise governance |
| Midjourney / DALL-E | AI image generation | S:● SMB:● E:◐ | N/A - these *are* the AI tools | Use with brand guidelines as constraints |
| Runway | AI video generation + editing | S:◐ SMB:◐ E:◐ | Partially - AI video is still maturing across the board | Frontier tech; quality improving fast |

## SHIP: Push to channels, on schedule, in the right language

| Vendor / Tool | Capability | Size Fit | DIY viable? | Notes |
| --- | --- | --- | --- | --- |
| Mailchimp | Email marketing + basic automation | S:● SMB:● E:— | Partially - AI can draft emails, but deliverability infra is Mailchimp's value | Free tier for solo; the default SMB email tool |
| Buffer / Hootsuite | Social media scheduling + analytics | S:● SMB:● E:◐ | Partially - scheduling yes, cross-platform analytics no | Solo essential; enterprise uses native tools |
| Braze | Cross-channel customer engagement | S:— SMB:— E:● | No - deep real-time personalization engine | Mobile-first; lifecycle orchestration |
| Iterable | Cross-channel marketing automation | S:— SMB:◐ E:● | No - event-driven journey orchestration | Competes with Braze at enterprise |
| WordPress | CMS powering ~43% of all websites; plugins, themes, WooCommerce | S:● SMB:● E:● | Partially - AI can draft posts, but WordPress is the publishing infra | Powers ~43% of all websites. CMS-market share has dipped from a ~65% peak (2022) to ~60%. VIP tier powers enterprise sites (e.g. White House, Sony, Wired); solo essential |
| Shopify | E-commerce CMS, storefront, payments, fulfillment | S:● SMB:● E:● | No - you're buying the commerce infrastructure | #2 CMS globally (~6.8%); Shopify Plus is the explicit enterprise tier |
| Squarespace / Wix | Website builders, templates, hosting, basic e-commerce | S:● SMB:◐ E:— | Partially - AI site builders are emerging but these are proven and fast | Solo/micro-biz default for "I need a site today"; growing at WordPress's expense |
| Webflow | Design-first CMS, visual builder, hosting, interactions | S:◐ SMB:● E:◐ | No - the visual builder is the product | Fastest-growing design CMS (~1.2% share); strong for agencies and design-led brands |
| Drupal / Acquia | Enterprise open-source CMS; Acquia is the commercial Drupal platform | S:— SMB:— E:● | No - enterprise-grade security, compliance, multilingual, content workflows | Declining market share (~1.1%) but entrenched in government (White House, NASA) and higher education. Acquia has been a Leader in the Gartner Magic Quadrant for DXP each year through 2025 |
| Sitecore | Enterprise DXP, CMS, personalization, commerce | S:— SMB:— E:● | No - deep enterprise content + personalization platform | Long-standing enterprise DXP; strong in .NET enterprise shops |
| Contentful | Headless CMS, API-first, structured content | S:— SMB:● E:● | No - the content infrastructure layer for modern apps | The headless CMS leader; content delivered via API to any frontend |
| Contentstack | Headless CMS, composable DXP | S:— SMB:◐ E:● | No - composable enterprise content platform | Composable enterprise content platform; competes with Contentful at enterprise |
| AEM Sites (Adobe) | Enterprise CMS, content fragments, multi-site management | S:— SMB:— E:● | No - enterprise web content infrastructure | The publishing backbone for global Adobe-stack brands |
| Adobe Campaign | Cross-channel orchestration, email, push, SMS | S:— SMB:— E:● | No - deep journey orchestration tied to AEP profiles | Competes with Salesforce Marketing Cloud at enterprise |
| Salesforce Marketing Cloud | Enterprise omnichannel marketing | S:— SMB:— E:● | No - the enterprise elephant | Deep Salesforce ecosystem integration |
| Salesforce Pardot (Account Engagement) | B2B marketing automation, lead nurturing, scoring | S:— SMB:◐ E:● | Partially - AI can draft nurture emails, but scoring engine + CRM sync is the value | The B2B counterpart to Marketing Cloud; rides on Salesforce CRM |
| Salesforce Commerce Cloud | E-commerce storefronts, order management, merchandising | S:— SMB:— E:● | No - enterprise commerce infrastructure | Where marketing meets revenue for retail/DTC brands |
| Smartling / Phrase | Translation management + localization | S:— SMB:◐ E:● | Partially - AI translation is strong for solo, but TMS workflow is the value at scale | Enterprise localization infrastructure |
| Google Ads | Paid search (SEM), display, YouTube ads, Performance Max | S:● SMB:● E:● | No - you're buying access to Google's search intent graph | The #1 paid channel for most businesses; solo can start at $5/day |
| Meta Ads (Facebook + Instagram) | Paid social, retargeting, lookalike audiences, shop integration | S:● SMB:● E:● | No - you're buying access to Meta's behavioral graph | Largest social ad platform; strong for B2C and local business |
| LinkedIn Ads | Paid B2B targeting by job title, company, industry, seniority | S:◐ SMB:● E:● | No - LinkedIn's professional targeting is unmatched | Expensive per-click but highest-quality B2B leads |
| X Ads (Twitter) | Promoted posts, trending takeovers, follower campaigns | S:◐ SMB:◐ E:● | No - you're buying reach into X's real-time conversation | Volatile platform; strong for brand awareness and event-driven moments |
| TikTok Ads | Short-form video ads, creator partnerships, shop integration | S:◐ SMB:● E:● | No - you're buying into TikTok's algorithm and Gen Z/Millennial audience | Fastest-growing ad platform; strong for consumer brands |
| YouTube (Google) | Video ads (pre-roll, discovery, shorts), channel publishing | S:● SMB:● E:● | Partially - organic publishing is free; paid ads require Google Ads | Second-largest search engine; video is the medium for every tier |
| Pinterest Ads | Visual discovery ads, shopping pins, idea pins | S:◐ SMB:● E:◐ | No - Pinterest's intent-driven visual search is proprietary | Strong for home, fashion, food, wedding verticals |

## MULTIPLY: Reshape and personalize what you already made

| Vendor / Tool | Capability | Size Fit | DIY viable? | Notes |
| --- | --- | --- | --- | --- |
| Optimizely | A/B testing, experimentation, CMS | S:— SMB:◐ E:● | Partially - basic A/B via free tools, but statistical rigor at scale needs Optimizely | The experimentation standard |
| VWO | A/B testing + CRO | S:— SMB:● E:◐ | Partially - simpler than Optimizely, more SMB-accessible | Good SMB alternative to Optimizely |
| Unbounce | Landing page builder + smart traffic | S:◐ SMB:● E:◐ | Partially - AI can build landing pages, but Unbounce's traffic routing is the value | Purpose-built for conversion |
| Adobe Target | A/B testing, multivariate testing, AI-powered personalization | S:— SMB:— E:● | No - deep integration with AEP profiles + AEM content | The enterprise experimentation standard in Adobe shops; Sensei AI auto-allocates |
| Dynamic Yield | Personalization engine | S:— SMB:— E:● | No - enterprise real-time personalization | Deep commerce personalization; Dynamic Yield advertises ~300 global brands on its own pages |

## MEASURE: Attribute, dashboard, analyze

| Vendor / Tool | Capability | Size Fit | DIY viable? | Notes |
| --- | --- | --- | --- | --- |
| Google Analytics 4 | Web + app analytics | S:● SMB:● E:● | N/A - already free | Universal starting point; everyone needs this |
| Adobe Analytics | Enterprise web + app analytics, real-time segmentation, attribution | S:— SMB:— E:● | No - enterprise analytics infrastructure tied to AEP | The enterprise alternative to GA4; deeper segmentation, real-time data, Analysis Workspace |
| Amplitude | Product analytics, behavioral cohorts | S:— SMB:● E:● | No - behavioral analytics infrastructure | Strong for product-led growth |
| Mixpanel | Event-based product analytics | S:— SMB:● E:● | No - competes with Amplitude | Simpler setup than Amplitude |
| Looker (Google) | BI + data exploration | S:— SMB:◐ E:● | No - enterprise BI infrastructure | Requires data warehouse |
| Tableau (Salesforce) | BI + visualization | S:— SMB:◐ E:● | No - enterprise BI standard | Powerful but heavy; Salesforce ecosystem |
| Heap (Contentsquare) | Auto-capture analytics | S:— SMB:● E:● | No - retroactive analytics is the unique value | Captures everything; query later. Acquired by Contentsquare in Dec 2023 and being integrated into the Contentsquare experience-analytics platform |
| Meta Business Suite | Facebook + Instagram ad performance, audience insights, organic metrics | S:● SMB:● E:● | N/A - free with any Meta business account | If you run Meta Ads, this is where you measure them |
| LinkedIn Campaign Manager | B2B ad performance, lead gen metrics, demographic breakdown | S:◐ SMB:● E:● | N/A - free with any LinkedIn ad account | The only place to measure LinkedIn Ads performance |
| Google Search Console | Organic search performance, indexing, SEO health | S:● SMB:● E:● | N/A - already free | Pairs with GA4; essential for any SEO work |
| Profound | AI-visibility tracking across ChatGPT / Perplexity / AI Overviews / Gemini / Claude; citation + sentiment reports; AI-crawler (agent) analytics with CDN log ingestion | S:— SMB:◐ E:● | No - proprietary consumer-browser capture across 10+ engines; vendor-first-party MCP + SDKs dominate the consumption surface | Starter $99/mo (ChatGPT only); Growth $399/mo (multi-engine); API + MCP Enterprise-tier only. Hosted MCP at `mcp.tryprofound.com`, plus Python + TypeScript SDKs (launched 2026-03-31). Series C $96M at $1B valuation (Feb 2026). Vendor calls the category AEO (Answer Engine Optimization); house term is GEO. Full review: [tool-reviews/profound.md](tool-reviews/profound.md) |

## LEARN: Close the loop, update the playbook

| Vendor / Tool | Capability | Size Fit | DIY viable? | Notes |
| --- | --- | --- | --- | --- |
| Notion | Wiki, retrospective docs, knowledge base | S:● SMB:● E:◐ | Partially - AI can generate retro docs, but Notion's collaboration is the value | The solo/SMB knowledge home. Notion also appears under DECIDE for editorial-calendar use |
| Confluence (Atlassian) | Enterprise wiki + knowledge management | S:— SMB:◐ E:● | Partially - the tool is less important than the habit | Enterprise standard; Jira integration |
| Airtable | Structured knowledge + workflow tracking | S:◐ SMB:● E:◐ | Partially - a spreadsheet + AI can approximate | Flexible; sits between spreadsheet and database |

---

## Stack Notes

Several vendors above are sold as coherent stacks rather than standalone products. Individual rows list them by verb; the integration is the value.

- **Adobe Experience Cloud** ties together AEM Sites (SHIP), AEM Assets (MAKE), AEP (KNOW), Adobe Target (MULTIPLY), Adobe Campaign (SHIP), and Adobe Analytics (MEASURE).
- **Salesforce Marketing ecosystem** ties together Salesforce CRM (KNOW), Salesforce Data Cloud (KNOW), Marketing Cloud (SHIP), Pardot / Account Engagement (SHIP), Commerce Cloud (SHIP), and Tableau (MEASURE).
- **Notion** appears in both DECIDE (editorial calendar) and LEARN (knowledge base); same tool, distinct use cases.

---

## Out of Scope (intentional)

This companion focuses on tooling directly tied to the 8 marketing verbs. Several adjacent categories are deliberately omitted and may be added as the project grows:

- **PR / influencer / community** (BuzzSumo, Sprinklr Community, Muck Rack).
- **Review and reputation management** (G2, Trustpilot).
- **Video hosting and editing** beyond YouTube ads (Wistia, Vimeo, Loom).
- **Event and webinar platforms** (Zoom Webinars, Hopin).
- **CDP selection guidance**: multiple CDPs are listed in KNOW (Segment, Bloomreach, AEP, Salesforce Data Cloud) but the decision has stack-wide consequences not covered here.
- **Composable vs monolithic DXP**: both patterns are represented under SHIP without a decision guide.

If one of these is load-bearing for your engagement, open an issue or PR.

---

*This companion is deliberately seeded, not exhaustive. Add vendors as you encounter them in real engagements. The "DIY viable?" column is the most important one - it tells you when to build and when to buy.*
