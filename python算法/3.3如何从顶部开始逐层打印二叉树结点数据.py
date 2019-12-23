# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 14:31:43 2019

@author: wenbin
"""

"""
给定一棵二叉树,要求逐层打印二叉树结点的数据,例如有如下二叉树:
        1
    2       3
  4   5   6    7
对这棵二叉树层序遍历的结果为1,2,3,4,5,6,7;
"""
from collections import deque

class BiTNode:
    # the node of the binary tree
    def __init__(self , data = None):
        self.Data = data
        self.Lchild = None
        self.Rchild = None

def GenerateTree():
    # generate the tree for the case research
    Root = BiTNode(data = 1)
    Root.Lchild = BiTNode(data = 2) ; Root.Rchild = BiTNode(data = 3)
    Root.Lchild.Lchild = BiTNode(data = 4) ; Root.Lchild.Rchild = BiTNode(data = 5)
    Root.Rchild.Lchild = BiTNode(data = 6) ; Root.Rchild.Rchild = BiTNode(data = 7)
    return Root

def PrintMidOrder(Root):
    # print the binary tree by the middle order
    if Root == None:
        return 
    if Root.Lchild != None:
        PrintMidOrder(Root.Lchild)
    print(Root.Data , " " , end = "")
    if Root.Rchild != None:
        PrintMidOrder(Root.Rchild)

def TraversalbyLayer(Root):
    # traversal the tree by layer, 1st layer, 2nd layer````,时间复杂夫O(n),空间复杂度O(n)
    queue = deque() # new a queue
    queue.append(Root)
    print("Traversal the binary tree in the order by layer!")
    while len(queue) != 0:
        tempnode = queue.popleft()
        print(tempnode.Data , " " , end = "")
        if tempnode.Lchild != None:
            queue.append(tempnode.Lchild)
        if tempnode.Rchild != None:
            queue.append(tempnode.Rchild)

def PrintAtLevel(root , level):
    # travelsal the tree by layer. 空间复杂度是O(1)，以时间换取空间
    if root == None or level < 0 :  # 空树或是要求打印出负的层数,返回0
        return 
    elif level == 0:
        print(root.Data , " " , end = "")  # 打印出这一层的数据
        return 
    else:
        PrintAtLevel(root.Lchild , level - 1) 
        PrintAtLevel(root.Rchild , level - 1)

if __name__ == "__main__":
    Root = GenerateTree()
    print("The generating tree in the middel order is : ")
    PrintMidOrder(Root)
    print("")
    TraversalbyLayer(Root)
    print("")
    print("Another method : ")
    for i in range(3):
        PrintAtLevel(Root , i)
