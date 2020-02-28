# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 14:16:26 2020

@author: Administrator
"""

"""
插入排序:不断将没有排序的序列插入到已经排序的序列中去.
"""

def InsertSort(seq):
    for i in range(len(seq)):
        if i == 0:
            pass
        elif (seq[i] < seq[0]) :
            tmp = seq[i]
            for j in range(0,i):
                seq[i-j]=seq[i-j-1]
            seq[0]=tmp
        elif seq[i] > seq[i - 1]:
            pass
        else:
            for j in range(i):
                if seq[i] > seq[j] and seq[i] < seq[j+1]:
                    tmp = seq[i]
                    for m in range(j,i-1):
                        seq[i-m+j] = seq[i-m+j-1]
                    seq[j+1]=tmp
                    break
    return seq

if __name__ == "__main__":
    seq = [3,4,2,8,9,5,1]
    print("The original sequence is : " , seq)
    seq = InsertSort(seq)
    print("The sequence after sorting is : " , seq)