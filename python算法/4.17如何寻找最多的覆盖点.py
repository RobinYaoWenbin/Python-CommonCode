# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 15:28:17 2020

@author: Administrator
"""

"""
坐标轴上从左到右依次的点为a[0],a[1],a[2]```a[n-1],设一根木棒的长度为L,求L最多能覆盖坐标轴的几个点?
"""
import copy

def MaxPoi(arr , L):
    # 棒长L最多覆盖的点的数目
    maxp = 0 ; coverlist = [] ; maxplist = []
    for index in range(len(arr)):
        if len(coverlist) == 0:
            coverlist.append(arr[index])
            if len(coverlist) > maxp:
                maxplist = copy.deepcopy(coverlist)
                maxp = len(coverlist)
        else:
            if arr[index] - coverlist[0] <= L:
                coverlist.append(arr[index])
                if len(coverlist) > maxp:
                    maxplist = copy.deepcopy(coverlist)
                    maxp = len(coverlist)
                    # print(maxplist)
            else:
                coverlist.append(arr[index])
                while coverlist[-1] - coverlist[0] > L:
                    del coverlist[0]
                if len(coverlist) > maxp:
                    maxplist = copy.deepcopy(coverlist)
                    maxp = len(coverlist)
                    print(maxplist)
    return maxp , maxplist



if __name__ == "__main__":
    arr = [1,3,7,8,10,11,12,13,15,16,17,19,25]
    maxp , coverarr = MaxPoi(arr , 8)
    print("The maximum numbers that covered by the stick is : " , maxp)
    print("The covered array is : " , coverarr)