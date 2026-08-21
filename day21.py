# axis the element of the list using loop 

a = [10, 22, 450, 78]

# for i in a:
#     print(i)

# using the index of the list 

# for i in range(len(a)):
#     print(a[i])
    
# creating an array in python 
a = [10, 22, 450, 78]
psum = [0 for i in range(len(a))]

print(psum)

print(a)
sum = 0
for i in a:
    
    sum = sum +i
    print(sum,end = " ")
    