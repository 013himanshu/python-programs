n = int(input())
words = list()
for j in range (0, n):
    words.append(input())
dct = dict()
for i in words:
    dct[i] = dct.get(i, 0)+1
print(len(dct))
for k, v in dct.items():
    print(v, end=" ")
