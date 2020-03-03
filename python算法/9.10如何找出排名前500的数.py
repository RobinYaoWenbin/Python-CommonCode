# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 12:00:47 2020

@author: Administrator
"""

"""
有20个数组,每个数组500个元素,并且都是有序排列好的,现在如何在这20*500个数中找出排名前500的数.
"""

import heapq

def GetTop(data):
    rowsize = len(data)
    columnsize = len(data[0])
    result3 = [None] * columnsize  # 建立一个columnsize大小的最小堆
    heap = []
    i = 0
    while i < rowsize:  # 遍历一下各个数组
        arr = (None , None , None)  # 三个数值分别为数值,数值来源的数组,数值在数组中的次序index
        arr = (-data[i][0] , i , 0)
        heapq.heappush(heap , arr)  # 取出每个数组的最大值建立一个最大堆
        i += 1
    num = 0
    while num < columnsize:  # 找出最大的columnsize个数
        d = heapq.heappop(heap)  # 得到目前所有数组中最大的那个数
        result3[num] = -d[0]
        num += 1
        if (num >= columnsize):
            break
        arr=(-data[d[1]][d[2]+1] , d[1] , d[2]+1)
        heapq.heappush(heap , arr)
    return result3

if __name__ == "__main__":
    data = [[29 , 17 , 14 , 2 , 1] , [19 , 17 , 16 , 15 , 6] , [30 , 25 , 20 , 14 , 5]]
    print(GetTop(data))