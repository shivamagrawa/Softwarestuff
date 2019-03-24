world={"IND" :{"MAH" :["c1","c2"],"UP" :["c3","c4"], "MP" :["c5","c6"]},"USA" :{"ST1" :["C1","c2"],"ST2" :["C3","C4"],"ST3" :["c5","c6"]}}
for countryName in world:
    print(countryName)
    statemap=world[countryName]
    for stateName in statemap:
        print("\t - "+stateName)
        
        cities=statemap[stateName]
        for cityName in cities:
                print("\t \t -"+str(cityName))



d = {"k1":"v1", "k2":"v2"}

var = ""
for key in d:
    var = var + key + " : " + d[key] + ","
    print(var[ :len(var)])
