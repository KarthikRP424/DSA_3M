# the program to create the frequency hashmap

a = [1,2,3,4,5,6,7,8,9,1,2,3,4,5]

h = {}

for i in a:
    if(i in h.keys()):
        count = h[i]
        count +=1
        h[i] = count
    else:
        h[i] = 1
print(h)