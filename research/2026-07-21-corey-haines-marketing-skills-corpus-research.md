---
provenance:
  created: 2026-07-21
  for_project: agentic-marketing
  thread: Corey Haines marketing-skills corpus research + guest-video indexing
  source: authored in a separate video-research repo, mirrored here (see lineage note below)
---

# Corey Haines / Marketing Skills - corpus research and indexing (2026-07-21)

> Lineage: authored in the video-intel skill repo (that is where the corpus, search index, and scan/index tooling live), then mirrored here because agentic-marketing is the target practice repo for this material (see AWESOME-MARKETING-SKILLS.md). Other repos can query the video-intel search skill directly (it is globally installable and read-only), but in practice video research kicks off in video-intel and the note is mirrored to the true target with the provenance block above.

## What prompted this

Question from Daniel: run vector/hybrid search for Corey Haines (coreyhaines31/marketingskills), find which of my watched channels already cover his topics (one of them is "SEO Audit"), index three specific guest-appearance videos, and advise on whether to start slicing the corpus vertically by topic instead of only by channel (because Corey guests on other people's podcasts, so useful material lives on channels I do not follow wholesale).

The three URLs:
- https://www.youtube.com/watch?v=FaiQD5_q21c
- https://www.youtube.com/watch?v=YajqB9RDdzI
- https://www.youtube.com/watch?v=yjj1RedLMmc

## Finding 1: the corpus was already deep on Corey's themes, just unlabelled

A single hybrid query ("Corey Haines marketing skills", "SEO audit") pulled his ideas across six channels I already follow. The anchor is graceleungyl: she teaches the exact same construct Corey does (a "marketing skills library grouped by discipline" covering keyword research, blog writing, SEO audit, link building, plus a dedicated "SEO audit for AI search" video). Other coverage: simonscrapes explicitly name-drops "this Corey Haines copywriting skill from his marketing skill pack"; systemsmadebetter walks a Claude SEO plugin/skill; gregisenberg / ycombinator / iangarlic carry adjacent go-to-market material. Takeaway: "SEO audit" and "marketing skills" are not single-creator niches in the corpus, they are a cross-channel theme with graceleungyl as the strongest in-corpus companion to Corey.

## Finding 2: all three target videos are Corey guest appearances on different host channels

| Video | Host channel | Date | Length | Prior corpus status |
|---|---|---|---|---|
| FaiQD5_q21c "Does a Week of Marketing Work in an Afternoon" | TripleDart Digital (@tripledartdigital) | 2026-06-03 | 59:42 | not indexed |
| YajqB9RDdzI "Just give Claude these skills" (interview by Andrew Warner) | The Next New Thing (@TheNextNewThingAI) | 2026-02-11 | 30:22 | already indexed |
| yjj1RedLMmc "What Happens When You Give Claude 40 Marketing Skills" | Gerrid Smith (@iamgerrid) | 2026-06-17 | 41:03 | not indexed |

So only two needed indexing. YajqB9RDdzI was already in the corpus under thenextnewthingai (it had surfaced as the #2 hit for "SEO audit", where Corey demos the SEO-audit skill live).

## Recommendation: slice vertically, but do not build per-creator channels

The decision Daniel raised (channel-per-creator vs vertical/topic slicing) resolves cleanly in the existing architecture:

- A channel models a scannable FEED, not a person. A guest has no feed in the watchlist. A "coreyhaines" folder would misrepresent provenance (the video really lives on the host's channel) and you cannot `scan` a person anyway.
- The vertical/topic axis already exists, in three layers that cut across every channel folder: (1) hybrid search (proven here - one query retrieved Corey across six channels), (2) the concept/taxonomy layer (concepts.json per video rolled up into taxonomy.json - this IS the "common words across the corpus" Daniel asked about, currently 613 canonical concepts), and (3) the entity graph (scripts/intel_graph.py, issue #85) if we ever want "Corey Haines" as a first-class node with every co-occurrence.
- So: channels = provenance (horizontal). Concepts + search + entity graph = topic/person (vertical). Both axes already exist; adding per-creator folders would duplicate storage and fight the retrieval layer.

Guest videos therefore go under their HOST-channel folder for honest provenance; the person is found by querying, not by foldering.

## What was done (indexing + recovery)

- yjj1RedLMmc indexed into gerridsmith/ via the full pipeline: transcript (multimodal model) + mindmap-from-transcript + 12 concepts. Clean.
- FaiQD5_q21c indexed into tripledart/. First pass came back PARTIAL: the multimodal model truncated chunk 1 to 6 percent coverage (a "thin chunk", flagged by the pipeline as transcript_status: partial rather than crashing). Recovered via the sanctioned fallback: rebuilt the transcript from the YouTube caption track (`transcript --url ... --transcript-source yt-captions --force`, full 60-minute coverage, 1409 cues), then regenerated the mindmap and 16 concepts from the complete text.
- Registered both host channels in config.yaml as `enabled: false` (the documented non-scannable-source pattern, same as thenextnewthingai / earlyaidopters / kieranklaassen). This keeps them out of auto-scan forever (I never want TripleDart's or Gerrid's full marketing feed) while leaving them addressable for future one-offs, and it un-blocks the batch `concepts` command for those folders (that command iterates config channels; `index` and `taxonomy-build` instead walk the filesystem, so they pick up any folder).
- Mirrored config.yaml to G Drive (config.2026-07-21.yaml + config.latest.yaml).
- Rebuilt taxonomy (613 concepts from 1484 concept files) and the vector index (36,940 chunks). Verified all three videos are retrievable via hybrid search.

## Reusable workflow: indexing a guest appearance (the discipline going forward)

1. `python scripts/video_intel.py process --url "<url>" --channel <host>` - auto-routes to a host-channel folder (slugified from channel title even if the channel is not in config).
2. If the result is PARTIAL (thin multimodal-model chunk): `transcript --url "<url>" --channel <host> --transcript-source yt-captions --force`, then `mindmap --url ... --channel <host> --force`, then `concepts --channel <host> --force`.
3. Register the host in config.yaml as `enabled: false` so batch `concepts` can see it, then `taxonomy-build` and `index --force`. Mirror the config backup to G Drive.

Captions-first recovery beats a high-res retry for talking-head interviews: full coverage, near-free, and immune to the multimodal truncation. Trade-off: the captions transcript is speech-only (no on-screen SCREEN/OCR markers), which is an acceptable loss for a podcast-style interview.

## Follow-on

A curated top-down tutorial briefing ("marketingskills") was generated from the three Corey transcripts plus cross-creator context, held as a private companion to this note. It ranks Corey's actual skills most-to-least important with when/how-to-use notes and timestamped video deep-links, so the material is masterable without watching all three videos end to end. That briefing is the practical companion to this research note; apply it against the skills catalog in AWESOME-MARKETING-SKILLS.md.

## Top 5 skills to start with (from the marketingskills briefing)

Corey demos roughly 40 skills; this is where to start, ranked by value-for-effort for a practitioner:

1. Product Marketing (context) skill - the keystone, run it first. It captures positioning / ICP / messaging context that every other skill reads from; without it the rest produce generic output.
2. SEO Audit skill - Corey's own number-one to start with. Crawls every page for structure, metadata, schema, and internal linking and fixes them. Replaces what agencies charged thousands for.
3. Copywriting skill - the most universal and best-demoed. Rewrites any page or asset to a consistent voice; the clearest before/after in the talks.
4. Programmatic SEO skill - the highest-leverage ("a week of work in an afternoon"). Generates large sets of templated, ranking pages (for example integration / persona / location permutations).
5. Content Strategy + Keyword Research skill - the fuel for number 4. Finds the terms and plans the content that programmatic SEO then mass-produces.

Full ranked twelve with when/how notes and timestamped deep-links is in the private companion briefing.
