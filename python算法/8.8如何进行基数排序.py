# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 09:01:17 2020

@author: Administrator
"""

"""
基数排序:排序的过程就是将最低位优先法用于单关键字的情况.下面以[73,22,93,43,55,14,28,65,39,81]为例来介绍
"""

import math

def RadixSort(seq , radix = 10):
    # 参数radix的意思是几进制的意思
    k = int(math.ceil(math.log(max(seq) , radix)))  # 得到最大数字的位数
    bucket = [[] for i in range(radix)]  # 得到10个bucket
    for i in range(1 , k+1):
        for j in seq:  # 遍历数组
            bucket[int(j / (radix ** (i-1)) % (radix ** i))].append(j)
        del seq[:]
        for z in bucket:
            seq += z
            del z[:]
    return seq

if __name__ == "__main__":
    seq = [73,22,93,43,55,14,28,65,39,81]
    print("The original sequence is : " , seq)
    seq = RadixSort(seq)
    print("The sequence after sorting is : " , seq)