# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 10:47:39 2020

@author: Administrator
"""

"""
设计一个程序,当输入一个字符串时,要求输出这个字符串的所有排列.例如输入字符串abc,要求输出由字符a,b,c所能排列的所有字符串:
abc,acb,bac,bca,cba,cab.
"""

def StrPermutation(string):
    # return a list that includes all the permutation
    if len(string) == 1:  # 递归出口
        return [string]
    tmplist = StrPermutation(string[1:])
    tmp2 = []
    for index in range(len(tmplist)):
        for j in range(len(tmplist[index])):
            tmp2.append(tmplist[index][0:j] + string[0] + tmplist[index][j:])
        tmp2.append(tmplist[index] + string[0])
    return tmp2

if __name__ == "__main__":
    s = 'abc'
    permutation = StrPermutation(s)
    print("The permutation of the string ", s , " is : ")
    print(permutation)
    s = 'aba'
    permutation = StrPermutation(s)
    permutation = list(set(permutation))
    print("The permutation of the string ", s , " is : ")
    print(permutation)