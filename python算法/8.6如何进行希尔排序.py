# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 15:38:52 2020

@author: Administrator
"""

"""
希尔排序:首先将待排序的元素分成多个子序列,使得每个子序列的元素个数相对较少,对各个子序列分别进行直接插入排序,
待整个待排序序列"基本有序后",再对所有元素进行一次直接插入排序.
"""

def ShellSort(seq , shelllist):
    # 希尔排序
    for shellnum in shelllist:
        start = 0 
        for i in range(shellnum):  # 共有shellnum组,对每一组分别进行排序
            poi2 = start ; poi = poi2
            while poi2 < len(seq):  # 这个while循环里面做一个插入排序.
                poi = poi2
                if seq[poi] <= seq[start]:
                    tmp = seq[poi]
                    while poi - shellnum >= 0:
                        seq[poi] = seq[poi - shellnum]
                        poi = poi - shellnum
                    seq[start] = tmp
                        
                elif seq[poi] >= seq[poi - shellnum]:
                    pass
                else:
                    for j in range(start , poi , shellnum):
                        if seq[j] <= seq[poi] and seq[j+shellnum] >= seq[poi]:
                            tmp = seq[poi]
                            while poi - shellnum >= j:
                                seq[poi] = seq[poi-  shellnum]
                                poi = poi - shellnum
                            seq[j+shellnum] = tmp
                            break
                poi2 += shellnum
            start += 1
    return seq



if __name__ == "__main__":
    seq = [3,4,2,8,9,5,1]
    print("The original sequence is : " , seq)
    seq = ShellSort(seq , [5 , 3 , 1])
    print("The sequence after sorting is : " , seq)