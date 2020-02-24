# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 20:34:45 2020

@author: Administrator
"""

"""
如何比较a,b两个数的大小?不能使用大于,小于以及if语句.
"""

def GetMax(a , b):
    return 0.5*(abs(a-b) + a + b)

if __name__ == "__main__":
    print(GetMax(8 , 6))