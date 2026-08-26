# code for prefix sum of array

a = [1,2,3,4,5]
n = 5
psum = [0]*n

psum[0] = a[0]

for i in range(1,n):
    psum[i] = psum[i-1]+a[i]
    
print(psum)

print("the total sum of array is",psum[n-1])