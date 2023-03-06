
number = int (input("enter the number :"))

for i in range(1,number) :
    sum = 1
    for j in range(1,i) :
        sum = sum*j
    if sum == number :
        print("yes")
        break
    elif sum > number :
        print("no")
        break
    
        
