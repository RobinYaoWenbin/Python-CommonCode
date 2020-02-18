# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 09:48:24 2020

@author: Administrator
"""

"""
给定一个字符串,求串中字典序最大的子序列.字典序最大的子序列是这样构造的:
给定字符串a0a1···an-1,首先在字符串a0a1```an-1中找到最大的字符ai,然后在剩余的字符串ai+1```an-1中找到值最大的字符aj
然后在剩余的aj+1```an-1中找到值最大的字符ak```直到字符串的长度为0,则aiajak```即为答案.
"""

def GetMaxDictSubseq(s):
    maxdictord = s[-1]
    for i in range(len(s) - 1):
        if s[len(s) - i - 2] >= maxdictord[0]:
            maxdictord = s[len(s) - i - 2] + maxdictord
    return maxdictord

if __name__ == "__main__":
    s = "acbdxmng"
    result = GetMaxDictSubseq(s)
    print("The maximum dictionary order substring is : " , result)