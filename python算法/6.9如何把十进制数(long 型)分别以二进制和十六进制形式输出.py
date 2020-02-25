# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 09:54:13 2020

@author: Administrator
"""

"""
如何把十进制数(long型)分别以二进制和十六进制形式输出
python3中没有long了,所以直接用int.
"""

def intToBinary(n):
    hexNum = 8 * 8
    bit = []
    for i in range(hexNum):
        b = n >> i
        c,d = divmod(b , 2)
        bit.append(str(d))
    return ''.join(bit[::-1])

def intToHex(s):
    hexs = ""
    remainder = 0
    while s != 0:
        remainder = s % 16
        if remainder < 10:
            hexs = str(remainder + int('0')) + hexs
        else:
            hexs = str(remainder - 10 + ord('A')) + hexs
        s = s >> 4
        return chr(int(hexs))

if __name__ == "__main__":
    print("10的二进制输出为:" + intToBinary(10))
    print("10的十六进制输出为:" + intToHex(10))  