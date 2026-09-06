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

**Pinned to source commit `b7a0a8189437`. THIS IS THE THIRD RE-PIN.** The archive has chased this
repository three times in two days — `141eef7`, then `e42fadc`, now this — because Session F
is actively working in it and has no remote to push to.

> **ARCHIVING A LIVE REPOSITORY IS CHASING A MOVING TARGET, AND EVERY LAG IS A WINDOW IN
> WHICH THE ARCHIVE STATES SOMETHING ITS SOURCE HAS RETRACTED.** That window has been open
> twice already. **The fix is not a faster archiver; it is a remote, which is the owner's to
> authorise.**

    2662a678cc5b  CLIENT-DEEP-RESEARCH.md
    00625edae9df  CLIENT-ITEM-TABLE-COUNT.md
    50f1333cb997  method/agree.py
    e1a9c2ae0c47  method/checktext.py
    208e4f5632e6  method/dupcheck.py
    f389fa1a2a94  method/fields.py
    323073f7f561  method/join.py
    bee41c1d3a65  method/pattern.py
    3947d381afbe  method/pfs.py
    3ca0ee427102  method/scanall.py
    c64b807c1ae6  method/spellparse.py
    b0f3c7e1ba3e  method/total.py

sha256, first twelve, of the bytes as stored here, verified against the source at pin time.
`.gitattributes` marks this directory `-text` so git normalisation cannot rewrite them.

## The source commits, in order

    f7bd04a  04 Sep 10:42  Pre-register population decision and verification conditions before counting
    e5e8ee5  04 Sep 10:53  Publish bounded negative: client ships no item table
    a94c5eb  04 Sep 11:00  Close input gaps; evaluate union and V2 against named substitute objects
    9da35e0  04 Sep 11:02  Show the 18 corroborated names with item IDs; explain the 417->416 change
    141eef7  04 Sep 11:04  Resolve the 3085/3087 and 63/64 enumeration differences by naming methods
    e42fadc  06 Sep 01:23  MATERIAL CORRECTION: client does ship a partial item table (1,158 items)
    b7a0a81  06 Sep 01:30  Deep research partial: client contradicts published spell data

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
