# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 09:57:01 2020

@author: Administrator
"""

"""
写一个方法,检查字符串是否是整数,如果是整数,那么返回其整数值.
"""

def JudInt(s):
    if s[0] == '-':
        s = s[1:]
    if len(s) == 1:
        if s >= '0' and s <= '9':
            return True
        else:
            return False
    tmp = s[0]
    if tmp >= '0' and tmp <= '9':
            return JudInt(s[1:])
    else:
            return False


if __name__ == "__main__":
    s = "-543"
    if JudInt(s):
        print("The string is int")
    else:
        print("The string is not int")