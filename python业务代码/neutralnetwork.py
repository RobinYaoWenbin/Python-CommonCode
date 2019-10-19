# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 23:02:13 2019

@author: wenbin
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold
from sklearn.neural_network import MLPRegressor
from sklearn import preprocessing
import numpy as np
import copy

def GetData():
    #get the data from csv
    df = pd.read_csv("DealData.csv" , encoding = 'gbk')
    return df

def NeutralNetwork(df):
    #train data with MLP, and do the k fold cv
    score1 = 0 ; score2 = 0 ; score3 = 0 ; score4 = 0
    data = df.values  #transform the dataframe to the ndarray
    kf = KFold( n_splits = 10 )
    for train_index , test_index in kf.split(data):
        TrainData , TestData = data[train_index] , data[test_index]  #get train data and test data

        #standard the data
        min_max_scaler = preprocessing.MinMaxScaler()
        TrainData_sta = min_max_scaler.fit_transform(TrainData)
        TestData_sta = min_max_scaler.transform(TestData)

        #get the train data's feature and parameters
        TrainData_sta_x = TrainData_sta[: , 0:6]
        TrainData_sta_y1 = TrainData_sta[: , 6]
        TrainData_sta_y2 = TrainData_sta[: , 7]
        TrainData_sta_y3 = TrainData_sta[: , 8]
        TrainData_sta_y4 = TrainData_sta[: , 9]

        #get the test data's feature and parameters
        TestData_sta_x = TestData_sta[: , 0:6]
        TestData_sta_y1 = TestData_sta[: , 6]
        TestData_sta_y2 = TestData_sta[: , 7]
        TestData_sta_y3 = TestData_sta[: , 8]
        TestData_sta_y4 = TestData_sta[: , 9]

        #train MLPregressor, and i strongly recomend that do not need to train 4 model, that's strange.
        #just train one, and output a vector containing 4 elements.
        model_mlp1 = MLPRegressor(
            hidden_layer_sizes=(12 , ),  activation='relu', solver='adam', alpha=0.0001, batch_size='auto',
            learning_rate='constant', learning_rate_init=0.1, power_t=0.5, max_iter=5000, shuffle=True,
            random_state=1, tol=0.0001, verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True,
            early_stopping=False,beta_1=0.9, beta_2=0.999, epsilon=1e-08)
        model_mlp1.fit(TrainData_sta_x , TrainData_sta_y1)
        Result_y1 = model_mlp1.predict(TestData_sta_x)

        model_mlp2 = MLPRegressor(
            hidden_layer_sizes=(12 , ),  activation='relu', solver='adam', alpha=0.0001, batch_size='auto',
            learning_rate='constant', learning_rate_init=0.1, power_t=0.5, max_iter=5000, shuffle=True,
            random_state=1, tol=0.0001, verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True,
            early_stopping=False,beta_1=0.9, beta_2=0.999, epsilon=1e-08)
        model_mlp2.fit(TrainData_sta_x , TrainData_sta_y2)
        Result_y2 = model_mlp2.predict(TestData_sta_x)

        model_mlp3 = MLPRegressor(
            hidden_layer_sizes=(12 , ),  activation='relu', solver='adam', alpha=0.0001, batch_size='auto',
            learning_rate='constant', learning_rate_init=0.1, power_t=0.5, max_iter=5000, shuffle=True,
            random_state=1, tol=0.0001, verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True,
            early_stopping=False,beta_1=0.9, beta_2=0.999, epsilon=1e-08)
        model_mlp3.fit(TrainData_sta_x , TrainData_sta_y3)
        Result_y3 = model_mlp3.predict(TestData_sta_x)

        model_mlp4 = MLPRegressor(
            hidden_layer_sizes=(12 , ),  activation='relu', solver='adam', alpha=0.0001, batch_size='auto',
            learning_rate='constant', learning_rate_init=0.1, power_t=0.5, max_iter=5000, shuffle=True,
            random_state=1, tol=0.0001, verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True,
            early_stopping=False,beta_1=0.9, beta_2=0.999, epsilon=1e-08)
        model_mlp4.fit(TrainData_sta_x , TrainData_sta_y4)
        Result_y4 = model_mlp4.predict(TestData_sta_x)

        #get the predict data
        ResultData = copy.deepcopy(TestData_sta)
        ResultData[: , 6] = Result_y1
        ResultData[: , 7] = Result_y2
        ResultData[: , 8] = Result_y3
        ResultData[: , 9] = Result_y4

        ResultData = min_max_scaler.inverse_transform(ResultData)  #back to origin data, not standard

        #calculate the MSE
        ErrorMat = TestData - ResultData  #get the error of the train data
        ErrorMat = np.square(ErrorMat)

        MSE_y1 = ErrorMat[: , 6].sum() / len(ErrorMat[: , 6])  #get the mse
        MSE_y2 = ErrorMat[: , 7].sum() / len(ErrorMat[: , 7])  #get the mse
        MSE_y3 = ErrorMat[: , 8].sum() / len(ErrorMat[: , 8])  #get the mse
        MSE_y4 = ErrorMat[: , 9].sum() / len(ErrorMat[: , 9])  #get the mse

        #get the every fold's MSE, then sum it
        score1 += MSE_y1 ; score2 += MSE_y2 ; score3 += MSE_y3 ; score4 += MSE_y4

    score1 = score1 / 10 ; score2 = score2 / 10 ; score3 = score3 / 10 ; score4 = score4 / 10 ; 
    print("The average MSE of 10 fold cross validation of y1 is: " , score1)
    print("The average MSE of 10 fold cross validation of y2 is: " , score2)
    print("The average MSE of 10 fold cross validation of y3 is: " , score3)
    print("The average MSE of 10 fold cross validation of y4 is: " , score4)


if __name__ == "__main__":
    df = GetData()
    NeutralNetwork(df)