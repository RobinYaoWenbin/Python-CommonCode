# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 09:14:35 2019

@author: wenbin
"""

"""
K链翻转是指把K个相邻的结点看成一组进行翻转,如果剩余结点不足K个,则保持不变.假设给定链表1->2->3->4->5->6->7和一个数K,
如果K的值为2,那么翻转后的链表为2->1->4->3->6->5->7.如果K的值为3,那么翻转后的链表为:3->2->1->6->5->4->7.

Solution idea: my idea is to solve this problem by two steps. The first step is create a function 
that helps me reverse the sub-linked list. In details, i give the pre pointer and latter pointer of the 
sub-linked list, then the function return the reversed list that is totally reversed between pre pointer and latter pointer.(func KFlip)
Then i use a function KFlipLL() to reverse the full liked list. It is easy that a cycle can finish this.
"""

import math

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
    temp = Pointer.Next
    for i in range(Length):
        print(temp.Data , " -> " , end = "")
        temp = temp.Next
    print("None")

def KFlip(Pointer , k):
    # reverse the linked list that the head is pointer, and the length is k.
    FirstPoin = Pointer.Next
    temp = Pointer.Next
    prePoi = Pointer
    tempNext = None
    for i in range(k):
        tempNext = temp.Next
        temp.Next = prePoi
        prePoi = temp
        temp = tempNext
    Pointer.Next = prePoi
    FirstPoin.Next = tempNext

def KFlipLL(Pointer , k):
    Length = Pointer.Data
    temp = Pointer
    for i in range( math.floor(Length / k) ):
        KFlip(temp , k)
        for j in range(k):
            temp = temp.Next

if __name__ == "__main__":
    Head = ConstructLL()
    print("The linked list is : ")
    Display(Head)
    KFlipLL(Head , k = 3)
    print("The linked list after k flipped is :")
    Display(Head)
