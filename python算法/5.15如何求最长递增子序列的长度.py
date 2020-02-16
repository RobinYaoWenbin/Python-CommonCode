# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 15:53:42 2020

@author: Administrator
"""

"""
假设L=<a1,a2,```,an>是n个不同的实数的序列,L的递增子序列是这样一个子序列Lin=<ak1,ak2```akm>,
其中,k1<k2<```<km且ak1<ak2<```<akm.求最大的m值.

采用动态规划法求解
"""

def GetLongIncreaSeq(s):
    substrlen = []  # 第i个元素的含义是: 以第i个字符为结尾的最长子串的长度
    for i in range(len(s)):
        if i == 0:
            substrlen.append(1)
        else:
            maxlen = 1 ; tmp = 0
            for j in range(i):
                if s[j] < s[i]:
                    tmp = 1 + substrlen[j]
                if tmp > maxlen:
                    maxlen = tmp
            substrlen.append(maxlen)
    return max(substrlen)

if __name__ =="__main__":
    s = "xbcdabz"
    print("The length of longest increasing string is : " , GetLongIncreaSeq(s))