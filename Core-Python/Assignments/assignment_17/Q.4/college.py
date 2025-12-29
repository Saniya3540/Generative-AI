class College:
    def __init__(self, max_students):
        self.students = []  
        self.max_students = max_students

    def AddStudent(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            print(f"Student {student.Name} added.")
        else:
            print("College is full. Cannot add more students.")

    def GetStudent(self, student_id):
        for s in self.students:
            if s.StudentId == student_id:
                return s
        print("Student not found.")
        return None

    def RemoveStudent(self, student_id):
        for s in self.students:
            if s.StudentId == student_id:
                self.students.remove(s)
                print(f"Student {s.Name} removed.")
                return
        print("Student not found.")

    def __str__(self):
        if not self.students:
            return "No students in the college."
        result = ""
        for s in self.students:
            result += str(s) + "\n"
        return result
