from models.student import Student
from utils import load_data, save_data
STUDENT_FILE = "data/students.json"


class Student:
    """
    Represents a student in the Student Management System.
    """

    def __init__(self, student_id, full_name, email, phone, programme, registration_date):
        self.student_id = student_id
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.programme = programme
        self.registration_date = registration_date

    def display_info(self):
        """Display student details."""
        print("-" * 40)
        print(f"Student ID        : {self.student_id}")
        print(f"Full Name         : {self.full_name}")
        print(f"Email             : {self.email}")
        print(f"Phone             : {self.phone}")
        print(f"Programme         : {self.programme}")
        print(f"Registration Date : {self.registration_date}")
        print("-" * 40)

    def update_info(self, full_name, email, phone, programme):
        """Update student information."""
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.programme = programme

    def to_dict(self):
        """Convert the object to a dictionary."""
        return {
            "student_id": self.student_id,
            "full_name": self.full_name,
            "email": self.email,
            "phone": self.phone,
            "programme": self.programme,
            "registration_date": self.registration_date
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Student object from a dictionary."""
        return cls(
            data["student_id"],
            data["full_name"],
            data["email"],
            data["phone"],
            data["programme"],
            data["registration_date"]

        )
    # Load student data

    def load_students():
        data = load_data(STUDENT_FILE)
        return [Student.from_dict(student) for student in data]

   #  Save student data

    def save_students(students):
       data = [student.to_dict() for student in students]
    save_data(STUDENT_FILE, data)




    # Add student data
def add_student():
    students = load_students()


    print("\n=== Add Student ===")

    student_id = input("Student ID: ").strip()

    for student in students:
        if student.student_id == student_id:
            print("Student ID already exists.")
            return

    full_name = input("Full Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    programme = input("Programme: ")
    registration_date = input("Registration Date (YYYY-MM-DD): ")


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


    print("\nStudent added successfully")




    # View Students 

    def view_students():
        students = load_students()

        if not students:
            print("\nNo students found.")
            return
        
        print("\n=== Student List ===")

        for student in students:
            student.display_info()



         # Search for Student

    def search_students():
        students = load_students()

        student_id = input("\nEnter Student ID: ").strip()

        for student in students:
            if student.student_id == student_id:
                student.display_info()
                return

            print("Student not found.")



            # Update Student

    def update_student():
        students = load_students()

        students_id = input("\nEnter Student ID:").strip()

        for student in students:
            if student.student_id == student_id:
                print("\nEnter New Details")

                full_name = input("Full Name: ")
                email = input("Email: ")
                phone = input("Phone: ")
                programme = ("Programme: ")

                student.update_info(
                    full_name,
                    email,
                    phone,
                    programme
                )   

                save_students(students)

                print("Student updated successfully.")
                return

            print("Student not found.") 






 #        Delete Student  
  
             
    def delete_student():
        students = load_students()

        student_id = input("\nEnter Student ID: ").strip()

        for student in students:
            if student.student_id == student_id:
                students.remove(student)
                save_student(students)

                print("Student deleted successfully. ")
                return
            
            print("Student not found.")





    #      STUDENT MENU
          

    def student_menu():
        while True:
            print("\n========== Student Management ==========")
            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Back")

            choice = input("Choose an option: ").strip()

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
                break

            else:
                print("Invalid choice.")
                            


            



