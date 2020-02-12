# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 19:36:03 2020

@author: Administrator
"""

"""
有一个由大小写字母组成的字符串,请对它进行重新组合,使得其中的所有小写字母排在大写字母的前面
(大写字母或小写字母之间不要求保持原来的次序)
"""

def SortStr(s):
    i = 0 ; j = len(s) - 1
    while i < j:
        if s[i].isupper():
            pass
        else:
            i += 1
        if s[j].islower():
            pass
        else:
            j -= 1
        if s[i].isupper() and s[j].islower():
            if j < len(s) - 1:
                s = s[0:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
            else:
                s = s[0:i] + s[j] + s[i+1:j] + s[i]
            i+=1 ; j-=1
    return s

if __name__ == "__main__":
    s = "AbcDefa"
    s = SortStr(s)
    print("The string after sorting is : " , s)