def equilibrium_index(arr):
    total = sum(arr)
    leftsum = 0

    for i in range(len(arr)):
        rightsum = total - leftsum - arr[i]

        if leftsum == rightsum:
            return i

        leftsum = leftsum + arr[i]

    return -1

print(equilibrium_index([1,3,5,2,2]))