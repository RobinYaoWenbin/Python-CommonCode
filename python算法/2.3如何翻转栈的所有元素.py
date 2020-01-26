# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 09:27:11 2019

@author: wenbin
"""

"""
1.翻转栈的所有元素,例如输入栈{2,6,3,4,7},其中,1处在栈顶,翻转之后的栈为{7,4,3,6,2},其中5处在栈顶.
2.如何给栈进行排序,上述例子排序后变成{2 , 3 , 4 , 6 , 7}
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
    # flip all the data of the stack
    def FlipStack(self):
        NewStack = MyStack()
        while not self.empty(): 
            NewStack.push(self.pop())
        return NewStack
    # 对栈进行排序
    def RankStack(self):
        NewList = []
        while not self.empty():
            NewList.append(self.pop())
        NewList.sort()
        for i in range(len(NewList)):
            self.push(NewList[i])

if __name__ == "__main__":
    stack = MyStack()
    stack.push(2) ; stack.push(6) ; stack.push(3) ; stack.push(4) ; stack.push(7)
    print("the size of the created stack is : " , stack.size())
    print("the top of the created stack is : " , stack.top())
    stack = stack.FlipStack()
    print("\nstack has been flipped!")
    print("the size of the created stack is : " , stack.size())
    print("the top of the created stack is : " , stack.top())
    print("pop successfully! the element is : " , stack.pop())
    print("pop successfully! the element is : " , stack.pop() , "\n")

    stack = MyStack()
    stack.push(2) ; stack.push(6) ; stack.push(3) ; stack.push(4) ; stack.push(7)
    print("the size of the created stack is : " , stack.size())
    print("the top of the created stack is : " , stack.top())
    stack.RankStack()
    print("\nThe stack has been ordering!")
    print("the size of the created stack is : " , stack.size())
    print("the top of the created stack is : " , stack.top())
    print("pop successfully! the element is : " , stack.pop())
    print("pop successfully! the element is : " , stack.pop())