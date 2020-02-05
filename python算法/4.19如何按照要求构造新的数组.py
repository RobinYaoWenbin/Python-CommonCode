# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 09:32:55 2020

@author: Administrator
"""

"""
给定一个数组a[N],希望构造一个新的数组b[N],其中,b[i]=a[0]*a[1]*```*a[N-1]/a[i].
在构造数组的过程中,有如下几点要求:
(a) 不允许使用除法;
(b) 要求O(1)空间复杂度和O(N)时间复杂度;
(c) 除遍历计数器与a[N],b[N]外,不可以使用新的变量(包括栈临时变量,堆空间和全局静态变量等);
(d) 请用程序实现并简单描述;
"""

def ConstructArr(a , b):
    # 利用a数组构造一个新的数组
    b[0] = 1 ; lens = len(a)
    for i in range(len(a) - 1):
        b[i + 1] = a[i] * b[i]
    for i in range(len(a) - 1):
        b[lens - i - 1] = b[lens - i - 1] * b[0]
        b[0] *= a[lens - i - 1]

if __name__ == "__main__":
    a = [1,2,3,4,5,6,7,8,9,10] ; b = [None] * len(a)
    ConstructArr(a , b)
    print("The constructed array is : ")
    for i in range(len(b)):
        print(b[i] , " " , end = "")