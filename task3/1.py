def z(a,b=200):
    zog=0
    for i in range(a,b+1):
        if i%2==0:
            zog=zog+1
        
        i=i+1
    print("zog= ",zog)
x=int(input("x: "))
y=int(input("y: "))
z(x,y)
z(x)
