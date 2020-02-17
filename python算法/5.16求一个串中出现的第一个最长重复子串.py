# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 17:02:06 2020

@author: Administrator
"""

"""
给定一个字符串,找出这个字符串中最长的重复子串,比如给定字符串"banana",子字符串"ana"出现2次,因此最长重复子串为"ana".
"""

class CommonSubString:
    def maxPrefix(self , s1 , s2):
        i = 0
        while i < len(s1) and i < len(s2):
            if list(s1)[i] == list(s2)[i]:
                i += 1
            else:
                break
        return i

    def getMaxCommonStr(self , txt):
        n = len(txt)
        suffixes = [None] * n
        longestSubStrLen = 0
        longestSubStr = None
        i = 0
        while i < n:
            suffixes[i] = txt[i:]
            i += 1
        suffixes.sort()
        i = 1
        while i < n:
            tmp = self.maxPrefix(suffixes[i] , suffixes[i - 1])
            if tmp > longestSubStrLen:
                longestSubStrLen = tmp
                longestSubStr = suffixes[i][0 : longestSubStrLen]
            i += 1
        return longestSubStr

if __name__ == "__main__":
    txt = "abcdeabc"
    c = CommonSubString()
    print("最长公共子串为: " , c.getMaxCommonStr(txt))