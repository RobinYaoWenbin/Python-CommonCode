# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 19:32:16 2020

@author: Administrator
"""

"""
给定数组a1,a2,```,an,要求找出数组中的最大值和最小值.假设数组中的值两两各不相同.
"""

def GettheMinMax(array):
    maxv = array[0] ; minv = array[0]
    for item in array:
        if item > maxv:
            maxv = item
        if item < minv:
            minv = item
    return maxv , minv


def GettheMinMax2(array):
    # another method to find the maximum and minimum value of the array, 
    # and this method only needs the 3n/2 - 2 comparision.
    i = 0
    lens = len(array)
    while (i + 1) < lens:
        if array[i] > array[i + 1]:
            temp = array[i]
            array[i] = array[i + 1]
            array[i + 1] = temp
        i += 2
    i = 2
    minv = array[0] ; maxv = array[1]
    while (i + 1) < lens:
        if array[i] < minv:
            minv = array[i]
        if array[i + 1] > maxv:
            maxv = array[i + 1]
        i += 2
    if maxv < array[-1]:
        maxv = array[-1]
    if minv > array[-1]:
        minv = array[-1]
    return maxv , minv

if __name__ == "__main__":
    array = [7 , 3 , 19 , 40 , 4 , 7 , 1]
    maxv , minv = GettheMinMax(array)
    print("The maximun value is : " , maxv , ", and the minimum value is : " , minv)

    maxv , minv = GettheMinMax2(array)
    print("The second method, The maximun value is : " , maxv , ", and the minimum value is : " , minv)