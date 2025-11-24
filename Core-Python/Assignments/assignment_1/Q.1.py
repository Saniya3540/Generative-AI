#1. Write a program to calculate the percentage of student based on marks of any 5 subjects.
Maths=int(input("Enter the marks of maths subject out of 100:"))
Science=int(input("Enter the marks of science subject out of 100:"))
History=int(input("Enter the marks of history subject out of 100:"))
Hindi=int(input("Enter the marks of hindi subject out of 100:"))
Marathi=int(input("Enter the marks of marathi subject out of 100:"))
Total= Maths+Science+History+Hindi+Marathi
Percentage= (Total/500)*100
print("The percentage of student is:",Percentage)