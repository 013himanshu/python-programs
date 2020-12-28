n=5
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end="")
    for k in range(i,i*2):
        print("*",end=" ")
    print("\n")