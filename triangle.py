a = int(input(" inter the number : "))
b = int(input(" inter the number : "))
c = int(input(" inter the number : "))
if a<=0 or b<=0 or c<=0 :
    print("the numbers are invalid")
elif a+b<c or a+c<b or b+c<a :
    print("this triangle cant be exist ")
else: 
    print(" this triangle doesnt have any problem ")   