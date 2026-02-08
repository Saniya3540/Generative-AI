from SY.symarks import SYMarks
from TY.tymarks import TYMarks


class Student:
    def __init__(self, roll_no, name, sy_marks, ty_marks):
        self.roll_no = roll_no
        self.name = name
        self.sy = sy_marks          
        self.ty = ty_marks         

    def display_result(self):
        total = self.sy.ComputerTotal + self.ty.theory + self.ty.practical
        percentage = total / 3

        if percentage >= 70:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        elif percentage >= 40:
            grade = "Pass Class"
        else:
            grade = "Fail"

        print("Roll No :", self.roll_no)
        print("Name    :", self.name)
        print("SY Computer Marks :", self.sy.ComputerTotal)
        print("TY Theory Marks  :", self.ty.theory)
        print("TY Practical Marks :", self.ty.practical)
        print("Percentage :", percentage)
        print("Grade :", grade)


sy = SYMarks(72, 65, 70)
ty = TYMarks(68, 75)

student = Student(101, "Saniya", sy, ty)
student.display_result()
