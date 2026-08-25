#creating an empty array

n = 10

a = [0]*n

print(a)




# to find the length of the arr

def length_of_array(arr):
    count = 0
    for i in arr:
        count= count + 1
    return count

print(length_of_array([1,2,3,4,5,6,7,8,9]))

# access the elements using index value

# a = [1,2,3,4,89]
# n = 0
# for i in a:
#     n = n + 1
    
# for i in range(n):
#     print(a[i])