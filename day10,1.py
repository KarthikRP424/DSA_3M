# using function 
def counting(number):
    
    frequency = {}
    
    for numbers in number:
        if numbers in frequency:
            frequency[numbers] +=1
        else:
            frequency[numbers] = 1
    
    return frequency


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

result = counting(numbers)

print("Frequency:", result)