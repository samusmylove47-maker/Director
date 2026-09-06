import sys, os, json, io
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from spellparse import parse
base=os.path.dirname(os.path.abspath(__file__))
lines, rows = parse(os.path.join(base,'client','spells_us.txt'))
B=r"C:\Users\Lindsey\Desktop\EQLS Director\peers\EQL50ups\research\data"
w=json.load(io.open(os.path.join(B,'eqbuddy-harvest-spells.json'),encoding='utf-8'))
cl={}
for r in rows: cl.setdefault(r[1], r)

def cmpfield(label, wikikey, col, scale):
    tot=agree=disagree=missing=0
    diffs=[]
    for e in w:
        n=e.get('name')
        if not n or n not in cl: continue
        wv=e.get(wikikey)
        if wv is None: missing+=1; continue
        try: cv=int(cl[n][col])/scale
        except Exception: missing+=1; continue
        tot+=1
        if abs(float(wv)-cv) < 0.051: agree+=1
        else:
            disagree+=1; diffs.append((n, float(wv), cv))
    print("\n=== %s : wiki['%s'] vs client col%d ===" % (label, wikikey, col))
    print("  comparable: %d   AGREE: %d (%.1f%%)   DISAGREE: %d   no-value: %d"
          % (tot, agree, 100.0*agree/tot if tot else 0, disagree, missing))
    assert agree+disagree==tot, "CHECKSUM FAIL"
    print("  checksum: agree + disagree == comparable  OK")
    diffs.sort(key=lambda t: -abs(t[1]-t[2]))
    for n,a,b in diffs[:10]:
        print("    %-34s wiki=%-10s client=%s" % (n[:34], a, b))
    return diffs

cmpfield("RECAST",    "recast_seconds",    10, 1000.0)
cmpfield("CAST TIME", "cast_time_seconds",  8, 1000.0)
cmpfield("MANA",      "mana",              14, 1.0)
