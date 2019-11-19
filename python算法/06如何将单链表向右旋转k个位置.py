# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 10:48:08 2019

@author: Wenbin
"""

"""
给定链表1->2->3->4->5->6->7,k = 3,那么旋转后的单链表变为5->6->7->1->2->3->4
"""

class LNode:
    def __init__(self , x = 0 , y = None):
        self.Data = x
        self.Next = y

def ConstructLinkedList(k):
    Head = LNode(x = k)
    temp = Head
    for i in range(k):
        temp.Next = LNode(x = (i + 1) )
        temp = temp.Next
    return Head

def Display(Pointer):
    temp = Pointer.Next
    while temp.Next != None:
        print(temp.Data , " -> " , end = "")
        temp = temp.Next
    print(temp.Data)

def RotateLinkedList(Pointer , k):
    Length = Pointer.Data
    temp = Pointer
    for i in range(Length - k):
        temp = temp.Next
    HNext = Pointer.Next
    Pointer.Next = temp.Next
    temp.Next = None
    temp = Pointer
    while temp.Next != None:
        temp = temp.Next
    temp.Next = HNext
    return Pointer


if __name__ == "__main__":
    Head = ConstructLinkedList(7)
    print("The Linked List is:")
    Display(Head)
    Head = RotateLinkedList(Head , 3)
    Display(Head)
