name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)
word = list()
for line in handle:
    if line.startswith("From "):
        words = line.split()
        word.append(words[1])

count = dict()
for i in word:
    count[i] = count.get(i, 0)+1

bigcount = 0
bigword = 0
for w,c in count.items():
    if c == 0 or c > bigcount:
        bigword = w
        bigcount = c
print(bigword, bigcount)
