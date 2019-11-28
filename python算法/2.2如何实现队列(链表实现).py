# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 21:54:49 2019

@author: wenbin
"""

"""
实现一个队列的数据结构,使其具有入队列,出队列,查看队列首尾元素,查看队列大小等功能
链表实现队列.
"""

class LNode:
    def __init__(self , x = 0 , y = None):
        self.Data = x
        self.Next = y

class MyQueue:
    def __init__(self):
        self.pHead = None
        self.pEnd = None
    # 判断队列是否为空,如果为空返回true,否则返回False
    def empty(self):
        if self.pHead == None:
            return True
        else:
            return False
    # 获取栈中元素的个数
    def size(self):
        size = 0
        p = self.pHead
        while p != None:
            p = p.Next
            size += 1
        return size
    # 入队列:把元素e加到队列尾
    def enQueue(self , e):
        p = LNode(x = e)
        if self.pHead == None:
            self.pHead = self.pEnd = p
        else:
            self.pEnd.Next = p
            self.pEnd = p
    # 出队列,删除队列的首元素
    def deQueue(self):
        if self.pHead == None:
            print("The Queue has been empty, so dequeue failed!")
        self.pHead = self.pHead.Next
        if self.pHead == None:
            self.pEnd = None
    # 取得队列首元素
    def getFront(self):
        if self.pHead == None:
            print("The queue has been empty, so get the first element failed!")
            return None
        return self.pHead.Data
    # 取得队列尾元素
    def getBack(self):
        if self.pEnd == None:
            print("The queue has been empty, so get the last element failed!")
            return None
        else:
            return self.pEnd.Data

if __name__ == "__main__":
    queue = MyQueue()
    queue.enQueue(5)
    queue.enQueue(3)
    print("队列头元素为: " , queue.getFront())
    print("队列尾元素为: " , queue.getBack())
    print("队列大小为: " , queue.size())