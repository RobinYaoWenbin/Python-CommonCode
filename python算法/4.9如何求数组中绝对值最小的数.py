# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 19:56:21 2020

@author: Administrator
"""

"""
有一个升序排列的数组,数组中可能有正数,负数或0,求数组中元素的绝对值最小的数.例如,数组[-10,-5,-2,7,15,50],
该数组中绝对值最小的数是-2
"""

def FindMin(arr):
    end = len(arr) # end 是不包括在arr里的
    start = 0   # start是包含在arr里的
    minv = 2 ^ 31
    while True:
        if arr[start] >= 0:
            if abs(minv) < arr[start]:
                return minv
            else:
                return arr[start]
        elif arr[end - 1] <= 0:
            if abs(minv) < - arr[end - 1]:
                return minv
            else:
                return arr[end - 1]
        else:
            if end - start >= 2:
                mid = int((start + end) / 2)
                if abs(arr[mid]) < abs(minv):
                    minv = arr[mid]
                if arr[mid] < 0:
                    start = mid + 1
                elif arr[mid] > 0:
                    end = mid
                else:
                    return 0
            else:
                return minv

if __name__ == "__main__":
    arr = [-10,-5,-2,7,15,50]
    minv = FindMin(arr)
    print("The element value with the lowest absolute value is : " , minv)


