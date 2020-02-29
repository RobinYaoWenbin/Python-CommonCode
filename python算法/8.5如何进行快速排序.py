# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 10:14:03 2020

@author: Administrator
"""

"""
快速排序:取一个key,然后对后面的数据分成两部分,左半部分都比key小,右半部分都比key大.
"""

def QuickSort(seq , left , right):
    # 对seq序列从left到right排序
    if left >= right:
        return seq
    key = seq[left]
    low = left  # 记录下left的初始值.
    high = right  # 记录下right的初始值.
    while left < right:
        while left < right and seq[right] >= key:  # 找到seq[right] < key
            right -= 1
        seq[left] = seq[right]
        while left < right and seq[left] <= key:  # 找到seq[left] > key
            left += 1
        seq[right] = seq[left]
    seq[right] = key
    # print(left , right) # 最后结束上述while循环时left和right是相同的.
    QuickSort(seq , low , left - 1)
    QuickSort(seq , left + 1 , high)
    return seq

if __name__ == "__main__":
    seq = [3,4,2,8,9,5,1]
    print("The original sequence is : " , seq)
    seq = QuickSort(seq,0,len(seq)-1)
    print("The sequence after sorting is : " , seq)