# Missing number in an array

num = [1,2,4,5]

n = 5

expected_sum = n * (n+1)//2

achual_sum = sum(num) 

missing_num = expected_sum - achual_sum

print(f"my missing number is {missing_num}")