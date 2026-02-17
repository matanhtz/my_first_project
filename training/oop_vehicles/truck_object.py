from training.oop_vehicles.vehicle_parent_object import VehicleParent


class TruckObject(VehicleParent):
    def __init__(self,brand,wheelsNumer):
        self.brand = brand
        self.wheelsNumer = wheelsNumer

    def calculate_distance(self,time,speed):
        distance = time * speed
        return distance