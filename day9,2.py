number = [10,20,30,10,50]

seen = set()

unique_number = []

for num in number:
    if num  not in seen:
        seen.add(num)
        unique_number.append(num)
        
print(unique_number)