

class AnimalParentObject():
    def calculate_distance(self,time,speed):
            distance = time * speed
            if distance < 10:
                print("lazy animal")

            else:
                print("animal ok")

            return distance