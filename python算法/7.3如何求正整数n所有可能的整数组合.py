# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 14:14:52 2020

@author: Administrator
"""

"""
给定一个正整数n,求解出所有和为n的整数组合,要求组合按照递增方式展示,而且唯一。例如:4=1+1+1+1,1+1+2,1+3,2+2,4+0.
"""

def GetAllConbin(n):
    if n == 2:
        return [[1,1],[2]]
    if n == 1:
        return [[1]]
    if n == 0:
        return 
    result = []
    for i in range(n):
        tmp = GetAllConbin(n-i-1)  # 得到的tmp是一个二维数组,数组里的每一个元素都是一个数组,该数组各个元素之和为n-1.
        if tmp == None:
            pass
        else:
            lens = len(tmp) - 1
            j = 0
            while lens-j >= 0:
                if tmp[lens - j][0] >= (i+1):
                    tmp[lens - j].insert(0 , (i + 1))
                else:
                    del tmp[lens - j]
                j += 1
            result.extend(tmp)
    result.extend([[n]])
    return result

if __name__ == "__main__":
    result = GetAllConbin(4)
    print(result)
