# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:51:03 2020

@author: Administrator
"""

"""
设计一个算法,判断给定的一个数n是否是某个数的平方,不能使用开放运算.例如,16就满足条件,因为它是4的平方;
而15则不满足条件,因为不存在一个数使其平方值为15.
"""

def isSquare(n):
    low = 1 ; high = n
    while True:
        tmp = int((low + high) / 2)
        if tmp ** 2 == n:
            return tmp
        elif tmp ** 2 > n:
            high = tmp
        elif tmp ** 2 < n:
            low = tmp
        else:
            pass
        if (high - low) < 3:
            for i in range(low , high + 1):
                if i * i == n:
                    return i
            return False

if __name__ == "__main__":
    n = 15
    if isSquare(n):
        x = isSquare(n)
        print(n , "is" , x , "'s square!")
    else:
        print(n , "can not be some number's square!")