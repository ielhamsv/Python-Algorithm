L1= [1,"python",2,"DB"]
L2=[100,'John',101,'Smith']
L2[0:0]=[1000]
print("a: ",L2)
L3=L2+L1
print("b: ",L3)
if "python" in L3:
    print("c: ","وجود دارد")
else:
    print("c: ","وجود ندارد")
    
