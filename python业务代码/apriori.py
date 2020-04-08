# -*- coding: utf-8 -*-
"""
Created on Wed Apr 08 16:43:21 2020

@author: wenbin

"""

from numpy import *
import pandas as pd
 
# 构造数据
def loadDataSet():
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]
 
# 将所有元素转换为frozenset型字典，存放到列表中
def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    # 使用frozenset是为了后面可以将这些值作为字典的键
    return list(map(frozenset, C1))  # frozenset一种不可变的集合，set可变集合
 
# 过滤掉不符合支持度的集合
# 返回 频繁项集列表retList 所有元素的支持度字典
def scanD(D, Ck, minSupport):
    ssCnt = {}
    for tid in D:
        for can in Ck:
            if can.issubset(tid):   # 判断can是否是tid的《子集》 （这里使用子集的方式来判断两者的关系）
                if can not in ssCnt:    # 统计该值在整个记录中满足子集的次数（以字典的形式记录，frozenset为键）
                    ssCnt[can] = 1
                else:
                    ssCnt[can] += 1
    numItems = float(len(D))
    retList = []        # 重新记录满足条件的数据值（即支持度大于阈值的数据）
    supportData = {}    # 每个数据值的支持度
    for key in ssCnt:
        support = ssCnt[key] / numItems
        if support >= minSupport:
            retList.insert(0, key)
        supportData[key] = support
    return retList, supportData # 排除不符合支持度元素后的元素 每个元素支持度
 
# 生成所有可以组合的集合
# 频繁项集列表Lk 项集元素个数k  [frozenset({2, 3}), frozenset({3, 5})] -> [frozenset({2, 3, 5})]
def aprioriGen(Lk, k):
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk): # 两层循环比较Lk中的每个元素与其它元素
        for j in range(i+1, lenLk):
            L1 = list(Lk[i])[:k-2]  # 将集合转为list后取值
            L2 = list(Lk[j])[:k-2]
            L1.sort(); L2.sort()        # 这里说明一下：该函数每次比较两个list的前k-2个元素，如果相同则求并集得到k个元素的集合
            if L1==L2:
                retList.append(Lk[i] | Lk[j]) # 求并集
    return retList  # 返回频繁项集列表Ck
 
# 封装所有步骤的函数
# 返回 所有满足大于阈值的组合 集合支持度列表
def apriori(dataSet, minSupport = 0.5):
    D = list(map(set, dataSet)) # 转换列表记录为字典  [{1, 3, 4}, {2, 3, 5}, {1, 2, 3, 5}, {2, 5}]
    C1 = createC1(dataSet)      # 将每个元素转会为frozenset字典    [frozenset({1}), frozenset({2}), frozenset({3}), frozenset({4}), frozenset({5})]
    L1, supportData = scanD(D, C1, minSupport)  # 过滤数据
    L = [L1]
    k = 2
    while (len(L[k-2]) > 0):    # 若仍有满足支持度的集合则继续做关联分析
        Ck = aprioriGen(L[k-2], k)  # Ck候选频繁项集
        Lk, supK = scanD(D, Ck, minSupport) # Lk频繁项集
        supportData.update(supK)    # 更新字典（把新出现的集合:支持度加入到supportData中）
        L.append(Lk)
        k += 1  # 每次新组合的元素都只增加了一个，所以k也+1（k表示元素个数）
    return L, supportData

 
####################################################################################
 # 关联规则挖掘

def calSupport(ab , dataSet):
    count = 0
    for i in range(len(dataSet)):
        if ab.issubset(set(dataSet[i])) :
            count += 1
    return count / len(dataSet)

def calCon(a , b , dataSet , supportData ):
    tmp1 = set(a) ; tmp2 = set(b)
    ab = frozenset(tmp1.union(tmp2))
    if ab in supportData.keys():
        con = supportData[ab] / supportData[a]
    else:

        tmp = calSupport(ab , dataSet)
        con = tmp / supportData[a]
    return con

def geneRule(L, supportData,dataSet , minConf=0.7 ):
    for i in range(len(L)):
        for j in range(len(L)):
            for k in range(len(L[i])):
                for m in range(len(L[j])):
                    if i == j and k == m:
                        pass
                    else:
                        tmp = calCon(L[i][k] , L[j][m] , dataSet , supportData )
                        if tmp >= minConf:
                            print(L[i][k] , " -> " , L[j][m] , " , confidence = " , tmp)


#####################################################################################
# 数据整理及主函数

def splitstr(x):
    x = x[1:-1]
    x = x.split(",")
    return x


def GetData():
    # read data from csv
    df = pd.read_csv("Groceries.csv" , encoding = 'gbk')
    df = df[['items']]
    df = df.applymap(splitstr)
    data = []
    for index in range(len(df)):
        data.append(df.iloc[index , 0])
    return data


if __name__ == "__main__":
    dataSet = GetData()
    # dataSet = loadDataSet()
    L,suppData = apriori(dataSet,minSupport=0.15)
    del L[-1]
    geneRule(L,suppData, dataSet , minConf=0.2 )
    print("频繁项集:")
    print(L)
    # print("rules:")
    # print(rules)