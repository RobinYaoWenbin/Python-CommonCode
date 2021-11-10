# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 14:32:51 2020

@author: Administrator
"""

import json
import urllib
import sys
import importlib
import os

class PointWithAttr(object):
    def __init__(self,id,lon,lat):
        self.id = id
        self.lon = lon
        self.lat = lat
        self.name = ''
        self.name1 = ''
        
    def __init__(self,id,lon,lat,type,name):
        self.id = id
        self.lon = lon
        self.lat = lat
        self.type = type
        self.name = name
        
class BoundryWithAttr(object):
    def __init__(self,point,boundrycoords):
        self.point = point
        self.boundrycoords = boundrycoords

class LineWithAttr(object):
    def __init__(self,name,coords):
        self.name = name
        # coords数据类型为列表
        self.coords = coords

def creatpoint(filename,idindex,lonindex,latindex,nameindex,name1index):
    doc = open(filename,'r')
    lines = doc.readlines()
    doc.close()
    points = []
    for line in lines:
        linesplit = line.split(',')
        id = linesplit[idindex]
        lon = linesplit[lonindex]
        lat = linesplit[latindex]
        name = linesplit[nameindex]
        name1 = linesplit[name1index]
        point = PointWithAttr(id , lon , lat , name , name1)
        points.append(point)
    return points

# 合并文件夹outputdirectory下的所有文本文件到finalfile
def mergetxt(outputdirectory , finalfile):
    f = open(finalfile , 'w' ,encoding="utf-8")
    f.close()
    with open(finalfile,'a' ,encoding="utf-8") as f:
        for filename in os.listdir(outputdirectory):
            file_path = os.path.join(outputdirectory , filename)
            with open(file_path , 'r',encoding="utf-8") as file1:
                context = file1.read()
            f.write(context)

# 百度坐标系转国测局坐标系(火星坐标,高德坐标,腾讯坐标)
def BDtoGCJ(ak , oldPoint):
        url = "http://restapi.amap.com/v3/assistant/coordinate/convert? key="+ak \
        + "&lacations=" + oldPoint.lon + "," + oldPoint.lat + "&coordsys=baidu"
        josn_obj = urllib2.urlopen(url)
        mydata = json.load(josn_obj)
        if mydata['info'] == "ok":
            newLon,newLat = mydata['locations'].split(',')
            newPoint = PointWithAttr(0,newLon,newLat,"GCJ02","GCJ02")
        else:
            print(mydata['info'])
            newPoint = '-1'
        return newPoint