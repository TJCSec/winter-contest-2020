from flask import Flask, request, render_template, url_for

from urllib.parse import urljoin, urlparse, urlencode, urlunparse
import os
import requests

import base64
import json
import hashlib
from time import time

app = Flask(__name__)

FLAG = open("flag.txt").read().strip()
SSO_ENDPOINT = os.getenv('SSO_ENDPOINT') or 'https://gwt-sso.winter-challenge.tjcsec.club'
MAX_TOKEN_AGE = 60

@app.route('/')
def index():
  # fetch provided token
  token = request.args.get('token')
  error = ''
  if token:
    try:
      # verify and decode token
      data = verify_token(token)
      uid, user = get_user(data)
      # send user page
      return render_template('index.html', user=user, flag=FLAG)
    except TokenError as e:
      error = str(e)
    except:
      error = 'Unknown error'
  # there was some error or there was no token, send default page
  return render_template('index.html', error=error, authorize_url=make_authorize_url())

# construct authorization url
def make_authorize_url():
  url = list(urlparse(urljoin(SSO_ENDPOINT, '/authorize')))
  url[4] = urlencode({'next': url_for('index', _external=True)})
  return urlunparse(url)

class TokenError(ValueError):
  pass

# verify a token
def verify_token(token):
  try:
    data, sig = (base64.urlsafe_b64decode(part.encode()) for part in token.split('~OMG~GINKOID~'))
  except:
    # the token is incorrectly formatted
    raise TokenError('Invalid token format')
  try:
    n, e = get_pubkey()
  except:
    # SSO server did not respond with a public key
    raise TokenError('Could not retrieve public key')
  sig = bytes_to_int(sig)
  h = hashlib.sha256()
  h.update(data)
  m = bytes_to_int(h.digest())
  if pow(sig, e, n) != m:
    # hash does not match expected value
    raise TokenError('Invalid token signature')
  return data.decode()

# retrieve the public key from the SSO server
def get_pubkey():
  r = requests.get(urljoin(SSO_ENDPOINT, '/pubkey'), timeout=10)
  pub = r.json()
  n, e = (bytes_to_int(base64.urlsafe_b64decode(pub[key])) for key in ('n', 'e'))
  return n, e

# decode token data (no signature) and check iat validity
def get_user(data):
  try:
    data = json.loads(data)
  except:
    # the token is invalid JSON
    raise TokenError('Invalid token data')
  try:
    elapsed = int(time()) - data['iat']
    if elapsed < 0 or elapsed > MAX_TOKEN_AGE:
      # the token was issued in the future (???) or has expired
      raise TokenError('Token expired')
    return data['uid'], data['username']
  except KeyError:
    # the token is missing properties
    raise TokenError('Invalid token properties')

# utility to convert bytes to int
def bytes_to_int(b):
  return int.from_bytes(b, 'big')

if __name__=='__main__':
  app.run()
