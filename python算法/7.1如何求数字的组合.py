# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:00:28 2020

@author: Administrator
"""

"""
用1,2,2,3,4,5这6个数字,写一个main函数,打印出所有不同的排列,例如:512234,412345等,要求:"4"不能在第三位,3与5不能相连.
"""
def ObeyRule(s):
    if s[2] == '4':
        return False
    for i in range(len(s) - 1):
        if (s[i] == '3' and s[i+1] == '5') or (s[i] == '5' and s[i+1] == '3'):
            return False
    return True

def main():
    strlist = ['1' , '2' , '2' , '4' ]
    result = [] ; result.append(strlist[0]) ; del strlist[0]
    while len(strlist) != 0:
        tmp = strlist[0]
        tmplist = []  
        for item in result:
            tmplist.append(item + tmp)
            for i in range(len(item)):
                tmplist.append(item[0:i] + tmp + item[i:])
        result = tmplist
        del strlist[0]
    result = set(result)
    for item in result:
        if ObeyRule(item):
            print(item , end = " ")
        else:
            pass



if __name__ == "__main__":
    main()