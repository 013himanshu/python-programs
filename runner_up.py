n = 3
arr = list(map(int, input().strip().split()))[:n]
maximum = max(arr)
c = arr.count(maximum)
for i in range(c):
    arr.remove(maximum)

runnerUp = max(arr)
print(runnerUp)
