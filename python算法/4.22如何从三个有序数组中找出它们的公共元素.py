# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 13:17:12 2020

@author: Administrator
"""

"""
给定以非递减顺序排序的三个数组,找出这三个数组中的所有公共元素.例如,给出下面三个数组:
ar1 = [2,5,12,20,45,85] , ar2 = [16,19,20,85,200] , ar3 = [3,4,15,20,39,72,85,190].
那么,这三个数组的公共元素为[20,85].
"""

def GetMin(arr1 , arr2 , arr3 , m , n , l):
    if m == len(arr1) - 1 :
        if n == len(arr2) - 1:
            return m , n , (l + 1)
        elif l == len(arr3) - 1:
            return m , (n + 1) , l
        else:
            if arr2[n] <= arr3[l]:
                return m , (n+1) , l
            else:
                return m , n , (l + 1)
    elif n == len(arr2) - 1:
        if l == len(arr3) - 1:
            return m + 1 , n , l
        else:
            if arr1[m] <= arr3[l]:
                return m+1 , n , l
            else:
                return m , n , l + 1
    elif l == len(arr3) - 1:
        if arr1[m] <= arr2[n]:
            return m+1 , n , l
        else:
            return m , n+1 , l
    else:
        if arr1[m] <= arr2[n] and arr1[m] <= arr3[l]: #arr1[m] is the minimum element
            return (m + 1) , n , l
        elif arr2[n] < arr1[m] and arr2[n] <= arr3[l]:
            return m , (n + 1) , l
        elif arr3[l] < arr1[m] and arr3[l] < arr2[n]:
            return m , n , (l + 1)
        else:
            print("still have some area that i haven't consider!")

def GetCommonEle(arr1 , arr2 , arr3):
    m = 0 ; n = 0 ; l = 0
    ans = []
    while m <len(arr1) - 1 or n < len(arr2) - 1 or l < len(arr3) - 1:
        if arr1[m] == arr2[n] and arr2[n] == arr3[l]:
            ans.append(arr1[m])
        m , n , l = GetMin(arr1 , arr2 , arr3 , m , n , l)
    return ans

if __name__ == "__main__":
    arr1 = [2,5,12,20,45,85]
    arr2 = [16,19,20,85,200]
    arr3 = [3,4,15,20,39,72,85,190]
    ans = GetCommonEle(arr1 , arr2 , arr3)
    print("The common element in three array is : \n" , ans)