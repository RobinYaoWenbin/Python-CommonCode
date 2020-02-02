# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 08:47:07 2020

@author: Administrator
"""

"""
有一个集合,求其全部子集(包含集合自身).给定一个集合s,它包含两个元素<a,b>,则其全部子集为<a,ab,b>.
使用蛮力法进行遍历,时间复杂度是O(2^N).
"""
import copy

def Getset(arr , item):
    combi = ''
    for index in range(len(item)):
        if item[len(item) - 1 - index] == '1':
            combi += arr[len(arr) - 1 - index]
    return combi

def GetAllsubset(arr):
    array = copy.deepcopy(arr)
    lens = len(array)
    N = 2 ** 3
    combination = list(range(0,N))
    for index in range(N):
        temp = bin(combination[index])[2:]
        for i in range(lens - len(temp)):
            temp = '0' + temp
        combination[index] = temp
    combinationarr = []
    for index in range(len(combination)):
        combinationarr.append(Getset(arr , combination[index]))
    combinationarr = list(set(combinationarr))
    return combinationarr

if __name__ == "__main__":
    array = ['a' , 'b' , 'c']
    combinationarr = GetAllsubset(array)
    print("All the aubset is :" , combinationarr)