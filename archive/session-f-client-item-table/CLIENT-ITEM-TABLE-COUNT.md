# Client Item Table Count — EverQuest Legends

**Session:** eqlsdeep-4f [abc245] (was "EQLS Research Session F" — local addresses rotate)
**Branch:** `client-item-table-count`
**File:** `CLIENT-ITEM-TABLE-COUNT.md`
**Date:** 2026-09-04, **materially corrected 2026-09-06** (see HEADLINE and §4 IF6)
**Status:** COMPLETE — a measured partial count plus a bounded negative, on three corpora.
**Peer inputs:** all three previously-missing artefacts located and used (§3).

---

## HEADLINE

> **CORRECTED 2026-09-06.** An earlier version of this report said flatly that the client
> ships *no* item table. **That was too strong, and it was wrong.** The client ships a
> **partial, special-purpose item table of 1,158 named items keyed by real item IDs**
> (§1.7). I missed it by characterising a 1,126-record table from a four-record sample —
> the same instrument fault I had already caught and written up once (§4, IF6). The
> corrected finding is below. The *conclusion for the project* is unchanged, but it now
> rests on a measurement rather than on an overstated absence.

**The client ships no GENERAL item table. It ships 1,158 item names — 7.0% of the items
the owner actually holds — covering spell reagents, gems, summoned items and alternate
currencies. That subset cannot serve as the project's denominator.**

The count the assignment asked for, stated precisely:

| Question | Answer |
|---|---|
| Item records in the client's own data | **1,158 unique named items** (1,081 in `dbstr` type 44 + 79 in type 17, deduplicated) |
| Are they keyed by real item IDs? | **Yes** — verified: 17 IDs appear in both this table and the owner's inventory with identical names (`10307 = Fire Beetle Eye`) |
| Is it the full item population? | **No.** It covers **47 of 674** real held/looted items — **93.0% absent** |
| Can it be the coverage denominator? | **No.** A denominator that omits 93% of real items is not a population |

The evidence that it is a *subset* rather than a *table*, and the strongest number here:

> **536 of 674 item names (79.5%) that the owner's two characters demonstrably held or
> looted appear in NO file shipped with the client** — across all 11,973 shipped files
> and all 83,137 members inside the 2,272 containers.

Items the client has never heard of are sitting in the player's inventory. Item data is
server-sent; what ships locally is the slice the client must be able to name on its own,
chiefly because spells reference it.

**Corroborated by a third, independent corpus:** of the project's own 581-name union
(reconstructed; §2.1 explains why 581 and not 587), **532 appear nowhere in shipped client
data either** — and the 49 that do are spell names, achievement objectives and help-page
examples. That corpus was chosen without reference to the owner's inventory, so these are
not the same measurement repeated.

**Consequence for the project: the denominator still cannot come from the client.** The
587–3,700 range is not collapsed. What *is* now settled is that no larger client-side item
table exists to be found — the surface has been enumerated, not merely searched.

---

## 0. PRE-REGISTRATION (committed as f7bd04a BEFORE any number was produced)

### 0.1 Population decision — PRIMARY

**PRIMARY POPULATION: ALL item records present in the client's own shipped data,**
regardless of whether the item is equippable, obtainable, or currently in-game.

Rationale: the denominator this project needs is "how many items does the client know
about". Any narrowing requires a per-record flag I had not confirmed existed. A
population I cannot compute is not a population I may promise.

**SECONDARY POPULATION:** equippable/obtainable subset — to be computed only if the data
carried an explicit slot or usability field.

**Outcome:** both are moot. There are no item records to partition. No secondary number
is published, exactly as the pre-registration required.

### 0.2 Read-only discipline — HELD

Nothing under the install was written, moved, renamed or deleted.

**Precision, because the first draft overstated this.** It said "all work was on copies."
That is not accurate and the accurate version is not weaker: the small candidate data
files were copied out with `cp -p`, but the full-install sweeps (`grep -r`, the container
parse) **read the install in place**. Reading is not writing, so the discipline holds —
but "worked only on copies" was a claim I had not earned, and this document should not
contain one.

Containers were opened in binary read mode and never rewritten. **Verified, not asserted:
`find <install> -newermt <session start>` returned zero files at the close of the 4 Sep
session.** Re-checked 6 Sep: the only files modified since are launcher caches, `debug.log`,
`eqclient.ini` and the owner's own hotbar `.ini`s — **the owner has been playing.** No
shipped data file has changed; every one retains its original mtime.

### 0.3 Publication intent (decided before the data existed)

- **Publishable:** the aggregate counts, population definition, method, client build
  date, and verification outcomes — i.e. this document.
- **NOT for redistribution:** the extracted name list and copied client data files.
  These stay internal. No bulk client data is republished, and none was asked for.
- The owner's inventory dump and chat logs are a named person's account contents and are
  used here only as a *probe corpus*; no part of them is published.

---

## 1. THE MEASUREMENT

### 1.1 Client build / patch date

| Evidence | Value |
|---|---|
| `eqgame.exe` mtime | **2026-09-02 11:11** |
| `dbstr_us.txt`, `eqstr_us.txt` mtime (data patch) | **2026-08-31 18:18** |
| `spells_us.txt` mtime | 2026-08-24 17:00 |
| Launcher patch check, last entry | 2026-09-05 10:57 — *"All files are up to date"* |

The install was fully patched as of 2026-09-05. **Re-verified 2026-09-06: no data file has
been patched since the measurement** — `eqgame.exe` still 09-02 11:11, `dbstr_us.txt` still
08-31 18:18. Every figure in this report is current, not merely as-of.

### 1.2 What was searched

| Scope | Count | Method |
|---|---|---|
| Top-level entries, excluding dotfiles | **3,085** | `ls -1` |
| Top-level entries, including dotfiles | **3,087** | `ls -A` |
| All files, recursive | **12,034** | `find . -type f` |
| Subdirectories, recursive | **63** | `find . -type d` minus `.` itself |
| Shipped files searched (player-generated excluded) | **11,973** | see exclusions below |
| PFS containers (.eqg/.s3d/.pak/.pfs) parsed | **2,272** (0 failures) | `method/scanall.py` |
| Members inside those containers | **83,137** | `method/total.py` |

**Every enumeration here names its method, because two of them differ by method rather
than by fact.** Session 0 independently measured 3,087 and 63 where I had 3,085 and 64;
both pairs are correct and neither is a disagreement:

- **3,085 vs 3,087** — exactly two dotfiles, `.DownloadInfo.txt` and `.DownloadStats.txt`.
  `ls -1` hides them, `ls -A` shows them. Both are launcher-written logs, so both were
  already excluded from the 11,973 shipped set either way; the choice changes no result.
- **63 vs 64** — `find . -type d` counts the root `.` itself. 63 is the count of actual
  subdirectories and is the better number.
- **12,034 recursive files** — reached independently by two sessions using different
  tools, and identical. That is the figure the conclusions rest on.

For anything published, use **3,087 top-level entries and 63 subdirectories**, stated with
the method. The earlier project figure of ~2,300 is superseded; Session 0, which produced
it, has withdrawn it and named how it arose.

Excluded as player-generated, not shipped: `Logs/`, `Screenshots/`, `userdata/`,
`backup/`, `GPUCache/`, `*Inventory.txt`, `Avenrae_*`, `UI_*.ini`, `eqclient.ini`,
`*.log`, `.DownloadInfo.txt`, `.DownloadStats.txt`, `UIErrors.txt`, `_characters.ini`,
`eqlsPlayerData.ini`.

### 1.3 Method (re-runnable)

1. **Build a probe corpus of known-real item names.** The owner's `/outputfile inventory`
   dump, `Avenrae_rivervale-Inventory.txt`, is a TSV of `Location, Name, ID, Count, Slots`
   listing items the character actually holds, with the game's own numeric item IDs
   (e.g. Bladestopper = 11632). 1,375 data rows.
2. **Normalise to base item names.** Strip the `(Exaltation)` socket decoration and the
   ` +N` upgrade suffix; unique-sort. 541 raw display names to **417 base names**.
   One entry, `Name`, is an artefact: line 1107 is a second section header
   (`KeyRing / Name / ID`). Removing it gives a **true corpus of 416 item names**.
3. **Search every shipped file** for those names as fixed strings, treating binaries as
   text: `grep -l -F -a -f names` over the 11,973-file list.
4. **Parse the containers rather than skipping them.** A ~40-line PFS reader
   (`scratchpad/pfs.py`) reads the EQ container format: uint32 directory offset,
   `"PFS "` magic, a directory of (crc, offset, size) triples, per-entry zlib block
   chains, and the filename list stored under CRC `0x61580AC9`. Applied to all 2,272
   containers.
5. **Decompress and search every text-like member** (`.txt/.csv/.ini/.xml/.json/.dat`)
   inside those containers — 147 members — for the same names.
6. **Widen the corpus (added 6 Sep).** Add a second character's inventory dump
   (`Shara_rivervale-Inventory.txt`) and every `You have looted a <NAME> from` line across
   33 chat logs — 5,132 loot mentions, 537 unique names. Corpus 416 → **674**.
7. **Sweep every `dbstr` type by exact match (added 6 Sep).** Rather than sampling records
   and reading them, test all 674 known item names for exact equality against every type's
   strings. **This is what found the item table my sampling had mislabelled** (§4, IF6),
   and it is the step to run first if this is ever repeated.

### 1.4 Result

**The corpus was widened on 6 Sep** from one character to two characters plus every
loot line in 33 chat logs — 416 names to **674**, a 62% increase. This directly attacks
the "one character's inventory" gap I named as the formal weakness in §5. The result got
*stronger*, which is the outcome that needed checking:

| Corpus | Size | Absent from all shipped files |
|---|---|---|
| Avenrae inventory only (4 Sep) | 416 | 306 — **73.6%** |
| **+ Shara inventory + 33 logs (6 Sep)** | **674** | **536 — 79.5%** |

Checksum on the wide run: 138 found + 536 absent = 674. ✔

| Test | Result |
|---|---|
| Corpus item names found in at least one shipped file | **138 / 674** |
| Corpus item names found in **NO** shipped file | **536 / 674 (79.5%)** |
| Item names found inside container members | **0** |
| Item names in `eqgame.exe` | **0** (only the `Name` header artefact) |
| Item names in `EQGraphics.dll` | **0** (`Diamond` = a material/texture token) |

The 110 that *do* appear are incidental references, not table rows. Their carriers:

| Carrier | Nature | Of the 138 |
|---|---|---|
| `Resources/Achievements/AchievementComponentsClient.txt` | achievement objectives naming items | **77** |
| **`dbstr_us.txt` type 44** | **a real item-ID → item-name table (§1.7)** | **52** |
| `dbstr_us.txt` type 17 | alternate currencies — also real item records (§1.7) | **25** |
| `spells_us.txt` | spell names and descriptions colliding with item names | 22 |
| `maps/*.txt` | map annotation labels | 4 |
| `dbstr_us.txt` type 7 | lore-group names ("Cleric Epic Weapons"), 216 records | 1 |
| binaries, `eqstr_us.txt`, `Storyline/`, `ZoneNames` | generic words and collisions | ~1 each |

**To find every carrier rather than the ones I happened to sample**, I matched all 674
corpus names against every `dbstr` type by exact string equality. Only types **17, 44 and
7** carry item names at all; types 1, 3, 11 and 27 have exactly one apparent match each,
every one a name collision with an AA or ability. That sweep is what surfaced type 44.

### 1.5 What the client actually ships

| File | Content | Records |
|---|---|---|
| `spells_us.txt` (38.2 MB) | **spell** table | 73,975 |
| `dbstr_us.txt` (9.83 MB) | AA names/descs, spell descs, mercenary tiers, factions — **and the item-name table, types 44 + 17 (§1.7)** | 72,927 |
| `eqstr_us.txt` | UI format strings | 7,142 |
| `eqlsstr_us.txt` | launcher/error strings | 354 |
| `Resources/ZoneNames.txt` | zone table | — |
| `Resources/ItemDistillerDefs.txt` | **the only ITEM_ID column in the install** — `#ITEM_ID^DISTILLER_RANK^`, no names | **22** |

`Resources/ItemDistillerDefs.txt` is the closest thing to item data in the entire
install: 22 rows, IDs 47001–47021 plus 52023, ranks only, no names. It is a distiller
rank lookup, not a table of items.

### 1.6 Item-adjacent counts — LABELLED, and NOT denominators

Publishable, but none of these is an item count. Stated explicitly so none is mistaken
for one later:

- **625** `IT*.eqg` files — item **appearance models**. Many items share a model; many
  items have none. This is not an item count and must not be used as one.
- **216** `dbstr` type-7 lore/item-group names.
- **79** `dbstr` type-17 alternate currencies.
- **499** `Resources/Layers/*_IT.txt` armour layer definitions — texture layering, not items.
- **674** base item names from **two characters plus 33 chat logs** (was 416 from one
  character). A floor from one account's play, not a table, and not a client fact.
- **1,158** the client's own item-name surface (§1.7) — real, measured, and covering only
  **7.0%** of items actually held. It is a spell-support table, not the population.

### 1.7 THE PARTIAL ITEM TABLE — `dbstr_us.txt` types 44 and 17

This is the section the first version of this report should have had.

**`dbstr_us.txt` type 44 is an item-ID → item-name table.** 1,126 records:

- ids 1–9 are resist types (`magic`, `fire`, `cold`, `poison`, …) — the nine records my
  original four-record sample landed on, which is why I called the whole table "resist
  types";
- **ids ≥ 1000 are 1,117 item records / 1,081 unique item names**, running to id 159,996.

**The IDs are real item IDs, not an internal index.** Verified by intersecting them with
the owner's inventory IDs: **17 IDs appear in both, every one with a matching name.**

| Item ID | type 44 name | inventory name |
|---|---|---|
| 10012 | Black Pearl | Black Pearl |
| 10031 | Fire Opal | Fire Opal |
| 10037 | Diamond | Diamond |
| 10307 | Fire Beetle Eye | Fire Beetle Eye |
| 11566 | Staff of Elemental Mastery: Fire | Staff of Elemental Mastery: Fire +4 |

**`dbstr_us.txt` type 17** adds 79 alternate currencies (Doubloon, Orum, the Mote of
… Potential ladder, Wind Runes). These are items with IDs in the same space.

**Combined shipped item-name surface: 1,158 unique names** (1,081 ∪ 79, deduplicated).

#### What it is, and why it is not the population

206 of the 1,081 type-44 names carry a `Summoned:` prefix. The rest are dominated by
gems, spell reagents, and focus items. **This is the set of items the client must be able
to name without the server** — because a spell summons them, consumes them, or checks for
them. It is a spell-support table that happens to contain items.

| Measure | Value |
|---|---|
| Client item-name surface | **1,158** |
| Real held/looted items covered | **47 of 674** |
| **Coverage** | **7.0%** |
| **Absent** | **93.0%** |

**A table that omits 93% of the items a single account demonstrably holds is not the
item population, and 1,158 must not be published as a denominator.** It is a real,
measured, publishable count of *a named thing* — the client's local item-name table — and
that is the only claim it supports.

### 1.8 Can the maximum item ID bound the table? No — the ID space is sparse

The Director raised this as an explicit hypothesis: if item IDs are **dense**, the highest
observed ID approximates the table size; if **sparse**, it is only a weak ceiling. The 416
IDs in the inventory dump answer it.

| Measure | Value |
|---|---|
| Unique numeric item IDs | 416 |
| Minimum / maximum | 1,069 / 177,946 |
| Span | 176,878 |
| **Occupancy of span** | **0.235%** |

Decile histogram of the ID space (counts per tenth, 0 → 177,946):

```
      0- 17794 : 253   ####################
  17794- 35589 : 116   #########
  35589- 53383 :   0
  53383- 71178 :   7
  71178- 88973 :   0
  88973-106767 :   0
 106767-124562 :   0
 124562-142356 :   0
 142356-160151 :   1
 160151-177946 :  38   ###
```

**The hypothesis is refuted: the IDs are sparse and strongly clustered, with five of ten
deciles completely empty.** Max-ID therefore yields only the ceiling "at most ~177,946
items", which is true and useless. The clustering into low and high blocks is consistent
with IDs allocated in ranges by content era, which is a further reason the span cannot be
read as a population.

Reported as the Director asked: it converts the guess into a refutation rather than a
bound, and the refutation is the useful half. **Max item ID must not be published as an
estimate of table size.**

---

## 2. VERIFICATION CONDITIONS — as specified in advance

> **REVISED 2026-09-06.** My previous version recorded all four as UNEVALUABLE, on the
> grounds that no client item table existed. **A client item table does exist** (§1.7), so
> all four are now evaluable and are evaluated below. UNEVALUABLE was the right verdict
> for the object I believed existed; it was the wrong verdict about the world.

The client table is `dbstr` types 44 + 17: **1,158 named items keyed by real item IDs.**
All four conditions are measured against that object, and every figure carries a checksum.

| # | Condition | Verdict | Measurement |
|---|---|---|---|
| V1 | The 587-name union must be a SUBSET of the client table | **FAIL** | 12 of 581 union names present; **569 absent** (12+569 = 581 ✔) |
| V2 | All 146 crosscheck names must appear in it | **FAIL** | 10 of 146 present; **136 absent** (10+136 = 146 ✔) |
| V3 | The total must sit at or above 587 | **PASS** | 1,158 ≥ 587 |
| V4 | The total must be consistent with the ≥1,470 floor | **FAIL** | 1,158 < 1,470 |

### THE VERDICTS ARE ABOUT THE CLIENT, NOT ABOUT THE PROJECT'S DATA

This is the single most misreadable result in the report, so it is stated before the
detail:

**V1 and V2 fail because the client table is small and special-purpose, not because the
project's item names are wrong.** The conditions were written on the assumption that the
client table would be the full item population and could therefore act as ground truth.
It is a **7%-coverage spell-support table** (§1.7). Measuring the project's 581 names
against it is measuring them against the wrong yardstick — and the yardstick is what
fails.

The composition of the passes proves it. The 10 crosscheck names that *are* present:

`bloodstone, cat's eye agate, fire beetle eye, ivory, malachite, pearl, ration,
throwing knife, topaz, water flask`

**Every one is a gem, a reagent or a vendor staple** — exactly the items a spell needs to
name locally. Not one is a piece of equipment. The table is not failing to contain the
project's items by accident; it was never built to contain them.

**Nothing here contradicts any name the project publishes.** A name absent from a table
that omits 93% of a real inventory has not been impeached by that absence.

**And V3's PASS should be given no weight.** 1,158 ≥ 587 is arithmetically true and
means nothing: the condition wanted a total item population above the known floor, and
1,158 is a count of a different thing. **A condition can pass for the wrong reason, and
reporting the PASS without saying so would be the most dishonest line in this document.**

### 2.1 The union, measured against shipped client data (a substitute object)

Reconstructed from the sources the audit names:

| Set | Source | Count |
|---|---|---|
| A | `assets/index-data.json`, entries with `kind == "item"`, unique `n` | **435** |
| B\A | `audit/CROSSCHECK-ITEMS.txt` | **146** |
| A ∩ (B\A) | — | 0 (disjoint by construction) |
| **Union** | | **581** |

**I could not reproduce 587; I get 581.** The audit read `window.__IX__` on 2026-08-31
and recorded A = 441; today's `index-data.json` yields A = 435. The six-name difference
is index drift between 31 Aug and 4 Sep, or a difference between the rendered
`window.__IX__` and the committed JSON. I have not resolved which, and I am not going to
call my 581 a reproduction of their 587.

Matching was case-insensitive, with backtick/apostrophe variants generated for every
name (the client writes ``Kelin`s``, the audit writes `Kelin's`) — without that, 15
punctuated names would have produced false negatives.

> **49 of 581 union names (8.4%) appear anywhere in shipped client data. 532 do not.**

And per *read the match, never the count* — the 49 are not table rows. The generic ones
are ordinary words (`arrow`, `axe`, `ivory`, `pearl`, `topaz`, `flail`). Every
distinctive one traces to an incidental carrier:

| Name | Carrier | What it actually is |
|---|---|---|
| dagger of marnek | `Help/exaltations.html` | an example item in the in-game help page |
| key of swords | `Resources/Achievements/AchievementComponentsClient.txt` | an achievement objective |
| earthshaker | achievements + `spells_us.txt` | also a spell name |
| prismatic shield | `spells_us.txt` | a spell |
| scalp of the ghoul lord | `spells_us.txt` | a spell/quest reference |
| slaver's lash | `spells_us.txt` | a spell reference |

This is an independent corpus — chosen without reference to the owner's inventory — and
it reproduces the §1.4 result. That is the point of running it.

### 2.2 V2 — the 146 crosscheck names, against two named objects

**Object 1 — shipped client data:** 19 of 146 present, 127 absent. All 19 are the
incidental/generic carriers above. This measures the client, not the project.

**Object 2 — the owner's inventory corpus (416 names):** **18 of the 146 are items the
owner's character actually holds.**

That second number is the useful one, and it is worth more than the check it substitutes
for. The 146 are items EQLBase verified that eqlsource's Index lacks. Eighteen of them
are independently corroborated as real, currently-obtainable items by a third source that
is neither EQLBase nor eqlsource:

Each one is shown with the inventory row that produced it and the game's own item ID, so
the match can be inspected rather than taken on the count (all 18 resolve to a real row;
there are no unresolved matches):

| Crosscheck name | Inventory row | Item ID |
|---|---|---|
| backpack | Backpack | 17005 |
| bracelet of distortion | Bracelet of Distortion +1 | 12803 |
| ethereal mist vambraces | Ethereal Mist Vambraces +6 | 4883 |
| fire beetle eye | Fire Beetle Eye | 10307 |
| ghoulbane | Ghoulbane +6 | 5403 |
| guise of the deceiver | Guise of the Deceiver +4 | 2469 |
| imbrued platemail vambraces | Imbrued Platemail Vambraces +4 | 4863 |
| midnight clad wristbands | Midnight Clad Wristbands +5 | 177797 |
| prismatic shield | Prismatic Shield +5 | 9405 |
| ration | Ration | 13007 |
| rod of understanding | Rod of Understanding +1 | 177940 |
| scalp of the ghoul lord | Scalp of the Ghoul Lord +2 | 26997 |
| shrieking ahlspiess | Shrieking Ahlspiess +4 | 7507 |
| umbral platemail vambraces | Umbral Platemail Vambraces +4 | 4843 |
| valorium vambraces | Valorium Vambraces +6 | 4853 |
| vermiculated armplates | Vermiculated Armplates +4 | 3803 |
| wand of swiftness | Wand of Swiftness +4 | 12506 |
| water flask | Water Flask | 13006 |

The ` +N` suffixes are upgrade decoration on the owner's copies, not different items; the
base name and the item ID are the identity. Four of the eighteen (`prismatic shield`,
`scalp of the ghoul lord`, `backpack`, `fire beetle eye`) also appear in shipped client
data — but as spell names and generic tokens, which is why §2.2 Object 1 must not be read
as corroboration.

**What this does NOT say:** the other 128 are not thereby doubtful. One character's
inventory is not a census — absence from it is uninformative. This is 18 confirmations
and 128 no-informations, not 18 confirmations and 128 doubts.

---

## 3. INPUT GAPS — now CLOSED

My first report listed three artefacts I could not find and recorded them as input gaps
rather than absences. **All three exist.** They are in a peer repository I had no reason
to know about:

    repo    C:\Users\Lindsey\Desktop\EQLS Director\peers\Resanddev
    branch  origin/claude/eqlsource-audit-redesign-2qrhpd
            audit/CROSSCHECK-ITEMS.txt
            audit/AUDIT-EVIDENCE.md   (the 587 union and the >=1,470 floor, with derivations)

The Director supplied the addresses and named the omission as its own. Recorded here
because the discipline is the point: **reporting these as "not found" rather than "not
there" is why they were recoverable.** Had my first report said the crosscheck file did
not exist, the correction would have looked like a contradiction instead of an address.

Note on retrieval: the files are on the branch but not in that repo's working tree, which
is checked out at an earlier state. I read them with `git show <ref>:<path>`, which reads
git objects and writes nothing — the tree was not checked out, modified, or touched. It
is the Blind Auditor's repository and read-only to me.

### 3.1 The 1,470 floor, now that I can see its derivation

`AUDIT-EVIDENCE.md` describes 1,470 as derived from "Gnoll Guard's defect arithmetic" and
the audit itself prefers 587 as "a better floor — not larger, but built from named items
and checkable one at a time." V4 asked for consistency with the 1,470 floor. There is no
total to be consistent with, so V4 is UNEVALUABLE; but the audit's own stated preference
for the 587 construction over the 1,470 one is worth carrying forward.

---

## 4. INSTRUMENT FAULTS — reported separately from findings, as required

**IF1 — My first dbstr conclusion was wrong.** My initial pass sampled four records per
`dbstr` type and I recorded "no item names observed in any sampled type". That was an
instrument fault: the sample was too shallow. The full-corpus scan found genuine item
names in types 7 and 17. The corrected statement is in §1.4. The earlier claim was
retracted before any number depended on it.

**IF2 — A badly chosen probe pattern.** My first three-name probe used "Rune of
Kildrukaun", which hit `spells_us.txt`. That is a **spell** (spell id 60362), not an
item. The hit was my pattern error, not evidence of an item table.

**IF3 — A PFS pairing bug, found and fixed.** My first container scan paired the filename
list with directory entries in directory order. The PFS filename list is in *data offset*
order. Fixed by sorting entries by offset before pairing, done before any member name was
reported. The extension histogram is an aggregate and was unaffected.

**IF6 — I CALLED A 1,126-RECORD ITEM TABLE "RESIST TYPES" FROM A FOUR-RECORD SAMPLE.
This is IF1 again, and this time it reached a published headline and stood for two days.**

`dbstr_us.txt` type 44 has 1,126 records. My original pass printed the first four —
`magic`, `fire`, `cold`, `poison` — and I recorded the type as "resist types". Those four
are ids 1–4. **Ids 1–9 are the only resist types in it. Ids ≥1000 are 1,117 item records
keyed by real item IDs**, running to id 159,996 (§1.7).

On that basis I published *"the client does not ship an item table"* — flatly, with no
qualifier. It was wrong. The client ships 1,158 named items.

**Why it survived when IF1 did not.** IF1 was caught because a full-corpus scan contradicted
it. This one was not, because my full-corpus scan *did* hit type 44 — 52 matches — and I
attributed those hits to the label I had already assigned the type. **A mislabel does not
announce itself on re-run; it silently absorbs the evidence that should have refuted it.**

**What actually caught it:** widening the corpus changed the *shape* of the results, not
just the totals. Type 44 jumped in the carrier ranking, I asked why a "resist type" table
was carrying dozens of item names, and looked at ids other than the first four.

**The general fix, now applied:** the type-by-type sweep in §1.4 tests *every* type by
exact match against known item names, rather than sampling records and reading them.
**Never characterise a table from its first N records — its first records are the most
likely to be special.** Low IDs are exactly where enumerations, defaults and sentinels
live, which is what made ids 1–9 so misleading.

**Direction of the error, stated plainly:** this one made my headline *stronger* and
cleaner than the truth. That is the second time in this report an error has failed in the
direction of my own thesis (see IF4), and both times the thesis was the thing I was least
inclined to re-examine.

**IF5 — A corpus figure moved between reports: 417 to 416. Here is why.**

My first report said 417 base item names; this one says 416. The change is a single
removal, and it is deliberate: `Name` is not an item. The inventory dump has a **second
section header** at line 1107 (`KeyRing / Name / ID`), and my extraction skipped only
line 1, so the word `Name` entered the corpus as if it were an item.

I found it while checking why `Name` matched 10,307 times across shipped files — a count
that made no sense for an item and would not have been noticed if only the total had been
compared. It is also the sole reason `eqgame.exe` and `EQGraphics.dll` showed any "hit"
at all; with it removed, both are clean.

**417 was wrong, 416 is right, and the correction shrinks my own headline** (the unmatched
count went from a possible 307 to 306). Recorded here rather than silently carried,
because a figure that moves between reports without a stated reason is exactly what this
project chases hardest. No other number in the first report changed.

**IF4 — Two set-comparison faults in the union test, caught before reporting.** Both were
caught only because the arithmetic was checked rather than the output trusted, which is
the entire content of *read the match, never the count*:

- `comm` was fed files sorted under different collations, producing "49 found" alongside
  "581 not found" — 630 outcomes from a 581-name set. An impossible total is the only
  reason this surfaced.
- Python wrote the union file with CRLF line endings; every comparison then failed
  silently and reported **"0 of 581 found"**, which is a clean, plausible, completely
  wrong number that would have *strengthened* my headline. It is the most dangerous
  error in this report's history: it failed in the direction of my thesis.

Both fixed (`LC_ALL=C`, `tr -d '\r'`), and every union figure in §2.1 carries a checksum
(`found + missing = 581`). **A result that agrees with your expectation deserves the
arithmetic check more than one that does not.**

---

## 5. BOUNDS ON THIS RESULT

What would still overturn the headline, stated honestly:

- **Encoding.** The scan matches ASCII/latin-1 byte sequences. Item names stored UTF-16,
  or with per-record obfuscation or compression, would not match. I have no evidence of
  such storage, and the client's other tables are all plain `^`-delimited ASCII.
- **Non-text binary members.** `.mod`, `.wld`, `.ter`, `.dds` members were counted and
  typed but not individually decoded. They are geometry and texture formats. An item
  table hidden in one is not ruled out by decoding, only by implausibility.
- ~~**The probe corpus is one character's inventory.**~~ **CLOSED 6 Sep.** This was the
  formal gap I named, and it has been attacked directly: the corpus is now **674 names
  from two characters plus 5,132 loot events across 33 chat logs**. The absence rate rose
  from 73.6% to **79.5%**, so widening the corpus strengthened rather than weakened the
  result. A residual version survives — all of it is still *one account's* play — but it
  is no longer one character, and the failure mode where the client table happens to hold
  only unseen items is now excluded by the type-44 enumeration (§1.7), which lists what the
  table actually contains rather than inferring it.
- **Server-side data is out of scope** and is where the evidence says the answer lives.

The containers were the flagged unknown — "an afternoon or a wall". **They were an
afternoon: ~40 lines of Python, 2,272 of 2,272 parsed, zero failures.** That question is
now closed, and the parser is reusable at `scratchpad/pfs.py`.

---

## 6. RECOMMENDATION

The denominator is not obtainable from the client install. Anyone re-attempting this
should not re-run the client sweep; it is done and it is negative. Remaining routes:

1. **Server-sourced.** Item data arrives over the wire; a saved item-link or bazaar
   corpus would be a real table.
2. **Accumulated inventory dumps.** The project's existing method, which yields a growing
   floor (currently 257 published; 416 base names available from one dump) — a floor, and
   honest as one, but never a denominator.
3. **Publish coverage against a named, bounded population** (e.g. "of the 442 items with
   pages") rather than against an unmeasured universal denominator.

Until then, published coverage fractions should not carry a client-derived denominator,
because there is no such thing.

### 6.1 One thing this work produced that was not asked for

**18 of the 146 crosscheck names are corroborated as real items by the owner's own
inventory** (§2.2). Those are EQLBase-verified items the eqlsource Index lacks, now
confirmed by a source independent of both. They are directly actionable as Index
additions, and the confirmation cost nothing beyond a set intersection.

The remaining 128 are **no-information, not doubt** — one character's inventory cannot
witness against an item. That asymmetry must survive into whatever uses this list.

### 6.2 Numbers in this report that must never be quoted as a denominator

Collected in one place because each is the right shape to be misread as one:

| Number | What it actually is |
|---|---|
| 625 | item **appearance model** files — many items share one, many have none |
| 177,946 | the **maximum observed item ID** — the ID space is 0.235% occupied (§1.7) |
| 416 / 542 | names / id-pairs from **one character's** inventory — a floor from one account |
| 216 / 79 | dbstr lore-**group** names / alternate **currencies** — neither is an item |
| 581 | a **reconstruction** of the project's own union, not a client measurement |
| **1,158** | the client's real item-name table — but **7.0% coverage** of items actually held. The most dangerous number here, because it is real, measured, client-derived, and the right order of magnitude to look like an answer |
