# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 11:11:47 2020

@author: Administrator
"""

"""
输入一棵二元查找树,将该二元查找树转换成一个排序的双向链表.要求不能创建任何新的结点,只能调整结点的指向.
比如下述的这棵树:
        4
    2       6
1      3 5      7
transfer to the doubly linked list like the following: 
1-2-3-4-5-6-7
"""

class BiTNode:
    # the node of the binary tree
    def __init__(self , x = None):
        self.Left = None
        self.Right = None
        self.Data = x

def ConstructTree():
    # construcy a tree 
    Root = BiTNode(x = 4)
    Root.Left = BiTNode(x = 2) ; Root.Right = BiTNode(x = 6)
    Root.Left.Left = BiTNode(1) ; Root.Left.Right = BiTNode(3)
    Root.Right.Left = BiTNode(5) ; Root.Right.Right = BiTNode(7)
    return Root

def PrintBiTreePostorder(Root):
    if Root == None:
        return 
    if Root.Left != None:
        PrintBiTreePostorder(Root.Left)
    if Root.Right != None:
        PrintBiTreePostorder(Root.Right)
    print(Root.Data , " " , end = "")

def Transfer2LinkedList(root , storelist):
    # transfer the binary tree to the doubly linked list
    # root: the root of a binary tree
    # storelist: a list to store all the node that belongs to the binary tree
    if root == None:
        return 
    if root.Left != None:
        Transfer2LinkedList(root.Left , storelist)
    storelist.append(root)
    if root.Right != None:
        Transfer2LinkedList(root.Right , storelist)

def TraversalLinkedlist(LL):
    # print the value stored in the doubly linked list in the order
    temp = LL
    while temp != None:
        print(temp.Data , " -> " , end = "")
        temp = temp.Left
    print("None")

def Transfer2LinkedList2(pHead , pEnd , root):
    # a better way to transfer the binary tree to a doubly linked list
    # pHead: doubly linked list's head; pEnd: doubly linked list's tail; root: the remaining tree's root
    if root == None:
        return 
    if root.Left != None:
        pHead , pEnd = Transfer2LinkedList2(pHead , pEnd , root.Left)
    if pHead != None and pEnd != None:
        pEnd.Right = root ; root.Left = pEnd ; pEnd = root
    if pHead == None:
        pHead = root
    if pEnd == None:
        pEnd = root
    if root.Right != None:
        pHead , pEnd = Transfer2LinkedList2(pHead , pEnd , root.Right)
    return pHead , pEnd

def TraversalLinkedlist2(LL):
    # print the value stored in the doubly linked list in the order
    temp = LL
    while temp != None:
        print(temp.Data , " -> " , end = "")
        temp = temp.Right
    print("None")

if __name__ == "__main__":
    Root1 = ConstructTree()  
    print("The binary tree in the postorder is : ")
    PrintBiTreePostorder(Root1)
    print("")
    storelist = [] # new a list to store the binary tree's node.
    Transfer2LinkedList(Root1 , storelist)
    LinkList = storelist[0]
    storelist[0].Left = storelist[1] ; storelist[0].Right = None # initiative the first node og the doubly linked list
    for index in range(1 , len(storelist) - 1):
        storelist[index].Left = storelist[index + 1]
        storelist[index].Right = storelist[index - 1]
    storelist[-1].Right = storelist[index] ; storelist[-1].Left = None
    TraversalLinkedlist(LinkList)

    Root2 = ConstructTree()
    # a better way to transfer the binary tree to the doubly linked list
    pHead = None ; pEnd = None
    pHead , pEnd = Transfer2LinkedList2(pHead , pEnd , Root2)
    print("a better way to transfer the binary tree to the doubly linked list: ")
    TraversalLinkedlist2(pHead)
    print("reversed traversal the doubly linked list: ")
    TraversalLinkedlist(pEnd)
