# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 13:08:39 2019

@author: wenbin
"""

"""
this program is the algotithm of dijkstra
注意:本代码的中的节点就是list数组的index,为了和python保持一致,因此下标从0开始,若题目为从1开始,则可将父节点的下标+1
"""

class Dijkstra():
    def __init__(self , AdjacencyMatrix , StartVertex):
        self.AdjMat = AdjacencyMatrix
        self.Vs = StartVertex
        print("Dijkstra algotithm start seccessfully , the matrix is:")
        print(self.AdjMat)
        print("the start vertex is:" , self.Vs )

    def DijkstraProcess(self):
        """
        this func use Algorithm Dijkstra to deal with the class's data
        """
        Msize = len(self.AdjMat)  #得到的数据的行数
        Vt = []  #已经确定的点的集合
        Uvt = []  #还没确定的点的集合
        dis = []  #各个点的权重 or 距离
        dis_certain = []  #已经确定的各个点的权重
        pv = []  #各个点的父节点
        for i in range(Msize):
            dis.append(float("inf"))
            dis_certain.append(float("inf"))
            pv.append(None)
        dis[self.Vs] = 0
        dis[self.Vs] = 0
        for i in range(Msize):
            MinValue = min(dis)
            MinIndex = dis.index(MinValue)
            dis_certain[MinIndex] = MinValue
            dis[MinIndex] = float("inf")
            Vt.append(MinIndex)  #将已经确定的点加到Vt中
            for j in range(Msize):
                if (j != MinIndex and j not in set(Vt)) and self.AdjMat[MinIndex][j] < 1000000000:  #判断一下dis[j]是否小于inf
                    if dis_certain[MinIndex] + self.AdjMat[MinIndex][j] < dis[j]:
                        dis[j] = dis_certain[MinIndex] + self.AdjMat[MinIndex][j]
                        pv[j] = MinIndex
        print("distance" , dis_certain)  #各个节点的最短路,列表中的index就是节点的编号
        print("pv" , pv)  #各个节点的父节点,从0开始计数

def TestData():
    #初始化邻接矩阵
    AdjacencyMatrix = [[0, 1, 4 ,  float("inf"), float("inf")],
                        [1, 0, float("inf"), 2, float("inf")],
                        [1, float("inf"), 0, float("inf"), 1],
                        [float("inf"), 3, float("inf"), 0, 3],
                        [float("inf"), float("inf"), float("inf"), 2, 0]]
    StartVertex = 0 #最短路的起始点
    return AdjacencyMatrix , StartVertex

def OR17homework():
    #该例子是运筹学书本第10.7题的题目
    AdjacencyMatrix = [[0, 2, float("inf") ,8, float("inf"),float("inf"),float("inf"),float("inf"),float("inf"),float("inf"),float("inf")],
                        [float("inf"), 0, float("inf"), 6,1, float("inf"),float("inf"),float("inf"),float("inf"),float("inf"),float("inf")],
                        [1, float("inf"), 0, float("inf"),float("inf"),float("inf"),float("inf"),float("inf"),float("inf"),float("inf"),float("inf")],
                        [float("inf"),float("inf"), 7,0, float("inf"), float("inf"),float("inf"),float("inf"),float("inf"),float("inf"),float("inf")],
                        [float("inf"), float("inf"), float("inf"), 5, 0,float("inf"), float("inf"), float("inf"), 1,float("inf"), float("inf")],
                        [float("inf"), float("inf"), float("inf"), 1, 3,0,4,float("inf"), float("inf"), float("inf"),float("inf")],
                        [float("inf"), float("inf"), float("inf"), 2,float("inf"), float("inf"), 0,float("inf"),3,1,float("inf")],
                        [float("inf"),float("inf"),float("inf"),float("inf"),2,float("inf"),float("inf"),0,float("inf"),float("inf"),9],
                        [float("inf"),float("inf"),float("inf"),float("inf"),float("inf"),6 , float("inf"),7,0,float("inf"),float("inf")],
                        [float("inf"),float("inf"),float("inf"),float("inf"),float("inf"),float("inf"),float("inf"),float("inf"),1,0,4],
                        [float("inf"),float("inf"),float("inf"),float("inf"),float("inf"),float("inf"),float("inf"),float("inf"),2,float("inf"),0]]
    StartVertex = 0 #最短路的起始点
    return AdjacencyMatrix , StartVertex

if __name__ == "__main__":
    # AdjacencyMatrix , StartVertex = TestData()
    AdjacencyMatrix , StartVertex = OR17homework()
    DijExample = Dijkstra(AdjacencyMatrix , StartVertex)
    DijExample.DijkstraProcess()