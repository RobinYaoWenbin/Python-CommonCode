# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 13:40:20 2020

@author: Administrator
"""

"""
给定一个整数数组,如何快速地求出该数组中第k小的数.假如数组为[4 , 0 , 1 , 0 , 2 , 3],那么第3小的元素是1.
引申问题,如何在O(N)时间复杂度内查找数组中前三名.
"""

def MergeSort(array , start , end):
    # merge sort the array from index start to end. Note that start is included, and end is not included.
    lens = end - start
    N = int(lens / 2)
    if N > 1:
        MergeSort(array , start , start + N)
    if lens - N > 1:
        MergeSort(array , start + N , end)
    poi1 = start ; poi2 = start + N
    tmp = []
    while poi1 < start + N and poi2 < end:
        if array[poi1] < array[poi2]:
            tmp.append(array[poi1])
            poi1 += 1
        else:
            tmp.append(array[poi2])
            poi2 += 1
    if poi1 == start + N:
        tmp.extend(array[poi2:end])
    elif poi2 == end:
        tmp.extend(array[poi1 : start + N])
    else:
        pass
    array[start:end] = tmp

import copy

def FindFir3Ele(array):
    bigarr = copy.deepcopy(array[0:3])
    MergeSort(bigarr, 0 , len(bigarr))
    for item in array[3:]:
        if item > bigarr[0]:
            bigarr[0] = item
            MergeSort(bigarr, 0 , len(bigarr))
        else:
            pass
    return bigarr

if __name__ == "__main__":
    array = [4 , 0 , 1 , 0 , 2 , 3]
    MergeSort(array, 0 , len(array))
    print(array)
    array = [4 , 0 , 1 , 0 , 2 , 3]
    bigarr = FindFir3Ele(array)
    print("The biggest 3 elements are : " , bigarr)