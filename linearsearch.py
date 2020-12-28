l1 = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
item = int(input("Enter No. to be found"))
found = False
for i in range(len(l1)):
    if l1[i] == item:
        found = True
        print("Found")
        break

if found == False:
    print("Not Found")