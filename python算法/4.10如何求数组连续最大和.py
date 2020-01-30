# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 09:54:48 2020

@author: Administrator
"""

"""
一个有n个元素的数组,这n个元素既可以是正数也可以使负数,数组中连续的一个或多个元素可以组成一个连续的子数组,
一个数组可能有多个这种连续的子数组,求子数组和的最大值.例如:对于数组[1,-2,4,8,-4,7,-1,-5]而言,
其最大和的子数组为[4,8,-4,7],最大值为15.
"""

import copy

def GetMaxSubarr(arr):
    # get the maximum sub-array from the arr
    lastpositive = [] ; lastnegative = [] ; tmp = []; maxv = -100000000 ; maxarr = []
    for item in arr:
        if tmp == [] or (tmp[-1] >= 0 and item >= 0) or (tmp[-1] < 0 and item < 0):
            tmp.append(item)
        else:  # 新的item与数组中的符号不相同
            if tmp[-1] >= 0:
                lastpositive.extend(lastnegative)
                if sum(lastpositive) > 0:
                    lastpositive.extend(tmp)
                    lastnegative = [] ; tmp = []
                    tmpv = sum(lastpositive)
                    if tmpv > maxv:
                        maxv = tmpv
                        maxarr = copy.deepcopy(lastpositive)
                else:
                    tmpv = sum(tmp)
                    if tmpv > maxv:
                        maxv = tmpv
                        maxarr = tmp
                    lastpositive = tmp
                    tmp = []
            elif tmp[-1] < 0:
                lastnegative = tmp
                tmp = []
            tmp.append(item)
    return maxarr , maxv

if __name__ == "__main__":
    arr = [1,-2,4,8,-4,7,-1,-5]
    subarr , maxv = GetMaxSubarr(arr)
    print("The maximum sum of sub-array is : " , subarr , " and the value is : " , maxv)