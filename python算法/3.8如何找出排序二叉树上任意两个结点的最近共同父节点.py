# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 11:26:08 2020

@author: Administrator
"""

"""
对于一棵给定的排序二叉树,求两个结点的共同父节点,例如在下图中,结点1和结点5的共同父节点为3.
                6
        3              9
    2       5       8       10
1         4      7
"""

class BiTNode:
    def __init__(self , x):
        self.Lchild = None
        self.Rchild = None
        self.Data = x

def ConstructTree():
    root = BiTNode(6) ; root.Lchild = BiTNode(3) ; root.Rchild = BiTNode(9)
    root.Lchild.Lchild = BiTNode(2) ; root.Lchild.Rchild = BiTNode(5)
    root.Lchild.Lchild.Lchild = BiTNode(1) ; root.Lchild.Rchild.Lchild = BiTNode(4)
    root.Rchild.Lchild = BiTNode(8) ; root.Rchild.Rchild = BiTNode(10); root.Rchild.Lchild.Lchild = BiTNode(7)
    return root

def PrintTreeMidorder(root):
    if root == None:
        return 
    if root.Lchild != None:
        PrintTreeMidorder(root.Lchild)
    print(root.Data , " " , end = "")
    if root.Rchild != None:
        PrintTreeMidorder(root.Rchild)

def JudWheParentNode(pnode , cnodedata ):
    # judge whether the pnode is the parent of the cnode.
    if pnode.Lchild != None:
        if pnode.Lchild.Data == cnodedata:
            return True
    if pnode.Rchild != None:
        if pnode.Rchild.Data == cnodedata:
            return True
    if pnode.Lchild == None and pnode.Rchild == None:
        return False
    elif pnode.Lchild == None and pnode.Rchild != None:
        return JudWheParentNode(pnode.Rchild , cnodedata)
    elif pnode.Lchild != None and pnode.Rchild == None:
        return JudWheParentNode(pnode.Lchild , cnodedata)
    else:
        return (JudWheParentNode(pnode.Lchild , cnodedata) or JudWheParentNode(pnode.Rchild , cnodedata))


def JudSmaPnode(data1 , data2 , root):
    # return the smallest pnode of node1 and node2.
    if JudWheParentNode(pnode = root.Lchild , cnodedata = data1 ) and \
        JudWheParentNode(pnode = root.Lchild , cnodedata = data2 ) :
        return JudSmaPnode(data1 , data2 , root.Lchild)
    elif JudWheParentNode(pnode = root.Rchild , cnodedata = data1 ) and \
        JudWheParentNode(pnode = root.Rchild , cnodedata = data2 ) :
        return JudSmaPnode(data1 , data2 , root.Rchild)
    else:
        return root


if __name__ == "__main__":
    root = ConstructTree()
    print("The binary tree in the middle order traversal is : ")
    PrintTreeMidorder(root)
    print("")
    smapnode = JudSmaPnode(data1 = 1 , data2 = 5 , root = root)
    print("The smallest parent node of both 1 and 5 is : " , smapnode.Data)