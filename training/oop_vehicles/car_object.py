from training.oop_vehicles.vehicle_parent_object import VehicleParent


class CarObject(VehicleParent):
    def __init__(self,brand,is_electric):
        self.brand = brand
        self.isElectric = is_electric

    def battery_available(self,capacity,usage):
        if self.isElectric:
            remaining_capacity = capacity - usage
            return remaining_capacity

        else:
            return -1

    def vehicle_price_average(self,prices):
        total_price = 0
        for price in prices:
            total_price = price + total_price
            print (total_price/len(prices))
