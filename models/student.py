class Student:

    def __init__(self, student_id, full_name, email, phone, programme, registration_date):
        self.student_id = student_id
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.programme = programme
        self.registration_date = registration_date

    def display_info(self):
        print("-" * 40)
        print(f"Student ID: {self.student_id}")
        print(f"Full Name: {self.full_name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print(f"Programme: {self.programme}")
        print(f"Registration Date: {self.registration_date}")
        print("-" * 40)

    def update_info(self, full_name, email, phone, programme):
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.programme = programme

    def to_dict(self):
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
        return cls(
            data["student_id"],
            data["full_name"],
            data["email"],
            data["phone"],
            data["programme"],
            data["registration_date"]
        )