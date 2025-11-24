#Q.1.Write a program to accept year from user and check if it is a leap year or not.
yr=int(input("Enter Year:"))
if yr%4==0:
    if yr%100==0:
        if yr%400==0:
            print("Leap Year!")
        else:
            print("Not a Leap Year.")
    else:
        print("Leap Year!")  
else:
    print("Not a Leap Year") 