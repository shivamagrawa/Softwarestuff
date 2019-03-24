class World_Map_Class:
    def __init__(self):
        print("inside Constructor..."+str(type(self)))

    def m1(self):
        d={}
        d={"key_1":"Val_1", "Key_2":"Val_2"}
        print("Inside m1")
        Collect_m3=self.m3()
        print("Value return is :" +str(Collect_m3))
        value=Collect_m3
        d={"MAH":value}
        print(d)

        for key in d:
            print(str(key)+" " +str(d[key]))


    def m2(self):
        print("Inside m2")
        self.m1()
        result = ""
        return result

    def m3(self):
        s=[2,1,6,6]
        s.sort()
        #print(s)
        City_List=[]
        for i in range(1,5):
            city = "City-" + str(i)
            print (city)
            City_List.append(city)
        return City_List


World_Map_Class= World_Map_Class()
print(World_Map_Class.m2())
