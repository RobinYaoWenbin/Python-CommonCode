# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 10:06:55 2020

@author: Administrator
"""

"""
数组中有N+2个数,其中,N个数出现了偶数次,2个数出现了奇数次(这两个数不相等),请用O(1)的空间复杂度,找出这两个数.
注意:不需要知道具体位置,只需要找出这两个数.
"""

def FindOdd(array):
    # there are N + 2 numbers in the array, find the number that appears in the odd times.
    ORv = array[0]
    for item in array[1 : ]:
        ORv ^= item
    obORv = str(bin(ORv));  obORv = obORv[2:]
    for i in range(len(obORv)):
        if obORv[len(obORv) - 1 - i] == '1':
            break
    N = i  # 转为二进制后的第N位为1
    ORNEEDARR = [] # 存储数组中所有二进制表示下第N位为1元素
    for index in range(len(array)):
        obtmp = str(bin(array[index])) ; obtmp = obtmp[2:]
        if (len(obtmp) < (N + 1)) and (obtmp[len(obtmp) - 1 - N] == '1'):
            ORNEEDARR.append(array[index])
    OddNum1 = ORv
    for item in ORNEEDARR:
        OddNum1 ^= item
    OddNum2 = ORv ^ OddNum1
    return OddNum1 , OddNum2

if __name__ == "__main__":
    array = [3 , 5 , 6 , 6 , 5 , 7 , 2 , 2]
    OddNum1 , OddNum2 = FindOdd(array)
    print("Two numbers that appears odd times in the array are : " , OddNum1 , " and " , OddNum2)
