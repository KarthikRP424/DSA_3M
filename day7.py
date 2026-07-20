# REVERSE AN ARRAY USING THE LOOP
numbers = [10,20,30,40,50]

reverse_numbers = []
for index in range(len(numbers)-1,-1,-1):
    reverse_numbers.append(numbers[index])
    
    
print(reverse_numbers)