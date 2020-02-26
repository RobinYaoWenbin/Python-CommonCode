# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 20:49:36 2020

@author: Administrator
"""

"""
给定一个数n,求出它的平方根,比如16的平方根为4.要求不能使用库函数.
"""

def SquRoot(n):
    i = 1
    while abs(n - i*i) > 0.00001:
        i = (i+n/i)/2
    return i

if __name__ == "__main__":
    n = 50
    print("The square root of " , n ," is " , SquRoot(n))