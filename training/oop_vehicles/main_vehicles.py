from training.oop_vehicles.car_object import CarObject
from training.oop_vehicles.truck_object import TruckObject

car1 = CarObject("Mazda",True)
car2 = CarObject("Toyota",False)
truck1 = TruckObject("Mazda",8)
truck2 = TruckObject("Toyota",12)
car1.vehicle_price(10000,0.2)
price_list = [120,200,160]
car2.vehicle_price_average(price_list)