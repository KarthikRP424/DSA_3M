arr = [10,20,30,920,10]

left = 0
right = len(arr)-1

is_palindrome = True

while left < right:
  if arr[left] != arr[right]:
    is_palindrome = False
    break

  left +=1
  right -=1

if is_palindrome:
  print("the number is palindrome")
else:
  print("the number is not a palindrome")