def seacrchele(arr,target):
    
    found = False
    
    for row in arr:
        
        for value in row:
            
            if value == target:
                found = True
                break
            
    return found

print(seacrchele([[1,2,3],[3,2,1],[1,9,10]], 9))