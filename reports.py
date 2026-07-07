from students import load_students
from assignments import load_assignments
from grades import load_grades
from announcements import load_announcements


#   TOTAL STUDENTS


def total_students():

    students = load_students()

    print("\n======== REPORT ========")
    print(f"Total Students : {len(students)}")


#  TOTAL ASSIGNMENTS


def total_assignments():

    assignments = load_assignments()

    print(f"Total Assignments : {len(assignments)}")



 #   TOTAL GRADES


def total_grades():

    grades = load_grades()

    print(f"Total Grades : {len(grades)}")   


#  TOTAL ANNOUNCEMENTS


def total_announcements():

    announcements = load_announcements()

    print(f"Total Announcements : {len(announcements)}")



# AVERAGE SCORE 



def average_score():

    grades = load_grades()

    if not grades:
        print("Average Score : 0")
        return

    total = sum(grade.score for grade in grades)

    average = total / len(grades)

    print(f"Average Score : {average:.2f}")



# TOP PERFORMING STUDENT


def top_student():

    grades = load_grades()

    if not grades:
        print("No grades available.")
        return

    highest = max(grades, key=lambda grade: grade.score)

    print("\n========== TOP STUDENT ==========")
    print(f"Student ID : {highest.student_id}")
    print(f"Course     : {highest.course}")
    print(f"Score      : {highest.score}")
    print(f"Grade      : {highest.calculate_grade()}")



# RECENTLY REGISTERED STUDENTS


def recent_students():

    students = load_students()

    if not students:
        print("No students found.")
        return

    print("\n========== RECENT STUDENTS ==========")

    recent = students[-5:]

    for student in recent:
        student.display_info()


#  COMPLETE DASHBOARD
# This combines everything into one report.


def dashboard():

    students = load_students()
    assignments = load_assignments()
    grades = load_grades()
    announcements = load_announcements()

    print("\n")
    print("=" * 50)
    print("      STUDENT MANAGEMENT DASHBOARD")
    print("=" * 50)

    print(f"Students        : {len(students)}")
    print(f"Assignments     : (assignments)")
    print(f"Grades          : {len(grades)}")
    print(f"Announcements   : {len(announcements)}")

    if grades:

        average = sum(g.score for g in grades) / len(grades)

        print(f"Average Score   : {average:.2f}")

    else:
        print("Average Score   : 0")

    print("=" * 50)



 #   REPORTS MENU


def reports_menu():

    while True:

        print("\n")
        print("=" * 45)
        print("REPORTS MODULE")
        print("=" * 45)

        print("1. Dashboard")
        print("2. Total Students")
        print("3. Total Assignments")
        print("4. Total Grades")
        print("5. Total Announcements")
        print("6. Average Score")
        print("7. Top Student")
        print("8. Recently Registered Students")
        print("9. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            dashboard()

        elif choice == "2":
            total_students()

        elif choice == "3":
            total_assignments()

        elif choice == "4":
            total_grades()

        elif choice == "5":
            total_announcements()

        elif choice == "6":
            average_score()

        elif choice == "7":
            top_student()

        elif choice == "8":
            recent_students()

        elif choice == "9":
            break

        else:
            print("Invalid choice.")   




