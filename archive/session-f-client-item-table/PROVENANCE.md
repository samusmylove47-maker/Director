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

**Pinned to source commit `141eef7783f7`.** Not to "copy time" — my first version of this
file said *verified identical to the source tree at copy time*, which was true when
written and false four minutes later, because Session F committed again while I was
archiving. **A snapshot must name the commit it snapshots, never the clock.** That is the
same fault as a read-date that has done its job being indistinguishable from one that has
gone stale, and it caught me inside the file whose only purpose is verification.

    f9ac576cd073  CLIENT-ITEM-TABLE-COUNT.md
    e1a9c2ae0c47  method/checktext.py
    3947d381afbe  method/pfs.py
    3ca0ee427102  method/scanall.py

sha256, first twelve, of the bytes as stored here. `.gitattributes` marks this directory
`-text` so git normalisation cannot rewrite them — a content hash that its own repository
silently invalidates is a fault this project has already found once, in an artifact that
did not survive its own repository.

## The source commits, in order

    f7bd04a  10:42:50  Pre-register population decision and verification conditions
    e5e8ee5  10:53:40  Publish bounded negative: client ships no item table
    a94c5eb  11:00:34  Close input gaps; evaluate union and V2 against named objects
    9da35e0  11:02:48  Show the 18 corroborated names; explain the 417->416 change
    141eef7  11:04:07  Resolve the 3085/3087 and 63/64 enumeration differences by naming methods

**The eleven minutes between the first two are the load-bearing fact.** A
pre-registration is only worth what its ordering can prove, and that ordering is
in the git history rather than in the prose — verifiable independently of
anything the session says about itself. Session 0 checked it there.

## The finding, in one line

**306 of 416 item names the owner's character demonstrably holds appear in no
file shipped with the client** — across 11,973 shipped files plus 83,137 members
inside 2,272 proprietary containers, parsed by `method/pfs.py`, 2,272 of 2,272
with zero failures. Items the client has never heard of are in the player's
inventory, which is only possible if item data is server-sent.

**The client is not a witness either way. It contradicts nothing this project
publishes; it simply cannot testify.**

`method/pfs.py` is the reusable half. It reads the PFS container format the
EverQuest client ships (uint32 directory offset, `PFS ` magic, crc/offset/size
triples, zlib block chains, filename list under CRC `0x61580AC9`). **Nobody here
needs to derive that format again.**
