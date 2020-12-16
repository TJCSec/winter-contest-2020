from flask import request
from urllib.parse import urljoin, urlparse, urlunparse, urlencode
import re

VALID_USERNAME = re.compile(r"^[A-Za-z_][A-Za-z\d_]*$")

def is_safe_url(target):
  ref_url = urlparse(request.host_url)
  test_url = urlparse(urljoin(request.host_url, target))
  return test_url.scheme in ("http", "https") and ref_url.netloc == test_url.netloc

def is_url(target):
  url = urlparse(target)
  return url.scheme in ("http", "https")

def int_to_bytes(i):
  return i.to_bytes((i.bit_length()+7)//8, 'big')

def bytes_to_int(b):
  return int.from_bytes(b, 'big')

def make_url(base, params):
  url = list(urlparse(base))
  url[4] = urlencode(params)
  return urlunparse(url)
