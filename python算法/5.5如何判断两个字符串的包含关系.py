# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 13:52:20 2020

@author: Administrator
"""

"""
给定由字母组成的字符串s1和s2,其中,s2中字母的个数少于s1,如何判断s1是否包含s2?即出现在s2中的字符在s1中都存在.
例如s1='abcdef',s2='acf',那么s1就包含s2;如果s1='abcdef',s2='acg',那么s1就不包含s2,因为s2中有'g',但是s1中没有'g'.
"""

def s1conclus2(s1 , s2):
    s1 = set(s1) ; s2 = set(s2)
    for item in s2:
        if item in s1:
            pass
        else:
            return False
    return True

if __name__ == "__main__":
    s1 = 'abcdef' ; s2 = 'acf'
    if s1conclus2(s1 , s2):
        print("s1 include s2!")
    else:
        print("s1 doesn't include s2!")