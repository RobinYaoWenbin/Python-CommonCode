# -*- coding: utf-8 -*-
"""
Created on Sun May  5 20:47:24 2019

@author: Administrator
"""

import math

#the distance between two node in the time series
def calcdist(x,y):
    # if the node is a list
    if type(x) == 'list':
        length = len(x)
        sum = 0
        for i in range(length):
            sum = sum + (x[i]-y[i])*(x[i]-y[i])
        return math.sqrt(sum)
    else:# the node is just a number
        return abs(x-y)

# DP return the distance,,已验证正确
def dynamicTimeWarp(seqA, seqB, d ):
    #输入:序列A,B和距离计算函数
    # create the cost matrix
    numRows, numCols = len(seqA), len(seqB)
    cost = [[0 for _ in range(numCols)] for _ in range(numRows)]   #距离矩阵

    # record father
    fa = [[(0,0) for _ in range(numCols)] for _ in range(numRows)]   #cost矩阵每个元素的父节点

    # initialize the first row and column
    cost[0][0] = d(seqA[0], seqB[0])
    # print("cost[0][0]:" , cost[0][0] )
    for i in range(1, numRows):
        cost[i][0] = cost[i - 1][0] + d(seqA[i], seqB[0])  #初始化第0列
        fa[i][0] = (i-1,0)   #记录该元素的父节点

    for j in range(1, numCols):
        cost[0][j] = cost[0][j - 1] + d(seqA[0], seqB[j])   #初始化第0行
        fa[0][j] = (0,j-1)   #记录该元素的父节点

    # fill in the rest of the matrix
    for i in range(1, numRows):
        for j in range(1, numCols):
            # choices = cost[i - 1][j], cost[i][j - 1], cost[i - 1][j - 1]
            # cost[i][j] = min(choices) + d(seqA[i], seqB[j])
            if cost[i-1][j] < cost[i][j-1]:
                if cost[i-1][j] < cost[i-1][j-1]:   #cost[i-1][j]是前面路径中最小的
                    cost[i][j] = cost[i-1][j] + d(seqA[i], seqB[j])
                    fa[i][j] = (i-1,j)
                else:                               #cost[i-1][j-1]是前面路径中最小的
                    cost[i][j] = cost[i - 1][j-1] + d(seqA[i], seqB[j])
                    fa[i][j] = (i-1,j-1)
            else:
                if cost[i][j-1] < cost[i-1][j-1]:   #cost[i][j-1]是前面路径中最小的
                    cost[i][j] = cost[i][j-1] + d(seqA[i], seqB[j])
                    fa[i][j] = (i,j-1)
                else:                               #cost[i-1][j-1]是前面路径中最小的
                    cost[i][j] = cost[i - 1][j - 1] + d(seqA[i], seqB[j])
                    fa[i][j] = (i-1,j-1)

    # show the cost matrix
    print("cost matrix:")
    for row in cost:
        for entry in row:
            print ("%.2f " % entry,end="")
        print("\n")

    # show the path
    path = []
    i = numRows - 1
    j = numCols - 1
    path.append((i,j))  #将最后一个node加入
    while i != 0 or j != 0:
        i,j=fa[i][j]
        path.append((i,j))
    print("path:")
    for cord in path[::-1] :
        print(cord, ' ', end="")
    print("\n")
    path_len = len(path)

    return cost[-1][-1] / path_len   #返回值:两个序列的DTW距离


# DP return the distance , 对角线cost*2m,已验证正确
def dynamicTimeWarp2(seqA, seqB, d ):
    #输入:序列A,B和距离计算函数

    #if seqA or seqB is None, then return the DTW result is 0
    if seqA is None or seqB is None :
        return 0

    # create the cost matrix
    numRows, numCols = len(seqA), len(seqB)
    if numRows==0 or numCols==0:
        return 0
    cost = [[0 for _ in range(numCols)] for _ in range(numRows)]   #距离矩阵

    # record father
    fa = [[(0,0) for _ in range(numCols)] for _ in range(numRows)]   #cost矩阵每个元素的父节点

    # initialize the first row and column
    cost[0][0] = 2 * d(seqA[0], seqB[0])
    # print("cost[0][0]:" , cost[0][0] )
    for i in range(1, numRows):
        cost[i][0] = cost[i - 1][0] + d(seqA[i], seqB[0])  #初始化第0列
        fa[i][0] = (i-1,0)   #记录该元素的父节点

    for j in range(1, numCols):
        cost[0][j] = cost[0][j - 1] + d(seqA[0], seqB[j])   #初始化第0行
        fa[0][j] = (0,j-1)   #记录该元素的父节点

    # fill in the rest of the matrix
    for i in range(1, numRows):
        for j in range(1, numCols):
            # choices = cost[i - 1][j], cost[i][j - 1], cost[i - 1][j - 1]
            # cost[i][j] = min(choices) + d(seqA[i], seqB[j])
            if cost[i-1][j] < cost[i][j-1]:
                if cost[i-1][j] + d(seqA[i], seqB[j]) < cost[i-1][j-1] + 2 * d(seqA[i], seqB[j]):   #cost[i-1][j]是前面路径中最小的
                    cost[i][j] = cost[i-1][j] + d(seqA[i], seqB[j])
                    fa[i][j] = (i-1,j)
                else:                               #cost[i-1][j-1]是前面路径中最小的
                    cost[i][j] = cost[i - 1][j-1] + 2 * d(seqA[i], seqB[j])
                    fa[i][j] = (i-1,j-1)
            else:
                if cost[i][j-1] + d(seqA[i], seqB[j]) < cost[i-1][j-1] + 2 * d(seqA[i], seqB[j]):   #cost[i][j-1]是前面路径中最小的
                    cost[i][j] = cost[i][j-1] + d(seqA[i], seqB[j])
                    fa[i][j] = (i,j-1)
                else:                               #cost[i-1][j-1]是前面路径中最小的
                    cost[i][j] = cost[i - 1][j - 1] + 2 * d(seqA[i], seqB[j])
                    fa[i][j] = (i-1,j-1)

    '''
    # show the cost matrix
    print("cost matrix:")
    for row in cost:
        for entry in row:
            print ("%.2f " % entry,end="")
        print("\n")
    '''

    # show the path
    path = []
    i = numRows - 1
    j = numCols - 1
    path.append((i,j))  #将最后一个node加入
    while i != 0 or j != 0:
        i,j=fa[i][j]
        path.append((i,j))
    # print("path:")
    # for cord in path[::-1] :
    #     print(cord, ' ', end="")
    # print("\n")

    path_len = len(path)
    return cost[-1][-1] / path_len   #返回值:两个序列的DTW距离


def test():
    seqA = [0,3,6,13]
    seqB = [0,0,4,12,2]
    # print(type(seqA))
    dist = dynamicTimeWarp2(seqA,seqB,calcdist)
    print(dist)

    """
    [0,0,0,3,6,13,25,22,7,2,1,0,0,0,0,0,0]
    [0,0,0,0,0,0,4,5,12,24,23,8,3,1,0,0]
    """


if __name__ == "__main__":
    test()