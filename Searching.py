import pandas as pd
xl=pd.ExcelFile("Travel Agent KB (2 sheets).xlsx")
df=xl.parse('Travel')
print(df)


Exel = xl
listOfcity = Exel.Cities
ListeOftime = Exel.Ttime

def GetCity(element, list):
    for i in range(len(list)):
        if element == list[i].name:
            return list[i]

def GetTimeT(City, Ttime):
    name = City.name
    ReturnL = []
    for i in range(len(Ttime)):
        if name == Ttime[i].city1:
            ReturnL.append(Ttime[i])
    return ReturnL

def CheckDay(Frange, Flights):
    ReturnL = []
    for k in range(len(Flights)):
        Dlist = Flights[k].days
        for i in range(len(Frange)):
            for j in range(len(Dlist)):
                if Frange[i] == Dlist[j]:
                    ReturnL.append([Dlist[j],Flights[k].Dtime,Flights[k].Atime])
    return ReturnL

def check_SpaceTime(foundedList, SpaceTime):
    for i in range(len(foundedList)):
        fo = foundedList[i]
        day = fo[0]
        Dtime = fo[1]
        arrTime = fo[2]
        for j in range(len(SpaceTime)):
            day2 = SpaceTime[j][0]
            Dtime2 = SpaceTime[j][1]
            arrTime2 = SpaceTime[j][2]
            if day == day2:
                L1 = Dtime.split(":")
                L2 = arrTime.split(":")
                L3 = Dtime2.split(":")
                L4 = arrTime2.split(":")
                if L1[0] <= L4[0] or L2[0] >= L3[0]:
                    return []
                elif list1[0] == L4[0] and L1[1] <= L4[1]:
                    return []
                elif list2[0] == L3[0] and L2[1] >= L4[1]:
                    return []
            return fo
    return foundedList[0]

def As_Searching(departure, destination, Ttime, SpaceTime, Frange, Olist):
    if departure == destination:
        for i in range(len(Olist)):
            print("Deparcure from "+ Olist[i][0] +" to "+Olist[i][1]+" on "+ Olist[i][2] + "in Dayes " + Olist[i][3] + " : " + Olist[i][4])
        return 
    Dcity = GetCity(departure,listOfcity)
    listOfcity.remove(dcity)
    edges = GetTimeT(dcity,ListeOftime)
    dummyHeuristic = 1000
    suitableDay = None
    suitableDepart = None
    suitableArr = None
    suitableTable = None
    for i in range(len(edges)):
        flightsList = edges[i].Flights
        foundedList = CheckDay(Frange,flightsList)
        if len(foundedList) > 0:
            Spacival = check_SpaceTime(foundedList,SpaceTime)
            if len(Spacival) > 0:
                Ncity = GetCity(edges[i].city2,listOfcity)
                if Ncity.name == departure:
                    heuristic = Exel.calculateTime(Spacival[1],Spacival[2])
                else:
                    heuristic = Exel.calculateDistance(dcity,Ncity) + Exel.calculateTime(Spacival[1],Spacival[2])
                if heuristic < dummyHeuristic:
                    dummyHeuristic = heuristic
                    suitableDay = Spacival[0]
                    suitableTable = edges[i]
                    suitableDepart = Spacival[1]
                    suitableArr = Spacival[2]

    newSpacival = [suitableDay,suitableDepart,suitableArr]
    SpaceTime.append(newSpacival)
    newOpen = [departure,suitableTable.city2,suitableDay,suitableDepart,suitableArr]
    Olist.append(newOpen)
    Ttime = Ttime + Exel.calculateTime(suitableDepart,suitableArr)
    if len(Olist) > 0:
        time2 = Olist[len(Olist)-1][4]
        Ttime = Ttime + Exel.calculateTime(time2,suitableDepart)
    if Ttime >= 12:
        Frange[0] = Exel.getNext(Frange[0])
        Ttime = Ttime - 12
    As_Searching(suitableTable.city2, destination, Ttime, SpaceTime, Frange, Olist)



