# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 20:02:32 2020

@author: Administrator
"""

"""
假设有一个中央调度机,有n个任务相同的任务需要调度到m台服务器上执行,由于每台服务器的配置不一样,因此,服务器执行一个任务所
花费的时间也不同.现在假设第i个服务器执行一个任务需要的时间为t[i]。假如,有2个执行机a与b,执行一个任务分别需要7min和10min,
有6个任务待调度.如果平分这6个任务,即a与b各3个任务,则最短需要30min执行完所有.如果a分4个任务,b分2个任务,则最短28min执行完.
请设计调度算法,使得所有任务完成所需要的时间最短.输入m台服务器,每台机器处理一个任务的时间为t[i],完成n个任务,
输出n个任务在m台服务器的分布.estimate_process_time(t,m,n)。
"""

def estimate_process_time(t , m , n):
    ans = [0] * m
    totaltime = 0 
    while sum(ans) < n:
        index = 0 ;  nexttotaltime = 2**20
        for i in range(m):
            tmp = t[i] * (ans[i] + 1)
            if tmp < totaltime:
                nexttotaltime = totaltime
                index = i
                break
            if tmp < nexttotaltime:
                nexttotaltime = tmp ; index = i
        totaltime = nexttotaltime ; ans[index] += 1
    return ans , totaltime

if __name__ == "__main__":
    t = [7 , 10]
    m = len(t) ; n = 6
    ans , totaltime = estimate_process_time(t , m , n)
    print("Server task assigned as : \n" , ans)
    print("Total time is : " , totaltime)
