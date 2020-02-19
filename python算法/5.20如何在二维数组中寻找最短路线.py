# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 19:37:03 2020

@author: Administrator
"""

"""
寻找一条从左上角(arr[0][0])到右下角(arr[m-1][m-1])的路线,使得沿途经过的数组中的整数的和最小.
"""

import numpy as np

def FindMinRoute(arr):
    (m , n) = arr.shape
    RouteLen = [[None] *n for _ in range(m)]
    Father = [[None] *n for _ in range(m)]
    RouteLen[0][0] = arr[0][0]
    for i in range(n - 1):
        RouteLen[0][i + 1] = RouteLen[0][i] + arr[0][i + 1]
        Father[0][i+1] = (0 , i)
    for i in range(m - 1):
        RouteLen[i+1][0] = RouteLen[i][0] + arr[i+1][0]
        Father[i+1][0] = (i , 0)
    i = 1
    while i < m:
        j = 1
        while j < n:
            RouteLen[i][j] = min(RouteLen[i-1][j] + arr[i][j] , RouteLen[i][j-1] + arr[i][j])
            if RouteLen[i-1][j] <= RouteLen[i][j-1] :
                Father[i][j] = (i-1 , j)
            else:
                Father[i][j] = (i , j - 1)
            j += 1
        i += 1
    i = m - 1 ; j = n - 1
    print("The route is : ")
    while True:
        print("({0} , {1})".format(i , j) , end = " ")
        i,j = Father[i][j]
        if Father[i][j] == None:
            print("(0 , 0)")
            break
    return RouteLen[-1][-1]

if __name__ == "__main__":
    arr = np.array([[1,4,3],
                    [8,7,5],
                    [2,1,5]])
    minlen = FindMinRoute(arr)
    print("The minimum length is : " , minlen)