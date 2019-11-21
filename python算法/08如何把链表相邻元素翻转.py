# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:05:46 2019

@author: wenbin
"""

"""
把链表相邻元素翻转,例如给定链表为1->2->3->4->5->6->7,则翻转后的链表变为2->1->4->3->6->5->7
"""

class LNode:
    def __init__(self , x = 0 , y = None):
        self.Data = x
        self.Next = y

def ConstructLL():
    k = 7
    Head = LNode(k)
    temp = Head
    for i in range(k):
        temp.Next = LNode((i + 1))
        temp = temp.Next
    return Head

def Display(Pointer):
    Length = Pointer.Data
    temp = Head
    for i in range(Length):
        temp = temp.Next
        print(temp.Data , " -> " , end = "")
    print("None")

def AdjacentElementFlip(Pointer):
    prePoin = Pointer
    Poin = prePoin.Next
    latPoin = Poin.Next

    while True:
        prePoin.Next = latPoin
        Poin.Next = latPoin.Next
        latPoin.Next = Poin
        if Poin.Next != None and Poin.Next.Next != None :
            prePoin = Poin
            Poin = prePoin.Next
            latPoin = Poin.Next
        else:
            break
    return Pointer

if __name__ == "__main__":
    Head = ConstructLL()
    print("The linked list is : ")
    Display(Head)
    Head = AdjacentElementFlip(Head)
    print("The linked list after fliping is : ")
    Display(Head)