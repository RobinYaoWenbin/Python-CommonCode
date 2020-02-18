# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 10:45:27 2020

@author: Administrator
"""

"""
给定一个能判断一个单词是否为另一个单词的子字符串的方法,记为isSubstring.如何判断s2是否能通过旋转s1得到
(只能使用一次isSubstring方法).例如:"waterbottle"可以通过字符串"erbottlewat"旋转得到.
"""

def isSubstring(s , sub):
    # judge whether sub is a sub-string of s
    if s == '' or sub == '':
        return True
    for i in range(len(s)):
        j = 0 ; m = i
        while m < len(s) and j < len(sub) and s[m] == sub[j]:
            m += 1 ; j += 1
        if j == len(sub):
            return True
    return False

def IsRotate(s1 , s2):
    # 这种方法存在一些漏洞,比如s1 = "acbacb" 和 s2 = "abcacb"正确结果是不可以经过旋转得到,但是却会出现能够旋转得到的结果.
    # 但是可以改进,考虑更多情况来减少错误,比如s1两部分是s2的子串,s2的两部分也是s1的子串这样做.
    for i in range(len(s1)):
        if isSubstring(s2 , s1[0:i]) and isSubstring(s2 , s1[i:]):
            return True
    return False

def IsRotate2(s1 , s2):
    # 最终的解法还是通过对题目进行观察了解其规律来解的,这些题目关键在于找到规律而不再是编程上的一些技巧了.
    # s1经过旋转得到的新字符串一定是s1s1的子串,因此题目转换为判断s2是否为s1s1的子串.
    s1s1 = s1+s1
    if isSubstring(s1s1 , s2):
        return True
    else:
        return False


if __name__ == "__main__":
    s1 = "waterbottle" ; s2 = "erbottlewat" 
    s1 = "abcabc" ; s2 = "abcacb"
    if IsRotate2(s1 , s2):
        print(s1 , "and" , s2 , " can be transformed by the operating of rotating!")
    else:
        print(s1 , "and" , s2 , " can not be transformed by the operating of rotating!")

