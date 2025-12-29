from student import Student

class MedicalStudent(Student):
    def __init__(self, student_id=0, name="", age=0, percentage=0.0,
                 specialization="", marks_of_internship=0):
        super().__init__(student_id, name, age, percentage)
        self.Specialization = specialization
        self.MarksOfInternship = marks_of_internship

    def Accept(self):
        super().Accept()
        self.Specialization = input("Enter Specialization: ")
        self.MarksOfInternship = float(input("Enter Marks of Internship: "))

    def CalculateRank(self):
        avg = (self.Percentage + self.MarksOfInternship) / 2
        if avg >= 75:
            return "Outstanding Medical Student"
        elif avg >= 60:
            return "Good Medical Student"
        else:
            return "Average Medical Student"

    def Display(self):
        super().Display()
        print("Specialization:", self.Specialization)
        print("Marks of Internship:", self.MarksOfInternship)
        print("Medical Rank:", self.CalculateRank())

    def __str__(self):
        return (f"MedicalStudent({super().__str__()}, "
                f"Specialization={self.Specialization}, "
                f"MarksOfInternship={self.MarksOfInternship})")
