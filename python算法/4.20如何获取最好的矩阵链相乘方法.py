# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 19:42:35 2020

@author: Administrator
"""

"""
给定一个矩阵序列,找到最有效的方式将这些矩阵相乘在一起.给定表示矩阵链的数组p,使得第i个矩阵Ai的维数为p[i-1]*p[i].
编写一个函数MatrixChainOrder(),该函数应该返回乘法运算所需的最小乘法数.
输入:p=(40,20,30,10,30)
输出:26000
有四个大小为40*20,20*30,30*10和10*30的矩阵.假设这四个矩阵为A,B,C和D,该函数的执行方法可以执行乘法运算的次数最少.
"""

def MatrixChainOrder(p , minMulti):
    lens = len(p) - 1
    if lens == 2:
        minMulti = p[0] * p[1] * p[2]
        return minMulti
    elif lens > 2:
        minMulti = min(MatrixChainOrder(p[0:-1] , minMulti) + p[0] * p[-2] * p[-1] , \
            MatrixChainOrder(p[1:] , minMulti) + p[0] * p[1] * p[-1])
        return minMulti

if __name__ == "__main__":
    p = [40 , 20 , 30 , 10 , 30]
    minMulti = 2 ** 10
    minMulti = MatrixChainOrder(p , minMulti) 
    print("The minimum multiple times is : " , minMulti)