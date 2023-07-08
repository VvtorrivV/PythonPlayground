
def count_window_avg(T,dx,window,arr):
    number_of_windows=int(T/window)
    number_of_points_in_window=int(window/dx)
    sum=0
    res=[]
    for j in range(number_of_windows):
        for i in range(j*number_of_points_in_window,j*number_of_points_in_window+number_of_points_in_window):
            sum=sum+arr[i]
            if(i==j*number_of_points_in_window+number_of_points_in_window-1):
                sum=sum/number_of_points_in_window
                res.append(sum)
                sum=0
    print(res)


if __name__ == '__main__':
    fx=[1,3,2,6,4,3,1,3,2,4,1,3,2,6,4,3,1,3,2,4]

    # T - okres czasu [s]
    # dx - częśtotliwość próbkowania [s]
    # window - okno czasowe
    count_window_avg(10,1,3,fx)

