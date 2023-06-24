import random

import pandas as pd
import matplotlib.pyplot as plt

def count_avg(T, number_points, f_podst, t_zad):
    avg=[]
    df=[]
    suma=0
    length=int(T/t_zad)
    for i in range(number_points):
        df.append(random.randint(0,100))
    #print(length)
    for j in range(length):
        for i in range(j*t_zad,j*t_zad+t_zad):
            suma=suma+df[i]
            if(i==j*t_zad+t_zad-1):
                #print(suma)
                avg.append(suma/t_zad)
                suma=0
                print(str(j)+": "+str(avg[j]))
    return avg

if __name__ == '__main__':
    #count_avg takes 4 parameters:
    #T - period of time
    #number_points - number of samples over a period of time
    #f_podst - frequency base
    #t_zad - averaging window time/number of time windows to be counted
    count_avg(720,720,10,6)

