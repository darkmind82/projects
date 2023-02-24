import random
computer_number = random.randint(10,40)
print("wellcome to <<guess the number>> game ,enter your guess :")
guess_times = 0
for i in range(1,11):
    user_number =int (input())
    guess_times =+ i
    
    if computer_number == user_number:
        print ("well done *")
        print ("you win")
        break
    elif computer_number > user_number:
        print("x")
        print("go up") 
    elif computer_number < user_number:
        print("x")
        print("go down ")

print( "guess times :", guess_times)
