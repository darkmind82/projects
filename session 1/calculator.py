import math
a = int (input("enter number1 :"))
b = int(input("enter number2 :"))
print("this program can do mathematical exercises such as:\n + \n -\n *\n / \n radical \n factorial \n sin \n cos \n tan \n cot")
list_1= input("what do you want from program?")
if list_1 == "+":
    print(a+b)
elif list_1 == "-":
    print(a-b)
elif list_1 == "*":
    print(a*b)
elif list_1 == "/":
    print (a/b)
elif list_1 == "radical":
    print(math.sqrt(a))
    print(math.sqrt(b))
elif list_1 == "factorial":
    fact=1  
    for i in range(1, a+1):
        fact = fact * i
    print(fact)

    fact = 1
    for i in range(1, b+1):
        fact = fact * i
    print(fact)
elif list_1 == "sin" :
    print("a :",math.sin(math.radians(a)))
    print(math.sin(math.radians(b)))

elif list_1 == "cos" :
    print(math.cos(math.radians(a)))
    print(math.cos(math.radians(b)))
elif list_1 == "tan":
    print(math.tan(math.radians(a)))
    print(math.tan(math.radians(b)))
elif list_1 == "cot":
    print(math.cos(math.radians(a)) / math.sin(math.radians(a)))
    print(math.sin(math.radians(b)) /math.cos(math.radians(b)))
   










