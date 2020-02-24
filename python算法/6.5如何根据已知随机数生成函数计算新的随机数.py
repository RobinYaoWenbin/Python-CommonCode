# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 20:28:51 2020

@author: Administrator
"""

"""
已知随机数rand7()产生的随机数是整数1~7的均匀分布,如何构造rand10()函数,使其产生的随机数是整数1-10的均匀分布.
"""
import random

def rand7():
    return random.randint(1,7)

def rand10():
    x = 0
    while True:
        x = (rand7() - 1) * 7 + rand7()
        if x <= 40:
            break
    return x % 10 + 1


if __name__ == "__main__":
    print(rand10())