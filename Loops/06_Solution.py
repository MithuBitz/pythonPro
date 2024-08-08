# Factorial Calculator

# Need to wrap inside a int() bcoz input return in string
# number = int(input("Enter a number greter then 0: "))
number = 5
factorial = 1

print(number)

while number > 0 :
    factorial *= number
    number -= 1


print("Factorial of ", number, "is: ", factorial)
