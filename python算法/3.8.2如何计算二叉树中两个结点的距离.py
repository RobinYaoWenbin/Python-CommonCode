# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 11:06:49 2020

@author: Administrator
"""

"""
在没有给出父节点的条件下,计算二叉树中两个结点的距离.两个结点之间的距离是从一个结点到达另一个结点所需的最小的边数.
例如:给出下面的二叉树:
        1
    2       3
4      5  6     7
Dist(4 , 5) = 2
Dist(4 , 6) = 4
"""

class BiTNode:
    def __init__(self , x):
        self.Data = x
        self.Lchild = None
        self.Rchild = None

def ConstructTree():
    root = BiTNode(1) ; root.Lchild = BiTNode(2) ; root.Rchild = BiTNode(3)
    root.Lchild.Lchild = BiTNode(4) ; root.Lchild.Rchild = BiTNode(5)
    root.Rchild.Lchild = BiTNode(6) ; root.Rchild.Rchild = BiTNode(7)
    return root

def PrintTreeMidorder(root):
    if root == None:
        return 
    if root.Lchild != None:
        PrintTreeMidorder(root.Lchild)
    print(root.Data , " " , end = "")
    if root.Rchild != None:
        PrintTreeMidorder(root.Rchild)

def FindParentNode(root , x1 , x2):
    # find the smallest common parent node of the node1 and node2
    if root == None or root.Data == x1 or root.Data == x2:
        return root
    lchild = FindParentNode(root.Lchild , x1 , x2)
    rchild = FindParentNode(root.Rchild , x1 , x2)
    if lchild == None:
        return rchild
    elif rchild == None:
        return lchild
    else:
        return root

def root2nodedist(root , x):
    # claculate the distance between the root and the node which data is x.
    if root == None:
        return None
    if root.Data == x:
        return 0
    if root2nodedist(root.Lchild , x) != None:
        return root2nodedist(root.Lchild , x) + 1
    elif root2nodedist(root.Rchild , x) != None:
        return root2nodedist(root.Rchild , x) + 1

def Dist(root , x1 , x2):
    # get the distance of x1 and x2.
    ComPare = FindParentNode(root , x1 , x2)
    return root2nodedist(root , x1) + root2nodedist(root , x2) - 2 * root2nodedist(root , ComPare.Data)

if __name__ == "__main__":
    root = ConstructTree()
    print("The binary tree in the middle order traversal is : ")
    PrintTreeMidorder(root)
    print("")
    print("The distance between 4 and 5 is : " , Dist(root , 4 , 5))
    print("The distance between 4 and 6 is : " , Dist(root , 4 , 6))