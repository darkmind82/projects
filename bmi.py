height = float (input ( "enter height: "))
weight = float (input ( "enter weight: "))
bmi = weight/height**2
if bmi <18.5 :
    print("underweight")
elif 18.5<= bmi <=24.9 :
    print("normal weight")
elif 25<= bmi<=29.9 :
    print("overweight")
elif 30<=bmi<=34.9 :
    print ("obestry")
elif 35<=bmi<=39.9 :
    print ("extrathi obestry")



