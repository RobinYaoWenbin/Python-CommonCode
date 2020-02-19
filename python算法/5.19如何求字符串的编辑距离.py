# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 17:19:34 2020

@author: Administrator
"""

"""
编辑距离又称Levenshtein,是指两个字符串之间由一个转成另一个所需的最少编辑操作次数.
许可的编辑操作包括将一个字符替换成另一个字符,插入一个字符,删除一个字符.请设计并实现一个算法来计算两个字符串的编辑距离,
并计算其复杂度.在某些应用场景下,替换操作的代价比较高,假设替换操作的代价是插入和删除的两倍,算法该如何调整.

动态规划方法求解,很难!
"""

def CalLevDis(s1 , s2 , replace):
    # calculate the Levenshtein with s1 to s2
    if s1 == None and s2 == None:
        return 0
    elif s1 == None:
        return len(s2)
    elif s2 == None:
        return len(s1)
    len1 = len(s1) ; len2 = len(s2)
    D = [([None] * (len2 + 1)) for i in range(len1 + 1)]
    i = 0
    while i < len1 + 1:
        D[i][0] = i;  i += 1
    i = 0
    while i < len2 + 1:
        D[0][i]=  i ; i += 1
    i = 1
    while i < len1 + 1:
        j = 1
        while j < len2 + 1:
            if list(s1)[i-1] == list(s2)[j-1]:
                D[i][j] = min(D[i-1][j] + 1 , D[i][j-1] + 1,D[i-1][j-1])
            else:
                D[i][j] = min(D[i-1][j] + 1 , D[i][j-1] + 1,D[i-1][j-1] + replace)
            j += 1
        i += 1
    return D[len1][len2]

if __name__ == "__main__":
    s1 = 'bciln' ; s2 = 'fciling'
    dist = CalLevDis(s1 , s2 , 2)
    print("The Levenshtein distance from " , s1 , "to" , s2  ,"is: " , dist)