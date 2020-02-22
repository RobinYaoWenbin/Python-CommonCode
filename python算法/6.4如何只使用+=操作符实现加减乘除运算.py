# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 16:38:44 2020

@author: wenbi
"""

"""
如何只使用+=操作符实现加减乘除运算
"""

def ArithOpe(a , b , sym):
    if sym == "+":
        a += b
        return a
    elif sym == "-":
        if a >= b:
            c = 0
            while b!=a:
                b+=1 ; c+=1
            return c
        else:
            c = 0
            while b!=a:
                a+=1
                c+=1
            return -c
    elif sym == "*":
        result = 0
        for i in range(b):
            result += a
        return result
    elif sym == "/":
        result = -1 ; tmp = 0
        while tmp < a:
            tmp += b
            result += 1
        tmp = ArithOpe(tmp , b , '-')
        tmp = ArithOpe(a , tmp , '-')
        return result , tmp



if __name__ == "__main__":
    a = 3 ; b = 4
    result = ArithOpe(a , b , '+')
    print(a , "+" , b,"=" , result)
    result = ArithOpe(a , b , '-')
    print(a , "-" , b,"=" , result)
    result = ArithOpe(a , b , '*')
    print(a , "*" , b,"=" , result)
    result , tmp = ArithOpe(a , b , '/')
    print(a , "/" , b,"=" , result , "``````" , tmp)

