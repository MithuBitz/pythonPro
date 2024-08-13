# Class Inheritance and isinstance() Function

class Car: 

    # class variable
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand    # __brand makes brand private
        self.__model = model
        Car.total_car += 1
    
    def get_brand(self):
        return self.__brand + "!"
    
    def fullname(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    #Declare a static method which can only access by the Class not instances
    @staticmethod # @staticmethod is actually a decorator which enhence a method of a class
    def generalDes():
        return "Car has four wheels"
    
    @property # property decorator makes the model attribute as a read only(not update on instance)
    def model(self):
        return self.__model
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charger"
    
class Engine():
    def engine_info(self):
        return "Engine information available"

class Battery():
    def battery_info(self):
        return "Battery information available"

class EvCar(Engine, Battery, Car): # Multiple Inheritance
    pass

# my_ev = ElectricCar("Tata", "Nexon", "AAA")

# To check my_ev is a instance of Car and ElectricCar class
# print(isinstance(my_ev, Car)) # if it is true then yes my_ev is a instance of Car class
# print(isinstance(my_ev, ElectricCar))

my_fav = EvCar("Tata","Nexon EV")

print(my_fav.battery_info())
print(my_fav.engine_info())