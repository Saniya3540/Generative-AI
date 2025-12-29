class Student:
    def __init__(self, student_id=0, name="", age=0, percentage=0.0):
        self.StudentId = student_id
        self.Name = name
        self.Age = age
        self.Percentage = percentage

    def __str__(self):
        return f"{self.StudentId}, {self.Name}, {self.Age}, {self.Percentage}"
