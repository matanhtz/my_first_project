from training.student_tests.person_object import PersonObject


class StudentObject(PersonObject):
    def __init__(self, history_grade, geography_grade, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.history_grade = history_grade
        self.geography_grade = geography_grade

    def analyze_grade(self):
        if self.history_grade > 60 and self.geography_grade > 60:
            print(f"{self.first_name} {self.last_name} passed all exams")

        else:
            print(f"{self.first_name} {self.last_name} did not pass all exams")
