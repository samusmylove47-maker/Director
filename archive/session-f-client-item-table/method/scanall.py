import os, sys, collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from pfs import read_pfs
SRC=r"C:\Users\Public\Daybreak Game Company\Installed Games\EverQuest Legends"
exts=collections.Counter(); ok=0; bad=0; badlist=[]; textmembers=[]
for fn in sorted(os.listdir(SRC)):
    p=os.path.join(SRC,fn)
    if not os.path.isfile(p): continue
    if os.path.splitext(fn)[1].lower() not in ('.eqg','.s3d','.pak','.pfs'): continue
    try:
        names, files, inflate = read_pfs(p); ok+=1
        for n in names or []:
            e=os.path.splitext(n)[1].lower()
            exts[e]+=1
            if e in ('.txt','.csv','.ini','.dat','.xml','.json'):
                textmembers.append((fn,n))
    except Exception as ex:
        bad+=1; badlist.append((fn,str(ex)[:50]))
print("containers parsed OK:", ok, "| failed:", bad)
print("=== member extension histogram ===")
for e,c in exts.most_common(20): print(f"  {e or '(none)':10s} {c}")
print("=== text-like members (candidate data tables):", len(textmembers))
for fn,n in textmembers[:40]: print("   ",fn,"->",n)
print("=== parse failures ===")
for fn,e in badlist[:15]: print("   ",fn,":",e)
