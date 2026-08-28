def two_sum(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] +arr[j]==target:
                return[i,j]
            
    return []

print(two_sum([2,7,12,99], 9))