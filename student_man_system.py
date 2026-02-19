import json

FILE_NAME = "students.json"


# -------------------------
# Student Class (OOP)
# -------------------------
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "course": self.course
        }


# -------------------------
# File Handling
# -------------------------
def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# -------------------------
# Features
# -------------------------
def add_student(students):
    name = input("Enter student name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")

    student = Student(name, age, course)
    students.append(student.to_dict())

    save_students(students)
    print("Student added successfully.")


def view_students(students):
    if not students:
        print("No students found.")
        return

    print("\nStudent List:")
    for i, student in enumerate(students, start=1):
        print(f"{i}. {student['name']} | Age: {student['age']} | Course: {student['course']}")


def search_student(students):
    name = input("Enter student name to search: ")

    found = False
    for student in students:
        if student["name"].lower() == name.lower():
            print("Found:", student)
            found = True

    if not found:
        print("Student not found.")


def delete_student(students):
    view_students(students)

    try:
        index = int(input("Enter student number to delete: "))
        if 1 <= index <= len(students):
            removed = students.pop(index - 1)
            save_students(students)
            print("Removed:", removed["name"])
        else:
            print("Invalid number.")
    except:
        print("Invalid input.")


# -------------------------
# Menu System
# -------------------------
def main():
    students = load_students()

    while True:
        print("\n==== STUDENT MANAGEMENT SYSTEM ====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


main()
