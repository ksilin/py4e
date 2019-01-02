fname = input('please enter file name: ')

try: 
  fhand = open(fname)
except:
  print('failed to open file: %s' % fname)
  exit()

spamConf = []

for l in fhand:
  if l.startswith('X-DSPAM-Confidence'):
    nstr = l[l.find(':') + 1:].strip()
    spamConf = spamConf + [float(nstr)]

print('mean spam conf: %g' % (sum(spamConf)/len(spamConf)))
