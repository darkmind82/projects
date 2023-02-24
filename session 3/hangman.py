import random
words_bank = ["victory","woman","life","freedom","black","fastfood","love","nature","cofee","friend","computer","artificial intelligence"]
user_mistakes = 0

correct_chars = []
wrong_chars =[]

word = random.choice(words_bank)

while user_mistakes < 6 :
    sum = 0
    for i in range(len(word)) :
        if word[i] in correct_chars:
            print(word[i],end ="")
            sum += 1
        else:
            print("_",end=" ")
        
    if sum == len(word):
        print ("  you win ")
        break
    user_char = input("       please write your guess: ")
    if len(user_char) == 1:
        if user_char in word:
            print("correct")
            correct_chars.append(user_char)
        else:
            user_mistakes += 1
            print("wrong")
            wrong_chars.append(user_char)
    else:
        print("enter just one charector :| ")
if user_mistakes == 6 :
    print("game over x_x")
    
     