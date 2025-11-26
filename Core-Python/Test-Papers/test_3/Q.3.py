# 3.write a program to accept basic salary of n emp.(n should be accepted from user).if basic salary is below 20000 then 
#   da=10%,ta=12%,and hra=15% otherwise da=15%,ta=18% and hra=20%.Based on this clculate the total salary of each emp
#   and also total salary of all emp.
emp=int(input("Enter total employee:"))
total_emp_salary=0
for i in range(emp):
   n=int(input("Enter employee salary:"))
   if n<20000:
       da=(10/100)*n
       ta=(12/100)*n
       hra=(15/100)*n
   else:
        da=(15/100)*n
        ta=(18/100)*n
        hra=(20/100)*n
   total_salary=n+da+ta+hra
   total_emp_salary+=total_salary
   print("Total Salary of Employee:",total_salary)
print("Total Salary of all employee",total_emp_salary)


