# Client Deep Research — first-party answers in the EQ Legends install

**Session:** eqlsdeep-4f [abc245]
**Branch:** `client-item-table-count`
**Date:** 2026-09-06
**Status:** priorities 1, 2, 3 and 4 answered. Priority 5 NOT STARTED. Session stopping — pin here.
**Companion:** `CLIENT-ITEM-TABLE-COUNT.md` (the item-table assignment, closed)

---

## HEADLINE

**The client states recast, cast time and mana for all 73,975 spells, and it contradicts
the wiki the project publishes from.**

> **Recast: 136 spells where the wiki says 2.25 s and the client says 1.5 s.**
> One systematic difference, not 136 defects.
> **Plus 27 further recast conflicts, 51 cast-time conflicts, and 67 mana conflicts**
> that are idiosyncratic — 41 and 64 distinct value-pairs respectively, i.e. genuinely
> per-spell rather than one rule.

The client is first-party and the wiki is a transcription. Where they disagree, the client
should win — **but the 2.25/1.5 split looks like a ruleset difference between EQ variants,
not a wiki error, and that distinction must be settled before anything is republished.**

---

## 0. PRE-REGISTRATION AND BOUNDS

**Population, fixed before counting:** all 73,975 records in `spells_us.txt`; all 22 data
rows in `ItemDistillerDefs.txt`. No subsetting.

**Read-only:** verified, not asserted. `find <install> -newermt <session start>` — every
shipped data file retains its original mtime (`spells_us.txt` 2026-08-24 17:00,
`dbstr_us.txt` 2026-08-31 18:18). The install's only changed files are the owner's own
play — chat logs, hotbars, `userdata/`. **The owner is playing while I read.** Candidate
files were copied to scratch; large sweeps read in place. Reading is not writing.

**Publication intent, decided before the data:** field semantics, aggregate counts,
conflict counts and methodology are publishable. **The extracted spell tables are not**,
and are not being produced as a public artefact.

**Client build:** `eqgame.exe` 2026-09-02 11:11; launcher "All files are up to date"
2026-09-05 10:57. No patch since measurement.

---

## 1. THE CRLF GUARD — and why the one I was first given would not have caught it

Session C's amended rule was correct and I adopted it before parsing anything.

`spells_us.txt` **is CRLF**: 73,975 lines, 73,975 carriage returns, 173 fields per row.
Field 173 is exactly where a `\r` would ride along in Python — `.` matches CR, so a
`matched/read` counter reads a clean 100% while every `$`-anchored pattern downstream
silently fails.

**What I carry instead — a positive control at the layer that breaks.** `method/spellparse.py`
normalises once, where lines are created, and its `parity_test()` asserts on real CRLF
bytes that:

1. the CRLF fixture produces rows at all (catches the JavaScript mode),
2. CRLF and LF parses are **identical**,
3. **no field ends in `\r`** (catches the Python mode),
4. a `$`-anchored regex still matches a field sourced from CRLF.

```
PARITY OK (CRLF == LF, no CR in fields, $-anchor works)
lines read: 73975 | rows parsed: 73975 | parsed/read: 100.0000%
field counts: {173: 73975} | CR in any field: False
```

Normalise at the boundary, once; do not defend pattern by pattern. Every count below also
carries an explicit checksum assertion.

---

## 2. PRIORITY 1 — `spells_us.txt`

### 2.1 Structure

73,975 records, `^`-delimited, **uniformly 173 fields** (no ragged rows). Field semantics
were identified empirically, then **confirmed against spells whose values are independently
known** rather than assumed:

| Col | Meaning | Confirmation |
|---|---|---|
| 0 | spell id | 73,975 distinct, max 74,100 |
| 1 | spell name | 66,444 distinct — **names are NOT unique**, see §2.3 |
| 8 | cast time (ms) | Gate 5000; Summon Corpse 5000 |
| 9 | recovery time (ms) | 1500 near-universally — the global cooldown |
| 10 | **recast time (ms)** | **Harm Touch 1,200,000 = 20 min; Lay on Hands 4,200,000 = 70 min; Divine Aura 900,000 = 15 min** — all match long-known EQ values |
| 14 | mana | Gate 70; Summon Corpse 500 |
| 36–51 | **class levels, 16 columns**, 255 = cannot cast | Harm Touch `SHD 254`; Lay on Hands `PAL 254`; Divine Aura `CLR 1 / PAL 48` |

Class column order is the standard EQ order: WAR CLR PAL RNG SHD DRU MNK BRD ROG SHM NEC
WIZ MAG ENC BST BER.

**This directly fills the `=Upgrades` gap.** Session B's 2,011 scraped spells with recast
times are vendored and read by nothing; the client states recast for **all 73,975 records**
as column 10, first-party.

### 2.2 The join to the project's data

Against `EQL50ups/research/data/eqbuddy-harvest-spells.json` (1,929 wiki records):

```
wiki names matched in client : 1,763 of 1,929  (91.4%)
wiki names NOT in client     :   166
checksum: 1,763 + 166 = 1,929  OK
```

**The join works.** 91.4% on exact name match, before any normalisation of punctuation or
roman numerals — so the ceiling is higher than this with modest effort.

### 2.3 An instrument hazard I had to clear first — spell names are not unique

The client has **73,975 rows but 66,444 distinct names; 3,604 names carry more than one
row.** A naive `name → first row` join silently compares the wiki's spell against the wrong
record.

I therefore re-ran every comparison against **all** rows sharing a name, counting a
disagreement only when **no** client row agrees:

| Field | Disagreements, first-row join | Resolved by another row | **True conflicts** |
|---|---|---|---|
| Recast | 172 | 9 | **163** |
| Cast time | 56 | 5 | **51** |
| Mana | 71 | 4 | **67** |

**18 of the 299 apparent conflicts were my own join artefact.** Had I reported the
first-row numbers they would have been wrong in the direction of a more dramatic finding.

### 2.4 Agreement, and the contradiction

| Field | Comparable | Agree | Agree % | True conflicts |
|---|---|---|---|---|
| Recast | 1,685 | 1,513 | **89.8%** | 163 |
| Cast time | 1,683 | 1,627 | **96.7%** | 51 |
| Mana | 1,694 | 1,623 | **95.8%** | 67 |

*(checksums asserted: agree + disagree = comparable, for each row)*

**Grouping the conflicts by (wiki value, client value) is what makes them interpretable —
and it changes the finding completely:**

| Field | True conflicts | Distinct value-pairs | Shape |
|---|---|---|---|
| **Recast** | 163 | **20** | **136 of them (83%) are the single pair `wiki 2.25 → client 1.5`** |
| Cast time | 51 | 41 | scattered, genuinely per-spell |
| Mana | 67 | 64 | scattered, genuinely per-spell |

**The recast result is ONE finding, not 163.** A single systematic 2.25 s → 1.5 s
difference across 136 spells, plus 27 individual cases. Reporting "163 recast
contradictions" would be true by the count and false by the meaning.

### 2.5 What I am NOT claiming

**I have not established that the wiki is wrong.** 2.25 and 1.5 are both plausible global
recast floors, and they differ by exactly 1.5×. **The likeliest explanation is that the
wiki source describes a different EQ ruleset from the Legends client** — which would make
this a provenance finding about the source, not an error list.

That distinction decides whether 136 published values need changing or none do, and **it
cannot be settled from inside the client.** It needs someone who knows which server the
`eqbuddy` harvest came from. **Do not republish anything off the back of this until that is
answered.**

The scattered cast-time and mana conflicts are a different matter: 41 and 64 distinct
value-pairs are not one rule, and those are the ones most likely to be genuine
transcription defects worth checking individually.

### 2.6 The full 173-column sweep — done properly, not sampled

The Director's instruction was to sweep rather than characterise from a sample — my own
step 7, written after IF6. I had profiled roughly 50 of 173 columns. **Profiling all 173
found three payloads I would otherwise have missed**, which is IF6's lesson holding.

| Col | Content | Evidence |
|---|---|---|
| **172** | **the spell EFFECT SLOTS, packed pipe-delimited** | see below |
| **81** | **recourse spell id** (spell → spell FK) | `Siphon Strength` → 2463 `Siphon Strength Recourse`; `Dark Empathy` → 3650 `Dark Empathy Recourse` |
| 145 | a second spell-id reference | `Flames of Kesh`yk I/II/III` → 429 `Strength of Stone` |
| 167 | item-ID-space reference, only 3 real values (177700/1/2) on 254 spells; −1 elsewhere | — |
| 3 | pet/actor tag, 3,341 distinct | `PCPetMagS01L005ElemErf` |
| 165 | ability-id-shaped text, 1,930 distinct | `100110600` |

> **CORRECTED 2026-09-06, same session.** My first description of this column said the
> record was `1 + 5n` pipe-separated fields, a slot **count** followed by five fields per
> slot, with the SPA first in each slot. **That was wrong** — I had split on `|` only and
> missed that `$` is the slot separator, so multi-slot spells were being mangled and the
> leading number is a slot **index**, not a count. Filed as IF9. The corrected structure is
> below and is now validated across every row rather than read off three examples.

**Column 172 is the largest untapped payload in the install: the spell effect slots.**

**Structure — `$` separates slots, `|` separates fields within a slot:**

```
slot | SPA | base1 | base2 | max | calc          (6 fields, always)
```

```
Gate           id 36     1|26|98|1|100|0
Complete Heal  id 1292   1|101|1|0|100|1
Harm Touch     id 40993  1|0|-139210|0|100|0
multi-slot     1|36|-1|0|100|0 $ 2|35|-1|0|100|0 $ 3|0|5|0|100|0
```

**Validated across the whole file, not sampled:**

| Check | Result |
|---|---|
| Total effect slots | **275,022** |
| Slots that are **not** exactly 6 fields wide | **0** |
| Rows whose slot indices run exactly 1,2,3,… | **71,237** (3 exceptions) |
| Rows with no effect data | 2,735 |
| **Distinct SPA values in field 1** | **434** — against EverQuest's ~500-entry SPA table |

**Field 1 is the SPA (effect type), confirmed against independently-known values:**

- **Gate carries SPA 26** — 26 is Gate in EQ's long-known SPA table.
- **Complete Heal carries SPA 101** — 101 is the Complete Heal SPA. *(This is better
  evidence than the example in my first version, which came from a different record — see
  IF9.)*
- **Harm Touch carries SPA 0** (hit-point change) with base **−139,210** — right sign,
  right magnitude.
- The two commonest SPAs across 275,022 slots are **10** (89,152) and **0** (26,789) —
  a null/stat effect and hit-point change, exactly the expected shape.

**So the client ships computable spell effects — type, base, and formula inputs — for all
73,975 spells.** Session C's 1,067-entry hand-maintained roster and its 56-heading stacking
table are transcriptions of something the client states outright.

**What I have NOT established:** the identity and order of `base1 / base2 / max / calc`.
The slot framing and the SPA position are now proven across 275,022 slots; **the remaining
four fields are named here by convention, not by evidence.** That is the afternoon's work
against the published SPA table, and it is the highest-value thing left in this file.

---

## 3. PRIORITY 2 — `Resources/ItemDistillerDefs.txt`

```
lines read 23 | comment 1 | data rows 22 | checksum OK
```

Format `#ITEM_ID^DISTILLER_RANK^`: ids **47001–47021 carrying ranks 1–21**, plus **52023
with rank −1** (a sentinel).

**My assessment: this is probably NOT ground truth for the `+0…+10` upgrade curve, and
Session B should not treat it as such without more evidence.**

- The rank space is **1–21**, not the 11 values a `+0…+10` curve needs. Nothing maps
  cleanly.
- "Distiller" in EverQuest denotes **augmentation-removal** consumables sold in ranks, a
  different mechanic from item upgrade tiers.
- The client **does not name these items**: ids 47001–47021 appear in no item-name table
  (`dbstr` types 44/17). *(Note: `dbstr` type 6 has an id 47001, but type 6 is keyed by
  **spell** id — a different ID space, and a trap worth flagging.)*

**Stated at the width of the evidence: I did not find a link between this file and the
upgrade curve. That is not proof there is none** — it is 22 rows and a name, and I have no
`+N` model from Session B in front of me to test against. If Session B can send its curve,
this is a ten-minute check rather than an open question.

---

## 4. NOT STARTED

**Priority 4 is answered in §4; priority 3 in §5.** Priority 5 (systematic contradiction sweep) is not started. Reported as not started rather than left to be inferred from silence.

The §2.4 method generalises directly to priority 5: join a published dataset to a
first-party client table, group conflicts by value-pair, and **read the shape before
reporting the count.**

---

## 4. PRIORITY 4 — LOCKOUTS AND INSTANCES

**The client describes the lockout system in full. It ships the SCHEMA and the RULES; it
ships no DURATIONS.** Both halves matter to Session D.

Method: exhaustive term sweep of `eqstr_us.txt` (7,144 lines read, 97 matched, **all 97
printed and read — not sampled**), then a whole-install sweep, then the UI definitions.

### 4.1 There are TWO separate mechanisms, and the client names both

| | Replay timer | Event lockout |
|---|---|---|
| Keyed to | **a zone** | **an event** |
| Client's own words | *"the amount of time you must wait before being allowed to enter another instance of **that zone**"* (str 3536) | *"they have recently experienced %2 … until they can **experience it again**"* (3561, 3592) |
| Cleared by | time only | time **or the event occurring** — *"or until event %2 has occurred"* (3592); *"once %2 has been completed"* (3561) |

**Conflating these two would be a modelling error, and only the client distinguishes them
this cleanly.**

### 4.2 Replay timers are per-zone AND per-difficulty

> **str 3519: `You have %1d:%2h:%3m:%4s remaining until you may enter %5 (Difficulty %6).`**

This is the template behind the `/dzListTimers` line recorded earlier in this project — the
one that printed a null as a 56-year duration. **The `(Difficulty %6)` parameter is
first-party evidence that a replay timer is scoped to zone *and difficulty*, not zone
alone.**

### 4.3 The lockout record is a triple — from the client's own UI

`uifiles/default_modern/EQUI_DynamicZoneWnd.xml`, listbox `DZ_TimerList`:

> **columns: `Lockout Time` | `Instance Name` | `Event Name`**

That is the client's own schema for a lockout row. `DZ_MemberList` carries
`Members: | Status: | Flagged:` — so members also carry a per-player **Flagged** state.

### 4.4 A third mechanism: instance CHARGES

Separate from both timers, and easy to miss:

- str 257 — *"You are out of instance charges, you must wait."*
- str 396 — *"…you must wait until you have at least one charge available."*
- str 3527 — *"Accepting will incur you **a charge or a replay timer**."*

**"a charge OR a replay timer" is the client stating these are alternative costs.** Any
model with only timers in it is missing a mechanic.

### 4.5 Event lockouts propagate to the whole group

> str 5089: *"Including %1 in the expedition **will prevent everyone in the expedition from
> experiencing %2**."*
> str 5043: *"One or more raid members has an event lockout for this instance: %1 Click yes
> to **apply the above lockout(s)** and begin the expedition."*

**One locked-out member can impose that lockout on every other member.** For a tool that
projects a raid's availability, this is the difference between a per-character model and a
per-roster one.

### 4.6 THE BOUND — no durations ship, and this is the useful negative

**Every duration in every one of these strings is a format parameter** (`%1d:%2h:%3m:%4s`),
not a value. I swept the whole install: no lockout period, no reset interval, and **no
weekly or daily reset constant** appears in any shipped file.

**So Session D cannot get reset periods from the client, and should stop looking.** The
durations are server-sent, exactly as item data is. What the client *does* settle for free
is the **shape**: two mechanisms plus charges, replay scoped by zone+difficulty, lockouts
scoped by event, group propagation, and a three-field timer record.

**Stated at the width of the evidence:** I did not find durations in the install. Given the
sweep was exhaustive over shipped files rather than sampled, that is a strong negative —
but it remains "I did not find", not "they are not there".

---

## 5. PRIORITY 3 — ZONES AND DIFFICULTY

**The most important result here is a warning, not a finding: there are TWO five-tier
difficulty scales in this game and they are different objects.**

### 5.1 The client's five-tier scale is NOT the site's five tiers

Exhaustive regex over `eqstr_us.txt` (7,144 lines read, **102 tier strings matched, all
counted**) yields **exactly five distinct tiers**:

| Client tier | Occurrences |
|---|---|
| LOW DIFFICULTY | 15 |
| LOW TO MODERATE DIFFICULTY | 31 |
| MODERATE DIFFICULTY | 28 |
| MODERATE TO HIGH DIFFICULTY | 13 |
| HIGH DIFFICULTY | 15 |

**Every one of the 102 is a Race / Class / Deity rating shown at character creation** —
the string is literally *"This Race / Class / Deity combination is of … DIFFICULTY"*.

The site's `learn/difficulty.html` publishes a *different* five: **instanced zone
difficulty, "5 tiers", "D4 is the maximum", "the zone line names yours"** — mob damage,
resists, aggro range and loot condition.

> **Two unrelated five-tier scales, both called "difficulty", in the same client. Anyone
> joining them on the number five will produce a confident, wrong result.**

I nearly did: I found a five-tier scale while looking for a five-tier scale, and the count
matched. **It matched because five is a common number of tiers, not because they are the
same thing.**

### 5.2 Does the client corroborate the ZONE tiers? Unevaluable — and here is why

The client **confirms instanced zone difficulty exists as a first-class parameter**:

- str 3519 — `…until you may enter %5 (Difficulty %6)`
- str 15605 — *"The current zone you are currently in does not match your instanced
  difficulty zone."*
- `EQUI_PersonalInstanceWnd.xml` and `EQUI_RaidRequestWnd.xml` both carry a
  **`Difficulty:` combobox**, alongside `Type:` and a third `Spawning` selector.

**But the comboboxes are empty in the XML — they are populated at runtime from the
server.** The client therefore **names the axis and ships none of its values.**

**So "5 tiers" and "D4 is the maximum" are UNEVALUABLE against the client.** Not
contradicted, not confirmed. The site cites EQL Tools for that scaling work and labels it
by how it is known, which remains the right provenance; **the client cannot be added as a
second witness.**

### 5.3 Zone experience modifiers — a bounded negative

`Resources/ZoneNames.txt` is **700 rows, uniformly 4 fields**: `id ^ name ^ a ^ b`.
577 distinct names, ids to 999. Fields 3 and 4 are **binary**, not modifiers:

| (a, b) | rows |
|---|---|
| (0, 0) | 622 |
| (12, 60) | 74 |
| (12, 0) | 4 |

The 74 carrying `12^60` are the classic home and newbie zones (South Qeynos, North Qeynos,
Surefall Glade, Qeynos Hills, Highpass Hold…). **Whatever the pair encodes, it is a flag
with two states, not a per-zone experience multiplier.**

**I found no zone experience modifier anywhere in the install.** The only experience
mechanic the client states is a *legacy server max-level bonus* (strs 9079, 9085, 9124 —
*"Your legacy server experience bonus … has increased to %1%"*), which is account-scoped,
not zone-scoped.

**Stated at the width of the evidence: I did not find zone experience modifiers. The sweep
was exhaustive over shipped files rather than sampled, so it is a strong negative — but it
remains "I did not find."**

### 5.4 Three additions to the lockout picture (§4), found in the difficulty UI

Worth folding into D's model:

- **Charges regenerate on a timer.** `PersonalInst_TimerList` columns are
  **`Next Charge` | `Current Charges`** — so charges are a replenishing pool, not a fixed
  allowance.
- **Raid lockouts carry a Type.** `RaidRqst_TimerList` columns are
  **`Lockout Time` | `Name` | `Type`** — a *different* schema from `DZ_TimerList`
  (`Lockout Time | Instance Name | Event Name`). **Two lockout lists with two schemas.**
- **Instances have three independent axes**, not one: `Difficulty`, `Type`, and
  `Spawning`. The placeholder text in both windows reads `South Qeynos 1 (Adaptive)` —
  **"Adaptive" is a named mode**, and it appears in the instance's display name.

---

## 6. INSTRUMENT FAULTS

**IF7 — The first-row join would have manufactured 18 conflicts.** Spell names are not
unique (3,604 duplicated). Comparing against the first matching row alone produced 172/56/71
disagreements; comparing against all rows sharing a name gives 163/51/67. Caught by asking
whether the join key was unique **before** reporting, not after. **A join on a non-unique
key does not fail — it produces plausible wrong answers.**

**IF9 — I published the wrong structure for column 172, and it was IF7 wearing a new coat.**

My first pass split column 172 on `|` alone and reported the record as `1 + 5n` — a slot
**count** followed by five fields per slot. **`$` is the slot separator.** The leading
number is a slot **index**. Multi-slot spells were being silently mangled into one
over-long row, and the tell was sitting in my own output: fields ending `0$2`, which I had
in front of me and read past.

**Two compounding causes, both mine, both previously catalogued:**

1. **Sampling.** I described the format from three examples — all of which happened to be
   single-slot spells, where splitting on `|` alone gives the right answer. **The sample was
   accurate and unrepresentative at once**, which is precisely IF6's shape.
2. **IF7 again, in a new place.** My probe used `{r[1]: r for r in rows}`, which keeps the
   **last** row per name, while every other section of this report used the **first**. So my
   `Complete Heal` example came from id 46303 and my recast figures from id 1292 — **two
   different records quoted as one spell in the same document.** Spell names are not unique
   and I already knew it.

**Corrected and validated across all 275,022 slots: every slot is exactly 6 fields, zero
exceptions.** The SPA conclusion survives and is stronger — 434 distinct SPA values against
a ~500-entry table.

**Caught before anyone acted on it, but only just:** the Director was relaying the old
structure to Session C as tomorrow's first task the same evening. **A wrong structure is
worse than no structure, because it is actionable.**

**IF8 — Counting conflicts without grouping them nearly produced a false headline.** "163
recast contradictions" was my first result and it was arithmetically correct. 136 of them
are one systematic offset. **The count was right and the finding would have been wrong**;
only grouping by value-pair exposed it. This is the same lesson as IF4 in the companion
report, one level up: check the *shape* of a result that agrees with your expectation, not
just its arithmetic.
