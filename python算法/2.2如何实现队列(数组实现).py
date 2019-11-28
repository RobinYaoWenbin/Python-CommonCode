# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 19:34:48 2019

@author: wenbin
"""

"""
实现一个队列的数据结构,使其具有入队列,出队列,查看队列首尾元素,查看队列大小等功能
数组实现队列.
"""

class MyQueue:
    def __init__(self):
        self.arr = []
        self.front = 0  #队尾头
        self.rear = 0  #队尾尾
    # 判断队列是否为空
    def isEmpty(self):
        return self.front == self.rear
    # 返回队列的大小
    def size(self):
        return self.rear - self.front
    # 返回队列首元素
    def getFront(self):
        if self.isEmpty():
            return None
        else:
            return self.arr[self.front]
    #返回队列尾元素
    def getBack(self):
        if self.isEmpty():
            return None
        else:
            return self.arr[self.rear - 1]
    # 删除队列头元素
    def deQueue(self):
        if self.rear > self.front:
            self.front += 1
        else:
            print("The queue has been empty!")
    # 把新元素加入队列尾
    def enQueue(self , item):
        self.arr.append(item)
        self.rear += 1

if __name__ == "__main__":
    queue = MyQueue()
    queue.enQueue(5)
    queue.enQueue(3)
    print("The first element of the queue is : " , queue.getFront())
    print("The last element of the queue is : " , queue.getBack())
    print("The size of queue is : " , queue.size())

