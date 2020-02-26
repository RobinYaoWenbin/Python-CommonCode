# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 09:56:55 2020

@author: Administrator
"""

"""
实现一个函数,要求在不使用循环的前提下输出1到100
"""

def print1to100(n):
    if n == 1:
        print(n , end = " ")
        return 
    else:
        print(n,  end = " ")
        print1to100(n-1)

if __name__ == "__main__":
    print1to100(100)