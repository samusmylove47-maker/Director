# Client Item Table Count — EverQuest Legends

**Session:** EQLS Research Session F [d1e38f]
**Branch:** `client-item-table-count`
**File:** `CLIENT-ITEM-TABLE-COUNT.md`
**Date:** 2026-09-04
**Status:** COMPLETE — bounded negative result, corroborated by two independent corpora.
**Peer inputs:** all three previously-missing artefacts located and used (§3).

---

## HEADLINE

**The EverQuest Legends client does not ship an item table. The requested count cannot
be produced from the client, because the thing to be counted is not there.**

This is a measured negative with a stated bound, not a failure to look. Every surface in
the install was searched, including all 2,272 proprietary containers, which were parsed
rather than skipped. The strongest single number:

> **306 of 416 item names (73.6%) that the owner's own character demonstrably possesses
> appear in NO file shipped with the client** — across all 11,973 shipped files and all
> 83,137 members inside the containers.

Items whose names the client has never heard of are nonetheless in the player's
inventory. That is only possible if item data is server-sent. This matches stock
EverQuest architecture.

**Corroborated by a second, independent corpus:** of the project's own 581-name union
(reconstructed; see §2.1 for why it is 581 and not 587), **532 appear nowhere in shipped
client data either** — and the 49 that do are spell names, achievement objectives and
help-page examples, not table rows. That corpus was chosen without reference to the
owner's inventory, so the two results are not the same measurement twice.

**Consequence for the project: the denominator cannot come from the client.** The
587–3,700 range is not collapsed by this work. It is, however, now known that this
method cannot collapse it, which closes off the approach rather than leaving it open.

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

Nothing under the install was written, moved, renamed or deleted. All work was on copies
in a session scratch directory, made with `cp -p`. Containers were opened read-only
(binary read mode). Verifiable: every file in the install retains its original mtime.

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
| Launcher patch check (`.DownloadInfo.txt`, last entry) | 2026-09-03 19:26 — *"All files are up to date"* |

The install was fully patched as of 2026-09-03.

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
   inside those containers — 147 members — for the same 416 names.

### 1.4 Result

| Test | Result |
|---|---|
| Corpus item names found in at least one shipped file | **110 / 416** |
| Corpus item names found in **NO** shipped file | **306 / 416 (73.6%)** |
| Item names found inside container members | **0** |
| Item names in `eqgame.exe` | **0** (only the `Name` header artefact) |
| Item names in `EQGraphics.dll` | **0** (`Diamond` = a material/texture token) |

The 110 that *do* appear are incidental references, not table rows. Their carriers:

| Carrier | Nature | Count |
|---|---|---|
| `Resources/Achievements/AchievementComponentsClient.txt` | achievement objectives naming items | 71 corpus names |
| `dbstr_us.txt` type 7 | lore-group / item-group names ("Cleric Epic Weapons") | 216 records total |
| `dbstr_us.txt` type 17 | alternate currency names (Doubloon, Orum, Wind Rune Ozah) | 79 records total |
| `dbstr_us.txt` type 27 | AA ability names colliding with item names ("Cloak of Scales") | — |
| `spells_us.txt` | spell descriptions mentioning items | — |
| binaries | generic English words (`Diamond`, `Ruby`, `Backpack`) | false positives |

### 1.5 What the client actually ships

| File | Content | Records |
|---|---|---|
| `spells_us.txt` (38.2 MB) | **spell** table | 73,975 |
| `dbstr_us.txt` (9.83 MB) | AA names/descs, spell descs, mercenary tiers, factions, currencies | 72,927 |
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
- **416** base item names / **542** unique id–name pairs from **one character's**
  inventory. A floor from one account, not a table, and not a client fact.

### 1.7 Can the maximum item ID bound the table? No — the ID space is sparse

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

All four were specified before the work, against a **client item table**. That object
does not exist, so three of them have no referent.

**UNEVALUABLE is a third verdict, not a bad version of PASS or FAIL.** A condition whose
subject does not exist has not been failed — it cannot be reached. Recording it as FAILED
would assert something about the project's data that this work does not support. (This
distinction was corrected by the Director after my first draft used "fails at the
premise"; the correction is right and I have adopted it.)

| # | Condition | Verdict |
|---|---|---|
| V1 | The 587-name union must be a SUBSET of the client table | **UNEVALUABLE** — no client table exists to be a superset. Measured against a substitute object in §2.1, labelled as such. |
| V2 | All 146 names in `CROSSCHECK-ITEMS.txt` must appear in it | **UNEVALUABLE as written**; measured against two named substitute objects in §2.2. |
| V3 | The total must sit at or above 587 | **UNEVALUABLE** — there is no total. |
| V4 | The total must be consistent with the >=1,470 floor | **UNEVALUABLE** — same. |

None of this contradicts any name the project publishes. The client is not a witness
either way.

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
- **The probe corpus is one character's inventory.** 416 names, weighted toward what one
  player owns. A client table containing *only* items this character has never held would
  produce exactly the observed result. I consider this very unlikely — 306 misses out of
  416 is not a sampling artefact — but it is the formal gap.
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
