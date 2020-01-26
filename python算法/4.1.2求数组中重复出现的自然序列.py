# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 09:13:54 2020

@author: Administrator
"""

"""
对于一个给定的自然数N,有一个N+M个元素的数组,其中存放了小于等于N的所有自然数,求重复出现的自然数序列{X}.
"""

def GetDupNum(array , num):
    # get the duplicated number of the array, the length of the different number array is N.
    s = set()
    if array == None:
        return s
    lens = len(array)
    index = array[0]  # initial the index
    num = lens - num  # get the number of the duplicated element in the array
    while True:
        if array[index] < 0:
            num -= 1
            array[index] = lens - num
            s.add(index)
        if num == 0:
            return s
        array[index] *= (-1)
        index = array[index] * (-1)

if __name__ == "__main__":
    array = [1,2,3,3,3,4,5,5,5,5,6]
    num = 6
    s = GetDupNum(array , num)
    for i in s:
        print(i , " " , end = "")