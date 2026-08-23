# patter using spacing

n = 5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ", end="")
#     for j in range(i+1):
#         print("*", end="")
#     print()
    

for i in range(1,n+1,1):
    for j in range(1,n-n+i+1,1):
        print(" ", end="")
    for j in range(1,(n-i)+1+1,1):
        print("*", end="")
    print()