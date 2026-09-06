import sys, os, json, io, collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from spellparse import parse
base=os.path.dirname(os.path.abspath(__file__))
lines, rows = parse(os.path.join(base,'client','spells_us.txt'))
B=r"C:\Users\Lindsey\Desktop\EQLS Director\peers\EQL50ups\research\data"
w=json.load(io.open(os.path.join(B,'eqbuddy-harvest-spells.json'),encoding='utf-8'))
allrows=collections.defaultdict(list)
for r in rows: allrows[r[1]].append(r)
dupnames=sum(1 for k,v in allrows.items() if len(v)>1)
print("client rows: %d | distinct names: %d | names with >1 row: %d" % (len(rows), len(allrows), dupnames))

for label,key,col,scale in [("RECAST","recast_seconds",10,1000.0),
                            ("CAST","cast_time_seconds",8,1000.0),
                            ("MANA","mana",14,1.0)]:
    firstonly=0; anyrow=0; trueconflict=0; conflicts=[]
    for e in w:
        n=e.get('name'); wv=e.get(key)
        if not n or n not in allrows or wv is None: continue
        cands=[]
        for r in allrows[n]:
            try: cands.append(int(r[col])/scale)
            except Exception: pass
        if not cands: continue
        first=cands[0]
        ok_first = abs(float(wv)-first)<0.051
        ok_any   = any(abs(float(wv)-c)<0.051 for c in cands)
        if not ok_first: firstonly+=1
        if ok_any: anyrow+=1
        if not ok_any:
            trueconflict+=1
            if len(conflicts)<8: conflicts.append((n,float(wv),sorted(set(cands))[:4],len(allrows[n])))
    print("\n=== %s ===" % label)
    print("  disagreements using FIRST row only      : %d" % firstonly)
    print("  of those, resolved by ANOTHER client row: %d" % (firstonly-trueconflict))
    print("  TRUE conflicts (no client row agrees)   : %d" % trueconflict)
    for n,wv,cs,k in conflicts:
        print("    %-30s wiki=%-9s client rows(%d)=%s" % (n[:30], wv, k, cs))
