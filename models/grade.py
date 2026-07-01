class Grade:
    """
    Represents a student's grade.
    """

    def __init__(self, student_id, course, score):
        self.student_id = student_id
        self.course = course
        self.score = float(score)

    def calculate_grade(self):
        """
        Calculate letter grade based on score.
        """

        if self.score >= 70:
            return "A"

        elif self.score >= 60:
            return "B"

        elif self.score >= 50:
            return "C"

        elif self.score >= 45:
            return "D"

        elif self.score >= 40:
            return "E"

        else:
            return "F"

    def display_grade(self):
        print("-" * 40)
        print(f"Student ID : {self.student_id}")
        print(f"Course     : {self.course}")
        print(f"Score      : {self.score}")
        print(f"Grade      : {self.calculate_grade()}")
        print("-" * 40)

    def update_score(self, score):
        self.score = float(score)

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "course": self.course,
            "score": self.score
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["student_id"],
            data["course"],
            data["score"]
        )