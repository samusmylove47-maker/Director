import sys, os, collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from spellparse import parse, parity_test
base=os.path.dirname(os.path.abspath(__file__))
print(parity_test(base))
lines, rows = parse(os.path.join(base,'client','spells_us.txt'))
# CORRECTED: '$' separates slots; '|' separates fields within a slot
widths=collections.Counter(); badslot=0; total=0; seqok=0; seqbad=0; empty=0
spa=collections.Counter()
for r in rows:
    v=r[172]
    if v=='' or v=='0': empty+=1; continue
    parts=v.split('$')
    nums=[]
    for i,p in enumerate(parts):
        f=p.split('|'); widths[len(f)]+=1; total+=1
        if len(f)!=6: badslot+=1; continue
        spa[f[1]]+=1
        if f[0].lstrip('-').isdigit(): nums.append(int(f[0]))
    if nums==list(range(1,len(nums)+1)): seqok+=1
    else: seqbad+=1
print("\nrows with no effect data      :", empty)
print("total slots parsed            :", total)
print("slot field-width distribution :", widths.most_common())
print("slots NOT 6 fields wide       :", badslot)
print("\n--- is field 0 a 1-based slot INDEX? ---")
print("rows whose field-0 sequence is exactly 1,2,3,... :", seqok)
print("rows where it is not                            :", seqbad)
print("\ndistinct SPA values (field 1):", len(spa))
print("top 12 SPAs:", spa.most_common(12))
