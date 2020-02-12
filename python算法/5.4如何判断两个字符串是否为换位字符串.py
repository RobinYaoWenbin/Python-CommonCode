# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 10:04:34 2020

@author: Administrator
"""

"""
换位字符串是指组成字符串的字符相同,但位置不同.例如,由于字符串"aaaabbc"与字符串"abcbaaa"就是由相同的字符所组成的,
因此它们是换位字符串.
"""

def JudTranstr(str1 , str2):
    strdict = dict()
    for i in range(len(str1)):
        if str1[i] in strdict:
            strdict[str1[i]] += 1
        else:
            strdict[str1[i]] = 1
    for i in range(len(str2)):
        if str2[i] in strdict:
            strdict[str2[i]] -= 1
        else:
            return False
    for key , value in strdict.items():
        if value == 0:
            pass
        else:
            return False
    return True

if __name__ == "__main__":
    str1 = 'aaaabbc' ; str2 = 'abcbaaa'
    if JudTranstr(str1 , str2):
        print("Two strings are the same!")
    else:
        print("Two strings are not same!")
