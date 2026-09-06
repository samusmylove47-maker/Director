# Client Deep Research — first-party answers in the EQ Legends install

**Session:** eqlsdeep-4f [abc245]
**Branch:** `client-item-table-count`
**Date:** 2026-09-06
**Status:** PARTIAL — priorities 1 and 2 answered, 3–5 not started. Reporting as instructed.
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

Priorities 3 (zones/difficulty), 4 (lockouts/instances) and 5 (systematic contradiction
sweep) are untouched. Reported as not started rather than left to be inferred from silence.

The §2.4 method generalises directly to priority 5: join a published dataset to a
first-party client table, group conflicts by value-pair, and **read the shape before
reporting the count.**

---

## 5. INSTRUMENT FAULTS

**IF7 — The first-row join would have manufactured 18 conflicts.** Spell names are not
unique (3,604 duplicated). Comparing against the first matching row alone produced 172/56/71
disagreements; comparing against all rows sharing a name gives 163/51/67. Caught by asking
whether the join key was unique **before** reporting, not after. **A join on a non-unique
key does not fail — it produces plausible wrong answers.**

**IF8 — Counting conflicts without grouping them nearly produced a false headline.** "163
recast contradictions" was my first result and it was arithmetically correct. 136 of them
are one systematic offset. **The count was right and the finding would have been wrong**;
only grouping by value-pair exposed it. This is the same lesson as IF4 in the companion
report, one level up: check the *shape* of a result that agrees with your expectation, not
just its arithmetic.
