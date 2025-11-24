#Q.10.WAP to check if person is eligible to marry or not (male age >=21 and female age>=18)
age=int(input("Enter Your Age:"))
gender=input("Are u Male?(y/n)")
if gender=='Y' or gender=='y':
    if age>=21:
        print("You are Eligible to Marriage")
    else:
        print("You are Small")
elif gender=='N' or gender=='n':
    if age>=18:
        print("You are Eligible to Marriage")
    else:
        print("You are Small")
else:
    print("Invalid input")

