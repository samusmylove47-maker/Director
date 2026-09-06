import io, os, sys
# Normalise at the boundary, ONCE, where lines are created. Nothing downstream defends.
def read_rows(path):
    with io.open(path,'rb') as f: raw=f.read()
    text = raw.decode('latin-1').replace('\r\n','\n').replace('\r','\n')
    lines = [l for l in text.split('\n') if l!='']
    return lines

def parse(path):
    lines = read_rows(path)
    rows = [l.split('^') for l in lines]
    return lines, rows

# ---- POSITIVE CONTROL: parity over REAL CRLF bytes, at the layer that breaks ----
def parity_test(tmp):
    body = "1^Alpha^7^\n2^Beta^9^\n"
    crlf = tmp+"/_crlf.txt"; lf = tmp+"/_lf.txt"
    io.open(crlf,'wb').write(body.replace('\n','\r\n').encode('latin-1'))
    io.open(lf,'wb').write(body.encode('latin-1'))
    a = parse(crlf)[1]; b = parse(lf)[1]
    assert a, "PARITY FAIL: CRLF fixture produced NO rows"
    assert a == b, "PARITY FAIL: CRLF and LF parses differ:\n  %r\n  %r" % (a,b)
    # the specific killer: trailing field must not carry a CR
    assert not any(fld.endswith('\r') for row in a for fld in row), "PARITY FAIL: CR rode into a field"
    # and an anchored pattern downstream must still work
    import re
    assert re.search(r'7$', a[0][2]) is not None, "PARITY FAIL: $-anchored match failed on CRLF-sourced field"
    return "PARITY OK (CRLF == LF, no CR in fields, $-anchor works)"

if __name__=='__main__':
    tmp=os.path.dirname(os.path.abspath(__file__))
    print(parity_test(tmp))
    p=sys.argv[1]
    lines, rows = parse(p)
    fc={}
    for r in rows: fc[len(r)]=fc.get(len(r),0)+1
    print("lines read     :", len(lines))
    print("rows parsed    :", len(rows))
    print("parsed/read    : %.4f%%" % (100.0*len(rows)/max(1,len(lines))))
    print("field counts   :", fc)
    print("CR in any field:", any('\r' in f for r in rows for f in r))
