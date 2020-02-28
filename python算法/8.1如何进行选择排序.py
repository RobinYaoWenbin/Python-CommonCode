# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 12:38:33 2020

@author: Administrator
"""

"""
选择排序:每次都选出剩余数组中最小的元素与未排序的数组的首元素交换.
"""

def SelectSort(seq):
    i = 0  # 已经排序好的数组的最后一个元素
    while i < len(seq):
        minv = 10000000000 ; minindex = -1
        for j in range(i , len(seq)):
            if seq[j] < minv:
                minv = seq[j] ; minindex = j
        tmp = seq[i]
        seq[i] = seq[minindex]
        seq[minindex] = tmp
        i += 1
    return seq

if __name__ == "__main__":
    seq = [3,4,2,8,9,5,1]
    print("The original sequence is : " , seq)
    seq = SelectSort(seq)
    print("The sequence after sorting is : " , seq)