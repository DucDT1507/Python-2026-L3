from domains.course import Course
from domains.student import Student


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
    print("Invalid input! Please enter a valid number.")


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


def input_marks(students, courses, mark_manager):
  if not courses:
    print("Error: No courses available.")
    return
  if not students:
    print("Error: No students available.")
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
      mark_manager.add_mark(c_id, student.id, score)
    except ValueError:
      print("Invalid score. Skipping student.")