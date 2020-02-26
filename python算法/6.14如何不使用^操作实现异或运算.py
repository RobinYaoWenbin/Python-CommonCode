# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 09:23:59 2020

@author: Administrator
"""

"""
不使用^操作实现异或运算.
"""

def xor(x , y):
    bx = bin(x)[2:]
    by = bin(y)[2:]
    obres = '' ; i = 0
    while i < len(bx) and i <len(by):
        if bx[len(bx) - 1 - i] == by[len(by) - 1 - i]:
            obres = '0' + obres
        else:
            obres = '1' + obres
        i += 1
    if i == len(bx) and i == len(by):
        return (int(obres , 2))
    elif i == len(bx) and i < len(by):
        for j in range(i , len(by)):
            if by[len(by) - 1 - j] == '0':
                obres = '0' + obres
            else:
                obres = '1' + obres
        return (int(obres , 2))
    elif i == len(by) and i < len(bx):
        for j in range(i , len(bx)):
            if bx[len(bx) - 1 - j] == '0':
                obres = '0' + obres
            else:
                obres = '1' + obres
        return (int(obres , 2))

if __name__ == "__main__":
    x = 3 ; y = 5
    print(x , " ^ " , y," is : " , xor(x , y))