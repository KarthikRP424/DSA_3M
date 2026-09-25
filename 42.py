# find largest row sum 

def largest_sum(arr):

  n = len(arr)

  largest = 0 

  for i in range(n):
      sum = 0
      for value in arr[i]:
        sum = sum + value
      if sum > largest:
        largest = sum

  return largest


print(largest_sum([[1,2,3],[4,5,6],[7,8,9]]))