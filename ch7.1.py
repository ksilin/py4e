fhand = open('mbox.txt')
print(fhand)


# the for loop reads the file linewise, 
# meaning it can read huge files without RAM pressure
# hande.read() would read the entire file in memory
# calls to read exhaust the source
lcount = 0
for line in fhand:
  lcount = lcount + 1

# print(len(fhand.lines)) - there is no lines method or similar
print(lcount)

# writing to file
outfile = open('out.txt', 'w')
outfile.write('hi')
outfile.close()