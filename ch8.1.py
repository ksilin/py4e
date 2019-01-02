
fname = "romeo.txt"
try: 
  fhand = open(fname)
except:
  print('failed to open file: %s' % fname)
  exit()

words = []

for l in fhand:
    w = l.split()
    for word in w:
      if not (word in words): words.append(word)

print('found %d word: %s' % (len(words), sorted(words)))
