# Roadmap: candidate futures, and what would trigger each

The README says what this repository is. This file says what it might become, so the question "what should I do next here" has a written answer instead of a fresh debate. Each candidate carries a trigger: the observable condition under which it becomes the next move. Until the trigger fires, the candidate is parked on purpose, not forgotten.

## The direction that does not change

This repository teaches a method: eight verbs, seven commandments, a scored map of where agents help. The method is the durable part. Tool lists, vendor reviews and platform notes are perishable and live in [research/](research/README.md), dated. Any future that trades teaching for cataloguing is refused below.

## Candidates

| Candidate | What it would look like | Trigger | Status (2026-10-01) |
| --- | --- | --- | --- |
| **Split the method into a `method/` folder** | One page per verb, plus commandments, mapping and the scored table, each linkable and teachable on its own | The Anatomy no longer reads end to end in one sitting, or three or more validated tool reviews exist per verb and want a per-verb home | Parked. The Anatomy is 6,700 words and reads as one argument; splitting it now fragments the argument to gain links nobody has asked for |
| **One specimen skill in the repo** | A single real SKILL.md here as the reference implementation of an always-running SENSE skill: a report watcher that notices a monthly publication and notifies the operator, generic to any publisher | A second operating repo wants the same watcher, which proves it is general | Parked. Skills are built where they are used; the first candidate exists in production and is one month old |
| **Date-stamp and revalidate the scores** | Each section-3 table carries its assessment date; scores revisited yearly against what agents can do now | The first anniversary of the scores (April 2027), or a reader challenges a score with evidence | Open. Cheap; the next content pass should do it |
| **A second worked example at enterprise scale** | The README's solo-practice example paired with an anonymised enterprise one: same verbs, different instrumentation and governance | An engagement ends and its lessons can be written without identifying anyone | Parked until it can be written cleanly |
| **More tool reviews** | Reviews run on demand with the procedure, filed under research/ with their date | A reader or a project needs the verdict on a specific tool | On demand, never as a backlog. Reviewing tools nobody is choosing between is the trap this repo climbed out of |

## Refused

- **A documentation site.** Navigation is not the problem; a reader who cannot find the method in a README with one bold link will not find it behind a site either. A site adds build and upkeep without adding a sentence of method.
- **A complete catalogue of marketing AI tools.** The space changes faster than one person can review it, and completeness was never the value. The 20-minute procedure is the answer to "what about tool X."
- **Skills roadmaps without skills.** Removed in v2.2. The repo promises only what exists.

## How this file is used

Read it before proposing a restructure or a new top-level artifact. If a trigger has fired, the candidate moves into CHANGELOG as work; if a candidate is abandoned, it moves to Refused with the reason. Private planning that cannot be public (engagement specifics, positioning against named competitors) stays out of this repository entirely.
