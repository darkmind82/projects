import random
print ("welcome to <<rock,paper,scissors>> game")
name = input ("enter your name :")
round = int(input ("how many rounds would you like to play ? "))
computer_score =0
user_score = 0
for i in range (round) :
    number = random.randint(1,3)
    if number == 1 : 
        computer_choice = "rock"
    elif number == 2:
        computer_choice = "paper"
    elif number == 3:
        computer_choice = "scissors"

    user_choice =input("enter your choice :")

    print("computer:",computer_choice)
    print(name,":",user_choice)
    if computer_choice =="rock" and user_choice == "paper" or computer_choice == "paper" and user_choice == "scissors" or computer_choice == "scissors" and user_choice == "rock" :
        user_score = user_score + 1 
    elif computer_choice == "rock"and user_choice == "scissors" or computer_choice == "paper" and user_choice == "rock" or computer_choice == "scissors" and user_choice == "paper" :
        computer_score = computer_score + 1
    elif computer_choice == user_choice :
        print("your choices are the same , score = 0 for both player")

print( "computer score:", computer_score)
print(name,"score:", user_score)

if computer_score > user_score :
    print ( "you lose :( ")
elif user_score > computer_score :
    print ( "you win :) ")


