from Students.data import load_students, students


def view_students():
    load_students()
    try:
        if len(students) == 0:
            print("No Students Found")
            return
        for student in students:
            print(student)
    except Exception as e:
        print("Error: ", str(e))    