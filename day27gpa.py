# genarating all the pair of an array

a = [1,2,3,4]

for i in range(len(a)):
    for j in range(i+1, len(a)):
        print(a[i], a[j])   
