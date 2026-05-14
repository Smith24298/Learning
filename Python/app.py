

from Students import *


while(True):
    choice = int (input("""
    1. Add Student
    2. View Student
    3. Search Student
    4.Delete Student
    5.Exit                    
    """))
    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        break
    else:
        print("Invalid Choice")


