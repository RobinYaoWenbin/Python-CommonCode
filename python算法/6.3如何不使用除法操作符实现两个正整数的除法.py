# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 10:46:47 2020

@author: wenbin
"""

"""
如何不使用除法操作符实现两个正整数的除法
"""

def Divide(x1 , x2):
    # 不使用除法实现x1除x2
    result = 0
    while x1 >= x2:
        x1 -= x2 ; result += 1
    return result , x1

def Plus(x1 , x2):
    # 不用加减乘除实现加法操作,这种方法只能实现两个正数相加.
    sums = 0
    carry = 0
    while True:
        sums = x1 ^ x2  # 不考虑进位时的相加操作
        carry = (x1 & x2) << 1
        x1 = sums ; x2 = carry
        if carry == 0:
            break
    return sums

def Subtraction(x1 , x2):
    # 不使用加减乘除实现减法
    x2 = ~(x2 - 1)
    result = Plus(x1 , x2)
    return result

def Multi(a , b):
    # 不使用加减乘除实现相乘操作
    neg = (a>0)^(b>0)
    if b < 0:
        b = Plus(~b , 1)
    if a < 0:
        a = Plus(~a , 1)
    result = 0
    bit_pos = dict()
    i= 0
    while i < 32:
        bit_pos[1<<i] = i
        i += 1
    while b > 0:
        pos = bit_pos[b&~(b-1)]
        result += (a<<pos)
        b &= b-1
    if neg:
        result = Plus(~result , 1)
    return result

if __name__ == "__main__":
    x1 = 14 ; x2 = 4
    result , x1 = Divide(x1 , x2)
    print("The x2 divided by x1 is : " , result , " and the remaining is : " , x1)
    x1 = 14 ; x2 = 4
    result = Plus(x1 , x2)
    print("The x2 plus x1 is : " , result )
    x1 = 14 ; x2 = -4
    result = Subtraction(x1 , x2)
    print("The x2 subtraction x1 is : " , result )
    x1 = 14 ; x2 = 4
    result = Multi(x1 , x2)
    print("The x2 multiply x1 is : " , result )