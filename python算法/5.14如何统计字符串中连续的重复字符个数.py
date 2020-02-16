# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 10:15:23 2020

@author: Administrator
"""

"""
用递归的方法实现一个求字符串中连续出现相同字符的最大值,例如字符串"aaabbcc"中连续出现字符'a'的最大值为3,
字符串"abbc"中连续出现字符'b'的最大值为2.
"""

def GetLongestChar(s):
    if len(s) == 0 or len(s) == 1:
        return len(s)
    tmp = 1 ; lasts = s[0]
    for i in range(len(s) - 1):
        if s[i+1] == lasts:
            tmp += 1
        else:
            break
    return max(tmp , GetLongestChar(s[(i+1):]))


if __name__ == "__main__":
    s = "aaabbcc"
    print("The longest same successive string is : " , GetLongestChar(s))
    s = "abbc"
    print("The longest same successive string is : " , GetLongestChar(s))