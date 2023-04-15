students = []

def add_student(name):
    students.append(name)
    print(f"{name} added to the list.")

def remove_student(name):
    if name in students:
        students.remove(name)
        print(f"{name} removed from the list.")
    else:
        print(f"{name} is not in the list.")

def print_students():
    for student in students:
        print(student)

def get_student_number(name):
    if name in students:
        number = students.index(name) + 1
        print(f"{name} is student number {number}.")
    else:
        print(f"{name} is not in the list.")

def remove_students(names):
    for name in names:
        remove_student(name)

add_student("Ali Aydın")
add_student("Fatma Yılmaz")
add_student("Mehmet Öztürk")

print_students()

get_student_number("Fatma Yılmaz")

remove_students(["Ali Aydın", "Mehmet Öztürk"])

print_students()