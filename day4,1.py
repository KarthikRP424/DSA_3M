# number = [11,22,33,44]

# reverse = number[::-1]

# print("the reverse list is",reverse)


# THE CODE FOR PALINDROME

name = input("enter the name:-")


reverse = name[::-1]

if reverse == name:
    print(f"this {name} name is palindrome")
else:
    print(f"this {name} is not a palindrome")