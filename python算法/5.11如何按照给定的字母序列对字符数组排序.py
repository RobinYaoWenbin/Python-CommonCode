# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 11:01:17 2020

@author: Administrator
"""

"""
已知字母序列[d,g,e,c,f,b,o,a],请实现一个方法,要求对输入的一组字符串input=["bed" , "dog" , "dear" , "eye"]
按照字母顺序排序并打印.本例的输出顺序为:dear,dog,eye,bed.
"""

def GetNum(seq , s):
    lens = len(str(len(seq))) 
    for i in range(len(seq)):
        if seq[i] == s:
            i = str(i)
            while len(i) < lens:
                i = '0' + i
            return i
    tmp = ''
    for i in range(lens):
        tmp += '9'
    return tmp

def PrintinOrd(seq , strlist):
    numlist = []
    for i in range(len(strlist)):
        tmpnum = ''
        for j in range(len(strlist[i])):
            tmpnum += GetNum(seq , strlist[i][j])
        numlist.append(tmpnum)
    sortlist = []
    for i in range(len(numlist)):
        sortlist.append((strlist[i] , numlist[i]))
    sortlist = sorted(sortlist,key=lambda x:x[1], reverse=False)
    print("The list's order in the sequence order is : ")
    for i in range(len(sortlist)):
        print(sortlist[i][0] , end = " ")
    # print(sortlist)

if __name__ == "__main__":
    strlist = ["bed" , "dog" , "dear" , "eye" , "open" , "hello"]
    seq = "dgecfboahijkmnv"
    PrintinOrd(seq , strlist)