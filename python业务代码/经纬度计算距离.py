# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:47:52 2019

@author: Administrator
"""

import math

EARTH_REDIUS = 6378.137

def rad(d):
    return d * math.pi / 180.0

def getDistance(point1 , point2):
    #本函数用来计算两个经纬度坐标间的直线距离
    lng1 = point1[0]
    lat1 = point1[1]
    lng2 = point2[0]
    lat2 = point2[1]
    radLat1 = rad(lat1)
    radLat2 = rad(lat2)
    a = radLat1 - radLat2
    b = rad(lng1) - rad(lng2)
    s = 2 * math.asin(math.sqrt(math.pow(math.sin(a/2), 2) + math.cos(radLat1) * \
        math.cos(radLat2) * math.pow(math.sin(b/2), 2)))
    s = s * EARTH_REDIUS
    return s

print(getDistance((129.30 , 38.26) , (120.40 , 30.35)))