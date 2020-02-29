# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 21:23:57 2020

@author: Administrator
"""

"""
归并排序:将数组分成两部分,分别对左右两部分进行排序,然后将排序好的两个子序列合并即可.
"""

def MergeSort(seq , start , end):
    # 对seq进行排序,start和end分别是左闭右开
    if start >= end - 1:
        return seq
    mid = int((end + start) / 2)
    seq = MergeSort(seq , start , mid)
    seq = MergeSort(seq , mid , end)
    i = start ; j = mid
    tmp = []
    tmp.extend(seq[:start])
    while i < mid and j < end:
        if seq[i] <= seq[j]:
            tmp.append(seq[i]) ; i += 1
        else:
            tmp.append(seq[j]) ; j += 1
    if i < mid:
        tmp.extend(seq[i:mid])
    elif j < end:
        tmp.extend(seq[j:end])
    else:pass
    tmp.extend(seq[end:])
    seq = tmp
    return seq


if __name__ == "__main__":
    seq = [3,4,2,8,9,5,1]
    print("The original sequence is : " , seq)
    seq = MergeSort(seq,0,len(seq))
    print("The sequence after sorting is : " , seq)