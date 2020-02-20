# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 08:41:12 2020

@author: Administrator
"""

"""
编写一个截取字符串的函数,输入为一个字符串和字节数,输出为按字节截取的字符串.
但是要保证汉字不被截半个,例如"人ABC"4,应该截为"人AB",输入"人ABC们DEF",6,应该输出为"人ABC",而不是"人ABC+们的半个".

注意,在python中字符串就是用unicode编码的,因此print("\u4e00")就会打印出中文"一",python可以自动将uncode打印为中文.
本题只要能够确定一个字符是否是中文就变得很简单了.
"""

def isChineses(c):
    return True if c>="\u4e00" and c <= '\u9fa5' else False

def InterceptString(s , bitelen):
    for i in range(len(s)):
        if isChineses(s[i]):
            
            #print(bitelen)
            if bitelen >= 2:
                print(s[i] , end = " ")
                bitelen -= 2
            else:
                break
        else:
            if bitelen >= 1:
                print(s[i] , end = " ")
                bitelen -= 1
            else:
                break
        

if __name__ == "__main__":
    s = "人ABC们DEF"
    # s_uni = s.encode('unicode-escape').decode()
    interstr = InterceptString(s,6)
    #print("\u4e00")   # 在python中unicode会自动输出为中文
