# reverse an array 

def reverse_array(arr):
    n = 0
    
    for i in arr:
        n = n+1
        
    i = 0
    j = n-1
    
    while(i<j):
        arr[i] = arr[i]+arr[j]
        arr[j] = arr[i]-arr[j]
        arr[i] = arr[i]-arr[j]
        i = i+1
        j = j-1

    return arr

print(reverse_array([1,2,3,4,5,6,7,8,9]))