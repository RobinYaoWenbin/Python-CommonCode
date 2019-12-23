# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 10:29:13 2019

@author: wenbin
"""

"""
实现思路为:取数组的中间元素作为根节点,将数组分成左右两部分,对数组的两部分用递归的方式分别构建左右子树.然后递归即可构造出
"""

import math

class BiTNode:
    # the node of the binary tree
    def __init__(self):
        self.Data = None
        self.Lchild = None
        self.Rchild = None

def FindMiddle(arr):
    # find the middle number's index of the array
    length = len(arr)
    return math.floor(length / 2)

def ConvertList2Bitree(arr , pnode , flag):
    # convert the array to binary tree
    mid = FindMiddle(arr)
    NewNode = BiTNode() # new a binary tree node
    NewNode.Data = arr[mid]
    if flag == "L":
        pnode.Lchild = NewNode
    elif flag == "R":
        pnode.Rchild = NewNode
    Larr = arr[:mid] ; Rarr = arr[mid + 1 : ]
    if len(Larr) != 0:
        ConvertList2Bitree(arr = Larr , pnode = NewNode , flag = "L")
    if len(Rarr) != 0:
        ConvertList2Bitree(arr = Rarr , pnode = NewNode , flag = "R")

def PrintBiTreeinMidOrder(Root):
    # print the binary tree by the middle order
    if Root == None:
        return 
    if Root.Lchild != None:
        PrintBiTree(Root.Lchild)
    print(Root.Data)
    if Root.Rchild != None:
        PrintBiTree(Root.Rchild)

def PrintBiTreeinPreOrder(Root):
    # print the binary tree by the preorder
    if Root == None:
        return 
    print(Root.Data)
    if Root.Lchild != None:
        PrintBiTreeinPreOrder(Root.Lchild)
    if Root.Rchild != None:
        PrintBiTreeinPreOrder(Root.Rchild)

if __name__ == "__main__":
    arr  = [(i + 1) for i in range(10)]
    print("The array is : " , arr)
    mid = FindMiddle(arr)
    BiTree = BiTNode()
    BiTree.Data = arr[mid]
    Larr = arr[:mid] ; Rarr = arr[mid + 1 : ]
    ConvertList2Bitree(Larr , BiTree , "L")
    ConvertList2Bitree(Rarr , BiTree , "R")
    print("The binary tree in the middle order traversal based on the array is : ")
    PrintBiTreeinMidOrder(BiTree)
    print("The binary tree in the preorder traversal based on the array is : ")
    PrintBiTreeinPreOrder(BiTree)

