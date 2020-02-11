# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 22:21:54 2020

@author: Administrator
"""

"""
给定N个磁盘,每个磁盘大小为D,i=0...N-1,现在要在这N个磁盘上"顺序分配"M个分区,每个分区大小为P[j], j=0....M-1,
顺序分配的意思是:分配一个分区P[j]时,如果当前磁盘剩余空间足够,则在当前磁盘分配;如果不够,则尝试下一个磁盘,
直到找到一个磁盘D[i+k]可以容纳该分区,分配下一个分区P[j+1]时,则从当前磁盘D[i+k]的剩余空间开始分配,
不在使用D[i+k]之前磁盘末分配的空间,如果这M个分区不能在这N个磁盘完全分配,则认为分配失败,
请实现函数,is_allocable判断给定N个磁盘(数组D)和M个分区(数组P),是否会出现分配失败的情况.
举例:磁盘为[120,120,120],分区为[60,60,80,20,80]可分配,如果为[60,80,80,20,80]则分配失败。
"""

def is_allocable(d , p):
    while len(d) != 0 and len(p) != 0:  # 要么磁盘空间分配完了,要么分区全部成功分完了
        if d[0] >= p[0]:
            d[0] = d[0] - p[0]
            del p[0]
        elif d[0] < p[0]:
            del d[0]
    if len(d) == 0 and len(p) != 0:
        return False
    elif len(d) != 0 and len(p) == 0:
        return True
    else:
        return True

if __name__ == "__main__":
    d = [120,120,120]  # 磁盘
    p = [60,60,80,20,80]  # 分区
    if is_allocable(d , p):
        print("Allocable successfully!")
    else:
        print("Allocable unsuccessfully!")