#Q.8.WAP to prompt user to enter userid and password.After verifying userid and password display a 4 digit random number and ask user to enter the same. If user enters the same number then show him success message otherwise failed. (Something like captcha)
import random
username=input("Enter the Username:")
password=input("Enter the Password:")
if username=="Saniya" and password=="san6061":
    print("Correct Username and Password!")
    x=random.randint(1000,9999)
    print("Your 4 digit number is:",x)
    user_input=int(input("ENetr 4 digit number:"))
    if x==user_input:
        print("Success!")
    else:
        print("Failed!")
else:
    print("Incorrect Username or Password!")

