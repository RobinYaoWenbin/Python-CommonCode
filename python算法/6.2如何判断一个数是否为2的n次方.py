# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 20:46:46 2020

@author: Administrator
"""

"""
如何判断一个数是否是2的n次方
"""

def IsPowerof2(n):
    if n < 1:
        return False
    i = 1
    while i <= n:
        if i == n:
            return True
        i <<= 1
    return False

if __name__ == "__main__":
    n = 17
    if IsPowerof2(n):
        print(n , "is the power of 2!")
    else:
        print(n , "is not the power of 2!")