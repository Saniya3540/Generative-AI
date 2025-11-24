#8. Write a program to convert days into years,weeks and days.
num=int(input("Enter the days:"))
yr=num//365
week=(num%365)//7
days=(num%365)%7
print ( yr, "years",week,"weeks",days,"days")