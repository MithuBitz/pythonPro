# Encapsulation
# Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.
class Car: 
    def __init__(self, brand, model):
        self.__brand = brand    # __brand makes brand private
        self.model = model
    
    def get_brand(self):
        return self.__brand + "!"
    
    def fullname(self):
        return f"{self.__brand} {self.model}"
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    

my_car = Car("Hyndai", "i20")
print(my_car.get_brand())
print(my_car.fullname())

my_ev_car = ElectricCar("Tata", "Nexon", "AA")

print(my_ev_car.fullname())
print(my_ev_car.battery_size)