# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 21:22:38 2020

@author: Administrator
"""

"""
在一个二维数组中,每一行都按照从左到右递增的顺序排序,每一列都按照从上到下递增的顺序排序.
请实现一个函数,输入这样的一个二维数组和一个整数,判断数组中是否含有该整数.
例如,下面的二维数组就是符合这种约束条件的.如果这个数组中查找数字7,由于数组中含有该数字,则返回True;
如果再这个数组中查找数字5,由于数组中不含有该数字,则返回False.
1  2  8  9
2  4  9  12
4  7  10  13
6  8  11  15
"""
import numpy as np

def JudgeNumExit(arr,  k):
    m , n = arr.shape
    x = 0 ; y = n - 1
    while x < m and y > 0:
        if arr[x][y] > k:
            y -= 1
        elif arr[x][y] < k:
            x += 1
        else:
            return True
    return False

if __name__ == "__main__":
    arr = np.array([[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]])
    k = 5
    flag = JudgeNumExit(arr , k)
    if flag:
        print(k , " have been find!")
    else:
        print(k , " does not exit!")