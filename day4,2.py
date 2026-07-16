# THE SECOND LARGEST ELEMENT

list = [22,1,5,88,7]

largest = 0
second_largest = 0

for number in list:
    if number > largest:
        second_largest = largest
        largest = number
        
    elif number > second_largest and number != largest:
        second_largest = number
        
        
print("the largest element is ",largest)
print("the second largest element is ", second_largest)