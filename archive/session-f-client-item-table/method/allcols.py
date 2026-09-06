import sys, os, collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from spellparse import parse, parity_test
base=os.path.dirname(os.path.abspath(__file__))
print(parity_test(base))
lines, rows = parse(os.path.join(base,'client','spells_us.txt'))
print("lines %d / rows %d / %.4f%%\n" % (len(lines), len(rows), 100.0*len(rows)/len(lines)))
n=len(rows[0])
INTERESTING=[]
print("col | distinct |        min |        max | nonzero%% | kind")
for c in range(n):
    vals=[r[c] for r in rows]
    d=len(set(vals))
    nums=[v for v in vals if v.lstrip('-').isdigit()]
    isnum = len(nums)==len(vals)
    if isnum:
        iv=[int(v) for v in nums]
        nz=100.0*sum(1 for v in iv if v!=0)/len(iv)
        lo,hi=min(iv),max(iv)
        if d==1: kind="CONSTANT=%d"%lo
        elif d==2: kind="binary flag"
        elif hi<=255 and lo>=0 and d<=60: kind="small enum"
        elif hi>1000000: kind="large/id-or-ms"
        else: kind=""
        # flag columns that look like they hold IDs into another table
        if d>500 and hi>1000: kind=(kind+" HIGH-CARD").strip()
        print("%3d | %8d | %10d | %10d | %7.1f | %s" % (c,d,lo,hi,nz,kind))
        if d>500 and hi>1000: INTERESTING.append(c)
    else:
        smp=next((v for v in vals if v), '')
        print("%3d | %8d | %10s | %10s | %7s | TEXT  e.g. %r" % (c,d,'-','-','-',smp[:26]))
        INTERESTING.append(c)
print("\nHIGH-CARDINALITY / TEXT columns (candidate keys or names):", INTERESTING)
