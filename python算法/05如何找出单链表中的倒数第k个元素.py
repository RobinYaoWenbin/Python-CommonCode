# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 22:10:26 2019

@author: wenbin
"""

"""
找出单链表中的倒数第k个元素,例如给定单链表:1->2->3->4->5->6->7,则单链表的倒数第k=3个元素为5.
"""

class LNode():
    def __init__(self , x = 0 , next = None):
        self.Data = x
        self.Next = next

def InputData():
    Length = int(input("Please input the length of the linked list:"))
    Head = LNode(x = Length , next = None)
    temp = Head
    for i in range(Length):
        temp.Next = LNode(x = int(input("Node's data:")) , next = None)
        temp = temp.Next
    return Head

def Display(Head):
    Length = Head.Data
    temp = Head.Next
    for i in range(Length - 1):
        print(temp.Data , " -> " , end = "")
        temp = temp.Next
    print(temp.Data)

def GetkElementReverse(Head ):
    k = int(input("Please input the reversed order that you would like to get:"))
    Length = Head.Data
    n = Length - k
    temp = Head
    for i in range(n):
        temp = temp.Next
    print(temp.Next.Data)

def GetkElementReverse2(Head ):
    k = int(input("Please input the reversed order that you would like to get:"))
    PointerQuick = Head
    PointerSlow = Head
    for i in range(k):
        PointerQuick = PointerQuick.Next
    while PointerQuick != None:
        PointerQuick = PointerQuick.Next
        PointerSlow = PointerSlow.Next
    print(PointerSlow.Data)


if __name__ == "__main__":
    Head = InputData()
    print("The linked list that input is: ")
    Display(Head)
    GetkElementReverse2(Head)

