#!/usr/bin/env python3

from pwn import *
from io import BytesIO
from PIL import Image
import base64

host = args.HOST or "localhost"
port = args.PORT or 30003

r = remote(host, port)
img = Image.open(BytesIO(base64.b64decode(r.recvline())))

THRESHOLD = 200
img = img.crop((0, 0, 512, 512))
img = img.convert("L").point(lambda x: (0, 255)[x > THRESHOLD])

for y in range(512):
  for x in range(512):
    if img.getpixel((x, y)) == 0:
      x1, y1 = x, y
      break
  else:
    continue
  break

for y in range(511, -1, -1):
  for x in range(512):
    if img.getpixel((x, y)) == 0:
      x2, y2 = x, y
      break
  else:
    continue
  break

y2 -= 49
d = math.sqrt((x1-x2)**2 + (y1-y2)**2)

r.sendline(str(d))
print(r.recvall().decode())
