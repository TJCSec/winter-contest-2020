#!/usr/bin/env sage

import os
os.environ["TERM"] = "linux"

from pwn import *

host = args.HOST or "localhost"
port = args.PORT or 30002

def get_enc():
  r = remote(host, port)
  r.recvuntil("magic...")
  r.recvline()
  n = Integer(r.recvline().strip().split()[-1])
  c = Integer(r.recvline().strip().split()[-1])
  r.close()
  return n, c

e = 17

encs = [get_enc() for _ in range(e)]
n, c = zip(*encs)
me = crt([*c], [*n])
m = int(me.nth_root(e))

flag = m.to_bytes((m.bit_length()+7)//8, "big")
print(flag.decode())
