s=input("Enter string: ")
string="Hello"
print("a: ",string+" "+s)
n=int(input("Enter n: "))
print("b: ",s[n])
s2=input("Enter new string: ")
if s2 in s:
    print("c: ","وجود دارد")
else:
    print("c: ","وجود ندارد")
