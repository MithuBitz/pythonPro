# Need to wrap inside a int() bcoz input return in string
age = int(input("Please enter your age: "))

day = "Wednesday"

#if the age is above 18 then ticket price 12 and below 18 price is 8
price = 12 if age >= 18 else 8

# if the day is Wednesday then 2 discount
if day == "Wednesday" :
    price = price - 2
    # price -= 2


print("Your ticket price is :", price)