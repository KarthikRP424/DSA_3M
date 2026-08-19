# Without using max():

# Find the largest number
# Find the smallest number
# Find the sum of all numbers
# Find the average

numbers = [15, 42, 8, 27, 35]

largest = numbers[0]
smallest = numbers[0]
total = 0

for num in numbers:
    if num > largest:
        largest = num
    elif num < smallest:
        smallest = num
        
    total +=num
    
    average = total / len(numbers)

        
        
        
print(smallest)
print(largest)
print(total)
print(average)