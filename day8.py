# Second largest element in an array 

# method 1

number = [11,12,13,14,15,11]

unique_number = list(set(number))

unique_number.sort()

print("the second largest element in an array is:",unique_number[-2])