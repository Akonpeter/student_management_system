from models.assignment import Assignment
from utils import load_data, save_data


ASSIGNMENT_FILE = "data/assignments.json"


# LOAD ASSIGNMENT


def load_assignments():
    data = load_data(ASSIGNMENT_FILE)
    return



# SAVE ASSIGNMENT



def save_assignments(assignments):
    data = [assignment.to_dict() for assignment in assignments]
    save_data(ASSIGNMENT_FILE, data)


# CREATE ASSIGNMENT



def create_assignment():

    assignments = load_assignments()

    print("\n===== Create Assignment ===== ")

    title = input("Assignment Title: ").strip()

    for assignment in assignments:
        if assignment.title.lower() == title.lower():
            print("Assignment already exists.")
            return
        
    course = input("Course Name: ").strip()
    due_date = input("Due Date (YYYY-MM-DD): ").strip()
    description = input("Description: ").strip()

    assignment = Assignment(
        title,
        course,
        due_date=
        description
    ) 

    assignment.append(assignment)

    save_assignments(assignments)

    print("\nAssignment created successfully!")



    # VIEW ASSIGNMENT

def view_assignments():

    assignments = load_assignments()

    print("\n===== Assignment List =====")

    if not assignments:
        print("No assignments found. ")
        return
    
    for assignment in assignments:
        assignment.display_assignment()



# SEARCH ASSIGNMENT

def search_assignment():

    assignments = load_assignments()

    title = input("\nEnter Assignment Title: ").strip()

    for assignment in assignments:
        if assignment.title.lower() == title.lower():
            assignment.display_assignment()
            return

        print("Assignment not found.")



#   UPDATE ASSIGNMENT


def update_assignment():

    assignments = load_assignments()

    title = input("\nEnter Assignment Title: ").strip()

    for assignment in assignments:

        if assignment.title.lower() == title.lower():

            print("\nEnter New Details")


            course = input("Course Name: ")
            due_date = input("Due Date: ")
            description = input("Description: ")


            assignment.update_assignment(
                course,
                due_date,
                description

            ) 

            save_assignments(assignments)

            print("Assignment updated successfully.")
            return
        
    print("Assignment not found.")



# DELETE ASSIGNMENT


def delete_assignment():

    assignments = load_assignments()

    title = input("\nEnter Assignment Title: ").strip()

    for assignment in assignments:

        if assignment.title.lower() == title.lower():

            assignments.remove(assignment)

            save_assignments(assignments)

            print("Assignment deleted successfully.")
            return
        print("Assignment has been deleted.")




#   ASSIGNMENT MENU 


def assignment_menu():

    while True:

        print("\n")
        print("=" * 40)
        print("ASSIGNMENT MANAGEMENT")
        print("=" * 40)



        print("1. Create Assignment")
        print("2. View Assignments")
        print("3. Search Assignment")
        print("4. Update Assignment")
        print("5. Delete Assignment")
        print("6. Back")


        choice = input("Enter choice: ")

        if choice == "1":
            create_assignment()

        elif choice == "2":
            view_assignments()

        elif choice == "3":
            search_assignment()

        elif choice == "4":
            update_assignment()

        elif choice == "5":
            delete_assignment()

        elif choice == "6":
            break

        else:
            print("Invalid choice.")




