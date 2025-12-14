#1. Create a class Complex Number with data members as real and imag and add following methods :
#a. Constructor
#b. Destructor
#c. Overload +,- operator

class Complex_Num:
    def __init__(self,real=0,imag=0):
        if real==0 and imag==0:
            self.real=int(input("Enter Real Number:"))
            self.imag=int(input("Enter Imaginary number:"))
        else:
            self.real=real
            self.imag=imag

    #def __del__(self):
     #   print("Complex Number {self.real}+{self.imag}i is destroyed!")

    def __str__(self):
        data=str(self.real)+"+"+str(self.imag)+"i"
        return data
    
    def __add__(self,other):
        return Complex_Num(self.real+other.real,self.imag+other.imag)
    
    def __sub__(self,other):
        return Complex_Num(self.real-other.real,self.imag-other.imag)
    

    def __del__(self):
        print(f"Complex Number {self.real}+{self.imag}i is destroyed!")

c1=Complex_Num()
print("C1:",c1)

c2=Complex_Num(2,3)
print("C2:",c2)

c3=Complex_Num(6,9)
print("C3:",c3)

c4=c2+c3
print("C4:",c4)

c5=c4-c2
print("c5:",c5)