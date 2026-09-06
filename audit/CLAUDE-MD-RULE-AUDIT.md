# CLAUDE.md rule audit — evidence for the correction PR

**Commissioned by the owner 5 September 2026. Produced by 27 agents over `eql-source@origin/main`
`CLAUDE.md` (947 lines, 10 sections) against the Director's ledger (22,461 lines, 379 rulings)
and the repository's full history.**

**THIS FILE IS EVIDENCE, NOT AN INSTRUCTION.** Session A makes the edits and opens the PR;
the owner merges. Nothing here is authority to delete a rule.

---

## Headline

    rules audited   191
    FORM            PRINCIPLE 94 · SITUATION 55 · FACT 42
    VERDICT         CAUGHT 142 · CANNOT-TELL 23 · NEVER-FIRED 13 · BOTH 8 · BLOCKED-ONLY 5

**10 of the 18 `NEVER-FIRED` / `BLOCKED-ONLY` verdicts were OVERTURNED when a second agent
was tasked with refuting them.** Acting on the survey alone would have deleted working rules.

> **INSTRUMENT LIMIT, reported by the audit against itself: the ledger is structurally blind to
> rules that fire inside a session's reasoning.** One rule was found firing only in a session
> transcript — no commit, no ruling, no trace in 176 refs. **So `NEVER-FIRED` here means
> "left no record", never "did nothing".**

---

## PART 1 — DO NOT DELETE THESE. Verdicts overturned on adversarial verification.

### `2-source-hierarchy` — CLAUDE.md L128-131 (origin/main, samusmylove47-maker/eql-source) — "**Exception, deliberate:** the survey plates carry no tier badges yet. They are in

    was:  BLOCKED-ONLY
    is:   ACTIVE — CATCHING. Do not delete. Escalate instead: the rule is in unresolved conflict with RULING R207 (HANDOFF.md:20426-20427, 1 Sep 2026, status `ruled`, unexecuted), which ordered "badges on, everywhere" against the exact 6-of-13 split still live on origin/main today. The Director must either execute R207 and retire L128-131, or re-rule R207 and keep it — but the choice must be made explicitly

REFUTED, on three independent grounds. I searched by consequence rather than by the rule's words: I looked for the ACTION the rule forbids (a badge added to a plate; a missing-badge defect filed) and for its outcome in commits, audit docs and the ledger.  === 0. INSTRUMENT FAULT — reported as an instrument fault, not as a finding === Two of the three searches the first agent cites cannot match anything. `git grep` defaults to BASIC regex, where `|` is a literal character. Measured in the repo just now:   git grep -in "ungraded|incomplete and ungraded|absence as a defect" origin/main   -> 0 lines   git grep -inE "ungraded|incomplete and ungraded|absence as a defect" origin/main  -> 21 lines The repository-wide negative is void: it is a dead grep, and a dead grep and an empty region are indistinguishable. (Their HANDOFF.md grep returns 0 with AND without -E, so that negative stands for tho

### `3-hard-rules` — CLAUDE.md L357-359 (origin/main, eql-source): "**New Sebilis / New Sebilisian Expedition content is out of scope** for the dungeon plates. The one exc

    was:  NEVER-FIRED (prohibition half; exception half live and shipping)
    is:   FIRED - once, and unrecorded. The prohibition half was applied on 8 Aug 2026 by a dungeon-plate geometry research session, which ruled `newsebexp.txt` (New Sebilis, 1,166 lines) out of scope and so declined the content of the only CC0-licensed map source in its survey. KEEP THE RULE. The firing lives only in the session transcript - it never reached HANDOFF.md, a commit message, or any of the 176 

REFUTED. I found one instance of the PROHIBITION half firing. It is outside the corpus the first agent searched, which is exactly why its five searches were sound and still missed it.  THE FIRING. On 8 Aug 2026 a research session was dispatched from the site repo (cwd `C:\Users\Lindsey\Desktop\EQL Source\eql-source`, branch `feat/plot-labels`) with a task that names the dungeon plates explicitly: "The project holds 181 recorded named-mob coordinates across ten dungeons ... but has no zone GEOMETRY", and lists them - Najena, Splitpaw, Crushbone, Befallen, Blackburrow, Lower Guk, Nagafen's Lair, The Hole, The Warrens, Castle Mistmoore. Hunting for legally usable geometry it reached `https://github.com/crande25/eql-maps`, the ONLY candidate it found under a fully permissive licence (CC0 1.0, README quoted verbatim in the report). Its assessment, verbatim:    "It ships one file (`newsebexp.t

### `4-file-map` — CLAUDE.md L374 (section 4, File map): `site.config.json    site name, tagline and URL. The ONLY place these live`

    was:  NEVER-FIRED
    is:   FIRING, PARTIALLY ENFORCED — fired for the URL, unenforced for the name. The rule fired materially at 0a8f46fb (8 Aug 2026), where the site URL moved from eqlsource.netlify.app to eqlsource.com and the only hand-edited file carrying the new value was site.config.json, with public/sitemap.xml and public/robots.txt following as generated output; it is enforced by a hard build stop at _build/sitemap.

REFUTED. The rule fired on the one real test it has ever faced, and it is backed by three live guards the original evidence missed or truncated.  THE FIRING. Commit 0a8f46fb (8 Aug 2026, "Publish only public/, so internal files cannot be deployed at all") changed the site URL from `https://eqlsource.netlify.app` to `https://eqlsource.com`. This is the only time in the repo's history any site identity value actually changed (`git log --all --follow -p -- site.config.json` returns exactly two commits touching values: ffc04d67 baseline, 0a8f46fb this change). Attributing every added line carrying the new URL in that commit (`git show 0a8f46fb --format='' -U0 | awk '/^\+\+\+ /{f=$2} /^\+.*eqlsource\.com/{c[f]++}'`) yields exactly three files: site.config.json (1 line), public/sitemap.xml (32), public/robots.txt (1). The latter two are generated — _build/sitemap.py:131 writes public/robots.tx

### `4-file-map` — CLAUDE.md L495 (verified at `git show "origin/main:CLAUDE.md" | sed -n '495p'`): `state/              automation memory. Do not hand-edit`

    was:  NEVER-FIRED
    is:   FIRED, AND OVERBROAD — do not delete. It fires as a decision rule at a fork, twice on the record: `a108c998` refused to hand-merge a conflicted `state/last-build.json` and rebuilt instead; `8f657711` declined to re-stamp `state/` to suppress a collateral failure. But it is true only of `state/last-build.json`. `state/watchlist.json` is hand-maintained by design (docs/AUTOMATION.md:117, docs/SOURCE

REFUTED. The first agent searched for a VIOLATION (someone caught hand-editing state/). This rule is a prohibition, so it fires mainly by CHANGING A DECISION, not by catching a culprit. I searched commit-message BODIES — `git log --all --format='%H%n%s%n%b%n===END===' | grep` — which no channel in the original evidence covered (the first agent used `git grep` over the origin/main TREE and `grep -F` over the ledger; neither reads commit bodies). Three firings:  FIRING 1 — commit `a108c998` ("The item side of sightings.py discarded a named mob's drop…"), body lines 56-62:   "REBASED ONTO main AFTER #191 MERGED. The conflicts were public/search.html and    state/last-build.json, both GENERATED. A generated file is never hand-merged: the    branch was reset onto the new main, only the three SOURCE files were carried    back - _build/sightings.py, _build/publicdata.py, docs/BACKLOG.md - and  

### `5-build-and-verify` — CLAUDE.md section 5, L551 and L568-572 (origin/main, samusmylove47-maker/eql-source) — the ban on extending `scripts/conformance.js` to judge type: "*

    was:  BLOCKED-ONLY — the ban has been cited to force work elsewhere (HANDOFF.md:13961-13963, R44, the hand-run CDP probe) but has never been found catching a defect; the opposite is on record at HANDOFF.md:
    is:   FIRED-AND-CAUGHT (by its substance), AND ALREADY OVERTAKEN — not BLOCKED-ONLY. Two corrections. (a) The ban's substance has a catch in the current tree: 32 Cinzel side-bearing findings correctly discarded as non-defects (`scripts/conformance.js:606-611`) and 10 desktop 16ch findings held as a typographic decision rather than fixed or tuned out (`docs/BACKLOG.md:118-123`) — though the ban is not in

REFUTED on two independent grounds, both found outside the first agent's search radius.  **METHOD CONTROL (run first, as required).** My method was: (1) scan every commit SUBJECT via `git log --all --oneline --format='%h %ad %s'` for the rule's CONSEQUENCE rather than its words; (2) `git grep` the whole `origin/main` tree — `docs/`, `scripts/` headers, eql-source's own `HANDOFF.md` — not just CLAUDE.md and the Director's ledger; (3) read `docs/BACKLOG.md` Acceptance notes, where findings are held open. Control target: the WCAG-AA contrast rule, already known to be CATCHING (HANDOFF.md:7449-7452). Step 1 surfaced `b0beb078` "Teach the sweep to read colour, and it found 124 things in daylight", whose body records the catch (masthead 1.06:1 on 699 pages, three tokens moved 4.24→4.51, 4.12→4.59, 4.10→4.56); step 2 surfaced CLAUDE.md:707 "WCAG AA on all text". The method finds a known firing.

### `5-build-and-verify` — CLAUDE.md L633-639 (origin/main, eql-source): "**A READ-ONLY INVESTIGATION MUST RUN A GENERATOR AS A SUBPROCESS, NEVER IMPORT IT.**… importing a modul

    was:  NEVER-FIRED
    is:   FIRED (prohibition arm), once, recorded — not NEVER-FIRED. Evidence: eql-source `a108c998` (2026-09-04), "MEASURED BEFORE CHANGING ANYTHING, by replicating the join rather than importing the generator", a read-only investigation of `_build/sightings.py` two and a half days after the rule entered §5 in `371a1cca`. The rule must NOT be deleted. Its affirmative half ("run it as a subprocess") has no 

REFUTED. One firing found, inside the very five-day window the original verdict examined.  THE FIRING. eql-source commit `a108c998`, 2026-09-04 11:09:36 -0400, "The item side of sightings.py discarded a named mob's drop because WE had not catalogued the item". Ancestor of origin/main (verified with `git merge-base --is-ancestor`; merged via PR #192, `9ff880fd`). Commit body, verbatim:    "MEASURED BEFORE CHANGING ANYTHING, by replicating the join rather than    importing the generator: of 5,360 discarded drops, 930 came from a mob our    own roster NAMES - 94 mobs, 265 distinct items…"  That is a read-only measurement phase, conducted on a generator (`_build/sightings.py`), where the agent names the prohibited operation and records having refused it. The rule entered §5 in `371a1cca` at 2026-09-01 22:55:46 -0400; the firing is 2 days 12 hours later.  IT IS NOT VACUOUS COMPLIANCE. `_build

### `6-design-system` — CLAUDE.md L667-669 (origin/main, verified by `git show "origin/main:CLAUDE.md" | sed -n '665,670p'`): "**Monochrome chrome, polychrome content.** The 

    was:  NEVER-FIRED (SITUATION) — "Applied constantly, enforced by nothing, and I found no defect it caught."
    is:   FIRED — LOAD-BEARING, NOT MECHANISED. Keep the rule. Four documented firings on origin/main, the strongest being docs/VISUAL.md:53-58 (commit 8caf32f7), where the accuracy objection is expressly declared inapplicable and this rule is what still refuses decorative AI header art. Narrow amendment warranted, to the enumeration only: drop or correct the accent count (DESIGN.md:93-94 and .claude/comman

REFUTED — and the refutation is sitting inside the original verdict's own evidence line.  **POSITIVE CONTROL (run first, method validated before any conclusion).** My method was NOT the first agent's. It was content pickaxe over all refs — `git log --all -S"<substring>"` — plus `git grep -n <phrase> origin/main` across the whole tree (`_build/`, `scripts/`, `.claude/`, `docs/`, `public/`), then `git merge-base --is-ancestor <c> origin/main` on every hit. Control: I ran that exact method against two rules in the SAME CLAUDE.md section that are already known to have fired. `-S"outline claim"` → 50085a8e (2026-09-01, "heading skips closed on all 717 pages, and the fix for them silently stripped type on seven"). `-S"No fourth typeface"` → 0af51267 (2026-08-20, "correct the faces count") and 31b546ea. Both known firings found. The method works. Applied to this rule, `-S"monochrome"` returns *

### `7-writing-voice` — CLAUDE.md (origin/main) line 728, section 7 "Writing voice": "Zone ZEM is the one sanctioned experience figure." — the closing sentence of the paragra

    was:  NEVER-FIRED. "Searched and found no instance either way… The exemption is plainly HONOURED… but it functions as a permission, not a constraint, so there is nothing for it to catch or block."
    is:   NOT NEVER-FIRED AS CHARACTERISED — DO NOT DELETE. Correct label: APPLIED-AT-ENACTMENT; CONSTRAINT ARM ARMED BUT NEVER TESTED, AND CURRENTLY UNENFORCED AGAINST A LIVE COUNTER-EXAMPLE. Three findings the Director should have: (1) the rule was applied to real page content in the commit that wrote it — 2d48b193 rewrote two ZEM sentences to keep the figure and drop the first-person framing, so "no inst

REFUTED IN ITS TWO LOAD-BEARING CLAIMS; the bare label "never fired since enactment" I could not overturn. Taking the three parts separately.  === 1. "Searched and found no instance either way" — REFUTED, by the enacting commit's own diff ===  The first agent searched the rule's words in commit MESSAGES and in the ledger. I searched the DIFFS. `git log --all -p -- _build/source _build/build1.py _build/build3.py assets/zones-index.json | grep -E "^COMMIT\||^-.*\bZEM\b"` shows that `2d48b193` (17 Aug 2026 13:42:47 -0400) — the same commit that WROTE section 7, including line 728 — edited ZEM sentences rather than leaving them alone:    _build/changelog.py   -  body="Survey 13, and the highest experience rate we have recorded &mdash; <strong>ZEM 139, "   +  body="Survey 13, and the highest ZEM on the site &mdash; <strong>139, "    _build/source/kedgekeep.html   -  <div class="cell"><dt>ZEM<

### `7-writing-voice` — CLAUDE.md L753-756 (section 7, writing voice): "**`public/data/*.vN.json` keeps its fields**, including sighting counts and session dates. It is a pub

    was:  NEVER-FIRED — "no instance either way, no catch, no block"; demonstrably honoured but never observed changing an outcome.
    is:   HONOURED AND LOAD-BEARING — not NEVER-FIRED. The rule has changed an outcome at least twice (2d48b193 on 17 Aug 2026, overriding the generic sweep's default on the four published files; a108c998 on 4 Sep 2026, determining that the fix take the form of an added optional field and confining a rename to the internal layer), and it carries live enforcement at scripts/check.py:1224-1231. It has never b

REFUTED IN WIDTH, NOT IN SUBSTANCE. I found no catch either — but I found two commits where the rule demonstrably changed what someone did, which "NEVER-FIRED" denies.  FIRING 1 — the rule overrode an active removal, 17 Aug 2026, commit 2d48b193 (peers/eql-source). This is the sweep itself, and its body records the override as a decision: "The published datasets keep their fields. public/data/*.vN.json is a contract and fields are never removed, so the descriptions are reworded and the shape is untouched; the counts are gone from every page a reader sees. DECIDED RATHER THAN TIDIED." The sweep's stated scope was removal of exactly these things — "GONE, EVERYWHERE: ... 'seen x73' tallies, play dates, session windows". It reached the files: `git show --stat 2d48b193 -- public/data` shows all six touched. The sightings diff changes ONLY the prose, and rewrites the description to advertise w

### `8-adding-things` — CLAUDE.md section 8b, origin/main lines 802-804 (confirmed at those exact lines by `git grep -n "a restyled archive" origin/main -- CLAUDE.md`): "**Do

    was:  NEVER-FIRED (with the qualifier "it has never fired because nobody has tested it, not because it is inert", and the claim that the 19-21 Aug site-wide restyles "passed the archive by without a check s
    is:   FIRED — and it CAUGHT something. First firing 10 Aug 2026 (`394267b3`, on origin/main), one day after the rule was written: an audit's proposal to split the archive to per-plate URLs and add a banner per plate was refused in the rule's own terms, and the accepted finding was rerouted into noindex plus a warning above the blocks, leaving `assets/archive-plates.json` untouched. Further invocations a

REFUTED. The rule fired on 10 August 2026 — one day after it was written — and the firing is recorded verbatim in a commit that is on origin/main.  THE FIRING. Commit `394267b3` "Second audit: the retraction now reaches the row" (Lindsey, 2026-08-10 21:25:18 -0400, on origin/main). Its commit message has a section headed **"ACCEPTED WITH A VARIATION"**, and item 8 is the archive, verbatim:    "8. The archive. Agreed it was the one page publishing unmarked data we       had already established was wrong, and that "kept verbatim" had been       allowed to override "marked on sight". It is noindex now and carries       a warning naming the six bad Najena coordinates. NOT split to       per-plate URLs and NOT banner-per-plate: the plates stay untouched,       which is what an archive is for. The warning sits above them."  This is the rule catching something. An audit found a real fault (the 

---

## PART 2 — STALE. Facts or reasons that are now false.

**Correct the fact. Do not delete the rule unless Part 1 or the owner says so.**

### Section `2-source-hierarchy`

**1. L56-57 (tier M): "Always publish trio, level, zone, difficulty label, date and sample size beside the figure."**

  *form:* `SITUATION`  ·  *verdict:* `CAUGHT`

Two of the six named nouns — date and sample size — are forbidden on reader-facing pages by §7 and by the generator that writes those pages. The rule states a publication standard the site deliberately no longer meets. The list-of-nouns form is what makes it fail: had it said 'a measured figure never appears without the conditions that bound it', §7's rewording of those conditions would not have broken it.

**2. L80-83: "Page carries `{{Classic Era}}` → its prose is import until proven otherwise. Nine of the ten surveyed zone pages carry it."**

  *form:* `SITUATION`  ·  *verdict:* `CAUGHT`

Three separate problems with 'Nine of the ten surveyed zone pages'. (1) The site surveys THIRTEEN zones, not ten: assets/zones-index.json holds 13 slugs and public/dungeons/ ships 13 survey pages. (2) assets/wiki-provenance.json — the dataset that exists to hold exactly this — still holds only ten zones; kedgekeep, planeoffear and planeofhate have no provenance row at all. (3) `git grep -in "Classic Era" origin/main` returns zero hits inside wiki-provenance.json, so the nine-of-ten count is recorded in no dataset and cannot be re-derived from the repository. It is a number typed beside data it claims to come from, which is the fault §3:344-347 names. Separately, the rule names ONE template string and the wiki has at least a second: docs/PLANES.md:24 records that Plane of Fear boss pages carry `{{Fear Era}}`, which this rule's vocabulary does not cover.

**3. L128-131: "**Exception, deliberate:** the survey plates carry no tier badges yet. They are incomplete and ungraded on purpose, pending a later phase that verifies and grades them in full. Do not add badges to them as part of other**

  *form:* `SITUATION`  ·  *verdict:* `BLOCKED-ONLY`

Its stated fact is false. Seven of the thirteen published surveys carry thirty tier badges between them, counted on origin/main: mistmoore 12 tM, planeoffear 1 t3 + 5 t5, planeofhate 1 t3 + 4 t5, kedgekeep 1 t3 + 3 t5, najena 3 t5, lowerguk 3 t5, nagafenslair 1 t5. Commits ff604ad5 and 2239ba99 added badges to surveys as part of other work, which the rule forbids. The term is stale too: §8b (CLAUDE.md:792) records that the plates were retired on 10 Aug 2026 and 'plate' now survives only as a numeric field. And the 'later phase' the exception is pending on has no date, no owner and no falsifier — the only open-ended deferral I found in the section.

**4. L134-137: "**Multiclass.** Characters run three classes at once. Two at creation, third at level 10, primary and race lock permanently at 11. The active trio uses the level of the *lowest* class in it."**

  *form:* `FACT`  ·  *verdict:* `CAUGHT`

THE CLEAREST STALE FACT IN THE SECTION. The site itself has published the opposite of this sentence since 31 August 2026. _build/build13.py:268-289 carries it as `status='open'` with legends='<strong>Not recorded.</strong> It is repeated widely, including in this project's own working notes, that the active trio uses the level of the lowest class in it. Nothing has been read that says so.' and evidence 'No source read'. The note names the failure: 'This sat inside the multiclass entry above until 31 August 2026, asserted at T1 and marked Settled on evidence that spoke only to the level-11 lock: three claims, one source, one badge.' Director rulings R65, R71, R99, R138, R144, R157 (HANDOFF.md:11861-11953) traced the claim to FIVE sites with 'a combined provenance of zero'. §2 is the sixth site and still asserts it flatly. The constitution now claims more than the site it governs is willing to claim.

**5. L198-211: "**The instance grammar has four shapes, not two.** Measured across 80 distinct zone strings… **The second shape is the trap**… `- Solo` does not occur at all — 0 of 68."**

  *form:* `FACT`  ·  *verdict:* `CAUGHT`

The paragraph carries two denominators for one corpus, thirteen lines apart. `git log -S "0 of 68" ... -- CLAUDE.md` returns 914c15b2 (22 Aug 2026); `git log -S "80 distinct" ... -- CLAUDE.md` returns f3dbe37c (27 Aug 2026), whose diff reads exactly `-Measured across 68 distinct` / `+Measured across 80 distinct`. The header was re-measured 68 to 80 and the `- Solo` sentence below it kept 68. The corpus grew; one of the two figures did not move. This is the fault §3:344-347 names — a number typed beside the data it claims to come from.

**6. L289-290: "And the Sky pages' 'D0, the only tier measured' is typed rather than read from the dataset. It is true today and it is the pattern §3 forbids."**

  *form:* `FACT`  ·  *verdict:* `CAUGHT`

The fact is now false. The sentence is derived in both generators and gated against re-typing, so 'is typed rather than read from the dataset. It is true today' no longer describes the repository. The clause is a known-gap entry that outlived its gap.

**7. L292-298: the difficulty name table — "| **D0** | Base / Normal — the default. The open world, and any instance run at base."**

  *form:* `FACT`  ·  *verdict:* `CAUGHT`

'Base / Normal' contradicts the same section's own prose 120 lines above, and the site was corrected away from it. 209fbb41 (1 Sep 2026): 'THE GAME'S NAME FOR BASE IS "NORMAL". "BASE" IS OURS… /learn/difficulty printed "D0 Base / Normal", putting our own inferred label beside the game's actual word as if they were alternatives. They are not… "Base / Normal" now appears nowhere on the site.' That commit then names this exact row: 'NOTE FOR THE OWNER, not acted on: CLAUDE.md's own summary table at line 281 carries "Base / Normal" too, while its prose twenty lines earlier is precise… the imprecision that reached the page is still in the file the next session reads first.' Verified today at CLAUDE.md:294, and `git grep -rn "Base / Normal" origin/main` returns that line and nothing else in the entire repository. The constitution is now the sole surviving carrier of a form it taught the site to remove.

### Section `3-hard-rules`

**8. L352-353: "**Never edit files in `dungeons/` or `tools/` directly.** They are generated. Edit the originals in `_build/source/` and run `./build.sh`."**

  *form:* `SITUATION`  ·  *verdict:* `CANNOT-TELL`

STALE, and the staleness has disarmed its enforcement. Neither `dungeons/` nor `tools/` has existed at the repository root since commit `0a8f46fb`, 8 Aug 2026, "Publish only public/, so internal files cannot be deployed at all". `git ls-tree --name-only origin/main dungeons/ tools/` returns empty; the directories are `public/dungeons/` and `public/tools/`. The baseline commit `ffc04d67` (7 Aug 2026) shows them at top level, so the move is one day after the repository's first day and nearly a month before today. CLAUDE.md contains ZERO instances of the string `public/dungeons`, while using `public/` correctly at lines 415, 431, 440 and 753 — the file was partly updated for the restructure and this line was not. `.claude/settings.json` still denies exactly `Edit(dungeons/**)` and `Edit(tools/**)`, paths that no longer exist, so on the plain reading of gitignore-style path patterns those two deny entries no longer match the generated pages they were written to protect. I state the path facts as measured; the consequence for pattern matching is inference from the pattern syntax, not some

**9. L354-355: "**Never push straight to `main` for content changes.** Branch, open a pull request, let the human merge. Merging is what publishes."**

  *form:* `PRINCIPLE`  ·  *verdict:* `CAUGHT`

The instruction is sound; the trailing REASON clause "Merging is what publishes" is false in at least one repository this constitution governs. R133, HANDOFF.md:11929 and narrative at 17952-17968: "`deploy.yml` fires `on: push: branches: [claude/eql-gear-optimizer-tfzvh6, main]`, one workflow, no others. Every push B makes goes to players; there is no staging step... The project's rule — 'the owner merges; merging publishes' — assumes merging is the gate, and in B's repo it is not." Session B flagged it rather than letting it be discovered. The ledger status is `pending`, marked the owner's decision, so this is an open governance question already on the record, not a new one. Scope note: the reason still holds for eql-source itself, where main is the deploy target; it fails wherever the rule travels, and CLAUDE.md is asserted to bind beyond this repository. The clause "let the human merge" is separately affected by commit `633215ba` — see the next rule.

**10. L356: "**Never merge your own pull request.**"**

  *form:* `PRINCIPLE`  ·  *verdict:* `BLOCKED-ONLY`

Stale in operative status rather than in a stated fact — the text asserts no fact and gives no reason, so it cannot be falsified the way L352's paths or L355's reason can, and I flag that so the Director is not misled by the boolean. What is false is that it binds: its enforcement was withdrawn at the owner's explicit instruction on 7 Aug 2026 while the sentence stands unchanged in the constitution, so a session reading CLAUDE.md alone will comply with a rule the owner set aside. It is also CONTESTED rather than settled: the Director was still issuing it verbatim as a standing order to Session B around 31 Aug 2026 (HANDOFF.md:10420, "Branch, PR, the owner merges. Never merge your own."), three weeks after the owner removed its enforcement. Note against R378, which lists this rule among the principles "fired dozens of times, right every time": I found no evidence of it firing correctly even once, and the only documented instance of it acting is the one where it blocked work. That disagreement is the sharpest thing in this section and I record it as a disagreement rather than resolving

### Section `4-file-map`

**11. L374: `site.config.json    site name, tagline and URL. The ONLY place these live`**

  *form:* `PRINCIPLE`  ·  *verdict:* `NEVER-FIRED`

The word ONLY is false as a description of the tree. The site name lives in site.config.json AND, as a typed literal, in 28 of the 60 files in _build/. This is the project's own signature fault — a value typed beside the data it claims to come from — inside the rule that forbids it.

**12. L392: `site.css          the entire design system, one file`**

  *form:* `FACT`  ·  *verdict:* `CANNOT-TELL`

'The entire design system, one file' is true of the generated chrome and false of the shipped tree. 673 pages carry a duplicated inline sheet whose rules are in no stylesheet, and a second stylesheet (fonts.css) exists. The claim was already contradicted when R22/F12 was ruled and the gap has widened since.

**13. L385-386: `app/    GENERATED — the Sky Ledger's browser build, served under a content hash. Written by _build/skyledger.py`**

  *form:* `FACT`  ·  *verdict:* `CANNOT-TELL`

The map describes public/app/ as holding one app from one generator. It holds two, from two generators, and the second generator (_build/lockouts.py) is absent from the map entirely. A reader following this entry would not know the Lockouts bundle exists or what writes it.

**14. The map as a whole (L372-496) presents itself as the file map of the repository.**

  *form:* `FACT`  ·  *verdict:* `CANNOT-TELL`

Not wrong, but no longer a map: it covers roughly a quarter of _build/ and a fifth of docs/. Two paths that matter are missing rather than merely omitted — _build/lockouts.py (writes one of the two served apps) and wrangler.jsonc (the host). Separately, the map's own root is inconsistent: index.html, assets/, tools/ and archive/ are written without the public/ prefix while three entries inside the same block spell out public/assets/og/, public/app/ and public/data/.

**15. A second copy of this file map exists at README.md:60-108 and has drifted from it.**

  *form:* `FACT`  ·  *verdict:* `CANNOT-TELL`

The duplicate advertises a withdrawn tool as live. This is the exact failure the Director's own CLAUDE.md names when it says a pointer 'will never be a copy. A copy goes stale.'

**16. L495: `state/              automation memory. Do not hand-edit`**

  *form:* `PRINCIPLE`  ·  *verdict:* `NEVER-FIRED`

'automation memory' understates what state/ holds. `git ls-tree origin/main state/` = last-build.json, last-check.json, watchlist.json. Only watchlist.json is automation memory; last-build.json is the build fingerprint that check.py:679-721 depends on, is TRACKED (the fact on which ruling R113 turned, Director HANDOFF.md:11909), and is the file whose absence now fails the build. The map gives no hint of that.

### Section `5-build-and-verify`

**17. L544-549: "Hand-run and not part of `build.sh` — it takes about four minutes… It loads every built page over `file://` at 1440x900 and 390x844 and reports console errors, `scrollWidth` against `innerWidth`, and an empty body."**

  *form:* `FACT`  ·  *verdict:* `CANNOT-TELL`

The three-item report list omits the two grounds and both the contrast and clip findings — i.e. it omits the two things the sweep has most recently caught. HANDOFF.md:8207 already states the operative rule the section does not: "`conformance.js` must run at both viewports in both themes".

**18. L551, L568-572: the ban on extending `conformance.js` to judge type — "**THE REASON THIS TOOL WAS BANNED FROM JUDGING TYPE NO LONGER HOLDS**… It may still be the right rule… Ask before extending it; do not treat the old sentence a**

  *form:* `SITUATION`  ·  *verdict:* `BLOCKED-ONLY`

The section already declares this rule's reason dead, so the staleness is self-documented rather than hidden. What is NOT documented, and is the sharpest thing I found: THE DEAD REASON IS STILL LIVE IN THE SCRIPT. `scripts/conformance.js` lines 34-36 on origin/main still read "It makes NO typography or aesthetic judgement, and it must not be extended to make one. Every page links three Google-hosted faces, this script aborts every non-file: request, and the fonts therefore render as system fallbacks". Commit cb82331b corrected the script's runtime OUTPUT (two console.log lines) and left the header untouched; it corrected "all four places" and this was a fifth. §5 line 574 sends the reader to that same header for the two traps. So the section says "nobody should cite the fallback fonts" while the file it points at still does — the propagation fault gate.py exists to catch, in the instrument §5 governs. Separately, commit 87af07eb (4 Sep 2026, three days after "Ask before extending it") extended the sweep to measure content against its own box — "item names painting over the column bes

**19. L553-554: "…so the three Google-hosted faces fall back" (the section's restatement of the superseded reason).**

  *form:* `FACT`  ·  *verdict:* `CANNOT-TELL`

Defensible as a faithful quotation of what the retired sentence literally said — the pre-cb82331b §5 text did read "the three Google-hosted faces" — but nothing marks it as a quotation of a figure that was itself already wrong, and §6 records that the three-to-four correction landed on 20 Aug, ten days before the self-hosting. Same class as the known Plane of Sky example.

**20. L591-596: "`scripts/gate.py` is the propagation gate, run by `check.py`… It refuses a build where a count disagrees with the data it came from, a withheld coordinate reaches a table, a page metadata asserts a figure the body hedge**

  *form:* `SITUATION`  ·  *verdict:* `CAUGHT`

No listed item is false; the enumeration has been outgrown by a large factor. gate.py on origin/main is 1,204 lines with 41 `fail(` calls, and gate_selftest.py carries 43+ mutation cases against the six it started with. The original sixth condition — "a verification count disagrees with the ledger, in either direction", still a live self-test case at gate_selftest.py:277 — is not among the five named here. A reader takes this list for the gate's scope.

**21. L600-602: "`check.py` also verifies that every internal link resolves, every page has the site chrome and a favicon, `zones-index.json` matches the files on disk, no page has lost its stylesheet, and **no page claims more verified**

  *form:* `SITUATION`  ·  *verdict:* `CAUGHT`

"plates" is the retired noun. Commit 0d55a2ec (9 Aug 2026) is titled "Retire the plates. The guides are Dungeon surveys now", and commit 4f885884 states it flatly: "The plates became surveys on 10 August." That same commit is the precedent for why this matters — a check in check.py went DEAD because its regex read "(\w+) of the ten plates have not cleared" against a page that had said "of the 13 surveys" for eight days: "It matched nothing." A stale noun killed a check once already. Narrow the claim honestly: the field name `plate` survives in zones-index.json as an ordinal 1-13, so the word is not wholly retired; it is the page-and-artefact sense that is.

**22. L612-619: "**This repo requires Python 3.12 or newer.** On 3.11 `build.sh` dies with `SyntaxError: unterminated string literal` in `_build/build24.py`… `build17.py` and `build24.py` both nest same-type quotes inside f-string repla**

  *form:* `FACT`  ·  *verdict:* `CAUGHT`

TWO NARROW FAULTS, neither of which touches the conclusion. (1) THE STATED MECHANISM IS WRONG FOR ONE OF THE TWO NAMED FILES. build17.py:479 does nest same-type quotes — an `f'…'` opened inside a replacement field of an outer `f'…'`. build24.py does not: the construct at :129-132 is a replacement field SPANNING THREE LINES inside a single-quoted f-string, a different PEP 701 grant, and that is precisely why the recorded error is "unterminated string literal" at build24.py:130 rather than a quote-nesting error. (2) "fifty-two" does not reproduce under either count I could construct: build.sh invokes 42 distinct generators today, and _build/ holds 59 .py files. HANDOFF.md:9041 records "2 of 52" as measured on 18 Aug 2026, so the denominator has moved rather than being wrong when written.

### Section `6-design-system`

**23. L692-699: "`scripts/headstyle.js` is the instrument ... It aborts remote requests exactly as `conformance.js` does — which since 30 Aug 2026 means it aborts nothing, because the faces are local — it is still sound, because **it on**

  *form:* `SITUATION`  ·  *verdict:* `CAUGHT`

THREE FALSE PREMISES IN ONE BULLET, and the project already flagged two of them. (1) "It aborts remote requests exactly as conformance.js does" IS FALSE. I swept all 168 lines of scripts/headstyle.js for abort/Fetch.enable/requestPaused/continueRequest: there is NO request interception anywhere. The only occurrences of "abort" are in the header narrating that this claim was wrong. Commit cb82331b (Tue Sep 1 2026) says so in terms: "Two of the four were mine ... CLAUDE.md section 6 and scripts/headstyle.js, both of which said headstyle 'aborts the webfonts exactly as conformance.js does'. It never did." headstyle.js's header was corrected; §6 was only half-corrected — the clause "which since 30 Aug 2026 means it aborts nothing" was appended while the false premise was left standing. (2) "equally-handicapped builds" IS THE SUPERSEDED REASON. headstyle.js:37 states flatly "So there was never a handicap to cancel", and headstyle.js:40-45 gives the reason that actually applies: "what it is FOR is proving a change moved nothing. A threshold or a target value would make it a style opinion, 

**24. L701-705: "**The plate cards** are the home page's signature: one card per zone, washed with its own accent, carrying its plate number cropped by the card edge. They reflow, so adding a zone needs no layout change. A fixed-column **

  *form:* `SITUATION`  ·  *verdict:* `CAUGHT`

THE DESCRIPTION OMITS THE FLOOR PLAN, WHICH IS THE PART DESIGN.md CALLS THE SIGNATURE. DESIGN.md:96-98 reads "**The plate cards** — one per zone, accent-washed, plate number cropped by the card edge, and **the zone's own floor plan drawn from the game's mesh**. This is the site's signature and the visual language the rest of the page extends." §6 lists the accent wash and the cropped number and stops. Measured: public/index.html ships 13 `plate-art` elements and 16 `<svg>`, and assets/zone-geometry.json holds 13 zones — the floor plans are there and are the dominant visual content of each card. THE LEDGER ALREADY FOUND THIS AND NAMED IT AS THE SAME REPEATING FAULT (HANDOFF.md:12924-12930): "**`CLAUDE.md` §6 IS STALE, AND IT IS THE FILE A SESSION READS FIRST.** It describes the plate cards — accent wash, cropped number — **and never mentions the floor plan** ... A session reading only `CLAUDE.md` would not learn the SVGs are identity at all. **This is the same failure that file already records about itself** over three typefaces versus four ... **Second confirmed instance of the same 

### Section `7-writing-voice`

**25. L724-726: "Nothing is tied to a character. No kill counts, swing counts, hit rates, \"seen x12\" tallies, session windows, play dates, hours farmed, attacker counts, or damage shares."**

  *form:* `SITUATION`  ·  *verdict:* `BOTH`

"Nothing is tied to a character" is superseded in part. R376 (HANDOFF.md:12172, committed 6d02212, 2026-09-05 — today) records the owner ruling: "It's fine for my character's name to appear in B's example, and for Shara's name to appear as an example, or in screenshots." §7 has not moved: `diff` of the §7 block at 2d48b193 against origin/main is IDENTICAL, and CLAUDE.md was last touched 2026-09-02 (428001a9). The file is one owner ruling behind. The counts half of the clause (kill counts, session windows, play dates) was NOT cleared and R376 says so explicitly — "section 7 forbids in a clause DISTINCT from the name clause" — so only the character-name half is stale.

**26. L726-728: "**No experience per kill at all** — experience is a function of the reader's level, so a figure measured at 26 tells a stranger at 35 nothing true."**

  *form:* `PRINCIPLE`  ·  *verdict:* `CAUGHT`

The words "at all" are now false as an absolute. HANDOFF.md:3427-3428 (ruling of 30 Aug 2026) splits published from computed: "**Computed** — different for every reader, derived from their own input, never stored and never transmitted | **§7 does not apply.**" A reader's own experience figure, computed in a tool from their own log, is expressly outside the rule. The file still says "at all" and carries no trace of the carve-out. The REASON is not stale — the ruling was derived FROM it — only the absoluteness is.

**27. L738: "Three exemptions, all deliberate:"**

  *form:* `FACT`  ·  *verdict:* `CANNOT-TELL`

"Three" against four rendered bullets (CLAUDE.md:740, 742, 746, 753). Exactly the ten-islands shape, in a section whose own subject is figures typed beside the thing they count.

**28. L740-741: "**Sample inputs on tools** may show a character name, because a reader needs to see the shape of what to type."**

  *form:* `SITUATION`  ·  *verdict:* `CAUGHT`

The exemption in the file is narrower than the exemptions in force, in two directions the file does not record. (a) HANDOFF.md:3449-3456, ruled 30 Aug 2026: "**Sample *output* gets the same narrow exemption and no more**: it must be plainly marked as a sample, and it must not carry measured figures from our own characters." §7 still says inputs only. (b) R376 (HANDOFF.md:12172, 2026-09-05) extends the clearance to screenshots. Neither reached the file; §7 is byte-identical to 2026-08-17.

**29. L742-745: "**`credits.html` names the site's own characters, once.** ... It is the only page that does, and a future sweep should not read it as a violation."**

  *form:* `SITUATION`  ·  *verdict:* `BOTH`

Stale twice over. (1) Superseded by R376 above, and §7 is unchanged since 2026-08-17. (2) FALSE AS WRITTEN against the tree, and this is the finding I would most want checked before anyone acts on it. `public/app/eqls-lockouts.514e9ebb.html` — 318,529 bytes, linked from the HOME PAGE at `public/index.html:329` and from `public/tools/lockouts.html:115` — carries the site's own character names in source comments (Shara ×13, Avenrae ×16), together with kill counts ("18 roster boss kills, 3 task grants, 3 tokens", lines 1141-1142, 3202), play dates and clock times ("[Mon Aug 10 17:14:49 2026]", line 1754; "04 Aug 12.2% 11 Aug 35.7% 18 Aug 27.1%", line 2722), and account playtime ("approximately 0 years, 12 days", line 641). Every one of those is a noun L724-725 names. WHETHER §7 REACHES IT IS GENUINELY UNSETTLED BY THE PROJECT'S OWN TWO PRECEDENTS, TWO DAYS APART: commit 209fbb41 (1 Sep) holds that names "appear ONLY inside CSS comments and reach no reader"; commit 7c2567c4 (3 Sep) treats grepping a shipped bundle as the leak test and holds work on the result. Commit 737700f9 adds a thir

### Section `8-adding-things`

**30. L772: "`check.py` fails if the home page stops linking a zone."**

  *form:* `FACT`  ·  *verdict:* `CANNOT-TELL`

STALE SINCE 2026-08-08, and the drift is traceable to the hour. `ebd2f3c8` (2026-08-08, "Withdraw the spectrum; extend the plate language across the page") added BOTH this CLAUDE.md sentence and a matching check on `index.html`. `ab20fc1e` (2026-08-08, "Make the home page an actual home page") moved the check to `dungeons/index.html`, rewrote the failure message, and added the comment explaining why the home page must NOT carry it — and its `--stat` shows five files changed (build1.py, changelog.py, site.css, index.html, check.py) with CLAUDE.md untouched. The sentence has stated a non-existent guarantee for four weeks.

**31. L774-779: "**A new raid encounter.** There is no template any more, and that is deliberate. `_build/build4.py` held a self-contained 3D engine and rendered the Eye of Veeshan; both were withdrawn on 17 August 2026 because the tact**

  *form:* `FACT`  ·  *verdict:* `CAUGHT`

THE DATE IS CONTRADICTED BY THE PROJECT'S OWN RECORDS. `_build/build4.py` was deleted by `ac6f3c7f`, authored AND committed 2026-08-16 19:07:29 -0400 (`git log --diff-filter=D -- _build/build4.py` returns that one commit); its first merge onto the ancestry path to main is `f1282f89`, 2026-08-16 19:24:32 -0400. Both are 16 August in local time and in UTC. build.sh's own doctrine is that "merging to main is what publishes". The ledger agrees with the history at HANDOFF.md:8465 — "The 3D engine and the only encounter guide were deleted on **16 August**" — while asserting the other date at HANDOFF.md:12276 — "the withdrawal was 17 August". `_build/changelog.py:37` dates the published entry 17 Aug 2026. So the project holds both dates and CLAUDE.md carries the one its own git history contradicts. Note also that the 17 August text was WRITTEN by the 16 August commit, i.e. dated a day forward at the moment of writing.

**32. L784-785: "Measured figures — damage to kill, attacker counts, what a boss cast — belong on the zone page, where they already are."**

  *form:* `SITUATION`  ·  *verdict:* `CANNOT-TELL`

The trailing clause "where they already are" is now false for one of the three named figure kinds. Attacker counts reach no page under public/dungeons/. A defensible reading rescues part of it — the Plane of Sky has no dungeons/ page (it is absent from zones-index.json) and `public/raids/plane-of-sky.html` IS its zone page, and `ac6f3c7f`'s own commit body says the measured half "already lives on the Sky page" — but that reading does not cover The Hole, whose D4 figures live only on learn/ and sources.html. Damage-to-kill and boss-cast figures (spell names appear on public/dungeons/planeofhate.html) do satisfy the claim.

**33. L787-788: "**A correction.** Update the change log on `sources.html`, typed as Addition / Correction / Source refresh."**

  *form:* `SITUATION`  ·  *verdict:* `CAUGHT`

THE LOCATION IS WRONG. `public/sources.html` is a generated file — `_build/build2.py:517` writes it, reading `ENTRIES` from `_build/changelog.py` (`build2.py:99`). `_build/changelog.py:1` says so: "The change log, in one place. sources.html renders all of it." A contributor who follows this line literally edits a build output that the next `./build.sh` overwrites. The correct target is `_build/changelog.py`. The instruction predates the split: `git log -S "Update the change log on" origin/main -- CLAUDE.md` returns only `ffc04d67` (2026-08-07, the baseline), while changelog.py was created by `ab20fc1e` (2026-08-08). The same error is in `.claude/commands/newzone.md:20` ("Add a Change log row to `sources.html`"). The typed taxonomy itself is exactly current and not stale.

### Section `9-known-gaps`

**34. L822-825: "Every raid-boss fight in every log we hold is a public pick-up raid of 5-7 players, and our own characters dealt 13-44% of the damage. 'Killed by one trio' was never true of any of them."**

  *form:* `FACT`  ·  *verdict:* `CAUGHT`

The numbers were exactly true the day they were written and are false now. Re-run against the 11 Aug dataset (git show 3d9f4810:assets/raids-measured.json): 14 fights, attackers 5-7 with no exceptions, share 13.5%-44.0% with no exceptions. The corpus has since grown 14 -> 213 and the ranges no longer hold. This is the section's own signature fault - a sentence typed beside a figure - committed in the paragraph that exists to forbid it. It has propagated: public/sources.html publishes the hand-typed "Every raid-boss fight on record here is a public pick-up raid, not a trio" in the 11 Aug FIX entry, which a reader meets as a current statement.

**35. L825-826: "`raidstats.py` now records `attackers` and `our_damage_share_pct` per fight so no page can restate it wrongly."**

  *form:* `FACT`  ·  *verdict:* `CAUGHT`

The stated REASON is false. The fields do not stop a page restating it wrongly, because the restatement is hand-authored prose, not generated: public/sources.html carries "Every raid-boss fight on record here is a public pick-up raid, not a trio" as typed text that no build step reads those fields to produce. Recording a field guards generated figures only; it has no reach into prose beside them - which is the fault this same item was opened to fix.

**36. L871-873: the supplied re-derivation command - `python3 -c "import json,collections;f=json.load(open('assets/raids-measured.json',...));f=f.get('fights',f);..."`**

  *form:* `SITUATION`  ·  *verdict:* `BLOCKED-ONLY`

It defends against a data shape the file has never had, and crashes on the shape it does have. A session told to "re-derive rather than trusting the table" and handed this gets a traceback, and the likely recovery is to trust the table.

**37. L875-883: "The plane-boss half closed 14 Aug 2026." Cazic-Thule killed at D2, D3 and D4 and Innoruuk at D3 and D4, along with ten of Innoruuk's court; Cazic-Thule heals itself sixteen times at D2; Innoruuk mixes three class kits.**

  *form:* `FACT`  ·  *verdict:* `CAUGHT`

Two enumerations have gone narrow. (i) The corpus now also holds Cazic-Thule at D0 (17 Aug 2026, The Plane of Fear - Group) and one Cazic-Thule fight whose tier is unresolved (19 Aug), and Innoruuk at D1 - so "killed at D2, D3 and D4" and "at D3 and D4" now understate the record. (ii) "ten of Innoruuk's court": assets/raids-measured.json holds ELEVEN distinct non-Innoruuk bosses in Plane of Hate zones, and held eleven on 14 Aug too, so the figure was never derived. The same "ten of his court" is typed a second time into zones-index.json's planeofhate `verify_gate`. CAVEAT, stated because I cannot close it: I cannot rule out that one of the eleven (Ashenbone Broodmaster) is deliberately excluded from "court". What is certain is that the number is hand-typed in two places with nothing to check it against.

**38. L886-890: Phinigel Autropos "ran three at once" - backstab, druid and wizard - and "Innoruuk's three are all spell lists; this is the first record where one of the three is melee".**

  *form:* `FACT`  ·  *verdict:* `CAUGHT`

Mistress of Scorn on 12 Aug 2026 backstabs while casting three spells, six days before Phinigel. Commit 67afde67 (4 Sep 2026) closed this in the code and in the generated page but did not touch CLAUDE.md, addressing the correction to the Director instead. The constitution is one day behind its own repository.

**39. L890-894: "`melee_verbs` is parsed into `assets/raids-measured.json` and rendered by no page, and the boss table on `learn/difficulty.html` has a Spells column and no melee column - so every backstabbing raid boss in the corpus re**

  *form:* `SITUATION`  ·  *verdict:* `CAUGHT`

Stale as of 4 Sep 2026, by one day. This is the sharpest instance in the section: a gap that closed, whose closing commit says in its own message that CLAUDE.md still names it, and which the constitution therefore still lists as open. A cold session reading L891 would be told the opposite of what the built page does.

**40. L899-903: "A single client under-witnesses a large raid, and the attacker count is how you tell" - Master Yael at D1, six attackers both times, 1.1x apart; where one client saw two attackers and the other twelve, the same boss at **

  *form:* `SITUATION`  ·  *verdict:* `CAUGHT`

The 2-attacker Terror D3 record no longer exists: merge() has since combined Avenrae's thin view with Shara's into an 11-attacker record of 160,850. The nearest surviving pair for that boss and tier is 3 vs 12 at 48.8x, and the widest same-boss-same-tier ratio in the corpus is now Dread at D3, 1 vs 12, 346x. The same 60x figure is typed a second time into _build/raidstats.py:675, so both copies went stale together - a figure typed beside data, duplicated, in the section that forbids exactly that.

**41. L914-915: "What it cannot do is say which measured body is which island... Ten `/loc` readings, one per island, label the chart permanently."**

  *form:* `SITUATION`  ·  *verdict:* `CAUGHT`

Two faults. (i) The count: nine islands, not ten - and it was nine on the day the sentence was written. `git log -S` puts "Ten `/loc`" into CLAUDE.md at 67e17fa7 (10 Aug 2026), and build8.py's RING held nine entries in that same commit. Checked RING at five commits from 10 Aug to 4 Sep: nine every time. A likely source of the ten: `assets/sky.json['islands']` has ten keys, but one is the sentinel `"any"` / "Zone-wide" / "wind runes, any mob" - counting it naively gives ten. That last step is inference; the nine is measured. (ii) The tense: the file says the readings "label the chart permanently" as though done. They are not - assets/sky-islands.json carries no label field on any of the 21 bodies, and the page says such readings "WOULD label this chart permanently".

**42. L919-920: "Five Sky class tooltips - Ranger, Rogue, Shadow Knight, Shaman, Wizard reward stat blocks unconfirmed for Legends. Turn-ins are current."**

  *form:* `SITUATION`  ·  *verdict:* `CAUGHT`

docs/SWEEP-2026-08-17.md items 92 and 93 found this on 17 Aug 2026 - "Eleven classes fail, not five" - and both items are still marked `unverified` in that file. The fix reached neither the site (public/sources.html:129 still names the five) nor the constitution. I derived the eleven independently from assets/sky.json rather than accepting the sweep's word.

**43. L921-922: "Respawn ceilings - the 28 July patch lowered maximums without publishing figures. Affected surveys state pre-patch timers as ceilings."**

  *form:* `SITUATION`  ·  *verdict:* `CAUGHT`

The stated reason names one patch and there are now two. _build/changelog.py:28 records the 18 August 2026 Daybreak notes fixing high-level named in Kedge Keep taking "an excessively long time to respawn", and says in place: "No figure was published this time either, so the ceiling stands and NOW HAS A SECOND REASON TO BE WRONG." The rule still fires correctly; its stated cause is a month out of date.

**44. L926-930: "not every zone has cleared them... `verify_level` in `assets/zones-index.json` is the only answer, and `verify_gate` carries either the evidence for a cleared zone or the name of the gate still open."**

  *form:* `PRINCIPLE`  ·  *verdict:* `CAUGHT`

The `verify_gate` half is false as stated. Only 9 of 13 zones carry a verify_gate at all; four zones at verify_level "full" - najena, splitpaw, lowerguk, nagafenslair - have verify_gate null, so it does NOT carry "the evidence for a cleared zone". And for the three open zones it carries a prose explanation of why a gate cannot be attempted rather than "the name of the gate still open".

**45. L933: "A zone marked `none` has had no gate attempted, not a gate failed."**

  *form:* `FACT`  ·  *verdict:* `CANNOT-TELL`

False for all three zones it describes. `none` means gate 3 is unattemptable for want of recorded named coordinates (planeoffear, planeofhate) or that zone coverage is thin (kedgekeep) - not that no gate was attempted. A cold session reading this would under-rate work already done and recorded, which is the same shape as the error this very item retracted on 18 Aug 2026.

### Section `10-when-unsure`

**46. Line 946: "usually one screenshot, one log line, or one `/loc`" — the enumeration of what a resolver typically is.**

  *form:* `SITUATION`  ·  *verdict:* `CAUGHT`

The word "usually" is a factual claim about which evidence typically closes a gap, and it has not been revised since the file was received. Of roughly nine named resolvers I could find — three shipped `what_would_settle_it` values, three shipped falsifiers, and the six ledger lines cited above — one names a screenshot; I found none naming one log line, and none naming one `/loc`. That is a grep sample, not a census, and one clean firing of "one screenshot" survives inside it, so I report "usually" as weakened rather than disproven. Two further pressures on `/loc` specifically: `logstats.py:174-302` has no capture for `/loc` (HANDOFF.md:8411), so a `/loc` cannot enter the measured pipeline on its own; and commit f3dbe37c (27 Aug 2026) "Stop publishing withheld coordinates" sits alongside CLAUDE.md:594, which makes "a withheld coordinate reaches a table" a gate failure. The site has also moved off the surface the list was written for — 0d55a2ec "Retire the plates. The guides are Dungeon surveys now.", b44070f2 "Add the 50 Upgrades tool page", 31f2227c "Publish the overlay". ONE THING I

---

## PART 3 — Method, so this can be repeated or refuted

### `1-standing-agreement`

**Method.** All paths absolute. Constitution read via `cd C:/Users/Lindsey/Desktop/EQLS Director/peers/eql-source && export MSYS_NO_PATHCONV=1 MSYS2_ARG_CONV_EXCL='*' && git show "origin/main:CLAUDE.md" | cat -n` — section 1 runs lines 29-45, the `---` at 46, blank at 47. Confirmed the file exists in the tree with `git ls-tree origin/main --name-only` before trusting any git show result.  LEDGER (C:/Users/Lindsey/Desktop/EQLS Director/HANDOFF.md, 22,461 lines, 379 rows matching `^| R[0-9]`): case-insensitive `grep -in` for 2-4 distinct stems per rule, deliberately including paraphrase stems as well as verbatim ones. Terms run: "traceable", "named source", "source with a date", "with a date", "undated", 

**Control.** CONTROL PASSED, and it exposed a fault in the naive method that would have produced a false NEVER-FIRED.  Control rule: rule 7, "every gap stated rather than smoothed over" — known firing at HANDOFF.md:9354. Exact method re-run: `grep -in "smooth" HANDOFF.md` returns 5182, 9354, 12103. It found the known firing, and it found it as a PARAPHRASE ("a gap is named rather than smoothed"), not a quotation. So the method tolerates paraphrase.  SENSITIVITY FAULT, and this is the part the Director should have: `grep -inc "traceable" HANDOFF.md` returns 0. Zero. Yet rule 6 ("every claim traceable to a named source with a date") demonstrably fires twice — HANDOFF.md:6171 and HANDOFF.md:14649 — under th

**Unmeasured.** WHAT I COULD NOT ESTABLISH.  1. No NEVER-FIRED verdict is offered, and no absence is claimed anywhere in this report. Every rule in lines 29-47 was found firing. I did not search the six peer sessions' own repositories or transcripts, only HANDOFF.md and origin/main of eql-source, so a rule could have fired in places I never looked — that would only add firings, never subtract them.  2. I cannot measure silent compliance. A rule that works by being obeyed leaves no ledger row. HANDOFF.md:13260-1

### `2-source-hierarchy`

**Method.** All searches run in C:/Users/Lindsey/Desktop/EQLS Director/peers/eql-source with MSYS_NO_PATHCONV=1 and MSYS2_ARG_CONV_EXCL='*' exported, plus the Director ledger at C:/Users/Lindsey/Desktop/EQLS Director/HANDOFF.md.  SECTION READ IN FULL: `git show "origin/main:CLAUDE.md" | sed -n '48,330p'` (947-line file; §2 spans 48-330, confirmed by `git show "origin/main:CLAUDE.md" | grep -n "^## "` which gives §2 at 48 and §3 at 331).  THREE SEARCH CHANNELS, run per rule with its distinctive phrase: (A) history — `git log origin/main --oneline -i --grep="<term>"` over 510 commits; and `git log -S "<literal>" --oneline --date=short --format="%h %ad %s" origin/main -- CLAUDE.md` to date individual sente

**Control.** CONTROL RULE: "The provenance test — apply before trusting any eqlwiki page as tier 2" (CLAUDE.md:65-90). Chosen because commit da74c6c2 states its own firing in words I did not write: "Found by applying the provenance test added to CLAUDE.md this morning, against the site's own flagship guide" and "This is the second time in one day that the provenance test has caught a live inaccuracy. It was worth adding."  CONTROL RUN, all three channels, verbatim: (A) `git log origin/main --oneline -i --grep="provenance test"` → 6 commits, including da74c6c2 "The Eye of Veeshan's stat block was classic EverQuest data". FOUND. (B) `git grep -in "provenance test" origin/main` → 25 hits: CLAUDE.md:63, CLAU

**Unmeasured.** SIX THINGS I COULD NOT ESTABLISH.  1. ANYTHING ABOUT LIVE EQLWIKI. The provenance test's own factual claims — Spiroc Lord created Jan 2025, Bazzt Zzzt Nov 2025 "and never edited since", the `{{Classic Era}}` template's current spread, whether any Plane of Sky/Hate/Fear boss page has since gained a post-launch measured edit — are claims about a website. This audit read a git tree. `grep -ci "Spiroc" HANDOFF.md` returns 0 and no dated re-read exists in the repo, so nothing in this project watches 

### `3-hard-rules`

**Method.** Three-part search, run identically against every rule. (1) Ledger: `grep -n -i "<distinctive term>" HANDOFF.md` over all 22,461 lines / 379 `| R123 |` rows, then read every hit in context with `sed -n`. Terms run: "invent a number", "not recorded", "NOT_RECORDED", "merge your own", "merged my own", "self-merge", "unreviewed", "push to main", "pushed to main", "straight to main", "pull request", "Sebilis", "Iksar", "Expedition", "out of scope", "worse copy", "half-rebuild", "flagged gap", "delete a gap", "gaps close", "look complete", "tidying", "classic EverQuest", "Legends", "BACKLOG", "forbids", "build.sh", "_build/source", "dungeons/", "hand-edit", "regenerat". (2) Source repo: `git grep 

**Control.** Two controls, run with the identical three-part method. CONTROL A, on line 348 "Never present classic EverQuest as Legends" — a rule I had independently confirmed fires: the method returned exactly ONE HANDOFF.md hit (line 1699), and that single hit is a substantive catch (B's dual-wield audit taking the classic class table as its yardstick). This is the load-bearing control, because the Sebilis rule I am reporting NEVER-FIRED also returns exactly one HANDOFF hit — the method demonstrably detects a real firing at n=1, so the Sebilis null is a null in the searched corpus rather than a method failure. The difference is only visible on READING the hit, which I did in both cases. CONTROL B, on l

**Unmeasured.** Six things I could not establish, stated so they are not read as nulls.  1. PERMISSION DENIALS ARE INVISIBLE TO BOTH INSTRUMENTS. The rules at L352 and L356 were enforced through `.claude/settings.json`, and a denied tool call writes nothing to HANDOFF.md and nothing to git. Neither the ledger nor the history can show whether either rule ever caught an edit or a merge. This is why L352 is CANNOT-TELL rather than NEVER-FIRED, and it means my BLOCKED-ONLY verdict on L356 rests on the one occasion 

### `4-file-map`

**Method.** Read lines 370-509 in full from `git show "origin/main:CLAUDE.md"` (947 lines total; section 4 spans 370-509, section 5 begins at 510). Extracted every instruction, prohibition and standard from the map block.  For each rule, four searches: (1) Director ledger — `grep -n -F "<distinctive phrase>" HANDOFF.md` (22,461 lines, 379 rows matching `^| R[0-9]`), literal (-F) after an unescaped `.` produced a false positive early on. (2) eql-source's OWN HANDOFF.md (384 lines, a DIFFERENT file from the Director ledger) — `git show "origin/main:HANDOFF.md"`, same literal greps. Added only after the positive control exposed that (1) alone was insufficient. (3) History — `git log --oneline origin/main -

**Control.** CONTROL RUN, AND IT FAILED FIRST — which is the reportable part.  Control 1 (passed): contamination.py's inward-only rule, known to fire. `grep -n -F "attack ad" HANDOFF.md` -> 2 hits, including line 3834 where the rule's own words are quoted to convict a real shipped defect. Method finds a known firing. Also `grep -c -F "gate_selftest" HANDOFF.md` -> 55, and `grep -n -F "edited in place" HANDOFF.md` -> line 12801, both known-firing.  Control 2 (FAILED, and I corrected the method): I ran the identical search for serve.py — `grep -c -F "serve.py" HANDOFF.md` -> 0 in the Director ledger. Under my original method that is a NEVER-FIRED. It would have been FALSE. `git grep -l -F "serve.py" origin

**Unmeasured.** WHAT I COULD NOT ESTABLISH:  1. NEVER-FIRED remains the weakest verdict here, and my control proves why. The serve.py case shows the Director ledger alone produces false negatives; I cannot rule out that a fifth channel I did not search (session transcripts, closed PRs, the six sessions' own repos, GitHub issue threads) records the site.config.json or state/ rules firing. Both NEVER-FIRED verdicts rest on affirmative evidence — 29 uncaught violations sitting on main, and check.py's own comment s

### `5-build-and-verify`

**Method.** Read the section in full via `git show "origin/main:CLAUDE.md" | sed -n '495,670p'` with MSYS_NO_PATHCONV=1 and MSYS2_ARG_CONV_EXCL='*' exported (the shell note is real: an unquoted ref:path mangles silently). INSTRUMENT FAULT FOUND AND CORRECTED MID-AUDIT: the local checkout's HEAD is `e6039020`, four commits behind `origin/main` `f98e7cd0`, so a bare `git log -- scripts/conformance.js` returned a truncated history that omitted the three most recent commits. Every subsequent read was pinned to `origin/main` explicitly; the earlier bare-HEAD result was discarded, not used. Ledger searches, all against C:/Users/Lindsey/Desktop/EQLS Director/HANDOFF.md (22,461 lines, 381 rows matching "^| R"):

**Control.** POSITIVE CONTROL, run before any NEVER-FIRED verdict, against a rule I had already found firing — §5's `newline='\n'` write rule (line 623). Ledger arm: `grep -n -F 'newline="\n"' HANDOFF.md` returns six hits, including HANDOFF.md:17268 which cites the section by name — "`stamp.py` wrote `state/last-build.json` without `newline=\"\\n\"`, which `CLAUDE.md` §5 [requires]" — plus R117 at HANDOFF.md:11913 and the fix at HANDOFF.md:17260. History arm: `git log --all --oneline -S'newline="\n"'` in eql-source returns `bd8c215a` "TO DIRECTOR: R113 — an impossible comparison now fails, and stamp.py writes LF". Both arms of the method find a known firing. TWO CALIBRATION NOTES THE DIRECTOR SHOULD WEIG

**Unmeasured.** WHAT I COULD NOT ESTABLISH, and the Director should not read any of this as settled. (1) I did not execute anything the section instructs. I did not run build.sh, check.py, gate_selftest.py, toolsmoke.js, conformance.js or prose_budget.py — no build, no browser, no sweep. Every claim about what a script does is read from its source on origin/main, which is the weaker witness this project's own record repeatedly says it is. In particular I did not re-measure the five font widths, the 238-second s

### `6-design-system`

**Method.** All work read-only, in C:/Users/Lindsey/Desktop/EQLS Director/peers/eql-source with MSYS_NO_PATHCONV=1 and MSYS2_ARG_CONV_EXCL='*' exported before every quoted `git show "ref:path"`.  READ: `git show "origin/main:CLAUDE.md" | grep -n '' | sed -n '655,725p'` — section read in full before any search. (Piping through `grep -n ''` gives true file line numbers; `cat -n` after `sed` does not.)  PER-RULE SEARCH, four channels, run for every rule: (a) ledger: `grep -n -i "<term>" HANDOFF.md` (22,461 lines) and `grep -n "^| R[0-9]" HANDOFF.md | grep -i "<term>"` for the 379 numbered ruling rows. (b) commit messages: `git log --all --oneline -i --grep="<term>"`. (c) file history: `git log --all --onel

**Control.** CONTROL RUN, AND IT FAILED THE FIRST INSTRUMENT — which changed my method.  Control rule: "A heading level is an outline claim, not a size" (CLAUDE.md:678), known to fire at commit 50085a8e ("heading skips closed on all 717 pages, and the fix for them silently stripped type on seven").  (a) Ledger channel FAILED to find the known firing. `grep -n -i "heading level" HANDOFF.md` returns 2 hits (lines 1982, 2145) and both are about card treatment in an unrelated table design. `grep -n "703" HANDOFF.md` returns 8 hits and every one is PR #153's 703-FILE count, a different subject. The Director's ledger does not record this firing at all. (b) Git channel SUCCEEDED: `git log --all --oneline -i --g

**Unmeasured.** WHAT I COULD NOT ESTABLISH:  1. BLOCKED-ONLY IS STRUCTURALLY UNMEASURABLE HERE. The repository records work that landed. Legitimate work a rule silently deterred leaves no commit, no ledger row, and no diff. I therefore report no BLOCKED-ONLY verdict in this section, and that is a limit of the instrument, not a finding that no rule ever over-fired. R207 (HANDOFF.md:12003) is the closest thing to a deferral record I found, and it defers work *toward* the WCAG rule rather than being blocked by it.

### `7-writing-voice`

**Method.** Read the section in full from `git show "origin/main:CLAUDE.md"` (947 lines total; §7 = 718-766, extracted with awk on line numbers and re-checked byte-for-byte with `cat -A` for the list structure). Established the section's own history: `git log -L 718,766:CLAUDE.md origin/main` and a direct `diff` of the §7 block at `2d48b193` against `origin/main` — IDENTICAL, so §7 is unchanged since 2026-08-17.  Two-pronged search per rule, plus a live-site prong where the rule makes a checkable claim: (1) LEDGER: `grep -nEi "<pattern>" HANDOFF.md` (22,461 lines, 379 rows matching `^| R[0-9]`), always with hyphen/space-tolerant alternation — see method_control for why. (2) HISTORY: `git log --format="C

**Control.** Run before any NEVER-FIRED verdict, and it FAILED first, which is the important part.  CONTROL A (ledger prong). Known-firing rule: "No experience per kill at all" — known to fire because commit `72a41071` (2026-08-17) withdraws Castle Mistmoore's experience section citing the rule's own 26/35 reason verbatim. Method as first written, `grep -n -i "experience per kill" HANDOFF.md`, returned NOTHING. That is an instrument fault, not a finding: the ledger writes it hyphenated. CONTROL A2, `grep -nEi "experience[ -]per[ -]kill" HANDOFF.md`, returns HANDOFF.md:10082. Every ledger search in this audit was re-run hyphen-tolerant after that. Had I not run the control I would have filed at least one 

**Unmeasured.** Five things I could not establish, stated so nobody builds on them.  1. THE SCOPE WORD IS UNDECIDED AND IT DECIDES TWO OF MY FINDINGS. §7 says "any page a reader sees" (per the ledger's gloss at HANDOFF.md:3563) but never defines it, and the project has ruled three different ways within three days: comments "reach no reader" (209fbb41, 1 Sep); grepping a shipped bundle IS the test (7c2567c4, 3 Sep); `public/app/` "is not one of our pages" (737700f9). Until that is settled, my measurement of `pub

### `8-adding-things`

**Method.** All work read-only against `C:/Users/Lindsey/Desktop/EQLS Director/peers/eql-source` (origin/main) and `C:/Users/Lindsey/Desktop/EQLS Director/HANDOFF.md`, with MSYS_NO_PATHCONV=1 and MSYS2_ARG_CONV_EXCL='*' exported before every `git show "ref:path"`.  SECTION READ: `git show "origin/main:CLAUDE.md" | sed -n '760,815p'` with absolute line numbers restored by awk. 947 lines total.  THREE INSTRUMENTS, run per rule: 1. Ledger: `grep -n -i "<distinctive phrase>" HANDOFF.md` (22,461 lines; 379 rows matching `^| R[0-9]`). Phrases used: "drawing is an assertion", "a drawing", "encounter model", "no template", "Eye of Veeshan", "island 7", "build4", "restyl", "archive-plates", "/archive/index", "th

**Control.** Required before the one NEVER-FIRED verdict (rule 13, "do not restyle them in the archive"). I ran the IDENTICAL three-instrument method against two rules from this same section that I had already found firing, and against the target, side by side:    phrase                            ledger grep -c | git log -S | git log --all --grep   "a drawing is an assertion"              3       |     4      |     2      <- KNOWN FIRING, FOUND   "must never read as new content"         0       |     1      |     2      <- KNOWN FIRING, FOUND   "restyled archive"                       0       |     1      |     1      <- target  The control fires. For "a drawing is an assertion" the method returns HANDO

**Unmeasured.** WHAT I COULD NOT ESTABLISH.  1. WHETHER THE ZONE-ADDITION CHECKS HAVE EVER CAUGHT ANYTHING. `check.py`'s accent- and plate-uniqueness failures happen on a contributor's machine before a commit exists. A firing that is fixed in the working tree leaves no artefact in git or the ledger. I searched both and found nothing either way; that is a limit of the instrument, not evidence the checks are idle. The same limit applies to the `_build/source/<slug>.html` warning.  2. THE TWO DATE DISCREPANCIES — 

### `9-known-gaps`

**Method.** Read the whole section from `git show "origin/main:CLAUDE.md"` (947 lines total; section 9 spans 809-942, bounded by the `## 9.` and `## 10.` headers found with `git show "origin/main:CLAUDE.md" | grep -n "^## "`). Extracted 24 distinct rules/claims.  Then, per rule, three legs: (a) LEDGER — `grep -n -i "<distinctive phrase>" HANDOFF.md` (22,461 lines) for: "typed beside|hand-typed", "trio", "outside the credits", "our_damage_share", "damage_is_floor", "fullest view", "verify_level", "verify_gate", "gate 3|room list|120 units", "asymmetry", "re-derive", "hit point", "island", "28 July|respawn ceiling", "port level", "Sky class tooltip", "eleven class", "SWEEP-2026-08-17", "not tidying|close 

**Control.** CONTROL RULE: "Other players are never named on the site outside the credits" (CLAUDE.md:826-827) — chosen because I had already found it firing before designing the NEVER-FIRED test.  Ran all three legs of my exact method against it: - (a) `grep -n -i "named on the site outside the credits" HANDOFF.md` → HIT at HANDOFF.md:5545-5547, a live firing: a lockout window named eight players and the rule stopped them reaching the site ("The count and the shape may be recorded; the names are discarded"). - (b) `git grep -n -i -c "outside the credits" origin/main` → HIT in 4 files (`_build/raidstats.py` x3, `_build/changelog.py`, `_build/logstats.py`, `public/sources.html`). - (c) `git log origin/mai

**Unmeasured.** Nine things I could not establish, stated so the Director does not read this audit as wider than it is.  1. **THE INSTRUMENT FAULT, restated as a fault and not a finding.** The re-derivation command at CLAUDE.md:872 cannot run: `AttributeError: 'list' object has no attribute 'get'`. I therefore re-derived the self-heal table with my own equivalent code, not with the section's. My numbers match the table exactly, but the section's own instrument did not verify itself and has never been able to.  

### `10-when-unsure`

**Method.** Set MSYS_NO_PATHCONV=1 and MSYS2_ARG_CONV_EXCL='*' throughout. (1) Read the section: `git show "origin/main:CLAUDE.md" | awk 'NR>=938 && NR<=960'`; confirmed line 947 is EOF via `wc -l` (947). (2) Provenance: `git log --oneline origin/main -- CLAUDE.md` (50 commits); `git log -S` on "When you are unsure", "hedging the prose", "one log line", "Naming the missing evidence"; `git show ffc04d67:CLAUDE.md | grep -A12 "When you are unsure"` and `git show 5974980b -- CLAUDE.md` to diff the one edit. (3) Ledger, `grep -in` over the 22,461-line HANDOFF.md for: hedg, unsure, "say so", "what would resolve", "would resolve it", "missing evidence", "naming the missing", "one screenshot", "one log line", 

**Control.** POSITIVE CONTROL RUN, and it passed. I picked §3's "Never invent a number" (CLAUDE.md:333) — known to fire, because commit `a61b64ea` is titled "CLAUDE.md carried an invented number, in the rule that forbids them". I then ran my exact method against it without using that title: `grep -in "invent a number" HANDOFF.md` returned :10311 ("whose first hard rule is *never invent a number*, sitting for five days"), :13206, and R378 at :12174; `grep -inE "invented (a )?number" HANDOFF.md` returned R29 at :11825 and :13202. So the ledger-grep arm finds a known firing of a rule in a different section. SECOND CONTROL, on this section's own mechanism, to prove the method has resolution here and not only

**Unmeasured.** FIVE THINGS I COULD NOT ESTABLISH. (1) WHETHER §10 HAS EVER BLOCKED. I searched HANDOFF.md for over-refus, "too cautious", over-cautious, "excess caution", over-hedg, "refused too", over-fire, over-fires, over-fired, and got exactly one hit — R378 at :12174 — which names three over-firing clauses and none of them is §10 (section 7's forbidden-noun list, the `conformance.js` type ban, and `/ship`). That is a possible absence of block-evidence, not an absence; the search was over one file and elev
