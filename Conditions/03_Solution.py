# Grade Calculator Question

# Need to wrap inside a int() bcoz input return in string
score = int(input("Please enter student score: "))

# To prevent the negative score
if score < 0 :
    print("You check your score again!")
    exit()

if score < 60 : 
    print("Your Grade is F")

elif score < 70 : 
    print("Your Grade is D")

elif score < 80 :
    print("Your Grade is C")

elif score < 90 :
    print("Your Grade is B")

elif score <= 100 :
    print("Your Grade is A")

else :
    print("Score must be within 0-100")