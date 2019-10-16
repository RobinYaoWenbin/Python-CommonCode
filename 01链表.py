# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:46:27 2019

@author: wenbin
"""

class LNode:
    #define a structure of linked list
    def __init__(self , data ):
        self.data = data
        self.NextNode = None

def GetLinkedList():
    #this func is used to get the Linked list that is defined by tester
    LinkedListLen = int(input("please input the length of the linked list:"))
    Head = LNode(LinkedListLen)  #new a head of the linked list, and set the data as the length of the list
    LastNode = Head
    for i in range(LinkedListLen):
        TempData = input("please this node's data:")
        TempNode = LNode(TempData)
        LastNode.NextNode = TempNode
        LastNode = TempNode
    return Head

def ReverseLinkedList(Head):
    '''
    this func is used to reverse the Linked List
    input:
    Head : the input Linked List
    output : 
    the reversed Linked list
    '''
    LinkedListLen = Head.data
    HeadRerversed = LNode(LinkedListLen)
    TempNode = Head.NextNode  #the node that needs to join the new list
    LastNode = HeadRerversed  #last node of the new list
    for i in range(LinkedListLen):
        NextNode = HeadRerversed.NextNode  #document the next node of the new list temporarilly
        HeadRerversed.NextNode = LNode(TempNode.data)
        HeadRerversed.NextNode.NextNode = NextNode
        TempNode = TempNode.NextNode

def DisPlayLinkedList(Head):
    LinkedListLen = Head.data
    TempNode = Head.NextNode
    for i in range(LinkedListLen):
        print(TempNode.data , end = ' ')
        TempNode = TempNode.NextNode

if __name__ == "__main__":
    HeadInput = GetLinkedList()
    print("the input linked list is following, please check")
    DisPlayLinkedList(HeadInput)
    ReversedHead =ReverseLinkedList(HeadInput)
    DisPlayLinkedList(ReversedHead)