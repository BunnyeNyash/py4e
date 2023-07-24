# Get the name of the file and open it
name = input('Enter file:')
handle = open(name, 'r')

# Count word frequency (make a histogram)
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# Find the most common word
bigcount = None
bigword = None
for word, count in list(counts.items()):
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

# All done (print the stuff out)
print(bigword, bigcount)

# Code: http://www.py4e.com/code3/words.py
