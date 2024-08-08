# Validate Input

while True:
    number = int(input("Please type any number between 1 and 10: "))
    if 1 <= number <= 10 :
        print("Thanks bro!")
        break
    else: 
        print("Invalid entry! Please enter a number again")

