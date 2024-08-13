# Class Variables
# Add a class variable to Car that keeps track of the number of cars created

# 7. Static Method
# Add a static method to the Car class that returns a general description of a car.

# 8. Property Decorators
# Use a property decorator in the Car class to make the model attribute read-only 

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
    

my_fev = Car("Tata", "Harrier")
Car("Mahindra", "XUV700")
ElectricCar("Tata", "Nexon", "AAA")

# cannot change the model becoz it is readonly
# my_fev.model = "Safari"
# only access to read the model
print(my_fev.model)

print(Car.total_car)
print(Car.generalDes())