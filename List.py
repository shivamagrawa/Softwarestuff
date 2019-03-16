l=[1,2,3,"Shivam","Agrawal"]
print(l)

print("Fourth Index : "+str(l[4]))

print("First Index : "+str(l[0]))

print(l[0:4])

print("Before "+str(len(l)))
l.append("Adding another value in list")
print(l)
print("After "+str(len(l)))



s=l[2]
print(s)

l[1]="yes"
s=l[1]
print(l)
print(s)

for item in l:
    print("List of value: "+str(item))


l1=["New String","List"]
print(l)

l.extend(l1)
print(l)

l.append(l1)
print(l)
print("Print with str: "+str(l))


s=[4,2,5,1]
a=["xyz","abc"]
print(a.sort())
print(s.sort())
print(s)
print(a)

print(s)

for item in range(1,10):
    print(item)
print(type(item))


print(l)

v=l.pop()
print("print item is :"+str(v))


v=l.pop(3)
print("print item is :"+str(v))

print(l)



t = ()
t = (1,3,4,5)
t = (1,3,4,"asdasd","asdas")

# Accessing # reading.
print(t[0])

print(t)

l = ["one", "two"]

t = (1,2,3, l)


l = t[3]# assign list to variable l.

print(type(l))

print(l)

l.append("three...")
print(l)
print(t)

print(t.index(3))

