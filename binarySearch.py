l1 = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
item = int(input("Enter No. to be found"))
first = 0
last = len(l1) - 1
found = False

while first <= last and not found:
    mid = (first + last) // 2
    if l1[mid] == item:
        found = True
        break
    else:
        if item < l1[mid]:
            last = mid - 1
        else:
            first = mid + 1
if found == True:
    print("No. Found")
else:
    print("not Found")