# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 20:32:37 2019

@author: wenbin
"""

"""
给定一棵二叉树,它的每个结点都是正整数或负整数,如何找一棵子树,使得它所有的结点和最大.
"""

class BiTNode:
    # the node of the binary tree
    def __init__(self , data = None):
        self.Data = data
        self.Lchild = None
        self.Rchild = None

def GenerateTree():
    Root = BiTNode(data = 6)
    Root.Lchild = BiTNode(3) ; Root.Rchild = BiTNode(-7)
    Root.Lchild.Lchild = BiTNode(-1) ; Root.Lchild.Rchild = BiTNode(9)
    return Root

def PrintinMidOrder(Root):
    # print the binary tree in the middle order.
    if Root == None:
        return 
    if Root.Lchild != None:
        PrintinMidOrder(Root.Lchild)
    print(Root.Data , " " , end = "")
    if Root.Rchild != None:
        PrintinMidOrder(Root.Rchild)

def SumofSubtree(root , EleSum):
    # get the sum of the root and its childs
    EleSum = EleSum + root.Data 
    if root.Lchild != None:
        EleSum = SumofSubtree(root.Lchild , EleSum)
    if root.Rchild != None:
        EleSum = SumofSubtree(root.Rchild , EleSum)
    return EleSum

def FindbiggestSubtree(Root , sum_sub , rootnode):
    # find the biggest sum of the subtree's elements
    if Root == None:
        return 0
    if Root.Lchild != None:
        sum_sub , rootnode = FindbiggestSubtree(Root.Lchild , sum_sub , rootnode)
    if Root.Rchild != None:
        sum_sub , rootnode = FindbiggestSubtree(Root.Rchild , sum_sub , rootnode)
    temp = SumofSubtree(Root , 0)  # the temp node's sum of the subtree!
    if temp > sum_sub:
        sum_sub = temp
        rootnode = Root
    return sum_sub , rootnode

if __name__ == "__main__":
    Root = GenerateTree()
    print("The generated binary tree in the middle order is : ")
    PrintinMidOrder(Root)
    print("")
    maxsubtree , rootnode = FindbiggestSubtree(Root , 0 , None)
    print("The max sum of the subtree is : " , maxsubtree)
    print("The max sum of the subtree's traversal by middle order is : ")
    PrintinMidOrder(rootnode)