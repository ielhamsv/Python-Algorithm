def list(n):
    l=[]
    
    for i in range(n):
        x=int(input("x: "))
        l.append(x)
    l.sort()
    return l
    

n=int(input("n: "))
print(list(n))
