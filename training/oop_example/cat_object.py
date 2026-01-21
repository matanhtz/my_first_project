from training.oop_example.animal_parent_object import AnimalParentObject


class CatObject(AnimalParentObject):
    def __init__(self, legs_amount, age):
        self.legs_amount = legs_amount
        self.age = age

    def make_noise(self):
        print("Miao Miao")