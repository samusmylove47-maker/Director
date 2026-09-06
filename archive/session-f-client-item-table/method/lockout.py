import sys, os, re, collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from spellparse import read_rows, parity_test
base=os.path.dirname(os.path.abspath(__file__))
print(parity_test(base))
TERMS=["replay","lockout","lock out","dynamic zone","expedition","instance",
       "dzadd","dzlist","timer remaining","may enter","reset","cooldown",
       "raid instance","personal instance","dz "]
def sweep(path,label):
    lines=read_rows(path)
    hits=[]
    for l in lines:
        low=l.lower()
        for t in TERMS:
            if t in low: hits.append((t,l)); break
    print("\n=== %s ===\n  lines read: %d | lines matched: %d" % (label,len(lines),len(hits)))
    return lines,hits
CL=os.path.join(base,'client')
lines,hits = sweep(os.path.join(CL,'eqstr_us.txt'),'eqstr_us.txt (UI string table)')
c=collections.Counter(t for t,_ in hits)
print("  term histogram:", dict(c))
print("\n  --- ALL matches (not a sample) ---")
for t,l in hits:
    print("   ", l[:150])
