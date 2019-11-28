# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 19:11:30 2019

@author: wenbin
"""

"""
实现一个数据结构,使其具有以下方法:压栈,弹栈,取栈顶元素,判断栈是否为空以及获取栈中元素个数.
链表实现stack
"""

class LNode:
    def __init__(self , x = 0 , y = None):
        self.Data = x
        self.Next = y

class MyStack:
    def __init__(self):
        self.Data = None
        self.Next = None

    # 判断stack是否为空,如果为空返回true, 否则返回false
    def empty(self):
        if self.Next == None:
            return True
        else:
            return False

    # 获取栈中元素的个数
    def size(self):
        size = 0
        p = self.Next
        while p != None:
            p = p.Next
            size += 1
        return size
    # 入栈
    def push(self , e):
        p = LNode(x = e , y = self.Next)
        self.Next = p
    # 出栈
    def pop(self):
        tmp = self.Next
        if tmp != None:
            self.Next = tmp.Next
            return tmp.Data
        else:
            print("stack has been empty!")
        return None
    # 取得栈顶元素
    def top(self):
        if self.Next != None:
            return self.Next.Data
        else:
            print("Stack has been empty!")
        return None

if __name__ == "__main__":
    stack = MyStack()
    stack.push(5)
    stack.push(3)
    print("栈顶元素为:" , stack.top())
    print("栈大小为:" , stack.size())
    x = stack.pop()
    print("pop successfully! The element is : " , x)
    x = stack.pop()
    print("pop successfully! The element is : " , x)
    x = stack.pop()
