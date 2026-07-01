from models.grade import Grade
from utils import load_data, save_data
from students import load_students

GRADE_FILE = "data/grades.json"



# LOAD GRADE


def load_grades():
    data = load_data(GRADE_FILE)
    return [Grade.from_dict(item) for item in data]


def save_grades(grades):
    data = [grade.to_dict() for grade in grades]
    save_data(GRADE_FILE, data)


def add_grade():

    grades = load_grades()
    students = load_students()

    print("\n========== Add Grade ==========")

    student_id = input("Student ID: ").strip()

    # Check if student exists

    student_exists = False

    for student in students:
        if student.student_id == student_id:
            student_exists = True
            break

    if not student_exists:
        print("Student ID does not exist.")
        return

    course = input("Course Name: ").strip()

    for grade in grades:
     if grade.student_id == student_id and grade.course.lower() == course.lower():
        print("Grade already exists for this student and course.")
        return

    try:
        score = float(input("Score (0 - 100): "))

        if score < 0 or score > 100:
            print("Score must be between 0 and 100.")
            return

    except ValueError:
        print("Invalid score.")
        return

    grade = Grade(
        student_id,
        course,
        score
    )

    grades.append(grade)

    save_grades(grades)

    print("Grade added successfully!")



#   VIEW GRADES


def view_grades():
    grades = load_grades()

    print("\n===== Student Grades =====")

    if not grades:
        print("No grades found.")
        return
    
    for grade in grades:
        grade.display_grade()



# SEARCH GRADE


def search_grade():

    grades = load_grades()

    student_id = input("Student ID: ").strip()
    course = input("Course Name: ").strip()

    for grade in grades:

        if (
            grade.student_id == student_id
            and grade.course.lower() == course.lower()
        ):
            grade.display_grade()
            return

    print("Grade not found.")



# UPDATE  GRADE

def update_grade():

    grades = load_grades()

    student_id = input("Student ID: ").strip()
    course = input("Course Name: ").strip()

    for grade in grades:

        if grade.student_id == student_id:

            score = float(input("New Score: "))

            grade.update_score(score)

            save_grades(grades)

            print("Grade updated successfully.")

            return

    print("Grade not found.")  




    #  DELETE GRADE


def delete_grade():

    grades = load_grades()

    student_id = input("Student ID: ").strip()
    course = input("Course Name: ").strip()

    for grade in grades:

        if grade.student_id == student_id:
            

            grades.remove(grade)

            save_grades(grades)

            print("Grade deleted.")

            return

    print("Grade not found.")   




    #  AVERAGE SCORE


def calculate_average():

    grades = load_grades()

    if not grades:
        print("No grades available.")
        return

    total = sum(grade.score for grade in grades)

    average = total / len(grades)

    print(f"\nAverage Score : {average:.2f}")




#   GRADE MENU



def grade_menu():

    while True:

        print("\n")
        print("=" * 40)
        print("GRADE MANAGEMENT")
        print("=" * 40)

        print("1. Add Grade")
        print("2. View Grades")
        print("3. Search Grade")
        print("4. Update Grade")
        print("5. Delete Grade")
        print("6. Calculate Average")
        print("7. Back")

        choice = input("Choose: ")

        if choice == "1":
            add_grade()

        elif choice == "2":
            view_grades()

        elif choice == "3":
            search_grade()

        elif choice == "4":
            update_grade()

        elif choice == "5":
            delete_grade()

        elif choice == "6":
            calculate_average()

        elif choice == "7":
            break

        else:
            print("Invalid choice.")



