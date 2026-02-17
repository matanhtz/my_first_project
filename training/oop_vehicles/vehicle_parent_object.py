

class VehicleParent:
    def vehicle_price(self,price,tax):
        total_price = price + (price*tax)
        print(total_price)
        return total_price