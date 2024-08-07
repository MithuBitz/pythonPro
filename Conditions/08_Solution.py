# Password Strength Checker

password = input("Please enter password: ")

# print(len(password))
pass_len = len(password)

if pass_len < 6 :
    strength = "Weak"
elif pass_len <= 10 :
    strength = "Medium"
elif pass_len > 10 :
    strength = "Strong"


print(strength + " password")

