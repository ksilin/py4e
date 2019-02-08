### extract links from files with regex
import urllib.request, urllib.parse, urllib.error
import re
import ssl

# ignore SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://docs.python.org"
hrefRe = b'href="(http[s]?://.+?)"'
page = urllib.request.urlopen(url).read()
links = re.findall(hrefRe, page)

for l in links:
  print(l.decode())