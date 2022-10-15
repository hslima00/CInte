# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 14:41:02 2022

@author: Resende
"""

#this function takes an input the name of a file and remove outliers, interpolates the missing, 
#normalizes and predicts outputs 

import datetime
from sklearn.model_selection import train_test_split
import pandas as pd
import joblib
import numpy as np
from funcs import * 
from sklearn.metrics import precision_score, recall_score, confusion_matrix, f1_score
def TestMe(file):
    
    #load the max and min array to normalize data 
    min_array = np.loadtxt("min.txt")
    max_array = np.loadtxt("max.txt")
    
    
    #load model 
    model = joblib.load("model.sav")
                    
    prof_test = pd.read_csv(file, sep=",", decimal=".")
    prof_test=parse_date_time(prof_test)
    
    prof_test = drop_outliners(prof_test, threshold=6,
                         collumn_to_remove_outliers=
                         ["S1Temp", "S2Temp","S3Temp",
                          "CO2","PIR1", "PIR2","S1Light",
                           "S2Light","S3Light"])

    
    prof_test = prof_test.interpolate(method='linear', limit_direction='forward', axis=0)
    
    y_prof = prof_test['Persons']
    x_prof = prof_test.drop(['Persons'], axis=1)
    x_prof = x_prof.drop(['DateTime'], axis=1)
    
    x_prof = normalize_test_set(x_prof, min_array, max_array)
    
    y_pred_prof = model.predict(x_prof)
    
    c_matrix = confusion_matrix(y_prof, y_pred_prof)
    
    print("\n")
    print("Here's the confunsion matrix obtained")
    print(c_matrix)
    print("\n")
    print("Macro-Precision:  ",precision_score(y_prof, y_pred_prof, average='macro')*100, "")
    print("Macro-Recall:     ",recall_score(y_prof, y_pred_prof, average='macro')*100, "")
    print("Macro-F1:         ", f1_score(y_prof, y_pred_prof, average='macro')*100, "")
    print("\n")
    
    for i in range(4):
        print("Precision (",i,"persons):  ", c_matrix[i][i] / np.sum(c_matrix[i]) * 100,"%")
    
    print("\n")
    
    for i in range(4):
        aux = 0
        for j in range(4):
            aux += c_matrix[j][i]
            
        print("Recall (",i,"persons):  ", c_matrix[i][i] / aux *100,"%")
        aux = 0
    


