# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 15:09:30 2020

@author: Administrator
"""

"""
如题目诉述.代码写的有些糟糕,但是结果应该是对的,运用了快排中的partition的思路.
"""

def GetMid(arr):
    lens = len(arr)
    if lens % 2 == 1:
        o = 0 ; d = lens - 1  #中位数查询数组的起止位置
        start = o + 1 ; end = d ; pos = o  # 两个指针以及key的index
        while pos != (lens - 1) / 2:
            while start < end:
                if arr[start] < arr[pos]:
                    start += 1
                elif arr[end] > arr[pos]:
                    end -= 1
                else:
                    temp = arr[start] ; arr[start] = arr[end] ; arr[end] = temp
            if arr[start] < arr[pos]:
                temp = arr[start] ; arr[start] = arr[pos] ; arr[pos] = temp ; pos = start
            else :
                 temp = arr[start - 1] ; arr[start - 1] = arr[pos] ; arr[pos] = temp ; pos = start - 1
            if pos < (lens - 1) / 2:
                o = pos + 1 ; d = d ; start = o + 1 ; end = d ; pos = o 
            elif pos > (lens - 1) / 2:
                 o  = o ; d = pos - 1 ; start = o + 1; end = d ; pos = o
            else:
                break
        print("The middle number is : " , arr[pos])
    else:
        o = 0 ; d = lens - 1  #中位数查询数组的起止位置
        start = o + 1 ; end = d ; pos = o  # 两个指针以及key的index
        while pos != (lens - 2) / 2:
            while start < end:
                if arr[start] < arr[pos]:
                    start += 1
                elif arr[end] > arr[pos]:
                    end -= 1
                else:
                    temp = arr[start] ; arr[start] = arr[end] ; arr[end] = temp
            if arr[start] < arr[pos]:
                temp = arr[start] ; arr[start] = arr[pos] ; arr[pos] = temp ; pos = start
            else :
                 temp = arr[start - 1] ; arr[start - 1] = arr[pos] ; arr[pos] = temp ; pos = start - 1
            if pos < (lens - 2) / 2:
                o = pos + 1 ; d = d ; start = o + 1 ; end = d ; pos = o 
            elif pos > (lens - 2) / 2:
                 o  = o ; d = pos - 1 ; start = o + 1; end = d ; pos = o
            else:
                break
        midnum1 = arr[pos]
        while pos != (lens) / 2:
            while start < end:
                if arr[start] < arr[pos]:
                    start += 1
                elif arr[end] > arr[pos]:
                    end -= 1
                else:
                    temp = arr[start] ; arr[start] = arr[end] ; arr[end] = temp
            if arr[start] < arr[pos]:
                temp = arr[start] ; arr[start] = arr[pos] ; arr[pos] = temp ; pos = start
            else :
                 temp = arr[start - 1] ; arr[start - 1] = arr[pos] ; arr[pos] = temp ; pos = start - 1
            if pos < (lens) / 2:
                o = pos + 1 ; d = d ; start = o + 1 ; end = d ; pos = o 
            elif pos > (lens) / 2:
                 o  = o ; d = pos - 1 ; start = o + 1; end = d ; pos = o
            else:
                break
        midnum2 = arr[pos]
        print("The middle number is : " , (midnum1 + midnum2) / 2)


if __name__ == "__main__":
    arr = [7,5,3,1,11,9]
    GetMid(arr)