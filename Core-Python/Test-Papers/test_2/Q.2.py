#Q.2.Write a program to accept 3 digit number.If first digit is double of second digit and half of third digit then display "Yes,you have done it",otherwise display "Please try next time".
num=int(input("Enter digit number:"))
n1=num//100
n2=(num//10) %10
n3=num%10
if n1==2*n2 and n1==n3/2:
    print("Yes,you have done it.")
else:
    print("Please try next time.")