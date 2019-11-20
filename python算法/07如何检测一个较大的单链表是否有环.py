# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:35:58 2019

@author: wenbin
"""

"""
单链表有环指的是单链表中某个结点的next域指向的是链表中在它之前的某一个结点,
这样在链表的尾部形成一个环形结构.如何判断单链表是否有环存在?
"""

class LNode:
    def __init__(self , x = 0 , y = None):
        self.Data = x
        self.Next = y

def ConstructLL():
    k = 7
    Head1 = LNode(k)  # new a linked list that does not have the ring
    temp = Head1
    for i in range(k):
        temp.Next = LNode((i + 1))
        temp = temp.Next
    Head2 = LNode(k)  # new a linked list that has the ring
    temp = Head2
    for i in range(k):
        temp.Next = LNode((i + 1))
        temp = temp.Next
    temp2 = Head2
    for i in range(3):
        temp2 = temp2.Next
    temp.Next = temp2
    return Head1 , Head2

def DisplayLL(Pointer):
    Length = Pointer.Data
    temp = Pointer.Next
    for i in range(Length):
        print(temp.Data , " -> " , end = "")
        temp = temp.Next
    if temp != None :
        print(temp.Data)
    else:
        print("None")

def DetectRing(Pointer):
    PoinSet = set()
    temp = Pointer
    while temp != None and temp not in PoinSet:
        PoinSet.add(temp)
        temp = temp.Next
    if temp == None:
        print("The linked list has no ring!")
    elif temp in PoinSet:
        print("The linked list has a ring! And the ring's entrance is " , temp.Data)

if __name__ == "__main__":
    Head1 , Head2 = ConstructLL()
    print("The first linked list without ring is:")
    DisplayLL(Head1)
    print("The second linked list with ring is:")
    DisplayLL(Head2)
    DetectRing(Head1)
    DetectRing(Head2)