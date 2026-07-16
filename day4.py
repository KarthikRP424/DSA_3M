def liner(nums,item):
    for index in range(len(nums)):
        if nums[index] == item:
            print(f"the item is found  index {index}")
            return index
        
    print("the item is not found")
    return -1
    
    
result = liner([10,20,30,40],30)

print(f"the result is {result}")