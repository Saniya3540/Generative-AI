#Q.4.
interior_area = float(input("Enter interior wall area: "))
interior_rate = float(input("Enter cost per unit for interior paint: "))

exterior_area = float(input("Enter exterior wall area: "))
exterior_rate = float(input("Enter cost per unit for exterior paint: "))

interior_cost = interior_area * interior_rate
exterior_cost = exterior_area * exterior_rate
total_cost = interior_cost + exterior_cost

print("Interior painting cost:", interior_cost)
print("Exterior painting cost:", exterior_cost)
print("Total painting cost:", total_cost)
