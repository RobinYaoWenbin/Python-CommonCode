# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 14:40:48 2020

@author: Administrator
"""

"""
冒泡排序:每次将最大的冒泡到未排序的最后一个.
"""

def BubbleSort(seq):
    for i in range(len(seq)):
        maxv = -1000000 ; maxind = -1
        for j in range(len(seq) - i):
            if seq[j] > maxv:
                maxv = seq[j] ; maxind = j
        seq[maxind] = seq[len(seq) - i - 1]
        seq[len(seq) - i - 1] = maxv
    return seq

if __name__ == "__main__":
    seq = [3,4,2,8,9,5,1]
    print("The original sequence is : " , seq)
    seq = BubbleSort(seq)
    print("The sequence after sorting is : " , seq)