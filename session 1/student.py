name = input ( " enter the first name  and last name of student: ")
a = float (input ( "enter first score : "))
b = float (input ( "enter the second score : "))
c = float (input ( "enter the third score : "))
ave = (a + b + c)/3 
if ave<12:
    print("fail")
elif  12<=ave<17: 
    print( "normal") 
elif  ave>=17:
    print( "excellent")
    