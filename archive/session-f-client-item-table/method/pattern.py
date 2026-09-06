import sys, os, json, io, collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from spellparse import parse
base=os.path.dirname(os.path.abspath(__file__))
lines, rows = parse(os.path.join(base,'client','spells_us.txt'))
B=r"C:\Users\Lindsey\Desktop\EQLS Director\peers\EQL50ups\research\data"
w=json.load(io.open(os.path.join(B,'eqbuddy-harvest-spells.json'),encoding='utf-8'))
allrows=collections.defaultdict(list)
for r in rows: allrows[r[1]].append(r)

for label,key,col,scale in [("RECAST","recast_seconds",10,1000.0),
                            ("CAST","cast_time_seconds",8,1000.0),
                            ("MANA","mana",14,1.0)]:
    pat=collections.Counter(); tot=0
    for e in w:
        n=e.get('name'); wv=e.get(key)
        if not n or n not in allrows or wv is None: continue
        cands=[]
        for r in allrows[n]:
            try: cands.append(int(r[col])/scale)
            except Exception: pass
        if not cands: continue
        if any(abs(float(wv)-c)<0.051 for c in cands): continue
        tot+=1
        pat[(float(wv), cands[0])]+=1
    print("\n=== %s : %d true conflicts, grouped by (wiki, client) pair ===" % (label, tot))
    cum=0
    for (a,b),c in pat.most_common(6):
        cum+=c
        print("    wiki=%-9s client=%-9s  x%-4d   (%.0f%% of conflicts)" % (a,b,c,100.0*c/tot))
    print("    top 6 pairs cover %d of %d = %.0f%%" % (cum, tot, 100.0*cum/tot))
    print("    distinct (wiki,client) pairs: %d" % len(pat))
