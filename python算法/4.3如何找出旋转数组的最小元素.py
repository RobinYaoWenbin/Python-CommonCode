# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 10:09:16 2020

@author: Administrator
"""

"""
把一个有序数组最开始的若干个元素搬到数组的末尾,称之为数组的旋转.输入一个排好序的数组的一个旋转,输出旋转数组的最小元素.
例如,数组[3,4,5,1,2]为数组[1,2,3,4,5]的一个旋转,该数组的最小值为1.
"""

def GetMininArray(array):
    for i in range(len(array)):
        if array[len(array) - i - 1] >= array[len(array) - i - 2]: 
            pass
        else:
            return array[len(array) - i - 1]

def RotateArray(array , N):
    # rotate the array. Putting the first N elements into the last of the array.
    lens = len(array)
    for i in range(N):
        temp = array[i]
        array[i] = array[lens - N + i]
        array[lens - N + i] = temp
    return


if __name__ == "__main__":
    array = [3 , 4 , 5 , 1 , 2]
    minv = GetMininArray(array)
    print("The minimum value in the array is : " , minv)
    array = [1,2,3,4,5,6]
    RotateArray(array , 3)
    print("The rotated array is : " , array)