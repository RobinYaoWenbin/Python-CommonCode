# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 12:24:54 2019

@author: wenbin
"""

"""
已知两个链表head1和head2各自有序(例如升序排列),请把它们合并成一个链表,要求合并后的链表依然有序.
"""

class LNode:
    def __init__(self , x = 0 , y = None):
        self.Data = x
        self.Next = y

def ConstructLL(l1 , l2):
    Head1 = LNode(l1)
    temp = Head1
    for i in range(l1):
        temp.Next = LNode((2 * i + 1))
        temp = temp.Next

    Head2 = LNode(l2)
    temp = Head2
    for i in range(l2):
        temp.Next = LNode((2 * i + 2))
        temp = temp.Next
    return Head1 , Head2

def Display(Pointer):
    Length = Pointer.Data
    temp = Pointer.Next
    for i in range(Length):
        print(temp.Data , " -> " , end = "")
        temp = temp.Next
    print("None")

def MergeLL(Pointer1 , Pointer2):
    Poi1 = Pointer1.Next ; Poi2 = Pointer2.Next
    Length = Pointer1.Data + Pointer2.Data
    MerLL = LNode(Length)
    temp = MerLL
    while Poi1 != None and Poi2 != None:
        if Poi1.Data < Poi2.Data:
            temp.Next = LNode(x = Poi1.Data)
            Poi1 = Poi1.Next
            temp = temp.Next
        elif Poi1.Data >= Poi2.Data:
            temp.Next = LNode(x = Poi2.Data)
            Poi2 = Poi2.Next
            temp = temp.Next
    if Poi1 == None:
        temp.Next = Poi2
    elif Poi2 == None:
        temp.Next = Poi1
    return MerLL


if __name__ == "__main__":
    Head1 , Head2 = ConstructLL(l1 = 4 , l2 = 3)
    print("The first linked list is : ")
    Display(Head1)
    print("The second linked list is : ")
    Display(Head2)
    MerLL = MergeLL(Head1 , Head2)
    print("The merged linked list is : ")
    Display(MerLL)
