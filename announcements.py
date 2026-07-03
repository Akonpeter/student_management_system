from datetime import datetime

from models.announcement import Announcement
from utils import load_data, save_data

ANNOUNCEMENT_FILE = "data/announcements.json"



# LOAD ANNOUNCEMENTS

def load_announcements():
    data = load_data(ANNOUNCEMENT_FILE)
    return [Announcement.from_dict(item) for item in data]



# SAVE ANNOUNCEMENT


def save_announcements(announcements):
    data = [announcement.to_dict() for announcement in announcements]
    save_data(ANNOUNCEMENT_FILE, data)




# CREATE ANNOUNCEMENT

def create_announcement():

    announcements = load_announcements()

    print("\n========== CREATE ANNOUNCEMENT ==========")

    title = input("Title: ").strip()

    # Prevent duplicate titles
    for announcement in announcements:
        if announcement.title.lower() == title.lower():
            print("Announcement already exists.")
            return

    message = input("Message: ").strip()

    # Automatically generate today's date
    today = datetime.now().strftime("%Y-%m-%d %H:%M")

    announcement = Announcement(
        title,
        today,
        message
    )

    announcements.append(announcement)

    save_announcements(announcements)

    print("\nAnnouncement created successfully!")







 # VIEW ANNOUNCEMENT


def view_announcements():

    announcements = load_announcements()

    print("\n========== ANNOUNCEMENTS ==========")

    if not announcements:
        print("No announcements available.")
        return

    for announcement in announcements:
        announcement.display_announcement() 





# SEARCH ANNOUNCEMENT


def search_announcement():

    announcements = load_announcements()

    title = input("Enter Title: ").strip()

    for announcement in announcements:

        if announcement.title.lower() == title.lower():
            announcement.display_announcement()
            return

    print("Announcement not found.")




# DELETE ANNOUNCEMENT


def delete_announcement():

    announcements = load_announcements()

    title = input("Enter Title: ").strip()

    for announcement in announcements:

        if announcement.title.lower() == title.lower():

            announcements.remove(announcement)

            save_announcements(announcements)

            print("Announcement deleted successfully.")

            return

    print("Announcement not found.")



# ANNOUNCEMENT MENU


def announcement_menu():

    while True:

        print("\n")
        print("=" * 45)
        print("      ANNOUNCEMENT MANAGEMENT")
        print("=" * 45)
        print("1. Create Announcement")
        print("2. View Announcements")
        print("3. Search Announcement")
        print("4. Delete Announcement")
        print("5. Back")
        print("=" * 45)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_announcement()

        elif choice == "2":
            view_announcements()

        elif choice == "3":
            search_announcement()

        elif choice == "4":
            delete_announcement()

        elif choice == "5":
            break

        else:
            print("Invalid choice.")




