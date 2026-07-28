import sys

sys.setrecursionlimit(2000)

i = 0

def greet():
    global i
    i += 1

    print("Hello Ram", i)

    if i == 10:
        return

    greet()


greet()