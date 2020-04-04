# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 08:43:28 2020

@author: Administrator
"""
import heapq

def Waittime(N , M , needtime):
    if N < M:
        return 0
    toltime = 0
    dafan = needtime[0:M]  # 打饭的同学及其需要的时间
    heapq.heapify(dafan)
    needtime = needtime[M:]
    while len(needtime) != 0:
        if len(dafan) < M:
            dafan.append(needtime[0])
            del needtime[0]
        else:
            # index = dafan.index(min(dafan))
            # mintime = dafan[index]
            mintime = heapq.heappop(dafan) 
            toltime += mintime
            for i in range(len(dafan)):
                dafan[i] -= mintime
    if len(dafan) == M:
        toltime += min(dafan)
    return toltime

def Waittime2(N , M , needtime):
    if N < M:
        return 0
    dafan = needtime[0:M] 
    heapq.heapify(dafan)
    needtime = needtime[M:]
    for i in range(len(needtime)):
        tmp = heapq.heappop(dafan)
        tmp += needtime[i]
        heapq.heappush(dafan , tmp)
    return heapq.heappop(dafan)


if __name__ == "__main__":
    N , M = input ().split(' ') #以空格为间隔符
    N = int(N) ; M = int(M)
    needtime = []
    for i in range(N):
        needtime.append(int(input()))
    print(Waittime2(N , M , needtime))
