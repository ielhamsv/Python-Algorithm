def tekrar(x,n):
    k=x//10
    number=0
    while k!=0: 
        b=x%10
        if b==n:
           number=number+1
        k=x//10   
        x=k    
    print("tekrar: ",number) 
x=int(input("x: "))        
n=int(input("n: "))
tekrar(x,n)
