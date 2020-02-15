# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 12:35:59 2020

@author: Administrator
"""

"""
判断一个字符串是否包含重复字符,例如:"good"就包含重复字符'o',而'abc'就不包含重复字符.
"""

def JuddupStr(s):
    sdict = dict()
    for i in range(len(s)):
        if s[i] in sdict:
            sdict[s[i]] += 1
        else:
            sdict[s[i]] = 1
    for key , value in sdict.items():
        if value > 1:
            return True
    return False

if __name__ == "__main__":
    s = "GOODS"
    if JuddupStr(s):
        print("There are duplicate string in the strings.")
    else:
        print("There are not duplicate string in the strings.")