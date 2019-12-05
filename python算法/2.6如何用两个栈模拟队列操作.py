# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 19:43:12 2019

@author: wenbin
"""

"""
题目要求用两个栈来模拟队列,假设使用栈A和栈B模拟队列Q,A为插入栈,B为弹出栈,以实现队列Q.
再假设A和B都为空,可以认为栈A提供入队列的功能,栈B提供出队列的功能.
要入队列,入栈A即可,而出队列则需要分两种情况考虑:
如果栈B不为空,则直接弹出栈B的数据.
如果栈B为空,则依次弹出栈A的数据,放入栈B中,再弹出栈B的数据.
"""

class MyStack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
    def size(self):
        return len(self.items)
    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.items[-1]
    def pop(self):
        if self.isEmpty():
            return None
        else:
            x = self.items.pop()
            return x
    def push(self , data):
        self.items.append(data)

class MyQueue:
    def __init__(self):
        self.pushStack = MyStack()
        self.popStack = MyStack()
    def isEmpty(self):
        if (self.pushStack.isEmpty()) and (self.popStack.isEmpty()):
            return True
        else:
            return False
    def size(self):
        return (self.pushStack.size() + self.popStack.size())
    def top(self):
        if self.popStack.top() != None:
            return self.popStack.top()
        elif self.pushStack.isEmpty():
            return None
        else:
            while not self.pushStack.isEmpty():
                x = self.pushStack.pop()
                self.popStack.push(x)
            return self.popStack.top()
    def pop(self):
        if self.popStack.top() != None:
            return self.popStack.pop()
        elif self.pushStack.top() == None:
            return None
        else:
            while not self.pushStack.isEmpty():
                x = self.pushStack.pop()
                self.popStack.push(x)
            return self.popStack.pop()
    def push(self , data):
        self.pushStack.push(data)

if __name__ == "__main__":
    queue = MyQueue()
    Input1 = [1 , 3 , 2]
    Input2 = [5 , 4 , 6]
    for item in Input1:
        queue.push(item)
    print("queue's top is : " , queue.top())
    print("the popping element is : " , queue.pop())
    for item in Input2:
        queue.push(item)
    while not queue.isEmpty():
        print("the popping element is : " , queue.pop())