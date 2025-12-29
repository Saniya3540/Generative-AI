from student import Student

class EnggStudent(Student):
    def __init__(self, student_id=0, name="", age=0, percentage=0.0,
                 branch="", internal_marks=0):
        super().__init__(student_id, name, age, percentage)
        self.Branch = branch
        self.InternalMarks = internal_marks

    def Accept(self):
        super().Accept()
        self.Branch = input("Enter Branch: ")
        self.InternalMarks = int(input("Enter Internal Marks: "))

    def CalculateRank(self):
        avg = (self.Percentage + self.InternalMarks) / 2
        if avg >= 75:
            return "Excellent Engineer"
        elif avg >= 60:
            return "Good Engineer"
        else:
            return "Average Engineer"

    def Display(self):
        super().Display()
        print("Branch:", self.Branch)
        print("Internal Marks:", self.InternalMarks)
        print("Engineering Rank:", self.CalculateRank())

    def __str__(self):
        return (f"EnggStudent({super().__str__()}, "
                f"Branch={self.Branch}, "
                f"InternalMarks={self.InternalMarks})")

