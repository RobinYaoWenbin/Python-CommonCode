# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 20:11:35 2020

@author: Administrator
"""

"""
随机地从大小为n的数组中选取m个整数,要求每个元素被选中的概率相等.
"""

import random

def GetmEle(Num , n , m):
    GetNum = []
    for i in range(m):
        index = random.randint(0  , n - i - 1)
        GetNum.append(Num[index])
        del Num[index]
    return GetNum

if __name__ == "__main__":
    Num = [1,2,3,4,5,6,7,8,9,10]
    n = 10 ; m = 6
    result = GetmEle(Num , n , m)
    print("The number that randomly selected is : " , result)