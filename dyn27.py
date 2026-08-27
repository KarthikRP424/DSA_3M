# the code for dynamic array

d = []

d.append(10)
d.append(20)
d.append(30)
d.append(40)
d.append(50)

print(d)

print(45 in d)

x = d.index(30) # this will return the index of 30 in the array
print("the index value of 30 is",x)

d.pop() # this will remove the last element from the array
print(d)
d.pop()
print(d)

y = d.index(20)
d.pop(y)

print(d)