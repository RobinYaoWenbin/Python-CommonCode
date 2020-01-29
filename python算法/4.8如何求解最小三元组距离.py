# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 09:50:55 2020

@author: Administrator
"""

"""
已知三个升序整数数组a[l],b[m],c[n],请在三个数组中各找一个元素,使得组成的三元组距离最小.
三元组距离的定义是:假设a[i],b[j],c[k]是一个三元组,那么距离为:Distance=max(|a[i]-b[j]|,|a[i]-c[k]|,|b[j]-c[k]|),
请设计一个求最小三元组距离的最优算法.
"""

def GetDist(a , b , c):
    # get the distance among a,b,c
    dist = max(abs(a - b) , abs(a - c) , abs(b - c))
    return dist , min(a , b , c)

def FindMinDist(arr1 , arr2 , arr3):
    # find the minimum distance among three arrays, one element one array.
    poi1 = 0 ; poi2 = 0 ; poi3 = 0
    mindist = 2 ^ 31
    while poi1 < len(arr1) and poi2 < len(arr2) and poi3 < len(arr3):
        tmp_dist , minv = GetDist(arr1[poi1] , arr2[poi2] , arr3[poi3])
        if tmp_dist < mindist:
            mindist = tmp_dist
        if minv == arr1[poi1]:
            poi1 += 1
        elif minv == arr2[poi2]:
            poi2 += 1
        elif minv == arr3[poi3]:
            poi3 += 1
    if poi1 == len(arr1):
        while poi2 < len(arr2) and poi3 < len(arr3):
            tmp_dist , _= GetDist(arr1[-1] , arr2[poi2] , arr3[poi3])
            if tmp_dist < mindist:
                mindist = tmp_dist
            if arr2[poi2] < arr3[poi3]:
                poi2 += 1
            else:
                poi3 += 1
    elif poi2 == len(arr2):
        while poi1 < len(arr1) and poi3 < len(arr3):
            tmp_dist , _ = GetDist(arr2[-1] , arr1[poi1] , arr3[poi3])
            if tmp_dist < mindist:
                mindist = tmp_dist
            if arr1[poi1] < arr3[poi3]:
                poi1 += 1
            else:
                poi3 += 1
    else:
        while poi1 < len(arr1) and poi2 < len(arr2):
            tmp_dist = GetDist(arr1[poi1] , arr2[poi2] , arr3[-1])
            if tmp_dist < mindist:
                mindist = tmp_dist
            if arr1[poi1] < arr2[poi2]:
                poi1 += 1
            else:
                poi2 += 1
    return mindist

if __name__ == "__main__":
    a = [3,4,5,7,15]
    b = [10,12,14,16,17]
    c = [20,21,23,24,37,40]
    mindist = FindMinDist(a , b , c)
    print("The minimum distance among three arrays is : " , mindist)