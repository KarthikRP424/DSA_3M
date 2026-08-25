# linear search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i]==target:
            print("Element found at index:",i)
        else:
            print("Element not found at index:",i)
print(linear_search([1,2,3,4,5,6,7,8,9], 5))