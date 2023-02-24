count = 0
sum = 0
while True:
    score = input("enter student's score :")
    if score == "exit":
        break
    score =float(score)
    sum = sum + score 
    count = count +1
ave=sum/count
print(ave)




