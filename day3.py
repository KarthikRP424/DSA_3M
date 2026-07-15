#Finding the Average

marks = [10,20,30,40]

total = 0

for num in marks:
    total += num
    
Average = total / len(marks)

print("the total average is",Average) 

# find the max number

numbers = [12,3,33,44,23,35]

max_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num
    
print("the maximum number is ",max_num)

# FINDING THE MINIMUM ELEMENT


numbers = [12,3,33,44,23,35]

min_num = numbers[0]

for num in numbers:
    if num < min_num:
        min_num = num
    
print("the minimum number is ",min_num)


#Find Maximum and Minimum Together

numbers = [10,20,5,66,77]

max = numbers[0]
min = numbers[0]

for number in numbers:
    if number > max:
        max = number
        
    if number < min:
        min = number
        
print("the maximum is  ",max)
print("the minimum number is ",min)
