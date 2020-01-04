# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 19:44:18 2020

@author: Administrator
"""

"""
输入一个整数数组,判断该数组是否是某二元查找树的后续遍历的结果.如果是,那么返回True,否则返回False.
例如数组[1,3,2,5,7,6,4]就是下图中二叉树的后续遍历序列.
        4
    2       6
1     3  5      7
"""

class BiTNode:
    def __init__(self , x = None):
        self.Lchild = None
        self.Rchild = None
        self.Data = x

def ConstructTree():
    Root = BiTNode(4)
    Root.Lchild = BiTNode(2) ; Root.Rchild = BiTNode(6)
    Root.Lchild.Lchild = BiTNode(1) ; Root.Lchild.Rchild = BiTNode(3)
    Root.Rchild.Lchild = BiTNode(5) ; Root.Rchild.Rchild = BiTNode(7)
    return Root

def PrintTreePostorder(root):
    if root == None:
        return
    if root.Lchild != None:
        PrintTreePostorder(root.Lchild)
    if root.Rchild != None:
        PrintTreePostorder(root.Rchild)
    print(root.Data , " " , end = "")

def JudgeWhePostorder(root , arr):
    # judge whether the array is the binary tree's postorder traversal
    if root == None:
        return 
    if root.Lchild != None:
        JudgeWhePostorder(root.Lchild , arr)
    if root.Rchild != None:
        JudgeWhePostorder(root.Rchild , arr)
    if arr[0] == root.Data:
        del arr[0]
    else:
        return 

if __name__ == "__main__":
    Root = ConstructTree()
    print("The binary tree in the postorder is : ")
    PrintTreePostorder(Root)
    print("")
    arr = [1,3,2,5,7,6 , 4]
    JudgeWhePostorder(Root , arr)
    if len(arr) == 0:
        print("True")
    else:
        print("False")
