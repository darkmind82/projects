import random 

numbers = []
length = int(input("enter the number of numbers: "))
for i in range (length):
    rand = random.randint(-100,100)
    numbers.append(rand)
print (numbers)
