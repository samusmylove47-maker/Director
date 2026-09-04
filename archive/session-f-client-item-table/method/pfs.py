import struct, zlib, sys, os
# EQ PFS container (.eqg / .s3d / .pak / .pfs): read-only directory lister
def read_pfs(path):
    with open(path,'rb') as f: b=f.read()
    if len(b)<12: raise ValueError("too small")
    dir_off, = struct.unpack_from('<I', b, 0)
    magic = b[4:8]
    if magic != b'PFS ': raise ValueError("bad magic %r" % magic)
    cnt, = struct.unpack_from('<I', b, dir_off)
    entries=[]
    for i in range(cnt):
        crc, off, size = struct.unpack_from('<III', b, dir_off+4+i*12)
        entries.append((crc,off,size))
    def inflate(off,size):
        out=b''; p=off
        while len(out)<size:
            dl, il = struct.unpack_from('<II', b, p); p+=8
            out += zlib.decompress(b[p:p+dl]); p+=dl
        return out
    names=None
    for crc,off,size in entries:
        if crc==0x61580AC9:
            d=inflate(off,size)
            n,=struct.unpack_from('<I',d,0); p=4; names=[]
            for _ in range(n):
                ln,=struct.unpack_from('<I',d,p); p+=4
                names.append(d[p:p+ln-1].decode('latin-1')); p+=ln
    files=[(off,size) for crc,off,size in entries if crc!=0x61580AC9]
    return names, files, inflate
if __name__=='__main__':
    p=sys.argv[1]
    names, files, inflate = read_pfs(p)
    print("container:", os.path.basename(p))
    print("entries:", len(files), "| names listed:", len(names) if names else 0)
    for n in (names or [])[:15]: print("   ", n)
