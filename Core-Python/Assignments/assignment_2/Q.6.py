#6. WAP to calculate total salary of employee based on basic, da=10% of basic, ta=12% of basic, hra=15% of basic.
basic=float(input("Enter the basic salary:"))
da=(basic*(10/100))
print(da,"is da")
ta=(basic*(12/100))
print(ta,"is ta")
hra=(basic*(15/100))
print(hra,"is hra")
Total_Salary= basic+da+ta+hra
print(da,"+",ta,"+",hra)
print("Total Salary of Employee is:",Total_Salary)