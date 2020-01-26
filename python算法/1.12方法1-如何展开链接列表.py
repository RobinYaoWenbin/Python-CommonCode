# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 15:36:11 2019

@author: Yao wenbin
"""

"""
题目描述:
给定一个有序链表,其中每个结点也表示一个有序列表,结点包含两个类型的指针:
(1) 指向主链表中下一个结点的指针;
(2) 指向此结点头的链表;
所有链表都被排序.请参见以下示例:
3 -> 11 -> 15 -> 30
|v   |v    |v    |v
6    21    22    39
|v         |v    |v
8          50    40
|v               |v
31               55
实现一个函数flatten(), 该函数用来将链表扁平化成单个链表,扁平化的链表也应该被排序.例如,对于上述的输入链表,输出的链表应该为:
3->6->8->11->15->21->22->30->31->39->40->45->50.

解决思路:
在构造链接列表时,就设置两种数据结构，一是主链表，二是子链表，主链表有两个指针域，分别指向主链表的下一个和子链表的下一个，
而子链表中的Node只有一个指针域，指向下一个Node.
设主链表的长度为L,则我设置L个指针,起始的时候分别指向主链表的各个Node,然后依次取出各个指针中最小的指针的数据域中的数据,
添加到新的单链表的最后，然后该指针在子链表中下移一格。
这种方法的时间复杂度是O(n),空间复杂度也是O(n).
"""

class LNode:
    """
    linked list's node, there are one pointer domains, one data domain
    """
    def __init__(self , x = 0 , y = None ):
        self.Data = x
        self.Right = y

    def Insert(self , data):
        """
        Insert a node to the next position of the LNode.
        input
        data : the inserting node's data
        """
        nextnode = self.Right
        self.Right = LNode(data)
        self.Right.Right = nextnode

class HeadNode(LNode):
    """
    define a node that is the head of the linked list.
    """
    def __init__(self , x = 0 , y = None):
        super(HeadNode , self).__init__(x , y)

    def Display(self):
        # display the linked list table
        Length = self.Data
        print("The  main linked list is : ")
        temp = self.Right
        while temp != None:
            print(temp.Data , " -> " , end = "")
            temp = temp.Right
        print("None")
        temphead = self.Right
        for i in range(Length):
            print("order {0} sub linked list is : ".format((i + 1)))
            print(temphead.Data , " -> " , end = "")
            temp = temphead.Down
            while temp != None:
                print(temp.Data , " -> " , end = "")
                temp = temp.Right
            print("None")
            temphead = temphead.Right

    def DisplaySingleList(self):
        # display the single linked list
        temp = self.Right
        while temp != None:
            print(temp.Data , " -> " , end = "")
            temp = temp.Right
        print("None")

    def flatten(self):
        """
        change the linked list table to the single linked list, remaining the single linked list is ordered.
        """
        PoiList = []  # store the pointer of the main linked list
        Length = self.Data
        temp = self.Right
        NewList = HeadNode( -5 )  # new a node, and set the length of the linked list as -5, because i still do not know the total length of the single linked list
        m = 0  # document the length of the linked list
        while temp != None:
            PoiList.append(temp)
            temp = temp.Right
        temp = NewList
        while len(PoiList) != 0:
            # delete the None value
            while None in PoiList:
                PoiList.remove(None)
            minPoi = PoiList[0]
            minj = 0
            for j in range(len(PoiList)):
                if PoiList[j].Data < minPoi.Data :
                    minPoi = PoiList[j]
                    minj = j
            temp.Right = LNode(minPoi.Data)
            m += 1
            temp = temp.Right
            if type(minPoi) == LNode:
                PoiList[minj] = minPoi.Right
            elif type(minPoi == MainNode):
                PoiList[minj] = minPoi.Down
            while None in PoiList:
                PoiList.remove(None)
        NewList.Data = m
        return NewList

class MainNode(LNode):
    """
    linked list table's main node, there are two pointer domains, one data domain
    """
    def __init__(self , x = 0 , y = None , z = None):
        self.Down = z
        super(MainNode , self).__init__(x , y)

    def Insert(self , data):
        nextnode = self.Right
        self.Right = MainNode(data)
        self.Right.Right = nextnode

def ConstructLinkedListTable():
    """
    create a ordered linked list, which is also the head of several other linked list.
    Here is the example that i have created:
    3 -> 11 -> 15 -> 30
    |v   |v    |v    |v
    6    21    22    39
    |v         |v    |v
    8          50    40
    |v               |v
    31               55
    I called it linked list table, because it looks like a table, which is indexd by a linked list.
    """
    Head = HeadNode(4)
    Head.Right = MainNode(3)
    Head.Right.Insert(30) ; Head.Right.Insert(15) ; Head.Right.Insert(11)
    temphead = Head.Right
    temphead.Down = LNode(6)
    temphead.Down.Insert(31) ; temphead.Down.Insert(8)
    temphead = temphead.Right
    temphead.Down = LNode(21)
    temphead = temphead.Right
    temphead.Down = LNode(22)
    temphead.Down.Insert(50)
    temphead = temphead.Right
    temphead.Down = LNode(39)
    temphead.Down.Insert(55) ; temphead.Down.Insert(40)
    return Head


if __name__ == "__main__":
    Head = ConstructLinkedListTable()
    Head.Display()
    NewList = Head.flatten()
    print("After flattening , the single linked list is : ")
    NewList.DisplaySingleList()