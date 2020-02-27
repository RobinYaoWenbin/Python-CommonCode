# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 20:03:36 2020

@author: Administrator
"""

"""
有一个函数func1能返回0和1两个值,返回0和1的概率都是1/2,问怎么利用这个函数得到另一个函数func2,使func2也只能返回0和1,
且返回0的概率为1/4,返回1的概率为3/4.
"""

import random

def func1():
    return random.randint(0 , 1)

def func2():
    return (1 -func1() * func1())

if __name__ == "__main__":
    print(func2())