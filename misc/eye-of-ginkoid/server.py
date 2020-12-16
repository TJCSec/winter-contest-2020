#!/usr/bin/env python3

from PIL import Image, ImageDraw
from random import randrange
from io import BytesIO
import base64
import math
import select
import sys

# thanks saigautam
def input_timeout(prompt, timeout):
  sys.stdout.write(prompt)
  sys.stdout.flush()
  ready, _, _ = select.select([sys.stdin], [],[], timeout)
  if ready:
    return sys.stdin.readline().rstrip('\n')
  raise Exception("Too slow!")

SIZE = 512
GINK = 50
EPSILON = 0.000001

dist = lambda x1, y1, x2, y2: math.sqrt((x1-x2)**2 + (y1-y2)**2)

img = Image.new("RGB", (SIZE, SIZE+50), (255, 255, 255))
gink = Image.open("ginkoid.png")
gink.thumbnail((GINK, GINK))

x1, y1, x2, y2 = (randrange(SIZE - GINK) for _ in range(4))
d = dist(x1, y1, x2, y2)
while d < GINK:
  x2, y2 = (randrange(SIZE - GINK) for _ in range(2))
  d = dist(x1, y1, x2, y2)

img.paste(gink, (x1, y1))
img.paste(gink, (x2, y2))

draw = ImageDraw.Draw(img)
draw.text((40, 512), f"How far apart (in pixels, within {EPSILON}) are the centers of the ginkoids?\n", (25, 116, 213))

buffer = BytesIO()
img.save(buffer, format="PNG")
print(base64.b64encode(buffer.getvalue()).decode())

try:
  if abs(float(input_timeout("> ", 1)) - d) <= EPSILON:
    print("Good job!")
    print(open("flag.txt").read().strip())
  else:
    raise ValueError("Nope!")
except Exception as e:
  print(e)
