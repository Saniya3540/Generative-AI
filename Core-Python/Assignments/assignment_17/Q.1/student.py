class Student:
    def __init__(self, student_id=0, name="", age=0, percentage=0.0):
        self.StudentId = student_id
        self.Name = name
        self.Age = age
        self.Percentage = percentage

    def Accept(self):
        self.StudentId = int(input("Enter Student ID: "))
        self.Name = input("Enter Name: ")
        self.Age = int(input("Enter Age: "))
        self.Percentage = float(input("Enter Percentage: "))

    def CalculateRank(self):
        if self.Percentage >= 75:
            return "Distinction"
        elif self.Percentage >= 60:
            return "First Class"
        elif self.Percentage >= 50:
            return "Second Class"
        else:
            return "Fail"

    def Display(self):
        print("Student ID:", self.StudentId)
        print("Name:", self.Name)
        print("Age:", self.Age)
        print("Percentage:", self.Percentage)
        print("Rank:", self.CalculateRank())

    def __str__(self):
        return f"StudentId={self.StudentId}, Name={self.Name}, Age={self.Age}, Percentage={self.Percentage}"

s1 = Student()
s1.Accept()
s1.Display()
print(s1)

s2=Student(102,"Saniya",21,90)
s2.Display()
print(s2)