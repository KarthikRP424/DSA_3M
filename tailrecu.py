count = 0

def func():
    
    global count
    
    if count == 4:
        return
    
    count +=1
    
    func()
    
    print("Hey i am karthik")
    
func()


# recursiom using parameters


def func(x, n):
    
    if n == 0:
        return 
    
    print(x)
    func(x, n-1)
    
func(3,4)
    
    
    