from domains.mark import MarkManager
import input as in_mod
import output as out_mod


def main():
  students = []
  courses = []
  mark_manager = MarkManager()

  while True:
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Input Students")
    print("2. Input Courses")
    print("3. Input Marks for Course")
    print("4. List Students (Sorted by GPA)")
    print("5. List Courses")
    print("6. Show Course Marks")
    print("0. Exit")

    choice = input("Enter choice (0-6): ").strip()

    if choice == "1":
      in_mod.input_students(students)
    elif choice == "2":
      in_mod.input_courses(courses)
    elif choice == "3":
      in_mod.input_marks(students, courses, mark_manager)
    elif choice == "4":
      out_mod.list_students_sorted_by_gpa(students, courses, mark_manager)
    elif choice == "5":
      out_mod.list_courses(courses)
    elif choice == "6":
      out_mod.show_marks(students, mark_manager)
    elif choice == "0":
      print("Goodbye")
      break
    else:
      print("Invalid choice Please select an option from 0 to 6.")


if __name__ == "__main__":
  main()