def column_sum1(arr):
    
    rows = len(arr)
    column = len(arr[0])
    
    for j in range(rows):
        column_sum = 0
        
        for i in range(column):
            column_sum = column_sum + arr[i][j]
    return column_sum       
            

print(column_sum1([[1,2,3],[3,2,1],[1,9,10]]))
