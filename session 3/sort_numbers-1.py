numbers = []
for i in range(10):
    user = float (input("enter number :"))
    numbers.append(user)

sum = 0
for i in range(len(numbers)):
    help_box = numbers[i]
    for j in range(i + 1, len(numbers)):
        if help_box > numbers[j]:
            sum += 1
            help_box = numbers[j]
            p = j

    if i != len(numbers) / 2:
        numbers[p] = numbers[i]
        numbers[i] = help_box       

if sum == 0:
    print("numbers are already sorted")

     

print(numbers)	