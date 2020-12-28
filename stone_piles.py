def maximumStones(arr, n):
    # Write your code here
    sum = 0
    for i in range(0, n+1):
        lft = 0
        ryt = 0
        for j in range(0, n):
            if j % 2 == 0:
                lft = lft + arr[j]
            else:
                ryt = ryt + arr[j]
        if lft == ryt:
            sum = lft + ryt
            break
        else:
            ind = arr.index(max(arr))
            arr[ind] = arr[ind] - 1
            continue

    return sum


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()[:n]))

    result = maximumStones(arr, n)

    print(result)
