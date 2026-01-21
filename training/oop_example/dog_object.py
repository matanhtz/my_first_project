from training.oop_example.animal_parent_object import AnimalParentObject


class DogObject(AnimalParentObject):
    def __init__(self, name, age):
        print(f"info of dog {name}")
        self.name = name
        self.age = age

    def go_to_sleep(self, time_to_sleep):
        print(f"go to sleep for {time_to_sleep} seconds")

    def make_noise(self):
        print("woof woof")
