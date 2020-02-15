# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 11:34:32 2020

@author: Administrator
"""

"""
给定主字符串S与模式字符串P,判断P是否是S的子串,如果是,那么找出P在S中的第一次出现的下标.
"""

def StringMatch(s , p):
    if len(s) < len(p):
        return False
    for i in range(len(s)):
        m = i
        for j in range(len(p)):
            if s[m] == p[j]:
                m += 1
                if m - i == len(p):
                    return i
            else:
                break
    return False

if __name__ == "__main__":
    s = "xyzabcd" ; p = "cd"
    if not StringMatch(s , p):
        print("does't find")
    else:
        n = StringMatch(s , p)
        print("The first matching index is : " , n)