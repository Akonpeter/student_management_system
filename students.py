"""
students.py

This module handles all student management operations:
- Add Student
- View Students
- Search Student
- Update Student
- Delete Student
"""

from models.student import Student
from utils import load_data, save_data

# Path to the student data file
STUDENT_FILE = "data/students.json"


# ==========================
# LOAD STUDENTS
# ==========================

def load_students():
    """
    Load students from the JSON file.
    Returns a list of Student objects.
    """
    data = load_data(STUDENT_FILE)
    return [Student.from_dict(student) for student in data]


# ==========================
# SAVE STUDENTS
# ==========================

def save_students(students):
    """
    Save the list of Student objects to the JSON file.
    """
    data = [student.to_dict() for student in students]
    save_data(STUDENT_FILE, data)


# ==========================
# ADD STUDENT
# ==========================

def add_student():
    students = load_students()

    print("\n========== ADD STUDENT ==========")

    student_id = input("Student ID: ").strip()

    # Check if ID already exists
    for student in students:
        if student.student_id == student_id:
            print("Student ID already exists.")
            return

    full_name = input("Full Name: ").strip()
    email = input("Email Address: ").strip()
    phone = input("Phone Number: ").strip()
    programme = input("Programme: ").strip()
    registration_date = input("Registration Date (YYYY-MM-DD): ").strip()

    new_student = Student(
        student_id,
        full_name,
        email,
        phone,
        programme,
        registration_date
    )

    students.append(new_student)
    save_students(students)

    print("\nStudent added successfully!")


# ==========================
# VIEW STUDENTS
# ==========================

def view_students():
    students = load_students()

    print("\n========== STUDENT LIST ==========")

    if not students:
        print("No students found.")
        return

    for student in students:
        student.display_info()


# ==========================
# SEARCH STUDENT
# ==========================

def search_student():
    students = load_students()

    print("\n========== SEARCH STUDENT ==========")

    student_id = input("Enter Student ID: ").strip()

    for student in students:
        if student.student_id == student_id:
            print("\nStudent Found:")
            student.display_info()
            return

    print("Student not found.")


# ==========================
# UPDATE STUDENT
# ==========================

def update_student():
    students = load_students()

    print("\n========== UPDATE STUDENT ==========")

    student_id = input("Enter Student ID: ").strip()

    for student in students:
        if student.student_id == student_id:

            print("\nEnter New Details")

            full_name = input("Full Name: ").strip()
            email = input("Email Address: ").strip()
            phone = input("Phone Number: ").strip()
            programme = input("Programme: ").strip()

            student.update_info(
                full_name,
                email,
                phone,
                programme
            )

            save_students(students)

            print("\nStudent updated successfully!")
            return

    print("Student not found.")


# ==========================
# DELETE STUDENT
# ==========================

def delete_student():
    students = load_students()

    print("\n========== DELETE STUDENT ==========")

    student_id = input("Enter Student ID: ").strip()

    for student in students:
        if student.student_id == student_id:

            students.remove(student)
            save_students(students)

            print("\nStudent deleted successfully!")
            return

    print("Student not found.")


# ==========================
# STUDENT MENU
# ==========================

def student_menu():
    while True:

        print("\n")
        print("=" * 40)
        print("     STUDENT MANAGEMENT MENU")
        print("=" * 40)
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Back to Main Menu")
        print("=" * 40)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Returning to Main Menu...")
            break

        else:
            print("Invalid choice. Please try again.")