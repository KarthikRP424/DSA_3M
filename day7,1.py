#REVERSE AN ARRAY USING THE POINTER 

element = [11,22,33,44,55]

left = 0
right = len(element)-1

while left<right:
    
    element[left] , element[right] = element[right] , element[left]
    
    left +=1
    right -=1
print(element)
