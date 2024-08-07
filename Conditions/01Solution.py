# Need to wrap inside a int() bcoz input return in string
age = int(input("Please enter your age: "))

# Indentation is important
if age < 13 :
    print("You are a Child")
elif age < 20 :
    print("You are a Teenager")
elif age < 60 :
    print("You are a Adult")
else : 
    print("You are a Senior")