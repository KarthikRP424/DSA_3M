# Find the second largest number in an array

num = [12,33,48,40,55]

largest = float("-inf")

second_largest = ("-inf")

for number in num:
    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest and number != largest:
        second_largest = number
        
print(f"the largest number is {largest}")
print(f"the second largest array is {second_largest}")