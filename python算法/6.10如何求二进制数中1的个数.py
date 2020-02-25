# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 10:25:20 2020

@author: Administrator
"""

"""
给定一个整数,输出这个整数的二进制表示中1的个数.例如,给定整数7,其二进制表示为111,因此输出结果为3.
"""

def count1(n):
    obn = bin(n)[2:]
    count = 0
    for i in range(len(obn)):
        if obn[i] == '1':
            count += 1
    return count

if __name__ == "__main__":
    n = 8
    print("The number of 1 in the binary representation of " , n , "is : ", count1(n))