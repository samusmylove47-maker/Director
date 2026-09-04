import os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from pfs import read_pfs
SRC=r"C:\Users\Public\Daybreak Game Company\Installed Games\EverQuest Legends"
tot=0;cont=0
for fn in os.listdir(SRC):
    p=os.path.join(SRC,fn)
    if not os.path.isfile(p) or os.path.splitext(fn)[1].lower() not in ('.eqg','.s3d','.pak','.pfs'): continue
    try:
        ns,files,inf=read_pfs(p); cont+=1; tot+=len(files)
    except Exception: pass
print("containers:",cont,"total members:",tot)
