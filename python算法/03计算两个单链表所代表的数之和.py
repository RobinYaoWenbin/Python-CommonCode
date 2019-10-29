# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 10:41:29 2019

@author: wenbin
"""

"""
给定两个单链表，链表的每个节点代表一位数，计算两个数的和。例如:输入链表(3->1->5)和链表(5->9->2)，输出8->0->8，
即513+295=808，注意个位数在链表头
"""

class LNode():
    def __init__(self , x = 0 , Node = None):
        self.Data = x
        self.Next = Node

def InputData():
    Length = int(input("please input the length of linked list: "))
    Head1 = LNode(Length)
    Head2 = LNode(Length)
    Temp1 = Head1
    Temp2 = Head2
    for i in range(Length):
        Temp1.Next = LNode(int(input("please input the node's data of linked list1: ")))
        Temp1 = Temp1.Next
    for i in range(Length):
        Temp2.Next = LNode(int(input("please input the node's data of linked list2: ")))
        Temp2 = Temp2.Next
    return Head1 , Head2

def AddTwoLinkedList(Head1 , Head2):
    Temp1 = Head1 ; Temp2 = Head2
    Num1 = "" ; Num2 = ""
    while Temp1.Next != None:
        if Temp1 != Head1:
            Num1 = Num1 + str(Temp1.Data)
            Num2 = Num2 + str(Temp2.Data)
        Temp1 = Temp1.Next ; Temp2 = Temp2.Next
    Num1 = Num1 + str(Temp1.Data);  Num2 = Num2 + str(Temp2.Data)
    Num1 = int(Num1[::-1]) ; Num2 = int(Num2[::-1]) # 逆序str
    Result = Num1 + Num2
    print(Num1 , " + " , Num2 , " = " , Result)


if __name__ == "__main__":
    Head1 , Head2 = InputData()
    AddTwoLinkedList(Head1 , Head2)