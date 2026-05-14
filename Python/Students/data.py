import json

students = []
def save_students():
    with open("Python/Data/student.json", "w") as f:
        json.dump(students, f)
def load_students():
    global students
    try:
        with open("Python/Data/student.json", "r") as f:
            students.clear()
            students.extend(json.load(f))
    except FileNotFoundError:
        students = []