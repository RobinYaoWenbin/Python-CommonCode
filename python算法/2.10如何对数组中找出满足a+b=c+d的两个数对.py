# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 20:16:04 2019

@author: wenbin
"""

"""
给定一个数组,找出数组中是否有两个数对(a , b)和(c , d),使得a+b=c+d,其中a , b , c , d是不同的元素.
如果有多种答案,打印任意一个即可.例如给定数组:[3 , 4 , 7 , 10 , 20 , 9 , 8],可以找到两个数对(3 , 8)和(4 , 7),使得3+8=4+7.
"""

def GetSamePairs():
    arr = [ 3 , 4 , 7 , 10 , 20 , 9 , 8]
    arrnum = len(arr)
    sumdict = dict()
    for i in range(arrnum):
        for j in range( i + 1 , arrnum):
            pairsum = arr[i] + arr[j]
            if pairsum not in sumdict:
                sumdict[pairsum] = (i , j)
            else:
                sameturple = sumdict[pairsum]
                print("the same sum pairs are : ( " , arr[sameturple[0]] , " , " ,  arr[sameturple[1]] , \
                    " ) and ( " , arr[i] , " , "  , arr[j] , " )" )
                return None
    print("Failing to output the same sum pairs!!!")

if __name__ == "__main__":
    GetSamePairs()