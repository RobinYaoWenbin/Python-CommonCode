# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 13:29:51 2019

@author: wenbin
"""

"""
假设给定链表1->2->3->4->5->6->7中指向第5个元素的指针,要求把结点5删掉,删除后链表变为1->2->3->4->6->7
"""

class LNode:
    def __init__(self , x = 0 , y = None):
        self.Data = x
        self.Next = y

def ConstructLL(k):
    Head = LNode(k)
    temp = Head
    for i in range(k):
        temp.Next = LNode( (i + 1) )
        temp = temp.Next
    return Head

def Display(Pointer):
    Length = Pointer.Data
    temp = Pointer.Next
    for i in range(Length):
        print(temp.Data , " -> " , end = "")
        temp = temp.Next
    print("None")

def GetPointer( Pointer , k ):
    temp = Pointer
    for i in range(k):
        temp = temp.Next
    return temp

def DelNode(Head , k):
    Poi = GetPointer(Head , 5)
    NextPoi = Poi.Next
    Poi.Data = NextPoi.Data
    Poi.Next = NextPoi.Next
    Head.Data = Head.Data - 1
    return Head

if __name__ == "__main__":
    Head = ConstructLL(7)
    print("The linked list is : ")
    Display(Head)
    Head = DelNode(Head , 5)
    print("The linked list after deleting one of the pointer is : ")
    Display(Head)