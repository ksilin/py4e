### extract links from files with beautiful soup / urllinks.py
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
import ssl

# ignore SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://docs.python.org"
page = urllib.request.urlopen(url).read()
soup = BeautifulSoup(page, 'html.parser')
tags = soup('a')
print("found", len(tags),  "paragraphs")
for t in tags:
  print(t.get('href', None))