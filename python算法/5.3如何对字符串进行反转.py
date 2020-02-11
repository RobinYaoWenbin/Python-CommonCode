# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 10:50:38 2020

@author: Administrator
"""

"""
实现字符串的反转,要求不使用任何系统方法,且时间复杂度最小
"""

def ReverseStr(string):
    lens = len(string)
    mid = int(lens / 2)
    for i in range(mid):
        temp = string[i]
        string = string[0:i] + string[lens - i - 1] + string[i + 1 : lens - i - 1] + temp + string[lens - i:]
    return string

def WordReversed(words):
    wordlist = words.split()
    lens = len(wordlist)
    mid = int(lens / 2)
    for i in range(mid):
        temp = wordlist[i]
        wordlist[i] = wordlist[lens - i - 1]
        wordlist[lens - i - 1] = temp
    string = ''
    for i in range(lens):
        string += wordlist[i]
        string += " "
    return string

if __name__ == "__main__":
    string = 'abcdefg'
    string = ReverseStr(string)
    print("The string after reversing is : " , string)
    string = "how are you"
    string = WordReversed(string)
    print("The words after reversing is : " , string)