# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 10:28:09 2020

@author: Administrator
"""

"""
把一个含有N个元素的数组循环右移K位,要求时间复杂度是O(N),且只允许使用两个附加变量.
"""

def FlipArr(arr , start , end):
    # 将array中index从start到end的元素翻转一下,包括start,但是不包括end.
    mid = int((end - start) / 2)
    for i in range(mid):
        temp = arr[start + i] ; arr[start + i] = arr[end - 1 - i] ; arr[end - 1 - i] = temp

def RotateRight(arr , k):
    # 将arr做一个循环右移k位
    lens = len(arr)
    if k < lens:
        pass
    else:
        k = k % lens
    FlipArr(arr , 0 , lens - k)
    FlipArr(arr , lens - k , lens)
    FlipArr(arr , 0 , lens)
    print("The array after flipping is : ")
    for i in range(lens):
        print(arr[i] , end = " ")

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8]
    RotateRight(arr , 10)