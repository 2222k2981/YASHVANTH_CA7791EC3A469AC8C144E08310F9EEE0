class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  # Sort the list of student objects based on CGPA in descending order
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  return sorted_students


# Test the function with a list of student objects
students = [
    Student("Dhaanush", "A123", 9.8),
    Student("Chandhru", "A124", 8.9),
    Student("Karthi", "A125", 9.2),
    Student("Krithish", "A126", 7.8),
]

sorted_students = sort_students(students)

# Display the sorted list of students
for student in sorted_students:
  print(
      f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}"
  )
