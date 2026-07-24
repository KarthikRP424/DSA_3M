#Missing number in an array more than 10 like 10 , 20,30 like this 


num = [10,20,40,60]

difference = 10

for index in range(len(num)-1):
    expected_num = num[index]+difference
    
    if expected_num != num[index+1]:
        print("The missing number is ",expected_num)