element = [0,1,2,0,4,9,0]

result = []
count_zero = 0

for number in element:
    if number == 0:
        count_zero +=1
    else:
        result.append(number)
        
for _ in range(count_zero):
    result.append(0)
    
print(result)