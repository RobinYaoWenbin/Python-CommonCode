# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 21:24:50 2019

@author: Yaocwenbin
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

解决思路:(该问题更好的解决办法)
使用归并排序中的合并操作，使用归并的方法把这些链表来逐个归并.
使用递归的方法,递归地合并已经扁平化地链表与当前地链表.在使用过程中使用Down指针储存扁平化处理后地链表.
该方法时间复杂度是O(n),空间复杂度是O(1)
"""

class Node:
    def __init__(self , data):
        self.Data = data
        self.Next = None
        self.Down = None

class MergeLinkedList:
    def __init__(self):
        self.head = None

    def Merge(self ,a , b):
        if a == None:
            return b
        if b == None:
            return a
        if a.Data < b.Data:
            result = a
            result.Down = self.Merge(a.Down , b)
        else:
            result = b
            result.Down = self.Merge(a , b.Down)
        return result

    def flatten(self , root):
        if root == None or root.Next == None:
            return root
        root.Next = self.flatten(root.Next)
        root = self.Merge(root , root.Next)
        return root

    def Insert(self , head_ref , data):
        new_node = Node(data)
        new_node.Down = head_ref
        head_ref = new_node
        return head_ref

    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.Data , " -> " , end = "")
            temp = temp.Down
        print("None")

if __name__ == "__main__":
    L = MergeLinkedList()
    L.head = L.Insert(L.head , 31)
    L.head = L.Insert(L.head , 8)
    L.head = L.Insert(L.head , 6)
    L.head = L.Insert(L.head , 3)
    L.head.Next = L.Insert(L.head.Next , 21)
    L.head.Next = L.Insert(L.head.Next , 11)
    L.head.Next.Next = L.Insert(L.head.Next.Next , 50)
    L.head.Next.Next = L.Insert(L.head.Next.Next , 22)
    L.head.Next.Next = L.Insert(L.head.Next.Next , 15)
    L.head.Next.Next.Next = L.Insert(L.head.Next.Next.Next  , 55)
    L.head.Next.Next.Next = L.Insert(L.head.Next.Next.Next  , 40)
    L.head.Next.Next.Next = L.Insert(L.head.Next.Next.Next  , 39)
    L.head.Next.Next.Next = L.Insert(L.head.Next.Next.Next  , 30)
    L.head.Next.Next.Next = L.flatten(L.head)
    L.printList()
