# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 22:12:12 2019

@author: wenbin
"""

"""
给定一个没有排序的链表，去掉其重复项，并保留原顺序，例如链表1->3->1->5->5->7,result:1->3->5->7
"""

class LNode:
    def __init__(self , num = 0 , node = None):
        self.Data = num
        self.Next = node

def InputData():
    # input data
    Length = int(input("Please input the length of data: "))
    Head = LNode(Length , None)
    Temp = Head
    for i in range(Length):
        InputData = int(input("the node's data: "))
        Temp.Next = LNode(InputData , None)
        Temp = Temp.Next
    return Head

def RemoveDuplicates(Head):
    # remove the duplicates from the linked list
    DifferEle = []
    Temp = Head
    Last = Head
    while Last.Next != None:
        if Temp.Data not in DifferEle and Temp != Head:
            DifferEle.append(Temp.Data)
        elif Temp.Data in DifferEle and Temp != Head:
            Last.Next = Temp.Next
        Last = Temp
        Temp = Temp.Next
    return Head

def Output(Head):
    Temp = Head
    while Temp.Next != None :
        if Temp != Head:
            print(Temp.Data , " -> ", end = "")
        Temp = Temp.Next
    print(Temp.Data)

if __name__ == "__main__":
    Head = InputData()
    Head = RemoveDuplicates(Head)
    Output(Head)