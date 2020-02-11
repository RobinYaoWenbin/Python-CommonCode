# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 18:40:27 2020

@author: Administrator
"""

"""
给定一个N*N的迷宫,一只老鼠需要从迷宫的左上角(对应矩阵的[0][0])走到迷宫的右下角(对应矩阵的[N-1][N-1]),
老鼠只能向两方向移动:向右或向下.在迷宫中,0表示没有路(是死胡同),1表示有路.例如;给定下面的迷宫:
1  0  0  0
1  1  0  1
0  1  0  0
1  1  1  1
图中标粗的路径就是一条合理的路径.请给出算法来找到这么一条合理路径.
"""
import numpy as np

def GetFather(solu , i , j):
    if i == 0:
        return i , (j - 1)
    elif j == 0:
        return (i - 1) , j
    elif solu[i - 1][j] == 1:
        return (i - 1) , j
    elif solu[i][j - 1] == 1:
        return i , (j - 1)
    else:
        print("error in finding the father coodinate!")


def GetRoute(arr):
    shape = arr.shape
    solu = np.zeros(shape, dtype = int, order = 'C')
    i = 0 ; j = 0 ; solu[i][j] = 1  # the start index of the coodinate
    while (i != shape[0] - 1) or (j != shape[1] - 1):
        if  j + 1 < shape[1] and arr[i][j+1] == 1 and solu[i][j+1] != -1:
            solu[i][j + 1] = 1 ; j += 1
        elif i + 1 < shape[0] and arr[i + 1][j] == 1 and solu[i + 1][j] != -1:
            solu[i+1][j] = 1 ; i += 1
        elif i + 1 < shape[0] and j + 1 < shape[1] and arr[i][j+1] == 0 and arr[i + 1][j] == 0:
            solu[i][j] = -1 ; i,j = GetFather(solu , i , j)
        elif i == shape[0] - 1 and arr[i][j+1] == 0 :
            solu[i][j] = -1 ; i,j = GetFather(solu , i , j)
        elif j == shape[1] - 1 and arr[i + 1][j] == 0 :
            solu[i][j] = -1 ; i,j = GetFather(solu , i , j)
        else:
            print("error in finding the successful path!")
    return solu


if __name__ == "__main__":
    arr = np.array([ [1,0,0,0],
            [1,1,0,1],
            [0,1,0,0],
            [1,1,1,1] ])
    solu = GetRoute(arr)
    print("The successful path is : \n" , solu)
