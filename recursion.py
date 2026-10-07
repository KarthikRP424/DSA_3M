# def greet():
    
#     print("Hello I am Karthik and i am AI engineer")
#     # greet()  infinite recursion
    
    
# greet()


def greet(count):
    
    if count == 4:
        return
    
    print("Hello I am Karthik and i am AI engineer")
    count += 1
    greet(count)

greet(0)


count = 0

def greet():
    global count

    if count == 4:
        return

    print("Hello I am Karthik and I am AI engineer")
    count += 1
    greet()

greet()