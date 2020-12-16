#!/usr/bin/env python3

import hashlib

flag = open("flag.txt").read().strip()

def sha512(b):
  h = hashlib.sha512()
  h.update(b)
  return h.hexdigest()

with open("output.txt", "w") as f:
  for c in flag:
    f.write(sha512(c.encode()))
