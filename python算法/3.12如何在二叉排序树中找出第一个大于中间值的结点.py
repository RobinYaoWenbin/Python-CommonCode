# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 17:12:07 2020

@author: Administrator
"""

"""
对于一棵二叉排序树,令f=(最大值+最小值)/2,设计一个算法,找出距离f值最近,大于f值的结点.例如,下图所给定的二叉排序树中,
最大值为7,最小值为1,因此,f = (1 + 7) / 2 = 4,那么在这棵二叉树中,距离结点4最近且大于4的结点为5.
"""

class BiTNode:
    def __init__(self , x):
        self.Data = x
        self.Lchild = None
        self.Rchild = None

def ConstructTree():
    root = BiTNode(x = 4) ; root.Lchild = BiTNode(x = 2) ; root.Rchild = BiTNode(x = 6)
    root.Lchild.Lchild = BiTNode(x = 1) ; root.Lchild.Rchild = BiTNode(x = 3)
    root.Rchild.Lchild = BiTNode(x = 5) ; root.Rchild.Rchild = BiTNode(x = 7)
    return root

def PrintTreeinMidOrder(root):
    if root == None:
        return 
    if root.Lchild != None:
        PrintTreeinMidOrder(root.Lchild)
    print(root.Data , " " , end = "")
    if root.Rchild != None:
        PrintTreeinMidOrder(root.Rchild)

def GetMin(root):
    if root == None:
        return None
    if root.Rchild != None:
        return GetMin(root.Lchild)
    else:
        return root.Data

def GetMax(root):
    if root == None:
        return None
    if root.Rchild != None:
        return GetMax(root.Rchild)
    else:
        return root.Data

def GetNode(root , x , Node):
    # get the node which data is larger than x from binary tree, and it is the first larger than x data.
    if root == None:
        return None
    if root.Lchild != None:
        Node = GetNode(root.Lchild , x , Node)
    if root.Rchild != None:
        Node = GetNode(root.Rchild , x , Node)
    if root.Data > x:
        if Node == None:
            Node = root
        else:
            if root.Data < Node.Data:
                Node = root
    return Node

def Getf(root):
    # get the tree's f that is the average of maximun and minimum
    f = (GetMin(root) + GetMax(root)) / 2
    Node = None
    Node = GetNode(root , f , Node)
    if Node == None:
        print("None")
    else:
        print("The node that larger than {0}, and is the smallest one of all nodes \
that conform the rule is {1}".format(f , Node.Data))

if __name__ == "__main__":
    root = ConstructTree()
    print("The binary tree that i build is : ")
    PrintTreeinMidOrder(root)
    print("")
    Getf(root)
