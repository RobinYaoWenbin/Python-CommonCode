# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:12:37 2020

@author: Administrator
"""

"""
给定一个数组,已知这个数组中有大量的重复的数字,如何对这个数组进行高效地排序.
"""

def SortArr(arr):
    arrset = set(arr)
    arrset = list(arrset)
    arrset = sorted(arrset)
    arrdict = dict()
    for index in range(len(arrset)):
        arrdict[arrset[index]] = 0
    for index in range(len(arr)):
        arrdict[arr[index]] += 1
    arr = []
    for index in range(len(arrset)):
        tmpn = arrdict[arrset[index]]
        for i in range(tmpn):
            arr.append(arrset[index])
    return arr

if __name__ == "__main__":
    arr = [15,12,15,2,2,12,2,3,12,100,3,3]
    arr = SortArr(arr)
    print("The array after sorting is : \n" , arr)