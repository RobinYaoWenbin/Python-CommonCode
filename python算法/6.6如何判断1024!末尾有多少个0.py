# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 09:30:27 2020

@author: Administrator
"""

"""
如何判断1024!末尾有多少个0.
有点像脑筋急转弯,一般来说根本想不到.
"""

def method(N):
    k = 1
    while 5 ** k < N:
        k += 1
    k -= 1
    count = 0
    for i in range(k):
        tmp = int(N / (5 ** (i+1)))
        count += tmp
    return count

if __name__ == "__main__":
    print("The number of 0 of 1024! is : " , method(1024))