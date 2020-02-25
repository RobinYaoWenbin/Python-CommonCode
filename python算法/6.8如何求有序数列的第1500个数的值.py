# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 09:34:31 2020

@author: Administrator
"""

"""
一个有序数列,序列中的每一个值都能被2或者3或者5所整除,1是这个序列的第一个元素.求第1500个值是多少.
"""

def Get1500Ele():
    count = 1
    number = 1
    while True:
        number += 1
        if number % 2 == 0 or number % 3 == 0 or number % 5 == 0:
            count += 1
        if count == 1500:
            break
    return number

def GetNext2(n):
    # 获取大于n的最小的能被2整除的数字
    if n%2 == 0:
        return (n+2)
    else:
        return (n+1)

def GetNext3(n):
    tmp = n % 3
    return (n+3-tmp)

def GetNext5(n):
    tmp = n % 5
    return (n+5-tmp)

def Get1500Ele2():
    i = 1
    for j in range(1500-1):
        i = min(GetNext2(i) , GetNext3(i) , GetNext5(i))
    return i 

if __name__ == "__main__":
    print("The 1500th number is : " , Get1500Ele())
    print("The 1500th number is : " , Get1500Ele2())