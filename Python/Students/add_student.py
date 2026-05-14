from Students.data import save_students, students
from Students.data import load_students
def add_student():
    load_students()

    flag = int(input("Do you want to add demo student? (1 for Yes, 0 for No): "))

         
    Student_demo = {
        "name": "Smith Faldu",
        "age": 22,
        "roll_no": 1,
        "mobile_no": 1234567890,
        "parents_mobile_no": 1234567890,
        "Address": "123 Main St",
        "City": "Anytown",
        "state": "AnyState"
        }
    if flag == 1:
        students.append(Student_demo)
        save_students()
        print("Demo Student Added Successfully")
        return
    try:
        
        name = input("Enter Student Name: ")
        age = int(input("Enter Student Age: "))
        roll_no = int(input("Enter Student Roll No: "))
        mobile_no = int(input("Enter Student Mobile No: "))
        parents_mobile_no = int(input("Enter Student Parents Mobile No: "))
        Address = input("Enter Student Address: ")
        City = input("Enter Student City: ")
        state = input("Enter Student State: ")
        student = {

            "name": name,
            "age": age, 
            "roll_no": roll_no, 
            "mobile_no": mobile_no, 
            "parents_mobile_no": parents_mobile_no, 
            "Address": Address, 
            "City": City, 
            "state": state
            
            }
        students.append(student)
        save_students()
        print("Student Added Successfully")
    except Exception as e:
        print("Error: ", e)