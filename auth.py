ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"


def login():
    """
    Authenticate the administrator.
    Allows up to three login attempts.
    """
    print("\n===== Administrator Login =====")

    attempts = 3

    while attempts > 0:
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            print("\nLogin Successful!\n")
            return True

        attempts -= 1
        print(f"\nInvalid credentials. Attempts remaining: {attempts}")

    print("\nToo many failed attempts.")
    return False



def logout():
    """
    Log out the administrator.
    """
    print("\nYou have been logged out successfully.\n")