fname = "mbox.txt"
try: 
  fhand = open(fname)
except:
  print('failed to open file: %s' % fname)
  exit()

addresses = {}
topCount = 0
topName = ""

for l in fhand:
  if(l.startswith("From")):
    w = l.split()
    address = w[1]
    count = addresses.get(address, 0) + 1
    addresses[address] = addresses.get(address, 0) + 1
    if(count >= topCount):
      topCount = count
      topName = address

print('found %d addresses:' % (len(addresses)))
print('top committer: %s : %d' % (topName, topCount))
for a in addresses: 
  print(a, addresses[a])
