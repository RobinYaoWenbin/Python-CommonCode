# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 09:31:09 2019

@author: wenbin
"""

"""
用O(1)的时间复杂度求栈中的最小元素
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

def GetMinEleinConstantTime():
    # find the minimum value in the constant time.
    InputValue = [5,2,4,6,8,1,9,4]
    stack = MyStack()
    SmallValueStack = MyStack()
    for index in range(len(InputValue)):
        stack.push(InputValue[index])
        if (SmallValueStack.isEmpty()) or (SmallValueStack.top() >= InputValue[index]):
            SmallValueStack.push(InputValue[index])
    while not stack.isEmpty():
        print("The smallest element in the stack is : " , SmallValueStack.top())
        x = stack.pop()
        print("The popping element in the stack is : " , x)
        if x == SmallValueStack.top():
            SmallValueStack.pop()

if __name__ == "__main__":
    GetMinEleinConstantTime()