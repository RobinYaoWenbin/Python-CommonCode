 # -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 15:22:55 2019

@author: wenbin
"""

"""
输入两个整数序列,其中一个序列表示栈的push顺序,判断另一个序列有没有可能是对应的pop顺序.
"""

class LNode:
    def __init__(self , x = 0 , y = None):
        self.Data = x
        self.Next = y

class MyStack:
    def __init__(self):
        self.Data = None  # the head's data of the stack
        self.Next = None
    def isEmpty(self):
        if self.Next == None:
            return True
        else:
            return False
    def size(self):
        size = 0
        temp = self.Next
        while temp != None:
            temp = temp.Next
            size += 1
        return size
    def push(self , data):
        p = LNode(data)
        p.Next = self.Next
        self.Next = p
    def pop(self):
        temp = self.Next
        if temp != None:
            self.Next = temp.Next
            return temp.Data
        return None
    def top(self):
        if self.Next != None:
            return self.Next.Data
        else :
            return None

def GetPossibleSeqOutStack():
    # judge whether the sequence is possible order to pop out.
    InputSeq = [1 , 2 , 3 , 4 , 5]  # the input sequence
    OutSeq = [3 , 2 , 5 , 4 , 1]  # the possible output sequence
    # OutSeq = [5 , 3 , 4 , 1 , 2]
    stack = MyStack()
    stack.push(InputSeq[0])
    del InputSeq[0] # after pushing the element into stack, i delete the element.
    while (len(InputSeq) != 0):
        if stack.top() == OutSeq[0] :
            stack.pop()
            del OutSeq[0]
        else:
            stack.push(InputSeq[0])
            del InputSeq[0]
    while (stack.size() != 0) and (stack.top() == OutSeq[0]):
            stack.pop()
            del OutSeq[0]
    if stack.size() == 0:
        print("The sequence can be possible popping out order!")
    else:
        print("The sequence can not be possible popping out order!")

if __name__ == "__main__":
    GetPossibleSeqOutStack()