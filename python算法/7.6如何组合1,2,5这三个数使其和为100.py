# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 09:49:25 2020

@author: Administrator
"""

"""
求出用1,2,5这三个数不同个数组合的和为100的组合个数.为了更好地理解题目的意思,下面给出几组可能的组合:
100个1,0个2和0个5,它们的和为100,50个1,25个2,0个5的和也是100;50个1,20个2,2个5的和也为100.
"""
import numpy as np

def GetAllCombi(n):
    if n == 1:
        return [[1,0 ,0]]
    elif n == 2:
        return [[2,0,0] , [0,1,0]]
    elif n == 3:
        return [[3,0,0] , [1,1,0]]
    elif n == 4:
        return [[4,0,0],[2,1,0],[0,2,0]]
    elif n == 5:
        return [[5,0,0],[3,1,0],[1,2,0],[0,0,1]]
    eles = [1 , 2 , 5]
    result = []
    for index in range(len(eles)):
        tmp = GetAllCombi(n - eles[index])
        for item in tmp:
            item[index] += 1
        result.extend(tmp)
    result = np.array(result)
    result = list(set([tuple(t) for t in result]))
    result = [list(t) for t in result]
    return result

def combinationCount(n):
    count = 0
    m = 0
    while m <= n:
        count += int((m + 2) / 2)
        m += 5
    return count


if __name__ == "__main__":
    result = GetAllCombi(10)
    print(result)
    print(combinationCount(100))