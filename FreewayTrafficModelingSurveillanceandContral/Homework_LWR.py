# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 20:04:03 2019

@author: Wenbin Yao
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

#define the global variable
UnitX = 0.5  #every segment's length
UnitTime = 0.00278  #unit time
K = 180 #total round
Vf = 100  #free speed
DensityMax = 160 
rk = 800  #for every time, on ramp flow is 800 veh/h
beta = 0.1  #off ramp coefficient
DensityIni = 20  #every segment's initial density

class Segment:
    # define a class of segment.
    kt = 0 #document the time of round
    QoutNext_k2 = 0 #the flow of next segment at the time kt.
    Density_k1 = 0 #the density of time kt - 1
    Density_k2 = 0 #the density of time kt 
    Velocity = 0  #the speed of the segment at the time kt
    SegOrd = 0 #the order of segment
    QoutLast_k1 = 0  # last segment's flow at the time kt - 1
    Qout_k1 = 0  # flow of time kt - 1
    Qout_k2 = 0 #flow of time kt

    def __init__(self , DensityNextSeg_k2 , Density_k1 , kt , SegOrd , QoutLast_k1 , Qout_k1):
        self.DensityNextSeg_k2 = DensityNextSeg_k2
        self.Density_k1 = Density_k1
        self.kt = kt
        self.SegOrd = SegOrd
        self.QoutLast_k1 = QoutLast_k1
        self.Qout_k1 = Qout_k1

    def GetParameter(self):
        if self.SegOrd == 0 or self.SegOrd == 2 or self.SegOrd == 3 or self.SegOrd == 5:
            #get the parameter of the segment that we need, which is the order 1,3,4,6. there is no ramp.
            temp = self.Density_k1 + UnitTime / UnitX * (self.QoutLast_k1 - self.Qout_k1) #get next time density
            if temp > 160:
                self.Density_k2 = 160
            elif temp < 0:
                self.Density_k2 = 0
            else:
                self.Density_k2 = temp
            # get Qout at time kt
            if self.Density_k2 <= 80:
                QDemand = self.Density_k2 * Vf * (1 - self.Density_k2 / DensityMax)
            elif self.Density_k2 > 80:
                QDemand = 4000
            if self.DensityNextSeg_k2 <= 80:
                QCapNextSeg = 4000
            elif self.DensityNextSeg_k2 > 80:
                QCapNextSeg = self.DensityNextSeg_k2 * Vf * (1 - self.DensityNextSeg_k2 / DensityMax)
            self.Qout_k2 = min(QDemand , QCapNextSeg)

            #fet velocity
            if self.Density_k2 < 0.0000000001:
                self.Velocity = 0
            else:
                self.Velocity = self.Qout_k2 / self.Density_k2
            
        elif self.SegOrd == 1:
            #get the parameter of the segment that we need, which is the order 2. there is off ramp.
            temp = self.Density_k1 + UnitTime / UnitX * (self.QoutLast_k1 - self.Qout_k1 - beta * self.QoutLast_k1) #get next time density
            if temp > 160:
                self.Density_k2 = 160
            elif temp < 0:
                self.Density_k2 = 0
            else:
                self.Density_k2 = temp
            # get Qout at time kt
            if self.Density_k2 <= 80:
                QDemand = self.Density_k2 * Vf * (1 - self.Density_k2 / DensityMax)
            elif self.Density_k2 > 80:
                QDemand = 4000
            if self.DensityNextSeg_k2 <= 80:
                QCapNextSeg = 4000
            elif self.DensityNextSeg_k2 > 80:
                QCapNextSeg = self.DensityNextSeg_k2 * Vf * (1 - self.DensityNextSeg_k2 / DensityMax)
            self.Qout_k2 = min(QDemand , QCapNextSeg)
            #get velocity
            if self.Density_k2 < 0.0000000001:
                self.Velocity = 0
            else:
                self.Velocity = self.Qout_k2 / self.Density_k2

        elif self.SegOrd == 4:
            # get the parameter of the segment that we need, which is the order 4. there is on ramp.
            temp = self.Density_k1 + UnitTime / UnitX * (self.QoutLast_k1 - self.Qout_k1 + rk ) #get next time density
            if temp > 160:
                self.Density_k2 = 160
            elif temp < 0:
                self.Density_k2 = 0
            else:
                self.Density_k2 = temp
            # get Qout at time kt
            if self.Density_k2 <= 80:
                QDemand = self.Density_k2 * Vf * (1 - self.Density_k2 / DensityMax)
            elif self.Density_k2 > 80:
                QDemand = 4000
            if self.DensityNextSeg_k2 <= 80:
                QCapNextSeg = 4000
            elif self.DensityNextSeg_k2 > 80:
                QCapNextSeg = self.DensityNextSeg_k2 * Vf * (1 - self.DensityNextSeg_k2 / DensityMax)
            self.Qout_k2 = min(QDemand , QCapNextSeg)
            #get velocity
            if self.Density_k2 < 0.0000000001:
                self.Velocity = 0
            else:
                self.Velocity = self.Qout_k2 / self.Density_k2

        else:
            print("There is no such segment, please check the order of segment!")

def Time(kt , SegmentListLasttime):
    '''
    calculate the traffic flow of kt time
    input:kt:time ; SegmentListLasttime:a list of cevery segment last time
    '''
    if kt == 1:  # first time of evolution of the link
        SegmentList = [0 for j in range(6)]  # new a list to store the segment 1-6 of this time
        for i in range(6):
            j = 5 - i
            if j == 5:
                SegmentTemp = Segment(0 , 20 , kt , j , 1750 , 1750)
                SegmentTemp.GetParameter()
                SegmentList[j] = SegmentTemp
            elif j == 0:
                SegmentTemp = Segment(SegmentList[j + 1].Density_k2 , 20 , kt , j , 4000 , 1750)
                SegmentTemp.GetParameter()
                SegmentList[j] = SegmentTemp
            else:
                SegmentTemp = Segment(SegmentList[j + 1].Density_k2 , 20 , kt , j , 1750 , 1750)
                SegmentTemp.GetParameter()
                SegmentList[j] = SegmentTemp
        return SegmentList
    elif kt > 1 and kt <= 100:
        SegmentList = [0 for j in range(6)]  #new a list to store the segment1-6 of this time
        for i in range(6):
            j = 5 - i
            if j == 5:
                SegmentTemp = Segment(0 , SegmentListLasttime[j].Density_k2 , kt , j , \
                    SegmentListLasttime[j - 1].Qout_k2 , SegmentListLasttime[j].Qout_k2)
                SegmentTemp.GetParameter()
                SegmentList[j] = SegmentTemp
            elif j == 0:
                SegmentTemp = Segment(SegmentList[j + 1].Density_k2 , SegmentListLasttime[j].Density_k2 , kt , j , \
                    4000 , SegmentListLasttime[j].Qout_k2)
                SegmentTemp.GetParameter()
                SegmentList[j] = SegmentTemp
            else:
                SegmentTemp = Segment(SegmentList[j + 1].Density_k2 , SegmentListLasttime[j].Density_k2 , kt , j , \
                    SegmentListLasttime[j - 1].Qout_k2 , SegmentListLasttime[j].Qout_k2)
                SegmentTemp.GetParameter()
                SegmentList[j] = SegmentTemp
        return SegmentList
    elif kt > 100 and kt <= 180:
        SegmentList = [0 for j in range(6)]  #new a list to store the segment1-6 of this time
        for i in range(6):
            j = 5 - i
            if j == 5:
                SegmentTemp = Segment(0 , SegmentListLasttime[j].Density_k2 , kt , j , \
                    SegmentListLasttime[j - 1].Qout_k2 , SegmentListLasttime[j].Qout_k2)
                SegmentTemp.GetParameter()
                SegmentList[j] = SegmentTemp
            elif j == 0:
                SegmentTemp = Segment(SegmentList[j + 1].Density_k2 , SegmentListLasttime[j].Density_k2 , kt , j , \
                    2000 , SegmentListLasttime[j].Qout_k2)
                SegmentTemp.GetParameter()
                SegmentList[j] = SegmentTemp
            else:
                SegmentTemp = Segment(SegmentList[j + 1].Density_k2 , SegmentListLasttime[j].Density_k2 , kt , j , \
                    SegmentListLasttime[j - 1].Qout_k2 , SegmentListLasttime[j].Qout_k2)
                SegmentTemp.GetParameter()
                SegmentList[j] = SegmentTemp
        return SegmentList
    else:
        print("Time restricted to 0-180, other time still not support!")
        return None

def TimeSpacePlot(SegmentTimeseries):
    # 3-dimensional time-space plots for the speed and density
    SpeedList = []  # store every segment's speed over time
    DensityList = []  # store every segment's density over time
    for i in range(6):
        tempspeed = []  #store segment's flow over time
        tempdensity = [] #same func with above
        for ti in range(1 , K + 1):
            tempspeed.append(SegmentTimeseries[ti][i].Velocity)
            tempdensity.append(SegmentTimeseries[ti][i].Density_k2)
        SpeedList.append(tempspeed)
        DensityList.append(tempdensity)

    # plot 3-dimensional time-space plots for the speed 
    TimeList = np.linspace(1, 180 , 180) #X轴数据
    SegmentList = [0 for j in range(180)]
    SpeedList2 = SpeedList[0]
    DensityList2 = DensityList[0]

    # new a figure and set it into 3d
    plt.rcParams['savefig.dpi'] = 300 #图片像素
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # set figure information
    ax.set_title(" 3-dimensional time-space plots for the speed ")
    ax.set_xlabel("Time(Unit)")
    ax.set_ylabel("Segment(start from 0)")
    ax.set_zlabel("Speed(km/h)")
    for i in range(5):
        TimeList = np.append(TimeList , np.linspace(1, 180 , 180))
        SegmentList = np.append(SegmentList , [(i + 1) for j in range(180)])
        SpeedList2 = np.append(SpeedList2 , SpeedList[i + 1])
        DensityList2 = np.append(DensityList2 , DensityList[i + 1])
    surf = ax.plot_trisurf(TimeList, SegmentList , SpeedList2 , cmap=cm.jet, linewidth=0.2)
    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.savefig('速度三维时空图.png')
    plt.show()

    plt.rcParams['savefig.dpi'] = 300 #图片像素
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    # set figure information
    ax.set_title("3-dimensional time-space plots for the density ")
    ax.set_xlabel("Time(Unit)")
    ax.set_ylabel("Segment(start from 0)")
    ax.set_zlabel("Density(veh/km)")
    surf = ax.plot_trisurf(TimeList, SegmentList , DensityList2 , cmap=cm.jet, linewidth=0.2)
    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.savefig('密度三维时空图.png')
    plt.show()

def FlowDensityPlot(SegmentTimeseries):
    # plot of Flow and Density diagram over time
    FlowList = []  # store every segment's flow over time
    DensityList = []  # store every segment's density over time
    for i in range(6):
        tempflow = []  #store segment's flow over time
        tempdensity = [] #same func with above
        for ti in range(1 , K + 1):
            tempflow.append(SegmentTimeseries[ti][i].Qout_k2)
            tempdensity.append(SegmentTimeseries[ti][i].Density_k2)
        FlowList.append(tempflow)
        DensityList.append(tempdensity)
    #plot 
    plt.rcParams['savefig.dpi'] = 300 #图片像素
    plt.figure(figsize=(8,4))
    x = np.linspace(1, 180 , 180)#X轴数据
    for i in range(6):
        plt.plot(x , FlowList[i] , label = "Segment" + str(i) , linewidth=2)#将$包围的内容渲染为数学公式
    plt.xlabel("Time(Unit)")
    plt.ylabel("Flow(veh/hour)")
    plt.title("Line chart of flow changing with time")
    # plt.ylim(-1.5,1.5)
    plt.legend()#显示左下角的图例
    plt.savefig('流量随时间变化折线图.png')
    plt.show()

    #plot density changing with time
    for i in range(6):
        plt.plot(x , DensityList[i] , label = "Segment" + str(i) , linewidth=2)#将$包围的内容渲染为数学公式
    plt.xlabel("Time(Unit)")
    plt.ylabel("Density(veh/km)")
    plt.title("Line chart of density changing with time")
    # plt.ylim(-1.5,1.5)
    plt.legend()#显示左下角的图例
    plt.savefig('密度随时间变化折线图.png')
    plt.show()

if __name__ == "__main__":
    SegmentTimeseries = []  #set a list to store every time's segment list
    SegmentTimeseries.append(None)
    SegmentListLasttime = None  #initialize the SegmentListLasttime
    for ti in range(1 , K + 1):
        SegmentTimeseries.append( Time(ti , SegmentListLasttime) )
        SegmentListLasttime = SegmentTimeseries[ti]  #update SegmenntLasttime
    
    # Test blow result is right
    print("Time 1 segment 0 : Qout: " , SegmentTimeseries[1][0].Qout_k2 , " veh/hour") 
    print("Time 2 segment 0 : Density: " , SegmentTimeseries[2][0].Density_k2 , " veh/km")
    print("Time 50 segment 5 : Qout: " , SegmentTimeseries[50][5].Qout_k2 , " veh/hour")
    print("Time 180 segment 3 : Qout: " , SegmentTimeseries[180][3].Qout_k2 , " veh/hour")
    print("Time 180 segment 4 : Qout: " , SegmentTimeseries[180][4].Qout_k2 , " veh/hour")

    # plot Flow and Density diagram over time
    FlowDensityPlot(SegmentTimeseries)

    # 3-dimensional time-space plots for the speed and density
    TimeSpacePlot(SegmentTimeseries)