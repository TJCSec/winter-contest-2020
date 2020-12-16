from flask import current_app as app
from flask_login import current_user

from time import time
import base64
import json
import hashlib

from .utils import int_to_bytes, bytes_to_int

RSA_N, RSA_E, RSA_D = (app.config[key] for key in ('RSA_N', 'RSA_E', 'RSA_D'))

def get_pubkey():
  n, e = (base64.urlsafe_b64encode(int_to_bytes(x)).decode() for x in (RSA_N, RSA_E))
  return {
    'n': n,
    'e': e,
  }

def get_token():
  token = {
    'uid': current_user.uid,
    'username': current_user.username,
    'iat': int(time())
  }
  token = json.dumps(token).encode()
  h = hashlib.sha256()
  h.update(token)
  m = bytes_to_int(h.digest())
  sig = pow(m, RSA_D, RSA_N)
  sig = int_to_bytes(sig)
  return f'{base64.urlsafe_b64encode(token).decode()}~OMG~GINKOID~{base64.urlsafe_b64encode(sig).decode()}'
