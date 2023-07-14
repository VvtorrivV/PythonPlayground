
def count_moving_avg(T, window, dx, arr):
    sum=0
    avg=[]
    number_of_points=window*dx
    i=0
    for j in range(T):
        if(i<3):
            sum=sum+arr[i]
            avg.append(sum/(i+1))
            i=i+1
        if(i>=3 and i<len(arr)):
            sum=sum+arr[i]-arr[i-3]
            avg.append(sum/number_of_points)
            i=i+1
    print(avg)
    return 0

if __name__ == '__main__':
    arr=[1,2,3,5,1,1,2,4,5,2]
    count_moving_avg(12,3,0.5,arr)