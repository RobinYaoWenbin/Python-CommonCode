# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 13:06:44 2019

@author: wenbin
"""

"""
两棵二叉树相等是指这两棵二叉树有相同的结构,并且在相同的位置上的结点有相同的值.如何判断两棵二叉树是否相等呢?
"""

class BiTNode:
    # define the class of the node of the binary tree
    def __init__(self , data = None):
        self.Data = data
        self.Lchild = None
        self.Rchild = None

def ConstructTree():
    # construct the tree
    root = BiTNode(6)
    node1 = BiTNode(3)
    node2 = BiTNode(-7)
    node3 = BiTNode(-1)
    node4 = BiTNode(9)
    root.Lchild = node1
    root.Rchild = node2
    node1.Lchild = node3
    node1.Rchild = node4
    return root

def ConstructTree2():
    # construct the tree
    root = BiTNode(5)
    node1 = BiTNode(3)
    node2 = BiTNode(-7)
    node3 = BiTNode(-1)
    node4 = BiTNode(9)
    root.Lchild = node1
    root.Rchild = node2
    node1.Lchild = node3
    node1.Rchild = node4
    return root

def PrintMidorder(Root):
    # print the binary tree in the middle order
    if Root == None:
        return 
    if Root.Lchild != None:
        PrintMidorder(Root.Lchild)
    print(Root.Data , " " , end = "")
    if Root.Rchild != None:
        PrintMidorder(Root.Rchild)

def Bitree2List(Root , StoreList):
    # output the element from the binary tree to the list
    if Root == None:
        return 
    if Root.Lchild != None:
        Bitree2List(Root.Lchild , StoreList)
    if Root.Rchild != None:
        Bitree2List(Root.Rchild , StoreList)
    StoreList.append(Root.Data)


def JudgeWheSame(Root1 , Root2):
    # input is two trees' roots, we judge whether two binary tree are the same.
    treelist1 = [] ; treelist2 = []
    Bitree2List(Root1 , treelist1) ; Bitree2List(Root2 , treelist2)
    count = 0
    if len(treelist1) != len(treelist2):
        return False
    for i in range(len(treelist1)):
        if treelist1[i] == treelist2[i]:
            count += 1
        else:
            break
    if count < len(treelist1):
        return False
    else:
        return True

def isEqual(root1 , root2):
    if root1 == None and root2 == None:
        return True
    if root1 == None and root2 != None:
        return False
    if root1!=None and root2 == None:
        return False
    if root1.Data == root2.Data:
        return isEqual(root1.Lchild , root2.Lchild) and isEqual(root1.Rchild , root2.Rchild)
    else:
        return False

if __name__ == "__main__":
    Bitree1 = ConstructTree()
    print("The binary tree constructed is : ")
    PrintMidorder(Bitree1)
    print("")

    Bitree2 = ConstructTree2()
    print("The binary tree constructed is : ")
    PrintMidorder(Bitree2)
    print("")
    print("Two binary trees are the same, " , JudgeWheSame(Bitree1 , Bitree2))

    print("Second way to consider whether two trees are the same, " , isEqual(Bitree1 , Bitree2))
