n=5
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end="")
    for k in range(0,(i*2)-1):
        print("*",end="")

    print("\n")