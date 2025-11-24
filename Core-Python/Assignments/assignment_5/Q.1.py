#Q.1. Write a program to prompt user to enter userid and password. If Id and password is incorrect give him chance to re-enter the credentials. Let him try 3 times. After that program to terminate.
count=1
while count<=3:
    username=input("Enter Userid:")
    password=input("Enter Password:")
    if username=="Saniya" and password=="sanu1234":
        print("Login Successfully!")
        break
    else:
        print("Please correct username and password.")
        count+=1
else:
    print("Too many attempts! Terminate")