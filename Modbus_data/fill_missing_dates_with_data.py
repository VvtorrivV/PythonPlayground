import datetime
import random
import time

import pandas as pd


def txt_to_df(filepath):
    data=pd.read_csv(filepath, sep=",")
    return data

def prepare_data(df):
    df['seconds'] = pd.DatetimeIndex(df['date']).second
    seconds = df['seconds'].values
    val = df['data'].values
    return seconds, val

if __name__ == '__main__':
    df=txt_to_df(r'E:\KlepanieKodu\Modbus_data\test.txt')
    x=[]
    y=[]
    seconds,val=prepare_data(df)
    arr=[]
    j=0
    arr.append(seconds[0])
    for i in range(1,len(seconds)):
        if (seconds[i] < seconds[i-1]):
            j = j + 1
        arr.append(60*j+seconds[i])
    y.append(val[0])
    for i in range(1,len(arr)):
        if(arr[i]!=arr[i-1]+1):
            y.append(val[i-1])
        y.append(val[i])
    for i in range(len(y)):
        x.append(i)
    print(x)
    print(y)


