# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 11:06:59 2020

@author: Administrator
"""

"""
二叉树的镜像就是二叉树对称的二叉树,就是交换每一个非叶子结点的左子树指针和右子树指针,如下图所示,
请写出能实现该功能的代码.注意:请勿对该树做任何假设,它不一定是平衡树,也不一定有序.
"""

class BiTNode:
    def __init__(self , x = None):
        self.Data = x
        self.Lchild = None
        self.Rchild = None

def ConstructTree():
    root = BiTNode(x = 4)
    root.Lchild = BiTNode(x = 2) ; root.Rchild = BiTNode(x = 6)
    root.Lchild.Lchild = BiTNode(x = 1) ; root.Lchild.Rchild = BiTNode(x = 3)
    root.Rchild.Lchild = BiTNode(x = 5)
    return root

def PrintTreeinMidorder(root):
    if root == None:
        return
    if root.Lchild != None:
        PrintTreeinMidorder(root.Lchild)
    print(root.Data , " " , end = "")
    if root.Rchild != None:
        PrintTreeinMidorder(root.Rchild)

def MirrorTree(root):
    # 将root为根的子树进行镜像反转
    if root == None:
        return 
    temp = root.Lchild
    root.Lchild = root.Rchild
    root.Rchild = temp
    if root.Lchild != None:
        MirrorTree(root.Lchild)
    if root.Rchild != None:
        MirrorTree(root.Rchild)

if __name__ == "__main__":
    root = ConstructTree()
    print("The tree that i build is : ")
    PrintTreeinMidorder(root)
    print("")
    MirrorTree(root)  # 对root为根的树进行镜像反转
    print("After the mirror flipping, the tree turns out to be : ")
    PrintTreeinMidorder(root)
    print("")