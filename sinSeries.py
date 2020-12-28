x=30
powerno=int(input("Enter power no."))
if powerno%2!=0:
    i=3
    z=0
    while i<=powerno:
        resultup=1
        resultdown=1
        n=i
        for j in range(1,n+1):
            resultup=resultup*x

        n=i
        for k in range(1,n+1):
            resultdown=resultdown*k

        if z==0:
            x=x-(resultup/resultdown)
        elif z%2!=0:
            x=x+(resultup/resultdown)

        z=z+1
        i=i+2

    print (x)
else:
    print ("Enter a odd no. and it must be greater than or equal to 3")
