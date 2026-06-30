class Assignment:
    """
    Represents an assignment.
    """

    def __init__(self, title, course, due_date, description):
        self.title = title
        self.course = course
        self.due_date = due_date
        self.description = description

    def display_assignment(self):
        print("-" * 40)
        print(f"Title       : {self.title}")
        print(f"Course      : {self.course}")
        print(f"Due Date    : {self.due_date}")
        print(f"Description : {self.description}")
        print("-" * 40)

    def update_assignment(self, course, due_date, description):
        self.course = course
        self.due_date = due_date
        self.description = description

    def to_dict(self):
        return {
            "title": self.title,
            "course": self.course,
            "due_date": self.due_date,
            "description": self.description
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["title"],
            data["course"],
            data["due_date"],
            data["description"]
        )