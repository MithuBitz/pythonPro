# Pet Food Recommendation

species = "Cat"

# Need to wrap inside a int() bcoz input return in string
age = int(input("Please enter the age: "))

if species == "Dog" and age < 2:
    food = "Puppy food"
elif species == "Cat" and age > 5:
    food = "Senior cat food"
else :
    food = "food not specify"

print(age, "year ", species, " food is ", food)