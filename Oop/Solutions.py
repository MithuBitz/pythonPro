class Car: 
    def __init__(self, brand, model):
        self.brand = brand # brand is access from the parameters of __init__ 
        self.model = model # self.model is the inside value of the attribute in __init__
    
    def carDetails(self):
        return f"{self.brand} {self.model}"
    

# Inheritance - Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        

# Create a my_Car instance
my_Car = Car("Hyundai", "i20")
# Access the attributes
print(my_Car.brand)
print(my_Car.model)
print(my_Car.carDetails())

my_fev_car = Car("Mahindra", "XUV700")
print(my_fev_car.brand)
print(my_fev_car.carDetails())

# Create a Electric Car instance
my_ev_car = ElectricCar("Tata", "Nexon", "AA")

print(my_ev_car.carDetails())
print(my_ev_car.battery_size)