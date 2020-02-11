# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 09:56:04 2020

@author: Administrator
"""

"""
如何求两个字符串的最长公共子串,例如字符串'abccade'与字符串'dgcadde'的最长公共子串是'cad'.
本题我使用"滑动比较法解决".
"""

def GetLongestComStr(str1 , str2):
    #把str1作为基准,str2作为匹配字符串依次进行匹配
    maxstr = [] ; maxlen = 0
    for i in range(len(str1)):
        m = i
        for j in range(len(str2)):
            if str1[m] == str2[j]:
                tmp += str1[m]
                if len(tmp) > maxlen:
                    maxstr = tmp ; maxlen = len(maxstr)
                if m < len(str1) - 1:
                    m += 1
                else:
                    break
            else:
                tmp = '' ; m = i
    return maxstr , maxlen

if __name__ == "__main__":
    str1 = 'abccade' ; str2 = 'dgcadde'
    maxstr , maxlen = GetLongestComStr(str1 , str2)
    print("The longest common string of " , str1 , " and " , str2," is :\n" , maxstr)
    print("The length of the common string  is : " , maxlen)