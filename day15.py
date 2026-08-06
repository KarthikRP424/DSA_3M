arr = [10,29,40,50,70]

largest = arr[0]

for num in arr:
    if num > largest:
        largest = num
        
print(f"the largest number is {largest}")