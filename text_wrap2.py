str = "abcdefghijklmnopqrstuvwxyz"
i = 0
n = 4
j = n
for x in range(len(str)):
    print(str[i:n])
    i = n
    n = n + j
