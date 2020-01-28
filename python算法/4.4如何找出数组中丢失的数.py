# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 19:51:12 2020

@author: Administrator
"""

"""
给定一个由n-1个整数组成的未排序的数组序列,其元素都是1到n中的不同的整数.请写出一个寻找数组序列中缺失整数的线性时间算法.
"""

def FindMissValue(array , N):
    # find the missing value in the array
    sumv = 0
    for item in array:
        sumv += item
    missv = (1 + N) * N / 2 - sumv
    return missv

def FindMissValue2(array , N):
    value1 = N
    for i in range(N - 1):
        value1 ^= (i + 1)
    for item in array:
        value1 ^= item
    return value1

if __name__ == "__main__":
    array = [2 , 1 , 4 , 5]
    missv = FindMissValue(array,  5)
    print("The missing value in the array is : " , missv)
    missv = FindMissValue2(array,  5)
    print("The missing value in the array is : " , missv)