fruit = 'banana'
print(fruit[1])


str = 'X-DSPAM-Confidence: 0.8475 '
colonpos = str.find(':')
aftercolon = str[colonpos + 1:]
stripped = aftercolon.strip()
fl = float(stripped)
print('found: %g' % fl)