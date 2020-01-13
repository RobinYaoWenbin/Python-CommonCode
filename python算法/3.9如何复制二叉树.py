# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 09:39:28 2020

@author: Administrator
"""

"""
给定一个二叉树根节点,复制该树,返回新建树的根结点.
        1
    2       3
4      5  6
"""

class BiTNode:
    def __init__(self , x):
        self.Data = x
        self.Lchild = None
        self.Rchild = None

def ConstructBiTree():
    root = BiTNode(x = 1)
    root.Lchild = BiTNode(x = 2) ; root.Rchild = BiTNode(x = 3)
    root.Lchild.Lchild = BiTNode(x = 4) ; root.Lchild.Rchild = BiTNode(x = 5)
    root.Rchild.Lchild = BiTNode(x = 6)
    return root

def PrintTreeinMidorder(root):
    if root == None:
        return 
    if root.Lchild != None:
        PrintTreeinMidorder(root.Lchild)
    print(root.Data , " " , end = "")
    if root.Rchild != None:
        PrintTreeinMidorder(root.Rchild)

def DeepCopyTree(root):
    # copy the binary tree, and return the new tree's root
    if root == None:
        return 
    else:
        temp = BiTNode(root.Data)  #拷贝一下根结点
    if root.Lchild != None:
        temp.Lchild = DeepCopyTree(root.Lchild)  # 拷贝一下左子树
    if root.Rchild != None:
        temp.Rchild = DeepCopyTree(root.Rchild)  # 拷贝一下右子树
    return temp

if __name__ == "__main__":
    root = ConstructBiTree()
    print("The constructed binary tree in the middle order is : ")
    PrintTreeinMidorder(root)
    print("")
    root_copy = DeepCopyTree(root)
    root.Data = 7
    print("The copying binary tree is : ")
    PrintTreeinMidorder(root_copy)
    print("")