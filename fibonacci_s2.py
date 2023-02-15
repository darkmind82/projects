print ("how many numbers of the fibonacci sequence should be printed")
N = int (input("enter the number :"))
n1=1
n2=1
print (n1,end="  ")
print(n2,end="  ")
fibonacci=0
for i in range(1,N-1):
    print(n1+n2,end="  ")
    fibonacci=n2
    n2=n1+n2
    n1=fibonacci 
print("\n")   

