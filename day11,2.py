number = [10,20,30,40,50]
# Left rotation
# rotated = number[1:] + number[:1]
k = 2

rotated = number[k:] + number[:k]

# Right rotation

rotated2 = number[-1:] + number[:-1]

print(rotated)

print(rotated2)