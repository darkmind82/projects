#import math
#a = int (input("enter the first number :"))
#b = int (input("enter the second number :"))
#print("kmm :" , math.icm(a,b))

first = int (input("enter first number :"))
    
second = int (input("enter second number :"))


def lcm(a, b):
   if a > b:
       kmm = a
   else:
       kmm = b

   while(True):

       if(kmm % a == 0) and (kmm % b == 0):
           break
       kmm += 1

   return kmm


    
print("kmm: ", lcm(first,second))