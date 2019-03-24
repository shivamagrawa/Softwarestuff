student={"name":"Shivam Agrawal","age":28, "contacts":[{"tag":"Personal","number":8975388414},{"tag":"Office","number":9422420302}]}
print(student)
studentList=student['contacts']
print(studentList)

for item in studentList:
    print(item)
    print(item["tag"])


s={1,2,4,7}

l={9,3,4,6}

print(l)
s=set(l)
print(s)
s.add(8)
print(s)


d = [{"tag":"Official", "number" :"8983237271"},{"tag":"Personell", "number" :"1234567890"} ]

dd=d[0]
print(dd)
dd=d[1]
print(dd)
for dd in d:
     print(dd["tag"])
     print(dd["number"])

