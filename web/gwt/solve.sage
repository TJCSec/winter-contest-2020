import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)

load('coppersmith.sage')

import requests
from urllib.parse import urljoin
import base64
from time import time
import json
import hashlib

SSO_ENDPOINT = os.getenv('SSO_ENDPOINT') or 'https://gwt-sso.winter-challenge.tjcsec.club'
APP_ENDPOINT = os.getenv('APP_ENDPOINT') or 'https://gwt-app.winter-challenge.tjcsec.club'

def get_pubkey():
  r = requests.get(urljoin(SSO_ENDPOINT, '/pubkey'))
  pub = r.json()
  N, e = (bytes_to_int(base64.urlsafe_b64decode(pub[key])) for key in ('n', 'e'))
  return N, e

def bytes_to_int(b):
  return Integer(int.from_bytes(b, 'big'))

def int_to_bytes(i):
  i = int(i)
  return i.to_bytes((i.bit_length()+7)//8, 'big')

N, e = get_pubkey()

print('fetched public key')

bounds = (floor(N^.25), 2^2048)
R = Integers(e)
P1.<k, s> = PolynomialRing(R)
f = 2*k*((N+1)//2 - s) + 1
K, S = small_roots(f, bounds)[0]

d = (2*Integer(K)*((N+1)//2 - Integer(S)) + 1) // e
print(d)

data = {
  'uid': int(1),
  'username': 'ginkoid',
  'iat': int(time()),
}
data = json.dumps(data).encode()
h = hashlib.sha256()
h.update(data)
m = bytes_to_int(h.digest())
sig = power_mod(m, d, N)
sig = int_to_bytes(sig)
token = f'{base64.urlsafe_b64encode(data).decode()}~OMG~GINKOID~{base64.urlsafe_b64encode(sig).decode()}'

print(token)

r = requests.get(APP_ENDPOINT, params={'token': token})

import re
print(re.search(r'flag\{.+\}', r.text).group(0))
