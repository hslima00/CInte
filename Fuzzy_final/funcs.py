from cProfile import label
import pandas as pd
import matplotlib.pyplot as plt
from numpy import percentile
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import datetime
import matplotlib.dates as mdates
import operator


def plot_data(data_df, temperature=False, CO2=False, PIR=False, light=False, PIR_Join = False, Temp_join=False, MeanLight=False, persons=False):
    """
    Plot the temperature data from the dataframe
    :param df: dataframe
    :param title: title of the plot
    :param print: print the plot
    :return: None
    """
    if temperature:
        if Temp_join:
            # plot MeanTemp and Persons with 2 y axis and DateTime as x axis
            fig, ax1 = plt.subplots(figsize=(20, 10))
            ax1.plot(data_df.index.values, data_df['MeanTemp'], color='r', marker='.', label='MeanTemp')
            ax1.set_xlabel('DateTime')
            ax1.set_ylabel('MeanTemp', color='r')
            ax1.tick_params('y', colors='r')
            ax2 = ax1.twinx()
            ax2.plot(data_df.index.values, data_df['Persons'], color='b', marker='.', label='Persons')
            ax2.set_ylabel('Persons', color='b')
            ax2.tick_params('y', colors='b')
            fig.tight_layout()
            plt.show()
        else:
            data_df.plot(x='DateTime', y='MeanTemp',y2='Persons', figsize=(20, 10), title='Temperature')
     
            #data_df.plot(x='DateTime', y=['S1Temp','S2Temp','S3Temp'], figsize=(20, 10), title='Temperature')
        #data_df.plot(x='DateTime', y='S2Temp', figsize=(20, 10), label='Temperature from sensor 2', color='blue')
        #data_df.plot(x='DateTime', y='S3Temp', figsize=(20, 10), label='Temperature from sensor 3', color='green')
        #data_df.legend()
        #data_df.show()
    if CO2:
        # plot CO2 and Persons with 2 y axis and DateTime as x axis and a horizontal line when persons = 2
        fig, ax1 = plt.subplots(figsize=(20, 10))
        ax1.plot(data_df.index.values, data_df['CO2'], color='r', marker='.', label='CO2')
        ax1.set_xlabel('DateTime')
        ax1.set_ylabel('CO2', color='r')
        ax1.tick_params('y', colors='r')
        ax2 = ax1.twinx()
        ax2.plot(data_df.index.values, data_df['Persons'], color='b', marker='.', label='Persons')
        ax2.set_ylabel('Persons', color='b')
        ax2.tick_params('y', colors='b')
        fig.tight_layout()
        plt.show()



   

        #data_df.plot(x='DateTime', y=['CO2','Persons'], figsize=(20, 10), title='CO2 Sensor', color='red')
    if PIR:
        data_df.plot(x='DateTime', y=['PIR1','PIR2'], figsize=(20, 10), title='PIR Sensor')
        #data_df.plot(x='DateTime', y='PIR2', figsize=(20, 10), title='IR motion from sensor 2', color='blue')
    if PIR_Join:
        # plot PIR and Persons with 2 y axis and DateTime as x axis and a horizontal line when persons = 2
        fig, ax1 = plt.subplots(figsize=(20, 10))
        ax1.plot(data_df.index.values, data_df['PIR'], color='g', marker='.', label='PIR')
        ax1.set_xlabel('DateTime')
        ax1.set_ylabel('PIR', color='r')
        ax1.tick_params('y', colors='r')
        ax2 = ax1.twinx()
        ax2.plot(data_df.index.values, data_df['Persons'], color='b', marker='.', label='Persons')
        ax2.set_ylabel('Persons', color='b')
        ax2.tick_params('y', colors='b')
        fig.tight_layout()
        plt.show()

        #data_df.plot(x='DateTime', y=['PIR','Persons'], figsize=(20, 10), title='PIR Sensor', color='red')
    if light:
        if MeanLight:
            # plot MeanLigth and Persons with 2 y axis and DateTime as x axis and a horizontal line when persons = 2
            fig, ax1 = plt.subplots(figsize=(20, 10))
            ax1.plot(data_df.index.values, data_df['MeanLight'], color='g', marker='.', label='MeanLight')
            ax1.set_xlabel('DateTime')
            ax1.set_ylabel('MeanLight', color='r')
            ax1.tick_params('y', colors='r')
            ax2 = ax1.twinx()
            ax2.plot(data_df.index.values, data_df['Persons'], color='b', marker='.', label='Persons')
            ax2.set_ylabel('Persons', color='b')
            ax2.tick_params('y', colors='b')
            fig.tight_layout()
            plt.show()
            #data_df.plot(x='DateTime', y=['MeanLight','Persons'], figsize=(20, 10), title='Light')
        else:
            pass
            #data_df.plot(x='DateTime', y=['S1Light','S2Light','S3Light'], figsize=(20, 10), title='Light')
    if persons:
        data_df.plot(x='DateTime', y='Persons', figsize=(20, 10), title='Persons', color='red')
        #data_df.plot(x='DateTime', y='S2Light', figsize=(20, 10), title='Light from sensor 2', color='blue')
        #data_df.plot(x='DateTime', y='S3Light', figsize=(20, 10), title='Light from sensor 3', color='green')
    #if Temp_join:
    #    data_df.plot(x='DateTime', y='MeanTemp', figsize=(20, 10), title='Temperature', color='red')



def scatter_plot(data_df, temperature=False,C02_PIR=False,light=False, title=None):
    """
    Scatter plot of the data
    :param data_df: dataframe
    :param temperature: plot temperature
    :param C02_PIR: plot C02 and PIR
    :param light: plot light sensor data
    :return: None
    """
    if temperature:
        plt.figure(figsize=(20, 10))
        plt.subplot(311)
        plt.scatter(data_df.index.values, data_df['S1Temp'], color='r', marker='.', label='S1Temp');
        plt.subplot(312)
        plt.scatter(data_df.index.values, data_df['S2Temp'], color='b', marker='.', label='S2Temp');    #aquecedor ou algo do género (luz)
        plt.subplot(313)
        plt.scatter(data_df.index.values, data_df['S3Temp'], color='g', marker='.');
        plt.show()
    if C02_PIR:
        plt.figure(figsize=(20, 10))
        plt.subplot(311)
        plt.scatter(data_df.index.values, data_df['CO2'], color='r', marker='.');
        plt.subplot(312)
        plt.scatter(data_df.index.values, data_df['PIR1'], color='b', marker='.');
        plt.subplot(313)
        plt.scatter(data_df.index.values, data_df['PIR2'], color='g', marker='.');
        plt.show()
    if light:
        plt.figure(figsize=(20, 10))
        plt.subplot(311)
        plt.scatter(data_df.index.values, data_df['S1Light'], color='r', marker='.');
        plt.subplot(312)
        plt.scatter(data_df.index.values, data_df['S2Light'], color='b', marker='.');
        plt.subplot(313)
        plt.scatter(data_df.index.values, data_df['S3Light'], color='g', marker='.');
        plt.show()

def parse_date_time(data_df):
    """
    Parse the date and time from the dataframe
    :param data_df: dataframe
    :return: dataframe
    """
    data_df['DateTime'] = data_df['Date'].astype(str) + ' ' + data_df['Time'].astype(str)
    data_df.drop(['Date', 'Time'], axis=1, inplace=True)
    return data_df

def drop_outliners(data_df, threshold=6, 
                collumn_to_remove_outliers=["S1Temp", "S2Temp", "S3Temp",
                                            "S1Light", "S2Light", "S3Light",
                                            "CO2", "PIR1", "PIR2"]):
    """
    Drop outliners from the dataframe
    :return: dataframe
    """
    for collumn in collumn_to_remove_outliers:

        k = threshold
        std = data_df[collumn].std()
        mean = data_df[collumn].mean()

        for i, value in data_df[collumn].items():

            if (value>k*std+mean) or (value<mean-k*std):
                print("Removed outlined from index ",i+2,"from ",collumn, "with value of:", value)
                outliner_index=i
                # pop out the outlier
                data_df.drop(outliner_index, inplace=True)

    return data_df

def normalize_test_set(data_df, min_array, max_array):
    i = 0
    for collumn in data_df:

        if (collumn != "DateTime"):
            data_df[collumn] = (data_df[collumn] - min_array[i]) / (max_array[i] - min_array[i])
        i=i+1    
    return data_df

def normalize_train_set(data_df):
    """
    Normalize the data from the dataframe
    :param data_df: dataframe
    :return: dataframe
    """
    min_array = []
    max_array = []
    for collumn in data_df.columns:
        if (collumn != "DateTime") and (collumn != "Persons"):
            min = data_df[collumn].min()
            max = data_df[collumn].max()
            min_array.append(min)
            max_array.append(max)
            data_df[collumn] = (data_df[collumn] - min) / (max - min)
    return data_df, min_array, max_array
    


