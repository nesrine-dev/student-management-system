students = []

def add_student():
    name = input("Enter student name: ")
    students.append(name)
    print("Student added successfully!")

def delete_student():
    name = input("Enter student name to delete: ")
    if name in students:
        students.remove(name)
        print("Student deleted.")
    else:
        print("Student not found.")

def search_student():
    name = input("Enter student name to search: ")
    if name in students:
        print("Student found.")
    else:
        print("Student not found.")

def display_students():
    print("Student List:")
    for student in students:
        print(student)

while True:
    print("\n1.Add Student")
    print("2.Delete Student")
    print("3.Search Student")
    print("4.Display Students")
    print("5.Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        delete_student()
    elif choice == "3":
        search_student()
    elif choice == "4":
        display_students()
    elif choice == "5":
        break
