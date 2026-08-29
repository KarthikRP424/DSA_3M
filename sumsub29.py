# sum of sub array

a = [1,2,3,4,5,6]

for i in range(len(a)):
    for j in range(i, len(a)):
        print(sum(a[i:j+1]))