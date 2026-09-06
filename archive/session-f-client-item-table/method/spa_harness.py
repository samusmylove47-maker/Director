import sys, os, collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from spellparse import parse, parity_test
base=os.path.dirname(os.path.abspath(__file__))
print(parity_test(base))
lines, rows = parse(os.path.join(base,'client','spells_us.txt'))
print("lines %d / rows %d / %.4f%%\n" % (len(lines),len(rows),100.0*len(rows)/len(lines)))
by=collections.defaultdict(list)
for r in rows: by[r[1]].append(r)

def slots(v):
    p=v.split('|')
    if not p or not p[0].isdigit(): return None,[]
    n=int(p[0]); rest=p[1:]
    return n,[tuple(rest[i*5:(i+1)*5]) for i in range(n) if len(rest)>=(i+1)*5]

# spells whose in-game behaviour is independently known - the decode test set
PROBES=["Gate","Complete Heal","Harm Touch","Burst of Flame","Strength","Spirit of Wolf",
        "Invisibility","Levitate","Bind Affinity","Superior Healing","Clarity",
        "Root","Snare","Blinding Luminance","Yaulp"]
print("%-20s %-6s  slots  (f1=SPA, f2..f5 UNIDENTIFIED)" % ("spell","id"))
for nm in PROBES:
    if nm not in by: continue
    r=by[nm][0]; n,sl=slots(r[172])
    print("%-20s %-6s  n=%s  %s" % (nm[:20], r[0], n, sl))

# distribution of first-field values across ALL slots in ALL spells -> is it really SPA?
c=collections.Counter()
tot=0
for r in rows:
    n,sl=slots(r[172])
    for s in sl:
        c[s[0]]+=1; tot+=1
print("\ntotal effect slots across all %d spells: %d" % (len(rows), tot))
print("distinct first-field values: %d  (SPA table is ~500 in EQ)" % len(c))
print("top 15 first-field values:", c.most_common(15))
