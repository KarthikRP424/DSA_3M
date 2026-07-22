array = [10,10,10,10]  

#array = [12,292,338,88,99]

largest = float("-inf")
second_largest = float('-inf')

for number in array:
    if number > largest:
        second_largest = largest
        largest = number
        
    elif number > second_largest and number != largest:
        
        second_largest = number
        
        
if second_largest == float("-inf"):
    print("there is no second largest element in this array")
    
else:
    print(f"the second largest element is {second_largest}")