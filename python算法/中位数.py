# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 10:16:24 2020

@author: Administrator
"""

def Ans(a ,N , lr , m):
    acopy = []
    for i in range(N):
        acopy.append(a[i])
    median = dict()
    a.sort()
    for i in range(N):
        if i < N / 2:
            median[a[i]] = 2 * i + 1
        else:
            median[a[i]] = 2 * (N - i) - 1
    for i in range(m):
        l,r = lr[i]
        maxv = median[acopy[l-1]]
        for j in range(r-l + 1):
            if median[acopy[l+j-1]] > maxv:
                maxv = median[acopy[l+j-1]]
        print(maxv)


if __name__ == "__main__":
    N = int(input ())
    a = input ().split(' ')
    for i in range(len(a)):
        a[i] = int(a[i])
    m = int(input())
    lr = []
    for i in range(m):
        tmp1 , tmp2 = input ().split(' ') #以空格为间隔符
        tmp1 = int(tmp1) ; tmp2 = int(tmp2)
        lr.append([tmp1 , tmp2])
    Ans( a , N , lr , m)