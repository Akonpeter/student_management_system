from auth import login, logout
from students import student_menu
from assignments import assignment_menu


def display_main_menu():
    """Display the main menu."""
    print("\n" + "=" * 40)
    print(" STUDENT MANAGEMENT SYSTEM ")
    print("=" * 40)
    print("1. Student Management")
    print("2. Assignment Management")
    print("3. Grade Management")
    print("4. Announcement Management")
    print("5. Reports")
    print("6. Logout")
    print("7. Exit")
    print("=" * 40)


def main():
    """Main application function."""

    if not login():
        print("Application closed.")
        return

    while True:
        display_main_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
         student_menu()

        elif choice == "2":
         assignment_menu()
        elif choice == "3":
            print("\nGrade Management Module (Coming Soon...)")

        elif choice == "4":
            print("\nAnnouncement Module (Coming Soon...)")

        elif choice == "5":
            print("\nReports Module (Coming Soon...)")

        elif choice == "6":
            logout()

            if login():
                continue
            else:
                break

        elif choice == "7":
            print("\nThank you for using the Student Management System.")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()