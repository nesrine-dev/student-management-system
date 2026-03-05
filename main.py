students = []

def add_student():
    name = input("Enter student name: ")
    students.append(name)
    print("Student added successfully!")

def delete_student():
    name = input("Enter student name to delete: ")
    if name in students:
        students.remove(name)
        print("Student removed.")
    else:
        print("Student not found.")

def search_student():
    name = input("Enter student name to search: ")
    if name in students:
        print("Student found.")
    else:
        print("Student not found.")

def show_students():
    print("\nStudent List:")
    for student in students:
        print(student)

while True:
    print("\nStudent Management System")
    print("1 Add Student")
    print("2 Delete Student")
    print("3 Search Student")
    print("4 Show Students")
    print("5 Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        delete_student()
    elif choice == "3":
        search_student()
    elif choice == "4":
        show_students()
    elif choice == "5":
        break
    else:
        print("Invalid option")
