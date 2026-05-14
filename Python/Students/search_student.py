from Students.data import load_students, students


def search_student():
    load_students()
    try:
        roll_no = int(input("Enter Student Roll No: "))
        for student in students:
            if student["roll_no"] == roll_no:
                print("Student Found: ", student)
                return
        print("Student Not Found")
    except Exception as e:
        print("Error: ", str(e))