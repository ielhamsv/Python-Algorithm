print("""
a. whitespace تعداد کاراکتر هاي
b. تعداد کاراکتر هاي کوچک
c. تعداد کاراکتر هاي بزرگ
d. تعداد ارقام
e. تعداد کاراکتر هاي خاص
f. مجموع ارقام رشته
""")
def whitespace(s):
    a=0
    for i in s:
        if i==" ":
            a=a+1
    print("a= ",a)    

def lower(s):
    b=0
    for i in s:
        if i.islower():
            b=b+1
    print("b= ",b)

def upper(s):
    c=0
    for i in s:
        if i.isupper():
            c=c+1
    print("c= ",c)
def number(s):
    d=0
    for i in s:
        if i.isdigit():
            d=d+1
    print("d= ",d)
def khas(s):
    e=0
    for i in s:
        if not i.isalnum():
            
            e=e+1
    print("e= ",e)
def sume(s):
    f=0
    for i in s:
        if i.isdigit():
            f=f+int(s[i])
    print(f)
s=input("enter string: ")
A=whitespace(s)
B=lower(s)
C=upper(s)
D=number(s)
E=khas(s)
F=sume(s)
print("a=%d"(A))
print("b={}".format(B))
print(f"c={C}")
print("d=%d"(D))
print("e=%d"(E))
print("f=%d"(F))            
        
      




            
