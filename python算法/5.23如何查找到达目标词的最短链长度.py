# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 15:25:57 2020

@author: Administrator
"""

"""
给定一个词典和两个长度相同的"开始"和"目标"的单词.找到从"开始"到"目标"最小链的长度.如果它存在,那么这条链中的相邻单词只有
一个字符不同,而链中的每个单词都是有效的单词,即它存在于词典中.可以假设词典中存在"目标"字,所有词典词的长度相同.
例如:
给定一个单词词典为:[pooN,pbcc,zamc,poIc,pbca,pbIc,poIN]
                start=TooN
                target=pbca
    输出结果为:7
    因为:TooN(start)-pooN-poIN-poIc-pbIc-pbcc-pbca(target).

这个题目还是比较复杂的,下面是书上给出的答案,但是我觉得貌似还是存在一些问题的,
第一个问题是广度优先的时候,会把D中的元素给删除,这就有些问题,之前添加队列中的元素,如果最后遍历时失败了,应该要加回到
D中去才对;第二个问题是这个方法似乎也没有成功找到最短的路线.
而且书里还把难度标记成3星,呵呵呵,这个确实是一个工程量比较大的题目.
"""
import copy
from collections import deque

class QItem:
    def __init__(self , word , lens):
        self.word = word
        self.lens = lens

def isAdjacent(a , b):
    diff = 0
    lens = len(a)
    i = 0
    while i < lens:
        if list(a)[i] != list(b)[i]:
            diff += 1
        if diff > 1:
            return False
        i += 1
    return diff == 1

def ShortestChainLen(start , target , D):
    Q = deque()
    item = QItem(start , 1)
    Q.append(item)
    while len(Q)>0:
        curr = Q[0]
        Q.pop()
        for it in D:
            tmp = it
            if isAdjacent(curr.word , tmp):
                item.word = tmp
                item.lens = curr.lens + 1
                Q.append(item)
                D.remove(tmp)
                if tmp == target:
                    return item.lens


if __name__ == "__main__":
    D = ['pooN' , 'pbcc' , 'zama' , 'poIc' , 'pbca' , 'pbIc' , 'poIN' , ]
    start = "TooN" ; target = "pbca"
    print("最短的链条的长度是: " , ShortestChainLen(start , target , D))
