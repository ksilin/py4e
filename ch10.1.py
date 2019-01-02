import string

fname = "romeo.txt"
try: 
  fhand = open(fname)
except:
  print('failed to open file: %s' % fname)
  exit()

wordHash = {}
topCount = 0
topWord = ""

for l in fhand:
    ll = l.strip().translate(str.maketrans('','',string.punctuation))
    words = ll.split()
    for w in words:
      wordHash[w] = wordHash.get(w, 0) + 1

# DSU - decorate-sort-undecorate
revWordTuples = []
for w, count in wordHash.items():
  revWordTuples.append((count, w))

s = sorted(revWordTuples, reverse = True)
unpacked = []
for count, w in s:
  unpacked.append(w)

print('found %d words:' % (len(wordHash)))
for a in s: 
  print(a)
# for a in unpacked: 
#  print(a)
