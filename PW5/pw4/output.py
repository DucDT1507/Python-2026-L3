import numpy as np


def list_courses(courses):
  if not courses:
    print("No courses available.")
    return

  print("Courses List")
  print(f"{'ID':<10} | {'Name':<25} | {'Credits':<10}")
  print("-" * 50)
  for c in courses:
    print(f"{c.id:<10} | {c.name:<25} | {c.credits:<10}")


def list_students_sorted_by_gpa(students, courses, mark_manager):
  if not students:
    print("No students available.")
    return

  gpas = np.array([
      mark_manager.calculate_gpa(s.id, courses) for s in students
  ])
  sorted_indices = np.argsort(gpas)[::-1]

  print("\n=== Students List (Sorted by GPA Descending) ===")
  print(f"{'ID':<10} | {'Name':<20} | {'DoB':<12} | {'GPA':<6}")
  print("-" * 56)

  for idx in sorted_indices:
    s = students[idx]
    gpa = gpas[idx]
    print(f"{s.id:<10} | {s.name:<20} | {s.dob:<12} | {gpa:<6.2f}")


def show_marks(students, mark_manager):
  if not mark_manager.marks:
    print("No marks recorded yet.")
    return

  course_id = input("\nEnter Course ID to view marks: ").strip()
  print(f"\n=== Marks for Course {course_id} ===")
  print(f"{'Student ID':<12} | {'Name':<20} | {'Mark':<10}")
  print("-" * 48)

  found = False
  for student in students:
    mark = mark_manager.get_mark(course_id, student.id)
    if mark is not None:
      print(f"{student.id:<12} | {student.name:<20} | {mark:<10.1f}")
      found = True

  if not found:
    print("No marks found for this course.")