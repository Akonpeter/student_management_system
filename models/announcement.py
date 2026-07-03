class Announcement:
    """
    Represents an announcement.
    """

    def __init__(self, title, date, message):
        self.title = title
        self.date = date
        self.message = message

    def display_announcement(self):
        print("-" * 50)
        print(f"Title   : {self.title}")
        print(f"Date    : {self.date}")
        print(f"Message : {self.message}")
        print("-" * 50)

    def to_dict(self):
        return {
            "title": self.title,
            "date": self.date,
            "message": self.message
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["title"],
            data["date"],
            data["message"]
        )