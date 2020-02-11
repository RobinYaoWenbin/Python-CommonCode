# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 14:04:06 2020

@author: Administrator
"""

"""
有两个有序的集合,集合中的每个元素都是一段范围,求其交集,例如集合{[4,8],[9,13]}和{[6,12]}的交集为{[6,8],[9,12]}.
"""
def GetMin(arr1 , arr2 , m , n):
    if m == len(arr1) - 1 and arr1[m][1] <= arr2[n][1]:
        n = len(arr2) - 1
        return m , n
    elif n == len(arr2) - 1 and arr1[m][1] >= arr2[n][1]:
        m = len(arr1) - 1
        return m , n
    if arr1[m][1] < arr2[n][1]:
        return (m + 1) , n
    elif arr1[m][1] > arr2[n][1]:
        return m , (n + 1)
    else:
        return (m + 1) , (n + 1)

def GetArrIntsec(arr1 , arr2):
    m = 0 ; n = 0
    ans = []
    while m < len(arr1) - 1 or n < len(arr2) - 1:
        if arr1[m][1] <= arr2[n][0]:
            if m == len(arr1) - 1:
                n = len(arr2) - 1
            else:
                m += 1
        elif arr1[m][0] >= arr2[n][1]:
            if n == len(arr2) - 1:
                m = len(arr1) - 1
            else:
                n += 1
        else:
            tmp1 = max(arr1[m][0] , arr2[n][0]) ; tmp2 = min(arr1[m][1] , arr2[n][1])
            ans.append([tmp1 , tmp2])
            m , n = GetMin(arr1 , arr2 , m , n)
    if arr1[m][1] <= arr2[n][0]:
        pass
    elif arr1[m][0] >= arr2[n][1]:
        pass
    else:
        tmp1 = max(arr1[m][0] , arr2[n][0]) ; tmp2 = min(arr1[m][1] , arr2[n][1])
        ans.append([tmp1 , tmp2])
    return ans


if __name__ == "__main__":
    arr1 = [[4,8] , [9,13] , [15 , 16] , [30,32]]
    arr2 = [[6,12] , [13 , 17] , [20 , 50]]
    ans = GetArrIntsec(arr1 , arr2)
    print("Two arrays' intersection is : \n" , ans)