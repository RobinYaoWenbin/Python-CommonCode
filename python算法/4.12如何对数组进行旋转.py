# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 10:39:07 2020

@author: Administrator
"""

"""
请实现方法:print_rotate_matrix(int matrix , int n),该方法用于将一个n*n的二维数组逆时针旋转45度后打印,
例如,下图显示一个3*3的二维数组及其旋转后屏幕输出的效果.
1 2 3 逆时针旋转45度        3                   3
4 5 6 ------------->     2   6     屏幕输出     2 6
7 8 9                  1   5   9  ---------->  1 5 9
                         4   8                 4 8
                           7                   7
"""                    

def print_rotate_matrix(matrix , n):
    for i in range(n):  # 打印上半个
        t = n - i - 1
        l = 0
        while t < n:
            print(matrix[l][t] , end = " ")
            t += 1
            l += 1
        print("")
    for i in range(n - 1):  # 打印下半个
        l = i + 1 ; t = 0
        while l < n:
            print(matrix[l][t] , end = " ")
            l += 1
            t += 1
        print("")

if __name__ == "__main__":
    arr = [[1,2,3],[4,5,6],[7,8,9]]
    print_rotate_matrix(arr , 3)