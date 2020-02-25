# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 12:15:20 2020

@author: Administrator
"""

"""
给定任意一个正整数,求比这个数大且最小的"不重复数","不重复数"的含义是相邻两位不相同,例如1101是重复数,而1201是不重复数.
"""

def NonRep(n):
    for i in range(len(str(n)) - 1):
        if str(n)[i] == str(n)[i + 1]:
            return False
    return True

def GetNonRepeNum(n):
    tmp = n
    while True:
        tmp += 1
        if NonRep(tmp):
            return tmp

def Get01(n):
    tmp = ''
    for i in range(n):
        if i % 2 == 0:
            tmp = tmp + '0'
        else:
            tmp = tmp + '1'
    return tmp

def GetNonRepeNum2(n):
    while True:
        for i in range(len(str(n))-1):
            if str(n)[len(str(n)) - 1 - i] == str(n)[len(str(n)) - 2 - i]:
                n = int(str(int(str(n)[0 : (len(str(n)) - i)]) + 1) + Get01(i))
                break
        if i == len(str(n)) - 2:
                return n

if __name__ == "__main__":
    n = 23345
    print("The smallest non-repetition number that bigger than " , n , " is " , GetNonRepeNum(n))
    n = 23345
    print("The smallest non-repetition number that bigger than " , n , " is " , GetNonRepeNum2(n))