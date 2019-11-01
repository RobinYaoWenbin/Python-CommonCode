# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 16:43:12 2019

@author: wenbin
"""

"""
给定链表L0->L1->L2```Ln-1->Ln,把链表重新排序为L0->Ln->L1->Ln-1->L2->Ln-2```。要求:(1)在原来链表的基础上进行排序,即不能申请新的
节点;(2) 只能修改节点的next域,不能修改数据域
"""
import math

class LNode:
    def __init__(self , x = 0 , Point = None):
        self.Data = x
        self.Next = Point

def GetData():
    Head = LNode(9)
    Temp = Head
    for i in range(Head.Data):
        Temp.Next = LNode(i+1)
        Temp = Temp.Next
    return Head

def OutPut1(Head):  # output the Linked list that has the head
    Temp = Head
    while Temp != None :
        if Temp != Head and Temp.Next != None:
            print(Temp.Data , " -> " , end = "")
        elif Temp != Head and Temp.Next == None:
            print(Temp.Data , end = "")
        Temp = Temp.Next
    print("")

def OutPut2(Head):  # output the Linked list that do not have the head
    Temp = Head
    while Temp != None :
        if Temp.Next != None:
            print(Temp.Data , " -> " , end = "")
        elif Temp.Next == None:
            print(Temp.Data , end = "")
        Temp = Temp.Next
    print("")

def GetMiddle(Head):
    Length = Head.Data
    Middle = math.ceil(Length / 2)
    Temp = Head
    for i in  range(Middle):
        Temp = Temp.Next
    return Temp

def ReverseLinkedList(LinkList):
    # Reverse the Linked list that does not have Head
    Temp = LinkList
    NextNode = LinkList.Next
    LastNode = None
    while NextNode != None:
        Temp.Next = LastNode
        LastNode = Temp
        Temp = NextNode
        NextNode = NextNode.Next
    Temp.Next = LastNode
    return Temp

def MergeTwoLL(Head , ReverseLL):
    Temp1 = Head.Next
    Temp1Next = Temp1.Next
    Temp2 = ReverseLL
    Temp2Next = Temp2.Next
    while (Temp1 != None) and (Temp2 != None):
        Temp1Next = Temp1.Next
        Temp1.Next = Temp2 
        Temp2Next = Temp2.Next
        Temp2.Next = Temp1Next
        Temp1 = Temp1Next
        Temp2 = Temp2Next
    return Head

def ResortLinkedList(Head):
    Middle = GetMiddle(Head)
    # OutPut2(Middle)
    ReverseLL = ReverseLinkedList(Middle)
    # OutPut2(ReverseLL)
    Head = MergeTwoLL(Head , ReverseLL)
    return Head


if __name__ == "__main__":
    Head = GetData()
    print("Original Linked List: ")
    OutPut1(Head)
    Head = ResortLinkedList(Head)
    print("Reversed Linked ListL: ")
    OutPut1(Head)