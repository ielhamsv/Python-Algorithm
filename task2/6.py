while True:
    x=int(input("enter number: "))
    i=1
    fact=1
    while i<=x:
        fact=fact*i
        i=i+1
    print("fact= ",fact)
    chek=input("edame?(y/n): ")
    if chek=="n":
        break
    else:
        continue
    
