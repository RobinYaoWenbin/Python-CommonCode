# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 19:57:22 2019

@author: wenbin
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib 
import math
import pymssql
import numpy as np
import copy
import re
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from pyecharts import Map, Geo , Timeline

def GetData():
    # get bus num at different year
    df = pd.read_csv("Data.csv" , encoding = 'gbk')
    df.rename(columns = {"城市" : "city" ,"年份":"year" , "数量":"num"} , inplace = True)
    df = df[['year' , 'city' , 'num']]
    return df

def ShowNumWithYear(df):
    # show bus num in different year at different cities
    years = list(set(df['year']))
    years.sort()
    cities = []
    values = []
    total_num = 0
    geos = [] # store the geo every year
    timeline = Timeline(width=1500,height=800,is_auto_play=True, timeline_bottom=-10,timeline_symbol_size=20,\
        timeline_play_interval = 800,timeline_left=20,timeline_right=100 , is_timeline_show = False )
    for index in range(len(years)):
        df_temp = df[df['year'] == years[index]]
        cities = cities + list(df_temp['city'])
        values = values + list(df_temp['num'])
        total_num = sum(values)
        geos.append(Geo( str(years[index]) + " , Fist level title" , title_top = "10%" , title_text_size=50 , subtitle = "second level title" , \
            subtitle_text_size = 23 , subtitle_color="white", \
            title_color="red", title_pos="center", width=1200, height=600, \
            background_color='#404a59'))
        # type="effectScatter", is_random=True, effect_scale=5  使点具有发散性
        geos[index].add("数量", cities, values, type="effectScatter", maptype='china' , is_random=True, effect_scale=3,  is_selected = True,is_toolbox_show = True ,is_more_utils =True,\
            visual_text_color="#fff", symbol_size=10, is_label_show = True ,  legend_orient = 'left' ,is_legend_show = False, legend_top = 'bottom' , label_formatter = '{b}' , \
            is_visualmap=True, is_roam=True , label_text_color="#00FF00" , is_piecewise=True, label_text_size = 7,visual_range=[1, 300] , \
            geo_cities_coords = {'柯桥': [120.443 , 30.0822] ,}  , \
            pieces=[
                {"min":0.1, "max": 500 , "label": "0-500"},
                {"min": 500, "max": 1000 , "label": "501-1000"},
                {"min": 1001, "max": 2000 , "label": "1001-2000"},
                {"min":2001, "max": 5000, "label": "2001-5000"},
                {"min":5001, "max": 100000, "label": ">5000"}, ] )
        geos[index].show_config()
        geos[index].render("数量.html")
        #   时间轴定义
        timeline.add(geos[index],years[index] )
    timeline.render('redult.html')

if __name__ == "__main__":
    df = GetData()
    # print(df) 
    ShowNumWithYear(df)