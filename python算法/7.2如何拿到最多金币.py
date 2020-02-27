# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 09:32:58 2020

@author: Administrator
"""

"""
10个房间里放着数量随机的金币,每个房间只能进入一次,并只能在一个房间中拿金币.一个人采取如下策略:前4个房间只看不拿.
随后的房间只要看到比前4个房间都多的金币数就拿.否则就拿最后一个房间的金币.编程计算这种策略拿到最多金币的概率.
"""

import random

def GetLarGoad():
    med = []  # 10个房间的金币数量
    for i in range(10):
        med.append(random.randint(1,100))
    max4 = max(med[0:4]) ; mostgoad = 0
    for i in range(4 , 10):
        if med[i] > max4:
            mostgoad = med[i]
            break
    if mostgoad == 0:
        mostgoad = med[-1]
    if mostgoad == max(med):
        return 1
    else:
        return 0

if __name__ == "__main__":
    count = 0 ; N = 10000
    for i in range(N):
        if GetLarGoad():
            count += 1
        else:
            pass
    pro = count  / N
    print("The probability of getting the most goad coins is : " , pro)