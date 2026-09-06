# Preservation copy — Session F's client item-table extraction

**This is a COPY, not the original, taken 4 September 2026 by the Director.**

The original lives in an untracked local repository with **no remote configured**:

    C:\Users\Lindsey\Desktop\EQLSDeep    branch client-item-table-count

Four commits, one directory, one machine, no backup. Session F reported that
state correctly — **"NOT PUSHED — no remote configured. ORDERED, not DONE"** —
rather than describing the work as delivered. This copy exists because a parser
written so nobody repeats it was one deleted folder away from being repeated.

**It does not replace a proper home for that repository, which is still the
owner's to authorise.**

## What is here, and how to check it against the source

**Pinned to source commit `3df1fb4e5c84`. THE SIXTH RE-PIN, AND THE THIRD TAKEN AT REST.**

**WHY A FIFTH PIN IS NOT A RETURN TO CHASING, WHICH IS THE HABIT PIN-AT-REST REPLACED.**
Session F explicitly recommended *not* re-pinning on its account — `b45ba7f` is **weaker, not
false** — and warned that a pin taken to chase a commit is the exact practice we had just
abandoned. **The discriminator that made this one worth taking, and it is a rule rather than a
judgement call:**

> **RE-PIN AT REST WHEN THE SOURCE HAS MATERIALLY CHANGED — NOT WHEN IT HAS SIMPLY MOVED.**
> *Chasing is pinning because a commit exists. This is pinning because the copy would otherwise
> preserve a superseded artefact, and an archive outlives the repository it copies.*

`b45ba7f` carried a structure diagram reading `slot | SPA | base1 | base2 | max | calc`, with a
paragraph beneath it saying the last four were named by convention rather than by evidence.
**`5c95017` replaces the diagram itself with `slot | SPA | ? | ? | ? | ?` and marks the four
explicitly NOT ESTABLISHED.** *The prose caveat was already there and was not enough.* **A
reader building a parser copies the diagram and never reaches the paragraph** — so the archive
would have preserved, permanently, the one artefact most likely to be acted on and least likely
to carry its own caveat.

### THE TWO PREVIOUS PINS CARRIED A FALSE VERDICT. THIS ONE CARRIES THE CORRECTION.

**Pins four and five — `b45ba7f` and `5c95017` — state that the client is UNEVALUABLE on the
site's zone difficulty tiers, and that it *"names the axis and ships none of its values."*
THAT IS WRONG, AND IT IS WRONG IN THE DIRECTION OF UNDERSTATING WHAT THE CLIENT SUPPORTS.**
Session F overturned it at `cb0692c`, reopening after it had stopped, and refined it at
`3df1fb4`. **This pin carries the corrected text; the note is kept because those two pins are
in this file's own history and a reader tracing them needs to know.**

**The client ships all five tier values and confirms the site exactly:**

    eqstr_us.txt   15519  0 (Normal)
                   15520  1 (Awakened)
                   15521  2 (Adaptive)
                   15522  3 (Fused)
                   15571  4 (Refined)     <- 49 ids from the block

**Independently re-derived by the Director on a different path** — an unconstrained regex for
`<id> <digit> (<Name>)` over all 7,144 lines, assuming no ids — **returning exactly those five
and nothing else. No `5 (...)` exists, which is what makes "D4 is the maximum" a checkable
claim rather than only "five tiers exist".** *Awakened, Adaptive, Fused and Refined each occur
exactly once in the whole string table.*

> **THIS IS THE FIRST TIME IN THIS WORK THE CLIENT CORROBORATES A PUBLISHED CLAIM** rather than
> contradicting it or being silent. **The client is a second independent witness for the tier
> ladder** — not for the scaling figures, which remain EQL Tools' and are genuinely absent.

**THE ARCHIVE IS NOT REWRITTEN TO HIDE ANY OF THIS.** *Nothing above has been deleted; the
superseded verdict is named, dated and attributed.*

**AND F KEPT THE WRONG REASONING RATHER THAN DELETING IT.** §5.2b of the pinned document is
headed *"The original reasoning, kept because it was wrong in an instructive way"*, states the
false conclusion in full, and then says why it failed: **the comboboxes really are
runtime-populated — but the values live in the string table, which had not been swept for
them.** *An empty control does not mean absent data; it means the data is somewhere else.*

*A grep for the false sentence still finds it in this archive. It is inside a section that
exists to preserve it.* **That is the same discipline this file applies to the item-table
retraction: show the retraction rather than replace it.**

**THE THIRD PIN-AT-REST CROSSED ANYWAY.** F named `cb0692c` as the commit to take and had
committed `3df1fb4` by the time the pin was taken — the fourth crossing in two days. **The
copy is of HEAD as verified at pin time, not of the commit named in the request**, because the
verification is what the hashes below attest and a named commit is a claim about a moment that
had already passed.

**AND THE BOUND ON PIN-AT-REST, WHICH THIS EPISODE ESTABLISHED AND WHICH NO FASTER ARCHIVER
FIXES:** *pins four and five were both taken correctly, at rest, with clean trees and verified
byte-identity, and both preserved a falsehood.* **PIN-AT-REST PROTECTS AGAINST COPYING A
HALF-FINISHED STATE. IT CANNOT PROTECT AGAINST COPYING A FINISHED AND MISTAKEN ONE.** *Only a
note beside the pin can — and only if the note is kept when the pin moves, which is why it is
still here.*

**Original pin-at-rest note, which stands:** The archive chased this repository three times in two days — `141eef7`, `e42fadc`,
`b7a0a81` — every one of them while Session F was still working in it.

> **ARCHIVING A LIVE REPOSITORY IS CHASING A MOVING TARGET, AND EVERY LAG IS A WINDOW IN
> WHICH THE ARCHIVE STATES SOMETHING ITS SOURCE HAS RETRACTED.** That window was open twice.
> **The fix is not a faster archiver; it is a remote, which is the owner's to authorise.**

**WHAT CHANGED THE METHOD: PIN AT REST, NOT ON A CLOCK.** Session F now works to a stop, and
the archive is taken when its working tree is quiet. **This pin was taken with F stopped and
`git status` empty**, so for the first time the copy and the source cannot have diverged
mid-copy. *That is the same fault as recording hashes "verified identical at copy time" — a
snapshot must name the commit it snapshots, never the clock.*

    00625edae9df  CLIENT-ITEM-TABLE-COUNT.md
    208e4f5632e6  method/dupcheck.py
    2d58106edc01  method/slots.py
    30b9c1e1d710  method/lockout.py
    323073f7f561  method/join.py
    3947d381afbe  method/pfs.py
    3ca0ee427102  method/scanall.py
    45172814c604  method/deep.py
    50f1333cb997  method/agree.py
    00625edae9df  CLIENT-ITEM-TABLE-COUNT.md
    208e4f5632e6  method/dupcheck.py
    2d58106edc01  method/slots.py
    30b9c1e1d710  method/lockout.py
    323073f7f561  method/join.py
    3947d381afbe  method/pfs.py
    3ca0ee427102  method/scanall.py
    45172814c604  method/deep.py
    50f1333cb997  method/agree.py
    82464b135e79  method/spa_harness.py
    00625edae9df  CLIENT-ITEM-TABLE-COUNT.md
    208e4f5632e6  method/dupcheck.py
    2d58106edc01  method/slots.py
    30b9c1e1d710  method/lockout.py
    323073f7f561  method/join.py
    3947d381afbe  method/pfs.py
    3ca0ee427102  method/scanall.py
    45172814c604  method/deep.py
    50f1333cb997  method/agree.py
    82464b135e79  method/spa_harness.py
    854e4c4b7398  CLIENT-DEEP-RESEARCH.md
    b0f3c7e1ba3e  method/total.py
    bee41c1d3a65  method/pattern.py
    c64b807c1ae6  method/spellparse.py
    e1a9c2ae0c47  method/checktext.py
    edcaa5546ef0  method/allcols.py
    f389fa1a2a94  method/fields.py

sha256, first twelve, of the bytes as stored here, verified against the source at pin time.
**Verified at this pin: all 17 tracked files byte-identical to the source, source working
tree clean, source HEAD `3df1fb4`.**

**A SECOND CORRECTION LANDED BETWEEN PINS AND IS NOT SHOWN BELOW, BECAUSE IT NEVER REACHED
THIS ARCHIVE — but it reached further than the archive did.** At `019b4b7` Session F
published a structure for column 172 of `spells_us.txt` as *1 + 5n pipe fields, a slot count
followed by five fields per slot*; at `e02fb99` it retracted that. **The true format is
`slot|SPA|base1|base2|max|calc`, six fields always, slots separated by `$`, and the leading
number is an index rather than a count** — validated whole-file at 275,022 slots, none of
them the wrong width. *The documents copied here already carry the corrected version.*

**The reason it is recorded at all: the Director had already relayed the wrong structure to
Session C as its next morning's first task, and retracted it the same night.** F's ground for
demanding that was *a wrong structure is worse than no structure, because it is actionable*.
**The conclusion it supported never changed** — the client ships computable spell effects for
all 73,975 spells — **only the recipe, which is the half a downstream session codes against.**

`.gitattributes` marks this directory `-text` so git normalisation cannot rewrite them.

## The source commits, in order

    f7bd04a  04 Sep 10:42  Pre-register population decision and verification conditions before counting
    e5e8ee5  04 Sep 10:53  Publish bounded negative: client ships no item table
    a94c5eb  04 Sep 11:00  Close input gaps; evaluate union and V2 against named substitute objects
    9da35e0  04 Sep 11:02  Show the 18 corroborated names with item IDs; explain the 417->416 change
    141eef7  04 Sep 11:04  Resolve the 3085/3087 and 63/64 enumeration differences by naming methods
    e42fadc  06 Sep 01:23  MATERIAL CORRECTION: client does ship a partial item table (1,158 items)
    b7a0a81  06 Sep 01:30  Deep research partial: client contradicts published spell data
    019b4b7  06 Sep 01:32  Full 173-column sweep of spells_us.txt: effect slots, recourse FK
    721679d  06 Sep 01:35  Priority 4: client ships the lockout schema and rules, not the durations
    e02fb99  06 Sep 01:38  CORRECTION: col 172 structure was wrong - $ separates slots, not 1+5n
    b45ba7f  06 Sep 01:42  Priority 3: two different five-tier difficulty scales; do not conflate
    5c95017  06 Sep 01:59  Write fields 2-5 of the effect slot as unknowns, not as guessed names
    cb0692c  06 Sep 02:05  CORRECTION: the client DOES ship all five difficulty tiers
    3df1fb4  06 Sep 02:09  Separate 'five tiers exist' from 'D4 is the maximum'; both now measured

## The finding — CORRECTED 6 September, and the first version is shown because it was wrong

**WHAT THIS ARCHIVE SAID UNTIL 6 SEPTEMBER, AND IT IS RETRACTED:**

> ~~306 of 416 item names the owner's character demonstrably holds appear in no file
> shipped with the client... The client is not a witness either way. It contradicts
> nothing this project publishes; it simply cannot testify.~~

**THE CLIENT DOES SHIP AN ITEM TABLE.** `dbstr_us.txt` type 44 carries 1,117 item records
and 1,081 unique names running to id 159,996; type 17 carries 79 alternate currencies.
**Deduplicated: 1,158 named items, KEYED BY REAL ITEM IDS** — verified by intersecting with
the owner's own inventory dump, 17 ids present in both with every name matching
(`10307 = Fire Beetle Eye`).

**And the absence figure was superseded upward, not down.** Corpus widened from one
character's inventory to two characters plus 5,132 loot events across 33 chat logs — 416
names to 674 — and absence **rose from 73.6% to 79.5%: 536 of 674.**

**The four pre-registered conditions became evaluable and three FAIL:** V1 12 of 581
present, V2 10 of 146, V4 1,158 below the 1,470 floor. **V3 passes at 1,158 ≥ 587 and
Session F ruled that its pass be given NO WEIGHT — it counts a different thing.**

> **READ THE FAILURES AS FACTS ABOUT THE CLIENT, NOT ABOUT THIS PROJECT'S DATA.** *A name
> absent from a table that omits 93% of a real inventory has not been impeached.* The
> table covers 47 of 674 items the owner actually holds — 7.0% — and its composition says
> what it is: every crosscheck name in it is a gem, a reagent or a vendor staple, not one a
> piece of equipment, and 206 of the 1,081 carry a `Summoned:` prefix. **It is a
> spell-support table that happens to contain items.**

**THE PROJECT'S CONCLUSION IS UNCHANGED AND BETTER FOUNDED: 1,158 CANNOT BE THE
DENOMINATOR.** The route is closed by an **enumeration** now rather than by an absence.
**1,158 heads the do-not-quote list, above the 625 appearance models** — real, measured,
client-derived, and exactly the right order of magnitude to look like the answer.

**HOW THE FIRST VERSION SURVIVED, because it is the transferable part.** F characterised a
1,126-record table from its first four records — ids 1-4 are magic, fire, cold and poison,
so it labelled the whole type *resist types*. Its later full-corpus scan hit that table 52
times and filed every hit under the label already assigned. **A mislabel does not announce
itself on re-run; it silently absorbs the evidence that should refute it.** A wrong
negative is refuted by more data; a wrong name is fed by it.

**AND WHY THIS SECTION SHOWS ITS OWN RETRACTION.** Session F flagged that this archive was
pinned past its correction, and its reason is the one that matters: **an archive is exactly
where a retracted claim does the most damage, because it is trusted and nobody re-reads
it.** Silently replacing the text would have left no trace that the archive had ever been
wrong. It was wrong for eight hours and the record now says so.

`method/pfs.py` is the reusable half and is unaffected by any of this. It reads the PFS
container format the EverQuest client ships (uint32 directory offset, `PFS ` magic,
crc/offset/size triples, zlib block chains, filename list under CRC `0x61580AC9`), 2,272 of
2,272 with zero failures. **Nobody here needs to derive that format again.**
