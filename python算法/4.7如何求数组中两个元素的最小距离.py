# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 23:12:54 2020

@author: Administrator
"""

"""
给定一个数组,数组中含有重复元素,给定两个数组Num1和Num2,求这两个数组在数组中出现位置的最小距离.
"""

def FindMinDis(array , x1 , x2):
    poi1 = None ; poi2 = None
    dist = []
    for index in range(len(array)):
        if array[index] == x1:
            poi1 = index
            if poi2 == None:
                pass
            else:
                tmp = abs(poi2 - poi1)
                dist.append(tmp)
        if array[index] == x2:
            poi2 = index
            if poi1 == None:
                pass
            else:
                tmp = abs(poi2 - poi1)
                dist.append(tmp)
    return min(dist)

if __name__ == "__main__":
    array = [4,5,6,4,7,4,6,4,7,8,5,6,4,3,10,8]
    mindist = FindMinDis(array , 4 , 8)
    print("The minimum distance in the array is : " , mindist)

