# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:32:57 2020

@author: Administrator
"""

"""
回文字符串是指一个字符串从左到右与从右到左遍历得到的序列是相同的.例如"abcba"就是回文字符串,而"abcab"则不是回文字符串.
"""

def AddSym2Str(s):
    if len(s) == 0:
        return '*'
    return ('*' + s[0] + AddSym2Str(s[1:]))

def GetPalLen(i , s):
    lens = 0 ; j = 0 ; tmp = ''
    while (i - j >= 0) and (i + j < len(s)) and (s[i-j] == s[i+j]):
       
        if j == 0:
            tmp = s[i]
        else:
            tmp = s[i-j] + tmp +s[i+j]
        lens += 1 ; j += 1 
    return (2 * lens - 1) , tmp

def GetLongestPalStr(s):
    s = AddSym2Str(s)
    # print(s)
    p = [] ; strlongest = ''
    for i in range(len(s)):
        tmplen , tmpstr = GetPalLen(i , s)
        if len(p) == 0:
            strlongest = tmpstr
        elif tmplen > max(p):
            strlongest = tmpstr
        p.append(tmplen)
    return p , strlongest


if __name__ == "__main__":
    s = "abcdefgfedxyz"
    p , strlongest = GetLongestPalStr(s)
    strlongest = strlongest.replace("*", "")
    print("The longest palindrome string is : " ,strlongest)
    print("The longest length is : " , int((max(p) - 1) / 2))