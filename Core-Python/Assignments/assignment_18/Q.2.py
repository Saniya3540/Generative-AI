#2. Create a class Distance with data members as km,m and cm and add following methods :
#a. Constructor
#b. Destructor
#c. Overload +,- operator

class Distance:
    def __init__(self,km=0,m=0,cm=0):
        if km==0 and m==0 and cm==0:
            self.km=int(input("Enter distance in Km:"))
            self.m=int(input("Enter distance in m:"))
            self.cm=int(input("Enter distance in cm:"))
            print("------------------------------")
        else:
            self.km=km
            self.m=m
            self.cm=cm
            print("------------------------------")

    def __str__(self):
        return f"{self.km} km {self.m} m {self.cm} cm "
    
    def __add__(self,other):
        result=Distance(0,0,0)
        result.cm=self.cm+other.cm
        carry_m=result.cm//100
        result.cm=result.cm%100

        result.m=carry_m+self.m+other.m
        carry_km=result.m//1000
        result.m=result.m%1000

        result.km=carry_km+self.km+other.km
        return result
    
    
    def __sub__(self,other):
        result=Distance(0,0,0)
        km1, m1, cm1 = self.km, self.m, self.cm
        km2, m2, cm2 = other.km, other.m, other.cm
        # Subtract cm with borrowing if needed
        if cm1 < cm2:
            m1 -= 1
            cm1 += 100
        result.cm = cm1 - cm2
        # Subtract m with borrowing if needed
        if m1 < m2:
            km1 -= 1
            m1 += 1000
        result.m = m1 - m2
        # Subtract km
        result.km = km1 - km2

        return result
    
    def __del__(self):
        print(f"Distance {self.km} km {self.m} m {self.cm} cm ")
        print("------------------------------")

d1=Distance()
print("D1:",d1)

d2=Distance(1000,3000,4500)
print("D2:",d2)

d3=Distance(300,500,400)
print("D3:",d3)

d4=d2+d3
print("D4:",d4)

d5=d4-d3
print("D5:",d5)
        
        
