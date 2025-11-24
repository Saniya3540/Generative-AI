#Q.3. A farmer has a field which is half in circle shape and rest rectangle. He needs to do fencing for entire field using barbed wire 5 times. Circular section has radius 20 m and rectangle length is 50 m and breadth is 40 m. If cost of barbed wire is 35 Rs/m then calculate the total cost of fencing the field.
l=50
b=40
r=20
cost_per_m=35

perimeter_of_rect=(2*b)+l
perimeter_of_circle=3.14*r
sum=perimeter_of_rect+perimeter_of_circle
print("Sum of Perimeter:",sum)
total_wire=5*sum
print("Total Wire:",total_wire)
total_cost=total_wire*cost_per_m
print("Total Cost:",total_cost)
