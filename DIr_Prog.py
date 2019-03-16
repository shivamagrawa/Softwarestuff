d={}
d={"key_1":"Val_1", "Key_2":"Val_2"}

print(d)

value=d['key_1']
print(value)



l=[1,2,3]

value=l[2]

print(value)

d['key_3']="New Valuie"

print(d)

d['key_3'] = "Another New value..."

print(d)


for key in d:
    print(str(key)+" " +str(d[key]))

print(d.keys())
print(type(d.keys()))


