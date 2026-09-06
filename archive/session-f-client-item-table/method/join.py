import sys, os, json, io
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from spellparse import parse
base=os.path.dirname(os.path.abspath(__file__))
lines, rows = parse(os.path.join(base,'client','spells_us.txt'))
print("client rows read/parsed: %d/%d (%.2f%%)" % (len(lines),len(rows),100.0*len(rows)/len(lines)))

B=r"C:\Users\Lindsey\Desktop\EQLS Director\peers\EQL50ups\research\data"
w=json.load(io.open(os.path.join(B,'eqbuddy-harvest-spells.json'),encoding='utf-8'))
print("wiki spell records:", len(w))
keys=set()
for e in w[:400]: keys.update(e.keys())
print("wiki fields:", sorted(k for k in keys if 'recast' in k.lower() or 'recovery' in k.lower() or 'cast' in k.lower() or 'mana' in k.lower()))

# client name -> row (first wins; note duplicates)
cl={}
for r in rows:
    cl.setdefault(r[1], r)
print("client distinct spell names:", len(cl))

wn=[e.get('name') for e in w if e.get('name')]
matched=[n for n in wn if n in cl]
print("wiki names matched in client: %d of %d (%.1f%%)" % (len(matched), len(wn), 100.0*len(matched)/len(wn)))
print("wiki names NOT in client    : %d" % (len(wn)-len(matched)))
assert len(matched) + (len(wn)-len(matched)) == len(wn), "CHECKSUM FAIL"
print("checksum: matched + unmatched == total  OK")
