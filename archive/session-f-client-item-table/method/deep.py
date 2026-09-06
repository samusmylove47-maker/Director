import sys, os, collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from spellparse import parse
base=os.path.dirname(os.path.abspath(__file__))
lines, rows = parse(os.path.join(base,'client','spells_us.txt'))
by={r[1]:r for r in rows}
print("=== col 167 (item-ID space, 100%% populated, 4 distinct) ===")
print("  values:", collections.Counter(r[167] for r in rows).most_common())
print("=== col 81 / 145 (spell-ID space) — sample non -1 ===")
sid={r[0]:r[1] for r in rows}
for c in (81,145):
    ex=[(r[0],r[1],r[c]) for r in rows if r[c] not in ('-1','0')][:3]
    for a,b,v in ex:
        print("  col%d: spell %s %-26s -> %s = %r" % (c,a,b[:26],v, sid.get(v,'<not a spell id>')))
print("\n=== col 172: packed sub-record ===")
for nm in ("Complete Heal","Gate","Harm Touch"):
    if nm in by: print("  %-14s %r" % (nm, by[nm][172][:90]))
w=collections.Counter(len(r[172].split('|')) for r in rows)
print("  pipe-field-count distribution:", w.most_common(6))
# is it slot-structured? examine a known damage spell
print("\n=== structure probe: fields of col172 for a simple nuke ===")
for nm in ("Burst of Flame","Shock of Frost"):
    if nm in by:
        print("  %s -> %s" % (nm, by[nm][172]))
