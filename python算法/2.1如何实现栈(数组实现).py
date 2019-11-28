# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 15:15:04 2019

@author: wenbin
"""

"""
实现一个数据结构,使其具有以下方法:压栈,弹栈,取栈顶元素,判断栈是否为空以及获取栈中元素个数.
数组实现stack
"""

class MyStack:
    # 模拟栈
    def __init__(self):
        self.items = []
    # 判断栈是否为空
    def isEmpty(self):
        return len(self.items) == 0
    # 返回栈的大小
    def size(self):
        return len(self.items)
    # 返回栈顶元素
    def top(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]
        else:
            return None
    # 弹栈
    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else :
            print("Stack is empty")
            return None
    # 压栈
    def push(self , item):
        self.items.append(item)

if __name__ == "__main__":
    s = MyStack()
    s.push(4)
    s.push(3)
    print("The top element of the stack is " , s.top())
    print("The size of the stack is " , s.size())
    x = s.pop()
    print("Pop sunccessfully! The element is "  , x)
    s.pop()