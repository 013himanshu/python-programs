from collections import Counter
s = sorted(input())
c = Counter(s).most_common(3)
for i, j in c:
    print(i, j)
