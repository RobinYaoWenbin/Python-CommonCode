# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 18:39:10 2019

@author: wenbin
"""

"""
单链表相交指的是两个链表存在完全重合的部分,如下图所示:(书本第51页)
在上图中,这两个链表相交于结点5,要求判断两个链表是否相交,如果相交,找出相交处的结点.
"""

class LNode:
    def __init__(self , x = 0 , y = None):
        self.Data = x
        self.Next = y

def ConstructLL1():
    k = 7  # total length of the linked list
    m = 4  # different linked list's length
    Head1 = LNode(k) ; Head2 = LNode(k)
    temp1 = Head1 ; temp2 = Head2
    for i in range(m):
        temp1.Next = LNode((i + 1))
        temp1 = temp1.Next
        temp2.Next = LNode((i + 1))
        temp2 = temp2.Next
    temp1.Next = LNode(x = m + 1)
    temp1 = temp1.Next
    temp2.Next = temp1
    for i in range(k - m - 1):
        temp1.Next = LNode(k - m + i + 3)
        temp1 = temp1.Next
    return Head1 , Head2

def ConstructLL2():
    k = 7
    Head1 = LNode(k) ; Head2 = LNode(k)
    temp1 = Head1 ; temp2 = Head2
    for i in range(k):
        temp1.Next = LNode((i + 1))
        temp1 = temp1.Next
        temp2.Next = LNode((i + 1))
        temp2 = temp2.Next
    return Head1 , Head2

def Display(Pointer):
    Length = Pointer.Data
    temp = Pointer.Next
    for i in range(Length):
        print(temp.Data , " -> " , end = "")
        temp = temp.Next
    print("None")

def JudgeCross(Poi1 , Poi2):
    NodeSet1 = set() ; NodeSet2 = set()
    cur1 = Poi1.Next ; cur2 = Poi2.Next
    while cur1 != None and cur2 != None:
        NodeSet1.add(cur1) ; NodeSet2.add(cur2)
        cur1 = cur1.Next ; cur2 = cur2.Next
    while cur1 != None:
        NodeSet1.add(cur1)
        cur1 = cur1.Next
    while cur2 != None:
        NodeSet2.add(cur2)
        cur2 = cur2.Next
    Intsec = NodeSet1 & NodeSet2
    cur1 = Poi1.Next
    while cur1 != None:
        if cur1 in Intsec:
            return cur1
        else:
            cur1 = cur1.Next
    return None

if __name__ == "__main__":
    Head1 , Head2 = ConstructLL1()
    print(" Two linked list that we created are : ")
    Display(Head1)
    print("and")
    Display(Head2)
    flag = JudgeCross(Head1 , Head2)
    if flag == None:
        print(" Two linked lists do not cross!")
    else:
        print("Two linked lists do cross , and the crossing node's data is : " , flag.Data)

    Head1 , Head2 = ConstructLL2()
    print(" Two linked list that we created are : ")
    Display(Head1)
    print("and")
    Display(Head2)
    flag = JudgeCross(Head1 , Head2)
    if flag == None:
        print(" Two linked lists do not cross!")
    else:
        print("Two linked lists do cross , and the crossing node's data is : " , flag.Data)