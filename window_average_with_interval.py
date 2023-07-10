import math
import random


def count_window_avg(arr,T,window,dx):
    number_of_windows=int(T/window)
    number_of_points=math.floor(window/dx)
    sum=0
    res=[]
    counter=1
    number_of_rest_points=len(arr)-(number_of_points*number_of_windows)
    for i in range(number_of_windows):
        for j in range(i*number_of_points,i*number_of_points+number_of_points-1):
            sum=sum+arr[j]
            res.append(sum/counter)
            counter=counter+1
            if(counter==window):
                sum=sum+arr[j+1]
                res.append(sum/counter)
                counter=1
                sum=0
    for i in range(len(arr)-number_of_rest_points,len(arr)):
        sum=sum+arr[i]
        res.append(sum/counter)
        counter=counter+1
    return res

def create_data(length):
    arr=[]
    for i in range(length):
        arr.append(random.randint(0,10))
    return arr

if __name__ == '__main__':
    arr=[]
    arr=create_data(10)

    # arr - dane
    # T - okres czasu [1]
    # window - okno czasowe
    # dx - częstotliwość próbkowania
    res=count_window_avg(arr,5,3,0.5)
    print(res)