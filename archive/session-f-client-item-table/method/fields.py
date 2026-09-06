import sys, os, collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from spellparse import parse
lines, rows = parse(sys.argv[1])
n=len(rows[0])
print("columns:", n, " rows:", len(rows))
# find the 16-wide class-level block: columns dominated by 255 with a minority in 1..254
cand=[]
for c in range(n):
    vals=[r[c] for r in rows]
    num=sum(1 for v in vals if v.lstrip('-').isdigit())
    if num < len(vals)*0.99: continue
    iv=[int(v) for v in vals if v.lstrip('-').isdigit()]
    p255=sum(1 for v in iv if v==255)/len(iv)
    inrange=sum(1 for v in iv if 1<=v<=254)/len(iv)
    if p255>0.4 and inrange>0.02 and max(iv)<=255 and min(iv)>=0:
        cand.append(c)
print("class-level block candidates:", cand)
# report distinct-value profile for the first 40 numeric columns
print("\ncol | distinct | min | max | sample")
for c in range(0, 40):
    vals=[r[c] for r in rows]
    iv=[int(v) for v in vals if v.lstrip('-').isdigit()]
    d=len(set(vals))
    if iv:
        print("%3d | %8d | %10d | %10d | %s" % (c, d, min(iv), max(iv), vals[0][:28]))
    else:
        print("%3d | %8d | %10s | %10s | %s" % (c, d, '-','-', vals[0][:28]))
