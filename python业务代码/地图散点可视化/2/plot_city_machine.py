# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 09:36:45 2019

@author: MyPC
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

def get_data_signalmachine():
    df = pd.read_excel('Data.xlsx' , sheet_name='example')
    # df.fillna(0 , inplace = True)
    # df.set_index('year' , inplace = True)
    df.drop(columns = ['NO' , '首次售出年份' , '总计'] , inplace = True)
    df.rename(columns = {'行标签':'city'} , inplace = True)
    df.set_index('city' , inplace = True)
    df = df.T
    df.rename(columns = {'合计' : 'total'} , inplace = True)
    # print(df)
    return df 

def plot_map(df):
    # maptype='china' 只显示全国直辖市和省级
    # 数据只能是省名和直辖市的名称
    # province_distribution = {'青岛': 22, '龙口': 37.56, '河北': 21, '辽宁': 12, '江西': 6, '上海': 20, '安徽': 10, '江苏': 16, '湖南': 9, '浙江': 13, '海南': 2, '广东': 22, '湖北': 8, '黑龙江': 11, '澳门': 1, '陕西': 11, '四川': 7, '内蒙古': 3, '重庆': 3, '云南': 6, '贵州': 2, '吉林': 3, '山西': 12, '山东': 11, '福建': 4, '青海': 1, '舵主科技，质量保证': 1, '天津': 1, '其他': 1}
    # provice=list(province_distribution.keys())
    # values=list(province_distribution.values())
    years = list(df.index)
    geos = []
    timeline = Timeline(width=1700,height=900,is_auto_play=True, timeline_bottom=-10,timeline_symbol_size=20,timeline_play_interval=400,timeline_left=20,timeline_right=100 , \
        is_timeline_show = False )
    for index in range(len(years)):
        cities = list(df.columns)
        cities.remove('total')
        values = list(df.loc[years[index] , :])
        total_num = values[-1]
        del(values[-1])
        # print(cities)
        # print(values)
    
        geos.append(Geo( str(int(total_num)), title_top="10%" , title_text_size=50 , subtitle = years[index] +" , subtitle",  \
            subtitle_text_size = 23 , subtitle_color="white", \
            title_color="red", title_pos="center", width=1200, height=600, \
            background_color='#404a59'))
        # type="effectScatter", is_random=True, effect_scale=5  使点具有发散性
        geos[index].add("title level1", cities, values, type="effectScatter", maptype='china' , is_random=True, effect_scale=3,  is_selected = True,is_toolbox_show = True ,is_more_utils =True,\
            visual_text_color="#fff", symbol_size=10, is_label_show = True ,  legend_orient = 'left' ,is_legend_show = False, legend_top = 'bottom' , label_formatter = '{b}' , \
            is_visualmap=True, is_roam=True , label_text_color="#00FF00" , is_piecewise=True, label_text_size = 7,visual_range=[1, 300] , \
            geo_cities_coords = {'赣江': [115.934192 , 28.826235] , '红河州' : [103.381549,23.369996] , '蒙自' : [103.371546,23.40208] , '海安' : [120.469259,32.544553] , \
                '济阳' : [117.023094,36.965519] , '库车' : [82.970183,41.733785] , '文山-砚山' : [104.334442,23.621612] , '文安':[116.455985,38.891083] , '罗平':[104.309188,24.890519] , \
                '宣城' : [118.762662,30.957007] , '古田' : [118.747401,26.596702] , '泗阳':[118.699691,33.723524] , }  , \
            pieces=[
                {"min":0.1, "max": 50 , "label": "0-50"},
                {"min": 51, "max": 100 , "label": "51-100"},
                {"min": 101, "max": 200 , "label": "101-200"},
                {"min":201, "max": 500, "label": "201-500"},
                {"min":500, "max": 2900, "label": ">500"}, ] )
        geos[index].show_config()
        geos[index].render("xxxx售出数量.html")
        #   时间轴定义
        timeline.add(geos[index],years[index] )
    timeline.render('final_graph.html')
    

def main():
    df = get_data_signalmachine()
    # print(df)
    plot_map(df)


if __name__ == "__main__":
    main()