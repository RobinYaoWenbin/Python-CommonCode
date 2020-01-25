# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 14:38:33 2020

@author: Administrator
"""

"""
数字1-1000放在一个含有1001个元素的数组中,其中只有唯一的一个元素值重复,其他数字均只出现过一次.
设计一个算法,将重复元素找出来,要求每个元素只能访问一次.如果不使用辅助存储空间,能否设计一个算法实现.
"""
import copy

def Method1(array):
    if array == None:
        return -1
    length = len(array) - 1
    arr_dict = dict()
    for i in range(length):
        arr_dict[i + 1] = 0
    for item in array:
        if arr_dict[item] == 0:
            arr_dict[item] += 1
        elif arr_dict[item] == 1:
            return item

def Method2(array):
    result = array[0]
    for item in array[1 : ]:
        result = result ^ item
    for i in range(1000):
        result = result ^ (i + 1)
    return result

def Method3(array):
    if array == None:
        return -1
    index = 0
    while array[index] > 0:
        temp = array[index]
        array[index] = - temp
        index = temp
    return index

if __name__ == "__main__":
    array = [(i + 1) for i in range(1000)]
    array.append(125)
    replicated = Method1(array)
    print("Based on method1, The replicated element is : " , replicated)
    replicated = Method2(array)
    print("Based on method2, The replicated element is : " , replicated)
    array_copy = copy.deepcopy(array)
    replicated = Method3(array_copy)
    print("Based on method3, The replicated element is : " , replicated)