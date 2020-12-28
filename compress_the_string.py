import itertools

data1 = str(input())
data1 = list(map(int, data1))
keys = list()
groups = list()
for k, g in itertools.groupby(data1):
    result = len(list(g)), int(k)
    print(tuple(result), end=" ")

