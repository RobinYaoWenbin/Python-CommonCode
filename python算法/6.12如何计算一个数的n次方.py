# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 15:37:48 2020

@author: Administrator
"""

"""
给定一个数d和n,如何计算d的n次方?例如:d=2,n=3,d的n次方为2^3=8.
"""


def CalPower(d , n):
    if n > 0:
        tmp = 1
        for i in range(n):
            tmp *= d
        return tmp
    elif n == 0:
        return 1
    elif n < 0:
        tmp = 1
        for i in range(-n):
            tmp *= d
        return 1 / tmp

if __name__ == "__main__":
    d = 2 ; n=  3
    print(d , "的" , n , "次方为: " , CalPower(d , n))

    d = -2 ; n=  3
    print(d , "的" , n , "次方为: " , CalPower(d , n))

    d = 2 ; n= -3
    print(d , "的" , n , "次方为: " , CalPower(d , n))