from training.oop_example.dog_object import DogObject


class MainAnimals:
    dog1 = DogObject("Rexy",4)
    dog2 = DogObject("Lucky",2)

    dog1.make_noise()
    dog2.make_noise()

    dog1.calculate_distance(10,12)