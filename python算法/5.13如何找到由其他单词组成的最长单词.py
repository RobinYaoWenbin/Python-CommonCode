# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 18:36:29 2020

@author: Administrator
"""

"""
给定一个字符串数组,找出数组中最长的字符串,使其能由数组中其他的字符串组成.例如给定字符串数组
["test","tester","testertest","testing","apple","seattle","banana","batting","ngcat","batti","bat",
"testingtester","testbattingcat"].满足题目要求的字符串为testbattingcat,因为这个字符串可以由数组中的其他字符串
"test","batti","ngcat"组成.
"""

def ComposebyEle(strlist , longeststr):
    # 判断一下longeststr是否能由strlist这个list中的元素组成
    for i in range(len(strlist)):
        if strlist[i] == longeststr[0 : len(strlist[i])] :
            tmp = strlist[0:i] ; tmp.extend(strlist[i+1:])
            if len(strlist[i]) == len(longeststr):  # 递归出口
                return True
            if ComposebyEle(tmp , longeststr[len(strlist[i]) : ]):
                return True
            else:
                pass
    return False


def GetLongStr(strlist):
    strlist2 = []
    for i in range(len(strlist)):
        strlist2.append((strlist[i] , len(strlist[i])))
    strlist2 = sorted(strlist2 , key = lambda x : x[1] , reverse = True)
    for i in range(len(strlist2)):
        strlist[i] = strlist2[i][0]
    strindex = 0 ; longeststr = strlist[strindex]
    while True:
        if ComposebyEle(strlist[(strindex+1):] , longeststr):
            return longeststr
        else:
            strindex += 1 ; longeststr = strlist[strindex]
        if strindex == len(strlist) - 1:
            break
    return None

if __name__ == "__main__":
    strlist = ["test","tester","testertest","testing","apple","seattle","banana",\
        "batting","ngcat","batti","bat","testingtester","testbattingcat"]
    if GetLongStr(strlist) == None:
        print("Every word can not be composed by other words!")
    else:
        print("The longest word in the word list is : " , GetLongStr(strlist))