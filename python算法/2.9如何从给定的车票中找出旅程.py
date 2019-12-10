# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 18:53:36 2019

@author: wenbin
"""

"""
给定一趟旅途中所有的车票信息,根据这个车票信息找出这趟旅程的路线.例如:给定下面的车票:(从西安到成都),(北京到上海),
(大连到西安),(上海到大连).那么可以得到旅程路线为 北京->上海,上海->大连,大连->西安,西安->成都.假定给定的车票不会有环,
也就是说有一个城市只作为终点而不会作为起点.
"""

def GetTickets():
    TicketList = []  # new a list to store the traveling tickets
    TicketList.append(("西安" , "成都"))
    TicketList.append(("北京" , "上海"))
    TicketList.append(("大连" , "西安"))
    TicketList.append(("上海" , "大连"))
    return TicketList

def FindOrigin(TicketList):
    CitySet = set()
    for ticket in TicketList:
        CitySet.add(ticket[1])
    for ticket in TicketList:
        if ticket[0] not in CitySet:
            return ticket[0]

def FindNext(TicketList , Fir):
    # find the next site that is next to Fir
    for i in range(len(TicketList)):
        if TicketList[i][0] == Fir:
            return TicketList[i][1]

def GetTravelRoute():
    # find the traveler's travel route
    TicketList = GetTickets()
    RouLen = len(TicketList) + 1
    Ori = FindOrigin(TicketList)
    Route = [Ori]
    while len(Route) < RouLen:
        Route.append(FindNext(TicketList , Route[-1]))
    print("The traveler's route is : " , Route)

def EasierMethod():
    TicketList = GetTickets()
    TicketHash = dict()
    for index in range(len(TicketList)):
        TicketHash[TicketList[index][0]] = TicketList[index][1]
    Ori = FindOrigin(TicketList)
    RouLen = len(TicketList) + 1
    Route = [Ori]
    while len(Route) < RouLen:
        Route.append(TicketHash[Route[-1]])
    print("The traveler's route is : " , Route)

if __name__ == "__main__":
    # GetTravelRoute()  # a complex method, the time complexity is O(n2)
    EasierMethod()  # easier method, the time method is O(n)