# Question6: Transportation Mode Selection 

# Need to wrap inside a int() bcoz input return in string
distance = int(input("Please enter distance: "))

if distance < 3 :
    # print("Walk")
    transport = "Walk"
elif distance <= 15 :
    # print("Bike")
    transport = "Bike"
elif distance > 15 :
    # print("Car")
    transport = "Car"


print(transport)