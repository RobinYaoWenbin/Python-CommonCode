# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 11:48:33 2020

@author: Administrator
"""

"""
100个灯泡排成一排,第一轮将所有灯泡打开,第二轮每隔一个灯泡关掉一个,即排在偶数的灯泡被关掉,第三轮每隔两个灯泡,
将开着的灯泡关掉,关掉的灯泡打开.依次类推,第100轮结束的时候,还有几盏灯泡亮着.
"""

def Albumon():
    sta = [1 for i in range(100)]
    for i in range(100):
        j = 0
        while j < 100:
            sta[j] ^= 1
            j = j+(2+i)
    return sta

if __name__ == "__main__":
    sta = Albumon()
    for i in range(len(sta)):
        if sta[i] == 1:
            print(i , end = " ")