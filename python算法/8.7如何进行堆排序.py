# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 18:31:52 2020

@author: Administrator
"""

"""
堆排序:利用数据结构最小堆进行堆排序.这里使用数组来构造最小堆,不用BiTNode来构造.
因为数组比较简单,而且是堆是完全树,用数组来构造是比较恰当的.
"""
def BuildMinHeap(seq):
    MinHeap = [len(seq)]  # the first element is the size of the minimun heap
    for index in range(len(seq)):
        MinHeap.append(seq[index])
        Uncertain = len(MinHeap) - 1
        #print(MinHeap)
        while Uncertain > 1:
            if MinHeap[int(Uncertain / 2)] > MinHeap[Uncertain]:
                tmp = MinHeap[int(Uncertain / 2)]
                MinHeap[int(Uncertain / 2)] = MinHeap[Uncertain]
                MinHeap[Uncertain] = tmp
                Uncertain = int(Uncertain / 2)
            else:
                break
    return MinHeap

def AdjustHeap(MinHeap):
    Uncertain = 1
    while Uncertain <= int((len(MinHeap)-1) / 2):
        if (2*Uncertain+1) <= (len(MinHeap)-1):
            if MinHeap[2 * Uncertain + 1] <= MinHeap[2 * Uncertain] :
                if MinHeap[Uncertain] > MinHeap[2*Uncertain+1]:
                    tmp = MinHeap[2*Uncertain+1]
                    MinHeap[2*Uncertain+1] = MinHeap[Uncertain]
                    MinHeap[Uncertain] = tmp
                    Uncertain = 2 * Uncertain + 1
                else:
                    break
            else:
                if MinHeap[Uncertain] > MinHeap[2*Uncertain]:
                    tmp = MinHeap[2*Uncertain]
                    MinHeap[2*Uncertain] = MinHeap[Uncertain]
                    MinHeap[Uncertain] = tmp
                    Uncertain = 2 * Uncertain
                else:
                    break
        else:
            if MinHeap[Uncertain] > MinHeap[2*Uncertain]:
                tmp = MinHeap[2*Uncertain]
                MinHeap[2*Uncertain] = MinHeap[Uncertain]
                MinHeap[Uncertain] = tmp
                Uncertain = 2 * Uncertain
            else:
                break
    return MinHeap

def HeapSort(MinHeap):
    seq  = []
    # print(MinHeap)
    while len(MinHeap) > 1:
        seq.append(MinHeap[1])
        del MinHeap[1]
        MinHeap.insert(1 , MinHeap[-1])
        del MinHeap[-1]
        MinHeap = AdjustHeap(MinHeap)
        #print(MinHeap)
    return seq

if __name__ == "__main__":
    seq = [3,4,2,8,9,5,1]
    print("The original sequence is : " , seq)
    MinHeap = BuildMinHeap(seq)
    seq = HeapSort(MinHeap)
    print("The sequence after sorting is : " , seq)