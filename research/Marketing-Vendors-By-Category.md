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
| Google Trends | Free trend/search interest tracking | S:● SMB:● E:◐ | N/A — already free | Starting point for any size; limited depth |
| Google Alerts | Free keyword-based web monitoring | S:● SMB:● E:◐ | N/A — already free | Set up in 2 minutes; no historical data |
| Brandwatch | Social listening, trend analysis, sentiment | S:— SMB:◐ E:● | Partially — AI can scrape public feeds but lacks Brandwatch's historical index | Enterprise-grade; acquired by Cision |
| Sprout Social | Social listening + management | S:— SMB:● E:● | Partially — publishing yes, listening depth no | Strong SMB on-ramp; includes scheduling |
| Talkwalker | AI-powered consumer intelligence | S:— SMB:◐ E:● | No — proprietary data lake | Competes with Brandwatch at enterprise |
| Meltwater | Media monitoring, PR analytics | S:— SMB:◐ E:● | No — proprietary media database | Strongest for earned media / PR tracking |
| X (Twitter) | Real-time trending topics, hashtag monitoring, public conversation | S:● SMB:● E:● | Partially — free to browse; AI can scrape, but X's firehose API is the enterprise play | THE real-time signal platform; every marketer should be watching it |
| Reddit | Community signals, niche sentiment, product feedback | S:● SMB:● E:◐ | Partially — free to browse; subreddit monitoring is AI-friendly | Increasingly important for authentic voice-of-customer signals |

## KNOW: Build and maintain audience intelligence

| Vendor / Tool | Capability | Size Fit | DIY viable? | Notes |
| --- | --- | --- | --- | --- |
| HubSpot (CRM + personas) | Contact management, basic persona tools | S:◐ SMB:● E:◐ | Partially — AI can build persona docs, but CRM data layer is the value | Free tier available; grows with you |
| Segment (Twilio) | Customer data platform (CDP) | S:— SMB:◐ E:● | No — infrastructure play | The plumbing that unifies audience data |
| Bloomreach | CDP + personalization engine | S:— SMB:— E:● | No — deep commerce integration | Strong in e-commerce / retail verticals |
| Adobe Experience Platform (AEP) | Real-time CDP, unified customer profiles, journey orchestration | S:— SMB:— E:● | No — enterprise real-time identity resolution at scale | The backbone of Adobe's enterprise stack; feeds Target, Campaign, Journey Optimizer |
| Salesforce CRM | Contact/account management, lead tracking, opportunity pipeline | S:◐ SMB:● E:● | Partially — a spreadsheet + AI works for solo, but CRM is the system of record at scale | The enterprise default; everything else in the Salesforce ecosystem rides on this |
| Salesforce Data Cloud | CDP, unified profiles, real-time data activation | S:— SMB:— E:● | No — enterprise data unification layer | Salesforce's answer to AEP; connects CRM + Marketing Cloud + Commerce |
| Typeform / Tally | Survey + form builder | S:● SMB:● E:◐ | Partially — AI can draft surveys, but distribution is the value | Solo-friendly for primary research |
| SparkToro | Audience research (who they follow, read, listen to) | S:● SMB:● E:◐ | Partially — AI can approximate but lacks SparkToro's crawl index | Rand Fishkin's tool; great for solo/SMB |
| LinkedIn (audience tools) | Professional demographics, job titles, company size, industry targeting | S:● SMB:● E:● | No — LinkedIn's professional graph is proprietary and unique | The only platform with reliable B2B audience data at scale |
| Meta (Audience Insights) | Interest-based segments, lookalike audiences, behavioral data | S:◐ SMB:● E:● | No — Meta's behavioral graph is proprietary | Facebook + Instagram combined audience intelligence |

## DECIDE: Choose what to say, to whom, when, for how much

| Vendor / Tool | Capability | Size Fit | DIY viable? | Notes |
| --- | --- | --- | --- | --- |
| Notion / Coda | Editorial calendar, planning wiki | S:● SMB:● E:◐ | Yes — AI + a spreadsheet works | The simplest viable content calendar |
| CoSchedule | Marketing calendar + workflow | S:◐ SMB:● E:◐ | Partially — scheduling is DIY-able, cross-team coordination isn't | Purpose-built for content teams |
| HubSpot Marketing Hub | Campaign planning, automation, calendar | S:— SMB:● E:● | Partially — planning yes, automation engine no | The SMB workhorse |
| Marketo (Adobe) | Enterprise marketing automation | S:— SMB:— E:● | No — deep enterprise integration | Complex setup; powerful at scale |

## MAKE: Produce the assets

| Vendor / Tool | Capability | Size Fit | DIY viable? | Notes |
| --- | --- | --- | --- | --- |
| Adobe Creative Cloud | Professional design, video, photo | S:— SMB:◐ E:● | No — professional-grade tooling | Industry standard for enterprise creative |
| AEM Assets (Adobe DAM) | Digital asset management, metadata, rights, renditions | S:— SMB:— E:● | No — enterprise asset governance + MCP connector target | The single source of truth for brand assets at scale; integrates with AEM Sites |
| Cloudinary | Image/video management, optimization, transformation, AI tagging | S:◐ SMB:● E:● | Partially — API-first and has an MCP server; AI features rival standalone tools | Developer-focused; already MCP-ready for agentic workflows. Generative fill, smart crop, auto-tag |
| Aprimo | Enterprise DAM + content operations, AI-powered workflows | S:— SMB:— E:● | No — enterprise content governance at Fortune 500 scale | Gartner DAM Leader #1 (2025); "agentic DAM" with AI agents for compliance, tagging, planning |
| Bynder | Brand asset management, creative workflows, brand guidelines | S:— SMB:◐ E:● | No — brand portal + approval workflows are the moat | Strong for brand consistency at scale; lighter than Aprimo |
| Canva | Design, templates, brand kit, AI image generation | S:● SMB:● E:◐ | Partially — AI image tools compete, but Canva's templates are the real value | The solo/SMB design standard; increasingly enterprise-capable |
| Jasper | AI copy + brand voice | S:◐ SMB:● E:● | Yes — an AI agent with a brand voice SOP replicates core Jasper | Early mover in AI copy; enterprise features |
| Writer | Enterprise AI writing + style guide enforcement | S:— SMB:◐ E:● | Partially — AI can enforce style, but Writer's governance layer is the moat | Strong compliance / brand governance |
| Typeface | AI content generation with brand controls | S:— SMB:◐ E:● | Partially — the brand-safe generation pipeline is hard to replicate | Image Agent category leader |
| Copy.ai | AI copy workflows + templates | S:● SMB:● E:◐ | Yes — comparable output from a well-prompted agent | Good entry point; less enterprise governance |
| Midjourney / DALL-E | AI image generation | S:● SMB:● E:◐ | N/A — these *are* the AI tools | Use with brand guidelines as constraints |
| Runway | AI video generation + editing | S:◐ SMB:◐ E:◐ | Partially — AI video is still maturing across the board | Frontier tech; quality improving fast |

## SHIP: Push to channels, on schedule, in the right language

| Vendor / Tool | Capability | Size Fit | DIY viable? | Notes |
| --- | --- | --- | --- | --- |
| Mailchimp | Email marketing + basic automation | S:● SMB:● E:— | Partially — AI can draft emails, but deliverability infra is Mailchimp's value | Free tier for solo; the default SMB email tool |
| Buffer / Hootsuite | Social media scheduling + analytics | S:● SMB:● E:◐ | Partially — scheduling yes, cross-platform analytics no | Solo essential; enterprise uses native tools |
| Braze | Cross-channel customer engagement | S:— SMB:— E:● | No — deep real-time personalization engine | Mobile-first; lifecycle orchestration |
| Iterable | Cross-channel marketing automation | S:— SMB:◐ E:● | No — event-driven journey orchestration | Competes with Braze at enterprise |
| WordPress | CMS powering 43% of all websites; plugins, themes, WooCommerce | S:● SMB:● E:◐ | Partially — AI can draft posts, but WordPress is the publishing infra | The global default; declining from 65% peak but still dominant. Solo essential |
| Shopify | E-commerce CMS, storefront, payments, fulfillment | S:● SMB:● E:◐ | No — you're buying the commerce infrastructure | #2 CMS globally (6.8%); the e-commerce default for solo through mid-market |
| Squarespace / Wix | Website builders, templates, hosting, basic e-commerce | S:● SMB:◐ E:— | Partially — AI site builders are emerging but these are proven and fast | Solo/micro-biz default for "I need a site today"; growing at WordPress's expense |
| Webflow | Design-first CMS, visual builder, hosting, interactions | S:◐ SMB:● E:◐ | No — the visual builder is the product | Fastest-growing design CMS (1.2% share); strong for agencies and design-led brands |
| Drupal / Acquia | Enterprise open-source CMS; Acquia is the commercial Drupal platform | S:— SMB:— E:● | No — enterprise-grade security, compliance, multilingual, content workflows | Declining (1.1% share, down 31%) but entrenched: government (White House, NASA), universities (80% of top 100). Acquia is Gartner DXP Leader 6 years running |
| Sitecore | Enterprise DXP, CMS, personalization, commerce | S:— SMB:— E:● | No — deep enterprise content + personalization platform | Gartner DXP Leader; strong in .NET enterprise shops |
| Contentful | Headless CMS, API-first, structured content | S:— SMB:● E:● | No — the content infrastructure layer for modern apps | The headless CMS leader; content delivered via API to any frontend |
| Contentstack | Headless CMS, composable DXP | S:— SMB:◐ E:● | No — composable enterprise content platform | Gartner DXP Leader (2025); competes with Contentful at enterprise |
| AEM Sites (Adobe) | Enterprise CMS, content fragments, multi-site management | S:— SMB:— E:● | No — enterprise web content infrastructure + MCP connector target | The publishing backbone for global brands; content fragments are the unit agents can read/write via MCP |
| Adobe Campaign | Cross-channel orchestration, email, push, SMS | S:— SMB:— E:● | No — deep journey orchestration tied to AEP profiles | Competes with Salesforce Marketing Cloud at enterprise |
| Salesforce Marketing Cloud | Enterprise omnichannel marketing | S:— SMB:— E:● | No — the enterprise elephant | Deep Salesforce ecosystem integration |
| Salesforce Pardot (Account Engagement) | B2B marketing automation, lead nurturing, scoring | S:— SMB:◐ E:● | Partially — AI can draft nurture emails, but scoring engine + CRM sync is the value | The B2B counterpart to Marketing Cloud; rides on Salesforce CRM |
| Salesforce Commerce Cloud | E-commerce storefronts, order management, merchandising | S:— SMB:— E:● | No — enterprise commerce infrastructure | Where marketing meets revenue for retail/DTC brands |
| Smartling / Phrase | Translation management + localization | S:— SMB:◐ E:● | Partially — AI translation is strong for solo, but TMS workflow is the value at scale | Enterprise localization infrastructure |
| Google Ads | Paid search (SEM), display, YouTube ads, Performance Max | S:● SMB:● E:● | No — you're buying access to Google's search intent graph | The #1 paid channel for most businesses; solo can start at $5/day |
| Meta Ads (Facebook + Instagram) | Paid social, retargeting, lookalike audiences, shop integration | S:● SMB:● E:● | No — you're buying access to Meta's behavioral graph | Largest social ad platform; strong for B2C and local business |
| LinkedIn Ads | Paid B2B targeting by job title, company, industry, seniority | S:◐ SMB:● E:● | No — LinkedIn's professional targeting is unmatched | Expensive per-click but highest-quality B2B leads |
| X Ads (Twitter) | Promoted posts, trending takeovers, follower campaigns | S:◐ SMB:◐ E:● | No — you're buying reach into X's real-time conversation | Volatile platform; strong for brand awareness and event-driven moments |
| TikTok Ads | Short-form video ads, creator partnerships, shop integration | S:◐ SMB:● E:● | No — you're buying into TikTok's algorithm and Gen Z/Millennial audience | Fastest-growing ad platform; strong for consumer brands |
| YouTube (Google) | Video ads (pre-roll, discovery, shorts), channel publishing | S:● SMB:● E:● | Partially — organic publishing is free; paid ads require Google Ads | Second-largest search engine; video is the medium for every tier |
| Pinterest Ads | Visual discovery ads, shopping pins, idea pins | S:◐ SMB:● E:◐ | No — Pinterest's intent-driven visual search is proprietary | Strong for home, fashion, food, wedding verticals |

## MULTIPLY: Reshape and personalize what you already made

| Vendor / Tool | Capability | Size Fit | DIY viable? | Notes |
| --- | --- | --- | --- | --- |
| Optimizely | A/B testing, experimentation, CMS | S:— SMB:◐ E:● | Partially — basic A/B via free tools, but statistical rigor at scale needs Optimizely | The experimentation standard |
| VWO | A/B testing + CRO | S:— SMB:● E:◐ | Partially — simpler than Optimizely, more SMB-accessible | Good SMB alternative to Optimizely |
| Unbounce | Landing page builder + smart traffic | S:◐ SMB:● E:◐ | Partially — AI can build landing pages, but Unbounce's traffic routing is the value | Purpose-built for conversion |
| Adobe Target | A/B testing, multivariate testing, AI-powered personalization | S:— SMB:— E:● | No — deep integration with AEP profiles + AEM content | The enterprise experimentation standard in Adobe shops; Sensei AI auto-allocates |
| Dynamic Yield | Personalization engine | S:— SMB:— E:● | No — enterprise real-time personalization | Deep commerce personalization; 400+ global brands |

## MEASURE: Attribute, dashboard, analyze

| Vendor / Tool | Capability | Size Fit | DIY viable? | Notes |
| --- | --- | --- | --- | --- |
| Google Analytics 4 | Web + app analytics | S:● SMB:● E:● | N/A — already free | Universal starting point; everyone needs this |
| Adobe Analytics | Enterprise web + app analytics, real-time segmentation, attribution | S:— SMB:— E:● | No — enterprise analytics infrastructure tied to AEP | The enterprise alternative to GA4; deeper segmentation, real-time data, Analysis Workspace |
| Amplitude | Product analytics, behavioral cohorts | S:— SMB:● E:● | No — behavioral analytics infrastructure | Strong for product-led growth |
| Mixpanel | Event-based product analytics | S:— SMB:● E:● | No — competes with Amplitude | Simpler setup than Amplitude |
| Looker (Google) | BI + data exploration | S:— SMB:◐ E:● | No — enterprise BI infrastructure | Requires data warehouse |
| Tableau (Salesforce) | BI + visualization | S:— SMB:◐ E:● | No — enterprise BI standard | Powerful but heavy; Salesforce ecosystem |
| Heap | Auto-capture analytics | S:— SMB:● E:◐ | No — retroactive analytics is the unique value | Captures everything; query later |
| Meta Business Suite | Facebook + Instagram ad performance, audience insights, organic metrics | S:● SMB:● E:● | N/A — free with any Meta business account | If you run Meta Ads, this is where you measure them |
| LinkedIn Campaign Manager | B2B ad performance, lead gen metrics, demographic breakdown | S:◐ SMB:● E:● | N/A — free with any LinkedIn ad account | The only place to measure LinkedIn Ads performance |
| Google Search Console | Organic search performance, indexing, SEO health | S:● SMB:● E:● | N/A — already free | Pairs with GA4; essential for any SEO work |

## LEARN: Close the loop, update the playbook

| Vendor / Tool | Capability | Size Fit | DIY viable? | Notes |
| --- | --- | --- | --- | --- |
| Notion | Wiki, retrospective docs, knowledge base | S:● SMB:● E:◐ | Partially — AI can generate retro docs, but Notion's collaboration is the value | The solo/SMB knowledge home |
| Confluence (Atlassian) | Enterprise wiki + knowledge management | S:— SMB:◐ E:● | Partially — the tool is less important than the habit | Enterprise standard; Jira integration |
| Airtable | Structured knowledge + workflow tracking | S:◐ SMB:● E:◐ | Partially — a spreadsheet + AI can approximate | Flexible; sits between spreadsheet and database |

---

*This companion is deliberately seeded, not exhaustive. Add vendors as you encounter them in real engagements. The "DIY viable?" column is the most important one - it tells you when to build and when to buy.*
