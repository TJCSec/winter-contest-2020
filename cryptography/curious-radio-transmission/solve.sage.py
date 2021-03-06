

# This file was *autogenerated* from the file solve.sage
from sage.all_cmdline import *   # import sage library

_sage_const_30002 = Integer(30002); _sage_const_1 = Integer(1); _sage_const_17 = Integer(17); _sage_const_7 = Integer(7); _sage_const_8 = Integer(8)#!/usr/bin/env sage

import os
os.environ["TERM"] = "linux"

from pwn import *

host = args.HOST or "localhost"
port = args.PORT or _sage_const_30002 

def get_enc():
  r = remote(host, port)
  r.recvuntil("magic...")
  r.recvline()
  n = Integer(r.recvline().strip().split()[-_sage_const_1 ])
  c = Integer(r.recvline().strip().split()[-_sage_const_1 ])
  r.close()
  return n, c

e = _sage_const_17 

encs = [get_enc() for _ in range(e)]
n, c = zip(*encs)
me = crt([*c], [*n])
m = int(me.nth_root(e))

flag = m.to_bytes((m.bit_length()+_sage_const_7 )//_sage_const_8 , "big")
print(flag.decode())

