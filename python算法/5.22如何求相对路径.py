# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 14:06:44 2020

@author: Administrator
"""

"""
编写一个函数,根据两个文件的绝对路径算出其相对路径.例如a="/qihoo/app/a/b/c/d/new.c",b="/qihoo/app/1/2/test.c",
那么b相对于a的绝对路径是"../../../../1/2/test.c"
"""

def GetRelativePath(path1 , path2):
    samepath = ""
    for i in range(len(path1)):
        if path1[i] == path2[i]:
            samepath += path1[i]
        else :
            break
    return ".../" + path2[i:]

if __name__ == "__main__":
    path1 = "/qihoo/app/a/b/c/d/new.c"
    path2 = "/qihoo/app/1/2/test.c"
    rela = GetRelativePath(path1 , path2)
    print("The relative path is : " , rela)