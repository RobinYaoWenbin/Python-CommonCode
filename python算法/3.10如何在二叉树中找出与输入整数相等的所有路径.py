# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 14:22:55 2020

@author: Administrator
"""

"""
从树的根结点开始往下访问一直到叶子结点经过的所有结点形成一条路径.找出所有的这些路径,
使其满足这条路径上所有结点数据的和等于给定的整数.例如:给定如下二叉树与整数8,满足条件的路径为6->3->-1(6+3-1=8).
        6
    3       -7
-1     9
"""

class BiTNode:
    def __init__(self , x):
        self.Data = x
        self.Lchild = None
        self.Rchild = None

def ConstructTree():
    root = BiTNode(6)
    root.Lchild = BiTNode(3) ; root.Rchild = BiTNode(-7)
    root.Lchild.Lchild = BiTNode(-1) ; root.Lchild.Rchild = BiTNode(9)
    return root

def PrintTreeinMidorder(root):
    if root == None:
        return 
    if root.Lchild != None:
        PrintTreeinMidorder(root.Lchild)
    print(root.Data , " " , end = "")
    if root.Rchild != None:
        PrintTreeinMidorder(root.Rchild)

def GetLeafNode(root , LeafList):
    # get all the binary tree's leaf node
    if root == None:
        return 
    if root.Lchild != None:
        GetLeafNode(root.Lchild , LeafList)
    if root.Rchild != None:
        GetLeafNode(root.Rchild , LeafList)
    if root.Lchild == None and root.Rchild == None:
        LeafList.append(root)

def GetPath(root , leafnode , path):
    # get the path from root to the leafnode in the binary tree, the return of the function 
    # is to judge whether the leafnode is in the binary tree which root is the input root.
    if root == None:
        return False
    if root.Lchild == None and root.Rchild == None and root != leafnode:
        return False
    if root == leafnode:
        return True

    if GetPath(root.Lchild , leafnode , path):
        path.append(root.Lchild)
        return True
    if GetPath(root.Rchild , leafnode , path):
        path.append(root.Rchild)
        return True
    return False

def PathDisplay(root , k):
    # give the path in which the sum of all the nodes' data are the input k.
    leaflist = []
    pathlist = []
    path_index = []
    GetLeafNode(root , leaflist)
    for index in range(len(leaflist)):
        pathtemp = []
        GetPath(root , leaflist[index] , pathtemp)
        pathtemp.append(root) ; pathlist.append(pathtemp)
    for index in range(len(pathlist)):

        # print all the path to check.
        print("Path {0}".format(index + 1) , "")
        for node in pathlist[index]:
            print(node.Data , " " , end = "")
        print("")
        
        sum_node = 0
        for i in range(len(pathlist[index])):
            sum_node += pathlist[index][i].Data
        if sum_node == k:
            path_index.append(index)
    for i in range(len(path_index)):
        print("The {0}th path in which the sum of the node is {1}".format((i+1) , k))
        for node in pathlist[path_index[i]]:
            print(node.Data , " " , end = "")
        print("")
    if len(path_index) == 0:
        print("Sorry! there is no path conform the rule!")

if __name__ == "__main__":
    root = ConstructTree()
    print("The constructed binary tree is : ")
    PrintTreeinMidorder(root)
    print("")
    k = 18
    # print("The path where all the nodes' sum is {0} is following: ".format(k))
    PathDisplay(root = root , k = k)
