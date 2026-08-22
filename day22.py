# implementing the prefix sum array


def prefix_sum(a):
    sum = 0
    for i in range(len(a)):
        sum = sum + a[i]
    return sum

print(prefix_sum([10,20,30,40]))