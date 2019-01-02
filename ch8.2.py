
fname = "mbox.txt"
try: 
  fhand = open(fname)
except:
  print('failed to open file: %s' % fname)
  exit()

addresses = []

for l in fhand:
  if(l.startswith("From")):
    w = l.split()
    addresses.append(w[1])
asset = set(addresses)
print('found %d addresses: %s' % (len(asset), asset))
