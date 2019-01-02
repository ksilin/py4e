import re

fhand = open('mbox-short.txt')

res = []

for line in fhand:
  l = line.strip()
  addresses = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z0-9]', l)
  if(len(addresses) > 0):
    res.extend(addresses)

print(res)