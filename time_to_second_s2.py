time = input ( "enter (h:m:s) form of time : ")

seconds = sum(int(x) * 60 ** i for i, x in enumerate (reversed (time.split(':'))))
print(seconds,"seconds")