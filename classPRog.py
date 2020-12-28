class si:
    s=0
    r=0
    t=0


obj=si()
print("Before")
print("s= ",str(si.s),"r= ",str(si.r),"t= ",str(si.t))
si.s=10
si.r=5
si.t=20
print("Later:")
print("s= ",str(si.s),"r= ",str(si.r),"t= ",str(si.t))
calc=(si.s*si.r*si.t)/100
print(calc)