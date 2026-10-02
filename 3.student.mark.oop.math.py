import math
import numpy as np


class Student:

  def __init__(self, student_id, name, dob):
    self.id = student_id
    self.name = name
    self.dob = dob


class Course:

  def __init__(self, course_id, name, credits):
    self.id = course_id
    self.name = name
    self.credits = credits



def floor_to_one_decimal(val):
  
  return math.floor(val * 10) / 10.0


def input_students(students):
  try:
    count = int(input("Number of students: "))
    for i in range(count):
      print(f"\n--- Student {i + 1} ---")
      s_id = input("Student ID: ").strip()
      s_name = input("Student name: ").strip()
      s_dob = input("Student DoB (DD/MM/YYYY): ").strip()
      students.append(Student(s_id, s_name, s_dob))
    print(f"\nSuccessfully added {count} student(s).")
  except ValueError:
    print("Invalid input! Please enter a valid integer.")


def input_courses(courses):
  try:
    count = int(input("Number of courses: "))
    for i in range(count):
      print(f"\n--- Course {i + 1} ---")
      c_id = input("Course ID: ").strip()
      c_name = input("Course name: ").strip()
      credits = int(input("Course credits: "))
      courses.append(Course(c_id, c_name, credits))
    print(f"\nSuccessfully added {count} course(s).")
  except ValueError:
    print("Invalid input! Please enter valid numeric values.")


def input_marks(students, courses, marks):
  if not courses:
    print("Error: No courses available. Please input courses first.")
    return
  if not students:
    print("Error: No students available. Please input students first.")
    return

  c_id = input("Enter Course ID to input marks: ").strip()
  course_exists = any(c.id == c_id for c in courses)

  if not course_exists:
    print(f"Error: Course ID '{c_id}' not found.")
    return

  print(f"\nEntering Marks for Course {c_id}")
  for student in students:
    try:
      score = float(input(f"Mark for {student.name} (ID: {student.id}): "))
      floored_score = floor_to_one_decimal(score)
      marks[(c_id, student.id)] = floored_score
    except ValueError:
      print("Invalid score entered. Skipping student.")


def calculate_gpa(student_id, courses, marks):
  student_marks = []
  student_credits = []

  for course in courses:
    key = (course.id, student_id)
    if key in marks:
      student_marks.append(marks[key])
      student_credits.append(course.credits)

  if not student_credits:
    return 0.0

  np_marks = np.array(student_marks)
  np_credits = np.array(student_credits)

  return np.average(np_marks, weights=np_credits)


def list_students_sorted_by_gpa(students, courses, marks):
  if not students:
    print("No students available.")
    return

  gpas = np.array([calculate_gpa(s.id, courses, marks) for s in students])

  sorted_indices = np.argsort(gpas)[::-1]

  print("\n=== Students List (Sorted by GPA Descending) ===")
  print(f"{'ID':<10} | {'Name':<20} | {'DoB':<12} | {'GPA':<6}")
  print("-" * 56)

  for idx in sorted_indices:
    s = students[idx]
    gpa = gpas[idx]
    print(f"{s.id:<10} | {s.name:<20} | {s.dob:<12} | {gpa:<6.2f}")


def list_courses(courses):
  if not courses:
    print("No courses available.")
    return

  print("\n=== Courses List ===")
  print(f"{'ID':<10} | {'Name':<25} | {'Credits':<10}")
  print("-" * 50)
  for c in courses:
    print(f"{c.id:<10} | {c.name:<25} | {c.credits:<10}")


def show_marks(students, marks):
  if not marks:
    print("No marks recorded yet.")
    return

  course_id = input("\nEnter Course ID to view marks: ").strip()
  print(f"\n=== Marks for Course {course_id} ===")
  print(f"{'Student ID':<12} | {'Name':<20} | {'Mark':<10}")
  print("-" * 48)

  found = False
  for student in students:
    key = (course_id, student.id)
    if key in marks:
      print(
          f"{student.id:<12} | {student.name:<20} | {marks[key]:<10.1f}"
      )
      found = True

  if not found:
    print("No marks found for this course.")


def main():
  students = []
  courses = []
  marks = {}

  while True:
    print("\n STUDENT MANAGEMENT SYSTEM ")
    print("1. Input Students")
    print("2. Input Courses")
    print("3. Input Marks for Course")
    print("4. List Students (Sorted by GPA)")
    print("5. List Courses")
    print("6. Show Course Marks")
    print("0. Exit")

    choice = input("Enter choice (0-6): ").strip()

    if choice == "1":
      input_students(students)
    elif choice == "2":
      input_courses(courses)
    elif choice == "3":
      input_marks(students, courses, marks)
    elif choice == "4":
      list_students_sorted_by_gpa(students, courses, marks)
    elif choice == "5":
      list_courses(courses)
    elif choice == "6":
      show_marks(students, marks)
    elif choice == "0":
      print("Exiting application. Goodbye!")
      break
    else:
      print("Invalid choice! Please select an option from 0 to 6.")


if __name__ == "__main__":
  main()