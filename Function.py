def genCities(arg1,arg2=1,arg3=5):
    l=[]
    for i in range(arg2,arg3+1):
        rs=arg1 +"_Cities_" +str(i)
        l.append(rs)
    return l

def stateMap(*args):
    d={}
    for item in args:
        d[item]=genCities(item)
    return d

def worldMap():
    wmap={}
    wmap["IND"]=stateMap("UP","MP","MAH")
    wmap["US"]=stateMap("Califonia","NewYork","Sanfransisco")
    return wmap

world=worldMap()


for countryName in world:
    print(countryName)
    stateMap=world[countryName]
    for stateName in stateMap:
        print("\t -" +stateName)
        cities=stateMap[stateName]
        for city in cities:
            print("\t \t"+str(city))
