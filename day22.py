# implementing the prefix sum array


def prefix_sum(a):
    sum = 0
    for i in range(len(a)):
        sum = sum + a[i]
    return sum

print(prefix_sum([10,20,30,40]))

# leetcode problem 1480

class Solution(object):
    def runningSum(self, nums):
       pre = [0 for i in range(len(nums))]
       sum = 0
       for i in range(len(nums)):
        sum = sum + nums[i]
        pre[i] = sum
       return pre