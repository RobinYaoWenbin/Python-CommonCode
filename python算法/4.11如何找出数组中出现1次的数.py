# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 19:47:34 2020

@author: Administrator
"""

"""
一个数组里,除了三个数是唯一出现的,其余的数都出现偶数次,找出这三个数中的任意一个.比如数组序列为[1,2,4,5,6,4,2],
只有1,5,6这三个数字是唯一出现的,数字2与4均出现了偶数次(2次),只需要输出数字1,5,6中的任意一个就行.
"""

def FindOneDisNum(arr):
    # find the distinct number in the array that only appears once.
    ele_dict = dict()
    for item in arr:
        if item in ele_dict:
            ele_dict[item] ^= 1
        else:
            ele_dict[item] = 1
    for key , value in ele_dict.items():
        if value == 1:
            print(key , end = " ")
if __name__ == "__main__":
    arr = [6,3,4,5,9,4,3]
    print("The numbers that only appears once are: ")
    FindOneDisNum(arr)