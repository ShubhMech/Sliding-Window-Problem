arr = [1,3,2,4,5,6,4,3,2,6,7,5]
k = 3
sum_= 0
i,j = 0,0
while j < len(arr):
    print(i,j)
    if j-i < k-1:
        sum_ += arr[j]
        j += 1            
    elif j-i == k-1:
        if i != 0:
            sum_= max(sum_,sum__+arr[j]-arr[i-1])
            sum__ = arr[j]+sum__-arr[i-1]
        else:
            sum_=sum_+arr[j]
            sum__=sum_
        j += 1
        i += 1

arr = [1,3,2,4,5,6,4,3,2,6,7,5]  
