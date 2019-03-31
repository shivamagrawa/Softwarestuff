a=1
b=2

sum=(a+b)
print(sum)

def m1():
    print("Inside Python Function/method")

m1()

def m2():
    c=3
    d=4
    print(c+d)
m2()

def m3(agr1, arg2):
    a=agr1
    b=arg2
    print(a+b)
    print(a,b)
m3(9,7)
m3(7,8)
def m4(arg1=4,arg2=5):
    a=arg1
    b=arg2
    sum=a+b
    print(a+b)
    print(a,b)
m4(2,6)
m4(6)

def m5(arg1=None):
    print(arg1)
m5()

def m6(arg1,arg2=None):
    print(arg1)
    print(arg2)
m6(1)
m6(2,3)
m6(1,"Another Value")

def m7(arg1,arg2):
    sum=arg1+arg2
    return sum
d=m7(1,2)
print(d)

def m8(arg1):
    print(type(arg1))
l=[1,2,3,4]
m8(l)
m8("ABC")
m8((1,2,3))
m8({"a":"A"})


def m9(*args):
    print(type(args))
    sum=0
    for item in args:
        sum+=item
    return sum
print(m9(1,2,23,4))



def m10(**kvargs):
    print(type(kvargs))
    return kvargs
print(m10(Name="ABC",Age="23"))
