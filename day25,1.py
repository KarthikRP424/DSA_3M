# to move the elements in another empty array
n = 10

a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

b = [0]*n

for i in range(n):
    b[i]=a[i]

print(a)
print(b)