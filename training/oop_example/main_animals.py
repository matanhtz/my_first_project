from training.oop_example.cat_object import CatObject
from training.oop_example.dog_object import DogObject


class MainAnimals:
    dog1 = DogObject("Rexy",4)
    dog2 = DogObject("Lucky",2)
    cat1 = CatObject(4,1)

    dog1.make_noise()
    dog2.make_noise()
    cat1.make_noise()

    dog1.calculate_distance(10,12)

    dog2.go_to_sleep(5)
