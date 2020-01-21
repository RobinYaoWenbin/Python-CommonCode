# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 18:13:25 2020

@author: Administrator
"""

"""
# 这题好难,哭了
给定一棵二叉树,求各个路径的最大和,路径可以以任意结点作为起点和终点.比如给定以下二叉树:
        2
    5       3
1      6  4     8

最大和的路径为结点6->5->2->3->8,这条路径的和为24,因此返回24.
"""

class BiTNode:
    def __init__(self , x):
        self.Data = x
        self.Lchild = None
        self.Rchild = None

def ConstructTree():
    root = BiTNode(x = 2) ; root.Lchild = BiTNode(x = 5) ; root.Rchild = BiTNode(x = 3)
    root.Lchild.Lchild = BiTNode(x = 1) ; root.Lchild.Rchild = BiTNode(x = 6)
    root.Rchild.Lchild = BiTNode(x = 4) ; root.Rchild.Rchild = BiTNode(x = 8)
    return root

def PrintTreeinMidorder(root):
    if root == None:
        return 
    if root.Lchild != None:
        PrintTreeinMidorder(root.Lchild)
    print(root.Data , " " , end = "")
    if root.Rchild != None:
        PrintTreeinMidorder(root.Rchild)

def GetMaxPath(root , MaxPathResult):
    # 该函数的作用是返回以root为起始结点,叶子结点为最终结点的最长路径.
    # 而root为根节点的树的最长path的值在MaxPathResult中.
    if root == None:
        return 0
    sumLeft = GetMaxPath(root.Lchild , MaxPathResult)
    sumRight = GetMaxPath(root.Rchild , MaxPathResult)
    allMax = root.Data + sumLeft + sumRight
    leftMax = root.Data + sumLeft
    rightMax = root.Data + sumRight
    tempMax = max(allMax , leftMax , rightMax)
    if tempMax > MaxPathResult.Data:
        MaxPathResult.Data = tempMax
    subMax = sumLeft if sumLeft > sumRight else sumRight
    return subMax + root.Data

def findMaxPath(root):
    MaxPathResult = BiTNode(x = -(2^31))
    GetMaxPath(root , MaxPathResult)
    return MaxPathResult.Data

if __name__ == "__main__":
    root = ConstructTree()
    print("The tree that I build is : ")
    PrintTreeinMidorder(root)
    print("")
    maxpathvalue = findMaxPath(root)
    print("The maximum path is : " , maxpathvalue)