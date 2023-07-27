def List():
    l1=[]
    l2=[]
    x=int(input("number of first list items: "))
    for i in range(x):
        l1.append(input("first: "))
        
    y=int(input("number of second list items: "))    
    for j in range(y):
        l2.append(input("second: "))
    l1.sort(True)
    l2.sort(True)
    return l1,l2
List()
print("""
Append-1
Extend -2
Insert -3
Remove -4
Search -5
Display -6
Exit -7
""")
def one(l):
    s=input("enter string: ")
    L=l.append(s)
print(L)
def two(l):
    s=input("enter string: ")
    L=l.extend(s)
print(L)
def three(l):
    i=int(input("enter makan: "))
    L=l1.insert(i,l2)
print(L)
def four(l):
    x=int(input("x: "))
    L=l.remove(x)
print(L)
def five(l):
    x=int(input("x: "))
    if x in l:
        L=l.index(x)
    else:
        print("در ليست وجود ندارد")
    print(L)
def six():
    print(l1,l2)
while True:
    c=int(input("Enter your choice: "))
    if c==1:
        x=input("l1 or l2? ")
        if x=="l1":
            l=l1
        else:
            l=l2
        one(l)
    elif c==2:
        x=input("l1 or l2? ")
        if x=="l1":
            l=l1
        else:
            l=l2
        two(l)
    elif c==3:
        x=input("l1 or l2? ")
        if x=="l1":
            l=l1
        else:
            l=l2
        three(l)
    elif c==4:
        x=input("l1 or l2? ")
        if x=="l1":
            l=l1
        else:
            l=l2
        four(l)
        
    elif c==5:
        x=input("l1 or l2? ")
        if x=="l1":
            l=l1
        else:
            l=l2
        five(l)
    elif c==6:
         six()
    else:
        break


    
