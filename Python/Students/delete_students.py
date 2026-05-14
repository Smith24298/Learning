from Students.data import load_students,save_students,students
def delete_student():
    load_students()
    try:
        roll_no = int(input("Enter Student Roll No: "))
        for student in students:
            if student["roll_no"] == roll_no:
                students.remove(student)
                save_students()
                print("Student Deleted Successfully")
                return
        print("Student Not Found")

    except Exception as e:
        print("Error: ", str(e))