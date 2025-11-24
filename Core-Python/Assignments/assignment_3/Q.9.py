#Q.9.Input 5 subject marks from user and display grade(eg.First class,Second class ..)
Sub1=float(input("Enter Hindi subject marks out of 100:"))
Sub2=float(input("Enter Marathi subject marks out of 100:"))
Sub3=float(input("Enter Math subject marks out of 100:"))
Sub4=float(input("Enter Science subject marks out of 100:"))
Sub5=float(input("Enter History subject marks out of 100:"))
Percentage=((Sub1+Sub2+Sub3+Sub4+Sub5)/5)
if Percentage>=80:
    print("First Class!")
elif Percentage>=60:
    print("Second Class")
elif Percentage>=40:
    print("Third Class")
elif Percentage<40:
    print("You are failed")
else:
    print("Invalid Input")
