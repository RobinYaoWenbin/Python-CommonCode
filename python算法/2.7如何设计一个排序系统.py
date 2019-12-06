# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 11:02:11 2019

@author: wenbin
"""

"""
请设计一个排队系统,能够让每个进入队伍的用户都能看到自己在队列中所处的位置和变化,队伍可能随时有人加入和退出;
当有人退出影响到用户的位置排名时需要及时反馈到用户.
"""
"""
# this class seems can not solve this problem
class MyQueue:
    def __init__(self):
        self.arr = []
        self.front = 0 # the head of the queue
        self.rear = 0 # 队列尾
    def isEmpty(self):
        return (self.front == self.rear)
    def size(self):
        return (self.rear - self.front)
    def getFront(self):
        if self.isEmpty():
            return None
        return self.arr[self.front]
    def getBack(self):
        if self.isEmpty():
            return None
        else:
            return self.arr[self.rear - 1]
    def deQueue(self):
        if self.rear > self.front:
            self.front += 1
        else:
            print("The queue is empty!")
    def enQueue(self , data):
        self.arr.append(data)
        self.rear += 1
"""

from collections import deque

class User:
    def __init__(self , id , name):
        self.id = id # use the id to sign every user
        self.name = name
        self.seq = 0  # 在sequence中的位置
    def getName(self):
        return self.name
    def setName(self , name):
        self.name = name
    def setSeq(self , seq):
        self.seq = seq
    def getId(self):
        return self.id
    def equals(self , arg0):
        # judge whether two users are equal one.
        o = arg0
        return self.id == o.getId
    def toString(self):
        return ("id" + str(self.id) + ", name:" + self.name + ", seq:" + str(self.seq))

class MyQueue:
    def __init__(self):
        self.q = deque()  # 新建一个算双向队列
    def enQueue(self , u):
        u.setSeq(len(self.q) + 1)  # 给新入队列的user加一个编号，也就是队列中的最后一位
        self.q.append(u)
    def deQueue(self):
        self.q.popleft()  # 第一位出队列
        self.updateSeq()  # 重新更新下序列号
    def deQueuemove(self , u):
        self.q.remove(u)  # 把u用户出队列
        self.updateSeq()  # 重新更新下序列号
    def updateSeq(self):  
        # 遍历一遍queue, 重新编号
        i = 1
        for u in self.q:
            u.setSeq(i)
            i += 1
    def printList(self):
        for u in self.q:
            print(u.toString())

if __name__ == "__main__":
    u1 = User(1 , "user1")
    u2 = User(2 , "user2")
    u3 = User(3 , "user3")
    u4 = User(4 , "user4")
    queue = MyQueue()
    queue.enQueue(u1)
    queue.enQueue(u2)
    queue.enQueue(u3)
    queue.enQueue(u4)
    queue.deQueue()
    queue.deQueuemove(u3)
    queue.printList()