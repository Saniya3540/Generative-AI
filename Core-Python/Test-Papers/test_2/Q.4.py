#Q.4. Write a program to calculate the total cost of painting. The interior of building with four equal sized walls.
height=float(input("Enter height:"))
width=float(input("Enter width:"))
rate=float(input("Enter rate:"))
total_area=4*height*width
print("Total area is:",total_area)
total_cost=total_area*rate
print("Total Cost is:",total_cost)