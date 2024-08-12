# Polymorphism
# Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

class Car: 
    def __init__(self, brand, model):
        self.__brand = brand    # __brand makes brand private
        self.model = model
    
    def get_brand(self):
        return self.__brand + "!"
    
    def fullname(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charger"
    

car1 = Car("Mahindra", "XUV700")
print(car1.fullname())
print(car1.fuel_type())

car2 = ElectricCar("Tata", "NexonEV", "AAA")
print(car2.fullname())
print(car2.fuel_type())
        