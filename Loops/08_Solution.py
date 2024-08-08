# Prime Number Checker

number = int(input("Please enter a number to check Prime number or not: "))

is_prime = True

if number > 1 :
    for i in range(2, number) :
        if (number % i) == 0 :
            is_prime = False
            break        

print(is_prime)