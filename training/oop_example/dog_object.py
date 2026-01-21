


class DogObject():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def go_to_sleep(self, time_to_sleep):
        print(f"go to sleep for {time_to_sleep} seconds")

    def make_noise(self):
        print("woof woof")

    def calculate_distance(self,time,speed):
        distance = time * speed
        if distance < 10:
            print("lazy dog")

        else:
            print("dog ok")

        return distance
