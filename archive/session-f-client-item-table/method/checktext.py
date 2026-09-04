import os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from pfs import read_pfs
def out(s): sys.stdout.write(s.encode('ascii','replace').decode('ascii')+"\n")
SRC=r"C:\Users\Public\Daybreak Game Company\Installed Games\EverQuest Legends"
base=os.path.dirname(os.path.abspath(__file__))
names=[l.rstrip('\n') for l in open(os.path.join(base,'inv_names_base.txt'),encoding='latin-1') if l.strip() and l.strip()!='Name']
hits=[]; shown=0; total=0
for fn in sorted(os.listdir(SRC)):
    p=os.path.join(SRC,fn)
    if not os.path.isfile(p) or os.path.splitext(fn)[1].lower() not in ('.eqg','.s3d','.pak','.pfs'): continue
    try: ns, files, inflate = read_pfs(p)
    except Exception: continue
    files = sorted(files, key=lambda t: t[0])   # FIX: filename list is in data-offset order
    for i,(off,size) in enumerate(files):
        n = ns[i] if ns and i<len(ns) else ''
        if os.path.splitext(n)[1].lower() not in ('.txt','.csv','.ini','.xml','.json','.dat'): continue
        try: d=inflate(off,size).decode('latin-1')
        except Exception: continue
        total+=1
        if shown<3 and n.endswith('.txt'):
            out(f"--- SAMPLE {fn} -> {n} ---"); out(d[:180].replace('\r','')); shown+=1
        for nm in names:
            if nm in d: hits.append((fn,n,nm))
out("text-like members decompressed and searched: %d" % total)
out("ITEM-NAME HITS INSIDE CONTAINERS: %d" % len(hits))
for h in hits[:20]: out("    %s | %s | %s" % h)
