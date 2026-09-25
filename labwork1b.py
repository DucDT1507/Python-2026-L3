students = []
courses = []
marks = {}

def input_students():
    count = int(input("Number of student: "))
    for _ in range (count ):
        s_id = input("Student ID: ")
        s_name=input("Student name: ")
        s_DoB=input("Student DoB: ")
        students.append({"id":s_id,"name":s_name,"DoB":s_DoB})


def input_courses():
    count = int(input("Number of courses: "))
    for _ in range (count):
        c_id = input("Courses ID ")
        c_name=input("Courses name: ")
        courses.append({"id":c_id,"name":c_name})

def input_mark():
    if not courses or not students:
        print("Enter student and courses :")
        return
    c_id = input("Enter courses id: ")

    for student in students:
        score = float(input("Enter the marks: "))

    marks[(c_id,student['id'])] = score

def list_courses():
    print("\n=== Courses ===")
    for c in courses:
        print(f"ID: {c['id']} | Name: {c['name']}")

def list_students():
    print("\n=== Students ===")
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | DoB: {s['DoB']}")

def show_marks():
    course_id = input("\nEnter Course ID to view marks: ")
    print(f"\n=== Marks for Course {course_id} ===")
    
    for student in students:
        key = (course_id, student['id'])
        if key in marks:
            print(f"Name: {student['name']} | Mark: {marks[key]}")    

