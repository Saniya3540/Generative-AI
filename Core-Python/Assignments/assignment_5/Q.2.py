#Q.2. Enter number of students from user. For those many students accept marks of 5 subject marks from user and calculate percentage. Display all percentage and average percentage of students.
num=int(input("Enter the number of students:"))
count=1
total_percentage=0
while num>=count:
    Sub1=float(input("Enter marks of Hindi Subject out of 100:"))
    Sub2=float(input("Enter marks of Marathi Subject out of 100:"))
    Sub3=float(input("Enter marks of English Subject out of 100:"))
    Sub4=float(input("Enter marks of Maths Subject out of 100:"))
    Sub5=float(input("Enter marks of Geography Subject out of 100:"))

    Percentage=(Sub1+Sub2+Sub3+Sub4+Sub5)/5
    print("Percentage of Student is:",Percentage)
    total_percentage+=Percentage
    count+=1

avg=total_percentage/num
print("Average percentage of students is:",avg)