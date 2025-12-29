from student import Student
from college import College

college = College(3)

s1 = Student(101, "Alice", 20, 85)
college.AddStudent(s1)

s2 = Student(102, "Bob", 22, 78)
college.AddStudent(s2)

print("All students in college:")
print(college)

student = college.GetStudent(101)
if student:
    print("\nDetails of student ID 101:")
    print(student)

college.RemoveStudent(102)

print("\nAfter removal:")
print(college)
