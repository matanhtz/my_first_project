

class PersonObject:

    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def analyze_age(self):
        if self.age >= 18:
            print(f"{self.first_name} {self.last_name} is over 18")
            return True
        else:
            print(f"{self.first_name} {self.last_name} is under 18")
            return False

