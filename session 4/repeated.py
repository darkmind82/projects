numbers = []
result = []
len_numbers = int (input("how many numbers whold you like to have in your list? :"))
for i in range(len_numbers):
    user = int(input("enter number :"))
    numbers.append(user)
print (numbers)

for number in numbers :
    if number not in result :
        result.append(number)

print(result)
    


