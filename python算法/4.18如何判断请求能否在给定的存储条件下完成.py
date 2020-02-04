# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 11:38:36 2020

@author: Administrator
"""

"""
给定一台有m个存储空间的机器,有n个请求需要在这台机器上运行,第i个请求计算时需要占R[i]空间,
计算结果需要占O[i]个空间(O[i]<O[j]).请设计一个算法,判断这n个请求能否全部完成?若能,给出这n个请求的安排顺序.

编程的难度不大,但是思维难度很高!
按照R[i]-O[i]由大到小排列,然后按顺序处理,能成功则可以处理完成,否则则不行.
"""
def Sortarr(R , O):
    # 将O按照从小到大排序,同时将R也按照O中的顺序排列
    temp = []
    for index in range(len(R)):
        temp.append((R[index] - O[index] , R[index] , O[index]))
    temp = sorted(temp , key = lambda x : x[0] , reverse = True )
    for index in range(len(temp)):
        R[index] = temp[index][1] ; O[index] = temp[index][2]

def JudgeSuccess(R , O , M , N):
    Sortarr(R , O)
    havedeal = []
    for index in range(N):
        if sum(havedeal) + R[index] <= M:
            havedeal.append(O[index])
    if index == N - 1:
        return True
    else:
        return False

if __name__ == "__main__":
    R = [10 , 15 , 23 , 20 , 6 , 9 , 7 , 16]
    O = [2 , 7 , 8 , 4 , 5 , 8 , 6 , 8]
    M = 50 ; N = 8
    flag = JudgeSuccess(R , O , M , N)
    if flag:
        print("It can successfully deal with, the order is(R , O) : ")
        for i in range(N - 1):
            print(R[i] ,",", O[i] , end = " -> ")
        print(R[-1] ,",", O[-1])
    else:
        print("It can not successfully deal with!")