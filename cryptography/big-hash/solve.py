#!/usr/bin/env python3

import string
import hashlib

def sha512(b):
  h = hashlib.sha512()
  h.update(b)
  return h.hexdigest()

decode = {sha512(c.encode()): c for c in string.printable}

enc = open("output.txt").read()

flag = "".join(decode[enc[i:i+128]] for i in range(0, len(enc), 128))
print(flag)
